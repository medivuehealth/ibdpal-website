#!/usr/bin/env python3
"""Audit rel=amphtml links against on-disk AMP pages and hub routes."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
AMP_PAT = re.compile(r'rel="amphtml" href="([^"]+)"')


def main() -> int:
    blog_amp = {p.stem for p in (ROOT / "blogs" / "amp").glob("*.html")}
    guide_amp = {p.stem for p in (ROOT / "guides" / "amp").glob("*.html")}
    blog_html = {p.stem for p in (ROOT / "blogs").glob("*.html")}
    guide_html = {p.stem for p in (ROOT / "guides").glob("*.html")}

    issues: list[str] = []
    hub_links: list[str] = []
    amp_links = 0

    for html in sorted(ROOT.rglob("*.html")):
        if "node_modules" in html.parts:
            continue
        if len(html.parts) >= 2 and html.parts[-2] == "amp":
            continue
        text = html.read_text(encoding="utf-8")
        for m in AMP_PAT.finditer(text):
            amp_links += 1
            url = m.group(1)
            path = urlparse(url).path.rstrip("/")
            rel = html.relative_to(ROOT).as_posix()

            if re.fullmatch(r"/(guides|blog|support|library)/amp", path):
                hub_links.append(f"{rel} -> {url}")
                continue

            if path.startswith("/blog/") and path.endswith("/amp"):
                slug = path[len("/blog/") : -len("/amp")]
                if slug not in blog_amp:
                    issues.append(f"MISSING AMP FILE: {rel} -> {url}")
            elif path.startswith("/guides/") and path.endswith("/amp"):
                slug = path[len("/guides/") : -len("/amp")]
                if slug not in guide_amp:
                    issues.append(f"MISSING AMP FILE: {rel} -> {url}")
            else:
                issues.append(f"UNKNOWN PATTERN: {rel} -> {url}")

    for slug in sorted(blog_html - {"index"} - blog_amp):
        if slug in blog_amp:
            continue
        p = ROOT / "blogs" / f"{slug}.html"
        if p.exists() and 'rel="amphtml"' in p.read_text(encoding="utf-8"):
            issues.append(f"AMPHTML BUT NO FILE: blogs/{slug}.html")

    blogs_no_amphtml = []
    for slug in sorted(blog_html - {"index"}):
        p = ROOT / "blogs" / f"{slug}.html"
        t = p.read_text(encoding="utf-8")
        if slug in blog_amp and 'rel="amphtml"' not in t:
            blogs_no_amphtml.append(slug)

    print(f"amphtml links scanned: {amp_links}")
    print(f"blog AMP files: {len(blog_amp)}, blog pages: {len(blog_html - {'index'})}")
    print(f"guide AMP files: {len(guide_amp)}, guide pages: {len(guide_html - {'index'})}")

    if hub_links:
        print("\nHub-style amphtml (should be empty after fix):")
        for line in hub_links:
            print(" ", line)

    if issues:
        print("\nBroken amphtml links:")
        for line in issues:
            print(" ", line)

    if blogs_no_amphtml:
        print(f"\nBlogs with AMP file but missing amphtml link ({len(blogs_no_amphtml)}):")
        for slug in blogs_no_amphtml[:20]:
            print(" ", slug)
        if len(blogs_no_amphtml) > 20:
            print(f"  ... and {len(blogs_no_amphtml) - 20} more")

    orphan_blog_amp = sorted(blog_amp - blog_html)
    if orphan_blog_amp:
        print(f"\nOrphan blog AMP files ({len(orphan_blog_amp)}):")
        for slug in orphan_blog_amp[:10]:
            print(" ", slug)

    return 1 if (issues or hub_links) else 0


if __name__ == "__main__":
    sys.exit(main())
