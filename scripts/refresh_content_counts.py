#!/usr/bin/env python3
"""Refresh library counts from live inventory into site-config + About HTML.

Canonical source after refresh: site-config.js → librarySnapshot.
About Overview ("What you will find here") and Analytics ("Library snapshot")
both read those values via data-library-metric (site-global.js).

Also syncs header-reach copy in Analytics to use the same live
data-reach-metric counters as the site banner.

    python scripts/refresh_content_counts.py
"""
from __future__ import annotations

import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

BLOGS = len(list((ROOT / "blogs").glob("*.html")))
GUIDES = len(list((ROOT / "guides").glob("*.html"))) - 1  # exclude index
SPANISH = len(list((ROOT / "es").glob("*.html")))
RESOURCES = (ROOT / "resources-data.js").read_text(encoding="utf-8").count("title:")
SITEMAP = (ROOT / "sitemap.xml").read_text(encoding="utf-8").count("<url>")
ASOF = date.today().isoformat()
HUMAN_STAMP = re.sub(r" 0(\d),", r" \1,", date.today().strftime("%b %d, %Y"))


def _sub(text: str, pattern: str, repl: str, flags: int = 0) -> tuple[str, int]:
    return re.subn(pattern, repl, text, flags=flags)


def sync_site_config(text: str) -> tuple[str, list[str]]:
    notes: list[str] = []
    block = (
        "librarySnapshot: {\n"
        f"      asOf: '{ASOF}',\n"
        f"      articles: {BLOGS},\n"
        f"      guides: {GUIDES},\n"
        f"      resources: {RESOURCES},\n"
        f"      sitemap: {SITEMAP}\n"
        "    }"
    )
    new, n = _sub(
        text,
        r"librarySnapshot:\s*\{[^}]*\}",
        block,
        flags=re.S,
    )
    if n:
        notes.append("site-config librarySnapshot")
        return new, notes
    # Insert before localeMirrors if missing
    if "librarySnapshot:" not in text:
        new, n = _sub(
            text,
            r"(// EN↔ES content pairs)",
            block + ",\n    \\1",
        )
        if n:
            notes.append("site-config librarySnapshot inserted")
            return new, notes
    return text, notes


def sync_data_library_metrics(text: str) -> tuple[str, list[str]]:
    """Update HTML fallbacks inside data-library-metric nodes."""
    notes: list[str] = []
    pairs = [
        (r'(data-library-metric="articles"[^>]*>)\d+', rf"\g<1>{BLOGS}"),
        (r'(data-library-metric="guides"[^>]*>)\d+', rf"\g<1>{GUIDES}"),
        (r'(data-library-metric="resources"[^>]*>)\d+', rf"\g<1>{RESOURCES}"),
        (r'(data-library-metric="sitemap"[^>]*>)\d+', rf"\g<1>{SITEMAP}"),
        (
            r'(data-library-metric="asOf"[^>]*>)[^<]+',
            rf"\g<1>{HUMAN_STAMP}",
        ),
    ]
    for pat, repl in pairs:
        text, n = _sub(text, pat, repl)
        if n:
            notes.append(f"{pat[:32]}…×{n}")
    return text, notes


