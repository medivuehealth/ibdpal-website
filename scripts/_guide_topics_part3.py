"""Topics 28-58: nutrition, autoimmune, and Foundation guides."""
from __future__ import annotations

P = lambda *s: s
_f = lambda q, a: (q, a)
F = "https://www.crohnscolitisfoundation.org"

def add_part3(TOPICS):

    TOPICS["camp-oasis-kids-ibd"] = {
        "body": "This page summarizes Camp Oasis, the Crohn's and Colitis Foundation camp program for children and teens with IBD, and links to official Foundation resources.",
        "sections": [
            ("What Camp Oasis offers", P(
                "Camp Oasis provides a medically supervised summer camp experience where youth with IBD meet peers who understand infusions, diets, and bathroom needs.",
                "Activities include sports, arts, and outdoor programs adapted for varying energy levels. Medical volunteers oversee health needs on site.",
                "Many families report improved confidence and reduced isolation after camp. It is not a substitute for ongoing pediatric GI care.",
            )),
            ("Medical supervision and safety", P(
                "Camp medical teams include physicians and nurses familiar with IBD therapies. Parents complete detailed health forms before attendance.",
                "Medication administration, infusion schedules, and flare protocols follow camp policies coordinated with home GI teams.",
                "Ask the Foundation about current eligibility, session dates, and scholarship options each year.",
            )),
            ("Preparing your child", P(
                "Practice self-advocacy skills: asking for restrooms, describing symptoms, and carrying supplies.",
                "Pack labeled medications, comfort items, and contact numbers. Review dietary accommodations with camp staff early.",
                "Discuss homesickness plans and how counselors communicate with parents during sessions.",
            )),
            ("Parents and siblings", P(
                "Parent information sessions explain supervision models and emergency procedures.",
                "Siblings without IBD may have separate family programs depending on region.",
                "Use camp as respite care thoughtfully while ensuring home flare plans remain active.",
            )),
            ("After camp and year-round connection", P(
                "Many campers join teen groups and chapter events after summer ends.",
                "Bring camp stories to pediatric GI visits if symptoms or adherence changed.",
                "Foundation youth resources extend beyond one week of camp.",
            )),
        ],
        "tips": ["Apply early; slots and scholarships fill quickly.", "Share your child's flare plan with camp medical staff.", "Label all medications and supplies clearly.", "Practice overnight stays before a full camp session.", "Explore Foundation teen groups for year-round peers."],
        "faq": [_f("Is Camp Oasis only in the United States?", "Camp locations and policies are listed on Foundation sites. Verify current international participation rules."),
                _f("Can my child attend on biologics?", "Many campers are on advanced therapies. Medical forms document plans."),
                _f("Does the Foundation endorse IBDPal?", "No. Selected content is used under license; the Foundation does not endorse IBDPal.")],
        "related": [("Pediatric IBD help", "/guides/pediatric-crohns-colitis-help"), ("Youth school Foundation resources", "/guides/youth-school-foundation-resources"),
                    ("Foundation resources hub", "/crohns-colitis-foundation-resources"), ("Support groups overview", "/guides/crohns-colitis-support-groups"),
                    ("Camp Oasis on Foundation site", f"{F}/camp-oasis"), ("Newly diagnosed guide", "/guides/newly-diagnosed-crohns-colitis")],
    }

    TOPICS["ibd-prior-authorization-foundation"] = {
        "body": "This page explains prior authorization for IBD medications using Crohn's and Colitis Foundation patient navigation concepts and links to official appeals resources.",
        "sections": [
            ("What prior authorization means", P(
                "Insurers often require approval before covering expensive IBD drugs. Prior auth documents medical necessity with charts, labs, and prior therapies tried.",
                "Delays can interrupt infusions or injections. Start paperwork early when switching biologics.",
                "Foundation education helps patients understand the process without offering legal advice.",
            )),
            ("Information to gather", P(
                "Collect diagnosis codes, colonoscopy reports, calprotectin or CRP trends, and medication history including failures or intolerances.",
                "Ask your clinic which staff handles prior auth. Sign releases so they can speak with insurers.",
                "Keep fax numbers and reference IDs for every call.",
            )),
            ("Step therapy and appeals", P(
                "Step therapy rules may require trying specific drugs first. Safe Step Act reforms vary by state and plan.",
                "Denials are common. Appeals with physician letters and symptom logs often succeed on second review.",
                "Foundation appeal letter templates provide starting language your doctor personalizes.",
            )),
            ("Patient assistance and copay programs", P(
                "Manufacturer copay cards and foundation assistance funds help qualifying patients during auth delays.",
                "Financial counselors at infusion centers know program eligibility.",
                "Document household income and insurance type accurately on applications.",
            )),
            ("Staying on therapy during delays", P(
                "Never stop biologics without clinician guidance while waiting on auth.",
                "Clinics may provide samples or bridge doses when available.",
                "Escalate to plan medical directors with your gastroenterologist if delays risk harm.",
            )),
        ],
        "tips": ["Start prior auth before your last dose runs out.", "Save every denial letter.", "Ask insurers for case manager names.", "Use Foundation appeal templates with your doctor.", "Log symptoms during auth delays for appeals."],
        "faq": [_f("How long does prior auth take?", "Days to weeks depending on plan and drug. Urgent requests may expedite."),
                _f("Can I pay cash to skip auth?", "Sometimes, but costs are high. Discuss with your clinic."),
                _f("Who writes appeal letters?", "Your prescriber, often with templates from Foundation or clinic legal teams.")],
        "related": [("Foundation appeal letters", "/guides/foundation-ibd-appeal-letters"), ("Step therapy and Safe Step Act", "/guides/step-therapy-safe-step-act-ibd"),
                    ("Foundation medication guide", "/guides/foundation-ibd-medication-guide"), ("Biologics overview", "/guides/biologics-crohns-colitis"),
                    ("Foundation resources hub", "/crohns-colitis-foundation-resources"), ("Doctor visit prep", "/guides/crohns-doctor-visit-prep")],
    }

    TOPICS["foundation-diet-nutrition-ibd"] = {
        "body": "This page bridges Crohn's and Colitis Foundation diet and nutrition education with IBDPal guides for meal planning, deficiencies, and clinician collaboration.",
        "sections": [
            ("Foundation nutrition education overview", P(
                "Foundation materials cover general patterns for remission and flares, micronutrient needs, and when to involve registered dietitians.",
                "Read the original Foundation diet pages for full detail. IBDPal summarizes navigation paths, not every recipe.",
                "Nutrition supports medical care but does not replace anti-inflammatory treatment when disease is active.",
            )),
            ("Linking Foundation content to daily meals", P(
                "Pair Foundation handouts with IBDPal food logs to see personal tolerance.",
                "Introduce Foundation meal ideas one at a time during stable periods.",
                "Pediatric and adult needs differ. Use age-appropriate Foundation resources.",
            )),
            ("Micronutrients Foundation highlights", P(
                "Iron, vitamin D, calcium, B12, and zinc appear frequently in Foundation nutrition education due to malabsorption and bleeding.",
                "Ask your GI team which Foundation screening recommendations apply to your labs.",
                "Supplement only deficiencies documented with testing unless directed otherwise.",
            )),
            ("Special diets in Foundation materials", P(
                "Foundation content discusses low-residue patterns, enteral nutrition, and cautions about unproven extreme diets.",
                "Bring questions about FODMAP or anti-inflammatory approaches to your IBD dietitian.",
                "Avoid starting multi-food eliminations without supervision.",
            )),
            ("Using IBDPal alongside Foundation guides", P(
                "Track symptoms when trying Foundation meal suggestions. Data beats guessing.",
                "Share exports at visits with gastroenterology and nutrition teams.",
                "Return to Foundation sources when policies or research updates publish.",
            )),
        ],
        "tips": ["Bookmark Foundation diet pages as primary sources.", "Pair reading with clinician-approved labs.", "Log meals when testing Foundation recipes.", "Ask for dietitian referral if weight changes.", "Review IBDPal nutrition guides for deeper topics."],
        "faq": [_f("Does Foundation recommend one IBD diet?", "No. Foundation education emphasizes personalization with your care team."),
                _f("Can IBDPal replace a dietitian?", "No. Apps support logging; dietitians provide medical nutrition therapy."),
                _f("Are Foundation recipes safe in flares?", "Tolerance varies. Follow your flare plan from your GI team.")],
        "related": [("What should I eat with IBD?", "/guides/what-should-i-eat-crohns-colitis"), ("Iron deficiency nutrition", "/guides/iron-deficiency-nutrition-ibd"),
                    ("Foundation site: diet and nutrition", f"{F}/diet-and-nutrition"), ("Anti-inflammatory diet guide", "/guides/anti-inflammatory-diet-ibd"),
                    ("Protein and healing", "/guides/protein-healing-ibd-flare"), ("Complete nutrition article", "/blog/complete-ibd-nutrition-guide")],
    }

    TOPICS["anti-inflammatory-diet-ibd"] = {
        "intro": "Anti-inflammatory eating patterns emphasize whole foods, healthy fats, and limited ultra-processed items. Evidence in IBD is evolving and individual. This guide explains how patients discuss anti-inflammatory diets with their GI and dietitian teams. Education only, not a prescribed meal plan.",
        "sections": [
            ("What anti-inflammatory means in IBD", P(
                "Diets rich in vegetables, fruits, olive oil, nuts, and fatty fish are studied for general health and some IBD symptoms.",
                "Anti-inflammatory labels on blogs do not guarantee they reduce bowel inflammation on scopes.",
                "Medical treatment remains primary when calprotectin or CRP are elevated.",
            )),
            ("Foods often highlighted", P(
                "Oily fish, turmeric in cooking, colorful produce, and whole grains when tolerated are common examples in patient education.",
                "Ultra-processed snacks, excess added sugar, and trans fats are frequent reduction targets.",
                "Personal tolerance still rules during active symptoms.",
            )),
            ("Cautions and limitations", P(
                "High-fiber anti-inflammatory salads may worsen active colitis. Cooked or peeled produce may be better short term.",
                "Nightshade elimination lacks strong IBD-specific evidence for everyone.",
                "Children need adequate calories; do not impose adult wellness trends without pediatric GI input.",
            )),
            ("Combining diet with medical care", P(
                "Track symptoms and labs when changing patterns. Improvement in stool without lab change may mean irritant relief only.",
                "Ask whether diet trials should wait until inflammation is controlled.",
                "Registered dietitians help adapt Mediterranean-style patterns to strictures and ostomies.",
            )),
            ("Sustainable habits", P(
                "Small swaps beat extreme overhauls. Add one vegetable daily before eliminating entire food groups.",
                "Social meals matter for mental health. Flexibility prevents burnout.",
                "Revisit goals with your team yearly as disease activity shifts.",
            )),
        ],
        "tips": ["Cook vegetables soft during flares before raw salads.", "Prioritize protein even on anti-inflammatory plans.", "Log labs alongside diet experiments.", "Avoid juice cleanses marketed as anti-inflammatory.", "Ask your dietitian for culturally familiar swaps."],
        "faq": [_f("Will this diet cure IBD?", "No. It may support overall health but does not replace IBD medications when needed."),
                _f("Is keto anti-inflammatory?", "Keto is not standard IBD care and may harm gut microbiome diversity for some patients."),
                _f("Should I take turmeric supplements?", "Discuss doses and interactions with your GI before starting supplements.")],
        "related": [("Autoimmune nutrition basics", "/guides/autoimmune-nutrition-basics"), ("What should I eat with IBD?", "/guides/what-should-i-eat-crohns-colitis"),
                    ("Anti-inflammatory diet article", "/blog/anti-inflammatory-diet-ibd"), ("Foundation diet and nutrition", "/guides/foundation-diet-nutrition-ibd"),
                    ("Track symptoms and food", "/guides/track-ibd-symptoms-food"), ("Olive oil and omega-3 topics", "/blog/complete-ibd-nutrition-guide")],
    }

    TOPICS["iron-deficiency-nutrition-ibd"] = {
        "intro": "Iron deficiency and anemia are common in IBD because of bleeding, malabsorption, and inflammation blocking iron use. Nutrition and supplements work together under clinician guidance. This guide covers education topics patients review with their GI team. Not medical advice.",
        "sections": [
            ("Why iron matters in IBD", P(
                "Low iron reduces energy, exercise tolerance, and concentration. Anemia may persist even when bowel symptoms improve.",
                "Chronic inflammation raises hepcidin, trapping iron despite adequate intake.",
                "Repeat labs track response to therapy, not single snapshots.",
            )),
            ("Dietary iron sources", P(
                "Heme iron from lean red meat, poultry, and fish is absorbed better than plant iron for many people.",
                "Pair plant iron with vitamin C rich foods like citrus or bell peppers. Separate calcium supplements from iron doses when possible.",
                "During flares, tender proteins and fortified cereals may be easier than steak.",
            )),
            ("Oral versus IV iron", P(
                "Oral iron may worsen constipation or nausea. Take as directed with your team.",
                "IV iron is common when oral forms fail, losses are high, or inflammation blocks absorption.",
                "Do not double doses without labs. Excess iron harms organs.",
            )),
            ("Monitoring and side effects", P(
                "Check hemoglobin, ferritin, and sometimes CRP together. Ferritin may look normal during inflammation.",
                "Black stools from iron supplements differ from GI bleeding. Ask when unsure.",
                "Report breathing changes or chest pain urgently; they are not typical iron side effects.",
            )),
            ("Working with your care team", P(
                "Treat ongoing bleeding sources while repleting iron.",
                "Ask dietitians for high-iron recipes that respect texture needs.",
                "Log energy and exercise tolerance as iron stores recover.",
            )),
        ],
        "tips": ["Request iron studies at routine GI visits.", "Take vitamin C with plant iron sources.", "Separate iron and calcium doses by a few hours.", "Report black tarry stools not explained by supplements.", "Read anemia article for warning signs."],
        "faq": [_f("Can I fix anemia with diet alone?", "Sometimes mild cases improve, but many IBD patients need supplements or IV iron."),
                _f("Does spinach alone solve iron deficiency?", "Plant iron helps but absorption is lower. Medical assessment still matters."),
                _f("When is bleeding an emergency?", "Heavy bleeding, dizziness, or fainting need urgent evaluation.")],
        "related": [("Anemia article", "/blog/anemia-iron-deficiency-ibd"), ("UC diet foods", "/guides/ulcerative-colitis-diet-foods"),
                    ("Blood in stool article", "/blog/blood-in-stool-ibd-when-to-worry"), ("What should I eat with IBD?", "/guides/what-should-i-eat-crohns-colitis"),
                    ("Foundation diet and nutrition", "/guides/foundation-diet-nutrition-ibd"), ("Doctor visit prep", "/guides/crohns-doctor-visit-prep")],
    }

    TOPICS["vitamin-d-bone-nutrition-ibd"] = {
        "intro": "Vitamin D, calcium, and bone health deserve attention in IBD because of malabsorption, steroid use, inflammation, and sometimes limited sun exposure. This guide summarizes nutrition topics patients discuss with gastroenterology and bone health teams. Education only.",
        "sections": [
            ("Bone risk in Crohn's and colitis", P(
                "Osteopenia and osteoporosis occur at younger ages than in the general population. Disease activity, smoking, and steroids increase risk.",
                "DEXA scans may be recommended based on age, steroid history, and fracture risk.",
                "Treat inflammation and nutrition together rather than focusing only on supplements.",
            )),
            ("Vitamin D basics", P(
                "Vitamin D supports calcium absorption and immune regulation. Low levels are common in IBD clinics.",
                "Dosing should follow labs. High doses without monitoring cause toxicity.",
                "Sun exposure helps some patients but is not enough alone when deficiency is severe.",
            )),
            ("Calcium and dietary patterns", P(
                "Dairy, fortified plant milks, tofu set with calcium, and leafy greens contribute calcium when tolerated.",
                "Lactose intolerance may require lactase or alternate sources.",
                "Spread calcium intake across meals if supplements are needed.",
            )),
            ("Steroids and bone protection", P(
                "Prolonged prednisone accelerates bone loss. Clinicians may recommend calcium, vitamin D, and sometimes bisphosphonates.",
                "Weight-bearing exercise when safe supports bone density.",
                "Never stop steroids suddenly without medical guidance.",
            )),
            ("Labs and follow-up", P(
                "Ask about 25-hydroxy vitamin D, calcium, phosphorus, and PTH when bone health is a concern.",
                "Repeat DEXA per clinic protocol after starting therapy.",
                "Smoking cessation dramatically improves bone and IBD outcomes.",
            )),
        ],
        "tips": ["Ask when your next DEXA scan is due.", "Take vitamin D with a meal containing fat.", "Choose calcium sources you tolerate in flares.", "Discuss steroid bone protection at every prednisone course.", "Log falls or fractures for your GI team."],
        "faq": [_f("Can I take huge vitamin D doses from online forums?", "No. Toxicity is real. Dose per your clinician and labs."),
                _f("Is dairy required for strong bones?", "No. Fortified alternatives and supplements can work if planned."),
                _f("Do biologics help bones?", "Controlling inflammation may help indirectly. Bone-specific therapy still matters for some.")],
        "related": [("Calcium article", "/blog/calcium-ibd"), ("Foundation diet and nutrition", "/guides/foundation-diet-nutrition-ibd"),
                    ("What should I eat with IBD?", "/guides/what-should-i-eat-crohns-colitis"), ("Iron deficiency guide", "/guides/iron-deficiency-nutrition-ibd"),
                    ("Complete nutrition article", "/blog/complete-ibd-nutrition-guide"), ("Doctor visit prep", "/guides/crohns-doctor-visit-prep")],
    }

    TOPICS["protein-healing-ibd-flare"] = {
        "intro": "Adequate protein supports tissue repair during and after IBD flares, especially when appetite is low or losses are high. This guide explains how patients meet protein needs with their GI and dietitian teams. Education only, not a meal prescription.",
        "sections": [
            ("Why protein needs rise in flares", P(
                "Inflammation, fever, and diarrhea increase protein breakdown. Surgery and steroid use add further demand.",
                "Under-eating protein slows healing and muscle recovery.",
                "Children and teens need extra attention to growth during active disease.",
            )),
            ("High-quality protein sources", P(
                "Eggs, fish, poultry, Greek yogurt, tofu, and smooth nut butters are frequent choices when tender textures are needed.",
                "Protein shakes or enteral supplements may help when solids are hard. Choose products your dietitian approves.",
                "Spread protein across meals instead of one large serving.",
            )),
            ("When appetite is poor", P(
                "Eat protein first at meals when fullness comes quickly.",
                "Small snacks every few hours beat forcing large plates.",
                "Anti-nausea strategies from your team may improve intake.",
            )),
            ("Renal and special considerations", P(
                "Kidney disease changes protein targets. Share all diagnoses with your dietitian.",
                "Short bowel and ostomy patients need individualized electrolyte and protein plans.",
                "High-protein fad diets are not automatic IBD care.",
            )),
            ("Tracking progress", P(
                "Monitor weight weekly during flares. Unintended loss triggers clinic outreach.",
                "Handgrip strength and energy are informal signs of recovery.",
                "Repeat albumin and prealbumin only as your clinician orders; trends matter.",
            )),
        ],
        "tips": ["Add an egg or yogurt to breakfast daily.", "Keep ready-to-drink supplements for bad appetite days.", "Log weight weekly during flares.", "Ask dietitian for gram targets personalized to you.", "Pair protein with gentle starches if fiber is limited."],
        "faq": [_f("Are protein powders safe in IBD?", "Many are, but choose low-sugar options and confirm with your team if lactose or additives bother you."),
                _f("How much protein do I need?", "Depends on weight, age, and activity. Dietitians calculate targets."),
                _f("Does extra protein reduce inflammation?", "It supports healing but does not replace medical anti-inflammatory treatment.")],
        "related": [("Foods during a Crohn's flare", "/guides/foods-to-eat-crohns-flare"), ("Chicken protein article", "/blog/chicken-protein-ibd"),
                    ("What should I eat with IBD?", "/guides/what-should-i-eat-crohns-colitis"), ("Iron deficiency guide", "/guides/iron-deficiency-nutrition-ibd"),
                    ("High-protein meal plan article", "/blog/protein-meal-plan-ibd-remission"), ("Track symptoms and food", "/guides/track-ibd-symptoms-food")],
    }

    TOPICS["elimination-diet-when-to-stop-ibd"] = {
        "intro": "Elimination diets remove foods to test tolerance, but long unsupervised restriction harms nutrition and mental health in IBD. Knowing when to stop is as important as when to start. This guide outlines warning signs patients discuss with clinicians. Education only.",
        "sections": [
            ("Purpose of short elimination trials", P(
                "Supervised trials may clarify lactose, FODMAP, or other irritant patterns when inflammation is controlled.",
                "Trials should have start dates, end dates, and reintroduction schedules.",
                "Elimination cannot diagnose IBD itself; endoscopy and labs do.",
            )),
            ("Red flags to stop immediately", P(
                "Unintended weight loss, fainting, menstrual loss, or child growth faltering need urgent clinician review.",
                "Fear of eating, social isolation, or obsessive logging suggest psychological harm.",
                "Worsening inflammation on labs while restricting foods means medical treatment, not more elimination.",
            )),
            ("Nutrient gaps to watch", P(
                "Cutting dairy, gluten, and multiple food groups simultaneously risks calcium, iron, and B vitamin deficits.",
                "Supplements do not replace diverse food when restrictions are broad.",
                "Dietitians monitor labs during trials.",
            )),
            ("Healthy reintroduction", P(
                "Add one food group every few days with logs. Celebrate expanded variety.",
                "Some foods fail once but work months later after healing.",
                "Texture changes, such as cooked versus raw, alter results.",
            )),
            ("Partnering with your GI team", P(
                "Share social media diet lists for clinician review before starting.",
                "Ask whether calprotectin should be normal before trials.",
                "Mental health support helps when food anxiety persists after reintroduction.",
            )),
        ],
        "tips": ["Set a calendar end date before you start eliminating.", "Involve a dietitian for any multi-food removal.", "Weigh weekly during elimination.", "Stop if friends notice you avoiding all social meals.", "Treat flares medically before blaming foods."],
        "faq": [_f("How long should elimination last?", "Often two to six weeks for specific protocols, but only per your clinician or dietitian plan."),
                _f("Is carnivore diet safe for IBD?", "Extreme diets lack evidence and risk nutrient gaps. Discuss risks with your GI team."),
                _f("Can elimination cure inflammation?", "No. It may reduce irritant symptoms while inflammation needs medical care.")],
        "related": [("Crohn's food triggers", "/guides/crohns-food-triggers"), ("Gluten-free guide", "/guides/gluten-free-autoimmune-when"),
                    ("Autoimmune nutrition basics", "/guides/autoimmune-nutrition-basics"), ("Track symptoms and food", "/guides/track-ibd-symptoms-food"),
                    ("Autoimmune diet myths article", "/blog/autoimmune-diet-myths"), ("What should I eat with IBD?", "/guides/what-should-i-eat-crohns-colitis")],
    }

    TOPICS["autoimmune-nutrition-basics"] = {
        "intro": "IBD is autoimmune-related, and nutrition affects energy, bone health, and symptom comfort, but no universal autoimmune diet exists. This guide separates evidence-based habits from myths patients review with clinicians. Education only.",
        "sections": [
            ("Nutrition role versus immune treatment", P(
                "Medications that control inflammation remain cornerstone care. Food supports recovery and deficiencies.",
                "Autoimmune labels on wellness products are marketing, not diagnoses.",
                "Labs and scopes guide whether symptoms are inflammatory.",
            )),
            ("Patterns with modest evidence", P(
                "Mediterranean-style patterns, adequate omega-3 intake, and limiting ultra-processed foods align with general health guidance.",
                "Vitamin D repletion when deficient is commonly recommended in IBD clinics.",
                "Smoking cessation is one of the strongest lifestyle interventions for Crohn's disease.",
            )),
            ("Myths to question", P(
                "Carnivore, long-term juice cleanses, and unproven supplement stacks lack IBD-specific safety data.",
                "Food allergy panels without symptoms do not guide IBD nutrition.",
                "Social media cures rarely disclose medication use or surgical history.",
            )),
            ("Personalization and culture", P(
                "Respect cultural staples by modifying texture and spice rather than eliminating entire cuisines without cause.",
                "Pediatric growth trumps adult weight loss trends.",
                "Dietitians translate autoimmune education into practical family meals.",
            )),
            ("When to escalate care", P(
                "Rapid weight loss, persistent bleeding, or night stools need GI outreach, not more supplements.",
                "Mental health screening belongs in holistic autoimmune care.",
                "Clinical trials study nutrition therapies; ask your team about eligible studies.",
            )),
        ],
        "tips": ["Question diets that forbid all grains or all plants.", "Ask for labs before buying supplement stacks.", "Keep smoking cessation on your goal list if applicable.", "Log symptoms when trying any new protocol.", "Read autoimmune diet myths article on IBDPal."],
        "faq": [_f("Does gluten-free help all autoimmune disease?", "Only patients with celiac or documented gluten sensitivity benefit specifically."),
                _f("Are autoimmune protocols safe?", "Some are restrictive. Medical supervision prevents harm."),
                _f("Can probiotics treat IBD?", "Evidence is strain-specific. Ask your gastroenterologist.")],
        "related": [("Anti-inflammatory diet guide", "/guides/anti-inflammatory-diet-ibd"), ("Gluten-free guide", "/guides/gluten-free-autoimmune-when"),
                    ("Autoimmune diet myths article", "/blog/autoimmune-diet-myths"), ("Foundation complementary medicine", "/guides/foundation-complementary-medicine-ibd"),
                    ("What should I eat with IBD?", "/guides/what-should-i-eat-crohns-colitis"), ("Elimination diet guide", "/guides/elimination-diet-when-to-stop-ibd")],
    }

    TOPICS["gluten-free-autoimmune-when"] = {
        "intro": "Gluten-free diets are essential for celiac disease but are not required for every person with IBD or autoimmune conditions. This guide explains when testing and supervised trials make sense. Education only, not medical advice.",
        "sections": [
            ("Celiac versus IBD overlap", P(
                "Celiac disease is more common in IBD than in the general population. Screening may be recommended at diagnosis or with anemia.",
                "Celiac requires strict lifelong gluten avoidance and follow-up biopsies or serology.",
                "Non-celiac gluten sensitivity is debated and diagnosed by exclusion with clinician oversight.",
            )),
            ("When to test before going gluten free", P(
                "Serology and endoscopy need active gluten intake for accuracy. Do not stop gluten before testing unless your team instructs.",
                "Genetic tests alone do not diagnose celiac.",
                "IBD inflammation can affect villi; interpret results with gastroenterology.",
            )),
            ("Trial gluten-free diets safely", P(
                "Short supervised trials may help if celiac is ruled out and symptoms persist in remission.",
                "Replace wheat with fortified gluten-free grains to avoid fiber and iron gaps.",
                "Document stool, pain, and energy changes during trials.",
            )),
            ("Risks of unnecessary restriction", P(
                "Gluten-free packaged foods may be low in fiber and high in sugar.",
                "Social and cost burdens affect quality of life.",
                "Children should not be gluten free without clear medical indication.",
            )),
            ("Talking with your GI team", P(
                "Bring questions about chapati, bread, and cultural staples to dietitian visits.",
                "Ask whether symptoms correlate with gluten or with FODMAPs in wheat.",
                "Repeat celiac labs if exposure was uncertain during prior testing.",
            )),
        ],
        "tips": ["Get celiac blood tests before eliminating gluten.", "Choose fortified gluten-free grains when needed.", "Log symptoms during any trial.", "Separate celiac care from IBD care teams if both apply.", "Read celiac screening article on IBDPal."],
        "faq": [_f("Does ulcerative colitis require gluten free?", "Not routinely. Test for celiac when clinically indicated."),
                _f("Will gluten free put IBD in remission?", "Only if celiac or clear non-celiac sensitivity is documented."),
                _f("Are gluten sensitivity tests from labs reliable?", "Many non-standard panels lack validation. Use clinician-directed testing.")],
        "related": [("Celiac screening article", "/blog/celiac-ibd-screening"), ("Autoimmune nutrition basics", "/guides/autoimmune-nutrition-basics"),
                    ("Elimination diet guide", "/guides/elimination-diet-when-to-stop-ibd"), ("Chapati and roti article", "/blog/chapati-roti-ibd"),
                    ("What should I eat with IBD?", "/guides/what-should-i-eat-crohns-colitis"), ("Track symptoms and food", "/guides/track-ibd-symptoms-food")],
    }

    # Foundation getting-started and deep-dive guides
    TOPICS["what-is-ibd-foundation"] = {
        "body": "This page summarizes Crohn's and Colitis Foundation patient education on what inflammatory bowel disease is and how to use those materials with your clinician.",
        "sections": [
            ("IBD in plain language", P(
                "Inflammatory bowel disease includes Crohn's disease, ulcerative colitis, and sometimes IBD-unclassified. Chronic inflammation damages the digestive tract over time without treatment.",
                "Symptoms may include diarrhea, rectal bleeding, abdominal pain, weight loss, and fatigue. Some people have joint, skin, or eye involvement.",
                "IBD differs from irritable bowel syndrome, which does not cause the same inflammatory damage on scopes.",
            )),
            ("How diagnosis is made", P(
                "Gastroenterologists combine history, exam, stool tests, blood work, imaging, and endoscopy with biopsy.",
                "Disease location and behavior guide therapy. Ask your team to explain your classification in writing.",
                "Online education prepares questions; it does not replace testing.",
            )),
            ("Using Foundation pages with IBDPal", P(
                "Start with the Foundation What is IBD page as the authoritative source, then explore disease-specific pages.",
                "Log symptoms in IBDPal between visits so patterns are visible.",
                "Bring unfamiliar terms to clinic for clarification.",
            )),
            ("Treatment overview at patient level", P(
                "Goals include healing inflammation, preventing complications, and restoring quality of life.",
                "Medications range from anti-inflammatories to biologics. Surgery helps some patients.",
                "Nutrition, mental health, and vaccines are part of whole-person care.",
            )),
            ("Boundaries of patient education", P(
                "Foundation materials do not prescribe individual treatment. Your IBD clinician personalizes plans.",
                "The Foundation does not endorse IBDPal. Selected content is used under license.",
                "Call your clinic for red-flag symptoms rather than relying on websites alone.",
            )),
        ],
        "tips": ["Bookmark Foundation disease basics pages.", "Ask whether your disease is Crohn's, UC, or IBD-U.", "Note night stools and blood for your team.", "Explore newly diagnosed Foundation guide next.", "Save clinic after-hours numbers."],
        "faq": [_f("Is IBD contagious?", "No. It is not spread person to person."),
                _f("Can this page diagnose me?", "No. Only your clinician diagnoses after appropriate evaluation."),
                _f("Does Foundation endorse IBDPal?", "No. Content is licensed; endorsement does not occur.")],
        "related": [("Foundation: What is IBD", f"{F}/what-is-ibd"), ("What is Crohn's Foundation guide", "/guides/what-is-crohns-disease-foundation"),
                    ("What is UC Foundation guide", "/guides/what-is-ulcerative-colitis-foundation"), ("Newly diagnosed Foundation first week", "/guides/newly-diagnosed-foundation-first-week"),
                    ("Foundation resources hub", "/crohns-colitis-foundation-resources"), ("Newly diagnosed hub", "/newly-diagnosed")],
    }

    TOPICS["what-is-crohns-disease-foundation"] = {
        "body": "This page bridges Crohn's and Colitis Foundation education on Crohn's disease with IBDPal tools for logging and visit preparation.",
        "sections": [
            ("What Crohn's can affect", P(
                "Crohn's may involve any part of the gastrointestinal tract from mouth to anus, often in patches. Deep inflammation can lead to strictures or fistulas.",
                "Common symptoms include diarrhea, pain, fatigue, weight change, and perianal disease.",
                "Extraintestinal manifestations may affect joints, skin, and eyes.",
            )),
            ("Disease patterns clinicians track", P(
                "Location such as ileal, colonic, or ileocolonic disease shapes monitoring.",
                "Behavior includes inflammatory, stricturing, and penetrating phenotypes.",
                "Ask your GI team to explain your latest imaging and endoscopy in plain language.",
            )),
            ("Foundation Crohn's resources", P(
                "Read the Foundation What is Crohn's disease page as the primary source.",
                "Surgery, nutrition, and medication guides supplement basics.",
                "Youth and family materials exist for pediatric Crohn's.",
            )),
            ("Partnering with your care team", P(
                "Track stools, pain, and medications in IBDPal between visits.",
                "Do not use education pages for emergency triage.",
                "Report fever, severe pain, or obstruction symptoms promptly.",
            )),
            ("Education boundaries", P(
                "Foundation content is not individualized treatment advice.",
                "The Foundation does not endorse IBDPal.",
                "Second opinions are reasonable for complex Crohn's cases.",
            )),
        ],
        "tips": ["Ask disease location and behavior at visits.", "Bring one-week symptom summaries.", "Review Foundation surgery guide if operations are discussed.", "Log perianal symptoms without embarrassment.", "Explore Crohn's hub on IBDPal."],
        "faq": [_f("Can Crohn's be cured by diet?", "No. Nutrition matters but medical monitoring is essential."),
                _f("Will everyone need surgery?", "Not everyone. Many control disease with medications."),
                _f("Is Crohn's the same as UC?", "No. They are distinct IBD types with different patterns.")],
        "related": [("Foundation: What is Crohn's", f"{F}/what-is-crohns-disease"), ("What is IBD Foundation guide", "/guides/what-is-ibd-foundation"),
                    ("Crohn's disease hub", "/crohns-disease"), ("Foods during flares", "/guides/foods-to-eat-crohns-flare"),
                    ("Foundation surgery and ostomy", "/guides/foundation-ibd-surgery-ostomy"), ("Crohn's flare guide", "/guides/crohns-flare-what-to-do")],
    }

    TOPICS["what-is-ulcerative-colitis-foundation"] = {
        "body": "This page summarizes Foundation patient education on ulcerative colitis and how IBDPal supports symptom tracking between clinic visits.",
        "sections": [
            ("What ulcerative colitis involves", P(
                "UC causes continuous inflammation of the colon lining, starting at the rectum and extending variable distances.",
                "Symptoms often include bloody diarrhea, urgency, and cramping.",
                "Extent categories include proctitis, left-sided, and extensive colitis.",
            )),
            ("How UC differs from Crohn's", P(
                "UC is limited to the colon and affects the inner lining continuously, unlike patchy transmural Crohn's.",
                "Surgical cure of colon disease is possible for some UC patients, though pouch complications can occur.",
                "Your team explains which diagnosis fits your tests.",
            )),
            ("Foundation UC resources", P(
                "The Foundation What is ulcerative colitis page is the authoritative starting point.",
                "Medication, surgery, and cancer surveillance guides add depth.",
                "Bring questions from reading to gastroenterology visits.",
            )),
            ("Monitoring and cancer screening", P(
                "Long-standing colitis increases colorectal cancer risk. Surveillance colonoscopy schedules depend on duration and severity.",
                "Do not skip maintenance mesalamine or biologics without clinician input.",
                "Log blood and stool frequency during flares for triage.",
            )),
            ("Using IBDPal responsibly", P(
                "Symptom logs complement Foundation reading.",
                "Education does not replace emergency care for severe bleeding or pain.",
                "The Foundation does not endorse IBDPal.",
            )),
        ],
        "tips": ["Know your UC extent category.", "Track nocturnal stools separately.", "Review cancer surveillance guide with your GI.", "Ask about joint symptoms; they can link to IBD.", "Explore UC hub pages on IBDPal."],
        "faq": [_f("Is UC only diarrhea?", "Bleeding and urgency are common even with moderate stool counts."),
                _f("Can UC turn into Crohn's?", "Diagnoses can be reclassified if tests show Crohn's features."),
                _f("Does blood always mean emergency?", "Volume and dizziness matter. Call your team for guidance.")],
        "related": [("Foundation: What is UC", f"{F}/what-is-ulcerative-colitis"), ("UC flare management", "/guides/ulcerative-colitis-flare-management"),
                    ("UC diet foods", "/guides/ulcerative-colitis-diet-foods"), ("Colonoscopy surveillance guide", "/guides/foundation-ibd-colonoscopy-cancer-surveillance"),
                    ("What is IBD Foundation guide", "/guides/what-is-ibd-foundation"), ("Ulcerative colitis hub", "/ulcerative-colitis")],
    }

    TOPICS["foundation-ibd-appeal-letters"] = {
        "body": "This page explains how Crohn's and Colitis Foundation appeal letter templates support insurance denials for IBD medications and procedures, used with your prescriber.",
        "sections": [
            ("When appeals are needed", P(
                "Denials for biologics, infusions, imaging, or surgery often trigger formal appeals.",
                "Timelines are strict. Missing deadlines restarts the process.",
                "Foundation templates provide structure; your doctor personalizes medical facts.",
            )),
            ("Components of strong appeals", P(
                "Include diagnosis, prior therapies tried, objective labs, endoscopy findings, and harm risk if treatment delays.",
                "Patient impact statements add context but do not replace clinical evidence.",
                "Attach peer-reviewed references only when requested by insurers.",
            )),
            ("Levels of appeal", P(
                "Internal plan appeals, external independent review, and state insurance department complaints follow different rules.",
                "Keep copies of every submission and delivery confirmation.",
                "Clinic prior auth staff often lead; patients supply symptom logs.",
            )),
            ("Working with your GI office", P(
                "Sign medical release forms so staff can speak with payers.",
                "Provide IBDPal exports showing flare frequency during denials.",
                "Ask about bridge samples while appeals process.",
            )),
            ("After approval", P(
                "Confirm pharmacy benefit versus medical benefit routing for infusions.",
                "Set calendar reminders before reauthorization windows.",
                "Update appeal packets when switching jobs or insurers.",
            )),
        ],
        "tips": ["Fax appeals with confirmation pages.", "Highlight calprotectin or CRP trends.", "Include colonoscopy dates in packets.", "Never stop meds during appeals without advice.", "Review step therapy guide for context."],
        "faq": [_f("Can patients write appeals alone?", "Letters need clinician signatures and records. Templates help you participate."),
                _f("How many appeals are typical?", "Some plans need two or three levels. Persistence is common."),
                _f("Do appeals always win?", "No, but many succeed with complete documentation.")],
        "related": [("Prior authorization guide", "/guides/ibd-prior-authorization-foundation"), ("Step therapy guide", "/guides/step-therapy-safe-step-act-ibd"),
                    ("Foundation medication guide", "/guides/foundation-ibd-medication-guide"), ("Biologics overview", "/guides/biologics-crohns-colitis"),
                    ("Doctor visit prep", "/guides/crohns-doctor-visit-prep"), ("Foundation resources hub", "/crohns-colitis-foundation-resources")],
    }

    TOPICS["step-therapy-safe-step-act-ibd"] = {
        "body": "This page summarizes Foundation education on step therapy requirements and Safe Step Act reforms affecting access to IBD biologics.",
        "sections": [
            ("What step therapy means", P(
                "Insurers may require failing specific drugs before approving others.",
                "Rules vary by plan and state. Employer and Medicaid plans differ.",
                "Step therapy can delay optimal therapy if exemptions are not granted.",
            )),
            ("Safe Step Act overview", P(
                "Federal reforms aim to streamline exceptions when step therapy is inappropriate.",
                "State laws may offer additional patient protections.",
                "Foundation advocacy materials explain current rights without legal advice.",
            )),
            ("Exception and exemption requests", P(
                "Document prior failures, intolerances, and contraindications with chart notes.",
                "Harm predictions from delays strengthen cases.",
                "GI letters should cite specific plan criteria verbatim when possible.",
            )),
            ("Patient advocacy steps", P(
                "Call insurer case managers and take reference numbers.",
                "Involve employer HR for self-funded plans when appropriate.",
                "Legislators' offices sometimes help constituents with insurance barriers.",
            )),
            ("Clinical perspective", P(
                "Gastroenterologists choose drugs based on disease severity, location, and history, not only formulary order.",
                "Shared decision making includes discussing step therapy risks.",
                "Appeals and prior auth guides complement this topic.",
            )),
        ],
        "tips": ["Keep a medication history timeline handy.", "Ask clinic staff which steps your plan requires.", "Request written denial reasons.", "Explore copay assistance during delays.", "Log symptoms if treatment is postponed."],
        "faq": [_f("Does Safe Step Act ban step therapy?", "No. It improves exception processes; plans may still use step therapy."),
                _f("Can my doctor override instantly?", "Sometimes via peer-to-peer review, not always immediately."),
                _f("Do biosimilars count as steps?", "Plan language varies. Read your formulary.")],
        "related": [("Prior authorization guide", "/guides/ibd-prior-authorization-foundation"), ("Appeal letters guide", "/guides/foundation-ibd-appeal-letters"),
                    ("Biologics overview", "/guides/biologics-crohns-colitis"), ("Foundation medication guide", "/guides/foundation-ibd-medication-guide"),
                    ("Foundation resources hub", "/crohns-colitis-foundation-resources"), ("Doctor visit prep", "/guides/crohns-doctor-visit-prep")],
    }

    TOPICS["find-ccf-chapter-support-group"] = {
        "body": "This page helps you locate Crohn's and Colitis Foundation chapters and support groups near you using official Foundation locators and IBDPal community guides.",
        "sections": [
            ("Using the chapter locator", P(
                "Foundation websites list chapters by state and region with meeting calendars.",
                "Virtual meetings expanded access after the pandemic. Check hybrid options.",
                "Special interest groups may focus on parents, teens, or ostomy patients.",
            )),
            ("What chapter meetings offer", P(
                "Education speakers, walk events, advocacy training, and peer networking are common.",
                "Volunteers share practical insurance and school navigation tips from lived experience.",
                "Medical advice still comes from your personal GI team.",
            )),
            ("Starting if you are shy", P(
                "Attend as a listener first. Introduce yourself to moderators privately.",
                "Bring questions gathered from IBDPal guides.",
                "Follow up with one person contact rather than trying to meet everyone.",
            )),
            ("Beyond monthly meetings", P(
                "Foundation walks fundraise research and build community.",
                "Advocacy days connect patients with legislators on IBD policy.",
                "Camp Oasis and teen programs link to chapters seasonally.",
            )),
            ("Online safety", P(
                "Verify unofficial groups claiming Foundation affiliation.",
                "Protect privacy in public posts.",
                "Report dangerous treatment advice to moderators.",
            )),
        ],
        "tips": ["Search Foundation locator plus your city.", "Try one virtual meeting before traveling.", "Ask moderators about medical ground rules.", "Bring a friend for your first in-person event.", "Pair groups with clinic follow-up."],
        "faq": [_f("Are chapter meetings free?", "Most are; verify registration for special events."),
                _f("Can caregivers attend?", "Many groups welcome partners and parents."),
                _f("Do chapters provide medical care?", "No. They offer education and peer support.")],
        "related": [("Support groups overview", "/guides/crohns-colitis-support-groups"), ("IBD support near me", "/guides/ibd-support-near-me"),
                    ("Foundation emotional wellness", "/guides/foundation-emotional-wellness-ibd"), ("Camp Oasis guide", "/guides/camp-oasis-kids-ibd"),
                    ("Chapter finder on Foundation site", f"{F}/local-chapters"), ("Foundation resources hub", "/crohns-colitis-foundation-resources")],
    }

    TOPICS["foundation-emotional-wellness-ibd"] = {
        "body": "This page summarizes Crohn's and Colitis Foundation emotional wellness resources for coping with IBD-related stress, anxiety, and depression alongside medical care.",
        "sections": [
            ("Emotional impact of chronic IBD", P(
                "Diagnosis, flares, and treatments affect mood, body image, and relationships.",
                "Anxiety about bathrooms and needles is common and treatable.",
                "Mental health is part of whole-person IBD care, not a separate luxury.",
            )),
            ("Foundation wellness materials", P(
                "Foundation pages cover coping skills, family communication, and when to seek therapy.",
                "Use them with guidance from your GI and mental health professionals.",
                "Crisis resources differ from general wellness tips.",
            )),
            ("Skills and therapies that help", P(
                "Cognitive behavioral therapy, gut-directed hypnosis, and support groups show benefit in some studies.",
                "Medications for anxiety or depression may coexist with IBD drugs with coordination.",
                "Sleep, movement, and social connection support resilience.",
            )),
            ("Caregivers and partners", P(
                "Family burnout is real. Encourage loved ones to seek their own support.",
                "Open communication reduces conflict during flares.",
                "Partner guides on IBDPal complement Foundation reading.",
            )),
            ("When to escalate care", P(
                "Suicidal thoughts, panic attacks, or eating disorders need urgent professional help.",
                "Use crisis lines and emergency services as appropriate.",
                "Tell your GI if mood affects medication adherence.",
            )),
        ],
        "tips": ["Ask your clinic about GI psychology referrals.", "Schedule worry time instead of all-day rumination.", "Limit unmoderated forum scrolling before bed.", "Celebrate small functional wins weekly.", "Share Foundation pages with family."],
        "faq": [_f("Is depression normal with IBD?", "It is common and treatable. Tell your care team."),
                _f("Can therapy reduce flares?", "It may improve coping and adherence; medical treatment still matters."),
                _f("Does Foundation provide therapy?", "It provides education, not licensed counseling sessions.")],
        "related": [("Stress and anxiety guide", "/guides/stress-anxiety-ibd"), ("Partner and caregiver guide", "/guides/partner-caregiver-ibd"),
                    ("Sleep during flares", "/guides/sleep-ibd-flares"), ("Bathroom urgency anxiety article", "/blog/bathroom-urgency-anxiety-ibd"),
                    ("Foundation resources hub", "/crohns-colitis-foundation-resources"), ("IBD helpline guide", "/guides/ibd-crohns-colitis-helpline")],
    }

    TOPICS["newly-diagnosed-foundation-first-week"] = {
        "body": "This page outlines a first-week roadmap using Crohn's and Colitis Foundation newly diagnosed materials alongside IBDPal logging tools.",
        "sections": [
            ("Day one: breathe and document", P(
                "Write down your diagnosis terms, medications, and follow-up dates.",
                "Save clinic after-hours numbers in your phone.",
                "Read Foundation what is IBD pages at your own pace.",
            )),
            ("Days two to three: build support", P(
                "Tell trusted friends or family what you need: rides, meals, or quiet.",
                "Explore chapter or virtual support if ready.",
                "Start a simple symptom log, even one line per day.",
            )),
            ("Days four to five: organize care", P(
                "Activate patient portal accounts and pharmacy apps.",
                "List questions for your next nurse call.",
                "Review vaccine records with your team.",
            )),
            ("Days six to seven: daily life planning", P(
                "Consider school or work disclosure needs with HR or disability offices.",
                "Pack a small flare kit for outings.",
                "Schedule mental health check-in if mood is low.",
            )),
            ("Beyond week one", P(
                "Colonoscopy prep, biologic education, and nutrition visits unfold over months.",
                "Foundation hubs and IBDPal guides deepen topics as they arise.",
                "Progress is nonlinear. Flares do not erase learning.",
            )),
        ],
        "tips": ["Create a dedicated email folder for IBD paperwork.", "Photograph insurance cards front and back.", "Ask for written flare instructions.", "Bookmark Foundation newly diagnosed hub.", "Explore /newly-diagnosed on IBDPal."],
        "faq": [_f("Should I read everything at once?", "No. Pace yourself to avoid overwhelm."),
                _f("Can I work during week one?", "Many do. Rest when symptoms require."),
                _f("Is it normal to grieve?", "Yes. Counseling and groups help.")],
        "related": [("Newly diagnosed guide", "/guides/newly-diagnosed-crohns-colitis"), ("What is IBD Foundation guide", "/guides/what-is-ibd-foundation"),
                    ("First GI appointment", "/guides/first-gastroenterology-appointment-ibd"), ("Visit prep checklist", "/visit-prep"),
                    ("Newly diagnosed hub", "/newly-diagnosed"), ("Find a chapter group", "/guides/find-ccf-chapter-support-group")],
    }

    TOPICS["pregnancy-ibd-foundation-resources"] = {
        "body": "This page summarizes Foundation education on pregnancy planning, fertility, and medication safety in IBD with links to coordinated OB and GI care.",
        "sections": [
            ("Preconception planning", P(
                "Ideally meet with GI and obstetrics before conceiving to optimize disease activity.",
                "Active inflammation may affect fertility and pregnancy outcomes.",
                "Fathers with IBD should also review medication questions with clinicians.",
            )),
            ("Medication continuity", P(
                "Many IBD drugs are preferred over uncontrolled flares during pregnancy.",
                "Never stop biologics or immunomodulators without coordinated specialist advice.",
                "Foundation medication guides discuss pregnancy categories at patient level.",
            )),
            ("Monitoring during pregnancy", P(
                "Disease monitoring may include symptom assessment, labs, and selective endoscopy when needed.",
                "Flares during pregnancy need prompt GI and OB outreach.",
                "Nutrition, iron, and vitamin D remain priorities.",
            )),
            ("Delivery and postpartum", P(
                "Most patients can vaginally deliver unless obstetric reasons dictate otherwise.",
                "Postpartum flares occur. Sleep loss and stress management plans help.",
                "Breastfeeding decisions include medication transfer discussions.",
            )),
            ("Emotional and social support", P(
                "Pregnancy with chronic illness brings unique anxiety. Therapy and peer groups help.",
                "Partners should attend key visits when possible.",
                "Foundation family resources complement OB education classes.",
            )),
        ],
        "tips": ["Schedule preconception GI visit months before trying.", "Bring medication list to every OB appointment.", "Plan postpartum flare support early.", "Continue folate and iron per clinician orders.", "Log symptoms in IBDPal during pregnancy."],
        "faq": [_f("Does IBD lower fertility?", "Active inflammation and some surgeries can affect fertility. Planning helps."),
                _f("Are all IBD drugs unsafe in pregnancy?", "No. Risk-benefit favors controlling disease in many cases."),
                _f("Can I breastfeed on biologics?", "Many options exist. Discuss specific drugs with your teams.")],
        "related": [("Foundation medication guide", "/guides/foundation-ibd-medication-guide"), ("Partner and caregiver guide", "/guides/partner-caregiver-ibd"),
                    ("Foundation emotional wellness", "/guides/foundation-emotional-wellness-ibd"), ("What is IBD Foundation guide", "/guides/what-is-ibd-foundation"),
                    ("Foundation resources hub", "/crohns-colitis-foundation-resources"), ("Doctor visit prep", "/guides/crohns-doctor-visit-prep")],
    }

    TOPICS["youth-school-foundation-resources"] = {
        "body": "This page bridges Foundation youth and school resources for students with IBD, including 504 plans, nurse coordination, and teen programs.",
        "sections": [
            ("School rights and documentation", P(
                "Section 504 and similar laws may grant restroom access, medication timing, and absence flexibility.",
                "Medical letters should be concise and updated yearly.",
                "School nurses store emergency medications with signed plans.",
            )),
            ("Talking with teachers and coaches", P(
                "Share only what is needed for safety and attendance.",
                "PE modifications and hydration breaks are common accommodations.",
                "Bullying about bathroom use should be reported immediately.",
            )),
            ("Teen independence", P(
                "Gradually shift refill and appointment responsibility to teens.",
                "Peer groups and Camp Oasis reduce isolation.",
                "Mental health screening matters during adolescence.",
            )),
            ("College transition", P(
                "Register with disability services before classes begin.",
                "Dorm mini-fridges may store biologics with documentation.",
                "IBDPal college articles supplement Foundation guides.",
            )),
            ("Parents and guardians", P(
                "Balance advocacy with growing autonomy.",
                "Sibling support prevents family stress from focusing only on IBD.",
                "Foundation family programs offer webinars and printouts.",
            )),
        ],
        "tips": ["Renew 504 letters each summer.", "Meet the school nurse before day one.", "Practice self-advocacy phrases with your child.", "Explore Camp Oasis when age-eligible.", "Read college with IBD article before applications."],
        "faq": [_f("Must schools allow unlimited bathroom breaks?", "Reasonable accommodations are required; documentation helps."),
                _f("Can teens self-carry injectables?", "Policies vary; nurse plans clarify."),
                _f("Should teachers know diagnosis details?", "Functional needs can be described without full medical history.")],
        "related": [("Pediatric IBD help", "/guides/pediatric-crohns-colitis-help"), ("Workplace and school rights", "/guides/ibd-workplace-school-rights"),
                    ("Foundation workplace school rights", "/guides/foundation-workplace-school-rights-ibd"), ("Camp Oasis guide", "/guides/camp-oasis-kids-ibd"),
                    ("College with IBD article", "/blog/college-with-ibd"), ("Foundation resources hub", "/crohns-colitis-foundation-resources")],
    }

    TOPICS["foundation-ibd-clinical-trials"] = {
        "body": "This page explains how Crohn's and Colitis Foundation clinical trials education helps patients explore research participation with their GI teams.",
        "sections": [
            ("Why trials matter", P(
                "Clinical trials advance new IBD therapies and monitoring tools.",
                "Participation is voluntary and regulated with informed consent.",
                "Standard care continues alongside many studies.",
            )),
            ("Finding appropriate trials", P(
                "Foundation trial finders and academic center websites list enrolling studies.",
                "Inclusion criteria depend on disease type, prior meds, and labs.",
                "Your gastroenterologist identifies ethically appropriate options.",
            )),
            ("Safety and informed consent", P(
                "Read consent forms carefully. Ask about placebo chances, visit burden, and costs.",
                "Report side effects promptly to study teams.",
                "You may withdraw without losing standard care.",
            )),
            ("Practical participation issues", P(
                "Travel, time off work, and childcare affect feasibility.",
                "Some studies cover costs; others do not.",
                "Document trial participation for future clinicians.",
            )),
            ("After trials end", P(
                "Extension studies or commercial access may be available.",
                "Maintain follow-up scopes and labs per your GI plan.",
                "Share outcomes with your regular IBD team.",
            )),
        ],
        "tips": ["Ask your GI about open trials at your center.", "Keep consent binders accessible.", "Log symptoms consistently during studies.", "Verify insurance interaction before enrolling.", "Explore Foundation trial finder online."],
        "faq": [_f("Will I get placebo?", "Some trials use placebo; consent explains odds and crossover options."),
                _f("Are trials only for severe disease?", "Studies target varied severity levels with specific criteria."),
                _f("Can trials replace my GI?", "No. Study teams coordinate with your clinicians.")],
        "related": [("Biologics overview", "/guides/biologics-crohns-colitis"), ("Foundation medication guide", "/guides/foundation-ibd-medication-guide"),
                    ("What is IBD Foundation guide", "/guides/what-is-ibd-foundation"), ("Doctor visit prep", "/guides/crohns-doctor-visit-prep"),
                    ("Foundation resources hub", "/crohns-colitis-foundation-resources"), ("Newly diagnosed guide", "/guides/newly-diagnosed-crohns-colitis")],
    }

    TOPICS["foundation-ibd-surgery-ostomy"] = {
        "body": "This page summarizes Foundation patient education on IBD-related surgery, ostomies, and recovery planning with links to surgical informed consent topics.",
        "sections": [
            ("When surgery is considered", P(
                "Medically refractory disease, complications like stricture or fistula, cancer dysplasia, or acute emergencies may lead to surgery.",
                "Decisions are shared between patient, surgeon, and gastroenterologist.",
                "Second opinions are reasonable for major operations.",
            )),
            ("Types of procedures", P(
                "Resections, strictureplasty, colectomy with pouch, and permanent ostomies vary by diagnosis.",
                "Minimally invasive approaches depend on anatomy and expertise.",
                "Temporary diverting ostomies may protect anastomoses.",
            )),
            ("Ostomy life and support", P(
                "WOC nurses teach appliance management and skin care.",
                "Many patients swim, work, and travel with ostomies.",
                "Peer ostomy groups complement Foundation materials.",
            )),
            ("Recovery and follow-up", P(
                "Nutrition, hydration, and physical therapy support healing.",
                "Watch for blockage signs with ileostomies: pain, no output, vomiting.",
                "Crohn's can recur after surgery; UC colon removal may be curative for colon disease.",
            )),
            ("Emotional preparation", P(
                "Grief and body image changes are normal. Counseling helps.",
                "Partners benefit from intimacy education resources.",
                "Bring questions to pre-op visits in writing.",
            )),
        ],
        "tips": ["Meet WOC nursing before surgery if possible.", "Order extra ostomy supplies pre-discharge.", "Know blockage red flags.", "Review Foundation intimacy guide with partner.", "Log output changes after surgery."],
        "faq": [_f("Is ostomy permanent?", "Some are temporary loops; others permanent depending on operation."),
                _f("Will I need a special diet forever?", "Diets evolve through recovery. Dietitians personalize."),
                _f("Does surgery mean I failed?", "No. Surgery is a valid tool in IBD care.")],
        "related": [("Living with an ostomy", "/guides/living-with-ostomy-ibd"), ("Foundation intimacy guide", "/guides/foundation-ibd-intimacy-sexual-health"),
                    ("What is UC Foundation guide", "/guides/what-is-ulcerative-colitis-foundation"), ("Pain and fatigue guide", "/guides/foundation-ibd-pain-fatigue"),
                    ("IBD hydration guide", "/guides/ibd-hydration-fluids"), ("Foundation resources hub", "/crohns-colitis-foundation-resources")],
    }

    TOPICS["foundation-workplace-school-rights-ibd"] = {
        "body": "This page summarizes Foundation education on workplace and school rights for people with IBD, including accommodations and disclosure choices.",
        "sections": [
            ("Legal frameworks overview", P(
                "In the United States, ADA and Section 504 may protect employees and students with IBD.",
                "Other countries have parallel laws. Foundation materials are educational, not legal advice.",
                "Documentation from clinicians supports accommodation requests.",
            )),
            ("Workplace accommodations", P(
                "Flexible scheduling, remote work, restroom access, and leave for infusions are common requests.",
                "FMLA or local leave laws may apply for flare recovery.",
                "HR offices process forms; clinicians complete medical sections.",
            )),
            ("School and university settings", P(
                "504 plans travel with students across grades when updated.",
                "College disability services require separate registration.",
                "Nurses can administer medications per action plans.",
            )),
            ("Disclosure strategies", P(
                "You control how much detail employers or professors receive.",
                "Functional language focuses on needs, not full charts.",
                "Retaliation for lawful accommodation requests may be unlawful depending on jurisdiction.",
            )),
            ("Advocacy resources", P(
                "Foundation toolkits provide sample letters and rights summaries.",
                "Employment attorneys help complex cases.",
                "Keep written records of requests and responses.",
            )),
        ],
        "tips": ["Renew accommodation letters yearly.", "Register college disability services early.", "Know your clinic fax for forms.", "Document denied requests in writing.", "Pair with IBDPal workplace guide."],
        "faq": [_f("Must I disclose IBD to employers?", "You may request accommodations with limited disclosure supported by clinician letters."),
                _f("Can schools refuse restroom access?", "Reasonable access should be provided with proper documentation."),
                _f("Does Foundation provide lawyers?", "No. It offers education; legal counsel is separate.")],
        "related": [("Workplace and school rights IBDPal guide", "/guides/ibd-workplace-school-rights"), ("Youth school Foundation resources", "/guides/youth-school-foundation-resources"),
                    ("College with IBD article", "/blog/college-with-ibd"), ("Living with an ostomy", "/guides/living-with-ostomy-ibd"),
                    ("Partner and caregiver guide", "/guides/partner-caregiver-ibd"), ("Foundation resources hub", "/crohns-colitis-foundation-resources")],
    }

    TOPICS["foundation-ibd-medication-guide"] = {
        "body": "This page bridges the Crohn's and Colitis Foundation Medication Guide with IBDPal visit prep and adherence tools for IBD therapies.",
        "sections": [
            ("How to use the Medication Guide", P(
                "Foundation guides describe drug classes, common side effects, and monitoring at patient reading level.",
                "They supplement, not replace, pharmacy labels and clinician instructions.",
                "Update your reading when switching therapies.",
            )),
            ("Major drug classes in IBD", P(
                "Aminosalicylates, corticosteroids, immunomodulators, biologics, and targeted small molecules each have roles depending on disease.",
                "Combination therapy and sequential therapy are individualized.",
                "Ask why a specific class fits your case.",
            )),
            ("Adherence and safety", P(
                "Missed doses increase flare risk. Use reminders and travel letters.",
                "Report infections, rashes, or neurologic symptoms promptly.",
                "Vaccines and travel vaccines need planning on immunosuppression.",
            )),
            ("Pregnancy, surgery, and interactions", P(
                "Coordinate medication lists across GI, OB, surgeons, and dentists.",
                "Some drugs require holding before operations.",
                "Over-the-counter NSAIDs may worsen IBD; ask before using.",
            )),
            ("Insurance and access", P(
                "Prior authorization and step therapy affect timing.",
                "Appeal resources support denials.",
                "Patient assistance programs help qualifying households.",
            )),
        ],
        "tips": ["Carry a wallet medication list.", "Review Foundation guide before starting new drugs.", "Ask pharmacists about interactions.", "Never stop steroids suddenly.", "Log infusion and injection dates in IBDPal."],
        "faq": [_f("Can I read the guide instead of talking to my doctor?", "No. It prepares questions; clinicians personalize treatment."),
                _f("Are generic drugs OK?", "Often yes. Discuss switches with your team if symptoms change."),
                _f("Do biologics weaken immunity?", "They modify immune pathways; infection monitoring matters.")],
        "related": [("Biologics overview", "/guides/biologics-crohns-colitis"), ("Prior authorization guide", "/guides/ibd-prior-authorization-foundation"),
                    ("Vaccines and infection guide", "/guides/foundation-ibd-vaccines-infection"), ("Pregnancy resources", "/guides/pregnancy-ibd-foundation-resources"),
                    ("Doctor visit prep", "/guides/crohns-doctor-visit-prep"), ("Foundation resources hub", "/crohns-colitis-foundation-resources")],
    }

    TOPICS["foundation-ibd-pain-fatigue"] = {
        "body": "This page summarizes Foundation education on pain and fatigue in IBD, distinguishing inflammatory symptoms from other causes with your clinician.",
        "sections": [
            ("Sources of pain in IBD", P(
                "Inflammation, strictures, abscesses, arthritis, and functional pain can coexist.",
                "Location and timing help clinicians differentiate causes.",
                "Do not assume all pain equals active colitis without evaluation.",
            )),
            ("Fatigue beyond feeling tired", P(
                "Anemia, poor sleep, medications, depression, and inflammation contribute to fatigue.",
                "Energy may lag even when stool frequency improves.",
                "Multidisciplinary assessment is common in IBD centers.",
            )),
            ("Self-management strategies", P(
                "Gentle activity, sleep hygiene, and pacing tasks help when clinicians approve.",
                "Pain teams, physical therapy, and psychology add tools beyond drugs alone.",
                "Nutrition repletion treats reversible fatigue causes.",
            )),
            ("Medication and procedural options", P(
                "Treating inflammation remains foundational.",
                "Analgesic choices must avoid NSAIDs that may worsen IBD unless clinicians agree.",
                "Nerve pain agents and referrals may help selected patients.",
            )),
            ("When to seek urgent care", P(
                "Severe abdominal pain with fever, rigid abdomen, or vomiting needs emergency evaluation.",
                "Sudden pain changes after surgery warrant immediate outreach.",
                "Chest pain or shortness of breath are not typical IBD pain alone.",
            )),
        ],
        "tips": ["Log pain location and relation to meals.", "Track sleep hours during fatigue spikes.", "Ask about anemia labs when exhausted.", "Avoid NSAIDs unless GI approves.", "Use pain-fatigue entries in visit prep."],
        "faq": [_f("Is fatigue normal in remission?", "It can persist. Investigate treatable causes with your team."),
                _f("Should I push through pain daily?", "Pacing helps; severe pain needs medical assessment."),
                _f("Do opioids treat IBD inflammation?", "They mask pain and may worsen gut function. Use only as directed.")],
        "related": [("Sleep during flares", "/guides/sleep-ibd-flares"), ("Stress and anxiety guide", "/guides/stress-anxiety-ibd"),
                    ("Iron deficiency guide", "/guides/iron-deficiency-nutrition-ibd"), ("Extraintestinal manifestations", "/guides/foundation-ibd-extraintestinal-manifestations"),
                    ("Crohn's flare guide", "/guides/crohns-flare-what-to-do"), ("Foundation emotional wellness", "/guides/foundation-emotional-wellness-ibd")],
    }

    TOPICS["foundation-ibd-extraintestinal-manifestations"] = {
        "body": "This page summarizes Foundation education on extraintestinal manifestations of IBD affecting joints, skin, eyes, and other organs beyond the bowel.",
        "sections": [
            ("Common extraintestinal manifestations", P(
                "Peripheral arthritis, axial spondyloarthritis, erythema nodosum, pyoderma gangrenosum, and uveitis appear in some patients.",
                "Symptoms may flare with bowel activity or sometimes independently.",
                "Tell your GI about joint pain, eye redness, or new rashes promptly.",
            )),
            ("Coordinated specialty care", P(
                "Rheumatology, dermatology, and ophthalmology may join your team.",
                "Some symptoms need urgent eye evaluation to protect vision.",
                "Medication choices may treat both bowel and joint disease.",
            )),
            ("Monitoring and labs", P(
                "Inflammatory markers do not always correlate with joint pain.",
                "Imaging of spine and sacroiliac joints may be ordered.",
                "Skin biopsies clarify diagnosis when appearance is unclear.",
            )),
            ("Patient reporting tips", P(
                "Photo rashes with dates for telehealth.",
                "Note morning stiffness duration in joints.",
                "Eye pain, light sensitivity, or blurred vision need same-day outreach.",
            )),
            ("Education boundaries", P(
                "Foundation pages describe patterns; your clinicians diagnose specific manifestations.",
                "Do not start immunosuppressants without specialist coordination.",
                "The Foundation does not endorse IBDPal.",
            )),
        ],
        "tips": ["Report eye symptoms immediately.", "Track joint pain separately from abdominal pain.", "Bring photos of skin changes to visits.", "Ask if biologics target your joint disease.", "Read ankylosing spondylitis article if referred."],
        "faq": [_f("Do all IBD patients get joint pain?", "No, but it is common enough to screen in clinic."),
                _f("Can skin issues scar?", "Some lesions like pyoderma gangrenosum need aggressive care."),
                _f("Should I see an optometrist or ophthalmologist?", "Red painful eyes need urgent ophthalmology, not routine glasses visits.")],
        "related": [("Ankylosing spondylitis article", "/blog/ankylosing-spondylitis-ibd"), ("Pain and fatigue guide", "/guides/foundation-ibd-pain-fatigue"),
                    ("What is Crohn's Foundation guide", "/guides/what-is-crohns-disease-foundation"), ("Biologics overview", "/guides/biologics-crohns-colitis"),
                    ("Doctor visit prep", "/guides/crohns-doctor-visit-prep"), ("Foundation resources hub", "/crohns-colitis-foundation-resources")],
    }

    TOPICS["foundation-complementary-medicine-ibd"] = {
        "body": "This page summarizes Foundation guidance on complementary and integrative approaches in IBD, emphasizing safety and coordination with gastroenterology care.",
        "sections": [
            ("Defining complementary approaches", P(
                "Herbs, probiotics, acupuncture, mindfulness, and dietary supplements fall under complementary integrative health.",
                "Evidence quality varies widely. Some approaches lack IBD-specific trials.",
                "Complementary does not mean harmless or interchangeable with prescribed drugs.",
            )),
            ("Discussing supplements with your GI team", P(
                "Bring bottles to visits. Interactions with immunosuppressants matter.",
                "Probiotics are strain-specific; general yogurt marketing oversimplifies.",
                "Turmeric, aloe, and wormwood products carry bleeding or liver risks.",
            )),
            ("Mind-body practices", P(
                "Meditation, yoga, and gut-directed hypnosis may improve symptom coping.",
                "They support but rarely replace anti-inflammatory treatment when scopes show active disease.",
                "Choose instructors aware of chronic illness limitations.",
            )),
            ("Red flags in alternative marketing", P(
                "Cures claiming to eliminate biologics are dangerous.",
                "Detox programs and colon cleanses can dehydrate and disrupt electrolytes.",
                "Testimonials omit medication and surgical histories.",
            )),
            ("Integrative care done well", P(
                "Academic centers sometimes offer integrative IBD clinics with coordinated oversight.",
                "Tell all practitioners you have IBD and list your drugs.",
                "Foundation materials stress open communication with your gastroenterologist.",
            )),
        ],
        "tips": ["Show supplement labels at every GI visit.", "Avoid colon cleanse products.", "Ask for evidence behind probiotic strains.", "Pair yoga with medical care, not instead of it.", "Report new herbs before surgery."],
        "faq": [_f("Are probiotics FDA approved for IBD?", "Most are not approved as drugs. Discuss specific products with your team."),
                _f("Can acupuncture treat inflammation?", "It may help symptoms; bowel inflammation still needs GI monitoring."),
                _f("Is CBD legal and safe?", "Regulation varies. Interactions and liver effects need clinician input.")],
        "related": [("Autoimmune nutrition basics", "/guides/autoimmune-nutrition-basics"), ("Anti-inflammatory diet guide", "/guides/anti-inflammatory-diet-ibd"),
                    ("Stress and anxiety guide", "/guides/stress-anxiety-ibd"), ("Foundation emotional wellness", "/guides/foundation-emotional-wellness-ibd"),
                    ("Elimination diet guide", "/guides/elimination-diet-when-to-stop-ibd"), ("Foundation resources hub", "/crohns-colitis-foundation-resources")],
    }

    TOPICS["foundation-ibd-travel-restroom-access"] = {
        "body": "This page summarizes Foundation travel and restroom access resources for people with IBD, including cards, apps, and legal context.",
        "sections": [
            ("Restroom access challenges", P(
                "Urgency can make locked retail restrooms risky. Planning routes reduces anxiety.",
                "Some regions have ally restroom laws or medical cards explaining needs.",
                "Foundation materials describe advocacy without guaranteeing access in every venue.",
            )),
            ("Travel preparation", P(
                "Airport security, biologic storage, and time zones affect medication timing.",
                "Carry clinician letters for injectables and medical liquids.",
                "Identify hospitals at destination for flare contingencies.",
            )),
            ("Apps and cards", P(
                "Restroom finder apps crowdsource locations. Download offline maps before travel.",
                "Foundation and advocacy cards can be shown discreetly to staff.",
                "Translate key phrases for international trips.",
            )),
            ("Flying and road trips", P(
                "Aisle seats near lavatories help on planes. Pre-board when offered.",
                "Road trips plan gas station chains with reliable facilities.",
                "Pack flare kits in carry-on luggage only.",
            )),
            ("If access is denied", P(
                "Stay calm and ask for managers. Know local laws when applicable.",
                "Prioritize health over confrontation when symptoms are urgent.",
                "Document incidents for advocacy organizations if safe to do so.",
            )),
        ],
        "tips": ["Download restroom apps before departure.", "Carry a clinician travel letter.", "Wear discreet medical alert if desired.", "Know TSA rules for liquids and syringes.", "Read IBDPal travel planning guide too."],
        "faq": [_f("Do restroom cards guarantee entry?", "They help explain needs but do not override all store policies."),
                _f("Can I use employee restrooms?", "Some laws require reasonable access; outcomes vary."),
                _f("Should I avoid travel with active flares?", "Discuss trip timing with your GI team.")],
        "related": [("Travel planning guide", "/guides/ibd-travel-planning"), ("Flare emergency supplies", "/guides/ibd-flare-emergency-supplies"),
                    ("Dining out with IBD", "/guides/dining-out-with-ibd"), ("Living with an ostomy", "/guides/living-with-ostomy-ibd"),
                    ("Biologics and travel article", "/blog/biologics-flying-travel-ibd"), ("Bathroom urgency anxiety article", "/blog/bathroom-urgency-anxiety-ibd")],
    }

    TOPICS["foundation-ibd-intimacy-sexual-health"] = {
        "body": "This page summarizes Foundation education on intimacy, sexual health, and body image for people with IBD and ostomies.",
        "sections": [
            ("Common concerns patients report", P(
                "Fatigue, pain, ostomy appliances, and medication side effects affect desire and function.",
                "Partners may fear causing harm. Open conversation reduces assumptions.",
                "Problems are common and worth mentioning to clinicians.",
            )),
            ("Talking with partners", P(
                "Choose low-stress moments for education about IBD and ostomies.",
                "Humor and patience help when experimenting with covers or positions.",
                "Counseling supports couples when communication stalls.",
            )),
            ("Medical evaluation", P(
                "GI, gynecology, urology, and pelvic floor therapists address specific issues.",
                "Some medications affect libido. Adjustments may be possible.",
                "Perianal disease needs specialized surgical input before certain activities.",
            )),
            ("Ostomy-specific tips", P(
                "Empty pouches beforehand. Soft bands and lingerie designed for ostomies improve confidence.",
                "Leak anxiety decreases with practice and proper fit.",
                "Intimacy includes non-intercourse closeness when needed.",
            )),
            ("Safety and boundaries", P(
                "Consent and pacing matter always. Stop if pain occurs.",
                "STI prevention still applies. Immunosuppression raises infection stakes.",
                "Foundation materials are educational, not therapy.",
            )),
        ],
        "tips": ["Bring intimacy questions to clinic visits.", "Empty ostomy pouches before closeness.", "Explore pelvic floor therapy if referred.", "Read partner caregiver guide together.", "Give yourself grace during flares."],
        "faq": [_f("Is sex safe with IBD?", "Often yes when disease and partners are considered; ask about perianal disease."),
                _f("Will partners notice ostomies?", "Planning and modern appliances reduce visibility."),
                _f("Should I avoid sex during flares?", "Comfort guides choices; medical clearance matters for some cases.")],
        "related": [("Living with an ostomy", "/guides/living-with-ostomy-ibd"), ("Partner and caregiver guide", "/guides/partner-caregiver-ibd"),
                    ("Foundation surgery and ostomy", "/guides/foundation-ibd-surgery-ostomy"), ("Stress and anxiety guide", "/guides/stress-anxiety-ibd"),
                    ("Foundation emotional wellness", "/guides/foundation-emotional-wellness-ibd"), ("Pregnancy resources", "/guides/pregnancy-ibd-foundation-resources")],
    }

    TOPICS["foundation-ibd-vaccines-infection"] = {
        "body": "This page summarizes Foundation guidance on vaccines and infection prevention for people with IBD, especially on immunosuppressive therapy.",
        "sections": [
            ("Why vaccines matter in IBD", P(
                "Immunosuppressants and active inflammation raise infection risks.",
                "Vaccines reduce preventable illnesses that could complicate IBD care.",
                "Plans should be individualized with your GI and primary care.",
            )),
            ("Live versus non-live vaccines", P(
                "Live vaccines may be avoided on some therapies. Timing before starting biologics matters.",
                "Inactivated vaccines such as influenza, pneumococcal, and COVID-19 are commonly recommended.",
                "Travel vaccines need advance planning with your team.",
            )),
            ("Screening for latent infections", P(
                "TB and hepatitis B screening often precedes biologics.",
                "Treat latent TB before starting certain drugs.",
                "Repeat screening may be needed when switching therapies.",
            )),
            ("Everyday infection prevention", P(
                "Hand hygiene, food safety while traveling, and prompt care for fever on immunosuppression are key.",
                "Report shingles, persistent cough, or unusual rashes early.",
                "Dental and surgical teams need your medication list.",
            )),
            ("Family and household considerations", P(
                "Household members may need certain vaccines to protect immunosuppressed patients.",
                "Discuss newborn and live vaccine exposure with obstetrics when relevant.",
                "Foundation pages list talking points for clinicians.",
            )),
        ],
        "tips": ["Keep a vaccine card photo on your phone.", "Ask about vaccines before starting biologics.", "Report fever on immunosuppression promptly.", "Plan travel vaccines months ahead.", "Coordinate flu shots with infusion schedules."],
        "faq": [_f("Can I get vaccines during a flare?", "Often yes for inactivated vaccines; timing is individualized."),
                _f("Are vaccines safe on biologics?", "Generally recommended; discuss specific vaccines with your GI."),
                _f("Should household members get flu shots?", "Often recommended to protect immunosuppressed patients.")],
        "related": [("Biologics overview", "/guides/biologics-crohns-colitis"), ("Foundation medication guide", "/guides/foundation-ibd-medication-guide"),
                    ("Travel planning guide", "/guides/ibd-travel-planning"), ("Clinical trials guide", "/guides/foundation-ibd-clinical-trials"),
                    ("Doctor visit prep", "/guides/crohns-doctor-visit-prep"), ("Foundation resources hub", "/crohns-colitis-foundation-resources")],
    }

    TOPICS["foundation-ibd-colonoscopy-cancer-surveillance"] = {
        "body": "This page summarizes Foundation education on colonoscopy surveillance and colorectal cancer risk in longstanding IBD, especially colonic disease.",
        "sections": [
            ("Why surveillance matters", P(
                "Chronic colitis increases colorectal cancer risk compared with the general population.",
                "Duration, extent, severity, and family history influence screening schedules.",
                "Surveillance colonoscopy with biopsies detects dysplasia early.",
            )),
            ("How schedules are set", P(
                "Gastroenterologists use disease duration, prior dysplasia, and PSC presence to set intervals.",
                "Do not skip scopes because you feel well. Inflammation may be silent.",
                "Bring prior pathology reports to new clinics.",
            )),
            ("Preparing for surveillance scopes", P(
                "Bowel prep must visualize the colon well. Poor prep delays diagnosis.",
                "Coordinate biologic timing and anticoagulants with your team.",
                "Sedation plans and escorts follow standard colonoscopy rules.",
            )),
            ("If dysplasia is found", P(
                "Management may include enhanced surveillance, endoscopic removal, or surgery depending on findings.",
                "Multidisciplinary IBD-dysplasia teams exist at referral centers.",
                "Questions about fertility and pouch function belong in those visits.",
            )),
            ("Primary prevention alongside surveillance", P(
                "Controlling inflammation pharmacologically reduces cancer risk.",
                "Smoking cessation helps UC and general cancer risk.",
                "Report new bleeding or change in symptoms between scopes.",
            )),
        ],
        "tips": ["Know your last scope date and next due date.", "Bring pathology reports to new GI clinics.", "Follow prep instructions exactly.", "Ask how PSC changes surveillance if applicable.", "Do not skip scopes during remission."],
        "faq": [_f("Do Crohn's colitis patients need surveillance?", "Colonic Crohn's involvement may warrant protocols similar to UC. Personalize with your GI."),
                _f("Is annual colonoscopy always required?", "Intervals vary from one to five years or more based on risk."),
                _f("Does mesalamine prevent cancer?", "Controlling inflammation matters; discuss chemoprevention studies with your team.")],
        "related": [("Colonoscopy prep article", "/blog/colonoscopy-prep-ibd"), ("What is UC Foundation guide", "/guides/what-is-ulcerative-colitis-foundation"),
                    ("Foundation medication guide", "/guides/foundation-ibd-medication-guide"), ("UC flare management", "/guides/ulcerative-colitis-flare-management"),
                    ("Doctor visit prep", "/guides/crohns-doctor-visit-prep"), ("Foundation resources hub", "/crohns-colitis-foundation-resources")],
    }
