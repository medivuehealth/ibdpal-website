#!/usr/bin/env python3
"""Generate June 2026 family and lifestyle blog posts."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
DATA = ROOT / "data" / "june-2026-family-blogs.json"
VERCEL = ROOT / "vercel.json"
FALLBACK_IMAGE = BLOGS / "assets" / "low-residue" / "low-residue_1.jpg"

sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402

IMAGE_URLS = {
    "summer-heat": [
        "https://images.unsplash.com/photo-1527689368864-ff3787971085?auto=format&w=1200&q=80",
        "https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&w=1200&q=80",
        "https://images.unsplash.com/photo-1498837167922-ddd27525fc3a?auto=format&w=1200&q=80",
    ],
    "flare-go-bag": [
        "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?auto=format&w=1200&q=80",
        "https://images.unsplash.com/photo-1601925260368-aea7eab9a802?auto=format&w=1200&q=80",
        "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?auto=format&w=1200&q=80",
    ],
    "siblings-ibd": [
        "https://images.unsplash.com/photo-1511895426328-dc8714191300?auto=format&w=1200&q=80",
        "https://images.unsplash.com/photo-1516627145497-ae6968895b74?auto=format&w=1200&q=80",
        "https://images.unsplash.com/photo-1476703993599-0035a21b17a9?auto=format&w=1200&q=80",
    ],
    "ibd-help-center": [
        "https://images.unsplash.com/photo-1576091160550-2173dba999ef?auto=format&w=1200&q=80",
        "https://images.unsplash.com/photo-1423666639047-f5600c02736f?auto=format&w=1200&q=80",
        "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?auto=format&w=1200&q=80",
    ],
    "dining-out": [
        "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?auto=format&w=1200&q=80",
        "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&w=1200&q=80",
        "https://images.unsplash.com/photo-1559339352-11d035aa65de?auto=format&w=1200&q=80",
    ],
    "infusion-day": [
        "https://images.unsplash.com/photo-1579684385127-29ab1f1a3a2f?auto=format&w=1200&q=80",
        "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?auto=format&w=1200&q=80",
        "https://images.unsplash.com/photo-1586773866518-84b05970a393?auto=format&w=1200&q=80",
    ],
}


def download_image(url: str, dest: Path) -> bool:
    import ssl
    import urllib.request

    for ctx in (ssl.create_default_context(), ssl._create_unverified_context()):
        try:
            with urllib.request.urlopen(url, context=ctx, timeout=30) as resp:
                data = resp.read()
            if len(data) > 5000 and data[:2] == b"\xff\xd8":
                dest.write_bytes(data)
                return True
        except Exception:
            continue
    return False


def ensure_images(post: dict) -> None:
    asset = BLOGS / "assets" / post["asset_dir"]
    asset.mkdir(parents=True, exist_ok=True)
    urls = IMAGE_URLS.get(post["asset_dir"], [])
    for i, name in enumerate(post["images"]):
        dest = asset / name
        if dest.exists() and dest.stat().st_size >= 5000:
            continue
        url = urls[i] if i < len(urls) else (urls[0] if urls else None)
        if url and download_image(url, dest):
            continue
        if FALLBACK_IMAGE.exists():
            shutil.copy(FALLBACK_IMAGE, dest)
            print("used fallback image for", dest.name)


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
    posts = json.loads(DATA.read_text(encoding="utf-8"))["posts"]
    slugs = []
    for post in posts:
        ensure_images(post)
        out = BLOGS / f"{post['slug']}.html"
        out.write_text(render_post(post), encoding="utf-8")
        slugs.append(post["slug"])
        print("wrote", out.name)
    patch_vercel(slugs)
    print(f"Generated {len(slugs)} family/lifestyle blog posts")


if __name__ == "__main__":
    main()
