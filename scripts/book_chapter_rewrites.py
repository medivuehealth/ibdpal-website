"""Author-written chapter narratives replacing stacked web articles."""

from __future__ import annotations

Block = tuple[str, str | list[str] | list[str]]

CHAPTER_REWRITES: dict[int, list[Block]] = {
    5: [
        (
            "paragraph",
            "Nutrition will not cure Crohn's disease or ulcerative colitis, but it strongly shapes "
            "energy, healing capacity, and day-to-day comfort. Work with your gastroenterologist "
            "and, when possible, an IBD-experienced registered dietitian. Major patient-education "
            "sources stress individualized plans over one-size internet diets.",
        ),
        ("heading_h2", "Start with goals, not perfection"),
        (
            "paragraph",
            "During active flares the goal is often adequate calories, protein, and fluids with "
            "gentler textures. In remission the goal shifts toward variety, micronutrients, and "
            "sustainable habits. Weight trends, labs, and symptoms guide changes more than "
            "influencer rules.",
        ),
        ("heading_h2", "Hydration as a Daily Foundation"),
        (
            "paragraph",
            "Diarrhea, fever, and heat raise fluid needs. Sip steadily, know your urine color "
            "cues, and ask about oral rehydration when losses are high. See Chapter 10 for "
            "hydration guidance.",
        ),
        ("heading_h2", "Fiber and Texture Changes"),
        (
            "paragraph",
            "Soluble and insoluble fiber behave differently, and strictures change what is safe. "
            "Some people tolerate oats and peeled produce in remission yet need lower fiber during "
            "severe colitis. See Chapter 12 before making large fiber changes, especially if you "
            "have known narrowing.",
        ),
        ("heading_h2", "Temporary Restrictions During Flares"),
        (
            "paragraph",
            "Temporary low-residue eating can reduce stool bulk and urgency for selected patients. "
            "It is not meant as a forever diet. See Chapter 22 for low-residue patterns during flares.",
        ),
        (
            "paragraph",
            "A short, dietitian-supervised low-FODMAP trial sometimes reduces gas and bloating when "
            "IBS-like symptoms overlap with IBD in remission. It is not a cure for inflammation and "
            "should not replace medical therapy. See Chapter 23 for FODMAP basics.",
        ),
        ("heading_h2", "Dairy and Lactose Tolerance"),
        (
            "paragraph",
            "Lactose intolerance can appear or worsen during inflammation even if you tolerated milk "
            "before. Lactose-free dairy or alternatives may help while calcium and vitamin D still "
            "need attention. See Chapter 27 for dairy and lactose.",
        ),
        ("heading_h2", "Protein, Micronutrients, and Unintentional Weight Change"),
        (
            "paragraph",
            "Spreading protein intake across meals supports tissue repair and recovery. Iron, vitamin "
            "B12, vitamin D, zinc, and other nutrients may require monitoring based on individual risk. "
            "See Chapters 11, 13, and 20 for protein and deficiency guidance.",
        ),
        (
            "paragraph",
            "Pick one focus for the next two weeks (hydration, protein, or flare textures), track "
            "symptoms, and bring results to clinic. Extreme elimination diets that leave you underfed "
            "can worsen outcomes. Reliable nutrition support pairs medical therapy with practical "
            "food skills, not fear.",
        ),
    ],
    3: [
        (
            "paragraph",
            "Active inflammation changes nutrition before you feel ready to eat. Inflammation can "
            "increase protein needs and, in some situations, overall nutritional requirements, "
            "while nausea, pain, and urgency shrink appetite. That mismatch is common in Crohn's "
            "disease and ulcerative colitis, and it is one reason labs and symptoms do not always "
            "move together.",
        ),
        ("heading_h2", "How Inflammation Affects Intake and Absorption"),
        (
            "paragraph",
            "During flares the gut may move food faster, tolerate less fiber or fat, and absorb "
            "fewer calories even when portions look normal. Fever and night sweats add fluid losses. "
            "Medical therapy that quiets inflammation often improves tolerance before appetite fully "
            "returns.",
        ),
        (
            "paragraph",
            "Inflammation also traps iron and alters how the body uses protein for repair. That is "
            "why Part III pairs symptom patterns with laboratory monitoring rather than guessing "
            "from meals alone.",
        ),
        ("heading_h2", "Malabsorption Patterns by Anatomy"),
        (
            "paragraph",
            "Disease location matters. Terminal ileum Crohn's disease raises vitamin B12 and bile "
            "acid malabsorption risk. Extensive small bowel disease or prior resection can limit "
            "surface area for calories, fat-soluble vitamins, and minerals. Colitis may spare "
            "absorption yet still cause bleeding, urgency, and restricted intake.",
        ),
        (
            "paragraph",
            "Fat malabsorption can look like greasy stools, bloating, or weight loss despite "
            "adequate portions. Lactose intolerance may appear during active disease even when milk "
            "was tolerated before. These patterns deserve clinician review, not silent restriction.",
        ),
        ("heading_h2", "Surgery, Short Bowel, and Recovery Nutrition"),
        (
            "paragraph",
            "Resection, stricture repair, ostomy creation, and J-pouch surgery each change fluid, "
            "salt, and mineral needs. Early recovery often emphasizes hydration, gradual texture "
            "progression, and dietitian input. Output from ileostomies can deplete sodium, "
            "potassium, and magnesium quickly during high-output periods.",
        ),
        (
            "paragraph",
            "Surgery is a tool in IBD care, not a personal failure. Nutrition goals shift from "
            "preoperative optimization to postoperative healing and long-term maintenance. Chapter 48 "
            "covers ostomy and short-bowel eating in more detail.",
        ),
        ("heading_h2", "Weight Change as a Signal, Not a Moral Score"),
        (
            "paragraph",
            "Unintentional weight loss during active disease may reflect inflammation, poor intake, "
            "malabsorption, or bleeding. Weight gain can follow steroids, improved absorption in "
            "remission, or reduced activity during recovery. Track trends and bring them to clinic "
            "rather than chasing rapid fixes.",
        ),
        (
            "paragraph",
            "Children, teens, and older adults need extra attention when weight shifts because growth, "
            "bone density, and frailty risks differ by age. A short period of gentler textures may "
            "help intake during flares; prolonged restriction without labs can worsen deficiencies.",
        ),
    ],
    8: [
        (
            "paragraph",
            "Remission creates room to expand variety, but tolerance rebuilds gradually. The goal is "
            "not to rush every food back at once. It is to widen your reliable menu while watching "
            "symptoms, labs, and scopes with your team.",
        ),
        ("heading_h2", "Reintroducing Foods in Stages"),
        (
            "paragraph",
            "Start with foods that stayed safe during the flare, then add one new category at a time. "
            "Fiber, raw produce, dairy, and higher-fat meals are common trial points. Keep portions "
            "modest and note stool changes, urgency, and energy over several days rather than one meal.",
        ),
        (
            "paragraph",
            "Texture still matters. Peeled, well-cooked vegetables and soft grains often tolerate "
            "before salads or crunchy snacks return. If a food causes discomfort, pause the trial and "
            "discuss whether the issue is irritant tolerance or rising inflammation.",
        ),
        ("heading_h2", "Cultural Meals and Social Eating"),
        (
            "paragraph",
            "Remission should include foods that matter culturally and socially. Plan ahead for "
            "restaurants, holidays, and shared meals: identify safe staples, ask about preparation, "
            "and eat smaller portions when uncertainty is high. Chapter 47 discusses holiday and "
            "fasting contexts in more detail.",
        ),
        (
            "paragraph",
            "Avoid comparing your plate to remission influencers online. Their disease location, "
            "surgery history, and medication course may differ entirely from yours. Protein targets "
            "and meal planning for healing are covered in Chapter 11.",
        ),
        ("heading_h2", "When Symptoms Return"),
        (
            "paragraph",
            "A bad week after a new food does not automatically mean a full flare. Temporary return "
            "to gentler textures may help while you contact your team if bleeding, fever, weight "
            "loss, or rising inflammatory markers appear. Chapter 7 covers flare-first eating when "
            "symptoms escalate again.",
        ),
        (
            "paragraph",
            "Remission is maintenance, not permission to ignore follow-up labs. Periodic monitoring "
            "helps catch deficiencies and inflammation early while you enjoy a broader diet.",
        ),
    ],
    20: [
        (
            "paragraph",
            "Food is the foundation of nutrition, but it is not always enough to correct a "
            "deficiency or maintain intake during active disease. Depending on laboratory results, "
            "disease activity, anatomy, and tolerance, clinicians may use oral supplements, "
            "intravenous replacement, oral nutrition supplements, or enteral nutrition. These "
            "are treatment tools, not substitutes for individualized assessment.",
        ),
        ("heading_h2", "When Supplements May Be Needed"),
        (
            "paragraph",
            "Active inflammation, malabsorption, surgery, poor appetite, and medication effects "
            "can raise requirements or block absorption despite adequate food intake. Labs and "
            "symptoms guide whether supplementation is appropriate rather than internet trends "
            "or influencer stacks.",
        ),
        (
            "paragraph",
            "Common scenarios include low vitamin B12 after ileal disease or resection, vitamin "
            "D deficiency on steroids, zinc or magnesium losses during diarrhea, and inadequate "
            "protein when meals are skipped during flares.",
        ),
        ("heading_h2", "When Oral Replacement Is Not Enough"),
        (
            "paragraph",
            "Oral supplements fail when nausea, rapid transit, inflammation, or intolerance blocks "
            "absorption. Clinician-directed intravenous repletion may be appropriate when oral "
            "supplementation is ineffective, poorly tolerated, or insufficient in the setting of "
            "active disease.",
        ),
        (
            "paragraph",
            "Weight loss, inability to maintain oral intake, and rising deficiency markers despite "
            "supplements are reasons to escalate quickly rather than layering more over-the-counter "
            "products.",
        ),
        ("heading_h2", "Oral Nutrition Supplements"),
        (
            "paragraph",
            "Ready-to-drink shakes and medical oral nutrition supplements can bridge gaps when solid "
            "food is inadequate. Products vary in protein, calories, lactose, and fiber. A dietitian "
            "can match formulas to tolerance, kidney function, and goals.",
        ),
        (
            "paragraph",
            "Shakes are usually short-term supports during recovery, not replacements for normal "
            "meals once intake improves.",
        ),
        ("heading_h2", "Iron and Intravenous Replacement"),
        (
            "paragraph",
            "Iron deficiency is discussed in detail in Chapter 15. When oral iron is ineffective, "
            "poorly tolerated, or insufficient, clinicians may consider intravenous replacement "
            "based on laboratory findings and disease activity.",
        ),
        ("heading_h2", "Safety and Monitoring"),
        (
            "paragraph",
            "Bring every supplement bottle to clinic visits. High-dose vitamins, herbal blends, and "
            "multiple overlapping products can interact with IBD medications or harm organs when "
            "taken without monitoring.",
        ),
        (
            "paragraph",
            "Recheck labs after repletion plans start. Symptoms may improve before stores normalize, "
            "so follow-up testing guides when to stop or continue.",
        ),
    ],
    13: [
        (
            "paragraph",
            "Lab sheets can look like a foreign language. You do not need to memorize every "
            "reference range. You do need a few anchors so you can ask better questions at the "
            "next visit and connect results to nutrition, not to self-diagnose.",
        ),
        ("heading_h2", "Common Labs Patients Review"),
        (
            "paragraph",
            "Most IBD clinics cycle through a familiar panel: complete blood count (CBC), "
            "comprehensive metabolic panel, inflammatory markers, and stool tests such as "
            "fecal calprotectin. Nutrition-related tests often include iron studies, ferritin, "
            "vitamin B12, folate, and vitamin D.",
        ),
        (
            "list",
            [
                "CBC: anemia, white blood cell counts on immunosuppressants",
                "Chemistry panel: kidney and liver function on many IBD medicines",
                "Iron studies, B12, folate, vitamin D: absorption and intake gaps",
            ],
        ),
        ("heading_h2", "Calprotectin, CRP, and ESR"),
        (
            "paragraph",
            "Fecal calprotectin reflects neutrophil activity in stool and often rises when "
            "intestinal inflammation is active. C-reactive protein (CRP) and erythrocyte "
            "sedimentation rate (ESR) are blood markers of broader inflammation. They are not "
            "IBD-specific: infection, surgery recovery, or other illness can raise them.",
        ),
        (
            "paragraph",
            "Some people have active gut disease with a quiet CRP, especially with isolated "
            "ileal or rectal inflammation. That is why clinicians pair blood markers with "
            "symptoms, stool tests, and endoscopy rather than relying on one number alone.",
        ),
        (
            "paragraph",
            "Home calprotectin kits may help track trends between clinic visits when your team "
            "approves them; follow kit instructions and discuss out-of-range results with your "
            "clinician rather than changing treatment on your own.",
        ),
        ("heading_h2", "Interpreting Trends, Not Single Values"),
        (
            "paragraph",
            "Trends over time usually matter more than debating whether one result sits just "
            "above or below a lab's reference range. Rising calprotectin or CRP alongside "
            "worsening symptoms may prompt your team to reassess therapy. Falling markers often "
            "track with healing, but symptoms and scopes still guide decisions together.",
        ),
        (
            "paragraph",
            "Bring prior results to visits, note the dates of home versus clinic samples, and "
            "ask whether your team uses personal treat-to-target goals rather than population "
            "averages alone.",
        ),
        ("heading_h2", "Nutrition-Related Labs"),
        (
            "paragraph",
            "Inflammation, bleeding, malabsorption, and restricted diets can lower iron, B12, "
            "folate, vitamin D, zinc, and magnesium even when appetite seems adequate. Ferritin "
            "may rise during active inflammation despite low iron stores, so iron studies are "
            "interpreted with clinical context.",
        ),
        (
            "paragraph",
            "Chapters 15 through 20 discuss individual deficiencies and repletion. This chapter "
            "focuses on reading the numbers your team orders and knowing when nutrition labs "
            "deserve follow-up.",
        ),
        ("heading_h2", "When Labs and Symptoms Disagree"),
        (
            "paragraph",
            "You can feel miserable while markers look stable, or feel relatively well while "
            "silent inflammation persists. Functional symptoms, anemia, small bowel disease, or "
            "irritant intolerance can explain gaps between how you feel and what labs show.",
        ),
        (
            "paragraph",
            "When a single high calprotectin conflicts with improving symptoms, clinicians may "
            "repeat testing rather than act on one value alone. CRP may normalize while "
            "calprotectin remains elevated in some patterns. Blood and stool tests collected "
            "the same day can improve interpretation.",
        ),
        ("heading_h2", "Questions for Your Clinician"),
        (
            "list",
            [
                "How does this result compare with my last two tests?",
                "Does this number change our plan this month, or are we watching trends?",
                "Which nutrition labs should we recheck based on my disease location and diet?",
                "If home and clinic calprotectin differ, which should we trust?",
            ],
        ),
    ],
    17: [
        (
            "paragraph",
            "Terminal ileum disease, resection, methotrexate, and chronic inflammation each "
            "raise the risk of B12 and folate gaps. Fatigue and brain fog often have multiple "
            "stacking causes rather than one missing vitamin.",
        ),
        ("heading_h2", "Vitamin B12"),
        (
            "paragraph",
            "Crohn's disease involving the terminal ileum or prior ileal resection raises the "
            "risk of vitamin B12 deficiency. Long-term supplementation or injections may be "
            "needed even when you feel well; periodic labs are worth discussing with your team.",
        ),
        ("heading_h2", "Folate"),
        (
            "paragraph",
            "Folate supports red blood cell formation and cell division. Active inflammation, "
            "poor intake, alcohol use, and methotrexate therapy can lower folate status. "
            "Supplementation during methotrexate should follow your rheumatology or GI plan, "
            "not an arbitrary over-the-counter dose.",
        ),
        (
            "paragraph",
            "Leafy greens, legumes, fortified grains, and eggs contribute folate when tolerated. "
            "Cooking and texture changes during flares may shrink intake even when needs rise.",
        ),
        ("heading_h2", "Why Fatigue Is Common With IBD"),
        (
            "paragraph",
            "Exhaustion is not laziness. Active inflammation, anemia, poor sleep from nighttime "
            "symptoms, medication effects, dehydration, low calorie intake, and mood disorders "
            "can stack together. Some people feel tired before diarrhea returns.",
        ),
        ("heading_h2", "Brain Fog and Remission Fatigue"),
        (
            "paragraph",
            "Brain fog describes slow thinking, forgetfulness, or trouble concentrating at school "
            "or work. Contributors include iron-deficiency anemia, B12 malabsorption, sleep "
            "debt, pain, stress, and active inflammation. Fatigue can persist in remission and "
            "still deserves a workup: targeted labs, medication review, and mental health screening.",
        ),
        ("heading_h2", "Pacing, Energy, and Daily Life"),
        (
            "paragraph",
            "Energy budgeting helps: plan one essential task on high-symptom days instead of a "
            "full to-do list. Track fatigue on a simple 1 to 10 scale alongside sleep, stools, and "
            "meals for visit-ready trends. Short walks or stretching when approved may help more "
            "than all-day bed rest for some people.",
        ),
        (
            "paragraph",
            "During brain fog, use short lists, phone reminders, and break tasks into chunks. "
            "Alternate activity and rest to avoid crash cycles. School and workplace fatigue may "
            "qualify for accommodations when documented with your care team.",
        ),
        (
            "paragraph",
            "Gentle fuel and hydration support recovery; pair small frequent meals with adequate "
            "fluids when diarrhea is significant (see Chapter 10).",
        ),
        ("heading_h2", "Labs and Questions for Your Clinician"),
        (
            "list",
            [
                "Can we check CBC, iron studies, ferritin, B12, folate, vitamin D, and thyroid if fatigue is new or worsening?",
                "Could inflammation explain this even if stools seem stable?",
                "Is medication timing or dose affecting sleep or energy?",
                "Should we screen for depression, anxiety, or sleep apnea?",
            ],
        ),
        ("heading_h2", "When to Call the Clinic Sooner"),
        (
            "paragraph",
            "Contact your team promptly for sudden severe fatigue with fever, heavy bleeding, "
            "chest pain, shortness of breath, or fainting. Those may signal anemia acceleration, "
            "infection, or complications beyond ordinary tiredness.",
        ),
    ],
    21: [
        (
            "paragraph",
            "Carnivore, cleanse, and juice protocols circulate online. Inflammation control still "
            "belongs with your gastroenterology plan. This chapter separates marketing slogans "
            "from practical nutrition questions.",
        ),
        ("heading_h2", "What the Carnivore Pitch Claims"),
        (
            "paragraph",
            "All-meat plans remove fiber, most plant micronutrients, and usual carbohydrate sources. "
            "Anecdotes of short-term symptom calm are not the same as mucosal healing.",
        ),
        (
            "list",
            [
                "Zero fiber can feel easier during a flare but is not a lifelong evidence-based IBD diet",
                "Iron and protein may rise while vitamin C, folate, and magnesium often fall without planning",
                "Strict exclusion can shrink food variety and raise anxiety around eating",
            ],
        ),
        ("heading_h2", "Safer Framing If You Are Curious"),
        (
            "list",
            [
                "Ask whether a supervised, temporary low-residue phase fits your flare, not a permanent carnivore identity",
                "Keep prescribed medicines and monitoring on schedule",
                "Review labs for anemia, lipids, and vitamin status before extreme restriction",
                "Work with an IBD-aware dietitian if you need higher protein without cutting all plants forever",
            ],
        ),
        (
            "paragraph",
            "Online carnivore challenges are not clinical protocols. Do not stop biologics or other "
            "therapy because an influencer said meat cured them.",
        ),
        ("heading_h2", "When to Seek Care Promptly"),
        (
            "list",
            [
                "Black stools, heavy bleeding, or fainting",
                "Rapid weight loss with inability to keep food down",
                "Chest pain or severe dehydration",
                "High fever with rapid decline",
            ],
        ),
        ("heading_h2", "Common Carnivore Diet Myths"),
        (
            "list",
            [
                "Carnivore cures Crohn's or colitis: no high-quality evidence supports that claim",
                "All plants inflame the gut: tolerance is individual; many plant foods are used in remission diets",
                "If meat feels better, fiber is poison forever: texture and portion often matter more than a permanent ban",
                "Feeling better on all meat proves remission: hidden inflammation may still need labs or scopes",
            ],
        ),
        ("heading_h2", "Risks Specific to IBD Patients"),
        (
            "paragraph",
            "High red and processed meat intake correlates with worse outcomes in some epidemiologic "
            "studies. Very-low-fiber diets can contribute to constipation in some people, while "
            "patients with strictures require individualized fiber guidance. Discuss cardiovascular and kidney health with your team if you restrict plants long term, "
            "especially when you take steroids or have other medical conditions.",
        ),
        (
            "paragraph",
            "Removing FODMAPs and fiber can reduce gas short term while inflammation may still "
            "smolder. Placebo and regression to the mean explain some online success stories.",
        ),
        ("heading_h2", "Evidence-Based Alternatives"),
        (
            "paragraph",
            "Mediterranean-style patterns with tolerated plants support long-term health in remission. "
            "Exclusive enteral nutrition is a supervised medical elimination with exit plans. Work with "
            "IBD dietitians instead of influencer meal plans. Cleanse and detox detail is covered in Chapter 42.",
        ),
        ("heading_h2", "Questions for Your Gastroenterologist"),
        (
            "list",
            [
                "Is a short low-residue plan appropriate for my current flare?",
                "Which micronutrients should we monitor if I restrict plants?",
                "How do we rebuild a balanced plate in remission?",
            ],
        ),
    ],
    1: [
        (
            "paragraph",
            "If you live with Crohn's disease or ulcerative colitis, food is never just food. "
            "Meals carry memory, culture, comfort, and fear, especially when urgency, pain, or "
            "nausea turn ordinary choices into high-stakes decisions. This chapter explains how "
            "intestinal inflammation, anatomy, and treatment change what eating feels like, so the "
            "rest of this book can stay practical rather than prescriptive.",
        ),
        ("heading_h2", "How intestinal inflammation affects appetite"),
        (
            "paragraph",
            "Active inflammation can suppress appetite while illness, weight loss, poor intake, "
            "or recovery may increase nutritional needs. Cytokines and pain steal attention from "
            "hunger cues. Nausea, early fullness, and fear of symptoms after eating can shrink "
            "portions even when nutritional needs may be higher. During these periods, nutrition "
            "priorities shift toward adequate energy, protein, and fluids, not perfect variety.",
        ),
        ("heading_h2", "How Crohn's and ulcerative colitis affect digestion and absorption"),
        (
            "paragraph",
            "Crohn's disease can involve any part of the gastrointestinal tract and may affect "
            "multiple segments. Ulcerative colitis typically involves the colon. Disease location "
            "matters: terminal ileum involvement raises vitamin B12 malabsorption risk; extensive "
            "small bowel disease or resection changes how you absorb fat, bile acids, and several "
            "micronutrients. Colonic disease may increase fluid and electrolyte losses during diarrhea.",
        ),
        (
            "paragraph",
            "Surgery, including resection, strictureplasty, ostomy creation, or pouch surgery, can "
            "control disease or address complications while permanently changing anatomy. Short bowel physiology, rapid transit, and ostomy "
            "output each create distinct nutrition needs that no universal internet list captures.",
        ),
        ("heading_h2", "Why symptoms and inflammation do not always match"),
        (
            "paragraph",
            "You can feel miserable after a meal without proving that the food worsened intestinal "
            "inflammation. Lactose intolerance, FODMAP sensitivity, fat malabsorption, or anxiety "
            "around eating can drive symptoms while calprotectin or endoscopy findings stay stable. "
            "Conversely, you can feel relatively well while silent inflammation persists. That is why "
            "food logs help most when paired with labs, scopes, and clinician interpretation, not "
            "when used as a solo diagnostic tool.",
        ),
        ("heading_h2", "Common nutritional consequences"),
        (
            "paragraph",
            "People with IBD may face unintentional weight loss, low muscle mass, anemia, vitamin D "
            "deficiency, low vitamin B12, iron deficiency, zinc depletion, and bone health concerns. "
            "Causes include reduced intake, malabsorption, bleeding, inflammation-driven losses, "
            "medication effects, and overly restrictive self-directed diets. Periodic laboratory "
            "monitoring, individualized to your disease location, symptoms, medications, and history "
            ", helps catch gaps before they become severe.",
        ),
        ("heading_h2", "How nutrition priorities change during a flare"),
        (
            "paragraph",
            "During active symptoms, many patients benefit from smaller, frequent meals; gentler "
            "textures; adequate protein; and careful hydration with electrolyte replacement when "
            "diarrhea is significant. Temporary low-fiber or low-residue patterns may reduce "
            "mechanical irritation for some people; they are tools for symptom relief, not proof "
            "that fiber is harmful forever. Your gastroenterologist or IBD dietitian should guide "
            "texture changes if you have strictures or recent surgery.",
        ),
        ("heading_h2", "How priorities change during remission"),
        (
            "paragraph",
            "When inflammation quiets, the goal expands: rebuild dietary variety, correct "
            "deficiencies, support bone health, and find sustainable patterns that include cultural "
            "foods and social meals. Reintroduction should be gradual and monitored. Unnecessary "
            "long-term restriction can create its own nutritional and quality-of-life problems.",
        ),
        ("heading_h2", "Your first weeks after diagnosis"),
        (
            "paragraph",
            "The first month after diagnosis is less about mastering every nutrient and more about "
            "building a safe routine: who to call, what to track, which questions to ask, and how "
            "to protect sleep and nutrition while treatment starts. Write down your exact diagnosis, "
            "recent scope or imaging findings, and every medicine started or stopped. Save clinic "
            "numbers, pharmacy contacts, and insurance information. Track stool frequency, blood, "
            "pain, sleep, and meals in a notebook or food log. Consistency beats complexity.",
        ),
        (
            "paragraph",
            "Ask for written flare instructions. Request copies of colonoscopy, pathology, and "
            "imaging reports. Bring observations to appointments so limited visit time targets your "
            "real concerns. Second opinions are reasonable when plans feel unclear or symptoms "
            "persist despite treatment.",
        ),
    ],
}

