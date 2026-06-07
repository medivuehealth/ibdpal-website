#!/usr/bin/env python3
"""Replace em dashes with natural punctuation across the site.

Run after imports or generator edits that reintroduce U+2014. Site style: no em dash.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EM = "\u2014"
SKIP_DIRS = {".git", "__pycache__", "node_modules"}
EXTENSIONS = {".html", ".json", ".js", ".py", ".md", ".txt", ".css"}


def fix_text(text: str) -> str:
    if EM not in text:
        return text

    text = text.replace("Facebook: add URL", "Facebook: add URL")
    text = text.replace("YouTube: add URL", "YouTube: add URL")
    text = text.replace("<strong>IBDPal</strong> · MediVue", "<strong>IBDPal</strong> · MediVue")
    text = text.replace("education, not medical advice", "education, not medical advice")
    text = text.replace(f"Help Center{EM}for", "Help Center, for")
    text = text.replace(f"centers{EM}including", "centers, including")
    text = text.replace(f" {EM} ", " | ")
    text = re.sub(EM + r"(?=[A-Z])", ". ", text)
    text = text.replace(EM, ", ")
    return text


def main() -> None:
    changed = 0
    for path in ROOT.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix not in EXTENSIONS:
            continue
        try:
            original = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        updated = fix_text(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            print("fixed", path.relative_to(ROOT))
            changed += 1
    print(f"done: {changed} files")


if __name__ == "__main__":
    main()
