#!/usr/bin/env python3
"""Generate public plain-text audit exports (no PII / no raw patient free text).

Outputs:
  /analytics.txt          aggregated reach + library snapshot
  /content-insights.txt   aggregated search terms, gaps, top article views
  /content-inventory.txt  titles, categories, published/modified dates
"""
from __future__ import annotations

import json
import re
import sys
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://www.ibdpal.org"
BLOGS = ROOT / "blogs"
GUIDES = ROOT / "guides"
SITE_CONFIG = ROOT / "site-config.js"
VERCEL = ROOT / "vercel.json"
ROBOTS = ROOT / "robots.txt"
LLMS = ROOT / "llms.txt"

sys.path.insert(0, str(ROOT / "scripts"))
from amp_utils import discover_blogs  # noqa: E402

# Drop terms that look like free-text patient narrative or IDs.
SENSITIVE_TERM = re.compile(
    r"(?i)\b(my name|ssn|phone|email|@|http|https|patient id|\d{3}[-.]?\d{2}[-.]?\d{4})\b"
)


def load_site_config() -> dict:
    text = SITE_CONFIG.read_text(encoding="utf-8")
    reach_m = re.search(r"reachMetrics:\s*\{(.*?)\n\s*\},", text, re.S)
    lib_m = re.search(r"librarySnapshot:\s*\{(.*?)\n\s*\},", text, re.S)

    def parse_block(block: str) -> dict:
        out: dict = {}
        for m in re.finditer(r"(\w+)\s*:\s*('([^']*)'|\"([^\"]*)\"|([0-9.]+))", block):
            key = m.group(1)
            if m.group(3) is not None:
                out[key] = m.group(3)
            elif m.group(4) is not None:
                out[key] = m.group(4)
            else:
                raw = m.group(5)
                out[key] = float(raw) if "." in raw else int(raw)
        return out

    return {
        "reach": parse_block(reach_m.group(1)) if reach_m else {},
        "library": parse_block(lib_m.group(1)) if lib_m else {},
    }


def fetch_brief(days: int = 30, limit: int = 25) -> dict:
    url = f"{SITE}/api/web/analytics?action=brief&days={days}&limit={limit}"
    try:
        with urllib.request.urlopen(url, timeout=40) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return data if data.get("success") else {}
    except Exception as exc:  # noqa: BLE001
        print("WARN: analytics brief fetch failed:", exc)
        return {}


def fetch_gaps(days: int = 90, limit: int = 25) -> list[dict]:
    url = f"{SITE}/api/web/analytics?action=gaps&days={days}&limit={limit}"
    try:
        with urllib.request.urlopen(url, timeout=40) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return data.get("gaps") or []
    except Exception as exc:  # noqa: BLE001
        print("WARN: gaps fetch failed:", exc)
        return []


def clean_terms(rows: list[dict]) -> list[dict]:
    cleaned = []
    for row in rows:
        term = str(row.get("term") or "").strip().lower()
        if not term or len(term) > 60:
            continue
        if SENSITIVE_TERM.search(term):
            continue
        if re.search(r"\d{6,}", term):
            continue
        cleaned.append(row)
    return cleaned


def write_analytics(cfg: dict, brief: dict) -> None:
    reach = cfg.get("reach") or {}
    lib = cfg.get("library") or {}
    summary = brief.get("summary") or {}
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines = [
        "# IBDPal public analytics export",
        "# Aggregated reach only. No cookies, IPs, emails, or raw patient text.",
        f"# Generated: {generated}",
        f"# Source site: {SITE}",
        "",
        "## Reach (site-config verified snapshot)",
        f"anchor_date: {reach.get('anchorDate', '')}",
        f"total_readers_display_baseline: {reach.get('totalReaders', '')}",
        f"page_views_display_baseline: {reach.get('pageViews', '')}",
        f"typical_daily_visitors: {reach.get('typicalDailyVisitors', '')}",
        f"countries_reached_verified: {reach.get('internationalCountriesVerified', '')}",
        "countries_source: Vercel Web Analytics country breakdown (aggregated)",
        "",
        "## Library snapshot",
        f"as_of: {lib.get('asOf', '')}",
        f"articles: {lib.get('articles', '')}",
        f"guides: {lib.get('guides', '')}",
        f"resources: {lib.get('resources', '')}",
        f"sitemap_urls: {lib.get('sitemap', '')}",
        "",
        "## On-site search volume (last 30 days, aggregated)",
        f"searches: {summary.get('searches', 0)}",
        f"unique_normalized_terms: {summary.get('uniqueTerms', 0)}",
        f"zero_result_searches: {summary.get('zeroResultSearches', 0)}",
        "",
        "## Notes",
        "- Counts are privacy-oriented aggregates for content planning.",
        "- Geographic detail is limited to country totals when verified.",
        "- For URL lists use /sitemap.txt. For AI overview use /llms.txt.",
        "- Companion files: /content-insights.txt /content-inventory.txt",
        "",
    ]
    (ROOT / "analytics.txt").write_text("\n".join(lines), encoding="utf-8")
    print("wrote analytics.txt")


