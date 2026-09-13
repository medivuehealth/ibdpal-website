#!/usr/bin/env python3
# Prose style: do not use em dash.
"""Expand September 2026 gap posts to ~10-minute reads (~2000 words)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sept-2026-gap-posts.json"
BLOGS = ROOT / "blogs"

sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402

EXPANSIONS = {
    "flare-foods-ibd": """
<h2>Building a flare grocery short list</h2>
<p>When energy is low, decision fatigue makes food worse. Keep a short list on your phone with five breakfast options, five lunch or dinner bases, three snacks, and three fluids. Rotate within that list for a week instead of inventing new menus daily. Many people include white rice, eggs, ripe banana, soft bread, tender poultry, broth, oral rehydration, and one familiar comfort starch from their culture that has historically sat well.</p>
<p>Shop once for shelf-stable backups: rice, oats if tolerated, shelf-stable shakes your clinician accepts, electrolyte packets, and applesauce cups. Delivery apps help on high-urgency days, but review ingredients for spice oils and sugar alcohols. Pair shopping habits with <a href="/blog/ibd-flare-go-bag">a flare go-bag</a> so bathroom and hydration supplies travel with you.</p>
<h2>Texture upgrades that still feel gentle</h2>
<p>Gentle does not have to mean flavorless. Moist cooking methods such as steaming, poaching, slow simmering, and blending often work better than grilling hard exteriors or deep frying. Peel skins when insoluble fiber is a problem. Puree soups if chewing or nausea limits intake. Add flavor with mild herbs, a squeeze of tolerated citrus later in recovery, or a small amount of salt rather than heavy chili oils.</p>
<p>If smells trigger nausea, serve cooler foods, open a window, or let someone else cook. Cold smoothies may help some people and worsen urgency for others; test carefully. See practical notes in <a href="/blog/bone-broth-ibd">bone broth</a>, <a href="/blog/oatmeal-ibd">oatmeal timing</a>, and <a href="/blog/protein-shakes-ons-ibd">oral nutrition shakes</a>.</p>
<h2>Flare foods with an ostomy or J-pouch</h2>
<p>Output volume, gas, and odor concerns change the flare-food conversation. Some people thicken output with starches while others need more fluids and electrolytes after high output days. Chew thoroughly, introduce fibrous foods only with clinician guidance, and watch for blockage warning signs such as cramping with reduced output. Your wound ostomy nurse remains the best product and diet coach for pouch-specific issues.</p>
<p>Continue with <a href="/guides/living-with-ostomy-ibd">living with an ostomy</a>, <a href="/blog/ostomy-basics-ibd">ostomy basics</a>, and hydration resources linked earlier.</p>
<h2>Kids, teens, and caregivers: keeping calories up</h2>
<p>Young people in flares may refuse food because pain or embarrassment around urgency takes over. Caregivers can offer preferred safe foods first, then expand. Liquid calories count. Avoid power struggles that turn every meal into conflict. School nurses may need a temporary plan for snacks and bathroom access. Pediatric teams sometimes use exclusive enteral nutrition; adults increasingly discuss similar tools too.</p>
<p>See <a href="/guides/pediatric-crohns-colitis-help">pediatric help</a>, <a href="/blog/teen-nutrition-ibd">teen nutrition</a>, and <a href="/blog/adult-een-crohns-what-to-expect">adult EEN expectations</a>.</p>
<h2>Alcohol, coffee, and social eating during flares</h2>
<p>Social events rarely pause for IBD. A flare week is a reasonable time to choose mocktails, smaller portions, and earlier exits. Coffee and alcohol both can accelerate motility for some people. If you attend a meal, eat a safe snack beforehand so hunger does not push you into a risky large spicy plate. Communicate needs without oversharing if you prefer privacy.</p>
<p>More context: <a href="/blog/coffee-ibd">coffee and IBD</a>, <a href="/blog/alcohol-ibd">alcohol and IBD</a>, <a href="/blog/dining-out-ibd">dining out</a>.</p>
<h2>A seven-day flare food framework</h2>
<p>Days 1-2: prioritize fluids, electrolytes, and the smallest set of proven safe foods. Days 3-4: add a second protein and a soft cooked vegetable if pain and stool frequency stabilize. Days 5-7: if the clinical plan is working, trial one new food and keep the rest constant. If symptoms worsen after a new food, remove it and wait before the next trial. Frameworks prevent both under-eating and chaotic experimentation.</p>
<p>Log results for clinic calls. Escalating blood, fever, obstruction symptoms, or rapid weight loss means food frameworks take a back seat to medical evaluation.</p>
<h2>Common myths about flare foods</h2>
<ul class="blog-list">
<li><strong>Myth:</strong> Starving the flare heals the bowel. <strong>Reality:</strong> Prolonged under-eating worsens healing capacity.</li>
<li><strong>Myth:</strong> Everyone must go grain-free forever. <strong>Reality:</strong> Many people tolerate refined grains during flares and broader grains later.</li>
<li><strong>Myth:</strong> Probiotic foods fix flares overnight. <strong>Reality:</strong> Fermented foods can help or hurt; they are not rescue therapy.</li>
<li><strong>Myth:</strong> If a food once triggered you, it is banned for life. <strong>Reality:</strong> Tolerances often change with disease activity and surgery status.</li>
</ul>
<p>Keep myth-busting aligned with <a href="/blog/probiotics-ibd">probiotics overview</a> and <a href="/blog/autoimmune-diet-myths">autoimmune diet myths</a>.</p>
""",
    "crohns-diet-overview-ibd": """
