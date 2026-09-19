# -*- coding: utf-8 -*-
"""Build ~10-minute reader Q&A answers and publish ids 15-19."""
from __future__ import annotations

import json
import os
import re
from pathlib import Path

import psycopg2

ROOT = Path(__file__).resolve().parents[1]
SERVER_ENV = ROOT.parent / "ibdpal-server" / "config.env"
MAX_CHARS = 12000
TARGET_WORDS = 1950


def read_env(path: Path) -> dict:
    out = {}
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def words(text: str) -> int:
    return len(re.findall(r"\S+", text))


def approx_minutes(text: str) -> float:
    return round(words(text) / 220.0, 1)


A15 = r'''
Short answer: a GLP-1 medicine can change gut speed, fullness, and nausea for almost anyone who takes it. That does not automatically mean it is "bad for IBD," and it does not automatically mean it will calm gut inflammation either. For people with Crohn's disease or ulcerative colitis, the honest frame is this: GLP-1 drugs (semaglutide, tirzepatide, and related medicines sold under names such as Ozempic, Wegovy, Mounjaro, and Zepbound) act mainly on appetite, gastric emptying, and metabolic pathways. They are not IBD biologics. Some people with IBD feel better overall after weight loss and steadier blood sugar. Others notice more nausea, constipation, or diarrhea and wonder whether the drug is flaring their disease. Those two stories can both be true in different people, and only your gastroenterologist can sort which pattern is yours.

Start with what the medicine is designed to do. GLP-1 receptor agonists slow how quickly the stomach empties, increase satiety, and often reduce calorie intake. Slow emptying is useful for weight and glucose control. It is also the reason early weeks commonly bring nausea, early fullness, burping, and sometimes vomiting if doses climb too fast or meals are large and fatty. Diarrhea can appear too, especially when people change diet sharply, use sugar alcohols, or have an underlying bowel that already runs loose. Constipation is also reported. So if you already live with urgency, liquid stools, or post-resection bowel habits, a new GLP-1 can amplify symptoms that feel "IBD-ish" without proving that mucosal inflammation is rising.

That distinction matters more than social media threads admit. IBDPal readers often ask whether a GLP-1 "helps gut inflammation." Right now, patient education should stay careful: interesting research signals and clinic anecdotes are not the same as an approved IBD indication. Do not start, stop, or dose-escalate a GLP-1 to treat Crohn's or colitis on your own. If you and your clinicians choose a GLP-1 for obesity, type 2 diabetes, or another labeled reason, treat IBD monitoring as a parallel track. Keep your flare plan, calprotectin schedule, and biologic or small-molecule therapy exactly as prescribed unless your IBD team changes them in writing.

How do you tell side effect from flare? Use a two-week pattern log, not a single bad afternoon. Track dose day, meal size, fat content, stool form (a Bristol stool chart helps), night stools, blood, mucus, fever, abdominal pain location, and whether symptoms cluster in the hours after injection or after large meals. GLP-1 nausea often peaks after dose increases and eases when titration slows. Active IBD more often brings progressive urgency, night waking, blood, weight drop, or a rising fecal calprotectin. Neither rule is perfect. Overlap is common after ileal resection, with bile acid diarrhea, with IBS-like symptoms, and when anxiety about a new drug is high. Bring the log to both the prescribing clinician and your GI nurse. Ask explicitly: "Do we need a calprotectin now, or is this expected GLP-1 gut slowing?"

A useful way to organize the first month is to treat weeks 1 to 2 as an adaptation window and weeks 3 to 4 as a pattern window. In the adaptation window, mild nausea after larger dinners is common. In the pattern window, ask whether symptoms are drifting toward your personal flare signature. If your flares usually include night stools and blood, and those are absent while you mainly feel full and queasy after fatty meals, that leans toward drug effect. If night stools and blood return while calprotectin climbs, that leans toward disease activity—even if a GLP-1 started the same month.

Practical ways people reduce GLP-1 gut misery without abandoning therapy (always confirm with your prescriber): smaller meals, less grease, slower eating, careful alcohol limits, and not jumping dose weeks early because a friend "felt fine." Stay hydrated. Report persistent vomiting, inability to keep fluids down, severe upper abdominal pain, or signs of dehydration the same day. Those are not "wait and see if IBD calms down" symptoms. If you are on immunosuppression, fever plus worsening diarrhea still belongs on your IBD red-flag list even if you just started a GLP-1.

Insurance, compounding, and "research peptides" deserve a clear warning. Stick to pharmacy-dispensed, clinician-prescribed products. Unregulated pens and online powders add dosing and sterility risk on top of IBD complexity. If cost is the barrier, ask about manufacturer support and covered alternatives rather than gray-market substitutes. If your endocrinology or obesity clinic and your GI clinic do not talk to each other, you become the bridge—share medication lists and recent IBD labs at both visits.

Nutrition while appetite drops is easy to ignore until fatigue explodes. Rapid under-eating can worsen hair shedding, dizziness, and micronutrient gaps IBD already threatens—iron, B12, vitamin D, and protein among them. If you are losing weight faster than planned, tell both teams. An IBD-aware dietitian can help you keep protein up with smaller, more frequent meals that match GLP-1 fullness. Oral nutrition drinks sometimes help when solid food feels impossible, but they are not a free pass to skip medical follow-up.

Pregnancy, planned conception, and breastfeeding need separate counseling because metabolic medicines and IBD therapies have their own rules. Do not assume a GLP-1 is compatible because a friend used it. Ask before you are already pregnant. The same caution applies if you are scheduling elective endoscopy or surgery: tell anesthesia and surgical teams about every weekly injection.

People with prior bowel obstruction, severe gastroparesis symptoms, or complex post-surgical anatomy should mention that history before starting. Slowed gastric emptying is the therapeutic point of many GLP-1 medicines; in a complicated IBD anatomy it can feel different than in someone without intestinal disease. Your clinicians decide whether the benefit outweighs that risk for you.

Mental load matters too. Starting a visible, highly discussed medicine while living with an invisible chronic disease can spike health anxiety. Anxiety can loosen stools and amplify nausea without proving a flare. That does not mean "it is all in your head." It means your care plan may need both medical monitoring and practical anxiety supports—sleep, paced exposure to dose days, and clear thresholds for when to message clinic.

Bring these questions to your next visits: Why was this GLP-1 chosen for me given my IBD history? What titration schedule minimizes nausea? Which symptoms should trigger a same-week GI message versus an ER visit? Do we schedule a calprotectin checkpoint after dose increases? If diarrhea worsens, what is the first workup step—stool studies, binder trial discussion, or scope planning? Who owns dose changes if both clinics disagree?

Related education: [Should I be on a GLP-1 if I have IBD?](/ask/glp-1-if-i-have-ibd), [Reading IBD labs](/blog/reading-ibd-labs-calprotectin-crp), [CRP normal but still sick](/blog/crp-normal-still-symptoms-ibd), [When to call GI vs ER](/blog/when-to-call-gi-vs-er-ibd), and [Flare or bad few days](/ask/flare-or-bad-few-days).
'''.strip()


