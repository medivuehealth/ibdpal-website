#!/usr/bin/env python3
"""Inject meta keywords, sitemap link, and missing robots/canonical on static HTML pages."""
from __future__ import annotations

import re
from pathlib import Path

from seo_keywords import html_path_to_url, keywords_for_path

ROOT = Path(__file__).resolve().parents[1]
SITEMAP_LINK = '    <link rel="sitemap" type="application/xml" title="Sitemap" href="https://www.ibdpal.org/sitemap.xml">'
AUTHOR_META = '    <meta name="author" content="MediVue">'
ROBOTS_META = (
    '    <meta name="robots" content="index, follow, max-image-preview:large, '
    'max-snippet:-1, max-video-preview:-1">'
)

SKIP_DIRS = {"scripts", "node_modules"}


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

    url_path = canonical_from_html(text) or html_path_to_url(rel)
    if not url_path:
        return []

    if 'name="keywords"' not in text:
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