<h2>Disease location changes the diet conversation</h2>
<p>Ileal Crohn's, colonic Crohn's, perianal disease, and post-resection anatomy each shift priorities. Bile acid diarrhea after terminal ileum surgery can look like a flare but needs a different toolkit. Stricturing disease may limit skins, nuts, and raw fibrous salads even in quieter periods. Always ask your team to translate your last imaging and operative notes into food guidance.</p>
<p> complementary reading includes <a href="/blog/chronic-diarrhea-ibd-causes">chronic diarrhea causes</a> and <a href="/guides/foundation-ibd-surgery-ostomy">surgery and ostomy education themes</a>.</p>
<h2>Steroids, appetite, and the grocery cart</h2>
<p>Prednisone can spike hunger and blood sugar while masking how sick the bowel still is. That combination tempts large high-sugar intakes that later feel destabilizing. Plan protein-forward groceries before a taper starts when possible. As steroids drop, appetite may crash just as you need nutrition for healing. Coordinate with the taper article at <a href="/blog/steroid-taper-what-to-expect-ibd">steroid taper expectations</a> and <a href="/blog/prednisone-diet-ibd">prednisone diet notes</a> if available on your site library.</p>
<h2>Work, school, and meal timing with Crohn's</h2>
<p>A Crohn's diet overview is incomplete without logistics. Pack safe backups in bags and desk drawers. Know bathroom locations. Prefer meals that reheat gently rather than relying on spicy cafeteria unknowns during unstable weeks. Disability accommodations can include snack breaks and flexible timing around infusions or procedures.</p>
<p>See <a href="/blog/workplace-school-ibd-rights">workplace and school rights</a> and <a href="/blog/infusion-day-what-to-expect">infusion day planning</a>.</p>
<h2>Sample remission plate building blocks</h2>
<p>Once inflammation is quieter, build plates with a protein, a carbohydrate you digest well, a colorful plant your gut accepts, and fluid. Examples many dietitians discuss: salmon with rice and cooked carrots; tofu with soft tortillas and avocado if tolerated; eggs with potatoes and spinach cooked tender; yogurt bowls with ripe fruit and smooth nut butter. Variety across the week matters more than perfection at a single meal.</p>
<p>Food deep dives: <a href="/blog/salmon-fish-ibd">salmon</a>, <a href="/blog/tofu-ibd">tofu</a>, <a href="/blog/avocado-ibd">avocado</a>, <a href="/blog/spinach-ibd">spinach</a>.</p>
<h2>How to run a fair food trial</h2>
<p>Change one variable. Keep portion modest. Maintain the rest of the day's pattern. Log symptoms for 48 to 72 hours. Avoid starting three new supplements, a new workout, and a new cuisine in the same weekend. If anxiety about food is extreme, ask for dietitian or mental health support so fear does not become its own disease burden.</p>
<h2>When Crohn's diet content online becomes harmful</h2>
<p>Be cautious with accounts that shame medication, promise cure diets, or encourage dropping below a healthy weight. Credible education cites clinical partnership and acknowledges uncertainty. If reading leaves you terrified to eat, step away and return to your clinic plan plus a short trusted list of pages.</p>
<p>Balanced anchors: <a href="/eating-with-ibd">Eating With IBD</a>, <a href="/blog/eating-with-ibd-book-guide">book guide</a>, <a href="/resources">resource library</a>.</p>
<h2>Checklist before your next nutrition visit</h2>
<ul class="blog-list">
<li>Three-day food and symptom log</li>
<li>Weight trend for the last month</li>
<li>List of eliminated foods and why</li>
<li>Operative history and known strictures</li>
<li>Current medicines and recent labs</li>
<li>Top three quality-of-life food goals</li>
</ul>
<p>Bring that packet to GI and dietitian visits so advice matches your real pattern rather than a generic Crohn's stereotype.</p>
""",
    "ibd-surgery-peer-support": """
