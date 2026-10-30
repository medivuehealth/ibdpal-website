# -*- coding: utf-8 -*-
"""Publish the five pending ask_page Reader Q&A (question_id 20-24).

Usage: python scripts/publish_reader_qa_sep20_pending.py
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

import psycopg2

ROOT = Path(__file__).resolve().parents[1]
SERVER_ENV = ROOT.parent / "ibdpal-server" / "config.env"
MAX_CHARS = 12000
sys.path.insert(0, str(Path(__file__).resolve().parent))

from _qa_sep20_pending_items import ITEMS  # noqa: E402


def read_env(path: Path) -> dict:
    out = {}
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def words(text: str) -> int:
    return len(re.findall(r"\S+", text))


def approx_minutes(text: str) -> float:
    return round(words(text) / 220.0, 1)


def main() -> None:
    env = read_env(SERVER_ENV)
    url = os.environ.get("DATABASE_URL") or env.get("DATABASE_URL")
    if not url:
        raise SystemExit("No DATABASE_URL")

    if len(ITEMS) != 5:
        raise SystemExit(f"expected 5 items, got {len(ITEMS)}")

    for item in ITEMS:
        answer = item["answer"].strip()
        item["answer"] = answer
        if "—" in answer or "–" in answer:
            raise SystemExit(f"em/en dash in {item['slug']}")
        if "Related education:" not in answer:
            raise SystemExit(f"missing Related education: {item['slug']}")
        if len(answer) > MAX_CHARS:
            raise SystemExit(f"too long {item['slug']}: {len(answer)}")
        if not item.get("question_id"):
            raise SystemExit(f"missing question_id: {item['slug']}")

    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()
    updated = 0
    for item in ITEMS:
        cur.execute(
            """
            UPDATE ibdpal_reader_questions
            SET question_text = %s,
                title = %s,
                answer_text = %s,
                slug = %s,
                status = 'answered',
                published_at = COALESCE(published_at, NOW()),
                updated_at = NOW()
            WHERE question_id = %s
              AND status = 'new'
            RETURNING question_id, slug, status, source
            """,
            (
                item["question"],
                item["title"],
                item["answer"],
                item["slug"],
                item["question_id"],
            ),
        )
        out = cur.fetchone()
        if not out:
            raise SystemExit(
                f"no new row updated for question_id={item['question_id']} "
                f"slug={item['slug']} (already published or missing?)"
            )
        updated += 1
        print(
            json.dumps(
                {
                    "action": "published",
                    "id": out[0],
                    "slug": out[1],
                    "status": out[2],
                    "source": out[3],
                    "chars": len(item["answer"]),
                    "words": words(item["answer"]),
                    "approx_min_read": approx_minutes(item["answer"]),
                    "url": f"/ask/{out[1]}",
                },
                ensure_ascii=False,
            )
        )

    cur.execute(
        "SELECT status, COUNT(*)::int FROM ibdpal_reader_questions "
        "GROUP BY status ORDER BY 2 DESC"
    )
    print("updated", updated)
    print("counts", cur.fetchall())
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
