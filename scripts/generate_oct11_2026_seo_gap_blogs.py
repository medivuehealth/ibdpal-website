#!/usr/bin/env python3
"""Generate Oct 11 2026 SEO gap blogs (8 unique long form posts)."""
from __future__ import annotations

import json
import re
import shutil
import ssl
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
DATA = ROOT / "data" / "oct11-2026-seo-gap-posts.json"
SEARCH_GAP = ROOT / "data" / "search-gap-posts.json"
ALIASES = ROOT / "data" / "search-aliases.json"
VERCEL = ROOT / "vercel.json"
FALLBACK = BLOGS / "assets" / "low-residue" / "low-residue_1.jpg"

sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402
from oct11_seo_bodies import build_body  # noqa: E402
from oct11_seo_bodies._meta import DATE_DISPLAY, DATE_ISO, POST_META  # noqa: E402

MIN_WORDS = 1900

IMAGE_URLS = {
    "ulcerative-colitis-diet": "https://images.unsplash.com/photo-1490645935967-10de6ba17061?auto=format&w=1200&q=80",
    "cded-crohns": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&w=1200&q=80",
    "scd-ibd": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&w=1200&q=80",
    "colon-cancer-surveillance": "https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&w=1200&q=80",
    "smoking-ibd": "https://images.unsplash.com/photo-1516534778448-d36fa1d3c9f0?auto=format&w=1200&q=80",
    "disability-fmla-ibd": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&w=1200&q=80",
    "running-jogging-ibd": "https://images.unsplash.com/photo-1476480862126-209bfaa8dfc8?auto=format&w=1200&q=80",
    "spicy-nuts-seeds-ibd": "https://images.unsplash.com/photo-1596797038530-2c107229654b?auto=format&w=1200&q=80",
}


def word_count(html_body: str) -> int:
    text = html_body
    for tag in ("</p>", "</li>", "</h2>", "</h3>"):
        text = text.replace(tag, " ")
    out = []
    in_tag = False
    for ch in text:
        if ch == "<":
            in_tag = True
            continue
        if ch == ">":
            in_tag = False
            continue
        if not in_tag:
            out.append(ch)
    return len("".join(out).split())


def strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", " ", text)


def assert_no_dashes(text: str, label: str) -> None:
    plain = strip_html(text)
    for ch in ("-", "\u2013", "\u2014"):
        if ch in plain:
            idx = plain.index(ch)
            snippet = plain[max(0, idx - 40) : idx + 40]
            raise SystemExit(f"dash in {label}: {snippet!r}")


def assert_no_duplicate_paragraphs(body: str, slug: str) -> None:
    chunks: list[str] = []
    chunks.extend(re.findall(r"<p>(.*?)</p>", body, flags=re.DOTALL | re.IGNORECASE))
    chunks.extend(re.findall(r"<li>(.*?)</li>", body, flags=re.DOTALL | re.IGNORECASE))
    seen: dict[str, str] = {}
    for chunk in chunks:
        plain = " ".join(strip_html(chunk).split())
        if len(plain.split()) < 12:
            continue
        key = plain.lower()
        if key in seen:
            raise SystemExit(
                f"duplicate paragraph in {slug} ({len(plain.split())} words): {plain[:100]!r}..."
            )
        seen[key] = plain


def assert_post_prose(post: dict) -> None:
    for field in ("title", "description", "share", "category", "body"):
        assert_no_dashes(str(post[field]), f"{post['slug']}.{field}")
    for i, alt in enumerate(post.get("alts", [])):
        assert_no_dashes(alt, f"{post['slug']}.alt[{i}]")
    assert_no_duplicate_paragraphs(post["body"], post["slug"])


def build_posts() -> list[dict]:
    posts: list[dict] = []
    for meta in POST_META:
        post = dict(meta)
        post["date_display"] = DATE_DISPLAY
        post["date_iso"] = DATE_ISO
        post["body"] = build_body(post["slug"])
        posts.append(post)
    return posts


def download_image(url: str, dest: Path) -> bool:
    for ctx in (ssl.create_default_context(), ssl._create_unverified_context()):
        try:
            with urllib.request.urlopen(url, context=ctx, timeout=45) as resp:
                data = resp.read()
            if len(data) > 5000:
                dest.write_bytes(data)
                return True
        except Exception:
            continue
    return False


