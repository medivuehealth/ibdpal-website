#!/usr/bin/env python3
"""Assign every blog slug to at least one SEO hub in data/seo-expansion.json."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
SEO = ROOT / "data" / "seo-expansion.json"

HUB_ROUTES: list[tuple[re.Pattern[str], list[str]]] = [
    (re.compile(r"enteral|prebiotic|formula|parenteral|hospital-feeding|dysbiosis|gut-barrier|nutrition|diet|fodmap|fiber|protein|dairy|gluten|hydration|electrolyte|weight|micronutrient|probiotic|mediterranean|anti-inflammatory|vitamin|iron|zinc|magnesium|potassium|banana|rice|chicken|beef|egg|fish|tofu|bread|pasta|potato|tomato|apple|berry|melon|soup|tea|coffee|honey|oat|yogurt|cheese|milk|dal|tortilla|chapati|couscous|plantain|congee|miso|paneer|kimchi|dates|turkey|tuna|salmon|shrimp|zucchini|broccoli|carrot|spinach|avocado|almond|nut|seed|bone-broth|collagen|carnivore|juice|fasting|detox|cleanse|residue|meal|food|eat|low-cal|high-cal|sweet-potato|white-rice|white-bread|low-residue|dining-out|complete-ibd-nutrition", re.I), ["ibd-nutrition"]),
    (re.compile(r"stool|bristol|calprotectin|crp|mucus|diarrhea|constipation|calprotectin|labs|caliber|floating|pencil|pale|yellow|green|black|blood-in-stool", re.I), ["stool-labs-decoder"]),
    (re.compile(r"crohn|perianal|ostomy|j-pouch|stricture|fistula|ankylosing|extraintestinal|psc|pyoderma|uveitis|psoriasis|autoimmune|lupus|rheumatoid|hashimoto|sjogren|sclerosis|diabetes|celiac|overlap|hepatitis|thrombosis|osteoporosis", re.I), ["crohns-disease"]),
    (re.compile(r"colitis|uc-|ulcerative|mesalamine|5-asa|j-pouch", re.I), ["ulcerative-colitis"]),
    (re.compile(r"flare|fever|dehydration|vomiting|obstruction|er-visit|blood-in-stool|urgency|red-flag|when-to-call|when-to-go|steroid|prednisone|remicade|humira|stelara|skyrizi|rinvoq|entyvio|biologic|infusion|immunosuppress|methotrexate|insurance|prior-auth", re.I), ["flare-help"]),
    (re.compile(r"teen|school|college|dating|work|intimacy|bathroom-urgency|icn-|sibling|caregiver|partner|pediatric|high-school|social-life", re.I), ["teens-and-school"]),
    (re.compile(r"travel|swimming|pool|beach|heat|summer|humid", re.I), ["ibd-nutrition", "teens-and-school"]),
    (re.compile(r"stress|anxiety|depression|sleep|mental|emotional|fatigue|brain-fog", re.I), ["flare-help", "ulcerative-colitis"]),
]


def hubs_for_slug(slug: str) -> list[str]:
    found: list[str] = []
    for pattern, hubs in HUB_ROUTES:
        if pattern.search(slug):
            for h in hubs:
                if h not in found:
                    found.append(h)
    return found or ["ibd-nutrition"]


def main() -> None:
    seo = json.loads(SEO.read_text(encoding="utf-8"))
    hubs = seo.get("hubs", [])
    hub_by_slug = {h["slug"]: h for h in hubs}

    assigned: set[str] = set()
    for hub in hubs:
        for slug in hub.get("blog_slugs", []):
            assigned.add(slug)

    all_slugs = sorted(p.stem for p in BLOGS.glob("*.html"))
    added = 0
    for slug in all_slugs:
        if slug in assigned:
            continue
        for hub_slug in hubs_for_slug(slug):
            hub = hub_by_slug[hub_slug]
            slugs = hub.setdefault("blog_slugs", [])
            if slug not in slugs:
                slugs.append(slug)
                added += 1
        assigned.add(slug)

    SEO.write_text(json.dumps(seo, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Assigned {added} hub memberships; {len(all_slugs)} blogs total")


if __name__ == "__main__":
    main()
