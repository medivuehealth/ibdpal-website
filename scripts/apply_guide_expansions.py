#!/usr/bin/env python3
"""Merge guide-expansions.json into data/seo-landing-pages.json."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "seo-landing-pages.json"
EXPANSIONS = ROOT / "data" / "guide-expansions.json"
MIN_WORDS = 750


def word_count(page: dict) -> int:
    parts: list[str] = [page.get("intro", "")]
    for sec in page.get("sections", []):
        parts.append(sec.get("heading", ""))
        parts.extend(sec.get("paragraphs", []))
    parts.extend(page.get("tips", []) or [])
    for item in page.get("faq", []) or []:
        parts.append(item.get("q", ""))
        parts.append(item.get("a", ""))
    return len(re.findall(r"\b[\w']+\b", " ".join(parts)))


def merge_page(page: dict, expansion: dict) -> dict:
    out = dict(page)
    for key in ("intro", "sections", "tips", "faq", "related", "description"):
        if key in expansion and expansion[key]:
            out[key] = expansion[key]
    return out


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    expansions = json.loads(EXPANSIONS.read_text(encoding="utf-8"))
    by_slug = {p["slug"]: p for p in data["pages"]}
    missing = [s for s in expansions if s not in by_slug]
    if missing:
        print("ERROR: expansion slugs not in seo-landing-pages.json:", missing, file=sys.stderr)
        sys.exit(1)

    updated = 0
    for slug, expansion in expansions.items():
        page = by_slug[slug]
        before = word_count(page)
        merged = merge_page(page, expansion)
        after = word_count(merged)
        if after < MIN_WORDS:
            print(f"WARN {slug}: only {after} words after merge (target {MIN_WORDS}+)", file=sys.stderr)
        by_slug[slug] = merged
        updated += 1
        print(f"  {slug}: {before} -> {after} words")

    data["pages"] = [by_slug[p["slug"]] for p in data["pages"]]
    DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\nUpdated {updated} guides in {DATA}")


if __name__ == "__main__":
    main()
