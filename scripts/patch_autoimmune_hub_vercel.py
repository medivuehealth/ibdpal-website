#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "vercel.json"
text = path.read_text(encoding="utf-8")
needle = '"/ibd-autoimmune-associations"'
if needle in text:
    print("rewrite already present")
else:
    insert = (
        '    {\n'
        '      "source": "/ibd-autoimmune-associations",\n'
        '      "destination": "/ibd-autoimmune-associations.html"\n'
        '    },\n'
    )
    text = text.replace('"rewrites": [\n', '"rewrites": [\n' + insert)
    path.write_text(text, encoding="utf-8")
    print("added rewrite")
