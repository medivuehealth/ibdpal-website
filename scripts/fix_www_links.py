#!/usr/bin/env python3
"""Point all https://ibdpal.org URLs to https://www.ibdpal.org (avoids apex SSL errors)."""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APEX = re.compile(r"https://ibdpal\.org(?=[/#\"'])")
WWW = "https://www.ibdpal.org"
GLOBS = ("*.html", "*.json", "*.py", "*.js", "*.txt", "*.xml")
EXTRA = ("llms.txt", "sitemap.xml", "robots.txt")


def patch_text(text: str) -> str:
    return APEX.sub(WWW, text)


def main() -> None:
    count = 0
    for pattern in GLOBS:
        for path in ROOT.rglob(pattern):
            if path.is_relative_to(ROOT / "scripts" / "__pycache__"):
                continue
            if path.name == "fix_www_links.py":
                continue
            try:
                orig = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            new = patch_text(orig)
            if new != orig:
                path.write_text(new, encoding="utf-8")
                print(path.relative_to(ROOT))
                count += 1
    for name in EXTRA:
        path = ROOT / name
        if not path.is_file():
            continue
        try:
            orig = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        new = patch_text(orig)
        if new != orig:
            path.write_text(new, encoding="utf-8")
            print(path.relative_to(ROOT))
            count += 1
    print(f"Done. {count} files updated.")


if __name__ == "__main__":
    main()
