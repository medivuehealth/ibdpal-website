#!/usr/bin/env python3
# Prose style: do not use em dash.
"""Build home-engagement-data.js: recent posts, seasonal packs, aliases, gap answers."""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
OUT = ROOT / "home-engagement-data.js"
SEARCH_GAP = ROOT / "data" / "search-gap-posts.json"
ALIASES = ROOT / "data" / "search-aliases.json"

sys.path.insert(0, str(ROOT / "scripts"))
from amp_utils import discover_blogs  # noqa: E402

SEASONAL_PACKS = [
    {
        "id": "back-to-school",
        "months": [7, 8],
        "eyebrow": "Seasonal",
        "title": "Back-to-school IBD pack",
        "note": "Accommodations, lunches, and planning before August.",
        "links": [
            {"url": "/blog/school-planning-ibd-before-august", "title": "School planning before August"},
            {"url": "/blog/workplace-school-ibd-rights", "title": "School and workplace rights"},
            {"url": "/blog/teen-nutrition-ibd-growth", "title": "Teen nutrition and growth"},
            {"url": "/teens-and-school", "title": "Teens and school hub"},
        ],
    },
    {
        "id": "travel-summer",
        "months": [5, 6, 7],
        "eyebrow": "Seasonal",
        "title": "Travel and heat pack",
        "note": "Restrooms, meds, food, and hydration on the road.",
        "links": [
            {"url": "/blog/summer-travel-ibd-restrooms-meds-food-heat", "title": "Summer travel with IBD"},
            {"url": "/blog/travel-with-ibd", "title": "Travel planning basics"},
            {"url": "/blog/ibd-summer-heat-hydration", "title": "Heat and hydration"},
            {"url": "/guides/ibd-travel-planning", "title": "Travel planning guide"},
        ],
    },
    {
        "id": "flu-vaccine",
        "months": [9, 10, 11],
        "eyebrow": "Seasonal",
        "title": "Vaccines and infection season",
        "note": "Questions to ask when you take biologics or immunosuppressants.",
        "links": [
            {"url": "/blog/vaccines-biologics-immunosuppressants-ibd", "title": "Vaccines with biologics"},
            {"url": "/blog/understanding-biologics-ibd", "title": "Understanding biologics"},
            {"url": "/blog/when-to-call-gi-vs-er-ibd", "title": "GI nurse line vs ER"},
        ],
    },
    {
        "id": "holidays",
        "months": [11, 12],
        "eyebrow": "Seasonal",
        "title": "Holidays and special occasions",
        "note": "Food, travel, and stress around gatherings.",
        "links": [
            {"url": "/blog/icn-ibd-holidays-special-occasions", "title": "Holidays with IBD"},
            {"url": "/blog/dining-out-ibd-restaurants", "title": "Dining out"},
            {"url": "/blog/stress-coping-strategies-ibd", "title": "Stress coping"},
        ],
    },
    {
        "id": "new-year-habits",
        "months": [1, 2],
        "eyebrow": "Seasonal",
        "title": "Fresh start habits",
        "note": "Tracking, nutrition targets, and visit prep for the year ahead.",
        "links": [
            {"url": "/blog/tracking-food-symptoms-ibdpal", "title": "Track food and symptoms"},
            {"url": "/blog/how-ibdpal-nutrition-targets-work", "title": "Nutrition targets"},
            {"url": "/visit-prep", "title": "Visit prep checklist"},
            {"url": "/newly-diagnosed", "title": "Newly diagnosed hub"},
        ],
    },
    {
        "id": "flare-focus",
        "months": [3, 4],
        "eyebrow": "Seasonal",
        "title": "Flare readiness pack",
        "note": "First 48 hours, go-bag, and when to seek urgent care.",
        "links": [
            {"url": "/flare-help", "title": "Flare help hub"},
            {"url": "/blog/flare-first-48-hours", "title": "First 48 hours of a flare"},
            {"url": "/blog/ibd-flare-go-bag", "title": "Flare go-bag"},
            {"url": "/ibd-red-flags-urgent-care", "title": "Red flags and urgent care"},
        ],
    },
]


