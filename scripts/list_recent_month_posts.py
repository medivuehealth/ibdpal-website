#!/usr/bin/env python3
"""List blog posts with published/display dates in the last month window."""
from __future__ import annotations

import json
import re
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
DATA = ROOT / "data"
CUTOFF = date(2026, 7, 9)  # ~1 month before 2026-08-09


def parse_iso(s: str) -> date | None:
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00")).date()
    except Exception:
        return None


def from_html(path: Path) -> date | None:
    text = path.read_text(encoding="utf-8", errors="ignore")
    m = re.search(r'"datePublished"\s*:\s*"([^"]+)"', text)
    if m:
        d = parse_iso(m.group(1))
        if d:
            return d
    m = re.search(
        r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2}),\s*(202\d)",
        text,
    )
    if m:
        try:
            return datetime.strptime(f"{m.group(1)} {m.group(2)} {m.group(3)}", "%B %d %Y").date()
        except Exception:
            return None
    return None


def from_json_files() -> dict[str, date]:
    out: dict[str, date] = {}
    for path in DATA.glob("*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        posts = data if isinstance(data, list) else data.get("posts") if isinstance(data, dict) else None
        if not isinstance(posts, list):
            continue
        for post in posts:
            if not isinstance(post, dict) or "slug" not in post:
                continue
            iso = post.get("date_iso") or post.get("datePublished") or ""
            d = parse_iso(str(iso)) if iso else None
            if d:
                out[post["slug"]] = d
    return out


def main() -> None:
    from_json = from_json_files()
    rows = []
    for path in sorted(BLOGS.glob("*.html")):
        slug = path.stem
        d = from_json.get(slug) or from_html(path)
        if d and d >= CUTOFF:
            rows.append((d.isoformat(), slug))
    for d, slug in sorted(rows):
        print(f"{d}\t{slug}")
    print(f"TOTAL\t{len(rows)}")
    (DATA / "recent-month-posts.json").write_text(
        json.dumps({"cutoff": CUTOFF.isoformat(), "slugs": [s for _, s in sorted(rows)]}, indent=2)
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
