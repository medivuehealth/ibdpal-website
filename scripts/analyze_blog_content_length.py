#!/usr/bin/env python3
"""Measure blog body word counts (HTML), excluding site chrome and boilerplate."""
from __future__ import annotations

import html as html_mod
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS_DIR = ROOT / "blogs"

EXCLUDED_CLASSES = {
    "blog-medical-review",
    "blog-edu-disclaimer",
    "blog-figure-grid",
    "blog-photo-credit",
    "icn-attribution",
}

RELATED_PREFIXES = ("related reading:", "related:")


class BlogBodyExtractor(HTMLParser):
    """Extract visible text from div.blog-content, skipping boilerplate."""

    def __init__(self) -> None:
        super().__init__()
        self.in_content = False
        self.content_depth = 0
        self.skip_depth = 0
        self.pending_skip_heading = False
        self.chunks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = dict(attrs)
        classes = set((attr.get("class") or "").split())

        if tag == "div" and "blog-content" in classes:
            self.in_content = True
            self.content_depth = 1
            return

        if not self.in_content:
            return

        if self.content_depth:
            self.content_depth += 1

        if self.skip_depth:
            return

        if classes & EXCLUDED_CLASSES:
            self.skip_depth = 1
            return

        if tag == "h2" and attr.get("id", "").startswith("related-"):
            self.skip_depth = 1

    def handle_endtag(self, tag: str) -> None:
        if not self.in_content:
            return

        if self.skip_depth:
            self.skip_depth -= 1

        if self.content_depth:
            self.content_depth -= 1
            if self.content_depth == 0:
                self.in_content = False

    def handle_data(self, data: str) -> None:
        if not self.in_content or self.skip_depth:
            return

        text = data.strip()
        if not text:
            return

        lower = text.lower()
        if lower.startswith(RELATED_PREFIXES):
            return

        if text == "Medical Disclaimer":
            self.pending_skip_heading = True
            return

        if self.pending_skip_heading:
            self.pending_skip_heading = False
            return

        self.chunks.append(text)

    def body_text(self) -> str:
        return " ".join(self.chunks)


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w']+\b", text))


def analyze_html(path: Path) -> dict:
    html = path.read_text(encoding="utf-8")
    parser = BlogBodyExtractor()
    parser.feed(html)
    text = parser.body_text()
    title_match = re.search(
        r'<h1[^>]*class="blog-title"[^>]*>(.*?)</h1>', html, re.DOTALL
    )
    raw_title = title_match.group(1) if title_match else path.stem
    title = re.sub(r"\s+", " ", html_mod.unescape(re.sub(r"<[^>]+>", "", raw_title))).strip()
    return {
        "slug": path.stem,
        "title": title,
        "words": word_count(text),
        "path": str(path),
    }


def fmt_row(row: dict) -> str:
    return f"{row['slug']}\t{row['words']}\t{row['title']}\t{row['path']}"


def main() -> None:
    rows = [analyze_html(p) for p in sorted(BLOGS_DIR.glob("*.html"))]
    rows.sort(key=lambda r: r["words"])

    under_400 = [r for r in rows if r["words"] < 400]
    under_600 = [r for r in rows if r["words"] < 600]

    print(f"TOTAL_BLOGS={len(rows)}")
    print(f"UNDER_400={len(under_400)}")
    print(f"UNDER_600={len(under_600)}")
    print()
    print("=== TOP 10 THINNEST ===")
    for row in rows[:10]:
        print(fmt_row(row))
    print()
    print("=== ALL UNDER 400 WORDS ===")
    for row in under_400:
        print(fmt_row(row))
    print()
    print("=== ALL UNDER 600 WORDS (400-599) ===")
    for row in under_600:
        if row["words"] >= 400:
            print(fmt_row(row))
    print()
    print("=== TOP 10 LONGEST (style reference) ===")
    for row in reversed(rows[-10:]):
        print(fmt_row(row))


if __name__ == "__main__":
    main()
