#!/usr/bin/env python3
"""Tier 3 SEO: glossary, patient story URLs, and new blog wiring."""
from __future__ import annotations

import html
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GLOSSARY_DATA = ROOT / "data" / "ibd-glossary.json"
STORIES_DATA = ROOT / "data" / "patient-stories.json"
SEO_EXPANSION = ROOT / "data" / "seo-expansion.json"
STORIES_DIR = ROOT / "patient-stories"
SITEMAP = ROOT / "sitemap.xml"
VERCEL = ROOT / "vercel.json"
RESOURCES = ROOT / "resources-data.js"
LLMS = ROOT / "llms.txt"
SITE = "https://www.ibdpal.org"

sys.path.insert(0, str(ROOT / "scripts"))
from eeat_blocks import content_note_en, edu_disclaimer_en, hub_disclaimer_en, page_review_props  # noqa: E402
from generate_tier3_blogs import generate_tier3_blogs  # noqa: E402
from seo_head import breadcrumb_json, render_seo_head, web_page_json  # noqa: E402
from site_nav import PAGE_SCRIPTS, TAB_NAV_HTML, site_header_html  # noqa: E402

HEAD_ASSETS = """    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="/styles.css">
    <link rel="stylesheet" href="/site-layout-icn.css">
    <link rel="stylesheet" href="/site-polish.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/png" href="/IBDPal_Logo.png">
    <link rel="apple-touch-icon" href="/IBDPal_Logo.png">
"""

FOOTER = """
        <footer class="footer">
            <div class="footer-content">
                <div class="footer-links">
                    <a href="/glossary" class="footer-link">IBD Glossary</a>
                    <a href="/patient-stories" class="footer-link">Patient Stories</a>
                    <a href="/blog" class="footer-link">Blog</a>
                    <a href="/resources" class="footer-link">Resources</a>
                    <a href="/privacy" class="footer-link">Privacy</a>
                </div>
                <p><strong>IBDPal</strong> · MediVue nonprofit · Education only, not medical advice.</p>
                <p>&copy; 2026 MediVue. All rights reserved.</p>
            </div>
        </footer>
"""


