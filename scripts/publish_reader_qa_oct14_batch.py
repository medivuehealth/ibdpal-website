# -*- coding: utf-8 -*-
"""Publish Oct 14 Reader Q&A batch (12 ~10-min editorial answers).

Usage: python scripts/publish_reader_qa_oct14_batch.py
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

from _qa_oct14_part1 import ITEMS_PART1  # noqa: E402
from _qa_oct14_part2 import ITEMS_PART2  # noqa: E402
from _qa_oct14_part3 import ITEMS_PART3  # noqa: E402

ITEMS = ITEMS_PART1 + ITEMS_PART2 + ITEMS_PART3


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

    if len(ITEMS) != 12:
        raise SystemExit(f"expected 12 items, got {len(ITEMS)}")

    for item in ITEMS:
        answer = item["answer"].strip()
        item["answer"] = answer
        if len(answer) < 40 or len(answer) > MAX_CHARS:
            raise SystemExit(
                f"bad length {item['slug']}: {len(answer)} (max {MAX_CHARS})"
            )
        if "Related education:" not in answer:
            raise SystemExit(f"missing Related education: {item['slug']}")

    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()
    inserted = updated = 0
    for item in ITEMS:
        cur.execute(
            "SELECT question_id FROM ibdpal_reader_questions WHERE slug = %s LIMIT 1",
            (item["slug"],),
        )
        row = cur.fetchone()
        if row:
            cur.execute(
                """
                UPDATE ibdpal_reader_questions
                SET question_text = %s,
                    title = %s,
                    answer_text = %s,
                    status = 'answered',
                    published_at = COALESCE(published_at, NOW()),
                    updated_at = NOW()
                WHERE slug = %s
                RETURNING question_id, slug, status
                """,
                (item["question"], item["title"], item["answer"], item["slug"]),
            )
            updated += 1
            action = "updated"
        else:
            cur.execute(
                """
                INSERT INTO ibdpal_reader_questions (
                    question_text, title, answer_text, slug, source, status,
                    published_at, created_at, updated_at
                ) VALUES (%s, %s, %s, %s, 'editorial', 'answered', NOW(), NOW(), NOW())
                RETURNING question_id, slug, status
                """,
                (item["question"], item["title"], item["answer"], item["slug"]),
            )
            inserted += 1
            action = "published"
        out = cur.fetchone()
        print(
            json.dumps(
                {
                    "action": action,
                    "id": out[0],
                    "slug": out[1],
                    "status": out[2],
                    "chars": len(item["answer"]),
                    "words": words(item["answer"]),
                    "approx_min_read": approx_minutes(item["answer"]),
                    "url": f"/ask/{out[1]}",
                }
            )
        )

    cur.execute(
        "SELECT status, COUNT(*)::int FROM ibdpal_reader_questions GROUP BY status ORDER BY 2 DESC"
    )
    print("inserted", inserted, "updated", updated)
    print("counts", cur.fetchall())
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