A16 = r'''
Often yes in clinical terms—and often "not automatically" in insurance terms. Many IBD medicines begin as clinic infusions and later offer a subcutaneous (under-the-skin) maintenance option for some patients. Vedolizumab (Entyvio), risankizumab (Skyrizi), and other advanced therapies have pathways where IV induction is followed by injections at home or in clinic, depending on the label, your disease, and your team’s judgment. Infliximab products and other agents have their own IV-versus-subcut stories. The medical question and the pharmacy-benefit question are related but not identical. Your gastroenterologist decides whether a switch is appropriate for disease control. Your insurer and specialty pharmacy decide whether that new form is covered as a continuation or treated like a fresh authorization.

Clinically, a switch is usually considered after induction when disease is settling, lab trends look favorable, and you (or a caregiver) can learn injection technique, storage, and what to do if a dose is missed. Infusion chairs provide observation time and nursing support. Home pens trade that for convenience, travel flexibility, and fewer work absences. They also shift responsibility: refrigeration, sharps disposal, timing around travel, and recognizing injection-site reactions. Ask for teach-back training before your first solo dose. Ask what to do if the pen misfires, if you travel across time zones, or if a dose lands during a fever or infection workup.

Insurance is where people get blindsided. Medical benefit (Part B–style buy-and-bill infusions) and pharmacy benefit (specialty pharmacy pens) are different buckets. Moving from IV to subcut can change which department pays, which prior authorization form is required, which copay assistance applies, and whether step therapy resets. Some plans treat the subcutaneous product as a new request even when the active molecule is the same family. Others approve a "site of care" or "formulation change" more smoothly if your clinic’s authorization team submits clinical notes showing stable response and medical necessity for home administration. Do not assume the infusion approval letter covers the pen.

Before you celebrate leaving the infusion center, ask your clinic’s prior-auth or specialty pharmacy coordinator these concrete questions: Will this be billed under medical or pharmacy benefit? Is a new prior authorization required? What is the expected turnaround? Is there a bridge supply if approval lags? Does manufacturer support change when the NDC or formulation changes? Will my deductible reset mid-year? Get the answers in writing or in the patient portal when possible. If you have Medicare, Medicaid, or an employer carve-out specialty vendor, rules vary again. International readers should translate this into local hospital pharmacy and national formulary language rather than U.S. fax-prior-auth folklore.

Timing the switch matters for disease control. Avoid a gap between the last infusion and the first injection unless your team planned it. Ask whether drug levels, antibodies, calprotectin, or a clinic visit should land near the transition. If symptoms creep back during a coverage delay, call early—waiting weeks "hoping the pen arrives" can cost remission. Some teams keep one more infusion scheduled as a safety net until the first home shipments are in your fridge.

Build a home kit before day one: a working thermometer for the fridge shelf (not the door), a backup cool pack for short trips, a sharps container, alcohol swabs, a dosing calendar, and the specialty pharmacy phone number. Photograph the pen box lot numbers when they arrive. If a shipment is delayed, you want documentation ready for the clinic to escalate.

Side effects and monitoring do not disappear because the route changed. Injection-site redness is common; spreading rash, facial swelling, wheezing, or chest tightness is urgent. Keep vaccinations, TB and hepatitis screening history, and infection precautions on the same page you used for infusions. Travel with a cooling plan and a clinician letter if airport security may question refrigerated pens. If you share a household fridge with roommates, label a dedicated bin so doses are not tossed with leftovers.

Work and school logistics often improve with home injections, but they introduce new privacy questions. Some people inject in a locked office; others prefer clinic administration for that reason alone. Neither choice is more "serious." Choose the setting you can sustain for years, not the one that looks best on a forum.

If the insurer denies the subcutaneous version, that is not the end. Ask for the denial reason code, submit peer-to-peer review, and use appeal language that ties home administration to adherence, work or school constraints, and documented response to the molecule. Manufacturer hubs sometimes help with temporary supply during appeal. Meanwhile, do not stop therapy without a written interim plan from your IBD team. Temporary return to infusion can be a bridge, not a failure.

Caregivers deserve training too. If a partner or parent will help with injections, have them attend the teach-back visit. Missed doses after a caregiver schedule change are a common silent relapse trigger.

Related education: [Entyvio patient guide](/blog/entyvio-patient-guide-ibd), [Skyrizi patient questions](/blog/skyrizi-patient-questions-ibd), [Infusion day expectations](/blog/infusion-day-what-to-expect), [Prior authorization timeline](/blog/prior-authorization-biologics-timeline), and [Insurance and biologics](/blog/insurance-biologics-ibd).
'''.strip()