def write_insights(brief: dict, gaps: list[dict]) -> None:
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    searches = clean_terms(brief.get("topSearches") or [])
    hard = clean_terms(gaps or brief.get("hardGaps") or [])
    views = brief.get("topViews") or []
    lines = [
        "# IBDPal content insights export",
        "# Aggregated normalized search terms and article views only.",
        "# Excludes identifiable free-text and sensitive patient-entered details.",
        f"# Generated: {generated}",
        f"# Window: last 30 days (searches/views); gaps up to 90 days",
        "",
        "## Top normalized search terms",
        "# term | search_count | avg_results",
    ]
    for row in searches:
        lines.append(
            f"{row.get('term','')}\t{row.get('count',0)}\t{row.get('averageResults', row.get('average_results',''))}"
        )
    lines += ["", "## Hard zero-result / thin-result terms (aggregated)", "# term | count"]
    for row in hard:
        lines.append(f"{row.get('term','')}\t{row.get('count',0)}")
    lines += ["", "## Top article views (content events)", "# path | views"]
    for row in views:
        url = row.get("url") or ""
        if not url.startswith("/"):
            continue
        lines.append(f"{url}\t{row.get('count',0)}")
    lines += [
        "",
        "## Privacy",
        "- Terms are normalized keywords, not raw query dumps.",
        "- Do not reconstruct individual users from this file.",
        "",
    ]
    (ROOT / "content-insights.txt").write_text("\n".join(lines), encoding="utf-8")
    print("wrote content-insights.txt")


def guide_inventory() -> list[dict]:
    rows = []
    for path in sorted(GUIDES.glob("*.html")):
        if path.name.startswith("amp"):
            continue
        text = path.read_text(encoding="utf-8")
        title_m = re.search(r"<h1[^>]*>(.*?)</h1>", text, re.S)
        if not title_m:
            title_m = re.search(r"<title>(.*?)</title>", text, re.S)
        desc_m = re.search(r'<meta name="description" content="([^"]*)"', text)
        pub_m = re.search(r'property="article:published_time" content="([^"]*)"', text)
        mod_m = re.search(r'property="article:modified_time" content="([^"]*)"', text)
        title = re.sub(r"<[^>]+>", "", title_m.group(1)).strip() if title_m else path.stem
        rows.append(
            {
                "type": "guide",
                "path": f"/guides/{path.stem}",
                "title": title,
                "category": "Patient guide",
                "published": pub_m.group(1) if pub_m else "",
                "modified": mod_m.group(1) if mod_m else (pub_m.group(1) if pub_m else ""),
                "description": desc_m.group(1) if desc_m else "",
            }
        )
    return rows


def write_inventory() -> None:
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    posts = discover_blogs(BLOGS)
    rows = []
    for slug, post in sorted(posts.items()):
        text = (BLOGS / f"{slug}.html").read_text(encoding="utf-8")
        mod_m = re.search(r'property="article:modified_time" content="([^"]*)"', text)
        rows.append(
            {
                "type": "article",
                "path": f"/blog/{slug}",
                "title": post.get("title", slug),
                "category": post.get("category", ""),
                "published": post.get("date_iso", ""),
                "modified": mod_m.group(1) if mod_m else post.get("date_iso", ""),
            }
        )
    rows.extend(guide_inventory())
    lines = [
        "# IBDPal content inventory",
        "# Titles, categories, publication and update dates for education pages.",
        f"# Generated: {generated}",
        f"# Articles: {sum(1 for r in rows if r['type']=='article')}",
        f"# Guides: {sum(1 for r in rows if r['type']=='guide')}",
        "",
        "# type\tpath\tcategory\tpublished\tmodified\ttitle",
    ]
    for r in rows:
        title = r["title"].replace("\t", " ").replace("\n", " ")
        cat = str(r.get("category", "")).replace("\t", " ")
        lines.append(
            f"{r['type']}\t{r['path']}\t{cat}\t{r.get('published','')}\t{r.get('modified','')}\t{title}"
        )
    lines.append("")
    (ROOT / "content-inventory.txt").write_text("\n".join(lines), encoding="utf-8")
    print("wrote content-inventory.txt")


