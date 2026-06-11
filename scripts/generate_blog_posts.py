#!/usr/bin/env python3
# Prose style: do not use em dash. Use periods, commas, colons, or "|" in titles.
"""One-off generator for June 2026 lifestyle blog posts.

Images must be real JPEGs from https://images.unsplash.com/photo-{id}?auto=format&w=1200
or Pexels CDN | not unsplash.com/photos/{slug}/download (returns HTML).
"""
from __future__ import annotations
import html
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
sys.path.insert(0, str(ROOT / "scripts"))
from amp_utils import discover_blogs  # noqa: E402
from blog_related import related_reading_html  # noqa: E402
from eeat_blocks import (  # noqa: E402
    blog_medical_footer_en,
    content_note_en,
    edu_disclaimer_en,
    page_review_props,
    reviewed_by_org,
)
from site_nav import PAGE_SCRIPTS, SITE_HEADER_HTML, TAB_NAV_HTML  # noqa: E402

SEO_DATA = ROOT / "data" / "seo-expansion.json"

POSTS = [
    {
        "slug": "low-residue-diet-flare",
        "title": "Low-Residue Diet During an IBD Flare: A Practical Lifestyle Guide",
        "description": "What a low-residue pattern can look like during a flare, gentle meal ideas, and how to talk with your care team, educational only.",
        "category": "Nutrition · June 2026",
        "date_display": "June 1, 2026",
        "date_iso": "2026-06-01T12:00:00Z",
        "asset_dir": "low-residue",
        "images": ["low-residue_1.jpg", "low-residue_2.jpg", "low-residue_3.jpg"],
        "alts": [
            "Simple comforting soup for gentle eating during a flare",
            "Balanced plate with approachable foods",
            "Home-cooked meal prep for easier digestion",
        ],
        "share": "Low-residue eating ideas for IBD flares, lifestyle education only, not medical advice.",
        "body": """
<p>When symptoms flare, food can feel like a guessing game. A <strong>low-residue</strong> approach, eating foods that leave less bulk in the digestive tract, is sometimes suggested for short periods to give the bowel a break. It is not a forever diet, and it is not right for everyone. Think of it as a temporary “quiet menu” you shape with your clinician.</p>

<h2>What “Low-Residue” Means in Everyday Life</h2>
<p>Residue refers to the parts of food that are not fully digested and that add volume to stool. During active inflammation, smaller, gentler meals may feel easier. Low-residue patterns often emphasize refined grains, well-cooked vegetables without skins, tender proteins, and smooth textures, while limiting high-fiber whole grains, nuts, seeds, and tough raw produce.</p>
<p>Your team may recommend something different based on whether you have Crohn’s disease, ulcerative colitis, strictures, or recent surgery. That is why a personalized plan matters more than any blog checklist.</p>

<h2>Foods People Often Tolerate Better</h2>
<ul class="blog-list">
<li>White rice, pasta, or potatoes without skins</li>
<li>Refined bread or crackers</li>
<li>Eggs, fish, or tender chicken</li>
<li>Smooth nut butters in small amounts if approved</li>
<li>Ripe banana, melons, or canned fruit (no skins)</li>
<li>Broth-based soups and strained oatmeal</li>
</ul>

<h2>Foods Many People Scale Back Temporarily</h2>
<ul class="blog-list">
<li>Beans, lentils, and chunky chili</li>
<li>Nuts, seeds, and popcorn</li>
<li>Raw vegetables and leafy salads</li>
<li>Tough meats and sausage casings</li>
<li>High-fiber cereals and bran muffins</li>
</ul>
<p>Triggers are individual. Tracking with IBDPal can help you notice what felt calm versus what stirred up urgency, pain, or fatigue, then bring that log to your visit.</p>

<h2>Sample Gentle Day (Illustration Only)</h2>
<p><strong>Breakfast:</strong> Scrambled eggs, white toast, and half a ripe banana.<br>
<strong>Midday:</strong> Turkey sandwich on soft bread, applesauce, and water or electrolyte fluids.<br>
<strong>Dinner:</strong> Baked salmon, white rice, and well-cooked carrots.<br>
<strong>Snacks:</strong> Yogurt (if dairy works for you), rice pudding, or a smoothie without seeds.</p>
<p>Portions matter. Eating smaller amounts more often can feel kinder than three large meals.</p>

<h2>Lifestyle Tips Beyond the Plate</h2>
<p>Flares are exhausting. Give yourself permission to simplify cooking, sheet-pan meals, rotisserie chicken with rice, or asking for help. Keep hydration steady; diarrhea plus a limited menu can sneak up on fluid needs.</p>
<p>Plan groceries like you plan rest: a short list of “safe basics” reduces decision fatigue. If cooking smells worsen nausea, eat in a ventilated space or choose cooler foods.</p>

<h2>Working With Your Care Team</h2>
<p>Ask how long to stay low-residue, which fiber sources to reintroduce first, and whether you need calcium or multivitamin support while menus are narrow. Do not stay on a restrictive pattern longer than directed, your gut still needs balanced nutrition over time.</p>

<h2>When to Seek Prompt Medical Advice</h2>
<p>Contact your clinician if you see significant weight loss, blood in stool, fever, severe pain, or signs of dehydration. This article cannot tell you whether you need medication changes or hospital care.</p>
""",
    },
    {
        "slug": "travel-with-ibd",
        "title": "Travel With IBD: Planning Trips Without Letting Fear Run the Show",
        "description": "Packing, airports, food on the road, and confidence-building habits for traveling with Crohn’s or colitis, general education.",
        "category": "Lifestyle · June 2026",
        "date_display": "June 2, 2026",
        "date_iso": "2026-06-02T12:00:00Z",
        "asset_dir": "travel-ibd",
        "images": ["travel-ibd_1.jpg", "travel-ibd_2.jpg", "travel-ibd_3.jpg"],
        "alts": [
            "Packed suitcase ready for a planned trip",
            "Relaxed meal while traveling",
            "Travel planning at a desk with map",
        ],
        "share": "Travel tips for life with IBD, planning and packing ideas; not medical advice.",
        "body": """
<p>IBD does not have to cancel your dreams of visiting family, hiking a new city, or lying on a beach. It does ask for a different packing list and a mindset shift: <strong>prepare, then participate</strong>. Many people with Crohn’s disease or ulcerative colitis travel successfully by building routines that reduce surprises.</p>

<h2>Before You Book</h2>
<p>Talk with your gastroenterologist about timing: Are you in remission? Do you need vaccinations or travel letters for medication? If infusions or injections are due mid-trip, map clinics or carry documentation for biologics and coolers if required.</p>
<p>Research bathrooms along your route, airport maps, highway rest stops, and venue accessibility apps help more than you might expect. If you use a medical restroom card, keep it in your wallet and phone.</p>

<h2>Packing Like a Pro</h2>
<ul class="blog-list">
<li>Extra underwear, wipes, and a small disposal bag</li>
<li>Split medication between carry-on and checked luggage</li>
<li>Copy of prescription labels and a clinician letter</li>
<li>Electrolyte packets and familiar snacks</li>
<li>Heat patch or pain relief you already use at home</li>
<li>Insurance card and after-hours contact numbers</li>
</ul>
<p>Pack a “flare mini-kit” even when you feel great, confidence comes from knowing you are covered.</p>

<h2>Food on the Road</h2>
<p>Airports and highways are getting better at plant-forward options, but familiarity still wins for many bellies. Scout menus ahead, choose grilled over fried when possible, and prioritize hydration. If you follow a low-fiber pattern temporarily, note safe staples at chains you will pass.</p>
<p>Breakfast is often the easiest meal to control, hotel oatmeal, eggs, and bananas can anchor the day before unpredictable lunches.</p>

<h2>Time Zones and Routines</h2>
<p>Shift medication schedules gradually if crossing zones. Sleep loss can nudge symptoms, so build buffer days after long flights. Gentle walks and light stretching help circulation without overdoing it.</p>

<h2>Emotional Safety</h2>
<p>Anxiety about accidents can shrink your world. Name one ally on the trip who knows your plan. Practice short scripts: “I need to use the restroom, no problem if we pause.” Most people are kinder than our fears predict.</p>
<p>Tracking symptoms in IBDPal during travel helps you separate “travel stress” from true flare signs when you debrief with your team.</p>

<h2>Insurance and Backup Plans</h2>
<p>Know whether your plan covers out-of-area urgent care. Save maps to nearby hospitals just in case, not to catastrophize, but to free mental space for fun.</p>

<h2>Returning Home</h2>
<p>Give yourself a soft landing day. Restock groceries, hydrate, and schedule a check-in if symptoms linger more than a week. Bring your travel log to your next appointment, it turns anecdotes into useful data.</p>
""",
    },
    {
        "slug": "understanding-biologics-ibd",
        "title": "Understanding Biologics for IBD: A High-Level Guide",
        "description": "What biologics are, how they fit in IBD care, infusion vs injection, and questions to ask your doctor, education only.",
        "category": "Treatment basics · June 2026",
        "date_display": "June 3, 2026",
        "date_iso": "2026-06-03T12:00:00Z",
        "asset_dir": "biologics-basics",
        "images": ["biologics_1.jpg", "biologics_2.jpg", "biologics_3.jpg"],
        "alts": [
            "Person in a calm wellness moment",
            "Conversation with a healthcare professional",
            "Supportive hand-on-shoulder gesture of care",
        ],
        "share": "High-level overview of biologics in IBD, education only; talk with your clinician about your plan.",
        "body": """
<p>Hearing the word <strong>biologic</strong> can feel intimidating. These medicines are designed to target specific parts of the immune system that drive inflammation in Crohn’s disease and ulcerative colitis. They are not one-size-fits-all, and they are not the only tool, but for many people they are a cornerstone of remission.</p>

<h2>What Biologics Are (Without Jargon Overload)</h2>
<p>Biologics are large-molecule medicines made from living cells. Unlike daily pills that broadly calm inflammation, biologics tend to aim at particular pathways, such as proteins that ramp up immune activity in the gut. The goal is to reduce inflammation, allow healing, and improve quality of life.</p>
<p>They are typically prescribed when inflammation remains active despite other therapies, or when your clinician wants a targeted approach early based on your risk.</p>

<h2>Common Ways People Receive Them</h2>
<p><strong>Infusions</strong> happen in an infusion center or hospital outpatient unit on a schedule, often every few weeks after loading doses.<br>
<strong>Injections</strong> can be self-administered at home after training, often on a pen or syringe kept in the fridge.<br>
Your team chooses based on the specific drug, your preference, insurance, and monitoring needs.</p>

<h2>What Appointments May Involve</h2>
<ul class="blog-list">
<li>Screening tests before starting (infections, vaccines, labs)</li>
<li>Review of travel, surgery plans, and other medicines</li>
<li>Monitoring during visits for side effects and response</li>
<li>Occasional lab work between doses</li>
</ul>
<p>Keep a notebook or IBDPal log of how you feel week to week, fatigue, joint pain, stool changes, and mood all matter.</p>

<h2>Benefits People Hope For</h2>
<p>Many pursue biologics to achieve mucosal healing, meaning the lining of the intestine looks calmer on scopes, and to reduce hospitalizations. Lifestyle wins follow when urgency, pain, and unpredictability ease: returning to work, exercise, and social meals with more confidence.</p>

<h2>Risks and Real Talk</h2>
<p>All medicines carry risks. Biologics can affect infection risk because they modify immune pathways. Your clinician balances these risks against the harm of uncontrolled inflammation. Never stop or skip doses without a plan, flares can rebound.</p>
<p>Report fever, unusual fatigue, worsening diarrhea, or new pain promptly. Vaccination schedules may change; ask which live vaccines to avoid.</p>

<h2>Questions to Bring to Your Next Visit</h2>
<ul class="blog-list">
<li>Why is this biologic a fit for my disease type and severity?</li>
<li>How will we know it is working, and on what timeline?</li>
<li>What monitoring labs or tests do I need?</li>
<li>What are injection or infusion side effects I should watch for?</li>
<li>How does this interact with pregnancy plans, surgery, or travel?</li>
</ul>

<h2>Biologics Are One Chapter, Not the Whole Book</h2>
<p>Nutrition, sleep, stress care, and symptom tracking still matter. Biologics work best alongside a team you trust and habits that keep you grounded.</p>
""",
    },
    {
        "slug": "living-with-ibd-kids",
        "title": "Living With IBD as a Family: Support for Kids and Parents",
        "description": "Helping children with IBD feel normal, building school plans, and caring for parents’ energy, family lifestyle education.",
        "category": "Family · June 2026",
        "date_display": "June 4, 2026",
        "date_iso": "2026-06-04T12:00:00Z",
        "asset_dir": "ibd-kids",
        "images": ["ibd-kids_1.jpg", "ibd-kids_2.jpg", "ibd-kids_3.jpg"],
        "alts": [
            "Family picnic together outdoors",
            "Parent and child reading together",
            "Children playing outside happily",
        ],
        "share": "Family-centered ideas for kids living with IBD, support and routines; not medical advice.",
        "body": """
<p>When a child has Crohn’s disease or ulcerative colitis, the whole household rides the waves, appointments, medication schedules, missed school days, and the quiet worry parents carry at night. A lifestyle built on <strong>predictability, honesty, and small joys</strong> helps kids feel like kids first, and patients second.</p>

<h2>Language That Protects Dignity</h2>
<p>Use age-appropriate words. Younger children may say “tummy trouble”; teens may prefer direct terms. Avoid blame, “Did you eat something wrong?”, and replace with curiosity: “What do you think your body needed today?”</p>
<p>Let them choose how much they share with friends. A simple script (“I take medicine that helps my stomach”) can prevent rumors while preserving privacy.</p>

<h2>School and Activities</h2>
<p>Build a 504 plan or school health plan outlining bathroom access, nurse visits, hydration, and make-up work. PE teachers and coaches should know about fatigue flares without singling your child out.</p>
<p>Encourage activities they love, art, music, swimming if approved, because joy is medicine for mood. Modify rather than cancel when possible: sit during flare weeks, return when energy rebounds.</p>

<h2>Routines That Lower Stress</h2>
<ul class="blog-list">
<li>Medication reminders tied to daily anchors (breakfast, bedtime)</li>
<li>Go-bag in backpack: wipes, spare clothes, card with clinician number</li>
<li>Consistent sleep windows, even on weekends</li>
<li>Family meals that include at least one “safe” food they enjoy</li>
</ul>

<h2>For Parents and Caregivers</h2>
<p>Your bandwidth matters. Tag-team infusion days, divide pharmacy runs, and accept help from relatives without guilt. Burnout helps no one. If you are chronically sleep-deprived, talk with your own clinician about support resources.</p>
<p>Siblings may feel invisible, schedule one-on-one time so brothers and sisters know they matter too.</p>

<h2>Social Life and Mental Health</h2>
<p>Watch for withdrawal, slipping grades, or irritability that lingers. Counselors familiar with chronic illness can give kids tools peers cannot. Normalize asking for help; bravery includes texting a friend “not feeling great today.”</p>

<h2>Tracking Together</h2>
<p>Apps like IBDPal can turn vague memories into patterns, sleep, stool, pain, and mood, so pediatric visits focus on solutions instead of detective work. Let older kids own their entries to build agency.</p>

<h2>Celebrating Milestones</h2>
<p>Mark remission stretches, growth milestones, and ordinary wins: finishing a semester, trying a new food after clearance, or making it through a road trip. Hope grows from noticing progress, not perfection.</p>
""",
    },
    {
        "slug": "stress-emotional-wellness-ibd",
        "title": "Stress, Mood, and IBD: Everyday Ways to Protect Your Energy",
        "description": "How stress and gut symptoms interact, gentle coping tools, and when to reach for professional support, lifestyle education.",
        "category": "Wellness · June 2026",
        "date_display": "June 5, 2026",
        "date_iso": "2026-06-05T12:00:00Z",
        "asset_dir": "stress-wellness",
        "images": ["stress_1.jpg", "stress_2.jpg", "stress_3.jpg"],
        "alts": [
            "Calm moment by the water",
            "Quiet reading nook for relaxation",
            "Peaceful nature scene for mindfulness",
        ],
        "share": "Stress and mood ideas for life with IBD, wellness education, not therapy or medical advice.",
        "body": """
<p>Living with Crohn’s disease or ulcerative colitis means living with uncertainty. That alone can keep nerves on high alert. Stress does not <em>cause</em> IBD, but it can amplify how symptoms feel and how quickly you bounce back after setbacks.</p>

<h2>The Gut–Brain Connection in Plain Language</h2>
<p>Your digestive tract and nervous system chat constantly. When stress hormones rise, some people notice urgency, cramps, or fatigue flaring alongside loose stools. Others feel tension in their shoulders long before their gut speaks up. Neither experience is “in your head”, it is biology plus context.</p>

<h2>Micro-Habits That Add Up</h2>
<ul class="blog-list">
<li>Two-minute breathing breaks before meals</li>
<li>Short walks after dinner to signal wind-down</li>
<li>Phone-free first ten minutes of the morning</li>
<li>One enjoyable ritual daily (tea, music, stretching)</li>
</ul>
<p>Consistency beats intensity. A five-minute practice you actually do wins over an hour you never start.</p>

<h2>Boundaries as Healthcare</h2>
<p>Saying no to extra commitments during flare season is protective, not selfish. At work, discuss flexible hours or remote days if possible. With friends, trade big nights out for movie afternoons when energy is low.</p>

<h2>Social Support That Feels Safe</h2>
<p>Choose confidants who listen without comparing your story to their cousin’s neighbor. Online communities can help, or overwhelm. Curate inputs the way you curate food during a flare: nourishing, not noisy.</p>

<h2>When to Involve a Professional</h2>
<p>Therapists, social workers, and GI psychologists understand chronic illness. Seek help if anxiety blocks eating, you avoid leaving home, mood stays low for weeks, or sleep collapses. Medication and talk therapy can coexist with IBD treatments, tell all clinicians what you take.</p>

<h2>Track Mood Like You Track Symptoms</h2>
<p>IBDPal lets you log stress alongside stool and pain. Patterns help you prepare, exam week needs more rest, not more self-criticism.</p>

<h2>Compassion as a Lifestyle</h2>
<p>You are managing a full-time job your friends do not see. Celebrate showing up, appointment kept, meal tolerated, walk taken. Progress in IBD is rarely linear, but small steady choices matter.</p>
""",
    },
    {
        "slug": "sleep-rest-ibd-flares",
        "title": "Sleep and Rest During IBD Flares: Why Slowing Down Helps",
        "description": "Sleep, naps, pacing activity, and bedroom habits that support recovery during Crohn’s and colitis flares, general wellness.",
        "category": "Wellness · June 2026",
        "date_display": "June 6, 2026",
        "date_iso": "2026-06-06T12:00:00Z",
        "asset_dir": "sleep-rest",
        "images": ["sleep_1.jpg", "sleep_2.jpg", "sleep_3.jpg"],
        "alts": [
            "Restful bedroom ready for sleep",
            "Person resting on a comfortable sofa",
            "Soft morning light for a gentle wake-up",
        ],
        "share": "Sleep and rest tips during IBD flares, lifestyle education, not medical advice.",
        "body": """
<p>Night trips to the bathroom. Cramps that wake you at 3 a.m. Steroids that buzz like coffee in your veins. If flares and sleep feel like enemies, you are not alone. Rest is not laziness, it is part of how bodies heal.</p>

<h2>Why Sleep Matters for Inflammation</h2>
<p>Sleep supports immune balance, mood, and pain tolerance. Fragmented nights can leave you more sensitive to discomfort and less patient with the day ahead. Protecting rest is a legitimate medical goal, mention sleep troubles at appointments.</p>

<h2>Bedroom Tweaks That Help</h2>
<ul class="blog-list">
<li>Dim lights an hour before bed; use nightlights for safer bathroom trips</li>
<li>Keep the room cool and quiet; white noise masks household sounds</li>
<li>Charge phones away from arm’s reach to reduce scroll loops</li>
<li>Layer bedding for temperature swings and night sweats</li>
</ul>

<h2>Pacing Daytime Energy</h2>
<p>Think energy budgeting: urgent tasks in the morning, recovery blocks after. Lying down twenty minutes, not necessarily sleeping, can prevent the evening crash. If you nap, set a gentle alarm so night sleep stays possible.</p>

<h2>Food and Fluids Before Bed</h2>
<p>Large late dinners can stir symptoms. A small bland snack may steady some people; others do better with an earlier kitchen close. Reduce caffeine after lunch and discuss alcohol with your clinician, it can fragment sleep and irritate the gut.</p>

<h2>Medications and Timing</h2>
<p>Steroids and some symptom meds affect sleep. Ask whether dosing earlier in the day helps. Never adjust prescriptions without guidance.</p>

<h2>When Nights Stay Rough</h2>
<p>Track sleep in IBDPal or a simple diary: bedtime, wake-ups, pain, and stool urgency. Patterns guide adjustments, melatonin trials, antispasmodics at night, or mental health support for anxiety-driven insomnia.</p>

<h2>Permission to Rest</h2>
<p>Culture glorifies pushing through. With IBD, rest is strategy. Clear your calendar where you can, delegate chores, and tell your team honestly: “I am in a flare; I need slower days.” Healing includes closed eyes, not just cleared calendars.</p>
""",
    },
]


