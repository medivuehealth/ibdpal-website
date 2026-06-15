#!/usr/bin/env python3
"""Generate AMP variants for blog posts and SEO guides; wire canonical pairing and routes."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
BLOGS_AMP = BLOGS / "amp"
GUIDES = ROOT / "guides"
GUIDES_AMP = GUIDES / "amp"
DATA = ROOT / "data" / "seo-landing-pages.json"
VERCEL = ROOT / "vercel.json"
SITEMAP = ROOT / "sitemap.xml"

import sys

sys.path.insert(0, str(ROOT / "scripts"))
from amp_utils import amp_url_for, parse_blog_html, render_amp_blog, render_amp_guide  # noqa: E402


def patch_canonical_amphtml(path: Path, canonical_url: str, amp_url: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if 'rel="amphtml"' in text:
        text = re.sub(r'\s*<link rel="amphtml" href="[^"]*">', "", text)
    needle = f'<link rel="canonical" href="{canonical_url}">'
    if needle not in text:
        return False
    replacement = f'{needle}\n    <link rel="amphtml" href="{amp_url}">'
    if replacement in text:
        return False
    path.write_text(text.replace(needle, replacement, 1), encoding="utf-8")
    return True


def patch_vercel_amp() -> None:
    text = VERCEL.read_text(encoding="utf-8")
    blog_rule = '"/blog/:slug/amp"'
    guide_rule = '"/guides/:slug/amp"'
    inserts = []
    if blog_rule not in text:
        inserts.append("""    {
      "source": "/blog/:slug/amp",
      "destination": "/blogs/amp/:slug.html"
    }""")
    if guide_rule not in text:
        inserts.append("""    {
      "source": "/guides/:slug/amp",
      "destination": "/guides/amp/:slug.html"
    }""")
    if not inserts:
        return
    block = ",\n".join(inserts) + ",\n"
    text = text.replace('"rewrites": [\n', f'"rewrites": [\n{block}')
    VERCEL.write_text(text, encoding="utf-8")
    print("Updated vercel.json AMP rewrites")


def patch_sitemap_amp(blog_slugs: list[str], guide_slugs: list[str]) -> None:
    """Delegate to sync_sitemap (single source of truth; avoids duplicate AMP URLs)."""
    from sync_sitemap import main as sync_sitemap_main

    sync_sitemap_main()


def generate_blogs() -> list[str]:
    BLOGS_AMP.mkdir(parents=True, exist_ok=True)
    slugs = []
    for path in sorted(BLOGS.glob("*.html")):
        post = parse_blog_html(path)
        if not post:
            print("WARN: skip", path.name)
            continue
        out = BLOGS_AMP / f"{post['slug']}.html"
        out.write_text(render_amp_blog(post), encoding="utf-8")
        canonical = f"https://www.ibdpal.org/blog/{post['slug']}"
        amp = amp_url_for(f"/blog/{post['slug']}")
        if patch_canonical_amphtml(path, canonical, amp):
            print("linked amphtml", path.name)
        slugs.append(post["slug"])
        print("AMP blog", out.relative_to(ROOT))
    return slugs


def generate_guides() -> list[str]:
    GUIDES_AMP.mkdir(parents=True, exist_ok=True)
    pages = json.loads(DATA.read_text(encoding="utf-8"))["pages"]
    slugs = []
    for page in pages:
        slug = page["slug"]
        out = GUIDES_AMP / f"{slug}.html"
        out.write_text(render_amp_guide(page), encoding="utf-8")
        canonical_path = GUIDES / f"{slug}.html"
        if canonical_path.exists():
            canonical = f"https://www.ibdpal.org/guides/{slug}"
            amp = amp_url_for(f"/guides/{slug}")
            patch_canonical_amphtml(canonical_path, canonical, amp)
        slugs.append(slug)
        print("AMP guide", out.relative_to(ROOT))
    return slugs


def main() -> None:
    blog_slugs = generate_blogs()
    guide_slugs = generate_guides()
    patch_vercel_amp()
    patch_sitemap_amp(blog_slugs, guide_slugs)
    print(f"Done: {len(blog_slugs)} blog AMP pages, {len(guide_slugs)} guide AMP pages")


if __name__ == "__main__":
    main()