<h2>What to expect emotionally in the decision phase</h2>
<p>Choosing surgery after years of medical therapy can feel like failure even when it is a strong disease-control move. Peers who have already had resections often normalize that grief. They can also share how relief sometimes arrives after source inflammation or obstruction risk is addressed. Allow both truths: fear beforehand and possible functional gains afterward.</p>
<p>If hopelessness or panic dominate, ask for mental health support early rather than waiting until discharge. See <a href="/blog/ibd-depression-anxiety">depression and anxiety</a>.</p>
<h2>Practical packing lists peers often share</h2>
<ul class="blog-list">
<li>Loose clothing and high-waist options for tender incisions or pouches</li>
<li>Phone chargers, headphones, and a simple notebook for questions</li>
<li>List of medicines with doses and last biologic date</li>
<li>Electrolyte packets approved by your team</li>
<li>Comfort items for sleep in a noisy hospital</li>
<li>Extra undies and soft washcloths for home discharge days</li>
</ul>
<p>Confirm with your hospital which items are allowed. Ostomy supply starter kits vary; ask what you must obtain from a supplier before day three at home.</p>
<h2>Caregivers need support too</h2>
<p>Partners and parents often manage wound checks, pharmacy calls, and meal prep while hiding their own fear. Point them to caregiver resources and encourage one trusted friend to take a logistics shift. Peer groups for caregivers reduce burnout and prevent all advice from funneling through the patient alone.</p>
<p>Read <a href="/blog/icn-caregiver-coping-resource">caregiver coping</a> and <a href="/blog/caregiver-partner-ibd">partner caregiver themes</a> when available in your library.</p>
<h2>Returning to work, school, and intimacy</h2>
<p>Clearance timelines differ by procedure. Peers can describe pacing, but only your surgeon clears lifting, sports, and sexual activity. Ask specifically about ostomy intimacy products, scar desensitization, and when swimming is safe. Workplace return-to-work notes may need temporary reduced hours or nearby bathroom access.</p>
<p>Use <a href="/blog/workplace-school-ibd-rights">rights and accommodations</a>, <a href="/blog/swimming-pool-beach-ibd-ostomy">swimming guidance</a>, and <a href="/blog/exercise-physical-activity-ibd">exercise after illness</a>.</p>
<h2>Online support safety tips</h2>
<p>Prefer communities with moderation. Protect private health details. Be wary of sellers pushing unregulated supplements as mandatory after surgery. Screenshot helpful tips and verify medication or wound advice with clinicians before changing your plan. If a thread spikes your anxiety, mute it and return to your nurse line.</p>
<h2>Building a personal support map</h2>
<p>Write four contacts: surgical nurse line, GI nurse line, ostomy supplier or WOC nurse, and one peer or group moderator. Add after-hours instructions from discharge paperwork. Keep the map on paper and in your phone. Support fails most often when people cannot remember whom to call at 2 a.m.</p>
<p>Directory starting points remain <a href="/guides/ibd-support-near-me">support near me</a> and <a href="/guides/find-ccf-chapter-support-group">CCF chapter finder</a>.</p>
<h2>After the acute phase: staying connected</h2>
<p>Many people leave groups once wounds heal, then feel isolated at the six-month mark when surveillance scopes or medicine restarts loom. Staying loosely connected helps with long-term adherence and body-image adjustment. Anniversary feelings around surgery dates are common; plan a gentle check-in with a friend or counselor.</p>
""",
    "adalimumab-dose-frequency-ibd": """
