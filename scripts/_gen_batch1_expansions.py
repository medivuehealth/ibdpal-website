"""Generate blog-expansions-batch1.json for the 75 thinnest blog posts."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from blog_expansion_utils import html_word_count
from _batch1_extra_sections import EXTRA_SECTIONS
from _batch1_topics_data import TOPIC_REGISTRY

ROOT = Path(__file__).resolve().parents[1]
TSV_PATH = ROOT / "scripts" / "_thin_blogs.tsv"
OUT_PATH = ROOT / "data" / "blog-expansions-batch1.json"
TARGET_TOTAL = 800

# Additional sections added only when base content is below the append word target.
CLOSING_SECTION_POOL: list[tuple[str, list[str]]] = [
    (
        "Recording what works for your next visit",
        [
            "Keep a brief symptom and lifestyle log for one to two weeks before appointments. Note sleep, stress, meals, and bowel patterns so your clinician sees trends instead of a single bad day.",
            "List medications, supplements, and missed doses honestly. Small adherence gaps help your GI team adjust plans faster than guessing.",
            "Bring one prioritized question from this article so limited visit time addresses what matters most to you right now.",
        ],
    ),
    (
        "Building habits that last beyond a flare",
        [
            "Choose one practical step from this guide to practice this week rather than changing everything at once. Sustainable habits outperform short strict phases for most IBD patients.",
            "Pair new habits with existing routines, such as taking evening meds when you brush teeth, so they survive busy school or work weeks.",
            "Revisit your plan after travel, holidays, or medication changes because tolerance and priorities shift over time.",
        ],
    ),
    (
        "Coordinating care across your health team",
        [
            "Ask your gastroenterologist whether dietitian, mental health, physical therapy, or social work referrals would help the issues raised here.",
            "Share updates from other specialists at GI visits so drug interactions and overlapping symptoms are reviewed in one place.",
            "Use your patient portal to upload outside lab results and hospital records before appointments when possible.",
        ],
    ),
    (
        "Planning ahead when life gets busy",
        [
            "Pack medications, snacks, and a small symptom kit before exams, trips, or overtime weeks when routines slip first.",
            "Identify backup clinicians or infusion centers near work, campus, or relatives in case flares occur away from home.",
            "Discuss preventive plans with your clinician before predictable stress seasons such as finals, tax season, or postpartum return to work.",
        ],
    ),
    (
        "When symptoms shift despite good habits",
        [
            "Return to your GI team if new bleeding, fever, weight loss, or pain appears even when you follow general lifestyle guidance.",
            "Labs and stool markers sometimes change before you feel improvement, and sometimes lag behind symptoms. Your clinician interprets both together.",
            "Do not assume setbacks mean personal failure. Inflammatory bowel disease activity fluctuates and often responds to timely medical adjustment.",
        ],
    ),
]


def build(sections: list[tuple[str, list[str]]], faqs: list[tuple[str, str]]) -> str:
    parts: list[str] = []
    for title, paragraphs in sections:
        parts.append(f"<h2>{title}</h2>")
        for p in paragraphs:
            parts.append(f"<p>{p}</p>")
    parts.append("<h2>Common questions</h2>")
    for question, answer in faqs:
        parts.append(f"<h3>{question}</h3>")
        parts.append(f"<p>{answer}</p>")
    return "\n".join(parts)


def pad_to_target(html: str, target: int, extras: list[str]) -> str:
    """Insert unique filler paragraphs before Common questions if still under target."""
    if not extras:
        return html
    marker = "<h2>Common questions</h2>"
    if marker not in html:
        return html
    head, tail = html.split(marker, 1)
    used: set[str] = set()
    current = html_word_count(head)
    insertions: list[str] = []
    for extra in extras:
        if current >= target:
            break
        if extra in used:
            continue
        used.add(extra)
        insertions.append(f"<p>{extra}</p>")
        current = html_word_count(head + "\n" + "\n".join(insertions))
    if insertions:
        head = head.rstrip() + "\n" + "\n".join(insertions) + "\n"
    return head + marker + tail


def read_thin_slugs(limit: int = 75) -> list[tuple[str, int]]:
    """Return first `limit` unique slugs sorted by ascending word count."""
    seen: dict[str, int] = {}
    text = TSV_PATH.read_text(encoding="utf-8-sig")
    for line in text.strip().splitlines():
        slug, wc_str, *_ = line.split("\t")
        wc = int(wc_str)
        if slug not in seen:
            seen[slug] = wc
    ranked = sorted(seen.items(), key=lambda item: item[1])
    return ranked[:limit]


def make_append(slug: str, current_words: int) -> str:
    if slug not in TOPIC_REGISTRY:
        raise KeyError(f"Missing topic content for slug: {slug}")
    if slug not in EXTRA_SECTIONS:
        raise KeyError(f"Missing extra sections for slug: {slug}")
    topic = TOPIC_REGISTRY[slug]
    sections = list(topic["sections"]) + list(EXTRA_SECTIONS[slug])
    append_target = TARGET_TOTAL - current_words
    html = build(sections, topic["faqs"])
    shortfall = append_target - html_word_count(html)
    if shortfall > 20:
        start = sum(ord(c) for c in slug) % len(CLOSING_SECTION_POOL)
        added = 0
        while shortfall > 25 and added < len(CLOSING_SECTION_POOL):
            sections.append(CLOSING_SECTION_POOL[(start + added) % len(CLOSING_SECTION_POOL)])
            added += 1
            html = build(sections, topic["faqs"])
            shortfall = append_target - html_word_count(html)
    return pad_to_target(html, append_target, list(topic.get("extras", [])))


def assert_no_em_dash(text: str, slug: str) -> None:
    if "\u2014" in text or "—" in text:
        raise ValueError(f"Em dash found in expansion for {slug}")


def main() -> None:
    slugs = read_thin_slugs(75)
    slug_set = {s for s, _ in slugs}
    missing = slug_set - set(TOPIC_REGISTRY)
    extra = set(TOPIC_REGISTRY) - slug_set
    if missing:
        print(f"ERROR: missing content for {len(missing)} slugs:", sorted(missing), file=sys.stderr)
        sys.exit(1)
    if extra:
        print(f"WARNING: unused topic entries: {sorted(extra)}", file=sys.stderr)

    output: dict[str, dict[str, str]] = {}
    append_counts: list[int] = []

    for slug, current_wc in slugs:
        append_body = make_append(slug, current_wc)
        assert_no_em_dash(append_body, slug)
        output[slug] = {"append_body": append_body}
        append_counts.append(html_word_count(append_body))

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    first_slug = slugs[0][0]
    first_current = slugs[0][1]
    first_append = append_counts[0]
    print(f"Wrote {OUT_PATH}")
    print(f"Slug count: {len(output)}")
    print(f"Append words min/max/mean: {min(append_counts)}/{max(append_counts)}/{sum(append_counts)/len(append_counts):.1f}")
    print(f"Sample ({first_slug}): current={first_current}, append={first_append}, projected_total={first_current + first_append}")
    print(f"crohns-flare-what-to-do in batch: {'crohns-flare-what-to-do' in output}")


if __name__ == "__main__":
    main()