A17 = r'''
A falling fecal calprotectin is genuinely good news about gut inflammation. It is not a full verdict that every loose stool is now "just IBS." Think of calprotectin as a stool marker that often tracks neutrophilic inflammation in the intestine. When it falls into your personal target range, the odds of active mucosal IBD usually improve. Liquid stools can still continue for many other reasons: irritable bowel syndrome overlap, bile acid diarrhea after ileal disease or resection, diet change, infection, pelvic floor dysfunction, medication effects, microscopic inflammation below the radar of one test, or incomplete healing in a skip area. The useful clinical question is not "IBD or IBS forever?" It is "What is driving today’s liquid stool while inflammation markers look quieter?"

First, confirm the trend, not a single printout. Labs have cutoffs that vary by assay. A drop from very high to mid-range is progress even if the number is not yet "perfect." Ask your team what target they use for you, whether the sample was collected correctly, and whether a repeat is needed before rewriting your whole diagnosis. Blood markers such as CRP can be quiet while the gut is active, and the reverse story also happens: symptoms roar while calprotectin settles. That is why many IBD programs still use scopes, imaging, or structured symptom scores alongside stool tests.

IBS-like symptoms are common in people who already have Crohn's or ulcerative colitis. After inflammation cools, the bowel can remain hypersensitive. Urgency, loose stools with stress or meals, and bloating without blood or night fever can fit IBS overlap. Labeling it IBS does not mean the original IBD vanished or that you imagined years of disease. It means the treatment plan may shift toward diet structure, fiber titration when appropriate, gut-directed behavioral strategies, and careful medication choices—while you still keep IBD surveillance on the calendar.

Bile acid diarrhea deserves special mention after terminal ileum inflammation or resection. Excess bile acids in the colon pull water and cause urgent liquid stools even when calprotectin looks reassuring. Clinicians may trial a bile acid binder when the story fits. Do not start binders as a self-experiment without guidance if you have fat-soluble vitamin issues or complex medication lists. Pancreatic enzyme problems, small intestinal bacterial overgrowth after surgery, and overflow around partial obstruction are other "loose stool with quieter calprotectin" possibilities that need a clinician, not a forum poll.

Diet experiments can help or confuse. A sudden jump into sugar-free snacks, coffee stacking, or high-fat takeout can loosen stools without raising calprotectin. So can magnesium supplements, some antibiotics, and GLP-1 medicines. Before you conclude "my IBD is back," list every new food, drink, and drug from the past two weeks.

How should you act this week? Keep a seven-day diary: stool form, night stools, blood, mucus, meal triggers, caffeine, artificial sweeteners, new medicines, and stress load. Note whether urgency is meal-related or random. Share whether you ever feel incomplete emptying or pelvic pressure. Bring the diary plus your calprotectin numbers to the visit and ask three direct questions: Do we repeat stool testing? Do we need imaging or a scope despite the drop? Should we evaluate bile acid diarrhea, infection, or IBS overlap next?

Red flags still override a pretty lab value. New heavy bleeding, nocturnal stools that are escalating, fever, weight loss, severe pain, or dehydration needs same-week or urgent contact even if last month’s calprotectin looked better. A reassuring lab is a snapshot. Your body can change between draws.

Do not stop IBD therapy because stools remain loose. Mucosal healing and symptom healing are related but not identical clocks. Many people need months of stable therapy after calprotectin improves before anyone discusses de-escalation. Stopping a biologic because "it must be IBS now" is a common way silent inflammation returns.

It also helps to separate "function" from "identity." You can have quiet inflammation labs and still need bathroom mapping at work, a 504 plan at school, or pelvic floor physical therapy. Those supports are not evidence that your IBD team failed. They are evidence that living with a chronic gut condition is bigger than one biomarker.

If anxiety spikes every time stools loosen, ask for a written personal action plan: which changes wait 48 hours, which trigger a portal message, and which go to urgent care. Clear thresholds reduce catastrophic guessing at 2 a.m.

Related education: [Does one calprotectin mean I am getting worse?](/ask/calprotectin-one-result-getting-worse), [High calprotectin: what next](/blog/high-calprotectin-what-next), [Reading IBD labs](/blog/reading-ibd-labs-calprotectin-crp), [Normal CRP but still sick](/blog/crp-normal-still-symptoms-ibd), and [Flare or bad few days](/ask/flare-or-bad-few-days).
'''.strip()


