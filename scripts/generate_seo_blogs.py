#!/usr/bin/env python3
"""Generate SEO-focused blog posts: nutrition, diet, teen high school, and health topics."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402

BLOGS = ROOT / "blogs"

POSTS = [
    {
        "slug": "fodmap-diet-crohns-colitis",
        "title": "FODMAP Diet for Crohn's and Colitis: What Patients Search For",
        "description": "Low-FODMAP basics for IBD: what FODMAPs are, who may benefit, elimination phases, and working with a dietitian—not a DIY cure.",
        "category": "Nutrition · June 2026",
        "date_display": "June 15, 2026",
        "date_iso": "2026-06-15T12:00:00Z",
        "asset_dir": "fodmap-ibd",
        "images": ["fodmap_1.jpg"],
        "alts": ["Colorful vegetables and grains on a kitchen counter"],
        "share": "FODMAP diet basics for Crohn's and colitis—education only.",
        "body": """
<p>Search traffic around <strong>FODMAP diet Crohn's disease</strong> and <strong>low FODMAP ulcerative colitis</strong> is high—and confusing. FODMAPs are fermentable carbohydrates (fructans, lactose, polyols, and others) that can draw water into the gut and produce gas in some people. A low-FODMAP approach is <em>not</em> an IBD treatment; it may reduce <strong>functional symptoms</strong> like bloating and urgency when used with clinician guidance.</p>
<h2>Who Might Consider Low FODMAP?</h2>
<p>Patients with active inflammation still need medical therapy first. Some people in remission—or with overlapping irritable bowel–type symptoms—explore FODMAPs with an IBD dietitian to see if certain carbs worsen discomfort. Crohn's disease and colitis triggers remain individual.</p>
<h2>The Three Phases (Simplified)</h2>
<ul class="blog-list">
<li><strong>Restriction:</strong> Short-term lowering of high-FODMAP foods under supervision—usually weeks, not months alone.</li>
<li><strong>Reintroduction:</strong> Systematic testing to learn which groups you tolerate.</li>
<li><strong>Personalization:</strong> A sustainable pattern—not permanent elimination of all FODMAPs.</li>
</ul>
<h2>Common High-FODMAP Examples</h2>
<p>Onions, garlic, wheat in large amounts, some dairy, apples, cauliflower, and sugar alcohols (sorbitol, mannitol) appear on many lists. Lists change by portion size—another reason professional guidance helps.</p>
<h2>Cautions for Teens and Active Disease</h2>
<p>Restrictive diets during growth spurts can miss calories and calcium. Never replace prescribed IBD medication with diet experiments. Track symptoms in IBDPal and bring patterns to appointments.</p>
<h2>Questions for Your IBD Dietitian</h2>
<p>Is low FODMAP appropriate for my current inflammation level? How do we protect protein and micronutrients? Can we overlap with low-residue or other plans my team already suggested?</p>
""",
    },
    {
        "slug": "high-school-ibd-survival-guide",
        "title": "Crohn's and Colitis in High School: Bathrooms, 504 Plans, and Missing Class",
        "description": "Managing IBD in high school: bathroom access, 504 accommodations, explaining absences, and talking to teachers—education only.",
        "category": "Teen life · June 2026",
        "date_display": "June 16, 2026",
        "date_iso": "2026-06-16T12:00:00Z",
        "asset_dir": "high-school-ibd",
        "images": ["highschool_1.jpg"],
        "alts": ["Students in a bright school hallway"],
        "share": "High school with Crohn's or colitis—504 plans and bathroom basics.",
        "body": """
