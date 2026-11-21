#!/usr/bin/env python3
"""Publish /treatment-decisions hub without regenerating every SEO hub page."""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "seo-expansion.json"
VERCEL = ROOT / "vercel.json"
SITEMAP = ROOT / "sitemap.xml"
ALIASES = ROOT / "data" / "search-aliases.json"
BLOGS = ROOT / "blogs"
SITE = "https://www.ibdpal.org"
SLUG = "treatment-decisions"

sys.path.insert(0, str(ROOT / "scripts"))
from amp_utils import discover_blogs  # noqa: E402
from blog_related import patch_blog_html  # noqa: E402
from generate_seo_hubs import render_hub  # noqa: E402


def patch_vercel(path: str) -> None:
    text = VERCEL.read_text(encoding="utf-8")
    if f'"source": "{path}"' in text:
        return
    insert = f'    {{\n      "source": "{path}",\n      "destination": "{path}.html"\n    }},\n'
    text = text.replace('"rewrites": [\n', '"rewrites": [\n' + insert)
    VERCEL.write_text(text, encoding="utf-8")
    print("patched vercel.json")


def patch_sitemap(path: str) -> None:
    text = SITEMAP.read_text(encoding="utf-8")
    if f"{SITE}{path}</loc>" in text:
        return
    today = date.today().isoformat()
    entry = (
        f"  <url>\n    <loc>{SITE}{path}</loc>\n"
        f"    <lastmod>{today}</lastmod>\n"
        f"    <changefreq>monthly</changefreq>\n"
        f"    <priority>0.9</priority>\n  </url>\n"
    )
    text = text.replace("</urlset>", entry + "</urlset>")
    SITEMAP.write_text(text, encoding="utf-8")
    print("patched sitemap.xml")


def update_aliases() -> None:
    data = json.loads(ALIASES.read_text(encoding="utf-8"))
    extras = {
        "treatment decisions": "treatment decisions",
        "treatment monitoring": "treatment decisions",
        "monitoring hub": "treatment decisions",
        "tdm hub": "treatment decisions",
        "ibd treatment hub": "treatment decisions",
        "biologic monitoring hub": "treatment decisions",
    }
    data.update(extras)
    ALIASES.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("updated search-aliases.json")


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    hub = next(h for h in data["hubs"] if h["slug"] == SLUG)
    posts = discover_blogs(BLOGS)
    out = ROOT / f"{SLUG}.html"
    out.write_text(render_hub(hub, posts), encoding="utf-8")
    print("wrote", out.name)

    patch_vercel(f"/{SLUG}")
    patch_sitemap(f"/{SLUG}")
    update_aliases()

    hubs = data["hubs"]
    patched = 0
    for slug in hub.get("blog_slugs", []):
        path = BLOGS / f"{slug}.html"
        if path.exists() and patch_blog_html(path, slug, posts, hubs):
            patched += 1
    print(f"patched related reading on {patched} hub blogs")

    from sync_resources_library import main as sync_resources  # noqa: E402
    from generate_home_engagement_data import main as gen_engagement  # noqa: E402
    from refresh_content_counts import main as refresh_counts  # noqa: E402

    sync_resources()
    gen_engagement()
    refresh_counts()
    print("Done.")


if __name__ == "__main__":
    main()
