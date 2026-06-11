#!/usr/bin/env python3
"""Add site-layout-icn.css and site-polish.css to HTML pages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ICN_MARKER = "site-layout-icn.css"
POLISH_MARKER = "site-polish.css"
FONT_MARKER = "Plus+Jakarta+Sans"
ICN_REPLACEMENTS = [
    (
        '<link rel="stylesheet" href="/styles.css">',
        '<link rel="stylesheet" href="/styles.css">\n    <link rel="stylesheet" href="/site-layout-icn.css">',
    ),
    (
        '<link rel="stylesheet" href="styles.css">',
        '<link rel="stylesheet" href="styles.css">\n    <link rel="stylesheet" href="site-layout-icn.css">',
    ),
]
POLISH_SNIPPET = '    <link rel="stylesheet" href="/site-polish.css">'
POLISH_SNIPPET_REL = '    <link rel="stylesheet" href="site-polish.css">'
FONT_LINK = (
    '    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700'
    "&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap\" rel=\"stylesheet\">"
)


def _patch_icn(text: str) -> str:
    if ICN_MARKER in text:
        return text
    for old, new in ICN_REPLACEMENTS:
        if old in text:
            return text.replace(old, new, 1)
    return text


def _patch_polish(text: str) -> str:
    if POLISH_MARKER in text:
        return text
    if ICN_MARKER in text:
        needle = f'<link rel="stylesheet" href="/{ICN_MARKER}">'
        if needle in text:
            return text.replace(needle, needle + "\n" + POLISH_SNIPPET, 1)
        needle = f'<link rel="stylesheet" href="{ICN_MARKER}">'
        if needle in text:
            return text.replace(needle, needle + "\n" + POLISH_SNIPPET_REL, 1)
    return text


def _patch_font(text: str) -> str:
    if FONT_MARKER in text:
        return text
    old = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">'
    if old in text:
        return text.replace(old, FONT_LINK, 1)
    return text


def main():
    for path in ROOT.rglob("*.html"):
        text = path.read_text(encoding="utf-8")
        updated = _patch_icn(text)
        updated = _patch_polish(updated)
        updated = _patch_font(updated)
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            print("patched", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
