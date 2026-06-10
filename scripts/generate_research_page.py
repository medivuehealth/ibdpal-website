#!/usr/bin/env python3
"""Generate /research page and homepage Research tab from data/research-sources.json."""
from __future__ import annotations

import html
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "research-sources.json"
INDEX = ROOT / "index.html"
OUT = ROOT / "research.html"
SITEMAP = ROOT / "sitemap.xml"
VERCEL = ROOT / "vercel.json"
RESOURCES = ROOT / "resources-data.js"
LLMS = ROOT / "llms.txt"
SITE = "https://www.ibdpal.org"

sys.path.insert(0, str(ROOT / "scripts"))
from eeat_blocks import content_note_en, edu_disclaimer_en, hub_disclaimer_en, page_review_props  # noqa: E402
from seo_head import breadcrumb_json, render_seo_head, web_page_json  # noqa: E402
from site_nav import PAGE_SCRIPTS, TAB_NAV_HTML, site_header_html  # noqa: E402

HEAD_ASSETS = """    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="/styles.css">
    <link rel="stylesheet" href="/site-layout-icn.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/png" href="/IBDPal_Logo.png">
    <link rel="apple-touch-icon" href="/IBDPal_Logo.png">
"""

FOOTER = """
        <footer class="footer">
            <div class="footer-content">
                <div class="footer-links">
                    <a href="/ibd-nutrition" class="footer-link">Nutrition Hub</a>
                    <a href="/blog" class="footer-link">Blog</a>
                    <a href="/glossary" class="footer-link">Glossary</a>
                    <a href="/resources" class="footer-link">Resources</a>
                </div>
                <p><strong>IBDPal</strong> · MediVue nonprofit · Education only, not medical advice.</p>
                <p>&copy; 2025 MediVue. All rights reserved.</p>
            </div>
        </footer>
"""


def source_cards(sources: list[dict], *, compact: bool = False) -> str:
    cards = []
    for s in sources:
        topics = ", ".join(html.escape(t) for t in s.get("topics", []))
        pub = html.escape(s.get("publisher", ""))
        year = html.escape(str(s.get("year", "")))
        cards.append(
            f'<article class="research-source-card" id="{html.escape(s["id"])}">'
            f'<h3><a href="{html.escape(s["url"])}" rel="noopener noreferrer">{html.escape(s["title"])}</a></h3>'
            f'<p class="research-source-meta"><strong>{pub}</strong>'
            + (f" · {year}" if year else "")
            + (f' · <span class="research-source-topics">{topics}</span>' if topics else "")
            + "</p>"
            f'<p>{html.escape(s["summary"])}</p>'
            + (
                ""
                if compact
                else f'<p><a href="{html.escape(s["url"])}" class="seo-landing__cta" rel="noopener noreferrer">Read original source →</a></p>'
            )
            + "</article>"
        )
    return "\n".join(cards)


def tab_section(data: dict) -> str:
    return f"""            <!-- research-tab -->
            <div class="tab-content" id="research">
                <div class="research-hub" data-track-impression="research_tab" data-track-label="Research sources tab">
                    <h2 class="resources-hub__title">{html.escape(data['h1'])}</h2>
                    <p class="community-section__lead">{html.escape(data['intro'])}</p>
                    <div class="research-source-grid">
{source_cards(data['sources'], compact=True)}
                    </div>
                    <p class="resources-hub__more"><a href="/research">Open full research library page →</a> · <a href="/ibd-nutrition">Nutrition hub</a> · <a href="/blog/iron-b12-vitamin-d-ibd">Micronutrients article</a></p>
                    <p class="community-edu-disclaimer"><strong>Educational only.</strong> External links open publisher sites. IBDPal does not control third-party content.</p>
                </div>
            </div>
            <!-- /research-tab -->"""


