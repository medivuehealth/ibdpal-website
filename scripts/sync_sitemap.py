#!/usr/bin/env python3
"""Rebuild sitemap.xml plus crawl-friendly sitemap.txt / sitemap.json / HTML map."""
from __future__ import annotations

from datetime import date, datetime
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITEMAP = ROOT / "sitemap.xml"
SITEMAP_TXT = ROOT / "sitemap.txt"
SITEMAP_JSON = ROOT / "sitemap.json"
SITEMAP_HTML = ROOT / "sitemap.html"
SITE = "https://www.ibdpal.org"
ES_DATA = ROOT / "data" / "es-pages.json"

SKIP_ROOT_HTML = {
    "support.html",  # legacy stub; /support/index.html is canonical
}

# Non-canonical path aliases (served via rewrite from a differently named file)
SKIP_URL_PATHS = {
    "/privacy-app",  # canonical is /privacy/app
}

HUB_SLUGS = {
    "ibd-nutrition",
    "stool-labs-decoder",
    "what-is-ibd",
    "crohns-and-colitis",
    "crohns-disease",
    "ulcerative-colitis",
    "teens-and-school",
    "flare-help",
    "treatment-decisions",
}


def file_lastmod(path: Path) -> str:
    ts = path.stat().st_mtime
    return datetime.fromtimestamp(ts).date().isoformat()


def path_to_url(rel: Path) -> str | None:
    parts = rel.parts
    name = rel.name

    if name == "index.html":
        if len(parts) == 1:
            return "/"
        if parts[0] == "blogs":
            return "/blog"
        if parts[0] == "guides":
            return "/guides"
        if parts[0] == "support":
            return "/support"
        if parts[0] == "blog":
            return "/blog"
        if parts[0] == "patient-stories":
            return "/patient-stories"
        if parts[0] == "es":
            return f"/es/{parts[1]}" if len(parts) > 2 else "/es"
        return None

    if len(parts) == 1 and name.endswith(".html"):
        slug = name[:-5]
        if slug == "privacy-app":
            return "/privacy/app"
        return f"/{slug}"

    if len(parts) == 2 and parts[0] == "blogs" and name.endswith(".html"):
        return f"/blog/{name[:-5]}"

    if len(parts) == 2 and parts[0] == "tools" and name.endswith(".html"):
        return f"/tools/{name[:-5]}"

    if len(parts) == 3 and parts[0] == "blogs" and parts[1] == "amp" and name.endswith(".html"):
        return None

    if len(parts) == 2 and parts[0] == "guides" and name.endswith(".html"):
        return f"/guides/{name[:-5]}"

    if len(parts) == 3 and parts[0] == "guides" and parts[1] == "amp" and name.endswith(".html"):
        return None

    if len(parts) == 2 and parts[0] == "support" and name.endswith(".html"):
        return f"/support/{name[:-5]}"

    if len(parts) == 2 and parts[0] == "patient-stories" and name.endswith(".html"):
        return f"/patient-stories/{name[:-5]}"

    if len(parts) == 2 and parts[0] == "es" and name.endswith(".html"):
        return f"/es/{name[:-5]}"

    return None


def priority_for(path: str) -> float:
    if path == "/":
        return 1.0
    if path in {"/start-here", "/library", "/resources", "/research"}:
        return 0.94
    if path in {
        "/blog",
        "/guides",
        "/support",
        "/ibd-crohns-support",
        "/newly-diagnosed",
        "/crohns-colitis-foundation-resources",
        "/trusted-ibd-resources",
        "/ibd-red-flags-urgent-care",
    }:
        return 0.92
    if path in {f"/{s}" for s in HUB_SLUGS} or path == "/faq":
        return 0.88
    if path.startswith("/tools/"):
        return 0.9
    if path.startswith("/blog/") and path.endswith("/amp"):
        return 0.6
    if path.startswith("/guides/") and path.endswith("/amp"):
        return 0.6
    if path.startswith("/blog/"):
        return 0.85
    if path.startswith("/guides/"):
        return 0.84
    if path.startswith("/support/"):
        return 0.82
    if path in {"/about", "/impact", "/news", "/site-updates", "/resources", "/visit-prep", "/glossary"}:
        return 0.85
    if path in {"/privacy", "/privacy/app", "/terms", "/executive-summary", "/contact", "/founder", "/about-founders"}:
        return 0.55
    if path.startswith("/es/"):
        return 0.78
    if path.startswith("/patient-stories"):
        return 0.8
    return 0.75


