from __future__ import annotations


def S(title: str, *paragraphs: str) -> tuple[str, list[str]]:
    return (title, list(paragraphs))


def block(*items: tuple[str, list[str]]) -> list[tuple[str, list[str]]]:
    return list(items)


ALL_SPECS = {
    "colon_surveillance.py": dict(
        intro=(
            "Long standing ulcerative colitis and Crohn's colitis carry higher <strong>colorectal cancer</strong> risk than "
            "the general population for many patients. Surveillance colonoscopy finds precancerous change early when treatment "
            "options are broader. This page explains dysplasia in plain words, why timing is personalized, and how to prepare "
            "without fear mongering. Read with "
            "<a href=\"/guides/foundation-ibd-colonoscopy-cancer-surveillance\">colonoscopy surveillance guide</a>. "
            "Not your personal screening calendar. Education only."
        ),
        sections=block(
            S(
                "Why clinicians discuss cancer risk in IBD",
                "Chronic intestinal inflammation can alter lining cells over years. Surveillance aims to catch dysplasia or early cancer when endoscopic treatment or surgery is more manageable.",
                "Modern biologic control may lower risk compared with historical cohorts, yet many patients with extensive colitis still need structured scopes.",
                "Understanding risk helps you keep appointments even when bowel habits feel fine.",
                "Risk numbers are population level; your chart may differ based on duration and inflammation history.",
            ),
            S(
                "Dysplasia explained without lecture tone",
                "Dysplasia means abnormal appearing cells on biopsy, graded low or high by pathologists.",
                "Not all dysplasia equals cancer today, yet it triggers closer follow up or removal plans.",
                "Endoscopic resection can clear some lesions without immediate colectomy.",
                "Always ask for copies of pathology reports when transferring care.",
            ),
            S(
                "Surveillance scopes versus symptom scopes",
                "Surveillance happens on a schedule even when you feel well, using careful inspection techniques at specialty centers when available.",
                "Symptom scopes investigate bleeding or flare suspicion and may not reset the surveillance clock automatically.",
                "Bring prior interval dates to new gastroenterologists to avoid accidental gaps.",
                "Write the next due date on your calendar the day you wake from sedation.",
            ),
            S(
                "Factors that change interval length",
                "Disease duration, extent, prior dysplasia, primary sclerosing cholangitis, family history, and past inflammation severity influence timing.",
                "Only your GI should map years between scopes to your history.",
                "Primary sclerosing cholangitis adds layers; see <a href=\"/blog/primary-sclerosing-cholangitis-ibd\">PSC and IBD</a> for parallel reading.",
                "Pediatric onset patients may reach long duration earlier than they feel old.",
            ),
            S(
                "Chromoendoscopy and advanced inspection",
                "Some centers use dye spray techniques highlighting flat lesions. Ask whether your referral hospital offers advanced inspection.",
                "Flat dysplasia is why good prep matters beyond convenience.",
                "If travel to a specialty center is needed, plan lodging and companion support early.",
                "Insurance authorization letters may take weeks; start paperwork after your GI recommendation.",
            ),
            S(
                "Prep quality and medication holds",
                "Split dose prep improves visualization. Ask which IBD medicines continue and how to time diabetes or blood thinner holds.",
                "Poor prep can force short interval repeats, wasting PTO and causing frustration.",
                "Flavor choices and chilled prep cups help completion; ask nurses for tricks.",
                "Arrange bathroom access at home during prep day without shame.",
            ),
            S(
                "Sedation, drivers, and recovery",
                "Plan a responsible adult driver; rideshare alone may be refused.",
                "Resume eating slowly; post sedation bloating differs from flare pain yet deserves mention if severe.",
                "Biopsy sites can ooze briefly; know what bleeding amount triggers a call.",
                "Return to work timing varies; book light schedules the day after if possible.",
            ),
            S(
                "If polyps or dysplasia are found",
                "Endoscopic mucosal resection may remove small areas; some cases lead to colectomy discussion when risk is high.",
                "Second opinions at IBD centers of excellence are reasonable for complex pathology.",
                "Bring a notebook to multidisciplinary visits; vocabulary stacks quickly.",
                "Emotional support matters; fear is normal and deserves counseling resources.",
            ),
            S(
                "After colectomy and pouch surveillance",
                "Patients with pouches or retained rectal cuffs may have different cancer surveillance pathways.",
                "Surgical history changes which scopes you need; do not assume general population colon cancer screening pamphlets apply.",
                "Ask surgeons and GI who owns which interval going forward.",
                "Pouchitis flares do not replace cancer surveillance conversations.",
            ),
            S(
                "Lifestyle pieces that support whole health",
                "Treating inflammation, avoiding smoking, and keeping general age appropriate cancer screenings for other organs remain important.",
                "Diet quality supports wellbeing but does not replace colonoscopy when surveillance is due.",
                "Physical activity and sleep help resilience during prep weeks.",
                "Alcohol moderation may matter for liver health when PSC coexists.",
            ),
            S(
                "Talking with family about surveillance",
                "Relatives may fear scopes excessively; share education links rather than horror stories.",
                "Children of IBD patients ask if they will need lifetime scopes; pediatric teams answer separately.",
                "Partners can help track dates and drive duties without becoming appointment police.",
                "Workplaces may need FMLA for prep days; see work education pages if helpful.",
            ),
            S(
                "Insurance and cost planning",
                "Verify endoscopy benefits, facility fees, and anesthesia billing before scheduling.",
                "Financial counselors at hospitals can estimate out of pocket costs.",
                "Keep itemized bills for flex accounts when eligible.",
                "Charity care programs exist at many nonprofit hospitals if costs spike.",
            ),
            S(
                "Anxiety before scopes",
                "Sedation fears, embarrassment, and past traumatic prep drive avoidance.",
                "Tell anesthesia teams about prior nausea or panic; protocols adjust.",
                "Behavioral health can rehearse coping skills before the month of prep.",
                "Missing surveillance because of anxiety is common; ask for help early.",
            ),
            S(
                "Questions to bring on a card",
                "Write: last scope date, next due interval, whether chromoendoscopy is planned, prep type, and medication holds.",
                "Ask what result would trigger shorter intervals or surgery referral.",
                "Request portal message summaries after pathology returns.",
                "Store PDF pathology in a cloud folder labeled surveillance.",
            ),
        ),
        clinic=(
            "Based on my disease duration, extent, and history, when is my next surveillance colonoscopy due, and will you use "
            "chromoendoscopy or standard inspection? What prep and medication instructions apply?"
        ),
        faqs=[
            ("Does small bowel Crohn's need colorectal surveillance?", "Colon Crohn's follows colitis like pathways; small bowel only disease uses different imaging. Personalize with your GI."),
            ("Can I skip surveillance if I feel fine?", "Silent changes motivate surveillance; skipping without team agreement loses lead time."),
            ("Do biologics remove surveillance need?", "Biologics control inflammation but prior years of disease still matter for intervals."),
            ("Is cancer inevitable with IBD?", "No. Risk is elevated for many with long colitis, yet most patients never develop colorectal cancer."),
        ],
        related=[
            ("Surveillance guide", "/guides/foundation-ibd-colonoscopy-cancer-surveillance"),
            ("Colonoscopy prep tips", "/blog/colonoscopy-prep-ibd"),
            ("PSC and IBD", "/blog/primary-sclerosing-cholangitis-ibd"),
            ("Flare help", "/flare-help"),
        ],
        closing=["Surveillance is a planning tool, not a punishment. Keeping dates protects future you."],
    ),
    "smoking.py": dict(
        intro=(
            "Smoking touches <strong>Crohn's disease</strong> and <strong>ulcerative colitis</strong> differently in research, "
            "yet quitting remains a health priority for nearly everyone with IBD. This page explains nuance without promoting tobacco, "
            "covers quitting supports, and addresses vaping questions. Education only."
        ),
        sections=block(
            S(
                "Crohn's disease and smoking data",
                "Smoking links to higher Crohn's risk, more flares, fistula complications, and postoperative recurrence in many studies.",
                "Quitting improves surgical outcomes and may reduce flare frequency over time.",
                "Former smokers still need standard IBD care; damage is not always instantly reversible.",
                "Bring honest pack year history to preoperative visits.",
            ),
            S(
                "Ulcerative colitis nuance without tobacco advice",
                "Historical studies noted lower UC diagnosis rates among current smokers, which is not a reason to start or continue smoking.",
                "Smoking harms lungs, bones, cardiovascular health, and cancer risk, and complicates healing.",
                "Quitting may shift UC symptoms; clinicians can adjust medicines during cessation.",
                "Never trade lung health for colon symptom tricks.",
            ),
            S(
                "Nicotine replacement and prescriptions",
                "Patches, gum, lozenges, and prescription quit aids can be discussed with GI and primary care to limit interactions.",
                "List all nicotine products including pouches and vaping liquids at appointments.",
                "Dosing schedules may align with work breaks to reduce withdrawal irritability.",
                "Pregnancy and breastfeeding require specialized quit plans.",
            ),
            S(
                "Vaping and heated products",
                "Vaping is not harmless for lungs or surgery recovery; IBD specific outcome data remain limited.",
                "Teams usually prefer evidence based quit programs over trading cigarettes for chronic vaping.",
                "Flavoring chemicals carry their own lung stories; do not assume safety.",
                "If you vape THC where legal, separate medical discussions from nicotine plans.",
            ),
            S(
                "Cannabis smoking overlap",
                "Some patients use cannabis for symptoms where legal; inhaled cannabis still carries respiratory risks separate from inflammation control.",
                "Discuss forms, doses, and legal context honestly with your team.",
                "Edible forms may affect nausea differently than smoked forms.",
                "Driving laws apply regardless of medical use claims.",
            ),
            S(
                "Surgery, wounds, and biologics",
                "Smokers face higher infection and anastomotic complication rates for some bowel surgeries.",
                "Quitting before elective surgery when possible is a common preoperative goal.",
                "Wound healing slows; surgeons may delay cases until cessation plans start.",
                "Biologic timing continues during quit attempts unless anesthesia plans say otherwise.",
            ),
            S(
                "Bone health and steroids plus smoking",
                "Smoking and steroids both threaten bone density; dual exposure deserves DEXA conversations.",
                "Calcium and vitamin D supplementation may increase when teams agree.",
                "Weight bearing exercise helps when joints allow; see fitness education pages.",
                "Fall prevention matters when osteoporosis appears.",
            ),
            S(
                "Behavioral supports that stick",
                "Quit lines, apps, group counseling, and relapse plans beat willpower alone.",
                "Identify triggers such as alcohol nights, work stress, or social smoking patios.",
                "Replace rituals with walks, gum, or fidget tools during the first month.",
                "Celebrate smoke free weeks without shaming slips; restart quickly.",
            ),
            S(
                "Talking with family and coworkers",
                "Household smokers complicate quit attempts; negotiate smoke free cars and balconies.",
                "Coworkers may offer cigarettes socially; rehearse polite refusals.",
                "Kids benefit when parents quit; pediatricians support family plans.",
                "Privacy about quit attempts is fine; you owe no workplace announcement.",
            ),
            S(
                "Withdrawal and gut symptoms",
                "Nicotine withdrawal can irritate mood and sleep, indirectly affecting gut sensation.",
                "Some UC patients report symptom shifts after quitting; log stools to separate withdrawal from flare.",
                "Do not assume every change is a flare requiring steroids without messaging clinic.",
                "Hydration and regular meals stabilize withdrawal weeks for some people.",
            ),
            S(
                "Financial and access resources",
                "Many states offer free quit kits through health departments.",
                "Insurance may cover counseling and medicines with minimal copay.",
                "Employer wellness programs sometimes include nicotine coaching.",
                "Keep receipts if flex spending covers quit aids.",
            ),
            S(
                "When quitting feels impossible",
                "Multiple quit attempts are normal; each attempt teaches trigger patterns.",
                "Behavioral health can treat depression or anxiety fueling smoking.",
                "Harm reduction conversations belong with clinicians, not anonymous forums alone.",
                "Emergency breathing symptoms need urgent care regardless of quit status.",
            ),
            S(
                "Recording quit progress for clinic",
                "Note quit date, tools used, slips, and craving times in IBDPal or a notebook.",
                "Surgeons appreciate smoke free intervals measured in weeks before operations.",
                "Primary care can update problem lists so every specialist sees status.",
                "Victories include reduced pack count even before full cessation.",
            ),
            S(
                "Long term health after quitting",
                "Cardiovascular risk falls over years after quitting.",
                "Lung function may stabilize; cancer risk declines gradually.",
                "IBD medicines continue as prescribed; quitting is complementary, not a substitute.",
                "Annual lung screening discussions apply to heavy former smokers per primary care guidelines.",
            ),
        ),
        clinic=(
            "I want to quit smoking with my Crohn's or colitis care plan. Which nicotine replacement or prescriptions are safe with "
            "my current IBD meds, and how should we watch flare symptoms during withdrawal?"
        ),
        faqs=[
            ("Will quitting cause a UC flare?", "Some patients report symptom shifts; clinicians can adjust IBD meds and support gradual cessation."),
            ("Is one cigarette daily harmless?", "Even low levels carry surgical and cardiovascular risks; teams still encourage full cessation."),
            ("Does secondhand smoke matter?", "Reduce exposure when possible, especially around children and before surgery."),
            ("Can I use nicotine gum forever?", "Discuss long term gum use with clinicians; goal is usually nicotine freedom eventually."),
        ],
        related=[
            ("Surgery recovery", "/blog/ibd-surgery-recovery-nutrition"),
            ("Stress management", "/blog/stress-management-ibd"),
            ("Biologics overview", "/blog/biologics-ibd-overview"),
            ("Resources", "/resources"),
        ],
        closing=["Quitting is a medical project, not a character exam. Clinicians want to help you breathe and heal."],
    ),
    "disability_fmla.py": dict(
        intro=(
            "Crohn's disease and ulcerative colitis disrupt work when flares, infusions, and surgeries collide with shift schedules. "
            "This United States focused page explains <strong>FMLA basics</strong>, disability documentation themes, and reasonable "
            "accommodation ideas. It is not legal advice. Confirm details with HR, state agencies, or an employment attorney."
        ),
        sections=block(
            S(
                "Why work questions spike after diagnosis",
                "Newly diagnosed patients fear bathroom access, attendance points, and stigma from managers.",
                "Knowing vocabulary like FMLA, ADA, and intermittent leave reduces panic when a flare hits mid quarter.",
                "Documentation habits started early save scrambling during hospitalizations.",
                "Remote work culture changed options yet did not erase legal protections.",
            ),
            S(
                "FMLA eligibility in plain words",
                "The Family and Medical Leave Act may provide unpaid job protected leave for serious health conditions when employer size, tenure, and hours thresholds are met.",
                "Covered employers generally have fifty or more employees within a radius; employees need about twelve months tenure and sufficient hours.",
                "State family leave laws sometimes add paid benefits; check your state labor site.",
                "Self employed workers often lack FMLA yet may have other programs.",
            ),
            S(
                "Serious health condition and IBD",
                "Hospitalizations, some infusion schedules, and incapacity periods may qualify when certification supports them.",
                "Intermittent leave can cover flare days, infusion days, or postoperative recovery if documented.",
                "Mental health flare related incapacity may also qualify when certified.",
                "Keep dates aligned with portal notes and infusion chair schedules.",
            ),
            S(
                "Certification paperwork tips",
                "Ask GI offices for forms early; portal uploads reduce phone tag.",
                "Provide job description summaries so clinicians describe functional limits accurately.",
                "Renew certifications before they expire to avoid attendance surprises.",
                "Store PDF copies in a labeled cloud folder.",
            ),
            S(
                "ADA accommodations beyond leave",
                "Reasonable accommodations may include flexible start times after infusion fatigue, remote work on flare days, nearby restroom access, and break flexibility.",
                "Students may use Section 504 plans with similar themes.",
                "Accommodations should be dialogues, not demands, documented in writing when HR agrees.",
                "Trial periods help everyone evaluate whether a change works.",
            ),
            S(
                "Talking with HR without oversharing",
                "Share functional limits: need predictable bathroom access, unable to stand six hours during flare, need telework twice monthly.",
                "You do not owe graphic symptoms to direct managers.",
                "HR professionals trained in medical privacy handle details; route through them when possible.",
                "Email creates paper trails; keep tone factual.",
            ),
            S(
                "Short term and long term disability policies",
                "Private disability insurance policies differ in elimination periods and definitions of disability.",
                "Own occupation versus any occupation language matters for high earners.",
                "Social Security disability is a separate federal process with its own medical evidence rules.",
                "Lawyers specializing in disability can review denials; this page does not provide legal strategy.",
            ),
            S(
                "Attendance policies and point systems",
                "FMLA protected absences should not count against attendance points when applied correctly.",
                "Track which days were FMLA coded on pay stubs.",
                "If points accrue wrongly, escalate with HR in writing citing certification dates.",
                "Union members may have additional grievance paths.",
            ),
            S(
                "Infusions, remotes work, and PTO",
                "Infusion days may consume PTO unless FMLA or sick leave applies.",
                "Ask whether chair time qualifies for intermittent leave certification.",
                "Remote work on infusion day helps some people continue projects safely.",
                "Fatigue the day after infusion may need schedule flexibility too.",
            ),
            S(
                "Surgery and postoperative leave",
                "Major resections may need continuous leave blocks plus intermittent follow up.",
                "Surgeon notes should list lifting restrictions and expected recovery weeks.",
                "Short term disability forms often ask for procedure codes; provide operative reports if requested.",
                "Return to work plans can phase hours upward gradually.",
            ),
            S(
                "Gig economy and contract workers",
                "Independent contractors typically lack FMLA; plan savings buffers when possible.",
                "Professional associations occasionally offer hardship grants.",
                "Clients may accept deadline shifts if informed early with professionalism.",
                "Document income loss if applying for assistance programs.",
            ),
            S(
                "Discrimination and retaliation themes",
                "Retaliation for protected leave or disability accommodation can be unlawful in many scenarios; outcomes depend on facts.",
                "Document manager comments, emails, and attendance changes after disclosures.",
                "Legal counsel interprets specifics; this education page flags the concept only.",
                "EEOC deadlines apply; do not wait years to seek advice if concerned.",
            ),
            S(
                "School and higher education parallels",
                "College disability services offices coordinate restroom access and exam extensions.",
                "K through 12 teams use 504 plans with nurse involvement for meds and bathroom passes.",
                "Professors appreciate early semester conversations rather than crisis emails before finals.",
                "Dorm selection near bathrooms helps some students.",
            ),
            S(
                "Building a personal work packet",
                "Maintain one folder: diagnosis summary, medication list, FMLA certifications, accommodation letters, and infusion schedule.",
                "Update after each scope or surgery.",
                "Share packet slices as needed rather than entire charts.",
                "IBDPal logs can export symptom timelines supporting intermittent leave patterns.",
            ),
        ),
        clinic=(
            "I need work documentation for intermittent IBD flares and infusions. Can you complete FMLA or disability forms and "
            "state expected absence frequency without disclosing more than necessary?"
        ),
        faqs=[
            ("Is FMLA paid?", "FMLA itself is unpaid; some states or employers add paid leave programs separately."),
            ("Can my boss fire me for absences?", "Protected leave and accommodation laws may limit retaliation; facts matter and lawyers interpret cases."),
            ("Must I tell coworkers?", "No. HR conversations can stay confidential while you share only logistics with teammates if you choose."),
            ("Does remote work replace FMLA?", "No. Remote work may be an accommodation while FMLA covers job protected absence when eligible."),
        ],
        related=[
            ("Travel and work", "/blog/biologics-flying-travel-ibd"),
            ("Infusion scheduling", "/blog/infusion-appointment-ibd"),
            ("Stress management", "/blog/stress-management-ibd"),
            ("Ask IBDPal", "/ask"),
        ],
        closing=["Work protections exist so illness does not automatically mean career loss. Use paperwork early and keep copies."],
    ),
    "running.py": dict(
        intro=(
            "Running and jogging attract people with Crohn's disease and ulcerative colitis who want cardio fitness, yet urgency, "
            "fatigue, and joint pain complicate route planning. This guide covers flare versus remission pacing, hydration, and "
            "links to <a href=\"/blog/yoga-for-ibd-crohns-colitis\">yoga</a>, "
            "<a href=\"/blog/walking-for-ibd-crohns-colitis\">walking</a>, "
            "<a href=\"/blog/strength-training-gym-ibd\">strength training</a>, and "
            "<a href=\"/blog/exercise-during-ibd-flare\">exercise during flares</a>. Education only."
        ),
        sections=block(
            S(
                "Why running tempts IBD patients",
                "Running offers efficient cardio when time is tight and can boost mood when inflammation is quiet.",
                "It also jostles the gut and raises urgency fears on routes without bathrooms.",
                "A planned run walk program beats heroic sprints followed by crash naps.",
                "Fitness goals should serve health, not punish flares.",
            ),
            S(
                "Remission baseline building",
                "Start with run walk intervals on flat paths with known restrooms every mile or less.",
                "Increase weekly mileage gently; many IBD runners cap increases below classic ten percent rules.",
                "Rest days are training days too when calprotectin recently normalized.",
                "Track morning heart rate or sleep if overtraining signs appear.",
            ),
            S(
                "Flare week downgrades",
                "Swap outdoor runs for indoor walking, gentle yoga, or rest when calprotectin is high or stools turn nocturnal.",
                "See exercise during flare article for red flags that stop all impact activity.",
                "Maintaining zero movement sometimes worsens stiffness; choose lowest impact option approved by your team.",
                "Return dates after flares should be tentative, not contractual.",
            ),
            S(
                "Bathroom mapping and gear",
                "Scout coffee shops, gyms, and park restrooms along loops.",
                "Carry a small kit: wipes, spare liner, zip bag, phone with offline maps.",
                "Waist belts should not squeeze stoma appliances; adjust brands until bounce feels safe.",
                "Tell one friend your loop path when running alone.",
            ),
            S(
                "Hydration and electrolytes on runs",
                "Diarrhea plus sweat stacks fluid losses; sip early instead of chugging at the finish.",
                "Ask clinicians before concentrated electrolyte packets if sugars trigger stools.",
                "Practice drink timing on short loops before race day.",
                "Weigh yourself before and after hot runs to estimate sweat loss.",
            ),
            S(
                "Heat, cold, and season shifts",
                "Summer dawn runs reduce heat urgency for some people.",
                "Winter layers help joints; warm up indoors before icy paths.",
                "Allergy seasons may affect breathing; distinguish asthma from deconditioning.",
                "Treadmills near home bathrooms reduce anxiety for beginners.",
            ),
            S(
                "Anemia and low hemoglobin",
                "Low hemoglobin makes target paces impossible; treat iron and inflammation before chasing personal records.",
                "Symptoms include breathlessness on stairs separate from running.",
                "Repeat labs after iron trials per hematology advice.",
                "Walk run intervals remain valid training while rebuilding stores.",
            ),
            S(
                "Joint disease and spondyloarthritis",
                "Axial joint pain may prefer lower impact days when sacroiliac joints ache.",
                "Physical therapy exercises complement running when cleared.",
                "NSAIDs for joint pain often clash with IBD; ask before using them to run.",
                "Shoe rotation and surface choice matter on inflamed days.",
            ),
            S(
                "Ostomy and J pouch runners",
                "Support belts and appliance emptying before runs reduce worry.",
                "Discuss bouncing impact with surgery teams after recent operations.",
                "Hydration needs rise with high output ostomies.",
                "Test adhesives in humidity before signing up for humid races.",
            ),
            S(
                "Medication timing and infusion weeks",
                "Some feel best day after infusion; others feel wiped.",
                "Log personal patterns a month before judging plans failed.",
                "Steroid tapers can temporarily inflate capacity then crash during taper.",
                "Anti diarrhea medicines around runs require clinician approval; never self medicate to force mileage.",
            ),
            S(
                "Race events versus casual jogs",
                "Marathons are possible for some athletes with meticulous planning; many choose shorter events.",
                "Corral bathroom lines stress urgency; plan conservative start times.",
                "Packet pickup days disrupt routine; sleep and hydration still matter.",
                "DNS a race without shame if a flare arrives race week.",
            ),
            S(
                "Strength cross training",
                "Strong glutes and core stabilize running form when fatigue hits.",
                "Link with strength training guide for twice weekly sessions.",
                "Heavy squats during active flares may wait; bodyweight work might stay.",
                "Balance run days with strength days to protect joints.",
            ),
            S(
                "Pelvic floor and urgency fear",
                "Fear of incontinence stops some runners before muscles fail.",
                "Pelvic floor physical therapy can help beyond willpower alone.",
                "Gradual exposure runs near bathrooms rebuild confidence.",
                "Dark clothing choices are personal coping tools, not medical requirements.",
            ),
            S(
                "When to stop and message clinic",
                "Pause for new fever, heavy bleeding, black stools, fainting, chest pain, vomiting that will not stop, or pain unlike baseline after activity.",
                "Bring activity logs to GI visits so clinicians see context.",
                "Celebrate restarted weeks after setbacks; that skill predicts long term fitness.",
                "Education supports shared decisions with gastroenterology and physical therapy teams.",
            ),
        ),
        clinic=(
            "I want to jog with my IBD. Given recent flares, anemia, or surgery, what weekly mileage and intensity are reasonable, "
            "and which symptoms should stop me immediately?"
        ),
        faqs=[
            ("Does running cause flares?", "Exercise does not cause IBD inflammation, yet dehydration or overtraining can worsen symptoms. Treat flares medically."),
            ("Are treadmills safer?", "They offer nearby bathrooms; many beginners prefer them for anxiety relief."),
            ("Can I run with an ostomy?", "Many people do with belts and planning; ask surgery team after recent operations."),
            ("Should I eat before morning runs?", "Small tolerated carbs help some; others prefer empty stomach trials near bathrooms."),
        ],
        related=[
            ("Walking guide", "/blog/walking-for-ibd-crohns-colitis"),
            ("Yoga guide", "/blog/yoga-for-ibd-crohns-colitis"),
            ("Strength training", "/blog/strength-training-gym-ibd"),
            ("Exercise during flare", "/blog/exercise-during-ibd-flare"),
        ],
        closing=["Running can fit IBD life when routes, fluids, and flare humility are planned. Consistency beats hero days."],
    ),
    "spicy_nuts.py": dict(
        intro=(
            "Spicy meals, nuts, and seeds dominate IBD trigger lists online. Crohn's disease and ulcerative colitis patients ask "
            "whether capsaicin, peanut butter, or whole seeds are safe. This page covers tolerance trials, stricture caution, and "
            "the difference between symptom irritation and inflammation. Education only."
        ),
        sections=block(
            S(
                "Why spice and crunch questions persist",
                "Capsaicin can speed transit or burn inflamed rectums in some ulcerative colitis patients.",
                "Whole nuts and seeds add mechanical load that narrowed segments dislike.",
                "Social media absolutes ignore remission versus flare context.",
                "Trials beat forever bans when teams agree inflammation is controlled.",
            ),
            S(
                "Spicy foods and symptom pathways",
                "Mild spice in remission may be fine while active proctitis prefers bland oils and herbs.",
                "Hot chili sauces hide garlic and onion fermentables that confuse FODMAP trials.",
                "Separate spice tests from sauce tests when logging.",
                "Rectal burning after meals deserves mention even without visible blood.",
            ),
            S(
                "Nuts versus nut butters",
                "Smooth peanut or almond butter spreads reduce mechanical load compared with whole nuts.",
                "Fat content still matters; large spoonfuls may speed urgency for some people.",
                "Trial one teaspoon on a safe starch before sandwiches full of butter.",
                "Salted varieties affect hydration; read labels.",
            ),
            S(
                "Seeds, popcorn, and strictures",
                "Stricturing Crohn's patients should ask explicitly before crunch heavy snacks.",
                "Popcorn combines insoluble fiber and sharp hulls many teams pause during stricture worry.",
                "Obstructive symptoms such as vomiting with bloating need urgent evaluation, not more fiber experiments.",
                "Imaging history guides crunch more than generic internet seed bans.",
            ),
            S(
                "Trial method clinicians prefer",
                "Change one variable at a time with a small portion and log 48 hours.",
                "Stop if pain, vomiting, or nocturnal stools rise.",
                "Retry in remission only after team agrees inflammation is quiet.",
                "Children need choking safety considered separately from IBD tolerance.",
            ),
            S(
                "Nutrition upside when tolerated",
                "Nuts offer calories, protein, and unsaturated fats helpful for weight maintenance.",
                "Spices like turmeric in food amounts differ from high dose supplement hype.",
                "Sprinkle ground seeds on yogurt may fit when whole seeds do not.",
                "Calorie dense foods help some underweight Crohn's patients in remission.",
            ),
            S(
                "Restaurant and cultural meals",
                "Ask for sauce on side, choose mild curries, swap whole nut garnishes for smooth sauces when testing.",
                "Explain needs without apologizing; kitchens often adjust heat.",
                "Buffets hide mixed oils; small plates reduce accidental triggers.",
                "Travel packs of safe nut butter help when airline meals are unknown.",
            ),
            S(
                "School policies versus medical texture",
                "Allergy free classrooms may ban peanuts while medically you trial almond butter at home.",
                "Separate school policy letters from gastroenterology advice.",
                "504 plans can clarify bathroom access unrelated to nut rules.",
                "Teachers appreciate simple safe snack lists.",
            ),
            S(
                "Flare versus remission rules of thumb",
                "Flares often favor bland proteins, low fiber textures, and paused crunch.",
                "Remission reintroduction might start with smooth nut butter before whole cashews.",
                "Spice may return last after oil and fiber trials succeed.",
                "Calprotectin trends should guide timing more than calendar ego.",
            ),
            S(
                "Ostomy and output considerations",
                "High fat nut loads may increase output volume for some ostomates.",
                "Empty appliances before spice experiments when output is unpredictable.",
                "Hydration rises when output loosens after curry nights.",
                "Skin care remains priority when output acidity changes.",
            ),
            S(
                "Allergy testing confusion",
                "Positive skin tests to foods you tolerate clinically should be interpreted with allergists.",
                "Do not eliminate wide groups based on panels alone without IBD context.",
                "Oral allergy syndrome from pollen cross reactivity differs from IBD decisions.",
                "Bring both allergy and GI notes to combined visits when possible.",
            ),
            S(
                "Supplement powders and nut flours",
                "Almond flour baked goods concentrate fat and calories; portion size still matters.",
                "Chia and flax gel may soothe some constipated patients yet worsen diarrhea predominant patterns.",
                "Protein powders with nut flavors may include artificial sweeteners that stir stools.",
                "Read ingredient lists for sugar alcohols during trials.",
            ),
            S(
                "When spice or nuts are the wrong focus",
                "Active inflammation may need medicines before any trigger hunt.",
                "Bile acid diarrhea mimics food triggers; clinicians test separately.",
                "Infection or C diff recurrence deserves testing when symptoms change abruptly.",
                "Do not delay scope or stool studies because a blogger blamed chili.",
            ),
            S(
                "Logging and clinic follow up",
                "Record brand, portion, preparation, and symptoms in IBDPal for two days after trials.",
                "Bring logs to dietitians instead of memory alone.",
                "Celebrate successful reintroductions without labeling yourself cured.",
                "Failed trials still provide useful data for the next plan.",
            ),
        ),
        clinic=(
            "Do I have strictures or active proctitis that should limit whole nuts, seeds, or spicy foods? If a trial is OK, "
            "what portion and preparation style should I start with?"
        ),
        faqs=[
            ("Are seeds always forbidden?", "Old diverticulosis myths do not automatically apply to IBD. Individualize with imaging and symptoms."),
            ("Is almond flour safer than whole almonds?", "Often yes for texture; fat load still matters."),
            ("Does spicy food cause inflammation?", "Spice usually irritates symptoms for some; it does not replace treating mucosal inflammation with meds."),
            ("Can children with IBD eat nuts?", "Ask pediatrics about texture, choking, and allergy policy together."),
        ],
        related=[
            ("Flare foods", "/blog/flare-foods-ibd"),
            ("Low residue ideas", "/blog/low-residue-diet-ibd"),
            ("Fiber overview", "/blog/fiber-ibd-flare-remission"),
            ("IBD nutrition hub", "/ibd-nutrition"),
        ],
        closing=["Spice and crunch are experiments, not morality tests. Let data and clinicians guide reintroduction."],
    ),
}