def figure_grid(asset_dir: str, images: list[str], alts: list[str]) -> str:
    figs = []
    for img, alt in zip(images, alts):
        src = f"/blogs/assets/{asset_dir}/{img}"
        figs.append(
            f'                            <figure>\n'
            f'                                <img src="{src}" alt="{html.escape(alt)}" width="800" height="600" loading="lazy">\n'
            f'                            </figure>'
        )
    inner = "\n".join(figs)
    return (
        '                        <div class="blog-figure-grid blog-figure-grid--three" aria-label="Photos for this article">\n'
        f"{inner}\n"
        "                        </div>\n"
        '                        <p class="blog-photo-credit"><em>Photos: <a href="https://unsplash.com/license" rel="noopener noreferrer">Unsplash License</a> (free use).</em></p>\n'
    )


def _related_section(slug: str) -> str:
    hubs = json.loads(SEO_DATA.read_text(encoding="utf-8")).get("hubs", [])
    posts = discover_blogs(BLOGS)
    return related_reading_html(slug, posts, hubs)


def render_post(p: dict) -> str:
    slug = p["slug"]
    related = _related_section(slug)
    asset = p["asset_dir"]
    thumb = f"/blogs/assets/{asset}/{p['images'][0]}"
    canonical = f"https://www.ibdpal.org/blog/{slug}"
    amp_html = f"{canonical}/amp"
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "IBDPal", "item": "https://www.ibdpal.org/"},
                    {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://www.ibdpal.org/#blogs"},
                    {"@type": "ListItem", "position": 3, "name": p["title"], "item": canonical},
                ],
            },
            {
                "@type": "Article",
                "headline": p["title"],
                "description": p["description"],
                "datePublished": p["date_iso"],
                "dateModified": p["date_iso"],
                "author": {"@type": "Organization", "name": "MediVue", "url": "https://www.ibdpal.org/"},
                "reviewedBy": reviewed_by_org(),
                **page_review_props(),
                "publisher": {
                    "@type": "Organization",
                    "name": "MediVue",
                    "url": "https://www.ibdpal.org/",
                    "logo": {"@type": "ImageObject", "url": "https://www.ibdpal.org/favicon.ico"},
                },
                "image": [f"https://www.ibdpal.org{thumb}"],
                "mainEntityOfPage": {"@type": "WebPage", "@id": canonical},
                "isAccessibleForFree": True,
            },
        ],
    }
    ld_json = json.dumps(ld, separators=(",", ":"))
    disclaimer = content_note_en() + edu_disclaimer_en()
    medical = blog_medical_footer_en()
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(p["title"])} | IBDPal Blog</title>
    <meta name="description" content="{html.escape(p["description"])}">
    <link rel="stylesheet" href="/styles.css">
    <link rel="stylesheet" href="/site-layout-icn.css">
    <link rel="stylesheet" href="/site-polish.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/png" href="/IBDPal_Logo.png">
    <link rel="apple-touch-icon" href="/IBDPal_Logo.png">

    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
    <link rel="canonical" href="{canonical}">
    <link rel="amphtml" href="{amp_html}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{canonical}">
    <meta property="og:title" content="{html.escape(p["title"])} | IBDPal Blog">
    <meta property="og:description" content="{html.escape(p["description"])}">
    <meta property="og:site_name" content="IBDPal">
    <meta property="og:locale" content="en_US">
    <meta property="og:image" content="https://www.ibdpal.org{thumb}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{html.escape(p["title"])} | IBDPal Blog">
    <meta name="twitter:description" content="{html.escape(p["description"])}">
    <meta property="article:published_time" content="{p["date_iso"]}">
    <script type="application/ld+json">{ld_json}</script>
