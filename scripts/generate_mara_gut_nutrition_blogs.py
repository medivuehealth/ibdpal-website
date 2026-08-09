#!/usr/bin/env python3
# Prose style: do not use em dash.
"""Generate Mara-lab-informed gut/nutrition blogs (~10 min each)."""
from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
DATA = ROOT / "data" / "mara-gut-nutrition-posts.json"
VERCEL = ROOT / "vercel.json"
FALLBACK = BLOGS / "assets" / "gut-nutrition" / "ulcerative-colitis-crohns-nutrition_1.jpg"

sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402


def word_count(html_body: str) -> int:
    text = html_body
    for tag in ("</p>", "</li>", "</h2>", "</h3>", "</ul>"):
        text = text.replace(tag, " ")
    text = re.sub(r"<[^>]+>", " ", text)
    return len([w for w in text.split() if w.strip()])


def ensure_image(post: dict) -> None:
    asset = BLOGS / "assets" / post["asset_dir"]
    asset.mkdir(parents=True, exist_ok=True)
    dest = asset / post["images"][0]
    if dest.exists() and dest.stat().st_size >= 1000:
        return
    src_name = post.get("copy_from")
    if src_name:
        src = BLOGS / "assets" / src_name
        if src.exists():
            shutil.copy(src, dest)
            print("copied", dest.name, "from", src_name)
            return
    # Prefer existing file in asset_dir
    existing = sorted(asset.glob("*.jpg")) + sorted(asset.glob("*.png"))
    if existing:
        shutil.copy(existing[0], dest)
        print("copied", dest.name, "from", existing[0].name)
        return
    if FALLBACK.exists():
        shutil.copy(FALLBACK, dest)
        print("copied fallback", dest.name)


def patch_vercel(slugs: list[str]) -> None:
    text = VERCEL.read_text(encoding="utf-8")
    inserts = []
    for slug in slugs:
        src = f'"/blog/{slug}"'
        if src in text:
            continue
        inserts.append(
            f'    {{\n      "source": "/blog/{slug}",\n'
            f'      "destination": "/blogs/{slug}.html"\n    }}'
        )
    if not inserts:
        return
    block = ",\n".join(inserts) + ",\n"
    text = text.replace('"rewrites": [\n', f'"rewrites": [\n{block}')
    VERCEL.write_text(text, encoding="utf-8")
    print("patched vercel.json (+", len(inserts), "rewrites)")


def main() -> None:
    if not DATA.is_file():
        raise SystemExit(f"Missing {DATA}. Run build_mara_gut_nutrition_posts_json.py first.")
    posts = json.loads(DATA.read_text(encoding="utf-8"))
    slugs = []
    for post in posts:
        words = word_count(post["body"])
        minutes = max(1, round(words / 200))
        print(f"{post['slug']}: ~{words} words (~{minutes} min @200wpm)")
        # ~10 min at ~160-200 wpm conversational reading (site target band)
        if words < 1600:
            raise SystemExit(
                f"Post too short for ~10 min read: {post['slug']} ({words} words; need >=1600)"
            )
        ensure_image(post)
        out = BLOGS / f"{post['slug']}.html"
        out.write_text(render_post(post), encoding="utf-8")
        slugs.append(post["slug"])
        print("wrote", out.name)
    patch_vercel(slugs)
    print("Done.", len(slugs), "posts.")


if __name__ == "__main__":
    main()