def default_aliases() -> dict:
    return {
        "entereal": "enteral",
        "entrail": "enteral",
        "glutten": "gluten",
        "biologic": "biologics",
        "biologicals": "biologics",
        "prednison": "prednisone",
        "diarrhoea": "diarrhea",
        "faecal": "fecal",
        "calprotectin": "calprotectin",
        "crohns": "crohn",
        "crohn's": "crohn",
        "ulcerative colitus": "ulcerative colitis",
        "self manageme": "self management",
        "remision": "remission",
    }


def recent_posts(posts: dict[str, dict], now: datetime) -> dict:
    week = []
    month = []
    for slug, post in posts.items():
        iso = post.get("date_iso") or ""
        if not iso:
            continue
        try:
            published = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        except ValueError:
            continue
        age_days = (now - published).total_seconds() / 86400.0
        item = {
            "slug": slug,
            "url": f"/blog/{slug}",
            "title": post["title"],
            "date_iso": iso,
            "category": post.get("category") or "Article",
        }
        if age_days <= 7:
            week.append(item)
        if age_days <= 31:
            month.append(item)

    def sort_key(row: dict) -> str:
        return row.get("date_iso") or ""

    week.sort(key=sort_key, reverse=True)
    month.sort(key=sort_key, reverse=True)
    return {"week": week[:8], "month": month[:12]}


def gap_answers(now: datetime) -> list[dict]:
    if not SEARCH_GAP.exists():
        return []
    data = json.loads(SEARCH_GAP.read_text(encoding="utf-8"))
    out = []
    for post in data.get("posts", []):
        iso = post.get("date_iso") or ""
        try:
            published = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        except ValueError:
            published = now
        age_days = (now - published).total_seconds() / 86400.0
        if age_days > 45:
            continue
        terms = post.get("match_terms") or post.get("tags") or []
        label = terms[0] if terms else post["slug"].replace("-", " ")
        out.append(
            {
                "slug": post["slug"],
                "url": f"/blog/{post['slug']}",
                "title": post["title"],
                "search_label": str(label).title(),
                "match_terms": terms[:6],
                "badge": f"New: answers searches for {str(label).title()}",
                "date_iso": iso,
            }
        )
    out.sort(key=lambda row: row.get("date_iso") or "", reverse=True)
    return out[:6]


def active_seasonal(now: datetime) -> list[dict]:
    month = now.month
    active = [pack for pack in SEASONAL_PACKS if month in pack["months"]]
    if not active:
        # Always offer one helpful pack.
        active = [pack for pack in SEASONAL_PACKS if pack["id"] == "flare-focus"]
    return active


def main() -> None:
    now = datetime.now(timezone.utc)
    posts = discover_blogs(BLOGS)
    aliases = default_aliases()
    if ALIASES.exists():
        aliases.update(json.loads(ALIASES.read_text(encoding="utf-8")))

    payload = {
        "generated_at": now.isoformat(),
        "recent": recent_posts(posts, now),
        "seasonal": active_seasonal(now),
        "aliases": aliases,
        "gap_answers": gap_answers(now),
    }
    js = (
        "/* Generated by scripts/generate_home_engagement_data.py */\n"
        "window.IBDPAL_HOME_ENGAGEMENT = "
        + json.dumps(payload, ensure_ascii=False, indent=2)
        + ";\n"
    )
    OUT.write_text(js, encoding="utf-8")
    print(
        "wrote",
        OUT.name,
        f"week={len(payload['recent']['week'])}",
        f"month={len(payload['recent']['month'])}",
        f"seasonal={len(payload['seasonal'])}",
        f"gap_answers={len(payload['gap_answers'])}",
    )


if __name__ == "__main__":
    main()
