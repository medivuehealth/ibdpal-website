#!/usr/bin/env python3
"""Refresh site header + tab nav from site_nav.py (3-layer chrome)."""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from site_nav import (  # noqa: E402
    SITE_HEADER_HTML,
    TAB_NAV_HTML,
    TAB_NAV_HOME_HTML,
    site_header_html,
)

SOCIAL_BLOCK = re.compile(r"<div class=\"site-social-bar\".*?</div>\s*", re.DOTALL)
HEADER_BLOCK = re.compile(
    r"(?:<div class=\"site-social-bar\".*?</div>\s*)?<header class=\"header\">.*?</header>",
    re.DOTALL,
)
TAB_BLOCK = re.compile(
    r'<nav class="tab-navigation"[^>]*>.*?</nav>',
    re.DOTALL,
)


def tab_nav_for(path: Path) -> str:
    if path.name == "index.html":
        return TAB_NAV_HOME_HTML.strip()
    nav = TAB_NAV_HTML
    if path.parent.name == "blogs":
        nav = nav.replace(
            'class="tab-button" data-tab="blogs"',
            'class="tab-button active" data-tab="blogs"',
            1,
        )
    return nav.strip()


def header_for(path: Path) -> str:
    if path.name == "recursos.html" and path.parent.name == "es":
        return site_header_html(tagline="Apoyo a pacientes con EII").strip()
    return SITE_HEADER_HTML.strip()


def patch_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    text = SOCIAL_BLOCK.sub("", text)
    hm = HEADER_BLOCK.search(text)
    if hm:
        text = text[: hm.start()] + header_for(path) + text[hm.end() :]
    tm = TAB_BLOCK.search(text)
    if tm:
        text = text[: tm.start()] + tab_nav_for(path) + text[tm.end() :]
    text = re.sub(r"<div class=\"app-container\">\s*</div>\s*", '<div class="app-container">\n', text)
    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main():
    for path in sorted(ROOT.rglob("*.html")):
        if patch_file(path):
            print("patched", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
