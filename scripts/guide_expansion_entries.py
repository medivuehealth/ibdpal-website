"""Expansion content for all 58 IBDPal patient guides."""
from __future__ import annotations

FOUNDATION_INTRO = (
    "Selected Crohn's & Colitis Foundation educational content and Marks are used on IBDPal under license. "
    "{body} "
    "The Foundation does not endorse IBDPal. Education only, not medical advice."
)


def sec(h: str, p1: str, p2: str, p3: str) -> dict:
    return {"heading": h, "paragraphs": [p1, p2, p3]}


def rel(*pairs: tuple[str, str]) -> list[dict]:
    return [{"label": a, "url": b} for a, b in pairs]


def fq(q: str, a: str) -> dict:
    return {"q": q, "a": a}


def mk(intro: str, sections: list, tips: list, faq_items: list, related: list) -> dict:
    return {"intro": intro, "sections": sections, "tips": tips, "faq": faq_items, "related": related}


def fmk(body: str, sections: list, tips: list, faq_items: list, related: list) -> dict:
    return mk(FOUNDATION_INTRO.format(body=body), sections, tips, faq_items, related)


ENTRIES: dict[str, dict] = {
    "what-should-i-eat-crohns-colitis": 
mk(
        "There is no single best diet for Crohn's disease or ulcerative colitis. Triggers, tolerance, and nutrient needs differ by person and by whether inflammation is active or quiet. This guide summarizes patterns many patients discuss with their gastroenterologist or IBD dietitian. Education only, not medical advice.",
        [
            sec('How disease activity changes food choices', 'During remission, many people aim for a varied pattern with fruits, vegetables, lean protein, and grains when their clinician agrees it is safe. The goal is adequate calories, protein, and micronutrients without unnecessary restriction.', 'During active symptoms, softer and lower-fiber foods are often easier to tolerate for a short time. Bananas, applesauce, white rice, plain pasta, eggs, broth-based soups, and lean poultry or fish appear frequently in patient education. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Your GI team may suggest temporary changes while inflammation is treated. Return to a broader diet when symptoms improve, rather than staying on a minimal list indefinitely without guidance. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
            sec('Building meals that support energy and healing', 'Spread protein across the day if appetite is low. Eggs, yogurt, tofu, fish, and tender meats are common choices when tolerated. Pair protein with gentle starches if fiber feels harsh.', 'Healthy fats from olive oil, avocado, or nut butters may help calories when weight is a concern. Introduce one new food at a time so you can notice patterns without guessing. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Ask whether you need labs for iron, vitamin D, vitamin B12, folate, zinc, or magnesium. Malabsorption and chronic inflammation can affect stores even when you eat well. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Fiber, FODMAPs, and special diets', "Fiber is not always harmful in IBD. Some people reduce insoluble fiber during flares and reintroduce cooked vegetables and whole grains in remission with their team's support.", 'Low FODMAP or other structured approaches are sometimes used under dietitian supervision for symptom relief. They are tools, not universal cures, and should fit your medical plan. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Avoid copying social media elimination lists without clinician input. Over-restriction can cause weight loss, fatigue, and social stress without improving inflammation. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Hydration and eating rhythm', 'Diarrhea, sweating, vomiting, or poor intake increase fluid needs. Water, oral rehydration solutions, broth, and decaffeinated teas are frequent suggestions when losses are higher.', 'Smaller, more frequent meals may feel better than large portions when nausea or early fullness is present. Keep simple snacks available for low-energy days. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Alcohol and high-caffeine drinks may worsen symptoms for some people. Ask your team what limits make sense for you.'),
            sec('Working with your IBD nutrition team', 'Bring a one- to two-week food and symptom log to appointments. Note stool pattern, pain, blood, urgency, and energy alongside meals.', 'Registered dietitians with IBD experience can help with enteral nutrition questions, repletion of deficiencies, and safe reintroduction plans. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'If you lose weight unintentionally, skip meals often, or fear most foods, tell your clinician promptly. Nutrition support is part of comprehensive IBD care.'),
        ],
        [
            'Log meals and symptoms for at least one week before diet visits.',
            'Reintroduce one new food every few days when expanding your diet.',
            'Ask your GI team about iron, B12, and vitamin D labs at least yearly.',
            'Keep gentle backup meals frozen for flare weeks.',
            "Pair online diet tips with your clinic's written plan, not instead of it.",
        ],
        [
            fq('Is there one best diet for all people with IBD?', 'No. Disease location, surgery history, activity level, and personal triggers vary. Your gastroenterologist or IBD dietitian should personalize guidance.'),
            fq('Should I cut out all fiber forever?', 'Not usually. Many patients temporarily lower fiber during active symptoms and expand variety in remission with clinician guidance.'),
            fq('Can diet alone put IBD in remission?', 'Nutrition matters and some supervised therapies are used clinically, but most people need medical monitoring and treatment tailored by their IBD team.'),
            fq('When should I see a dietitian?', 'Consider a referral for weight change, strictures, short bowel, repeated flares, anemia, or if you feel afraid to eat.'),
        ],
        rel(
            ("Foods during a Crohn's flare", '/guides/foods-to-eat-crohns-flare'),
            ('Anti-inflammatory diet and IBD', '/blog/anti-inflammatory-diet-ibd'),
            ("FODMAP diet for Crohn's and colitis", '/blog/fodmap-diet-crohns-colitis'),
            ('Track food and symptoms', '/guides/track-ibd-symptoms-food'),
            ('Foundation diet and nutrition bridge', '/guides/foundation-diet-nutrition-ibd'),
            ('Complete IBD nutrition article', '/blog/complete-ibd-nutrition-guide'),
        ),
    ),    "foods-to-eat-crohns-flare": 
mk(
        "When Crohn's inflammation is active, many people shift toward easy-to-digest meals and steady fluids. Food choices do not replace medical treatment, but they may reduce bowel irritation while your GI team adjusts therapy. These are common patterns from patient education, not rules that fit everyone.",
        [
            sec('Gentle foods many patients tolerate', 'Soft fruits such as bananas and applesauce, refined grains like white rice and plain pasta, and well-cooked potatoes are frequent short-term choices. Broth-based soups provide fluid and sodium when appetite is low.', 'Lean protein from eggs, tofu, fish, or tender poultry can help maintain muscle when intake drops. Smooth nut butters or yogurt may add calories if dairy is tolerated. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Avoid assuming a food is safe because it is on a list. Personal triggers still matter, and strictures or prior surgery can change what feels comfortable. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
            sec('Hydration during active diarrhea', 'Water alone may not replace electrolytes lost in stool. Oral rehydration solutions, diluted sports drinks, or broth can help when your team approves them.', 'Sip steadily through the day rather than chugging large volumes if nausea is present. Ice chips or popsicles may be easier when solids are hard to manage. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Limit alcohol and excess caffeine if they worsen urgency or dehydration. Herbal teas without strong laxative herbs are often better tolerated. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists.'),
            sec('Foods to approach carefully', 'Raw vegetables, tough skins, popcorn, nuts, seeds, and high-fat fried foods bother many people during flares. Spicy sauces and sugar alcohols in sugar-free products can increase gas or urgency.', 'Large salads, cruciferous vegetables, and heavy cream sauces are common short-term avoids, not lifetime bans. Reintroduce them when symptoms calm with guidance. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'If you have a known stricture, follow texture advice from your GI team. Fiber and bulk may need special modification. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.'),
            sec('Meal timing and portion size', 'Smaller meals four to six times daily may feel better than three large plates. Stop eating when comfortably full rather than pushing through pain.', 'Keep a few ready options at home: rice, eggs, canned fruit, and low-fiber crackers. Planning reduces stress on bad days. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'If you cannot maintain intake for more than a day or two, contact your clinic. Early nutrition support can prevent worsening weakness. Patient education supports shared decision making; it does not replace individual medical assessment.'),
            sec('Pairing diet with medical flare care', 'Medication changes, stool testing, imaging, or labs may be needed even if food adjustments help symptoms slightly. Do not delay outreach hoping diet alone will fix inflammation.', 'Track stool count, blood, fever, and weight at home. Share trends with your GI team at scheduled check-ins or sooner if red flags appear. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Mental health support matters during flares. Anxiety about food is common and worth discussing with your care team. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
        ],
        [
            'Stock oral rehydration packets before symptoms worsen.',
            'Cook vegetables until very soft before trying raw salads again.',
            'Eat the highest-protein foods when appetite is best, often mornings.',
            'Avoid comparing your flare menu to remission social media posts.',
            'Call your GI team if you cannot drink enough fluids for 24 hours.',
        ],
        [
            fq("Can the right foods stop a Crohn's flare?", 'Diet may ease irritation but does not treat underlying inflammation. Medical care from your IBD team is essential.'),
            fq('Is the BRAT diet enough long term?', 'BRAT-style foods are short-term comfort choices. Long restriction without clinician input can cause nutrient gaps.'),
            fq('Should I fast during a flare?', 'Do not fast without medical advice. Prolonged fasting can worsen fatigue and electrolyte problems.'),
        ],
        rel(
            ("Crohn's flare: what to do", '/guides/crohns-flare-what-to-do'),
            ('Flare first 48 hours article', '/blog/flare-first-48-hours'),
            ('IBD hydration guide', '/guides/ibd-hydration-fluids'),
            ('Low-residue diet basics', '/guides/low-residue-diet-ibd'),
            ('Flare help hub', '/flare-help'),
            ('Best foods during a flare article', '/blog/best-foods-crohns-flare'),
        ),
    ),    "ulcerative-colitis-diet-foods": 
mk(
        'Ulcerative colitis affects the colon lining, so diet during flares often focuses on reducing bowel irritation while maintaining nutrition. No single food list works for everyone, but patterns below are common in UC patient education. Pair these ideas with your gastroenterologist or IBD dietitian for a plan that fits your disease extent and activity.',
        [
            sec('UC flares and bowel-friendly choices', 'During active colitis, many patients tolerate soft, low-fiber foods temporarily. White rice, plain pasta, eggs, applesauce, and well-cooked carrots are frequent examples in clinic handouts.', 'Protein at each meal supports healing when appetite is reduced. Fish, tofu, and tender chicken are common choices if red meat feels heavy. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', "Spicy foods, large salads, and high-fiber bran may increase urgency for some people. Reintroduce them gradually when symptoms improve with your team's guidance. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends."),
            sec('Blood, urgency, and hydration', 'Visible blood and frequent stools increase fluid and electrolyte needs. Water plus oral rehydration solutions or broth may help when approved by your clinician.', 'Track how many bowel movements occur daily and whether blood is increasing. These details help your GI team decide on medication changes. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Caffeine and alcohol can worsen urgency for some patients. Ask whether temporary limits make sense during active symptoms. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
            sec('Remission nutrition goals', 'When inflammation is quiet, expanding variety supports long-term health. Cooked vegetables, fruits, whole grains, and legumes may be reintroduced stepwise.', 'Iron, vitamin D, and calcium are common labs in UC because of bleeding, steroid use, or dietary gaps. Request monitoring at routine visits. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'A registered dietitian can help if you fear food, lose weight, or follow multiple restrictions. Early support prevents malnutrition. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.'),
            sec('Personal triggers and food logs', "UC triggers differ from Crohn's triggers and from person to person. A simple log linking meals to stool pattern, pain, and energy reveals patterns faster than memory alone.", 'Introduce one new food every few days when expanding your diet. Note whether symptoms change within 24 to 48 hours. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Do not eliminate entire food groups without clinician input. Over-restriction can harm growth in youth and energy in adults. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
            sec('Medical care alongside diet', 'Diet supports comfort but does not replace anti-inflammatory treatment when colitis is active. Contact your IBD team if symptoms worsen or new fever appears.', 'Rescue plans, steroid courses, or biologic adjustments may be needed even when you eat carefully. Follow your written flare instructions. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Bring food logs and symptom trends to appointments. Shared data leads to faster, safer treatment decisions. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
        ],
        [
            "Compare stool count and blood to your personal baseline, not someone else's.",
            'Keep bland backup meals ready for high-urgency days.',
            'Ask about iron and vitamin D labs after bleeding episodes.',
            'Reintroduce fiber slowly in remission with dietitian support.',
            'Call your GI team if you cannot keep fluids down for 24 hours.',
        ],
        [
            fq('Does milk cause UC flares?', 'Lactose intolerance is common but separate from UC inflammation. Your team can guide testing and calcium sources.'),
            fq('Should all UC patients avoid fiber?', 'Not always. Many lower fiber during flares and increase cooked fiber in remission with clinician guidance.'),
            fq('Can diet cure ulcerative colitis?', 'No. Nutrition is one part of care. Medical treatment and monitoring remain essential.'),
        ],
        rel(
            ('UC flare management', '/guides/ulcerative-colitis-flare-management'),
            ('What should I eat with IBD?', '/guides/what-should-i-eat-crohns-colitis'),
            ('Low-residue diet basics', '/guides/low-residue-diet-ibd'),
            ('Blood in stool article', '/blog/blood-in-stool-ibd-when-to-worry'),
            ('Track symptoms and food', '/guides/track-ibd-symptoms-food'),
            ('Flare help hub', '/flare-help'),
        ),
    ),    "crohns-disease-diet-nutrition": 
mk(
        "Crohn's disease can affect any part of the digestive tract, so nutrition needs vary by disease location, prior surgery, and activity level. This guide outlines common diet and nutrition topics patients review with their GI team. It is educational only and does not replace personalized medical or nutrition advice.",
        [
            sec("How Crohn's location shapes nutrition", "Small bowel Crohn's may affect absorption of iron, B12, and fat-soluble vitamins. Colonic disease may present more with urgency and bleeding.", 'Strictures and prior resections change texture needs. Your clinician may recommend modified fiber or enteral nutrition in specific situations. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', "Pediatric Crohn's requires attention to growth. Parents should work closely with pediatric GI and dietitian teams on calories and micronutrients. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment."),
            sec('Flare versus remission eating', 'During flares, softer and lower-residue foods are often easier to tolerate short term. During remission, many patients rebuild variety with clinician support.', "Exclusive enteral nutrition is a supervised therapy for some Crohn's patients, especially youth. It is not a DIY juice cleanse. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.", 'Return toward a balanced pattern when symptoms improve rather than staying on a minimal diet out of fear. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
            sec('Micronutrients and labs to discuss', "Iron deficiency, low vitamin D, low B12, zinc deficiency, and bone health are frequent discussion points in Crohn's clinics.", 'Steroids, malabsorption, and chronic inflammation all influence labs. Annual or symptom-based testing may be appropriate. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Supplements should match documented deficiencies. High-dose self-supplementation can mask problems or cause side effects. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Protein, calories, and healing', 'Adequate protein supports tissue repair during and after flares. Spread intake across the day if appetite is low.', 'Healthy fats and calorie-dense snacks help when weight loss is unintended. Nut butters, olive oil, and smoothies are common tools when tolerated. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Tell your team if you skip meals regularly or fear eating. Early nutrition intervention prevents complications. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
            sec('Partnering with your care team', 'Bring a food and symptom log to visits. Note pain location, stool pattern, blood, and energy alongside meals.', 'Ask for dietitian referral if you have strictures, short bowel, repeated hospitalizations, or complex restrictions. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', "Online lists are starting points only. Your Crohn's phenotype and labs should guide real decisions. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists."),
        ],
        [
            "Ask where your Crohn's is located and how that affects diet advice.",
            'Request iron, B12, and vitamin D labs at routine visits.',
            'Introduce new foods one at a time when expanding after flares.',
            'Keep oral rehydration supplies at home for diarrhea-heavy weeks.',
            'Use IBDPal or a paper log to show trends, not single bad days.',
        ],
        [
            fq("Is Crohn's diet the same as colitis diet?", 'Patterns overlap, but location, surgery, and complications differ. Personalize with your IBD team.'),
            fq("Should I take probiotics for Crohn's?", 'Evidence varies by product and patient. Ask your gastroenterologist before starting supplements.'),
            fq('Can diet replace biologics?', 'No. Nutrition supports overall care but does not replace medical treatment for active inflammation.'),
        ],
        rel(
            ("Foods during a Crohn's flare", '/guides/foods-to-eat-crohns-flare'),
            ('Protein and healing in flares', '/guides/protein-healing-ibd-flare'),
            ('Iron deficiency nutrition', '/guides/iron-deficiency-nutrition-ibd'),
            ("What is Crohn's? Foundation basics", '/guides/what-is-crohns-disease-foundation'),
            ('Complete nutrition article', '/blog/complete-ibd-nutrition-guide'),
            ("Crohn's disease hub", '/crohns-disease'),
        ),
    ),    "low-residue-diet-ibd": 
mk(
        'A low-residue or low-fiber diet reduces undigested material moving through the bowel. Some IBD patients use it short term during symptoms or before procedures, always with clinician guidance. This guide explains common principles and limits. It is not a long-term plan unless your GI team recommends one.',
        [
            sec('What low-residue means in practice', 'Low-residue eating limits high-fiber foods such as whole grains, nuts, seeds, raw vegetables, and tough fruit skins. The goal is less bulk and slower transit when the bowel is irritated.', 'Cooking, peeling, and pureeing foods can lower residue without eliminating nutrition entirely. Well-cooked carrots, potatoes without skin, and refined grains are typical examples. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Duration matters. Many patients use this pattern for days to weeks, then expand under supervision. Staying low-residue indefinitely can reduce micronutrient intake. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('When clinicians suggest it', 'Active diarrhea, pre-colonoscopy prep windows, strictures, or post-operative phases are common reasons a team may suggest temporary low-residue choices.', 'It does not treat inflammation itself. Medication adjustments, imaging, or labs may still be needed during flares. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Ask your clinician how long to stay low-residue and how to reintroduce fiber safely afterward. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
            sec('Foods often included and avoided', 'Included examples: white bread, white rice, plain pasta, eggs, tender meat, canned fruit without skins, smooth peanut butter, and well-cooked vegetables without seeds.', 'Often limited: popcorn, corn, berries with seeds, cruciferous vegetables, legumes, whole nuts, and bran cereals. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Personal tolerance still rules. A food on an avoid list may be fine for you in small amounts, or a safe food may trigger symptoms. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Nutrition pitfalls to avoid', 'Low-residue does not mean low protein or low calories. Maintain adequate intake for healing, especially during flares.', 'Calcium, fiber for colon health in remission, and fermented foods may be deferred temporarily but should be planned back in with your team. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Children and teens need growth-focused plans. Do not impose adult low-residue lists without pediatric GI input. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
            sec('Transitioning back to regular eating', 'Reintroduce fiber gradually: cooked vegetables first, then whole grains and raw produce as tolerated.', 'Log symptoms as you expand. One new food every few days clarifies triggers versus coincidence. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Pair dietary changes with medical follow-up. Symptom relief from low-residue eating does not always mean inflammation resolved. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
        ],
        [
            'Clarify with your GI team how long low-residue should last.',
            'Peel and cook produce to reduce residue while keeping some nutrients.',
            'Do not skip protein during low-residue phases.',
            'Plan a fiber reintroduction schedule with your clinician.',
            'Use low-residue as a tool, not an identity.',
        ],
        [
            fq('Is low-residue the same as low-FODMAP?', 'No. They target different mechanisms. Some foods overlap, but the plans serve different goals and need clinician context.'),
            fq('Can I eat salad on low-residue?', 'Large raw salads are usually limited. Small amounts of well-cooked greens may be acceptable depending on your situation.'),
            fq('Will low-residue put me in remission?', 'It may ease symptoms temporarily but does not replace anti-inflammatory treatment for active IBD.'),
        ],
        rel(
            ("Foods during a Crohn's flare", '/guides/foods-to-eat-crohns-flare'),
            ('UC diet foods guide', '/guides/ulcerative-colitis-diet-foods'),
            ('Colonoscopy prep article', '/blog/colonoscopy-prep-ibd'),
            ('What should I eat with IBD?', '/guides/what-should-i-eat-crohns-colitis'),
            ('Foundation diet and nutrition', '/guides/foundation-diet-nutrition-ibd'),
        ),
    ),    "ibd-hydration-fluids": 
mk(
        'Dehydration is a common concern in IBD when diarrhea, vomiting, fever, or poor intake increase fluid losses. Hydration supports energy, kidney function, and electrolyte balance. This guide covers practical fluid strategies patients discuss with their GI team. It does not replace medical assessment for severe dehydration.',
        [
            sec('Why IBD raises fluid needs', 'Frequent stools, ostomy output, night sweats, and vomiting all increase water and electrolyte losses. Fever adds further demand.', 'Some medications and hot weather amplify risk. Travel, exercise, and illness stacks burdens quickly. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Thirst alone is a late signal. Track urine color, dizziness, heart rate, and intake patterns during symptomatic weeks. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.'),
            sec('What to drink and when', 'Water is the base, but diarrhea often needs sodium and potassium replacement. Oral rehydration solutions, broth, or clinician-approved electrolyte drinks may help.', 'Sip steadily through the day. Large gulps may worsen nausea. Ice chips and popsicles count toward intake when solids are hard. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Limit alcohol and excess caffeine if they worsen urgency or sleep. Herbal teas without strong laxative herbs are often better tolerated. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
            sec('Signs to contact your care team', 'Very dark urine, dizziness on standing, rapid heartbeat, confusion, or inability to keep fluids down for 24 hours need prompt outreach.', "Bloody diarrhea with lightheadedness may require urgent evaluation. Follow your clinic's red-flag instructions. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.", 'Infants, children, and older adults dehydrate faster. Caregivers should call pediatric or adult GI teams early. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Hydration with ostomies and surgery', 'High ostomy output increases sodium needs. Your team may recommend specific electrolyte strategies or labs.', 'After bowel surgery, absorption patterns change. Follow surgeon and GI guidance on fluids and salts. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Weighing yourself at the same time daily can reveal fluid loss trends when stool counts are hard to measure. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
            sec('Everyday habits that help', 'Carry a bottle and set phone reminders if you forget to drink. Pair fluids with meals and medications unless told otherwise.', "During flares, reduce intense exercise until intake stabilizes. Resume gradually with your team's OK. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.", 'Discuss sports drinks, coconut water, and homemade oral rehydration recipes with your clinician to avoid too much sugar or too little sodium. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists.'),
        ],
        [
            'Keep oral rehydration packets in your bag and at home.',
            'Track intake and stool count during bad weeks.',
            'Ask your team about sodium needs with high ostomy output.',
            'Avoid chugging large volumes if nauseated.',
            'Seek urgent care if you cannot retain fluids.',
        ],
        [
            fq('Is water enough during diarrhea?', 'Often not. Electrolytes lost in stool may need replacement. Ask your GI team what products are appropriate.'),
            fq('Do sports drinks help IBD flares?', 'Some help short term, but sugar content and sodium levels vary. Clinician guidance prevents wrong balance.'),
            fq('When is dehydration an emergency?', 'Confusion, fainting, very low urine output, or persistent vomiting with dizziness warrant urgent evaluation.'),
        ],
        rel(
            ("Crohn's flare: what to do", '/guides/crohns-flare-what-to-do'),
            ('Flare emergency supplies', '/guides/ibd-flare-emergency-supplies'),
            ('Foods during a flare', '/guides/foods-to-eat-crohns-flare'),
            ('Living with an ostomy', '/guides/living-with-ostomy-ibd'),
            ('Flare help hub', '/flare-help'),
            ('Chronic diarrhea causes article', '/blog/chronic-diarrhea-ibd-causes'),
        ),
    ),    "crohns-colitis-support-groups": 
mk(
        "Living with Crohn's disease or ulcerative colitis can feel isolating. Support groups connect you with peers who understand flares, medications, work stress, and relationship challenges. This guide explains types of IBD support and how to find groups safely. Education only, not a substitute for medical care.",
        [
            sec('Types of IBD peer support', 'In-person chapter meetings, virtual groups, teen and parent groups, and condition-specific communities each serve different needs.', 'Some groups are facilitated by health professionals; others are peer-led. Ask how meetings are moderated and what privacy rules apply. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Online forums offer 24/7 access but vary in quality. Prefer spaces with clear community guidelines and referral to clinicians for medical decisions. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.'),
            sec('Benefits many patients report', 'Sharing practical tips on clinic navigation, insurance, and daily coping can reduce anxiety. Hearing remission stories may restore hope.', "Caregivers and partners benefit from separate groups focused on their role. Family attendance at patient groups should follow each group's norms. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.", 'Support complements medical care. Peers cannot diagnose, prescribe, or replace your gastroenterologist. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
            sec('Finding reputable groups', "The Crohn's and Colitis Foundation chapters list local meetings and events. Hospitals and academic centers sometimes host IBD networks.", 'Ask your GI clinic if they recommend local groups or social workers who facilitate connections. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Camp Oasis and youth programs serve children and teens with IBD. Parents should review medical supervision policies. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Safety and boundaries online', 'Avoid sharing personal identifiers publicly. Be cautious with treatment advice from strangers.', 'Report misinformation politely or leave groups that encourage stopping prescribed medications without medical oversight. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Crisis support belongs to licensed helplines and your care team, not general chat rooms. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Starting when you feel ready', 'You can listen without sharing at first meetings. Many people attend only during newly diagnosed or flare seasons.', 'If a group feels negative or overwhelming, try another format. Fit matters more than loyalty to one community. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Bring questions from support back to your clinician. Peer experience informs; your team personalizes. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists.'),
        ],
        [
            'Try one virtual and one in-person option before deciding.',
            'Ask moderators how medical misinformation is handled.',
            'Bring a friend or partner to your first meeting if allowed.',
            'Use IBDPal logs to share concrete trends with peers and clinicians.',
            'Check Foundation chapter listings for local events.',
        ],
        [
            fq('Are online IBD groups safe?', 'Many are helpful with clear rules. Protect privacy and verify medical advice with your GI team.'),
            fq('Can support groups replace therapy?', 'No. They complement mental health care but are not licensed counseling.'),
            fq('Do I have to share my story?', 'No. Listening is a valid way to participate.'),
        ],
        rel(
            ('Find a Foundation chapter group', '/guides/find-ccf-chapter-support-group'),
            ('IBD support near me', '/guides/ibd-support-near-me'),
            ('Foundation emotional wellness', '/guides/foundation-emotional-wellness-ibd'),
            ('Stress and anxiety with IBD', '/guides/stress-anxiety-ibd'),
            ('Camp Oasis for kids', '/guides/camp-oasis-kids-ibd'),
            ('IBD helpline resources', '/guides/ibd-crohns-colitis-helpline'),
        ),
    ),    "ibd-support-near-me": 
mk(
        'Finding IBD support close to home can improve coping, practical knowledge, and sense of community. This guide helps you search local chapters, hospital programs, and vetted online options. Always verify that peer advice aligns with guidance from your gastroenterologist or IBD center.',
        [
            sec('Start with your IBD clinic', 'Ask nurses, social workers, or patient navigators if the practice hosts groups or partners with local chapters.', 'Academic IBD centers often list community events, education nights, and mentor programs on their websites. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Bring a one-page summary of what you need: newly diagnosed support, parenting a child with IBD, or ostomy peers. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Foundation chapters and events', "The Crohn's and Colitis Foundation maintains chapter locators with meetings, walks, and advocacy events.", 'Chapter volunteers understand insurance appeals, school forms, and local provider networks from lived experience. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Virtual chapter meetings expand access if driving or symptoms limit attendance. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
            sec('Hospital and nonprofit resources', "Children's hospitals may offer teen IBD groups and family education days. Adult hospitals sometimes partner with ostomy associations.", 'Faith communities, community centers, and rare-disease coalitions occasionally host IBD speakers. Check event medical disclaimers. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Libraries and patient education departments may keep printed resource lists updated yearly. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Evaluating online local groups', 'Search social platforms for city plus IBD or ostomy keywords, then review group rules and admin activity.', 'Prefer groups that redirect medical questions to clinicians and discourage dangerous home remedies. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', "Protect your address, employer details, and children's identities in public posts. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends."),
            sec('When professional support fits better', 'Severe anxiety, depression, trauma, or eating disorders need licensed mental health care, not only peer groups.', 'GI psychologists and social workers specialize in coping with chronic illness. Ask your clinic for referrals. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Crisis lines and emergency services remain the right path for suicidal thoughts or medical emergencies. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
        ],
        [
            'Search Foundation chapter locator plus your ZIP code.',
            'Ask your GI office for a social work referral.',
            'Try a virtual meeting if travel is hard during flares.',
            'Visit one session before committing long term.',
            'Pair peer support with clinic follow-up, not instead of it.',
        ],
        [
            fq('How do I find pediatric IBD support?', "Children's hospitals, Camp Oasis, and Foundation family programs are common starting points."),
            fq('Are ostomy groups separate from IBD groups?', 'Often yes, though overlap exists. Both can be valuable depending on your needs.'),
            fq('What if no local group exists?', 'Virtual Foundation meetings and moderated online communities can fill gaps.'),
        ],
        rel(
            ("Crohn's and colitis support groups overview", '/guides/crohns-colitis-support-groups'),
            ('Find a Foundation chapter', '/guides/find-ccf-chapter-support-group'),
            ('Pediatric IBD help', '/guides/pediatric-crohns-colitis-help'),
            ('Partner and caregiver guide', '/guides/partner-caregiver-ibd'),
            ('Foundation resources hub', '/crohns-colitis-foundation-resources'),
        ),
    ),    "pediatric-crohns-colitis-help": 
mk(
        "When a child or teen has Crohn's disease or ulcerative colitis, families juggle growth, school, emotions, and complex treatment plans. This guide highlights education topics parents discuss with pediatric GI teams. It does not replace individualized pediatric medical advice.",
        [
            sec('Pediatric IBD differs from adult care', 'Growth, puberty, bone density, and vaccine schedules need special attention. Pediatric gastroenterologists monitor height, weight, and development at each visit.', "Exclusive enteral nutrition and specific biologic pathways are more common in pediatric Crohn's than in many adult practices. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.", 'Parents should receive written flare plans, school forms, and emergency contacts from the care team. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('School, activities, and social life', '504 plans or equivalent accommodations may cover restroom access, medication timing, and make-up work after absences.', 'Coaches, teachers, and school nurses benefit from concise medical letters without oversharing private details. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Camp Oasis and teen groups help young patients meet peers who understand IBD. Review medical supervision policies before enrolling. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
            sec('Nutrition and growth at home', 'Avoid restrictive diets without dietitian and GI approval. Children need adequate calories for growth even during symptoms.', 'Track appetite, stool pattern, and energy alongside meals. Bring logs to clinic visits. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Iron, vitamin D, and zinc deficiencies are common discussion points in pediatric labs. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Emotional health for child and family', 'Anxiety about bathrooms, body image, and injections is normal. Child psychologists familiar with chronic illness can help.', 'Siblings may need their own support. Family meetings with social workers can improve communication. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Watch for signs of depression, eating disorders, or medication avoidance. Report concerns early. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Building a durable care partnership', 'Transition planning to adult GI should start in adolescence. Teens gradually take ownership of appointments and refills.', 'Keep a shared calendar for infusions, labs, and scopes. Missing monitoring delays catches complications. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Use reputable Foundation and hospital education rather than unmoderated social media for treatment decisions. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
        ],
        [
            'Request a written school accommodation letter each year.',
            'Keep a pediatric flare kit at school and home.',
            'Log growth metrics and symptoms between visits.',
            'Explore Camp Oasis and teen support when age-appropriate.',
            'Ask when transition to adult GI should begin.',
        ],
        [
            fq('Can my child play sports with IBD?', 'Many do with clinician clearance. Plan hydration, restroom access, and recovery after flares.'),
            fq('Should kids follow adult diet blogs?', 'No. Pediatric plans must protect growth. Work with pediatric GI and dietitian teams.'),
            fq('How do we handle injections at school?', "Coordinate with school nurse and your team's medication action plan."),
        ],
        rel(
            ('Youth and school Foundation resources', '/guides/youth-school-foundation-resources'),
            ('Camp Oasis guide', '/guides/camp-oasis-kids-ibd'),
            ('Newly diagnosed guide', '/guides/newly-diagnosed-crohns-colitis'),
            ('Track symptoms and food', '/guides/track-ibd-symptoms-food'),
            ('College with IBD article', '/blog/college-with-ibd'),
            ('Newly diagnosed hub', '/newly-diagnosed'),
        ),
    ),    "newly-diagnosed-crohns-colitis": 
mk(
        "A new Crohn's or colitis diagnosis brings tests, new vocabulary, and uncertainty about daily life. This guide outlines first steps many patients take with their GI team in the early weeks. Education only, not medical advice or a treatment plan.",
        [
            sec('Understanding your diagnosis', "IBD includes Crohn's disease, ulcerative colitis, and sometimes IBD-unclassified. Location, severity, and extraintestinal features shape your roadmap.", 'Colonoscopy, imaging, stool tests, and blood work help classify disease. Keep copies of pathology and imaging reports. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Write down words you do not know and ask at your next visit. Good clinicians welcome questions. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Building your care team', 'Gastroenterologist, nurse, dietitian, pharmacist, and mental health support each play roles. Ask who to call for flares versus routine refills.', 'Save infusion center, after-hours, and portal messaging instructions in your phone. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Second opinions are reasonable for complex cases. Bring records digitally when possible. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
            sec('Daily life in the first months', 'Start simple symptom and food logs. Patterns help faster than guessing triggers.', "Learn your clinic's red-flag symptoms: fever, severe pain, persistent bleeding, dehydration, or new joint or eye issues. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.", 'Tell employers or school nurses only what you need for accommodations. You control disclosure. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Medications and follow-up', 'Many treatment plans include anti-inflammatory drugs, immunomodulators, or biologics. Ask about monitoring labs and infection prevention.', 'Take medications as prescribed unless your team says otherwise. Stopping suddenly can cause rebound inflammation. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Vaccine updates and travel planning become ongoing topics. Request a medication list card for emergencies. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Emotional adjustment and support', 'Grief, anger, and fear are common after diagnosis. Peer groups and counseling can help alongside medical care.', 'Partners and parents need education too. Share Foundation and IBDPal guides rather than carrying everything alone. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Progress is rarely linear. Celebrate small wins like completed labs or returned energy. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
        ],
        [
            'Create a binder or folder for test results and visit notes.',
            'Save after-hours GI contact in your phone today.',
            'Start a one-line daily symptom note.',
            'Ask for a written flare plan before you need it.',
            'Explore newly diagnosed Foundation resources.',
        ],
        [
            fq('Will I need surgery?', 'Some patients do, many do not. Your disease course is individual. Focus on monitoring and adherence first.'),
            fq('Can I work or study normally?', 'Many people do with accommodations during flares. School and workplace rights guides can help.'),
            fq('Is IBD contagious?', 'No. IBD is not spread person to person.'),
        ],
        rel(
            ('Foundation newly diagnosed first week', '/guides/newly-diagnosed-foundation-first-week'),
            ('What is IBD? Foundation basics', '/guides/what-is-ibd-foundation'),
            ('First GI appointment guide', '/guides/first-gastroenterology-appointment-ibd'),
            ('Visit prep checklist', '/visit-prep'),
            ('Newly diagnosed hub', '/newly-diagnosed'),
            ('Track symptoms and food', '/guides/track-ibd-symptoms-food'),
        ),
    ),    "crohns-flare-what-to-do": 
mk(
        "A Crohn's flare means symptoms have worsened beyond your usual baseline, often signaling increased inflammation. Medical decisions belong with your IBD team. This guide covers recognizing flare signs, first 24 to 48 hour steps, hydration, diet, when to call for help, logging, medications, and mental health. Education only, not medical advice.",
        [
            sec('Recognizing flare signs early', 'Compare current symptoms to your typical remission pattern. More frequent stools, new or heavier bleeding, worsening pain, fever, fatigue, mouth sores, or unintended weight loss may signal a flare.', 'Nighttime bowel movements, cramping that limits activity, or joint pain can accompany bowel inflammation. Note when changes started and whether they are accelerating. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'A single bad day differs from a sustained trend. Track three to seven days before deciding it is a true flare versus a brief stomach bug. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
            sec('First 24 to 48 hours at home', 'Contact your IBD team using their flare pathway if symptoms exceed your written plan. Many clinics offer nurse triage or on-call GI coverage.', 'Rest, simplify meals, and pause nonessential stress where possible. Gather recent labs, medication list, and symptom log for the call. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', "Do not start steroids left over from prior years or borrow a friend's medication unless your clinician explicitly instructs you. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists."),
            sec('Hydration, electrolytes, and diet adjustments', 'Increase fluids with water, oral rehydration solutions, or broth if your team approves. Diarrhea and fever raise sodium and potassium needs.', 'Shift toward softer, lower-fiber foods temporarily if they reduce irritation. Bananas, rice, applesauce, eggs, and lean protein are common short-term choices. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Alcohol, heavy spices, and large high-fat meals often worsen symptoms. Reexpand diet when inflammation improves with medical treatment. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.'),
            sec('When to call GI, urgent care, or the ER', 'Call your GI team for worsening stool count, blood, pain, or fever according to your action plan. Same-day nurse triage may prevent ER visits.', 'Urgent care can help with dehydration assessments, fever workups, or pain control when GI is unreachable, if they coordinate with your records. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Go to the emergency room for severe abdominal pain, fainting, heavy bleeding, persistent vomiting, high fever, or signs of dehydration despite fluids. Trust your instinct when symptoms feel unlike prior flares. Patient education supports shared decision making; it does not replace individual medical assessment.'),
            sec('What to log, medications, and mental health', 'Log stool frequency, blood presence, pain score, temperature, weight, and foods tolerated. Photos of stool are usually unnecessary unless your team requests them.', 'Take prescribed maintenance and rescue medications on schedule. Missing biologics or immunomodulators can prolong flares. Ask about drug levels or stool calprotectin if flares repeat. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Flares increase anxiety and sleep disruption. Brief walks, breathing exercises, and counseling referrals help. You are not failing because a flare occurred; inflammation needs medical attention. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
        ],
        [
            'Save your clinic flare hotline and after-hours number now.',
            'Keep oral rehydration packets and bland foods stocked.',
            'Log symptoms daily during flares for faster triage.',
            'Never change biologics or steroids without clinician guidance.',
            'Tell someone you trust when symptoms worsen for emotional support.',
        ],
        [
            fq('How do I know if it is a flare or a virus?', 'Duration, blood, joint pain, and comparison to your baseline help. Your GI team may order stool tests or labs.'),
            fq('Should I go to the ER for blood in stool?', 'Heavy bleeding, dizziness, or large clots need urgent evaluation. Call your team for guidance on moderate changes.'),
            fq('Can stress alone cause a flare?', 'Stress affects symptoms and may influence inflammation for some people. Medical assessment still matters when bowel symptoms change.'),
        ],
        rel(
            ('Flare help hub', '/flare-help'),
            ("Foods during a Crohn's flare", '/guides/foods-to-eat-crohns-flare'),
            ('Flare first 48 hours article', '/blog/flare-first-48-hours'),
            ('Flare emergency supplies', '/guides/ibd-flare-emergency-supplies'),
            ('IBD hydration guide', '/guides/ibd-hydration-fluids'),
            ('Stress and anxiety with IBD', '/guides/stress-anxiety-ibd'),
        ),
    ),    "ulcerative-colitis-flare-management": 
mk(
        'Ulcerative colitis flares often bring increased bowel frequency, urgency, blood, and fatigue. Early communication with your gastroenterologist can shorten recovery and prevent complications. This guide summarizes UC flare self-management topics patients review in clinic. Education only, not a substitute for medical care.',
        [
            sec('UC flare symptoms to track', 'Count bowel movements day and night. Note blood amount, urgency, cramping, and fever.', 'Weight loss, racing heart, or dizziness may signal dehydration or anemia. Weigh yourself weekly during flares. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Compare symptoms to your last remission period. Sudden changes warrant faster outreach than gradual drift. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.'),
            sec('First steps in the first days', 'Use your written flare plan if you have one. Call the IBD nurse line before starting old steroid packs on your own.', 'Simplify diet toward low-residue, low-irritant foods if tolerated. Hydrate with oral rehydration solutions when diarrhea is heavy. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Cancel nonessential obligations to rest. Stress management supports but does not replace medical treatment. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
            sec('Medical treatment and testing', 'Stool calprotectin, blood work, and sigmoidoscopy or colonoscopy may guide therapy changes. Follow through on ordered tests.', 'Rescue steroids, increased mesalamine, or biologic adjustments are common paths. Adherence to maintenance drugs prevents future flares. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Ask about blood clots, anemia, and infection risks during severe flares. Hospitalization is sometimes needed for IV steroids or fluids. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('When to seek urgent or emergency care', 'Severe bleeding, fainting, extreme abdominal distension, or ten or more bloody stools daily are examples of scenarios requiring emergency evaluation.', 'Toxic megacolon is rare but serious. Severe pain with fever and a rigid abdomen need immediate care. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'If unsure, call your GI on-call line. Document their advice and symptoms. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Recovery and preventing the next flare', 'Taper medications only as directed. Finish courses unless your team adjusts early based on side effects.', 'Reintroduce foods slowly as symptoms improve. Fiber expansion should be gradual with clinician input. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Review vaccine status, smoking cessation, and medication levels at follow-up. Log triggers and stressors for future planning. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists.'),
        ],
        [
            'Keep a UC flare card with clinic numbers in your wallet.',
            'Photograph medication labels for nurse triage calls.',
            'Track nocturnal stools separately; they matter clinically.',
            'Do not stop mesalamine without asking your team.',
            'Schedule follow-up labs after rescue steroid courses.',
        ],
        [
            fq('Is bloody diarrhea always an emergency?', 'Not always, but volume, dizziness, and pace of change matter. Call your team for personalized triage.'),
            fq('Can I travel during a UC flare?', 'Mild changes may be OK with planning. Worsening symptoms usually need treatment before travel.'),
            fq('Does UC always need hospitalization in flares?', 'No, but severe cases might. Early outreach reduces admission risk.'),
        ],
        rel(
            ("Crohn's flare guide", '/guides/crohns-flare-what-to-do'),
            ('UC diet foods', '/guides/ulcerative-colitis-diet-foods'),
            ('Flare help hub', '/flare-help'),
            ('Blood in stool article', '/blog/blood-in-stool-ibd-when-to-worry'),
            ('Track symptoms and food', '/guides/track-ibd-symptoms-food'),
            ('Foundation pain and fatigue', '/guides/foundation-ibd-pain-fatigue'),
        ),
    ),    "track-ibd-symptoms-food": 
mk(
        'Symptom and food tracking helps you and your GI team spot patterns, evaluate treatments, and prepare for visits. Simple, consistent logs beat perfect but abandoned apps. This guide explains what to record and how to use data without obsessing. Education only, not medical advice.',
        [
            sec('Why tracking matters in IBD', 'Memory bias makes single clinic days unreliable. A week of logs shows stool frequency, blood, pain, and diet links more clearly.', 'Medication changes, travel, stress, and menstrual cycles affect symptoms. Notes provide context labs alone miss. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Tracking supports disability paperwork, school forms, and insurance appeals with objective trends. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('What to log each day', 'Stool count, blood presence, urgency, pain score, energy, sleep, and key foods are core fields. Weight weekly adds value during flares.', 'Record medications taken, missed doses, and supplements. Note fever, joint pain, or skin changes. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'One line per meal plus snacks is enough. Perfect calorie counts are rarely needed unless a dietitian requests them. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
            sec('Food logging without fear', 'Track patterns, not moral judgment. Foods are data points, not failures.', 'Introduce one new food at a time when testing tolerance. Mark days of travel, alcohol, or restaurant meals. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Share logs with your dietitian to separate inflammation from irritant symptoms when possible. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Tools: paper, apps, and IBDPal', 'Paper diaries work when phones feel overwhelming. Photo of a notebook page is fine for portals.', 'Apps should export PDF or CSV for clinic visits. Check privacy policies before syncing health data. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'IBDPal and similar tools combine symptoms, meals, and Bristol stool types for flare discussions. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Using logs at appointments', 'Summarize the worst week and the best week since your last visit. Highlight changes after medication adjustments.', 'Ask whether calprotectin, CRP, or imaging align with your symptom log. Mismatch guides further testing. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Stop logging intensively once patterns are clear if it harms mental health. Your clinician can suggest lighter cadence. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
        ],
        [
            'Log at the same times daily to build habit.',
            'Use Bristol stool chart terms for clarity.',
            'Note menstrual cycle days if urgency fluctuates.',
            'Export a PDF before each GI visit.',
            'Pair food logs with sleep and stress columns.',
        ],
        [
            fq('Do I need to log forever?', 'No. Many patients log heavily around flares and lightly in remission.'),
            fq('Can tracking cause anxiety?', 'Yes. Simplify fields or pause if obsessive. Discuss with your care team.'),
            fq('Should I photograph every meal?', 'Usually not required unless a dietitian asks.'),
        ],
        rel(
            ('IBD nutrition tracking app guide', '/guides/ibd-nutrition-tracking-app'),
            ("Crohn's food triggers", '/guides/crohns-food-triggers'),
            ('Visit prep checklist', '/visit-prep'),
            ('Bristol stool chart article', '/blog/bristol-stool-chart-ibd'),
            ('Tracking with IBDPal article', '/blog/tracking-food-symptoms-ibdpal'),
            ('Doctor visit prep guide', '/guides/crohns-doctor-visit-prep'),
        ),
    ),    "ibd-nutrition-tracking-app": 
mk(
        'Nutrition tracking apps can help IBD patients document intake, symptoms, and trends between clinic visits. Choosing the right tool depends on your goals, privacy comfort, and whether a dietitian will review exports. This guide compares practical features without endorsing a single product. Education only.',
        [
            sec('Goals before choosing an app', 'Clarify whether you need calorie counts, macro tracking, trigger identification, or simple meal photos for your dietitian.', 'Pediatric patients need age-appropriate tools and caregiver involvement. Growth-focused tracking differs from adult weight loss apps. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'If mental health suffers from detailed logging, prioritize minimal fields or paper logs. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Features that help IBD care', 'Custom symptoms, stool type, pain scores, and medication reminders support flare conversations.', 'Export to PDF or CSV helps gastroenterology visits. Cloud backup prevents lost data during phone upgrades. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Barcode scanners speed entry but miss home-cooked meals. Quick free-text notes often work better for mixed diets. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
            sec('Privacy and data sharing', 'Read whether health data is sold, shared with employers, or used for ads. HIPAA-covered apps differ from consumer wellness apps.', 'Disable public social feeds if they encourage comparison or risky advice. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Ask your clinic if they integrate with any patient portals before paying for premium tiers. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('IBDPal and combined approaches', 'IBDPal links meals, symptoms, and disease education in one IBD-focused experience. Use it alongside clinician guidance, not as diagnosis.', 'Some patients use a simple symptom app plus a photo food diary. Consistency beats feature overload. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Bring exported summaries to visits rather than scrolling live during short appointments. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Working with your dietitian', 'Share two weeks of logs before nutrition visits. Highlight flares, travel, and restaurant weeks.', 'Ask which metrics matter: protein grams, iron intake, or simply meal timing. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Stop tracking fields your dietitian does not use. Simpler logs improve adherence. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
        ],
        [
            'Pick one app and use it for two weeks before switching.',
            'Turn off calorie goals if they trigger restriction.',
            'Export data the night before GI visits.',
            'Log medications alongside meals.',
            'Ask your dietitian which app exports they prefer.',
        ],
        [
            fq('Are nutrition apps medical devices?', 'Most consumer apps are not FDA-cleared for IBD treatment. Treat them as diaries.'),
            fq('Can apps diagnose food allergies?', 'No. Elimination and testing need clinician supervision.'),
            fq('Is IBDPal a replacement for my GI?', 'No. It supports education and logging between professional visits.'),
        ],
        rel(
            ('Track symptoms and food', '/guides/track-ibd-symptoms-food'),
            ('What should I eat with IBD?', '/guides/what-should-i-eat-crohns-colitis'),
            ('Tracking with IBDPal article', '/blog/tracking-food-symptoms-ibdpal'),
            ('Anti-inflammatory diet guide', '/guides/anti-inflammatory-diet-ibd'),
            ('Doctor visit prep', '/guides/crohns-doctor-visit-prep'),
            ('Complete nutrition article', '/blog/complete-ibd-nutrition-guide'),
        ),
    ),    "crohns-doctor-visit-prep": 
mk(
        "Prepared GI visits lead to better questions, faster decisions, and less anxiety. This guide helps Crohn's and colitis patients organize symptoms, medications, and goals before appointments. Education only, not medical advice.",
        [
            sec('Two weeks before the visit', 'Request records if you changed clinics. Gather imaging, colonoscopy reports, and lab printouts.', 'Start or update a symptom and food log. Note worst days, blood, nocturnal stools, and weight change. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'List questions as they arise in your phone notes. Prioritize top three for the visit. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Medication and allergy list', 'Bring exact drug names, doses, schedules, and last infusion or injection dates. Include supplements and over-the-counter items.', 'Note missed doses or side effects since the last visit. Pharmacy printouts help accuracy. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Ask about refills, prior authorizations, and travel letters at the end of the appointment. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
            sec('What to bring physically or digitally', 'Insurance cards, photo ID, stool diary exports, and a support person if allowed.', 'Wear comfortable clothing if abdominal exam is likely. Arrive with a full bladder only if ultrasound is scheduled. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Use the visit prep checklist on IBDPal to avoid forgetting key topics. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists.'),
            sec('During the appointment', 'Share your top concerns in the first five minutes. Ask what follow-up tests are needed and when results return.', 'Request written flare instructions if you do not have them. Clarify after-hours contacts. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Repeat back the plan in your own words to confirm understanding. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.'),
            sec('After the visit', 'Schedule labs, infusions, or scopes before leaving the building when possible.', 'Message portal questions if instructions were unclear. Do not guess on steroid tapers. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Update your emergency medication card and share changes with your pharmacy. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
        ],
        [
            'Email yourself a visit summary right after the appointment.',
            'Bring a printed medication list even if records are electronic.',
            'Ask how to reach the team after hours.',
            'Request portal access for caregivers if appropriate.',
            'Use /visit-prep checklist before every GI visit.',
        ],
        [
            fq('Should I bring stool samples to routine visits?', 'Only if requested. Call ahead about collection kits.'),
            fq('Can I record the visit?', 'Ask permission first. Some clinics allow audio for personal use.'),
            fq('What if I forget questions?', 'Send a portal message within 24 hours with remaining items.'),
        ],
        rel(
            ('Visit prep checklist', '/visit-prep'),
            ('First gastroenterology appointment', '/guides/first-gastroenterology-appointment-ibd'),
            ('Track symptoms and food', '/guides/track-ibd-symptoms-food'),
            ('Biologics overview', '/guides/biologics-crohns-colitis'),
            ('Foundation medication guide', '/guides/foundation-ibd-medication-guide'),
            ('Prior authorization guide', '/guides/ibd-prior-authorization-foundation'),
        ),
    ),    "biologics-crohns-colitis": 
mk(
        'Biologic therapies target specific immune pathways in moderate to severe IBD. Understanding how they work, how they are given, and what monitoring involves helps patients partner with their GI team. This guide is educational only and does not recommend starting or stopping any drug.',
        [
            sec('What biologics are in IBD', 'Common classes include anti-TNF agents, integrin inhibitors, IL-12/23 inhibitors, and JAK inhibitors for some patients. Your clinician matches class to disease type, history, and insurance.', 'Biologics are not interchangeable. Switching may require washout periods and new monitoring plans. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Biosimilars can be appropriate for some patients. Ask whether your pharmacy plans cover them. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Infusions, injections, and adherence', 'Dosing may be IV at infusion centers or subcutaneous at home. Learn storage, travel, and missed-dose rules.', 'Pre-medications, infusion reactions, and injection site care should be reviewed with nurses before the first dose. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Set calendar reminders and travel letters before trips. Do not skip doses without clinician guidance. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
            sec('Monitoring and infection prevention', 'TB screening, hepatitis panels, and periodic labs are standard before and during therapy.', 'Report fever, cough, skin changes, or neurologic symptoms promptly. Some infections need pausing therapy. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Vaccine updates, including influenza, COVID-19, and pneumococcal vaccines per schedule, matter on immunosuppression. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Side effects and expectations', 'Not everyone responds immediately. Drug levels and calprotectin may guide dose adjustments.', 'Discuss risks of lymphoma, skin cancer, and liver enzyme changes in context of your personal history. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Pregnancy planning and surgery timing need coordinated biologic plans. Involve your GI early. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Insurance, prior auth, and appeals', 'Biologics often require prior authorization and step therapy documentation. Start paperwork early when switching drugs.', 'Patient assistance programs exist for qualifying households. Clinic financial counselors can help. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Keep denial letters. Appeals with medical records and symptom logs are common. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
        ],
        [
            'Store injectables per label instructions.',
            'Carry a medication card listing your biologic and last dose.',
            'Report infection symptoms before your next scheduled dose.',
            'Ask about travel letters for airport syringes.',
            'Track symptoms before and after dose changes.',
        ],
        [
            fq('Do biologics cure IBD?', 'They control inflammation for many patients but are not cures. Maintenance plans vary.'),
            fq('Can I drink alcohol on biologics?', 'Discuss with your GI. Liver monitoring and personal risk matter.'),
            fq('What if I miss an infusion?', 'Call your team immediately for timing instructions. Do not double doses without advice.'),
        ],
        rel(
            ('Foundation medication guide', '/guides/foundation-ibd-medication-guide'),
            ('Prior authorization guide', '/guides/ibd-prior-authorization-foundation'),
            ('Vaccines and infection risk', '/guides/foundation-ibd-vaccines-infection'),
            ('Biologics and travel article', '/blog/biologics-flying-travel-ibd'),
            ('Step therapy and Safe Step Act', '/guides/step-therapy-safe-step-act-ibd'),
            ('Clinical trials guide', '/guides/foundation-ibd-clinical-trials'),
        ),
    ),    "ibd-travel-planning": 
mk(
        "Travel with Crohn's or colitis takes extra planning for medications, restrooms, food, and flare contingencies. Many patients travel widely with preparation and clinician support. This guide covers practical steps before domestic or international trips. Education only.",
        [
            sec('Before you book', 'Discuss destination vaccines, malaria prophylaxis, and food safety with your GI team. Timing biologic doses around travel reduces surprises.', 'Check insurance coverage abroad and consider travel medical policies for longer trips. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Research restroom access laws and apps for your destination. Airport security rules apply to liquids and syringes. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Packing medications and supplies', 'Carry meds in original labeled containers in hand luggage. Bring extra days in case of delays.', 'Obtain travel letters for injectables and coolers for biologics if needed. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Pack wipes, spare underwear, ostomy supplies, and oral rehydration packets in a carry-on flare kit. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
            sec('Food and water strategies', 'Bottled water and cooked foods reduce infection risk in some regions. Peel fresh fruit when unsure.', 'Research restaurant phrases or cards explaining dietary needs. Simple, cooked choices often feel safest during active symptoms. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Avoid risky street food if immunosuppressed. Balance adventure with clinician advice. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists.'),
            sec('Time zones and schedules', 'Shift medication times gradually for large zone changes. Ask your team for a written schedule.', 'Infusion centers abroad exist but need advance planning. Never assume walk-in availability. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Track symptoms during travel jet lag so you do not confuse fatigue with flares. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('If symptoms flare away from home', "Use your clinic's on-call line or telehealth when available. Know local urgent care options before departure.", 'Travel insurance with medical evacuation is worth considering for remote areas. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Document visits and labs to share with your home GI after return. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
        ],
        [
            'Photograph your prescription labels before leaving.',
            'Download restroom finder apps for your route.',
            'Carry a clinician letter for security screenings.',
            'Pack twice the ostomy supplies you expect to need.',
            'Review Foundation travel restroom guide before long trips.',
        ],
        [
            fq('Can I fly with injectable biologics?', 'Yes with proper documentation and storage. Ask your team for a travel letter.'),
            fq('Should I avoid developing countries on immunosuppression?', 'Not always, but vaccine and infection planning is essential. Personalize with your GI.'),
            fq('What if my medication is lost abroad?', 'Contact manufacturer patient support and local pharmacies early. Embassies may assist.'),
        ],
        rel(
            ('Foundation travel and restroom access', '/guides/foundation-ibd-travel-restroom-access'),
            ('Flare emergency supplies', '/guides/ibd-flare-emergency-supplies'),
            ('Biologics and travel article', '/blog/biologics-flying-travel-ibd'),
            ('Dining out with IBD', '/guides/dining-out-with-ibd'),
            ('Vaccines and infection', '/guides/foundation-ibd-vaccines-infection'),
            ('IBD hydration guide', '/guides/ibd-hydration-fluids'),
        ),
    ),    "ibd-workplace-school-rights": 
mk(
        'IBD can affect attendance, restroom needs, and energy at work or school. Laws and policies may provide accommodations when documentation is in place. This guide outlines common rights topics patients discuss with clinicians and administrators. Not legal advice.',
        [
            sec('Disclosure and documentation', 'You choose how much to share. Medical letters should state needed accommodations without unnecessary diagnosis detail.', 'In the U.S., ADA and Section 504 may apply depending on setting. Other countries have parallel frameworks. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'HR and disability offices often have forms your clinician completes. Start early each school year. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Common accommodations', 'Flexible breaks, remote work options, extra time on exams, restroom passes, and modified PE may be reasonable.', 'Infusion appointments and post-operative recovery may need protected leave. Know FMLA or local equivalents. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Ostomy supplies and refrigeration for biologics can be workplace discussions. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
            sec('Talking with employers and professors', 'Focus on functional needs: predictable restroom access, occasional telework, or deadline flexibility during flares.', 'Provide a point of contact for HR rather than debating symptoms with every coworker. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Professors appreciate advance notice before midterms when symptoms flare. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists.'),
            sec('Students and parents', 'School nurses can store emergency medications and flare kits. 504 plans travel between grades when updated.', 'Bullying about restroom use should be reported. Foundation youth resources support families. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'College disability services require separate registration from high school plans. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.'),
            sec('When to seek legal help', 'Denials of reasonable accommodation, termination after disclosure, or discrimination may need employment attorneys or advocacy groups.', 'Keep written records of requests and responses. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Foundation workplace guides provide starting language, not legal representation. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
        ],
        [
            'Renew accommodation letters annually.',
            'Know your clinic fax for HR forms.',
            'Register with college disability services before classes start.',
            'Keep a private symptom log for accommodation reviews.',
            'Review Foundation workplace rights guide for sample language.',
        ],
        [
            fq('Must I tell my boss I have IBD?', 'No. You may request accommodations with functional language and medical documentation.'),
            fq('Can I be fired for frequent bathroom breaks?', 'Retaliation for reasonable accommodations may be unlawful depending on jurisdiction. Document interactions.'),
            fq('Do accommodations guarantee perfect attendance?', 'No. They reduce barriers but medical leave may still be needed.'),
        ],
        rel(
            ('Foundation workplace and school rights', '/guides/foundation-workplace-school-rights-ibd'),
            ('Youth school Foundation resources', '/guides/youth-school-foundation-resources'),
            ('College with IBD article', '/blog/college-with-ibd'),
            ('Living with an ostomy', '/guides/living-with-ostomy-ibd'),
            ('Partner and caregiver guide', '/guides/partner-caregiver-ibd'),
            ('Newly diagnosed guide', '/guides/newly-diagnosed-crohns-colitis'),
        ),
    ),    "living-with-ostomy-ibd": 
mk(
        'Some people with IBD live with a temporary or permanent ostomy after surgery. Adjustment takes time, but many return to work, sports, and relationships with the right support and supplies. This guide covers practical education topics patients discuss with surgeons and WOC nurses. Not medical advice.',
        [
            sec('Types of ostomies in IBD', 'Ileostomy and colostomy are common depending on surgery type. Temporary loop ostomies may be reversed later.', 'Stoma location, appliance type, and output consistency affect daily routines. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Wound ostomy continence nurses teach pouch changes, skin care, and problem solving. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Daily appliance and skin care', 'Empty pouches when one-third full to reduce leaks. Measure stoma regularly as swelling decreases after surgery.', 'Barrier rings, paste, and proper fit prevent skin breakdown. Photograph irritated skin for telehealth visits. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Order supplies through durable medical equipment providers before running low. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
            sec('Diet, hydration, and blockages', 'High ostomy output increases dehydration risk. Salty snacks and electrolyte drinks may help when clinicians approve.', 'Chew thoroughly and hydrate to reduce blockage risk with ileostomies. Know warning signs: pain, no output, vomiting. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Introduce new foods slowly and log reactions. Pineapple, nuts, and corn affect people differently. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Clothing, activity, and travel', 'Ostomy wraps and supportive underwear improve confidence. Many swim with specialized covers.', 'Contact sports may need protection. Discuss weight limits and core exercises with your surgeon. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Travel with extra supplies in carry-on bags and know TSA guidance on liquids and scissors. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Emotional adjustment and support', 'Grief and body image changes are normal. Peer ostomy groups and counseling help.', 'Intimacy conversations with partners improve with education. Foundation intimacy guides address common fears. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Tell your GI if output changes suddenly; it may signal blockage or disease recurrence rather than appliance issues alone. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
        ],
        [
            'Save WOC nurse contact for urgent appliance problems.',
            'Carry a spare kit everywhere for the first year.',
            'Weigh weekly if output is high.',
            'Join an ostomy support group online or locally.',
            'Review Foundation surgery and ostomy resources.',
        ],
        [
            fq('Will everyone notice my pouch?', 'Modern appliances are discreet under clothing. Most people cannot tell.'),
            fq('Can I shower with the pouch on?', 'Yes. Many wear appliances in the shower and pat dry afterward.'),
            fq('Does an ostomy mean IBD is cured?', "Not always. Crohn's can recur; UC surgery may be curative for colon disease. Surveillance continues."),
        ],
        rel(
            ('Foundation surgery and ostomy', '/guides/foundation-ibd-surgery-ostomy'),
            ('Foundation intimacy guide', '/guides/foundation-ibd-intimacy-sexual-health'),
            ('IBD hydration guide', '/guides/ibd-hydration-fluids'),
            ('Travel planning', '/guides/ibd-travel-planning'),
            ('Support groups overview', '/guides/crohns-colitis-support-groups'),
            ('Workplace rights', '/guides/ibd-workplace-school-rights'),
        ),
    ),    "stress-anxiety-ibd": 
mk(
        'Stress and anxiety do not cause IBD, but they can worsen symptoms and quality of life. Coping skills, therapy, and medical care work together. This guide outlines mental health topics patients discuss with GI teams and counselors. Education only, not mental health treatment.',
        [
            sec('Mind-gut connection in IBD', 'The gut-brain axis links emotional state to motility, pain perception, and immune signaling.', 'Anxiety about bathrooms, accidents, and needles is common and treatable. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Treating mental health may improve daily function even when inflammation labs are improving. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Signs to seek professional help', 'Panic attacks, persistent low mood, trauma flashbacks, or avoidance of food and social life need licensed care.', 'GI psychologists specialize in chronic illness coping. Ask your clinic for referrals. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Crisis hotlines and emergency services handle suicidal thoughts. Do not rely on forums alone. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
            sec('Skills that help day to day', 'Breathing exercises, brief walks, scheduled worry time, and cognitive behavioral strategies reduce rumination.', 'Exposure planning for travel and restaurants can rebuild confidence with therapist support. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Sleep hygiene supports both mood and inflammation monitoring. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists.'),
            sec('Medication and therapy options', 'Antidepressants help some patients with pain and anxiety. Coordinate with GI to avoid interactions.', 'SSRIs and therapy combinations are common. Stigma should not block treatment. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Tell both mental health and GI teams about all prescriptions and supplements. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.'),
            sec('Partnering with your GI team', 'Share anxiety symptoms like nausea from fear of eating. They affect nutrition and adherence.', 'Ask whether symptoms are inflammatory versus functional when labs and scopes are stable. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Foundation emotional wellness resources complement clinic care. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
        ],
        [
            'Schedule bathroom breaks before stressful events.',
            'Try five-minute breathing apps daily, not only in crises.',
            'Ask your clinic about GI psychology referrals.',
            'Limit doom-scrolling in IBD forums before bed.',
            'Pair peer support with licensed therapy when needed.',
        ],
        [
            fq('Did stress cause my IBD?', 'IBD is not caused by stress alone. Stress can affect symptoms and coping.'),
            fq('Is anxiety normal with IBD?', 'Very common. Treatment helps and is not a sign of weakness.'),
            fq('Can therapy reduce flares?', 'It may improve coping and adherence. Medical flares still need GI treatment.'),
        ],
        rel(
            ('Foundation emotional wellness', '/guides/foundation-emotional-wellness-ibd'),
            ('Sleep during flares', '/guides/sleep-ibd-flares'),
            ('Bathroom urgency anxiety article', '/blog/bathroom-urgency-anxiety-ibd'),
            ('Partner and caregiver guide', '/guides/partner-caregiver-ibd'),
            ("Crohn's flare guide", '/guides/crohns-flare-what-to-do'),
            ('IBD helpline resources', '/guides/ibd-crohns-colitis-helpline'),
        ),
    ),    "sleep-ibd-flares": 
mk(
        'Sleep disruption is common during IBD flares because of nocturnal stools, pain, steroids, and anxiety. Poor sleep worsens fatigue and mood. This guide covers sleep hygiene topics patients discuss with their GI and primary care teams. Education only.',
        [
            sec('Why flares steal sleep', 'Nighttime bowel movements break sleep cycles. Urgency anxiety makes it hard to fall back asleep.', 'Prednisone and other steroids can cause insomnia. Ask about dosing time adjustments with your clinician. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Abdominal pain and fever compound fragmentation. Treating inflammation helps sleep long term. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Bedtime routines that help', 'Limit screens one hour before bed. Dim lights signal melatonin release.', 'Avoid large late meals if they trigger reflux or urgency. Sips of water are fine unless restricted. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Keep a bedside flare kit to reduce panic trips to the bathroom. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
            sec('Managing nocturnal symptoms', 'Log nocturnal stool count for your GI team. It influences treatment urgency.', 'Anti-diarrheal medications are sometimes used at night with clinician guidance. Do not self-start. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Discuss pain plans that balance relief with alertness the next day. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists.'),
            sec('Daytime habits', 'Morning light exposure and short walks improve circadian rhythm when energy allows.', 'Caffeine cutoff before noon helps if steroids already cause jitters. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Naps longer than 30 minutes may worsen night insomnia. Rest propped up if lying flat triggers urgency. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.'),
            sec('When to ask for more help', 'Persistent insomnia despite improving bowels may need sleep medicine referral.', 'Screen for sleep apnea if snoring and daytime sleepiness appear. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Mental health support helps when fear of accidents dominates nights. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
        ],
        [
            'Track nights with three or more bowel movements separately.',
            'Ask if evening steroid doses can shift earlier.',
            'Use dim night-lights to reduce fully waking.',
            'Keep phone out of bed to lower anxiety scrolling.',
            'Discuss melatonin with your clinician before trying.',
        ],
        [
            fq('Should I restrict fluids at night?', 'Only if your team advises for specific heart or kidney conditions. Dehydration worsens flares.'),
            fq('Are sleep aids safe with IBD meds?', 'Some interact. Always ask both GI and prescribing clinicians.'),
            fq('Will sleep improve when inflammation calms?', 'Often yes, though anxiety habits may linger and need therapy.'),
        ],
        rel(
            ('Stress and anxiety with IBD', '/guides/stress-anxiety-ibd'),
            ("Crohn's flare guide", '/guides/crohns-flare-what-to-do'),
            ('Foundation pain and fatigue', '/guides/foundation-ibd-pain-fatigue'),
            ('UC flare management', '/guides/ulcerative-colitis-flare-management'),
            ('Flare help hub', '/flare-help'),
            ('Track symptoms and food', '/guides/track-ibd-symptoms-food'),
        ),
    ),    "partner-caregiver-ibd": 
mk(
        'Partners and caregivers play important roles in IBD journeys without becoming substitute clinicians. Healthy support balances empathy, boundaries, and practical help. This guide offers education for loved ones and patients navigating relationships. Not couples therapy or medical advice.',
        [
            sec('What caregivers can do well', 'Listen without fixing every problem. Accompany appointments when invited and take notes.', 'Help stock flare kits, manage insurance calls, and watch for red-flag symptoms. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Learn medication names and after-hours contacts for emergencies. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Boundaries that protect relationships', 'Patients retain autonomy over body and treatment decisions. Caregivers should not police food without agreement.', 'Schedule non-IBD time together. Illness should not consume every conversation. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Caregiver burnout is real. Respite and peer support for partners matter. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Communication during flares', 'Use a simple scale for pain and fatigue instead of guessing.', 'Agree on signals for when to call the GI team versus rest at home. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Avoid blame language about flares. Inflammation is medical, not moral failure. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
            sec('Intimacy and body image', 'Ostomies, scars, and fatigue affect intimacy temporarily or long term. Open, patient conversations help.', 'Foundation intimacy guides provide sensitive education for couples. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Professional counseling supports couples when communication stalls. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.'),
            sec('Kids and family planning', 'Parents with IBD benefit from explaining age-appropriate facts to children.', 'Pregnancy planning requires GI and OB coordination. Caregivers join medication safety discussions. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Genetic risk is modest but real. Focus on support rather than fear. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
        ],
        [
            'Ask how your loved one wants help before acting.',
            'Attend one GI visit yearly if welcomed.',
            'Keep emergency numbers on the fridge.',
            'Find caregiver support groups separately.',
            'Read Foundation family resources together.',
        ],
        [
            fq('How can I help without hovering?', 'Ask directly: Do you want advice, company, or quiet? Respect the answer.'),
            fq('Should partners come to every infusion?', 'Only if the patient wants that. Some prefer independence.'),
            fq('Is caregiver stress normal?', 'Yes. Seek support for yourself too.'),
        ],
        rel(
            ('Foundation emotional wellness', '/guides/foundation-emotional-wellness-ibd'),
            ('Foundation intimacy guide', '/guides/foundation-ibd-intimacy-sexual-health'),
            ('Stress and anxiety guide', '/guides/stress-anxiety-ibd'),
            ('Pediatric IBD help', '/guides/pediatric-crohns-colitis-help'),
            ('Pregnancy Foundation resources', '/guides/pregnancy-ibd-foundation-resources'),
            ('Support groups overview', '/guides/crohns-colitis-support-groups'),
        ),
    ),    "crohns-food-triggers": 
mk(
        "Food triggers in Crohn's disease vary widely and may change with disease activity. Identifying personal patterns helps comfort but does not replace treating inflammation. This guide explains how patients and dietitians approach trigger discovery safely. Education only.",
        [
            sec('Triggers versus inflammation', 'Some foods irritate symptomatic bowel without raising calprotectin. Others coincide with active inflammation unrelated to diet.', 'Do not assume every symptom after eating proves a trigger. Viruses, stress, and medication gaps also matter. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Labs and scopes help separate inflammatory flares from irritant responses. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Structured food reintroduction', 'Elimination should be short and supervised. Long restrictive lists harm nutrition.', 'Reintroduce one food every three to seven days while logging stools, pain, and gas. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Portion size and cooking method change tolerance. Raw apple may fail while applesauce is fine. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
            sec('Common suspect foods', 'High-fat meals, lactose, caffeine, alcohol, sugar alcohols, and large fiber loads appear often in patient reports.', 'Spicy foods and artificial sweeteners bother some people. Cultural diets need individualized adaptation. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Nightshade and gluten elimination lack universal evidence. Test only with clinician oversight. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists.'),
            sec('Working with a dietitian', 'Registered dietitians prevent accidental malnutrition during elimination trials.', 'They align plans with strictures, short bowel, and biologic schedules. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Bring IBDPal or paper logs showing timing of symptoms after meals. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.'),
            sec('When to stop searching for triggers', 'If weight drops, fear of food grows, or social life shrinks, pause elimination and involve your GI team.', 'Treat active inflammation medically before chasing minor triggers. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Remission expands food options for many patients. Re-test old triggers periodically. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
        ],
        [
            'Log sleep and stress alongside meals.',
            'Test foods in remission when possible.',
            'Cook vegetables soft before blaming the vegetable.',
            'Ask about lactose hydrogen breath testing.',
            'Stop elimination diets that lack clinician supervision.',
        ],
        [
            fq('Are food allergy tests enough?', 'Not for IBD triggers. They detect IgE allergies, not most intolerance patterns.'),
            fq('Should I avoid gluten automatically?', 'Only if celiac is ruled in or out with your team and a supervised trial makes sense.'),
            fq('Can triggers change after surgery?', 'Yes. Anatomy changes absorption and tolerance.'),
        ],
        rel(
            ('Elimination diet: when to stop', '/guides/elimination-diet-when-to-stop-ibd'),
            ('Track symptoms and food', '/guides/track-ibd-symptoms-food'),
            ('What should I eat with IBD?', '/guides/what-should-i-eat-crohns-colitis'),
            ('Dairy and lactose article', '/blog/dairy-lactose-ibd'),
            ('Anti-inflammatory diet guide', '/guides/anti-inflammatory-diet-ibd'),
            ('FODMAP article', '/blog/fodmap-diet-crohns-colitis'),
        ),
    ),    "ibd-crohns-colitis-helpline": 
mk(
        "Crohn's and colitis helplines and nurse lines connect patients with education, emotional support, and navigation resources. They do not replace your personal GI team for medical orders. This guide explains when to use national helplines versus clinic contacts. Education only.",
        [
            sec('Foundation helpline and IBD Help Center', "The Crohn's and Colitis Foundation offers information specialists for resources, programs, and general education.", 'Hours and languages vary. Check current listings on Foundation websites before calling. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Helpline staff do not diagnose or prescribe. They point to vetted materials and local chapters. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Your clinic nurse line', 'IBD centers often provide flare triage numbers with faster access to your chart.', 'Use clinic lines for medication changes, infusion reactions, and worsening symptoms. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Save after-hours GI coverage instructions in your phone contacts. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
            sec('Crisis and mental health lines', 'Suicidal thoughts, self-harm urges, or domestic violence need emergency and crisis services, not general IBD helplines.', '988 and local emergency numbers apply in the United States. Know your country equivalents when traveling. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'GI teams appreciate knowing when mental health crises affect medication adherence. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists.'),
            sec('Insurance and prior auth navigation', 'Foundation and clinic financial counselors help with appeals, copay cards, and patient assistance.', 'Document denial letters and symptom logs when calling for navigation help. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Step therapy questions may need both insurer and prescriber involvement. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.'),
            sec('Preparing for a productive call', 'Have insurance card, medication list, and recent labs nearby.', 'Write your top three questions first. Note callback number if queues are long. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Follow up with your personal GI for anything medical beyond general education. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
        ],
        [
            'Save clinic and Foundation numbers separately in contacts.',
            'Call clinic lines first for urgent symptoms.',
            'Use 988 for mental health crises in the U.S.',
            'Keep denial letters handy for insurance calls.',
            'Log call dates and reference numbers.',
        ],
        [
            fq('Can helplines order tests?', 'No. Only your licensed care team orders diagnostics and prescriptions.'),
            fq('Are helplines free?', 'Foundation services are typically free; verify current policies.'),
            fq('Should I call for medication refills?', 'Use pharmacy and clinic portals for refills unless instructed otherwise.'),
        ],
        rel(
            ('Find a Foundation chapter', '/guides/find-ccf-chapter-support-group'),
            ('Prior authorization guide', '/guides/ibd-prior-authorization-foundation'),
            ('Foundation emotional wellness', '/guides/foundation-emotional-wellness-ibd'),
            ("Crohn's flare guide", '/guides/crohns-flare-what-to-do'),
            ('Foundation resources hub', '/crohns-colitis-foundation-resources'),
            ('Support groups overview', '/guides/crohns-colitis-support-groups'),
        ),
    ),    "first-gastroenterology-appointment-ibd": 
mk(
        'Your first gastroenterology appointment for suspected or new IBD can feel overwhelming. Preparation helps you use limited time well and reduces repeat visits for missing data. This guide walks through common first-visit topics. Education only, not medical advice.',
        [
            sec('Before the visit', 'Bring prior colonoscopy reports, imaging CDs or links, pathology, and lab printouts from other clinics.', 'List symptoms with start dates: blood, weight change, nocturnal stools, joint pain, rashes, and family history. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Note all medications including antibiotics, NSAIDs, supplements, and birth control. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('What may happen at the visit', 'History, abdominal exam, and rectal exam are common. You can request a chaperone.', 'The gastroenterologist may order stool studies, blood work, imaging, or schedule colonoscopy. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Ask what diagnoses are being considered and what would change the plan. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Questions worth asking', 'What red flags should trigger a call before the next test?', 'How long until results and who communicates them? Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Will you coordinate with my primary care doctor and dietitian? Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists.'),
            sec('Colonoscopy planning', 'Bowel prep choices depend on disease location and prior surgeries. Follow instructions exactly.', 'Arrange a driver and day off work. Ask about holding iron or certain meds beforehand. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Sedation options and anesthesia clearance may need extra appointments. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.'),
            sec('After the first visit', 'Schedule follow-up before leaving if possible. Portal activation prevents phone tag.', 'Start a symptom log immediately if you are not already tracking. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Seek second opinions for complex cases without guilt. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
        ],
        [
            'Arrive with a written timeline of symptoms.',
            'Bring a support person if allowed.',
            'Ask for colonoscopy prep in writing.',
            'Request after-hours contact before you leave.',
            'Use visit prep checklist at /visit-prep.',
        ],
        [
            fq('Will I be diagnosed at the first visit?', 'Sometimes suspicion is clear, but many diagnoses need endoscopy and pathology.'),
            fq('Should I stop eating before the first visit?', 'Unless told otherwise, eat normally unless fasting labs are scheduled.'),
            fq('Can I record the visit?', 'Ask the clinician first.'),
        ],
        rel(
            ('Visit prep checklist', '/visit-prep'),
            ('Newly diagnosed guide', '/guides/newly-diagnosed-crohns-colitis'),
            ('Doctor visit prep guide', '/guides/crohns-doctor-visit-prep'),
            ('Colonoscopy prep article', '/blog/colonoscopy-prep-ibd'),
            ('What is IBD? Foundation basics', '/guides/what-is-ibd-foundation'),
            ('Newly diagnosed hub', '/newly-diagnosed'),
        ),
    ),    "ibd-flare-emergency-supplies": 
mk(
        'A flare emergency kit reduces stress when symptoms spike away from home. Contents should match your personal disease pattern and clinician advice. This guide lists common supplies IBD patients pack for work, school, and travel. Education only.',
        [
            sec('Core kit for most patients', 'Include wipes, spare underwear, sealable bags, hand sanitizer, and a small towel.', 'Oral rehydration packets and a water bottle help when diarrhea worsens. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Keep a laminated card with GI after-hours number and medication allergies. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Medication and documentation', 'Carry a few days of prescribed rescue meds only if your clinician approves on-the-go storage.', 'Travel letters for injectables and a medication list with generic names support urgent care visits. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Insurance card copies speed registration. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Ostomy and post-surgical additions', 'Pack full appliance changes, barrier wipes, scissors, and disposal bags.', 'Skin barrier paste prevents leaks during long outings. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'High-output supplies include extra electrolyte packets. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
            sec('Work, school, and car kits', 'Duplicate kits in backpack, desk, and car reduce panic when symptoms hit unexpectedly.', 'Teachers and nurses can store labeled kits with permission forms. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Restroom access cards from advocacy groups help in public venues. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.'),
            sec('Maintaining and refreshing kits', 'Check expiration dates quarterly. Replace crushed snacks and leaked packets.', 'Update phone numbers after clinic changes. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Practice using supplies before a crisis so steps feel automatic. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
        ],
        [
            'Pack kits before remission ends; flares arrive unannounced.',
            'Use discrete pouches if privacy matters.',
            'Include a change of mask for clinic visits.',
            'Add a snack you tolerate for low blood sugar.',
            'Review kit contents with your GI nurse yearly.',
        ],
        [
            fq('Should I include opioids in my kit?', 'Only if prescribed and legally carried. Most flare kits focus on hygiene and hydration.'),
            fq('Can kids carry kits at school?', 'Yes with nurse agreements and 504 plans.'),
            fq('What about TSA and kits?', 'Liquids follow airport rules; document medical need when possible.'),
        ],
        rel(
            ("Crohn's flare guide", '/guides/crohns-flare-what-to-do'),
            ('Flare help hub', '/flare-help'),
            ('IBD hydration guide', '/guides/ibd-hydration-fluids'),
            ('Travel planning', '/guides/ibd-travel-planning'),
            ('Living with an ostomy', '/guides/living-with-ostomy-ibd'),
            ('Flare first 48 hours article', '/blog/flare-first-48-hours'),
        ),
    ),    "dining-out-with-ibd": 
mk(
        'Restaurant meals can be enjoyable with IBD when you plan ahead for restrooms, menu choices, and flare contingencies. Confidence grows with practice and clinician-aligned strategies. This guide shares common dining-out tips patients use. Education only.',
        [
            sec('Choosing restaurants wisely', 'Scout restroom locations with apps before seated meals. Chains with reliable access reduce anxiety.', 'Buffets and heavy spice kitchens may be harder during active symptoms. Simple grilled options are frequent fallbacks. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Call ahead about ingredients if you have severe allergies separate from IBD. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Ordering strategies', 'Ask for sauces on the side and vegetables cooked well done. Plain rice, fish, or chicken are common safe starters.', 'Share plates to keep portions moderate. Take leftovers home if large meals trigger urgency. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Avoid known personal triggers even when dining socially. Politeness does not require eating everything. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
            sec('Alcohol, caffeine, and dessert', 'Happy hour drinks may worsen diarrhea or interact with meds. Sparkling water with lime is a discreet alternative.', 'Caffeine after dinner can disrupt sleep already fragile during flares. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Rich desserts and sugar alcohols bother some patients. Fruit sorbet may be gentler. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists.'),
            sec('Timing and social pressure', 'Eat earlier if evening urgency disrupts sleep. Snack before events to avoid starving at late dinners.', 'Script simple phrases: I am keeping it mild tonight for my stomach. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Leave early without guilt if symptoms flare. Health beats politeness. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.'),
            sec('When to skip dining out', 'Active fevers, heavy bleeding, or dehydration are signs to rest at home and call your GI team.', 'Post-operative and stricture phases may need texture-modified meals at home. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Return to restaurants as recovery allows. Goals shift with disease activity. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
        ],
        [
            'Preview menus online before you go.',
            'Sit near restrooms when possible.',
            'Carry a discreet flare kit in your bag.',
            'Eat smaller portions and chew thoroughly.',
            'Log meals that correlate with next-day symptoms.',
        ],
        [
            fq('Should I avoid restaurants entirely with IBD?', 'Many patients dine out safely in remission or with careful choices.'),
            fq('Is salad always risky?', 'Raw high-fiber salads may bother active disease. Cooked vegetables are often easier.'),
            fq('How do I handle work dinners?', 'Eat selectively, limit alcohol, and plan restroom breaks in advance.'),
        ],
        rel(
            ('Travel planning', '/guides/ibd-travel-planning'),
            ("Crohn's food triggers", '/guides/crohns-food-triggers'),
            ('Foundation travel restroom access', '/guides/foundation-ibd-travel-restroom-access'),
            ('Stress and anxiety guide', '/guides/stress-anxiety-ibd'),
            ('What should I eat with IBD?', '/guides/what-should-i-eat-crohns-colitis'),
            ('Bathroom urgency anxiety article', '/blog/bathroom-urgency-anxiety-ibd'),
        ),
    ),    "camp-oasis-kids-ibd": 
fmk(
        "This page summarizes Camp Oasis, the Crohn's and Colitis Foundation camp program for children and teens with IBD, and links to official Foundation resources.",
        [
            sec('What Camp Oasis offers', 'Camp Oasis provides a medically supervised summer camp experience where youth with IBD meet peers who understand infusions, diets, and bathroom needs.', 'Activities include sports, arts, and outdoor programs adapted for varying energy levels. Medical volunteers oversee health needs on site. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Many families report improved confidence and reduced isolation after camp. It is not a substitute for ongoing pediatric GI care. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Medical supervision and safety', 'Camp medical teams include physicians and nurses familiar with IBD therapies. Parents complete detailed health forms before attendance.', 'Medication administration, infusion schedules, and flare protocols follow camp policies coordinated with home GI teams. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Ask the Foundation about current eligibility, session dates, and scholarship options each year. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
            sec('Preparing your child', 'Practice self-advocacy skills: asking for restrooms, describing symptoms, and carrying supplies.', 'Pack labeled medications, comfort items, and contact numbers. Review dietary accommodations with camp staff early. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Discuss homesickness plans and how counselors communicate with parents during sessions. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Parents and siblings', 'Parent information sessions explain supervision models and emergency procedures.', 'Siblings without IBD may have separate family programs depending on region. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Use camp as respite care thoughtfully while ensuring home flare plans remain active. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('After camp and year-round connection', 'Many campers join teen groups and chapter events after summer ends.', 'Bring camp stories to pediatric GI visits if symptoms or adherence changed. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Foundation youth resources extend beyond one week of camp. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
        ],
        [
            'Apply early; slots and scholarships fill quickly.',
            "Share your child's flare plan with camp medical staff.",
            'Label all medications and supplies clearly.',
            'Practice overnight stays before a full camp session.',
            'Explore Foundation teen groups for year-round peers.',
        ],
        [
            fq('Is Camp Oasis only in the United States?', 'Camp locations and policies are listed on Foundation sites. Verify current international participation rules.'),
            fq('Can my child attend on biologics?', 'Many campers are on advanced therapies. Medical forms document plans.'),
            fq('Does the Foundation endorse IBDPal?', 'No. Selected content is used under license; the Foundation does not endorse IBDPal.'),
        ],
        rel(
            ('Pediatric IBD help', '/guides/pediatric-crohns-colitis-help'),
            ('Youth school Foundation resources', '/guides/youth-school-foundation-resources'),
            ('Foundation resources hub', '/crohns-colitis-foundation-resources'),
            ('Support groups overview', '/guides/crohns-colitis-support-groups'),
            ('Camp Oasis on Foundation site', 'https://www.crohnscolitisfoundation.org/camp-oasis'),
            ('Newly diagnosed guide', '/guides/newly-diagnosed-crohns-colitis'),
        ),
    ),    "ibd-prior-authorization-foundation": 
fmk(
        "This page explains prior authorization for IBD medications using Crohn's and Colitis Foundation patient navigation concepts and links to official appeals resources.",
        [
            sec('What prior authorization means', 'Insurers often require approval before covering expensive IBD drugs. Prior auth documents medical necessity with charts, labs, and prior therapies tried.', 'Delays can interrupt infusions or injections. Start paperwork early when switching biologics. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Foundation education helps patients understand the process without offering legal advice. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Information to gather', 'Collect diagnosis codes, colonoscopy reports, calprotectin or CRP trends, and medication history including failures or intolerances.', 'Ask your clinic which staff handles prior auth. Sign releases so they can speak with insurers. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Keep fax numbers and reference IDs for every call. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
            sec('Step therapy and appeals', 'Step therapy rules may require trying specific drugs first. Safe Step Act reforms vary by state and plan.', 'Denials are common. Appeals with physician letters and symptom logs often succeed on second review. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Foundation appeal letter templates provide starting language your doctor personalizes. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists.'),
            sec('Patient assistance and copay programs', 'Manufacturer copay cards and foundation assistance funds help qualifying patients during auth delays.', 'Financial counselors at infusion centers know program eligibility. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Document household income and insurance type accurately on applications. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.'),
            sec('Staying on therapy during delays', 'Never stop biologics without clinician guidance while waiting on auth.', 'Clinics may provide samples or bridge doses when available. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Escalate to plan medical directors with your gastroenterologist if delays risk harm. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
        ],
        [
            'Start prior auth before your last dose runs out.',
            'Save every denial letter.',
            'Ask insurers for case manager names.',
            'Use Foundation appeal templates with your doctor.',
            'Log symptoms during auth delays for appeals.',
        ],
        [
            fq('How long does prior auth take?', 'Days to weeks depending on plan and drug. Urgent requests may expedite.'),
            fq('Can I pay cash to skip auth?', 'Sometimes, but costs are high. Discuss with your clinic.'),
            fq('Who writes appeal letters?', 'Your prescriber, often with templates from Foundation or clinic legal teams.'),
        ],
        rel(
            ('Foundation appeal letters', '/guides/foundation-ibd-appeal-letters'),
            ('Step therapy and Safe Step Act', '/guides/step-therapy-safe-step-act-ibd'),
            ('Foundation medication guide', '/guides/foundation-ibd-medication-guide'),
            ('Biologics overview', '/guides/biologics-crohns-colitis'),
            ('Foundation resources hub', '/crohns-colitis-foundation-resources'),
            ('Doctor visit prep', '/guides/crohns-doctor-visit-prep'),
        ),
    ),    "foundation-diet-nutrition-ibd": 
fmk(
        "This page bridges Crohn's and Colitis Foundation diet and nutrition education with IBDPal guides for meal planning, deficiencies, and clinician collaboration.",
        [
            sec('Foundation nutrition education overview', 'Foundation materials cover general patterns for remission and flares, micronutrient needs, and when to involve registered dietitians.', 'Read the original Foundation diet pages for full detail. IBDPal summarizes navigation paths, not every recipe. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Nutrition supports medical care but does not replace anti-inflammatory treatment when disease is active. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Linking Foundation content to daily meals', 'Pair Foundation handouts with IBDPal food logs to see personal tolerance.', 'Introduce Foundation meal ideas one at a time during stable periods. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Pediatric and adult needs differ. Use age-appropriate Foundation resources. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
            sec('Micronutrients Foundation highlights', 'Iron, vitamin D, calcium, B12, and zinc appear frequently in Foundation nutrition education due to malabsorption and bleeding.', 'Ask your GI team which Foundation screening recommendations apply to your labs. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Supplement only deficiencies documented with testing unless directed otherwise. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists.'),
            sec('Special diets in Foundation materials', 'Foundation content discusses low-residue patterns, enteral nutrition, and cautions about unproven extreme diets.', 'Bring questions about FODMAP or anti-inflammatory approaches to your IBD dietitian. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Avoid starting multi-food eliminations without supervision. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.'),
            sec('Using IBDPal alongside Foundation guides', 'Track symptoms when trying Foundation meal suggestions. Data beats guessing.', 'Share exports at visits with gastroenterology and nutrition teams. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Return to Foundation sources when policies or research updates publish. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
        ],
        [
            'Bookmark Foundation diet pages as primary sources.',
            'Pair reading with clinician-approved labs.',
            'Log meals when testing Foundation recipes.',
            'Ask for dietitian referral if weight changes.',
            'Review IBDPal nutrition guides for deeper topics.',
        ],
        [
            fq('Does Foundation recommend one IBD diet?', 'No. Foundation education emphasizes personalization with your care team.'),
            fq('Can IBDPal replace a dietitian?', 'No. Apps support logging; dietitians provide medical nutrition therapy.'),
            fq('Are Foundation recipes safe in flares?', 'Tolerance varies. Follow your flare plan from your GI team.'),
        ],
        rel(
            ('What should I eat with IBD?', '/guides/what-should-i-eat-crohns-colitis'),
            ('Iron deficiency nutrition', '/guides/iron-deficiency-nutrition-ibd'),
            ('Foundation site: diet and nutrition', 'https://www.crohnscolitisfoundation.org/diet-and-nutrition'),
            ('Anti-inflammatory diet guide', '/guides/anti-inflammatory-diet-ibd'),
            ('Protein and healing', '/guides/protein-healing-ibd-flare'),
            ('Complete nutrition article', '/blog/complete-ibd-nutrition-guide'),
        ),
    ),    "anti-inflammatory-diet-ibd": 
mk(
        'Anti-inflammatory eating patterns emphasize whole foods, healthy fats, and limited ultra-processed items. Evidence in IBD is evolving and individual. This guide explains how patients discuss anti-inflammatory diets with their GI and dietitian teams. Education only, not a prescribed meal plan.',
        [
            sec('What anti-inflammatory means in IBD', 'Diets rich in vegetables, fruits, olive oil, nuts, and fatty fish are studied for general health and some IBD symptoms.', 'Anti-inflammatory labels on blogs do not guarantee they reduce bowel inflammation on scopes. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Medical treatment remains primary when calprotectin or CRP are elevated. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Foods often highlighted', 'Oily fish, turmeric in cooking, colorful produce, and whole grains when tolerated are common examples in patient education.', 'Ultra-processed snacks, excess added sugar, and trans fats are frequent reduction targets. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Personal tolerance still rules during active symptoms. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
            sec('Cautions and limitations', 'High-fiber anti-inflammatory salads may worsen active colitis. Cooked or peeled produce may be better short term.', 'Nightshade elimination lacks strong IBD-specific evidence for everyone. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Children need adequate calories; do not impose adult wellness trends without pediatric GI input. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists.'),
            sec('Combining diet with medical care', 'Track symptoms and labs when changing patterns. Improvement in stool without lab change may mean irritant relief only.', 'Ask whether diet trials should wait until inflammation is controlled. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Registered dietitians help adapt Mediterranean-style patterns to strictures and ostomies. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.'),
            sec('Sustainable habits', 'Small swaps beat extreme overhauls. Add one vegetable daily before eliminating entire food groups.', 'Social meals matter for mental health. Flexibility prevents burnout. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Revisit goals with your team yearly as disease activity shifts. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
        ],
        [
            'Cook vegetables soft during flares before raw salads.',
            'Prioritize protein even on anti-inflammatory plans.',
            'Log labs alongside diet experiments.',
            'Avoid juice cleanses marketed as anti-inflammatory.',
            'Ask your dietitian for culturally familiar swaps.',
        ],
        [
            fq('Will this diet cure IBD?', 'No. It may support overall health but does not replace IBD medications when needed.'),
            fq('Is keto anti-inflammatory?', 'Keto is not standard IBD care and may harm gut microbiome diversity for some patients.'),
            fq('Should I take turmeric supplements?', 'Discuss doses and interactions with your GI before starting supplements.'),
        ],
        rel(
            ('Autoimmune nutrition basics', '/guides/autoimmune-nutrition-basics'),
            ('What should I eat with IBD?', '/guides/what-should-i-eat-crohns-colitis'),
            ('Anti-inflammatory diet article', '/blog/anti-inflammatory-diet-ibd'),
            ('Foundation diet and nutrition', '/guides/foundation-diet-nutrition-ibd'),
            ('Track symptoms and food', '/guides/track-ibd-symptoms-food'),
            ('Olive oil and omega-3 topics', '/blog/complete-ibd-nutrition-guide'),
        ),
    ),    "iron-deficiency-nutrition-ibd": 
mk(
        'Iron deficiency and anemia are common in IBD because of bleeding, malabsorption, and inflammation blocking iron use. Nutrition and supplements work together under clinician guidance. This guide covers education topics patients review with their GI team. Not medical advice.',
        [
            sec('Why iron matters in IBD', 'Low iron reduces energy, exercise tolerance, and concentration. Anemia may persist even when bowel symptoms improve.', 'Chronic inflammation raises hepcidin, trapping iron despite adequate intake. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Repeat labs track response to therapy, not single snapshots. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Dietary iron sources', 'Heme iron from lean red meat, poultry, and fish is absorbed better than plant iron for many people.', 'Pair plant iron with vitamin C rich foods like citrus or bell peppers. Separate calcium supplements from iron doses when possible. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'During flares, tender proteins and fortified cereals may be easier than steak. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
            sec('Oral versus IV iron', 'Oral iron may worsen constipation or nausea. Take as directed with your team.', 'IV iron is common when oral forms fail, losses are high, or inflammation blocks absorption. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Do not double doses without labs. Excess iron harms organs. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists.'),
            sec('Monitoring and side effects', 'Check hemoglobin, ferritin, and sometimes CRP together. Ferritin may look normal during inflammation.', 'Black stools from iron supplements differ from GI bleeding. Ask when unsure. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Report breathing changes or chest pain urgently; they are not typical iron side effects. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.'),
            sec('Working with your care team', 'Treat ongoing bleeding sources while repleting iron.', 'Ask dietitians for high-iron recipes that respect texture needs. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Log energy and exercise tolerance as iron stores recover. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
        ],
        [
            'Request iron studies at routine GI visits.',
            'Take vitamin C with plant iron sources.',
            'Separate iron and calcium doses by a few hours.',
            'Report black tarry stools not explained by supplements.',
            'Read anemia article for warning signs.',
        ],
        [
            fq('Can I fix anemia with diet alone?', 'Sometimes mild cases improve, but many IBD patients need supplements or IV iron.'),
            fq('Does spinach alone solve iron deficiency?', 'Plant iron helps but absorption is lower. Medical assessment still matters.'),
            fq('When is bleeding an emergency?', 'Heavy bleeding, dizziness, or fainting need urgent evaluation.'),
        ],
        rel(
            ('Anemia article', '/blog/anemia-iron-deficiency-ibd'),
            ('UC diet foods', '/guides/ulcerative-colitis-diet-foods'),
            ('Blood in stool article', '/blog/blood-in-stool-ibd-when-to-worry'),
            ('What should I eat with IBD?', '/guides/what-should-i-eat-crohns-colitis'),
            ('Foundation diet and nutrition', '/guides/foundation-diet-nutrition-ibd'),
            ('Doctor visit prep', '/guides/crohns-doctor-visit-prep'),
        ),
    ),    "vitamin-d-bone-nutrition-ibd": 
mk(
        'Vitamin D, calcium, and bone health deserve attention in IBD because of malabsorption, steroid use, inflammation, and sometimes limited sun exposure. This guide summarizes nutrition topics patients discuss with gastroenterology and bone health teams. Education only.',
        [
            sec("Bone risk in Crohn's and colitis", 'Osteopenia and osteoporosis occur at younger ages than in the general population. Disease activity, smoking, and steroids increase risk.', 'DEXA scans may be recommended based on age, steroid history, and fracture risk. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Treat inflammation and nutrition together rather than focusing only on supplements. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Vitamin D basics', 'Vitamin D supports calcium absorption and immune regulation. Low levels are common in IBD clinics.', 'Dosing should follow labs. High doses without monitoring cause toxicity. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Sun exposure helps some patients but is not enough alone when deficiency is severe. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
            sec('Calcium and dietary patterns', 'Dairy, fortified plant milks, tofu set with calcium, and leafy greens contribute calcium when tolerated.', 'Lactose intolerance may require lactase or alternate sources. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Spread calcium intake across meals if supplements are needed. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists.'),
            sec('Steroids and bone protection', 'Prolonged prednisone accelerates bone loss. Clinicians may recommend calcium, vitamin D, and sometimes bisphosphonates.', 'Weight-bearing exercise when safe supports bone density. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Never stop steroids suddenly without medical guidance. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.'),
            sec('Labs and follow-up', 'Ask about 25-hydroxy vitamin D, calcium, phosphorus, and PTH when bone health is a concern.', 'Repeat DEXA per clinic protocol after starting therapy. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Smoking cessation dramatically improves bone and IBD outcomes. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
        ],
        [
            'Ask when your next DEXA scan is due.',
            'Take vitamin D with a meal containing fat.',
            'Choose calcium sources you tolerate in flares.',
            'Discuss steroid bone protection at every prednisone course.',
            'Log falls or fractures for your GI team.',
        ],
        [
            fq('Can I take huge vitamin D doses from online forums?', 'No. Toxicity is real. Dose per your clinician and labs.'),
            fq('Is dairy required for strong bones?', 'No. Fortified alternatives and supplements can work if planned.'),
            fq('Do biologics help bones?', 'Controlling inflammation may help indirectly. Bone-specific therapy still matters for some.'),
        ],
        rel(
            ('Calcium article', '/blog/calcium-ibd'),
            ('Foundation diet and nutrition', '/guides/foundation-diet-nutrition-ibd'),
            ('What should I eat with IBD?', '/guides/what-should-i-eat-crohns-colitis'),
            ('Iron deficiency guide', '/guides/iron-deficiency-nutrition-ibd'),
            ('Complete nutrition article', '/blog/complete-ibd-nutrition-guide'),
            ('Doctor visit prep', '/guides/crohns-doctor-visit-prep'),
        ),
    ),    "protein-healing-ibd-flare": 
mk(
        'Adequate protein supports tissue repair during and after IBD flares, especially when appetite is low or losses are high. This guide explains how patients meet protein needs with their GI and dietitian teams. Education only, not a meal prescription.',
        [
            sec('Why protein needs rise in flares', 'Inflammation, fever, and diarrhea increase protein breakdown. Surgery and steroid use add further demand.', 'Under-eating protein slows healing and muscle recovery. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Children and teens need extra attention to growth during active disease. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('High-quality protein sources', 'Eggs, fish, poultry, Greek yogurt, tofu, and smooth nut butters are frequent choices when tender textures are needed.', 'Protein shakes or enteral supplements may help when solids are hard. Choose products your dietitian approves. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Spread protein across meals instead of one large serving. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('When appetite is poor', 'Eat protein first at meals when fullness comes quickly.', 'Small snacks every few hours beat forcing large plates. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Anti-nausea strategies from your team may improve intake. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists.'),
            sec('Renal and special considerations', 'Kidney disease changes protein targets. Share all diagnoses with your dietitian.', 'Short bowel and ostomy patients need individualized electrolyte and protein plans. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'High-protein fad diets are not automatic IBD care. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.'),
            sec('Tracking progress', 'Monitor weight weekly during flares. Unintended loss triggers clinic outreach.', 'Handgrip strength and energy are informal signs of recovery. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Repeat albumin and prealbumin only as your clinician orders; trends matter. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
        ],
        [
            'Add an egg or yogurt to breakfast daily.',
            'Keep ready-to-drink supplements for bad appetite days.',
            'Log weight weekly during flares.',
            'Ask dietitian for gram targets personalized to you.',
            'Pair protein with gentle starches if fiber is limited.',
        ],
        [
            fq('Are protein powders safe in IBD?', 'Many are, but choose low-sugar options and confirm with your team if lactose or additives bother you.'),
            fq('How much protein do I need?', 'Depends on weight, age, and activity. Dietitians calculate targets.'),
            fq('Does extra protein reduce inflammation?', 'It supports healing but does not replace medical anti-inflammatory treatment.'),
        ],
        rel(
            ("Foods during a Crohn's flare", '/guides/foods-to-eat-crohns-flare'),
            ('Chicken protein article', '/blog/chicken-protein-ibd'),
            ('What should I eat with IBD?', '/guides/what-should-i-eat-crohns-colitis'),
            ('Iron deficiency guide', '/guides/iron-deficiency-nutrition-ibd'),
            ('High-protein meal plan article', '/blog/protein-meal-plan-ibd-remission'),
            ('Track symptoms and food', '/guides/track-ibd-symptoms-food'),
        ),
    ),    "elimination-diet-when-to-stop-ibd": 
mk(
        'Elimination diets remove foods to test tolerance, but long unsupervised restriction harms nutrition and mental health in IBD. Knowing when to stop is as important as when to start. This guide outlines warning signs patients discuss with clinicians. Education only.',
        [
            sec('Purpose of short elimination trials', 'Supervised trials may clarify lactose, FODMAP, or other irritant patterns when inflammation is controlled.', 'Trials should have start dates, end dates, and reintroduction schedules. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Elimination cannot diagnose IBD itself; endoscopy and labs do. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Red flags to stop immediately', 'Unintended weight loss, fainting, menstrual loss, or child growth faltering need urgent clinician review.', 'Fear of eating, social isolation, or obsessive logging suggest psychological harm. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Worsening inflammation on labs while restricting foods means medical treatment, not more elimination. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Nutrient gaps to watch', 'Cutting dairy, gluten, and multiple food groups simultaneously risks calcium, iron, and B vitamin deficits.', 'Supplements do not replace diverse food when restrictions are broad. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Dietitians monitor labs during trials. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists.'),
            sec('Healthy reintroduction', 'Add one food group every few days with logs. Celebrate expanded variety.', 'Some foods fail once but work months later after healing. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Texture changes, such as cooked versus raw, alter results. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.'),
            sec('Partnering with your GI team', 'Share social media diet lists for clinician review before starting.', 'Ask whether calprotectin should be normal before trials. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Mental health support helps when food anxiety persists after reintroduction. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
        ],
        [
            'Set a calendar end date before you start eliminating.',
            'Involve a dietitian for any multi-food removal.',
            'Weigh weekly during elimination.',
            'Stop if friends notice you avoiding all social meals.',
            'Treat flares medically before blaming foods.',
        ],
        [
            fq('How long should elimination last?', 'Often two to six weeks for specific protocols, but only per your clinician or dietitian plan.'),
            fq('Is carnivore diet safe for IBD?', 'Extreme diets lack evidence and risk nutrient gaps. Discuss risks with your GI team.'),
            fq('Can elimination cure inflammation?', 'No. It may reduce irritant symptoms while inflammation needs medical care.'),
        ],
        rel(
            ("Crohn's food triggers", '/guides/crohns-food-triggers'),
            ('Gluten-free guide', '/guides/gluten-free-autoimmune-when'),
            ('Autoimmune nutrition basics', '/guides/autoimmune-nutrition-basics'),
            ('Track symptoms and food', '/guides/track-ibd-symptoms-food'),
            ('Autoimmune diet myths article', '/blog/autoimmune-diet-myths'),
            ('What should I eat with IBD?', '/guides/what-should-i-eat-crohns-colitis'),
        ),
    ),    "autoimmune-nutrition-basics": 
mk(
        'IBD is autoimmune-related, and nutrition affects energy, bone health, and symptom comfort, but no universal autoimmune diet exists. This guide separates evidence-based habits from myths patients review with clinicians. Education only.',
        [
            sec('Nutrition role versus immune treatment', 'Medications that control inflammation remain cornerstone care. Food supports recovery and deficiencies.', 'Autoimmune labels on wellness products are marketing, not diagnoses. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Labs and scopes guide whether symptoms are inflammatory. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Patterns with modest evidence', 'Mediterranean-style patterns, adequate omega-3 intake, and limiting ultra-processed foods align with general health guidance.', 'Vitamin D repletion when deficient is commonly recommended in IBD clinics. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', "Smoking cessation is one of the strongest lifestyle interventions for Crohn's disease. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends."),
            sec('Myths to question', 'Carnivore, long-term juice cleanses, and unproven supplement stacks lack IBD-specific safety data.', 'Food allergy panels without symptoms do not guide IBD nutrition. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Social media cures rarely disclose medication use or surgical history. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
            sec('Personalization and culture', 'Respect cultural staples by modifying texture and spice rather than eliminating entire cuisines without cause.', 'Pediatric growth trumps adult weight loss trends. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Dietitians translate autoimmune education into practical family meals. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.'),
            sec('When to escalate care', 'Rapid weight loss, persistent bleeding, or night stools need GI outreach, not more supplements.', 'Mental health screening belongs in holistic autoimmune care. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Clinical trials study nutrition therapies; ask your team about eligible studies. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
        ],
        [
            'Question diets that forbid all grains or all plants.',
            'Ask for labs before buying supplement stacks.',
            'Keep smoking cessation on your goal list if applicable.',
            'Log symptoms when trying any new protocol.',
            'Read autoimmune diet myths article on IBDPal.',
        ],
        [
            fq('Does gluten-free help all autoimmune disease?', 'Only patients with celiac or documented gluten sensitivity benefit specifically.'),
            fq('Are autoimmune protocols safe?', 'Some are restrictive. Medical supervision prevents harm.'),
            fq('Can probiotics treat IBD?', 'Evidence is strain-specific. Ask your gastroenterologist.'),
        ],
        rel(
            ('Anti-inflammatory diet guide', '/guides/anti-inflammatory-diet-ibd'),
            ('Gluten-free guide', '/guides/gluten-free-autoimmune-when'),
            ('Autoimmune diet myths article', '/blog/autoimmune-diet-myths'),
            ('Foundation complementary medicine', '/guides/foundation-complementary-medicine-ibd'),
            ('What should I eat with IBD?', '/guides/what-should-i-eat-crohns-colitis'),
            ('Elimination diet guide', '/guides/elimination-diet-when-to-stop-ibd'),
        ),
    ),    "gluten-free-autoimmune-when": 
mk(
        'Gluten-free diets are essential for celiac disease but are not required for every person with IBD or autoimmune conditions. This guide explains when testing and supervised trials make sense. Education only, not medical advice.',
        [
            sec('Celiac versus IBD overlap', 'Celiac disease is more common in IBD than in the general population. Screening may be recommended at diagnosis or with anemia.', 'Celiac requires strict lifelong gluten avoidance and follow-up biopsies or serology. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Non-celiac gluten sensitivity is debated and diagnosed by exclusion with clinician oversight. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('When to test before going gluten free', 'Serology and endoscopy need active gluten intake for accuracy. Do not stop gluten before testing unless your team instructs.', 'Genetic tests alone do not diagnose celiac. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'IBD inflammation can affect villi; interpret results with gastroenterology. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
            sec('Trial gluten-free diets safely', 'Short supervised trials may help if celiac is ruled out and symptoms persist in remission.', 'Replace wheat with fortified gluten-free grains to avoid fiber and iron gaps. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Document stool, pain, and energy changes during trials. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists.'),
            sec('Risks of unnecessary restriction', 'Gluten-free packaged foods may be low in fiber and high in sugar.', 'Social and cost burdens affect quality of life. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Children should not be gluten free without clear medical indication. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.'),
            sec('Talking with your GI team', 'Bring questions about chapati, bread, and cultural staples to dietitian visits.', 'Ask whether symptoms correlate with gluten or with FODMAPs in wheat. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Repeat celiac labs if exposure was uncertain during prior testing. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
        ],
        [
            'Get celiac blood tests before eliminating gluten.',
            'Choose fortified gluten-free grains when needed.',
            'Log symptoms during any trial.',
            'Separate celiac care from IBD care teams if both apply.',
            'Read celiac screening article on IBDPal.',
        ],
        [
            fq('Does ulcerative colitis require gluten free?', 'Not routinely. Test for celiac when clinically indicated.'),
            fq('Will gluten free put IBD in remission?', 'Only if celiac or clear non-celiac sensitivity is documented.'),
            fq('Are gluten sensitivity tests from labs reliable?', 'Many non-standard panels lack validation. Use clinician-directed testing.'),
        ],
        rel(
            ('Celiac screening article', '/blog/celiac-ibd-screening'),
            ('Autoimmune nutrition basics', '/guides/autoimmune-nutrition-basics'),
            ('Elimination diet guide', '/guides/elimination-diet-when-to-stop-ibd'),
            ('Chapati and roti article', '/blog/chapati-roti-ibd'),
            ('What should I eat with IBD?', '/guides/what-should-i-eat-crohns-colitis'),
            ('Track symptoms and food', '/guides/track-ibd-symptoms-food'),
        ),
    ),    "what-is-ibd-foundation": 
fmk(
        "This page summarizes Crohn's and Colitis Foundation patient education on what inflammatory bowel disease is and how to use those materials with your clinician.",
        [
            sec('IBD in plain language', "Inflammatory bowel disease includes Crohn's disease, ulcerative colitis, and sometimes IBD-unclassified. Chronic inflammation damages the digestive tract over time without treatment.", 'Symptoms may include diarrhea, rectal bleeding, abdominal pain, weight loss, and fatigue. Some people have joint, skin, or eye involvement. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'IBD differs from irritable bowel syndrome, which does not cause the same inflammatory damage on scopes. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('How diagnosis is made', 'Gastroenterologists combine history, exam, stool tests, blood work, imaging, and endoscopy with biopsy.', 'Disease location and behavior guide therapy. Ask your team to explain your classification in writing. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Online education prepares questions; it does not replace testing. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
            sec('Using Foundation pages with IBDPal', 'Start with the Foundation What is IBD page as the authoritative source, then explore disease-specific pages.', 'Log symptoms in IBDPal between visits so patterns are visible. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Bring unfamiliar terms to clinic for clarification. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists.'),
            sec('Treatment overview at patient level', 'Goals include healing inflammation, preventing complications, and restoring quality of life.', 'Medications range from anti-inflammatories to biologics. Surgery helps some patients. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Nutrition, mental health, and vaccines are part of whole-person care. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.'),
            sec('Boundaries of patient education', 'Foundation materials do not prescribe individual treatment. Your IBD clinician personalizes plans.', 'The Foundation does not endorse IBDPal. Selected content is used under license. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Call your clinic for red-flag symptoms rather than relying on websites alone. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
        ],
        [
            'Bookmark Foundation disease basics pages.',
            "Ask whether your disease is Crohn's, UC, or IBD-U.",
            'Note night stools and blood for your team.',
            'Explore newly diagnosed Foundation guide next.',
            'Save clinic after-hours numbers.',
        ],
        [
            fq('Is IBD contagious?', 'No. It is not spread person to person.'),
            fq('Can this page diagnose me?', 'No. Only your clinician diagnoses after appropriate evaluation.'),
            fq('Does Foundation endorse IBDPal?', 'No. Content is licensed; endorsement does not occur.'),
        ],
        rel(
            ('Foundation: What is IBD', 'https://www.crohnscolitisfoundation.org/what-is-ibd'),
            ("What is Crohn's Foundation guide", '/guides/what-is-crohns-disease-foundation'),
            ('What is UC Foundation guide', '/guides/what-is-ulcerative-colitis-foundation'),
            ('Newly diagnosed Foundation first week', '/guides/newly-diagnosed-foundation-first-week'),
            ('Foundation resources hub', '/crohns-colitis-foundation-resources'),
            ('Newly diagnosed hub', '/newly-diagnosed'),
        ),
    ),    "what-is-crohns-disease-foundation": 
fmk(
        "This page bridges Crohn's and Colitis Foundation education on Crohn's disease with IBDPal tools for logging and visit preparation.",
        [
            sec("What Crohn's can affect", "Crohn's may involve any part of the gastrointestinal tract from mouth to anus, often in patches. Deep inflammation can lead to strictures or fistulas.", 'Common symptoms include diarrhea, pain, fatigue, weight change, and perianal disease. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Extraintestinal manifestations may affect joints, skin, and eyes. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Disease patterns clinicians track', 'Location such as ileal, colonic, or ileocolonic disease shapes monitoring.', 'Behavior includes inflammatory, stricturing, and penetrating phenotypes. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Ask your GI team to explain your latest imaging and endoscopy in plain language. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec("Foundation Crohn's resources", "Read the Foundation What is Crohn's disease page as the primary source.", 'Surgery, nutrition, and medication guides supplement basics. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', "Youth and family materials exist for pediatric Crohn's. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment."),
            sec('Partnering with your care team', 'Track stools, pain, and medications in IBDPal between visits.', 'Do not use education pages for emergency triage. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Report fever, severe pain, or obstruction symptoms promptly. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Education boundaries', 'Foundation content is not individualized treatment advice.', 'The Foundation does not endorse IBDPal. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', "Second opinions are reasonable for complex Crohn's cases. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist."),
        ],
        [
            'Ask disease location and behavior at visits.',
            'Bring one-week symptom summaries.',
            'Review Foundation surgery guide if operations are discussed.',
            'Log perianal symptoms without embarrassment.',
            "Explore Crohn's hub on IBDPal.",
        ],
        [
            fq("Can Crohn's be cured by diet?", 'No. Nutrition matters but medical monitoring is essential.'),
            fq('Will everyone need surgery?', 'Not everyone. Many control disease with medications.'),
            fq("Is Crohn's the same as UC?", 'No. They are distinct IBD types with different patterns.'),
        ],
        rel(
            ("Foundation: What is Crohn's", 'https://www.crohnscolitisfoundation.org/what-is-crohns-disease'),
            ('What is IBD Foundation guide', '/guides/what-is-ibd-foundation'),
            ("Crohn's disease hub", '/crohns-disease'),
            ('Foods during flares', '/guides/foods-to-eat-crohns-flare'),
            ('Foundation surgery and ostomy', '/guides/foundation-ibd-surgery-ostomy'),
            ("Crohn's flare guide", '/guides/crohns-flare-what-to-do'),
        ),
    ),    "what-is-ulcerative-colitis-foundation": 
fmk(
        'This page summarizes Foundation patient education on ulcerative colitis and how IBDPal supports symptom tracking between clinic visits.',
        [
            sec('What ulcerative colitis involves', 'UC causes continuous inflammation of the colon lining, starting at the rectum and extending variable distances.', 'Symptoms often include bloody diarrhea, urgency, and cramping. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Extent categories include proctitis, left-sided, and extensive colitis. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec("How UC differs from Crohn's", "UC is limited to the colon and affects the inner lining continuously, unlike patchy transmural Crohn's.", 'Surgical cure of colon disease is possible for some UC patients, though pouch complications can occur. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Your team explains which diagnosis fits your tests. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Foundation UC resources', 'The Foundation What is ulcerative colitis page is the authoritative starting point.', 'Medication, surgery, and cancer surveillance guides add depth. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Bring questions from reading to gastroenterology visits. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
            sec('Monitoring and cancer screening', 'Long-standing colitis increases colorectal cancer risk. Surveillance colonoscopy schedules depend on duration and severity.', 'Do not skip maintenance mesalamine or biologics without clinician input. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Log blood and stool frequency during flares for triage. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Using IBDPal responsibly', 'Symptom logs complement Foundation reading.', 'Education does not replace emergency care for severe bleeding or pain. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'The Foundation does not endorse IBDPal. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
        ],
        [
            'Know your UC extent category.',
            'Track nocturnal stools separately.',
            'Review cancer surveillance guide with your GI.',
            'Ask about joint symptoms; they can link to IBD.',
            'Explore UC hub pages on IBDPal.',
        ],
        [
            fq('Is UC only diarrhea?', 'Bleeding and urgency are common even with moderate stool counts.'),
            fq("Can UC turn into Crohn's?", "Diagnoses can be reclassified if tests show Crohn's features."),
            fq('Does blood always mean emergency?', 'Volume and dizziness matter. Call your team for guidance.'),
        ],
        rel(
            ('Foundation: What is UC', 'https://www.crohnscolitisfoundation.org/what-is-ulcerative-colitis'),
            ('UC flare management', '/guides/ulcerative-colitis-flare-management'),
            ('UC diet foods', '/guides/ulcerative-colitis-diet-foods'),
            ('Colonoscopy surveillance guide', '/guides/foundation-ibd-colonoscopy-cancer-surveillance'),
            ('What is IBD Foundation guide', '/guides/what-is-ibd-foundation'),
            ('Ulcerative colitis hub', '/ulcerative-colitis'),
        ),
    ),    "foundation-ibd-appeal-letters": 
fmk(
        "This page explains how Crohn's and Colitis Foundation appeal letter templates support insurance denials for IBD medications and procedures, used with your prescriber.",
        [
            sec('When appeals are needed', 'Denials for biologics, infusions, imaging, or surgery often trigger formal appeals.', 'Timelines are strict. Missing deadlines restarts the process. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Foundation templates provide structure; your doctor personalizes medical facts. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Components of strong appeals', 'Include diagnosis, prior therapies tried, objective labs, endoscopy findings, and harm risk if treatment delays.', 'Patient impact statements add context but do not replace clinical evidence. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Attach peer-reviewed references only when requested by insurers. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Levels of appeal', 'Internal plan appeals, external independent review, and state insurance department complaints follow different rules.', 'Keep copies of every submission and delivery confirmation. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Clinic prior auth staff often lead; patients supply symptom logs. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
            sec('Working with your GI office', 'Sign medical release forms so staff can speak with payers.', 'Provide IBDPal exports showing flare frequency during denials. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Ask about bridge samples while appeals process. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('After approval', 'Confirm pharmacy benefit versus medical benefit routing for infusions.', 'Set calendar reminders before reauthorization windows. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Update appeal packets when switching jobs or insurers. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
        ],
        [
            'Fax appeals with confirmation pages.',
            'Highlight calprotectin or CRP trends.',
            'Include colonoscopy dates in packets.',
            'Never stop meds during appeals without advice.',
            'Review step therapy guide for context.',
        ],
        [
            fq('Can patients write appeals alone?', 'Letters need clinician signatures and records. Templates help you participate.'),
            fq('How many appeals are typical?', 'Some plans need two or three levels. Persistence is common.'),
            fq('Do appeals always win?', 'No, but many succeed with complete documentation.'),
        ],
        rel(
            ('Prior authorization guide', '/guides/ibd-prior-authorization-foundation'),
            ('Step therapy guide', '/guides/step-therapy-safe-step-act-ibd'),
            ('Foundation medication guide', '/guides/foundation-ibd-medication-guide'),
            ('Biologics overview', '/guides/biologics-crohns-colitis'),
            ('Doctor visit prep', '/guides/crohns-doctor-visit-prep'),
            ('Foundation resources hub', '/crohns-colitis-foundation-resources'),
        ),
    ),    "step-therapy-safe-step-act-ibd": 
fmk(
        'This page summarizes Foundation education on step therapy requirements and Safe Step Act reforms affecting access to IBD biologics.',
        [
            sec('What step therapy means', 'Insurers may require failing specific drugs before approving others.', 'Rules vary by plan and state. Employer and Medicaid plans differ. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Step therapy can delay optimal therapy if exemptions are not granted. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Safe Step Act overview', 'Federal reforms aim to streamline exceptions when step therapy is inappropriate.', 'State laws may offer additional patient protections. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Foundation advocacy materials explain current rights without legal advice. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Exception and exemption requests', 'Document prior failures, intolerances, and contraindications with chart notes.', 'Harm predictions from delays strengthen cases. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'GI letters should cite specific plan criteria verbatim when possible. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
            sec('Patient advocacy steps', 'Call insurer case managers and take reference numbers.', 'Involve employer HR for self-funded plans when appropriate. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', "Legislators' offices sometimes help constituents with insurance barriers. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway."),
            sec('Clinical perspective', 'Gastroenterologists choose drugs based on disease severity, location, and history, not only formulary order.', 'Shared decision making includes discussing step therapy risks. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Appeals and prior auth guides complement this topic. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
        ],
        [
            'Keep a medication history timeline handy.',
            'Ask clinic staff which steps your plan requires.',
            'Request written denial reasons.',
            'Explore copay assistance during delays.',
            'Log symptoms if treatment is postponed.',
        ],
        [
            fq('Does Safe Step Act ban step therapy?', 'No. It improves exception processes; plans may still use step therapy.'),
            fq('Can my doctor override instantly?', 'Sometimes via peer-to-peer review, not always immediately.'),
            fq('Do biosimilars count as steps?', 'Plan language varies. Read your formulary.'),
        ],
        rel(
            ('Prior authorization guide', '/guides/ibd-prior-authorization-foundation'),
            ('Appeal letters guide', '/guides/foundation-ibd-appeal-letters'),
            ('Biologics overview', '/guides/biologics-crohns-colitis'),
            ('Foundation medication guide', '/guides/foundation-ibd-medication-guide'),
            ('Foundation resources hub', '/crohns-colitis-foundation-resources'),
            ('Doctor visit prep', '/guides/crohns-doctor-visit-prep'),
        ),
    ),    "find-ccf-chapter-support-group": 
fmk(
        "This page helps you locate Crohn's and Colitis Foundation chapters and support groups near you using official Foundation locators and IBDPal community guides.",
        [
            sec('Using the chapter locator', 'Foundation websites list chapters by state and region with meeting calendars.', 'Virtual meetings expanded access after the pandemic. Check hybrid options. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Special interest groups may focus on parents, teens, or ostomy patients. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('What chapter meetings offer', 'Education speakers, walk events, advocacy training, and peer networking are common.', 'Volunteers share practical insurance and school navigation tips from lived experience. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Medical advice still comes from your personal GI team. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Starting if you are shy', 'Attend as a listener first. Introduce yourself to moderators privately.', 'Bring questions gathered from IBDPal guides. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Follow up with one person contact rather than trying to meet everyone. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
            sec('Beyond monthly meetings', 'Foundation walks fundraise research and build community.', 'Advocacy days connect patients with legislators on IBD policy. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Camp Oasis and teen programs link to chapters seasonally. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Online safety', 'Verify unofficial groups claiming Foundation affiliation.', 'Protect privacy in public posts. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Report dangerous treatment advice to moderators. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
        ],
        [
            'Search Foundation locator plus your city.',
            'Try one virtual meeting before traveling.',
            'Ask moderators about medical ground rules.',
            'Bring a friend for your first in-person event.',
            'Pair groups with clinic follow-up.',
        ],
        [
            fq('Are chapter meetings free?', 'Most are; verify registration for special events.'),
            fq('Can caregivers attend?', 'Many groups welcome partners and parents.'),
            fq('Do chapters provide medical care?', 'No. They offer education and peer support.'),
        ],
        rel(
            ('Support groups overview', '/guides/crohns-colitis-support-groups'),
            ('IBD support near me', '/guides/ibd-support-near-me'),
            ('Foundation emotional wellness', '/guides/foundation-emotional-wellness-ibd'),
            ('Camp Oasis guide', '/guides/camp-oasis-kids-ibd'),
            ('Chapter finder on Foundation site', 'https://www.crohnscolitisfoundation.org/local-chapters'),
            ('Foundation resources hub', '/crohns-colitis-foundation-resources'),
        ),
    ),    "foundation-emotional-wellness-ibd": 
fmk(
        "This page summarizes Crohn's and Colitis Foundation emotional wellness resources for coping with IBD-related stress, anxiety, and depression alongside medical care.",
        [
            sec('Emotional impact of chronic IBD', 'Diagnosis, flares, and treatments affect mood, body image, and relationships.', 'Anxiety about bathrooms and needles is common and treatable. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Mental health is part of whole-person IBD care, not a separate luxury. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Foundation wellness materials', 'Foundation pages cover coping skills, family communication, and when to seek therapy.', 'Use them with guidance from your GI and mental health professionals. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Crisis resources differ from general wellness tips. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Skills and therapies that help', 'Cognitive behavioral therapy, gut-directed hypnosis, and support groups show benefit in some studies.', 'Medications for anxiety or depression may coexist with IBD drugs with coordination. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Sleep, movement, and social connection support resilience. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
            sec('Caregivers and partners', 'Family burnout is real. Encourage loved ones to seek their own support.', 'Open communication reduces conflict during flares. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Partner guides on IBDPal complement Foundation reading. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('When to escalate care', 'Suicidal thoughts, panic attacks, or eating disorders need urgent professional help.', 'Use crisis lines and emergency services as appropriate. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Tell your GI if mood affects medication adherence. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
        ],
        [
            'Ask your clinic about GI psychology referrals.',
            'Schedule worry time instead of all-day rumination.',
            'Limit unmoderated forum scrolling before bed.',
            'Celebrate small functional wins weekly.',
            'Share Foundation pages with family.',
        ],
        [
            fq('Is depression normal with IBD?', 'It is common and treatable. Tell your care team.'),
            fq('Can therapy reduce flares?', 'It may improve coping and adherence; medical treatment still matters.'),
            fq('Does Foundation provide therapy?', 'It provides education, not licensed counseling sessions.'),
        ],
        rel(
            ('Stress and anxiety guide', '/guides/stress-anxiety-ibd'),
            ('Partner and caregiver guide', '/guides/partner-caregiver-ibd'),
            ('Sleep during flares', '/guides/sleep-ibd-flares'),
            ('Bathroom urgency anxiety article', '/blog/bathroom-urgency-anxiety-ibd'),
            ('Foundation resources hub', '/crohns-colitis-foundation-resources'),
            ('IBD helpline guide', '/guides/ibd-crohns-colitis-helpline'),
        ),
    ),    "newly-diagnosed-foundation-first-week": 
fmk(
        "This page outlines a first-week roadmap using Crohn's and Colitis Foundation newly diagnosed materials alongside IBDPal logging tools.",
        [
            sec('Day one: breathe and document', 'Write down your diagnosis terms, medications, and follow-up dates.', 'Save clinic after-hours numbers in your phone. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Read Foundation what is IBD pages at your own pace. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Days two to three: build support', 'Tell trusted friends or family what you need: rides, meals, or quiet.', 'Explore chapter or virtual support if ready. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Start a simple symptom log, even one line per day. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Days four to five: organize care', 'Activate patient portal accounts and pharmacy apps.', 'List questions for your next nurse call. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Review vaccine records with your team. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
            sec('Days six to seven: daily life planning', 'Consider school or work disclosure needs with HR or disability offices.', 'Pack a small flare kit for outings. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Schedule mental health check-in if mood is low. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Beyond week one', 'Colonoscopy prep, biologic education, and nutrition visits unfold over months.', 'Foundation hubs and IBDPal guides deepen topics as they arise. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Progress is nonlinear. Flares do not erase learning. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
        ],
        [
            'Create a dedicated email folder for IBD paperwork.',
            'Photograph insurance cards front and back.',
            'Ask for written flare instructions.',
            'Bookmark Foundation newly diagnosed hub.',
            'Explore /newly-diagnosed on IBDPal.',
        ],
        [
            fq('Should I read everything at once?', 'No. Pace yourself to avoid overwhelm.'),
            fq('Can I work during week one?', 'Many do. Rest when symptoms require.'),
            fq('Is it normal to grieve?', 'Yes. Counseling and groups help.'),
        ],
        rel(
            ('Newly diagnosed guide', '/guides/newly-diagnosed-crohns-colitis'),
            ('What is IBD Foundation guide', '/guides/what-is-ibd-foundation'),
            ('First GI appointment', '/guides/first-gastroenterology-appointment-ibd'),
            ('Visit prep checklist', '/visit-prep'),
            ('Newly diagnosed hub', '/newly-diagnosed'),
            ('Find a chapter group', '/guides/find-ccf-chapter-support-group'),
        ),
    ),    "pregnancy-ibd-foundation-resources": 
fmk(
        'This page summarizes Foundation education on pregnancy planning, fertility, and medication safety in IBD with links to coordinated OB and GI care.',
        [
            sec('Preconception planning', 'Ideally meet with GI and obstetrics before conceiving to optimize disease activity.', 'Active inflammation may affect fertility and pregnancy outcomes. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Fathers with IBD should also review medication questions with clinicians. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Medication continuity', 'Many IBD drugs are preferred over uncontrolled flares during pregnancy.', 'Never stop biologics or immunomodulators without coordinated specialist advice. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Foundation medication guides discuss pregnancy categories at patient level. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Monitoring during pregnancy', 'Disease monitoring may include symptom assessment, labs, and selective endoscopy when needed.', 'Flares during pregnancy need prompt GI and OB outreach. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Nutrition, iron, and vitamin D remain priorities. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
            sec('Delivery and postpartum', 'Most patients can vaginally deliver unless obstetric reasons dictate otherwise.', 'Postpartum flares occur. Sleep loss and stress management plans help. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Breastfeeding decisions include medication transfer discussions. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Emotional and social support', 'Pregnancy with chronic illness brings unique anxiety. Therapy and peer groups help.', 'Partners should attend key visits when possible. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Foundation family resources complement OB education classes. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
        ],
        [
            'Schedule preconception GI visit months before trying.',
            'Bring medication list to every OB appointment.',
            'Plan postpartum flare support early.',
            'Continue folate and iron per clinician orders.',
            'Log symptoms in IBDPal during pregnancy.',
        ],
        [
            fq('Does IBD lower fertility?', 'Active inflammation and some surgeries can affect fertility. Planning helps.'),
            fq('Are all IBD drugs unsafe in pregnancy?', 'No. Risk-benefit favors controlling disease in many cases.'),
            fq('Can I breastfeed on biologics?', 'Many options exist. Discuss specific drugs with your teams.'),
        ],
        rel(
            ('Foundation medication guide', '/guides/foundation-ibd-medication-guide'),
            ('Partner and caregiver guide', '/guides/partner-caregiver-ibd'),
            ('Foundation emotional wellness', '/guides/foundation-emotional-wellness-ibd'),
            ('What is IBD Foundation guide', '/guides/what-is-ibd-foundation'),
            ('Foundation resources hub', '/crohns-colitis-foundation-resources'),
            ('Doctor visit prep', '/guides/crohns-doctor-visit-prep'),
        ),
    ),    "youth-school-foundation-resources": 
fmk(
        'This page bridges Foundation youth and school resources for students with IBD, including 504 plans, nurse coordination, and teen programs.',
        [
            sec('School rights and documentation', 'Section 504 and similar laws may grant restroom access, medication timing, and absence flexibility.', 'Medical letters should be concise and updated yearly. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'School nurses store emergency medications with signed plans. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists.'),
            sec('Talking with teachers and coaches', 'Share only what is needed for safety and attendance.', 'PE modifications and hydration breaks are common accommodations. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Bullying about bathroom use should be reported immediately. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment.'),
            sec('Teen independence', 'Gradually shift refill and appointment responsibility to teens.', 'Peer groups and Camp Oasis reduce isolation. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Mental health screening matters during adolescence. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
            sec('College transition', 'Register with disability services before classes begin.', 'Dorm mini-fridges may store biologics with documentation. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'IBDPal college articles supplement Foundation guides. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Parents and guardians', 'Balance advocacy with growing autonomy.', 'Sibling support prevents family stress from focusing only on IBD. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Foundation family programs offer webinars and printouts. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
        ],
        [
            'Renew 504 letters each summer.',
            'Meet the school nurse before day one.',
            'Practice self-advocacy phrases with your child.',
            'Explore Camp Oasis when age-eligible.',
            'Read college with IBD article before applications.',
        ],
        [
            fq('Must schools allow unlimited bathroom breaks?', 'Reasonable accommodations are required; documentation helps.'),
            fq('Can teens self-carry injectables?', 'Policies vary; nurse plans clarify.'),
            fq('Should teachers know diagnosis details?', 'Functional needs can be described without full medical history.'),
        ],
        rel(
            ('Pediatric IBD help', '/guides/pediatric-crohns-colitis-help'),
            ('Workplace and school rights', '/guides/ibd-workplace-school-rights'),
            ('Foundation workplace school rights', '/guides/foundation-workplace-school-rights-ibd'),
            ('Camp Oasis guide', '/guides/camp-oasis-kids-ibd'),
            ('College with IBD article', '/blog/college-with-ibd'),
            ('Foundation resources hub', '/crohns-colitis-foundation-resources'),
        ),
    ),    "foundation-ibd-clinical-trials": 
fmk(
        "This page explains how Crohn's and Colitis Foundation clinical trials education helps patients explore research participation with their GI teams.",
        [
            sec('Why trials matter', 'Clinical trials advance new IBD therapies and monitoring tools.', 'Participation is voluntary and regulated with informed consent. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Standard care continues alongside many studies. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists.'),
            sec('Finding appropriate trials', 'Foundation trial finders and academic center websites list enrolling studies.', 'Inclusion criteria depend on disease type, prior meds, and labs. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Your gastroenterologist identifies ethically appropriate options. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Safety and informed consent', 'Read consent forms carefully. Ask about placebo chances, visit burden, and costs.', 'Report side effects promptly to study teams. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'You may withdraw without losing standard care. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
            sec('Practical participation issues', 'Travel, time off work, and childcare affect feasibility.', 'Some studies cover costs; others do not. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Document trial participation for future clinicians. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('After trials end', 'Extension studies or commercial access may be available.', 'Maintain follow-up scopes and labs per your GI plan. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Share outcomes with your regular IBD team. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
        ],
        [
            'Ask your GI about open trials at your center.',
            'Keep consent binders accessible.',
            'Log symptoms consistently during studies.',
            'Verify insurance interaction before enrolling.',
            'Explore Foundation trial finder online.',
        ],
        [
            fq('Will I get placebo?', 'Some trials use placebo; consent explains odds and crossover options.'),
            fq('Are trials only for severe disease?', 'Studies target varied severity levels with specific criteria.'),
            fq('Can trials replace my GI?', 'No. Study teams coordinate with your clinicians.'),
        ],
        rel(
            ('Biologics overview', '/guides/biologics-crohns-colitis'),
            ('Foundation medication guide', '/guides/foundation-ibd-medication-guide'),
            ('What is IBD Foundation guide', '/guides/what-is-ibd-foundation'),
            ('Doctor visit prep', '/guides/crohns-doctor-visit-prep'),
            ('Foundation resources hub', '/crohns-colitis-foundation-resources'),
            ('Newly diagnosed guide', '/guides/newly-diagnosed-crohns-colitis'),
        ),
    ),    "foundation-ibd-surgery-ostomy": 
fmk(
        'This page summarizes Foundation patient education on IBD-related surgery, ostomies, and recovery planning with links to surgical informed consent topics.',
        [
            sec('When surgery is considered', 'Medically refractory disease, complications like stricture or fistula, cancer dysplasia, or acute emergencies may lead to surgery.', 'Decisions are shared between patient, surgeon, and gastroenterologist. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Second opinions are reasonable for major operations. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Types of procedures', 'Resections, strictureplasty, colectomy with pouch, and permanent ostomies vary by diagnosis.', 'Minimally invasive approaches depend on anatomy and expertise. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Temporary diverting ostomies may protect anastomoses. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Ostomy life and support', 'WOC nurses teach appliance management and skin care.', 'Many patients swim, work, and travel with ostomies. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Peer ostomy groups complement Foundation materials. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
            sec('Recovery and follow-up', 'Nutrition, hydration, and physical therapy support healing.', 'Watch for blockage signs with ileostomies: pain, no output, vomiting. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', "Crohn's can recur after surgery; UC colon removal may be curative for colon disease. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway."),
            sec('Emotional preparation', 'Grief and body image changes are normal. Counseling helps.', 'Partners benefit from intimacy education resources. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Bring questions to pre-op visits in writing. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
        ],
        [
            'Meet WOC nursing before surgery if possible.',
            'Order extra ostomy supplies pre-discharge.',
            'Know blockage red flags.',
            'Review Foundation intimacy guide with partner.',
            'Log output changes after surgery.',
        ],
        [
            fq('Is ostomy permanent?', 'Some are temporary loops; others permanent depending on operation.'),
            fq('Will I need a special diet forever?', 'Diets evolve through recovery. Dietitians personalize.'),
            fq('Does surgery mean I failed?', 'No. Surgery is a valid tool in IBD care.'),
        ],
        rel(
            ('Living with an ostomy', '/guides/living-with-ostomy-ibd'),
            ('Foundation intimacy guide', '/guides/foundation-ibd-intimacy-sexual-health'),
            ('What is UC Foundation guide', '/guides/what-is-ulcerative-colitis-foundation'),
            ('Pain and fatigue guide', '/guides/foundation-ibd-pain-fatigue'),
            ('IBD hydration guide', '/guides/ibd-hydration-fluids'),
            ('Foundation resources hub', '/crohns-colitis-foundation-resources'),
        ),
    ),    "foundation-workplace-school-rights-ibd": 
fmk(
        'This page summarizes Foundation education on workplace and school rights for people with IBD, including accommodations and disclosure choices.',
        [
            sec('Legal frameworks overview', 'In the United States, ADA and Section 504 may protect employees and students with IBD.', 'Other countries have parallel laws. Foundation materials are educational, not legal advice. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Documentation from clinicians supports accommodation requests. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists.'),
            sec('Workplace accommodations', 'Flexible scheduling, remote work, restroom access, and leave for infusions are common requests.', 'FMLA or local leave laws may apply for flare recovery. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'HR offices process forms; clinicians complete medical sections. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('School and university settings', '504 plans travel with students across grades when updated.', 'College disability services require separate registration. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Nurses can administer medications per action plans. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
            sec('Disclosure strategies', 'You control how much detail employers or professors receive.', 'Functional language focuses on needs, not full charts. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Retaliation for lawful accommodation requests may be unlawful depending on jurisdiction. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Advocacy resources', 'Foundation toolkits provide sample letters and rights summaries.', 'Employment attorneys help complex cases. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Keep written records of requests and responses. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
        ],
        [
            'Renew accommodation letters yearly.',
            'Register college disability services early.',
            'Know your clinic fax for forms.',
            'Document denied requests in writing.',
            'Pair with IBDPal workplace guide.',
        ],
        [
            fq('Must I disclose IBD to employers?', 'You may request accommodations with limited disclosure supported by clinician letters.'),
            fq('Can schools refuse restroom access?', 'Reasonable access should be provided with proper documentation.'),
            fq('Does Foundation provide lawyers?', 'No. It offers education; legal counsel is separate.'),
        ],
        rel(
            ('Workplace and school rights IBDPal guide', '/guides/ibd-workplace-school-rights'),
            ('Youth school Foundation resources', '/guides/youth-school-foundation-resources'),
            ('College with IBD article', '/blog/college-with-ibd'),
            ('Living with an ostomy', '/guides/living-with-ostomy-ibd'),
            ('Partner and caregiver guide', '/guides/partner-caregiver-ibd'),
            ('Foundation resources hub', '/crohns-colitis-foundation-resources'),
        ),
    ),    "foundation-ibd-medication-guide": 
fmk(
        "This page bridges the Crohn's and Colitis Foundation Medication Guide with IBDPal visit prep and adherence tools for IBD therapies.",
        [
            sec('How to use the Medication Guide', 'Foundation guides describe drug classes, common side effects, and monitoring at patient reading level.', 'They supplement, not replace, pharmacy labels and clinician instructions. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Update your reading when switching therapies. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists.'),
            sec('Major drug classes in IBD', 'Aminosalicylates, corticosteroids, immunomodulators, biologics, and targeted small molecules each have roles depending on disease.', 'Combination therapy and sequential therapy are individualized. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Ask why a specific class fits your case. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Adherence and safety', 'Missed doses increase flare risk. Use reminders and travel letters.', 'Report infections, rashes, or neurologic symptoms promptly. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Vaccines and travel vaccines need planning on immunosuppression. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
            sec('Pregnancy, surgery, and interactions', 'Coordinate medication lists across GI, OB, surgeons, and dentists.', 'Some drugs require holding before operations. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Over-the-counter NSAIDs may worsen IBD; ask before using. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Insurance and access', 'Prior authorization and step therapy affect timing.', 'Appeal resources support denials. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Patient assistance programs help qualifying households. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
        ],
        [
            'Carry a wallet medication list.',
            'Review Foundation guide before starting new drugs.',
            'Ask pharmacists about interactions.',
            'Never stop steroids suddenly.',
            'Log infusion and injection dates in IBDPal.',
        ],
        [
            fq('Can I read the guide instead of talking to my doctor?', 'No. It prepares questions; clinicians personalize treatment.'),
            fq('Are generic drugs OK?', 'Often yes. Discuss switches with your team if symptoms change.'),
            fq('Do biologics weaken immunity?', 'They modify immune pathways; infection monitoring matters.'),
        ],
        rel(
            ('Biologics overview', '/guides/biologics-crohns-colitis'),
            ('Prior authorization guide', '/guides/ibd-prior-authorization-foundation'),
            ('Vaccines and infection guide', '/guides/foundation-ibd-vaccines-infection'),
            ('Pregnancy resources', '/guides/pregnancy-ibd-foundation-resources'),
            ('Doctor visit prep', '/guides/crohns-doctor-visit-prep'),
            ('Foundation resources hub', '/crohns-colitis-foundation-resources'),
        ),
    ),    "foundation-ibd-pain-fatigue": 
fmk(
        'This page summarizes Foundation education on pain and fatigue in IBD, distinguishing inflammatory symptoms from other causes with your clinician.',
        [
            sec('Sources of pain in IBD', 'Inflammation, strictures, abscesses, arthritis, and functional pain can coexist.', 'Location and timing help clinicians differentiate causes. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Do not assume all pain equals active colitis without evaluation. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Fatigue beyond feeling tired', 'Anemia, poor sleep, medications, depression, and inflammation contribute to fatigue.', 'Energy may lag even when stool frequency improves. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Multidisciplinary assessment is common in IBD centers. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Self-management strategies', 'Gentle activity, sleep hygiene, and pacing tasks help when clinicians approve.', 'Pain teams, physical therapy, and psychology add tools beyond drugs alone. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Nutrition repletion treats reversible fatigue causes. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
            sec('Medication and procedural options', 'Treating inflammation remains foundational.', 'Analgesic choices must avoid NSAIDs that may worsen IBD unless clinicians agree. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Nerve pain agents and referrals may help selected patients. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('When to seek urgent care', 'Severe abdominal pain with fever, rigid abdomen, or vomiting needs emergency evaluation.', 'Sudden pain changes after surgery warrant immediate outreach. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Chest pain or shortness of breath are not typical IBD pain alone. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
        ],
        [
            'Log pain location and relation to meals.',
            'Track sleep hours during fatigue spikes.',
            'Ask about anemia labs when exhausted.',
            'Avoid NSAIDs unless GI approves.',
            'Use pain-fatigue entries in visit prep.',
        ],
        [
            fq('Is fatigue normal in remission?', 'It can persist. Investigate treatable causes with your team.'),
            fq('Should I push through pain daily?', 'Pacing helps; severe pain needs medical assessment.'),
            fq('Do opioids treat IBD inflammation?', 'They mask pain and may worsen gut function. Use only as directed.'),
        ],
        rel(
            ('Sleep during flares', '/guides/sleep-ibd-flares'),
            ('Stress and anxiety guide', '/guides/stress-anxiety-ibd'),
            ('Iron deficiency guide', '/guides/iron-deficiency-nutrition-ibd'),
            ('Extraintestinal manifestations', '/guides/foundation-ibd-extraintestinal-manifestations'),
            ("Crohn's flare guide", '/guides/crohns-flare-what-to-do'),
            ('Foundation emotional wellness', '/guides/foundation-emotional-wellness-ibd'),
        ),
    ),    "foundation-ibd-extraintestinal-manifestations": 
fmk(
        'This page summarizes Foundation education on extraintestinal manifestations of IBD affecting joints, skin, eyes, and other organs beyond the bowel.',
        [
            sec('Common extraintestinal manifestations', 'Peripheral arthritis, axial spondyloarthritis, erythema nodosum, pyoderma gangrenosum, and uveitis appear in some patients.', 'Symptoms may flare with bowel activity or sometimes independently. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Tell your GI about joint pain, eye redness, or new rashes promptly. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Coordinated specialty care', 'Rheumatology, dermatology, and ophthalmology may join your team.', 'Some symptoms need urgent eye evaluation to protect vision. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Medication choices may treat both bowel and joint disease. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Monitoring and labs', 'Inflammatory markers do not always correlate with joint pain.', 'Imaging of spine and sacroiliac joints may be ordered. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Skin biopsies clarify diagnosis when appearance is unclear. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
            sec('Patient reporting tips', 'Photo rashes with dates for telehealth.', 'Note morning stiffness duration in joints. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Eye pain, light sensitivity, or blurred vision need same-day outreach. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Education boundaries', 'Foundation pages describe patterns; your clinicians diagnose specific manifestations.', 'Do not start immunosuppressants without specialist coordination. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'The Foundation does not endorse IBDPal. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
        ],
        [
            'Report eye symptoms immediately.',
            'Track joint pain separately from abdominal pain.',
            'Bring photos of skin changes to visits.',
            'Ask if biologics target your joint disease.',
            'Read ankylosing spondylitis article if referred.',
        ],
        [
            fq('Do all IBD patients get joint pain?', 'No, but it is common enough to screen in clinic.'),
            fq('Can skin issues scar?', 'Some lesions like pyoderma gangrenosum need aggressive care.'),
            fq('Should I see an optometrist or ophthalmologist?', 'Red painful eyes need urgent ophthalmology, not routine glasses visits.'),
        ],
        rel(
            ('Ankylosing spondylitis article', '/blog/ankylosing-spondylitis-ibd'),
            ('Pain and fatigue guide', '/guides/foundation-ibd-pain-fatigue'),
            ("What is Crohn's Foundation guide", '/guides/what-is-crohns-disease-foundation'),
            ('Biologics overview', '/guides/biologics-crohns-colitis'),
            ('Doctor visit prep', '/guides/crohns-doctor-visit-prep'),
            ('Foundation resources hub', '/crohns-colitis-foundation-resources'),
        ),
    ),    "foundation-complementary-medicine-ibd": 
fmk(
        'This page summarizes Foundation guidance on complementary and integrative approaches in IBD, emphasizing safety and coordination with gastroenterology care.',
        [
            sec('Defining complementary approaches', 'Herbs, probiotics, acupuncture, mindfulness, and dietary supplements fall under complementary integrative health.', 'Evidence quality varies widely. Some approaches lack IBD-specific trials. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Complementary does not mean harmless or interchangeable with prescribed drugs. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Discussing supplements with your GI team', 'Bring bottles to visits. Interactions with immunosuppressants matter.', 'Probiotics are strain-specific; general yogurt marketing oversimplifies. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Turmeric, aloe, and wormwood products carry bleeding or liver risks. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Mind-body practices', 'Meditation, yoga, and gut-directed hypnosis may improve symptom coping.', 'They support but rarely replace anti-inflammatory treatment when scopes show active disease. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Choose instructors aware of chronic illness limitations. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
            sec('Red flags in alternative marketing', 'Cures claiming to eliminate biologics are dangerous.', 'Detox programs and colon cleanses can dehydrate and disrupt electrolytes. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Testimonials omit medication and surgical histories. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Integrative care done well', 'Academic centers sometimes offer integrative IBD clinics with coordinated oversight.', 'Tell all practitioners you have IBD and list your drugs. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Foundation materials stress open communication with your gastroenterologist. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
        ],
        [
            'Show supplement labels at every GI visit.',
            'Avoid colon cleanse products.',
            'Ask for evidence behind probiotic strains.',
            'Pair yoga with medical care, not instead of it.',
            'Report new herbs before surgery.',
        ],
        [
            fq('Are probiotics FDA approved for IBD?', 'Most are not approved as drugs. Discuss specific products with your team.'),
            fq('Can acupuncture treat inflammation?', 'It may help symptoms; bowel inflammation still needs GI monitoring.'),
            fq('Is CBD legal and safe?', 'Regulation varies. Interactions and liver effects need clinician input.'),
        ],
        rel(
            ('Autoimmune nutrition basics', '/guides/autoimmune-nutrition-basics'),
            ('Anti-inflammatory diet guide', '/guides/anti-inflammatory-diet-ibd'),
            ('Stress and anxiety guide', '/guides/stress-anxiety-ibd'),
            ('Foundation emotional wellness', '/guides/foundation-emotional-wellness-ibd'),
            ('Elimination diet guide', '/guides/elimination-diet-when-to-stop-ibd'),
            ('Foundation resources hub', '/crohns-colitis-foundation-resources'),
        ),
    ),    "foundation-ibd-travel-restroom-access": 
fmk(
        'This page summarizes Foundation travel and restroom access resources for people with IBD, including cards, apps, and legal context.',
        [
            sec('Restroom access challenges', 'Urgency can make locked retail restrooms risky. Planning routes reduces anxiety.', 'Some regions have ally restroom laws or medical cards explaining needs. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Foundation materials describe advocacy without guaranteeing access in every venue. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Travel preparation', 'Airport security, biologic storage, and time zones affect medication timing.', 'Carry clinician letters for injectables and medical liquids. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Identify hospitals at destination for flare contingencies. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Apps and cards', 'Restroom finder apps crowdsource locations. Download offline maps before travel.', 'Foundation and advocacy cards can be shown discreetly to staff. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Translate key phrases for international trips. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
            sec('Flying and road trips', 'Aisle seats near lavatories help on planes. Pre-board when offered.', 'Road trips plan gas station chains with reliable facilities. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Pack flare kits in carry-on luggage only. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('If access is denied', 'Stay calm and ask for managers. Know local laws when applicable.', 'Prioritize health over confrontation when symptoms are urgent. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Document incidents for advocacy organizations if safe to do so. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
        ],
        [
            'Download restroom apps before departure.',
            'Carry a clinician travel letter.',
            'Wear discreet medical alert if desired.',
            'Know TSA rules for liquids and syringes.',
            'Read IBDPal travel planning guide too.',
        ],
        [
            fq('Do restroom cards guarantee entry?', 'They help explain needs but do not override all store policies.'),
            fq('Can I use employee restrooms?', 'Some laws require reasonable access; outcomes vary.'),
            fq('Should I avoid travel with active flares?', 'Discuss trip timing with your GI team.'),
        ],
        rel(
            ('Travel planning guide', '/guides/ibd-travel-planning'),
            ('Flare emergency supplies', '/guides/ibd-flare-emergency-supplies'),
            ('Dining out with IBD', '/guides/dining-out-with-ibd'),
            ('Living with an ostomy', '/guides/living-with-ostomy-ibd'),
            ('Biologics and travel article', '/blog/biologics-flying-travel-ibd'),
            ('Bathroom urgency anxiety article', '/blog/bathroom-urgency-anxiety-ibd'),
        ),
    ),    "foundation-ibd-intimacy-sexual-health": 
fmk(
        'This page summarizes Foundation education on intimacy, sexual health, and body image for people with IBD and ostomies.',
        [
            sec('Common concerns patients report', 'Fatigue, pain, ostomy appliances, and medication side effects affect desire and function.', 'Partners may fear causing harm. Open conversation reduces assumptions. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Problems are common and worth mentioning to clinicians. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists.'),
            sec('Talking with partners', 'Choose low-stress moments for education about IBD and ostomies.', 'Humor and patience help when experimenting with covers or positions. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Counseling supports couples when communication stalls. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Medical evaluation', 'GI, gynecology, urology, and pelvic floor therapists address specific issues.', 'Some medications affect libido. Adjustments may be possible. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Perianal disease needs specialized surgical input before certain activities. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
            sec('Ostomy-specific tips', 'Empty pouches beforehand. Soft bands and lingerie designed for ostomies improve confidence.', 'Leak anxiety decreases with practice and proper fit. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Intimacy includes non-intercourse closeness when needed. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Safety and boundaries', 'Consent and pacing matter always. Stop if pain occurs.', 'STI prevention still applies. Immunosuppression raises infection stakes. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Foundation materials are educational, not therapy. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
        ],
        [
            'Bring intimacy questions to clinic visits.',
            'Empty ostomy pouches before closeness.',
            'Explore pelvic floor therapy if referred.',
            'Read partner caregiver guide together.',
            'Give yourself grace during flares.',
        ],
        [
            fq('Is sex safe with IBD?', 'Often yes when disease and partners are considered; ask about perianal disease.'),
            fq('Will partners notice ostomies?', 'Planning and modern appliances reduce visibility.'),
            fq('Should I avoid sex during flares?', 'Comfort guides choices; medical clearance matters for some cases.'),
        ],
        rel(
            ('Living with an ostomy', '/guides/living-with-ostomy-ibd'),
            ('Partner and caregiver guide', '/guides/partner-caregiver-ibd'),
            ('Foundation surgery and ostomy', '/guides/foundation-ibd-surgery-ostomy'),
            ('Stress and anxiety guide', '/guides/stress-anxiety-ibd'),
            ('Foundation emotional wellness', '/guides/foundation-emotional-wellness-ibd'),
            ('Pregnancy resources', '/guides/pregnancy-ibd-foundation-resources'),
        ),
    ),    "foundation-ibd-vaccines-infection": 
fmk(
        'This page summarizes Foundation guidance on vaccines and infection prevention for people with IBD, especially on immunosuppressive therapy.',
        [
            sec('Why vaccines matter in IBD', 'Immunosuppressants and active inflammation raise infection risks.', 'Vaccines reduce preventable illnesses that could complicate IBD care. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Plans should be individualized with your GI and primary care. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('Live versus non-live vaccines', 'Live vaccines may be avoided on some therapies. Timing before starting biologics matters.', 'Inactivated vaccines such as influenza, pneumococcal, and COVID-19 are commonly recommended. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Travel vaccines need advance planning with your team. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Screening for latent infections', 'TB and hepatitis B screening often precedes biologics.', 'Treat latent TB before starting certain drugs. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Repeat screening may be needed when switching therapies. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
            sec('Everyday infection prevention', 'Hand hygiene, food safety while traveling, and prompt care for fever on immunosuppression are key.', 'Report shingles, persistent cough, or unusual rashes early. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Dental and surgical teams need your medication list. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Family and household considerations', 'Household members may need certain vaccines to protect immunosuppressed patients.', 'Discuss newborn and live vaccine exposure with obstetrics when relevant. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Foundation pages list talking points for clinicians. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit.'),
        ],
        [
            'Keep a vaccine card photo on your phone.',
            'Ask about vaccines before starting biologics.',
            'Report fever on immunosuppression promptly.',
            'Plan travel vaccines months ahead.',
            'Coordinate flu shots with infusion schedules.',
        ],
        [
            fq('Can I get vaccines during a flare?', 'Often yes for inactivated vaccines; timing is individualized.'),
            fq('Are vaccines safe on biologics?', 'Generally recommended; discuss specific vaccines with your GI.'),
            fq('Should household members get flu shots?', 'Often recommended to protect immunosuppressed patients.'),
        ],
        rel(
            ('Biologics overview', '/guides/biologics-crohns-colitis'),
            ('Foundation medication guide', '/guides/foundation-ibd-medication-guide'),
            ('Travel planning guide', '/guides/ibd-travel-planning'),
            ('Clinical trials guide', '/guides/foundation-ibd-clinical-trials'),
            ('Doctor visit prep', '/guides/crohns-doctor-visit-prep'),
            ('Foundation resources hub', '/crohns-colitis-foundation-resources'),
        ),
    ),    "foundation-ibd-colonoscopy-cancer-surveillance": 
fmk(
        'This page summarizes Foundation education on colonoscopy surveillance and colorectal cancer risk in longstanding IBD, especially colonic disease.',
        [
            sec('Why surveillance matters', 'Chronic colitis increases colorectal cancer risk compared with the general population.', 'Duration, extent, severity, and family history influence screening schedules. Symptom patterns tracked over several days are more useful to your clinician than a single snapshot.', 'Surveillance colonoscopy with biopsies detects dysplasia early. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice.'),
            sec('How schedules are set', 'Gastroenterologists use disease duration, prior dysplasia, and PSC presence to set intervals.', 'Do not skip scopes because you feel well. Inflammation may be silent. Write down questions for your gastroenterologist before each visit so limited appointment time is used well.', 'Bring prior pathology reports to new clinics. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends.'),
            sec('Preparing for surveillance scopes', 'Bowel prep must visualize the colon well. Poor prep delays diagnosis.', 'Coordinate biologic timing and anticoagulants with your team. Medication adherence and follow-up labs are as important as diet changes for many IBD patients.', 'Sedation plans and escorts follow standard colonoscopy rules. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment.'),
            sec('If dysplasia is found', 'Management may include enhanced surveillance, endoscopic removal, or surgery depending on findings.', 'Multidisciplinary IBD-dysplasia teams exist at referral centers. Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift.', 'Questions about fertility and pouch function belong in those visits. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist. Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit. Your GI team can adjust recommendations based on labs, imaging, and symptom trends. Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment. If symptoms worsen while you try these steps, contact your clinic using your flare pathway.'),
            sec('Primary prevention alongside surveillance', 'Controlling inflammation pharmacologically reduces cancer risk.', 'Smoking cessation helps UC and general cancer risk. Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist.', 'Report new bleeding or change in symptoms between scopes. If symptoms worsen while you try these steps, contact your clinic using your flare pathway. Bring these observations to your next IBD appointment so your team can personalize advice. Children, older adults, and post-surgical patients may need modified guidance from specialists. Patient education supports shared decision making; it does not replace individual medical assessment. Discuss how this topic applies to your current disease activity with your gastroenterologist.'),
        ],
        [
            'Know your last scope date and next due date.',
            'Bring pathology reports to new GI clinics.',
            'Follow prep instructions exactly.',
            'Ask how PSC changes surveillance if applicable.',
            'Do not skip scopes during remission.',
        ],
        [
            fq("Do Crohn's colitis patients need surveillance?", "Colonic Crohn's involvement may warrant protocols similar to UC. Personalize with your GI."),
            fq('Is annual colonoscopy always required?', 'Intervals vary from one to five years or more based on risk.'),
            fq('Does mesalamine prevent cancer?', 'Controlling inflammation matters; discuss chemoprevention studies with your team.'),
        ],
        rel(
            ('Colonoscopy prep article', '/blog/colonoscopy-prep-ibd'),
            ('What is UC Foundation guide', '/guides/what-is-ulcerative-colitis-foundation'),
            ('Foundation medication guide', '/guides/foundation-ibd-medication-guide'),
            ('UC flare management', '/guides/ulcerative-colitis-flare-management'),
            ('Doctor visit prep', '/guides/crohns-doctor-visit-prep'),
            ('Foundation resources hub', '/crohns-colitis-foundation-resources'),
        ),
    ),}