<p><strong>Managing Crohn's disease in high school</strong> or <strong>ulcerative colitis at school</strong> means juggling symptoms, stigma, and schedules. You are not alone—many districts support students through Section 504 plans and nurse partnerships.</p>
<h2>Bathroom Access Without Drama</h2>
<p>Urgency is a medical need, not bad behavior. A 504 plan can include unlimited bathroom passes, a buddy hall pass, preferential seating near exits, and permission to leave class without public explanation. Keep a clinician letter on file that describes functional needs without oversharing.</p>
<h2>504 Plan Basics for IBD</h2>
<ul class="blog-list">
<li>Extra time on tests and assignments during flares</li>
<li>Modified PE when medically needed</li>
<li>Access to water and snacks; refrigerator for biologics if applicable</li>
<li>Absence policies: home instruction or late work when documented</li>
</ul>
<p>Meet the school nurse and counselor before the year starts. Parents and teens can attend together; older students may lead the conversation.</p>
<h2>Missing Class and Keeping Up</h2>
<p>Track flare days in IBDPal exports to share with the team. Ask teachers for condensed notes or recorded lessons. Colleges notice effort and communication—not perfection during illness.</p>
<h2>Telling Friends (Your Choice)</h2>
<p>Some teens tell close friends; others use vague "stomach condition" scripts. Both are valid. See our article on <a href="/blog/social-life-dating-teens-ibd">social life and dating with IBD</a> for more peer strategies.</p>
<h2>When Symptoms Escalate at School</h2>
<p>Know your clinic's same-day line. Severe pain, heavy bleeding, or dehydration signs need urgent evaluation—not waiting until final bell.</p>
""",
    },
    {
        "slug": "teen-nutrition-ibd-growth",
        "title": "Nutrition for Teens With IBD: Growth, Protein, and School Lunches",
        "description": "Teen Crohn's and colitis nutrition: calories for growth, protein goals, cafeteria tips, and when poor growth needs a clinic call.",
        "category": "Nutrition · June 2026",
        "date_display": "June 17, 2026",
        "date_iso": "2026-06-17T12:00:00Z",
        "asset_dir": "teen-nutrition",
        "images": ["teen_nutrition_1.jpg"],
        "alts": ["Healthy lunch with fruit, sandwich, and vegetables"],
        "share": "Teen nutrition with IBD—growth, protein, and school lunches.",
        "body": """
<p>Parents often search <strong>teen Crohn's nutrition</strong> or <strong>IBD growth delay</strong> after noticing clothes fitting differently or growth charts flattening. Active inflammation steals calories and nutrients; healing requires enough fuel.</p>
<h2>Growth and Weight Monitoring</h2>
<p>Pediatric gastroenterologists track height velocity and BMI. Falling off your curve during puberty warrants discussion—medication adjustment, enteral nutrition, or supplement plans may be options your team already uses.</p>
<h2>Protein and Key Nutrients</h2>
<ul class="blog-list">
<li><strong>Protein:</strong> Eggs, yogurt, tender meats, tofu, smoothies—especially after steroid courses.</li>
<li><strong>Calcium &amp; vitamin D:</strong> Bones are building now; ask about labs and fortified foods.</li>
<li><strong>Iron:</strong> Fatigue plus heavy periods or intestinal loss—common teen combo; test, don't guess.</li>
</ul>
<h2>School Cafeteria Survival</h2>
<p>Identify two to three go-to meals that do not worsen your symptoms. Pack backup snacks if lines are long. Hydration matters in hot climates and during sports—see <a href="/blog/hydration-tips-ibd">hydration tips for IBD</a>.</p>
<h2>Restrictive Diets and Social Eating</h2>
<p>Low-residue or low-FODMAP trials should be time-limited and supervised. Teens need flexibility for pizza nights and team dinners when possible—perfection is not the goal; adequacy is.</p>
<h2>Tracking Helps Conversations</h2>
<p>Log meals, energy, and stools in IBDPal before dietitian visits. Patterns beat memory when school weeks blur together.</p>
""",
    },
    {
        "slug": "anti-inflammatory-diet-ibd",
        "title": "Anti-Inflammatory Diet and IBD: What Research Suggests (and What It Doesn't)",
        "description": "Anti-inflammatory eating with Crohn's or colitis: Mediterranean patterns, omega-3s, ultra-processed foods, and limits of diet-only claims.",
        "category": "Diet · June 2026",
        "date_display": "June 18, 2026",
        "date_iso": "2026-06-18T12:00:00Z",
        "asset_dir": "anti-inflammatory-ibd",
        "images": ["anti_inflammatory_1.jpg"],
        "alts": ["Mediterranean-style plate with vegetables and olive oil"],
        "share": "Anti-inflammatory diet and IBD—evidence-based overview.",
        "body": """