def sync_library_page_and_impact(text: str) -> tuple[str, list[str]]:
    notes: list[str] = []
    text, n = _sub(
        text,
        r"(By the numbers \()[^)]+(\))",
        rf"\g<1>{HUMAN_STAMP}\2",
    )
    if n:
        notes.append("library by-the-numbers date")
    text, n = _sub(
        text,
        r'(library-stat__n">)\d+(</span><span class="library-stat__l">Articles</span>)',
        rf"\g<1>{BLOGS}\2",
    )
    if n:
        notes.append("library articles")
    text, n = _sub(
        text,
        r'(library-stat__n">)\d+(</span><span class="library-stat__l">Patient guides</span>)',
        rf"\g<1>{GUIDES}\2",
    )
    if n:
        notes.append("library guides")
    text, n = _sub(
        text,
        r'(library-stat__n">)\d+(</span><span class="library-stat__l">Spanish pages</span>)',
        rf"\g<1>{SPANISH}\2",
    )
    if n:
        notes.append("library spanish")
    text, n = _sub(
        text,
        r'(library-stat__n">)\d+\+?(</span><span class="library-stat__l">Resource library entries</span>)',
        rf"\g<1>{RESOURCES}\2",
    )
    if n:
        notes.append("library resources")
    text, n = _sub(
        text,
        r'(library-stat__n">)\d+\+?(</span><span class="library-stat__l">Education and resource pages</span>)',
        rf"\g<1>{SITEMAP}\2",
    )
    if n:
        notes.append("library sitemap")
    text, n = _sub(
        text,
        r"IBD Content Library \| \d+\+? Free Education Pages",
        f"IBD Content Library | {SITEMAP} Free Education Pages",
    )
    if n:
        notes.append("library title")
    text, n = _sub(
        text,
        r"IBDPal impact: \d+\+? free education and resource pages, \d+ articles,",
        f"IBDPal impact: {SITEMAP} free education and resource pages, {BLOGS} articles,",
    )
    if n:
        notes.append("impact blurb")
    text, n = _sub(
        text,
        r"<strong>\d+ articles</strong> including ImproveCareNow",
        f"<strong>{BLOGS} articles</strong> including ImproveCareNow",
    )
    if n:
        notes.append("impact articles")
    text, n = _sub(
        text,
        r"<strong>\d+\+? total education and resource pages</strong>",
        f"<strong>{SITEMAP} total education and resource pages</strong>",
    )
    if n:
        notes.append("impact pages")
    return text, notes


def ensure_analytics_reach_live(text: str) -> tuple[str, list[str]]:
    """Replace stale/duplicated reach copy with one live data-reach-metric line."""
    notes: list[str] = []
    live_li = (
        "<li>Header reach matches the site banner (same live Vercel Analytics counters): "
        '<strong data-reach-metric="totalReaders" data-reach-count="0">0</strong> readers · '
        '<strong data-reach-metric="pageViews" data-reach-count="0">0</strong> views · '
        '<strong data-reach-metric="countries" data-reach-count="0">0</strong> countries</li>'
    )
    new, n = _sub(
        text,
        r"<li>Header reach (?:remains anchored to Vercel Web Analytics|matches the site banner)"
        r".*?</li>",
        live_li,
        flags=re.S,
    )
    if n:
        notes.append("analytics reach -> live banner counters")
    return new, notes


def main() -> None:
    print(
        {
            "blogs": BLOGS,
            "guides": GUIDES,
            "spanish": SPANISH,
            "resources": RESOURCES,
            "sitemap": SITEMAP,
            "asOf": ASOF,
            "stamp": HUMAN_STAMP,
        }
    )

    cfg_path = ROOT / "site-config.js"
    cfg = cfg_path.read_text(encoding="utf-8")
    cfg2, notes = sync_site_config(cfg)
    if cfg2 != cfg:
        cfg_path.write_text(cfg2, encoding="utf-8")
        print("updated site-config.js |", ", ".join(notes))
    else:
        print("unchanged site-config.js")

    for path in (
        ROOT / "index.html",
        ROOT / "about.html",
        ROOT / "impact.html",
        ROOT / "library.html",
        ROOT / "site-updates.html",
    ):
        text = path.read_text(encoding="utf-8")
        orig = text
        all_notes: list[str] = []
        text, n = sync_data_library_metrics(text)
        all_notes.extend(n)
        text, n = sync_library_page_and_impact(text)
        all_notes.extend(n)
        if path.name == "index.html":
            text, n = ensure_analytics_reach_live(text)
            all_notes.extend(n)
        if text != orig:
            path.write_text(text, encoding="utf-8")
            print("updated", path.name, "|", ", ".join(all_notes) or "edits")
        else:
            print("unchanged", path.name)


if __name__ == "__main__":
    main()