A18 = r'''
Both are possible—and you should not guess alone from a bathroom mirror. Advanced IBD therapies (biologics and targeted small molecules) can be associated with skin changes in some people. IBD itself also links to extraintestinal skin disease. Steroid tapers, antibiotics, nutrition gaps, and everyday eczema triggers muddy the picture further. The practical approach is to describe the rash clearly, photograph it, note timing against dose changes, and get the right clinician eyes on it quickly when it is severe, painful, blistering, or near the eyes.

Start by separating common patterns patients report. Acne-like bumps on the face, chest, or back can appear or worsen with certain therapies and with steroid exposure. Eczema-like dry, itchy patches can flare when the skin barrier is stressed, when immunosuppression shifts immune tone, or when a person already had atopic dermatitis. Psoriasiform rashes are discussed with some anti-TNF and other pathways; paradoxical inflammation is a known clinic conversation, not a personal failure. None of these labels are DIY diagnoses. A dermatologist familiar with IBD medicines and an IBD clinician who knows your drug history should share the story.

Timing is one of your best clues. Did the skin change within days of a steroid burst, a new induction dose, or a biologic class switch? Did it appear after months of stable maintenance? Did antibiotics for a fistula or pouchitis precede it? Write a one-page timeline: drug names, dates, skin onset, itch versus pain, distribution, and whether gut symptoms moved in parallel. Bring prior photos. Clinics make better decisions with a timeline than with "my skin has been crazy."

When is skin an urgent problem? Rapidly spreading painful ulcers, fever with rash, facial swelling, trouble breathing, blistering that looks like a burn, eye involvement, or skin breaking down over joints needs same-day care—ER or urgent dermatology depending on severity. Do not wait for the next infusion nurse visit. For itchy but stable patches, same-week primary care or dermatology triage plus a message to your GI team is usually the path.

Do not stop your IBD drug the night a pimple cluster appears. Abrupt cessation can jeopardize gut remission. Ask whether the plan is topical care, a dermatology referral, a temporary bridge, lab checks, or—only if specialists agree—a class change. Sometimes the gut is quiet and the skin still needs separate treatment. Sometimes bowel and skin flare together as extraintestinal activity. Sometimes the "acne" is steroid-related and improves as the taper continues under supervision.

Infection risk deserves respect on immunosuppression. What looks like acne can occasionally be folliculitis or another infection. What looks like eczema can be superinfected. If lesions are warm, draining, or exquisitely tender, say so. Avoid borrowing someone else’s oral steroid cream pack without guidance, especially on the face.

Lifestyle supports are adjuncts, not cures: gentle cleansers, fragrance-light moisturizers, not picking, sun care that matches your photosensitivity risk, and nutrition adequate in protein and micronutrients while you heal. If you are exploring diet changes for skin, keep IBD realities in view—extreme elimination during active gut disease can backfire. Makeup and "skin cycling" trends are optional; barrier repair and clinician-directed treatment are not.

Body image after steroids, weight change, or visible rash is part of IBD care even when labs look fine. If skin changes are keeping you from work, school, or intimacy, say that plainly. Quality-of-life impact can justify faster dermatology access.

Ask your team these questions at the next contact: Is this a known reaction pattern for my medicine? Do I need dermatology now or watchful waiting? Could this be paradoxical inflammation, infection, steroid effect, or an extraintestinal manifestation? If we change therapy, what is the gut monitoring plan during the switch? Should I pause any nonessential supplements that worsen acne?

Related education: [Extraintestinal manifestations](/blog/ibd-extraintestinal-manifestations), [Pyoderma and erythema nodosum](/blog/pyoderma-erythema-nodosum-ibd), [Joint aches, eyes, and skin Q&A](/ask/joint-aches-eye-pain-skin-ibd), and [Understanding biologics](/blog/understanding-biologics-ibd).
'''.strip()


