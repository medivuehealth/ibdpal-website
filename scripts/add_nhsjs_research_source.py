#!/usr/bin/env python3
import json
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "data" / "research-sources.json"
data = json.loads(p.read_text(encoding="utf-8"))
entry = {
    "id": "nhsjs-stem-cell-crohns-2025",
    "title": "Stem Cell Therapeutics for Crohn's Disease",
    "publisher": "National High School Journal of Science (NHSJS)",
    "year": "2025",
    "url": "https://nhsjs.com/2025/stem-cell-therapeutics-for-crohns-disease/",
    "topics": [
        "Crohn's disease",
        "stem cells",
        "regenerative medicine",
        "IBD therapeutics",
        "student research",
    ],
    "summary": (
        "NHSJS review of stem cell therapeutics for Crohn's disease: immune modulation, "
        "tissue repair themes, clinical-trial context, limitations, and future directions. "
        "Linked for education; not medical advice."
    ),
    "license_note": "External journal article. Link and summarize; respect NHSJS copyright for full text.",
    "shelf": "publications",
}
ids = {s["id"] for s in data["sources"]}
if entry["id"] not in ids:
    data["sources"].insert(0, entry)
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("added research source")
else:
    print("already present")
