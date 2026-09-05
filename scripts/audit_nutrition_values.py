#!/usr/bin/env python3
"""Audit DRI baselines and food-composition tables against NIH DRI reference strings."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRI_JSON = ROOT / "data" / "nutrition-dri-baselines.json"
FOOD_JSON = ROOT / "data" / "nutrition-food-sources.json"

# Canonical adult NIH DRI strings used in the book (19–50 unless noted).
NIH_BASELINES: dict[str, dict[str, str]] = {
    "female-19-50": {
        "Protein": "46 g/day (RDA)",
        "Fiber": "25 g/day (AI)",
        "Vitamin D": "600 IU / 15 mcg (RDA)",
        "Vitamin B12": "2.4 mcg/day (RDA)",
        "Iron": "18 mg/day (RDA)",
        "Folate (DFE)": "400 mcg/day (RDA)",
        "Calcium": "1,000 mg/day (RDA)",
        "Zinc": "8 mg/day (RDA)",
        "Omega-3 (ALA)": "1.1 g/day (AI)",
    },
    "male-19-50": {
        "Protein": "56 g/day (RDA)",
        "Fiber": "38 g/day (AI)",
        "Vitamin D": "600 IU / 15 mcg (RDA)",
        "Vitamin B12": "2.4 mcg/day (RDA)",
        "Iron": "8 mg/day (RDA)",
        "Folate (DFE)": "400 mcg/day (RDA)",
        "Calcium": "1,000 mg/day (RDA)",
        "Zinc": "11 mg/day (RDA)",
        "Omega-3 (ALA)": "1.6 g/day (AI)",
    },
}

FOOD_DRI_KEYS = {
    "iron": ("driAdultFemale", "18 mg/day (RDA, menstruating adults)"),
    "vitamin-b12": ("driAdultFemale", "2.4 mcg/day (RDA)"),
    "vitamin-d": ("driAdultFemale", "600 IU / 15 mcg (RDA); 800 IU after 70"),
    "calcium": ("driAdultFemale", "1,000 mg/day (RDA); 1,200 mg for women 51+"),
    "folate": ("driAdultFemale", "400 mcg/day (RDA)"),
    "zinc": ("driAdultFemale", "8 mg/day (RDA)"),
}


def audit_dri_profiles(dri: dict) -> list[str]:
    errors: list[str] = []
    for profile in dri.get("profiles", []):
        pid = profile.get("id", "")
        expected = NIH_BASELINES.get(pid)
        if not expected:
            continue
        rows = {r["nutrient"]: r.get("baseline", "") for r in profile.get("macros", []) + profile.get("micros", [])}
        for nutrient, baseline in expected.items():
            actual = rows.get(nutrient, "")
            if actual != baseline:
                errors.append(f"DRI profile {pid}: {nutrient} expected '{baseline}', got '{actual}'")
            if rows.get(nutrient) and not profile.get("macros") and nutrient in rows:
                pass
        for row in profile.get("macros", []) + profile.get("micros", []):
            if not row.get("source"):
                errors.append(f"DRI {pid} {row.get('nutrient')}: missing source tag")
    return errors


def audit_food_sources(food: dict) -> list[str]:
    errors: list[str] = []
    for nutrient in food.get("nutrients", []):
        nid = nutrient.get("id", "")
        if nid in FOOD_DRI_KEYS:
            key, expected = FOOD_DRI_KEYS[nid]
            actual = nutrient.get(key, "")
            if expected not in actual and actual != expected:
                errors.append(f"Food source {nid}: {key}='{actual}' (expected contains '{expected}')")
        for food_row in nutrient.get("foods", []):
            amount = str(food_row.get("amount", ""))
            if amount and not re.search(r"\d", amount):
                errors.append(f"Food source {nid}: non-numeric amount '{amount}' for {food_row.get('food')}")
            if amount.lower() == "varies" or "varies" in amount.lower():
                if "brand" not in str(food_row.get("food", "")).lower():
                    errors.append(f"Food source {nid}: vague amount '{amount}' for {food_row.get('food')}")
    return errors


def main() -> int:
    dri = json.loads(DRI_JSON.read_text(encoding="utf-8"))
    food = json.loads(FOOD_JSON.read_text(encoding="utf-8"))
    errors = audit_dri_profiles(dri) + audit_food_sources(food)
    if errors:
        print("Nutrition value audit FAILED:")
        for err in errors:
            print(f"  - {err}")
        return 1
    print("Nutrition value audit: OK (DRI profiles + food source reference strings)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