<p><strong>Anti-inflammatory diet Crohn's disease</strong> and <strong>anti-inflammatory diet ulcerative colitis</strong> searches spike after celebrity headlines. No food pattern replaces biologics, small molecules, or steroids when inflammation is active—but long-term eating still matters for health.</p>
<h2>Patterns With Supportive Data</h2>
<p>Many IBD dietitians discuss <strong>Mediterranean-style</strong> meals: vegetables, fruits, olive oil, fish, legumes when tolerated, and whole grains in remission. CD-TREAT and other research diets exist for specific situations—always clinician-led.</p>
<h2>Foods Often Limited During Flares</h2>
<p>Ultra-processed snacks, excessive alcohol, and large fatty meals may worsen symptoms for some people. That is different from claiming they "cause" IBD.</p>
<h2>Omega-3s and Fiber</h2>
<p>Fish and flax may support general health; fiber is reintroduced gradually in remission per team advice. Jumping to extreme exclusion cleanses can trigger malnutrition—especially in teens.</p>
<h2>Marketing vs. Medicine</h2>
<p>Supplements promising to "cure" colitis are red flags. Ask for PubMed-backed handouts from your center, not influencer meal plans.</p>
<h2>Pair Diet With Tracking</h2>
<p>Anti-inflammatory eating is personal. Use IBDPal food logs to see whether tomato sauce, dairy, or spicy foods correlate with <em>your</em> symptoms—not someone else's list online.</p>
""",
    },
    {
        "slug": "exercise-physical-activity-ibd",
        "title": "Exercise With Crohn's or Colitis: Staying Active Without Overdoing It",
        "description": "Can you play sports with IBD? Exercise benefits, flare pacing, ostomy and j-pouch tips, and when to rest—general health education.",
        "category": "Health · June 2026",
        "date_display": "June 19, 2026",
        "date_iso": "2026-06-19T12:00:00Z",
        "asset_dir": "exercise-ibd",
        "images": ["exercise_1.jpg"],
        "alts": ["Person jogging outdoors on a tree-lined path"],
        "share": "Exercise and IBD—staying active safely.",
        "body": """
<p>Teens and parents ask: <strong>Can you play sports with Crohn's disease?</strong> and <strong>Is exercise safe with ulcerative colitis?</strong> For most people in remission or mild disease, yes—with adjustments during flares and after surgery.</p>
<h2>Why Movement Helps</h2>
<p>Regular activity supports bone density, mood, sleep, and cardiovascular health—areas where IBD patients already face extra risk. It does not replace medication but complements care.</p>
<h2>During a Flare</h2>
<p>Prioritize rest, gentle stretching, and short walks if tolerated. Dehydration and anemia can make intense workouts unsafe—check hemoglobin and fluids with your team.</p>
<h2>High School Sports</h2>
<p>Coordinate with coaches using the same 504 documentation as classroom needs. Bathroom maps for away games, uniform comfort, and emergency kits reduce anxiety. See <a href="/blog/high-school-ibd-survival-guide">high school IBD guide</a> for school planning.</p>
<h2>After Ostomy or J-Pouch Surgery</h2>
<p>Many athletes return to running, swimming, and weight training with ostomy nurses' guidance on support garments and hydration. Progress gradually; soreness vs. surgical red flags should be reviewed with your surgeon.</p>
<h2>Building a Sustainable Routine</h2>
<p>Mix aerobic and resistance work when healthy. Track energy in IBDPal to learn your ceiling—some weeks 20 minutes counts as a win.</p>
""",
    },
    {
        "slug": "iron-b12-vitamin-d-ibd",
        "title": "Iron, B12, and Vitamin D With IBD: Deficiencies Patients Ask About",
        "description": "Common IBD nutrient deficiencies: iron anemia, B12 malabsorption, vitamin D, and lab questions to bring to your gastroenterologist.",
        "category": "Health · June 2026",
        "date_display": "June 20, 2026",
        "date_iso": "2026-06-20T12:00:00Z",
        "asset_dir": "vitamins-ibd",
        "images": ["vitamins_1.jpg"],
        "alts": ["Sunlight on a windowsill with a glass of water"],
        "share": "Iron, B12, and vitamin D with IBD—common deficiency questions.",
        "body": """
