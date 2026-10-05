#!/usr/bin/env python3
# Prose style: do not use em dash.
"""Generate Oct 2026 search-gap blogs: mango + abdominal/stomach pain."""
from __future__ import annotations

import json
import re
import shutil
import ssl
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
DATA = ROOT / "data" / "oct2026-search-gap-posts.json"
SEARCH_GAP = ROOT / "data" / "search-gap-posts.json"
ALIASES = ROOT / "data" / "search-aliases.json"
VERCEL = ROOT / "vercel.json"
FALLBACK = BLOGS / "assets" / "low-residue" / "low-residue_1.jpg"

sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402

DATE_ISO = "2026-10-04T18:00:00Z"
DATE_DISPLAY = "October 4, 2026"
MIN_WORDS = 1000

IMAGE_URLS = {
    "mango-ibd": "https://images.unsplash.com/photo-1553279768-865429fa0078?auto=format&w=1200&q=80",
    "abdominal-pain-ibd": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&w=1200&q=80",
}


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


POSTS: list[dict] = [
    {
        "slug": "mango-ibd-crohns-colitis",
        "title": "Mango and IBD: Fiber, Sugar, Flare Tips, and When It Fits",
        "description": "Mango with Crohn's or ulcerative colitis: ripe vs green, fiber and FODMAP notes, flare tips, and dietitian questions. Education only.",
        "category": "Nutrition · October 2026",
        "date_display": DATE_DISPLAY,
        "date_iso": DATE_ISO,
        "asset_dir": "mango-ibd",
        "images": ["mango-ibd_1.jpg"],
        "alts": ["Sliced ripe mango representing IBD food questions"],
        "share": "Mango and IBD: fiber, sugar, flare tips. Education only.",
        "resource_category": "nutrition",
        "match_terms": [
            "mango",
            "mango ibd",
            "mango crohn",
            "mango crohn's",
            "mango colitis",
            "mango ulcerative colitis",
            "can i eat mango with crohn's",
        ],
        "tags": ["mango", "fruit", "nutrition", "FODMAP", "Crohn's", "colitis", "flare"],
        "body": """
<p>People searching <strong>mango IBD</strong>, <strong>mango Crohn's</strong>, or <strong>mango ulcerative colitis</strong> usually want a clear answer: Is mango safe, or will it trigger urgency? Tolerance is individual. This page is patient education for Crohn's disease and ulcerative colitis. It is not a diet prescription.</p>
<p>Pair this with <a href="/blog/flare-foods-ibd">flare foods</a>, <a href="/blog/crohns-diet-overview-ibd">Crohn's diet overview</a>, <a href="/blog/fodmap-diet-crohns-colitis">FODMAP overview</a>, and the <a href="/ibd-nutrition">IBD nutrition hub</a>.</p>

<h2>Why mango shows up in IBD food searches</h2>
<p>Mango is sweet, juicy, and common in many cuisines. It also carries fiber, natural sugar, and volume. During quiet remission, many people enjoy small ripe portions. During active colitis or small-bowel Crohn's, fruit sugar and fiber can speed transit or increase gas. Searchers want flare-versus-remission rules of thumb, not a forever ban.</p>

<h2>Nutrition snapshot</h2>
<p>A typical cup of diced ripe mango provides vitamin C, vitamin A precursors, potassium, and mostly carbohydrate with moderate fiber. Exact amounts vary by variety and ripeness. Green mango is firmer and more acidic. Dried mango concentrates sugar and portion size quickly.</p>
<ul class="blog-list">
<li><strong>Macros:</strong> mostly carbohydrate; low fat and protein</li>
<li><strong>Fiber:</strong> present in flesh; skins add more roughage</li>
<li><strong>FODMAP notes:</strong> ripe mango can be higher FODMAP at larger servings for some people; portion size matters</li>
<li><strong>Electrolytes:</strong> potassium can help on low-intake days if tolerated</li>
</ul>

<h2>Flare versus remission</h2>
<h3>During a louder flare</h3>
<ul class="blog-list">
<li>Many teams prefer lower-fiber, lower-volume fruits first (see <a href="/blog/banana-ibd-crohns-colitis">bananas</a> or cooked soft options)</li>
<li>If you try mango, start with a few ripe cubes without skin, well chewed</li>
<li>Skip large smoothies that dump a whole fruit's sugar at once</li>
<li>Avoid dried mango strips as a "healthy snack" during urgency weeks</li>
</ul>
<h3>In quieter remission</h3>
<ul class="blog-list">
<li>Ripe mango can fit Mediterranean-style variety for some people</li>
<li>Test one serving size and log symptoms for 24 to 48 hours</li>
<li>Pair with a protein or fat source if pure fruit sugar feels racy</li>
<li>Ask about strictures before fibrous skins or large fibrous bites</li>
</ul>

<h2>Prep ideas that often feel kinder</h2>
<p>Peel fully. Cut into small cubes. Serve ripe rather than firm green if acidity bothers you. Puree into a thin sauce over rice or yogurt if chewing volume is hard. Freeze tiny cubes for slow snacking rather than drinking a large blended portion in one sitting.</p>

<h2>Common myths</h2>
<ul class="blog-list">
<li><strong>"Tropical fruit is always bad for IBD."</strong> Not for everyone. Location of disease, fiber load, and portion decide more than the word tropical.</li>
<li><strong>"If mango once caused urgency, never again."</strong> Re-test carefully in remission with your team. Timing, portion, and disease activity change tolerance.</li>
<li><strong>"Dried mango is the same as fresh."</strong> Drying concentrates sugar and makes overeating easy.</li>
</ul>

<h2>How to track mango with IBDPal</h2>
<p>Log ripeness, peeled versus with skin, portion (cups or grams), and symptoms for a day or two. Patterns beat memory at clinic visits. See <a href="/blog/tracking-food-symptoms-ibdpal">tracking food and symptoms</a>.</p>

<h2>Clinic script</h2>
<p>&quot;I want to know if small amounts of ripe peeled mango fit my Crohn's/colitis plan in flare versus remission. Any portion limits given my disease location or FODMAP guidance?&quot;</p>

<h2>Questions people search</h2>
<h3>Can I eat mango during a flare?</h3>
<p>Many people wait until stools calm. If your team allows fruit trials, use tiny ripe peeled portions and stop if pain or urgency rises.</p>
<h3>Is mango high FODMAP?</h3>
<p>Serving size matters. Ask a dietitian for your personal FODMAP plan rather than copying a chart alone.</p>
<h3>What about mango juice or lassi?</h3>
<p>Juice removes fiber but keeps sugar. Dairy lassi adds lactose for some. Test components separately when possible.</p>

<h2>When food questions become urgent</h2>
<p>Contact care promptly for severe pain, vomiting, inability to keep fluids down, heavy bleeding, fever, or rapid weight loss. See <a href="/flare-help">flare help</a> and <a href="/blog/when-to-go-er-ibd">when to go to the ER</a>.</p>
<p>Related: <a href="/blog/melon-ibd">melon</a> · <a href="/blog/grapes-ibd">grapes</a> · <a href="/blog/strawberries-ibd">strawberries</a> · <a href="/eating-with-ibd">Eating With IBD book</a> · <a href="/resources">resource library</a>.</p>

<h2>Portion ideas people actually use</h2>
<ul class="blog-list">
<li><strong>Tiny trial:</strong> 2 to 4 peeled ripe cubes with a bland starch</li>
<li><strong>Remission snack:</strong> half cup diced mango with Greek yogurt if lactose is tolerated</li>
<li><strong>Cooked option:</strong> briefly warm diced mango into a soft sauce over white rice</li>
<li><strong>Avoid for trials:</strong> dried strips, candied pieces, large juice glasses, and unpeeled firm green mango</li>
</ul>

<h2>Mango with strictures, ostomy, or J-pouch</h2>
<p>Fibrous skins and large fibrous bites are higher risk when the bowel is narrowed. People with an ostomy often care more about output volume and gas after sugary fruit. J-pouch teams may prefer lower-fiber fruit patterns during pouchitis flares. None of these situations has a universal mango rule. Ask your surgeon or IBD dietitian before you assume online charts apply.</p>

<h2>Comparing mango to other tropical fruits people search</h2>
<p>Banana is often gentler during flares for many people. Melon can be watery and lower fiber in some servings. Grapes and berries add skins and seeds. Mango sits in the middle: soft when ripe, still sweet, still fibrous if you keep the skin. Use IBDPal food logs to compare your own responses instead of ranking fruits forever.</p>

<h2>Shopping and kitchen checklist</h2>
<ul class="blog-list">
<li>Choose fragrant ripe fruit that yields slightly to pressure</li>
<li>Wash the outside before cutting so the knife does not drag surface dirt into the flesh</li>
<li>Peel with a sharp knife or peeler; discard skin</li>
<li>Cut over a bowl to catch juice; sip water separately if juice volume feels large</li>
<li>Store leftovers covered in the fridge and finish within a day or two</li>
</ul>

<h2>What to tell a dietitian in one minute</h2>
<p>Bring: disease location, recent calprotectin or scope notes if you have them, whether you are in flare or remission, any FODMAP guidance already given, and your mango trial size. Ask whether sugar alcohols in &quot;mango flavored&quot; snacks are a separate issue from fresh fruit. Ask whether dried mango is off the table for now.</p>

<p>Education supports shared decisions. It does not replace your gastroenterologist or dietitian. Stop and seek care for chest pain, fainting, fever with bloody stools, or a sudden severe abdominal change unlike your usual IBD pattern.</p>
<p>Home prep counts. A few ripe cubes beat a giant smoothie on uncertain days. Consistency of logging matters more than perfect food rules copied from strangers online.</p>
<p>If joint pain, anemia, or ostomy output change how fruit sits, say so in clinic. Advice for isolated gut disease may not fit multi-system reality.</p>
<p>Seasonal mango windows vary by country. Frozen ripe mango without added sugar can be a steadier option than waiting for peak season if you already tolerate it.</p>
<p>Parents offering mango to kids with IBD should confirm texture and choking risk with pediatrics, especially during flares when appetite is fragile.</p>
<p>Travel tip: airport snack packs of dried mango look convenient and often backfire. Pack a safer backup you already tolerate, then re-test fresh mango at home.</p>
<p>If mango pollen or oral allergy syndrome makes your mouth itch with raw fruit, mention that separately. Cooking sometimes changes oral symptoms; gut IBD decisions still belong with your GI team.</p>
""".strip(),
    },
    {
        "slug": "abdominal-pain-stomach-pain-ibd",
        "title": "Abdominal Pain and Stomach Pain with IBD: What to Track and When to Call",
        "description": "Abdominal or stomach pain with Crohn's or colitis: location clues, flare vs other causes, red flags, and clinic questions. Education only.",
        "category": "Wellness · Symptoms · October 2026",
        "date_display": DATE_DISPLAY,
        "date_iso": DATE_ISO,
        "asset_dir": "abdominal-pain-ibd",
        "images": ["abdominal-pain-ibd_1.jpg"],
        "alts": ["Person resting with hands near abdomen representing IBD pain questions"],
        "share": "Abdominal and stomach pain with IBD: what to track and when to call. Education only.",
        "resource_category": "wellness",
        "match_terms": [
            "abdominal pain",
            "stomach",
            "stomach pain",
            "belly pain",
            "stomach ache ibd",
            "abdominal pain crohn",
            "stomach pain colitis",
        ],
        "tags": ["abdominal pain", "stomach pain", "symptoms", "flare", "Crohn's", "colitis"],
        "body": """
<p>Searches for <strong>abdominal pain</strong>, <strong>stomach pain</strong>, and <strong>stomach</strong> are among the most common on IBDPal. People want to know whether the ache is a flare, gas, medication effect, or something urgent. This article is patient education for Crohn's disease and ulcerative colitis. It is not a diagnosis tool.</p>
<p>Related: <a href="/blog/flare-symptoms-ibd">flare symptoms</a>, <a href="/blog/when-to-call-gi-vs-er-ibd">GI nurse line vs ER</a>, <a href="/blog/ibd-joint-pain-arthritis">joint pain</a>, and <a href="/flare-help">flare help</a>.</p>

<h2>Stomach pain versus abdominal pain in everyday language</h2>
<p>Patients often say stomach when they mean anywhere in the belly. Clinicians map pain by location: upper (epigastric), around the navel, lower right, lower left, or diffuse. Location plus stool change, fever, and vomiting helps triage. Write the zone in your log instead of only the word stomach.</p>

<h2>Common IBD-related patterns people discuss</h2>
<ul class="blog-list">
<li><strong>Inflammatory pain:</strong> often with urgency, blood, mucus, or rising calprotectin</li>
<li><strong>Gas and bloating pain:</strong> crampy, shifts with bowel movements or meals</li>
<li><strong>Stricture or obstructive worry:</strong> severe cramping, vomiting, inability to pass stool or gas needs urgent evaluation</li>
<li><strong>Post-meal pain:</strong> may relate to fat load, lactose, or narrowed segments</li>
<li><strong>Medication-related discomfort:</strong> steroids, NSAIDs, or antibiotics can confuse the picture</li>
</ul>

<h2>What to track for 48 to 72 hours</h2>
<ul class="blog-list">
<li>Location and whether pain radiates to back or shoulder</li>
<li>Severity 0 to 10 at worst and average</li>
<li>Relation to meals, movement, and bathroom trips</li>
<li>Stool form, blood, nocturnal stools</li>
<li>Fever, dizziness, vomiting, weight change</li>
<li>New medicines, NSAIDs, or skipped IBD doses</li>
</ul>
<p>IBDPal symptom logging keeps this next to food and meds so clinic visits show a timeline, not a single bad afternoon.</p>

<h2>Red flags that mean same-day or emergency care</h2>
<ul class="blog-list">
<li>Sudden severe pain unlike your usual pattern</li>
<li>Vomiting that will not stop, or green bilious vomit</li>
<li>Hard, swollen abdomen; no gas or stool with escalating pain</li>
<li>High fever with bloody stools</li>
<li>Fainting, chest pain, or confusion</li>
<li>Heavy bleeding or black tarry stools</li>
</ul>
<p>Use your clinic's flare pathway and <a href="/blog/when-to-go-er-ibd">when to go to the ER</a>. Do not wait for a perfect log if red flags are present.</p>

<h2>Flare pain versus other causes your team may consider</h2>
<p>Not every belly ache is mucosal flare. Infection, bile acid diarrhea, adhesions after surgery, gallbladder issues, menstrual cramps, constipation with overflow, and anxiety-driven gut sensitivity can overlap. Your team may order labs, stool studies, imaging, or endoscopy based on the story. Self-labeling every cramp as flare can delay the right test.</p>

<h2>Clinic script you can copy</h2>
<p>&quot;I have abdominal/stomach pain in [location] for [duration], severity [0-10], with [stool/fever/vomit details]. Is this consistent with my Crohn's/colitis pattern, or should we evaluate obstruction, infection, or another cause? What should I do if it worsens overnight?&quot;</p>

<h2>Questions people search before messaging clinic</h2>
<h3>Is left-sided pain always colitis?</h3>
<p>Left lower pain is common in ulcerative colitis flares, but location alone is not proof. Right lower pain raises small-bowel Crohn's questions for some people. Imaging and exam decide.</p>
<h3>Can stress cause IBD stomach pain?</h3>
<p>Stress does not cause Crohn's or colitis, but it can amplify pain perception and motility. Treat inflammation and coping together when both are loud.</p>
<h3>Should I take NSAIDs for the ache?</h3>
<p>Many IBD teams discourage ibuprofen and similar NSAIDs. Ask before using them. See <a href="/blog/nsaids-ibd-risk">NSAIDs and IBD</a>.</p>

<h2>Pain while waiting for a visit</h2>
<p>Follow the written plan your GI already gave for flares. Rest, hydration, and heat packs help some people. Avoid escalating opioids without guidance. If you use prescribed rescue medicines, log them so the team sees frequency.</p>

<h2>Kids, pregnancy, and post-surgery notes</h2>
<p>Pediatric pain reporting can be vague. Parents should watch for withdrawal from food, fever, and growth concerns. Pregnancy needs obstetric and GI coordination. After surgery, new severe pain deserves a low threshold to call, especially with fever or wound changes.</p>

<p>Related reading: <a href="/blog/chronic-diarrhea-ibd-causes">chronic diarrhea</a>, <a href="/blog/blood-in-stool-ibd-when-to-worry">blood in stool</a>, <a href="/blog/constipation-ibd-causes">constipation</a>, <a href="/blog/gas-bloating-ibd">gas and bloating</a>, <a href="/ask">reader Q&amp;A</a>.</p>

<h2>How location language helps the nurse line</h2>
<ul class="blog-list">
<li><strong>Upper middle:</strong> &quot;pain under my breastbone / upper stomach&quot;</li>
<li><strong>Around the navel:</strong> &quot;pain around my belly button&quot;</li>
<li><strong>Lower right:</strong> &quot;pain in the lower right where my appendix would be&quot;</li>
<li><strong>Lower left:</strong> &quot;pain in the lower left&quot;</li>
<li><strong>Diffuse:</strong> &quot;the whole belly hurts and feels tight&quot;</li>
</ul>
<p>Add whether pressing makes it worse, whether walking helps, and whether a bowel movement changes the score. That short script saves repeat portal messages.</p>

<h2>Pain scales that are useful in clinic</h2>
<p>Use the same 0 to 10 scale each day. Note the worst score, not only the average. Note if pain stops sleep. Note rescue medicines taken. Patterns over a week beat a single dramatic number without context.</p>

<h2>After surgery or hospital discharge</h2>
<p>New severe pain after resection, abscess drainage, or pouch surgery needs a low threshold to call, especially with fever, wound drainage, vomiting, or no gas. Bring your discharge instructions when you call so the team can match your symptoms to the written plan.</p>

<h2>Work, school, and travel pain plans</h2>
<p>Know your clinic after-hours number before you need it. Keep a one-page summary of diagnoses, current meds, and allergies in your phone. If you travel, know the nearest ER and whether your infusion center has a nurse line. See also <a href="/blog/biologics-flying-travel-ibd">biologics and travel</a>.</p>

<p>Education supports shared decisions. It does not replace your gastroenterologist, surgeon, or emergency services. Seek care for the red-flag list above or any change that feels medically wrong for you.</p>
<p>Bring photos of stool only if your clinic asked for them. A short written timeline usually travels better in the portal than a long paragraph.</p>
<p>If pain repeatedly peaks after the same meal type, pause that food and reintroduce later with dietitian guidance rather than eliminating your entire diet overnight.</p>
<p>Night pain that wakes you deserves mention even if daytime pain seems mild. Nocturnal symptoms often change urgency of evaluation.</p>
<p>Partners and caregivers can help by noting when you last ate, last passed stool, and whether you look pale or dehydrated. Those details speed triage calls.</p>
<p>If pain is new after starting a medicine, do not silently tough it out for weeks. Ask whether timing fits a known side effect, infection risk, or dose issue.</p>
<p>People with IBD and endometriosis, kidney stones, or gallbladder disease may need parallel evaluations. Tell each specialist the full list so tests are not duplicated blindly.</p>
""".strip(),
    },
]


