#!/usr/bin/env python3
"""Patch blog HTML files with append_body from data/blog-expansions.json."""
from __future__ import annotations

import re
from pathlib import Path

from blog_expansion_utils import html_word_count, load_expansions, merge_blog_body, strip_trailing_related

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"

FIGURE_GRID = re.compile(
    r'(\s*<div class="blog-figure-grid[^"]*".*?</div>\s*'
    r'(?:<p class="blog-photo-credit">.*?</p>\s*)?)',
    re.S,
)


def extract_body(html: str) -> tuple[str, str, str]:
    """Return prefix, core prose (disclaimer through body), suffix after body."""
    start = html.find('<div class="blog-content">')
    if start == -1:
        raise ValueError("no blog-content")
    after_open = start + len('<div class="blog-content">')
    end = html.find("</div>", after_open)
    # find closing div for blog-content: before related section
    related_idx = html.find('class="seo-related-reading"', after_open)
    if related_idx == -1:
        related_idx = html.find("</div>", after_open)
    # walk back to closing </div> of blog-content
    chunk = html[after_open:]
    depth = 1
    pos = 0
    while pos < len(chunk) and depth:
        next_open = chunk.find("<div", pos)
        next_close = chunk.find("</div>", pos)
        if next_close == -1:
            break
        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open + 4
        else:
            depth -= 1
            pos = next_close + 6
            if depth == 0:
                body_inner = chunk[:next_close]
                suffix_start = after_open + next_close
                return html[:after_open], body_inner, html[suffix_start:]
    raise ValueError("could not parse blog-content")


def patch_file(path: Path, expansions: dict) -> bool:
    slug = path.stem
    entry = expansions.get(slug)
    if not entry:
        return False

    html = path.read_text(encoding="utf-8")
    prefix, inner, suffix = extract_body(html)

    # Strip disclaimers and figure grid from inner for merge; reattach after
    disclaimers = ""
    for cls in ("blog-medical-review", "blog-edu-disclaimer"):
        m = re.search(rf'(<p class="{cls}">.*?</p>\s*)', inner, re.S)
        if m:
            disclaimers += m.group(1)
            inner = inner.replace(m.group(1), "", 1)

    fig = ""
    fm = FIGURE_GRID.search(inner)
    if fm:
        fig = fm.group(1)
        inner = inner.replace(fig, "", 1)

    medical = ""
    mm = re.search(r'(<h2>Medical Disclaimer</h2>\s*<p>.*?</p>\s*)', inner, re.S)
    if mm:
        medical = mm.group(1)
        inner = inner.replace(medical, "", 1)

    icn = ""
    im = re.search(r'(<div class="icn-attribution">.*?</div>\s*)', inner, re.S)
    if im:
        icn = im.group(1)
        inner = inner.replace(icn, "", 1)

    core = inner.strip()
    merged_core = merge_blog_body(core, slug, expansions).strip()
    if "<!-- blog-expansion-applied -->" in core:
        return False

    before_words = html_word_count(core)
    if before_words >= 650:
        return False

    merged_core = merged_core + "\n<!-- blog-expansion-applied -->"
    after_words = html_word_count(merged_core)
    if after_words <= before_words + 50:
        return False

    new_inner = f"\n{disclaimers}{merged_core}\n{fig}{icn}{medical}"
    path.write_text(prefix + new_inner + suffix, encoding="utf-8")
    print(f"  patched {slug}: {before_words} -> {after_words} words")
    return True


def main() -> None:
    expansions = load_expansions()
    patched = 0
    for path in sorted(BLOGS.glob("*.html")):
        if patch_file(path, expansions):
            patched += 1
    print(f"Patched {patched} blog files")


if __name__ == "__main__":
    main()
