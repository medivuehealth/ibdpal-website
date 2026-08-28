#!/usr/bin/env python3
"""Regenerate all blog HTML from source generators."""
from __future__ import annotations

import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

GENERATORS = [
    "generate_blog_posts",
    "generate_patient_blogs",
    "generate_seo_blogs",
    "generate_seo_wellness_blogs",
    "generate_ibd_topic_blogs",
    "generate_icn_blogs",
    "generate_june_family_blogs",
    "generate_wave1_food_nutrition_blogs",
    "generate_wave2_food_nutrition_blogs",
    "generate_wave3_food_nutrition_blogs",
    "generate_wave4_food_nutrition_blogs",
    "generate_mara_gut_nutrition_blogs",
    "generate_eureka_top5_blogs",
    "generate_enteral_nutrition_blog",
    "generate_enteral_supplement_blogs",
    "generate_flare_symptoms_blog",
    "generate_autoimmune_assoc_blogs",
    "generate_wave2_autoimmune_blogs",
    "generate_analytics_gap_blogs",
    "generate_july_2026_gap_blogs",
    "generate_vercel_page_gap_blogs",
    "generate_vercel_aug2026_traffic_blogs",
    "generate_search_gap_blog",
    "generate_tier3_blogs",
    "generate_microbiome_probiotic_blogs",
]


def main() -> None:
    for name in GENERATORS:
        mod = importlib.import_module(name)
        if hasattr(mod, "main"):
            print(f"Running {name}.main()...")
            mod.main()
        else:
            print(f"SKIP {name} (no main)")


if __name__ == "__main__":
    main()
