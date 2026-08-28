"""Extra sections part 2 for batch-1 slugs."""
from __future__ import annotations


def register(E):
    entries = {
        "icn-health-literacy-toolkit-ibd": (
            ("Teaching teens to read lab printouts", [
                "Highlight which values your clinic texts about versus which are informational only.",
                "Practice pronouncing drug names before appointments to reduce intimidation.",
                "Store glossary pages from the toolkit in phone notes for quick reference.",
            ]),
            ("Partnering with nurses for plain-language summaries", [
                "Ask nurses to recap visit plans in writing when medical terms pile up.",
                "Request interpreter services when family language preferences differ from chart language.",
                "Repeat back instructions before leaving clinic to confirm understanding.",
            ]),
        ),
        "icn-ibd-holidays-special-occasions": (
            ("Hosting gatherings when you have IBD", [
                "Offer to bring a safe main dish so you know at least one plate works for your gut.",
                "Plan recovery naps after long social days even when you feel okay midday.",
                "Keep electrolyte drinks stocked when holiday foods are saltier than usual.",
            ]),
            ("Traveling to relatives out of town", [
                "Research infusion centers and ER locations near relatives before booking tickets.",
                "Ship biologics ahead when flying with cold packs is stressful.",
                "Share a concise medical summary with a trusted relative in case you need help.",
            ]),
        ),
        "icn-transfer-toolkit-adult-care": (
            ("Insurance literacy during transition", [
                "Learn prior authorization steps before parents lose dependent coverage at age limits.",
                "Understand copay accumulator policies that affect manufacturer card benefits.",
                "Save specialty pharmacy apps on your phone with login credentials secured.",
            ]),
            ("Building an adult care team locally", [
                "Interview adult gastroenterologists about after-hours coverage and infusion access.",
                "Transfer records six to eight weeks before last pediatric visit to avoid gaps.",
                "Schedule first adult visit while still connected to pediatric team for warm handoff.",
            ]),
        ),
        "osteoporosis-bone-health-ibd": (
            ("Fall prevention at home and outdoors", [
                "Remove tripping hazards and use night lights when steroid courses affect balance.",
                "Wear supportive shoes on icy or uneven surfaces if neuropathy or weakness coexist.",
                "Discuss hip protector garments if prior fractures occurred.",
            ]),
            ("Monitoring response to bone therapy", [
                "Repeat DEXA on schedule your endocrinologist sets, often every one to two years.",
                "Report dental extractions before IV bisphosphonates due to jaw osteonecrosis risk.",
                "Track height loss at annual visits in teens and adults on long steroids.",
            ]),
        ),
        "icn-self-management-handbook-ibd": (
            ("Using symptom zones green yellow red", [
                "Define personal green zone activities you can do without restriction during stable weeks.",
                "Yellow zone triggers earlier nursing calls or diet adjustments before ER needs arise.",
                "Red zone symptoms match emergency instructions your clinician provides in writing.",
            ]),
            ("Sharing handbook progress with clinicians", [
                "Bring completed module summaries to visits to focus discussion efficiently.",
                "Note barriers like cost or transportation that block handbook goals so social work can help.",
                "Revise goals after major surgery or therapy class changes.",
            ]),
        ),
        "immunosuppressants-ibd-basics": (
            ("Lab monitoring routines on thiopurines", [
                "Schedule CBC and liver tests on calendar alerts tied to refill dates.",
                "Report fever or mouth sores before next labs if they occur between visits.",
                "Ask whether home phlebotomy is available if clinic trips are burdensome.",
            ]),
            ("Travel and sick-day rules on immunomodulators", [
                "Carry a medication list translating generic and brand names for international travel.",
                "Ask whether to hold doses during serious infections per written sick-day plan.",
                "Wear medical alert jewelry if severe allergy or adrenal issues coexist.",
            ]),
        ),
        "lupus-autoimmune-basics": (
            ("Sun protection as daily medicine", [
                "Broad-spectrum SPF, hats, and shade reduce lupus flares triggered by ultraviolet light.",
                "Some IBD patients on photosensitive drugs share similar needs; combine strategies.",
                "Review medication lists for drugs that add sun sensitivity beyond lupus itself.",
            ]),
            ("Kidney and blood pressure monitoring", [
                "Home blood pressure cuffs help when lupus nephritis requires tight control.",
                "Bring urine dipstick logs if nephrology requested home monitoring.",
                "Report swelling in legs or sudden weight gain promptly.",
            ]),
        ),
        "ibd-extraintestinal-manifestations": (
            ("Creating a specialist contact sheet", [
                "List ophthalmology, rheumatology, dermatology, and hepatology numbers in one note.",
                "Specify which symptoms route to which specialist to reduce phone tag.",
                "Update sheet after insurance changes alter provider networks.",
            ]),
            ("When EIMs appear before gut diagnosis", [
                "Some patients present with joint or eye disease years before IBD is recognized.",
                "Tell all specialists about bowel symptoms even if mild when evaluating EIMs.",
                "Family history of psoriasis or spondylitis raises suspicion for gut overlap.",
            ]),
        ),
        "icn-mental-health-provider-guide": (
            ("Interview questions for prospective therapists", [
                "Ask whether they treat chronic illness coping and medical trauma regularly.",
                "Confirm telehealth availability if travel to infusion centers consumes time.",
                "Discuss session frequency and crisis coverage before committing.",
            ]),
            ("Integrating therapy with medical adherence", [
                "Therapists can help build routines for injections without shame about needle fear.",
                "Share therapy goals with GI team only with your written consent.",
                "Combine therapy with peer support for layered resilience.",
            ]),
        ),
        "how-to-read-colonoscopy-report-ibd": (
            ("Understanding prep and incomplete segments", [
                "Segments labeled not visualized may need repeat scope after better prep.",
                "Ask whether retroflexion in rectum was performed when bleeding persists.",
                "Poor prep does not mean your clinician blames you; it guides timing of repeats.",
            ]),
            ("Linking report language to treatment choices", [
                "Active ulceration may prompt steroid bridge or biologic escalation.",
                "Scarring and strictures change diet and dilation plans differently from active ulcers.",
                "Request drawing or diagram if anatomy terms confuse you.",
            ]),
        ),
        "icn-college-ibd-toolkit": (
            ("Infirmary and disability office coordination", [
                "Introduce yourself to campus health before crises so records are on file.",
                "Give disability office clinician letter updates annually before syllabus week.",
                "Confirm whether infirmary stocks biologics or only refers outward.",
            ]),
            ("Managing midterm flares academically", [
                "Incomplete policies differ by professor; disability office centralizes letters.",
                "Online exam proctoring may allow bathroom breaks when documented.",
                "Plan lighter course loads during infusion-heavy semesters if possible.",
            ]),
        ),
        "perianal-crohns-fistula-abscess": (
            ("Sitz baths and wound care routines", [
                "Warm water soaks two to three times daily may soothe after drainage procedures.",
                "Pat dry gently; aggressive wiping worsens fissures adjacent to fistulas.",
                "Use barrier creams recommended by colorectal team, not random diaper creams.",
            ]),
            ("Communication with colorectal surgeons", [
                "Describe drainage color, odor changes, and fever at each follow-up.",
                "MRI results may guide seton adjustments; ask for copy in patient portal.",
                "Smoking cessation counseling improves fistula healing odds substantially.",
            ]),
        ),
        "icn-caregiver-coping-resource": (
            ("Sibling and extended family inclusion", [
                "Explain IBD briefly to siblings so secrecy does not breed fear.",
                "Grandparents can help logistics but should follow medical boundaries parents set.",
                "Family meetings with social worker mediate when relatives disagree on diet rules.",
            ]),
            ("Caregiver health maintenance", [
                "Keep your own primary care visits and screenings current while managing pediatric IBD.",
                "Exercise and sleep protect caregivers from burnout-related illness.",
                "Respite nights from trusted relatives prevent chronic exhaustion.",
            ]),
        ),
        "icn-lifestyle-ibd-toolkit": (
            ("Completing modules without overwhelm", [
                "Finish one module weekly instead of bingeing all sections before visits.",
                "Pause modules during hospitalization and resume when home routines stabilize.",
                "Share completion certificates with school nurses if they motivate teens.",
            ]),
            ("Linking lifestyle changes to quality metrics", [
                "Track sleep and hydration modules alongside symptom apps for richer visit data.",
                "Discuss unrealistic module goals with nurse if they increase anxiety.",
                "Celebrate small streaks to build confidence after difficult disease years.",
            ]),
        ),
        "workplace-school-ibd-rights": (
            ("Documenting accommodations in writing", [
                "Verbal promises from managers fail without HR or disability office confirmation.",
                "Specify bathroom proximity, remote days, and flexible start times clearly.",
                "Renew accommodations annually even if symptoms improved recently.",
            ]),
            ("Handling discrimination calmly", [
                "Keep email trails when requests are denied or mocked.",
                "EEOC deadlines apply in US workplaces; legal aid clinics advise low-cost options.",
                "Union stewards may assist with collective bargaining health clauses.",
            ]),
        ),
        "colonoscopy-prep-ibd": (
            ("Managing prep with prior vomiting or nausea", [
                "Split-dose prep with anti-nausea premeds helps many IBD patients complete intake.",
                "Sip through a straw and chase with clear sports drinks if taste triggers gag reflex.",
                "Call endoscopy nurses if you vomit more than one prep dose; they may adjust timing.",
            ]),
            ("Post-procedure pain expectations", [
                "Gas pain from insufflation resolves with walking and time for most patients.",
                "Report severe abdominal pain unlike prior scopes immediately.",
                "Resume diet per written instructions, often gradual after polypectomy.",
            ]),
        ),
        "hydration-tips-ibd": (
            ("Electrolyte choices by situation", [
                "Oral rehydration solutions beat soda for sodium replacement during high output days.",
                "Limit pure water alone when output exceeds three liters daily to avoid hyponatremia risk.",
                "Coconut water lacks ideal sodium for severe losses; ask clinic for preferred products.",
            ]),
            ("Hydration during exercise and heat", [
                "Weigh before and after workouts if ileostomy output rises with activity.",
                "Schedule outdoor exercise in cooler hours during humid summers.",
                "Carry electrolyte packets in gym bags and school backpacks.",
            ]),
        ),
        "nsaids-ibd-risk": (
            ("Documenting NSAID allergy or intolerance", [
                "Medical alert bracelets note ibuprofen avoidance when reactions were severe.",
                "Tell physical therapists and dentists before they recommend NSAID creams or pills.",
                "Keep acetaminophen dosing chart on fridge when children share household.",
            ]),
            ("Migraine and menstrual pain alternatives", [
                "Discuss triptans, hormonal options, or acetaminophen plans with clinicians for cycle pain.",
                "Heat packs and PT help some joint pains without oral NSAIDs.",
                "Report any NSAID trial symptoms within forty-eight hours to your GI team.",
            ]),
        ),
        "psoriasis-ibd-connection": (
            ("Skin care while on biologics", [
                "Moisturize plaques and monitor for infection signs when scratching breaks skin.",
                "Phototherapy schedules coordinate with IBD visits to reduce travel burden.",
                "Biologic injection sites rotate separately from psoriasis biologic sites when two drugs used.",
            ]),
            ("Avoiding conflicting prescriptions", [
                "Do not start IL-17 psoriasis drugs without GI approval due to colitis flare risk.",
                "Share dermatology notes with gastroenterology after every therapy change.",
                "Topical steroid strength on large body areas still absorbs systemically; disclose use.",
            ]),
        ),
        "bathroom-urgency-anxiety-ibd": (
            ("Gradual exposure planning", [
                "List feared locations from least to most anxiety-provoking and practice visits weekly.",
                "Bring a trusted friend first time returning to triggering venues.",
                "Celebrate small wins like completing a grocery trip without incident.",
            ]),
            ("Pelvic floor therapy crossover", [
                "Hypertonic pelvic floor muscles worsen urgency; PT teaches relaxation techniques.",
                "Biofeedback complements CBT for bathroom anxiety in selected patients.",
                "Ask GI team for referral when inflammation is controlled yet urgency persists.",
            ]),
        ),
        "iron-b12-vitamin-d-ibd": (
            ("Injection schedules and labs", [
                "B12 injections may be monthly after loading doses when ileum absorption fails.",
                "Vitamin D rechecks in late winter catch seasonal drops common in northern climates.",
                "Iron infusions may repeat based on ferritin targets your hematologist sets.",
            ]),
            ("Food-first strategies when tolerated", [
                "Pair plant iron with vitamin C sources during remission expansion of diet.",
                "Fortified cereals help teens who avoid meat during flares.",
                "Fatty fish twice weekly supports vitamin D when supplements are insufficient alone.",
            ]),
        ),
        "humid-weather-ibd-symptoms": (
            ("Cooling strategies beyond air conditioning", [
                "Cooling towels and mist fans help outdoor events when AC is unavailable.",
                "Light-colored breathable fabrics reduce heat retention with ostomy appliances.",
                "Plan indoor alternatives for yard work during heat advisories.",
            ]),
            ("Recognizing heat illness versus flare", [
                "Confusion, minimal sweating, and rapid pulse suggest heat emergency needing ER care.",
                "Blood in stool still indicates IBD evaluation even during heat waves.",
                "Track symptoms indoors with AC to see if heat alone drives discomfort.",
            ]),
        ),
        "what-remission-means-ibd": (
            ("Patient-reported outcomes alongside scopes", [
                "Quality-of-life surveys capture fatigue and social function scopes miss.",
                "Share app trends when symptoms feel worse despite normal appearance on last scope.",
                "Set personal goals beyond stool form, like travel or sports participation.",
            ]),
            ("Maintenance therapy adherence in silent remission", [
                "Skipping infusions because you feel well risks antibodies and relapse.",
                "Calendar alerts for labs and scopes matter even in good years.",
                "Discuss step-down trials only with treat-to-target confirmation from your clinician.",
            ]),
        ),
        "protein-meal-plan-ibd-remission": (
            ("Batch cooking for low-energy weeks", [
                "Slow-cooker shredded chicken freezes in portions for quick remission meals.",
                "Smooth nut butters add protein to smoothies when chewing meat tires jaw muscles.",
                "Label containers with dates to rotate freezer stock safely.",
            ]),
            ("Restaurant protein choices", [
                "Grilled fish or chicken often tolerates better than fried proteins during early remission.",
                "Ask for sauces on side to control fat load that triggers diarrhea.",
                "Carry safe snacks when restaurant portions are unpredictable.",
            ]),
        ),
        "anti-inflammatory-diet-ibd": (
            ("Ultra-processed food reduction realistically", [
                "Swap sugary drinks for water or herbal tea one at a time rather than overnight overhauls.",
                "Frozen vegetables count toward anti-inflammatory plates when fresh prep is hard.",
                "Forgive imperfect weeks; long-term patterns matter more than single meals.",
            ]),
            ("Spices and herbs in everyday cooking", [
                "Turmeric, ginger, and garlic flavor food without relying on heavy cream sauces.",
                "Nightshade spices like paprika affect individuals differently; test during remission.",
                "Discuss high-dose curcumin supplements with pharmacist before starting.",
            ]),
        ),
        "j-pouch-basics-ibd": (
            ("Pouch function years after takedown", [
                "Frequency often stabilizes twelve to twenty-four months post reversal but varies lifelong.",
                "Imodium use may be scheduled before long meetings with clinician approval.",
                "Pouchitis flares need stool tests to exclude C difficile mimics.",
            ]),
            ("Fertility and obstetric planning with pouches", [
                "High-risk OB monitors pouch patients during pregnancy for obstruction symptoms.",
                "Vaginal delivery is often feasible; discuss perianal history with obstetric team.",
                "Postpartum pouch function changes may require temporary diet adjustments.",
            ]),
        ),
        "exercise-physical-activity-ibd": (
            ("Returning after hospitalization or surgery", [
                "Follow surgical clearance timelines before lifting or core strain.",
                "Start with five to ten minute walks daily and increase ten percent weekly if tolerated.",
                "Stop and call clinic if exercise triggers bleeding or severe pain.",
            ]),
            ("Hydration and ostomy supplies during sports", [
                "Drink on schedule during practices, not only when thirsty.",
                "Empty pouches before running or jumping sports to reduce leak anxiety.",
                "Support belts prevent appliance tug during yoga inversions when approved.",
            ]),
        ),
        "social-life-dating-teens-ibd": (
            ("Setting boundaries on social media", [
                "Private accounts reduce unwanted questions about weight or bathroom use.",
                "Think before posting mid-flare photos that future employers might see.",
                "Peer support groups offline often feel safer than public comment threads.",
            ]),
            ("Consent conversations about disclosure", [
                "Friends do not need full diagnosis to respect bathroom privacy requests.",
                "Practice short explanations for why you skip certain foods at parties.",
                "Counselors help rehearse dating disclosure when readiness feels unclear.",
            ]),
        ),
        "anemia-iron-deficiency-ibd": (
            ("Oral iron side effect management", [
                "Split doses morning and evening to reduce nausea on oral iron.",
                "Liquid iron stains teeth; use straws and rinse mouth after doses.",
                "Switch formulations if constipation becomes unbearable before abandoning treatment silently.",
            ]),
            ("When IV iron fits better", [
                "Active colitis, oral intolerance, or ferritin under twenty may prompt infusion.",
                "Infusion centers monitor for rare reactions during first doses.",
                "Repeat infusions scheduled when labs show incomplete repletion.",
            ]),
        ),
        "gluten-wheat-ibd": (
            ("Reintroduction trials after elimination", [
                "Reintroduce wheat on a quiet symptom week with clinician awareness.",
                "Add one wheat serving daily for three days while logging symptoms.",
                "Stop and call clinic if bleeding or severe pain returns during challenge.",
            ]),
            ("Gluten-free labeling and dining out", [
                "Ask restaurants about cross-contact if celiac is confirmed, not merely sensitivity.",
                "Gluten-free packaged foods may be low in fiber; compensate with tolerated plants.",
                "School lunch programs may accommodate celiac with documentation on file.",
            ]),
        ),
        "teen-nutrition-ibd-growth": (
            ("Growth chart reviews with parents and teens", [
                "Ask clinicians to explain height velocity graphs in plain language each visit.",
                "Celebrate growth improvements after enteral nutrition or remission induction.",
                "Address delayed puberty questions openly with pediatric endocrinology when needed.",
            ]),
            ("Sports and calorie needs", [
                "Athletic teens need higher protein and calories; dietitians adjust when flares reduce intake.",
                "Hydration plans differ for wrestlers cutting weight versus soccer midfielders.",
                "Monitor iron status when menstrual periods start during active IBD.",
            ]),
        ),
        "college-with-ibd": (
            ("Part-time enrollment and medical leave", [
                "Know difference between medical leave and dropping courses for transcript impact.",
                "Financial aid offices adjust packages when enrollment status changes mid-semester.",
                "Return plans include infusion scheduling around exam calendars.",
            ]),
            ("Roommate and resident advisor communication", [
                "Disclose only what you need for bathroom access and fridge medication storage.",
                "Resident advisors can facilitate private bathroom arrangements when medically documented.",
                "Conflict mediation helps when roommates misunderstand frequent bathroom trips.",
            ]),
        ),
        "ankylosing-spondylitis-ibd": (
            ("Morning mobility routines", [
                "Gentle stretching before getting out of bed reduces spinal stiffness for many patients.",
                "Heat showers help some; others prefer cold after exercise per physical therapy plan.",
                "Track stiffness duration in minutes for rheumatology visits.",
            ]),
            ("Imaging follow-up expectations", [
                "MRI sacroiliac joints may repeat when symptoms progress despite therapy.",
                "X-rays show damage later than MRI inflammation; both guide treatment.",
                "Report new heel pain or eye redness between scheduled visits.",
            ]),
        ),
        "mucus-urgency-tenesmus-ibd": (
            ("Rectal therapy adherence support", [
                "Set phone alarms for evening enemas when morning pills are easier to remember.",
                "Travel kits include suppositories even for short trips if tenesmus is active.",
                "Ask clinic about compounded rectal formulations if commercial enemas sting.",
            ]),
            ("Skin care with frequent wiping", [
                "Use water wipes or bidet attachments to reduce perianal skin breakdown.",
                "Barrier ointments protect skin when diarrhea is frequent.",
                "Report perianal fissures separately from tenesmus so surgeons evaluate.",
            ]),
        ),
        "ibd-pregnancy-planning": (
            ("Male partner medication review", [
                "Methotrexate and some other drugs require male washout intervals before conception attempts.",
                "Sperm banking discussions occur when gonadotoxic therapy is planned.",
                "Partners attend preconception visits when possible for unified planning.",
            ]),
            ("Obstetric monitoring during third trimester", [
                "Growth ultrasounds and blood pressure checks intensify with IBD and preterm risk factors.",
                "Report decreased fetal movement per obstetric instructions immediately.",
                "Postpartum GI follow-up scheduled before delivery when feasible.",
            ]),
        ),
        "reading-ibd-labs-calprotectin-crp": (
            ("Home calprotectin kit technique", [
                "Follow kit timing for sample collection after bowel movement, not during urination.",
                "Ship samples promptly when mail-in labs require refrigeration.",
                "Log kit results beside clinic lab results to compare trends.",
            ]),
            ("When discordant labs need repeat testing", [
                "Repeat calprotectin in two weeks if symptoms conflict with a single high value.",
                "CRP may normalize while calprotectin remains elevated in isolated gut inflammation.",
                "Ask whether blood and stool tests same day improve interpretation.",
            ]),
        ),
        "swimming-pool-beach-ibd-ostomy": (
            ("Sun and skin care at the beach", [
                "Reapply sunscreen around stoma skin and wear hats when on photosensitive medications.",
                "Rinse salt and sand gently to preserve appliance adhesion after ocean swims.",
                "Shade breaks prevent heat exhaustion when inflammation already causes fatigue.",
            ]),
            ("Public pool locker room confidence", [
                "Change appliances in accessible stalls with disposal bags packed discreetly.",
                "Many patients change before leaving home and swim for set time blocks only.",
                "Support groups share brand-specific tips for secure swimming barriers.",
            ]),
        ),
        "celiac-ibd-screening": (
            ("Maintaining gluten before blood tests", [
                "Two gluten-containing slices of bread daily for six weeks is a common rechallenge before repeat serology when prior trials were gluten-free.",
                "Discuss shorter protocols with GI if symptoms were severe on gluten.",
                "Never self-diagnose celiac without biopsy confirmation in most guidelines.",
            ]),
            ("Dual diet planning if celiac confirmed", [
                "Gluten-free whole grains prevent constipation when IBD remission expands fiber.",
                "Separate toasters and colanders reduce cross-contact at home.",
                "Annual dietitian visits monitor micronutrient levels on strict gluten-free IBD diets.",
            ]),
        ),
        "pyoderma-erythema-nodosum-ibd": (
            ("Leg elevation and compression for erythema nodosum", [
                "Elevate legs during flares to reduce shin nodule pain when safe for heart health.",
                "Compression stockings may help some patients after acute tenderness resolves.",
                "Avoid trauma to nodules; pressure from tight boots worsens pain.",
            ]),
            ("Wound clinics for pyoderma gangrenosum", [
                "Specialized wound centers co-manage immunosuppression with dermatology.",
                "Gentle non-adherent dressings protect ulcers during biologic loading periods.",
                "Photograph weekly size changes for telehealth wound reviews.",
            ]),
        ),
        "dairy-lactose-ibd": (
            ("Calcium tracking on low-dairy diets", [
                "Log calcium sources daily until habit forms after lactose reduction.",
                "Lactose-free milk retains protein and calcium for many patients.",
                "Fortified orange juice or supplements fill gaps when dietitian confirms need.",
            ]),
            ("Hidden lactose in medications and foods", [
                "Read labels for whey, milk solids, and lactose in processed meats and pills.",
                "Pharmacists identify lactose-free formulations of common medications when needed.",
                "Challenge small yogurt portions separately from milk trials to map tolerance.",
            ]),
        ),
        "icn-accommodations-toolkit-ibd": (
            ("Renewing 504 plans after therapy changes", [
                "Update plans when infusion schedules shift from every eight to every four weeks.",
                "Include telehealth infusion options if home infusion becomes medically necessary.",
                "Remove outdated restrictions that no longer match current function.",
            ]),
            ("Workplace accommodation examples beyond bathrooms", [
                "Remote work days during severe flares may be reasonable accommodations when documented.",
                "Parking proximity reduces fatigue for employees with anemia and IBD.",
                "Flexible deadlines during hospitalization prevent punitive performance reviews.",
            ]),
        ),
        "when-to-go-er-ibd": (
            ("What to pack for ER visits", [
                "Bring medication list, insurance card, recent labs, and phone charger.",
                "Save PDFs of colonoscopy reports in phone files for upload if asked.",
                "Have someone drive you when possible to advocate while you are ill.",
            ]),
            ("After ER discharge follow-through", [
                "Schedule GI follow-up within days, not weeks, after flare-related ER care.",
                "Understand which ER prescriptions replace home meds temporarily.",
                "Ask whether stool tests sent from ER need result follow-up with GI.",
            ]),
        ),
        "psc-ibd-liver": (
            ("Colon surveillance intensity with PSC", [
                "Annual or more frequent colonoscopy may apply even when colitis symptoms are mild.",
                "Biopsies screen for dysplasia earlier than standard colitis protocols.",
                "Transition surveillance schedules when liver transplant listing occurs.",
            ]),
            ("Cholangitis episode recognition", [
                "Fever, jaundice, and right upper quadrant pain triad needs urgent hepatology contact.",
                "Blood cultures and antibiotics start quickly in cholangitis emergencies.",
                "Keep hepatology after-hours numbers accessible during travel.",
            ]),
        ),
        "uveitis-eye-inflammation-ibd": (
            ("Eye drop adherence and technique", [
                "Wash hands and avoid bottle tip contact with lashes to prevent contamination.",
                "Space steroid drops from glaucoma screening visits when on long courses.",
                "Never share eye drops between family members.",
            ]),
            ("Driving and work safety during flares", [
                "Blurry vision may require time off driving until ophthalmology clears you.",
                "Adjust screen brightness and take breaks when photophobia flares during work.",
                "Inform employers only as needed for safety accommodations.",
            ]),
        ),
        "ibd-autoimmune-overlap": (
            ("Unified vaccination planning", [
                "One spreadsheet tracking vaccines satisfies multiple specialists reviewing records.",
                "Ask which specialist orders live vaccines before biologics when overlap exists.",
                "Travel vaccine appointments consolidate questions from rheumatology and GI.",
            ]),
            ("Avoiding duplicate testing", [
                "Share recent labs across portals when systems connect to reduce blood draws.",
                "Clarify which specialist owns each monitoring lab to prevent gaps or duplication.",
                "Bring outside records on USB or paper when changing centers.",
            ]),
        ),
        "steroid-taper-what-to-expect-ibd": (
            ("Adrenal insufficiency sick-day rules", [
                "Vomiting or surgery during taper may require stress-dose steroids per endocrinology card.",
                "Medical alert jewelry lists adrenal insufficiency when prolonged steroids occurred.",
                "Keep emergency hydrocortisone injection if prescribed and train family on use.",
            ]),
            ("Joint aches during low prednisone doses", [
                "Temporary arthralgia near taper end is common and distinguishes from new RA flares with swelling.",
                "Log pain location and swelling photos for clinician review before assuming flare.",
                "Physical activity gentle movement may ease steroid withdrawal aches when approved.",
            ]),
        ),
        "high-school-ibd-survival-guide": (
            ("Standardized testing accommodations", [
                "SAT and ACT extended time requires separate documentation from daily 504 plans.",
                "Start paperwork junior year before registration deadlines.",
                "Practice tests under accommodation conditions to build stamina.",
            ]),
            ("Athletics and PE modifications", [
                "Modified PE credits still count toward graduation when medically necessary.",
                "Coach communication includes hydration and bathroom access without sharing entire chart.",
                "Return-to-play after surgery follows surgeon and pediatric GI clearance jointly.",
            ]),
        ),
        "gas-bloating-ibd": (
            ("Low FODMAP overlap cautions", [
                "Temporary FODMAP reduction may help bloating but should not replace inflammation treatment.",
                "Reintroduce FODMAP groups systematically with dietitian to avoid permanent over-restriction.",
                "Do not assume bloating means IBS alone when calprotectin is unchecked.",
            ]),
            ("Movement and posture relief", [
                "Short walks after meals reduce gas retention for some patients.",
                "Yoga poses recommended by PT may help pelvic floor related bloating.",
                "Avoid tight waistbands during painful distension episodes.",
            ]),
        ),
        "constipation-ibd-causes": (
            ("Pelvic floor biofeedback basics", [
                "Biofeedback teaches relaxation of pelvic muscles that paradoxically block evacuation.",
                "Sessions are non-invasive and complement medical treatment of strictures.",
                "Ask for referral when digital rectal exam suggests dyssynergia.",
            ]),
            ("Laxative trials with clinician guidance", [
                "Polyethylene glycol trials need hydration and timing instructions in writing.",
                "Stop and call clinic if cramping worsens or vomiting starts on laxatives.",
                "Do not stack multiple laxatives without phone approval during stricture history.",
            ]),
        ),
        "remicade-infusion-day-tips-ibd": (
            ("Pre-medication and reaction history", [
                "Tell nurses about prior infusion reactions even if mild so premeds adjust.",
                "Antihistamines may cause drowsiness; plan rides accordingly first sessions.",
                "Report chest pain or throat tightness immediately during infusion.",
            ]),
            ("Productivity and comfort in the chair", [
                "Compression socks reduce leg swelling during long infusions for some patients.",
                "Snack choices follow center policy; bring clear fluids if allowed.",
                "Use restroom before line placement when bladder urgency is high.",
            ]),
        ),
        "stelara-diet-ibd": (
            ("Subcutaneous injection site rotation", [
                "Rotate thighs and abdomen sites to reduce lipohypertrophy nodules.",
                "Allow refrigerated pens to warm slightly before injection to reduce sting per label.",
                "Report persistent injection site reactions separately from gut symptoms.",
            ]),
            ("Nutrition while starting ustekinumab", [
                "No mandatory fasting around injections; maintain adequate calories during induction.",
                "Continue malabsorption monitoring early in therapy when weight gain begins.",
                "Alcohol moderation discussions continue with liver and disease context.",
            ]),
        ),
        "fodmap-diet-crohns-colitis": (
            ("Monash app and serving sizes", [
                "Serving size matters on FODMAP lists; small onion portions may tolerate while large do not.",
                "Use dietitian interpretation rather than app flags alone during IBD care.",
                "Track symptoms alongside FODMAP reintroduction in one journal.",
            ]),
            ("Exiting low FODMAP safely", [
                "Set reintroduction end dates to prevent years of unnecessary restriction.",
                "Reintroduce during remission weeks for clearest interpretation.",
                "Share reintroduction results with GI team to separate FODMAP triggers from inflammation.",
            ]),
        ),
    }

    for slug, pair in entries.items():
        E(slug, pair[0], pair[1])
