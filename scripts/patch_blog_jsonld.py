#!/usr/bin/env python3
"""Add BreadcrumbList to blog Article JSON-LD if missing."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"


def patch_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "BreadcrumbList" in text:
        return False
    m_canon = re.search(r'<link rel="canonical" href="(https://ibdpal\.org/blog/[^"]+)"', text)
    m_title = re.search(r"<title>([^<]+)</title>", text)
    if not m_canon or not m_title:
        return False
    canonical = m_canon.group(1)
    title = m_title.group(1).replace(" | IBDPal Blog", "").strip()
    m_ld = re.search(
        r'<script type="application/ld\+json">(\{.*?\})</script>',
        text,
        re.DOTALL,
    )
    if not m_ld:
        return False
    try:
        old = json.loads(m_ld.group(1))
    except json.JSONDecodeError:
        return False
    article = old if old.get("@type") == "Article" else None
    if not article and "@graph" in old:
        return False
    if not article:
        article = old
    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "IBDPal", "item": "https://www.ibdpal.org/"},
                    {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://www.ibdpal.org/#blogs"},
                    {"@type": "ListItem", "position": 3, "name": title, "item": canonical},
                ],
            },
            article,
        ],
    }
    new_ld = json.dumps(graph, separators=(",", ":"), ensure_ascii=False)
    new_text = text[: m_ld.start(1)] + new_ld + text[m_ld.end(1) :]
    path.write_text(new_text, encoding="utf-8")
    return True


def main():
    n = 0
    for f in sorted(BLOGS.glob("*.html")):
        if patch_file(f):
            print("patched", f.name)
            n += 1
    print("done,", n, "files")


if __name__ == "__main__":
    main()