def shell(title: str, description: str, path: str, body: str, json_ld: dict) -> str:
    seo = render_seo_head(
        title=title,
        description=description,
        path=path,
        json_ld=json_ld,
        hreflang_es=f"{SITE}/es/recursos",
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
{seo}{HEAD_ASSETS}</head>
<body>
    <div class="app-container">
{site_header_html()}
{TAB_NAV_HTML}
        <main class="main-content" id="main-content">
{body}
        </main>
{FOOTER}
    </div>
{PAGE_SCRIPTS}
</body>
</html>
"""


def defined_term_set_json(terms: list[dict], path: str) -> dict:
    return {
        "@type": "DefinedTermSet",
        "@id": f"{SITE}{path}#glossary",
        "name": "IBD glossary",
        "hasDefinedTerm": [
            {
                "@type": "DefinedTerm",
                "name": t["term"],
                "description": t["definition"],
                "url": f"{SITE}{path}#{t['slug']}",
            }
            for t in terms
        ],
    }


def render_glossary(data: dict) -> str:
    path = "/glossary"
    letters: dict[str, list] = {}
    for t in data["terms"]:
        letters.setdefault(t["term"][0].upper(), []).append(t)
    sections = ""
    for letter in sorted(letters.keys()):
        items = ""
        for t in sorted(letters[letter], key=lambda x: x["term"]):
            items += (
                f'<dt id="{html.escape(t["slug"])}"><strong>{html.escape(t["term"])}</strong></dt>'
                f'<dd>{html.escape(t["definition"])}</dd>'
            )
        sections += f'<section class="seo-landing__block"><h2>{letter}</h2><dl class="glossary-list">{items}</dl></section>'
    body = f"""
            <article class="support-section seo-landing">
                <h1>{html.escape(data['h1'])}</h1>
{content_note_en()}{edu_disclaimer_en()}
                <p class="support-intro">{html.escape(data['intro'])}</p>
{sections}
                <p><a href="/faq">IBD FAQ</a> · <a href="/guides">Patient guides</a> · <a href="/blog">Blog</a></p>
                {hub_disclaimer_en()}
            </article>"""
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            breadcrumb_json(path, data["h1"]),
            {**web_page_json(path, data["h1"], data["description"]), **page_review_props()},
            defined_term_set_json(data["terms"], path),
        ],
    }
    return shell(data["title"], data["description"], path, body, ld)


def render_stories_index(data: dict, stories: list[dict]) -> str:
    path = "/patient-stories"
    cards = ""
    for s in stories:
        url = f"/patient-stories/{s['slug']}"
        age = f", {s['age']}" if s.get("age") else ""
        cards += (
            f'<div class="story-card"><h2><a href="{url}">{html.escape(s["name"])}{age} | '
            f'{html.escape(s["condition"])}</a></h2>'
            f'<p>"{html.escape(s["quote"])}"</p>'
            f'<p><a href="{url}" class="seo-landing__cta">Read story →</a></p></div>'
        )
    body = f"""
            <article class="support-section">
                <h1>{html.escape(data['h1'])}</h1>
{content_note_en()}{edu_disclaimer_en()}
                <p class="support-intro">{html.escape(data['intro'])}</p>
{cards}
                <p><em>Want to share your story?</em> Email <a href="mailto:info@ibdpal.org">info@ibdpal.org</a> with "Patient story" in the subject. We never publish without written consent.</p>
                {hub_disclaimer_en()}
            </article>"""
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            breadcrumb_json(path, data["h1"]),
            {**web_page_json(path, data["h1"], data["description"]), **page_review_props()},
            {
                "@type": "ItemList",
                "name": "IBD patient stories",
                "numberOfItems": len(stories),
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": i + 1,
                        "url": f"{SITE}/patient-stories/{s['slug']}",
                        "name": s["headline"],
                    }
                    for i, s in enumerate(stories)
                ],
            },
        ],
    }
    return shell(data["title"], data["description"], path, body, ld)


def render_story(story: dict, index_meta: dict) -> str:
    path = f"/patient-stories/{story['slug']}"
    age = f", {story['age']}" if story.get("age") else ""
    paras = "".join(f"<p>{html.escape(p)}</p>" for p in story.get("paragraphs", []))
    title = f"{story['name']}{age} | {story['condition']} | IBDPal"
    desc = f"Patient story: {story['headline']}. Shared with consent for education only, not medical advice."
    body = f"""
            <article class="support-section story-page">
                <p class="blog-back"><a href="/patient-stories" class="blog-back-link">← All patient stories</a></p>
                <h1>{html.escape(story['headline'])}</h1>
                <p class="support-intro"><strong>{html.escape(story['name'])}{age}</strong> · {html.escape(story['condition'])}</p>
{content_note_en()}
                <blockquote class="story-quote"><p>"{html.escape(story['quote'])}"</p></blockquote>
{paras}
                <p><em>Shared with permission. Not medical advice or outcome data.</em></p>
                {hub_disclaimer_en()}
            </article>"""
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@context": "https://schema.org",
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "IBDPal", "item": SITE + "/"},
                    {"@type": "ListItem", "position": 2, "name": "Patient stories", "item": SITE + "/patient-stories"},
                    {"@type": "ListItem", "position": 3, "name": story["headline"], "item": SITE + path},
                ],
            },
            {
                **web_page_json(path, story["headline"], desc),
                **page_review_props(),
                "@type": "Article",
                "articleSection": "Patient stories",
                "author": {"@type": "Organization", "name": "MediVue"},
            },
        ],
    }
    return shell(title, desc, path, body, ld)


def patch_vercel(blog_slugs: list[str], story_slugs: list[str]) -> None:
    text = VERCEL.read_text(encoding="utf-8")
    inserts = []
    if '"/glossary"' not in text:
        inserts.append('    {\n      "source": "/glossary",\n      "destination": "/glossary.html"\n    }')
    if '"/patient-stories/:slug"' not in text:
        inserts.append(
            '    {\n      "source": "/patient-stories/:slug",\n      "destination": "/patient-stories/:slug.html"\n    }'
        )
    if '"/patient-stories"' in text and 'patient-stories/index.html' not in text:
        text = text.replace(
            '"destination": "/patient-stories.html"',
            '"destination": "/patient-stories/index.html"',
        )
    for slug in blog_slugs:
        src = f"/blog/{slug}"
        if f'"source": "{src}"' in text:
            continue
        inserts.append(
            f'    {{\n      "source": "{src}",\n      "destination": "/blogs/{slug}.html"\n    }}'
        )
    if inserts:
        block = ",\n".join(inserts) + ",\n"
        text = text.replace('"rewrites": [\n', f'"rewrites": [\n{block}')
    VERCEL.write_text(text, encoding="utf-8")


def patch_sitemap(urls: list[tuple[str, float]]) -> None:
    today = date.today().isoformat()
    text = SITEMAP.read_text(encoding="utf-8")
    if "<!-- tier3-seo -->" in text:
        text = re.sub(r"\n  <!-- tier3-seo -->.*?(?=\n  <!-- |\n</urlset>)", "", text, flags=re.DOTALL)
    entries = []
    for loc, priority in urls:
        entries.append(
            f"  <url>\n    <loc>{SITE}{loc}</loc>\n    <lastmod>{today}</lastmod>\n"
            f"    <changefreq>monthly</changefreq>\n    <priority>{priority}</priority>\n  </url>"
        )
    block = "  <!-- tier3-seo -->\n" + "\n".join(entries)
    anchor = "  <!-- es-pages -->"
    if anchor in text:
        text = text.replace(anchor, block + "\n" + anchor)
    else:
        text = text.replace("  <!-- amp-pages -->", block + "\n  <!-- amp-pages -->")
    SITEMAP.write_text(text, encoding="utf-8")


def patch_resources() -> None:
    if not RESOURCES.exists():
        return
    text = RESOURCES.read_text(encoding="utf-8")
    entries = [
        "  { title: 'IBD Glossary', category: 'getting-started', type: 'site', url: '/glossary', tags: ['terms', 'definitions'] },",
    ]
    for entry in entries:
        if "/glossary" in text:
            break
        text = text.replace("window.IBDPAL_RESOURCES = [\n", "window.IBDPAL_RESOURCES = [\n" + entry + "\n", 1)
    RESOURCES.write_text(text, encoding="utf-8")


def patch_hub_blog_slugs(slugs: list[str]) -> None:
    data = json.loads(SEO_EXPANSION.read_text(encoding="utf-8"))
    hub_map = {
        "ibd-pregnancy-planning": ["crohns-disease", "ulcerative-colitis", "teens-and-school"],
        "college-with-ibd": ["teens-and-school"],
        "j-pouch-basics-ibd": ["ulcerative-colitis", "crohns-disease"],
        "when-to-go-er-ibd": ["flare-help", "crohns-disease", "ulcerative-colitis"],
    }
    for slug in slugs:
        for hub_slug in hub_map.get(slug, []):
            for hub in data["hubs"]:
                if hub["slug"] == hub_slug and slug not in hub.get("blog_slugs", []):
                    hub.setdefault("blog_slugs", []).insert(0, slug)
    SEO_EXPANSION.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def patch_llms_glossary() -> None:
    if not LLMS.exists():
        return
    text = LLMS.read_text(encoding="utf-8")
    marker = "## Glossary & stories"
    block = marker + f"\n- {SITE}/glossary\n- {SITE}/patient-stories"
    stories = json.loads(STORIES_DATA.read_text(encoding="utf-8"))["stories"]
    for s in stories:
        block += f"\n- {SITE}/patient-stories/{s['slug']}"
    if marker in text:
        text = re.sub(r"## Glossary & stories.*?(?=\n## |\Z)", block + "\n", text, flags=re.DOTALL)
    else:
        text = text.replace("## Organization", block + "\n\n## Organization")
    LLMS.write_text(text, encoding="utf-8")


def main() -> None:
    glossary = json.loads(GLOSSARY_DATA.read_text(encoding="utf-8"))
    stories_data = json.loads(STORIES_DATA.read_text(encoding="utf-8"))
    stories = stories_data["stories"]

    (ROOT / "glossary.html").write_text(render_glossary(glossary), encoding="utf-8")
    print("wrote glossary.html")

    STORIES_DIR.mkdir(parents=True, exist_ok=True)
    (STORIES_DIR / "index.html").write_text(
        render_stories_index(stories_data["index"], stories), encoding="utf-8"
    )
    print("wrote patient-stories/index.html")
    story_slugs = []
    for story in stories:
        out = STORIES_DIR / f"{story['slug']}.html"
        out.write_text(render_story(story, stories_data["index"]), encoding="utf-8")
        story_slugs.append(story["slug"])
        print("wrote patient-stories/" + story["slug"] + ".html")

    old_index = ROOT / "patient-stories.html"
    if old_index.exists():
        old_index.unlink()
        print("removed legacy patient-stories.html")

    blog_slugs = generate_tier3_blogs()
    patch_hub_blog_slugs(blog_slugs)

    sitemap_urls = [("/glossary", 0.87), ("/patient-stories", 0.85)]
    sitemap_urls += [(f"/patient-stories/{s}", 0.84) for s in story_slugs]
    sitemap_urls += [(f"/blog/{s}", 0.86) for s in blog_slugs]
    patch_sitemap(sitemap_urls)
    patch_vercel(blog_slugs, story_slugs)
    patch_resources()
    patch_llms_glossary()

    print("Run: python scripts/generate_seo_hubs.py && python scripts/generate_amp_pages.py")


if __name__ == "__main__":
    main()
