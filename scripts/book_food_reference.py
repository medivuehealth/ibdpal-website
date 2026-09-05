"""Transform food blog blocks into standardized reference entries."""

from __future__ import annotations

import re
from typing import Any

Block = tuple[str, str | list[str] | dict]

FLARE_MARKERS = ("during a flare", "flare (when", "gentler textures", "active symptoms", "urgency")
REMISSION_MARKERS = ("during remission", "in remission", "when variety", "when inflammation is quiet")
PREP_MARKERS = ("prep", "preparation", "cook", "serve", "ideas")
NUTRITION_MARKERS = (
    "nutrition",
    "macro",
    "micronutrient",
    "potassium",
    "protein",
    "iron",
    "fiber",
    "serving",
)
WATCH_MARKERS = ("watch", "myth", "caution", "stricture", "avoid if")
TEAM_MARKERS = ("questions for", "ask your", "dietitian", "care team")
PARENT_SKIP_MARKERS = ("flare versus remission",)


def food_name_from_title(title: str) -> str:
    t = re.sub(r"\s*\|\s*.*$", "", title)
    t = re.sub(r":.*$", "", t)
    for suffix in (
        r"\s+and IBD.*$",
        r"\s+for IBD.*$",
        r"\s+with IBD.*$",
        r"\s+in IBD.*$",
    ):
        t = re.sub(suffix, "", t, flags=re.I)
    name = t.strip()
    if not name:
        return "FOOD"
    return name.upper()


def blocks_to_food_entry(title: str, blocks: list[Block]) -> list[Block]:
    name = food_name_from_title(title)
    flare: list[str] = []
    remission: list[str] = []
    nutrition: list[str] = []
    watch: list[str] = []
    prep: list[str] = []
    team: list[str] = []
    other: list[str] = []
    image_block: Block | None = None

    current_bucket = "other"
    for kind, content in blocks:
        if kind == "image":
            if image_block is None:
                image_block = (kind, content)
            continue
        if kind.startswith("heading_"):
            h = str(content).lower()
            if any(m in h for m in PARENT_SKIP_MARKERS):
                # Keep reading child H3s under the parent; do not dump into flare yet.
                current_bucket = "other"
                continue
            if any(m in h for m in FLARE_MARKERS) or (
                "flare" in h and "remission" not in h and "versus" not in h
            ):
                current_bucket = "flare"
            elif any(m in h for m in REMISSION_MARKERS):
                current_bucket = "remission"
            elif any(m in h for m in PREP_MARKERS):
                current_bucket = "prep"
            elif any(m in h for m in NUTRITION_MARKERS):
                current_bucket = "nutrition"
            elif any(m in h for m in WATCH_MARKERS) or "myth" in h:
                current_bucket = "watch"
            elif any(m in h for m in TEAM_MARKERS):
                current_bucket = "team"
            else:
                current_bucket = "other"
            continue
        if kind == "paragraph":
            text = str(content)
            target = {
                "flare": flare,
                "remission": remission,
                "nutrition": nutrition,
                "watch": watch,
                "prep": prep,
                "team": team,
            }.get(current_bucket, other)
            target.append(text)
        elif kind == "list" and isinstance(content, list):
            target = {
                "flare": flare,
                "remission": remission,
                "nutrition": nutrition,
                "watch": watch,
                "prep": prep,
                "team": team,
            }.get(current_bucket, other)
            target.extend(str(i) for i in content)

    out: list[Block] = [("heading_h2", name)]
    if image_block is not None:
        out.append(image_block)

    def add_section(label: str, items: list[str]) -> None:
        if not items:
            return
        out.append(("heading_h3", label))
        if len(items) == 1 and len(items[0]) > 80:
            out.append(("paragraph", items[0]))
        elif all(len(i) < 120 for i in items):
            out.append(("list", items[:6]))
        else:
            for item in items[:4]:
                out.append(("paragraph", item))

    # Prefer dedicated buckets; fall back to lead paragraphs if flare/remission empty.
    add_section("During a flare", flare or other[:1])
    add_section("During remission", remission or (other[1:2] if len(other) > 1 else []))
    add_section("Nutrition", nutrition)
    add_section("What to watch for", watch)
    add_section("Preparation or modification ideas", prep)
    if team:
        add_section("Ask your care team if", team)

    if len(out) <= 2 and other:
        out.append(("paragraph", " ".join(other[:2])))

    return out
