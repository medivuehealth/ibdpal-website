# -*- coding: utf-8 -*-
"""Publish one Reader Q&A: caregiver memory / child shrug at GI visits (~10 min).

Usage: python scripts/publish_reader_qa_cant_remember_child_symptoms.py
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
TARGET_WORDS_MIN = 1900
TARGET_WORDS_MAX = 2400

ITEM = {
    "slug": "cant-remember-child-stomach-pain-doctor-visit",
    "title": (
        "I feel like I’m failing him because I can’t remember how often his "
        "stomach hurt. How do I answer the doctor when my child shrugs?"
    ),
    "question": (
        "I feel like I’m failing him because I can’t remember how often his "
        "stomach hurt. How do I answer the doctor when my child shrugs?"
    ),
    "answer": r'''
The mother had done everything her son’s doctor asked. She had watched what he ate, paid attention when he complained of pain, and tried to remember which days were worse. But when the gastroenterologist asked her nine-year-old son how often his stomach hurt, he shrugged. She guessed.

“I feel like I’m failing him,” she wrote to IBDPal’s Reader Q&A inbox, “because I can’t remember.”

I read her email three times. I remembered being eleven, newly diagnosed with Crohn’s disease, sitting on an exam table and trying to turn two weeks of unpredictable symptoms into an answer. I knew how much could disappear between experiencing pain and explaining it.

So I revised the tracker around those questions. I replaced numerical pain scales with faces a child could select, simplified meal entries, and created a one-page summary families could bring to appointments.

Short answer: you are not failing him. A shrug from a nine-year-old, and a blank spot in a parent’s memory, are normal under chronic illness, not proof of careless parenting. What helps is a tiny, repeatable record kept close to when symptoms happen, plus a one-page visit summary, so the appointment is not a memory test. This is education for caregivers, not a diagnosis of your child and not a substitute for his gastroenterology team.

Why this moment hurts so much is worth saying plainly. Parents of children with IBD are already watching meals, bathroom trips, school absences, medicine timing, and mood. Then a calm clinical question, “How often does his stomach hurt?”, asks the brain to convert weeks of interrupted nights and half-finished lunches into a clean number. Kids often minimize, shrug, or say “I don’t know” because pain is hard to quantify, because the room is strange, or because they want the visit to end. Adults do the same thing. When I was newly diagnosed, I could feel a day clearly and still fail to translate it into clinic language. The gap is not a character flaw. It is how memory works under stress.

Guessing in the exam room does not mean you have been inattentive at home. It means the system asked for statistics without giving you a tool that fits real family life. Many clinics still open with frequency questions that assume perfect recall. Your job is not to become a walking spreadsheet. Your job is to bring a small pattern the clinician can use: better, worse, or same; night pain or not; school days missed; blood or no blood; what changed since the last visit. Those anchors beat a fake precise number invented under pressure.

A shrug from your son is clinical information too. It can mean he cannot score pain yet, he feels shy, he is protecting you, he has adapted to discomfort, or he is having a quieter day in a loud week. Do not treat the shrug as the full truth of the month. Treat it as one data point, then add caregiver observation. Pediatric IBD teams expect parents to fill in function: appetite, energy for play, bathroom urgency, nighttime waking, and whether he looks like himself. Saying “He shrugged, and here is what I observed at home” is honest advocacy, not talking over him.

Build a caregiver log that is small enough to survive a busy week. Capture five fields most days, close to when something happens:

• Pain: faces a child can tap (skip forcing 0 to 10 numbers)
• Stools: about how many, and any blood or mucus in plain words
• Night: woke for bathroom or pain? yes / no
• School or activity: full day / left early / stayed home
• Meals: a short, simple entry, not a full recipe diary
• One note: food fear, missed medicine, fever, vomiting, or “seemed fine”

That is enough for most follow-up visits. You do not need every bite, every mood, or a color-coded binder. If you miss a day, leave it blank and continue. A messy two-week strip with dates beats a perfect system abandoned after three days. In IBDPal, those same ideas show up as face-based pain, simpler meal logging, and a one-page summary you can take to clinic. Notebook versions work too; see [symptom and food tracking](/guides/track-ibd-symptoms-food) and [visit prep](/visit-prep).

Use language a child can answer. “How often does your stomach hurt?” is abstract. Try “Point to the face that matches your tummy,” or green / yellow / red days, not an interrogation after every snack. Some kids will only tell a parent in the car, not in the white-coated room. Ask him privately before the visit what he wants said out loud. Agree on a signal if he wants you to take over when the questions get hard. That respects his voice without leaving the clinician with only a shrug.

Translate memory into a one-page visit sheet the night before. Write four lines at the top:

1) Since last visit: better / worse / mixed
2) Worst stretch: dates and what it looked like (example: “Oct 6 to 11, night pain, left school twice”)
3) Current week: stools, blood, appetite, energy
4) Top three questions you need answered before you leave

Add medicines with doses, last growth numbers if you have them, and any ER or nurse-line calls. Bring two copies. When the doctor asks how often his stomach hurt, you can say, “He is not sure. On our log, pain was a lot on four school days this month, mostly evenings, and he woke twice last week.” That sentence is more useful than a guess of “maybe every other day?” invented while everyone stares at you.

Separate “cannot remember” from “did not notice.” You noticed. You watched food. You heard the complaints. What failed was storage, not love. Chronic caregiving fills working memory with logistics until the details blur. Sleep loss makes this worse. So does fear. Many parents remember the scare (blood on the toilet, a bad ER night) and lose the ordinary middle days. A two-minute nightly note protects the middle. Put the note where life already happens: phone lock screen reminder, fridge pad, or shared family calendar. If two caregivers trade evenings, decide who logs that day so the story does not split.

Food watching and symptom watching are related but not the same task. You can track meals without turning dinner into a courtroom. On rough days, jot what he ate and whether pain or urgency followed in the next few hours. On quiet days, a simple “ate normally” is fine. Patterns often show up as repeats, same late snack before night pain, same huge gap between lunch and dinner before afternoon crashes, not as a single villain food. If the clinic or a dietitian asked for diet detail, keep a short window (seven to fourteen days) rather than a lifelong novel. Pair that with [pediatric Crohn’s and colitis help](/guides/pediatric-crohns-colitis-help) and, when relevant, [child IBD diet and meeting nutrition needs](/ask/child-ibd-diet-meeting-nutrition-needs) style questions for the care team.

School is often where memory goes to hide. Ask the teacher or nurse, without sharing his whole chart, whether bathroom frequency or early pickups are showing up. A quick weekly note can fill gaps you cannot see. A 504 or health plan can support bathroom access and also leave a light trail of school interruptions. You need signal for clinic, not surveillance.

What clinicians can do with imperfect data is broader than parents fear. They combine your story with exam findings, growth curves, labs, stool tests, imaging, and endoscopy when needed. A missing exact pain count does not make the visit worthless. Clear function statements help triage: missed school, night waking, blood, weight trend, fever, vomiting, new severe pain. Lead with those. If you truly do not know stool frequency, say “I don’t know the number; I know he is up at night and avoiding lunch.” That is stronger than a polished guess.

Avoid turning the log into a second full-time job. If tracking starts to poison every meal or every car ride, shrink it again. Three fields beat ten abandoned fields. Skip public pain quizzes in front of siblings. Skip arguing about whether yesterday was a four or a five; faces and function beat fake precision. Capture direction and impact. Save deep-dives for weeks when the team asks a specific question, such as a medicine change or nutrition trial.

A practical week you can start tonight:

Day 1: Choose the five-field template and put a two-minute reminder at bedtime.
Day 2 to 3: Log without judging yourself for messy notes.
Day 4: Practice face-based pain with your son once at bedtime.
Day 5: Message school for bathroom or pickup patterns if useful.
Day 6: Draft the one-page visit summary; update it Sundays.
Day 7: Write the shrug sentence: “He’s unsure; here is our two-week pattern.”

Before the next gastroenterology visit, rehearse roles in the car. Who answers first? Which topics he wants private time to discuss with the clinician? Which three starred questions must be spoken even if the visit runs short? Bring the log highlights, not the whole archive, unless the team asks. If the portal allows, send the one-pager ahead. Related visit skills live in [how to prepare questions for a gastroenterology appointment](/ask/prepare-questions-gastroenterology-appointment) and [tracking symptoms between doctor appointments](/ask/track-symptoms-between-doctor-appointments).

Questions worth asking the care team when memory and shrugs collide: What symptoms matter most between visits for a child his age and diagnosis? What should we record daily versus only when things change? Which changes are portal-message appropriate, which need a same-day nurse call, and which are ER? How should we handle it when he minimizes pain in the room? Do you want stool counts, pain scores, school absences, or all three? Is a nurse educator or pediatric IBD dietitian available to help us set up a simple home routine? If growth or labs are the main guide right now, how do home notes still help? What does “better” look like over the next four to six weeks in concrete terms?

Red flags still override logging projects. Persistent vomiting, signs of dehydration, severe or rapidly worsening abdominal pain, heavy bleeding, black stools, fever with worsening diarrhea, unusual lethargy, or a sudden sharp weight drop needs prompt medical contact, not a prettier notebook. New obstruction-type symptoms in a child with Crohn’s, severe cramping with vomiting and trouble passing stool or gas, need urgent evaluation. If he almost stops eating or drinking, treat that as clinical, not as picky behavior. The log supports ordinary follow-up. Emergencies get the phone and the ER pathway your clinic taught you.

Emotionally, trade the story “I failed because I forgot” for “I need a system that fits a human family.” Forgetting details while carrying a child’s chronic illness is common. I have lived the patient side of that blank look on the exam table. Many caregivers live the parent side of it. Neither side means the child is unprotected. What protects him is partnership: his voice when he can give it, your observations when he cannot, and a clinic that can work with patterns instead of perfect recall.

If guilt is loud this week, write one true sentence on the visit sheet: “I am paying attention; I need help turning attention into a record.” That is not weakness. That is how good pediatric IBD care actually works. Come back to your small log and your three questions. Over a month, the bedtime note becomes ordinary, the shrug becomes less scary, and the appointment becomes a planning conversation instead of a quiz.

Related education: [Visit prep](/visit-prep), [Track IBD symptoms and food](/guides/track-ibd-symptoms-food), [Track symptoms between doctor appointments](/ask/track-symptoms-between-doctor-appointments), [Prepare questions for a gastroenterology appointment](/ask/prepare-questions-gastroenterology-appointment), [Pediatric Crohn’s and colitis help](/guides/pediatric-crohns-colitis-help), [Child IBD diet and meeting nutrition needs](/ask/child-ibd-diet-meeting-nutrition-needs).
'''.strip(),
}


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

    answer = ITEM["answer"].strip()
    ITEM["answer"] = answer
    wc = words(answer)
    if "—" in answer or "–" in answer:
        raise SystemExit("em/en dash found; remove before publish")
    if "Related education:" not in answer:
        raise SystemExit("missing Related education")
    if len(answer) > MAX_CHARS:
        raise SystemExit(f"too long: {len(answer)} chars")
    if wc < TARGET_WORDS_MIN or wc > TARGET_WORDS_MAX:
        raise SystemExit(f"word count {wc} outside {TARGET_WORDS_MIN}-{TARGET_WORDS_MAX}")

    # verify related ask slugs used in body exist when possible (soft)
    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(
        "SELECT question_id FROM ibdpal_reader_questions WHERE slug = %s LIMIT 1",
        (ITEM["slug"],),
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
            (ITEM["question"], ITEM["title"], ITEM["answer"], ITEM["slug"]),
        )
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
            (ITEM["question"], ITEM["title"], ITEM["answer"], ITEM["slug"]),
        )
        action = "published"
    out = cur.fetchone()
    print(
        json.dumps(
            {
                "action": action,
                "id": out[0],
                "slug": out[1],
                "status": out[2],
                "chars": len(ITEM["answer"]),
                "words": wc,
                "approx_min_read": approx_minutes(ITEM["answer"]),
                "url": f"/ask/{out[1]}",
            },
            ensure_ascii=False,
        )
    )
    cur.execute(
        "SELECT status, COUNT(*)::int FROM ibdpal_reader_questions GROUP BY status ORDER BY 2 DESC"
    )
    print("counts", cur.fetchall())
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