# Expanded stub chapters (replace NEW_CHAPTER_STUBS when present here)
CHAPTER_REWRITES[24] = [
    (
        "paragraph",
        "FODMAP reintroduction is a structured experiment supervised by your dietitian, not a "
        "test you pass or fail. After a short elimination phase, you add one FODMAP group at a "
        "time while noting gas, bloating, stool pattern, and pain over several days per group.",
    ),
    ("heading_h2", "What the evidence says"),
    (
        "paragraph",
        "Low-FODMAP approaches are primarily symptom-management strategies for irritable bowel-type "
        "symptoms in selected IBD patients in remission or with minimal inflammation. They do not "
        "replace anti-inflammatory medical therapy. Evidence label: Symptom-management strategy.",
    ),
    ("heading_h2", "Common reintroduction order (individualized)"),
    (
        "list",
        [
            "Fructans (onion, wheat, garlic), often tested first or avoided during active flares",
            "Lactose (milk, soft cheeses, yogurt), separate from primary IBD inflammation",
            "Polyols (stone fruits, sugar alcohols, some sweeteners)",
            "Galacto-oligosaccharides (legumes, some nuts)",
            "Excess fructose (honey, apples, mango in large portions)",
        ],
    ),
    ("heading_h2", "During a flare"),
    (
        "paragraph",
        "Pause reintroduction. Symptom noise from inflammation can mimic FODMAP intolerance. "
        "Resume when your gastroenterologist agrees disease activity is quieter and your dietitian "
        "approves the timeline.",
    ),
    ("heading_h2", "During remission"),
    (
        "paragraph",
        "Follow the challenge portions and schedule recommended by your dietitian. If symptoms flare, stop that group and retry later at a lower "
        "portion. If symptoms stay calm, add the food to your tolerated list and continue. The goal "
        "is the widest safe diet, not the shortest elimination list.",
    ),
    ("heading_h2", "When to ask your care team"),
    (
        "list",
        [
            "How long should my elimination phase last given my current inflammation?",
            "Which FODMAP groups fit my disease location and stricture history?",
            "Should we pause all reintroduction during active flares?",
            "Could my symptoms reflect inflammation rather than FODMAPs?",
        ],
    ),
]

