#!/usr/bin/env python3
"""Point EN mirror page language controls at their paired /es/ URLs."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def en_file(en_path: str) -> Path | None:
    if en_path == "/":
        return ROOT / "index.html"
    slug = en_path.lstrip("/")
    candidates = [
        ROOT / f"{slug}.html",
        ROOT / "blogs" / f"{slug.split('/')[-1]}.html",
    ]
    for path in candidates:
        if path.is_file():
            return path
    return None


def main() -> None:
    data = json.loads((ROOT / "data" / "locale-mirrors.json").read_text(encoding="utf-8"))
    needle = 'href="/es/recursos" class="site-lang__link" data-lang="es"'
    for en, es in (data.get("mirrors") or {}).items():
        path = en_file(en)
        if not path:
            print("missing", en)
            continue
        text = path.read_text(encoding="utf-8")
        repl = f'href="{es}" class="site-lang__link" data-lang="es"'
        if needle not in text:
            print("skip", path.relative_to(ROOT))
            continue
        path.write_text(text.replace(needle, repl), encoding="utf-8")
        print("updated", path.relative_to(ROOT), "->", es)


if __name__ == "__main__":
    main()