def ensure_image(post: dict) -> None:
    asset = BLOGS / "assets" / post["asset_dir"]
    asset.mkdir(parents=True, exist_ok=True)
    dest = asset / post["images"][0]
    if dest.exists() and dest.stat().st_size >= 1000:
        return
    url = IMAGE_URLS.get(post["asset_dir"])
    if url and download_image(url, dest):
        print("downloaded", dest.name)
        return
    if FALLBACK.exists():
        shutil.copy(FALLBACK, dest)
        print("fallback", dest.name)


def patch_vercel(slugs: list[str]) -> None:
    text = VERCEL.read_text(encoding="utf-8")
    inserts = []
    for slug in slugs:
        if f'"/blog/{slug}"' in text:
            continue
        inserts.append(
            f'    {{\n      "source": "/blog/{slug}",\n'
            f'      "destination": "/blogs/{slug}.html"\n    }}'
        )
    if not inserts:
        return
    text = text.replace('"rewrites": [\n', '"rewrites": [\n' + ",\n".join(inserts) + ",\n")
    VERCEL.write_text(text, encoding="utf-8")
    print("patched vercel.json")


def update_search_gap(posts: list[dict]) -> None:
    data = {"posts": []}
    if SEARCH_GAP.exists():
        data = json.loads(SEARCH_GAP.read_text(encoding="utf-8"))
        if isinstance(data, list):
            data = {"posts": data}
    by_slug = {p["slug"]: p for p in data.get("posts", [])}
    for post in posts:
        by_slug[post["slug"]] = {
            "slug": post["slug"],
            "match_terms": post.get("match_terms", []),
            "title": post["title"],
            "description": post["description"],
            "category": post["category"],
            "date_display": post["date_display"],
            "date_iso": post["date_iso"],
            "asset_dir": post["asset_dir"],
            "resource_category": post.get("resource_category", "wellness"),
            "tags": post.get("tags", []),
        }
    data["posts"] = list(by_slug.values())
    SEARCH_GAP.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("updated search-gap-posts.json")


def update_aliases() -> None:
    data = json.loads(ALIASES.read_text(encoding="utf-8"))
    extras = {
        "ulcerative colitis diet": "ulcerative colitis diet",
        "uc diet": "ulcerative colitis diet",
        "colitis diet plan": "ulcerative colitis diet",
        "crohn exclusion diet": "cded",
        "cded diet": "cded",
        "crohns disease exclusion diet": "cded",
        "specific carbohydrate diet": "scd",
        "scd diet ibd": "scd",
        "ibd colon cancer": "colon cancer ibd",
        "colorectal cancer colitis": "colon cancer ibd",
        "surveillance colonoscopy ibd": "colon cancer ibd",
        "smoking crohn": "smoking ibd",
        "smoking ulcerative colitis": "smoking ibd",
        "vaping ibd": "smoking ibd",
        "fmla ibd": "disability work ibd",
        "disability crohn": "disability work ibd",
        "work accommodations ibd": "disability work ibd",
        "running with crohn": "running ibd",
        "jogging colitis": "running ibd",
        "spicy food ibd": "spicy nuts seeds ibd",
        "nuts seeds ibd": "spicy nuts seeds ibd",
        "can i eat nuts with crohn": "spicy nuts seeds ibd",
    }
    data.update(extras)
    ALIASES.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("updated search-aliases.json")


def main() -> None:
    posts = build_posts()
    for post in posts:
        assert_post_prose(post)
    DATA.write_text(json.dumps(posts, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    slugs: list[str] = []
    counts: list[tuple[str, int]] = []
    for post in posts:
        ensure_image(post)
        wc = word_count(post["body"])
        if wc < MIN_WORDS:
            raise SystemExit(f"too short: {post['slug']} ({wc})")
        out = BLOGS / f"{post['slug']}.html"
        out.write_text(render_post(post), encoding="utf-8")
        slugs.append(post["slug"])
        counts.append((post["slug"], wc))
        print(f"wrote {out.name} (~{wc} words)")
    patch_vercel(slugs)
    update_search_gap(posts)
    update_aliases()
    print("assert_no_dashes passed for all posts")
    print("assert_no_duplicate_paragraphs passed for all posts")
    print("Done.", len(slugs), "posts")
    for slug, wc in counts:
        print(f"  {slug}: {wc} words")


if __name__ == "__main__":
    main()
