#!/usr/bin/env python3
"""Patch HTML files: canonical host script + absolute ibdpal.org tab links."""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL_SCRIPT = '    <script src="/canonical-host.js"></script>\n'
TAB_REPLACEMENTS = [
    ('href="/#overview"', 'href="https://ibdpal.org/#overview"'),
    ('href="/#app"', 'href="https://ibdpal.org/#app"'),
    ('href="/#resources"', 'href="https://ibdpal.org/#resources"'),
    ('href="/#blogs"', 'href="https://ibdpal.org/#blogs"'),
    ('href="/#community"', 'href="https://ibdpal.org/#community"'),
    ('href="/#contact"', 'href="https://ibdpal.org/#contact"'),
    ('href="/#privacy"', 'href="https://ibdpal.org/#privacy"'),
    ('href="/#support"', 'href="https://ibdpal.org/#support"'),
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
        "window.location.replace('https://ibdpal.org/#privacy')",
    )
    text = text.replace(
        "window.location.replace('/#support')",
        "window.location.replace('https://ibdpal.org/#support')",
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
