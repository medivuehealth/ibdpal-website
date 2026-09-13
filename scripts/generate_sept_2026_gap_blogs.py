#!/usr/bin/env python3
# Prose style: do not use em dash.
"""Generate ~10-minute September 2026 analytics gap blog posts."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
DATA = ROOT / "data" / "sept-2026-gap-posts.json"
SEARCH_GAP = ROOT / "data" / "search-gap-posts.json"
ALIASES = ROOT / "data" / "search-aliases.json"
VERCEL = ROOT / "vercel.json"
FALLBACK = BLOGS / "assets" / "er-ibd" / "er_1.jpg"

sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402


def p(*parts: str) -> str:
    return "\n".join(parts)


POSTS = [
    {
        "slug": "flare-foods-ibd",
        "title": "Flare Foods for IBD: What to Eat, What to Pause, and How to Rebuild",
        "description": "Practical flare foods guide for Crohn's and ulcerative colitis: gentle plates, hydration, protein, what to pause, and when food is not enough. Education only.",
        "category": "Nutrition · September 2026",
        "date_display": "September 13, 2026",
        "date_iso": "2026-09-13T16:00:00Z",
        "asset_dir": "crohns-flare",
        "images": ["crohns-flare-safe-foods_1.jpg"],
        "alts": ["Simple gentle foods often used during an IBD flare"],
        "share": "Flare foods for IBD: what to eat, pause, and rebuild. Education only.",
        "resource_category": "nutrition",
        "match_terms": [
            "flare foods",
            "foods during a flare",
            "what to eat during flare",
            "flare diet",
            "crohn flare foods",
            "colitis flare foods",
        ],
        "tags": [
            "flare foods",
            "flare diet",
            "nutrition",
            "low residue",
            "Crohn's",
            "colitis",
            "hydration",
            "protein",
        ],
        "body": p(
            "<p>People searching <strong>flare foods</strong> usually want a plain answer: what can I eat when Crohn's disease or ulcerative colitis is loud, and what should I pause until the gut settles? Food does not cause IBD, and no single plate cures a flare. Still, gentler textures and simpler meals can reduce urgency, cramping, and fear of eating while your care team treats inflammation. This guide is educational and aligned with common Crohn's &amp; Colitis Foundation nutrition themes. It is not a personalized diet prescription.</p>",
            "<h2>What \"flare foods\" really means</h2>",
            "<p>Flare foods are temporary, easier-to-tolerate options for active symptoms. Think soft textures, lower insoluble fiber for some people, less spice, less grease, and fewer large volumes at once. The goal is enough calories, protein, and fluids to protect weight and strength, not a permanent elimination lifestyle. When inflammation improves, most clinicians want you to expand variety again with a dietitian when possible.</p>",
            "<p>Start with the hubs at <a href=\"/flare-help\">flare help</a>, <a href=\"/guides/foods-to-eat-crohns-flare\">foods during a Crohn's flare</a>, and <a href=\"/blog/flare-first-48-hours\">the first 48 hours of a flare</a>. Use this article as the food-focused companion.</p>",
            "<h2>First 48 hours: keep it simple and hydrating</h2>",
            "<p>Early in a flare, many people do better with small, frequent portions rather than three heavy meals. Warm liquids and soft carbs often feel safer than raw salads or fried takeout. Common starter ideas patients discuss with teams include:</p>",
            '<ul class="blog-list">',
            "<li>White rice, plain congee, or well-cooked pasta without heavy sauce</li>",
            "<li>Ripe banana, peeled cooked apple, or applesauce if fruit is tolerated</li>",
            "<li>Eggs scrambled soft, plain turkey, or tender chicken</li>",
            "<li>Bone broth, clear soup, or oral rehydration fluids between meals</li>",
            "<li>Smooth nut butters in tiny amounts if fat does not trigger urgency</li>",
            "</ul>",
            "<p>Read deeper food notes in <a href=\"/blog/white-rice-ibd-flare\">white rice during flares</a>, <a href=\"/blog/banana-ibd-crohns-colitis\">bananas and IBD</a>, <a href=\"/blog/congee-rice-porridge-ibd\">congee</a>, <a href=\"/blog/chicken-protein-ibd\">chicken protein</a>, and <a href=\"/blog/eggs-ibd-nutrition\">eggs</a>.</p>",
            "<h2>Protein still matters when appetite drops</h2>",
            "<p>Flares raise protein needs for healing while appetite falls. Missing protein for days accelerates muscle loss and fatigue. Aim for whatever your clinician or dietitian has recommended, often distributed across the day. Softer options include eggs, Greek yogurt if lactose is tolerated, tofu, ground turkey, fish, or oral nutrition shakes your team approves.</p>",
            "<p>If solid food intake collapses, ask early about oral nutrition supplements or enteral nutrition. See <a href=\"/blog/protein-shakes-ons-ibd\">protein shakes and oral nutrition</a>, <a href=\"/blog/enteral-nutrition-ibd\">enteral nutrition overview</a>, and <a href=\"/blog/taste-fatigue-enteral-formula-ibd\">taste fatigue with formula</a>.</p>",
            "<h2>Foods many people pause during loud flares</h2>",
            "<p>Pause lists are individual. A food that bothers one person may be fine for another. Patterns that often get paused temporarily include:</p>",
            '<ul class="blog-list">',
            "<li>Raw cruciferous vegetables, large salads, corn skins, and tough peels</li>",
            "<li>Very spicy sauces, heavy fried foods, and large high-fat meals</li>",
            "<li>Sugar alcohols in sugar-free gum or candy that worsen gas and loose stools</li>",
            "<li>Alcohol and high-caffeine energy drinks if they worsen urgency</li>",
            "<li>Dairy for people with lactose intolerance during inflammation</li>",
            "<li>Seeds, nuts, or popcorn if your team has flagged strictures</li>",
            "</ul>",
            "<p>Pair this with <a href=\"/blog/low-residue-diet-flare\">low-residue ideas</a>, <a href=\"/blog/dairy-lactose-ibd\">dairy and lactose</a>, <a href=\"/blog/onion-garlic-ibd-fodmap\">onion and garlic FODMAP notes</a>, and <a href=\"/blog/gas-bloating-ibd\">gas and bloating</a>.</p>",
            "<h2>Hydration is part of the flare-food plan</h2>",
            "<p>Frequent stools, fever, and reduced intake pull water and electrolytes. Sipping through the day beats occasional large gulps. Oral rehydration solutions, diluted juice if tolerated, broths, and water all have roles. Watch for dizziness, dark urine, dry mouth, or rapid heartbeat, and contact care sooner if fluids will not stay down.</p>",
            "<p>See <a href=\"/blog/hydration-tips-ibd\">hydration tips</a>, <a href=\"/guides/ibd-hydration-fluids\">hydration fluids guide</a>, <a href=\"/blog/electrolytes-flare-ibd\">electrolytes during flares</a>, and <a href=\"/blog/dehydration-ibd-warning-signs\">dehydration warning signs</a>.</p>",
            "<h2>Crohn's vs ulcerative colitis food differences</h2>",
            "<p>Ulcerative colitis flares often center on bloody diarrhea and rectal urgency, so lower-residue plates and careful dairy trials are common discussion points. Small-bowel Crohn's may add nausea, early fullness, or post-meal pain if narrowing is present. If you have known strictures, ask which fiber textures are restricted before experimenting. Disease location matters more than internet one-size lists.</p>",
            "<p>Compare <a href=\"/guides/crohns-disease-diet-nutrition\">Crohn's diet nutrition guide</a>, <a href=\"/guides/ulcerative-colitis-diet-foods\">ulcerative colitis diet foods</a>, and the overview in <a href=\"/blog/crohns-diet-overview-ibd\">Crohn's diet overview</a>.</p>",
            "<h2>A sample day many patients draft with a dietitian</h2>",
            "<p>This is an illustration, not a prescription. Adjust for allergies, cultural staples, ostomy output, diabetes, and clinician advice.</p>",
            '<ul class="blog-list">',
            "<li><strong>Breakfast:</strong> scrambled eggs, white toast or soft rice, ripe banana, oral rehydration sip</li>",
            "<li><strong>Mid-morning:</strong> yogurt or lactose-free alternative, or a small oral nutrition shake</li>",
            "<li><strong>Lunch:</strong> tender chicken and white rice with peeled cooked carrot</li>",
            "<li><strong>Afternoon:</strong> applesauce or smooth peanut butter on soft bread if tolerated</li>",
            "<li><strong>Dinner:</strong> baked fish or turkey, mashed potato without skins, zucchini cooked soft</li>",
            "<li><strong>Evening:</strong> warm broth or tea without heavy caffeine if evenings worsen urgency</li>",
            "</ul>",
            "<p>Explore individual foods people look up often: <a href=\"/blog/avocado-ibd\">avocado</a>, <a href=\"/blog/chocolate-ibd\">chocolate</a>, <a href=\"/blog/tortillas-ibd\">tortillas</a>, <a href=\"/blog/oranges-citrus-ibd\">citrus</a>, <a href=\"/blog/tea-ibd\">tea</a>, and <a href=\"/blog/potato-ibd-white\">white potatoes</a>.</p>",
            "<h2>When food alone is not enough</h2>",
            "<p>Call your GI team if you cannot keep fluids down, are losing weight quickly, see escalating blood, have severe pain with vomiting, or feel lightheaded. Nutrition support, steroids, infection testing, or therapy changes may be needed. Food strategies support care; they do not replace it.</p>",
            "<p>Use <a href=\"/blog/when-to-call-gi-vs-er-ibd\">GI nurse line vs ER</a>, <a href=\"/blog/flare-symptoms-ibd\">flare symptoms</a>, and <a href=\"/blog/vomiting-obstruction-ibd-warning-signs\">vomiting and obstruction warnings</a>.</p>",
            "<h2>Rebuilding the plate after a flare</h2>",
            "<p>As symptoms quiet, reintroduce one food at a time every few days while logging stool, pain, and energy. Prioritize colorful plants, fiber your anatomy can handle, and enjoyable cultural foods rather than staying on white-rice-only forever. Dietitians can pace reintroduction after exclusive enteral nutrition or major therapy changes.</p>",
            "<p>See <a href=\"/blog/food-reintroduction-after-een-ibd\">food reintroduction after EEN</a>, <a href=\"/blog/what-remission-means-ibd\">what remission means</a>, <a href=\"/blog/complete-ibd-nutrition-guide\">complete IBD nutrition guide</a>, and the book landing at <a href=\"/eating-with-ibd\">Eating With IBD</a>.</p>",
            "<h2>Questions worth asking your care team</h2>",
            '<ul class="blog-list">',
            "<li>Which textures should I limit if I have strictures or an ostomy?</li>",
            "<li>Do I need oral nutrition supplements or labs for iron, B12, vitamin D, or zinc?</li>",
            "<li>How long should this gentler pattern last before we expand foods?</li>",
            "<li>Would a short supervised low-residue or FODMAP trial help symptoms while inflammation is treated?</li>",
            "<li>When should weight loss or poor intake trigger a same-week visit?</li>",
            "</ul>",
            "<p>Related: <a href=\"/guides/what-should-i-eat-crohns-colitis\">what should I eat</a>, <a href=\"/tools/food-pain-tracker\">food pain tracker</a>, <a href=\"/blog/tracking-food-symptoms-ibdpal\">tracking food and symptoms</a>, <a href=\"/visit-prep\">visit prep</a>.</p>",
        ),
    },
    {
        "slug": "crohns-diet-overview-ibd",
        "title": "Crohn's Diet Overview: Flare, Remission, and What \"Diet\" Really Means",
        "description": "Clear Crohn's diet overview for patients: no single cure diet, flare vs remission eating, protein, fiber timing, and clinic questions. Education only.",
        "category": "Nutrition · September 2026",
        "date_display": "September 13, 2026",
        "date_iso": "2026-09-13T16:10:00Z",
        "asset_dir": "gut-nutrition",
        "images": ["ulcerative-colitis-crohns-nutrition_1.jpg"],
        "alts": ["Nutrition education materials for Crohn's disease eating patterns"],
        "share": "Crohn's diet overview: flare vs remission eating without diet myths. Education only.",
        "resource_category": "nutrition",
        "match_terms": [
            "crohn diet",
            "crohns diet",
            "crohn's diet",
            "diet for crohn",
            "what to eat crohn",
            "crohn's disease diet",
        ],
        "tags": [
            "crohn diet",
            "Crohn's",
            "nutrition",
            "remission",
            "flare",
            "fiber",
            "protein",
            "diet",
        ],
        "body": p(
            "<p>Searches for <strong>Crohn diet</strong> or <strong>Crohn's diet</strong> spike whenever symptoms change. People want a map: what helps in a flare, what supports remission, and which internet rules to ignore. There is no single Crohn's cure diet. The best pattern depends on disease location, strictures, surgeries, medicines, culture, and tolerances. This overview is educational, not a meal prescription.</p>",
            "<h2>The most important mindset shift</h2>",
            "<p>Food can ease symptoms and protect nutrition status. Medicine treats inflammation. Confusing those jobs leads to under-eating, fear, and delayed care. A useful Crohn's diet plan protects calories and micronutrients, reduces symptom triggers you have verified, and stays flexible as disease activity changes.</p>",
            "<p>Use <a href=\"/guides/crohns-disease-diet-nutrition\">the Crohn's diet nutrition guide</a>, <a href=\"/guides/what-should-i-eat-crohns-colitis\">what should I eat</a>, and <a href=\"/blog/complete-ibd-nutrition-guide\">the complete IBD nutrition guide</a> alongside this overview.</p>",
            "<h2>Flare phase: gentler, not empty</h2>",
            "<p>During active Crohn's, many people prefer smaller meals, softer textures, and less insoluble fiber. That might mean white rice, peeled cooked vegetables, tender proteins, and careful dairy trials. The risk is cutting so many foods that weight and strength fall. If intake collapses, ask about oral supplements or enteral nutrition early.</p>",
            "<p>See the companion hub <a href=\"/blog/flare-foods-ibd\">flare foods for IBD</a>, <a href=\"/guides/foods-to-eat-crohns-flare\">foods to eat in a Crohn's flare</a>, and <a href=\"/blog/low-residue-diet-flare\">low-residue diet in a flare</a>.</p>",
            "<h2>Remission phase: rebuild variety on purpose</h2>",
            "<p>Remission is the time to widen the plate, not stay stuck on beige foods forever. Mediterranean-style patterns, adequate protein, colorful plants your gut accepts, and enjoyable cultural staples support long-term health. Reintroduce one change at a time and log outcomes for clinic visits.</p>",
            "<p>Read <a href=\"/blog/what-remission-means-ibd\">what remission means</a>, <a href=\"/blog/anti-inflammatory-diet-ibd\">anti-inflammatory diet themes</a>, <a href=\"/blog/mediterranean-diet-autoimmune\">Mediterranean pattern notes</a>, and <a href=\"/blog/protein-meal-plan-ibd-remission\">protein meal ideas in remission</a>.</p>",
            "<h2>Fiber is timing, not a moral rule</h2>",
            "<p>Fiber is not universally bad in Crohn's. Soluble fiber can be soothing for some people. Insoluble skins, seeds, and raw salads can aggravate others, especially with strictures. Ask your clinician whether your anatomy needs temporary fiber limits. Blind lifelong low-fiber diets can worsen constipation or micronutrient gaps for the wrong patient.</p>",
            "<p>Deepen with <a href=\"/blog/fiber-and-ibd-diet\">fiber and the IBD diet</a> and <a href=\"/blog/fiber-prebiotics-enteral-feeds-microbiome\">fiber, prebiotics, and feeds</a>.</p>",
            "<h2>Protein, calories, and unintentional weight loss</h2>",
            "<p>Inflammation and diarrhea raise energy needs while nausea lowers intake. Unintentional weight loss deserves a clinic conversation, not only a new grocery list. Prioritize protein at each eating occasion and ask about shakes if solids are hard. Track weight weekly during unstable periods.</p>",
            "<p>See <a href=\"/blog/ibd-unintentional-weight-changes\">unintentional weight changes</a>, <a href=\"/guides/protein-healing-ibd-flare\">protein for healing</a>, and <a href=\"/blog/protein-shakes-ons-ibd\">oral nutrition shakes</a>.</p>",
            "<h2>Micronutrients Crohn's patients ask about often</h2>",
            "<p>Iron, B12, folate, vitamin D, calcium, zinc, magnesium, and potassium come up repeatedly after small-bowel disease or resection. Food helps, but labs and supplements may still be needed. Do not start high-dose iron or megavitamins without guidance if they worsen stools or interact with medicines.</p>",
            "<p>Browse <a href=\"/blog/micronutrients-ibd-deficiencies\">micronutrient deficiencies</a>, <a href=\"/blog/anemia-iron-deficiency-ibd\">iron deficiency anemia</a>, <a href=\"/blog/iron-b12-vitamin-d-ibd\">iron, B12, and vitamin D</a>, and <a href=\"/blog/how-ibdpal-nutrition-targets-work\">nutrition targets in IBDPal</a>.</p>",
            "<h2>Popular named diets: how to think about them</h2>",
            "<p>Exclusive enteral nutrition, partial enteral nutrition, Mediterranean patterns, and carefully supervised elimination trials each have different evidence and practical burdens. Social media \"autoimmune diets,\" juice cleanses, and extreme carnivore claims often overpromise. If you try a structured plan, do it with a clinician and a plan to stop if weight or labs worsen.</p>",
            "<p>Compare <a href=\"/blog/enteral-nutrition-ibd\">enteral nutrition</a>, <a href=\"/blog/exclusive-vs-partial-enteral-nutrition-crohns\">EEN vs PEN</a>, <a href=\"/blog/fodmap-diet-crohns-colitis\">FODMAP basics</a>, <a href=\"/blog/carnivore-diet-ibd-myths\">carnivore myths</a>, and <a href=\"/blog/juice-cleanse-detox-ibd\">juice cleanse cautions</a>.</p>",
            "<h2>Cultural staples belong in a Crohn's diet plan</h2>",
            "<p>Rice porridge, dal textures, soft chapati, paneer, tortillas, and other staples can fit when prepared for your current tolerance. A good plan respects culture instead of importing someone else's grocery list. Ask a dietitian how to adapt family recipes during flares and remissions.</p>",
            "<p>Examples: <a href=\"/blog/congee-rice-porridge-ibd\">congee</a>, <a href=\"/blog/dal-lentils-ibd\">dal</a>, <a href=\"/blog/chapati-roti-ibd\">chapati</a>, <a href=\"/blog/paneer-ibd\">paneer</a>, <a href=\"/blog/tortillas-ibd\">tortillas</a>.</p>",
            "<h2>Tracking that makes clinic visits faster</h2>",
            "<p>Log stool frequency, blood, pain after meals, skipped foods, and weight. Note whether symptoms track with missed medicines or infection exposures. Apps like IBDPal or a simple notebook beat memory alone when comparing flare and remission weeks.</p>",
            "<p>Try <a href=\"/tools/food-pain-tracker\">food pain tracker</a>, <a href=\"/blog/tracking-food-symptoms-ibdpal\">tracking food and symptoms</a>, and <a href=\"/visit-prep\">visit prep</a>.</p>",
            "<h2>Questions for your gastroenterologist or dietitian</h2>",
            '<ul class="blog-list">',
            "<li>Given my disease location and surgeries, which textures should I limit?</li>",
            "<li>What weight or lab trend should trigger nutrition support?</li>",
            "<li>Is a short elimination trial useful, or should we focus on treating inflammation first?</li>",
            "<li>Which micronutrients should we check this season?</li>",
            "<li>How do my medicines (steroids, methotrexate, biologics) change nutrition priorities?</li>",
            "</ul>",
            "<p>Related: <a href=\"/eating-with-ibd\">Eating With IBD book</a>, <a href=\"/blog/eating-with-ibd-book-guide\">book guide</a>, <a href=\"/newly-diagnosed\">newly diagnosed hub</a>, <a href=\"/resources\">resource library</a>.</p>",
        ),
    },
]


def more_posts() -> list[dict]:
    """Remaining four posts kept separate for file readability."""
    return [
        {
            "slug": "ibd-surgery-peer-support",
            "title": "IBD Surgery and Peer Support: Finding People Who Understand the Road Ahead",
            "description": "How to find IBD surgery support groups, what to ask before and after resection or ostomy surgery, and how peer support fits with clinical care. Education only.",
            "category": "Support · September 2026",
            "date_display": "September 13, 2026",
            "date_iso": "2026-09-13T16:20:00Z",
            "asset_dir": "icn-ostomy",
            "images": ["icn-ostomy_1.jpg"],
            "alts": ["Supportive education context for IBD surgery and ostomy peer support"],
            "share": "IBD surgery and peer support: how to find people and questions to ask. Education only.",
            "resource_category": "wellness",
            "match_terms": [
                "having surgery would like support group",
                "ibd surgery support",
                "ostomy support group",
                "crohn surgery support",
                "support group after surgery",
                "ibd peer support surgery",
            ],
            "tags": [
                "surgery",
                "support group",
                "ostomy",
                "peer support",
                "Crohn's",
                "colitis",
                "recovery",
            ],
            "body": p(
                "<p>People typing <strong>having surgery would like support group</strong> are usually not looking for another pamphlet. They want humans who have walked resection, ostomy, J-pouch, or abscess drainage pathways and can say what the first weeks actually feel like. Peer support does not replace your surgeon or gastroenterologist. It reduces isolation and helps you ask better clinical questions.</p>",
                "<h2>Why surgery raises a different kind of loneliness</h2>",
                "<p>Medical visits cover risks, consent, and wound care. Friends may not know how to talk about stoma bags, night emptying, body image, or fear of recurrence. A well-run support space normalizes those topics and points you back to clinicians when red flags appear.</p>",
                "<p>Start with <a href=\"/guides/ibd-support-near-me\">IBD support near me</a>, <a href=\"/guides/find-ccf-chapter-support-group\">CCF chapter and support group finder</a>, and <a href=\"/guides/foundation-ibd-surgery-ostomy\">Foundation surgery and ostomy themes</a>.</p>",
                "<h2>Types of support that help around surgery</h2>",
                '<ul class="blog-list">',
                "<li><strong>Local Crohn's &amp; Colitis Foundation groups</strong> for disease-wide peer connection</li>",
                "<li><strong>Ostomy visitor or WOC nurse programs</strong> for practical pouch and skin tips</li>",
                "<li><strong>Hospital pre-hab or education classes</strong> for bowel prep, lines, and recovery expectations</li>",
                "<li><strong>Online moderated communities</strong> when geography or energy limits in-person meetings</li>",
                "<li><strong>Caregiver circles</strong> so partners and parents have their own questions answered</li>",
                "</ul>",
                "<p>Also see <a href=\"/guides/living-with-ostomy-ibd\">living with an ostomy</a>, <a href=\"/blog/ostomy-basics-ibd\">ostomy basics</a>, and caregiver notes in <a href=\"/blog/icn-caregiver-coping-resource\">caregiver coping</a>.</p>",
                "<h2>Before surgery: questions peers often remind you to ask</h2>",
                "<p>Bring a notebook to surgical consults. Peer mentors frequently suggest clarifying:</p>",
                '<ul class="blog-list">',
                "<li>What operation is planned, and what tissue will be removed or diverted?</li>",
                "<li>Will an ostomy be temporary or permanent, and who teaches pouch care?</li>",
                "<li>How will pain, nutrition, and IBD medicines be handled in the hospital?</li>",
                "<li>What complications should trigger a night call versus a clinic message?</li>",
                "<li>When can I shower, drive, lift, return to work or school, and travel?</li>",
                "</ul>",
                "<p>Pair prep with <a href=\"/visit-prep\">visit prep</a>, <a href=\"/blog/hospital-feeding-ibd-enteral-parenteral\">hospital feeding notes</a>, and <a href=\"/blog/enteral-nutrition-after-ibd-surgery\">enteral nutrition after surgery</a>.</p>",
                "<h2>The first weeks after: what support groups help normalize</h2>",
                "<p>Fatigue, irregular output, wound anxiety, sleep disruption, and mood swings are common themes. Peers can share packing lists, clothing tips, and pacing ideas. They should never tell you to stop prescribed medicines or skip imaging. If someone pushes miracle products, step back and ask your clinical team.</p>",
                "<p>Watch for dehydration, obstruction symptoms, fever, or wound problems using <a href=\"/blog/vomiting-obstruction-ibd-warning-signs\">vomiting and obstruction warnings</a>, <a href=\"/blog/dehydration-ibd-warning-signs\">dehydration signs</a>, and <a href=\"/blog/when-to-call-gi-vs-er-ibd\">GI vs ER</a>.</p>",
                "<h2>How to evaluate a support group quickly</h2>",
                '<ul class="blog-list">',
                "<li>Is there a moderator or clear community guidelines?</li>",
                "<li>Do members redirect medical decisions to clinicians?</li>",
                "<li>Are teens, adults, ostomy, and J-pouch experiences labeled clearly?</li>",
                "<li>Is the tone practical rather than competitive about \"worst case\" stories?</li>",
                "<li>Can you listen first without sharing until you feel safe?</li>",
                "</ul>",
                "<h2>Ostomy-specific peer support</h2>",
                "<p>Living with a stoma is a skill set. Peer visitors and ostomy nurses help with bag choice, leaks, skin barriers, intimacy questions, and swimming or sports confidence. Ask your hospital whether a visitor program is available before discharge.</p>",
                "<p>Read <a href=\"/blog/swimming-pool-beach-ibd-ostomy\">swimming with an ostomy</a>, <a href=\"/blog/travel-with-ibd\">travel with IBD</a>, and workplace notes in <a href=\"/blog/workplace-school-ibd-rights\">workplace and school rights</a>.</p>",
                "<h2>Mental health is part of surgical recovery</h2>",
                "<p>Grief about body change, fear of recurrence, and decision fatigue are common. Ask your IBD team for counseling referrals. Peer support helps, and so does professional mental health care when anxiety or depression take over daily function.</p>",
                "<p>See <a href=\"/blog/ibd-depression-anxiety\">depression and anxiety with IBD</a> and <a href=\"/blog/stress-coping-ibd\">stress coping</a>.</p>",
                "<h2>A simple outreach script</h2>",
                "<p>If cold-calling a group feels hard, try: \"I have Crohn's or colitis surgery coming up and I am looking for peer support about recovery and daily life. Are there meetings or mentors for people before and after surgery?\" Save the time, format, and contact in your phone next to your clinic numbers.</p>",
                "<h2>Questions for your surgical and GI teams</h2>",
                '<ul class="blog-list">',
                "<li>Which local support programs do you recommend for my procedure?</li>",
                "<li>Who is my wound or ostomy nurse after discharge?</li>",
                "<li>What nutrition plan should I follow for the first two weeks?</li>",
                "<li>When should IBD maintenance therapy restart?</li>",
                "<li>What follow-up imaging or scopes are planned?</li>",
                "</ul>",
                "<p>Related: <a href=\"/guides/ibd-support-near-me\">support near me</a>, <a href=\"/flare-help\">flare help</a>, <a href=\"/newly-diagnosed\">newly diagnosed</a>, <a href=\"/contact\">contact IBDPal</a>.</p>",
            ),
        },
        {
            "slug": "adalimumab-dose-frequency-ibd",
            "title": "Adalimumab (Humira) Dose and Frequency in IBD: Questions to Ask Your Clinic",
            "description": "Patient education on adalimumab (Humira) dosing language, induction vs maintenance, biosimilars, missed doses, and clinic questions. Not prescribing advice.",
            "category": "Medications · September 2026",
            "date_display": "September 13, 2026",
            "date_iso": "2026-09-13T16:30:00Z",
            "asset_dir": "humira-fatigue",
            "images": ["humira-fatigue_1.jpg"],
            "alts": ["Medication education context for adalimumab Humira dosing questions"],
            "share": "Adalimumab (Humira) dose and frequency: questions to ask your IBD clinic. Education only.",
            "resource_category": "treatment",
            "match_terms": [
                "adalimumab dose and frequency",
                "humira dose",
                "humira frequency",
                "adalimumab dosing",
                "how often humira",
                "humira every other week",
            ],
            "tags": [
                "adalimumab",
                "Humira",
                "biologics",
                "dosing",
                "frequency",
                "biosimilar",
                "Crohn's",
                "colitis",
            ],
            "body": p(
                "<p>Searches for <strong>adalimumab dose and frequency</strong> are common after a new prescription, a prior authorization letter, or a conversation about biosimilars. Adalimumab (often known by the brand Humira, plus multiple biosimilars) is a biologic used in Crohn's disease and ulcerative colitis. Exact dose, injection schedule, and escalation decisions belong to your gastroenterologist. This article explains the language you will hear and the questions that make visits safer. It is not a dosing calculator.</p>",
                "<h2>Induction vs maintenance in plain language</h2>",
                "<p>Many biologic plans start with higher or more frequent dosing to quiet inflammation (induction), then move to a maintenance rhythm. Your letter or pharmacy calendar may show loading injections followed by every-other-week or weekly maintenance depending on the plan your clinician chose. Do not copy a schedule from a forum post. Device type, disease severity, body weight considerations in some contexts, and prior biologic failure all influence the written order.</p>",
                "<p>Background reading: <a href=\"/blog/understanding-biologics-ibd\">understanding biologics</a>, <a href=\"/blog/starting-biologic-first-12-weeks\">first 12 weeks on a biologic</a>, and <a href=\"/blog/humira-fatigue-ibd\">Humira and fatigue</a>.</p>",
                "<h2>What \"dose and frequency\" documents usually include</h2>",
                '<ul class="blog-list">',
                "<li>Medication name (adalimumab or a specific biosimilar name)</li>",
                "<li>Strength per injection and number of pens or syringes per date</li>",
                "<li>Injection day schedule and whether a loading sequence is included</li>",
                "<li>Storage, travel, and missed-dose instructions from the pharmacy or specialty pharmacy</li>",
                "<li>Lab monitoring and infection precautions your clinic expects</li>",
                "</ul>",
                "<p>If the paperwork and the verbal plan disagree, call before injecting. Specialty pharmacies and clinics sometimes update schedules after insurance review.</p>",
                "<h2>Weekly vs every-other-week conversations</h2>",
                "<p>Patients often hear that some people stay on every-other-week dosing while others are moved to weekly injections if drug levels, symptoms, or inflammatory markers suggest a need. Escalation is a clinical judgment that may involve therapeutic drug monitoring, calprotectin, scope findings, and shared goals. Never change frequency on your own because symptoms flared for two days.</p>",
                "<p>Related labs and flare context: <a href=\"/blog/reading-ibd-labs-calprotectin-crp\">calprotectin and CRP</a>, <a href=\"/blog/flare-symptoms-ibd\">flare symptoms</a>, and <a href=\"/blog/steroid-taper-what-to-expect-ibd\">steroid taper expectations</a>.</p>",
                "<h2>Biosimilars and interchangeable products</h2>",
                "<p>Insurance plans increasingly cover adalimumab biosimilars. Your clinic should tell you the exact product name, training for the device, and whether a pharmacy substitution is expected. Ask how to report injection-site reactions or new symptoms after a switch. Education pages about biosimilars are not the same as your personal order.</p>",
                "<p>See also vaccines and infection planning in <a href=\"/blog/vaccines-biologics-immunosuppressants-ibd\">vaccines with biologics</a> and access themes in <a href=\"/blog/prior-authorization-biologics-timeline\">prior authorization timeline</a>.</p>",
                "<h2>Missed doses, travel, and timing tips patients ask about</h2>",
                "<p>Specialty pharmacies usually provide a missed-dose window. If you are late, call them or the clinic rather than double-injecting. For travel, plan refrigeration or insulated storage as instructed, pack extra supplies, and keep medication in carry-on bags. Injection-day fatigue, mild injection-site redness, or temporary soreness can happen; fever, severe rash, chest symptoms, or signs of infection need prompt clinical advice.</p>",
                "<p>Practical companions: <a href=\"/blog/biologics-travel-ibd\">traveling with biologics</a>, <a href=\"/blog/infusion-day-what-to-expect\">infusion day expectations</a> for clinic-administered therapies, and <a href=\"/blog/ibd-flare-go-bag\">flare go-bag</a>.</p>",
                "<h2>Fatigue, infection risk, and when to hold a dose</h2>",
                "<p>Doctors sometimes hold or delay a biologic during significant infection. That decision is individualized. Do not skip doses because of ordinary tiredness without asking. Track energy, fever, cough, urinary symptoms, and wound issues so the nurse line can advise quickly.</p>",
                "<p>Read <a href=\"/blog/humira-fatigue-ibd\">Humira and fatigue</a>, <a href=\"/blog/fever-ibd-flare-or-infection\">fever: flare or infection</a>, and <a href=\"/blog/when-to-call-gi-vs-er-ibd\">when to call GI vs ER</a>.</p>",
                "<h2>What to bring to a dosing conversation</h2>",
                '<ul class="blog-list">',
                "<li>Current injection calendar with dates actually taken</li>",
                "<li>Symptom timeline since the last change in therapy</li>",
                "<li>Recent labs, stool studies, and scope summaries if you have them</li>",
                "<li>Insurance letters naming the covered product</li>",
                "<li>Questions about pregnancy planning, surgery timing, or vaccines</li>",
                "</ul>",
                "<h2>Questions to ask before your next injection cycle</h2>",
                '<ul class="blog-list">',
                "<li>What is my exact induction and maintenance schedule in writing?</li>",
                "<li>Which product name should appear on the pen or syringe?</li>",
                "<li>When would we consider weekly dosing, drug levels, or a therapy switch?</li>",
                "<li>What infections or surgeries require holding a dose?</li>",
                "<li>Who do I call for missed-dose advice after hours?</li>",
                "<li>How do biosimilar switches work with my insurance this year?</li>",
                "</ul>",
                "<p>Related: <a href=\"/guides/ibd-medications-overview\">medications overview</a>, <a href=\"/blog/understanding-biologics-ibd\">biologics guide</a>, <a href=\"/visit-prep\">visit prep</a>, <a href=\"/resources\">resource library</a>.</p>",
            ),
        },
        {
            "slug": "periods-menstrual-cycle-ibd",
            "title": "Periods and IBD: How the Menstrual Cycle Can Interact with Gut Symptoms",
            "description": "Menstrual cycle and IBD: tracking period-week flares, pain overlap, iron loss, contraception questions, and clinic talking points. Education only.",
            "category": "Wellness · September 2026",
            "date_display": "September 13, 2026",
            "date_iso": "2026-09-13T16:40:00Z",
            "asset_dir": "pregnancy-ibd",
            "images": ["pregnancy_1.jpg"],
            "alts": ["Calendar and wellness context for menstrual cycle tracking with IBD"],
            "share": "Periods and IBD: cycle tracking, iron, pain overlap, and clinic questions. Education only.",
            "resource_category": "wellness",
            "match_terms": [
                "periods",
                "period ibd",
                "menstrual cycle ibd",
                "period flare",
                "menstruation crohn",
                "ibd period symptoms",
            ],
            "tags": [
                "periods",
                "menstrual cycle",
                "hormones",
                "iron",
                "fatigue",
                "Crohn's",
                "colitis",
                "women's health",
            ],
            "body": p(
                "<p>People searching <strong>periods</strong> on an IBD site are usually noticing a pattern: gut urgency, cramping, fatigue, or joint pain that intensifies around menstruation. Hormonal shifts do not cause Crohn's or ulcerative colitis, but they can amplify symptoms already present. Tracking the overlap helps your gastroenterologist and gynecology or primary care clinicians separate cycle effects from true inflammatory flares.</p>",
                "<h2>What patients commonly notice around their period</h2>",
                '<ul class="blog-list">',
                "<li>More frequent stools or looser consistency in the days before bleeding starts</li>",
                "<li>Lower abdominal cramping that is hard to separate from IBD pain</li>",
                "<li>Heavier fatigue, brain fog, or sleep disruption</li>",
                "<li>Joint aches or headaches that cluster with PMS</li>",
                "<li>Nausea or appetite changes that shrink food intake for a few days</li>",
                "</ul>",
                "<p>Compare notes with <a href=\"/blog/flare-symptoms-ibd\">flare symptoms</a>, <a href=\"/blog/ibd-fatigue-brain-fog\">fatigue and brain fog</a>, and <a href=\"/blog/ibd-joint-pain-arthritis\">joint pain</a>.</p>",
                "<h2>How to track cycle and gut symptoms together</h2>",
                "<p>For two to three cycles, log period start and end dates, stool frequency, blood from the bowel versus menstrual blood, pain scores, missed work or school, and medicines taken for cramps. Note NSAID use carefully. Ibuprofen and similar medicines can irritate the gut and are often discouraged in IBD unless a clinician approves an exception.</p>",
                "<p>Tools and companions: <a href=\"/blog/tracking-food-symptoms-ibdpal\">tracking in IBDPal</a>, <a href=\"/blog/nsaids-ibd-risk\">NSAIDs and IBD</a>, and <a href=\"/visit-prep\">visit prep</a>.</p>",
                "<h2>Iron loss: periods plus IBD bleeding</h2>",
                "<p>Heavy menstrual bleeding plus intestinal blood loss raises anemia risk. Fatigue that worsens each cycle deserves a hemoglobin and iron panel conversation, not only more coffee. Ask whether periods are heavy enough to need gynecology input while GI inflammation is addressed.</p>",
                "<p>See <a href=\"/blog/anemia-iron-deficiency-ibd\">iron deficiency anemia</a>, <a href=\"/blog/iron-b12-vitamin-d-ibd\">iron, B12, and vitamin D</a>, and <a href=\"/guides/iron-deficiency-nutrition-ibd\">iron nutrition guide</a>.</p>",
                "<h2>Pain control that respects the gut</h2>",
                "<p>Heat, rest, hydration, and clinician-approved pain plans beat improvising with leftover NSAIDs. If opioids or frequent urgent-care visits become the pattern, ask for a coordinated plan between GI and gynecology. Endometriosis and IBD can coexist; unexplained pelvic pain deserves evaluation rather than being labeled \"just colitis\" forever.</p>",
                "<h2>Contraception, fertility planning, and medicines</h2>",
                "<p>Some people notice symptom changes after starting or stopping hormonal contraception. Others need contraception counseling because of teratogenic medicines such as methotrexate. Bring both your GI and reproductive health clinicians into the same plan before conception attempts. Biologic timing around pregnancy is individualized.</p>",
                "<p>Related: <a href=\"/blog/pregnancy-ibd\">pregnancy and IBD themes</a>, <a href=\"/guides/ibd-medications-overview\">medications overview</a>, and <a href=\"/blog/understanding-biologics-ibd\">biologics guide</a>.</p>",
                "<h2>Teen and young adult considerations</h2>",
                "<p>Adolescents with IBD may start periods during active disease, steroid courses, or under-nutrition. Delayed or irregular cycles can reflect illness stress, low body weight, or other endocrine issues. School bathroom access and period supplies belong in accommodation plans alongside IBD needs.</p>",
                "<p>See <a href=\"/guides/pediatric-crohns-colitis-help\">pediatric Crohn's and colitis help</a>, <a href=\"/blog/workplace-school-ibd-rights\">school and workplace rights</a>, and <a href=\"/blog/social-life-dating-teens-ibd\">teen social life and dating</a>.</p>",
                "<h2>When cycle-week symptoms need a same-week call</h2>",
                '<ul class="blog-list">',
                "<li>Bowel bleeding that is clearly heavier than your menstrual baseline and IBD baseline</li>",
                "<li>Fever, severe abdominal pain, or vomiting with cycle symptoms</li>",
                "<li>Fainting, breathless fatigue, or suspected severe anemia</li>",
                "<li>Sudden inability to keep fluids or medicines down</li>",
                "</ul>",
                "<p>Use <a href=\"/blog/blood-in-stool-ibd-when-to-worry\">blood in stool guidance</a>, <a href=\"/blog/when-to-call-gi-vs-er-ibd\">GI vs ER</a>, and <a href=\"/ibd-red-flags-urgent-care\">red flags hub</a>.</p>",
                "<h2>Questions to bring to clinic</h2>",
                '<ul class="blog-list">',
                "<li>Do my logs look like cycle amplification, IBD flare, or both?</li>",
                "<li>Should we check iron studies around my period week?</li>",
                "<li>What pain medicines are safest for me?</li>",
                "<li>Do contraception choices interact with my IBD therapy goals?</li>",
                "<li>When should gynecology join the care team?</li>",
                "</ul>",
                "<p>Related: <a href=\"/blog/mucus-urgency-tenesmus-ibd\">urgency and tenesmus</a>, <a href=\"/blog/chronic-diarrhea-ibd-causes\">chronic diarrhea</a>, <a href=\"/resources\">resource library</a>.</p>",
            ),
        },
        {
            "slug": "eating-with-ibd-book-guide",
            "title": "Eating With IBD Book Guide: What It Covers and How to Use It With IBDPal",
            "description": "Guide to the Eating With IBD book: who it helps, how it pairs with IBDPal tools, flare vs remission chapters, and where to start. Education only.",
            "category": "Nutrition · September 2026",
            "date_display": "September 13, 2026",
            "date_iso": "2026-09-13T16:50:00Z",
            "asset_dir": "gut-nutrition",
            "images": ["ulcerative-colitis-crohns-nutrition_2.jpg"],
            "alts": ["Nutrition education materials related to the Eating With IBD book"],
            "share": "Eating With IBD book guide: what it covers and how to use it with IBDPal.",
            "resource_category": "nutrition",
            "match_terms": [
                "eating with ibd book",
                "eating with ibd",
                "ibd nutrition book",
                "ibdpal book",
                "aryan shashi kumar book",
                "crohn nutrition book",
            ],
            "tags": [
                "Eating With IBD",
                "book",
                "nutrition",
                "Amazon",
                "Crohn's",
                "colitis",
                "MediVue",
                "diet",
            ],
            "body": p(
                "<p>If you searched <strong>Eating With IBD book</strong>, you are looking for the practical nutrition companion from MediVue / IBDPal, written to help people living with Crohn's disease and ulcerative colitis make calmer food decisions. This page explains what the book is for, how it pairs with free IBDPal web tools, and where to start reading. It is educational marketing and patient navigation, not a substitute for your clinician or dietitian.</p>",
                "<h2>Where to open the book page</h2>",
                "<p>The main landing page is <a href=\"/eating-with-ibd\">Eating With IBD</a>. From there you can read the overview and follow the Amazon link when you are ready to purchase. Founder context lives on <a href=\"/founder\">the founder page</a> and in the About sections of IBDPal.</p>",
                "<h2>Who the book is designed to help</h2>",
                '<ul class="blog-list">',
                "<li>Newly diagnosed patients overwhelmed by conflicting diet advice</li>",
                "<li>People in flares who need gentler meal structure without starvation diets</li>",
                "<li>Patients in remission rebuilding variety and confidence</li>",
                "<li>Caregivers shopping and cooking for someone with IBD</li>",
                "<li>Readers who want clinic-ready questions, not miracle claims</li>",
                "</ul>",
                "<p>If you are in an emergency symptom pattern, pause the book and use <a href=\"/flare-help\">flare help</a> or <a href=\"/blog/when-to-call-gi-vs-er-ibd\">GI vs ER guidance</a> first.</p>",
                "<h2>How the book fits with free IBDPal content</h2>",
                "<p>The book organizes nutrition themes end to end. The website adds living updates, single-food articles, trackers, and local support directories. Use both: book for structured reading, site for searchable deep dives.</p>",
                "<p>High-traffic companions include <a href=\"/blog/flare-foods-ibd\">flare foods</a>, <a href=\"/blog/crohns-diet-overview-ibd\">Crohn's diet overview</a>, <a href=\"/blog/complete-ibd-nutrition-guide\">complete nutrition guide</a>, and <a href=\"/guides/what-should-i-eat-crohns-colitis\">what should I eat</a>.</p>",
                "<h2>Suggested reading paths</h2>",
                "<p><strong>If you are flaring:</strong> skim hydration, protein, and gentler textures first. Pair with <a href=\"/blog/flare-first-48-hours\">flare first 48 hours</a>, <a href=\"/blog/hydration-tips-ibd\">hydration tips</a>, and <a href=\"/blog/low-residue-diet-flare\">low-residue ideas</a>.</p>",
                "<p><strong>If you are newly diagnosed:</strong> start with mindset, clinic partnership, and micronutrients, then food rules. Use <a href=\"/newly-diagnosed\">newly diagnosed hub</a> and <a href=\"/blog/newly-diagnosed-first-30-days\">first 30 days</a>.</p>",
                "<p><strong>If you are rebuilding after EEN or hospital food:</strong> focus on reintroduction pacing with <a href=\"/blog/food-reintroduction-after-een-ibd\">food reintroduction after EEN</a> and <a href=\"/blog/enteral-nutrition-ibd\">enteral nutrition</a>.</p>",
                "<h2>Topics readers usually expect inside</h2>",
                '<ul class="blog-list">',
                "<li>How IBD changes digestion, absorption, and appetite</li>",
                "<li>Flare-first eating versus remission expansion</li>",
                "<li>Protein, fluids, and electrolyte basics</li>",
                "<li>Fiber timing and cultural staple adaptations</li>",
                "<li>Micronutrient gaps and lab-informed questions</li>",
                "<li>How to talk with a GI dietitian without shame</li>",
                "</ul>",
                "<p>Website deep dives that mirror those themes: <a href=\"/blog/micronutrients-ibd-deficiencies\">micronutrients</a>, <a href=\"/blog/fiber-and-ibd-diet\">fiber</a>, <a href=\"/blog/protein-meal-plan-ibd-remission\">protein in remission</a>, and food pages such as <a href=\"/blog/banana-ibd-crohns-colitis\">banana</a> or <a href=\"/blog/white-rice-ibd-flare\">white rice</a>.</p>",
                "<h2>How to use the book with IBDPal tracking</h2>",
                "<p>Read a chapter, pick one experiment (for example, protein at breakfast for a week), and log stool, pain, energy, and weight. Bring the log to clinic. Tracking turns book ideas into shared decision-making instead of lonely rule-following.</p>",
                "<p>Try <a href=\"/tools/food-pain-tracker\">food pain tracker</a>, <a href=\"/blog/tracking-food-symptoms-ibdpal\">tracking food and symptoms</a>, and <a href=\"/blog/how-ibdpal-nutrition-targets-work\">nutrition targets</a>.</p>",
                "<h2>What the book is not</h2>",
                '<ul class="blog-list">',
                "<li>Not a promise that diet alone remits IBD</li>",
                "<li>Not a reason to stop biologics, immunomodulators, or steroids</li>",
                "<li>Not individualized medical nutrition therapy for strictures, ostomy, or pediatrics without your team</li>",
                "<li>Not an attack on cultural foods or a demand for expensive specialty products</li>",
                "</ul>",
                "<h2>Buying and support details</h2>",
                "<p>Purchase links and cover details stay on <a href=\"/eating-with-ibd\">the Eating With IBD page</a>. For nonprofit and project context, see <a href=\"/about\">About</a> and <a href=\"/founder\">Founder</a>. For site feedback, use <a href=\"/contact\">Contact</a>.</p>",
                "<h2>Questions the book helps you bring to clinic</h2>",
                '<ul class="blog-list">',
                "<li>Which chapter themes match my disease location and surgeries?</li>",
                "<li>Should we involve a GI dietitian this quarter?</li>",
                "<li>Which labs should guide supplements while I change eating patterns?</li>",
                "<li>How long should a gentler flare menu last before we expand foods?</li>",
                "</ul>",
                "<p>Related: <a href=\"/resources\">resource library</a>, <a href=\"/blog/crohns-diet-overview-ibd\">Crohn's diet overview</a>, <a href=\"/blog/flare-foods-ibd\">flare foods</a>, <a href=\"/guides/crohns-disease-diet-nutrition\">Crohn's nutrition guide</a>.</p>",
            ),
        },
    ]


def ensure_image(post: dict) -> None:
    asset = BLOGS / "assets" / post["asset_dir"]
    asset.mkdir(parents=True, exist_ok=True)
    dest = asset / post["images"][0]
    if dest.exists() and dest.stat().st_size >= 1000:
        return
    if FALLBACK.exists():
        shutil.copy(FALLBACK, dest)


def patch_vercel(slugs: list[str]) -> None:
    text = VERCEL.read_text(encoding="utf-8")
    inserts = []
    for slug in slugs:
        needle = f'"/blog/{slug}"'
        if needle in text:
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
        "flare foods": "flare foods",
        "foods during a flare": "flare foods",
        "what to eat during flare": "flare foods",
        "flare diet": "flare foods",
        "crohn diet": "crohn diet",
        "crohns diet": "crohn diet",
        "crohn's diet": "crohn diet",
        "diet for crohn": "crohn diet",
        "eating with ibd book": "eating with ibd",
        "ibd nutrition book": "eating with ibd",
        "ibdpal book": "eating with ibd",
        "having surgery would like support group": "surgery support",
        "ibd surgery support": "surgery support",
        "ostomy support group": "surgery support",
        "adalimumab dose and frequency": "adalimumab",
        "humira dose": "adalimumab",
        "humira frequency": "adalimumab",
        "adalimumab dosing": "adalimumab",
        "period ibd": "periods",
        "menstrual cycle ibd": "periods",
        "period flare": "periods",
        "menstruation crohn": "periods",
    }
    aliases.update(extras)
    ALIASES.write_text(json.dumps(aliases, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("updated search-aliases.json")


def update_search_gap(posts: list[dict]) -> None:
    if SEARCH_GAP.exists():
        data = json.loads(SEARCH_GAP.read_text(encoding="utf-8"))
    else:
        data = {"posts": []}
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
    # crude strip tags
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


def main() -> None:
    posts = POSTS + more_posts()
    DATA.write_text(json.dumps(posts, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("wrote", DATA.name)
    slugs = []
    for post in posts:
        ensure_image(post)
        wc = word_count(post["body"])
        mins = max(1, round(wc / 200))
        out = BLOGS / f"{post['slug']}.html"
        out.write_text(render_post(post), encoding="utf-8")
        slugs.append(post["slug"])
        print(f"wrote {out.name} (~{wc} words, ~{mins} min)")
    patch_vercel(slugs)
    update_aliases(posts)
    update_search_gap(posts)
    print("Done.", len(slugs), "posts.")
    print("Next: amp + sitemap + sync_resources + home engagement")


if __name__ == "__main__":
    main()