A19 = r'''
Surgery can be life-changing and medically necessary. It is not a magic eraser that guarantees "cured forever" for every person with inflammatory bowel disease. The honest answer depends on which disease you have, which operation you had, and what "cure" means to you—no more colon, no more symptoms, or no chance of future inflammation anywhere.

Ulcerative colitis primarily affects the colon and rectum. When the entire colon and rectum are removed, the original UC disease target is gone. Many people do extremely well after restorative proctocolectomy with ileal pouch–anal anastomosis (J-pouch) or after a permanent ileostomy. That said, pouches can develop pouchitis—inflammation of the pouch—with urgency, frequency, and discomfort that feel painfully familiar. Some people develop cuffitis in remaining rectal tissue. A smaller group is later recognized as Crohn's disease of the pouch when the pattern does not behave like simple pouchitis. So even after "the colon is gone," inflammation can still need antibiotics, advanced therapy, or further procedures. Calling UC surgery a cure is shorthand that leaves out pouchitis and quality-of-life work.

Crohn's disease can involve any part of the GI tract. Removing a diseased segment—or diverting stool with an ostomy—treats complications like obstruction, abscess, fistula, or refractory colitis. It does not remove the immune tendency that defines Crohn's. Inflammation can return at the anastomosis, in the small bowel, in the perineum, or elsewhere. Ostomy surgery can dramatically improve life when disease or complications demand it, and many people thrive with a stoma. It is still Crohn's afterward, which means ongoing surveillance, medication decisions, and nutrition planning remain part of care for a large share of patients.

What should you ask before surgery so expectations are clear? What is the primary goal—cancer risk, refractory bleeding, dysplasia, toxic colitis, stricture, fistula, or medication failure? Is the plan a temporary diversion, a permanent stoma, or a pouch reconstruction in stages? What are pouchitis rates and Crohn's-of-the-pouch discussions in your center’s experience? Who will manage pouch care long term? What sexual function, fertility, body-image, and return-to-work counseling is available? Surgery teams that answer these without hype are doing you a favor.

After a J-pouch, learn the difference between expected adaptation and warning signs. Early months often mean frequent stools while the pouch learns capacity. Escalating blood, night accidents that worsen after a stable baseline, fever, dehydration, or obstruction symptoms need prompt contact. After an ostomy, learn appliance fit, high-output rules, skin care, and when output volume or consistency changes signal dehydration or active disease. High-output ileostomy is a medical issue, not a personal failure at "getting used to it."

Medications after surgery are not a moral judgment. Some people need prophylaxis or continued advanced therapy based on risk factors. Others step down under close watch. Do not stop medicines because surgery "should have finished this." Confirm the plan in writing: who checks calprotectin, who scopes the pouch, who adjusts therapy if pouchitis repeats.

Emotionally, the word "cure" can create loneliness when symptoms persist. You are not ungrateful for wanting relief and still needing care. Peer ostomy and pouch nurses, wound-ostomy-continence specialists, and IBD mental health support help as much as surgical technique for long-term living. Partners and family members need education too so they do not treat every bathroom trip as catastrophe or, conversely, ignore dehydration.

If you are deciding between pouch and permanent ostomy, there is no universal winner. Body anatomy, sphincter function, prior surgeries, fertility plans, and personal preference all matter. Second opinions at high-volume IBD surgery centers are reasonable for big irreversible choices. Bring a written list of must-have outcomes: fewer hospitalizations, ability to work, intimacy goals, athletic goals, and travel plans. Surgeons can only match a plan to goals you name.

Travel, swimming, and intimacy after pouch or ostomy are possible for many people with planning—appliance choice, backup supplies, and honest conversation. Isolation after surgery is common and treatable with peer support; it is not proof that surgery failed.

Related education: [J-pouch basics](/blog/j-pouch-basics-ibd), [Ostomy basics](/blog/ostomy-basics-ibd), [ICN pediatric ostomy toolkit](/blog/icn-ostomy-toolkit-pediatric), and [Swimming and activity with an ostomy](/blog/swimming-pool-beach-ibd-ostomy).
'''.strip()


