#!/usr/bin/env python3
"""Replace text logo headers with IBDPal_Logo.png across HTML pages."""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from site_nav import LOGO_SRC, SITE_HEADER_HTML, SITE_HEADER_STATIC_HTML  # noqa: E402

ICON_SNIPPET = f"""    <link rel="icon" type="image/png" href="{LOGO_SRC}">
    <link rel="apple-touch-icon" href="{LOGO_SRC}">"""

# Match legacy logo blocks (various whitespace / inline styles)
LOGO_BLOCK = re.compile(
    r"<header class=\"header\">.*?</header>",
    re.DOTALL,
)

HOME_NAV = '<a href="/" class="nav-link">Home</a>'


def patch_icons(text: str) -> str:
    if "IBDPal_Logo.png" in text and "apple-touch-icon" in text:
        return text
    if 'href="/favicon.ico"' in text and ICON_SNIPPET not in text:
        text = text.replace(
            '<link rel="icon" type="image/x-icon" href="/favicon.ico">',
            '<link rel="icon" type="image/x-icon" href="/favicon.ico">\n' + ICON_SNIPPET,
            1,
        )
    if 'href="favicon.ico"' in text and "apple-touch-icon" not in text:
        text = text.replace(
            '<link rel="icon" type="image/x-icon" href="favicon.ico">',
            '<link rel="icon" type="image/x-icon" href="favicon.ico">\n'
            '    <link rel="icon" type="image/png" href="IBDPal_Logo.png">\n'
            '    <link rel="apple-touch-icon" href="IBDPal_Logo.png">',
            1,
        )
    return text


def main():
    for path in ROOT.rglob("*.html"):
        if path.name.startswith("."):
            continue
        text = path.read_text(encoding="utf-8")
        if "logo-img" in text and "apple-touch-icon" in text:
            continue
        original = text
        m = LOGO_BLOCK.search(text)
        if m and "logo-img" not in m.group(0):
            header = SITE_HEADER_STATIC_HTML if HOME_NAV in m.group(0) else SITE_HEADER_HTML
            if "English</a>" in m.group(0):
                header = m.group(0)  # keep Spanish header structure; only patch logo div
                header = re.sub(
                    r"<div class=\"logo\">.*?</div>",
                    f"""<div class="logo">
                <a href="/" class="logo-brand" aria-label="IBDPal home">
                    <img src="{LOGO_SRC}" alt="IBDPal" class="logo-img" width="180" height="52" decoding="async">
                </a>
                <span class="tagline">Apoyo a pacientes con EII</span>
            </div>""",
                    header,
                    count=1,
                    flags=re.DOTALL,
                )
            text = text[: m.start()] + header.strip() + text[m.end() :]
        text = patch_icons(text)
        if text != original:
            path.write_text(text, encoding="utf-8")
            print("patched", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
