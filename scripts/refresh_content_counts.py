#!/usr/bin/env python3
"""Refresh displayed content analytics counts from live inventory."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

BLOGS = len(list((ROOT / "blogs").glob("*.html")))
GUIDES = len(list((ROOT / "guides").glob("*.html"))) - 1  # exclude index
SPANISH = len(list((ROOT / "es").glob("*.html")))
RESOURCES = (ROOT / "resources-data.js").read_text(encoding="utf-8").count("title:")
SITEMAP = (ROOT / "sitemap.xml").read_text(encoding="utf-8").count("<url>")
RP = f"{RESOURCES}+"
SP = f"{SITEMAP}+"


def main() -> None:
    print(
        {
            "blogs": BLOGS,
            "guides": GUIDES,
            "spanish": SPANISH,
            "resources": RESOURCES,
            "sitemap": SITEMAP,
        }
    )

    files = [
        ROOT / "index.html",
        ROOT / "about.html",
        ROOT / "impact.html",
        ROOT / "library.html",
        ROOT / "site-updates.html",
        ROOT / "scripts" / "ui_snippets.py",
        ROOT / "scripts" / "generate_static_pages.py",
    ]

    subs = [
        (
            '>107</span><span class="library-stat__l">Articles</span>',
            f'>{BLOGS}</span><span class="library-stat__l">Articles</span>',
        ),
        (
            '>35</span><span class="library-stat__l">Patient guides</span>',
            f'>{GUIDES}</span><span class="library-stat__l">Patient guides</span>',
        ),
        (
            '>8</span><span class="library-stat__l">Spanish pages</span>',
            f'>{SPANISH}</span><span class="library-stat__l">Spanish pages</span>',
        ),
        (
            '>200+</span><span class="library-stat__l">Resource library entries</span>',
            f'>{RP}</span><span class="library-stat__l">Resource library entries</span>',
        ),
        (
            '>240+</span><span class="library-stat__l">Education and resource pages</span>',
            f'>{SP}</span><span class="library-stat__l">Education and resource pages</span>',
        ),
        (
            "IBD Content Library | 240+ Free Education Pages",
            f"IBD Content Library | {SP} Free Education Pages",
        ),
        (
            "240+ free education and resource pages, 107 articles",
            f"{SP} free education and resource pages, {BLOGS} articles",
        ),
        ("117 in-depth articles", f"{BLOGS} in-depth articles"),
        ("37 step-by-step patient guides", f"{GUIDES} step-by-step patient guides"),
        (
            "210+ searchable resource library entries",
            f"{RP} searchable resource library entries",
        ),
        ("250+ education and sitemap pages", f"{SP} education and sitemap pages"),
        (
            "250+ total education and resource pages",
            f"{SP} total education and resource pages",
        ),
        ("250+ free pages", f"{SP} free pages"),
        ("<strong>107 articles</strong>", f"<strong>{BLOGS} articles</strong>"),
        (
            "<strong>35 patient guides</strong>",
            f"<strong>{GUIDES} patient guides</strong>",
        ),
        (
            "<strong>200+</strong> curated entries",
            f"<strong>{RP}</strong> curated entries",
        ),
        (
            "<strong>240+ total education and resource pages</strong>",
            f"<strong>{SP} total education and resource pages</strong>",
        ),
        (
            "<strong>Library counts:</strong> <strong>117 articles</strong>, <strong>37 guides</strong>, <strong>210+</strong> resource entries, <strong>250+</strong> sitemap education pages",
            f"<strong>Library counts:</strong> <strong>{BLOGS} articles</strong>, <strong>{GUIDES} guides</strong>, <strong>{RP}</strong> resource entries, <strong>{SP}</strong> sitemap education pages",
        ),
        (
            '"IBD Content Library | 240+ Free Education Pages | IBDPal"',
            f'"IBD Content Library | {SP} Free Education Pages | IBDPal"',
        ),
        (
            '"IBDPal impact: 240+ free education and resource pages, 107 articles,',
            f'"IBDPal impact: {SP} free education and resource pages, {BLOGS} articles,',
        ),
        (
            '<div class="library-stat"><span class="library-stat__n">107</span>',
            f'<div class="library-stat"><span class="library-stat__n">{BLOGS}</span>',
        ),
        (
            '<div class="library-stat"><span class="library-stat__n">35</span>',
            f'<div class="library-stat"><span class="library-stat__n">{GUIDES}</span>',
        ),
        (
            '<div class="library-stat"><span class="library-stat__n">8</span>',
            f'<div class="library-stat"><span class="library-stat__n">{SPANISH}</span>',
        ),
        (
            '<div class="library-stat"><span class="library-stat__n">200+</span>',
            f'<div class="library-stat"><span class="library-stat__n">{RP}</span>',
        ),
        (
            '<div class="library-stat"><span class="library-stat__n">240+</span>',
            f'<div class="library-stat"><span class="library-stat__n">{SP}</span>',
        ),
    ]

    for path in files:
        text = path.read_text(encoding="utf-8")
        orig = text
        for old, new in subs:
            text = text.replace(old, new)
        if text != orig:
            path.write_text(text, encoding="utf-8")
            print("updated", path.relative_to(ROOT))
        else:
            print("unchanged", path.relative_to(ROOT))

    bullet = (
        f'<li><strong>Content analytics refresh:</strong> library counts updated to '
        f"<strong>{BLOGS} articles</strong>, <strong>{GUIDES} guides</strong>, "
        f"<strong>{RP}</strong> resource entries, and <strong>{SP}</strong> sitemap education pages "
        f"(Aug 23, 2026)</li>"
    )
    for path in (
        ROOT / "index.html",
        ROOT / "site-updates.html",
        ROOT / "scripts" / "ui_snippets.py",
    ):
        text = path.read_text(encoding="utf-8")
        if "Content analytics refresh" in text:
            print("bullet exists", path.name)
            continue
        m = re.search(
            r'(<h2>August 2026</h2>\s*<ul class="seo-landing__list">\s*)',
            text,
        )
        if not m:
            print("no August block", path.name)
            continue
        text = text[: m.end()] + bullet + "\n                            " + text[m.end() :]
        path.write_text(text, encoding="utf-8")
        print("bullet added", path.name)


if __name__ == "__main__":
    main()
