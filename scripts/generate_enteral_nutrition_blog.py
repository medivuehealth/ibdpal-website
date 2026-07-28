#!/usr/bin/env python3
# Prose style: do not use em dash.
"""Generate enteral nutrition search-gap blog post."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
DATA = ROOT / "data" / "enteral-nutrition-post.json"
VERCEL = ROOT / "vercel.json"
SRC_IMG = BLOGS / "assets" / "gut-nutrition" / "ulcerative-colitis-crohns-nutrition_1.jpg"

sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402


def ensure_image(post: dict) -> None:
    asset = BLOGS / "assets" / post["asset_dir"]
    asset.mkdir(parents=True, exist_ok=True)
    dest = asset / post["images"][0]
    if dest.exists() and dest.stat().st_size >= 1000:
        return
    if SRC_IMG.exists():
        shutil.copy(SRC_IMG, dest)
        print("copied image", dest.name)
    else:
        print("WARN: missing source image", SRC_IMG)


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


def main() -> None:
    posts = json.loads(DATA.read_text(encoding="utf-8"))
    slugs = []
    for post in posts:
        ensure_image(post)
        out = BLOGS / f"{post['slug']}.html"
        out.write_text(render_post(post), encoding="utf-8")
        slugs.append(post["slug"])
        print("wrote", out.name)
    patch_vercel(slugs)
    print("Done.", len(slugs), "posts.")


if __name__ == "__main__":
    main()
