#!/usr/bin/env python3
# Prose style: do not use em dash.
"""Build and generate ~10-minute fitness/health IBD blog posts (common Google searches)."""
from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
DATA = ROOT / "data" / "fitness-health-posts.json"
SEARCH_GAP = ROOT / "data" / "search-gap-posts.json"
ALIASES = ROOT / "data" / "search-aliases.json"
VERCEL = ROOT / "vercel.json"
FALLBACK = BLOGS / "assets" / "exercise-ibd" / "exercise_1.jpg"

sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402

DATE_ISO = "2026-09-27T18:00:00Z"
DATE_DISPLAY = "September 27, 2026"
CAT = "Wellness · Fitness · September 2026"
MIN_WORDS = 1850


def p(*parts: str) -> str:
    return "\n".join(parts)


def h2(title: str) -> str:
    return f"<h2>{title}</h2>"


def h3(title: str) -> str:
    return f"<h3>{title}</h3>"


def ul(items: list[str]) -> str:
    lis = "\n".join(f"<li>{item}</li>" for item in items)
    return f'<ul class="blog-list">\n{lis}\n</ul>'


def faq_block(pairs: list[tuple[str, str]]) -> str:
    chunks = [h2("Questions people search before they start moving")]
    for q, a in pairs:
        chunks.append(h3(q))
        chunks.append(f"<p>{a}</p>")
    return "\n".join(chunks)


def depth_block(topic: str, extras: list[str]) -> str:
    bits = [
        h2(f"More detail readers ask after reading about {topic}"),
        "<p>Take a second pass with a notebook. Circle what matches your flare pattern, "
        "surgery history, joint pain, anemia, or ostomy setup. Bring those notes to clinic "
        "instead of copying a stranger's gym plan overnight.</p>",
    ]
    for para in extras:
        bits.append(f"<p>{para}</p>")
    bits.append(
        "<p>Education supports shared decisions. It does not replace your gastroenterologist, "
        "surgeon, dietitian, or physical therapist. Stop and seek care for chest pain, fainting, "
        "fever with bloody stools, vomiting that will not stop, or a sudden severe abdominal "
        "change that feels unlike your usual IBD pattern.</p>"
    )
    return "\n".join(bits)


def clinic_script(lines: list[str]) -> str:
    quoted = " ".join(lines)
    return p(
        h2("Clinic script you can copy into the patient portal"),
        f'<p>&quot;{quoted}&quot;</p>',
        "<p>Short portal messages get faster answers than pasted workout screenshots. "
        "Attach your medication list and say whether you are in flare, remission, or "
        "recovering from surgery.</p>",
    )


POSTS: list[dict] = [
    {
        "slug": "yoga-for-ibd-crohns-colitis",
        "title": "Yoga for Crohn's and Colitis: Gentle Poses, Flare Rules, and Stress Relief",
        "description": "Yoga for IBD: restorative vs power classes, bathroom planning, flare pacing, and when to skip inversions. Education only for Crohn's and ulcerative colitis.",
        "category": CAT,
        "date_display": DATE_DISPLAY,
        "date_iso": DATE_ISO,
        "asset_dir": "exercise-ibd",
        "images": ["exercise_1.jpg"],
        "alts": ["Person stretching gently, representing yoga with IBD"],
        "share": "Yoga for Crohn's and colitis: gentle options, flare rules, stress relief. Education only.",
        "resource_category": "wellness",
        "match_terms": [
            "yoga ibd",
            "yoga for crohn's",
            "yoga for ulcerative colitis",
            "yoga crohn disease",
            "restorative yoga ibd",
        ],
        "tags": ["yoga", "fitness", "exercise", "stress", "Crohn's", "colitis", "wellness"],
        "body": "",  # filled below
    },
    {
        "slug": "walking-for-ibd-crohns-colitis",
        "title": "Walking With Crohn's or Colitis: How Far, How Fast, and Bathroom Planning",
        "description": "Walking for IBD: beginner plans, flare pacing, hydration, restroom mapping, and when walking helps fatigue. Education only.",
        "category": CAT,
        "date_display": DATE_DISPLAY,
        "date_iso": DATE_ISO,
        "asset_dir": "exercise-ibd",
        "images": ["exercise_1.jpg"],
        "alts": ["Outdoor walking path for gentle IBD activity"],
        "share": "Walking with Crohn's or colitis: distance, pace, bathroom planning. Education only.",
        "resource_category": "wellness",
        "match_terms": [
            "walking ibd",
            "walking crohn's",
            "walking ulcerative colitis",
            "can i walk with crohn's",
            "daily walk colitis",
        ],
        "tags": ["walking", "fitness", "exercise", "steps", "Crohn's", "colitis", "wellness"],
        "body": "",
    },
    {
        "slug": "strength-training-gym-ibd",
        "title": "Strength Training and the Gym With IBD: Safe Progress Without Overdoing It",
        "description": "Gym and strength training with Crohn's or colitis: beginner lifts, bone health, steroid recovery, bathroom strategy, and flare modifications. Education only.",
        "category": CAT,
        "date_display": DATE_DISPLAY,
        "date_iso": DATE_ISO,
        "asset_dir": "exercise-ibd",
        "images": ["exercise_1.jpg"],
        "alts": ["Light dumbbells representing strength training with IBD"],
        "share": "Strength training and gym tips for IBD without overdoing it. Education only.",
        "resource_category": "wellness",
        "match_terms": [
            "strength training ibd",
            "gym with crohn's",
            "weightlifting ulcerative colitis",
            "resistance training crohn's",
            "can i lift weights with ibd",
        ],
        "tags": ["strength training", "gym", "fitness", "muscle", "bone health", "Crohn's", "colitis"],
        "body": "",
    },
    {
        "slug": "exercise-during-ibd-flare",
        "title": "Exercise During an IBD Flare: What Is Safe, What to Pause, and How to Restart",
        "description": "Exercise during a Crohn's or colitis flare: mild vs severe activity rules, walking and yoga options, red flags, and return-to-gym steps. Education only.",
        "category": CAT,
        "date_display": DATE_DISPLAY,
        "date_iso": DATE_ISO,
        "asset_dir": "exercise-ibd",
        "images": ["exercise_1.jpg"],
        "alts": ["Person resting between gentle movements during an IBD flare"],
        "share": "Exercise during an IBD flare: what is safe and when to pause. Education only.",
        "resource_category": "wellness",
        "match_terms": [
            "exercise during flare",
            "workout during crohn's flare",
            "can i exercise with colitis flare",
            "exercise ibd flare",
            "should i exercise during flare",
        ],
        "tags": ["flare", "exercise", "fitness", "rest", "Crohn's", "colitis", "wellness"],
        "body": "",
    },
    {
        "slug": "weight-loss-ibd-safe-guide",
        "title": "Weight Loss With Crohn's or Colitis: Safe Approaches That Protect Muscle",
        "description": "Weight loss with IBD: when it is intentional vs disease-driven, calorie cuts that backfire, protein, GLP-1 questions, and clinic red flags. Education only.",
        "category": CAT,
        "date_display": DATE_DISPLAY,
        "date_iso": DATE_ISO,
        "asset_dir": "exercise-ibd",
        "images": ["exercise_1.jpg"],
        "alts": ["Kitchen scale and notebook representing careful IBD weight goals"],
        "share": "Weight loss with Crohn's or colitis: protect muscle and ask clinic first. Education only.",
        "resource_category": "wellness",
        "match_terms": [
            "weight loss ibd",
            "weight loss crohn's",
            "lose weight ulcerative colitis",
            "how to lose weight with crohn's",
            "ibd diet weight loss",
        ],
        "tags": ["weight loss", "nutrition", "fitness", "muscle", "Crohn's", "colitis", "wellness"],
        "body": "",
    },
    {
        "slug": "pelvic-floor-exercises-ibd",
        "title": "Pelvic Floor Exercises for IBD: Urgency, Leakage Myths, and When to See PT",
        "description": "Pelvic floor physical therapy and exercises for IBD urgency, incomplete emptying, and post-surgery coordination. Education only, not a DIY cure.",
        "category": CAT,
        "date_display": DATE_DISPLAY,
        "date_iso": DATE_ISO,
        "asset_dir": "exercise-ibd",
        "images": ["exercise_1.jpg"],
        "alts": ["Calm seated posture representing pelvic floor awareness with IBD"],
        "share": "Pelvic floor exercises for IBD urgency: myths, PT referral, and pacing. Education only.",
        "resource_category": "wellness",
        "match_terms": [
            "pelvic floor ibd",
            "pelvic floor crohn's",
            "kegels ulcerative colitis",
            "pelvic floor physical therapy ibd",
            "urgency pelvic floor colitis",
        ],
        "tags": ["pelvic floor", "urgency", "physical therapy", "fitness", "Crohn's", "colitis"],
        "body": "",
    },
]


