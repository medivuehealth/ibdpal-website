"""Topics 3-30 for guide expansions."""
from __future__ import annotations

P = lambda *s: s

def add_part2(TOPICS):
    T = lambda intro, sections, tips, faq, related, body=None: TOPICS.update({}) or None  # noqa - use inline

    TOPICS["ulcerative-colitis-diet-foods"] = {
        "intro": "Ulcerative colitis affects the colon lining, so diet during flares often focuses on reducing bowel irritation while maintaining nutrition. No single food list works for everyone, but patterns below are common in UC patient education. Pair these ideas with your gastroenterologist or IBD dietitian for a plan that fits your disease extent and activity.",
        "sections": [
            ("UC flares and bowel-friendly choices", P(
                "During active colitis, many patients tolerate soft, low-fiber foods temporarily. White rice, plain pasta, eggs, applesauce, and well-cooked carrots are frequent examples in clinic handouts.",
                "Protein at each meal supports healing when appetite is reduced. Fish, tofu, and tender chicken are common choices if red meat feels heavy.",
                "Spicy foods, large salads, and high-fiber bran may increase urgency for some people. Reintroduce them gradually when symptoms improve with your team's guidance.",
            )),
            ("Blood, urgency, and hydration", P(
                "Visible blood and frequent stools increase fluid and electrolyte needs. Water plus oral rehydration solutions or broth may help when approved by your clinician.",
                "Track how many bowel movements occur daily and whether blood is increasing. These details help your GI team decide on medication changes.",
                "Caffeine and alcohol can worsen urgency for some patients. Ask whether temporary limits make sense during active symptoms.",
            )),
            ("Remission nutrition goals", P(
                "When inflammation is quiet, expanding variety supports long-term health. Cooked vegetables, fruits, whole grains, and legumes may be reintroduced stepwise.",
                "Iron, vitamin D, and calcium are common labs in UC because of bleeding, steroid use, or dietary gaps. Request monitoring at routine visits.",
                "A registered dietitian can help if you fear food, lose weight, or follow multiple restrictions. Early support prevents malnutrition.",
            )),
            ("Personal triggers and food logs", P(
                "UC triggers differ from Crohn's triggers and from person to person. A simple log linking meals to stool pattern, pain, and energy reveals patterns faster than memory alone.",
                "Introduce one new food every few days when expanding your diet. Note whether symptoms change within 24 to 48 hours.",
                "Do not eliminate entire food groups without clinician input. Over-restriction can harm growth in youth and energy in adults.",
            )),
            ("Medical care alongside diet", P(
                "Diet supports comfort but does not replace anti-inflammatory treatment when colitis is active. Contact your IBD team if symptoms worsen or new fever appears.",
                "Rescue plans, steroid courses, or biologic adjustments may be needed even when you eat carefully. Follow your written flare instructions.",
                "Bring food logs and symptom trends to appointments. Shared data leads to faster, safer treatment decisions.",
            )),
        ],
        "tips": ["Compare stool count and blood to your personal baseline, not someone else's.", "Keep bland backup meals ready for high-urgency days.", "Ask about iron and vitamin D labs after bleeding episodes.", "Reintroduce fiber slowly in remission with dietitian support.", "Call your GI team if you cannot keep fluids down for 24 hours."],
        "faq": [("Does milk cause UC flares?", "Lactose intolerance is common but separate from UC inflammation. Your team can guide testing and calcium sources."),
                ("Should all UC patients avoid fiber?", "Not always. Many lower fiber during flares and increase cooked fiber in remission with clinician guidance."),
                ("Can diet cure ulcerative colitis?", "No. Nutrition is one part of care. Medical treatment and monitoring remain essential.")],
        "related": [("UC flare management", "/guides/ulcerative-colitis-flare-management"), ("What should I eat with IBD?", "/guides/what-should-i-eat-crohns-colitis"),
                    ("Low-residue diet basics", "/guides/low-residue-diet-ibd"), ("Blood in stool article", "/blog/blood-in-stool-ibd-when-to-worry"),
                    ("Track symptoms and food", "/guides/track-ibd-symptoms-food"), ("Flare help hub", "/flare-help")],
    }

    TOPICS["crohns-disease-diet-nutrition"] = {
        "intro": "Crohn's disease can affect any part of the digestive tract, so nutrition needs vary by disease location, prior surgery, and activity level. This guide outlines common diet and nutrition topics patients review with their GI team. It is educational only and does not replace personalized medical or nutrition advice.",
        "sections": [
            ("How Crohn's location shapes nutrition", P(
                "Small bowel Crohn's may affect absorption of iron, B12, and fat-soluble vitamins. Colonic disease may present more with urgency and bleeding.",
                "Strictures and prior resections change texture needs. Your clinician may recommend modified fiber or enteral nutrition in specific situations.",
                "Pediatric Crohn's requires attention to growth. Parents should work closely with pediatric GI and dietitian teams on calories and micronutrients.",
            )),
            ("Flare versus remission eating", P(
                "During flares, softer and lower-residue foods are often easier to tolerate short term. During remission, many patients rebuild variety with clinician support.",
                "Exclusive enteral nutrition is a supervised therapy for some Crohn's patients, especially youth. It is not a DIY juice cleanse.",
                "Return toward a balanced pattern when symptoms improve rather than staying on a minimal diet out of fear.",
            )),
            ("Micronutrients and labs to discuss", P(
                "Iron deficiency, low vitamin D, low B12, zinc deficiency, and bone health are frequent discussion points in Crohn's clinics.",
                "Steroids, malabsorption, and chronic inflammation all influence labs. Annual or symptom-based testing may be appropriate.",
                "Supplements should match documented deficiencies. High-dose self-supplementation can mask problems or cause side effects.",
            )),
            ("Protein, calories, and healing", P(
                "Adequate protein supports tissue repair during and after flares. Spread intake across the day if appetite is low.",
                "Healthy fats and calorie-dense snacks help when weight loss is unintended. Nut butters, olive oil, and smoothies are common tools when tolerated.",
                "Tell your team if you skip meals regularly or fear eating. Early nutrition intervention prevents complications.",
            )),
            ("Partnering with your care team", P(
                "Bring a food and symptom log to visits. Note pain location, stool pattern, blood, and energy alongside meals.",
                "Ask for dietitian referral if you have strictures, short bowel, repeated hospitalizations, or complex restrictions.",
                "Online lists are starting points only. Your Crohn's phenotype and labs should guide real decisions.",
            )),
        ],
        "tips": ["Ask where your Crohn's is located and how that affects diet advice.", "Request iron, B12, and vitamin D labs at routine visits.", "Introduce new foods one at a time when expanding after flares.", "Keep oral rehydration supplies at home for diarrhea-heavy weeks.", "Use IBDPal or a paper log to show trends, not single bad days."],
        "faq": [("Is Crohn's diet the same as colitis diet?", "Patterns overlap, but location, surgery, and complications differ. Personalize with your IBD team."),
                ("Should I take probiotics for Crohn's?", "Evidence varies by product and patient. Ask your gastroenterologist before starting supplements."),
                ("Can diet replace biologics?", "No. Nutrition supports overall care but does not replace medical treatment for active inflammation.")],
        "related": [("Foods during a Crohn's flare", "/guides/foods-to-eat-crohns-flare"), ("Protein and healing in flares", "/guides/protein-healing-ibd-flare"),
                    ("Iron deficiency nutrition", "/guides/iron-deficiency-nutrition-ibd"), ("What is Crohn's? Foundation basics", "/guides/what-is-crohns-disease-foundation"),
                    ("Complete nutrition article", "/blog/complete-ibd-nutrition-guide"), ("Crohn's disease hub", "/crohns-disease")],
    }

    TOPICS["low-residue-diet-ibd"] = {
        "intro": "A low-residue or low-fiber diet reduces undigested material moving through the bowel. Some IBD patients use it short term during symptoms or before procedures, always with clinician guidance. This guide explains common principles and limits. It is not a long-term plan unless your GI team recommends one.",
        "sections": [
            ("What low-residue means in practice", P(
                "Low-residue eating limits high-fiber foods such as whole grains, nuts, seeds, raw vegetables, and tough fruit skins. The goal is less bulk and slower transit when the bowel is irritated.",
                "Cooking, peeling, and pureeing foods can lower residue without eliminating nutrition entirely. Well-cooked carrots, potatoes without skin, and refined grains are typical examples.",
                "Duration matters. Many patients use this pattern for days to weeks, then expand under supervision. Staying low-residue indefinitely can reduce micronutrient intake.",
            )),
            ("When clinicians suggest it", P(
                "Active diarrhea, pre-colonoscopy prep windows, strictures, or post-operative phases are common reasons a team may suggest temporary low-residue choices.",
                "It does not treat inflammation itself. Medication adjustments, imaging, or labs may still be needed during flares.",
                "Ask your clinician how long to stay low-residue and how to reintroduce fiber safely afterward.",
            )),
            ("Foods often included and avoided", P(
                "Included examples: white bread, white rice, plain pasta, eggs, tender meat, canned fruit without skins, smooth peanut butter, and well-cooked vegetables without seeds.",
                "Often limited: popcorn, corn, berries with seeds, cruciferous vegetables, legumes, whole nuts, and bran cereals.",
                "Personal tolerance still rules. A food on an avoid list may be fine for you in small amounts, or a safe food may trigger symptoms.",
            )),
            ("Nutrition pitfalls to avoid", P(
                "Low-residue does not mean low protein or low calories. Maintain adequate intake for healing, especially during flares.",
                "Calcium, fiber for colon health in remission, and fermented foods may be deferred temporarily but should be planned back in with your team.",
                "Children and teens need growth-focused plans. Do not impose adult low-residue lists without pediatric GI input.",
            )),
            ("Transitioning back to regular eating", P(
                "Reintroduce fiber gradually: cooked vegetables first, then whole grains and raw produce as tolerated.",
                "Log symptoms as you expand. One new food every few days clarifies triggers versus coincidence.",
                "Pair dietary changes with medical follow-up. Symptom relief from low-residue eating does not always mean inflammation resolved.",
            )),
        ],
        "tips": ["Clarify with your GI team how long low-residue should last.", "Peel and cook produce to reduce residue while keeping some nutrients.", "Do not skip protein during low-residue phases.", "Plan a fiber reintroduction schedule with your clinician.", "Use low-residue as a tool, not an identity."],
        "faq": [("Is low-residue the same as low-FODMAP?", "No. They target different mechanisms. Some foods overlap, but the plans serve different goals and need clinician context."),
                ("Can I eat salad on low-residue?", "Large raw salads are usually limited. Small amounts of well-cooked greens may be acceptable depending on your situation."),
                ("Will low-residue put me in remission?", "It may ease symptoms temporarily but does not replace anti-inflammatory treatment for active IBD.")],
        "related": [("Foods during a Crohn's flare", "/guides/foods-to-eat-crohns-flare"), ("UC diet foods guide", "/guides/ulcerative-colitis-diet-foods"),
                    ("Colonoscopy prep article", "/blog/colonoscopy-prep-ibd"), ("What should I eat with IBD?", "/guides/what-should-i-eat-crohns-colitis"),
                    ("Foundation diet and nutrition", "/guides/foundation-diet-nutrition-ibd")],
    }

    TOPICS["ibd-hydration-fluids"] = {
        "intro": "Dehydration is a common concern in IBD when diarrhea, vomiting, fever, or poor intake increase fluid losses. Hydration supports energy, kidney function, and electrolyte balance. This guide covers practical fluid strategies patients discuss with their GI team. It does not replace medical assessment for severe dehydration.",
        "sections": [
            ("Why IBD raises fluid needs", P(
                "Frequent stools, ostomy output, night sweats, and vomiting all increase water and electrolyte losses. Fever adds further demand.",
                "Some medications and hot weather amplify risk. Travel, exercise, and illness stacks burdens quickly.",
                "Thirst alone is a late signal. Track urine color, dizziness, heart rate, and intake patterns during symptomatic weeks.",
            )),
            ("What to drink and when", P(
                "Water is the base, but diarrhea often needs sodium and potassium replacement. Oral rehydration solutions, broth, or clinician-approved electrolyte drinks may help.",
                "Sip steadily through the day. Large gulps may worsen nausea. Ice chips and popsicles count toward intake when solids are hard.",
                "Limit alcohol and excess caffeine if they worsen urgency or sleep. Herbal teas without strong laxative herbs are often better tolerated.",
            )),
            ("Signs to contact your care team", P(
                "Very dark urine, dizziness on standing, rapid heartbeat, confusion, or inability to keep fluids down for 24 hours need prompt outreach.",
                "Bloody diarrhea with lightheadedness may require urgent evaluation. Follow your clinic's red-flag instructions.",
                "Infants, children, and older adults dehydrate faster. Caregivers should call pediatric or adult GI teams early.",
            )),
            ("Hydration with ostomies and surgery", P(
                "High ostomy output increases sodium needs. Your team may recommend specific electrolyte strategies or labs.",
                "After bowel surgery, absorption patterns change. Follow surgeon and GI guidance on fluids and salts.",
                "Weighing yourself at the same time daily can reveal fluid loss trends when stool counts are hard to measure.",
            )),
            ("Everyday habits that help", P(
                "Carry a bottle and set phone reminders if you forget to drink. Pair fluids with meals and medications unless told otherwise.",
                "During flares, reduce intense exercise until intake stabilizes. Resume gradually with your team's OK.",
                "Discuss sports drinks, coconut water, and homemade oral rehydration recipes with your clinician to avoid too much sugar or too little sodium.",
            )),
        ],
        "tips": ["Keep oral rehydration packets in your bag and at home.", "Track intake and stool count during bad weeks.", "Ask your team about sodium needs with high ostomy output.", "Avoid chugging large volumes if nauseated.", "Seek urgent care if you cannot retain fluids."],
        "faq": [("Is water enough during diarrhea?", "Often not. Electrolytes lost in stool may need replacement. Ask your GI team what products are appropriate."),
                ("Do sports drinks help IBD flares?", "Some help short term, but sugar content and sodium levels vary. Clinician guidance prevents wrong balance."),
                ("When is dehydration an emergency?", "Confusion, fainting, very low urine output, or persistent vomiting with dizziness warrant urgent evaluation.")],
        "related": [("Crohn's flare: what to do", "/guides/crohns-flare-what-to-do"), ("Flare emergency supplies", "/guides/ibd-flare-emergency-supplies"),
                    ("Foods during a flare", "/guides/foods-to-eat-crohns-flare"), ("Living with an ostomy", "/guides/living-with-ostomy-ibd"),
                    ("Flare help hub", "/flare-help"), ("Chronic diarrhea causes article", "/blog/chronic-diarrhea-ibd-causes")],
    }

    TOPICS["crohns-colitis-support-groups"] = {
        "intro": "Living with Crohn's disease or ulcerative colitis can feel isolating. Support groups connect you with peers who understand flares, medications, work stress, and relationship challenges. This guide explains types of IBD support and how to find groups safely. Education only, not a substitute for medical care.",
        "sections": [
            ("Types of IBD peer support", P(
                "In-person chapter meetings, virtual groups, teen and parent groups, and condition-specific communities each serve different needs.",
                "Some groups are facilitated by health professionals; others are peer-led. Ask how meetings are moderated and what privacy rules apply.",
                "Online forums offer 24/7 access but vary in quality. Prefer spaces with clear community guidelines and referral to clinicians for medical decisions.",
            )),
            ("Benefits many patients report", P(
                "Sharing practical tips on clinic navigation, insurance, and daily coping can reduce anxiety. Hearing remission stories may restore hope.",
                "Caregivers and partners benefit from separate groups focused on their role. Family attendance at patient groups should follow each group's norms.",
                "Support complements medical care. Peers cannot diagnose, prescribe, or replace your gastroenterologist.",
            )),
            ("Finding reputable groups", P(
                "The Crohn's and Colitis Foundation chapters list local meetings and events. Hospitals and academic centers sometimes host IBD networks.",
                "Ask your GI clinic if they recommend local groups or social workers who facilitate connections.",
                "Camp Oasis and youth programs serve children and teens with IBD. Parents should review medical supervision policies.",
            )),
            ("Safety and boundaries online", P(
                "Avoid sharing personal identifiers publicly. Be cautious with treatment advice from strangers.",
                "Report misinformation politely or leave groups that encourage stopping prescribed medications without medical oversight.",
                "Crisis support belongs to licensed helplines and your care team, not general chat rooms.",
            )),
            ("Starting when you feel ready", P(
                "You can listen without sharing at first meetings. Many people attend only during newly diagnosed or flare seasons.",
                "If a group feels negative or overwhelming, try another format. Fit matters more than loyalty to one community.",
                "Bring questions from support back to your clinician. Peer experience informs; your team personalizes.",
            )),
        ],
        "tips": ["Try one virtual and one in-person option before deciding.", "Ask moderators how medical misinformation is handled.", "Bring a friend or partner to your first meeting if allowed.", "Use IBDPal logs to share concrete trends with peers and clinicians.", "Check Foundation chapter listings for local events."],
        "faq": [("Are online IBD groups safe?", "Many are helpful with clear rules. Protect privacy and verify medical advice with your GI team."),
                ("Can support groups replace therapy?", "No. They complement mental health care but are not licensed counseling."),
                ("Do I have to share my story?", "No. Listening is a valid way to participate.")],
        "related": [("Find a Foundation chapter group", "/guides/find-ccf-chapter-support-group"), ("IBD support near me", "/guides/ibd-support-near-me"),
                    ("Foundation emotional wellness", "/guides/foundation-emotional-wellness-ibd"), ("Stress and anxiety with IBD", "/guides/stress-anxiety-ibd"),
                    ("Camp Oasis for kids", "/guides/camp-oasis-kids-ibd"), ("IBD helpline resources", "/guides/ibd-crohns-colitis-helpline")],
    }

    TOPICS["ibd-support-near-me"] = {
        "intro": "Finding IBD support close to home can improve coping, practical knowledge, and sense of community. This guide helps you search local chapters, hospital programs, and vetted online options. Always verify that peer advice aligns with guidance from your gastroenterologist or IBD center.",
        "sections": [
            ("Start with your IBD clinic", P(
                "Ask nurses, social workers, or patient navigators if the practice hosts groups or partners with local chapters.",
                "Academic IBD centers often list community events, education nights, and mentor programs on their websites.",
                "Bring a one-page summary of what you need: newly diagnosed support, parenting a child with IBD, or ostomy peers.",
            )),
            ("Foundation chapters and events", P(
                "The Crohn's and Colitis Foundation maintains chapter locators with meetings, walks, and advocacy events.",
                "Chapter volunteers understand insurance appeals, school forms, and local provider networks from lived experience.",
                "Virtual chapter meetings expand access if driving or symptoms limit attendance.",
            )),
            ("Hospital and nonprofit resources", P(
                "Children's hospitals may offer teen IBD groups and family education days. Adult hospitals sometimes partner with ostomy associations.",
                "Faith communities, community centers, and rare-disease coalitions occasionally host IBD speakers. Check event medical disclaimers.",
                "Libraries and patient education departments may keep printed resource lists updated yearly.",
            )),
            ("Evaluating online local groups", P(
                "Search social platforms for city plus IBD or ostomy keywords, then review group rules and admin activity.",
                "Prefer groups that redirect medical questions to clinicians and discourage dangerous home remedies.",
                "Protect your address, employer details, and children's identities in public posts.",
            )),
            ("When professional support fits better", P(
                "Severe anxiety, depression, trauma, or eating disorders need licensed mental health care, not only peer groups.",
                "GI psychologists and social workers specialize in coping with chronic illness. Ask your clinic for referrals.",
                "Crisis lines and emergency services remain the right path for suicidal thoughts or medical emergencies.",
            )),
        ],
        "tips": ["Search Foundation chapter locator plus your ZIP code.", "Ask your GI office for a social work referral.", "Try a virtual meeting if travel is hard during flares.", "Visit one session before committing long term.", "Pair peer support with clinic follow-up, not instead of it."],
        "faq": [("How do I find pediatric IBD support?", "Children's hospitals, Camp Oasis, and Foundation family programs are common starting points."),
                ("Are ostomy groups separate from IBD groups?", "Often yes, though overlap exists. Both can be valuable depending on your needs."),
                ("What if no local group exists?", "Virtual Foundation meetings and moderated online communities can fill gaps.")],
        "related": [("Crohn's and colitis support groups overview", "/guides/crohns-colitis-support-groups"), ("Find a Foundation chapter", "/guides/find-ccf-chapter-support-group"),
                    ("Pediatric IBD help", "/guides/pediatric-crohns-colitis-help"), ("Partner and caregiver guide", "/guides/partner-caregiver-ibd"),
                    ("Foundation resources hub", "/crohns-colitis-foundation-resources")],
    }

    TOPICS["pediatric-crohns-colitis-help"] = {
        "intro": "When a child or teen has Crohn's disease or ulcerative colitis, families juggle growth, school, emotions, and complex treatment plans. This guide highlights education topics parents discuss with pediatric GI teams. It does not replace individualized pediatric medical advice.",
        "sections": [
            ("Pediatric IBD differs from adult care", P(
                "Growth, puberty, bone density, and vaccine schedules need special attention. Pediatric gastroenterologists monitor height, weight, and development at each visit.",
                "Exclusive enteral nutrition and specific biologic pathways are more common in pediatric Crohn's than in many adult practices.",
                "Parents should receive written flare plans, school forms, and emergency contacts from the care team.",
            )),
            ("School, activities, and social life", P(
                "504 plans or equivalent accommodations may cover restroom access, medication timing, and make-up work after absences.",
                "Coaches, teachers, and school nurses benefit from concise medical letters without oversharing private details.",
                "Camp Oasis and teen groups help young patients meet peers who understand IBD. Review medical supervision policies before enrolling.",
            )),
            ("Nutrition and growth at home", P(
                "Avoid restrictive diets without dietitian and GI approval. Children need adequate calories for growth even during symptoms.",
                "Track appetite, stool pattern, and energy alongside meals. Bring logs to clinic visits.",
                "Iron, vitamin D, and zinc deficiencies are common discussion points in pediatric labs.",
            )),
            ("Emotional health for child and family", P(
                "Anxiety about bathrooms, body image, and injections is normal. Child psychologists familiar with chronic illness can help.",
                "Siblings may need their own support. Family meetings with social workers can improve communication.",
                "Watch for signs of depression, eating disorders, or medication avoidance. Report concerns early.",
            )),
            ("Building a durable care partnership", P(
                "Transition planning to adult GI should start in adolescence. Teens gradually take ownership of appointments and refills.",
                "Keep a shared calendar for infusions, labs, and scopes. Missing monitoring delays catches complications.",
                "Use reputable Foundation and hospital education rather than unmoderated social media for treatment decisions.",
            )),
        ],
        "tips": ["Request a written school accommodation letter each year.", "Keep a pediatric flare kit at school and home.", "Log growth metrics and symptoms between visits.", "Explore Camp Oasis and teen support when age-appropriate.", "Ask when transition to adult GI should begin."],
        "faq": [("Can my child play sports with IBD?", "Many do with clinician clearance. Plan hydration, restroom access, and recovery after flares."),
                ("Should kids follow adult diet blogs?", "No. Pediatric plans must protect growth. Work with pediatric GI and dietitian teams."),
                ("How do we handle injections at school?", "Coordinate with school nurse and your team's medication action plan.")],
        "related": [("Youth and school Foundation resources", "/guides/youth-school-foundation-resources"), ("Camp Oasis guide", "/guides/camp-oasis-kids-ibd"),
                    ("Newly diagnosed guide", "/guides/newly-diagnosed-crohns-colitis"), ("Track symptoms and food", "/guides/track-ibd-symptoms-food"),
                    ("College with IBD article", "/blog/college-with-ibd"), ("Newly diagnosed hub", "/newly-diagnosed")],
    }

    TOPICS["newly-diagnosed-crohns-colitis"] = {
        "intro": "A new Crohn's or colitis diagnosis brings tests, new vocabulary, and uncertainty about daily life. This guide outlines first steps many patients take with their GI team in the early weeks. Education only, not medical advice or a treatment plan.",
        "sections": [
            ("Understanding your diagnosis", P(
                "IBD includes Crohn's disease, ulcerative colitis, and sometimes IBD-unclassified. Location, severity, and extraintestinal features shape your roadmap.",
                "Colonoscopy, imaging, stool tests, and blood work help classify disease. Keep copies of pathology and imaging reports.",
                "Write down words you do not know and ask at your next visit. Good clinicians welcome questions.",
            )),
            ("Building your care team", P(
                "Gastroenterologist, nurse, dietitian, pharmacist, and mental health support each play roles. Ask who to call for flares versus routine refills.",
                "Save infusion center, after-hours, and portal messaging instructions in your phone.",
                "Second opinions are reasonable for complex cases. Bring records digitally when possible.",
            )),
            ("Daily life in the first months", P(
                "Start simple symptom and food logs. Patterns help faster than guessing triggers.",
                "Learn your clinic's red-flag symptoms: fever, severe pain, persistent bleeding, dehydration, or new joint or eye issues.",
                "Tell employers or school nurses only what you need for accommodations. You control disclosure.",
            )),
            ("Medications and follow-up", P(
                "Many treatment plans include anti-inflammatory drugs, immunomodulators, or biologics. Ask about monitoring labs and infection prevention.",
                "Take medications as prescribed unless your team says otherwise. Stopping suddenly can cause rebound inflammation.",
                "Vaccine updates and travel planning become ongoing topics. Request a medication list card for emergencies.",
            )),
            ("Emotional adjustment and support", P(
                "Grief, anger, and fear are common after diagnosis. Peer groups and counseling can help alongside medical care.",
                "Partners and parents need education too. Share Foundation and IBDPal guides rather than carrying everything alone.",
                "Progress is rarely linear. Celebrate small wins like completed labs or returned energy.",
            )),
        ],
        "tips": ["Create a binder or folder for test results and visit notes.", "Save after-hours GI contact in your phone today.", "Start a one-line daily symptom note.", "Ask for a written flare plan before you need it.", "Explore newly diagnosed Foundation resources."],
        "faq": [("Will I need surgery?", "Some patients do, many do not. Your disease course is individual. Focus on monitoring and adherence first."),
                ("Can I work or study normally?", "Many people do with accommodations during flares. School and workplace rights guides can help."),
                ("Is IBD contagious?", "No. IBD is not spread person to person.")],
        "related": [("Foundation newly diagnosed first week", "/guides/newly-diagnosed-foundation-first-week"), ("What is IBD? Foundation basics", "/guides/what-is-ibd-foundation"),
                    ("First GI appointment guide", "/guides/first-gastroenterology-appointment-ibd"), ("Visit prep checklist", "/visit-prep"),
                    ("Newly diagnosed hub", "/newly-diagnosed"), ("Track symptoms and food", "/guides/track-ibd-symptoms-food")],
    }

    TOPICS["crohns-flare-what-to-do"] = {
        "intro": "A Crohn's flare means symptoms have worsened beyond your usual baseline, often signaling increased inflammation. Medical decisions belong with your IBD team. This guide covers recognizing flare signs, first 24 to 48 hour steps, hydration, diet, when to call for help, logging, medications, and mental health. Education only, not medical advice.",
        "sections": [
            ("Recognizing flare signs early", P(
                "Compare current symptoms to your typical remission pattern. More frequent stools, new or heavier bleeding, worsening pain, fever, fatigue, mouth sores, or unintended weight loss may signal a flare.",
                "Nighttime bowel movements, cramping that limits activity, or joint pain can accompany bowel inflammation. Note when changes started and whether they are accelerating.",
                "A single bad day differs from a sustained trend. Track three to seven days before deciding it is a true flare versus a brief stomach bug.",
            )),
            ("First 24 to 48 hours at home", P(
                "Contact your IBD team using their flare pathway if symptoms exceed your written plan. Many clinics offer nurse triage or on-call GI coverage.",
                "Rest, simplify meals, and pause nonessential stress where possible. Gather recent labs, medication list, and symptom log for the call.",
                "Do not start steroids left over from prior years or borrow a friend's medication unless your clinician explicitly instructs you.",
            )),
            ("Hydration, electrolytes, and diet adjustments", P(
                "Increase fluids with water, oral rehydration solutions, or broth if your team approves. Diarrhea and fever raise sodium and potassium needs.",
                "Shift toward softer, lower-fiber foods temporarily if they reduce irritation. Bananas, rice, applesauce, eggs, and lean protein are common short-term choices.",
                "Alcohol, heavy spices, and large high-fat meals often worsen symptoms. Reexpand diet when inflammation improves with medical treatment.",
            )),
            ("When to call GI, urgent care, or the ER", P(
                "Call your GI team for worsening stool count, blood, pain, or fever according to your action plan. Same-day nurse triage may prevent ER visits.",
                "Urgent care can help with dehydration assessments, fever workups, or pain control when GI is unreachable, if they coordinate with your records.",
                "Go to the emergency room for severe abdominal pain, fainting, heavy bleeding, persistent vomiting, high fever, or signs of dehydration despite fluids. Trust your instinct when symptoms feel unlike prior flares.",
            )),
            ("What to log, medications, and mental health", P(
                "Log stool frequency, blood presence, pain score, temperature, weight, and foods tolerated. Photos of stool are usually unnecessary unless your team requests them.",
                "Take prescribed maintenance and rescue medications on schedule. Missing biologics or immunomodulators can prolong flares. Ask about drug levels or stool calprotectin if flares repeat.",
                "Flares increase anxiety and sleep disruption. Brief walks, breathing exercises, and counseling referrals help. You are not failing because a flare occurred; inflammation needs medical attention.",
            )),
        ],
        "tips": ["Save your clinic flare hotline and after-hours number now.", "Keep oral rehydration packets and bland foods stocked.", "Log symptoms daily during flares for faster triage.", "Never change biologics or steroids without clinician guidance.", "Tell someone you trust when symptoms worsen for emotional support."],
        "faq": [("How do I know if it is a flare or a virus?", "Duration, blood, joint pain, and comparison to your baseline help. Your GI team may order stool tests or labs."),
                ("Should I go to the ER for blood in stool?", "Heavy bleeding, dizziness, or large clots need urgent evaluation. Call your team for guidance on moderate changes."),
                ("Can stress alone cause a flare?", "Stress affects symptoms and may influence inflammation for some people. Medical assessment still matters when bowel symptoms change.")],
        "related": [("Flare help hub", "/flare-help"), ("Foods during a Crohn's flare", "/guides/foods-to-eat-crohns-flare"),
                    ("Flare first 48 hours article", "/blog/flare-first-48-hours"), ("Flare emergency supplies", "/guides/ibd-flare-emergency-supplies"),
                    ("IBD hydration guide", "/guides/ibd-hydration-fluids"), ("Stress and anxiety with IBD", "/guides/stress-anxiety-ibd")],
    }

    TOPICS["ulcerative-colitis-flare-management"] = {
        "intro": "Ulcerative colitis flares often bring increased bowel frequency, urgency, blood, and fatigue. Early communication with your gastroenterologist can shorten recovery and prevent complications. This guide summarizes UC flare self-management topics patients review in clinic. Education only, not a substitute for medical care.",
        "sections": [
            ("UC flare symptoms to track", P(
                "Count bowel movements day and night. Note blood amount, urgency, cramping, and fever.",
                "Weight loss, racing heart, or dizziness may signal dehydration or anemia. Weigh yourself weekly during flares.",
                "Compare symptoms to your last remission period. Sudden changes warrant faster outreach than gradual drift.",
            )),
            ("First steps in the first days", P(
                "Use your written flare plan if you have one. Call the IBD nurse line before starting old steroid packs on your own.",
                "Simplify diet toward low-residue, low-irritant foods if tolerated. Hydrate with oral rehydration solutions when diarrhea is heavy.",
                "Cancel nonessential obligations to rest. Stress management supports but does not replace medical treatment.",
            )),
            ("Medical treatment and testing", P(
                "Stool calprotectin, blood work, and sigmoidoscopy or colonoscopy may guide therapy changes. Follow through on ordered tests.",
                "Rescue steroids, increased mesalamine, or biologic adjustments are common paths. Adherence to maintenance drugs prevents future flares.",
                "Ask about blood clots, anemia, and infection risks during severe flares. Hospitalization is sometimes needed for IV steroids or fluids.",
            )),
            ("When to seek urgent or emergency care", P(
                "Severe bleeding, fainting, extreme abdominal distension, or ten or more bloody stools daily are examples of scenarios requiring emergency evaluation.",
                "Toxic megacolon is rare but serious. Severe pain with fever and a rigid abdomen need immediate care.",
                "If unsure, call your GI on-call line. Document their advice and symptoms.",
            )),
            ("Recovery and preventing the next flare", P(
                "Taper medications only as directed. Finish courses unless your team adjusts early based on side effects.",
                "Reintroduce foods slowly as symptoms improve. Fiber expansion should be gradual with clinician input.",
                "Review vaccine status, smoking cessation, and medication levels at follow-up. Log triggers and stressors for future planning.",
            )),
        ],
        "tips": ["Keep a UC flare card with clinic numbers in your wallet.", "Photograph medication labels for nurse triage calls.", "Track nocturnal stools separately; they matter clinically.", "Do not stop mesalamine without asking your team.", "Schedule follow-up labs after rescue steroid courses."],
        "faq": [("Is bloody diarrhea always an emergency?", "Not always, but volume, dizziness, and pace of change matter. Call your team for personalized triage."),
                ("Can I travel during a UC flare?", "Mild changes may be OK with planning. Worsening symptoms usually need treatment before travel."),
                ("Does UC always need hospitalization in flares?", "No, but severe cases might. Early outreach reduces admission risk.")],
        "related": [("Crohn's flare guide", "/guides/crohns-flare-what-to-do"), ("UC diet foods", "/guides/ulcerative-colitis-diet-foods"),
                    ("Flare help hub", "/flare-help"), ("Blood in stool article", "/blog/blood-in-stool-ibd-when-to-worry"),
                    ("Track symptoms and food", "/guides/track-ibd-symptoms-food"), ("Foundation pain and fatigue", "/guides/foundation-ibd-pain-fatigue")],
    }

    TOPICS["track-ibd-symptoms-food"] = {
        "intro": "Symptom and food tracking helps you and your GI team spot patterns, evaluate treatments, and prepare for visits. Simple, consistent logs beat perfect but abandoned apps. This guide explains what to record and how to use data without obsessing. Education only, not medical advice.",
        "sections": [
            ("Why tracking matters in IBD", P(
                "Memory bias makes single clinic days unreliable. A week of logs shows stool frequency, blood, pain, and diet links more clearly.",
                "Medication changes, travel, stress, and menstrual cycles affect symptoms. Notes provide context labs alone miss.",
                "Tracking supports disability paperwork, school forms, and insurance appeals with objective trends.",
            )),
            ("What to log each day", P(
                "Stool count, blood presence, urgency, pain score, energy, sleep, and key foods are core fields. Weight weekly adds value during flares.",
                "Record medications taken, missed doses, and supplements. Note fever, joint pain, or skin changes.",
                "One line per meal plus snacks is enough. Perfect calorie counts are rarely needed unless a dietitian requests them.",
            )),
            ("Food logging without fear", P(
                "Track patterns, not moral judgment. Foods are data points, not failures.",
                "Introduce one new food at a time when testing tolerance. Mark days of travel, alcohol, or restaurant meals.",
                "Share logs with your dietitian to separate inflammation from irritant symptoms when possible.",
            )),
            ("Tools: paper, apps, and IBDPal", P(
                "Paper diaries work when phones feel overwhelming. Photo of a notebook page is fine for portals.",
                "Apps should export PDF or CSV for clinic visits. Check privacy policies before syncing health data.",
                "IBDPal and similar tools combine symptoms, meals, and Bristol stool types for flare discussions.",
            )),
            ("Using logs at appointments", P(
                "Summarize the worst week and the best week since your last visit. Highlight changes after medication adjustments.",
                "Ask whether calprotectin, CRP, or imaging align with your symptom log. Mismatch guides further testing.",
                "Stop logging intensively once patterns are clear if it harms mental health. Your clinician can suggest lighter cadence.",
            )),
        ],
        "tips": ["Log at the same times daily to build habit.", "Use Bristol stool chart terms for clarity.", "Note menstrual cycle days if urgency fluctuates.", "Export a PDF before each GI visit.", "Pair food logs with sleep and stress columns."],
        "faq": [("Do I need to log forever?", "No. Many patients log heavily around flares and lightly in remission."),
                ("Can tracking cause anxiety?", "Yes. Simplify fields or pause if obsessive. Discuss with your care team."),
                ("Should I photograph every meal?", "Usually not required unless a dietitian asks.")],
        "related": [("IBD nutrition tracking app guide", "/guides/ibd-nutrition-tracking-app"), ("Crohn's food triggers", "/guides/crohns-food-triggers"),
                    ("Visit prep checklist", "/visit-prep"), ("Bristol stool chart article", "/blog/bristol-stool-chart-ibd"),
                    ("Tracking with IBDPal article", "/blog/tracking-food-symptoms-ibdpal"), ("Doctor visit prep guide", "/guides/crohns-doctor-visit-prep")],
    }

    TOPICS["ibd-nutrition-tracking-app"] = {
        "intro": "Nutrition tracking apps can help IBD patients document intake, symptoms, and trends between clinic visits. Choosing the right tool depends on your goals, privacy comfort, and whether a dietitian will review exports. This guide compares practical features without endorsing a single product. Education only.",
        "sections": [
            ("Goals before choosing an app", P(
                "Clarify whether you need calorie counts, macro tracking, trigger identification, or simple meal photos for your dietitian.",
                "Pediatric patients need age-appropriate tools and caregiver involvement. Growth-focused tracking differs from adult weight loss apps.",
                "If mental health suffers from detailed logging, prioritize minimal fields or paper logs.",
            )),
            ("Features that help IBD care", P(
                "Custom symptoms, stool type, pain scores, and medication reminders support flare conversations.",
                "Export to PDF or CSV helps gastroenterology visits. Cloud backup prevents lost data during phone upgrades.",
                "Barcode scanners speed entry but miss home-cooked meals. Quick free-text notes often work better for mixed diets.",
            )),
            ("Privacy and data sharing", P(
                "Read whether health data is sold, shared with employers, or used for ads. HIPAA-covered apps differ from consumer wellness apps.",
                "Disable public social feeds if they encourage comparison or risky advice.",
                "Ask your clinic if they integrate with any patient portals before paying for premium tiers.",
            )),
            ("IBDPal and combined approaches", P(
                "IBDPal links meals, symptoms, and disease education in one IBD-focused experience. Use it alongside clinician guidance, not as diagnosis.",
                "Some patients use a simple symptom app plus a photo food diary. Consistency beats feature overload.",
                "Bring exported summaries to visits rather than scrolling live during short appointments.",
            )),
            ("Working with your dietitian", P(
                "Share two weeks of logs before nutrition visits. Highlight flares, travel, and restaurant weeks.",
                "Ask which metrics matter: protein grams, iron intake, or simply meal timing.",
                "Stop tracking fields your dietitian does not use. Simpler logs improve adherence.",
            )),
        ],
        "tips": ["Pick one app and use it for two weeks before switching.", "Turn off calorie goals if they trigger restriction.", "Export data the night before GI visits.", "Log medications alongside meals.", "Ask your dietitian which app exports they prefer."],
        "faq": [("Are nutrition apps medical devices?", "Most consumer apps are not FDA-cleared for IBD treatment. Treat them as diaries."),
                ("Can apps diagnose food allergies?", "No. Elimination and testing need clinician supervision."),
                ("Is IBDPal a replacement for my GI?", "No. It supports education and logging between professional visits.")],
        "related": [("Track symptoms and food", "/guides/track-ibd-symptoms-food"), ("What should I eat with IBD?", "/guides/what-should-i-eat-crohns-colitis"),
                    ("Tracking with IBDPal article", "/blog/tracking-food-symptoms-ibdpal"), ("Anti-inflammatory diet guide", "/guides/anti-inflammatory-diet-ibd"),
                    ("Doctor visit prep", "/guides/crohns-doctor-visit-prep"), ("Complete nutrition article", "/blog/complete-ibd-nutrition-guide")],
    }

    TOPICS["crohns-doctor-visit-prep"] = {
        "intro": "Prepared GI visits lead to better questions, faster decisions, and less anxiety. This guide helps Crohn's and colitis patients organize symptoms, medications, and goals before appointments. Education only, not medical advice.",
        "sections": [
            ("Two weeks before the visit", P(
                "Request records if you changed clinics. Gather imaging, colonoscopy reports, and lab printouts.",
                "Start or update a symptom and food log. Note worst days, blood, nocturnal stools, and weight change.",
                "List questions as they arise in your phone notes. Prioritize top three for the visit.",
            )),
            ("Medication and allergy list", P(
                "Bring exact drug names, doses, schedules, and last infusion or injection dates. Include supplements and over-the-counter items.",
                "Note missed doses or side effects since the last visit. Pharmacy printouts help accuracy.",
                "Ask about refills, prior authorizations, and travel letters at the end of the appointment.",
            )),
            ("What to bring physically or digitally", P(
                "Insurance cards, photo ID, stool diary exports, and a support person if allowed.",
                "Wear comfortable clothing if abdominal exam is likely. Arrive with a full bladder only if ultrasound is scheduled.",
                "Use the visit prep checklist on IBDPal to avoid forgetting key topics.",
            )),
            ("During the appointment", P(
                "Share your top concerns in the first five minutes. Ask what follow-up tests are needed and when results return.",
                "Request written flare instructions if you do not have them. Clarify after-hours contacts.",
                "Repeat back the plan in your own words to confirm understanding.",
            )),
            ("After the visit", P(
                "Schedule labs, infusions, or scopes before leaving the building when possible.",
                "Message portal questions if instructions were unclear. Do not guess on steroid tapers.",
                "Update your emergency medication card and share changes with your pharmacy.",
            )),
        ],
        "tips": ["Email yourself a visit summary right after the appointment.", "Bring a printed medication list even if records are electronic.", "Ask how to reach the team after hours.", "Request portal access for caregivers if appropriate.", "Use /visit-prep checklist before every GI visit."],
        "faq": [("Should I bring stool samples to routine visits?", "Only if requested. Call ahead about collection kits."),
                ("Can I record the visit?", "Ask permission first. Some clinics allow audio for personal use."),
                ("What if I forget questions?", "Send a portal message within 24 hours with remaining items.")],
        "related": [("Visit prep checklist", "/visit-prep"), ("First gastroenterology appointment", "/guides/first-gastroenterology-appointment-ibd"),
                    ("Track symptoms and food", "/guides/track-ibd-symptoms-food"), ("Biologics overview", "/guides/biologics-crohns-colitis"),
                    ("Foundation medication guide", "/guides/foundation-ibd-medication-guide"), ("Prior authorization guide", "/guides/ibd-prior-authorization-foundation")],
    }

    TOPICS["biologics-crohns-colitis"] = {
        "intro": "Biologic therapies target specific immune pathways in moderate to severe IBD. Understanding how they work, how they are given, and what monitoring involves helps patients partner with their GI team. This guide is educational only and does not recommend starting or stopping any drug.",
        "sections": [
            ("What biologics are in IBD", P(
                "Common classes include anti-TNF agents, integrin inhibitors, IL-12/23 inhibitors, and JAK inhibitors for some patients. Your clinician matches class to disease type, history, and insurance.",
                "Biologics are not interchangeable. Switching may require washout periods and new monitoring plans.",
                "Biosimilars can be appropriate for some patients. Ask whether your pharmacy plans cover them.",
            )),
            ("Infusions, injections, and adherence", P(
                "Dosing may be IV at infusion centers or subcutaneous at home. Learn storage, travel, and missed-dose rules.",
                "Pre-medications, infusion reactions, and injection site care should be reviewed with nurses before the first dose.",
                "Set calendar reminders and travel letters before trips. Do not skip doses without clinician guidance.",
            )),
            ("Monitoring and infection prevention", P(
                "TB screening, hepatitis panels, and periodic labs are standard before and during therapy.",
                "Report fever, cough, skin changes, or neurologic symptoms promptly. Some infections need pausing therapy.",
                "Vaccine updates, including influenza, COVID-19, and pneumococcal vaccines per schedule, matter on immunosuppression.",
            )),
            ("Side effects and expectations", P(
                "Not everyone responds immediately. Drug levels and calprotectin may guide dose adjustments.",
                "Discuss risks of lymphoma, skin cancer, and liver enzyme changes in context of your personal history.",
                "Pregnancy planning and surgery timing need coordinated biologic plans. Involve your GI early.",
            )),
            ("Insurance, prior auth, and appeals", P(
                "Biologics often require prior authorization and step therapy documentation. Start paperwork early when switching drugs.",
                "Patient assistance programs exist for qualifying households. Clinic financial counselors can help.",
                "Keep denial letters. Appeals with medical records and symptom logs are common.",
            )),
        ],
        "tips": ["Store injectables per label instructions.", "Carry a medication card listing your biologic and last dose.", "Report infection symptoms before your next scheduled dose.", "Ask about travel letters for airport syringes.", "Track symptoms before and after dose changes."],
        "faq": [("Do biologics cure IBD?", "They control inflammation for many patients but are not cures. Maintenance plans vary."),
                ("Can I drink alcohol on biologics?", "Discuss with your GI. Liver monitoring and personal risk matter."),
                ("What if I miss an infusion?", "Call your team immediately for timing instructions. Do not double doses without advice.")],
        "related": [("Foundation medication guide", "/guides/foundation-ibd-medication-guide"), ("Prior authorization guide", "/guides/ibd-prior-authorization-foundation"),
                    ("Vaccines and infection risk", "/guides/foundation-ibd-vaccines-infection"), ("Biologics and travel article", "/blog/biologics-flying-travel-ibd"),
                    ("Step therapy and Safe Step Act", "/guides/step-therapy-safe-step-act-ibd"), ("Clinical trials guide", "/guides/foundation-ibd-clinical-trials")],
    }

    TOPICS["ibd-travel-planning"] = {
        "intro": "Travel with Crohn's or colitis takes extra planning for medications, restrooms, food, and flare contingencies. Many patients travel widely with preparation and clinician support. This guide covers practical steps before domestic or international trips. Education only.",
        "sections": [
            ("Before you book", P(
                "Discuss destination vaccines, malaria prophylaxis, and food safety with your GI team. Timing biologic doses around travel reduces surprises.",
                "Check insurance coverage abroad and consider travel medical policies for longer trips.",
                "Research restroom access laws and apps for your destination. Airport security rules apply to liquids and syringes.",
            )),
            ("Packing medications and supplies", P(
                "Carry meds in original labeled containers in hand luggage. Bring extra days in case of delays.",
                "Obtain travel letters for injectables and coolers for biologics if needed.",
                "Pack wipes, spare underwear, ostomy supplies, and oral rehydration packets in a carry-on flare kit.",
            )),
            ("Food and water strategies", P(
                "Bottled water and cooked foods reduce infection risk in some regions. Peel fresh fruit when unsure.",
                "Research restaurant phrases or cards explaining dietary needs. Simple, cooked choices often feel safest during active symptoms.",
                "Avoid risky street food if immunosuppressed. Balance adventure with clinician advice.",
            )),
            ("Time zones and schedules", P(
                "Shift medication times gradually for large zone changes. Ask your team for a written schedule.",
                "Infusion centers abroad exist but need advance planning. Never assume walk-in availability.",
                "Track symptoms during travel jet lag so you do not confuse fatigue with flares.",
            )),
            ("If symptoms flare away from home", P(
                "Use your clinic's on-call line or telehealth when available. Know local urgent care options before departure.",
                "Travel insurance with medical evacuation is worth considering for remote areas.",
                "Document visits and labs to share with your home GI after return.",
            )),
        ],
        "tips": ["Photograph your prescription labels before leaving.", "Download restroom finder apps for your route.", "Carry a clinician letter for security screenings.", "Pack twice the ostomy supplies you expect to need.", "Review Foundation travel restroom guide before long trips."],
        "faq": [("Can I fly with injectable biologics?", "Yes with proper documentation and storage. Ask your team for a travel letter."),
                ("Should I avoid developing countries on immunosuppression?", "Not always, but vaccine and infection planning is essential. Personalize with your GI."),
                ("What if my medication is lost abroad?", "Contact manufacturer patient support and local pharmacies early. Embassies may assist.")],
        "related": [("Foundation travel and restroom access", "/guides/foundation-ibd-travel-restroom-access"), ("Flare emergency supplies", "/guides/ibd-flare-emergency-supplies"),
                    ("Biologics and travel article", "/blog/biologics-flying-travel-ibd"), ("Dining out with IBD", "/guides/dining-out-with-ibd"),
                    ("Vaccines and infection", "/guides/foundation-ibd-vaccines-infection"), ("IBD hydration guide", "/guides/ibd-hydration-fluids")],
    }

    TOPICS["ibd-workplace-school-rights"] = {
        "intro": "IBD can affect attendance, restroom needs, and energy at work or school. Laws and policies may provide accommodations when documentation is in place. This guide outlines common rights topics patients discuss with clinicians and administrators. Not legal advice.",
        "sections": [
            ("Disclosure and documentation", P(
                "You choose how much to share. Medical letters should state needed accommodations without unnecessary diagnosis detail.",
                "In the U.S., ADA and Section 504 may apply depending on setting. Other countries have parallel frameworks.",
                "HR and disability offices often have forms your clinician completes. Start early each school year.",
            )),
            ("Common accommodations", P(
                "Flexible breaks, remote work options, extra time on exams, restroom passes, and modified PE may be reasonable.",
                "Infusion appointments and post-operative recovery may need protected leave. Know FMLA or local equivalents.",
                "Ostomy supplies and refrigeration for biologics can be workplace discussions.",
            )),
            ("Talking with employers and professors", P(
                "Focus on functional needs: predictable restroom access, occasional telework, or deadline flexibility during flares.",
                "Provide a point of contact for HR rather than debating symptoms with every coworker.",
                "Professors appreciate advance notice before midterms when symptoms flare.",
            )),
            ("Students and parents", P(
                "School nurses can store emergency medications and flare kits. 504 plans travel between grades when updated.",
                "Bullying about restroom use should be reported. Foundation youth resources support families.",
                "College disability services require separate registration from high school plans.",
            )),
            ("When to seek legal help", P(
                "Denials of reasonable accommodation, termination after disclosure, or discrimination may need employment attorneys or advocacy groups.",
                "Keep written records of requests and responses.",
                "Foundation workplace guides provide starting language, not legal representation.",
            )),
        ],
        "tips": ["Renew accommodation letters annually.", "Know your clinic fax for HR forms.", "Register with college disability services before classes start.", "Keep a private symptom log for accommodation reviews.", "Review Foundation workplace rights guide for sample language."],
        "faq": [("Must I tell my boss I have IBD?", "No. You may request accommodations with functional language and medical documentation."),
                ("Can I be fired for frequent bathroom breaks?", "Retaliation for reasonable accommodations may be unlawful depending on jurisdiction. Document interactions."),
                ("Do accommodations guarantee perfect attendance?", "No. They reduce barriers but medical leave may still be needed.")],
        "related": [("Foundation workplace and school rights", "/guides/foundation-workplace-school-rights-ibd"), ("Youth school Foundation resources", "/guides/youth-school-foundation-resources"),
                    ("College with IBD article", "/blog/college-with-ibd"), ("Living with an ostomy", "/guides/living-with-ostomy-ibd"),
                    ("Partner and caregiver guide", "/guides/partner-caregiver-ibd"), ("Newly diagnosed guide", "/guides/newly-diagnosed-crohns-colitis")],
    }

    TOPICS["living-with-ostomy-ibd"] = {
        "intro": "Some people with IBD live with a temporary or permanent ostomy after surgery. Adjustment takes time, but many return to work, sports, and relationships with the right support and supplies. This guide covers practical education topics patients discuss with surgeons and WOC nurses. Not medical advice.",
        "sections": [
            ("Types of ostomies in IBD", P(
                "Ileostomy and colostomy are common depending on surgery type. Temporary loop ostomies may be reversed later.",
                "Stoma location, appliance type, and output consistency affect daily routines.",
                "Wound ostomy continence nurses teach pouch changes, skin care, and problem solving.",
            )),
            ("Daily appliance and skin care", P(
                "Empty pouches when one-third full to reduce leaks. Measure stoma regularly as swelling decreases after surgery.",
                "Barrier rings, paste, and proper fit prevent skin breakdown. Photograph irritated skin for telehealth visits.",
                "Order supplies through durable medical equipment providers before running low.",
            )),
            ("Diet, hydration, and blockages", P(
                "High ostomy output increases dehydration risk. Salty snacks and electrolyte drinks may help when clinicians approve.",
                "Chew thoroughly and hydrate to reduce blockage risk with ileostomies. Know warning signs: pain, no output, vomiting.",
                "Introduce new foods slowly and log reactions. Pineapple, nuts, and corn affect people differently.",
            )),
            ("Clothing, activity, and travel", P(
                "Ostomy wraps and supportive underwear improve confidence. Many swim with specialized covers.",
                "Contact sports may need protection. Discuss weight limits and core exercises with your surgeon.",
                "Travel with extra supplies in carry-on bags and know TSA guidance on liquids and scissors.",
            )),
            ("Emotional adjustment and support", P(
                "Grief and body image changes are normal. Peer ostomy groups and counseling help.",
                "Intimacy conversations with partners improve with education. Foundation intimacy guides address common fears.",
                "Tell your GI if output changes suddenly; it may signal blockage or disease recurrence rather than appliance issues alone.",
            )),
        ],
        "tips": ["Save WOC nurse contact for urgent appliance problems.", "Carry a spare kit everywhere for the first year.", "Weigh weekly if output is high.", "Join an ostomy support group online or locally.", "Review Foundation surgery and ostomy resources."],
        "faq": [("Will everyone notice my pouch?", "Modern appliances are discreet under clothing. Most people cannot tell."),
                ("Can I shower with the pouch on?", "Yes. Many wear appliances in the shower and pat dry afterward."),
                ("Does an ostomy mean IBD is cured?", "Not always. Crohn's can recur; UC surgery may be curative for colon disease. Surveillance continues.")],
        "related": [("Foundation surgery and ostomy", "/guides/foundation-ibd-surgery-ostomy"), ("Foundation intimacy guide", "/guides/foundation-ibd-intimacy-sexual-health"),
                    ("IBD hydration guide", "/guides/ibd-hydration-fluids"), ("Travel planning", "/guides/ibd-travel-planning"),
                    ("Support groups overview", "/guides/crohns-colitis-support-groups"), ("Workplace rights", "/guides/ibd-workplace-school-rights")],
    }

    TOPICS["stress-anxiety-ibd"] = {
        "intro": "Stress and anxiety do not cause IBD, but they can worsen symptoms and quality of life. Coping skills, therapy, and medical care work together. This guide outlines mental health topics patients discuss with GI teams and counselors. Education only, not mental health treatment.",
        "sections": [
            ("Mind-gut connection in IBD", P(
                "The gut-brain axis links emotional state to motility, pain perception, and immune signaling.",
                "Anxiety about bathrooms, accidents, and needles is common and treatable.",
                "Treating mental health may improve daily function even when inflammation labs are improving.",
            )),
            ("Signs to seek professional help", P(
                "Panic attacks, persistent low mood, trauma flashbacks, or avoidance of food and social life need licensed care.",
                "GI psychologists specialize in chronic illness coping. Ask your clinic for referrals.",
                "Crisis hotlines and emergency services handle suicidal thoughts. Do not rely on forums alone.",
            )),
            ("Skills that help day to day", P(
                "Breathing exercises, brief walks, scheduled worry time, and cognitive behavioral strategies reduce rumination.",
                "Exposure planning for travel and restaurants can rebuild confidence with therapist support.",
                "Sleep hygiene supports both mood and inflammation monitoring.",
            )),
            ("Medication and therapy options", P(
                "Antidepressants help some patients with pain and anxiety. Coordinate with GI to avoid interactions.",
                "SSRIs and therapy combinations are common. Stigma should not block treatment.",
                "Tell both mental health and GI teams about all prescriptions and supplements.",
            )),
            ("Partnering with your GI team", P(
                "Share anxiety symptoms like nausea from fear of eating. They affect nutrition and adherence.",
                "Ask whether symptoms are inflammatory versus functional when labs and scopes are stable.",
                "Foundation emotional wellness resources complement clinic care.",
            )),
        ],
        "tips": ["Schedule bathroom breaks before stressful events.", "Try five-minute breathing apps daily, not only in crises.", "Ask your clinic about GI psychology referrals.", "Limit doom-scrolling in IBD forums before bed.", "Pair peer support with licensed therapy when needed."],
        "faq": [("Did stress cause my IBD?", "IBD is not caused by stress alone. Stress can affect symptoms and coping."),
                ("Is anxiety normal with IBD?", "Very common. Treatment helps and is not a sign of weakness."),
                ("Can therapy reduce flares?", "It may improve coping and adherence. Medical flares still need GI treatment.")],
        "related": [("Foundation emotional wellness", "/guides/foundation-emotional-wellness-ibd"), ("Sleep during flares", "/guides/sleep-ibd-flares"),
                    ("Bathroom urgency anxiety article", "/blog/bathroom-urgency-anxiety-ibd"), ("Partner and caregiver guide", "/guides/partner-caregiver-ibd"),
                    ("Crohn's flare guide", "/guides/crohns-flare-what-to-do"), ("IBD helpline resources", "/guides/ibd-crohns-colitis-helpline")],
    }

    TOPICS["sleep-ibd-flares"] = {
        "intro": "Sleep disruption is common during IBD flares because of nocturnal stools, pain, steroids, and anxiety. Poor sleep worsens fatigue and mood. This guide covers sleep hygiene topics patients discuss with their GI and primary care teams. Education only.",
        "sections": [
            ("Why flares steal sleep", P(
                "Nighttime bowel movements break sleep cycles. Urgency anxiety makes it hard to fall back asleep.",
                "Prednisone and other steroids can cause insomnia. Ask about dosing time adjustments with your clinician.",
                "Abdominal pain and fever compound fragmentation. Treating inflammation helps sleep long term.",
            )),
            ("Bedtime routines that help", P(
                "Limit screens one hour before bed. Dim lights signal melatonin release.",
                "Avoid large late meals if they trigger reflux or urgency. Sips of water are fine unless restricted.",
                "Keep a bedside flare kit to reduce panic trips to the bathroom.",
            )),
            ("Managing nocturnal symptoms", P(
                "Log nocturnal stool count for your GI team. It influences treatment urgency.",
                "Anti-diarrheal medications are sometimes used at night with clinician guidance. Do not self-start.",
                "Discuss pain plans that balance relief with alertness the next day.",
            )),
            ("Daytime habits", P(
                "Morning light exposure and short walks improve circadian rhythm when energy allows.",
                "Caffeine cutoff before noon helps if steroids already cause jitters.",
                "Naps longer than 30 minutes may worsen night insomnia. Rest propped up if lying flat triggers urgency.",
            )),
            ("When to ask for more help", P(
                "Persistent insomnia despite improving bowels may need sleep medicine referral.",
                "Screen for sleep apnea if snoring and daytime sleepiness appear.",
                "Mental health support helps when fear of accidents dominates nights.",
            )),
        ],
        "tips": ["Track nights with three or more bowel movements separately.", "Ask if evening steroid doses can shift earlier.", "Use dim night-lights to reduce fully waking.", "Keep phone out of bed to lower anxiety scrolling.", "Discuss melatonin with your clinician before trying."],
        "faq": [("Should I restrict fluids at night?", "Only if your team advises for specific heart or kidney conditions. Dehydration worsens flares."),
                ("Are sleep aids safe with IBD meds?", "Some interact. Always ask both GI and prescribing clinicians."),
                ("Will sleep improve when inflammation calms?", "Often yes, though anxiety habits may linger and need therapy.")],
        "related": [("Stress and anxiety with IBD", "/guides/stress-anxiety-ibd"), ("Crohn's flare guide", "/guides/crohns-flare-what-to-do"),
                    ("Foundation pain and fatigue", "/guides/foundation-ibd-pain-fatigue"), ("UC flare management", "/guides/ulcerative-colitis-flare-management"),
                    ("Flare help hub", "/flare-help"), ("Track symptoms and food", "/guides/track-ibd-symptoms-food")],
    }

    TOPICS["partner-caregiver-ibd"] = {
        "intro": "Partners and caregivers play important roles in IBD journeys without becoming substitute clinicians. Healthy support balances empathy, boundaries, and practical help. This guide offers education for loved ones and patients navigating relationships. Not couples therapy or medical advice.",
        "sections": [
            ("What caregivers can do well", P(
                "Listen without fixing every problem. Accompany appointments when invited and take notes.",
                "Help stock flare kits, manage insurance calls, and watch for red-flag symptoms.",
                "Learn medication names and after-hours contacts for emergencies.",
            )),
            ("Boundaries that protect relationships", P(
                "Patients retain autonomy over body and treatment decisions. Caregivers should not police food without agreement.",
                "Schedule non-IBD time together. Illness should not consume every conversation.",
                "Caregiver burnout is real. Respite and peer support for partners matter.",
            )),
            ("Communication during flares", P(
                "Use a simple scale for pain and fatigue instead of guessing.",
                "Agree on signals for when to call the GI team versus rest at home.",
                "Avoid blame language about flares. Inflammation is medical, not moral failure.",
            )),
            ("Intimacy and body image", P(
                "Ostomies, scars, and fatigue affect intimacy temporarily or long term. Open, patient conversations help.",
                "Foundation intimacy guides provide sensitive education for couples.",
                "Professional counseling supports couples when communication stalls.",
            )),
            ("Kids and family planning", P(
                "Parents with IBD benefit from explaining age-appropriate facts to children.",
                "Pregnancy planning requires GI and OB coordination. Caregivers join medication safety discussions.",
                "Genetic risk is modest but real. Focus on support rather than fear.",
            )),
        ],
        "tips": ["Ask how your loved one wants help before acting.", "Attend one GI visit yearly if welcomed.", "Keep emergency numbers on the fridge.", "Find caregiver support groups separately.", "Read Foundation family resources together."],
        "faq": [("How can I help without hovering?", "Ask directly: Do you want advice, company, or quiet? Respect the answer."),
                ("Should partners come to every infusion?", "Only if the patient wants that. Some prefer independence."),
                ("Is caregiver stress normal?", "Yes. Seek support for yourself too.")],
        "related": [("Foundation emotional wellness", "/guides/foundation-emotional-wellness-ibd"), ("Foundation intimacy guide", "/guides/foundation-ibd-intimacy-sexual-health"),
                    ("Stress and anxiety guide", "/guides/stress-anxiety-ibd"), ("Pediatric IBD help", "/guides/pediatric-crohns-colitis-help"),
                    ("Pregnancy Foundation resources", "/guides/pregnancy-ibd-foundation-resources"), ("Support groups overview", "/guides/crohns-colitis-support-groups")],
    }

    TOPICS["crohns-food-triggers"] = {
        "intro": "Food triggers in Crohn's disease vary widely and may change with disease activity. Identifying personal patterns helps comfort but does not replace treating inflammation. This guide explains how patients and dietitians approach trigger discovery safely. Education only.",
        "sections": [
            ("Triggers versus inflammation", P(
                "Some foods irritate symptomatic bowel without raising calprotectin. Others coincide with active inflammation unrelated to diet.",
                "Do not assume every symptom after eating proves a trigger. Viruses, stress, and medication gaps also matter.",
                "Labs and scopes help separate inflammatory flares from irritant responses.",
            )),
            ("Structured food reintroduction", P(
                "Elimination should be short and supervised. Long restrictive lists harm nutrition.",
                "Reintroduce one food every three to seven days while logging stools, pain, and gas.",
                "Portion size and cooking method change tolerance. Raw apple may fail while applesauce is fine.",
            )),
            ("Common suspect foods", P(
                "High-fat meals, lactose, caffeine, alcohol, sugar alcohols, and large fiber loads appear often in patient reports.",
                "Spicy foods and artificial sweeteners bother some people. Cultural diets need individualized adaptation.",
                "Nightshade and gluten elimination lack universal evidence. Test only with clinician oversight.",
            )),
            ("Working with a dietitian", P(
                "Registered dietitians prevent accidental malnutrition during elimination trials.",
                "They align plans with strictures, short bowel, and biologic schedules.",
                "Bring IBDPal or paper logs showing timing of symptoms after meals.",
            )),
            ("When to stop searching for triggers", P(
                "If weight drops, fear of food grows, or social life shrinks, pause elimination and involve your GI team.",
                "Treat active inflammation medically before chasing minor triggers.",
                "Remission expands food options for many patients. Re-test old triggers periodically.",
            )),
        ],
        "tips": ["Log sleep and stress alongside meals.", "Test foods in remission when possible.", "Cook vegetables soft before blaming the vegetable.", "Ask about lactose hydrogen breath testing.", "Stop elimination diets that lack clinician supervision."],
        "faq": [("Are food allergy tests enough?", "Not for IBD triggers. They detect IgE allergies, not most intolerance patterns."),
                ("Should I avoid gluten automatically?", "Only if celiac is ruled in or out with your team and a supervised trial makes sense."),
                ("Can triggers change after surgery?", "Yes. Anatomy changes absorption and tolerance.")],
        "related": [("Elimination diet: when to stop", "/guides/elimination-diet-when-to-stop-ibd"), ("Track symptoms and food", "/guides/track-ibd-symptoms-food"),
                    ("What should I eat with IBD?", "/guides/what-should-i-eat-crohns-colitis"), ("Dairy and lactose article", "/blog/dairy-lactose-ibd"),
                    ("Anti-inflammatory diet guide", "/guides/anti-inflammatory-diet-ibd"), ("FODMAP article", "/blog/fodmap-diet-crohns-colitis")],
    }

    TOPICS["ibd-crohns-colitis-helpline"] = {
        "intro": "Crohn's and colitis helplines and nurse lines connect patients with education, emotional support, and navigation resources. They do not replace your personal GI team for medical orders. This guide explains when to use national helplines versus clinic contacts. Education only.",
        "sections": [
            ("Foundation helpline and IBD Help Center", P(
                "The Crohn's and Colitis Foundation offers information specialists for resources, programs, and general education.",
                "Hours and languages vary. Check current listings on Foundation websites before calling.",
                "Helpline staff do not diagnose or prescribe. They point to vetted materials and local chapters.",
            )),
            ("Your clinic nurse line", P(
                "IBD centers often provide flare triage numbers with faster access to your chart.",
                "Use clinic lines for medication changes, infusion reactions, and worsening symptoms.",
                "Save after-hours GI coverage instructions in your phone contacts.",
            )),
            ("Crisis and mental health lines", P(
                "Suicidal thoughts, self-harm urges, or domestic violence need emergency and crisis services, not general IBD helplines.",
                "988 and local emergency numbers apply in the United States. Know your country equivalents when traveling.",
                "GI teams appreciate knowing when mental health crises affect medication adherence.",
            )),
            ("Insurance and prior auth navigation", P(
                "Foundation and clinic financial counselors help with appeals, copay cards, and patient assistance.",
                "Document denial letters and symptom logs when calling for navigation help.",
                "Step therapy questions may need both insurer and prescriber involvement.",
            )),
            ("Preparing for a productive call", P(
                "Have insurance card, medication list, and recent labs nearby.",
                "Write your top three questions first. Note callback number if queues are long.",
                "Follow up with your personal GI for anything medical beyond general education.",
            )),
        ],
        "tips": ["Save clinic and Foundation numbers separately in contacts.", "Call clinic lines first for urgent symptoms.", "Use 988 for mental health crises in the U.S.", "Keep denial letters handy for insurance calls.", "Log call dates and reference numbers."],
        "faq": [("Can helplines order tests?", "No. Only your licensed care team orders diagnostics and prescriptions."),
                ("Are helplines free?", "Foundation services are typically free; verify current policies."),
                ("Should I call for medication refills?", "Use pharmacy and clinic portals for refills unless instructed otherwise.")],
        "related": [("Find a Foundation chapter", "/guides/find-ccf-chapter-support-group"), ("Prior authorization guide", "/guides/ibd-prior-authorization-foundation"),
                    ("Foundation emotional wellness", "/guides/foundation-emotional-wellness-ibd"), ("Crohn's flare guide", "/guides/crohns-flare-what-to-do"),
                    ("Foundation resources hub", "/crohns-colitis-foundation-resources"), ("Support groups overview", "/guides/crohns-colitis-support-groups")],
    }

    TOPICS["first-gastroenterology-appointment-ibd"] = {
        "intro": "Your first gastroenterology appointment for suspected or new IBD can feel overwhelming. Preparation helps you use limited time well and reduces repeat visits for missing data. This guide walks through common first-visit topics. Education only, not medical advice.",
        "sections": [
            ("Before the visit", P(
                "Bring prior colonoscopy reports, imaging CDs or links, pathology, and lab printouts from other clinics.",
                "List symptoms with start dates: blood, weight change, nocturnal stools, joint pain, rashes, and family history.",
                "Note all medications including antibiotics, NSAIDs, supplements, and birth control.",
            )),
            ("What may happen at the visit", P(
                "History, abdominal exam, and rectal exam are common. You can request a chaperone.",
                "The gastroenterologist may order stool studies, blood work, imaging, or schedule colonoscopy.",
                "Ask what diagnoses are being considered and what would change the plan.",
            )),
            ("Questions worth asking", P(
                "What red flags should trigger a call before the next test?",
                "How long until results and who communicates them?",
                "Will you coordinate with my primary care doctor and dietitian?",
            )),
            ("Colonoscopy planning", P(
                "Bowel prep choices depend on disease location and prior surgeries. Follow instructions exactly.",
                "Arrange a driver and day off work. Ask about holding iron or certain meds beforehand.",
                "Sedation options and anesthesia clearance may need extra appointments.",
            )),
            ("After the first visit", P(
                "Schedule follow-up before leaving if possible. Portal activation prevents phone tag.",
                "Start a symptom log immediately if you are not already tracking.",
                "Seek second opinions for complex cases without guilt.",
            )),
        ],
        "tips": ["Arrive with a written timeline of symptoms.", "Bring a support person if allowed.", "Ask for colonoscopy prep in writing.", "Request after-hours contact before you leave.", "Use visit prep checklist at /visit-prep."],
        "faq": [("Will I be diagnosed at the first visit?", "Sometimes suspicion is clear, but many diagnoses need endoscopy and pathology."),
                ("Should I stop eating before the first visit?", "Unless told otherwise, eat normally unless fasting labs are scheduled."),
                ("Can I record the visit?", "Ask the clinician first.")],
        "related": [("Visit prep checklist", "/visit-prep"), ("Newly diagnosed guide", "/guides/newly-diagnosed-crohns-colitis"),
                    ("Doctor visit prep guide", "/guides/crohns-doctor-visit-prep"), ("Colonoscopy prep article", "/blog/colonoscopy-prep-ibd"),
                    ("What is IBD? Foundation basics", "/guides/what-is-ibd-foundation"), ("Newly diagnosed hub", "/newly-diagnosed")],
    }

    TOPICS["ibd-flare-emergency-supplies"] = {
        "intro": "A flare emergency kit reduces stress when symptoms spike away from home. Contents should match your personal disease pattern and clinician advice. This guide lists common supplies IBD patients pack for work, school, and travel. Education only.",
        "sections": [
            ("Core kit for most patients", P(
                "Include wipes, spare underwear, sealable bags, hand sanitizer, and a small towel.",
                "Oral rehydration packets and a water bottle help when diarrhea worsens.",
                "Keep a laminated card with GI after-hours number and medication allergies.",
            )),
            ("Medication and documentation", P(
                "Carry a few days of prescribed rescue meds only if your clinician approves on-the-go storage.",
                "Travel letters for injectables and a medication list with generic names support urgent care visits.",
                "Insurance card copies speed registration.",
            )),
            ("Ostomy and post-surgical additions", P(
                "Pack full appliance changes, barrier wipes, scissors, and disposal bags.",
                "Skin barrier paste prevents leaks during long outings.",
                "High-output supplies include extra electrolyte packets.",
            )),
            ("Work, school, and car kits", P(
                "Duplicate kits in backpack, desk, and car reduce panic when symptoms hit unexpectedly.",
                "Teachers and nurses can store labeled kits with permission forms.",
                "Restroom access cards from advocacy groups help in public venues.",
            )),
            ("Maintaining and refreshing kits", P(
                "Check expiration dates quarterly. Replace crushed snacks and leaked packets.",
                "Update phone numbers after clinic changes.",
                "Practice using supplies before a crisis so steps feel automatic.",
            )),
        ],
        "tips": ["Pack kits before remission ends; flares arrive unannounced.", "Use discrete pouches if privacy matters.", "Include a change of mask for clinic visits.", "Add a snack you tolerate for low blood sugar.", "Review kit contents with your GI nurse yearly."],
        "faq": [("Should I include opioids in my kit?", "Only if prescribed and legally carried. Most flare kits focus on hygiene and hydration."),
                ("Can kids carry kits at school?", "Yes with nurse agreements and 504 plans."),
                ("What about TSA and kits?", "Liquids follow airport rules; document medical need when possible.")],
        "related": [("Crohn's flare guide", "/guides/crohns-flare-what-to-do"), ("Flare help hub", "/flare-help"),
                    ("IBD hydration guide", "/guides/ibd-hydration-fluids"), ("Travel planning", "/guides/ibd-travel-planning"),
                    ("Living with an ostomy", "/guides/living-with-ostomy-ibd"), ("Flare first 48 hours article", "/blog/flare-first-48-hours")],
    }

    TOPICS["dining-out-with-ibd"] = {
        "intro": "Restaurant meals can be enjoyable with IBD when you plan ahead for restrooms, menu choices, and flare contingencies. Confidence grows with practice and clinician-aligned strategies. This guide shares common dining-out tips patients use. Education only.",
        "sections": [
            ("Choosing restaurants wisely", P(
                "Scout restroom locations with apps before seated meals. Chains with reliable access reduce anxiety.",
                "Buffets and heavy spice kitchens may be harder during active symptoms. Simple grilled options are frequent fallbacks.",
                "Call ahead about ingredients if you have severe allergies separate from IBD.",
            )),
            ("Ordering strategies", P(
                "Ask for sauces on the side and vegetables cooked well done. Plain rice, fish, or chicken are common safe starters.",
                "Share plates to keep portions moderate. Take leftovers home if large meals trigger urgency.",
                "Avoid known personal triggers even when dining socially. Politeness does not require eating everything.",
            )),
            ("Alcohol, caffeine, and dessert", P(
                "Happy hour drinks may worsen diarrhea or interact with meds. Sparkling water with lime is a discreet alternative.",
                "Caffeine after dinner can disrupt sleep already fragile during flares.",
                "Rich desserts and sugar alcohols bother some patients. Fruit sorbet may be gentler.",
            )),
            ("Timing and social pressure", P(
                "Eat earlier if evening urgency disrupts sleep. Snack before events to avoid starving at late dinners.",
                "Script simple phrases: I am keeping it mild tonight for my stomach.",
                "Leave early without guilt if symptoms flare. Health beats politeness.",
            )),
            ("When to skip dining out", P(
                "Active fevers, heavy bleeding, or dehydration are signs to rest at home and call your GI team.",
                "Post-operative and stricture phases may need texture-modified meals at home.",
                "Return to restaurants as recovery allows. Goals shift with disease activity.",
            )),
        ],
        "tips": ["Preview menus online before you go.", "Sit near restrooms when possible.", "Carry a discreet flare kit in your bag.", "Eat smaller portions and chew thoroughly.", "Log meals that correlate with next-day symptoms."],
        "faq": [("Should I avoid restaurants entirely with IBD?", "Many patients dine out safely in remission or with careful choices."),
                ("Is salad always risky?", "Raw high-fiber salads may bother active disease. Cooked vegetables are often easier."),
                ("How do I handle work dinners?", "Eat selectively, limit alcohol, and plan restroom breaks in advance.")],
        "related": [("Travel planning", "/guides/ibd-travel-planning"), ("Crohn's food triggers", "/guides/crohns-food-triggers"),
                    ("Foundation travel restroom access", "/guides/foundation-ibd-travel-restroom-access"), ("Stress and anxiety guide", "/guides/stress-anxiety-ibd"),
                    ("What should I eat with IBD?", "/guides/what-should-i-eat-crohns-colitis"), ("Bathroom urgency anxiety article", "/blog/bathroom-urgency-anxiety-ibd")],
    }

    from _guide_topics_part3 import add_part3
    add_part3(TOPICS)