<h2>How specialty pharmacies fit into dosing reality</h2>
<p>Adalimumab is often dispensed by a specialty pharmacy that ships on a schedule, offers injection training, and handles refill timing. Delays happen after insurance changes, address updates, or holiday shipping. Track your remaining pens and request refills earlier than you think you need. If a shipment will arrive late, call both pharmacy and clinic the same day rather than waiting until the injection morning.</p>
<p>Access companions: <a href="/blog/prior-authorization-biologics-timeline">prior authorization timeline</a> and manufacturer support listings on the IBDPal news or partners pages when available.</p>
<h2>Injection technique and site rotation basics</h2>
<p>Training videos and nurse visits matter. Rotate sites, avoid bruised or infected skin, and follow device instructions for the exact product you received. Biosimilar devices can differ from the Humira pen you saw on social media. If you fear needles, ask about support programs or supervised first injections. Never heat pens on a stove or microwave to warm them.</p>
<h2>Monitoring while on adalimumab</h2>
<p>Clinics may order blood counts, liver enzymes, inflammatory markers, and sometimes drug levels or antibodies when response is unclear. Tuberculosis screening and hepatitis screening usually occur before start. Keep vaccine records updated with the guidance in <a href="/blog/vaccines-biologics-immunosuppressants-ibd">vaccines with biologics</a>. Report persistent cough, fever, shingles-like rash, or night sweats promptly.</p>
<h2>Combining adalimumab with other IBD therapies</h2>
<p>Some plans include immunomodulators, short steroid bridges, or topical therapies. Combination strategies are individualized because infection and monitoring risks change. Do not add or stop methotrexate, azathioprine, or steroids based on forum anecdotes. Bring a full medication list to every visit, including over-the-counter pain medicines.</p>
<p>See <a href="/guides/ibd-medications-overview">medications overview</a> and <a href="/blog/immunosuppressants-ibd">immunosuppressants overview</a>.</p>
<h2>What partial response can look like</h2>
<p>Stool frequency may improve before energy returns. Joint symptoms may lag gut gains. Conversely, labs may improve while urgency remains from IBS overlap or bile acids. A dosing conversation should include what success means for you: night sleep, work attendance, blood clearance, or scope healing. Clarify the timeline your clinician wants before declaring failure.</p>
<p>Symptom framing help: <a href="/blog/flare-symptoms-ibd">flare symptoms</a>, <a href="/blog/what-remission-means-ibd">remission meanings</a>, <a href="/blog/ibd-fatigue-brain-fog">fatigue</a>.</p>
<h2>Surgery, dental work, and dose holds</h2>
<p>Tell surgeons and dentists you are on a biologic. Timing of perioperative holds varies by procedure infection risk and disease control. Only your IBD clinician should authorize holding doses. After surgery, confirm the restart date in writing so specialty pharmacy shipments match.</p>
<p>Surgery support context: <a href="/blog/ibd-surgery-peer-support">surgery and peer support</a>.</p>
<h2>Cost stress and adherence</h2>
<p>Copay anxiety leads to delayed starts and quiet missed doses. Ask about foundation assistance, manufacturer cards when eligible, and biosimilar options your insurer prefers. A social worker or specialty pharmacist can often navigate paperwork faster than patients alone. Adherence support is medical care, not a personal failing.</p>
""",
    "periods-menstrual-cycle-ibd": """
