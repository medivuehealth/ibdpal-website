#!/usr/bin/env python3
"""Generate ImproveCareNow CC-attributed resource highlight pages."""
from __future__ import annotations

import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
DATA = ROOT / "data" / "icn-resources.json"
SITEMAP = ROOT / "sitemap.xml"
VERCEL = ROOT / "vercel.json"
SITE = "https://www.ibdpal.org"

sys.path.insert(0, str(ROOT / "scripts"))
from eeat_blocks import icn_attribution_block  # noqa: E402
from generate_blog_posts import render_post  # noqa: E402

FALLBACK_IMAGE = BLOGS / "assets" / "low-residue" / "low-residue_1.jpg"
IMAGE_URLS = {
    "icn-accommodations": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&w=1200&q=80",
    "icn-college": "https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&w=1200&q=80",
    "icn-caregiver": "https://images.unsplash.com/photo-1511895426328-dc8714191300?auto=format&w=1200&q=80",
    "icn-mental-health": "https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?auto=format&w=1200&q=80",
    "icn-transfer": "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&w=1200&q=80",
    "icn-ostomy": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&w=1200&q=80",
    "icn-holidays": "https://images.unsplash.com/photo-1512389142860-9c449e58a543?auto=format&w=1200&q=80",
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


def prepare_post(raw: dict) -> dict:
    post = dict(raw)
    asset = post["asset_dir"]
    img_name = f"{asset}_1.jpg"
    post.setdefault("images", [img_name])
    post.setdefault("alts", [post["title"]])
    attribution = icn_attribution_block(post["icn_source_title"], post["icn_source_url"])
    post["body"] = post["body"] + "\n" + attribution
    return post


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
    if "<!-- icn-blogs -->" in text:
        text = re.sub(
            r"\n  <!-- icn-blogs -->.*?(?=\n  <!-- |\n</urlset>)",
            "",
            text,
            flags=re.DOTALL,
        )
    entries = "\n".join(
        f"  <url><loc>{SITE}/blog/{slug}</loc><lastmod>{today}</lastmod></url>"
        for slug in slugs
    )
    marker = "\n  <!-- icn-blogs -->"
    insert = f"{marker}\n{entries}"
    text = text.replace("</urlset>", f"{insert}\n</urlset>")
    SITEMAP.write_text(text, encoding="utf-8")
    print("patched sitemap (+", len(slugs), "ICN blogs)")


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    slugs = write_blogs(data["posts"])
    patch_vercel(slugs)
    patch_sitemap(slugs)


if __name__ == "__main__":
    main()
