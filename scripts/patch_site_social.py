#!/usr/bin/env python3
"""Insert ICN-style social bar + refresh headers from site_nav.py."""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from site_nav import (  # noqa: E402
    SITE_HEADER_HTML,
    SITE_HEADER_STATIC_HTML,
    SITE_SOCIAL_BAR_HTML,
)

HEADER_BLOCK = re.compile(r"<header class=\"header\">.*?</header>", re.DOTALL)
SOCIAL_BLOCK = re.compile(r"<div class=\"site-social-bar\".*?</div>\s*", re.DOTALL)
HOME_NAV = '<a href="/" class="nav-link">Home</a>'


def patch_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    text = SOCIAL_BLOCK.sub("", text)
    m = HEADER_BLOCK.search(text)
    if not m:
        return False
    header = SITE_HEADER_STATIC_HTML if HOME_NAV in m.group(0) else SITE_HEADER_HTML
    if "English</a>" in m.group(0) and "Apoyo" in m.group(0):
        header = SITE_SOCIAL_BAR_HTML + m.group(0)
    text = text[: m.start()] + header.strip() + text[m.end() :]
    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main():
    for path in ROOT.rglob("*.html"):
        if patch_file(path):
            print("patched", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
