#!/usr/bin/env python3
"""Repair U+FFFD replacement characters introduced by bad encoding round-trips."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REP = "\ufffd"


def fix_text(text: str) -> str:
    if REP not in text:
        return text

    text = text.replace(f"Crohn{REP}s", "Crohn's")
    text = text.replace(f"parents{REP} energy", "parents' energy")
    text = text.replace(f"bowel{REP}type", "bowel-type")
    text = text.replace(f"Gut{REP}Brain", "Gut-brain")
    text = re.sub(rf"(\w){REP}s\b", r"\1's", text)
    text = re.sub(rf"Hour (\d+){REP}(\d+)", r"Hour \1-\2", text)
    text = re.sub(rf"(\d+\.?\d*){REP}(\d)", r"\1-\2", text)
    text = re.sub(rf"Free to download {REP} For all ages {REP}", "Free to download · For all ages ·", text)
    text = re.sub(rf"</strong> {REP} ", r"</strong> - ", text)

    prev = None
    while prev != text:
        prev = text
        text = re.sub(rf"{REP}([^{REP}<]+?){REP}", r'"\1"', text)

    text = re.sub(rf" {REP} ", " · ", text)
    text = text.replace(REP, "'")
    return text


def main() -> int:
    dirs = [ROOT / "blogs", ROOT / "es"]
    changed = 0
    remaining = 0
    for base in dirs:
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*.html")):
            original = path.read_text(encoding="utf-8")
            if REP not in original:
                continue
            fixed = fix_text(original)
            if REP in fixed:
                remaining += fixed.count(REP)
                print(f"WARN still has {REP}: {path.relative_to(ROOT)} ({fixed.count(REP)})")
            if fixed != original:
                path.write_text(fixed, encoding="utf-8")
                changed += 1
                print(f"fixed {path.relative_to(ROOT)}")
    print(f"done: {changed} files updated, {remaining} replacement chars left")
    return 1 if remaining else 0


if __name__ == "__main__":
    sys.exit(main())
