#!/usr/bin/env python3
"""Compute public content counts for library/impact pages."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def count_glob(pattern: str) -> int:
    return len(list(ROOT.glob(pattern)))


def content_counts() -> dict[str, int]:
    blog_articles = count_glob("blogs/*.html")
    guides = count_glob("guides/*.html") - 1  # exclude index
    support_states = count_glob("support/*.html") - 2  # exclude index + landing
    spanish = count_glob("es/*.html")
    stories = count_glob("patient-stories/*.html") - 1
    hubs = 12  # nutrition, flare, crohns, uc, faq, glossary, research, teens, etc.
    total_education = blog_articles + guides + support_states + spanish + stories + hubs
    return {
        "blogs": blog_articles,
        "guides": guides,
        "support_states": support_states,
        "spanish": spanish,
        "stories": stories,
        "hubs": hubs,
        "total_education": total_education,
        "articles_and_guides": blog_articles + guides,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(content_counts(), indent=2))
