"""Shared helpers for blog body expansion and word counts."""
from __future__ import annotations

import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPANSIONS_PATH = ROOT / "data" / "blog-expansions.json"

STRIP_TAIL_PATTERNS = (
    re.compile(r"<p>\s*Related:.*?</p>\s*$", re.I | re.S),
    re.compile(r"<p>\s*Related reading:.*?</p>\s*$", re.I | re.S),
)


class VisibleTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.chunks: list[str] = []

    def handle_data(self, data: str) -> None:
        text = data.strip()
        if text:
            self.chunks.append(text)


def html_word_count(fragment: str) -> int:
    parser = VisibleTextParser()
    parser.feed(fragment)
    return len(re.findall(r"\b[\w']+\b", " ".join(parser.chunks)))


def load_expansions() -> dict:
    if not EXPANSIONS_PATH.is_file():
        return {}
    return json.loads(EXPANSIONS_PATH.read_text(encoding="utf-8"))


def strip_trailing_related(body: str) -> tuple[str, str]:
    """Return (body_without_tail, trailing_related_html)."""
    for pattern in STRIP_TAIL_PATTERNS:
        match = pattern.search(body.rstrip())
        if match:
            return body[: match.start()].rstrip(), match.group(0)
    return body.rstrip(), ""


def merge_blog_body(body: str, slug: str, expansions: dict | None = None) -> str:
    if "<!-- blog-expansion-applied -->" in body:
        return body
    expansions = expansions if expansions is not None else load_expansions()
    entry = expansions.get(slug)
    if not entry:
        return body

    if entry.get("replace_body"):
        return entry["replace_body"].strip()

    append = (entry.get("append_body") or "").strip()
    if not append:
        return body

    core, related_tail = strip_trailing_related(body)
    merged = f"{core}\n\n{append}"
    if related_tail:
        merged = f"{merged}\n\n{related_tail}"
    merged = merged.strip() + "\n<!-- blog-expansion-applied -->"
    return merged
