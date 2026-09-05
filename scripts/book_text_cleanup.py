"""Repair compilation artifacts and drop website-navigation residue."""

from __future__ import annotations

import re

from book_prose_cleanup import apply_prose_replacements, remove_figure_references

# Orphan link labels from seo-landing related-resource lists
NAV_ORPHAN_RE = re.compile(
    r"^(?:"
    r"Foods during a Crohn'?s flare"
    r"|Protein and healing in flares"
    r"|Iron deficiency nutrition"
    r"|What is Crohn'?s\?? Foundation basics"
    r"|What is IBD\?? Foundation basics"
    r"|Complete nutrition article"
    r"|Complete IBD nutrition article"
    r"|Foundation diet and nutrition"
    r"|Foundation newly diagnosed"
    r"|Newly diagnosed hub"
    r"|Crohn'?s disease hub"
    r"|Track symptoms and food"
    r"|Track food and symptoms"
    r"|Visit prep checklist"
    r"|First GI appointment guide"
    r"|Doctor visit prep guide"
    r"|Colonoscopy prep article"
    r"|Chicken protein article"
    r"|High-protein meal plan article"
    r"|Flare help hub"
    r"|Flare first 48 hours article"
    r"|Anti-inflammatory diet and IBD"
    r"|FODMAP diet for Crohn'?s and colitis"
    r"|UC diet foods guide"
    r"|IBD hydration guide"
    r"|Stress and anxiety with IBD"
    r"|Low-residue diet for flares"
    r")\s*$",
    re.I,
)

BULLET_CHARS = "\uf0b7\u2022\u25cf\u25aa\u25e6\u2043\u2219"

JOIN_FIX_RE = re.compile(
    r"([a-z,\)])([A-Z][a-z])"  # missing break: situationsPediatric -> situations. Pediatric
)

PROTECTED_TOKENS = (
    "MediVue",
    "FoodData Central",
    "FoodData",
    "IBDPal",
    "NIHDRI",
    "USDA",
    "PubMed",
    "GitHub",
    "YouTube",
    "LinkedIn",
    "OpenTable",
    "McDonald",
    "iPhone",
    "iPad",
)

FAQ_HEADING_RE = re.compile(
    r"^(?:Is|Should|Can|Does|Will|Are|Do|Have|Could|Would|Must|Was|Were)\s+.+\?\s*$",
    re.I,
)


def _protect_tokens(text: str) -> tuple[str, dict[str, str]]:
    mapping: dict[str, str] = {}
    out = text
    for i, token in enumerate(PROTECTED_TOKENS):
        if token not in out:
            continue
        key = f"__TOK{i}__"
        mapping[key] = token
        out = out.replace(token, key)
    return out, mapping


def _restore_tokens(text: str, mapping: dict[str, str]) -> str:
    out = text
    for key, token in mapping.items():
        out = out.replace(key, token)
    return out


def fix_joined_words(text: str) -> str:
    protected, mapping = _protect_tokens(text)
    fixed = JOIN_FIX_RE.sub(r"\1. \2", protected)
    return _restore_tokens(fixed, mapping)


def format_book_heading(text: str) -> str:
    """Normalize section headings without paragraph-style terminal punctuation."""
    t = text.replace("\u00ad", "").replace("\ufeff", "")
    t = replace_dashes(t)
    t = re.sub(r"\.{2,}", ".", t)
    return titlecase_section_heading(t.strip().rstrip("."))


def capitalize_sentence(text: str) -> str:
    t = text.strip()
    if not t:
        return t
    if t[0].islower() and t[0].isalpha():
        return t[0].upper() + t[1:]
    return t


def _titlecase_words(text: str, *, paren_or_quote: bool = False) -> str:
    """Title-case a heading fragment; parenthetical/quoted spans capitalize all major words."""
    t = text.strip().rstrip(".")
    if not t:
        return t
    if re.match(r"^how can support the non-formula parts of care$", t, re.I):
        return "Supporting the Non-Formula Parts of Care"
    t = re.sub(r"\bVitamin ([a-z])\b", lambda m: f"Vitamin {m.group(1).upper()}", t)
    t = re.sub(r"\bWhat Omega-3 Fats Does\b", "What Omega-3 Fats Do", t, flags=re.I)
    t = re.sub(
        r"\bSample Flare Day ([a-d])\b",
        lambda m: f"Sample Flare Day {m.group(1).upper()}",
        t,
        flags=re.I,
    )
    if t.isupper() and len(t.split()) <= 8:
        return t
    small = {
        "a", "an", "the", "and", "or", "but", "in", "on", "at", "to", "for",
        "of", "with", "vs", "versus", "from", "by", "as", "if",
    }
    if not paren_or_quote:
        small.add("when")
    words = t.split()
    out: list[str] = []
    for i, w in enumerate(words):
        lw = w.lower().strip(",")
        if i >= 1 and words[i - 1].lower() == "vitamin" and len(lw) == 1 and lw.isalpha():
            out.append(lw.upper())
            continue
        if re.fullmatch(r"[a-d]", lw) and i > 0 and words[i - 1].lower() == "day":
            out.append(lw.upper())
            continue
        if i > 0 and lw in small:
            out.append(w.lower() if w.islower() else lw)
        elif lw in ("b12", "dexa", "ibd", "dri", "crp"):
            out.append(w.upper() if lw == "b12" else lw.upper())
        elif "-" in w:
            out.append("-".join(_titlecase_words(part, paren_or_quote=paren_or_quote) for part in w.split("-")))
        else:
            out.append(w[:1].upper() + w[1:] if w else w)
    return " ".join(out)


