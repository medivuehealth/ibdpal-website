"""Global deduplication and merged-chapter compilation."""

from __future__ import annotations

import re
from typing import Any

from book_citations import GLOBAL_SINGLE_USE_SOURCES
from book_chapter_filters import filter_blocks_for_chapter

REPEAT_HEADING_SKIP = {
    "medical disclaimer",
    "questions for your gastroenterologist or dietitian",
    "when food questions become urgent",
    "how to track",
    "related reading",
    "related resources",
    "start with goals, not perfection",
    "common myths",
    "nutrition snapshot",
    "frequently asked questions",
    "faq",
    "building habits that last beyond a flare",
    "coordinating care across your health team",
    "planning ahead when life gets busy",
    "when symptoms shift despite good habits",
    "recording what works for your next visit",
}

ARTICLE_TITLE_HEADING = re.compile(
    r"(complete ibd nutrition|newly diagnosed with|and IBD:.*tips|and IBD:.*fiber)",
    re.I,
)

SEO_OPENING_SKIP = (
    "searches like",
    "this pillar page maps",
    "points you to deeper",
)


from book_prose_cleanup import GlobalRepeatTracker, filter_chapter_sections, heading_starts_skip_section, norm_heading, should_drop_list_item, should_drop_paragraph

GLOBAL_BOILERPLATE_PREFIXES = (
    "discuss how this topic applies",
    "patient education supports shared decision",
    "logging patterns in",
    "keeping a notebook or diary helps",
    "your gi team can adjust recommendations",
    "second opinions are reasonable",
    "if symptoms worsen while you try these steps",
    "bring these observations to your next ibd appointment",
    "children, older adults, and post-surgical patients",
    "write down questions for your gastroenterologist",
    "symptom patterns tracked over several days",
    "medication adherence and follow-up labs",
    "tell your team about travel, work stress",
    "bring prior colonoscopy, imaging",
)


class GlobalBoilerplateTracker:
    """Drop repeated web-import boilerplate after first occurrence in the manuscript."""

    def __init__(self) -> None:
        self.seen: set[str] = set()

    def is_repeat(self, text: str) -> bool:
        lower = text.lower().strip()
        if not any(lower.startswith(p) for p in GLOBAL_BOILERPLATE_PREFIXES):
            return False
        key = lower[:100]
        if key in self.seen:
            return True
        self.seen.add(key)
        return False


class GlobalDeduper:
    """Tracks single-use sources across the manuscript."""

    def __init__(self) -> None:
        self.sources_used: set[str] = set()

    def should_skip_source(self, src: str, *, allow_reuse: bool = False) -> bool:
        if allow_reuse:
            return False
        if src in GLOBAL_SINGLE_USE_SOURCES and src in self.sources_used:
            return True
        return False

    def mark_source_used(self, src: str) -> None:
        self.sources_used.add(src)


class ChapterDeduper:
    """Per-chapter paragraph deduplication when merging multiple sources."""

    def __init__(self) -> None:
        self.paragraphs: set[str] = set()

    def fingerprint(self, text: str) -> str:
        norm = re.sub(r"\s+", " ", text.lower()).strip()
        return norm[:160]

    def seen_paragraph(self, text: str) -> bool:
        key = self.fingerprint(text)
        if key in self.paragraphs:
            return True
        self.paragraphs.add(key)
        return False


def is_food_reference_chapter(chapter: dict) -> bool:
    return chapter.get("part") == 6 and 32 <= chapter.get("num", 0) <= 38


def should_skip_heading(text: str, *, food_mode: bool = False) -> bool:
    from book_prose_cleanup import (
        heading_starts_skip_section,
        is_food_article_structure_heading,
        is_seo_residue_heading,
        norm_heading,
    )

    if food_mode and is_food_article_structure_heading(text):
        return False
    if heading_starts_skip_section(text, food_mode=food_mode):
        return True
    lower = norm_heading(text)
    if not food_mode and lower in REPEAT_HEADING_SKIP:
        return True
    if food_mode and lower in {
        "medical disclaimer",
        "related reading",
        "related resources",
        "how to track",
        "questions for your gastroenterologist or dietitian",
        "when food questions become urgent",
    }:
        return True
    if is_seo_residue_heading(text) and not (
        food_mode and is_food_article_structure_heading(text)
    ):
        return True
    if food_mode and lower.startswith("how to track"):
        return True
    if ARTICLE_TITLE_HEADING.search(text):
        return True
    return False


