#!/usr/bin/env python3
"""Rebuild resources-data.js from base entries, blogs, and keyword map."""
from __future__ import annotations

import json
import re
import sys
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
GUIDES = ROOT / "guides"
BASE = ROOT / "data" / "resources-base.json"
KEYWORDS = ROOT / "data" / "ibd-resource-keywords.json"
TOPIC_POSTS = ROOT / "data" / "ibd-topic-posts.json"
OUT = ROOT / "resources-data.js"

sys.path.insert(0, str(ROOT / "scripts"))
from amp_utils import discover_blogs  # noqa: E402

CATEGORY_FROM_LABEL = {
    "nutrition": "nutrition",
    "treatment": "treatment",
    "treatment basics": "treatment",
    "wellness": "wellness",
    "lifestyle": "wellness",
    "family": "family",
    "flares": "wellness",
    "product & ibd": "getting-started",
    "product": "getting-started",
}

GUIDE_CATEGORY = {
    "biologics-crohns-colitis": "treatment",
    "low-residue-diet-ibd": "nutrition",
    "crohns-disease-diet-nutrition": "nutrition",
    "ulcerative-colitis-diet-foods": "nutrition",
    "foods-to-eat-crohns-flare": "nutrition",
    "crohns-food-triggers": "nutrition",
    "what-should-i-eat-crohns-colitis": "nutrition",
}


def js_str(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


def blog_category_from_html(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    m = re.search(r'class="blog-date">[^·]*·\s*([^<]+)</p>', text)
    if not m:
        return "wellness"
    label = m.group(1).strip().lower()
    return CATEGORY_FROM_LABEL.get(label, "wellness")


def load_topic_meta() -> dict[str, dict]:
    if not TOPIC_POSTS.exists():
        return {}
    data = json.loads(TOPIC_POSTS.read_text(encoding="utf-8"))
    return {p["slug"]: p for p in data.get("posts", [])}


def parse_guide(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    if path.name == "index.html":
        return None
    title_m = re.search(r"<h1[^>]*>(.*?)</h1>", text, re.S)
    desc_m = re.search(r'<meta name="description" content="([^"]*)"', text)
    if not title_m:
        return None
    title = html.unescape(re.sub(r"<[^>]+>", "", title_m.group(1)).strip())
    slug = path.stem
    return {
        "title": title,
        "category": GUIDE_CATEGORY.get(slug, "getting-started"),
        "type": "site",
        "url": f"/guides/{slug}",
        "description": desc_m.group(1) if desc_m else "",
        "tags": [],
    }


def merge_tags(*parts: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for part in parts:
        for t in part:
            key = t.lower().strip()
            if key and key not in seen:
                seen.add(key)
                out.append(t.strip())
    return out


def format_entry(item: dict) -> str:
    tags = item.get("tags") or []
    keywords = item.get("keywords") or []
    parts = [
        f"title: {js_str(item['title'])}",
        f"category: {js_str(item['category'])}",
        f"type: {js_str(item['type'])}",
        f"url: {js_str(item['url'])}",
        f"tags: {json.dumps(tags, ensure_ascii=False)}",
    ]
    if item.get("description"):
        parts.append(f"description: {js_str(item['description'])}")
    if keywords:
        parts.append(f"keywords: {json.dumps(keywords, ensure_ascii=False)}")
    return "  { " + ", ".join(parts) + " }"


def main() -> None:
    base = json.loads(BASE.read_text(encoding="utf-8"))
    kw_map = json.loads(KEYWORDS.read_text(encoding="utf-8"))
    topic_meta = load_topic_meta()
    posts = discover_blogs(BLOGS)

    entries: list[dict] = []
    seen_urls: set[str] = set()

    for item in base:
        url = item["url"]
        if url in seen_urls:
            continue
        seen_urls.add(url)
        key = url.strip("/").replace("guides/", "guides/")
        extra = kw_map.get(key, [])
        entries.append(
            {
                **item,
                "tags": merge_tags(item.get("tags", []), extra),
                "keywords": extra,
            }
        )

    for slug, post in sorted(posts.items()):
        url = f"/blog/{slug}"
        if url in seen_urls:
            continue
        seen_urls.add(url)
        meta = topic_meta.get(slug, {})
        extra = kw_map.get(slug, [])
        tags = merge_tags(meta.get("tags", []), extra)
        if not tags:
            tags = ["article", "ibd"]
        cat = meta.get("resource_category") or blog_category_from_html(BLOGS / f"{slug}.html")
        entries.append(
            {
                "title": post["title"],
                "category": cat,
                "type": "blog",
                "url": url,
                "description": post.get("description", ""),
                "tags": tags,
                "keywords": extra,
            }
        )

    guide_slugs_in_kw = {k for k in kw_map if k.startswith("guides/")}
    for slug_path in sorted(guide_slugs_in_kw):
        slug = slug_path.replace("guides/", "")
        path = GUIDES / f"{slug}.html"
        if not path.exists():
            continue
        parsed = parse_guide(path)
        if not parsed:
            continue
        url = parsed["url"]
        if url in seen_urls:
            continue
        seen_urls.add(url)
        extra = kw_map[slug_path]
        entries.append(
            {
                **parsed,
                "tags": merge_tags(parsed.get("tags", []), extra),
                "keywords": extra,
            }
        )

    lines = [
        "/**",
        " * Filterable patient resource library (education links + site content).",
        " * Generated by scripts/sync_resources_library.py — do not edit by hand.",
        " */",
        "window.IBDPAL_RESOURCES = [",
    ]
    lines.extend(format_entry(e) + "," for e in entries)
    lines.append("];")
    lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT.name} ({len(entries)} entries, {len(posts)} blogs)")


if __name__ == "__main__":
    main()
