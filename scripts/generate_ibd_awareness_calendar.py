#!/usr/bin/env python3
# Prose style: do not use em dash.
"""Generate /ibd-awareness-calendar from data/ibd-awareness-calendar.json."""
from __future__ import annotations

import html
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "ibd-awareness-calendar.json"
OUT = ROOT / "ibd-awareness-calendar.html"
VERCEL = ROOT / "vercel.json"
SITEMAP = ROOT / "sitemap.xml"
ALIASES = ROOT / "data" / "search-aliases.json"
RESOURCES_BASE = ROOT / "data" / "resources-base.json"
SITE = "https://www.ibdpal.org"
PATH = "/ibd-awareness-calendar"

import sys

sys.path.insert(0, str(ROOT / "scripts"))
from eeat_blocks import content_note_en, edu_disclaimer_en, hub_disclaimer_en  # noqa: E402
from seo_head import breadcrumb_json, render_seo_head, web_page_json  # noqa: E402
from site_nav import PAGE_SCRIPTS, TAB_NAV_HTML, site_header_html  # noqa: E402


def link_list(items: list[dict], *, external: bool = False) -> str:
    lis = []
    for item in items:
        url = html.escape(item["url"])
        label = html.escape(item["label"])
        rel = ' rel="noopener noreferrer"' if external or item["url"].startswith("http") else ""
        lis.append(f"<li><a href=\"{url}\"{rel}>{label}</a></li>")
    return f'<ul class="seo-landing__list">{"".join(lis)}</ul>'


def month_section(m: dict) -> str:
    badge = ""
    if m.get("major"):
        label = html.escape(m.get("campaign_label") or "Major campaign")
        badge = f' <span class="blog-card-chip">{label}</span>'
    highlights = ""
    if m.get("highlight_dates"):
        rows = "".join(
            f"<li><strong>{html.escape(h['label'])}:</strong> {html.escape(h['date'])}</li>"
            for h in m["highlight_dates"]
        )
        highlights = f"<ul class=\"seo-landing__list\">{rows}</ul>"
    note = ""
    if m.get("campaign_note"):
        note = f"<p>{html.escape(m['campaign_note'])}</p>"
    external = ""
    if m.get("external"):
        external = f"<p><strong>Official / Foundation links:</strong></p>{link_list(m['external'], external=True)}"
    return f"""
                <section class="seo-landing__block" id="month-{m['month']:02d}">
                    <h2>{html.escape(m['name'])}: {html.escape(m['event'])}{badge}</h2>
                    <p>{html.escape(m['relevance'])}</p>
                    {highlights}
                    {note}
                    {external}
                    <p><strong>IBDPal resources to feature:</strong></p>
                    {link_list(m.get('links') or [])}
                </section>"""