def download_image(url: str, dest: Path) -> bool:
    for ctx in (ssl.create_default_context(), ssl._create_unverified_context()):
        try:
            with urllib.request.urlopen(url, context=ctx, timeout=45) as resp:
                data = resp.read()
            if len(data) > 5000:
                dest.write_bytes(data)
                return True
        except Exception:
            continue
    return False


def ensure_image(post: dict) -> None:
    asset = BLOGS / "assets" / post["asset_dir"]
    asset.mkdir(parents=True, exist_ok=True)
    dest = asset / post["images"][0]
    if dest.exists() and dest.stat().st_size >= 1000:
        return
    url = IMAGE_URLS.get(post["asset_dir"])
    if url and download_image(url, dest):
        print("downloaded", dest.name)
        return
    if FALLBACK.exists():
        shutil.copy(FALLBACK, dest)
        print("fallback", dest.name)


def patch_vercel(slugs: list[str]) -> None:
    text = VERCEL.read_text(encoding="utf-8")
    inserts = []
    for slug in slugs:
        if f'"/blog/{slug}"' in text:
            continue
        inserts.append(
            f'    {{\n      "source": "/blog/{slug}",\n'
            f'      "destination": "/blogs/{slug}.html"\n    }}'
        )
    if not inserts:
        return
    text = text.replace('"rewrites": [\n', '"rewrites": [\n' + ",\n".join(inserts) + ",\n")
    VERCEL.write_text(text, encoding="utf-8")
    print("patched vercel.json")


