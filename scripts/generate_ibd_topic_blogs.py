#!/usr/bin/env python3
"""Generate IBD topic blog posts (dairy, gluten, immunosuppressants, etc.)."""
from __future__ import annotations

import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
DATA = ROOT / "data" / "ibd-topic-posts.json"
SITEMAP = ROOT / "sitemap.xml"
VERCEL = ROOT / "vercel.json"
SITE = "https://www.ibdpal.org"

sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402

IMAGE_URLS = {
    "dairy-ibd": "https://images.unsplash.com/photo-1550583724-b2692b85b150?auto=format&w=1200&q=80",
    "gluten-ibd": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&w=1200&q=80",
    "immunosuppressants-ibd": "https://images.unsplash.com/photo-1587854692152-cf1804701a67?auto=format&w=1200&q=80",
    "steroids-ibd": "https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&w=1200&q=80",
    "fiber-ibd": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&w=1200&q=80",
    "alcohol-ibd": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7b88?auto=format&w=1200&q=80",
    "mesalamine-ibd": "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?auto=format&w=1200&q=80",
}


def download_image(url: str, dest: Path) -> bool:
    import ssl
    import urllib.request

    for ctx in (
        ssl.create_default_context(),
        ssl._create_unverified_context(),
    ):
        try:
            with urllib.request.urlopen(url, context=ctx, timeout=30) as resp:
                data = resp.read()
            if len(data) > 5000 and data[:2] == b"\xff\xd8":
                dest.write_bytes(data)
                return True
        except Exception:
            continue
    return False


def prepare_post(raw: dict) -> dict:
    post = dict(raw)
    asset = post["asset_dir"]
    img_name = f"{asset}_1.jpg"
    post.setdefault("images", [img_name])
    post.setdefault("alts", [post["title"]])
    return post


FALLBACK_IMAGE = BLOGS / "assets" / "low-residue" / "low-residue_1.jpg"


def ensure_image(post: dict) -> None:
    asset = BLOGS / "assets" / post["asset_dir"]
    asset.mkdir(parents=True, exist_ok=True)
    dest = asset / post["images"][0]
    if dest.exists() and dest.stat().st_size >= 5000:
        return
    url = IMAGE_URLS.get(post["asset_dir"])
    if url and download_image(url, dest):
        return
    if FALLBACK_IMAGE.exists():
        shutil.copy(FALLBACK_IMAGE, dest)
        print("used fallback image for", dest.name)
    else:
        print("WARN: no image for", dest)


def write_blogs(posts: list[dict]) -> list[str]:
    slugs = []
    for raw in posts:
        post = prepare_post(raw)
        ensure_image(post)
        out = BLOGS / f"{post['slug']}.html"
        out.write_text(render_post(post), encoding="utf-8")
        slugs.append(post["slug"])
        print("wrote", out.name)
    return slugs


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


def patch_sitemap(slugs: list[str]) -> None:
    today = date.today().isoformat()
    text = SITEMAP.read_text(encoding="utf-8")
    if "<!-- ibd-topic-blogs -->" in text:
        text = re.sub(
            r"\n  <!-- ibd-topic-blogs -->.*?(?=\n  <!-- |\n</urlset>)",
            "",
            text,
            flags=re.DOTALL,
        )
    entries = []
    for slug in slugs:
        entries.append(
            f"  <url>\n    <loc>{SITE}/blog/{slug}</loc>\n    <lastmod>{today}</lastmod>\n"
            f"    <changefreq>monthly</changefreq>\n    <priority>0.85</priority>\n  </url>"
        )
    block = "  <!-- ibd-topic-blogs -->\n" + "\n".join(entries)
    anchor = "  <!-- nutrition-baselines-blog -->"
    if anchor in text:
        text = text.replace(anchor, block + "\n" + anchor)
    else:
        text = text.replace("  <!-- tier3-seo -->", block + "\n  <!-- tier3-seo -->")
    SITEMAP.write_text(text, encoding="utf-8")
    print("patched sitemap.xml (+", len(slugs), "urls)")


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    slugs = write_blogs(data["posts"])
    patch_vercel(slugs)
    patch_sitemap(slugs)
    print("Next:")
    print("  python scripts/sync_resources_library.py")
    print("  python scripts/generate_seo_hubs.py")
    print("  python scripts/generate_amp_pages.py")
    print("  python scripts/sync_llms_txt.py")


if __name__ == "__main__":
    main()