def render_page(data: dict) -> str:
    year = data.get("year", date.today().year)
    months_html = "".join(month_section(m) for m in data["months"])
    major = [m for m in data["months"] if m.get("major")]
    major_lis = "".join(
        f'<li><a href="#month-{m["month"]:02d}"><strong>{html.escape(m["name"])}</strong></a> · {html.escape(m["event"])}</li>'
        for m in major
    )
    body = f"""
            <article class="support-section seo-landing" data-track-impression="hub_ibd_awareness_calendar">
                <p class="blog-back"><a href="/start-here" class="blog-back-link">← Start here</a> · <a href="/library">Content library</a></p>
                <h1>{html.escape(data["h1"])}</h1>
{content_note_en()}{edu_disclaimer_en()}
                <p class="support-intro">{html.escape(data["intro"])}</p>
                <p class="hub-header-footnote"><small>Calendar year {year} · Updated {html.escape(data.get("updated", ""))} · Education only</small></p>

                <section class="seo-landing__block">
                    <h2>Four major annual campaigns</h2>
                    <p>{html.escape(data.get("priority_note", ""))}</p>
                    <ul class="seo-landing__list">{major_lis}</ul>
                    <p>Use these months for new articles, graphics, Foundation cross-links, and community outreach. Smaller months still get a short feature or resource highlight.</p>
                </section>

                <section class="seo-landing__block">
                    <h2>Two dates to prioritize above everything else</h2>
                    <ul class="seo-landing__list">
                        <li><strong>World IBD Day · May 19</strong> · Global IBD-specific week of education and outreach. Jump to <a href="#month-05">May</a>.</li>
                        <li><strong>Crohn's &amp; Colitis Awareness Week · December 1-7</strong> · Official U.S. observance (not a formal month-long December designation). 2026 Foundation theme: What It Takes. Jump to <a href="#month-12">December</a>.</li>
                    </ul>
                </section>

                <section class="seo-landing__block">
                    <h2>How to use this calendar</h2>
                    <ul class="seo-landing__list">
                        <li>Publish or refresh one timely article or graphic per month</li>
                        <li>Link existing hubs instead of reinventing topics</li>
                        <li>Point readers to the IBDPal app for logging and visit prep</li>
                        <li>Update this page annually when Foundation campaign names change</li>
                    </ul>
                    <p><a href="/#app" class="seo-landing__cta">Explore IBDPal app tools →</a></p>
                </section>
{months_html}
                <section class="seo-landing__block">
                    <h2>Related planning pages</h2>
                    <ul class="seo-landing__list">
                        <li><a href="/treatment-decisions">Treatment decisions and monitoring hub</a></li>
                        <li><a href="/crohns-colitis-foundation-resources">Foundation resources</a></li>
                        <li><a href="/site-updates">Site updates changelog</a></li>
                        <li><a href="/#news-advocacy">Advocacy news</a></li>
                    </ul>
                </section>
                {hub_disclaimer_en()}
            </article>"""

    ld = {
        "@context": "https://schema.org",
        "@graph": [
            breadcrumb_json(PATH, data["h1"]),
            {
                **web_page_json(PATH, data["h1"], data["description"], medical=True),
                "keywords": "World IBD Day, Crohn's Colitis Awareness Week, IBD awareness calendar, National Nutrition Month, Health Literacy Month",
            },
        ],
    }
    head = render_seo_head(
        title=data["title"],
        description=data["description"],
        path=PATH,
        json_ld=ld,
        keywords="World IBD Day, Crohn's and Colitis Awareness Week, IBD awareness calendar, IBDPal",
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <meta name="theme-color" content="#FFE5DC">
{head}
    <link rel="stylesheet" href="/styles.css">
    <link rel="stylesheet" href="/site-layout-icn.css">
    <link rel="stylesheet" href="/site-polish.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/png" href="/IBDPal_Logo.png">
    <link rel="apple-touch-icon" href="/IBDPal_Logo.png">
</head>
<body>
    <div class="container">
{site_header_html()}
{TAB_NAV_HTML}
        <main class="main-content" id="main-content">
{body}
        </main>
        <footer class="footer">
            <div class="footer-content">
                <div class="footer-links">
                    <a href="/start-here" class="footer-link">Start here</a>
                    <a href="/library" class="footer-link">Content library</a>
                    <a href="/resources" class="footer-link">Resource library</a>
                    <a href="/treatment-decisions" class="footer-link">Treatment hub</a>
                    <a href="/privacy" class="footer-link">Privacy</a>
                </div>
                <p><strong>IBDPal</strong> · MediVue nonprofit · Education only, not medical advice.</p>
                <p>&copy; {year} MediVue. All rights reserved.</p>
            </div>
        </footer>
    </div>
{PAGE_SCRIPTS}
</body>
</html>
"""


def patch_vercel() -> None:
    text = VERCEL.read_text(encoding="utf-8")
    if f'"source": "{PATH}"' in text:
        return
    insert = f'    {{\n      "source": "{PATH}",\n      "destination": "{PATH}.html"\n    }},\n'
    text = text.replace('"rewrites": [\n', '"rewrites": [\n' + insert)
    VERCEL.write_text(text, encoding="utf-8")
    print("patched vercel.json")


def patch_sitemap() -> None:
    text = SITEMAP.read_text(encoding="utf-8")
    if f"{SITE}{PATH}</loc>" in text:
        return
    today = date.today().isoformat()
    entry = (
        f"  <url>\n    <loc>{SITE}{PATH}</loc>\n"
        f"    <lastmod>{today}</lastmod>\n"
        f"    <changefreq>yearly</changefreq>\n"
        f"    <priority>0.9</priority>\n  </url>\n"
    )
    text = text.replace("</urlset>", entry + "</urlset>")
    SITEMAP.write_text(text, encoding="utf-8")
    print("patched sitemap.xml")


def update_aliases() -> None:
    data = json.loads(ALIASES.read_text(encoding="utf-8"))
    extras = {
        "ibd awareness calendar": "ibd awareness calendar",
        "awareness calendar": "ibd awareness calendar",
        "world ibd day": "ibd awareness calendar",
        "crohn's colitis awareness week": "ibd awareness calendar",
        "crohns colitis awareness week": "ibd awareness calendar",
        "what it takes ibd": "ibd awareness calendar",
        "national nutrition month ibd": "ibd awareness calendar",
    }
    data.update(extras)
    ALIASES.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("updated search-aliases.json")


def update_resources_base() -> None:
    items = json.loads(RESOURCES_BASE.read_text(encoding="utf-8"))
    entry = {
        "title": "IBD Awareness Calendar",
        "category": "getting-started",
        "type": "site",
        "url": PATH,
        "tags": [
            "awareness",
            "World IBD Day",
            "Crohn's Colitis Awareness Week",
            "calendar",
            "campaign",
            "nutrition month",
            "health literacy",
        ],
        "description": "Annual IBDPal awareness calendar with World IBD Day, Crohn's & Colitis Awareness Week, and month-by-month education themes.",
    }
    if any(i.get("url") == PATH for i in items):
        return
    items.insert(0, entry)
    RESOURCES_BASE.write_text(json.dumps(items, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("updated resources-base.json")


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    OUT.write_text(render_page(data), encoding="utf-8")
    print("wrote", OUT.name)
    patch_vercel()
    patch_sitemap()
    update_aliases()
    update_resources_base()


if __name__ == "__main__":
    main()