def update_search_gap(posts: list[dict]) -> None:
    data = {"posts": []}
    if SEARCH_GAP.exists():
        data = json.loads(SEARCH_GAP.read_text(encoding="utf-8"))
        if isinstance(data, list):
            data = {"posts": data}
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


def update_aliases() -> None:
    data = json.loads(ALIASES.read_text(encoding="utf-8"))
    extras = {
        "mango ibd": "mango",
        "mango crohn": "mango",
        "mango crohn's": "mango",
        "mango crohns": "mango",
        "mango colitis": "mango",
        "mango ulcerative colitis": "mango",
        "can i eat mango with crohn's": "mango",
        "stomach pain": "abdominal pain",
        "belly pain": "abdominal pain",
        "stomach ache": "abdominal pain",
        "stomach ache ibd": "abdominal pain",
        "abdominal pain crohn": "abdominal pain",
        "abdominal pain colitis": "abdominal pain",
        "stomach pain colitis": "abdominal pain",
        "stomach pain crohn's": "abdominal pain",
        "latest ibd news": "ibd news",
        "ibd news": "ibd news",
        "latest news ibd": "ibd news",
        "partial enteral": "enteral",
    }
    data.update(extras)
    ALIASES.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("updated search-aliases.json")


def main() -> None:
    DATA.write_text(json.dumps(POSTS, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    slugs = []
    for post in POSTS:
        ensure_image(post)
        wc = word_count(post["body"])
        if wc < MIN_WORDS:
            raise SystemExit(f"too short: {post['slug']} ({wc})")
        out = BLOGS / f"{post['slug']}.html"
        out.write_text(render_post(post), encoding="utf-8")
        slugs.append(post["slug"])
        print(f"wrote {out.name} (~{wc} words)")
    patch_vercel(slugs)
    update_search_gap(POSTS)
    update_aliases()
    print("Done.", len(slugs), "posts")


if __name__ == "__main__":
    main()
