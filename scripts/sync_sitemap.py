#!/usr/bin/env python3
"""Rebuild sitemap.xml from indexable site files (www.ibdpal.org URLs)."""
from __future__ import annotations

from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITEMAP = ROOT / "sitemap.xml"
SITE = "https://www.ibdpal.org"

SKIP_ROOT_HTML = {
    "support.html",  # legacy stub; /support/index.html is canonical
}

# Hash-canonical or redirect-only URLs (not indexable standalone pages)
SKIP_URL_PATHS = {
    "/privacy",  # 301 to /#privacy; canonical is fragment URL
}

HUB_SLUGS = {
    "ibd-nutrition",
    "crohns-disease",
    "ulcerative-colitis",
    "teens-and-school",
    "flare-help",
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
        return f"/{slug}"

    if len(parts) == 2 and parts[0] == "blogs" and name.endswith(".html"):
        return f"/blog/{name[:-5]}"

    if len(parts) == 3 and parts[0] == "blogs" and parts[1] == "amp" and name.endswith(".html"):
        return f"/blog/{name[:-5]}/amp"

    if len(parts) == 2 and parts[0] == "guides" and name.endswith(".html"):
        return f"/guides/{name[:-5]}"

    if len(parts) == 3 and parts[0] == "guides" and parts[1] == "amp" and name.endswith(".html"):
        return f"/guides/{name[:-5]}/amp"

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
    if path in {"/blog", "/guides", "/support", "/library", "/ibd-crohns-support", "/newly-diagnosed"}:
        return 0.92
    if path in {f"/{s}" for s in HUB_SLUGS} or path == "/faq" or path == "/research":
        return 0.88
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
    if path in {"/terms", "/executive-summary", "/contact", "/founder"}:
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
    if path in {"/privacy", "/terms", "/executive-summary"}:
        return "yearly"
    return "monthly"


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
    return entries


def render_sitemap(entries: dict[str, tuple[str, float, str]]) -> str:
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for path in sorted(entries.keys(), key=lambda p: (p.count("/"), p)):
        lastmod, priority, changefreq = entries[path]
        lines.append("  <url>")
        lines.append(f"    <loc>{SITE}{path}</loc>")
        lines.append(f"    <lastmod>{lastmod}</lastmod>")
        lines.append(f"    <changefreq>{changefreq}</changefreq>")
        lines.append(f"    <priority>{priority:.2f}</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    entries = discover_entries()
    SITEMAP.write_text(render_sitemap(entries), encoding="utf-8")
    print(f"wrote {SITEMAP.name} ({len(entries)} URLs, last synced {date.today().isoformat()})")


if __name__ == "__main__":
    main()
