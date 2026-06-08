#!/usr/bin/env python3
"""Rebuild llms.txt URL lists from blogs, guides, and SEO hub pages."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LLMS = ROOT / "llms.txt"
DATA = ROOT / "data" / "seo-expansion.json"
BLOGS = ROOT / "blogs"
GUIDES = ROOT / "guides"
SUPPORT = ROOT / "support"
SITE = "https://www.ibdpal.org"


def blog_urls() -> list[str]:
    return sorted(f"{SITE}/blog/{p.stem}" for p in BLOGS.glob("*.html"))


def guide_urls() -> list[str]:
    pages = sorted(
        f"{SITE}/guides/{p.stem}" for p in GUIDES.glob("*.html") if p.stem != "index"
    )
    return [f"{SITE}/guides", *pages]


def hub_urls() -> list[str]:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    urls = [f"{SITE}/blog", f"{SITE}/faq", f"{SITE}/support"]
    for hub in data.get("hubs", []):
        urls.append(f"{SITE}/{hub['slug']}")
    for p in SUPPORT.glob("*.html"):
        if p.stem != "index":
            urls.append(f"{SITE}/support/{p.stem}")
    return sorted(set(urls))


def section_block(title: str, urls: list[str]) -> str:
    lines = [title] + [f"- {u}" for u in urls]
    return "\n".join(lines)


def sync_llms_txt() -> None:
    text = LLMS.read_text(encoding="utf-8")
    blog_block = section_block("## Blog (education, not medical advice)", blog_urls())
    guide_block = section_block("## Patient guides (search topics)", guide_urls())
    hub_block = section_block("## SEO hubs & directories", hub_urls())

    text = re.sub(
        r"## Blog \(education, not medical advice\).*?(?=\n## )",
        blog_block + "\n\n",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"## Patient guides \(search topics\).*?(?=\n## |\Z)",
        guide_block + "\n\n",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"## SEO hubs & directories.*?(?=\n## |\Z)",
        hub_block + "\n",
        text,
        flags=re.DOTALL,
    )
    LLMS.write_text(text, encoding="utf-8")


def main() -> None:
    sync_llms_txt()
    print(f"Updated {LLMS.name}: {len(blog_urls())} blogs, {len(guide_urls())} guides, {len(hub_urls())} hub URLs")


if __name__ == "__main__":
    main()
