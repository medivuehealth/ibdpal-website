#!/usr/bin/env python3
"""Patch HTML files: canonical host script + absolute ibdpal.org tab links."""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL_SCRIPT = '    <script src="/canonical-host.js"></script>\n'
WWW = "https://www.ibdpal.org"
TAB_REPLACEMENTS = [
    ('href="/#overview"', f'href="{WWW}/#overview"'),
    ('href="/#app"', f'href="{WWW}/#app"'),
    ('href="/#resources"', f'href="{WWW}/#resources"'),
    ('href="/#blogs"', f'href="{WWW}/#blogs"'),
    ('href="/#community"', f'href="{WWW}/#community"'),
    ('href="/#contact"', f'href="{WWW}/#contact"'),
    ('href="/#privacy"', f'href="{WWW}/#privacy"'),
    ('href="/#support"', f'href="{WWW}/#support"'),
    ('href="https://www.ibdpal.org/#overview"', f'href="{WWW}/#overview"'),
    ('href="https://www.ibdpal.org/#app"', f'href="{WWW}/#app"'),
    ('href="https://www.ibdpal.org/#resources"', f'href="{WWW}/#resources"'),
    ('href="https://www.ibdpal.org/#blogs"', f'href="{WWW}/#blogs"'),
    ('href="https://www.ibdpal.org/#community"', f'href="{WWW}/#community"'),
    ('href="https://www.ibdpal.org/#contact"', f'href="{WWW}/#contact"'),
    ('href="https://www.ibdpal.org/#privacy"', f'href="{WWW}/#privacy"'),
    ('href="https://www.ibdpal.org/#support"', f'href="{WWW}/#support"'),
]


def patch_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    orig = text
    for old, new in TAB_REPLACEMENTS:
        text = text.replace(old, new)
    if 'canonical-host.js' not in text and "<head>" in text:
        text = text.replace(
            "<head>\n",
            "<head>\n" + CANONICAL_SCRIPT,
            1,
        )
        # Also handle head with charset first
        if 'canonical-host.js' not in text:
            text = re.sub(
                r'(<meta name="viewport"[^>]+>\n)',
                r'\1' + CANONICAL_SCRIPT,
                text,
                count=1,
            )
    text = text.replace(
        "window.location.replace('/#privacy')",
        "window.location.replace('https://www.ibdpal.org/#privacy')",
    )
    text = text.replace(
        "window.location.replace('https://www.ibdpal.org/#privacy')",
        "window.location.replace('https://www.ibdpal.org/#privacy')",
    )
    text = text.replace(
        "window.location.replace('/#support')",
        "window.location.replace('https://www.ibdpal.org/#support')",
    )
    text = text.replace(
        "window.location.replace('https://www.ibdpal.org/#support')",
        "window.location.replace('https://www.ibdpal.org/#support')",
    )
    if text != orig:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> None:
    count = 0
    for path in ROOT.rglob("*.html"):
        if patch_file(path):
            print(f"Patched {path.relative_to(ROOT)}")
            count += 1
    print(f"Done. {count} files updated.")


if __name__ == "__main__":
    main()