CHAPTER_REWRITES[39] = [
    (
        "paragraph",
        "These sample days illustrate gentle combinations only. Portions, textures, and food choices "
        "must match your anatomy, strictures, ostomy output, bleeding status, and care team's guidance. "
        "Substitute foods from Part VI that you already tolerate.",
    ),
    ("heading_h2", "Sample Flare Day A"),
    (
        "list",
        [
            "Breakfast: congee or white rice porridge with soft-cooked egg",
            "Mid-morning: ripe banana",
            "Lunch: plain chicken broth with soft noodles",
            "Afternoon: oral rehydration sips per clinician advice",
            "Dinner: baked salmon with peeled mashed potato",
        ],
    ),
    ("heading_h2", "Sample Flare Day B"),
    (
        "list",
        [
            "Breakfast: oatmeal cooked extra soft with lactose-free yogurt",
            "Mid-morning: smooth applesauce (peeled)",
            "Lunch: turkey with white rice",
            "Afternoon: decaffeinated tea plus hydration goal",
            "Dinner: scrambled eggs with white toast",
        ],
    ),
    ("heading_h2", "Sample Flare Day C, Cultural Staples"),
    (
        "list",
        [
            "Breakfast: soft idli or khichdi with mild, well-cooked dal (small portion)",
            "Lunch: plain rice with soft-cooked chicken and broth",
            "Afternoon: lassi or oral rehydration if dairy tolerated",
            "Dinner: congee-style rice porridge with tofu or egg",
        ],
    ),
    ("heading_h2", "Sample Flare Day D, Mediterranean / Middle Eastern"),
    (
        "list",
        [
            "Breakfast: white pita with smooth hummus (small portion if legumes tolerated)",
            "Lunch: chicken soup with well-cooked carrots and rice",
            "Dinner: baked fish with peeled potato and strained broth",
        ],
    ),
    (
        "paragraph",
        "Track stool frequency, blood, pain, sleep, and meals in a notebook or app your team "
        "recommends. Contact your clinic for severe pain, vomiting, inability to keep fluids down, "
        "heavy bleeding, fever, or rapid weight loss.",
    ),
]

