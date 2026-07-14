#!/usr/bin/env python3
# Prose style: do not use em dash.
"""Generate short July 2026 gap blog posts."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
DATA = ROOT / "data" / "july-2026-gap-posts.json"
VERCEL = ROOT / "vercel.json"
FALLBACK = BLOGS / "assets" / "flare-48h" / "flare_1.jpg"

sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402


def ensure_image(post: dict) -> None:
    asset = BLOGS / "assets" / post["asset_dir"]
    asset.mkdir(parents=True, exist_ok=True)
    img = post["images"][0]
    dest = asset / img
    if dest.exists() and dest.stat().st_size >= 1000:
        return
    src_name = post.get("copy_from")
    if src_name:
        src = BLOGS / "assets" / src_name
        if src.exists():
            shutil.copy(src, dest)
            return
    # Prefer first existing jpg in asset dir
    existing = sorted(asset.glob("*.jpg"))
    if existing:
        shutil.copy(existing[0], dest)
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


def main() -> None:
    posts = json.loads(DATA.read_text(encoding="utf-8"))
    # Resolve images that already exist under asset_dir if copy targets wrong name
    for post in posts:
        asset = BLOGS / "assets" / post["asset_dir"]
        wanted = post["images"][0]
        if not (asset / wanted).exists():
            jpgs = sorted(asset.glob("*.jpg"))
            if jpgs:
                post["images"] = [jpgs[0].name]
                post["copy_from"] = f"{post['asset_dir']}/{jpgs[0].name}"
        ensure_image(post)
        out = BLOGS / f"{post['slug']}.html"
        out.write_text(render_post(post), encoding="utf-8")
        print("wrote", out.name)
    patch_vercel([p["slug"] for p in posts])
    print("Done.", len(posts), "posts.")


if __name__ == "__main__":
    main()