TXT_HEADER_BLOCK = """    {
      "source": "/analytics.txt",
      "headers": [
        {
          "key": "Content-Type",
          "value": "text/plain; charset=utf-8"
        },
        {
          "key": "Access-Control-Allow-Origin",
          "value": "*"
        },
        {
          "key": "Cache-Control",
          "value": "public, max-age=1800, s-maxage=1800"
        },
        {
          "key": "X-Robots-Tag",
          "value": "index, follow"
        }
      ]
    },
    {
      "source": "/content-insights.txt",
      "headers": [
        {
          "key": "Content-Type",
          "value": "text/plain; charset=utf-8"
        },
        {
          "key": "Access-Control-Allow-Origin",
          "value": "*"
        },
        {
          "key": "Cache-Control",
          "value": "public, max-age=1800, s-maxage=1800"
        },
        {
          "key": "X-Robots-Tag",
          "value": "index, follow"
        }
      ]
    },
    {
      "source": "/content-inventory.txt",
      "headers": [
        {
          "key": "Content-Type",
          "value": "text/plain; charset=utf-8"
        },
        {
          "key": "Access-Control-Allow-Origin",
          "value": "*"
        },
        {
          "key": "Cache-Control",
          "value": "public, max-age=1800, s-maxage=1800"
        },
        {
          "key": "X-Robots-Tag",
          "value": "index, follow"
        }
      ]
    },
"""


def patch_vercel() -> None:
    text = VERCEL.read_text(encoding="utf-8")
    if '"source": "/analytics.txt"' in text:
        print("vercel headers for analytics.txt already present")
        return
    text = text.replace(
        '      "source": "/llms.txt",',
        TXT_HEADER_BLOCK + '      "source": "/llms.txt",',
        1,
    )
    VERCEL.write_text(text, encoding="utf-8")
    print("patched vercel.json headers")


def patch_robots() -> None:
    text = ROBOTS.read_text(encoding="utf-8")
    block = (
        "# Public plain-text audit exports (aggregated, no PII):\n"
        f"# {SITE}/analytics.txt\n"
        f"# {SITE}/content-insights.txt\n"
        f"# {SITE}/content-inventory.txt\n"
        f"# {SITE}/llms.txt\n"
        f"# {SITE}/sitemap.txt\n"
    )
    if "/analytics.txt" in text:
        print("robots.txt already documents analytics.txt")
        return
    text = text.replace(
        "# Machine-readable content index for assistants and retrieval systems:\n",
        block + "# Machine-readable content index for assistants and retrieval systems:\n",
        1,
    )
    # Explicit allow for audit text files
    if "Allow: /analytics.txt" not in text:
        text = text.replace(
            "Allow: /a50b1f808a1d4c41b89fc4b35d46418a.txt",
            "Allow: /a50b1f808a1d4c41b89fc4b35d46418a.txt\n"
            "Allow: /analytics.txt\n"
            "Allow: /content-insights.txt\n"
            "Allow: /content-inventory.txt\n"
            "Allow: /llms.txt\n"
            "Allow: /sitemap.txt",
            1,
        )
    ROBOTS.write_text(text, encoding="utf-8")
    print("patched robots.txt")


def patch_llms() -> None:
    text = LLMS.read_text(encoding="utf-8")
    extra = (
        f"- Analytics (aggregated reach): {SITE}/analytics.txt\n"
        f"- Content insights (search/views aggregates): {SITE}/content-insights.txt\n"
        f"- Content inventory (titles/dates): {SITE}/content-inventory.txt\n"
    )
    if "/analytics.txt" in text:
        print("llms.txt already lists analytics.txt")
        return
    text = text.replace(
        f"- This file: {SITE}/llms.txt\n",
        f"- This file: {SITE}/llms.txt\n{extra}",
        1,
    )
    LLMS.write_text(text, encoding="utf-8")
    print("patched llms.txt")


def patch_changelog() -> None:
    path = ROOT / "scripts" / "ui_snippets.py"
    text = path.read_text(encoding="utf-8")
    bullet = (
        '                            <li><strong>Public text audit exports:</strong> '
        '<a href="/analytics.txt">analytics.txt</a>, '
        '<a href="/content-insights.txt">content-insights.txt</a>, '
        '<a href="/content-inventory.txt">content-inventory.txt</a> '
        "(aggregated, no PII); executive summary rewritten for nonprofit mission</li>\n"
    )
    if "Public text audit exports" in text:
        return
    anchor = '                        <h2>November 2026</h2>\n                        <ul class="seo-landing__list">\n'
    if anchor in text:
        path.write_text(text.replace(anchor, anchor + bullet, 1), encoding="utf-8")
        print("patched changelog")


def main() -> None:
    cfg = load_site_config()
    brief = fetch_brief(30, 25)
    gaps = fetch_gaps(90, 25)
    write_analytics(cfg, brief)
    write_insights(brief, gaps)
    write_inventory()
    patch_vercel()
    patch_robots()
    patch_llms()
    patch_changelog()
    try:
        from sync_site_updates_sections import main as sync_updates  # noqa: E402

        sync_updates()
    except Exception as exc:  # noqa: BLE001
        print("WARN: site updates sync:", exc)
    print("Done. Public URLs:")
    print(f"  {SITE}/analytics.txt")
    print(f"  {SITE}/content-insights.txt")
    print(f"  {SITE}/content-inventory.txt")


if __name__ == "__main__":
    main()
