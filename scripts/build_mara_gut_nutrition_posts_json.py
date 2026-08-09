#!/usr/bin/env python3
# Prose style: do not use em dash.
"""Build expanded enteral + Mara-lab-informed gut/nutrition blog JSON (~10 min each)."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "mara-gut-nutrition-posts.json"

# Public references (cite; do not overclaim ICU findings as IBD therapy).
PUBMED_FIBER = "https://pubmed.ncbi.nlm.nih.gov/41462238/"
LAB = "https://anesthesiology.duke.edu/research/serbanescu-lab"
PROFILE = "https://medschool.duke.edu/profile/mara-serbanescu"
AGA = "https://gastro.org/clinical-guidance/diet-and-nutritional-therapies-in-patients-with-ibd/"
CCF = "https://www.crohnscolitisfoundation.org/patientsandcaregivers"


def p(*parts: str) -> str:
    return "".join(f"<p>{x}</p>\n" for x in parts)


def h2(title: str) -> str:
    return f"<h2>{title}</h2>\n"


def ul(items: list[str]) -> str:
    return '<ul class="blog-list">\n' + "".join(f"<li>{i}</li>\n" for i in items) + "</ul>\n"


def long_faq(topic_lines: list[str]) -> str:
    """Append reusable depth so posts reach ~10 min without fluff-only filler."""
    chunks = [h2("Extended FAQ patients ask after reading research headlines")]
    for line in topic_lines:
        if line.startswith("Q:"):
            chunks.append(f"<h3>{line[2:].strip()}</h3>\n")
        else:
            chunks.append(p(line))
    return "".join(chunks)


def posts() -> list[dict]:
    date_iso = "2026-08-09T18:00:00Z"
    date_display = "August 9, 2026"
    cat = "Nutrition · August 2026"

    fiber_faq = long_faq(
        [
            "Q: Does the ICU trial mean prebiotic fiber is bad?",
            "No. It means that in a small group of critically ill trauma patients with heavy antibiotic "
            "exposure and baseline dysbiosis, scFOS-containing formula did not behave like a universal "
            "good. Healthy-volunteer or other clinical contexts can differ. Your IBD formula decision "
            "still belongs with your dietitian.",
            "Q: Should I request a fiber-free formula after every antibiotic course?",
            "Not automatically. Some people need fiber-free textures for strictures or high output; "
            "others tolerate soluble fiber in liquids. Ask for a time-limited plan tied to your antibiotic "
            "stop date rather than a forever rule based on one paper.",
            "Q: Can I take a prebiotic powder with EEN to \"fix\" dysbiosis?",
            "Do not stack products onto prescribed exclusive formula unless your team approves. Extra "
            "fermentable load can worsen symptoms and muddies whether EEN itself is working.",
            "Q: How is this different from food fiber advice in remission?",
            "Remission diet diversity is about whole dietary patterns over months. Formula fiber is a "
            "controlled ingredient inside medical nutrition. They interact with your care but are not "
            "interchangeable advice tracks.",
            "Q: What should caregivers watch in the first 72 hours after a formula fiber change?",
            "Track stool frequency and consistency, gas pain, nausea, urine color, and completed volume. "
            "Call for dizziness, inability to keep fluids, or obstruction-like pain. Keep a simple table "
            "on the fridge so night and day caregivers log the same way.",
            "Q: Where can I read more without getting lost?",
            f'Start with the <a href="{PUBMED_FIBER}" rel="noopener noreferrer">PubMed abstract</a>, '
            f'the <a href="{LAB}" rel="noopener noreferrer">AMP Lab page</a>, and IBDPal\'s '
            '<a href="/blog/enteral-nutrition-ibd">enteral overview</a>. Then write three questions '
            "for clinic instead of ten new Amazon supplements.",
        ]
    )
    een_faq = long_faq(
        [
            "Q: How exclusive is exclusive?",
            "Ask your center for a written list: water, clear fluids, gum, mints, medications with "
            "tiny food carriers, and toothbrushing rules. Ambiguity creates guilt and inconsistent results.",
            "Q: What if I break the plan once?",
            "Tell the team promptly. One unplanned meal is data, not moral failure. Hiding it helps no one "
            "interpret labs and symptoms.",
            "Q: Can PEN be long term?",
            "Some patients use nocturnal feeds for months while medicines stabilize disease and growth. "
            "Long-term PEN still needs monitoring for micronutrients, bone health, and social impact.",
            "Q: Does EEN replace biologics?",
            "Usually no. EEN may be induction, bridge, or adjunct. Clarify whether medicines pause, "
            "continue, or start at a defined week.",
            "Q: How do we handle holidays and birthdays?",
            "Plan them into the calendar at the start. Some protocols allow rare exceptions; others "
            "reschedule celebrations. Surprises are harder than planned flexibility.",
            "Q: What about exclusive formula in ulcerative colitis?",
            "EEN evidence and practice patterns are stronger historically in Crohn's disease. UC patients "
            "may still use formula for nutrition support. Ask what goal is realistic for your diagnosis.",
        ]
    )
    barrier_faq = long_faq(
        [
            "Q: Is leaky gut a recognized IBD diagnosis?",
            "IBD is diagnosed with clinical, endoscopic, histologic, and imaging criteria. Barrier "
            "dysfunction is a research and mechanistic concept, not a substitute diagnosis sold online.",
            "Q: Do stool microbiome kits guide IBD therapy?",
            "Most commercial kits do not change evidence-based IBD medication algorithms. Ask how a "
            "result would alter your plan before paying.",
            "Q: Can diet alone heal my barrier?",
            "Diet can support symptoms, nutrition status, and sometimes inflammation pathways under "
            "supervision. It does not reliably replace medicines that target immune pathways when those "
            "are indicated.",
            "Q: Why do ICU microbiome studies show up in IBD reading lists?",
            "Because barrier stress, dysbiosis, nutrition, and inflammation are shared scientific "
            "themes. Shared themes are not shared treatment protocols. Read with that filter.",
            "Q: What is a healthy curiosity habit?",
            "One primary source, one reputable foundation page, and one clinic question per month beats "
            "daily doomscrolling through microbiome Twitter.",
            "Q: How do I talk to relatives who send detox links?",
            "Thank them for caring, share one sentence from your GI about your actual plan, and ask them "
            "to stop forwarding cure claims. Boundaries protect adherence.",
        ]
    )
    hospital_faq = long_faq(
        [
            "Q: Why am I still NPO if I feel hungry?",
            "Hunger is real and valid. NPO may continue for imaging, theater slots, obstruction concerns, "
            "or pending surgical decisions. Ask for the specific reason and the next reassessment time.",
            "Q: Can I refuse a nasogastric tube?",
            "You can discuss risks and alternatives. Refusal may change nutrition options, including "
            "longer PN exposure. Ask for a goals-of-care style conversation if you feel pressured.",
            "Q: Who adjusts my home biologic during admission?",
            "Clarify whether GI, surgery, or the hospitalist owns holds and restarts. Get the plan in "
            "writing before discharge.",
            "Q: What if hospital formula causes diarrhea?",
            "Report timing, rate, and formula name. Teams may slow rates, change formula, evaluate "
            "infection, or adjust other medicines. Do not silently stop feeds without telling nursing.",
            "Q: How soon after surgery will I eat normal food?",
            "It depends on the operation, complications, and nausea. \"Normal\" may mean weeks of texture "
            "modification. Ask for a written advance ladder.",
            "Q: Should caregivers sleep in the room for overnight feeds?",
            "If learning pumps before discharge, yes for at least one night of supervised practice. After "
            "competence, rest when safe so nobody drives home exhausted.",
        ]
    )

    enteral_body = (
        p(
            "People searching <strong>Enteral</strong>, <strong>Entereal</strong> (a common misspelling), "
            "or <strong>EEN</strong> on IBDPal usually want a clear map of formula-based nutrition for "
            "Crohn's disease or ulcerative colitis. This longer guide explains what those terms mean, "
            "how exclusive and partial plans differ, what life with formula can feel like, and which "
            "questions help a gastroenterologist or dietitian personalize next steps. It is educational "
            "only and is not a treatment plan, dosing guide, or substitute for your IBD team."
        )
        + h2("What \"enteral\" means in plain language")
        + p(
            "<strong>Enteral nutrition</strong> means delivering nutrients through the gastrointestinal (GI) "
            "tract. That can be drinking specialized liquid formulas, or using a feeding tube when oral "
            "intake is not enough or not safe. \"Enteral\" refers to using the gut (enteric), not the bloodstream.",
            "If you typed <strong>entereal</strong>, you almost always mean <strong>enteral</strong>. "
            "Clinic notes, insurance codes, and research papers use the spelling <em>enteral</em>.",
            "Enteral nutrition is a medical nutrition therapy tool. It is not the same as casually replacing "
            "meals with store protein shakes, even when those shakes help some people meet calories."
        )
        + h2("Enteral versus parenteral nutrition")
        + ul(
            [
                "<strong>Enteral:</strong> Nutrition into the gut (oral formula or tube). Preferred when the "
                "gut can be used safely, because it supports gut lining and reduces some intravenous risks.",
                "<strong>Parenteral (TPN/PN):</strong> Nutrition into a vein. Reserved for situations where "
                "the bowel cannot be used adequately, decided by your hospital or IBD team.",
            ]
        )
        + p(
            "Patients sometimes hear both terms in the same admission. Ask which route is planned, why, "
            "and what would trigger a switch. Early use of the gut, when safe, is a theme across critical "
            "care and surgical nutrition research, including work discussed by groups studying microbiome "
            "and feeding in stressed patients. Those hospital contexts are not identical to outpatient "
            "Crohn's EEN, but they share a practical idea: if the gut can work, teams often try to use it."
        )
        + h2("Exclusive enteral nutrition (EEN)")
        + p(
            "<strong>EEN</strong> means using formula as the primary (often sole) source of nutrition for a "
            "defined period, instead of a normal mixed diet. In pediatric Crohn's disease, EEN is a "
            "well-known induction option in many centers because it can help calm inflammation and support "
            "growth while medicines are planned. Adults may also use exclusive or near-exclusive formula "
            "plans in selected cases, though medication strategies are more common in adult practice.",
            "EEN is not \"just a smoothie diet.\" Formulas are designed for complete nutrition under "
            "clinician and dietitian guidance. Duration, which formula, and how food is reintroduced are "
            "individualized. Stopping EEN early or adding random foods without a plan can undo progress "
            "or make symptoms harder to interpret.",
            "Ask whether your center treats EEN as induction alone, as a bridge to another therapy, or as "
            "support alongside steroids or biologics. Goals should be written: inflammation markers, "
            "weight, stool frequency, school or work function, and a food reintroduction date range."
        )
        + h2("Partial enteral nutrition and everyday formula use")
        + p(
            "Not every plan is exclusive. Many people use <strong>partial enteral nutrition (PEN)</strong>: "
            "formula plus some food, overnight tube feeds, or sip feeds between meals to protect weight, "
            "growth, or healing after surgery. Teens and caregivers often see this during growth concerns. "
            "See also <a href=\"/blog/teen-nutrition-ibd-growth\">teen nutrition and growth with IBD</a> "
            "and our deeper companion piece on "
            "<a href=\"/blog/exclusive-vs-partial-enteral-nutrition-crohns\">EEN versus PEN in Crohn's</a>."
        )
        + ul(
            [
                "Boosting calories when appetite is low",
                "Supporting remission while medicines work",
                "Bridging after flares when solid food feels hard",
                "Meeting protein and micronutrient goals with less meal stress",
                "Overnight nasogastric feeds when daytime volume is impossible",
            ]
        )
        + h2("Formula types patients hear about")
        + p(
            "Clinic conversations may mention <strong>polymeric</strong> formulas (more intact proteins), "
            "<strong>semi-elemental</strong> or <strong>elemental</strong> formulas (more broken-down "
            "proteins), overnight <strong>nasogastric (NG) tube</strong> feeds, or brand names such as "
            "Modulen or Peptamen. Brand availability and insurance coverage vary. Your dietitian chooses "
            "based on tolerance, calories, protein density, and clinical goals, not search popularity.",
            "Some formulas include fiber or prebiotic fibers such as fructooligosaccharides. Fiber "
            "composition is not a trivia detail. Microbiome and ICU nutrition studies show that fiber "
            "and antibiotic context can change how gut microbes respond to formula. That research does "
            "not automatically dictate which Crohn's formula you should drink, but it is a reason to ask "
            "your team why a fiber-containing or fiber-free product was chosen. See "
            "<a href=\"/blog/fiber-prebiotics-enteral-feeds-microbiome\">fiber, prebiotics, and formula feeds</a>."
        )
        + h2("How EEN and PEN fit beside diet therapies")
        + p(
            "Enteral nutrition sits inside a larger nutrition conversation that can also include "
            "low-residue patterns during flares, supervised exclusion diets, Mediterranean-style patterns "
            "in remission, and dietitian-led micronutrient repair. AGA clinical guidance discusses diet "
            "and nutritional therapies as support for medical care, not a standalone cure. Browse the "
            f'<a href="/ibd-nutrition">IBD nutrition hub</a>, <a href="{AGA}" rel="noopener noreferrer">'
            "AGA diet and nutrition update</a>, and "
            '<a href="/research#aga-diet-2024">our research summary</a>.',
            "Crohn's &amp; Colitis Foundation caregiver and patient hubs also cover nutrition themes in "
            f'accessible language: <a href="{CCF}" rel="noopener noreferrer">Foundation patients and caregivers</a>.'
        )
        + h2("What life with formula feeds can feel like")
        + p(
            "Taste fatigue, social meals, school or work schedules, and formula cost or insurance coverage "
            "are common real-world issues. Practical tips patients discuss with teams include rotating "
            "flavors (if allowed), chilling formula, using a straw, pacing sips, and planning bathroom "
            "access. None of these replace the plan your clinician wrote.",
            "If solid food is limited, ask about bone health, vitamin D, iron, B12, and other labs. Related "
            "reading: <a href=\"/blog/micronutrients-ibd-deficiencies\">micronutrient deficiencies in IBD</a> "
            "and <a href=\"/blog/how-ibdpal-nutrition-targets-work\">how IBDPal nutrition targets work</a>.",
            "Caregivers often need a second plan for travel, sports, and sleepovers. Write down calories "
            "per carton, fridge rules, and who to call if a shipment is late. Formula interruptions during "
            "EEN can feel like treatment interruptions. Plan buffers with the dietitian before the first week."
        )
        + h2("Tubes, pumps, and overnight feeds")
        + p(
            "When drinking enough volume is impossible, teams may discuss nasogastric tubes for overnight "
            "feeds. That can feel intimidating the first time. Ask who places the tube, how placement is "
            "confirmed, how to flush, what to do if the pump alarms, and how school nurses or campus health "
            "are looped in. Skin care at the nose and sleep positioning matter for comfort.",
            "Never increase pump rates or add foods into a tube without instructions. Aspiration risk and "
            "tolerance windows are clinical decisions. If vomiting, severe bloating, or breathing trouble "
            "appear during a feed, stop and follow the emergency instructions your team gave you."
        )
        + h2("Questions to bring to your GI or dietitian")
        + ul(
            [
                "Is the goal exclusive EEN, partial formula, or short-term sip feeds?",
                "Which formula and how many calories or cartons per day?",
                "Does this formula contain fiber or prebiotic fibers, and why?",
                "How long before we reintroduce food, and in what order?",
                "What side effects should I report (nausea, diarrhea, constipation, reflux)?",
                "Is a nasogastric tube optional if I cannot drink enough volume?",
                "How does this fit with steroids, biologics, or other medicines?",
                "What labs and weight checks mark success at week two and week six?",
            ]
        )
        + h2("Research context: why formula composition is studied carefully")
        + p(
            "Beyond IBD clinics, nutrition science teams study how enteral formulas interact with the gut "
            "microbiome during severe stress, antibiotics, and critical illness. The "
            f'<a href="{LAB}" rel="noopener noreferrer">Duke Anesthesiology Microbiome Profiling (AMP) Laboratory</a> '
            "led by Dr. Mara Serbanescu investigates how microbes and nutrition relate to immune responses "
            "and outcomes in perioperative and critically ill patients. Public lab pages and "
            f'<a href="{PROFILE}" rel="noopener noreferrer">Dr. Serbanescu\'s Duke profile</a> summarize that focus.',
            "A 2025 pilot randomized trial in critically ill trauma patients compared fiber-containing "
            "enteral nutrition with a fiber-free formula and tracked stool microbial communities over time "
            f'(<a href="{PUBMED_FIBER}" rel="noopener noreferrer">PubMed 41462238</a>). In that ICU setting, '
            "responses to prebiotic fiber were context-dependent and appeared influenced by antibiotic "
            "exposure. Those findings challenge one-size-fits-all prebiotic assumptions in the ICU. They "
            "are not a prescription for Crohn's formula choice, but they reinforce a patient-facing lesson: "
            "ask why your formula has the fiber profile it has, especially if antibiotics are also in play."
        )
        + h2("Insurance, school forms, and supply logistics")
        + p(
            "Formula coverage varies by plan, age, diagnosis codes, and whether a tube is documented. Ask "
            "your dietitian which letter of medical necessity language has worked for other patients at "
            "your center. Keep copies of prior authorizations. If a shipment slips, call the specialty "
            "pharmacy and the clinic the same day rather than waiting until the last carton.",
            "School 504 plans and college disability services can list private feeding time, nurse storage "
            "for cartons, and bathroom access during larger daytime volumes. Bring the written calorie "
            "target so staff are not guessing. Workplace conversations are similar: a quiet room and a "
            "refrigerator beat improvising in a bathroom stall.",
            "Travel with formula means knowing airline liquid rules for medically necessary nutrition, "
            "packing extras in case of delays, and confirming hotel fridge access. International trips "
            "need even more buffer because brand substitutions abroad may not match your tolerance."
        )
        + h2("EEN myths that create avoidable stress")
        + ul(
            [
                "<strong>Myth:</strong> Any meal replacement shake is EEN. "
                "<strong>Reality:</strong> Therapeutic formulas and durations are prescribed.",
                "<strong>Myth:</strong> Adults never use EEN. "
                "<strong>Reality:</strong> Less common than in pediatrics, but selected adults still do.",
                "<strong>Myth:</strong> One bad taste day means failure. "
                "<strong>Reality:</strong> Flavor fatigue is expected; teams have workarounds.",
                "<strong>Myth:</strong> Food reintroduction can be improvised from social media. "
                "<strong>Reality:</strong> Unplanned foods can confuse whether EEN helped.",
            ]
        )
        + p(
            "Social media before-and-after stories rarely show insurance denials, tube learning curves, or "
            "the week someone caught a virus mid-EEN. Compare notes with your clinical team, not with "
            "strangers' highlight reels."
        )
        + h2("How IBDPal can support the non-formula parts of care")
        + p(
            "Even on exclusive formula, symptom and energy logs help nurse lines understand whether night "
            "pain, stool blood, or fever are new. After reintroduction, meal and symptom pairing becomes "
            "more useful. Visit prep checklists keep calorie targets, formula brand, and questions in one "
            "place before clinic. Explore <a href=\"/blog/tracking-food-symptoms-ibdpal\">tracking food "
            "and symptoms</a> and <a href=\"/visit-prep\">visit prep</a>.",
            "Nutrition targets inside the app are educational companions, not a replacement for dietitian "
            "math. If your prescribed carton count and the app's general targets disagree, follow the "
            "prescription and ask the clinic to reconcile."
        )
        + h2("Sample week-one conversation agenda")
        + p(
            "Bring a one-page agenda to the first EEN or PEN visit so stress does not erase questions:"
        )
        + ul(
            [
                "Confirm exclusive versus partial definition in writing",
                "Review formula brand, fiber content, and daily volume",
                "Set weight and symptom checkpoints for days 7 and 14",
                "Name the after-hours contact for vomiting or tube problems",
                "Schedule the reintroduction planning visit before week four ends",
                "Ask how medicines change if formula induction succeeds or stalls",
            ]
        )
        + p(
            "Photograph the whiteboard plan if your center uses one. Memory during illness is unreliable, "
            "and caregivers in different households need the same numbers."
        )
        + h2("When to contact the care team promptly")
        + p(
            "Call your IBD team or seek urgent care for inability to keep fluids down, signs of dehydration, "
            "rapid weight loss, high fever, severe abdominal pain, or tube-site problems if you use a feeding "
            "tube. Formula plans should not delay evaluation of a dangerous flare. Related: "
            "<a href=\"/blog/dehydration-ibd-warning-signs\">dehydration warning signs</a>, "
            "<a href=\"/blog/when-to-go-er-ibd\">when to go to the ER</a>, and "
            "<a href=\"/flare-help\">flare help</a>."
        )
        + h2("Putting the Mara lab references in context for readers")
        + p(
            "If you follow academic nutrition and microbiome work, you may already know Dr. Mara "
            f'Serbanescu\'s <a href="{PROFILE}" rel="noopener noreferrer">Duke profile</a> and the '
            f'<a href="{LAB}" rel="noopener noreferrer">Anesthesiology Microbiome Profiling Laboratory</a>. '
            "Those pages describe translational research on microbes, immune responses, and outcomes in "
            "perioperative and critically ill patients, including nutrition-related projects. They are "
            "valuable public windows into why formula composition, fiber, and antibiotics are studied so "
            "carefully.",
            "IBDPal cites them so curious patients can read primary sources and lab overviews without "
            "pretending ICU protocols are home Crohn's protocols. Your actionable path remains: ask your "
            "IBD dietitian how formula type, fiber content, and duration serve your goals this month."
        )
        + h2("Related IBDPal reading")
        + p(
            "<a href=\"/blog/complete-ibd-nutrition-guide\">Complete IBD nutrition guide</a>, "
            "<a href=\"/blog/exclusive-vs-partial-enteral-nutrition-crohns\">EEN vs PEN</a>, "
            "<a href=\"/blog/fiber-prebiotics-enteral-feeds-microbiome\">Fiber and prebiotic formulas</a>, "
            "<a href=\"/blog/gut-barrier-dysbiosis-inflammation-ibd\">Gut barrier and dysbiosis</a>, "
            "<a href=\"/blog/hospital-feeding-ibd-enteral-parenteral\">Hospital feeding with IBD</a>, "
            "<a href=\"/guides/what-should-i-eat-crohns-colitis\">What should I eat</a>, "
            "<a href=\"/newly-diagnosed\">Newly diagnosed hub</a>, "
            "<a href=\"/visit-prep\">Visit prep checklist</a>."
        )
    )

    fiber_body = (
        p(
            "Formula cans list fiber grams as if more is always better. In real guts, especially after "
            "antibiotics or during severe illness, fiber and prebiotic additives can behave differently "
            "than they do in healthy volunteers. This article explains what prebiotic fibers in enteral "
            "formulas are meant to do, what a recent ICU pilot trial found, and which practical questions "
            "IBD patients can bring to a dietitian. Educational only. It does not recommend starting, "
            "stopping, or switching formulas on your own."
        )
        + h2("Fiber, prebiotics, and formula feeds: the basic vocabulary")
        + p(
            "<strong>Dietary fiber</strong> is plant carbohydrate that resists full digestion in the small "
            "intestine. Some fibers are fermented by gut microbes into short-chain fatty acids and other "
            "metabolites. <strong>Prebiotics</strong> are substrates selectively used by host microbes to "
            "confer a health benefit when evidence supports that claim. Short-chain "
            "fructooligosaccharides (scFOS) are one prebiotic fiber type used in some enteral formulas.",
            "Enteral formulas may be fiber-free, fiber-containing, or blended. In IBD care, fiber decisions "
            "also collide with stricture risk, flare urgency, and personal tolerance. A low-residue flare "
            "plan and a prebiotic ICU formula are not the same clinical problem. Keep those contexts "
            "separate when you read headlines."
        )
        + h2("Why researchers study formula fiber in dysbiotic guts")
        + p(
            "Critical illness, broad-spectrum antibiotics, and delayed feeding can flatten microbial "
            "diversity and allow expansion of potential pathogens sometimes called pathobionts. Nutrition "
            "researchers ask whether adding prebiotic fiber to tube feeds can steer communities toward "
            "more helpful patterns, or whether a dysbiotic, antibiotic-exposed gut responds unpredictably.",
            "The "
            f'<a href="{LAB}" rel="noopener noreferrer">Duke AMP Laboratory</a> studies how the microbiome '
            "influences immune responses and clinical outcomes in perioperative and critically ill patients, "
            "including nutrition-related projects. That public lab description is a good orientation to the "
            "science questions behind formula design, even when your personal care is outpatient IBD."
        )
        + h2("What the 2025 trauma ICU pilot trial reported")
        + p(
            "A pilot randomized trial led by Mara A. Serbanescu and colleagues compared enteral nutrition "
            "supplemented with short-chain fructooligosaccharides (scFOS-EN) versus a similar fiber-free "
            "formula (NF-EN) in mechanically ventilated trauma ICU patients. Stool communities were "
            "profiled with 16S rRNA sequencing across a 10-day window after formula initiation. The "
            f'PubMed record is <a href="{PUBMED_FIBER}" rel="noopener noreferrer">PMID 41462238</a> '
            "(BMC Medicine, 2025).",
            "Participants had profound baseline dysbiosis and received broad-spectrum antibiotics. Compared "
            "with fiber-free formula, scFOS-EN was associated with faster declines in Bifidobacterium and "
            "Firmicutes signals and with expansion patterns that included Enterobacteriaceae in that study "
            "cohort. The authors concluded that effects were context-dependent: prior and ongoing antibiotic "
            "exposure appeared to modify whether prebiotic fiber looked helpful or harmful for the microbial "
            "community. They cautioned against a universal prebiotic approach in the ICU and called for "
            "more personalized nutrition strategies."
        )
        + h2("What this does and does not mean for Crohn's or colitis")
        + ul(
            [
                "<strong>Does mean:</strong> Formula fiber is biologically active, not inert filler.",
                "<strong>Does mean:</strong> Antibiotics and baseline dysbiosis can change how fiber is "
                "fermented and which microbes expand.",
                "<strong>Does not mean:</strong> People with IBD should avoid all fiber formulas.",
                "<strong>Does not mean:</strong> ICU trauma results transfer one-to-one onto pediatric EEN "
                "or adult Crohn's sip feeds.",
                "<strong>Does not mean:</strong> You should add OTC prebiotic powders to prescribed formula "
                "without clinician guidance.",
            ]
        )
        + p(
            "IBD teams already individualize fiber for strictures, pouchitis, ostomies, and flares. The "
            "research literacy point is to ask better questions, not to self-experiment with hospital "
            "prebiotic strategies at home."
        )
        + h2("Questions worth asking your IBD dietitian")
        + ul(
            [
                "Is my current formula fiber-free, low fiber, or prebiotic-enriched, and why?",
                "If I am on antibiotics now, should formula fiber change temporarily?",
                "How should formula fiber interact with my flare low-residue plan?",
                "If I have a known stricture, which fibers are off limits in food and in formula?",
                "What symptoms should trigger a call: gas, osmotic diarrhea, constipation, reflux?",
                "Are we tracking weight, calprotectin, or stool frequency to judge the formula trial?",
            ]
        )
        + h2("Fiber in food versus fiber in formula")
        + p(
            "Food fiber arrives with texture, skins, and chewing demands that matter for stricturing "
            "Crohn's. Formula fiber is dissolved or suspended for tubes and sip feeds. Tolerance can "
            "differ even when the gram count looks similar on a label. During active narrowing, teams "
            "may prefer smooth textures while still debating soluble fiber in liquids. See "
            "<a href=\"/blog/fiber-and-ibd-diet\">fiber and IBD diet</a> and "
            "<a href=\"/blog/low-residue-diet-flare\">low-residue during a flare</a>.",
            "In remission, many people gradually rebuild diverse plant foods under guidance because "
            "microbiome diversity often tracks dietary variety. That is a different project than choosing "
            "scFOS grams inside a trauma ICU carton."
        )
        + h2("Antibiotics, dysbiosis, and \"helpful\" microbes")
        + p(
            "Antibiotics save lives in abscesses, pouchitis regimens, and perioperative care. They also "
            "reshape the microbiome. The ICU pilot's caution that anaerobic antibiotic exposure may alter "
            "responses to scFOS is a reminder that stacking interventions changes biology. If your IBD "
            "course includes frequent antibiotics, ask how nutrition support is adjusted rather than "
            "assuming a probiotic or prebiotic product will automatically restore balance.",
            "Over-the-counter probiotics are a separate topic with mixed evidence and safety nuances for "
            "immunosuppressed patients. Start with "
            "<a href=\"/research#nccih-probiotics\">NCCIH probiotic basics</a> and your clinician, not "
            "social media strain lists."
        )
        + h2("Connecting the dots to everyday IBD nutrition")
        + p(
            "Use formula conversations as part of a whole plan: calories, protein, hydration, micronutrients, "
            "and medicines. Related: <a href=\"/blog/enteral-nutrition-ibd\">enteral nutrition overview</a>, "
            "<a href=\"/blog/protein-meal-plan-ibd-remission\">protein meals in remission</a>, "
            "<a href=\"/blog/electrolytes-flare-ibd\">electrolytes during flares</a>, and "
            "<a href=\"/blog/how-nutrition-impacts-gut-health-ibd\">nutrition and gut health</a>.",
            "If you like research rabbit holes, read the PubMed abstract first, then ask your dietitian "
            "which sentences apply to your situation. Skipping that translation step is how ICU headlines "
            "become unsafe home experiments."
        )
        + h2("A patient-friendly reading path for the trial")
        + p(
            "If you want to engage the primary source without drowning in methods:"
        )
        + ul(
            [
                "Read the abstract conclusion first: context-dependent effects, antibiotic modifiers, "
                "caution against universal prebiotic assumptions in the ICU.",
                "Note the population: mechanically ventilated trauma patients, not ambulatory Crohn's.",
                "Note the intervention: scFOS-containing enteral formula versus fiber-free formula.",
                "Note the outcome type: stool microbial community dynamics, not IBD remission rates.",
                "Bring one sentence to clinic: \"Does my antibiotic history change which formula fiber "
                "profile you prefer for me?\"",
            ]
        )
        + p(
            "Full-text open access via the journal link on PubMed can help curious readers, but your "
            "dietitian still owns the translation to your stricture map, pouch, or pediatric growth plan."
        )
        + h2("Prebiotics, probiotics, and synbiotics: keep the labels straight")
        + p(
            "People mix these terms constantly. Prebiotics feed microbes. Probiotics are live microbes "
            "in a product. Synbiotics combine both. Hospital scFOS in a tube feed is a prebiotic fiber "
            "strategy inside complete nutrition, not the same as a capsule from a vitamin aisle. Safety, "
            "dose, and evidence differ. Immunosuppressed patients should not assume \"natural\" means "
            "risk-free, especially with live organisms.",
            "If a wellness coach recommends stacking a prebiotic powder onto prescribed EEN, pause. "
            "Extra fermentation load can worsen gas, osmotic diarrhea, or bloating during an already "
            "fragile week. Ask the prescribing dietitian before any add-on."
        )
        + h2("Strictures, pouches, ostomies: fiber is not one rule")
        + p(
            "Stricturing small-bowel Crohn's often needs texture caution even when soluble fiber in "
            "liquids is debated. J-pouch and ostomy output can swing with fermentable loads. A formula "
            "that helps one anatomy can aggravate another. Bring operative history and last imaging "
            "descriptions to nutrition visits so advice is not generic.",
            "Related anatomy-specific reading: <a href=\"/blog/j-pouch-basics-ibd\">J-pouch basics</a>, "
            "<a href=\"/blog/ostomy-basics-ibd\">ostomy basics</a>, "
            "<a href=\"/blog/perianal-crohns-fistula-abscess\">perianal Crohn's</a>."
        )
        + h2("Practical home experiment rules (that are mostly \"don't\")")
        + ul(
            [
                "Do not change fiber formula brands mid-EEN without clinic agreement",
                "Do not add multiple new fermentable foods the same week you change formula fiber",
                "Do not interpret one gassy afternoon as proof the microbiome is ruined",
                "Do log timing of antibiotics, formula changes, and stool output together",
                "Do call early if output and dizziness rise together after a switch",
            ]
        )
        + p(
            "Good logging turns anecdotes into clinical data. Nurse lines can act on \"output doubled "
            "within 24 hours of the new formula\" better than on \"my gut feels off.\""
        )
        + h2("When fiber or formula changes need urgent review")
        + p(
            "New severe bloating with vomiting, inability to pass gas with known strictures, dehydration "
            "from high-output diarrhea after a formula switch, or fever with immunosuppression deserve "
            "prompt clinical contact. See <a href=\"/blog/vomiting-obstruction-ibd-warning-signs\">vomiting "
            "and obstruction warning signs</a> and <a href=\"/ibd-red-flags-urgent-care\">IBD red flags</a>."
        )
        + h2("Related reading and sources")
        + p(
            f'<a href="{PUBMED_FIBER}" rel="noopener noreferrer">Serbanescu et al., BMC Med 2025 (PubMed)</a>, '
            f'<a href="{LAB}" rel="noopener noreferrer">Duke AMP Lab</a>, '
            f'<a href="{PROFILE}" rel="noopener noreferrer">Mara Serbanescu profile</a>, '
            f'<a href="{AGA}" rel="noopener noreferrer">AGA diet therapies update</a>, '
            '<a href="/ibd-nutrition">IBDPal nutrition hub</a>.'
        )
        + fiber_faq
        + h2("More detail for careful readers")
        + p(
            "On a second pass, label each paragraph ICU or IBD outpatient in your notes. Keeping those "
            "labels separate prevents accidental protocol mixing when you are tired. Education is strongest "
            "when it improves questions, not when it multiplies unsupervised experiments.",
            "If you share articles with family, send the PubMed link plus one sentence: this is research "
            "context, not a home feeding protocol. That single disclaimer prevents well-meant carton swaps."
        )
        + h2("Clinic script you can copy into the patient portal")
        + p(
            "\"I read a 2025 pilot trial on fiber-containing enteral nutrition and stool microbes in "
            "trauma ICU patients (PMID 41462238). I know I am not an ICU trauma patient. I still want to "
            "know whether my current formula is fiber-free or prebiotic-enriched, whether recent "
            "antibiotics change your preference, and which symptoms should trigger a formula call.\"",
            "Short portal messages get faster answers than pasted abstracts. Attach your formula label "
            "photo. If you are mid-EEN, say so in the first line so the dietitian sees urgency."
        )
    )

    een_pen_body = (
        p(
            "Families often hear \"we might try formula\" without a clear map of exclusive versus partial "
            "plans. This guide compares exclusive enteral nutrition (EEN) and partial enteral nutrition "
            "(PEN) for Crohn's disease in patient language: goals, schedules, school and work logistics, "
            "food reintroduction, and how to judge progress with your team. Education only, not a protocol "
            "to start without clinician supervision."
        )
        + h2("EEN and PEN in one sentence each")
        + ul(
            [
                "<strong>EEN:</strong> Formula provides essentially all nutrition for a defined induction "
                "or bridging period; mixed diet is paused or tightly limited.",
                "<strong>PEN:</strong> Formula covers a substantial share of calories while some foods "
                "remain, often overnight or between meals.",
            ]
        )
        + p(
            "Centers differ on how strict \"exclusive\" must be. Some allow clear fluids or specific "
            "chewing gum rules; others do not. Write the local definition down so home and clinic are "
            "not improvising different diets."
        )
        + h2("When teams discuss EEN")
        + p(
            "EEN is especially familiar in pediatric Crohn's induction because it can support mucosal "
            "healing goals and growth while avoiding or delaying steroids in selected patients. Adult "
            "use exists but varies by center, prior response, pregnancy planning, and patient preference. "
            "EEN may also appear before surgery, after surgery, or when oral intake collapses during a flare.",
            "EEN is labor-intensive. It asks for shopping logistics, taste endurance, social planning, and "
            "sometimes tube feeds. Success rates improve when the whole household understands the timeline."
        )
        + h2("When PEN is the better fit")
        + p(
            "PEN can protect weight when appetite is poor but a full exclusive period is unrealistic. "
            "Athletes, college students, and caregivers sometimes tolerate overnight feeds plus daytime "
            "meals better than weeks of only cartons. PEN is also used as a step-down after EEN or as "
            "long-term nutrition insurance beside biologics.",
            "PEN is not automatically \"EEN lite with the same anti-inflammatory punch.\" Ask what "
            "evidence and goals your center expects from the partial plan you are offered."
        )
        + h2("Building a day that is survivable")
        + p(
            "Map cartons onto wake, school, work, and sleep. Many people chill formula, use opaque cups "
            "in public, and keep spare cartons in a backpack. For tubes, practice pump setup before the "
            "first school night. Related logistics: "
            "<a href=\"/blog/high-school-ibd-survival-guide\">high school IBD guide</a>, "
            "<a href=\"/blog/college-with-ibd\">college with IBD</a>, "
            "<a href=\"/blog/teen-nutrition-ibd-growth\">teen nutrition and growth</a>."
        )
        + ul(
            [
                "Write calories per day and minimum completed volume that counts as adherence",
                "Plan bathroom access during larger daytime boluses",
                "Decide who reorders formula before the cupboard hits two cartons",
                "Agree on what \"cheating\" means so shame does not replace problem-solving",
            ]
        )
        + h2("Food reintroduction after EEN")
        + p(
            "Reintroduction is part of therapy, not an afterthought. Teams may use staged textures, "
            "supervised exclusion patterns, or gradual return to a Mediterranean-style template. Rapid "
            "junk-food rebound can confuse symptom attribution. Ask for a written week-by-week ladder "
            "and which symptoms should pause the ladder.",
            "Keep a simple food and stool log for the first two reintroduction weeks. IBDPal tracking "
            "can sit beside formula volumes: "
            "<a href=\"/blog/tracking-food-symptoms-ibdpal\">tracking food and symptoms</a>."
        )
        + h2("How to measure whether the plan is working")
        + ul(
            [
                "Weight and growth velocity for children and teens",
                "Energy, school attendance, and pain scores",
                "Stool frequency, blood, and night waking",
                "Lab markers your clinician chose (not every patient needs daily calprotectin)",
                "Tolerance: nausea, reflux, diarrhea attributable to formula rate",
            ]
        )
        + p(
            "If nothing is improving by the checkpoint your team set, ask about formula type changes, "
            "tube support, medication escalation, or infection testing. Do not silently stretch a failing "
            "plan for weeks out of stubbornness."
        )
        + h2("Formula composition still matters in EEN and PEN")
        + p(
            "Polymeric versus elemental debates, modular protein additives, and fiber content belong in "
            "the same visit as calorie math. Research outside IBD, including ICU work on fiber-containing "
            "enteral feeds and microbiome dynamics "
            f'(<a href="{PUBMED_FIBER}" rel="noopener noreferrer">PubMed 41462238</a>), shows that '
            "formula details interact with antibiotics and baseline dysbiosis. Translate that into one "
            "clinic question: why this product for me, now?"
        )
        + h2("Emotional load and family roles")
        + p(
            "EEN can strain siblings, partners, and mealtime culture. Name the strain early. Share cooking "
            "duties so the person on formula is not surrounded by aromas they cannot share, or conversely "
            "so caregivers are not eating sad leftovers in a closet. Mental health support is appropriate "
            "when nutrition therapy feels like identity loss. See "
            "<a href=\"/blog/depression-anxiety-ibd\">depression and anxiety with IBD</a> and "
            "<a href=\"/blog/partner-caregiver-ibd\">partner and caregiver themes</a>."
        )
        + h2("Questions for the EEN versus PEN decision visit")
        + ul(
            [
                "What outcome would make EEN clearly worth six weeks for us?",
                "If PEN is chosen, what food list is allowed in week one?",
                "What is the exit criteria if I cannot meet volume by day five?",
                "How do steroids or biologics change if formula is the induction path?",
                "Who is my after-hours contact for tube clogging or vomiting during feeds?",
            ]
        )
        + h2("Pediatric, teen, and adult differences that matter")
        + p(
            "In pediatrics, growth charts and school attendance often sit beside calprotectin as success "
            "markers. Parents may run the shopping and pump setup while the child experiences the taste "
            "burden. Teens need privacy scripts for friends and sports. Adults may care more about work "
            "meetings, childcare, and whether EEN conflicts with travel or caregiving roles.",
            "Adult Crohn's patients sometimes feel dismissed when they ask about EEN because medicines "
            "dominate adult algorithms. It is still fair to ask whether a time-limited exclusive or "
            "partial formula trial could support a specific goal such as steroid sparing, preoperative "
            "optimization, or bridging a medicine change. The answer may be no. Asking still clarifies "
            "the plan."
        )
        + h2("Taste fatigue toolkits teams actually use")
        + ul(
            [
                "Temperature changes: colder cartons, or room temperature if cold triggers cramps",
                "Approved flavorings only if your center allows them with that brand",
                "Straw pacing and smaller more frequent boluses",
                "Switching from oral to overnight tube for part of the volume",
                "Short planned breaks only if the protocol explicitly allows them",
            ]
        )
        + p(
            "Do not add cocoa powders, juice concentrates, or protein supplements that change osmolality "
            "unless the dietitian signs off. Well-meant kitchen creativity is a common reason EEN weeks "
            "derail."
        )
        + h2("When EEN or PEN overlaps with flares and ER risk")
        + p(
            "Formula does not cancel red flags. Heavy bleeding, obstruction symptoms, high fever on "
            "immunosuppression, or dehydration still need urgent pathways. Keep "
            "<a href=\"/blog/flare-first-48-hours\">flare first 48 hours</a> and "
            "<a href=\"/blog/when-to-call-gi-vs-er-ibd\">GI versus ER</a> handy even mid-EEN.",
            "If vomiting prevents volume goals for more than a short window your team defined, call "
            "rather than \"catching up\" with huge boluses that worsen reflux."
        )
        + h2("A 30-day planning template you can adapt")
        + p(
            "Days 1 to 3: confirm supplies, practice pump skills, set household rules. Days 4 to 14: "
            "protect sleep, track volumes, and use early nurse contact for tolerance issues. Days 15 to "
            "21: mid-course review of weight and symptoms. Days 22 to 30: lock the reintroduction ladder "
            "and medicine plan so the end of exclusive feeding is not improvised on a Friday night.",
            "Couples and co-parents should put the template on a shared note. Split night pump alarms "
            "and daytime carton counts so one person does not burn out silently."
        )
        + h2("Related reading")
        + p(
            "<a href=\"/blog/enteral-nutrition-ibd\">Enteral nutrition overview</a>, "
            "<a href=\"/blog/fiber-prebiotics-enteral-feeds-microbiome\">Fiber and prebiotic formulas</a>, "
            "<a href=\"/blog/hospital-feeding-ibd-enteral-parenteral\">Hospital feeding</a>, "
            "<a href=\"/guides/protein-healing-ibd-flare\">Protein during healing</a>, "
            "<a href=\"/ibd-nutrition\">Nutrition hub</a>."
        )
        + een_faq
        + h2("More detail for careful readers")
        + p(
            "Re-read the exclusive versus partial definitions with a highlighter. Ambiguous rules are the "
            "most common preventable cause of week-one conflict at home. If two caregivers disagree about "
            "whether gum or broth is allowed, ask the clinic for a one-line clarification the same day.",
            "Keep a paper backup of pump settings in case phone batteries die at night. Small logistics "
            "details protect the clinical plan as much as formula brand choice does."
        )
        + h2("Shared decision checklist before you leave the visit")
        + p(
            "Before you walk out, confirm five items aloud: exclusive or partial definition, formula "
            "name and daily volume, first checkpoint date, after-hours contact, and the medicine plan "
            "that runs beside formula. If any item is fuzzy, stay in the room until it is written.",
            "Take a photo of the after-visit summary. Send it to any caregiver who shops or manages "
            "night feeds. Misaligned households are a top reason volume goals fail in week one."
        )
        + h2("Worked examples of goals (illustrative, not prescriptions)")
        + p(
            "<strong>Example A:</strong> A teen with new ileal Crohn's starts six weeks of EEN aiming to "
            "improve stool frequency, stabilize weight, and delay steroids while a biologic prior "
            "authorization completes. Success is defined as weight gain, fewer night stools, and a "
            "scheduled reintroduction visit at week five.",
            "<strong>Example B:</strong> An adult with stricturing disease uses nocturnal PEN for 50 "
            "percent of calories during a low-appetite month, with daytime soft foods approved by the "
            "dietitian. Success is holding weight and completing workdays without ER visits.",
            "<strong>Example C:</strong> A preoperative optimization plan uses exclusive formula for a "
            "shorter window to improve nutrition markers before elective resection. Surgery dates and "
            "formula stop rules are written together so nobody is surprised.",
            "Your story will differ. The point of examples is to show how specific goals prevent "
            "vague \"try formula and see\" plans that never define success."
        )
        + h2("Monitoring labs and what they are not")
        + p(
            "Teams may check electrolytes, albumin or prealbumin with caution about interpretation, "
            "vitamin D, iron studies, B12, and inflammatory markers. Albumin falls with inflammation and "
            "is a poor isolated \"nutrition grade.\" Ask which numbers will actually change decisions.",
            "Stool calprotectin trends can help in some induction paths, but timing matters. Do not "
            "home-order panels from wellness companies and then reverse-engineer your EEN week."
        )
    )

    barrier_body = (
        p(
            "\"Leaky gut,\" dysbiosis, and microbiome are words that travel faster on social media than "
            "in clinic notes. This article translates gut barrier and microbial imbalance ideas into "
            "careful patient language for Crohn's and ulcerative colitis. It draws on publicly described "
            "research themes about how microbes, barrier function, and inflammation interact under stress, "
            "including work highlighted by microbiome-focused labs. Educational only. It is not a diagnosis "
            "of leaky gut syndrome and not a detox plan."
        )
        + h2("What the gut barrier is trying to do")
        + p(
            "Your intestinal lining is a selective gate. It absorbs nutrients and water while limiting "
            "how far microbes and microbial products travel into the body. Mucus, epithelial cells, immune "
            "cells, and the microbiome all participate. When illness, inflammation, poor blood flow, "
            "or severe physiologic stress disrupt that balance, researchers study whether microbial "
            "components and metabolites contribute to wider immune activation.",
            "Public descriptions of the "
            f'<a href="{LAB}" rel="noopener noreferrer">Duke AMP Laboratory</a> explain a related clinical '
            "research focus: how microbes may influence immune responses and complications in perioperative "
            "and critically ill patients, including pathways that involve barrier stress and inflammation. "
            "IBD is a different disease setting, but the vocabulary (barrier, dysbiosis, microbial products, "
            "immune signaling) overlaps enough to help patients read science news more calmly."
        )
        + h2("Dysbiosis without the hype")
        + p(
            "<strong>Dysbiosis</strong> means a microbial community pattern associated with a disrupted "
            "or disease-related state. It is not a single lab number you can order from a wellness booth. "
            "IBD research has described reduced diversity and shifts in certain bacterial groups in many "
            "patients, but patterns vary and causation is complex. Antibiotics, diet, inflammation itself, "
            "and genetics all leave fingerprints.",
            "Consumer stool tests marketed for \"optimize your microbiome\" rarely change IBD medication "
            "plans. If a test is offered, ask how the result would alter treatment. If it would not, you "
            "can save money and anxiety."
        )
        + h2("Microbial products, inflammation, and distal effects")
        + p(
            "Scientists study how microbial molecules in blood or tissues relate to organ injury, delirium "
            "risk in critical illness, and immune phenotypes in sepsis research programs. Those are "
            "specialized questions for ICU and translational labs, not DIY blood microbiome kits. For IBD "
            "patients, the practical translation is simpler: systemic symptoms like fatigue, joint pain, "
            "or brain fog can have many causes, and teams investigate inflammation, iron, sleep, medicines, "
            "and mental health rather than blaming a vague toxin narrative.",
            "Related IBDPal reading: <a href=\"/blog/ibd-fatigue-brain-fog\">fatigue and brain fog</a>, "
            "<a href=\"/blog/ibd-joint-pain-arthritis\">joint pain</a>, "
            "<a href=\"/blog/ibd-extraintestinal-manifestations\">extraintestinal manifestations</a>."
        )
        + h2("Nutrition as one lever, not a miracle switch")
        + p(
            "Diet patterns, exclusive enteral nutrition, and fiber composition can alter microbial "
            "substrates. That is one reason formula research measures stool communities when fiber is "
            "added or removed "
            f'(<a href="{PUBMED_FIBER}" rel="noopener noreferrer">fiber-containing EN pilot, PubMed 41462238</a>). '
            "In IBD, nutrition supports care alongside medicines that directly target immune pathways. "
            "AGA guidance frames diet therapies as adjuncts, not cures "
            f'(<a href="{AGA}" rel="noopener noreferrer">AGA clinical practice update</a>).',
            "If someone promises to \"seal your gut in 14 days\" with an expensive powder stack, treat "
            "that as marketing. Ask your IBD dietitian for evidence-aligned steps instead."
        )
        + h2("Barrier-friendly habits that are still boring (and useful)")
        + ul(
            [
                "Take prescribed IBD therapy consistently rather than substituting supplements",
                "Treat infections promptly without stockpiling leftover antibiotics",
                "Use dietitian-guided reintroduction after flares instead of permanent fear diets",
                "Protect sleep and hydration, which affect resilience even when they do not \"heal\" IBD",
                "Avoid NSAIDs when your clinician has flagged them as risky for your gut",
            ]
        )
        + p(
            "Boring habits are often the ones that survive peer review. See "
            "<a href=\"/blog/nsaids-ibd-risk\">NSAIDs and IBD</a>, "
            "<a href=\"/blog/sleep-rest-ibd-flares\">sleep during flares</a>, and "
            "<a href=\"/blog/hydration-tips-ibd\">hydration tips</a>."
        )
        + h2("How to read microbiome headlines without spiraling")
        + ul(
            [
                "Check whether the study was in mice, ICU patients, or ambulatory IBD",
                "Note sample size: pilot trials generate hypotheses more than house rules",
                "Look for antibiotic co-exposures that may explain microbial shifts",
                "Ask what clinical endpoint improved: symptoms, steroids spared, hospitalization, or only sequencing graphs",
            ]
        )
        + p(
            "Dr. Serbanescu's "
            f'<a href="{PROFILE}" rel="noopener noreferrer">Duke School of Medicine profile</a> and lab '
            "pages are examples of how academic groups describe ongoing programs. They are starting points "
            "for curiosity, not patient protocols."
        )
        + h2("When barrier worries should become a clinic call")
        + p(
            "Fever, severe pain, heavy bleeding, dehydration, or new neurologic changes are not "
            "\"detox reactions.\" They are medical symptoms. Use "
            "<a href=\"/flare-help\">flare help</a> and "
            "<a href=\"/blog/when-to-go-er-ibd\">ER guidance</a> when red flags appear."
        )
        + h2("What \"translocation\" talk means without catastrophizing")
        + p(
            "In research settings, scientists study whether microbial components cross a stressed barrier "
            "and influence immune cells elsewhere in the body. Public lab descriptions of microbiome "
            "profiling work in anesthesiology and critical care often mention complications such as organ "
            "dysfunction or secondary infection as outcomes of interest. That is a research agenda about "
            "mechanisms under extreme physiologic stress.",
            "For someone managing outpatient ulcerative colitis, hearing \"bacteria leaking into your blood\" "
            "on a podcast can create panic that does not match your clinical situation. If you are stable, "
            "on therapy, and without sepsis signs, you are not living inside an ICU translocation model. "
            "Bring fears to clinic instead of midnight supplement shopping."
        )
        + h2("Immune education that stays grounded")
        + p(
            "IBD involves immune-mediated inflammation of the gut, sometimes with joint, skin, or eye "
            "involvement. Microbiome patterns may influence risk and course, but they are one layer among "
            "genetics, environment, smoking history in Crohn's, prior infections, and medication access. "
            "No single yogurt, fermented tea, or spore product resets that network on a schedule influencers "
            "prefer.",
            "When researchers personalize nutrition in the ICU because antibiotics change fiber responses, "
            "the humble patient lesson is similar: context matters. Your antibiotic courses, steroid "
            "exposure, surgeries, and diet restrictions create a personal context your clinician knows "
            "better than a generic microbiome blog."
        )
        + h2("A calmer supplement conversation")
        + ul(
            [
                "List every capsule and powder you take, including \"just digestive enzymes\"",
                "Ask which ones have evidence in IBD versus marketing language",
                "Separate deficiency replacement (iron, B12, D) from microbiome optimization claims",
                "Stop one experiment at a time so you can tell what helped or harmed",
                "Avoid products that promise to cure Crohn's or replace biologics",
            ]
        )
        + p(
            "Dietitians and pharmacists can flag interactions. Bring bottles to visits. Related: "
            "<a href=\"/blog/micronutrients-ibd-deficiencies\">micronutrient deficiencies</a> and "
            "<a href=\"/blog/iron-b12-vitamin-d-ibd\">iron, B12, and vitamin D</a>."
        )
        + h2("Talking to kids and teens about barrier science")
        + p(
            "Young people deserve honest language without horror imagery. Try: \"Your gut lining is "
            "inflamed, medicines help calm that, and food choices support energy while we heal.\" Avoid "
            "telling them their guts are poisoned or dirty. Shame worsens avoidant eating and anxiety.",
            "School-age materials from reputable foundations beat random videos. Pair science curiosity "
            "with routine care: meds, sleep, hydration, and trusted adults. See "
            "<a href=\"/blog/living-with-ibd-kids\">living with IBD as a kid</a> and "
            "<a href=\"/teens-and-school\">teens and school hub</a>."
        )
        + h2("Related reading")
        + p(
            "<a href=\"/blog/how-nutrition-impacts-gut-health-ibd\">Nutrition and gut health</a>, "
            "<a href=\"/blog/gut-microbiome-autoimmune\">Gut microbiome and autoimmune overlap</a>, "
            "<a href=\"/blog/enteral-nutrition-ibd\">Enteral nutrition</a>, "
            "<a href=\"/blog/probiotics-ibd-gut-health\">Probiotics and IBD</a>, "
            "<a href=\"/research\">Research sources</a>."
        )
        + barrier_faq
        + h2("More detail for careful readers")
        + p(
            "If a headline uses leaky gut to sell a cleanse, close the tab. If a lab page describes "
            "mechanisms in critical illness, file it under research curiosity. Your daily checklist stays "
            "medicines, hydration, sleep, and the dietitian plan you already have.",
            "Teaching relatives this filter can reduce inbox noise. Share one foundation page and your "
            "clinic's written plan instead of debating every supplement advertisement."
        )
        + h2("A one-week calm reading plan")
        + p(
            "Day one: skim a foundation patient page on diet. Day two: read IBDPal's enteral overview. "
            "Day three: read the PubMed abstract on fiber-containing EN without doomscrolling comments. "
            "Day four: write three clinic questions. Day five: review your actual medication list. Day "
            "six: rest. Day seven: send the portal message or bring questions to the visit.",
            "Curiosity paced like this informs care. Curiosity that replaces sleep and meds undermines it."
        )
        + h2("How stress physiology fits without becoming a blame story")
        + p(
            "Severe physiologic stress, sleep loss, and undernutrition can alter barrier and immune "
            "signaling in research models. That does not mean patients \"caused\" Crohn's by stressing "
            "too much. Blame narratives harm adherence and relationships.",
            "Helpful framing: reduce controllable loads (sleep debt, skipped meds, NSAID overuse, "
            "extreme crash diets) because they make living with IBD harder, not because you owe the "
            "internet a perfect lifestyle. Pair stress skills with medical therapy. See "
            "<a href=\"/blog/stress-coping-strategies-ibd\">stress coping strategies</a>.",
            "If brain fog or mood changes are prominent, ask about anemia, B12, sleep apnea, steroid "
            "effects, and mental health referral rather than only microbiome explanations."
        )
        + h2("What to save from academic lab pages")
        + p(
            "When you visit a lab site, save the research questions, not the implied DIY protocol. For "
            f'example, the <a href="{LAB}" rel="noopener noreferrer">AMP Lab description</a> emphasizes '
            "microbiome influences on immune responses and outcomes in perioperative and critically ill "
            "patients, plus goals around mechanisms, biomarkers, and therapeutic targets. Those are "
            "scientific aims. Your therapeutic targets remain the ones on your after-visit summary.",
            f'Similarly, <a href="{PROFILE}" rel="noopener noreferrer">faculty profiles</a> help you '
            "see who leads a program. They are not appointment booking for IBD second opinions unless "
            "your care team makes a formal referral."
        )
        + h2("Bottom line for barrier and dysbiosis curiosity")
        + p(
            "Use barrier and microbiome language to ask better questions, not to diagnose yourself or "
            "abandon proven therapy. Nutrition, sleep, infection care, and prescribed medicines remain "
            "the daily work. Research labs will keep refining mechanisms; your job is partnership with "
            "the clinicians who know your history."
        )
    )

    hospital_body = (
        p(
            "Hospital weeks rearrange eating completely: NPO orders, clear liquids, tube feeds, or "
            "occasional parenteral nutrition. This guide explains how enteral and parenteral feeding "
            "show up for people with IBD during admissions, after surgery, and in recovery, plus which "
            "questions keep you oriented. Educational only. Follow the orders taped to your bedrail if "
            "they differ from general education here."
        )
        + h2("Why teams say \"use the gut when you can\"")
        + p(
            "When the bowel can safely receive nutrition, enteral feeding (oral diet, oral formula, or "
            "tube) is generally preferred over intravenous nutrition because it supports the gut lining "
            "and avoids some central-line risks. Critical care and surgical nutrition research programs, "
            "including microbiome-oriented labs such as the "
            f'<a href="{LAB}" rel="noopener noreferrer">Duke AMP Lab</a>, study how feeding strategies '
            "interact with microbes and inflammation during severe stress. The bedside translation for "
            "patients is practical: ask each day whether the plan is still NPO, and what the next step "
            "toward gut feeding is."
        )
        + h2("Common hospital nutrition stages")
        + ul(
            [
                "<strong>NPO:</strong> Nothing by mouth, often before procedures or when obstruction is feared",
                "<strong>Clear liquids:</strong> Temporary bridge, not a complete nutrition plan",
                "<strong>Oral diet advances:</strong> Texture and fiber ladder based on surgery and symptoms",
                "<strong>Enteral formula:</strong> Sip feeds or tube feeds when intake lags",
                "<strong>Parenteral nutrition:</strong> IV nutrition when the gut cannot be used adequately",
            ]
        )
        + p(
            "Write the stage on a notepad each morning. Hospital days blur. Knowing yesterday's plan "
            "helps you notice silent delays."
        )
        + h2("Tube feeds during admission")
        + p(
            "Nasoenteric tubes may deliver continuous or bolus feeds. Nurses manage rates, flushes, and "
            "residuals according to protocol. Tell the team about prior strictures, aspiration history, "
            "and home EEN formulas you tolerate. Do not assume the hospital brand matches your home brand; "
            "ask whether continuity matters for your induction plan.",
            "Fiber content may differ from your outpatient formula. Given research showing context-dependent "
            "microbial responses to fiber-containing enteral nutrition in critically ill trauma patients "
            f'(<a href="{PUBMED_FIBER}" rel="noopener noreferrer">PubMed 41462238</a>), it is reasonable '
            "to ask how antibiotics and formula fiber are being coordinated, without expecting an ICU "
            "trial to dictate your Crohn's outpatient plan."
        )
        + h2("Parenteral nutrition: what to understand without panic")
        + p(
            "TPN or PN can be lifesaving when the bowel needs rest or cannot absorb enough. It requires "
            "line care, glucose and electrolyte monitoring, and infection vigilance. Ask about goals and "
            "exit criteria: what gut function would allow weaning to enteral feeds? Related education: "
            "<a href=\"/blog/enteral-nutrition-ibd\">enteral overview</a> and "
            "<a href=\"/blog/exclusive-vs-partial-enteral-nutrition-crohns\">EEN vs PEN</a>."
        )
        + h2("After IBD surgery")
        + p(
            "Enhanced recovery pathways often encourage earlier oral intake when safe. Your surgeon and "
            "IBD team set the pace based on anastomosis type, sepsis risk, and nausea. Protein targets "
            "matter for wound healing; dietitians may add modular protein or formula even when meals "
            "look small. See <a href=\"/guides/protein-healing-ibd-flare\">protein during healing</a>.",
            "Ostomy education, output tracking, and dehydration prevention are part of nutrition too. "
            "High outputs can empty fluids faster than meal trays refill them. Use "
            "<a href=\"/blog/dehydration-ibd-warning-signs\">dehydration warning signs</a> and "
            "<a href=\"/blog/ostomy-basics-ibd\">ostomy basics</a> as conversation starters."
        )
        + h2("Medicines, infection, and feeding interactions")
        + p(
            "Steroids, antibiotics, and biologics timing may shift during admission. Feeding plans should "
            "be updated when nausea medicines, bowel regimens, or infection status change. If you were "
            "on EEN before admission, ask whether the hospital stay pauses, modifies, or restarts that plan.",
            "Bring a photo of your home formula label. Brand substitutions happen quietly at night shift "
            "change."
        )
        + h2("Discharge nutrition checklist")
        + ul(
            [
                "Written diet stage for the first 72 hours home",
                "Formula brand, rate, and supply plan if tube or sip feeds continue",
                "Follow-up with GI and dietitian dates",
                "Red flags: vomiting, wound issues, fever, inability to meet fluid goals",
                "Medication list reconciled with pharmacy, including any held biologics",
            ]
        )
        + p(
            "After ER or inpatient scares, structured follow-up prevents silent deterioration. See "
            "<a href=\"/blog/after-er-visit-ibd-follow-up\">after an ER visit</a> for a parallel checklist."
        )
        + h2("Questions to ask the hospital team daily")
        + ul(
            [
                "What is today's nutrition goal in calories and protein?",
                "Are we still NPO for a reason that remains active?",
                "If tube feeds, what is the target rate by tonight?",
                "If on PN, what is the planned bridge back to gut feeding?",
                "Who do I message if home formula shipment will not arrive before discharge?",
            ]
        )
        + h2("Related reading and public research context")
        + p(
            f'<a href="{LAB}" rel="noopener noreferrer">Duke AMP Lab overview</a>, '
            f'<a href="{PROFILE}" rel="noopener noreferrer">Mara Serbanescu profile</a>, '
            f'<a href="{PUBMED_FIBER}" rel="noopener noreferrer">Fiber-containing EN microbiome trial</a>, '
            '<a href="/blog/gut-barrier-dysbiosis-inflammation-ibd">Gut barrier and dysbiosis</a>, '
            '<a href="/flare-help">Flare help</a>, '
            '<a href="/ibd-nutrition">Nutrition hub</a>.'
        )
        + h2("ICU versus IBD ward: same words, different stakes")
        + p(
            "Critically ill trauma patients on ventilators face dysbiosis, multi-drug antibiotics, and "
            "organ support that most IBD admissions never require. Still, families hear overlapping "
            "vocabulary: enteral feeds, fiber, microbiome, inflammation. Knowing the difference protects "
            "you from copying ICU protocols at home after discharge.",
            "If your loved one is in an ICU with IBD as a background diagnosis, ask the ICU team and the "
            "GI consult service who owns nutrition decisions each day. Split ownership is a common source "
            "of conflicting messages about NPO status."
        )
        + h2("Caregiver roles during feeding transitions")
        + p(
            "Caregivers often become unofficial pump technicians and carton counters. Ask nurses for "
            "teach-back before discharge: show them you can start, pause, flush, and troubleshoot alarms. "
            "Record a phone video of the setup if the hospital allows. Sleep-deprived recall is a weak "
            "training plan.",
            "Emotional load is real when trays arrive with foods the patient cannot have yet. Request "
            "meal trays timed with the allowed stage, or ask for empty trays so aromas are not tormenting "
            "someone still NPO. Small dignity fixes matter."
        )
        + h2("Rebuilding appetite after the hospital")
        + p(
            "Taste changes from medicines, fear of pain after eating, and deconditioning all suppress "
            "appetite. PEN or sip feeds can bridge while solid foods return. Set protein targets first, "
            "then volume. Short walks, daylight, and constipation prevention (when appropriate) help "
            "appetite more than forcing huge holiday meals on day two home.",
            "If nausea persists, ask whether medicines, reflux, thrush, or delayed gastric emptying need "
            "attention before blaming \"picky eating.\" Related: "
            "<a href=\"/blog/protein-meal-plan-ibd-remission\">protein meal ideas</a> and "
            "<a href=\"/blog/low-residue-diet-flare\">low-residue ideas</a> only with clinician agreement."
        )
        + h2("Document packet to keep in a folder")
        + ul(
            [
                "Discharge nutrition orders and allowed diet stage",
                "Formula label photo and daily volume",
                "Surgery and anastomosis description in plain language",
                "Antibiotic list with stop dates",
                "GI and dietitian contact numbers",
                "Return precautions specific to your admission diagnosis",
            ]
        )
        + p(
            "Upload the packet to your patient portal if possible. Future ER visits go faster when prior "
            "feeding plans and strictures are visible."
        )
        + h2("A note on research curiosity during recovery")
        + p(
            "Some patients cope by reading science. That can be healthy if it reduces fear and improves "
            "questions. It becomes unhelpful when every abstract becomes a new self-protocol. Bookmark "
            f'<a href="{PUBMED_FIBER}" rel="noopener noreferrer">the fiber-EN microbiome pilot</a> and '
            f'the <a href="{LAB}" rel="noopener noreferrer">AMP Lab page</a> for later discussion, then '
            "return to sleep, meds, and the discharge checklist in front of you."
        )
        + hospital_faq
        + h2("More detail for careful readers")
        + p(
            "Photograph whiteboard nutrition goals each morning if your unit uses them. When shifts change, "
            "that photo helps you notice silent plan changes. Polite persistence is part of hospital "
            "nutrition safety.",
            "After discharge, keep the hospital dietitian's name in your notes. Continuity calls prevent "
            "formula brand surprises when specialty pharmacy substitutes products."
        )
        + h2("After discharge: first grocery and pharmacy run")
        + p(
            "Shop for the allowed diet stage only. Buy oral rehydration supplies if output is high. "
            "Confirm formula delivery ETA before you leave the hospital Wi-Fi. Fill new prescriptions "
            "the same day, especially anti-nausea or electrolyte products tied to feeding tolerance.",
            "Put the next GI and dietitian appointments in your calendar before you nap. Recovery weeks "
            "swallow unfinished scheduling tasks, and silent gaps after complex admissions are risky."
        )
        + h2("Line care and infection awareness for PN")
        + p(
            "If you go home with parenteral nutrition or a PICC, education on dressing changes, shower "
            "rules, and fever thresholds is non-negotiable. Fever with a central line is an urgent "
            "evaluation scenario for many teams. Keep the on-call number on the fridge.",
            "Never use the line for anything other than ordered infusions. Friends offering \"just a "
            "quick blood draw convenience\" are not a plan. Ask the infusion nurse which symptoms mean "
            "ER versus clinic same-day."
        )
        + h2("Coordinating GI, surgery, and nutrition voices")
        + p(
            "Mixed messages are common: surgery wants early feeds, GI worries about a stricture, "
            "nutrition wants protein targets. Request a brief multidisciplinary clarification when "
            "orders conflict. A three-line note in the chart preventing contradictory NPO instructions "
            "can spare a wasted day.",
            "As a patient, you can say: \"I am hearing two plans. Which one is active for the next "
            "twelve hours, and when do we revisit?\" Clear timeboxes beat vague reassurance."
        )
        + h2("Pediatric hospital nuances")
        + p(
            "Children may need play specialists for tube desensitization, child life support during "
            "NG placement, and school hospital tutors if admission stretches. Parents should ask for "
            "accurate growth plotting after discharge, not only weight on the last hospital day.",
            "Siblings need a simple explanation so they do not blame themselves or sneak forbidden "
            "snacks \"to help.\" Consistent rules across caregivers matter even more after discharge."
        )
        + h2("Closing reminder")
        + p(
            "Hunger, fear, and conflicting orders are normal during IBD admissions. Ask for the active "
            "nutrition plan every morning, learn tube or PN skills before discharge, and keep GI follow-up "
            "on the calendar. Education pages support that work; they do not replace the team at the bedside."
        )
    )

    return [
        {
            "slug": "enteral-nutrition-ibd",
            "title": "Enteral Nutrition for IBD: EEN, Formula Feeds, and Clinic Questions",
            "description": "Enteral nutrition and EEN for Crohn's and IBD: formula types, partial plans, tubes, research context on fiber formulas, and questions for your team. Education only.",
            "category": cat,
            "date_display": date_display,
            "date_iso": date_iso,
            "asset_dir": "enteral-nutrition-ibd",
            "images": ["enteral_1.jpg"],
            "alts": ["Nutrition formula setup illustrating enteral nutrition education for IBD"],
            "copy_from": "gut-nutrition/ulcerative-colitis-crohns-nutrition_1.jpg",
            "share": "Enteral nutrition and EEN for IBD, expanded patient guide. Education only.",
            "body": enteral_body,
        },
        {
            "slug": "fiber-prebiotics-enteral-feeds-microbiome",
            "title": "Fiber and Prebiotics in Enteral Formulas: What Microbiome Research Suggests",
            "description": "Fiber and scFOS in tube or sip feeds, why ICU microbiome trials urge caution with one-size-fits-all prebiotics, and IBD dietitian questions. Education only.",
            "category": cat,
            "date_display": date_display,
            "date_iso": date_iso,
            "asset_dir": "fiber-ibd",
            "images": ["fiber_1.jpg"],
            "alts": ["Fiber-rich foods representing formula fiber and prebiotic education"],
            "copy_from": "fiber-ibd/fiber_1.jpg",
            "share": "Fiber in enteral formulas and microbiome context. Education only, not ICU advice for home.",
            "body": fiber_body,
        },
        {
            "slug": "exclusive-vs-partial-enteral-nutrition-crohns",
            "title": "EEN vs Partial Enteral Nutrition in Crohn's: Choosing a Workable Plan",
            "description": "Exclusive enteral nutrition versus partial formula plans in Crohn's: goals, daily logistics, reintroduction, and how to measure progress. Education only.",
            "category": cat,
            "date_display": date_display,
            "date_iso": date_iso,
            "asset_dir": "enteral-nutrition-ibd",
            "images": ["enteral_1.jpg"],
            "alts": ["Formula nutrition setup for EEN and PEN patient education"],
            "share": "EEN versus partial enteral nutrition in Crohn's. Education only.",
            "body": een_pen_body,
        },
        {
            "slug": "gut-barrier-dysbiosis-inflammation-ibd",
            "title": "Gut Barrier, Dysbiosis, and Inflammation in IBD: A Calm Explainer",
            "description": "What gut barrier and dysbiosis mean for Crohn's and colitis patients, how to read microbiome headlines, and where nutrition fits. Education only.",
            "category": cat,
            "date_display": date_display,
            "date_iso": date_iso,
            "asset_dir": "gut-nutrition",
            "images": ["ulcerative-colitis-crohns-nutrition_2.jpg"],
            "alts": ["Calm nutrition context for gut barrier and microbiome education"],
            "share": "Gut barrier and dysbiosis explained for IBD. Education only.",
            "body": barrier_body,
        },
        {
            "slug": "hospital-feeding-ibd-enteral-parenteral",
            "title": "Hospital Feeding With IBD: Enteral, Parenteral, and After Surgery",
            "description": "NPO, tube feeds, TPN, and diet advances during IBD hospital stays and after surgery, with a discharge checklist. Education only.",
            "category": cat,
            "date_display": date_display,
            "date_iso": date_iso,
            "asset_dir": "er-ibd",
            "images": ["er_1.jpg"],
            "alts": ["Hospital setting for IBD feeding and recovery education"],
            "share": "Hospital enteral and parenteral feeding with IBD. Education only.",
            "body": hospital_body,
        },
    ]


def main() -> None:
    data = posts()
    OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    # Also refresh legacy single-post file used by older script.
    legacy = ROOT / "data" / "enteral-nutrition-post.json"
    legacy.write_text(json.dumps([data[0]], indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("wrote", OUT.relative_to(ROOT), f"({len(data)} posts)")
    print("wrote", legacy.relative_to(ROOT))


if __name__ == "__main__":
    main()
