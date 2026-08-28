"""Topic entries part 2 for blog-expansions-batch2 (slugs 83-99)."""
from __future__ import annotations


def entry(sections, faqs, pads):
    return {"sections": sections, "faqs": faqs, "pads": pads}

TOPICS_PART2: dict = {
"remicade-infusion-day-tips-ibd": entry([
    ("Before you leave home", [
        "Confirm your infusion appointment and whether labs are due the same day. Some centers require recent blood work before infliximab doses.",
        "Hydrate and eat a light meal unless fasting is required. Nausea during long infusions is easier to manage with a settled stomach.",
        "Bring your medication list, insurance card, and a clinician letter if your center requests it for first visits.",
    ]),
    ("What to pack for comfort", [
        "Layers help because infusion suites vary in temperature. Socks, a neck pillow, and headphones make multi-hour visits easier.",
        "Download shows or audiobooks in case Wi-Fi is spotty. A phone charger or power bank prevents boredom when batteries die mid-dose.",
        "Pack hard candies or ginger chews if nausea has happened before. Ask whether pre-medications like antihistamines are planned.",
    ]),
    ("During and after the infusion", [
        "Nurses monitor blood pressure and reactions during the drip. Report warmth, chest tightness, or rash immediately.",
        "Infusion reactions are uncommon but treatable when caught early. Slowing the rate or giving medicines often resolves symptoms.",
        "Fatigue the same day or next day is common. Plan lighter schedules and avoid driving if you feel unwell afterward.",
    ]),
    ("Building a long-term infusion routine", [
        "Maintenance intervals are typically every eight weeks for Crohn's disease, but your clinician may adjust based on levels and symptoms.",
        "Therapeutic drug monitoring sometimes guides dose changes. Keep copies of infliximab level results in your records.",
        "If you travel frequently, ask about switching to a biosimilar or coordinating infusions at another center early, not the week before departure.",
    ]),
], [
    ("Can I work the day after Remicade?", "Many people do, but some need a rest day. Learn your pattern and plan accordingly."),
    ("What if I miss a dose?", "Contact your infusion center promptly. Delays can allow inflammation to return and affect drug levels."),
    ("Are home infusions an option?", "Some patients qualify through specialty pharmacies. Discuss safety, monitoring, and insurance with your team."),
], [
    "Arrive early for parking and registration during busy clinic mornings.",
    "Note any joint improvement timeline to share at follow-up visits.",
]),
"stelara-diet-ibd": entry([
    ("Eating while on ustekinumab", [
        "Stelara targets specific immune pathways and does not usually require a special diet beyond what your IBD activity demands. Focus on adequate calories, protein, and micronutrients.",
        "Active flares still need gentle foods regardless of biologic use. Medication controls inflammation over weeks; diet supports comfort day to day.",
        "Ask whether any food-drug interactions apply to your other medicines. Ustekinumab itself has few dietary restrictions.",
    ]),
    ("Nutrition labs worth tracking", [
        "Iron, vitamin D, B12, and albumin remain important on biologics. Healing mucosa improves absorption, but deficiencies can persist.",
        "Weight changes after starting Stelara should be reported. Slow gain may reflect improving appetite; unintended loss needs evaluation.",
        "Bone health matters if you previously used steroids. Calcium-rich foods and weight-bearing activity support long-term strength.",
    ]),
    ("Travel and injection timing", [
        "Subcutaneous maintenance doses every eight or twelve weeks require planning around trips. Carry medication letters and cool storage supplies when flying.",
        "Time zone changes can shift injection dates slightly. Clarify acceptable windows with your clinician before altering schedules.",
        "Sick-day rules during infections may pause injections. Know whom to call for fever while immunosuppressed.",
    ]),
    ("When symptoms persist despite therapy", [
        "Therapeutic drug levels and antibodies sometimes explain incomplete response. Diet changes alone rarely fix inadequate drug exposure.",
        "Small bowel Crohn's may need imaging even when colon symptoms improve. Mention persistent pain or nausea.",
        "Registered dietitians help when fear of food limits intake. Nutrition should not be an afterthought in biologic care.",
    ]),
], [
    ("Should I avoid grapefruit on Stelara?", "Ustekinumab is not known for grapefruit interactions like some pills. Always verify with your pharmacist for your full medication list."),
    ("Can I drink alcohol?", "Moderation depends on liver health and other drugs. Ask your GI team for personalized guidance."),
    ("Will Stelara change my food triggers?", "Triggers may shift as inflammation heals, but biologics do not erase individual intolerances overnight."),
], [
    "Keep a weekly weight log during the first months of therapy.",
    "Soft, familiar meals on injection days reduce stress when appetite is low.",
]),
"fodmap-diet-crohns-colitis": entry([
    ("What low FODMAP tries to accomplish", [
        "FODMAPs are fermentable carbohydrates that can increase gas and urgency in sensitive guts. A short structured elimination may reduce symptoms in some IBD patients with irritable bowel overlap.",
        "Low FODMAP is not an anti-inflammatory diet for Crohn's or colitis. It does not replace medical treatment of active disease.",
        "Work with a dietitian trained in IBD when possible. DIY elimination can over-restrict nutrition and social eating.",
    ]),
    ("How the phases usually work", [
        "Elimination typically lasts two to six weeks under supervision. Reintroduction tests specific groups like lactose, fructans, and polyols one at a time.",
        "Personal tolerance lists emerge from reintroduction, not from internet charts alone. One person may handle garlic while another cannot.",
        "During active flares, clinicians may pause FODMAP trials until inflammation is quieter. High restriction during bleeding diarrhea risks malnutrition.",
    ]),
    ("Common high-FODMAP foods patients notice", [
        "Wheat, onion, garlic, apples, honey, and certain legumes are frequent triggers in education materials. Serving size matters as much as food name.",
        "Plant-based milks and protein bars often hide inulin or chicory root. Label reading becomes a practical skill.",
        "Cooked and peeled fruits sometimes tolerate better than raw versions. Texture changes alter fermentable load.",
    ]),
    ("Integrating FODMAP results with IBD care", [
        "Share your tolerance map with your gastroenterologist. Persistent symptoms despite a careful low FODMAP trial may warrant imaging or calprotectin testing.",
        "Do not stay on strict elimination indefinitely without reintroduction. Long-term restriction can reduce fiber diversity.",
        "Combine FODMAP insights with adequate protein and iron intake, especially if anemia is present.",
    ]),
], [
    ("Is low FODMAP safe in active colitis?", "Only with clinician guidance. Elimination during severe flares may not be appropriate."),
    ("Can FODMAP diet put IBD in remission?", "It may ease functional symptoms but does not treat underlying inflammation."),
    ("Do I need special supplements on low FODMAP?", "Some people need calcium, fiber, or multivitamins if groups are limited. Dietitians personalize plans."),
], [
    "Monash University resources are widely used for portion guidance.",
    "A reintroduction journal prevents forgetting which group caused symptoms.",
]),
"skyrizi-patient-questions-ibd": entry([
    ("Understanding risankizumab in IBD", [
        "Skyrizi is an IL-23 inhibitor approved for certain Crohn's disease and ulcerative colitis patients who need advanced therapy. It blocks a pathway involved in gut inflammation.",
        "Induction often includes intravenous doses followed by subcutaneous maintenance injections. Schedules vary by disease and response.",
        "Like other biologics, infection screening and vaccination updates typically precede starting therapy.",
    ]),
    ("What patients ask about effectiveness", [
        "Clinical trials show improvement in symptoms and healing markers for many participants, but individual response differs. Give the induction phase time while staying in touch with your team.",
        "Therapeutic drug monitoring is less routine than with anti-TNF medicines, yet symptoms prompting escalation should be reported early.",
        "Combination with other immunosuppressants depends on risk and history. Do not add methotrexate or steroids without instructions.",
    ]),
    ("Side effects and monitoring", [
        "Upper respiratory infections and headache appear commonly in trial summaries. Serious infections are less frequent but require vigilance.",
        "New rashes, oral thrush, or fever should be reported. Tuberculosis and hepatitis screening are standard before initiation.",
        "Live vaccines are generally avoided while on biologics. Plan flu and COVID vaccines with your clinician.",
    ]),
    ("Practical life on Skyrizi", [
        "Injection training from specialty pharmacies reduces anxiety for at-home doses. Rotate sites and store pens per manufacturer guidance.",
        "Travel letters document medical necessity for carrying injectables. Cool packs and original labeling speed airport security.",
        "Pregnancy and breastfeeding questions should be discussed before conception. Plans may include timing doses around family goals.",
    ]),
], [
    ("How is Skyrizi different from Stelara?", "Both target IL-23 pathways but are distinct molecules with different dosing and trial data. Your gastroenterologist chooses based on your history."),
    ("Can I switch from Humira to Skyrizi?", "Switches happen in practice with washout or overlap rules. Only your clinician should direct timing."),
    ("Will insurance cover Skyrizi?", "Coverage varies. Specialty pharmacies often handle prior authorization with your clinic's help."),
], [
    "Keep a photo of your prescription label for travel and refill calls.",
    "Note injection site reactions to discuss at follow-up.",
]),
"rinvoq-patient-questions-ibd": entry([
    ("JAK inhibitors in ulcerative colitis and Crohn's", [
        "Rinvoq (upadacitinib) is an oral Janus kinase inhibitor used in selected IBD patients. Daily pills appeal to people who prefer not to inject or infuse.",
        "JAK class medicines work inside immune cells to reduce inflammatory signaling. They are not traditional biologics but still suppress immunity.",
        "Eligibility depends on prior therapy failures, comorbidities, and cardiovascular risk profile. Your GI team weighs benefits against class warnings.",
    ]),
    ("Monitoring beyond the prescription", [
        "Blood counts, liver enzymes, and lipids are monitored on schedules defined by regulators and your clinic. Missed labs can delay refills.",
        "Herpes zoster vaccination is often recommended before starting. Ask about shingles prevention if you are eligible.",
        "Report deep vein thrombosis symptoms like leg swelling or chest pain urgently, though absolute risk must be interpreted with your doctor.",
    ]),
    ("Everyday considerations on Rinvoq", [
        "Take doses consistently with or without food per label instructions. Do not double up after missed pills without calling the clinic.",
        "Interactions with other immunosuppressants require coordination. Herbal supplements are not always harmless.",
        "Infections, including COVID-19, may be more severe when immunosuppressed. Have a sick-day plan for holding doses during high fevers.",
    ]),
    ("Long-term expectations", [
        "Symptom improvement may appear within weeks, but mucosal healing timelines vary. Continue scheduled colonoscopies or calprotectin checks.",
        "If response plateaus, switching classes rather than guessing dose changes is a team decision.",
        "Mental health and sleep still influence perceived symptoms. Holistic follow-up helps.",
    ]),
], [
    ("Why do JAK inhibitors have boxed warnings?", "Regulators highlight risks seen across the class, including infections and cardiovascular events in some populations. Personal risk varies."),
    ("Can I drink alcohol on Rinvoq?", "Liver monitoring makes honesty about alcohol important. Follow guidance from your hepatology-aware GI team."),
    ("Is Rinvoq safe in pregnancy?", "Discuss family planning early. Alternative therapies may be preferred around conception."),
], [
    "Set phone reminders for daily dosing at the same time.",
    "Upload lab results to your patient portal before refill visits.",
]),
"prednisone-diet-hunger-ibd": entry([
    ("Why steroid appetite feels overwhelming", [
        "Prednisone and similar steroids raise blood sugar and alter brain hunger signals. Many patients describe constant cravings unrelated to true nutritional need.",
        "The hunger is biochemical, not a willpower failure. Planning meals and snacks reduces guilt and chaotic eating.",
        "Steroid courses are usually temporary. Strategies focus on getting through weeks without long-term harm.",
    ]),
    ("Plate-building when portions balloon", [
        "Fill half the plate with vegetables or fruit when tolerated, a quarter with lean protein, and a quarter with starches. Volume from produce can satisfy eyes and stomach.",
        "Keep pre-portioned snacks instead of eating from large bags. Nuts, crackers, and chips are easy to overeat on steroids.",
        "Protein at breakfast may stabilize energy and reduce mid-morning sugar crashes that trigger more cravings.",
    ]),
    ("Foods to moderate, not moralize", [
        "Sugary drinks, bakery items, and late-night fast food add calories fast on steroids. Substitution beats total deprivation for most people.",
        "Sodium retention can cause swelling and blood pressure changes. Processed foods and restaurant meals often hide extra salt.",
        "Caffeine may worsen anxiety and sleep, which intensifies hunger the next day. Track patterns honestly.",
    ]),
    ("Protecting bones, mood, and metabolism", [
        "Calcium, vitamin D, and resistance exercise support bone health during steroid bursts. Ask whether you need prescriptions for bone protection.",
        "Mood swings and insomnia are steroid side effects. Tell your clinician if coping becomes difficult.",
        "Weigh yourself weekly and report rapid gains to your team. Adjustments to taper speed or nutrition support may help.",
    ]),
], [
    ("Should I diet aggressively on prednisone?", "Extreme restriction fights biology and can worsen fatigue. Focus on balanced portions and clinician-guided taper."),
    ("Why is my face puffy?", "Fluid retention and fat redistribution are common steroid effects. They often improve as doses fall."),
    ("Can I skip meals to control weight?", "Regular meals with protein prevent muscle loss. Skipping meals may worsen irritability and night eating."),
], [
    "Sugar-free gum or tea can bridge cravings between meals.",
    "Walking after dinner helps glucose and stress for some patients.",
]),
"mucus-in-stool-ibd": entry([
    ("When mucus reflects active inflammation", [
        "The intestinal lining produces mucus to protect tissue. Ulcerative colitis and Crohn's flares often increase visible mucus in stool, sometimes with blood or urgency.",
        "Sudden mucus spikes with abdominal pain, fever, or weight loss should trigger outreach to your GI team. Calprotectin testing may clarify activity.",
        "Mucus alone during remission may still warrant mention at visits, especially if new.",
    ]),
    ("Other causes that overlap with IBD", [
        "Irritable bowel syndrome can cause mucus without high inflammatory markers. History and exams help distinguish overlap from active IBD.",
        "Infections, including Clostridioides difficile after antibiotics, may change stool appearance. Stool studies are common workup steps.",
        "Partial obstruction or severe constipation occasionally passes mucus. Associated bloating and vomiting are warning signs.",
    ]),
    ("Tracking that helps clinicians", [
        "Note frequency, color, and association with blood or pain. Photos are optional but can supplement descriptions.",
        "Record diet changes, travel, and new medicines in the same week mucus changes. Context speeds decisions.",
        "Bring a Bristol stool chart description to appointments for shared language.",
    ]),
    ("Treatment direction depends on cause", [
        "If inflammation is confirmed, therapy escalation or adjustment treats the root issue rather than chasing mucus alone.",
        "For functional overlap, fiber trials, antispasmodics, or gut-directed therapy may help under supervision.",
        "Avoid repeated unsupervised colon cleanses that irritate the colon further.",
    ]),
], [
    ("Is mucus always bad?", "Not always. Small amounts can appear with dietary changes. Persistent or increasing mucus with other flare signs needs evaluation."),
    ("Should I take antibiotics for mucus?", "Only if your clinician identifies a bacterial infection. Antibiotics can worsen IBD balance when misused."),
    ("Can probiotics clear mucus?", "Evidence is mixed. Discuss strains and goals with your GI team before spending heavily."),
], [
    "Stool calprotectin at home kits may supplement clinic labs.",
    "Hydration supports mucus balance when diarrhea is present.",
]),
"methotrexate-alcohol-folate-ibd": entry([
    ("Why folic acid accompanies methotrexate", [
        "Methotrexate interferes with folate metabolism, which helps control inflammation but can cause mouth sores, nausea, and lab changes. Folic acid supplementation reduces some side effects.",
        "Dosing schedules for folate vary. Some patients take it weekly, others daily except methotrexate day. Follow your prescription exactly.",
        "Do not swap high-dose folate without asking. Timing matters for efficacy and tolerance.",
    ]),
    ("Alcohol guidance patients should clarify", [
        "Methotrexate and alcohol both stress the liver. Many clinicians recommend strict limits or avoidance, especially with abnormal liver enzymes.",
        "Social drinking patterns should be discussed honestly before starting therapy. Liver tests guide ongoing safety.",
        "Binge drinking is particularly risky on methotrexate. Plan safer choices during holidays.",
    ]),
    ("Monitoring and symptom vigilance", [
        "Regular CBC and liver function tests detect early toxicity. Keep lab appointments even when feeling well.",
        "Shortness of breath or dry cough may rarely signal lung inflammation. Report respiratory symptoms promptly.",
        "Sun sensitivity can increase on methotrexate. Use sunscreen and protective clothing outdoors.",
    ]),
    ("Pregnancy and family planning", [
        "Methotrexate is teratogenic. Reliable contraception is essential for people who can become pregnant while on therapy.",
        "Discuss washout intervals before conception with rheumatology or GI prescribers. Partners should know risks too.",
        "Men on methotrexate also need planning conversations. Guidelines evolve, so use current clinic advice.",
    ]),
], [
    ("Can I have one beer on methotrexate?", "There is no universal safe number. Many teams advise abstinence or minimal intake based on labs."),
    ("What if I miss folic acid?", "Take it when you remember per instructions, but do not double doses. Call the clinic if vomiting prevents oral methotrexate."),
    ("Does methotrexate interact with ibuprofen?", "NSAIDs can add liver and kidney strain. Use acetaminophen strategies your clinician approves for pain."),
], [
    "Keep methotrexate and folate pills in separate labeled containers.",
    "Alcohol-free social options reduce pressure at events.",
]),
"humira-fatigue-ibd": entry([
    ("Fatigue before and after starting adalimumab", [
        "Active inflammation commonly causes profound fatigue. Some patients feel more energy within weeks of effective biologic therapy as cytokines fall.",
        "Others feel tired despite improving labs. Anemia, thyroid disease, poor sleep, and depression frequently contribute and need separate workup.",
        "Track fatigue on a simple scale alongside stool symptoms to see if timelines align with injections.",
    ]),
    ("Injection day effects and immune activation", [
        "Mild fatigue or achiness after injections occurs for some people. It may reflect immune response rather than treatment failure.",
        "Rotating injection sites and allowing pens to warm to room temperature reduce discomfort that can worsen tiredness.",
        "Fever or severe weakness after doses needs prompt reporting. Infection must be ruled out when immunosuppressed.",
    ]),
    ("Medication and lab review", [
        "Therapeutic drug levels and anti-drug antibodies explain partial response. Fatigue may persist if inflammation is undertreated.",
        "Steroid withdrawal, methotrexate, and antihistamines also sedate. Review the full list with your clinician.",
        "Vitamin D, iron, and B12 deficiencies are treatable fatigue drivers in IBD. Request labs if not checked recently.",
    ]),
    ("Lifestyle pacing while healing", [
        "Gradual activity increases stamina without flare triggers. Crash-and-burn cycles worsen perceived fatigue.",
        "Sleep hygiene and stress tools complement medical care. Cognitive behavioral therapy helps some IBD patients.",
        "Work accommodations for fatigue are reasonable during recovery. Document needs with your care team.",
    ]),
], [
    ("Does Humira always cause fatigue?", "No. Many patients feel better on therapy. Persistent tiredness deserves investigation beyond the biologic label."),
    ("Should I stop exercising if I am exhausted?", "Gentle movement often helps. Severe flares may need rest until your clinician advises otherwise."),
    ("Can I switch injection time for energy?", "Discuss timing changes with your team. Consistency matters for drug levels."),
], [
    "Morning light exposure may help circadian rhythm when nights are disrupted.",
    "Pair iron-rich foods with vitamin C if anemia treatment is ongoing.",
]),
"pencil-thin-stool-ibd": entry([
    ("Why stool shape sometimes narrows", [
        "Stool shape reflects colon diameter and transit time. Temporary thin stools during constipation or after diarrhea are common.",
        "Persistent pencil-thin stools raise concern for narrowing from Crohn's strictures, tumors, or severe inflammation. Duration and progression matter.",
        "Do not panic over one odd bowel movement. Patterns over weeks guide urgency.",
    ]),
    ("Associated symptoms that increase concern", [
        "Bloating, vomiting, painful cramps, or inability to pass gas suggest obstruction risk. Seek emergency care per your clinic plan.",
        "Weight loss, night sweats, or blood mixed with thin stools need prompt GI outreach.",
        "Rectal pain with tenesmus can accompany distal inflammation without structural narrowing.",
    ]),
    ("Workup themes your team may consider", [
        "Imaging such as CT enterography or MR enterography evaluates strictures in Crohn's disease. Colonoscopy inspects the lumen directly when safe.",
        "Calprotectin and CRP show inflammatory activity but do not replace anatomy checks when narrowing is suspected.",
        "Prior surgery, adhesions, and radiation history change differential lists. Share full surgical records.",
    ]),
    ("Living with known strictures", [
        "Diet texture modification and chewing thoroughly reduce blockage risk. Some patients avoid nuts, skins, and raw vegetables with team guidance.",
        "Balloon dilation or surgery are options for symptomatic strictures. Decisions balance nutrition, symptoms, and cancer surveillance.",
        "Carry a plan for partial obstruction symptoms when traveling. Know nearest hospitals.",
    ]),
], [
    ("Is thin stool always cancer?", "No, but persistent change warrants evaluation. IBD strictures are a common explanation in Crohn's disease."),
    ("Should I take laxatives to widen stool?", "Random laxatives can worsen obstruction risk if a stricture is present. Ask before self-treating."),
    ("Can stress change stool shape?", "Stress alters motility, usually temporarily. Prolonged thin stools still deserve medical review."),
], [
    "A bowel diary with shape notes helps specialists triage faster.",
    "Report new inability to pass gas immediately.",
]),
"biologics-flying-travel-ibd": entry([
    ("Planning medications before flights", [
        "Carry injectable biologics in hand luggage with prescription labels and a clinician travel letter. Checked baggage temperature extremes can ruin medication.",
        "Cool packs and insulated travel cases should meet airline guidelines. TSA generally allows medically necessary liquids after screening.",
        "Bring extra doses if trip length crosses injection day. Time zones shift schedules slightly; confirm acceptable windows.",
    ]),
    ("Airport security and documentation", [
        "Declare medical supplies calmly at security. Original packaging speeds inspection compared with loose syringes.",
        "Letters stating medical necessity and generic names help international travel. Translate key lines if needed.",
        "Travel insurance that covers IBD flares and medication loss reduces financial stress abroad.",
    ]),
    ("Health precautions while flying", [
        "Cabin air is dry. Hydrate steadily if your team allows fluids, especially after diarrhea-heavy weeks.",
        "Deep vein thrombosis risk rises on long flights, particularly with active inflammation or steroids. Walk aisles and consider compression socks if approved.",
        "Avoid starting brand-new foods the day before travel. Familiar meals lower gut surprises mid-flight.",
    ]),
    ("If symptoms flare away from home", [
        "Know how to reach your home GI on-call service and local emergency options. Embassy lists help in foreign countries.",
        "Carry a short medical summary, medication list, and insurance card copies. Translation apps assist in pharmacies.",
        "Refill early before extended trips. Shipping biologics internationally is difficult and slow.",
    ]),
], [
    ("Can biologics go through X-ray machines?", "Manufacturer guidance varies. Ask your specialty pharmacy about storage during security screening."),
    ("Should I inject during the flight?", "Timing is personal and clinical. Bathroom space and jet lag matter. Plan with your team before departure."),
    ("Do I need vaccines before travel?", "Live vaccines may be restricted on biologics. Plan travel vaccines weeks ahead with your clinician."),
], [
    "Screenshot your infusion or pharmacy support number before leaving Wi-Fi.",
    "Seat aisle requests improve bathroom access on long routes.",
]),
"floating-stool-ibd": entry([
    ("What makes stool float", [
        "Gas trapped in stool, high fiber meals, or malabsorbed fat can cause floating stools. Occasional floaters are usually benign.",
        "Persistent greasy, foul-smelling stools that float and stick to the bowl suggest fat malabsorption. Pancreatic insufficiency and small bowel Crohn's enter the differential.",
        "Sudden changes lasting more than a week deserve mention at your GI visit.",
    ]),
    ("IBD-related malabsorption patterns", [
        "Active small bowel inflammation reduces bile acid and enzyme absorption. Resection length matters for chronic steatorrhea.",
        "Celiac disease overlap should be screened before blaming floating stool on IBD alone.",
        "Weight loss, bloating, and vitamin deficiencies alongside floating stool increase urgency of workup.",
    ]),
    ("Tests your clinician may order", [
        "Stool elastase or fat quantification assesses pancreatic function. Hydrogen breath tests evaluate carbohydrate malabsorption.",
        "Vitamin A, D, E, K levels reflect fat-soluble vitamin loss. Supplementation may follow confirmed deficiency.",
        "Imaging evaluates Crohn's extent when symptoms and labs suggest small bowel disease.",
    ]),
    ("Nutrition support when malabsorption is confirmed", [
        "Medium-chain triglyceride oils and enzyme replacement help some patients under dietitian care. Random fat restriction without guidance can worsen weight loss.",
        "Smaller, more frequent meals reduce post-meal urgency and bloating.",
        "Track response to pancreatic enzyme trials over several weeks, not days.",
    ]),
], [
    ("Does floating stool mean cancer?", "Usually not. Diet and gas explain many cases. Persistent greasy stools still need professional evaluation."),
    ("Will probiotics fix floating stool?", "They might help functional gas but not structural malabsorption. Targeted diagnosis comes first."),
    ("Should I cut all fat?", "Avoid self-prescribed zero-fat diets. Healthy fats support calories when inflammation is controlled."),
], [
    "Note whether stool clears the bowl or leaves an oily film.",
    "Bring dietary fat logs to nutrition appointments.",
]),
"pale-clay-stool-ibd": entry([
    ("Bile flow and stool color basics", [
        "Brown stool color largely comes from bile pigments. Pale, gray, or clay-colored stools can mean reduced bile reaching the intestine.",
        "Temporary color changes after bismuth medicines or some antibiotics happen. Review new medicines when color shifts.",
        "One pale stool without other symptoms may be incidental. Persistent change needs medical review.",
    ]),
    ("Connections to liver and bile-duct disease", [
        "Primary sclerosing cholangitis and bile-duct obstruction are considered when pale stool pairs with dark urine or jaundice.",
        "Gallstones and pancreatic head problems also alter bile flow. Abdominal pain and itching add context.",
        "IBD patients with PSC require coordinated hepatology follow-up.",
    ]),
    ("When to seek urgent care", [
        "Yellowing eyes, severe itching, fever, and right-upper pain with pale stool suggest cholangitis or obstruction. Use emergency pathways.",
        "Weight loss and light stools in older adults prompt expedited imaging discussions.",
        "Do not wait for routine appointments if systemic symptoms are accelerating.",
    ]),
    ("Workup and monitoring themes", [
        "Blood tests for bilirubin, alkaline phosphatase, and liver enzymes are common first steps. Ultrasound or MRCP may follow.",
        "Stool color photos help clinicians but do not replace labs. Bring a brief timeline.",
        "Treatment targets the underlying cause, not color alone.",
    ]),
], [
    ("Can food make stool pale?", "High fat meals or barium tests temporarily change appearance. Sustained clay color is different."),
    ("Is pale stool common in UC?", "Not typical unless bile flow is affected. Mention it even if gut symptoms feel stable."),
    ("Should I take liver cleanses?", "Avoid unregulated detox products. They can harm the liver and delay real diagnosis."),
], [
    "Stop bismuth products before worrying about color if your clinician agrees.",
    "Track urine color on the same days as pale stools.",
]),
"enteral-nutrition-after-ibd-surgery": entry([
    ("Why enteral nutrition appears after surgery", [
        "After some bowel surgeries, clinicians rest the gut briefly then advance nutrition through tubes or sips. Enteral feeding supports healing when oral intake is limited.",
        "Protein and calorie goals are higher during recovery. Malnutrition slows wound healing and immune recovery.",
        "Your surgical team coordinates with dietitians to choose formula type and rate.",
    ]),
    ("Tube types and transition home", [
        "Nasogastric tubes are short-term bridges. Gastrostomy tubes may support longer nutritional rehabilitation in select cases.",
        "Learning flushing, pump settings, and clog prevention empowers caregivers before discharge.",
        "Oral diet reintroduction happens in stages as ileus resolves and appetite returns.",
    ]),
    ("Managing taste fatigue and tolerance", [
        "Continuous drip feeds differ from bolus schedules in bloating and nausea. Adjustments are common in the first weeks.",
        "Room temperature formula and smaller boluses help some patients. Report reflux or aspiration symptoms immediately.",
        "Bowel output changes on formula. Hydration and electrolyte monitoring continue in clinic follow-up.",
    ]),
    ("Long-term nutrition goals", [
        "The aim is usually return to oral eating when safe. Tubes are tools, not failures.",
        "Micronutrient labs guide supplementation after resections. B12, iron, and vitamin D are frequent topics.",
        "Physical therapy and gradual activity rebuild muscle lost during hospitalization.",
    ]),
], [
    ("Is enteral nutrition only for children?", "No. Adults use it around surgery and severe malnutrition too."),
    ("Can I eat while on tube feeds?", "Sometimes clinicians allow sips or meals alongside tubes. Follow your center's advancement protocol."),
    ("What if formula causes diarrhea?", "Rate, osmolality, or formula protein source may change. Call the nutrition team rather than stopping feeds."),
], [
    "Label tubing dates and flush volumes on a kitchen whiteboard.",
    "Keep spare extension sets for travel to clinic appointments.",
]),
"high-calprotectin-what-next": entry([
    ("What elevated calprotectin suggests", [
        "Fecal calprotectin measures neutrophil protein in stool, a marker of intestinal inflammation. Elevated values often correlate with active IBD but can rise with infections and NSAID use.",
        "A single high result is a conversation starter, not an automatic treatment change. Trends and symptoms matter equally.",
        "Bring recent medicines, including ibuprofen, to interpretation visits.",
    ]),
    ("Steps clinicians commonly take", [
        "Repeat testing after obvious infections clear or NSAIDs stop may be requested. Persistent elevation prompts colonoscopy or imaging.",
        "Symptom review covers stool frequency, blood, pain, and weight. Quiet symptoms with high calprotectin still deserve attention.",
        "Therapeutic drug monitoring for biologics may follow if inflammation is suspected despite adherence.",
    ]),
    ("Patient actions while waiting for plans", [
        "Do not change doses alone. Partial adherence falsely suggests treatment failure.",
        "Log symptoms daily so appointments reflect recent weeks, not recall bias.",
        "Ask what result threshold your clinic uses for escalation. Numbers vary by lab.",
    ]),
    ("When calprotectin stays high in remission", [
        "Microscopic inflammation can exist with mild symptoms. Long-term cancer surveillance and therapy goals may shift.",
        "Alternative diagnoses like microscopic colitis are considered in selected cases.",
        "Shared decision making balances drug risks against ongoing inflammation.",
    ]),
], [
    ("Can stress raise calprotectin?", "Major stress does not typically spike calprotectin like active inflammation. Still report life changes."),
    ("Should I retest at home weekly?", "Home kits exist but follow clinician cadence. Over-testing can cause anxiety without benefit."),
    ("Does a normal calprotectin mean I can stop meds?", "Not automatically. Endoscopic remission and history guide maintenance therapy."),
], [
    "Save lab PDFs in one folder for trend review.",
    "Ask whether CRP adds information when calprotectin disagrees with symptoms.",
]),
"crp-normal-still-symptoms-ibd": entry([
    ("Limits of blood inflammation markers", [
        "CRP reflects systemic inflammation but not everyone with active IBD has high CRP. Small bowel disease and isolated rectal inflammation may show normal blood tests.",
        "Normal CRP does not prove you are imagining symptoms. It means this particular marker is not elevated at that moment.",
        "Calprotectin, imaging, and endoscopy provide complementary information.",
    ]),
    ("Non-inflammatory symptom sources", [
        "Irritable bowel syndrome overlap, bile acid diarrhea, and pelvic floor dysfunction cause significant symptoms with quiet labs.",
        "Scarring and strictures produce pain or bloating without high inflammatory markers.",
        "Functional symptoms are real and treatable even when CRP is normal.",
    ]),
    ("Medication and absorption factors", [
        "Partial therapeutic drug levels may allow localized symptoms. Anti-drug antibodies are worth checking on biologics.",
        "Anemia, thyroid disease, and vitamin deficiencies mimic flares. Expand labs when gut markers disagree with how you feel.",
        "Recent steroid tapers can cause aches and fatigue without CRP rise.",
    ]),
    ("Advocating effectively in clinic", [
        "Bring symptom diaries and photos of rashes or joint swelling. Extrintestinal activity may explain discordant labs.",
        "Ask explicitly whether endoscopy or MRI is indicated when symptoms persist.",
        "Second opinions are reasonable when disability from symptoms outpaces test findings.",
    ]),
], [
    ("Should I demand steroids if CRP is normal?", "Treatment should match disease evidence, not one lab. Your clinician may pursue deeper testing first."),
    ("Can diet fix normal CRP symptoms?", "Diet helps functional overlap but cannot replace evaluation for ongoing inflammation."),
    ("Is normal CRP good enough for remission?", "Many teams want calprotectin or endoscopy confirmation for complete remission goals."),
], [
    "Track extraintestinal symptoms on the same calendar as stools.",
    "Note whether symptoms follow meals, stress, or menstrual cycles.",
]),
"green-stool-ibd": entry([
    ("Common benign causes", [
        "Rapid transit can leave bile pigments less broken down, producing green stool. Large leafy salads, green food coloring, and iron supplements also tint color.",
        "After diarrhea flares, green stool often reflects speed rather than new disease.",
        "Single green stools after holiday meals rarely need workup.",
    ]),
    ("When to mention green stool to your GI team", [
        "Persistent green greasy stools with weight loss suggest malabsorption evaluation.",
        "Green stool with blood, fever, or severe pain belongs in urgent symptom review.",
        "New antibiotics can change flora and color temporarily. Note start dates.",
    ]),
    ("Tracking context that helps", [
        "Record meals with green dyes, supplements, and bowel movement frequency.",
        "Bristol stool type adds detail beyond color alone.",
        "Photos are optional; descriptions usually suffice.",
    ]),
    ("Treatment follows underlying cause", [
        "Active inflammation is treated medically. Color often normalizes as transit slows.",
        "If infection is found, targeted antibiotics matter. Probiotics are optional discussions.",
        "Avoid assuming green means infection without testing.",
    ]),
], [
    ("Does green stool mean infection?", "Sometimes, but diet and transit are common causes. Testing clarifies when other symptoms appear."),
    ("Can iron cause green stool?", "Yes, especially liquid formulations. Mention supplements at visits."),
    ("Should I stop vegetables if stool turns green?", "Not without guidance. Vegetables support nutrition in remission for many patients."),
], [
    "Note whether green color follows fast food or artificial dyes.",
    "Hydration helps when rapid transit follows diarrhea flares.",
]),
}
