# Part 2: remaining seven Oct 11 body specs (unique paragraphs).
from __future__ import annotations

def S(title: str, *paragraphs: str) -> tuple[str, list[str]]:
    return (title, list(paragraphs))


def block(*items: tuple[str, list[str]]) -> list[tuple[str, list[str]]]:
    return list(items)


ALL_SPECS = {
    "cded.py": dict(
        intro=(
            "The <strong>Crohn's Disease Exclusion Diet (CDED)</strong> combines supervised food exclusions with "
            "partial enteral nutrition for selected Crohn's disease patients. Online posts often skip formula math, "
            "growth checks, and lab monitoring. This page explains phases, typical exclusions, PEN basics, and why "
            "CDED is not a DIY cure. Education only."
        ),
        sections=block(
            S(
                "Origins and intended Crohn's population",
                "CDED emerged from pediatric Crohn's research examining whether specific dietary components plus formula support could assist standard medicines.",
                "Adult programs exist at some centers, yet availability varies by city, insurer, and dietitian staffing.",
                "Ulcerative colitis was not the primary study population; do not assume identical rules apply to UC without asking.",
                "Confirm with your gastroenterologist whether your phenotype matches protocols before buying specialty groceries.",
            ),
            S(
                "Phase one: strict lists plus formula",
                "Early weeks pair a narrow permitted food list with prescribed formula delivering part of daily calories.",
                "Volume schedules may split drinks across school or work breaks to limit nausea.",
                "Home cooking dominates because restaurant sauces hide emulsifiers excluded in manuals.",
                "Stopping early without messaging the team wastes effort and can leave inflammation untreated.",
            ),
            S(
                "Phase two: widening allowed foods",
                "Later phases reintroduce categories while tracking weight, stools, and inflammatory markers.",
                "Reintroduction is intentional, not a return to random takeout.",
                "Some foods remain optional if they never improved symptoms or labs.",
                "Calendar reminders help prevent accidental combo trials during holidays.",
            ),
            S(
                "Common exclusion categories",
                "Manuals often limit certain emulsifiers, thickeners, ultra processed snacks, and selected grains or dairy forms.",
                "Permitted fruits, vegetables, proteins, and fats still require portion guidance from your dietitian.",
                "Label reading becomes daily homework; brand swaps can silently break rules.",
                "Keep photographed labels for clinic review when symptoms drift.",
            ),
            S(
                "Partial enteral nutrition in plain words",
                "Partial enteral nutrition means medical formula supplements meals you still eat from permitted lists.",
                "Formulas differ in osmolality, fiber, and lactose; never swap brands without approval.",
                "Tube feeding routes exist for patients who cannot drink required volumes orally.",
                "Flavor, temperature, and straw pacing tricks improve tolerance for some teens.",
            ),
            S(
                "Monitoring labs, weight, and growth",
                "Expect weight checks, height velocity in children, vitamin D, iron studies, and inflammatory markers on a schedule.",
                "Restrictive phases can drop calcium, zinc, or fiber intake before anyone notices clinically.",
                "Mental health screening matters when food fear rises during strict weeks.",
                "Bring school absence data if fatigue blocks attendance.",
            ),
            S(
                "CDED versus Mediterranean style eating",
                "Mediterranean patterns emphasize olive oil, fish, legumes, and whole grains with flexibility many adults prefer in remission.",
                "CDED is stricter early and tied to formula protocols with different goals.",
                "Some patients transition toward Mediterranean meals after supervised reintroduction.",
                "Compare long term quality of life, not only short term calprotectin drops.",
            ),
            S(
                "CDED versus low FODMAP trials",
                "Low FODMAP targets fermentable carbohydrates for symptom trials with structured reintroduction.",
                "Running both experiments simultaneously blames the wrong foods when urgency returns.",
                "Sequential trials with professional oversight prevent chaotic elimination.",
                "Read <a href=\"/blog/fodmap-diet-crohns-colitis\">FODMAP overview</a> alongside CDED discussions.",
            ),
            S(
                "Who should avoid self starting CDED",
                "Eating disorder history, severe malnutrition, unstable flares, complex strictures, pregnancy, and breastfeeding require individualized medical nutrition therapy first.",
                "Patients awaiting surgery may need preoperative optimization rather than sudden exclusions.",
                "If formula copays are impossible, ask social work before day one rather than rationing silently.",
                "Teens need parental and school nurse coordination for daytime formula access.",
            ),
            S(
                "Medicines remain central",
                "Studies run CDED alongside immunomodulators, biologics, and steroids when clinicians prescribe them.",
                "Diet does not automatically replace endoscopy proven healing.",
                "Report medication changes to dietitians so timing aligns with infusion nausea or morning immunosuppression.",
                "Never stop IBD medicines because an influencer claimed diet alone cleared their photos.",
            ),
            S(
                "Travel, school, and social logistics",
                "Pack labeled bottles, nurse permission forms, and shelf stable backup options for trips.",
                "Medical letters help at airport security for powders and liquids.",
                "Hosts appreciate knowing you bring safe foods during strict phases without needing full diagnosis stories.",
                "Sports practices need hydration plans that respect formula volume limits.",
            ),
            S(
                "Insurance and formula access",
                "Ask early for prescription documentation and diagnosis codes supporting coverage.",
                "Denial letters become appeal templates; gastroenterology offices often keep sample letters.",
                "Manufacturer assistance programs help qualifying households; social workers know numbers.",
                "Track out of pocket costs for tax and flex spending documentation if applicable.",
            ),
            S(
                "When to pause and call the team",
                "Vomiting, fainting, rapid weight loss, inability to keep formula down, or new severe pain needs same day outreach.",
                "Psychological distress from restriction also warrants behavioral health support.",
                "Use <a href=\"/flare-help\">flare help</a> for clinic escalation paths already published.",
                "Do not treat dehydration as willpower failure.",
            ),
            S(
                "Documenting progress for visits",
                "Track formula ounces, permitted meals, stool count, pain scores, and missed work or school days.",
                "Photos of ingredient labels help dietitians spot hidden emulsifiers.",
                "IBDPal logs can align formula intake with symptom spikes for clearer stories.",
                "One page summaries beat long unstructured portal novels.",
            ),
        ),
        clinic=(
            "Is CDED appropriate for my Crohn's phenotype? If yes, who prescribes PEN, which formula fits my needs, "
            "and what labs will we track during each phase?"
        ),
        faqs=[
            ("Can CDED replace biologics?", "No. CDED is studied with standard IBD care, not as a guaranteed medicine substitute."),
            ("Can adults access CDED?", "Some adult centers offer supervised pathways; ask an IBD dietitian locally."),
            ("Is CDED the same as SCD?", "No. Specific Carbohydrate Diet uses different rules and evidence."),
            ("What if formula taste is awful?", "Ask about flavor trials and pacing before abandoning prescribed volume."),
        ],
        related=[
            ("Crohn's diet overview", "/blog/crohns-diet-overview-ibd"),
            ("Mediterranean diet notes", "/blog/mediterranean-diet-autoimmune"),
            ("SCD overview", "/blog/specific-carbohydrate-diet-scd-ibd"),
            ("IBD nutrition hub", "/ibd-nutrition"),
        ],
        closing=["CDED is a structured tool some Crohn's teams use with clear start and stop rules, not a moral test of willpower."],
    ),
    "scd.py": dict(
        intro=(
            "The <strong>Specific Carbohydrate Diet (SCD)</strong> removes many grains, certain sugars, and most processed foods. "
            "People with Crohn's disease or ulcerative colitis compare SCD with Mediterranean eating and research diets such as DINE CD. "
            "This page explains rules, nutrient gaps, evidence limits, and supervision needs. Education only."
        ),
        sections=block(
            S(
                "SCD rules in patient language",
                "SCD allows specific fruits, vegetables, meats, nuts, and fermented dairy while excluding conventional starches and disaccharides per community legal lists.",
                "Home cooking dominates because restaurant thickeners and starches are hard to verify.",
                "Legal lists update slowly; bring questions to dietitians rather than forum arguments.",
                "Children need calorie density monitoring when entire food groups disappear.",
            ),
            S(
                "Evidence and realistic expectations",
                "Small studies and surveys report symptom relief in selected IBD patients, yet trial quality varies compared with Mediterranean interventions in adults.",
                "SCD is not proven to replace medicines for everyone.",
                "Endoscopy healing should guide major treatment decisions, not stool frequency alone.",
                "Maintain follow up scopes or calprotectin checks your GI recommends.",
            ),
            S(
                "SCD compared with Mediterranean patterns",
                "Mediterranean eating usually keeps oats, legumes, and whole grains central with olive oil and fish.",
                "SCD removes staples many Mediterranean recipes require, affecting social meals and grocery cost.",
                "Some families blend ideas after structured trials end, under professional eyes.",
                "Flavor and culture matter for long adherence; rigid shame cycles backfire.",
            ),
            S(
                "DINE CD themes in plain words",
                "DINE CD studied Mediterranean style eating with optional modules in Crohn's disease, reporting inflammatory marker improvements in some participants versus usual education.",
                "DINE CD is not identical to SCD; less extreme restriction is a common adult takeaway.",
                "Ask whether local centers offer DINE style counseling.",
                "Compare goals: induction support versus lifelong flexibility.",
            ),
            S(
                "Nutrient gaps to monitor",
                "Calcium, vitamin D, thiamine, folate, and fiber may fall low without planning.",
                "Bone health labs deserve attention when dairy is limited.",
                "Pregnant patients need explicit calorie and folate planning.",
                "Periodic dietitian review beats guessing from multivitamin marketing.",
            ),
            S(
                "Mental health and social load",
                "Strict lists increase restaurant anxiety and family tension.",
                "Pair trials with stop dates and counseling when restriction becomes identity.",
                "Teens may hide disordered patterns behind SCD virtue language; watch for secrecy.",
                "Support groups focused on adherence without flexibility can harm; choose balanced communities.",
            ),
            S(
                "Structured trial method",
                "Baseline labs and weight, two to four week structured trial, symptom logs, and scheduled exit or reintroduction prevent endless restriction.",
                "Change one variable at a time when testing tolerance.",
                "Do not stack secret supplement stacks suggested online.",
                "Write stop rules if weight drops or mood crashes.",
            ),
            S(
                "SCD during flares versus remission",
                "Severe flares may need medical nutrition therapy or gentle textures before restrictive patterns.",
                "Starting SCD mid flare can blur whether medicines or diet moved markers.",
                "Remission trials offer cleaner attribution with your team.",
                "Hospitalized patients should follow inpatient guidance first.",
            ),
            S(
                "Ulcerative colitis readers",
                "Some UC patients attempt SCD, yet evidence is thinner than in Crohn's disease.",
                "Rectal bleeding and iron still need medical attention regardless of diet purity.",
                "Do not delay scope surveillance because symptoms feel diet controlled.",
                "Supervision remains essential for UC as for Crohn's.",
            ),
            S(
                "Kitchen workflow tips",
                "Batch cook legal proteins and freeze portions for fatigue days.",
                "Keep separate cutting boards if household members eat starches you avoid.",
                "Travel with safe snacks because airports rarely cater to SCD.",
                "Instant pot yogurt steps appear in community books; confirm pasteurization safety with dietitians.",
            ),
            S(
                "When SCD is a poor fit",
                "Complex strictures, short bowel, eating disorder history, or uncontrolled malnutrition need different pathways.",
                "If SCD social media increases shame, pause and discuss with behavioral health.",
                "Insurance may not cover extra dietitian visits; still prioritize safety over trend.",
                "Switching from SCD to inclusive remission eating also deserves professional planning.",
            ),
            S(
                "Talking with your GI and dietitian",
                "Bring legal lists you follow, typical day of eating, weight trend, and recent labs.",
                "Ask how SCD interacts with current biologics or steroids.",
                "Request written reintroduction priorities instead of vague someday guidance.",
                "Second opinions from IBD dietitians help when local access is thin.",
            ),
            S(
                "SCD and microbiome hype",
                "Online posts link SCD to microbiome shifts; science is evolving and individual.",
                "Stool tests marketed to consumers rarely guide personal SCD legality lists.",
                "Treat microbiome claims as conversation starters with researchers, not orders.",
                "Focus on symptoms, weight, and inflammation markers you can track clinically.",
            ),
            S(
                "Exit ramps and reintroduction",
                "Plan category reintroduction even if SCD helped; long term micronutrient diversity matters.",
                "Celebrate foods that return without symptoms instead of fearing entire aisles forever.",
                "If reintroduction fails, log details before blaming the wrong ingredient.",
                "Some patients maintain a hybrid plate: SCD breakfast, Mediterranean dinner, with team approval.",
            ),
        ),
        clinic=(
            "I am comparing SCD with Mediterranean or DINE CD style eating for my IBD. Which pattern fits my phenotype, "
            "and how will we monitor labs and weight if I try a restrictive trial?"
        ),
        faqs=[
            ("Is SCD safe during a flare?", "Flares may need medical nutrition first. Ask whether gentle textures should precede restrictive trials."),
            ("Can SCD cure IBD?", "No diet reliably cures IBD. Diets may support symptoms alongside prescribed treatments."),
            ("Is almond flour mandatory?", "Community recipes use almond flour often; nutrient balance still needs review."),
            ("Does SCD conflict with CDED?", "They differ; running both without guidance creates conflicting rules."),
        ],
        related=[
            ("Mediterranean diet", "/blog/mediterranean-diet-autoimmune"),
            ("CDED overview", "/blog/cded-crohns-exclusion-diet-ibd"),
            ("FODMAP overview", "/blog/fodmap-diet-crohns-colitis"),
            ("Flare foods", "/blog/flare-foods-ibd"),
        ],
        closing=["Restrictive trials deserve exit plans. Nutrition quality over the decade matters as much as the first enthusiastic month."],
    ),
}
