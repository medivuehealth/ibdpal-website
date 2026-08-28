#!/usr/bin/env python3
"""Measure patient guide body word counts (HTML + JSON source)."""
from __future__ import annotations

import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUIDES_DIR = ROOT / "guides"
DATA = ROOT / "data" / "seo-landing-pages.json"

# Boilerplate sections excluded from body word count
EXCLUDED_SECTION_IDS = {"related-heading", "app-cta-heading"}
EXCLUDED_CLASSES = {
    "blog-medical-review",
    "blog-edu-disclaimer",
    "community-edu-disclaimer",
    "seo-guide-keywords",
    "blog-back",
    "blog-back-link",
}


class BodyTextExtractor(HTMLParser):
    """Extract visible text from guide article, skipping boilerplate."""

    def __init__(self) -> None:
        super().__init__()
        self.in_article = False
        self.skip_depth = 0
        self.current_section_id: str | None = None
        self.current_tag: str | None = None
        self.class_stack: list[set[str]] = []
        self.chunks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = dict(attrs)
        classes = set((attr.get("class") or "").split())
        self.class_stack.append(classes)
        self.current_tag = tag

        if tag == "article" and "seo-landing" in classes:
            self.in_article = True
            return

        if not self.in_article or self.skip_depth:
            if self.in_article:
                self.skip_depth += 1
            return

        if tag == "section":
            sid = attr.get("id") or attr.get("aria-labelledby")
            self.current_section_id = sid
            if sid in EXCLUDED_SECTION_IDS:
                self.skip_depth = 1
            elif "seo-landing__faq" in classes:
                pass  # FAQ is substantive content
            return

        if classes & EXCLUDED_CLASSES:
            self.skip_depth = 1

    def handle_endtag(self, tag: str) -> None:
        if self.class_stack:
            self.class_stack.pop()
        if self.skip_depth:
            self.skip_depth -= 1
        if tag == "section":
            self.current_section_id = None
        if tag == "article":
            self.in_article = False
        self.current_tag = None

    def handle_data(self, data: str) -> None:
        if not self.in_article or self.skip_depth:
            return
        text = data.strip()
        if text:
            self.chunks.append(text)

    def body_text(self) -> str:
        return " ".join(self.chunks)


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w']+\b", text))


def json_body_word_count(page: dict) -> int:
    parts: list[str] = [page.get("intro", "")]
    for sec in page.get("sections", []):
        parts.append(sec.get("heading", ""))
        parts.extend(sec.get("paragraphs", []))
    parts.extend(page.get("tips", []) or [])
    for item in page.get("faq", []) or []:
        parts.append(item.get("q", ""))
        parts.append(item.get("a", ""))
    return word_count(" ".join(parts))


def analyze_html(path: Path) -> dict:
    html = path.read_text(encoding="utf-8")
    parser = BodyTextExtractor()
    parser.feed(html)
    text = parser.body_text()
    title_match = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.DOTALL)
    title = re.sub(r"<[^>]+>", "", title_match.group(1)) if title_match else path.stem
    title = re.sub(r"\s+", " ", title).strip()
    return {
        "slug": path.stem,
        "title": title,
        "words": word_count(text),
        "path": str(path),
    }


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    pages_by_slug = {p["slug"]: p for p in data["pages"]}

    guide_files = sorted(
        p for p in GUIDES_DIR.glob("*.html") if p.name != "index.html"
    )
    results = []
    for gf in guide_files:
        row = analyze_html(gf)
        src = pages_by_slug.get(row["slug"])
        row["json_words"] = json_body_word_count(src) if src else None
        row["category"] = src.get("category") if src else None
        row["section_count"] = len(src.get("sections", [])) if src else None
        results.append(row)

    results.sort(key=lambda r: r["words"])

    thresholds = [300, 400]
    print("=" * 72)
    print("IBDPal Patient Guide Content Length Analysis")
    print("=" * 72)
    print(f"Data source: {DATA}")
    print(f"Generator:   {ROOT / 'scripts' / 'generate_seo_landings.py'}")
    print(f"Total guides (non-index HTML): {len(results)}")
    print()

    for thresh in thresholds:
        thin = [r for r in results if r["words"] < thresh]
        print(f"--- Guides under {thresh} words (body only, excl. disclaimers/nav/footer/related/app-CTA) ---")
        print(f"Count: {len(thin)}")
        print(f"{'Words':>6}  {'JSON':>6}  {'Secs':>4}  Slug / Title")
        print("-" * 72)
        for r in thin:
            jw = r["json_words"] if r["json_words"] is not None else "-"
            sc = r["section_count"] if r["section_count"] is not None else "-"
            print(f"{r['words']:>6}  {str(jw):>6}  {str(sc):>4}  {r['slug']}")
            print(f"         {r['title'][:65]}")
            print(f"         {r['path']}")
        print()

    print("--- Full list (sorted ascending by HTML body word count) ---")
    print(f"{'Words':>6}  {'JSON':>6}  {'Secs':>4}  Category           Slug")
    print("-" * 72)
    for r in results:
        jw = r["json_words"] if r["json_words"] is not None else "-"
        sc = r["section_count"] if r["section_count"] is not None else "-"
        cat = (r["category"] or "?")[:18]
        print(f"{r['words']:>6}  {str(jw):>6}  {str(sc):>4}  {cat:<18} {r['slug']}")

    print()
    print("--- Top 5 longest guides (style reference candidates) ---")
    for r in results[-5:][::-1]:
        print(f"  {r['words']:>4} words  /guides/{r['slug']}  —  {r['title']}")


if __name__ == "__main__":
    main()