def filter_blocks_for_merge(
    blocks: list[tuple[str, str | list[str] | dict]],
    deduper: ChapterDeduper,
    *,
    food_mode: bool = False,
    global_boilerplate: GlobalBoilerplateTracker | None = None,
    global_repeat: GlobalRepeatTracker | None = None,
) -> list[tuple[str, str | list[str] | dict]]:
    out: list[tuple[str, str | list[str] | dict]] = []
    skip_section = False
    for kind, content in blocks:
        if kind.startswith("heading_"):
            text = str(content)
            if heading_starts_skip_section(text, food_mode=food_mode) or (
                not food_mode and norm_heading(text) in REPEAT_HEADING_SKIP
            ):
                skip_section = True
                continue
            skip_section = False
            if should_skip_heading(text, food_mode=food_mode):
                continue
            out.append((kind, content))
        elif skip_section:
            continue
        elif kind == "paragraph":
            text = str(content)
            if any(text.lower().startswith(p) for p in SEO_OPENING_SKIP):
                continue
            if should_drop_paragraph(text):
                continue
            if global_repeat and global_repeat.should_drop(text):
                continue
            if global_boilerplate and global_boilerplate.is_repeat(text):
                continue
            if deduper.seen_paragraph(text):
                continue
            out.append((kind, content))
        elif kind == "list" and isinstance(content, list):
            items = []
            for i in content:
                if should_drop_list_item(str(i)):
                    continue
                if global_repeat and global_repeat.should_drop(str(i)):
                    continue
                if global_boilerplate and global_boilerplate.is_repeat(i):
                    continue
                if not deduper.seen_paragraph(i):
                    items.append(i)
            if items:
                out.append((kind, items))
        elif kind == "image":
            out.append((kind, content))
    return out


def repair_blocks(
    blocks: list[tuple[str, str | list[str] | dict]],
) -> list[tuple[str, str | list[str] | dict]]:
    """Fix known compilation artifacts (orphan sentences, split lists)."""
    out: list[tuple[str, str | list[str] | dict]] = []
    i = 0
    while i < len(blocks):
        kind, content = blocks[i]
        if kind == "paragraph" and re.match(r"^scientists are actively studying", str(content), re.I):
            items: list[str] = []
            j = i + 1
            while j < len(blocks) and blocks[j][0] == "list":
                items.extend(str(x) for x in blocks[j][1])  # type: ignore[arg-type]
                j += 1
            tail = ""
            if j < len(blocks) and blocks[j][0] == "paragraph":
                tail_text = str(blocks[j][1]).strip()
                if re.match(r"^and how they may influence", tail_text, re.I):
                    tail = tail_text
                    j += 1
            if items:
                merged = "Research continues on " + ", ".join(items)
                if tail:
                    merged += " " + tail
                out.append(("paragraph", merged))
                i = j
                continue
        if kind == "paragraph" and re.match(r"^and how they may influence", str(content), re.I):
            i += 1
            continue
        if kind == "paragraph" and re.search(r"[:?]\s*[•\uf0b7\u2022]|[.!?]\s*[•\uf0b7\u2022]", str(content)):
            text = str(content)
            items = [s.strip() for s in re.split(r"\s*[•\uf0b7\u2022]\s*", text) if s.strip()]
            if len(items) > 1:
                intro = items[0]
                bullets = items[1:]
                if re.search(r"[:?]\s*$", intro) or (
                    len(intro.split()) <= 12 and intro.endswith(":")
                ):
                    out.append(("paragraph", intro))
                    out.append(("list", bullets))
                else:
                    out.append(("list", items))
                i += 1
                continue
        if kind == "paragraph":
            text = str(content)
            if re.search(r"[.!?][A-Za-z]", text) and not re.search(r"[.!?]\s+[A-Za-z]", text):
                parts = re.split(r"(?<=[.!?])(?=[A-Z])", text)
                if len(parts) > 1:
                    for part in parts:
                        part = part.strip()
                        if part:
                            out.append(("paragraph", part))
                    i += 1
                    continue
        if kind == "list" and isinstance(content, list):
            expanded: list[str] = []
            for item in content:
                item_str = str(item)
                if re.search(r"[.!?]\s*[•\uf0b7\u2022]", item_str):
                    expanded.extend(
                        s.strip() for s in re.split(r"\s*[•\uf0b7\u2022]\s*", item_str) if s.strip()
                    )
                elif re.search(r"[.!?][A-Za-z]", item_str) and not re.search(r"[.!?]\s+[A-Za-z]", item_str):
                    expanded.extend(
                        s.strip() for s in re.split(r"(?<=[.!?])(?=[A-Z])", item_str) if s.strip()
                    )
                else:
                    expanded.append(item_str)
            if expanded:
                out.append(("list", expanded))
                i += 1
                continue
        out.append((kind, content))
        i += 1
    return out


def demote_headings_for_merge(blocks: list[tuple[str, Any]]) -> list[tuple[str, Any]]:
    """After first source in a chapter, demote h2→h3 to avoid article-style hierarchy."""
    out: list[tuple[str, Any]] = []
    seen_content = False
    for kind, content in blocks:
        if kind.startswith("heading_") and seen_content:
            level = int(kind[-1])
            if level <= 2:
                kind = "heading_3"
        if kind == "paragraph" or kind == "list":
            seen_content = True
        out.append((kind, content))
    return out
