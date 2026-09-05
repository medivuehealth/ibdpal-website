"""Chapter-aware block filters to prevent stitched mini-articles and wrong-chapter material."""

from __future__ import annotations

import re

Block = tuple[str, str | list[str] | dict]

# Headings whose detailed content belongs in Part III (Chapters 13–20) only.
DEFICIENCY_DETAIL_HEADINGS = frozenset(
    h.lower()
    for h in (
        "Micronutrients patients ask about most",
        "Why deficiencies cluster in IBD",
        "Symptoms patients notice",
        "Testing and repletion",
        "Long-term prevention",
        "Labs and timing to discuss",
        "Teens, pregnancy, and surgery",
        "Food first, supplements second",
    )
)

DEFICIENCY_DETAIL_CHAPTERS = frozenset(range(13, 21))

# Enteral / formula detail belongs in Part V (Chapters 28–31).
ENTERAL_DETAIL_HEADINGS = frozenset(
    h.lower()
    for h in (
        "Enteral feeding after surgery",
        "Tube types and delivery",
        "Formula tolerance",
        "Elemental versus polymeric",
        "Nasogastric and nasoduodenal tubes",
        "Overnight tube feeds",
        "Hospital feeding pathways",
    )
)

ENTERAL_DETAIL_CHAPTERS = frozenset(range(28, 32))

# Autoimmune overlap extras that bloat Chapter 4.
CH4_SKIP_HEADINGS = frozenset(
    h.lower()
    for h in (
        "Vaccination and infection planning",
        "Unified vaccination planning",
        "USB records and care coordination",
        "Duplicate testing and records",
        "Specialist coordination checklist",
        "Extraintestinal map",
    )
)

# ICU / research-heavy fiber content (belongs out of Ch 12 patient handbook).
RESEARCH_ICU_MARKERS = (
    "scfos",
    "scfos-en",
    "mechanically ventilated",
    "16s",
    "shotgun sequencing",
    "profound baseline dysbiosis",
    "trauma icu",
    "portal script",
    "pubmed",
    "note the intervention",
)

CHAPTER_STOP_HEADINGS: dict[int, tuple[str, ...]] = {
    5: (
        "Flare versus remission frameworks",
        "Macronutrient and micronutrient pillars",
        "Common diet patterns in practice",
        "Working with your team",
    ),
    3: (
        "Micronutrients patients ask about most",
        "Common drivers of weight loss",
        "When weight loss needs faster attention",
        "Weight gain on steroids and in remission",
        "Nutrition levers that often help",
        "Weight loss red flags",
        "Weight gain causes in IBD",
        "Enteral feeding",
        "Tube feeds",
        "Formula tolerance",
    ),
    7: (
        "What low-residue means in practice",
        "What Low-Residue Means",
        "What low-residue means",
        "Foods often included and avoided",
        "Nutrition pitfalls to avoid",
        "Transitioning back to regular eating",
    ),
    6: (
        "Understanding your diagnosis",
        "Building your care team",
        "Colonoscopy and imaging",
        "Emotional adjustment",
        "Vaccines and travel",
    ),
    8: (
        "Ultra-processed foods",
        "Turmeric and supplements",
        "Omega-3 supplements",
        "Restaurant and batch cooking",
        "Mediterranean pattern details",
        "Protein Needs During Healing",
        "Building Tolerable Plates",
        "Restaurant Protein Choices",
        "Batch Cooking for Low-Energy Weeks",
        "Meal Prep on Good Weeks",
        "Remission Day Sample",
        "How Much Protein",
    ),
    10: (
        "Why IBD flares drive fluid loss",
        "Early warning signs patients notice",
        "Oral rehydration themes to discuss with your team",
        "When dehydration becomes urgent",
        "How dehydration interacts with flares and labs",
        "Practical day plan during a high-output day",
    ),
    13: (
        "Treatment themes your team may discuss",
        "How anemia develops in IBD",
        "Diagnosis beyond hemoglobin",
        "Oral iron side effect management",
        "IV iron and transfusions",
        "When to call the clinic about anemia",
    ),
    15: (
        "Vitamin B12",
        "Vitamin D and Bone Health",
        "Other Micronutrients",
        "Supplements: Smart, Not Random",
        "Injection schedules and labs",
        "Testing and replacement basics",
    ),
    20: (
        "Approximate Macros",
        "During a Flare",
        "In Remission",
        "Prep Ideas",
        "Nutrition snapshot",
    ),
    23: (
        "Reintroduction phase importance",
        "Exiting low FODMAP safely",
        "Recording what works for your next visit",
        "Building habits that last beyond a flare",
    ),
    28: (
        "Research context: why formula composition is studied carefully",
        "How IBDPal can support the non-formula parts of care",
        "Sample week-one conversation agenda",
        "Keeping ICU research in context",
    ),
    29: (
        "Recording what works for your next visit",
        "Building habits that last beyond a flare",
        "When symptoms shift despite good habits",
    ),
    30: (
        "Recording what works for your next visit",
        "Building habits that last beyond a flare",
        "When symptoms shift despite good habits",
    ),
    31: (
        "Recording what works for your next visit",
        "Building habits that last beyond a flare",
        "When symptoms shift despite good habits",
    ),
    43: (
        "Ustekinumab and nutrition basics",
        "Injection timing and meals",
        "Subcutaneous injection site rotation",
        "Nutrition while starting ustekinumab",
    ),
    42: (
        "What intermittent fasting involves",
        "Why fasting can backfire with IBD",
        "If you are curious, discuss guardrails",
        "Evidence-based nutrition patterns",
    ),
    45: (
        "Growth monitoring in pediatric IBD",
        "School lunch strategies",
        "Growth chart reviews with parents and teens",
        "Recording what works for your next visit",
        "Building habits that last beyond a flare",
    ),
}


