#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
bad = 'class="tab-button" class="tab-button active"'
good = 'class="tab-button active"'
for p in (ROOT / "blogs").glob("*.html"):
    t = p.read_text(encoding="utf-8")
    if bad in t:
        p.write_text(t.replace(bad, good), encoding="utf-8")
        print("fixed", p.name)
