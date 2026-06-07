#!/usr/bin/env python3
"""Generate SEO landing pages from data/seo-landing-pages.json.

Prose style: do not use em dash. Use periods, commas, colons, or "|" in titles.
"""
from __future__ import annotations

import html
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "seo-landing-pages.json"
GUIDES = ROOT / "guides"
SITEMAP = ROOT / "sitemap.xml"
VERCEL = ROOT / "vercel.json"
LLMS = ROOT / "llms.txt"

sys.path.insert(0, str(ROOT / "scripts"))
from seo_head import breadcrumb_json, render_seo_head, web_page_json  # noqa: E402
from site_nav import PAGE_SCRIPTS, TAB_NAV_HTML, site_header_html  # noqa: E402

FOOTER = """
        <footer class="footer">
            <div class="footer-content">
                <div class="footer-links">
                    <a href="/guides" class="footer-link">Patient Guides</a>
                    <a href="/ibd-crohns-support" class="footer-link">IBD Crohn's Support</a>
                    <a href="/resources" class="footer-link">Resource Library</a>
                    <a href="/newly-diagnosed" class="footer-link">Newly Diagnosed</a>
                    <a href="/visit-prep" class="footer-link">Visit Prep</a>
                    <a href="/privacy" class="footer-link">Privacy Policy</a>
                    <a href="/support" class="footer-link">App Support</a>
                </div>
                <p><strong>IBDPal</strong> · MediVue nonprofit · Education only, not medical advice.</p>
                <p>&copy; 2025 MediVue. All rights reserved.</p>
            </div>
        </footer>
"""

HEAD_ASSETS = """    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="/styles.css">
    <link rel="stylesheet" href="/site-layout-icn.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/png" href="/IBDPal_Logo.png">
    <link rel="apple-touch-icon" href="/IBDPal_Logo.png">
"""

DISCLAIMER = (
    '<p class="community-edu-disclaimer"><strong>Educational only.</strong> '
    "IBDPal does not provide medical advice, diagnosis, or treatment. "
    "Always consult your gastroenterologist or IBD care team for personal decisions.</p>"
)


def faq_json(faq: list[dict], page_id: str) -> dict | None:
    if not faq:
        return None
    return {
        "@type": "FAQPage",
        "@id": f"https://www.ibdpal.org{page_id}#faq",
        "mainEntity": [
            {
                "@type": "Question",
                "name": item["q"],
                "acceptedAnswer": {"@type": "Answer", "text": item["a"]},
            }
            for item in faq
        ],
    }


def guide_breadcrumb(path: str, name: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "IBDPal", "item": "https://www.ibdpal.org/"},
            {"@type": "ListItem", "position": 2, "name": "Patient Guides", "item": "https://www.ibdpal.org/guides"},
            {"@type": "ListItem", "position": 3, "name": name, "item": f"https://www.ibdpal.org{path}"},
        ],
    }


def shell(title: str, description: str, path: str, body: str, json_ld: dict) -> str:
    seo = render_seo_head(title=title, description=description, path=path, json_ld=json_ld)
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


def render_related(related: list[dict]) -> str:
    if not related:
        return ""
    items = "".join(
        f'<li><a href="{html.escape(r["url"])}">{html.escape(r["label"])}</a></li>'
        for r in related
    )
    return f"""
                <section class="seo-landing__block" aria-labelledby="related-heading">
                    <h2 id="related-heading">Related IBDPal resources</h2>
                    <ul class="seo-landing__list">{items}</ul>
                </section>"""


def render_page(page: dict) -> str:
    path = f"/guides/{page['slug']}"
    slug_id = page["slug"].replace("-", "_")
    sections_html = ""
    for sec in page.get("sections", []):
        paras = "".join(f"<p>{html.escape(p)}</p>" for p in sec.get("paragraphs", []))
        sections_html += f"""
                <section class="seo-landing__block">
                    <h2>{html.escape(sec["heading"])}</h2>
                    {paras}
                </section>"""

    tips = page.get("tips") or []
    tips_html = ""
    if tips:
        tips_html = (
            "<section class=\"seo-landing__block\"><h2>Practical tips</h2><ul class=\"seo-landing__list\">"
            + "".join(f"<li>{html.escape(t)}</li>" for t in tips)
            + "</ul></section>"
        )

    faq = page.get("faq") or []
    faq_html = ""
    if faq:
        faq_html = '<section class="seo-landing__block seo-landing__faq" aria-labelledby="faq-heading"><h2 id="faq-heading">Common questions</h2>'
        for item in faq:
            faq_html += f"<h3>{html.escape(item['q'])}</h3><p>{html.escape(item['a'])}</p>"
        faq_html += "</section>"

    keywords_meta = ", ".join(page.get("keywords", []))
    body = f"""
            <article class="support-section seo-landing" data-track-impression="guide_{slug_id}" data-track-label="{html.escape(page['h1'])}">
                <p class="blog-back"><a href="/guides" class="blog-back-link">← All patient guides</a></p>
                <h1>{html.escape(page['h1'])}</h1>
                <p class="support-intro">{html.escape(page['intro'])}</p>
                <p class="seo-guide-keywords"><small>Topics: {html.escape(keywords_meta)}</small></p>
{sections_html}
{tips_html}
{render_related(page.get("related", []))}
{faq_html}
                <section class="seo-landing__block" aria-labelledby="app-cta-heading">
                    <h2 id="app-cta-heading">Free tools on ibdpal.org</h2>
                    <p>Track nutrition and symptoms, explore our <a href="/#community">community map</a>, read the <a href="/#blogs">blog</a>, or download the <a href="/#app">IBDPal iOS app</a>.</p>
                    <p><a href="/#app" class="seo-landing__cta">Explore IBDPal →</a></p>
                </section>
                {DISCLAIMER}
            </article>"""

    graph = [
        guide_breadcrumb(path, page["h1"]),
        {
            **web_page_json(path, page["h1"], page["description"]),
            "keywords": keywords_meta,
            "about": {"@type": "MedicalCondition", "name": "Inflammatory bowel disease"},
        },
    ]
    faq_ld = faq_json(faq, path)
    if faq_ld:
        graph.append(faq_ld)

    json_ld = {"@context": "https://schema.org", "@graph": graph}
    return shell(page["title"], page["description"], path, body, json_ld)