def titlecase_section_heading(text: str) -> str:
    """Normalize blog-style sentence headings to title case for the book."""
    t = text.strip().rstrip(".")
    if not t or is_faq_heading(t):
        return t

    protected: list[str] = []

    def _protect(match: re.Match[str]) -> str:
        protected.append(match.group(0))
        return f"__PROT{len(protected) - 1}__"

    t = re.sub(r'"[^"]+"', _protect, t)
    t = re.sub(r"\([^)]+\)", _protect, t)
    t = _titlecase_words(t)
    for i, val in enumerate(protected):
        if val.startswith("("):
            repl = f"({_titlecase_words(val[1:-1], paren_or_quote=True)})"
        elif val.startswith('"'):
            repl = f'"{_titlecase_words(val[1:-1], paren_or_quote=True)}"'
        else:
            repl = val
        t = t.replace(f"__PROT{i}__", repl)
    return t


def fix_list_punctuation(item: str) -> str:
    out = capitalize_sentence(item)
    if len(out) > 25 and out[-1].isalnum() and not out.endswith((")", "]")):
        out += "."
    return out


def is_faq_heading(text: str) -> bool:
    t = text.strip()
    if not t:
        return False
    if FAQ_HEADING_RE.match(t):
        return True
    if t.endswith("?") and len(t.split()) <= 14:
        return True
    return False


def is_nav_orphan(text: str) -> bool:
    t = text.strip()
    if not t:
        return True
    if NAV_ORPHAN_RE.match(t):
        return True
    if t.lower().endswith(" article") and len(t.split()) <= 5:
        return True
    if t.lower().endswith(" guide") and len(t.split()) <= 6:
        return True
    if t.lower().endswith(" hub") and len(t.split()) <= 5:
        return True
    return False


def replace_dashes(text: str) -> str:
    """Replace em and en dashes with commas per publication style, preserving number ranges."""
    placeholders: list[str] = []

    def _hold_range(match: re.Match[str]) -> str:
        placeholders.append(match.group(0))
        return f"@@RANGE{len(placeholders) - 1}@@"

    out = re.sub(r"\d+[\u2013\u2014-]\d+", _hold_range, text)
    for dash in ("\u2014", "\u2013"):  # em dash, en dash
        out = out.replace(f" {dash} ", ", ")
        out = out.replace(f"{dash} ", ", ")
        out = out.replace(f" {dash}", ",")
        out = out.replace(dash, ", ")
    out = re.sub(r",\s*,+", ",", out)
    out = re.sub(r"\s+,", ",", out)
    for idx, original in enumerate(placeholders):
        out = out.replace(f"@@RANGE{idx}@@", original)
    return out


def replace_em_dash(text: str) -> str:
    """Backward-compatible alias."""
    return replace_dashes(text)


PAGE_REF_RE = re.compile(
    r"\b(?:see|on)\s+page\s+\d+\b",
    re.I,
)


