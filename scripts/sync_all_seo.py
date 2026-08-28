#!/usr/bin/env python3
"""Run full SEO sync after content expansions (hubs, resources, sitemap, llms, IndexNow list)."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
PYTHON = sys.executable


def run(script: str) -> None:
    path = ROOT / "scripts" / script
    print(f"\n>> {script}")
    subprocess.run([PYTHON, str(path)], check=True, cwd=ROOT)


def write_indexnow_urls() -> None:
    from amp_utils import discover_blogs  # noqa: E402

    sys.path.insert(0, str(ROOT / "scripts"))
    blogs = sorted(discover_blogs(ROOT / "blogs").keys())
    guides = sorted(
        p.stem for p in (ROOT / "guides").glob("*.html") if p.stem != "index"
    )
    urls = [
        "https://www.ibdpal.org/",
        "https://www.ibdpal.org/sitemap.xml",
        "https://www.ibdpal.org/llms.txt",
        "https://www.ibdpal.org/what-is-ibd",
        "https://www.ibdpal.org/crohns-and-colitis",
        "https://www.ibdpal.org/start-here",
        "https://www.ibdpal.org/newly-diagnosed",
        "https://www.ibdpal.org/guides",
        "https://www.ibdpal.org/blog",
    ]
    for hub in ("ibd-nutrition", "stool-labs-decoder", "crohns-disease", "ulcerative-colitis", "teens-and-school", "flare-help"):
        urls.append(f"https://www.ibdpal.org/{hub}")
    urls.extend(f"https://www.ibdpal.org/guides/{g}" for g in guides)
    urls.extend(f"https://www.ibdpal.org/blog/{b}" for b in blogs)
    out = DATA / "content-refresh-indexnow-urls.json"
    out.write_text(json.dumps(sorted(set(urls)), indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out.name} ({len(urls)} URLs)")


def main() -> None:
    run("assign_blog_hubs.py")
    run("generate_static_pages.py")
    run("generate_seo_landings.py")
    run("apply_blog_expansions_html.py")
    run("generate_seo_hubs.py")
    run("sync_resources_library.py")
    run("generate_amp_pages.py")
    run("sync_sitemap.py")
    run("sync_llms_txt.py")
    run("generate_home_engagement_data.py")
    run("refresh_content_counts.py")
    run("assign_blog_hubs.py")
    run("generate_seo_hubs.py")
    write_indexnow_urls()
    print("\nDone. Submit to Bing: npm run indexnow -- --file data/content-refresh-indexnow-urls.json")


if __name__ == "__main__":
    sys.path.insert(0, str(ROOT / "scripts"))
    main()
