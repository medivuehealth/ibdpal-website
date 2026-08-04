#!/usr/bin/env python3
# Prose style: do not use em dash.
"""Generate the flare-symptoms search-gap blog post (≥3 min read)."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
DATA = ROOT / "data" / "flare-symptoms-post.json"
SEARCH_GAP = ROOT / "data" / "search-gap-posts.json"
VERCEL = ROOT / "vercel.json"
FALLBACK = BLOGS / "assets" / "flare-48h" / "flare_1.jpg"
ER_FALLBACK = BLOGS / "assets" / "er-ibd" / "er_1.jpg"

sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402


def ensure_image(post: dict) -> None:
    asset = BLOGS / "assets" / post["asset_dir"]
    asset.mkdir(parents=True, exist_ok=True)
    dest = asset / post["images"][0]
    if dest.exists() and dest.stat().st_size >= 1000:
        return
    for src in (FALLBACK, ER_FALLBACK):
        if src.exists() and src != dest:
            shutil.copy(src, dest)
            print("copied image", dest.name, "from", src)
            return
    print("WARN: missing flare image; AMP/OG may lack local asset")


def patch_vercel(slugs: list[str]) -> None:
    text = VERCEL.read_text(encoding="utf-8")
    inserts = []
    for slug in slugs:
        src = f'"/blog/{slug}"'
        if src in text:
            continue
        inserts.append(
            f'    {{\n      "source": "/blog/{slug}",\n'
            f'      "destination": "/blogs/{slug}.html"\n    }}'
        )
    if not inserts:
        return
    block = ",\n".join(inserts) + ",\n"
    text = text.replace('"rewrites": [\n', f'"rewrites": [\n{block}')
    VERCEL.write_text(text, encoding="utf-8")
    print("patched vercel.json (+", len(inserts), "rewrites)")


def sync_search_gap(post: dict) -> None:
    """Keep search-gap-posts.json in sync so home engagement gap cards pick this up."""
    entry = {
        "slug": post["slug"],
        "match_terms": [
            "flare symptoms",
            "ibd flare symptoms",
            "crohn flare symptoms",
            "colitis flare symptoms",
            "symptoms of a flare",
            "flare signs",
        ],
        "title": post["title"],
        "description": post["description"],
        "category": post["category"],
        "date_display": post["date_display"],
        "date_iso": post["date_iso"],
        "asset_dir": post["asset_dir"],
        "resource_category": "wellness",
        "tags": [
            "flare symptoms",
            "flare",
            "IBD flare symptoms",
            "urgency",
            "bleeding",
            "diarrhea",
            "abdominal pain",
            "wellness",
            "crohn's",
            "colitis",
        ],
        "share": post["share"],
        "body": post["body"],
        "images": post["images"],
        "alts": post["alts"],
    }
    data = {"posts": []}
    if SEARCH_GAP.exists():
        data = json.loads(SEARCH_GAP.read_text(encoding="utf-8"))
    posts = data.get("posts") or []
    posts = [p for p in posts if p.get("slug") != post["slug"]]
    posts.insert(0, entry)
    data["posts"] = posts
    SEARCH_GAP.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("synced", SEARCH_GAP.name)


def word_count(html_body: str) -> int:
    text = html_body
    for tag in ("</p>", "</li>", "</h2>", "</h3>"):
        text = text.replace(tag, " ")
    while "<" in text and ">" in text:
        start = text.find("<")
        end = text.find(">", start)
        if end == -1:
            break
        text = text[:start] + " " + text[end + 1 :]
    return len([w for w in text.split() if w.strip()])


def main() -> None:
    posts = json.loads(DATA.read_text(encoding="utf-8"))
    slugs = []
    for post in posts:
        words = word_count(post["body"])
        minutes = max(1, round(words / 200))
        print(f"{post['slug']}: ~{words} words (~{minutes} min read @200wpm)")
        if words < 600:
            raise SystemExit(f"Post too short for 3+ min read: {words} words")
        ensure_image(post)
        out = BLOGS / f"{post['slug']}.html"
        out.write_text(render_post(post), encoding="utf-8")
        slugs.append(post["slug"])
        print("wrote", out.name)
        sync_search_gap(post)
    patch_vercel(slugs)
    print("Done.", len(slugs), "posts.")


if __name__ == "__main__":
    main()