CHAPTER_REWRITES[46] = [
    (
        "paragraph",
        "Many people with Crohn's disease or ulcerative colitis have healthy pregnancies when "
        "nutrition, inflammation, and medications are planned with gastroenterology and "
        "obstetric teams early. This chapter focuses on questions to bring to those visits, "
        "not medication protocols.",
    ),
    ("heading_h2", "Before Conception and Early Pregnancy"),
    (
        "paragraph",
        "Some IBD medications require changes before conception, while many others may be "
        "continued during pregnancy. Medication decisions differ by drug and individual "
        "circumstances, so review every prescription and supplement with your gastroenterology "
        "and obstetric teams before conception and throughout pregnancy.",
    ),
    (
        "paragraph",
        "Stable disease activity before conception is a common planning goal. Your teams can "
        "interpret labs, symptoms, and imaging together rather than relying on diet changes "
        "alone.",
    ),
    ("heading_h2", "Nutrition and Supplements"),
    (
        "paragraph",
        "Folate, iron, vitamin D, and protein needs may rise during pregnancy, especially with "
        "active IBD, bleeding, or restricted intake. An IBD dietitian can help when appetite is "
        "low or diets feel too narrow.",
    ),
    (
        "paragraph",
        "Food safety counseling reduces infection risk without unnecessary fear of entire food "
        "groups. Bring a current supplement list to every prenatal visit.",
    ),
    ("heading_h2", "Flares During Pregnancy"),
    (
        "paragraph",
        "Call your clinic promptly for worsening pain, bleeding, fever, dehydration, or "
        "inability to keep fluids down. Emergency care is appropriate for severe symptoms. "
        "Your team balances maternal and fetal safety.",
    ),
    ("heading_h2", "After Delivery"),
    (
        "paragraph",
        "Breastfeeding questions, postpartum flares, and sleep loss are common topics. Schedule "
        "GI follow-up early in the postpartum period if symptoms shift.",
    ),
    ("heading_h2", "Questions for Your Gastroenterology and Obstetric Teams"),
    (
        "list",
        [
            "Which of my IBD medications and supplements are appropriate before and during pregnancy?",
            "When should we recheck iron, folate, vitamin D, and other nutrition labs?",
            "How will we monitor disease activity during pregnancy?",
            "What symptoms should trigger urgent contact during pregnancy or postpartum?",
            "Who coordinates care between GI, obstetrics, and any maternal-fetal medicine specialists?",
        ],
    ),
]

