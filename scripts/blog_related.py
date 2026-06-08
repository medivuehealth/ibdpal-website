"""Build related-reading blocks for blog posts (2 articles + 1 guide + 1 hub)."""
from __future__ import annotations

import html
import re


def build_related_links(
    slug: str,
    posts: dict[str, dict],
    hubs: list[dict],
) -> list[tuple[str, str]]:
    """Return up to four (url, label) pairs: hub, guide, two blogs."""
    primary = next((h for h in hubs if slug in h.get("blog_slugs", [])), None)
    links: list[tuple[str, str]] = []

    if primary:
        links.append((f"/{primary['slug']}", primary["h1"]))
        for g in primary.get("guides", [])[:1]:
            links.append((g["url"], g["label"]))
        for other in primary.get("blog_slugs", []):
            if other == slug or other not in posts:
                continue
            links.append((f"/blog/{other}", posts[other]["title"]))
            if len([u for u, _ in links if u.startswith("/blog/")]) >= 2:
                break
    else:
        links.append(("/blog", "All blog posts"))
        links.append(("/guides", "Patient guides by topic"))
        for fallback in ("flare-first-48-hours", "best-foods-crohns-flare", "tracking-food-symptoms-ibdpal"):
            if fallback == slug or fallback not in posts:
                continue
            links.append((f"/blog/{fallback}", posts[fallback]["title"]))
            if len([u for u, _ in links if u.startswith("/blog/") and u != "/blog"]) >= 2:
                break

    seen: set[str] = set()
    unique: list[tuple[str, str]] = []
    for url, label in links:
        if url in seen:
            continue
        seen.add(url)
        unique.append((url, label))
    return unique[:4]


def related_reading_html(slug: str, posts: dict[str, dict], hubs: list[dict]) -> str:
    links = build_related_links(slug, posts, hubs)
    if not links:
        return ""
    items = "".join(
        f'<li><a href="{html.escape(url)}">{html.escape(label)}</a></li>' for url, label in links
    )
    return (
        f'\n                    <section class="seo-related-reading" aria-labelledby="related-{slug}">\n'
        f'                        <h2 id="related-{slug}">Related reading</h2>\n'
        f'                        <ul class="seo-landing__list">{items}</ul>\n'
        f"                    </section>\n"
    )


def patch_all_blogs(posts: dict[str, dict], hubs: list[dict], blogs_dir) -> int:
    count = 0
    for slug in posts:
        if patch_blog_html(blogs_dir / f"{slug}.html", slug, posts, hubs):
            count += 1
    return count


def patch_blog_html(path, slug: str, posts: dict, hubs: list[dict]) -> bool:
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"\s*<section class=\"seo-related-reading\".*?</section>", "", text, flags=re.S)
    block = related_reading_html(slug, posts, hubs)
    if not block:
        return False
    needle = '<div class="blog-vote" data-blog-slug='
    if needle not in text:
        return False
    path.write_text(text.replace(needle, block + "                    " + needle, 1), encoding="utf-8")
    return True
