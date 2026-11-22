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
PROMO_JS = ROOT / "awareness-month-promo.js"
VERCEL = ROOT / "vercel.json"
SITEMAP = ROOT / "sitemap.xml"
ALIASES = ROOT / "data" / "search-aliases.json"
RESOURCES_BASE = ROOT / "data" / "resources-base.json"
SITE = "https://www.ibdpal.org"
PATH = "/ibd-awareness-calendar"

import sys

sys.path.insert(0, str(ROOT / "scripts"))
from eeat_blocks import hub_disclaimer_en  # noqa: E402
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


def seo_month_list(months: list[dict]) -> str:
    """Compact crawlable list; not shown as a long page of sections."""
    items = []
    for m in months:
        major = " (major campaign)" if m.get("major") else ""
        items.append(
            f"<li><strong>{html.escape(m['name'])}</strong>: "
            f"{html.escape(m['event'])}{major}. {html.escape(m['relevance'])}</li>"
        )
    return (
        '<section class="iac__seo-list" aria-label="Full year overview">'
        f"<h2 class=\"iac__sr-only\">All {len(months)} months</h2>"
        f'<ul>{"".join(items)}</ul></section>'
    )


def interactive_calendar_html(year: int, major: list[dict]) -> str:
    weekdays = "".join(
        f'<div class="iac__weekday" aria-hidden="true">{d}</div>'
        for d in ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
    )
    jumps = "".join(
        f'<button type="button" class="iac__jump" data-iac-jump="{m["month"]}">'
        f'{html.escape(m["name"])}</button>'
        for m in major
    )
    return f"""
                <section class="iac" id="iac-root" aria-label="Interactive IBD awareness calendar for {year}">
                    <p class="iac__sr-only" data-iac-live aria-live="polite"></p>
                    <div class="iac__jumps" role="group" aria-label="Jump to major campaign months">
                        <span class="iac__jumps-label">Jump to</span>
                        {jumps}
                    </div>
                    <div class="iac__layout">
                        <div class="iac__calendar">
                            <div class="iac__toolbar">
                                <button type="button" class="iac__nav" data-iac-prev aria-label="Previous month">‹</button>
                                <h2 class="iac__month-label" data-iac-month-label>{year}</h2>
                                <button type="button" class="iac__nav" data-iac-next aria-label="Next month">›</button>
                            </div>
                            <div class="iac__weekdays">{weekdays}</div>
                            <div class="iac__grid" data-iac-grid role="grid" aria-label="Days of the month"></div>
                            <div class="iac__legend" aria-hidden="true">
                                <span class="iac__legend-item"><span class="iac__swatch iac__swatch--theme"></span> Month theme</span>
                                <span class="iac__legend-item"><span class="iac__swatch iac__swatch--peak"></span> Key event day</span>
                            </div>
                        </div>
                        <aside class="iac__panel" data-iac-panel aria-live="polite">
                            <p class="iac__panel-body">Loading month details…</p>
                        </aside>
                    </div>
                </section>"""


def render_page(data: dict) -> str:
    year = data.get("year", date.today().year)
    major = [m for m in data["months"] if m.get("major")]
    cal_json = json.dumps(data, ensure_ascii=False)
    short_intro = (
        f"Use the arrows to browse {year}. Highlighted days mark campaigns; "
        "details and resources stay in the panel beside the calendar."
    )
    body = f"""
            <article class="support-section seo-landing iac-page" data-track-impression="hub_ibd_awareness_calendar">
                <p class="blog-back"><a href="/start-here" class="blog-back-link">← Start here</a> · <a href="/library">Content library</a></p>
                <h1>{html.escape(data["h1"])}</h1>
                <p class="iac-page__lede">{html.escape(short_intro)}</p>
                <p class="hub-header-footnote"><small>Calendar year {year} · Updated {html.escape(data.get("updated", ""))} · Education only · Not medical advice</small></p>

{interactive_calendar_html(year, major)}

                <p class="iac-page__footer-links">
                    <a href="/treatment-decisions">Treatment hub</a>
                    · <a href="/crohns-colitis-foundation-resources">Foundation resources</a>
                    · <a href="/#app">IBDPal app</a>
                </p>
                {seo_month_list(data["months"])}
                {hub_disclaimer_en()}
            </article>
            <script>window.IBDPAL_AWARENESS_CALENDAR = {cal_json};</script>
            <script src="/ibd-awareness-calendar.js" defer></script>"""

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
    <link rel="stylesheet" href="/ibd-awareness-calendar.css">
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


def write_promo_js(data: dict) -> None:
    """Compact month labels for the home-page crisis-strip promo."""
    months = [
        {
            "month": m["month"],
            "name": m["name"],
            "event": m["event"],
            "major": bool(m.get("major")),
        }
        for m in data.get("months") or []
    ]
    payload = {
        "year": data.get("year", date.today().year),
        "path": PATH,
        "months": months,
    }
    PROMO_JS.write_text(
        "/* Generated from data/ibd-awareness-calendar.json — do not edit by hand. */\n"
        f"window.IBDPAL_AWARENESS_PROMO = {json.dumps(payload, ensure_ascii=False)};\n",
        encoding="utf-8",
    )
    print("wrote", PROMO_JS.name)


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
    write_promo_js(data)
    patch_vercel()
    patch_sitemap()
    update_aliases()
    update_resources_base()


if __name__ == "__main__":
    main()