def render_hub(hub: dict, pages: list[dict]) -> str:
    by_cat: dict[str, list] = {}
    for p in pages:
        by_cat.setdefault(p.get("category", "general"), []).append(p)

    cat_order = [
        "getting-started", "nutrition", "flares", "support", "tracking",
        "clinical", "treatment", "wellness", "family",
    ]
    sections = ""
    for cat in cat_order:
        items = by_cat.get(cat, [])
        if not items:
            continue
        label = cat.replace("-", " ").title()
        links = "".join(
            f'<li><a href="/guides/{html.escape(p["slug"])}">{html.escape(p["h1"])}</a>'
            f' <span class="seo-guide-cat-desc">,  {html.escape(p["description"][:90])}…</span></li>'
            for p in sorted(items, key=lambda x: x["h1"])
        )
        sections += f'<section class="seo-landing__block"><h2>{label}</h2><ul class="seo-landing__list seo-guide-hub-list">{links}</ul></section>'

    body = f"""
            <article class="support-section seo-landing" data-track-impression="guide_hub" data-track-label="Patient guides hub">
                <h1>{html.escape(hub['h1'])}</h1>
                <p class="support-intro">{html.escape(hub['intro'])}</p>
                <p><strong>{len(pages)} guides</strong> covering common Crohn's, colitis, and IBD searches, each with links to deeper articles and tools.</p>
{sections}
                {DISCLAIMER}
            </article>"""

    path = "/guides"
    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            breadcrumb_json(path, "Patient Guides"),
            web_page_json(path, hub["h1"], hub["description"]),
            {
                "@type": "ItemList",
                "name": "IBDPal patient guides",
                "numberOfItems": len(pages),
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": i + 1,
                        "url": f"https://www.ibdpal.org/guides/{p['slug']}",
                        "name": p["h1"],
                    }
                    for i, p in enumerate(pages)
                ],
            },
        ],
    }
    return shell(hub["title"], hub["description"], path, body, json_ld)


def patch_sitemap(pages: list[dict]) -> None:
    today = date.today().isoformat()
    urls = ['  <url>\n    <loc>https://www.ibdpal.org/guides</loc>\n    <lastmod>' + today + '</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.93</priority>\n  </url>']
    for p in pages:
        urls.append(
            f'  <url>\n    <loc>https://www.ibdpal.org/guides/{p["slug"]}</loc>\n'
            f'    <lastmod>{today}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.88</priority>\n  </url>'
        )
    block = "\n".join(urls)
    text = SITEMAP.read_text(encoding="utf-8")
    text = re.sub(r"\n  <!-- seo-guides -->.*?</urlset>", f"\n  <!-- seo-guides -->\n{block}\n</urlset>", text, flags=re.DOTALL)
    if "<!-- seo-guides -->" not in text:
        text = text.replace("</urlset>", f"  <!-- seo-guides -->\n{block}\n</urlset>")
    SITEMAP.write_text(text, encoding="utf-8")


def patch_vercel() -> None:
    text = VERCEL.read_text(encoding="utf-8")
    if '"/guides"' in text and '"/guides/:slug"' in text:
        return
    inserts = """    {
      "source": "/guides",
      "destination": "/guides/index.html"
    },
    {
      "source": "/guides/:slug",
      "destination": "/guides/:slug.html"
    },
"""
    text = text.replace('"rewrites": [\n', f'"rewrites": [\n{inserts}')
    VERCEL.write_text(text, encoding="utf-8")


def patch_llms(pages: list[dict]) -> None:
    if not LLMS.exists():
        return
    text = LLMS.read_text(encoding="utf-8")
    marker = "## Patient guides (search topics)"
    block = marker + "\n- https://www.ibdpal.org/guides\n"
    block += "\n".join(f"- https://www.ibdpal.org/guides/{p['slug']}" for p in pages)
    if marker in text:
        text = re.sub(r"## Patient guides \(search topics\).*?(?=\n## |\Z)", block + "\n", text, flags=re.DOTALL)
    else:
        text = text.rstrip() + "\n\n" + block + "\n"
    LLMS.write_text(text, encoding="utf-8")


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    hub = data["hub"]
    pages = data["pages"]
    GUIDES.mkdir(parents=True, exist_ok=True)

    (GUIDES / "index.html").write_text(render_hub(hub, pages), encoding="utf-8")
    for page in pages:
        out = GUIDES / f"{page['slug']}.html"
        out.write_text(render_page(page), encoding="utf-8")
        print(f"Wrote {out.relative_to(ROOT)}")

    patch_sitemap(pages)
    patch_vercel()
    patch_llms(pages)
    print(f"Generated {len(pages)} guides + hub. Updated sitemap, vercel.json, llms.txt")


if __name__ == "__main__":
    main()