ITEMS = [
    {
        "id": 15,
        "slug": "glp-1-ozempic-mounjaro-ibd-diarrhea-nausea",
        "title": "Will a GLP-1 like Ozempic or Mounjaro make IBD diarrhea or nausea worse?",
        "answer": A15,
    },
    {
        "id": 16,
        "slug": "iv-biologic-to-home-injection-insurance",
        "title": "Can I switch from an IV biologic infusion to a home injection of the same drug?",
        "answer": A16,
    },
    {
        "id": 17,
        "slug": "calprotectin-down-still-liquid-stools-ibs-or-flare",
        "title": "If calprotectin drops but I still have liquid stools, is it IBS instead of an IBD flare?",
        "answer": A17,
    },
    {
        "id": 18,
        "slug": "acne-eczema-on-advanced-ibd-therapy",
        "title": "Severe acne or eczema on advanced IBD therapy: drug side effect or another autoimmune issue?",
        "answer": A18,
    },
    {
        "id": 19,
        "slug": "j-pouch-ostomy-cure-or-inflammation-return",
        "title": "Does a J-pouch or ostomy cure IBD, or can inflammation return?",
        "answer": A19,
    },
]


def expand_to_target(base: str, topic_extra: list[str]) -> str:
    """Append educational paragraphs until near ~10 min / char cap."""
    text = base.strip()
    extras = list(topic_extra)
    i = 0
    while words(text) < TARGET_WORDS - 40 and len(text) < MAX_CHARS - 400 and i < len(extras):
        candidate = text + "\n\n" + extras[i].strip()
        if len(candidate) > MAX_CHARS:
            break
        text = candidate
        i += 1
    # If still short, repeat soft educational reminders carefully without inventing claims
    pad_idx = 0
    pads = [
        "This page is general education for people navigating Crohn's disease and ulcerative colitis. It cannot replace an exam, labs ordered for you, or a therapy plan written by your gastroenterologist.",
        "If two clinicians give conflicting advice about the same symptom cluster, ask them to coordinate—or request a short case conference note in your portal—so you are not stuck translating between clinics alone.",
        "Keep a one-page current medication list in your phone photos: dose, route, last administration date, pharmacy phone, and allergy list. Bring it to every urgent visit.",
        "When symptoms escalate, lead with function: sleep interrupted, missed work or school, inability to keep fluids, new blood, or dizziness. Function statements help triage faster than vague 'I feel awful' alone.",
    ]
    while words(text) < TARGET_WORDS - 20 and len(text) < MAX_CHARS - 250:
        candidate = text + "\n\n" + pads[pad_idx % len(pads)]
        if len(candidate) > MAX_CHARS:
            break
        text = candidate
        pad_idx += 1
        if pad_idx > 12:
            break
    return text[:MAX_CHARS]


