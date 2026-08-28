#!/usr/bin/env python3
"""Merge blog-expansions-batch*.json into data/blog-expansions.json."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = DATA / "blog-expansions.json"
BATCHES = [
    DATA / "blog-expansions-batch1.json",
    DATA / "blog-expansions-batch2.json",
    DATA / "blog-expansions-batch3.json",
]


def main() -> None:
    merged: dict = {}
    for path in BATCHES:
        if not path.is_file():
            raise SystemExit(f"Missing {path}")
        chunk = json.loads(path.read_text(encoding="utf-8"))
        added = 0
        for slug, entry in chunk.items():
            if slug not in merged:
                merged[slug] = entry
                added += 1
        print(f"  +{added} new from {path.name} ({len(chunk)} in file)")

    OUT.write_text(json.dumps(merged, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(merged)} expansions to {OUT}")


if __name__ == "__main__":
    main()
