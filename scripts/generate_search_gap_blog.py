#!/usr/bin/env python3
"""Generate a blog post from the top anonymous search-gap topic in Postgres."""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
DATA = ROOT / "data" / "search-gap-posts.json"
SITEMAP = ROOT / "sitemap.xml"
VERCEL = ROOT / "vercel.json"
SITE = "https://www.ibdpal.org"
FETCH_SCRIPT = ROOT / "scripts" / "fetch_content_ideas.js"

sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402

IMAGE_URLS = {
    "leg-knee-pain-ibd": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?auto=format&w=1200&q=80",
}
FALLBACK_IMAGE = BLOGS / "assets" / "low-residue" / "low-residue_1.jpg"
NOISE = re.compile(
    r"deployment|verification|\btest\b|embolism|^\d+$|^[a-z]{1,2}$",
    re.I,
)


def download_image(url: str, dest: Path) -> bool:
    import ssl
    import urllib.request

    for ctx in (ssl.create_default_context(), ssl._create_unverified_context()):
        try:
            with urllib.request.urlopen(url, context=ctx, timeout=30) as resp:
                data = resp.read()
            if len(data) > 5000 and data[:2] == b"\xff\xd8":
                dest.write_bytes(data)
                return True
        except Exception:
            continue
    return False


def load_search_rows() -> list[dict]:
    if not FETCH_SCRIPT.exists():
        return []
    proc = subprocess.run(
        ["node", str(FETCH_SCRIPT)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        print("WARN: could not query search gaps:", proc.stderr.strip() or proc.stdout.strip())
        return []
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        print("WARN: unexpected fetch_content_ideas output")
        return []


def pick_post_for_gap(rows: list[dict], posts: list[dict]) -> tuple[dict | None, dict | None]:
    cleaned = [row for row in rows if row.get("normalized_term") and not NOISE.search(row["normalized_term"])]
    if not cleaned:
        return None, None

    def score(row: dict) -> tuple:
        avg = float(row.get("avg_result_count") or 99)
        count = int(row.get("search_count") or 0)
        low_results = 0 if avg <= 4 else 1
        return (low_results, -count, avg)

    for row in sorted(cleaned, key=score):
        post = match_post(posts, row["normalized_term"])
        if post:
            return row, post
    return None, None


def match_post(posts: list[dict], term: str) -> dict | None:
    normalized = term.lower().strip()
    for post in posts:
        for candidate in post.get("match_terms", []):
            candidate_norm = candidate.lower().strip()
            if normalized == candidate_norm or normalized in candidate_norm or candidate_norm in normalized:
                return post
    return None


def prepare_post(raw: dict) -> dict:
    post = dict(raw)
    asset = post["asset_dir"]
    img_name = f"{asset}_1.jpg"
    post.setdefault("images", [img_name])
    post.setdefault("alts", [post["title"]])
    return post


def ensure_image(post: dict) -> None:
    asset = BLOGS / "assets" / post["asset_dir"]
    asset.mkdir(parents=True, exist_ok=True)
    dest = asset / post["images"][0]
    if dest.exists() and dest.stat().st_size >= 5000:
        return
    url = IMAGE_URLS.get(post["asset_dir"])
    if url and download_image(url, dest):
        return
    if FALLBACK_IMAGE.exists():
        shutil.copy(FALLBACK_IMAGE, dest)
        print("used fallback image for", dest.name)
    else:
        print("WARN: no image for", dest)


def write_blog(post: dict) -> str:
    prepared = prepare_post(post)
    ensure_image(prepared)
    out = BLOGS / f"{prepared['slug']}.html"
    out.write_text(render_post(prepared), encoding="utf-8")
    print("wrote", out.name)
    return prepared["slug"]


def patch_vercel(slug: str) -> None:
    text = VERCEL.read_text(encoding="utf-8")
    src = f'"/blog/{slug}"'
    if src in text:
        return
    insert = (
        f'    {{\n      "source": "/blog/{slug}",\n'
        f'      "destination": "/blogs/{slug}.html"\n    }}'
    )
    text = text.replace('"rewrites": [\n', f'"rewrites": [\n{insert},\n')
    VERCEL.write_text(text, encoding="utf-8")
    print("patched vercel.json")


def patch_sitemap(slug: str) -> None:
    today = date.today().isoformat()
    text = SITEMAP.read_text(encoding="utf-8")
    marker = "<!-- search-gap-blog -->"
    if marker in text:
        text = re.sub(
            rf"\n  {re.escape(marker)}.*?(?=\n  <!-- |\n</urlset>)",
            "",
            text,
            flags=re.DOTALL,
        )
    entry = (
        f"  {marker}\n"
        f"  <url>\n    <loc>{SITE}/blog/{slug}</loc>\n    <lastmod>{today}</lastmod>\n"
        f"    <changefreq>monthly</changefreq>\n    <priority>0.85</priority>\n  </url>"
    )
    anchor = "  <!-- seo-wellness-blogs -->"
    if anchor in text:
        text = text.replace(anchor, entry + "\n" + anchor)
    else:
        text = text.replace("  <!-- tier3-seo -->", entry + "\n  <!-- tier3-seo -->")
    SITEMAP.write_text(text, encoding="utf-8")
    print("patched sitemap.xml")


def main() -> None:
    catalog = json.loads(DATA.read_text(encoding="utf-8"))
    posts = catalog.get("posts", [])
    if not posts:
        raise SystemExit("No search-gap post templates found.")

    rows = load_search_rows()
    gap, post = pick_post_for_gap(rows, posts)
    if gap and post:
        print(
            "Top matched search gap:",
            gap["normalized_term"],
            f"(count={gap['search_count']}, avg_results={gap['avg_result_count']})",
        )
    elif not post:
        post = posts[0]
        print("Using default search-gap template:", post["slug"])

    slug = write_blog(post)
    patch_vercel(slug)
    patch_sitemap(slug)
    print("Next:")
    print("  python scripts/generate_amp_pages.py")
    print("  python scripts/sync_resources_library.py")
    print("  python scripts/sync_llms_txt.py")


if __name__ == "__main__":
    main()