def changefreq_for(path: str) -> str:
    if path == "/":
        return "weekly"
    if path.startswith("/blog/") or path in {"/news", "/site-updates"}:
        return "monthly"
    if path in {"/privacy", "/privacy/app", "/terms", "/executive-summary"}:
        return "yearly"
    return "monthly"


def load_hreflang_pairs() -> dict[str, dict[str, str]]:
    if not ES_DATA.is_file():
        return {}
    data = json.loads(ES_DATA.read_text(encoding="utf-8"))
    pairs: dict[str, dict[str, str]] = {}
    for en_path, es_path in data.get("mirrors", {}).items():
        pairs[en_path] = {
            "en": f"{SITE}{en_path}",
            "es": f"{SITE}{es_path}",
            "x-default": f"{SITE}{en_path}",
        }
        pairs[es_path] = {
            "en": f"{SITE}{en_path}",
            "es": f"{SITE}{es_path}",
            "x-default": f"{SITE}{en_path}",
        }
    return pairs


def discover_entries() -> dict[str, tuple[str, float, str]]:
    entries: dict[str, tuple[str, float, str]] = {}
    today = date.today().isoformat()

    for html_path in ROOT.rglob("*.html"):
        rel = html_path.relative_to(ROOT)
        if any(part.startswith(".") for part in rel.parts):
            continue
        if rel.parts[0] in {"scripts", "node_modules"}:
            continue
        if rel.name in SKIP_ROOT_HTML:
            continue

        url_path = path_to_url(rel)
        if not url_path or url_path in SKIP_URL_PATHS:
            continue

        lastmod = file_lastmod(html_path)
        entries[url_path] = (lastmod, priority_for(url_path), changefreq_for(url_path))

    # Homepage: prefer newest lastmod among key surfaces
    entries["/"] = (today, 1.0, "weekly")

    # Crawlable alias for homepage #about-founders (hash URLs are not sitemap-indexable alone)
    founder_html = ROOT / "founder.html"
    if founder_html.is_file():
        entries["/about-founders"] = (
            file_lastmod(founder_html),
            priority_for("/about-founders"),
            changefreq_for("/about-founders"),
        )

    return entries


def sorted_paths(entries: dict[str, tuple[str, float, str]]) -> list[str]:
    return sorted(entries.keys(), key=lambda p: (p.count("/"), p))


def render_sitemap(entries: dict[str, tuple[str, float, str]]) -> str:
    alternates = load_hreflang_pairs()
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">',
    ]
    for path in sorted_paths(entries):
        lastmod, priority, changefreq = entries[path]
        lines.append("  <url>")
        lines.append(f"    <loc>{SITE}{path}</loc>")
        for hreflang, href in alternates.get(path, {}).items():
            lines.append(
                f'    <xhtml:link rel="alternate" hreflang="{hreflang}" href="{html.escape(href, quote=True)}" />'
            )
        lines.append(f"    <lastmod>{lastmod}</lastmod>")
        lines.append(f"    <changefreq>{changefreq}</changefreq>")
        lines.append(f"    <priority>{priority:.2f}</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")
    lines.append("")
    return "\n".join(lines)


def render_sitemap_txt(entries: dict[str, tuple[str, float, str]]) -> str:
    """Plain URL list for crawlers / readers that mishandle XML."""
    return "\n".join(f"{SITE}{path}" for path in sorted_paths(entries)) + "\n"


