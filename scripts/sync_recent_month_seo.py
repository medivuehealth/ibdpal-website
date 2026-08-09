#!/usr/bin/env python3
"""
Wire all posts published since the recent-month cutoff into SEO/search/bot surfaces:
- data/ibd-resource-keywords.json
- data/search-aliases.json
- data/seo-expansion.json hub blog_slugs
Then regenerate resources, hubs, AMP, sitemap, llms.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
BLOGS = ROOT / "blogs"
RECENT = DATA / "recent-month-posts.json"

sys.path.insert(0, str(ROOT / "scripts"))

# Slug token → hub slug(s) for featured related lists
HUB_ROUTES: list[tuple[re.Pattern[str], list[str]]] = [
    (re.compile(r"enteral|prebiotic|formula|parenteral|hospital-feeding|dysbiosis|gut-barrier|nutrition|diet|fodmap|fiber|protein|dairy|gluten|hydration|electrolyte|weight|micronutrient|probiotic|mediterranean|anti-inflammatory", re.I), ["ibd-nutrition"]),
    (re.compile(r"crohn|perianal|ostomy|j-pouch|stricture|fistula", re.I), ["crohns-disease"]),
    (re.compile(r"colitis|uc-|ulcerative", re.I), ["ulcerative-colitis"]),
    (re.compile(r"flare|fever|dehydration|vomiting|obstruction|er-visit|blood-in-stool|diarrhea|constipation|urgency|mucus|red-flag|when-to-call|when-to-go", re.I), ["flare-help"]),
    (re.compile(r"teen|school|college|dating|work|intimacy|bathroom-urgency", re.I), ["teens-and-school"]),
    (re.compile(r"autoimmune|lupus|rheumatoid|hashimoto|sjogren|sclerosis|diabetes|celiac|psoriasis|psc|uveitis|pyoderma|osteoporosis|thrombosis|ankylosing|extraintestinal|overlap|vaccine-autoimmune|stress-autoimmune|fatigue-autoimmune|gut-microbiome-autoimmune|mediterranean-diet-autoimmune|autoimmune-diet", re.I), ["ibd-nutrition", "crohns-disease"]),
]

EXTRA_ALIASES = {
    # flares / ER
    "gi vs er": "when to call",
    "nurse line vs er": "when to call",
    "blood in stool": "bleeding",
    "rectal bleeding": "bleeding",
    "calprotectin": "labs",
    "crp": "labs",
    "ibd labs": "labs",
    "steroid taper": "steroids",
    "prednisone taper": "steroids",
    "entyvio": "biologics",
    "vedolizumab": "biologics",
    "prior auth": "prior authorization",
    "prior authorization": "prior authorization",
    "step therapy": "prior authorization",
    "newly diagnosed": "newly diagnosed",
    "first 30 days": "newly diagnosed",
    "sacroiliitis": "back pain",
    "back pain ibd": "back pain",
    "obstruction": "vomiting",
    "bowel obstruction": "vomiting",
    "dehydration": "dehydration",
    "electrolytes": "electrolytes",
    "fever flare": "fever",
    "flare symptoms": "flare",
    "leaky gut": "dysbiosis",
    "dysbiosis": "dysbiosis",
    "een": "enteral",
    "pen": "enteral",
    "tpn": "parenteral",
    # autoimmune cluster
    "hashimotos": "hashimoto",
    "hashimoto": "hashimoto",
    "sjogrens": "sjogren",
    "type 1 diabetes": "diabetes",
    "ankylosing spondylitis": "back pain",
    "primary sclerosing cholangitis": "psc",
    "erythema nodosum": "pyoderma",
    "pyoderma": "pyoderma",
    "uveitis": "uveitis",
}


def slug_keywords(slug: str, title: str = "", description: str = "") -> list[str]:
    words = re.split(r"[-_/]+", slug.lower())
    readable = slug.replace("-", " ")
    kws = [readable, slug]
    # meaningful tokens length > 2, skip filler
    skip = {"ibd", "and", "or", "the", "vs", "to", "for", "with", "what", "when", "how"}
    for w in words:
        if len(w) > 2 and w not in skip:
            kws.append(w)
    if title:
        kws.append(re.sub(r"\s*\|\s*.*$", "", title).strip())
    # common expansions
    joined = " ".join(words)
    if "enteral" in joined or "een" in words:
        kws += ["enteral", "entereal", "EEN", "formula", "tube feeding"]
    if "flare" in joined:
        kws += ["flare", "IBD flare", "flare symptoms"]
    if "autoimmune" in joined:
        kws += ["autoimmune", "autoimmune overlap", "immune"]
    if "biologic" in joined or "entyvio" in joined:
        kws += ["biologics", "biologic", "infusion"]
    if "dehydrat" in joined:
        kws += ["dehydration", "fluids", "hydration"]
    if "vomit" in joined or "obstruction" in joined:
        kws += ["vomiting", "obstruction", "stricture"]
    if "fever" in joined:
        kws += ["fever", "infection", "chills"]
    if "lab" in joined or "calprotectin" in joined:
        kws += ["calprotectin", "CRP", "labs", "bloodwork"]
    if "steroid" in joined or "taper" in joined:
        kws += ["steroids", "prednisone", "taper"]
    if "vaccine" in joined:
        kws += ["vaccines", "immunization", "immunosuppressants"]
    # unique preserve order
    out: list[str] = []
    for k in kws:
        k = k.strip()
        if k and k not in out:
            out.append(k)
    return out[:24]


def load_titles(slugs: list[str]) -> dict[str, tuple[str, str]]:
    meta: dict[str, tuple[str, str]] = {}
    for path in DATA.glob("*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        posts = data if isinstance(data, list) else data.get("posts") if isinstance(data, dict) else None
        if not isinstance(posts, list):
            continue
        for post in posts:
            if isinstance(post, dict) and post.get("slug") in slugs:
                meta[post["slug"]] = (post.get("title") or "", post.get("description") or "")
    # fallback from HTML
    for slug in slugs:
        if slug in meta:
            continue
        html = BLOGS / f"{slug}.html"
        if not html.is_file():
            continue
        text = html.read_text(encoding="utf-8", errors="ignore")
        tm = re.search(r"<title>([^|<]+)", text)
        dm = re.search(r'name="description" content="([^"]+)"', text)
        meta[slug] = (
            (tm.group(1).strip() if tm else slug),
            (dm.group(1).strip() if dm else ""),
        )
    return meta


def hubs_for_slug(slug: str) -> list[str]:
    found: list[str] = []
    for pat, hubs in HUB_ROUTES:
        if pat.search(slug):
            for h in hubs:
                if h not in found:
                    found.append(h)
    if not found:
        found.append("ibd-nutrition")
    return found


def run(cmd: list[str]) -> None:
    print("+", " ".join(cmd))
    subprocess.run(cmd, cwd=ROOT, check=True)


def main() -> None:
    # refresh recent list
    run([sys.executable, str(ROOT / "scripts" / "list_recent_month_posts.py")])
    recent = json.loads(RECENT.read_text(encoding="utf-8"))
    slugs: list[str] = recent["slugs"]
    print(f"Recent-month posts: {len(slugs)}")

    titles = load_titles(slugs)

    # keywords
    kw_path = DATA / "ibd-resource-keywords.json"
    keywords = json.loads(kw_path.read_text(encoding="utf-8"))
    updated_kw = 0
    for slug in slugs:
        title, desc = titles.get(slug, ("", ""))
        generated = slug_keywords(slug, title, desc)
        existing = keywords.get(slug) or []
        merged: list[str] = []
        for k in generated + list(existing):
            if k not in merged:
                merged.append(k)
        if keywords.get(slug) != merged:
            keywords[slug] = merged
            updated_kw += 1
    kw_path.write_text(json.dumps(keywords, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"keywords updated for {updated_kw} slugs")

    # aliases
    alias_path = DATA / "search-aliases.json"
    aliases = json.loads(alias_path.read_text(encoding="utf-8"))
    added_a = 0
    for k, v in EXTRA_ALIASES.items():
        if k not in aliases:
            aliases[k] = v
            added_a += 1
    alias_path.write_text(json.dumps(aliases, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"aliases +{added_a}")

    # seo hubs: put month posts near front of matching hubs
    seo_path = DATA / "seo-expansion.json"
    seo = json.loads(seo_path.read_text(encoding="utf-8"))
    hub_map = {h["slug"]: h for h in seo.get("hubs", [])}
    for slug in reversed(slugs):  # oldest first insert → newest end up first
        for hub_slug in hubs_for_slug(slug):
            hub = hub_map.get(hub_slug)
            if not hub:
                continue
            blogs = hub.setdefault("blog_slugs", [])
            if slug in blogs:
                blogs.remove(slug)
            blogs.insert(0, slug)
    # Cap each hub list to keep pages sane (keep first 28)
    for hub in seo.get("hubs", []):
        blogs = hub.get("blog_slugs") or []
        if len(blogs) > 28:
            hub["blog_slugs"] = blogs[:28]
    # Expand nutrition + crohn + flare keywords for month topics
    for hub_slug, extra in {
        "ibd-nutrition": [
            "enteral nutrition",
            "EEN",
            "flare diet",
            "autoimmune diet myths",
            "IBD electrolytes",
            "dehydration IBD",
        ],
        "flare-help": [
            "IBD fever",
            "IBD dehydration",
            "bowel obstruction IBD",
            "after ER visit IBD",
            "flare symptoms",
            "GI vs ER",
        ],
        "crohns-disease": [
            "EEN Crohn's",
            "perianal Crohn's",
            "Crohn's biologics",
            "extraintestinal Crohn's",
        ],
    }.items():
        hub = hub_map.get(hub_slug)
        if not hub:
            continue
        seen = []
        for w in extra + hub.get("keywords", []):
            if w not in seen:
                seen.append(w)
        hub["keywords"] = seen
    seo_path.write_text(json.dumps(seo, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("seo-expansion hubs updated")

    # Expand seo_keywords SLUG_TOPIC_WORDS via patching file lightly is hard; regenerate pages instead.
    run([sys.executable, str(ROOT / "scripts" / "sync_resources_library.py")])
    run([sys.executable, str(ROOT / "scripts" / "generate_seo_hubs.py")])
    run([sys.executable, str(ROOT / "scripts" / "generate_amp_pages.py")])
    run([sys.executable, str(ROOT / "scripts" / "sync_sitemap.py")])
    run([sys.executable, str(ROOT / "scripts" / "sync_llms_txt.py")])
    run([sys.executable, str(ROOT / "scripts" / "generate_home_engagement_data.py")])

    # write URL list for IndexNow
    urls = [f"https://www.ibdpal.org/blog/{s}" for s in slugs]
    urls += [
        "https://www.ibdpal.org/ibd-nutrition",
        "https://www.ibdpal.org/crohns-disease",
        "https://www.ibdpal.org/flare-help",
        "https://www.ibdpal.org/ulcerative-colitis",
        "https://www.ibdpal.org/teens-and-school",
        "https://www.ibdpal.org/blog",
        "https://www.ibdpal.org/sitemap.xml",
        "https://www.ibdpal.org/llms.txt",
    ]
    out_urls = DATA / "recent-month-indexnow-urls.json"
    out_urls.write_text(json.dumps(urls, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {out_urls.relative_to(ROOT)} ({len(urls)} urls)")


if __name__ == "__main__":
    main()