<h2>Separating menstrual blood from intestinal bleeding</h2>
<p>Clarity matters for triage. Menstrual blood comes from the vagina; intestinal bleeding appears with stool, on toilet paper after a bowel movement, or mixed in stool. During heavy periods, use pads or a menstrual cup carefully and still inspect stool separately when possible. If you cannot tell the difference and feel faint, seek urgent care rather than waiting for perfect certainty.</p>
<p>Use <a href="/blog/blood-in-stool-ibd-when-to-worry">blood in stool guidance</a> and <a href="/blog/black-stool-ibd">black stool education</a>.</p>
<h2>PMS, bloating, and IBD gas overlap</h2>
<p>Cycle-related bloating can stack on IBD gas and temporary lactose sensitivity. A short food simplification around peak PMS days helps some people, provided calories remain adequate. Gentle movement, heat, and hydration are reasonable first steps. Persistent one-sided severe pain still needs clinical review for other pelvic conditions.</p>
<p>See <a href="/blog/gas-bloating-ibd">gas and bloating</a> and <a href="/blog/dairy-lactose-ibd">dairy and lactose</a>.</p>
<h2>Sleep, mood, and steroids around the cycle</h2>
<p>If you are tapering steroids, mood and insomnia may intensify premenstrually. Tell both GI and mental health clinicians about the overlap so nobody assumes the other domain is solely responsible. Safety planning matters if mood crashes include hopelessness.</p>
<p>Companions: <a href="/blog/steroid-taper-what-to-expect-ibd">steroid taper</a>, <a href="/blog/sleep-rest-ibd">sleep and rest</a>, <a href="/blog/ibd-depression-anxiety">depression and anxiety</a>.</p>
<h2>Exercise through period weeks with IBD</h2>
<p>Light walking or stretching can ease cramps for some patients; high-intensity workouts may feel impossible during combined gut and menstrual symptoms. Adjust expectations week by week. Hydrate more if stools are loose. Stop for dizziness, heavy bleeding, or sharp abdominal pain.</p>
<p>Read <a href="/blog/exercise-physical-activity-ibd">exercise with IBD</a>.</p>
<h2>Partner communication and privacy</h2>
<p>You choose how much to disclose. Useful scripts include asking for heating pads, flexible dinner plans, or quiet transportation to clinic. For teens, caregivers should support supply access at school without policing every snack choice.</p>
<p>See <a href="/blog/social-life-dating-teens-ibd">teen social life</a> and <a href="/blog/caregiver-partner-ibd">partner support</a> when present in the library.</p>
<h2>Perimenopause and later hormonal transitions</h2>
<p>People with long-standing IBD may later notice new symptom patterns during perimenopause. Do not assume every change is IBD or every change is hormones. Parallel evaluation beats years of guesswork. Bring a three-month symptom and cycle calendar to visits.</p>
<h2>A one-page clinic summary template</h2>
<ul class="blog-list">
<li>Average cycle length and period duration</li>
<li>Days when gut symptoms reliably worsen</li>
<li>Pain medicines used and doses</li>
<li>Iron labs and last hemoglobin</li>
<li>Contraception method and fertility plans</li>
<li>Questions about endometriosis or gynecology referral</li>
</ul>
<p>Handing over a one-page summary saves visit time and reduces the chance that period overlap is dismissed.</p>
""",
    "eating-with-ibd-book-guide": """