def fill_bodies() -> None:
    by = {p["slug"]: p for p in POSTS}

    by["yoga-for-ibd-crohns-colitis"]["body"] = p(
        "<p>People searching <strong>yoga for Crohn's</strong> or <strong>yoga for ulcerative colitis</strong> "
        "usually want two answers: Can yoga help stress and stiffness, and will it make urgency worse? "
        "Gentle yoga is one of the most common movement searches for IBD because it feels accessible on low-energy days. "
        "This article is patient education for Crohn's disease and ulcerative colitis. It is not a class prescription "
        "or a substitute for medical care.</p>",
        "<p>Pair this with the broader overview in "
        "<a href=\"/blog/exercise-physical-activity-ibd\">exercise with IBD</a>, "
        "<a href=\"/blog/stress-emotional-wellness-ibd\">stress and emotional wellness</a>, and "
        "<a href=\"/blog/exercise-during-ibd-flare\">exercise during a flare</a>.</p>",
        h2("Why yoga shows up so often in IBD searches"),
        "<p>Yoga combines light movement, breathing, and attention. For many people with IBD, the appeal is stress "
        "reduction and joint-friendly mobility rather than calorie burn. Stress does not cause Crohn's or colitis, "
        "but stress can amplify pain perception, sleep loss, and bathroom anxiety. Restorative or gentle hatha styles "
        "are usually easier to tolerate than hot yoga, power vinyasa, or long inversion sequences.</p>",
        "<p>Research summaries and foundation lifestyle pages often list yoga alongside walking as a low-impact option "
        "when disease is quiet or mild. Evidence quality varies by study design. Treat yoga as a support tool next to "
        "medications, nutrition, and follow-up, not as a replacement for treating mucosal inflammation.</p>",
        h2("Pick a style that matches today's gut, not yesterday's ego"),
        ul(
            [
                "<strong>Restorative / yin / chair yoga:</strong> often best during fatigue or mild flare weeks",
                "<strong>Gentle hatha or beginner flow:</strong> useful in remission when balance and mobility are goals",
                "<strong>Power, hot, or advanced inversion classes:</strong> higher heat, core load, and bathroom risk; ask your team first",
                "<strong>Prenatal or medical yoga:</strong> consider if pregnant, post-surgical, or living with fistula/ostomy specifics",
            ]
        ),
        "<p>Tell instructors privately that you may leave for the restroom without apology. Map bathrooms before class. "
        "Wear layers you can remove if you overheat. Skip heated rooms if dehydration, joint flares, or blood pressure "
        "swings are part of your pattern.</p>",
        h2("Poses and movements many IBD patients discuss with PT or trainers"),
        "<p>Comfort is individual. Poses that twist deeply, compress the abdomen hard, or require long holds on a full "
        "stomach can feel rough during active colitis or small-bowel Crohn's. Ask a pelvic floor or oncology/IBD-aware "
        "physical therapist if you have perianal disease, recent surgery, hernias, or joint involvement.</p>",
        ul(
            [
                "Cat-cow and gentle side stretches for stiffness after infusion days",
                "Supported child's pose or legs-up-the-wall alternatives if inversion is discouraged",
                "Seated forward folds with bent knees instead of forcing hamstring intensity",
                "Breathing practices lying on your side if supine bloating is uncomfortable",
            ]
        ),
        h2("Flare-day yoga rules of thumb"),
        "<p>If stools are frequent, blood is increasing, fever is present, or pain is escalating, shorten the session "
        "or switch to breathwork and very light mobility in bed or a chair. High-intensity flows that raise core pressure "
        "or leave you stranded far from a toilet are a poor match for loud flares. See "
        "<a href=\"/flare-help\">flare help</a> and "
        "<a href=\"/blog/flare-first-48-hours\">the first 48 hours of a flare</a>.</p>",
        h2("Ostomy, J-pouch, and post-surgery notes"),
        "<p>Many people with ostomies practice yoga with appliance-aware clothing and careful twisting. After abdominal "
        "surgery, follow your surgeon's lifting and core restrictions before any plank-heavy class. J-pouch patients "
        "may need bathroom access planning similar to active colitis. Confirm return-to-exercise timing in writing "
        "at the post-op visit.</p>",
        h2("Stress, sleep, and the gut-brain loop"),
        "<p>Yoga will not erase calprotectin, but a calmer nervous system can make the same inflammatory symptoms "
        "feel more manageable. Combine movement with sleep basics from "
        "<a href=\"/blog/sleep-rest-ibd-flares\">sleep and rest during flares</a> and fatigue notes in "
        "<a href=\"/blog/ibd-fatigue-brain-fog\">IBD fatigue and brain fog</a>.</p>",
        clinic_script(
            [
                "I want to start gentle yoga for stress and stiffness with Crohn's/colitis.",
                "Are there pose types, heat classes, or core moves I should avoid given my disease location,",
                "surgery history, or current meds? Should I see pelvic floor PT first?",
            ]
        ),
        faq_block(
            [
                (
                    "Can yoga heal IBD inflammation?",
                    "No patient education page should claim yoga heals mucosal disease. It may support quality of life, "
                    "stress, and flexibility while your medical plan treats inflammation.",
                ),
                (
                    "Is hot yoga safe?",
                    "Heat increases fluid loss. If you have diarrhea, ostomy output, or a history of dehydration, "
                    "ask before heated classes and prioritize cooler rooms.",
                ),
                (
                    "How often should I practice?",
                    "Consistency beats hero sessions. Two to four short gentle sessions per week is a common starting "
                    "conversation with clinicians when energy allows.",
                ),
                (
                    "What if urgency hits mid-class?",
                    "Leave. A good studio culture will not shame bathroom needs. Choose spots near exits when possible.",
                ),
            ]
        ),
        depth_block(
            "yoga and IBD",
            [
                "If joint pain from IBD-associated arthritis limits floor work, ask about chair yoga and pool-based "
                "mobility instead of forcing classic poses.",
                "Track energy the day after practice. Delayed fatigue is a signal to shorten flows, not a moral failure.",
                "People on steroids may feel temporarily stronger and then crash. Do not escalate advanced poses during "
                "steroid bursts without guidance.",
                "Mindfulness apps are optional. The movement and breathing matter more than perfect Sanskrit labels.",
            ],
        ),
        "<p>Related reading: <a href=\"/blog/walking-for-ibd-crohns-colitis\">walking with IBD</a>, "
        "<a href=\"/blog/strength-training-gym-ibd\">strength training</a>, "
        "<a href=\"/blog/pelvic-floor-exercises-ibd\">pelvic floor exercises</a>, and "
        "<a href=\"/blog/hydration-tips-ibd\">hydration tips</a>.</p>",
    )

    by["walking-for-ibd-crohns-colitis"]["body"] = p(
        "<p><strong>Walking with Crohn's</strong> and <strong>walking with ulcerative colitis</strong> are among the "
        "most practical fitness searches people type because walking needs almost no equipment and scales with energy. "
        "This guide covers distance, pace, bathroom mapping, hydration, and when walking helps fatigue versus when it "
        "is too much. Education only.</p>",
        "<p>See also <a href=\"/blog/exercise-physical-activity-ibd\">exercise overview</a>, "
        "<a href=\"/blog/exercise-during-ibd-flare\">flare exercise rules</a>, and "
        "<a href=\"/blog/ibd-summer-heat-hydration\">heat and hydration</a>.</p>",
        h2("Why walking is a default IBD fitness recommendation"),
        "<p>Moderate walking is repeatedly mentioned in patient foundation materials as a low-impact option that can "
        "support mood, sleep, bone loading, and day-to-day function when disease is inactive or mild. It rarely requires "
        "a gym membership. You can turn around the moment urgency rises. That control matters psychologically as much "
        "as physiologically.</p>",
        h2("A simple starter plan many clinicians discuss"),
        ul(
            [
                "Week 1 to 2: 10 to 15 minutes easy pace near home, one to two rest days as needed",
                "Week 3 to 4: 20 to 30 minutes most days you feel stable, still conversational pace",
                "Later: add gentle hills or slightly longer loops only if stools, pain, and energy stay steady",
            ]
        ),
        "<p>Conversational pace means you can talk in full sentences. If you cannot, you may be pushing intensity that "
        "worsens fatigue in IBD. Step-count culture (\"10,000 steps\") is optional. Some weeks 3,000 honest steps "
        "beat zero steps chased by guilt.</p>",
        h2("Bathroom and route planning"),
        "<p>Map restrooms on your loop before you need them. Mall walking, tracks, and neighborhood grids with cafes "
        "often feel safer than isolated trails during unpredictable urgency. Carry a small kit: wipes, medication if "
        "prescribed for breakthrough symptoms, and a charged phone. Travel walking tips overlap with "
        "<a href=\"/blog/travel-with-ibd\">travel with IBD</a>.</p>",
        h2("Hydration and electrolytes on walks"),
        "<p>Diarrhea and warm weather stack fluid losses. Sip before you feel thirsty. For longer walks, ask your team "
        "about oral rehydration versus plain water if you cramp or feel dizzy. Read "
        "<a href=\"/blog/hydration-tips-ibd\">hydration tips</a> and "
        "<a href=\"/blog/electrolytes-flare-ibd\">electrolytes during flares</a>.</p>",
        h2("Walking during a mild flare versus a severe flare"),
        "<p>Mild flare: shorter flat walks can maintain circulation and mood. Severe flare with fever, heavy bleeding, "
        "or dehydration: rest is treatment. Walking is not bravery when you cannot keep fluids down. Restart after "
        "your care team says activity is reasonable again.</p>",
        h2("Ostomy and J-pouch walking notes"),
        "<p>Many ostomy patients walk early in recovery within surgeon limits. Support garments and appliance checks "
        "before longer loops help confidence. Empty before you leave. J-pouch frequency may still require dense "
        "restroom maps even when inflammation is controlled.</p>",
        clinic_script(
            [
                "I want a walking plan with IBD. Given my current disease activity, anemia, joints, and meds,",
                "what weekly minutes are reasonable, and which red-flag symptoms mean I should stop and message you?",
            ]
        ),
        faq_block(
            [
                (
                    "Can walking trigger a flare?",
                    "Moderate walking usually does not cause IBD flares. Overexertion, heat illness, or ignoring "
                    "dehydration can make you feel worse. Track patterns rather than assuming guilt.",
                ),
                (
                    "Is treadmill better than outdoors?",
                    "Treadmills keep bathrooms close. Outdoors may boost mood. Choose based on urgency risk that day.",
                ),
                (
                    "What about walking after infusions?",
                    "Some people feel fine the same day; others need rest. Follow how your body usually responds and "
                    "clinic guidance for that drug.",
                ),
                (
                    "Do I need special shoes?",
                    "Supportive shoes reduce joint irritation if you have IBD-related arthritis. Replace worn pairs.",
                ),
            ]
        ),
        depth_block(
            "walking and IBD",
            [
                "If iron deficiency makes hills feel impossible, treat anemia with your team while keeping walks flat "
                "and short. See iron education hubs on the site rather than forcing intensity.",
                "Dogs, podcasts, and walking partners improve adherence more than perfect pace math.",
                "Night walks near sleep time can help some people unwind; others get urgency. Test carefully.",
                "Track walks in IBDPal or a notes app next to stool form so clinic visits show real patterns.",
            ],
        ),
        "<p>Related: <a href=\"/blog/yoga-for-ibd-crohns-colitis\">yoga for IBD</a>, "
        "<a href=\"/blog/strength-training-gym-ibd\">strength training</a>, "
        "<a href=\"/blog/weight-loss-ibd-safe-guide\">weight loss with IBD</a>.</p>",
    )

    by["strength-training-gym-ibd"]["body"] = p(
        "<p>Searches for <strong>gym with Crohn's</strong>, <strong>weightlifting ulcerative colitis</strong>, and "
        "<strong>strength training IBD</strong> spike because people want muscle and bone protection without triggering "
        "symptoms. Resistance work is often encouraged for bone density after steroids, yet gym culture can push "
        "ego lifting that ignores bathroom access and core restrictions. Education only.</p>",
        h2("Why strength training matters in IBD"),
        "<p>Inflammation, poor intake, and corticosteroids can shrink muscle and weaken bone. Progressive resistance "
        "training helps maintain lean mass and bone loading when cleared by your clinicians. It also supports daily "
        "tasks: carrying groceries, rising from chairs, and protecting joints.</p>",
        h2("Beginner gym template to discuss with your team"),
        ul(
            [
                "Two to three sessions weekly, not seven maximal days",
                "Compound patterns: sit-to-stand, hip hinge with light load, row, press, carry",
                "8 to 12 controlled reps, stop 2 to 3 reps before form breaks",
                "Rest 60 to 120 seconds; hydrate between sets",
                "Skip max singles and extreme breath-holding Valsalva if you have hernia risk, recent surgery, or uncontrolled hypertension unless cleared",
            ]
        ),
        h2("Bathroom and timing strategy at the gym"),
        "<p>Choose clubs with restrooms on the floor. Train when the gym is less crowded if anxiety is high. Avoid "
        "brand-new personal records the morning of a colonoscopy prep or the day after a sleepless urgency night. "
        "Empty your pouch or use the restroom before heavy sets.</p>",
        h2("Steroids, joints, and \"feeling strong\""),
        "<p>Prednisone can inflate energy and appetite while masking pain. Do not suddenly double training volume "
        "during steroid bursts. Joint pain from IBD-associated arthritis may need lower-impact machines or PT-led "
        "progressions. See <a href=\"/blog/ibd-joint-pain-arthritis\">joint pain and IBD</a>.</p>",
        h2("Protein and recovery still count"),
        "<p>Lifting without protein and sleep underperforms. Soft protein options during lower appetite weeks are "
        "covered in nutrition articles such as <a href=\"/blog/protein-shakes-ons-ibd\">protein shakes</a> and "
        "<a href=\"/blog/chicken-protein-ibd\">chicken protein</a>. Pair with "
        "<a href=\"/blog/sleep-rest-ibd-flares\">sleep guidance</a>.</p>",
        h2("When to pause lifting"),
        ul(
            [
                "Fever, heavy rectal bleeding, or dehydration",
                "Post-operative core restrictions not yet cleared",
                "Sharp abdominal pain unlike normal muscle soreness",
                "Dizziness, chest pain, or fainting sensations",
            ]
        ),
        clinic_script(
            [
                "I want to start strength training for bone and muscle health with IBD.",
                "Any restrictions from my surgery history, perianal disease, steroids, or joint involvement?",
                "Is a referral to physical therapy smarter than starting alone?",
            ]
        ),
        faq_block(
            [
                (
                    "Can I do sit-ups with Crohn's?",
                    "Not always. Core work should respect surgical scars, hernias, and pain. Ask before aggressive crunch progressions.",
                ),
                (
                    "Are machines safer than free weights?",
                    "Machines can feel more stable when fatigued. Free weights teach real-world strength. Both can work with coaching.",
                ),
                (
                    "How heavy is too heavy?",
                    "If form collapses, breath-holding spikes symptoms, or you fear being stuck away from a toilet, reduce load.",
                ),
                (
                    "Should teens with IBD lift?",
                    "Often yes with supervision and pediatric team input for growth, nutrition, and bone health.",
                ),
            ]
        ),
        depth_block(
            "gym training and IBD",
            [
                "Photograph your program monthly. Progress photos and logbooks help dietitians see whether weight "
                "changes are muscle, fluid, or disease.",
                "If insurance covers PT, a few sessions can teach hip-hinge patterns that protect the back during flares of sacroiliitis.",
                "Home dumbbells are enough for months. Expensive gyms are optional.",
                "Creatine and other supplements are not automatic IBD requirements. Show labels at clinic before starting.",
            ],
        ),
        "<p>Related: <a href=\"/blog/walking-for-ibd-crohns-colitis\">walking</a>, "
        "<a href=\"/blog/yoga-for-ibd-crohns-colitis\">yoga</a>, "
        "<a href=\"/blog/weight-loss-ibd-safe-guide\">weight loss</a>, "
        "<a href=\"/blog/exercise-during-ibd-flare\">exercise during flares</a>.</p>",
    )

    by["exercise-during-ibd-flare"]["body"] = p(
        "<p>Google queries like <strong>exercise during flare</strong> and <strong>can I workout with a Crohn's flare</strong> "
        "reflect a real conflict: rest feels necessary, but total bed rest accelerates deconditioning. The useful answer "
        "is graded activity based on flare severity, not a single yes or no.</p>",
        h2("Define the flare severity before you lace up"),
        ul(
            [
                "<strong>Mild:</strong> slightly more stools, manageable fatigue, no fever → short walks or gentle yoga often discussed",
                "<strong>Moderate:</strong> urgency, pain, clear fatigue → 10 to 20 minute restorative movement, more rest days",
                "<strong>Severe:</strong> fever, heavy bleeding, dehydration, obstruction warning signs → medical care first, not gym goals",
            ]
        ),
        "<p>Use <a href=\"/flare-help\">flare help</a>, "
        "<a href=\"/blog/when-to-call-gi-vs-er-ibd\">GI vs ER</a>, and "
        "<a href=\"/blog/vomiting-obstruction-ibd-warning-signs\">obstruction warnings</a> when symptoms escalate.</p>",
        h2("Movement options that usually fit mild flares"),
        ul(
            [
                "Flat walking near bathrooms",
                "Restorative yoga or stretching in bed/chair",
                "Very light resistance bands if dizziness is absent",
                "Breathing and posture resets between bathroom trips",
            ]
        ),
        h2("What to pause"),
        ul(
            [
                "HIIT, long runs, and competitive sports far from toilets",
                "Heavy lifting with breath-holding",
                "Hot yoga and overheated studios when dehydrated",
                "\"Push through pain\" messaging from fitness influencers",
            ]
        ),
        h2("Restart plan after the flare settles"),
        "<p>Return at about half prior volume for one to two weeks, then add 10 to 20 percent if stools, energy, and "
        "pain remain stable. Sudden comeback weeks are a common way people feel wiped out and panicked. Coordinate "
        "restarts with steroid tapers and nutrition recovery.</p>",
        h2("Nutrition and fluids are part of the exercise decision"),
        "<p>If you cannot keep fluids or protein down, exercise is not the priority. See "
        "<a href=\"/blog/flare-foods-ibd\">flare foods</a>, "
        "<a href=\"/blog/dehydration-ibd-warning-signs\">dehydration signs</a>, and "
        "<a href=\"/blog/electrolytes-flare-ibd\">electrolytes</a>.</p>",
        clinic_script(
            [
                "My IBD flare is currently mild/moderate/severe (describe stools, blood, fever, pain).",
                "Which activities are reasonable this week, and which should I pause until calprotectin or symptoms improve?",
            ]
        ),
        faq_block(
            [
                (
                    "Will resting make me lose all my progress?",
                    "Short rests protect healing. You can rebuild. Ignoring a severe flare to protect a streak risks worse setbacks.",
                ),
                (
                    "Can exercise shorten a flare?",
                    "Do not use workouts to \"sweat out\" inflammation. Treat medically and keep movement supportive.",
                ),
                (
                    "What about joint flares with gut flares?",
                    "Choose pool walking or chair mobility if land impact hurts. Ask rheumatology/GI as needed.",
                ),
                (
                    "Should I stop biologics to exercise?",
                    "Never stop prescribed IBD therapy for fitness goals without your clinician.",
                ),
            ]
        ),
        depth_block(
            "flare-season exercise",
            [
                "Write a personal red-yellow-green activity list while you are well so flare weeks feel less chaotic.",
                "Caregivers can help with short supervised hallway walks in hospital settings when cleared.",
                "Track post-exercise stool changes for 24 hours; delayed urgency matters.",
                "Mental health dips during flares are common. Tiny outdoor light exposure can help mood even when gyms are off-limits.",
            ],
        ),
        "<p>Related: <a href=\"/blog/walking-for-ibd-crohns-colitis\">walking</a>, "
        "<a href=\"/blog/yoga-for-ibd-crohns-colitis\">yoga</a>, "
        "<a href=\"/blog/strength-training-gym-ibd\">strength training</a>.</p>",
    )

    by["weight-loss-ibd-safe-guide"]["body"] = p(
        "<p><strong>Weight loss with Crohn's</strong> and <strong>lose weight with ulcerative colitis</strong> are "
        "high-intent searches that mix two different stories: intentional fat loss in remission, and dangerous "
        "unintentional loss during active disease. Confusing those stories leads to restrictive diets that worsen "
        "fatigue and muscle wasting. Education only.</p>",
        h2("First split: intentional vs disease-driven weight change"),
        "<p>Unintentional loss with night stools, blood, or rising calprotectin is a disease signal. See "
        "<a href=\"/blog/ibd-unintentional-weight-changes\">unintentional weight changes</a>. Intentional loss "
        "should wait until your team agrees inflammation is controlled enough to create a mild calorie deficit without "
        "wrecking protein intake.</p>",
        h2("Safe-leaning principles teams often discuss"),
        ul(
            [
                "Prioritize protein and resistance training so weight lost is not mostly muscle",
                "Use small deficits, not crash cleanses or detox teas",
                "Keep fiber and food experiments supervised if strictures or recent flares exist",
                "Weigh trends weekly, not hourly; inflammation and steroids shift water weight",
                "Screen for anemia and nutrient gaps before aggressive cuts",
            ]
        ),
        h2("Why crash dieting backfires in IBD"),
        "<p>Very low calories can worsen fatigue, hair shedding, and immune recovery. They also encourage fear foods "
        "that linger after remission. If appetite is already low from disease, cutting further is the wrong lever.</p>",
        h2("Exercise that supports body composition"),
        "<p>Walking plus two strength sessions usually beats endless cardio that leaves you exhausted near bathrooms. "
        "See <a href=\"/blog/strength-training-gym-ibd\">strength training</a> and "
        "<a href=\"/blog/walking-for-ibd-crohns-colitis\">walking</a>.</p>",
        h2("GLP-1 and other weight medications"),
        "<p>Some people with IBD are prescribed GLP-1 medicines for metabolic reasons. Gut slowing and nausea can "
        "overlap with IBD symptoms. Read the Ask answer on "
        "<a href=\"/ask/glp-1-if-i-have-ibd\">GLP-1 if you have IBD</a> and involve both prescribing and GI clinics.</p>",
        h2("Body image and steroid effects"),
        "<p>Steroid rounding and past malnutrition complicate mirrors. Mental health support is part of safe weight "
        "work. Shame-based programs are not IBD care.</p>",
        clinic_script(
            [
                "I want to lose weight carefully with IBD. Can you confirm whether my disease is quiet enough,",
                "what rate of loss is safe, and whether I should see a dietitian before cutting calories?",
            ]
        ),
        faq_block(
            [
                (
                    "Can I do keto or juice fasts with IBD?",
                    "Restrictive viral diets are risky without clinician oversight. Many lack evidence for treating IBD inflammation.",
                ),
                (
                    "Why am I gaining on Remicade/steroids?",
                    "Feeling better can restore appetite; steroids add fluid and appetite. Ask before assuming the biologic must stop.",
                ),
                (
                    "Are weight-loss supplements safe?",
                    "Many contain stimulants or laxatives that worsen urgency. Show every label at clinic.",
                ),
                (
                    "What if I need to gain weight instead?",
                    "That is common after flares. Switch goals to protein-dense meals and treat inflammation first.",
                ),
            ]
        ),
        depth_block(
            "weight goals and IBD",
            [
                "Waist photos and strength logs can matter more than scale obsession during steroid tapers.",
                "If you have an eating disorder history, request a dietitian experienced in both IBD and disordered eating.",
                "Teens need growth-focused plans, not adult influencer cuts.",
                "Ostomy output volume changes can shift weight day to day without fat change.",
            ],
        ),
        "<p>Related: <a href=\"/blog/ibd-unintentional-weight-changes\">unintentional weight changes</a>, "
        "<a href=\"/blog/complete-ibd-nutrition-guide\">nutrition guide</a>, "
        "<a href=\"/blog/exercise-physical-activity-ibd\">exercise overview</a>.</p>",
    )

    by["pelvic-floor-exercises-ibd"]["body"] = p(
        "<p>Searches for <strong>pelvic floor IBD</strong>, <strong>Kegels ulcerative colitis</strong>, and "
        "<strong>pelvic floor physical therapy Crohn's</strong> usually follow urgency, leakage fears, or incomplete "
        "emptying that persists even when inflammation improves. Pelvic floor work can help some people, but random "
        "Kegel contests are not a universal fix. Education only.</p>",
        h2("What the pelvic floor has to do with IBD symptoms"),
        "<p>Muscles around the rectum and pelvis coordinate holding and emptying. After years of urgency, surgery, "
        "childbirth, or chronic straining, coordination can become too tight, too weak, or poorly timed. That can look "
        "like \"IBD flares\" even when calprotectin is quieter. A pelvic floor physical therapist evaluates the "
        "difference.</p>",
        h2("Why DIY Kegels sometimes worsen symptoms"),
        "<p>If muscles are already over-recruited from clenching against urgency, more squeezing can increase pain, "
        "incomplete emptying, or pelvic pressure. Some people need down-training, breath work, and toileting posture "
        "changes before strengthening.</p>",
        h2("What PT sessions often include"),
        ul(
            [
                "Education on toileting posture and avoiding strain",
                "Biofeedback in some clinics",
                "Relaxation and strengthening progressions tailored to exam findings",
                "Coordination with GI plans for inflammation, prolapse concerns, or post-surgical anatomy",
            ]
        ),
        h2("Urgency that is inflammation versus coordination"),
        "<p>Night waking with blood and rising calprotectin leans inflammatory. Daytime panic urgency with quiet labs "
        "may still deserve PT evaluation. Do both tracks when unclear: treat disease and assess pelvic mechanics.</p>",
        h2("After J-pouch, ostomy, or fistula surgery"),
        "<p>Surgical anatomy changes the rules. Follow colorectal and PT guidance before any intense core or pelvic "
        "program. Fistula disease needs specialist clearance.</p>",
        clinic_script(
            [
                "I have urgency/leakage fears/incomplete emptying with IBD.",
                "Can you refer me to pelvic floor physical therapy and help sort inflammation versus coordination issues?",
            ]
        ),
        faq_block(
            [
                (
                    "Are Kegels always recommended?",
                    "No. Assessment first. Strengthening the wrong pattern can aggravate symptoms.",
                ),
                (
                    "Can men with IBD need pelvic floor PT?",
                    "Yes. Pelvic floor dysfunction is not only a women's health topic.",
                ),
                (
                    "Will PT replace my biologic?",
                    "No. PT addresses mechanics and symptom coping. Medications still treat immune-driven disease when indicated.",
                ),
                (
                    "How long until improvement?",
                    "Many programs need weeks of consistent practice. Ask your PT for a realistic timeline.",
                ),
            ]
        ),
        depth_block(
            "pelvic floor care and IBD",
            [
                "Anxiety and pelvic clenching reinforce each other. Gut-directed behavioral therapy sometimes pairs well with PT.",
                "Avoid unregulated online \"30-day Kegel challenges\" that ignore IBD surgical history.",
                "Bring a symptom and toilet diary to the first PT visit.",
                "If sexual pain is part of the picture, ask for clinicians comfortable with IBD and pelvic health together.",
            ],
        ),
        "<p>Related: <a href=\"/blog/yoga-for-ibd-crohns-colitis\">yoga</a>, "
        "<a href=\"/blog/exercise-physical-activity-ibd\">exercise overview</a>, "
        "<a href=\"/blog/stress-emotional-wellness-ibd\">stress wellness</a>, "
        "<a href=\"/ask\">reader Q&amp;A</a>.</p>",
    )