def render_sitemap_json(entries: dict[str, tuple[str, float, str]]) -> str:
    """JSON mirror for AI tools and programmatic audits that strip XML tags."""
    rows = []
    for path in sorted_paths(entries):
        lastmod, priority, changefreq = entries[path]
        rows.append(
            {
                "loc": f"{SITE}{path}",
                "path": path,
                "lastmod": lastmod,
                "changefreq": changefreq,
                "priority": round(priority, 2),
            }
        )
    payload = {
        "generated_at": date.today().isoformat(),
        "canonical_xml": f"{SITE}/sitemap.xml",
        "plain_text": f"{SITE}/sitemap.txt",
        "html_map": f"{SITE}/sitemap",
        "url_count": len(rows),
        "urls": rows,
    }
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def bucket_for(path: str) -> str:
    if path == "/":
        return "Home"
    if path.startswith("/blog/"):
        return "Blog"
    if path.startswith("/guides/"):
        return "Guides"
    if path.startswith("/support/"):
        return "Support by state"
    if path.startswith("/es/"):
        return "Español"
    if path.startswith("/tools/"):
        return "Tools"
    return "Site pages"


def render_sitemap_html(entries: dict[str, tuple[str, float, str]]) -> str:
    """HTML URL directory for browser and markdown-style web readers."""
    groups: dict[str, list[str]] = {}
    for path in sorted_paths(entries):
        groups.setdefault(bucket_for(path), []).append(path)

    sections = []
    for name in ("Home", "Site pages", "Blog", "Guides", "Tools", "Support by state", "Español"):
        paths = groups.get(name) or []
        if not paths:
            continue
        items = "\n".join(
            f'        <li><a href="{html.escape(SITE + path)}">{html.escape(path or "/")}</a></li>'
            for path in paths
        )
        sections.append(
            f'      <section class="seo-landing__block">\n'
            f"        <h2>{html.escape(name)} ({len(paths)})</h2>\n"
            f'        <ul class="seo-landing__list">\n{items}\n        </ul>\n'
            f"      </section>"
        )

    body_sections = "\n".join(sections)
    today = date.today().isoformat()
    count = len(entries)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <meta name="theme-color" content="#FFE5DC">
    <script src="/canonical-host.js"></script>
    <title>IBDPal Sitemap | Crawlable URL Directory</title>
    <meta name="description" content="Human- and machine-readable IBDPal URL directory. Also available as sitemap.xml, sitemap.txt, and sitemap.json.">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{SITE}/sitemap">
    <link rel="alternate" type="application/xml" href="{SITE}/sitemap.xml" title="XML sitemap">
    <link rel="alternate" type="text/plain" href="{SITE}/sitemap.txt" title="Plain-text sitemap">
    <link rel="alternate" type="application/json" href="{SITE}/sitemap.json" title="JSON sitemap">
    <link rel="stylesheet" href="/styles.css">
    <link rel="stylesheet" href="/site-layout-icn.css">
    <link rel="stylesheet" href="/site-polish.css">
    <link rel="icon" type="image/png" href="/IBDPal_Logo.png">
</head>
<body>
    <div class="container">
        <main class="main-content" id="main-content">
            <article class="support-section seo-landing">
                <h1>IBDPal sitemap</h1>
                <p class="support-intro">{count} indexable URLs · synced {html.escape(today)}. Prefer machine formats when crawling: <a href="/sitemap.xml">sitemap.xml</a>, <a href="/sitemap.txt">sitemap.txt</a>, <a href="/sitemap.json">sitemap.json</a>, or <a href="/llms.txt">llms.txt</a>.</p>
{body_sections}
            </article>
        </main>
    </div>
    <script src="/site-config.js" defer></script>
    <script src="/site-global.js" defer></script>
</body>
</html>
"""


def main() -> None:
    entries = discover_entries()
    # Keep HTML map itself out of recursive discovery noise; add explicitly.
    entries["/sitemap"] = (date.today().isoformat(), 0.7, "monthly")

    SITEMAP.write_text(render_sitemap(entries), encoding="utf-8")
    SITEMAP_TXT.write_text(render_sitemap_txt(entries), encoding="utf-8")
    SITEMAP_JSON.write_text(render_sitemap_json(entries), encoding="utf-8")
    SITEMAP_HTML.write_text(render_sitemap_html(entries), encoding="utf-8")
    print(
        f"wrote {SITEMAP.name}, {SITEMAP_TXT.name}, {SITEMAP_JSON.name}, {SITEMAP_HTML.name} "
        f"({len(entries)} URLs, last synced {date.today().isoformat()})"
    )


if __name__ == "__main__":
    main()

