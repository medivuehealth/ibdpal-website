"""English/Spanish hreflang mirror map from data/es-pages.json."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "es-pages.json"
SITE = "https://www.ibdpal.org"


def load_data() -> dict:
    return json.loads(DATA.read_text(encoding="utf-8"))


def es_url_for_en_path(en_path: str) -> str | None:
    rel = load_data().get("mirrors", {}).get(en_path)
    return f"{SITE}{rel}" if rel else None


def en_path_for_es_slug(slug: str) -> str | None:
    for en_path, es_rel in load_data().get("mirrors", {}).items():
        if es_rel == f"/es/{slug}":
            return en_path
    return None