EXTRA = {
    15: [
        "Dose day routines help some people: inject at a consistent time, eat a smaller lower-fat meal beforehand, and keep oral rehydration options nearby if nausea has been an issue. If a dose was missed, follow the product instructions and your prescriber's rule—do not double up to catch up unless told to.",
        "Shared decision making should include your personal flare cost. If a prior flare put you in hospital, your threshold for checking calprotectin after messy GLP-1 weeks may be lower than someone with mild stable colitis. That is appropriate personalization, not overreaction.",
        "Watch for dehydration clues that get misread as just IBD fatigue: dry mouth, dark urine, lightheadedness on standing, and rising heart rate. GLP-1 nausea plus diarrhea can stack fluid losses quickly.",
        "If you use cannabis, alcohol, or other substances to cope with nausea, tell your clinicians. Interactions and masking of warning symptoms matter on immunosuppression.",
        "Adolescents and young adults on GLP-1 medicines need growth, bone, and nutrition monitoring conversations that adult weight-loss clinics sometimes skip. Bring your IBD dietitian into that discussion early.",
        "Travel with pens requires cooling plans and documentation. Do not leave devices in a hot car. If security questions refrigerated medication, a clinician letter plus original labeled packaging usually helps.",
        "If gallbladder-type pain, persistent vomiting, or severe upper abdominal pain appears, seek urgent evaluation. Do not assume every abdominal pain on a GLP-1 is 'normal IBD gas.'",
        "Ask whether anti-nausea strategies used for chemotherapy or migraine clinics are appropriate for you during titration—never borrow someone else's prescription.",
        "Weight-loss goals should be written beside IBD goals so one clinic does not celebrate scale changes while the other is quietly worried about malnutrition or muscle loss.",
        "If diarrhea improves only on days you barely eat, that is not remission—it may be reduced intake. Tell your team how little you are eating before they attribute improvement to the wrong cause.",
    ],
    16: [
        "Ask whether nurse visits for the first home doses are covered. A supervised first injection can catch technique errors before a whole maintenance cycle is compromised.",
        "If you have needle fear, say so before the switch is locked in. Some people do better with autoinjectors, clinic administration, or a slower desensitization plan than with a sudden move home.",
        "Document every shipment delay with dates. Appeals and manufacturer escalations move faster with a paper trail than with memory alone.",
        "Clarify who adjusts intervals if you flare after switching routes. Sometimes teams intensify monitoring without abandoning the molecule; sometimes they reverse to IV temporarily.",
        "For multi-dose pens or staggered schedules, put reminders in two places—phone and paper calendar—so a single dead battery does not equal a missed dose.",
        "If your specialty pharmacy changes mid-year because of insurance networks, request a warm handoff of remaining refills and prior-auth reference numbers.",
        "Compare your out-of-pocket estimate for a year of infusions versus a year of pens before you commit emotionally to leaving the chair. Convenience is valuable, but surprise pharmacy deductibles are a common reason people abandon an otherwise good drug.",
        "If you receive infusions through a hospital outpatient department, site-of-care policies may push you toward home or lower-cost sites anyway. Ask whether the subcut switch is being driven by clinical preference, payer policy, or both—so you can advocate for the reason that matches your goals.",
        "Cold-chain mistakes happen: pens left on a warm counter, frozen in a bad fridge pocket, or shipped in a heat wave. Ask the specialty pharmacy what temperature excursions require a replacement pen rather than guessing.",
        "Care plans should include a missed-dose algorithm for weekends and holidays when clinics are closed. Write it down while you are calm, not while you are staring at an empty fridge at 9 p.m. Sunday.",
        "If antibodies or drug levels guided your IV dosing, ask whether those labs still matter after a route change and when they should be redrawn.",
        "Employer leave policies sometimes cover infusion days but not training visits for home injections. Ask your clinic for a work letter that explains medical necessity of training time.",
    ],
    17: [
        "Ask whether your assay reports an exact number or a capped high value. Trends are easier when methods stay consistent across draws.",
        "Night stools remain a useful discriminator for many people. Meal-related daytime looseness with quiet nights and no blood can still be miserable, but it often points the workup differently than nocturnal inflammatory patterns.",
        "Pelvic floor dysfunction after years of urgency can perpetuate incomplete emptying and secondary soiling. Referral to specialty pelvic PT is not giving up on IBD care.",
        "If you recently completed antibiotics, ask about infection testing before escalating IBD therapy for loose stools alone.",
        "Post-meal urgency within 30 to 60 minutes can fit bile acid or IBS patterns; constant all-day liquidity with cramping and blood leans more inflammatory—but overlap exists, which is why teams combine history with tests.",
        "Children and teens may under-report bathroom frequency at school. Ask about hallway passes, accidents, and avoided cafeteria foods before concluding symptoms are mild.",
        "A single reassuring calprotectin does not cancel a pending colonoscopy if dysplasia surveillance or stricture assessment was already planned. Keep surveillance on the calendar unless your clinician reschedules it for a documented reason.",
        "If you track symptoms in IBDPal or another log, export or screenshot the week around the stool test. Matching the biomarker day to real life prevents arguments based on memory alone.",
        "Lactose, caffeine, and sugar alcohols are frequent quiet culprits after inflammation improves and people liberalize diet. Reintroduce one change at a time for a few days rather than celebrating with a full 'trigger buffet.'",
        "Ask whether bile acid diarrhea testing or empiric therapy is appropriate after ileal disease—even when calprotectin is improved. Missing that diagnosis leads people to escalate IBD drugs unnecessarily.",
        "Sexual activity, menses, and intense exercise can change bowel patterns without proving flare. Note those contexts in your diary so clinicians can interpret spikes fairly.",
        "If you are grieving the idea that 'quiet labs should equal quiet bowels,' say that out loud. Expectations management is part of recovery after a hard inflammatory year.",
    ],
    18: [
        "Photograph rashes in similar lighting over several days. Progression speed helps dermatology triage more than a single filtered selfie.",
        "Tell clinicians about biotin, collagen, and hormone supplements; some affect labs or acne patterns and are easy to forget on medication lists.",
        "If you wear adhesives for glucose monitors, ostomy appliances, or sensors, mention contact dermatitis history so teams do not confuse adhesive allergy with drug rash.",
        "Scalp, nails, and skin folds can be involved in some inflammatory patterns. Mention them even if you came in only for face acne.",
        "After starting isotretinoin or other systemic dermatology drugs, ensure GI is aware—coordination prevents two specialists from missing shared toxicity monitoring.",
        "Workplace or school appearance concerns are valid disability and accommodation topics when skin disease is severe. Ask social work or patient navigation for documentation help if needed.",
        "Steroid rebound acne can appear while the gut is actually improving. That timing mismatch confuses people into thinking the biologic failed when the steroid curve is the real story.",
        "Moisturize within minutes after bathing to lock water into the barrier. Fancy products are optional; consistent bland emollients are not, especially on immunosuppression when scratching raises infection risk.",
        "If a rash started after a new detergent, fragrance, or nickel-heavy jewelry, say so. Not every skin event on a biologic is caused by the biologic.",
        "Ask whether you need eye review if eyelids or periocular skin are involved—ocular inflammation and periocular dermatitis are different problems with different urgency.",
        "Keep a list of topicals already tried and whether they burned, helped, or stained clothing. Dermatology visits go faster with that list.",
        "Mental health support for visible disease is not vanity care. Persistent shame about skin can reduce adherence to the gut therapy that is keeping you out of hospital.",
    ],
    19: [
        "Ask how emergency departments in your region should be told you have a pouch or ostomy so teams avoid contraindicated exams or unnecessary delays.",
        "Nutrition after colectomy or small-bowel resection may permanently change B12, iron, hydration, and bile acid handling. Schedule lab calendars before you feel depleted.",
        "Sexual function and body image after pelvic surgery deserve planned follow-up, not only a pamphlet on discharge day. Ask who owns that referral.",
        "If pouchitis becomes recurrent, ask about evaluation for Crohn's of the pouch versus idiopathic pouchitis before cycling endless short antibiotic courses without a longer strategy.",
        "Ostomy output tracking for a few days after any major diet change helps catch high output early. Know your personal call-if-above-this-volume number from the surgical team.",
        "Reoperation rates and pouch failure are uncomfortable statistics, but high-volume centers discuss them openly. Prefer clarity over reassurance theater.",
        "Temporary loop ileostomies are not 'less serious' surgery. Dehydration and electrolyte shifts can still send people back to the ER if output teaching is incomplete.",
        "Ask about staged surgeries and what life looks like between stages—appliance supplies, wound care, work leave, and who to call at 2 a.m.",
        "Pouch patients should know their baseline 24-hour stool frequency after adaptation. A sudden jump from that baseline is more meaningful than comparing yourself to someone else's 'normal.'",
        "If you were told surgery would end medication forever and then you still need therapy, that is a planning mismatch—not a personal failure. Ask for a written post-op medication philosophy.",
        "Sports, pregnancy planning, and travel each interact with pouch or ostomy anatomy differently. Bring those life goals into pre-op visits so the operation chosen matches the life you want.",
        "Peer visitors and ostomy nurses often teach appliance tricks surgeons do not have time to cover. Request that referral before discharge, not three months into skin breakdown.",
    ],
}


