#!/usr/bin/env python3
"""Generate data/guide-expansions.json for all 58 patient guides."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "seo-landing-pages.json"
OUT = ROOT / "data" / "guide-expansions.json"

FOUNDATION_INTRO = (
    "Selected Crohn's & Colitis Foundation educational content and Marks are used on IBDPal under license. "
    "{body} "
    "The Foundation does not endorse IBDPal. Education only, not medical advice."
)

ALL_SLUGS = [
    "what-should-i-eat-crohns-colitis",
    "foods-to-eat-crohns-flare",
    "ulcerative-colitis-diet-foods",
    "crohns-disease-diet-nutrition",
    "low-residue-diet-ibd",
    "ibd-hydration-fluids",
    "crohns-colitis-support-groups",
    "ibd-support-near-me",
    "pediatric-crohns-colitis-help",
    "newly-diagnosed-crohns-colitis",
    "crohns-flare-what-to-do",
    "ulcerative-colitis-flare-management",
    "track-ibd-symptoms-food",
    "ibd-nutrition-tracking-app",
    "crohns-doctor-visit-prep",
    "biologics-crohns-colitis",
    "ibd-travel-planning",
    "ibd-workplace-school-rights",
    "living-with-ostomy-ibd",
    "stress-anxiety-ibd",
    "sleep-ibd-flares",
    "partner-caregiver-ibd",
    "crohns-food-triggers",
    "ibd-crohns-colitis-helpline",
    "first-gastroenterology-appointment-ibd",
    "ibd-flare-emergency-supplies",
    "dining-out-with-ibd",
    "camp-oasis-kids-ibd",
    "ibd-prior-authorization-foundation",
    "foundation-diet-nutrition-ibd",
    "anti-inflammatory-diet-ibd",
    "iron-deficiency-nutrition-ibd",
    "vitamin-d-bone-nutrition-ibd",
    "protein-healing-ibd-flare",
    "elimination-diet-when-to-stop-ibd",
    "autoimmune-nutrition-basics",
    "gluten-free-autoimmune-when",
    "what-is-ibd-foundation",
    "what-is-crohns-disease-foundation",
    "what-is-ulcerative-colitis-foundation",
    "foundation-ibd-appeal-letters",
    "step-therapy-safe-step-act-ibd",
    "find-ccf-chapter-support-group",
    "foundation-emotional-wellness-ibd",
    "newly-diagnosed-foundation-first-week",
    "pregnancy-ibd-foundation-resources",
    "youth-school-foundation-resources",
    "foundation-ibd-clinical-trials",
    "foundation-ibd-surgery-ostomy",
    "foundation-workplace-school-rights-ibd",
    "foundation-ibd-medication-guide",
    "foundation-ibd-pain-fatigue",
    "foundation-ibd-extraintestinal-manifestations",
    "foundation-complementary-medicine-ibd",
    "foundation-ibd-travel-restroom-access",
    "foundation-ibd-intimacy-sexual-health",
    "foundation-ibd-vaccines-infection",
    "foundation-ibd-colonoscopy-cancer-surveillance",
]

FOUNDATION_SLUGS = {
    "camp-oasis-kids-ibd",
    "ibd-prior-authorization-foundation",
    "foundation-diet-nutrition-ibd",
    "what-is-ibd-foundation",
    "what-is-crohns-disease-foundation",
    "what-is-ulcerative-colitis-foundation",
    "foundation-ibd-appeal-letters",
    "step-therapy-safe-step-act-ibd",
    "find-ccf-chapter-support-group",
    "foundation-emotional-wellness-ibd",
    "newly-diagnosed-foundation-first-week",
    "pregnancy-ibd-foundation-resources",
    "youth-school-foundation-resources",
    "foundation-ibd-clinical-trials",
    "foundation-ibd-surgery-ostomy",
    "foundation-workplace-school-rights-ibd",
    "foundation-ibd-medication-guide",
    "foundation-ibd-pain-fatigue",
    "foundation-ibd-extraintestinal-manifestations",
    "foundation-complementary-medicine-ibd",
    "foundation-ibd-travel-restroom-access",
    "foundation-ibd-intimacy-sexual-health",
    "foundation-ibd-vaccines-infection",
    "foundation-ibd-colonoscopy-cancer-surveillance",
}


def wc(text: str) -> int:
    return len(re.findall(r"\b[\w']+\b", text))


def page_words(exp: dict) -> int:
    parts = [exp.get("intro", "")]
    for sec in exp.get("sections", []):
        parts.append(sec.get("heading", ""))
        parts.extend(sec.get("paragraphs", []))
    parts.extend(exp.get("tips", []) or [])
    for item in exp.get("faq", []) or []:
        parts.append(item.get("q", ""))
        parts.append(item.get("a", ""))
    return wc(" ".join(parts))


def sec(h: str, p1: str, p2: str, p3: str) -> dict:
    return {"heading": h, "paragraphs": [p1, p2, p3]}


def rel(*pairs: tuple[str, str]) -> list[dict]:
    return [{"label": a, "url": b} for a, b in pairs]


def fq(q: str, a: str) -> dict:
    return {"q": q, "a": a}


def mk(intro: str, sections: list, tips: list, faq_items: list, related: list) -> dict:
    return {"intro": intro, "sections": sections, "tips": tips, "faq": faq_items, "related": related}


def fmk(body: str, sections: list, tips: list, faq_items: list, related: list) -> dict:
    return mk(FOUNDATION_INTRO.format(body=body), sections, tips, faq_items, related)


# Import full content from companion module
from guide_expansion_entries import ENTRIES  # noqa: E402


def main() -> None:
    missing = [s for s in ALL_SLUGS if s not in ENTRIES]
    if missing:
        print("Missing entries:", missing, file=sys.stderr)
        sys.exit(1)
    extra = [s for s in ENTRIES if s not in ALL_SLUGS]
    if extra:
        print("Extra entries:", extra, file=sys.stderr)
        sys.exit(1)

    for slug in ALL_SLUGS:
        exp = ENTRIES[slug]
        for key in ("intro", "sections", "tips", "faq", "related"):
            if key not in exp:
                print(f"ERROR {slug}: missing {key}", file=sys.stderr)
                sys.exit(1)
        text = json.dumps(exp)
        if "\u2014" in text or "—" in text:
            print(f"ERROR {slug}: contains em dash", file=sys.stderr)
            sys.exit(1)
        words = page_words(exp)
        if words < 750 or words > 950:
            print(f"WARN {slug}: {words} words (target 750-950)", file=sys.stderr)

    OUT.write_text(json.dumps(ENTRIES, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {OUT} ({len(ENTRIES)} guides)")
    for sample in ("crohns-flare-what-to-do", "what-should-i-eat-crohns-colitis", "what-is-ibd-foundation"):
        print(f"  {sample}: {page_words(ENTRIES[sample])} words")


if __name__ == "__main__":
    main()