<h2>Why a book still helps in a search-first world</h2>
<p>Short articles answer one question. A book gives sequence: mindset, flare tactics, remission rebuilding, micronutrients, and clinic communication in one arc. Readers who bounce between conflicting blogs often calm down when they follow a single coherent path, then use the website for updates and specific foods.</p>
<h2>How to read if concentration is limited</h2>
<p>During flares, cognition and sleep suffer. Use a twenty-minute timer. Read one subsection. Write one action. Stop. Audio-friendly reading with a partner also works. Highlight clinic questions in a different color so they are easy to find before appointments.</p>
<p>Energy support: <a href="/blog/ibd-fatigue-brain-fog">fatigue and brain fog</a> and <a href="/blog/sleep-rest-ibd">sleep and rest</a>.</p>
<h2>Pairing chapters with IBDPal tools</h2>
<ul class="blog-list">
<li>After flare chapters, open <a href="/flare-help">flare help</a> and <a href="/blog/flare-foods-ibd">flare foods</a></li>
<li>After tracking chapters, set up <a href="/tools/food-pain-tracker">food pain tracker</a></li>
<li>After micronutrient chapters, review <a href="/blog/micronutrients-ibd-deficiencies">deficiencies</a> and lab articles</li>
<li>After support chapters, search <a href="/guides/ibd-support-near-me">support near me</a></li>
</ul>
<h2>Using the book in family kitchens</h2>
<p>Share one chapter with the person who shops or cooks. Agree on three always-safe meals and two experimental meals for quieter weeks. Cultural recipes can be adapted rather than replaced. The goal is shared language, not culinary perfection.</p>
<p>Cultural food examples on the site include <a href="/blog/dal-lentils-ibd">dal</a>, <a href="/blog/chapati-roti-ibd">chapati</a>, <a href="/blog/congee-rice-porridge-ibd">congee</a>, and <a href="/blog/tortillas-ibd">tortillas</a>.</p>
<h2>Classroom, campus, and workplace use</h2>
<p>Students and employees can keep the book digital or physical copy with a bookmark on visit-prep questions. Combine with accommodation letters and a short flare plan. Nutrition knowledge helps, but bathroom access and infusion scheduling still need institutional support.</p>
<p>See <a href="/blog/workplace-school-ibd-rights">rights</a> and <a href="/guides/youth-school-foundation-resources">youth and school resources</a>.</p>
<h2>How clinicians may respond to book-based questions</h2>
<p>Good clinicians welcome organized questions. Bring the page or chapter title and your personal constraints. Expect individualized edits: strictures, ostomy, diabetes, kidney disease, or food insecurity change recommendations. If a clinician dismisses all nutrition talk, ask for a dietitian referral rather than arguing ideology.</p>
<h2>Gift giving and newly diagnosed friends</h2>
<p>The book can be a supportive gift when paired with permission: the recipient chooses when to read. Include a note that medicine remains central and that you can help with errands or meals. Avoid gifting extreme diet manifestos that conflict with IBD care.</p>
<p>Newly diagnosed path: <a href="/newly-diagnosed">hub</a>, <a href="/blog/newly-diagnosed-first-30-days">first 30 days</a>, and this guide.</p>
<h2>Keeping free and paid resources in balance</h2>
<p>IBDPal intends free education to stay robust. The book is an optional deeper companion. You should still be able to navigate flares, foods, and support directories without purchase. If search on the site fails for \"Eating With IBD book,\" use the direct link <a href="/eating-with-ibd">/eating-with-ibd</a> and this article at <a href="/blog/eating-with-ibd-book-guide">/blog/eating-with-ibd-book-guide</a>.</p>
""",
}


def word_count(html_body: str) -> int:
    text = re.sub(r"<[^>]+>", " ", html_body)
    return len(text.split())


def merge(body: str, extra: str) -> str:
    marker = "<p>Related:"
    idx = body.rfind(marker)
    if idx == -1:
        return body + "\n" + extra.strip() + "\n"
    return body[:idx] + extra.strip() + "\n" + body[idx:]


def main() -> None:
    posts = json.loads(DATA.read_text(encoding="utf-8"))
    for post in posts:
        extra = EXPANSIONS.get(post["slug"])
        if not extra:
            continue
        if "Building a flare grocery" in post["body"] or "Disease location changes" in post["body"] or "decision phase" in post["body"] and post["slug"] == "ibd-surgery-peer-support":
            # idempotent-ish: skip if already expanded
            if "seven-day flare food framework" in post["body"] or "Disease location changes the diet" in post["body"] or "specialty pharmacies fit" in post["body"] or "Separating menstrual blood" in post["body"] or "search-first world" in post["body"] or "packing lists peers" in post["body"]:
                print("skip already expanded", post["slug"])
                continue
        post["body"] = merge(post["body"], extra)
        wc = word_count(post["body"])
        print(f"{post['slug']}: ~{wc} words (~{max(1, round(wc/200))} min)")
        (BLOGS / f"{post['slug']}.html").write_text(render_post(post), encoding="utf-8")
    DATA.write_text(json.dumps(posts, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("updated", DATA.name)


if __name__ == "__main__":
    main()