def repair_text(text: str) -> str:
    """Fix joined sentences, embedded bullets, dashes, and odd whitespace."""
    out = text.replace("\u00ad", "").replace("\ufeff", "")
    out = replace_dashes(out)
    out = remove_figure_references(out)
    out = apply_prose_replacements(out)
    for ch in BULLET_CHARS:
        out = out.replace(ch, " • ")
    out = re.sub(r"[ \t]+", " ", out)
    out = fix_joined_words(out)
    out = re.sub(r"([.!?])([A-Z])", r"\1 \2", out)
    out = re.sub(r"([:?])([•\uf0b7\u2022])", r"\1 \2", out)
    for dup in (
        (
            "Soluble and insoluble fiber behave differently, and strictures change what is safe. "
            "Some people tolerate oats and peeled produce in remission yet need lower fiber during severe colitis."
        ),
        (
            "Lactose intolerance can appear or worsen during inflammation even if you tolerated milk before. "
            "Lactose-free dairy or alternatives may help while calcium and vitamin D still need attention."
        ),
    ):
        doubled = f"{dup}. {dup}."
        if doubled in out:
            out = out.replace(doubled, f"{dup}.", 1)
        doubled_space = f"{dup}.  {dup}."
        if doubled_space in out:
            out = out.replace(doubled_space, f"{dup}.", 1)
    out = re.sub(r"([.!?]\s+)this chapter\b", lambda m: m.group(1) + "This chapter", out, flags=re.I)
    out = capitalize_sentence(out)
    out = PAGE_REF_RE.sub("see the relevant chapter", out)
    out = re.sub(r"\.{2,}", ".", out)
    out = re.sub(r"\s+\.", ".", out)
    if len(out) > 20 and out[-1].isalnum() and not out.endswith((")", "]", "%")):
        if not (out.isupper() and len(out.split()) <= 10):
            out += "."
    return out.strip()


def finalize_text(text: str) -> str:
    """Last-pass normalization for any reader-facing string."""
    return repair_text(text)


def clean_paragraph(text: str) -> str | None:
    out = repair_text(text)
    if is_nav_orphan(out):
        return None
    if not out or len(out) < 20:
        return None
    return out


def clean_list_items(items: list[str]) -> list[str]:
    cleaned: list[str] = []
    for item in items:
        fixed = fix_list_punctuation(repair_text(item))
        if is_nav_orphan(fixed):
            continue
        if any(ch in item for ch in BULLET_CHARS):
            parts = re.split(r"[" + re.escape(BULLET_CHARS) + r"]+", item)
            for part in parts:
                p = clean_paragraph(part.strip())
                if p:
                    cleaned.append(fix_list_punctuation(p))
        elif fixed and not is_nav_orphan(fixed):
            cleaned.append(fixed)
    return cleaned


def expand_embedded_bullet_paragraph(
    text: str,
) -> list[tuple[str, str | list[str]]]:
    """Split paragraphs that contain embedded bullet markers into body + list."""
    if " • " not in text:
        return [("paragraph", text)]
    parts = [p.strip() for p in text.split(" • ") if p.strip()]
    if len(parts) <= 1:
        return [("paragraph", text)]
    blocks: list[tuple[str, str | list[str]]] = [("paragraph", parts[0])]
    if len(parts) > 1:
        blocks.append(("list", parts[1:]))
    return blocks


def _split_glued_reference_line(line: str) -> list[str]:
    """Split one reference string that may contain glued headings, URLs, or multiple entries."""
    line = line.strip().replace("\u00ad", "").replace("\ufeff", "")
    if not line:
        return []
    line = re.sub(r"^References\s*", "", line, flags=re.I)
    line = re.sub(r"(https?://\S+?)(\d+\.\s+)", r"\1\n\2", line)
    line = re.sub(r"(\bdoi:\S+)(\d+\.\s+)", r"\1\n\2", line, flags=re.I)
    if "\n" in line:
        out: list[str] = []
        for chunk in line.split("\n"):
            out.extend(_split_glued_reference_line(chunk))
        return out
    chunks = re.findall(
        r"\d+\.\s+.+?(?=\s*\d+\.\s+(?:[A-Z\"'(]|National|NIH|USDA|Crohn|World|American)|$)",
        line,
        flags=re.S,
    )
    if len(chunks) > 1:
        return [chunk.strip() for chunk in chunks if chunk.strip()]
    return [line] if line else []


def normalize_reference_lines(ref_lines: list[str]) -> list[str]:
    """Ensure each numbered reference is its own paragraph (fixes URL/ref glue)."""
    out: list[str] = []
    for line in ref_lines:
        out.extend(_split_glued_reference_line(line))
    return out


def clean_blocks(
    blocks: list[tuple[str, str | list[str] | dict]],
) -> list[tuple[str, str | list[str] | dict]]:
    out: list[tuple[str, str | list[str] | dict]] = []
    for kind, content in blocks:
        if kind == "paragraph":
            fixed = clean_paragraph(str(content))
            if fixed:
                out.extend(expand_embedded_bullet_paragraph(fixed))
        elif kind == "list" and isinstance(content, list):
            items = clean_list_items([str(i) for i in content])
            if items:
                out.append((kind, items))
        elif kind.startswith("heading_"):
            fixed = format_book_heading(str(content))
            if fixed and not is_faq_heading(fixed):
                out.append((kind, fixed))
        else:
            fixed = repair_text(str(content)) if isinstance(content, str) else content
            out.append((kind, fixed))
    return out