<p>Searches like <strong>iron deficiency Crohn's disease</strong>, <strong>B12 ulcerative colitis</strong>, and <strong>vitamin D IBD</strong> reflect real fatigue and bone-health worries. Malabsorption, bleeding, inflammation, and restricted diets all contribute.</p>
<h2>Iron and Anemia</h2>
<p>Low iron can cause breathlessness, pale skin, and brain fog—sometimes before obvious GI bleeding. Oral iron may irritate some guts; IV iron is common in IBD clinics. Menstruating teens need coordinated gynecology and GI follow-up.</p>
<h2>Vitamin B12</h2>
<p>Crohn's in the ileum or prior resections raise B12 deficiency risk. Long-term supplementation or injections may be needed even when you feel fine—levels are worth periodic labs.</p>
<h2>Vitamin D and Bone Health</h2>
<p>Steroids, inflammation, and limited sun exposure lower vitamin D. Adequate D supports bones alongside calcium, weight-bearing exercise, and treating active disease.</p>
<h2>Other Micronutrients</h2>
<p>Zinc, folate, magnesium, and protein status matter too—especially before surgery or biologic starts. One annual nutrition labs panel is typical in many centers; ask yours.</p>
<h2>Supplements: Smart, Not Random</h2>
<p>High-dose internet stacks can interact with medications. Bring bottles to visits. Food-first strategies plus targeted replacements beat guessing.</p>
""",
    },
    {
        "slug": "social-life-dating-teens-ibd",
        "title": "Social Life, Dating, and IBD as a Teen: Privacy, Friends, and Confidence",
        "description": "Teen life with Crohn's or colitis: telling friends, dating disclosure, parties, alcohol, and mental health check-ins—peer-focused education.",
        "category": "Teen life · June 2026",
        "date_display": "June 21, 2026",
        "date_iso": "2026-06-21T12:00:00Z",
        "asset_dir": "teen-social-ibd",
        "images": ["teen_social_1.jpg"],
        "alts": ["Teen friends laughing together outdoors"],
        "share": "Social life and dating with IBD as a teen—privacy and confidence.",
        "body": """
<p><strong>Dating with Crohn's disease</strong> and <strong>teen ulcerative colitis social life</strong> searches spike around homecoming and prom season. Illness does not cancel your right to friendships and romance—it changes how you plan.</p>
<h2>Choosing What to Share</h2>
<p>Layered disclosure works: "I have a chronic stomach condition" early; details with trusted people later. You owe no one your entire chart on a first date.</p>
<h2>Parties, Sleepovers, and Road Trips</h2>
<ul class="blog-list">
<li>Scout bathrooms and pack a small go-bag (supplies, wipes, change of clothes).</li>
<li>Have an exit phrase with a friend if symptoms spike.</li>
<li>Sleepovers: talk to the host parent privately if you need fridge space for meds.</li>
</ul>
<h2>Alcohol and Vaping</h2>
<p>Alcohol can trigger symptoms and interact with meds; many teens choose to skip. Peer pressure fades; your gut does not. Real friends respect boundaries.</p>
<h2>Body Image and Ostomies</h2>
<p>Bag hidden under formalwear, scars, steroid puffiness—normal insecurities. Online teen IBD communities (CCF, ImproveCareNow) normalize what school hallways do not show.</p>
<h2>Mental Health Matters</h2>
<p>Anxiety and depression rates are higher with IBD. School counselors, teletherapy, and crisis lines are strength moves—not weakness. Pair with <a href="/blog/stress-emotional-wellness-ibd">stress and mood with IBD</a> for coping tools.</p>
""",
    },
    {
        "slug": "protein-meal-plan-ibd-remission",
        "title": "High-Protein Meal Ideas for IBD Remission: Building Plates Your Gut Tolerates",
        "description": "IBD meal plan inspiration: high-protein breakfast, lunch, and dinner ideas for remission, gentle flare modifications, and dietitian follow-up.",
        "category": "Diet · June 2026",
        "date_display": "June 22, 2026",
        "date_iso": "2026-06-22T12:00:00Z",
        "asset_dir": "protein-meals-ibd",
        "images": ["protein_meals_1.jpg"],
        "alts": ["Balanced dinner plate with fish, rice, and vegetables"],
        "share": "High-protein IBD meal ideas for remission—education only.",
        "body": """
