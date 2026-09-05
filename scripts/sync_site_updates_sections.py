#!/usr/bin/env python3
"""Sync Site Updates monthly sections into index.html and site-updates.html."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from ui_snippets import UPDATES_MONTHLY_SECTIONS_HTML  # noqa: E402


def replace_updates_months(html: str) -> str:
    start = html.find('<section class="seo-landing__block updates-month">')
    if start < 0:
        raise SystemExit("updates-month start not found")
    # Prefer cutting before Stay in the loop; else after final updates-month section.
    stay = html.find('<h2>Stay in the loop</h2>', start)
    if stay >= 0:
        section_before = html.rfind('<section class="seo-landing__block">', start, stay)
        if section_before < 0:
            raise SystemExit("section before Stay in the loop not found")
        end = section_before
    else:
        # Standalone site-updates page: replace through last updates-month </section>
        end = start
        needle = '<section class="seo-landing__block updates-month">'
        pos = start
        last_close = -1
        while True:
            nxt = html.find(needle, pos)
            if nxt < 0:
                break
            close = html.find("</section>", nxt)
            if close < 0:
                break
            last_close = close + len("</section>")
            pos = close + 1
        if last_close < 0:
            raise SystemExit("could not find updates-month end")
        end = last_close
    return html[:start] + UPDATES_MONTHLY_SECTIONS_HTML.strip() + html[end:]


def main() -> None:
    index = ROOT / "index.html"
    text = index.read_text(encoding="utf-8")
    text = text.replace(
        '<h2 class="page-header-compact__title">Site Updates</h1></h2>',
        '<h2 class="page-header-compact__title">Site Updates</h2>',
    )
    text = text.replace(
        "Month-by-month changelog &middot; updated August 2026",
        "Month-by-month changelog &middot; updated September 2026",
    )
    text = text.replace(
        "Month-by-month changelog &middot; updated June 2026",
        "Month-by-month changelog &middot; updated September 2026",
    )
    marker = 'id="site-updates"'
    i = text.find(marker)
    if i < 0:
        raise SystemExit("site-updates panel missing")
    j = text.find('id="metrics"', i)
    if j < 0:
        raise SystemExit("metrics panel missing after site-updates")
    panel = text[i:j]
    panel2 = replace_updates_months(panel)
    text = text[:i] + panel2 + text[j:]
    index.write_text(text, encoding="utf-8")
    print("patched index.html")

    su = ROOT / "site-updates.html"
    st = su.read_text(encoding="utf-8")
    st = replace_updates_months(st)
    su.write_text(st, encoding="utf-8")
    print("patched site-updates.html")


if __name__ == "__main__":
    main()
