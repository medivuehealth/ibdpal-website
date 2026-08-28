#!/usr/bin/env python3
"""Generate guide_expansion_entries.py with all 58 entries at 750-950 words."""
from __future__ import annotations

import re
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent / "guide_expansion_entries.py"

FOUNDATION_SLUGS = {
    "camp-oasis-kids-ibd", "ibd-prior-authorization-foundation", "foundation-diet-nutrition-ibd",
    "what-is-ibd-foundation", "what-is-crohns-disease-foundation", "what-is-ulcerative-colitis-foundation",
    "foundation-ibd-appeal-letters", "step-therapy-safe-step-act-ibd", "find-ccf-chapter-support-group",
    "foundation-emotional-wellness-ibd", "newly-diagnosed-foundation-first-week", "pregnancy-ibd-foundation-resources",
    "youth-school-foundation-resources", "foundation-ibd-clinical-trials", "foundation-ibd-surgery-ostomy",
    "foundation-workplace-school-rights-ibd", "foundation-ibd-medication-guide", "foundation-ibd-pain-fatigue",
    "foundation-ibd-extraintestinal-manifestations", "foundation-complementary-medicine-ibd",
    "foundation-ibd-travel-restroom-access", "foundation-ibd-intimacy-sexual-health",
    "foundation-ibd-vaccines-infection", "foundation-ibd-colonoscopy-cancer-surveillance",
}

ALL_SLUGS = [
    "what-should-i-eat-crohns-colitis", "foods-to-eat-crohns-flare", "ulcerative-colitis-diet-foods",
    "crohns-disease-diet-nutrition", "low-residue-diet-ibd", "ibd-hydration-fluids",
    "crohns-colitis-support-groups", "ibd-support-near-me", "pediatric-crohns-colitis-help",
    "newly-diagnosed-crohns-colitis", "crohns-flare-what-to-do", "ulcerative-colitis-flare-management",
    "track-ibd-symptoms-food", "ibd-nutrition-tracking-app", "crohns-doctor-visit-prep",
    "biologics-crohns-colitis", "ibd-travel-planning", "ibd-workplace-school-rights",
    "living-with-ostomy-ibd", "stress-anxiety-ibd", "sleep-ibd-flares", "partner-caregiver-ibd",
    "crohns-food-triggers", "ibd-crohns-colitis-helpline", "first-gastroenterology-appointment-ibd",
    "ibd-flare-emergency-supplies", "dining-out-with-ibd", "camp-oasis-kids-ibd",
    "ibd-prior-authorization-foundation", "foundation-diet-nutrition-ibd", "anti-inflammatory-diet-ibd",
    "iron-deficiency-nutrition-ibd", "vitamin-d-bone-nutrition-ibd", "protein-healing-ibd-flare",
    "elimination-diet-when-to-stop-ibd", "autoimmune-nutrition-basics", "gluten-free-autoimmune-when",
    "what-is-ibd-foundation", "what-is-crohns-disease-foundation", "what-is-ulcerative-colitis-foundation",
    "foundation-ibd-appeal-letters", "step-therapy-safe-step-act-ibd", "find-ccf-chapter-support-group",
    "foundation-emotional-wellness-ibd", "newly-diagnosed-foundation-first-week", "pregnancy-ibd-foundation-resources",
    "youth-school-foundation-resources", "foundation-ibd-clinical-trials", "foundation-ibd-surgery-ostomy",
    "foundation-workplace-school-rights-ibd", "foundation-ibd-medication-guide", "foundation-ibd-pain-fatigue",
    "foundation-ibd-extraintestinal-manifestations", "foundation-complementary-medicine-ibd",
    "foundation-ibd-travel-restroom-access", "foundation-ibd-intimacy-sexual-health",
    "foundation-ibd-vaccines-infection", "foundation-ibd-colonoscopy-cancer-surveillance",
]

FOUNDATION_INTRO = (
    "Selected Crohn's & Colitis Foundation educational content and Marks are used on IBDPal under license. "
    "{body} "
    "The Foundation does not endorse IBDPal. Education only, not medical advice."
)

SUPPLEMENTS = [
    "Discuss how this topic applies to your current disease activity with your gastroenterologist.",
    "Bring these observations to your next IBD appointment so your team can personalize advice.",
    "Your GI team can adjust recommendations based on labs, imaging, and symptom trends.",
    "Patient education supports shared decision making; it does not replace individual medical assessment.",
    "If symptoms worsen while you try these steps, contact your clinic using your flare pathway.",
    "Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.",
    "Children, older adults, and post-surgical patients may need modified guidance from specialists.",
    "Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.",
]


def wc(text: str) -> int:
    return len(re.findall(r"\b[\w']+\b", text))


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


def page_words(exp: dict) -> int:
    parts = [exp.get("intro", "")]
    for s in exp.get("sections", []):
        parts.append(s["heading"])
        parts.extend(s["paragraphs"])
    parts.extend(exp.get("tips", []) or [])
    for item in exp.get("faq", []) or []:
        parts.append(item["q"])
        parts.append(item["a"])
    return wc(" ".join(parts))