<p><strong>High protein diet Crohn's disease</strong>, <strong>IBD meal plan</strong>, and <strong>ulcerative colitis protein</strong> are among the most common nutrition searches. Protein supports healing, muscle, and energy when inflammation is controlled.</p>
<h2>How Much Protein?</h2>
<p>Needs vary by age, surgery history, and activity. Many adults discuss roughly 1–1.2 g per kg body weight with dietitians during recovery—your clinic may personalize higher or lower.</p>
<h2>Remission Day Sample (Modify to Tolerance)</h2>
<ul class="blog-list">
<li><strong>Breakfast:</strong> Greek yogurt, banana, peanut butter oatmeal.</li>
<li><strong>Lunch:</strong> Turkey and avocado wrap, melon, water.</li>
<li><strong>Dinner:</strong> Baked salmon, well-cooked carrots, rice or potatoes.</li>
<li><strong>Snacks:</strong> Cheese, smoothies with whey or lactose-free protein if dairy OK.</li>
</ul>
<h2>During Mild Symptoms</h2>
<p>Shift to softer proteins: eggs, tofu, fish, broth-based soups. Pair with <a href="/blog/low-residue-diet-flare">low-residue flare guidance</a> if your team recommends it.</p>
<h2>Meal Prep on Good Weeks</h2>
<p>Batch cook rice, roast tender vegetables, and portion proteins for school or work lunches. Freezer backups prevent vending-machine defaults on busy days.</p>
<h2>When Meals Feel Impossible</h2>
<p>Oral supplements, liquid nutrition, or appetite workups belong in clinic conversations—not solo restriction. Log intake in IBDPal so visits show trends, not guesses.</p>
""",
    },
]

POST_IMAGE_URLS = {
    "fodmap-ibd": "https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "high-school-ibd": "https://images.unsplash.com/photo-1427504494785-3a9ca7044f45?auto=format&w=1200&q=80",
    "teen-nutrition": "https://images.pexels.com/photos/1095550/pexels-photo-1095550.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "anti-inflammatory-ibd": "https://images.pexels.com/photos/5938/food-salad-healthy-lunch.jpg?auto=compress&cs=tinysrgb&w=1200",
    "exercise-ibd": "https://images.pexels.com/photos/1571019/pexels-photo-1571019.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "vitamins-ibd": "https://images.unsplash.com/photo-1505576399279-565b52d4ac71?auto=format&w=1200&q=80",
    "teen-social-ibd": "https://images.pexels.com/photos/708392/pexels-photo-708392.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "protein-meals-ibd": "https://images.pexels.com/photos/1092730/pexels-photo-1092730.jpeg?auto=compress&cs=tinysrgb&w=1200",
}


def download_image(url: str, dest: Path) -> bool:
    import urllib.request

    try:
        urllib.request.urlretrieve(url, dest)
        data = dest.read_bytes()
        if len(data) > 5000 and data[:2] == b"\xff\xd8":
            return True
    except OSError:
        pass
    return False


def main():
    for p in POSTS:
        asset = BLOGS / "assets" / p["asset_dir"]
        asset.mkdir(parents=True, exist_ok=True)
        url = POST_IMAGE_URLS.get(p["asset_dir"])
        for img in p["images"]:
            dest = asset / img
            if url and (not dest.exists() or dest.stat().st_size < 5000):
                if not download_image(url, dest):
                    print("WARN: download failed for", dest)
        out = BLOGS / f"{p['slug']}.html"
        out.write_text(render_post(p), encoding="utf-8")
        print("wrote", out.name)


if __name__ == "__main__":
    main()