CHAPTER_REWRITES[51] = [
    (
        "paragraph",
        "Complete this worksheet after reading the book. Update it after medication changes, surgery, "
        "or sustained symptom shifts. Bring copies to GI and dietitian visits.",
    ),
    ("heading_h2", "Your personal nutrition snapshot"),
    (
        "list",
        [
            "Current disease state (flare / uncertain / remission): _______________",
            "Disease location: _______________",
            "Relevant surgeries: _______________",
            "Known strictures: _______________",
            "Current symptoms: _______________",
            "Main nutrition concerns: _______________",
        ],
    ),
    ("heading_h2", "My flare backup plan"),
    (
        "list",
        [
            "Tolerated starches: _______________",
            "Tolerated proteins: _______________",
            "Tolerated fluids: _______________",
            "Tolerated snacks: _______________",
            "Foods I temporarily modify: _______________",
            "Signs I should contact my care team: _______________",
        ],
    ),
    ("heading_h2", "Nutrition lab tracker"),
    (
        "paragraph",
        "Record date, result, and what your clinician said. Intervals should be individualized.",
    ),
    (
        "list",
        [
            "Iron / ferritin: _______________",
            "Vitamin B12: _______________",
            "Vitamin D (25-OH): _______________",
            "CRP or calprotectin (if used): _______________",
            "Other: _______________",
        ],
    ),
    ("heading_h2", "Food reintroduction tracker"),
    (
        "paragraph",
        "Food | Preparation | Portion | Symptoms | Timing | Try again?",
    ),
    ("heading_h2", "Questions for my GI / dietitian"),
    (
        "list",
        [
            "Am I at risk for iron deficiency given my bleeding history and labs?",
            "Do I need B12 monitoring based on my disease location or surgery?",
            "Should I modify fiber or texture given strictures or recent flares?",
            "Are any of my current restrictions unnecessary?",
            "Should I see an IBD-focused registered dietitian?",
            "Do any supplements interact with my medications?",
        ],
    ),
    ("heading_h2", "Three safe staple meals (last month)"),
    ("list", ["1. _______________", "2. _______________", "3. _______________"]),
    ("heading_h2", "Three foods under trial or reintroduction"),
    ("list", ["1. _______________", "2. _______________", "3. _______________"]),
    ("heading_h2", "Hydration goal and warning signs"),
    (
        "list",
        [
            "Goal: _______________",
            "Warning signs I watch for: _______________",
        ],
    ),
]


CHAPTER_PREPEND_BLOCKS: dict[int, list[Block]] = {}


def get_chapter_rewrite(chapter_num: int) -> list[Block] | None:
    return CHAPTER_REWRITES.get(chapter_num)


def get_chapter_prepend(chapter_num: int) -> list[Block] | None:
    return CHAPTER_PREPEND_BLOCKS.get(chapter_num)