def render_page(data: dict) -> str:
    path = "/research"
    body = f"""
            <article class="support-section seo-landing research-page">
                <h1>{html.escape(data['h1'])}</h1>
{content_note_en()}{edu_disclaimer_en()}
                <p class="support-intro">{html.escape(data['intro'])}</p>
                <div class="research-source-grid">
{source_cards(data['sources'])}
                </div>
                <section class="seo-landing__block">
                    <h2>Related on IBDPal</h2>
                    <ul class="seo-landing__list">
                        <li><a href="/ibd-nutrition">IBD nutrition hub</a></li>
                        <li><a href="/blog/fodmap-diet-crohns-colitis">FODMAP diet article</a></li>
                        <li><a href="/blog/iron-b12-vitamin-d-ibd">Iron, B12, and vitamin D</a></li>
                        <li><a href="/glossary">IBD glossary</a></li>
                    </ul>
                </section>
                {hub_disclaimer_en()}
            </article>"""
    graph = [
        breadcrumb_json(path, data["h1"]),
        {**web_page_json(path, data["h1"], data["description"]), **page_review_props()},
        {
            "@type": "ItemList",
            "name": "IBD nutrition research sources",
            "numberOfItems": len(data["sources"]),
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": i + 1,
                    "name": s["title"],
                    "url": s["url"],
                }
                for i, s in enumerate(data["sources"])
            ],
        },
    ]
    json_ld = {"@context": "https://schema.org", "@graph": graph}
    seo = render_seo_head(
        title=data["title"],
        description=data["description"],
        path=path,
        json_ld=json_ld,
        hreflang_es=f"{SITE}/es/recursos",
    )
    nav = TAB_NAV_HTML.replace(
        f'href="{SITE}/#research" class="tab-button"',
        f'href="{SITE}/#research" class="tab-button active"',
        1,
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
{nav}
        <main class="main-content" id="main-content">
{body}
        </main>
{FOOTER}
    </div>
{PAGE_SCRIPTS}
</body>
</html>
"""


def patch_index(tab_html: str) -> None:
    text = INDEX.read_text(encoding="utf-8")
    if "<!-- research-tab -->" in text:
        text = re.sub(
            r"<!-- research-tab -->.*?<!-- /research-tab -->",
            tab_html.strip(),
            text,
            flags=re.S,
        )
    else:
        text = text.replace(
            "            <!-- Blogs Tab -->",
            tab_html + "\n\n            <!-- Blogs Tab -->",
        )
    INDEX.write_text(text, encoding="utf-8")


def patch_vercel() -> None:
    text = VERCEL.read_text(encoding="utf-8")
    if '"/research"' in text:
        return
    insert = '    {\n      "source": "/research",\n      "destination": "/research.html"\n    },\n'
    text = text.replace('"rewrites": [\n', f'"rewrites": [\n{insert}')
    VERCEL.write_text(text, encoding="utf-8")


def patch_sitemap() -> None:
    today = date.today().isoformat()
    text = SITEMAP.read_text(encoding="utf-8")
    entry = (
        f"  <url>\n    <loc>{SITE}/research</loc>\n    <lastmod>{today}</lastmod>\n"
        f"    <changefreq>monthly</changefreq>\n    <priority>0.87</priority>\n  </url>"
    )
    if "<!-- research-page -->" in text:
        text = re.sub(
            r"  <!-- research-page -->.*?</url>",
            f"  <!-- research-page -->\n{entry}",
            text,
            flags=re.S,
        )
    else:
        text = text.replace(
            "  <!-- tier3-seo -->",
            f"  <!-- research-page -->\n{entry}\n  <!-- tier3-seo -->",
        )
    SITEMAP.write_text(text, encoding="utf-8")


def patch_resources(sources: list[dict]) -> None:
    if not RESOURCES.exists():
        return
    text = RESOURCES.read_text(encoding="utf-8")
    if "'/research'" in text:
        pass
    else:
        text = text.replace(
            "window.IBDPAL_RESOURCES = [\n",
            "window.IBDPAL_RESOURCES = [\n"
            "  { title: 'IBD Research Sources', category: 'nutrition', type: 'site', url: '/research', tags: ['research', 'diet', 'clinical'] },\n",
            1,
        )
    for s in sources:
        entry = (
            f"  {{ title: {json.dumps(s['title'])}, category: 'nutrition', type: 'external', "
            f"url: {json.dumps(s['url'])}, tags: {json.dumps(s.get('topics', []))} }},"
        )
        if s["url"] in text:
            continue
        text = text.replace(
            "window.IBDPAL_RESOURCES = [\n",
            "window.IBDPAL_RESOURCES = [\n" + entry + "\n",
            1,
        )
    RESOURCES.write_text(text, encoding="utf-8")


def patch_llms() -> None:
    if not LLMS.exists():
        return
    text = LLMS.read_text(encoding="utf-8")
    line = f"- {SITE}/research"
    if line in text:
        return
    marker = "## Glossary & stories"
    if marker in text:
        text = text.replace(marker, f"## Research sources\n{line}\n\n{marker}")
    else:
        text = text.rstrip() + f"\n\n## Research sources\n{line}\n"
    LLMS.write_text(text, encoding="utf-8")


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    OUT.write_text(render_page(data), encoding="utf-8")
    print("wrote research.html")
    patch_index(tab_section(data))
    print("patched index.html Research tab")
    patch_vercel()
    patch_sitemap()
    patch_resources(data["sources"])
    patch_llms()
    print("Updated vercel.json, sitemap.xml, resources-data.js, llms.txt")


if __name__ == "__main__":
    main()
