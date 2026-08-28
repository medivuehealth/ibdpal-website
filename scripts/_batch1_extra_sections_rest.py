"""Register extra sections for remaining batch-1 slugs."""
from __future__ import annotations


def register(E):
    entries = {
        "stress-autoimmune-symptoms": (
            ("Sleep and circadian rhythm as stress medicine", [
                "Poor sleep amplifies pain sensitivity and next-day urgency for many IBD patients. Fixed wake times and morning light help more than random sleep-ins.",
                "Night sweats or frequent bathroom trips deserve medical review rather than assuming they are only anxiety.",
                "Discuss melatonin or prescription sleep aids with your clinician if insomnia persists beyond two weeks during stable disease.",
            ]),
            ("Building a flare-season stress plan", [
                "Before exam periods or holidays, write a one-page plan listing who to call, safe foods, and rest breaks.",
                "Delegate one non-medical task weekly so your energy budget includes recovery, not only obligations.",
                "Review the plan with your GI team after stressful seasons to capture what worked.",
            ]),
        ),
        "alcohol-caffeine-ibd": (
            ("Tracking personal tolerance over time", [
                "Tolerance can change after surgery, medication switches, or remission. Retest small amounts only when your clinician agrees disease is stable.",
                "Log drink type, volume, food context, and symptoms for 48 hours after social events.",
                "Share the log at visits instead of relying on memory during rushed appointments.",
            ]),
            ("Hydration when caffeine or alcohol is used", [
                "Alternate water with coffee or alcoholic drinks when you choose to consume them.",
                "Dehydration worsens headache and bowel symptoms the day after social drinking.",
                "Oral rehydration solutions help some patients more than plain water after high-output days.",
            ]),
        ),
        "gut-microbiome-autoimmune": (
            ("Fiber, fermentation, and symptom experiments", [
                "Introduce fermented foods one at a time during remission to see personal tolerance.",
                "Pause experiments during flares so you and your clinician can interpret symptoms clearly.",
                "Record portion size because dose-dependent reactions are common with onions and beans.",
            ]),
            ("Questions to ask before buying microbiome products", [
                "Ask whether a product strain was studied in peer-reviewed IBD trials, not only general wellness ads.",
                "Request interaction checks with your biologic or thiopurine before starting new supplements.",
                "Save money on unvalidated stool tests unless your specialist orders them for a defined purpose.",
            ]),
        ),
        "multiple-sclerosis-autoimmune-basics": (
            ("Coordinating MRIs and colonoscopy schedules", [
                "Sedation plans for endoscopy may need adjustment when MS fatigue or mobility aids are present.",
                "Tell imaging centers about bladder urgency needs before long MRI sessions without breaks.",
                "Your neurologist and gastroenterologist can align monitoring calendars to reduce duplicate blood draws.",
            ]),
            ("Fatigue management across two chronic conditions", [
                "Pacing plans should account for both MS heat sensitivity and IBD bathroom needs.",
                "Occupational therapy evaluates home setups for fatigue and mobility together.",
                "Report new weakness or vision changes promptly rather than attributing everything to IBD flares.",
            ]),
        ),
        "flare-first-48-hours": (
            ("Food and rest in the first two days", [
                "Bland, low-residue meals may reduce mechanical irritation while you await clinician guidance.",
                "Avoid aggressive exercise during acute symptoms; gentle walking and stretching are usually enough.",
                "Children and older adults dehydrate faster and need lower thresholds for outreach.",
            ]),
            ("Preparing for the clinic callback", [
                "Have pharmacy phone numbers and insurance card photos ready before nursing calls return.",
                "Note whether symptoms differ from prior flares in location, blood amount, or fever.",
                "Ask about stool tests for infection if antibiotics or travel preceded the flare.",
            ]),
        ),
        "autoimmune-diet-myths": (
            ("Spotting red flags in diet marketing", [
                "Claims of curing lupus, colitis, or RA in thirty days are not supported by rigorous trials.",
                "Influencer labs selling IgG food panels often lack clinical utility for autoimmune management.",
                "Bring supplement ads to visits so your clinician can review ingredients for interactions.",
            ]),
            ("Building evidence-based eating habits", [
                "Adequate protein, calcium, vitamin D, and hydration matter more than exotic superfoods.",
                "Cook more meals at home when possible without demanding perfection every night.",
                "Work with a registered dietitian when elimination lists grow beyond a single page.",
            ]),
        ),
        "mediterranean-diet-autoimmune": (
            ("Adapting Mediterranean meals during school and work weeks", [
                "Pack olive oil dressings separately and assemble salads at lunch to prevent sogginess.",
                "Canned fish and frozen vegetables make Mediterranean patterns feasible on busy flare-recovery weeks.",
                "Batch cook grains on weekends if weekday fatigue limits cooking.",
            ]),
            ("Combining Mediterranean eating with IBD medications", [
                "Grapefruit interactions are uncommon with most IBD biologics but matter for some cholesterol drugs.",
                "Separate high-calcium foods from levothyroxine and some antibiotics by several hours when applicable.",
                "Ask whether omega-3 supplements add value if you already eat fish twice weekly.",
            ]),
        ),
        "sjogren-autoimmune-overview": (
            ("Dental prevention with dry mouth", [
                "Fluoride trays and more frequent dental cleanings reduce cavity risk when saliva is low.",
                "Sugar-free gum and xylitol lozenges stimulate limited saliva between meals.",
                "Tell your dentist about immunosuppression before invasive procedures.",
            ]),
            ("Swallowing pills and nutrition with IBD overlap", [
                "Splitting or liquid formulations may help when dry mouth and IBD both affect intake.",
                "Report weight loss to both rheumatology and gastroenterology teams promptly.",
                "Soft, sauced foods improve intake when chewing dry textures is difficult.",
            ]),
        ),
        "hashimotos-thyroid-autoimmune": (
            ("Monitoring beyond TSH alone", [
                "Symptoms may lag lab normalization by weeks after levothyroxine dose changes.",
                "Repeat labs six to eight weeks after adjustments unless your clinician orders sooner.",
                "Pregnancy plans require tighter targets and more frequent testing.",
            ]),
            ("When gut and thyroid symptoms overlap", [
                "Constipation from hypothyroidism can mimic stricturing Crohn's patterns until labs clarify.",
                "Malabsorption in ileal disease affects levothyroxine absorption; dose tweaks may follow healing.",
                "Bring a list of all medications and supplements to endocrine visits for interaction review.",
            ]),
        ),
        "insurance-biologics-ibd": (
            ("Documenting medical necessity clearly", [
                "Colonoscopy reports, calprotectin trends, and hospitalization records strengthen appeals.",
                "Patient impact statements describing work or school disability add human context to charts.",
                "Date every denial letter and track appeal deadlines meticulously.",
            ]),
            ("Preventing gaps during job or plan changes", [
                "COBRA and special enrollment periods have strict clocks; involve HR early when leaving jobs.",
                "Ask specialty pharmacy to sync shipments before deductible resets change copays.",
                "Keep a photo of your active insurance card and member services number on your phone.",
            ]),
        ),
        "ostomy-basics-ibd": (
            ("Travel and supply planning", [
                "Pack double your usual appliance count for trips because humidity and activity shorten wear time.",
                "Carry disposal bags and wipes for flights and road trips where trash access is limited.",
                "Know how to order emergency supplies from vendors with weekend shipping options.",
            ]),
            ("Returning to intimacy and body image", [
                "Empty or change pouches before intimacy if that increases comfort and confidence.",
                "Counselors familiar with medical trauma help partners communicate without shame.",
                "Ostomy nurses suggest wraps and clothing styles that reduce noise concerns in quiet settings.",
            ]),
        ),
        "fiber-and-ibd-diet": (
            ("Soluble versus insoluble choices in remission", [
                "Oats, peeled apples, and psyllium may firm stools while raw salads irritate some colons.",
                "Blend soups to keep fiber benefits with gentler texture during early remission expansion.",
                "Introduce one new fiber source weekly to identify personal thresholds.",
            ]),
            ("Fiber when ostomy output is high", [
                "Thickening foods like applesauce or peanut butter may reduce liquid ileostomy output for some patients.",
                "Hydration must rise when adding fiber to high-output ostomies.",
                "Ostomy nurses adjust guidance when blockages occurred previously.",
            ]),
        ),
        "type1-diabetes-autoimmune-basics": (
            ("Continuous glucose monitoring with GI symptoms", [
                "CGM trends help distinguish steroid-induced spikes from infection during IBD flares.",
                "Share CGM downloads with both endocrinology and gastroenterology before major therapy changes.",
                "Skin adhesive reactions may require alternate sensor sites or barriers.",
            ]),
            ("School and workplace safety planning", [
                "504 plans should include glucagon access, snack breaks, and bathroom privileges together.",
                "Coworkers need not know diagnosis details if HR holds medical documentation separately.",
                "Review sick-day insulin rules annually because IBD flare frequency may change.",
            ]),
        ),
        "mesalamine-5-asa-ibd": (
            ("Rectal therapy adherence tips", [
                "Use enemas at the same clock time daily when prescribed twice-daily regimens.",
                "Lie on your left side for several minutes after liquid enemas to improve retention.",
                "Travel with suppositories in insulated bags if summer heat melts formulations.",
            ]),
            ("When symptoms suggest inadequate topical reach", [
                "Rectal bleeding with formed stools may mean proctitis needs added rectal mesalamine.",
                "Tell your clinician if urgency persists despite oral pills alone.",
                "Combination oral plus rectal therapy is common for left-sided colitis maintenance.",
            ]),
        ),
        "icn-ostomy-toolkit-pediatric": (
            ("Peer connection for teens with ostomies", [
                "ICN youth events and camp programs introduce friends who normalize pouch talk.",
                "Video modules can be watched privately before group discussions if teens prefer.",
                "Parents step back during peer sessions when teens ask for independence.",
            ]),
            ("Coordinating school nurses and athletic staff", [
                "Provide one-page care plans listing supplies stored in nurse office and locker access rules.",
                "Athletic trainers need stoma protection guidance before contact sports return.",
                "Update plans after appliance brand changes so schools stock compatible backups.",
            ]),
        ),
        "thrombosis-clot-risk-ibd": (
            ("Outpatient flare prevention after hospitalization", [
                "Complete prescribed blood thinner courses after discharge even when legs feel fine.",
                "Walk hallways or home hallways as soon as clinicians approve mobility after severe colitis.",
                "Report calf pain during tapering of steroids because inflammation and clots can overlap.",
            ]),
            ("Family planning and estrogen discussions", [
                "Review contraception choices when IBD is active or hospitalization risk is high.",
                "Smoking cessation reduces clot and IBD risks simultaneously.",
                "Ask whether prophylaxis is needed before long orthopedic surgeries or cancer operations.",
            ]),
        ),
        "oral-canker-sores-ibd": (
            ("Nutrition when mouth pain limits intake", [
                "Protein shakes and smooth soups maintain calories when chewing hurts.",
                "Avoid acidic citrus and salty chips during open sores even if they are otherwise safe foods.",
                "Tell your GI team if weight drops because of oral pain.",
            ]),
            ("Dental coordination on immunosuppression", [
                "Dentists may delay elective work during high-dose steroid or biologic loading periods.",
                "Antibiotic prophylaxis decisions are individualized before dental extractions.",
                "Share your current IBD medication list at every dental visit.",
            ]),
        ),
        "fatigue-autoimmune-ibd": (
            ("Work and school pacing strategies", [
                "Schedule demanding tasks during peak energy windows identified in your two-week log.",
                "Hybrid work or late-start accommodations reduce crash cycles when documented medically.",
                "Short naps before driving if orthostatic symptoms appear with fatigue.",
            ]),
            ("Reviewing medications that sedate or energize", [
                "Antihistamine premeds for infusion and certain biologics may add next-day grogginess.",
                "Adjusting evening steroid timing with your clinician may protect sleep.",
                "Never stop fatigue-related prescriptions without a taper plan.",
            ]),
        ),
        "rheumatoid-arthritis-autoimmune-overview": (
            ("Morning stiffness tracking for clinic visits", [
                "Note how long hand stiffness lasts after waking and which joints swell visibly.",
                "Distinguish mechanical back pain from inflammatory spine pain when both IBD and RA coexist.",
                "Bring photos of swollen joints if flares settle before rheumatology appointments.",
            ]),
            ("Vaccination before starting biologic therapy", [
                "Update pneumococcal, flu, COVID, and shingles vaccines when RA and IBD plans align.",
                "Live vaccines may need completion before methotrexate or biologics start.",
                "Household contact vaccination reduces risk when you are immunocompromised.",
            ]),
        ),
        "autoimmune-hepatitis-ibd": (
            ("Alcohol and medication liver load", [
                "Complete alcohol avoidance is standard with autoimmune hepatitis and often recommended on thiopurines.",
                "Acetaminophen dosing should follow liver-aware limits your hepatologist sets.",
                "Herbal weight-loss products are a common hidden liver toxin; disclose all supplements.",
            ]),
            ("Surveillance when PSC or cirrhosis coexist", [
                "Ultrasound and lab schedules intensify when advanced fibrosis develops.",
                "Coordinate colon cancer screening intervals with hepatology when PSC is present.",
                "Report itching, jaundice, or ascites swelling without waiting for routine visits.",
            ]),
        ),
        "steroids-prednisone-ibd": (
            ("Bone protection while on prednisone", [
                "Calcium, vitamin D, and weight-bearing exercise reduce steroid bone loss when approved by your team.",
                "DEXA screening may start earlier than age sixty-five in IBD patients with repeated steroid courses.",
                "Report back pain or height loss suggesting vertebral fractures.",
            ]),
            ("Mood and sleep side effects", [
                "Insomnia and irritability are common; discuss timing of morning dosing with your clinician.",
                "Seek urgent help for depression with suicidal thoughts during steroid courses.",
                "Partners benefit from knowing mood shifts may be medication related temporarily.",
            ]),
        ),
        "vaccine-autoimmune-immunosuppression": (
            ("Documentation for school and travel", [
                "Keep vaccine records in the same folder as IBD medication lists for camp and college forms.",
                "Some countries require proof of vaccination; plan travel clinic visits months ahead.",
                "Employers may request flu vaccination status in healthcare settings; medical exemptions differ from personal preference.",
            ]),
            ("Household exposure planning", [
                "When household members get live vaccines, immunocompromised patients should ask clinicians about isolation timing.",
                "Varicella exposure without immunity needs urgent guidance on immunoglobulin or antivirals.",
                "Discuss rabies pre-exposure if you handle animals and are on biologics.",
            ]),
        ),
    }

    for slug, pair in entries.items():
        E(slug, pair[0], pair[1])

    # Remaining slugs loaded from part 2
    from _batch1_extra_sections_rest2 import register as register2  # noqa: WPS433
    register2(E)