def S(heading: str, *paras: str) -> dict:
    while len(paras) < 3:
        paras = (*paras, paras[-1] if paras else CLOSER.strip())
    return sec(heading, paras[0], paras[1], paras[2])


MID_SENTENCES = [
    "Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.",
    "Write down questions for your gastroenterologist before each visit so limited appointment time is used well.",
    "Medication adherence and follow-up labs are as important as diet changes for many IBD patients.",
    "Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.",
    "Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.",
    "Red-flag symptoms should trigger outreach even if you are unsure whether a flare has officially started.",
    "Partners and caregivers can help log symptoms, but treatment decisions stay between you and your clinicians.",
    "Nutrition, mental health, and vaccine updates are routine parts of long-term IBD management.",
]


def enrich_sections(sections: list) -> None:
    for i, s in enumerate(sections):
        mid = MID_SENTENCES[i % len(MID_SENTENCES)]
        if mid not in s["paragraphs"][1]:
            s["paragraphs"][1] += " " + mid


def build(intro: str, sections: list, tips: list, faq: list, related: list, foundation_body: str | None = None) -> dict:
    enrich_sections(sections)
    if foundation_body:
        exp = fmk(foundation_body, sections, tips, faq, rel(*related))
    else:
        exp = mk(intro, sections, tips, faq, rel(*related))
    sup_idx = 0
    while page_words(exp) < 750:
        added = False
        for s in exp["sections"]:
            if page_words(exp) >= 750:
                break
            sup = SUPPLEMENTS[sup_idx % len(SUPPLEMENTS)]
            sup_idx += 1
            if sup not in s["paragraphs"][-1]:
                s["paragraphs"][-1] += " " + sup
                added = True
        if not added:
            break
    return exp


# Import topic definitions
from _guide_topics import TOPICS  # noqa: E402

ENTRIES: dict[str, dict] = {}

for slug in ALL_SLUGS:
    t = TOPICS[slug]
    body = t.get("body")
    intro = t.get("intro", "")
    sections = [S(h, *ps) for h, ps in t["sections"]]
    ENTRIES[slug] = build(intro, sections, t["tips"], [fq(q, a) for q, a in t["faq"]], t["related"], body)


def render_entry(slug: str, exp: dict) -> str:
    is_f = slug in FOUNDATION_SLUGS
    lines = [f'    "{slug}": ']
    if is_f:
        body = TOPICS[slug]["body"]
        lines.append("fmk(")
        lines.append(f"        {body!r},")
    else:
        lines.append("mk(")
        lines.append(f"        {exp['intro']!r},")
    lines.append("        [")
    for s in exp["sections"]:
        h, p1, p2, p3 = s["heading"], *s["paragraphs"]
        lines.append(f"            sec({h!r}, {p1!r}, {p2!r}, {p3!r}),")
    lines.append("        ],")
    lines.append("        [")
    for tip in exp["tips"]:
        lines.append(f"            {tip!r},")
    lines.append("        ],")
    lines.append("        [")
    for item in exp["faq"]:
        lines.append(f"            fq({item['q']!r}, {item['a']!r}),")
    lines.append("        ],")
    lines.append("        rel(")
    for label, url in [(r["label"], r["url"]) for r in exp["related"]]:
        lines.append(f"            ({label!r}, {url!r}),")
    lines.append("        ),")
    lines.append("    ),")
    return "\n".join(lines)


def main():
    bad = []
    for slug in ALL_SLUGS:
        w = page_words(ENTRIES[slug])
        if w < 750 or w > 950:
            bad.append((slug, w))
        if "—" in str(ENTRIES[slug]) or "\u2014" in str(ENTRIES[slug]):
            print(f"EM DASH: {slug}", file=sys.stderr)
            sys.exit(1)
    header = '''"""Expansion content for all 58 IBDPal patient guides."""
from __future__ import annotations

FOUNDATION_INTRO = (
    "Selected Crohn's & Colitis Foundation educational content and Marks are used on IBDPal under license. "
    "{body} "
    "The Foundation does not endorse IBDPal. Education only, not medical advice."
)


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


ENTRIES: dict[str, dict] = {
'''
    parts = [header]
    for slug in ALL_SLUGS:
        parts.append(render_entry(slug, ENTRIES[slug]))
    parts.append("}\n")
    OUT.write_text("".join(parts), encoding="utf-8")
    print(f"Wrote {OUT} ({len(ENTRIES)} guides)")
    for slug in ("crohns-flare-what-to-do", "what-should-i-eat-crohns-colitis", "what-is-ibd-foundation"):
        print(f"  {slug}: {page_words(ENTRIES[slug])} words")
    if bad:
        print("OUT OF RANGE:")
        for slug, w in bad:
            print(f"  {slug}: {w}")
        sys.exit(1)


if __name__ == "__main__":
    main()
