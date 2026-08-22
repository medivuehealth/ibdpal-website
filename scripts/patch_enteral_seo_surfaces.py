#!/usr/bin/env python3
"""Patch search aliases, resource keywords, and SEO hub slugs for enteral/gut posts."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NEW_ALIASES = {
    "pen": "enteral",
    "partial enteral nutrition": "enteral",
    "partial formula": "enteral",
    "sip feeds": "enteral",
    "tube feed": "enteral",
    "ng tube": "enteral",
    "nasogastric": "enteral",
    "tpn": "parenteral",
    "parenteral": "parenteral",
    "parenteral nutrition": "parenteral",
    "iv nutrition": "parenteral",
    "hospital feeding": "parenteral",
    "npo": "parenteral",
    "prebiotic formula": "prebiotic",
    "prebiotics": "prebiotic",
    "scfose": "prebiotic",
    "scfos": "prebiotic",
    "fructooligosaccharides": "prebiotic",
    "formula fiber": "prebiotic",
    "dysbiosis": "dysbiosis",
    "leaky gut": "dysbiosis",
    "gut barrier": "dysbiosis",
    "intestinal barrier": "dysbiosis",
    "microbiome imbalance": "dysbiosis",
}

KEYWORD_MAP = {
    "enteral-nutrition-ibd": [
        "enteral",
        "entereal",
        "een",
        "exclusive enteral nutrition",
        "enteral nutrition",
        "formula feeding",
        "tube feeding",
        "tube feed",
        "nasogastric",
        "NG tube",
        "PEN",
        "partial enteral",
        "partial enteral nutrition",
        "sip feeds",
        "polymeric formula",
        "elemental formula",
        "Modulen",
        "Peptamen",
        "nutrition",
        "formula feeds",
    ],
    "fiber-prebiotics-enteral-feeds-microbiome": [
        "prebiotic",
        "prebiotics",
        "scFOS",
        "fructooligosaccharides",
        "formula fiber",
        "fiber formula",
        "enteral fiber",
        "tube feed fiber",
        "dysbiosis",
        "microbiome formula",
        "prebiotic formula",
        "enteral",
        "nutrition",
    ],
    "exclusive-vs-partial-enteral-nutrition-crohns": [
        "EEN",
        "PEN",
        "exclusive enteral",
        "partial enteral",
        "partial enteral nutrition",
        "exclusive vs partial",
        "Crohn formula",
        "Crohn's EEN",
        "enteral",
        "entereal",
        "tube feeding",
        "nutrition",
    ],
    "gut-barrier-dysbiosis-inflammation-ibd": [
        "dysbiosis",
        "leaky gut",
        "gut barrier",
        "intestinal barrier",
        "microbiome",
        "gut microbiome",
        "inflammation",
        "barrier function",
        "microbial imbalance",
        "nutrition",
    ],
    "hospital-feeding-ibd-enteral-parenteral": [
        "hospital feeding",
        "parenteral",
        "TPN",
        "PN",
        "IV nutrition",
        "NPO",
        "tube feeds",
        "enteral",
        "post surgery nutrition",
        "after surgery diet",
        "hospital diet IBD",
        "nutrition",
    ],
    "elemental-vs-polymeric-formula-ibd": [
        "elemental formula",
        "polymeric formula",
        "semi-elemental",
        "peptide formula",
        "amino acid formula",
        "Modulen",
        "Peptamen",
        "formula types IBD",
        "enteral",
        "EEN",
        "nutrition",
    ],
    "food-reintroduction-after-een-ibd": [
        "food reintroduction",
        "after EEN",
        "reintroduce food Crohn's",
        "EEN diet transition",
        "formula to food",
        "enteral",
        "EEN",
        "nutrition",
    ],
    "taste-fatigue-enteral-formula-ibd": [
        "taste fatigue",
        "formula taste",
        "EEN taste",
        "sip feed nausea",
        "formula flavor",
        "enteral",
        "nutrition",
    ],
    "nasogastric-tube-feeds-ibd-practical": [
        "NG tube",
        "nasogastric",
        "overnight feeds",
        "tube feeding IBD",
        "pump feeds",
        "enteral",
        "EEN",
        "nutrition",
    ],
    "adult-een-crohns-what-to-expect": [
        "adult EEN",
        "EEN adults",
        "exclusive enteral adult Crohn's",
        "adult formula induction",
        "enteral",
        "EEN",
        "Crohn's",
        "nutrition",
    ],
    "enteral-nutrition-after-ibd-surgery": [
        "after surgery formula",
        "post op enteral",
        "tube feeds after resection",
        "formula after ileostomy",
        "post surgery nutrition IBD",
        "enteral",
        "nutrition",
    ],
}

HUB_INSERTS = {
    "ibd-nutrition": [
        "enteral-nutrition-ibd",
        "exclusive-vs-partial-enteral-nutrition-crohns",
        "fiber-prebiotics-enteral-feeds-microbiome",
        "elemental-vs-polymeric-formula-ibd",
        "food-reintroduction-after-een-ibd",
        "taste-fatigue-enteral-formula-ibd",
        "nasogastric-tube-feeds-ibd-practical",
        "adult-een-crohns-what-to-expect",
        "enteral-nutrition-after-ibd-surgery",
        "gut-barrier-dysbiosis-inflammation-ibd",
        "hospital-feeding-ibd-enteral-parenteral",
    ],
    "crohns-disease": [
        "enteral-nutrition-ibd",
        "exclusive-vs-partial-enteral-nutrition-crohns",
        "adult-een-crohns-what-to-expect",
        "elemental-vs-polymeric-formula-ibd",
        "food-reintroduction-after-een-ibd",
    ],
    "flare-help": [
        "hospital-feeding-ibd-enteral-parenteral",
        "enteral-nutrition-ibd",
        "enteral-nutrition-after-ibd-surgery",
    ],
}

HUB_KEYWORDS = {
    "ibd-nutrition": [
        "enteral nutrition",
        "EEN",
        "exclusive enteral nutrition",
        "tube feeding IBD",
        "IBD diet",
        "crohn's nutrition",
        "ulcerative colitis diet",
        "what to eat IBD",
    ],
}


def main() -> None:
    aliases_path = ROOT / "data" / "search-aliases.json"
    aliases = json.loads(aliases_path.read_text(encoding="utf-8"))
    added_a = 0
    for k, v in NEW_ALIASES.items():
        if k not in aliases:
            aliases[k] = v
            added_a += 1
    aliases_path.write_text(json.dumps(aliases, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"search-aliases: +{added_a} keys ({len(aliases)} total)")

    kw_path = ROOT / "data" / "ibd-resource-keywords.json"
    keywords = json.loads(kw_path.read_text(encoding="utf-8"))
    for slug, words in KEYWORD_MAP.items():
        keywords[slug] = words
    kw_path.write_text(json.dumps(keywords, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"ibd-resource-keywords: updated {len(KEYWORD_MAP)} slugs")

    seo_path = ROOT / "data" / "seo-expansion.json"
    seo = json.loads(seo_path.read_text(encoding="utf-8"))
    for hub in seo.get("hubs", []):
        slug = hub.get("slug")
        if slug in HUB_KEYWORDS:
            # Keep unique order: new keywords first, then existing
            seen = []
            for w in HUB_KEYWORDS[slug] + hub.get("keywords", []):
                if w not in seen:
                    seen.append(w)
            hub["keywords"] = seen
        if slug in HUB_INSERTS:
            blogs = hub.setdefault("blog_slugs", [])
            for b in reversed(HUB_INSERTS[slug]):
                if b in blogs:
                    blogs.remove(b)
                blogs.insert(0, b)
            print(f"hub {slug}: blog_slugs leading with enteral cluster")
    # Hub description nudge for nutrition
    for hub in seo.get("hubs", []):
        if hub.get("slug") == "ibd-nutrition":
            hub["description"] = (
                "Nutrition and diet resources for Crohn's disease and ulcerative colitis: "
                "enteral nutrition and EEN, flare foods, FODMAP, hydration, protein, and patient guides."
            )
            hub["intro"] = (
                "Guides and articles on Crohn's and colitis nutrition, including formula feeds and "
                "enteral nutrition, to explore with your care team."
            )
    seo_path.write_text(json.dumps(seo, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("seo-expansion.json updated")


if __name__ == "__main__":
    main()