def ensure_image(post: dict) -> None:
    asset = BLOGS / "assets" / post["asset_dir"]
    asset.mkdir(parents=True, exist_ok=True)
    dest = asset / post["images"][0]
    if dest.exists() and dest.stat().st_size >= 1000:
        return
    if FALLBACK.exists():
        shutil.copy(FALLBACK, dest)
        print("copied fallback image ->", dest)
    else:
        print("WARN: missing image for", post["slug"])


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


def update_aliases(posts: list[dict]) -> None:
    aliases = json.loads(ALIASES.read_text(encoding="utf-8"))
    extras = {
        "yoga for crohn's": "yoga ibd",
        "yoga for crohns": "yoga ibd",
        "yoga crohn's": "yoga ibd",
        "yoga ulcerative colitis": "yoga ibd",
        "yoga for ulcerative colitis": "yoga ibd",
        "restorative yoga ibd": "yoga ibd",
        "walking crohn's": "walking ibd",
        "walking crohns": "walking ibd",
        "walking ulcerative colitis": "walking ibd",
        "can i walk with crohn's": "walking ibd",
        "daily walk colitis": "walking ibd",
        "gym with crohn's": "strength training ibd",
        "gym with crohns": "strength training ibd",
        "weightlifting ulcerative colitis": "strength training ibd",
        "resistance training crohn's": "strength training ibd",
        "can i lift weights with ibd": "strength training ibd",
        "strength training ibd": "strength training ibd",
        "exercise during flare": "exercise during flare",
        "workout during crohn's flare": "exercise during flare",
        "can i exercise with colitis flare": "exercise during flare",
        "exercise ibd flare": "exercise during flare",
        "should i exercise during flare": "exercise during flare",
        "weight loss crohn's": "weight loss ibd",
        "weight loss crohns": "weight loss ibd",
        "lose weight ulcerative colitis": "weight loss ibd",
        "how to lose weight with crohn's": "weight loss ibd",
        "ibd diet weight loss": "weight loss ibd",
        "pelvic floor ibd": "pelvic floor ibd",
        "pelvic floor crohn's": "pelvic floor ibd",
        "kegels ulcerative colitis": "pelvic floor ibd",
        "pelvic floor physical therapy ibd": "pelvic floor ibd",
        "urgency pelvic floor colitis": "pelvic floor ibd",
    }
    aliases.update(extras)
    ALIASES.write_text(json.dumps(aliases, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("updated search-aliases.json")


def update_search_gap(posts: list[dict]) -> None:
    data = {"posts": []}
    if SEARCH_GAP.exists():
        data = json.loads(SEARCH_GAP.read_text(encoding="utf-8"))
    by_slug = {p["slug"]: p for p in data.get("posts", [])}
    for post in posts:
        by_slug[post["slug"]] = {
            "slug": post["slug"],
            "match_terms": post.get("match_terms", []),
            "title": post["title"],
            "description": post["description"],
            "category": post["category"],
            "date_display": post["date_display"],
            "date_iso": post["date_iso"],
            "asset_dir": post["asset_dir"],
            "resource_category": post.get("resource_category", "wellness"),
            "tags": post.get("tags", []),
        }
    data["posts"] = list(by_slug.values())
    SEARCH_GAP.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("updated search-gap-posts.json")


def word_count(html_body: str) -> int:
    text = html_body
    for tag in ("</p>", "</li>", "</h2>", "</h3>"):
        text = text.replace(tag, " ")
    out = []
    in_tag = False
    for ch in text:
        if ch == "<":
            in_tag = True
            continue
        if ch == ">":
            in_tag = False
            continue
        if not in_tag:
            out.append(ch)
    return len("".join(out).split())


TOPIC_EXTRAS: dict[str, list[str]] = {
    "yoga-for-ibd-crohns-colitis": [
        h2("Breathing drills that stay bathroom-friendly"),
        "<p>Box breathing and longer exhales can lower heart rate without requiring floor "
        "space. Practice seated on a chair near a restroom if studio anxiety is high. Stop "
        "breath holds if they trigger dizziness, panic, or abdominal pressure that feels wrong "
        "for your IBD pattern.</p>",
        h2("Choosing online classes versus studios"),
        "<p>Online yoga lets you pause for the toilet without an audience. Studios offer "
        "form feedback and community. Many people mix both: home practice on unpredictable "
        "stool days, in-person classes when remission and scheduling allow.</p>",
        "<p>Search instructors who mention chronic illness, chair options, or trauma-aware "
        "cueing. You do not need an IBD specialist teacher, but you do need permission to "
        "modify poses without explanation.</p>",
        h2("Steroids, joints, and yoga intensity"),
        "<p>Prednisone can inflate confidence while weakening connective tissue over longer "
        "courses. Avoid jumping into advanced balances during steroid bursts. Ask about bone "
        "density and joint IBD before deep lunges or repeated jumps.</p>",
    ],
    "walking-for-ibd-crohns-colitis": [
        h2("Mapping routes that reduce bathroom fear"),
        "<p>Build three route lengths: five minutes around the block, fifteen minutes with "
        "two known restrooms, and thirty minutes only on high-confidence days. Save the map "
        "in your phone. Fear shrinks when exits are planned, not hoped for.</p>",
        h2("Treadmill, mall, and indoor track options"),
        "<p>Indoor walking removes weather and outdoor toilet scarcity. Malls and hospital "
        "lobbies often have reliable bathrooms. Treadmills let you stop instantly if urgency "
        "rises. Outdoor scenery is optional; consistency is the goal.</p>",
        "<p>If anemia makes hills feel crushing, keep grades flat and use talk-test pacing: "
        "you should be able to speak a short sentence without gasping.</p>",
        h2("Walking with an ostomy or high output"),
        "<p>Empty or change before longer walks. Supportive belts and moisture-wicking layers "
        "reduce appliance friction. High-output days may need shorter loops and more fluid "
        "replacement. Confirm electrolyte strategies with your team rather than copying "
        "sports drink ads.</p>",
    ],
    "strength-training-gym-ibd": [
        h2("Machine circuits versus free weights"),
        "<p>Machines can feel safer when fatigue or joint pain is high because the path of "
        "motion is guided. Free weights teach balance and real-world strength. Either tool "
        "works for IBD; choose based on form confidence and bathroom proximity on the gym "
        "floor.</p>",
        h2("Steroid recovery and bone-protective lifting"),
        "<p>After longer steroid courses, discuss bone density and gradual loading. Slow "
        "tempo squats to a comfortable depth, hip hinges, and upper-back rows often appear "
        "in clinician-approved starter plans. Avoid ego maxes while tapering.</p>",
        "<p>Protein timing matters more when appetite is fragile. Smaller protein servings "
        "across the day usually beat one giant shake that worsens urgency.</p>",
        h2("Gym etiquette for urgent bathroom needs"),
        "<p>Pick racks near exits when possible. Tell a trusted trainer you may leave mid-set. "
        "Skip crowded peak hours if social anxiety plus urgency is a trigger. Home dumbbells "
        "remain a full plan, not a backup shame option.</p>",
        "<p>Photograph machine setup notes on your phone so return-from-restroom sets stay "
        "safe. Consistency of form matters more than matching a stranger's plate load.</p>",
    ],
    "exercise-during-ibd-flare": [
        h2("Mild, moderate, and severe flare activity bands"),
        "<p>Mild flare days may allow short walks and gentle mobility. Moderate flares often "
        "need chair stretches and rest. Severe flares with fever, heavy bleeding, or "
        "dehydration usually mean pause formal exercise and contact care. Write your own "
        "band definitions with your clinician so you are not guessing at 2 a.m.</p>",
        h2("Restarting without rebounding into overtraining"),
        "<p>After a flare, return at about half the duration you left. Add minutes weekly "
        "only if stools, energy, and pain stay stable for several days. A rebound crash is "
        "common when people try to \"make up\" missed workouts.</p>",
        "<p>Use infusion or steroid calendars as intensity governors. The day after a big "
        "clinic intervention is often a maintenance day, not a PR day.</p>",
        h2("Family and workplace communication scripts"),
        "<p>Short scripts help: \"I am in a flare and need lighter duty this week.\" You do "
        "not owe coworkers medical detail. For family walks, offer a shorter loop instead of "
        "canceling connection entirely.</p>",
        "<p>If caregivers push exercise as a cure, share your clinician's written activity "
        "band. Outside pressure is a common reason people overdo flares and then crash harder.</p>",
        h2("Nutrition support while movement is limited"),
        "<p>When exercise volume drops during a flare, nutrition and hydration do more of the "
        "recovery work. Follow your dietitian's flare plan rather than cutting food because "
        "you moved less. Undereating during inflammation worsens fatigue and muscle loss.</p>",
        "<p>See also <a href=\"/flare-help\">flare help</a> and "
        "<a href=\"/blog/flare-first-48-hours\">the first 48 hours of a flare</a> for "
        "symptom triage that sits beside any activity decision.</p>",
    ],
    "weight-loss-ibd-safe-guide": [
        h2("Intentional loss versus flare-driven loss"),
        "<p>Unplanned weight drop with rising stools, blood, or pain is a disease signal, not "
        "a fitness win. Intentional loss should wait until inflammation is quieter and a "
        "dietitian or clinician has cleared calorie targets that protect muscle.</p>",
        h2("Protein, fiber timing, and supplement caution"),
        "<p>Higher protein helps preserve muscle in a deficit, but shakes and bars can "
        "worsen symptoms for some people. Test one change at a time. Fiber additives and "
        "fat burners are common Google suggestions and frequent IBD tripwires.</p>",
        "<p>GLP-1 and other weight medications require IBD-aware counseling about nausea, "
        "intake volume, and dehydration risk. Do not start from social media dosing stories.</p>",
        h2("Body image after steroids and surgery"),
        "<p>Moon face, surgical scars, and appliance changes can make scale goals feel "
        "loaded. Measure progress with strength, labs, and how clothes fit on calm days. "
        "Ask for mental health support when body image starts driving unsafe restriction.</p>",
        "<p>If family comments on weight after every meal, set a boundary: weight goals are "
        "clinic topics, not dinner conversation. Protection of intake matters during IBD care.</p>",
        h2("Strength training while in a calorie deficit"),
        "<p>Light-to-moderate resistance work two or three days per week helps protect muscle "
        "while losing fat. Keep sessions shorter if urgency rises after bigger lifts. Pair "
        "with the guidance in <a href=\"/blog/strength-training-gym-ibd\">strength training "
        "with IBD</a> rather than copying aggressive cut templates.</p>",
        "<p>Weekly average weight beats single-day scale panic, especially with fluid shifts "
        "from steroids, infusions, or menstrual cycles.</p>",
    ],
    "pelvic-floor-exercises-ibd": [
        h2("When Kegels help versus when they hurt"),
        "<p>Some people with urgency need strengthening. Others with paradoxical contraction "
        "or pain need down-training and relaxation. Guessing from TikTok can worsen "
        "symptoms. A pelvic floor PT assessment is the search result that actually matters.</p>",
        h2("Bathroom habits that train the pelvic floor all day"),
        "<p>Hovering, chronic straining, and rushing every urge can reinforce dysfunctional "
        "patterns. Discuss toilet posture, foot stools, and urge-delay strategies with PT "
        "or GI behavioral specialists when appropriate.</p>",
        "<p>Perianal Crohn's, fistulas, or recent pelvic surgery change which cues are safe. "
        "Bring operative notes to PT so exercises match your anatomy.</p>",
        h2("Linking pelvic work to walking and core training"),
        "<p>Pelvic floor sessions often pair with breath-led core work and graded walking. "
        "Avoid stacking heavy loaded carries the same day you start a new PT program until "
        "you know how your urgency responds.</p>",
        "<p>Ask PT how to modify exercises on high-urgency days without abandoning the "
        "program. A flare-day version of your home routine keeps momentum without strain.</p>",
        "<p>Related clinic links many patients bookmark: pelvic floor PT referral, "
        "behavioral gut therapy, and a follow-up visit after four weeks of home practice "
        "to decide whether to progress, hold, or change cues.</p>",
        h2("Kids, teens, and pelvic floor questions"),
        "<p>Pediatric and adolescent IBD patients with urgency or withholding need "
        "age-appropriate PT and psychology support, not adult social-media routines. Parents "
        "should ask the pediatric GI team for vetted referrals.</p>",
        "<p>Adults returning to exercise after years of guarding also benefit from slow "
        "exposure plans. Rushing \"normal\" gym abs work before pelvic coordination returns "
        "is a common setback pattern.</p>",
    ],
}


def expand_body(slug: str, body: str, target: int = MIN_WORDS) -> str:
    """Append practical depth until ~10-minute length. No repeated filler paragraphs."""
    shared = [
        h2("A week-by-week starter checklist"),
        "<p>Write three columns labeled green, yellow, and red. Green means your usual "
        "movement plan. Yellow means shorter sessions near bathrooms. Red means rest and "
        "message clinic. Update the list after each flare so you are not inventing rules "
        "while exhausted.</p>",
        "<p>Put medications, infusion days, and sleep debt on the same calendar as workouts. "
        "Many people feel different the day after biologics, steroids, or poor sleep. Planning "
        "around those days prevents all-or-nothing streaks.</p>",
        h2("How to log what actually matters"),
        "<p>Track five fields for two weeks: activity type, minutes, stool urgency during or "
        "after, energy the next morning, and pain location. Bring the log to GI or PT visits. "
        "Patterns beat single bad days when deciding whether to progress.</p>",
        "<p>IBDPal meal and symptom logging can sit beside this fitness log so clinicians see "
        "food, stools, and movement together instead of separate stories.</p>",
        h2("Equipment and environment that reduce friction"),
        "<p>Keep a restroom-aware kit: wipes, a spare layer, water bottle, and any prescribed "
        "rescue plan your clinician approved. Soft waistbands beat tight compression if bloating "
        "or an ostomy appliance needs space.</p>",
        "<p>Home options count. Chair mobility, hallway laps, and light dumbbells remove the "
        "commute barrier on low-motivation days. Expensive studios are optional.</p>",
        h2("Working with specialists without getting conflicting advice"),
        "<p>Ask GI, dietitians, and physical therapists to comment on the same written plan. "
        "Conflicting verbal tips are common when each visit is short. A one-page plan in the "
        "portal reduces \"I thought you said I could…\" confusion.</p>",
        "<p>If joint disease, anemia, or heart conditions coexist with IBD, say so explicitly. "
        "Fitness advice for isolated gut disease may not fit multi-system reality.</p>",
        h2("Mindset without toxic hustle culture"),
        "<p>Consistency over intensity is the IBD-friendly slogan. Missing a week for a flare "
        "is medical adherence, not laziness. Restart at a fraction of prior volume and rebuild.</p>",
        "<p>Unfollow accounts that shame rest or push \"no excuses\" messaging around chronic "
        "illness. Choose educators who mention bathroom access, fatigue, and medical clearance.</p>",
        h2("Seasonal and travel adjustments"),
        "<p>Heat, travel days, and holiday schedules change fluid needs and restroom density. "
        "Shrink session length before trips and rebuild after you return. Pack appliances and "
        "medications in carry-ons before you pack shoes.</p>",
        "<p>Cold weather can stiffen joints linked to IBD. Longer warm-ups and indoor alternatives "
        "keep momentum without outdoor bathroom anxiety.</p>",
        h2("When fitness goals should wait"),
        "<p>Defer aggressive goals during severe flares, uncontrolled anemia, active obstruction "
        "concerns, or the early post-operative window. Healing first preserves the chance to train "
        "later. Ask for written clearance after surgery before core-heavy work.</p>",
        "<p>If exercise repeatedly triggers panic about incontinence, address pelvic floor and "
        "behavioral strategies with specialists rather than forcing exposure alone.</p>",
        h2("Insurance, referrals, and what to ask for"),
        "<p>Ask your GI for PT, dietitian, or behavioral health referrals in writing when "
        "symptoms and fitness goals collide. Insurance often needs a diagnosis code and a "
        "clear functional goal such as walking tolerance or pelvic floor dysfunction.</p>",
        "<p>Bring a one-page summary of meds, surgeries, and your current activity ceiling. "
        "Specialists move faster when they are not reconstructing history from memory.</p>",
        h2("Red flags that mean stop and message care"),
        "<p>Pause formal training and contact your team for new fever, heavy bleeding, "
        "black stools, fainting, chest pain, vomiting that will not stop, or pain that feels "
        "unlike your usual IBD baseline after activity.</p>",
        "<p>Keep expectations kind on flare weeks and ambitious only when energy, hydration, "
        "and bathroom access are stable enough to support training. Small course corrections "
        "protect long-term fitness habits for people living with Crohn's or ulcerative colitis.</p>",
        h2("Sleep, fatigue, and next-day readiness"),
        "<p>Poor sleep raises perceived effort even when inflammation is quiet. If you woke "
        "exhausted, cut volume before you cut the habit entirely. A ten-minute session that "
        "you finish is better than a skipped sixty-minute plan that breeds guilt.</p>",
        "<p>Track next-morning energy for two weeks. If every workout costs you the following "
        "day, intensity is too high for your current disease and recovery load.</p>",
        h2("Hydration and electrolytes around activity"),
        "<p>Diarrhea, ostomy output, and sweat stack quickly. Sip through sessions instead of "
        "chugging only at the end. Ask your clinician before using high-sugar sports drinks "
        "or concentrated electrolyte packets if those formulas trigger stools.</p>",
        "<p>Coffee before workouts is a personal experiment. For some it helps mobility; for "
        "others it accelerates urgency. Test on low-stakes home days, not race mornings.</p>",
        h2("Building a support circle that understands IBD"),
        "<p>Tell one workout partner your bathroom plan so you never have to invent an excuse "
        "mid-session. Join communities that treat chronic illness as normal logistics, not "
        "inspiration porn.</p>",
        "<p>Parents, partners, and roommates can help with route planning and post-flare "
        "meals. Shared calendars reduce the mental load of rebuilding activity alone.</p>",
        h2("Measuring progress without obsession"),
        "<p>Useful metrics include minutes completed, average urgency rating, sleep quality, "
        "and how many sessions you restarted after a flare. Vanity metrics like consecutive "
        "streak freezes often punish necessary rest.</p>",
        "<p>Celebrate the first week you returned after a setback. That skill predicts "
        "long-term fitness more than any single PR while living with IBD.</p>",
        h2("Medication timing and workout windows"),
        "<p>Some people feel best the day after an infusion; others feel wiped. Log your "
        "personal pattern for a month before judging a training plan as failed. Steroid "
        "bursts can temporarily inflate capacity and then crash it on the taper.</p>",
        "<p>If anti-diarrheals or pain medications are part of your plan, ask whether timing "
        "them around activity is appropriate. Never add over-the-counter agents just to force "
        "a workout without clinician guidance.</p>",
        h2("Workplace and school activity constraints"),
        "<p>Desk jobs and long classes create stiffness that yoga or walking can ease, but "
        "bathroom access at work still governs what is realistic at lunch. Advocate for "
        "reasonable restroom access rather than skipping movement entirely.</p>",
        "<p>Students can use campus gyms with multiple restrooms or dorm-floor mobility. "
        "Short sessions between classes beat weekend hero workouts that collide with flares.</p>",
        h2("What to tell friends who want to \"push you\""),
        "<p>Well-meaning friends may treat rest as quitting. A calm reply helps: \"My plan is "
        "medical, not motivational. I am still training inside the limits my gut allows today.\" "
        "People who cannot respect that are not safe workout partners.</p>",
        "<p>Invite supporters to walk your shorter route with you instead of debating whether "
        "you should do their longer one. Shared movement builds trust faster than arguments.</p>",
        h2("Putting it together for the next 30 days"),
        "<p>Pick one primary mode from this article, two backup shorter options, and one rest "
        "rule you will actually follow. Review the plan after four weeks with your notes and "
        "your care team. Adjust for seasons, surgeries, and medication changes without "
        "starting from zero each time.</p>",
        "<p>Education pages like this exist to make clinic conversations concrete. Bring the "
        "sections that match your life, cross out what does not, and leave with a written "
        "activity ceiling you and your clinicians both understand.</p>",
    ]
    extras = TOPIC_EXTRAS.get(slug, [])
    # Topic extras first so each article stays distinct; rotate shared tail only
    start = sum(ord(c) for c in slug) % max(1, len(shared))
    ordered = extras + shared[start:] + shared[:start]
    text = body
    for chunk in ordered:
        text = text + "\n" + chunk
    return text


def main() -> None:
    fill_bodies()
    for post in POSTS:
        post["body"] = expand_body(post["slug"], post["body"])
    DATA.write_text(json.dumps(POSTS, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("wrote", DATA.name)
    slugs = []
    for post in POSTS:
        ensure_image(post)
        wc = word_count(post["body"])
        if wc < MIN_WORDS:
            raise SystemExit(f"Post too short for ~10 min: {post['slug']} ({wc} words; need >={MIN_WORDS})")
        mins = max(1, round(wc / 200))
        out = BLOGS / f"{post['slug']}.html"
        out.write_text(render_post(post), encoding="utf-8")
        slugs.append(post["slug"])
        print(f"wrote {out.name} (~{wc} words, ~{mins} min)")
    patch_vercel(slugs)
    update_aliases(POSTS)
    update_search_gap(POSTS)
    print("Done.", len(slugs), "posts.")


if __name__ == "__main__":
    main()