def _heading_text(content: str | list[str] | dict) -> str:
    return str(content).strip()


def _norm_heading(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip().rstrip(".")


# When a chapter has a manifest intro, drop the source article's duplicate opening lede.
SOURCE_LEDE_PREFIXES: dict[int, tuple[str, ...]] = {
    4: ("ibd is autoimmune-related, and nutrition affects energy",),
    11: ("adequate protein supports tissue repair",),
    15: ("iron deficiency and anemia are common in ibd",),
    16: ("vitamin d, calcium, and bone health deserve attention",),
    17: ("crohn's disease involving the terminal ileum or prior ileal resection raises",),
    20: ("iron deficiency and anemia are common in ibd because",),
    23: ("search traffic around fodmap",),
    27: ("many people with crohn's disease or ulcerative colitis search whether they must avoid all dairy",),
    28: ("people searching enteral",),
    30: ("searches for elemental formula ibd",),
    39: ("these sample days illustrate gentle combinations only",),
    41: ("probiotics for crohn's disease and probiotics for ulcerative colitis",),
    42: ("collagen powders are sold as gut lining repair",),
    43: ("prednisone can turn appetite into a freight train",),
    44: ("restaurant meals can be enjoyable with ibd when you plan ahead",),
    45: ("parents often search teen crohn's nutrition",),
    46: ("many people with crohn's disease or ulcerative colitis have healthy pregnancies",),
    47: ("tolerance with crohn's or ulcerative colitis is individual",),
    48: ("some people with ibd live with a temporary or permanent ostomy",),
    49: ("symptom and food tracking helps you and your gi team",),
    50: ("prepared gi visits lead to better questions",),
    51: ("complete this worksheet after reading the book",),
}

GENERIC_SOURCE_LEDE_RE = re.compile(
    r"^this (?:chapter|guide|page) (?:covers|summarizes|explains|states|describes)\b",
    re.I,
)


def _is_duplicate_source_lede(chapter_num: int, text: str, *, has_intro: bool) -> bool:
    lower = text.lower().strip()
    if not lower:
        return False
    prefixes = SOURCE_LEDE_PREFIXES.get(chapter_num, ())
    if any(lower.startswith(prefix) for prefix in prefixes):
        return True
    if has_intro and chapter_num >= 16 and GENERIC_SOURCE_LEDE_RE.match(lower):
        return True
    return False


def drop_duplicate_source_lede(
    chapter_num: int,
    blocks: list[Block],
    *,
    has_intro: bool = False,
) -> list[Block]:
    if not has_intro and chapter_num not in SOURCE_LEDE_PREFIXES:
        return blocks
    out: list[Block] = []
    dropped = False
    for kind, content in blocks:
        if not dropped and kind == "paragraph" and isinstance(content, str):
            if _is_duplicate_source_lede(chapter_num, content, has_intro=has_intro):
                dropped = True
                continue
        out.append((kind, content))
    return out


CHAPTER_SKIP_SECTIONS: dict[int, frozenset[str]] = {
    4: frozenset(
        _norm_heading(h)
        for h in (
            "Building Evidence-Based Eating Habits",
        )
    ),
    17: frozenset(
        _norm_heading(h)
        for h in (
            "Iron and Anemia",
            "Vitamin D and Bone Health",
            "Other Micronutrients",
            "Supplements: Smart, Not Random",
            "Testing and replacement basics",
            "Food and supplement coordination",
            "When to involve hematology",
            "Food-first strategies when tolerated",
        )
    ),
    22: frozenset(
        _norm_heading(h)
        for h in (
            'What "Low-Residue" Means in Everyday Life',
            "What “Low-Residue” Means in Everyday Life",
            "What low-residue means in everyday life",
        )
    ),
    27: frozenset(
        _norm_heading(h)
        for h in (
            "Get celiac ruled out before long gluten-free trials",
            "Gluten-free is not automatically anti-inflammatory",
            "Wheat vs gluten",
            "Practical steps",
            "Lactose Intolerance versus IBD Inflammation",
            "Gluten and Celiac Screening",
            "Celiac screening before elimination",
            "Calcium tracking on low-dairy diets",
        )
    ),
    41: frozenset(
        _norm_heading(h)
        for h in (
            "What research shows",
            "Talking with your GI team",
            "Reading labels and evidence tiers",
            "Coordination with biologics and antibiotics",
        )
    ),
    48: frozenset(
        _norm_heading(h)
        for h in (
            "What J-pouch surgery accomplishes",
            "Pouch function years after takedown",
        )
    ),
    42: frozenset(
        _norm_heading(h)
        for h in (
            "What collagen marketing claims",
            "Nutrition priorities that come first",
            "Safety considerations with IBD",
            "When a trial might be reasonable",
        )
    ),
}


PART_III_STACK_HEADINGS = frozenset(
    _norm_heading(h)
    for h in (
        "Micronutrients patients ask about most",
        "Why deficiencies cluster in IBD",
        "Symptoms patients notice",
        "Testing and repletion",
        "Long-term prevention",
        "Labs and timing to discuss",
        "Teens, pregnancy, and surgery",
        "Food first, supplements second",
    )
)


class GlobalDeficiencyStackTracker:
    """Drop repeated micronutrient-article sections after the first in Part III."""

    def __init__(self) -> None:
        self.seen: set[str] = set()

    def should_skip_section(self, heading: str) -> bool:
        key = _norm_heading(heading)
        if key not in PART_III_STACK_HEADINGS:
            return False
        if key in self.seen:
            return True
        self.seen.add(key)
        return False


def truncate_at_headings(blocks: list[Block], stop_headings: tuple[str, ...]) -> list[Block]:
    """Drop this heading and everything after it."""
    if not stop_headings:
        return blocks
    stop = {_norm_heading(h) for h in stop_headings}
    out: list[Block] = []
    for kind, content in blocks:
        if kind.startswith("heading_") and _norm_heading(_heading_text(content)) in stop:
            break
        out.append((kind, content))
    return out


def _skip_section_for_chapter(ch_num: int, heading: str) -> bool:
    key = _norm_heading(heading)
    if key in DEFICIENCY_DETAIL_HEADINGS and ch_num not in DEFICIENCY_DETAIL_CHAPTERS:
        return True
    if key in ENTERAL_DETAIL_HEADINGS and ch_num not in ENTERAL_DETAIL_CHAPTERS:
        return True
    if ch_num == 4 and key in CH4_SKIP_HEADINGS:
        return True
    return False


class ChapterBlockFilter:
    """Skip wrong-chapter sections and research-heavy paragraphs."""

    def __init__(
        self,
        chapter_num: int,
        *,
        deficiency_stack: GlobalDeficiencyStackTracker | None = None,
    ) -> None:
        self.chapter_num = chapter_num
        self.deficiency_stack = deficiency_stack
        self.skip_until_heading = False
        self.food_mode = 32 <= chapter_num <= 38

    def filter_blocks(self, blocks: list[Block]) -> list[Block]:
        from book_prose_cleanup import heading_starts_skip_section

        blocks = truncate_at_headings(blocks, CHAPTER_STOP_HEADINGS.get(self.chapter_num, ()))
        out: list[Block] = []
        for kind, content in blocks:
            if kind.startswith("heading_"):
                text = _heading_text(content)
                if heading_starts_skip_section(text, food_mode=self.food_mode):
                    self.skip_until_heading = True
                    continue
                if _norm_heading(text) in CHAPTER_SKIP_SECTIONS.get(self.chapter_num, frozenset()):
                    self.skip_until_heading = True
                    continue
                if (
                    self.deficiency_stack
                    and self.chapter_num in DEFICIENCY_DETAIL_CHAPTERS
                    and self.deficiency_stack.should_skip_section(text)
                ):
                    self.skip_until_heading = True
                    continue
                if _skip_section_for_chapter(self.chapter_num, text):
                    self.skip_until_heading = True
                    continue
                self.skip_until_heading = False
                out.append((kind, content))
            elif self.skip_until_heading:
                continue
            elif kind == "paragraph" and self.chapter_num == 12:
                lower = str(content).lower()
                if any(m in lower for m in RESEARCH_ICU_MARKERS):
                    continue
                if len(lower) > 400 and ("trial" in lower or "randomized" in lower):
                    continue
                out.append((kind, content))
            else:
                out.append((kind, content))
        return out


def filter_blocks_for_chapter(
    chapter_num: int,
    blocks: list[Block],
    *,
    deficiency_stack: GlobalDeficiencyStackTracker | None = None,
    drop_lede: bool = False,
    has_intro: bool = False,
) -> list[Block]:
    if drop_lede:
        blocks = drop_duplicate_source_lede(chapter_num, blocks, has_intro=has_intro)
    return ChapterBlockFilter(chapter_num, deficiency_stack=deficiency_stack).filter_blocks(blocks)
