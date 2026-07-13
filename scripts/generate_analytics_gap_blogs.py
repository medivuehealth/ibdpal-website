#!/usr/bin/env python3
# Prose style: do not use em dash.
"""Generate blog posts from Vercel 30-day analytics gap analysis (Jul 2026)."""
from __future__ import annotations

import json
import re
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
DATA = ROOT / "data" / "analytics-gap-posts.json"
VERCEL = ROOT / "vercel.json"
SITE = "https://www.ibdpal.org"
FALLBACK = BLOGS / "assets" / "er-ibd" / "er_1.jpg"

import sys

sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402


def ensure_image(post: dict) -> None:
    asset = BLOGS / "assets" / post["asset_dir"]
    asset.mkdir(parents=True, exist_ok=True)
    img = post["images"][0]
    dest = asset / img
    if dest.exists() and dest.stat().st_size >= 5000:
        return
    src_name = post.get("copy_from")
    if src_name:
        src = BLOGS / "assets" / src_name
        if src.exists():
            shutil.copy(src, dest)
            return
    if FALLBACK.exists():
        shutil.copy(FALLBACK, dest)


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


def write_posts(posts: list[dict]) -> list[str]:
    slugs = []
    for raw in posts:
        post = dict(raw)
        ensure_image(post)
        out = BLOGS / f"{post['slug']}.html"
        out.write_text(render_post(post), encoding="utf-8")
        slugs.append(post["slug"])
        print("wrote", out.name)
    return slugs


def main() -> None:
    posts = json.loads(DATA.read_text(encoding="utf-8"))
    slugs = write_posts(posts)
    patch_vercel(slugs)
    print("Done.", len(slugs), "posts.")
    print("Next: python scripts/generate_amp_pages.py && python scripts/sync_sitemap.py")


if __name__ == "__main__":
    main()
