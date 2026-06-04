#!/usr/bin/env python3
"""Add site-layout-icn.css to all HTML pages that only load styles.css."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = "site-layout-icn.css"
REPLACEMENTS = [
    (
        '<link rel="stylesheet" href="/styles.css">',
        '<link rel="stylesheet" href="/styles.css">\n    <link rel="stylesheet" href="/site-layout-icn.css">',
    ),
    (
        '<link rel="stylesheet" href="styles.css">',
        '<link rel="stylesheet" href="styles.css">\n    <link rel="stylesheet" href="site-layout-icn.css">',
    ),
]


def main():
    for path in ROOT.rglob("*.html"):
        text = path.read_text(encoding="utf-8")
        if MARKER in text:
            continue
        updated = text
        for old, new in REPLACEMENTS:
            if old in updated:
                updated = updated.replace(old, new, 1)
                break
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            print("patched", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
