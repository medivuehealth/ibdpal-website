#!/usr/bin/env python3
"""Inject meta keywords, sitemap link, and missing robots/canonical on static HTML pages."""
from __future__ import annotations

import re
from pathlib import Path

from seo_keywords import html_path_to_url, keywords_for_path

ROOT = Path(__file__).resolve().parents[1]
SITEMAP_LINK = '    <link rel="sitemap" type="application/xml" title="Sitemap" href="https://www.ibdpal.org/sitemap.xml">'
AUTHOR_META = '    <meta name="author" content="MediVue">'
THEME_COLOR_META = '    <meta name="theme-color" content="#FFE5DC">'
ROBOTS_META = (
    '    <meta name="robots" content="index, follow, max-image-preview:large, '
    'max-snippet:-1, max-video-preview:-1">'
)
VIEWPORT_OLD = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
VIEWPORT_NEW = '<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">'

SKIP_DIRS = {"scripts", "node_modules"}


def patch_viewport_theme(text: str) -> tuple[str, list[str]]:
    changes: list[str] = []
    if VIEWPORT_OLD in text and "viewport-fit=cover" not in text:
        text = text.replace(VIEWPORT_OLD, VIEWPORT_NEW, 1)
        changes.append("viewport")
    # Normalize: theme-color belongs after viewport (not before charset)
    text = re.sub(r"\s*<meta name=\"theme-color\" content=\"#FFE5DC\">\n?", "\n", text)
    if 'name="theme-color"' not in text and "viewport-fit=cover" in text:
        text = re.sub(
            r'(<meta name="viewport" content="width=device-width[^"]+">)',
            r"\1\n" + THEME_COLOR_META,
            text,
            count=1,
        )
        changes.append("theme-color")
    return text, changes


def canonical_from_html(text: str) -> str | None:
    m = re.search(r'<link rel="canonical" href="https://www\.ibdpal\.org([^"]+)"', text)
    return m.group(1) if m else None


def inject_after_description(text: str, insert: str) -> str:
    if insert.strip() in text:
        return text
    return re.sub(
        r"(<meta name=\"description\" content=\"[^\"]*\">)",
        r"\1\n" + insert,
        text,
        count=1,
    )


def inject_before_head_close(text: str, insert: str) -> str:
    if insert.strip() in text:
        return text
    return text.replace("</head>", insert + "\n</head>", 1)


def patch_file(path: Path) -> list[str]:
    rel = path.relative_to(ROOT)
    if rel.parts[0] in SKIP_DIRS:
        return []
    if "amp" in rel.parts:
        return []

    text = path.read_text(encoding="utf-8")
    original = text
    changes: list[str] = []

    text, mobile_changes = patch_viewport_theme(text)
    changes.extend(mobile_changes)

    url_path = canonical_from_html(text) or html_path_to_url(rel)

    if url_path and 'name="keywords"' not in text:
        kw = keywords_for_path(url_path)
        kw_line = f'    <meta name="keywords" content="{kw}">'
        text = inject_after_description(text, kw_line)
        changes.append("keywords")

    if 'rel="sitemap"' not in text:
        text = inject_before_head_close(text, SITEMAP_LINK)
        changes.append("sitemap")

    if 'name="author"' not in text:
        text = inject_after_description(text, AUTHOR_META)
        changes.append("author")

    if 'name="robots"' not in text and "<head>" in text:
        text = inject_after_description(text, ROBOTS_META)
        changes.append("robots")

    if path.name == "terms.html" and 'rel="canonical"' not in text:
        text = inject_after_description(
            text,
            '    <link rel="canonical" href="https://www.ibdpal.org/terms">',
        )
        changes.append("canonical")

    if text != original:
        path.write_text(text, encoding="utf-8")
    return changes


def main() -> None:
    touched = 0
    for html_path in sorted(ROOT.rglob("*.html")):
        rel = html_path.relative_to(ROOT)
        if rel.parts and rel.parts[0] in SKIP_DIRS:
            continue
        changes = patch_file(html_path)
        if changes:
            touched += 1
            print(f"patched {rel}: {', '.join(changes)}")
    print(f"done — updated {touched} HTML files")


if __name__ == "__main__":
    main()