def main() -> None:
    env = read_env(SERVER_ENV)
    url = os.environ.get("DATABASE_URL") or env.get("DATABASE_URL")
    if not url:
        raise SystemExit("No DATABASE_URL")

    published = []
    for item in ITEMS:
        answer = expand_to_target(item["answer"], EXTRA[item["id"]])
        if len(answer) < 40 or len(answer) > MAX_CHARS:
            raise SystemExit(f"bad length id={item['id']} len={len(answer)}")
        item = {**item, "answer": answer}
        published.append(
            {
                "id": item["id"],
                "slug": item["slug"],
                "title": item["title"],
                "chars": len(answer),
                "words": words(answer),
                "min": approx_minutes(answer),
            }
        )

    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()
    for item in ITEMS:
        answer = expand_to_target(item["answer"], EXTRA[item["id"]])
        cur.execute(
            """
            UPDATE ibdpal_reader_questions
            SET title = %s,
                answer_text = %s,
                slug = %s,
                status = 'answered',
                published_at = COALESCE(published_at, NOW()),
                updated_at = NOW()
            WHERE question_id = %s
            RETURNING question_id, slug, status, published_at
            """,
            (item["title"], answer, item["slug"], item["id"]),
        )
        row = cur.fetchone()
        if not row:
            raise SystemExit(f"missing id {item['id']}")
        print(
            json.dumps(
                {
                    "id": row[0],
                    "slug": row[1],
                    "status": row[2],
                    "published_at": row[3].isoformat() if row[3] else None,
                    "chars": len(answer),
                    "words": words(answer),
                    "approx_min_read": approx_minutes(answer),
                    "url": f"/ask/{row[1]}",
                }
            )
        )

    cur.execute(
        "SELECT status, COUNT(*)::int FROM ibdpal_reader_questions GROUP BY status ORDER BY 2 DESC"
    )
    print("counts", cur.fetchall())
    cur.execute("SELECT COUNT(*) FROM ibdpal_reader_questions WHERE status = 'new'")
    print("remaining_new", cur.fetchone()[0])
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
