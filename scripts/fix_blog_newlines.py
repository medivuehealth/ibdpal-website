#!/usr/bin/env python3
"""Remove accidental PowerShell `n literals from blog HTML."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BAD = "</p>`n                        <p"
GOOD = "</p>\n                        <p"

def main() -> None:
    fixed = 0
    for path in (ROOT / "blogs").glob("*.html"):
        text = path.read_text(encoding="utf-8")
        if "`n" not in text:
            continue
        path.write_text(text.replace(BAD, GOOD), encoding="utf-8")
        print(f"Fixed {path.name}")
        fixed += 1
    print(f"Done. {fixed} files updated.")


if __name__ == "__main__":
    main()