</head>
<body data-blog-share-text="{html.escape(p["share"])}">
    <div class="app-container">
{SITE_HEADER_HTML}

{TAB_NAV_HTML.replace('class="tab-button" data-tab="blogs"', 'class="tab-button active" data-tab="blogs"', 1)}

        <main class="main-content" data-track-impression="blog_article" data-track-label="Blog article body">
            <div class="blogs-section">
                <p class="blog-back"><a href="/#blogs" class="blog-back-link">← All posts</a></p>

                <article class="blog-post">
                    <div class="blog-header blog-header--with-thumb">
                        <img class="blog-header-thumb" src="{thumb}" alt="{html.escape(p["alts"][0])}" width="96" height="96" decoding="async">
                        <div class="blog-header-text">
                            <h1 class="blog-title">{html.escape(p["title"])}</h1>
                            <p class="blog-date">Posted on {p["date_display"]} · {html.escape(p["category"].split(" · ")[0])}</p>
                        </div>
                    </div>

                    <div class="blog-content">
{disclaimer}
{p["body"].strip()}
{figure_grid(asset, p["images"], p["alts"])}
{medical}
                    </div>
{related}
                    <div class="blog-vote" data-blog-slug="{slug}">
                        <p class="blog-vote-prompt">Was this article helpful?</p>
                        <div class="blog-vote-actions">
                            <button type="button" class="blog-vote-btn blog-vote-btn--up" data-vote="up" aria-label="Thumbs up, helpful">
                                <span class="blog-vote-icon" aria-hidden="true">👍</span>
                                <span class="blog-vote-count" data-vote-count="up">0</span>
                            </button>
                            <button type="button" class="blog-vote-btn blog-vote-btn--down" data-vote="down" aria-label="Thumbs down, not helpful">
                                <span class="blog-vote-icon" aria-hidden="true">👎</span>
                                <span class="blog-vote-count" data-vote-count="down">0</span>
                            </button>
                        </div>
                        <p class="blog-vote-status" hidden></p>
                    </div>
                    <div class="blog-footer">
                        <div class="blog-share">
                            <span class="share-label">Share this post:</span>
                            <a href="#" class="share-link" onclick="shareOnFacebook(event)">Facebook</a>
                            <a href="#" class="share-link" onclick="shareOnTwitter(event)">Twitter</a>
                            <a href="#" class="share-link" onclick="shareViaEmail(event)">Email</a>
                        </div>
                    </div>
                </article>
            </div>
        </main>

        <footer class="footer">
            <div class="footer-content">
                <div class="footer-links">
                    <a href="/privacy" class="footer-link">Privacy Policy</a>
                    <a href="/support" class="footer-link">Support</a>
                    <a href="/terms" class="footer-link">Terms of Service</a>
                </div>

                <p><strong>IBDPal iOS App</strong> and <strong>IBDPal.org</strong> are trademarks of MediVue, a nonprofit organization registered in the State of North Carolina.</p>

                <p>&copy; 2025 MediVue. All rights reserved. All content, software, algorithms, user interface designs, and intellectual property associated with IBDPal are proprietary to MediVue and protected by copyright, patent, and other intellectual property laws. No portion of this application or website may be reproduced, distributed, or transmitted without the express written permission of MediVue.</p>

                <p>IBDPal is designed to assist patients in managing their IBD condition but should not replace professional medical advice. Always consult with healthcare providers for medical decisions.</p>

                <p>MediVue is a 501(c)(3) nonprofit organization dedicated to improving healthcare outcomes for patients with inflammatory bowel diseases through innovative technology solutions and community support.</p>
            </div>
        </footer>
    </div>

    <script src="/blog-votes.js" defer></script>
{PAGE_SCRIPTS}
    <script src="/script.js"></script>
</body>
</html>
"""


def main():
    for p in POSTS:
        out = BLOGS / f"{p['slug']}.html"
        out.write_text(render_post(p), encoding="utf-8")
        print("wrote", out.name)


if __name__ == "__main__":
    main()
