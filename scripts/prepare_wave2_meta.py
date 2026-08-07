#!/usr/bin/env python3
"""Wave 2 nutrition guides + retag wave-1 post categories for article filters."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

WAVE1 = ROOT / "data" / "autoimmune-assoc-posts.json"
LANDINGS = ROOT / "data" / "seo-landing-pages.json"

ASSOC_SLUGS = {
    "ibd-extraintestinal-manifestations",
    "psc-ibd-liver",
    "ankylosing-spondylitis-ibd",
    "psoriasis-ibd-connection",
    "uveitis-eye-inflammation-ibd",
    "oral-canker-sores-ibd",
    "thrombosis-clot-risk-ibd",
    "osteoporosis-bone-health-ibd",
    "autoimmune-hepatitis-ibd",
}

NEW_GUIDES = [
    {
        "slug": "autoimmune-nutrition-basics",
        "category": "nutrition",
        "keywords": [
            "autoimmune nutrition",
            "autoimmune diet basics",
            "anti-inflammatory autoimmune eating",
            "autoimmune deficiency nutrition",
        ],
        "title": "Autoimmune Nutrition Basics | Realistic Starter Guide | IBDPal",
        "description": "Autoimmune nutrition basics: protect protein and calories, correct deficiencies, avoid extreme marketing diets. Education for broader autoimmune audiences.",
        "h1": "Autoimmune nutrition basics",
        "intro": "Nutrition supports energy and nutrient status in many autoimmune conditions. It does not replace disease-modifying therapy. Use this as a starter map, then personalize with your clinician or dietitian.",
        "sections": [
            {
                "heading": "Priorities that travel across diagnoses",
                "paragraphs": [
                    "Meet calorie and protein needs during flares or poor appetite.",
                    "Check and replete iron, B12, vitamin D, and other labs when ordered.",
                    "Prefer food patterns over detox products.",
                ],
            },
            {
                "heading": "When elimination is reasonable",
                "paragraphs": [
                    "Time-boxed trials with a reintroduction plan are safer than forever restriction.",
                    "Celiac disease requires a strict gluten-free diet after proper testing.",
                ],
            },
            {
                "heading": "If you also have IBD",
                "paragraphs": [
                    "Use IBD-specific flare textures and Foundation or AGA nutrition education alongside this overview.",
                    "Log meals and symptoms so GI and dietitian visits have data.",
                ],
            },
        ],
        "tips": [
            "Ask before starting specialty supplements on immunosuppression",
            "Reintroduce foods on purpose",
            "Pair with research publications for evidence context",
        ],
        "related": [
            {"label": "Autoimmune diet myths", "url": "/blog/autoimmune-diet-myths"},
            {"label": "Mediterranean-style autoimmune eating", "url": "/blog/mediterranean-diet-autoimmune"},
            {"label": "Anti-inflammatory diet IBD guide", "url": "/guides/anti-inflammatory-diet-ibd"},
            {"label": "Elimination diet timing", "url": "/guides/elimination-diet-when-to-stop-ibd"},
            {"label": "Nutrition hub", "url": "/ibd-nutrition"},
        ],
        "faq": [
            {
                "q": "Is there one autoimmune diet?",
                "a": "No. Needs differ by diagnosis, medications, surgeries, and tolerances. Marketing lists oversimplify.",
            },
            {
                "q": "Can diet put autoimmune disease in remission alone?",
                "a": "Diet can support comfort and nutrition. Disease control usually requires medical therapy guided by specialists.",
            },
        ],
    },
    {
        "slug": "gluten-free-autoimmune-when",
        "category": "nutrition",
        "keywords": [
            "gluten free autoimmune",
            "celiac vs autoimmune diet",
            "when gluten free necessary",
            "gluten autoimmune myths",
        ],
        "title": "Gluten-Free for Autoimmune Conditions: When It Applies",
        "description": "When gluten-free eating is medically required versus optional in autoimmune life. Screening-first guidance. Education only.",
        "h1": "Gluten-free eating for autoimmune conditions: when it applies",
        "intro": "Gluten-free diets are required for celiac disease. For other autoimmune diagnoses, evidence is mixed and unrestricted gluten avoidance can create nutrient gaps. Screen before long trials.",
        "sections": [
            {
                "heading": "Required vs optional",
                "paragraphs": [
                    "Celiac disease: strict gluten-free diet after confirmed diagnosis.",
                    "Non-celiac autoimmune conditions: gluten-free is not automatically evidence-based treatment.",
                ],
            },
            {
                "heading": "Screen first",
                "paragraphs": [
                    "Ask about celiac testing while still eating gluten.",
                    "If tests are negative, any trial should be time-boxed with reintroduction.",
                ],
            },
            {
                "heading": "IBD overlap",
                "paragraphs": [
                    "People with IBD have higher celiac rates than the general population, so screening questions still matter.",
                ],
            },
        ],
        "tips": [
            "Do not start lifelong gluten-free eating before testing if celiac is possible",
            "Watch fiber, iron, and B vitamins on packaged gluten-free foods",
            "Work with a dietitian for balanced swaps",
        ],
        "related": [
            {"label": "Celiac screening with IBD", "url": "/blog/celiac-ibd-screening"},
            {"label": "Gluten and wheat IBD article", "url": "/blog/gluten-wheat-ibd"},
            {"label": "Autoimmune nutrition basics", "url": "/guides/autoimmune-nutrition-basics"},
            {"label": "Elimination diet timing", "url": "/guides/elimination-diet-when-to-stop-ibd"},
        ],
        "faq": [
            {
                "q": "Should everyone with autoimmune disease go gluten-free?",
                "a": "No. Celiac disease requires it. Other conditions need individualized advice after proper evaluation.",
            },
            {
                "q": "Can I test for celiac after months gluten-free?",
                "a": "Testing is often less reliable after prolonged gluten avoidance. Ask your clinician how to proceed.",
            },
        ],
    },
]


def retag_wave1() -> None:
    posts = json.loads(WAVE1.read_text(encoding="utf-8"))
    for p in posts:
        if p["slug"] in ASSOC_SLUGS or "extraintestinal" in p["slug"] or p["slug"].startswith("psc-"):
            p["category"] = "Associations"
        else:
            p["category"] = "Autoimmune"
        # keep clinical association liver/clot as Associations already set
        if p["slug"] in {"ibd-autoimmune-overlap", "fatigue-autoimmune-ibd", "vaccine-autoimmune-immunosuppression", "celiac-ibd-screening"}:
            p["category"] = "Autoimmune"
    WAVE1.write_text(json.dumps(posts, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("retagged wave1 categories")


def append_guides() -> None:
    data = json.loads(LANDINGS.read_text(encoding="utf-8"))
    existing = {x["slug"] for x in data["pages"]}
    added = 0
    for g in NEW_GUIDES:
        if g["slug"] not in existing:
            data["pages"].append(g)
            added += 1
    LANDINGS.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"guides pages={len(data['pages'])} added={added}")


if __name__ == "__main__":
    retag_wave1()
    append_guides()
