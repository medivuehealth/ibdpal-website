#!/usr/bin/env python3
# Prose style: do not use em dash.
"""Generate Nov 21 2026 index-gap blogs: TDM, biologic failure, med monitoring,
insurance appeal toolkit, treatment comparison, post-surgery 30 days,
pathology report, clinical trials decision guide."""
from __future__ import annotations

import json
import shutil
import ssl
import sys
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
SEARCH_GAP = ROOT / "data" / "search-gap-posts.json"
ALIASES = ROOT / "data" / "search-aliases.json"
VERCEL = ROOT / "vercel.json"
SITEMAP = ROOT / "sitemap.xml"
FALLBACK = BLOGS / "assets" / "biologics-basics" / "biologics_1.jpg"
SITE = "https://www.ibdpal.org"

sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402

DATE_ISO = "2026-11-21T22:00:00Z"
DATE_DISPLAY = "November 21, 2026"
MIN_WORDS = 850

IMAGE_URLS = {
    "therapeutic-drug-monitoring-ibd": (
        "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&w=1200&q=80"
    ),
    "when-ibd-biologic-stops-working": (
        "https://images.unsplash.com/photo-1584820927498-cfe5211fd8bf?auto=format&w=1200&q=80"
    ),
    "ibd-medication-monitoring-checklist": (
        "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&w=1200&q=80"
    ),
    "ibd-insurance-denial-appeal-toolkit": (
        "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?auto=format&w=1200&q=80"
    ),
    "ibd-treatment-comparison-guide": (
        "https://images.unsplash.com/photo-1587854692152-cbe660dbde88?auto=format&w=1200&q=80"
    ),
    "after-ibd-surgery-first-30-days": (
        "https://images.unsplash.com/photo-1516549655169-df83a0774514?auto=format&w=1200&q=80"
    ),
    "understanding-ibd-pathology-report": (
        "https://images.unsplash.com/photo-1582719471384-894fbb16e074?auto=format&w=1200&q=80"
    ),
    "ibd-clinical-trials-patient-decision-guide": (
        "https://images.unsplash.com/photo-1576091160550-2173dba999ef?auto=format&w=1200&q=80"
    ),
}


def word_count(html_body: str) -> int:
    text = html_body
    for tag in ("</p>", "</li>", "</h2>", "</h3>"):
        text = text.replace(tag, " ")
    out = []
    in_tag = False
    for ch in text:
        if ch == "<":
            in_tag = True
            continue
        if ch == ">":
            in_tag = False
            continue
        if not in_tag:
            out.append(ch)
    return len("".join(out).split())


def download_image(url: str, dest: Path) -> bool:
    try:
        ctx = ssl.create_default_context()
        req = urllib.request.Request(url, headers={"User-Agent": "IBDPalBot/1.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=40) as resp:
            data = resp.read()
        if len(data) < 1000:
            return False
        dest.write_bytes(data)
        return True
    except Exception as exc:  # noqa: BLE001
        print("image fail", dest.name, exc)
        return False


def ensure_image(post: dict) -> None:
    asset = BLOGS / "assets" / post["asset_dir"]
    asset.mkdir(parents=True, exist_ok=True)
    dest = asset / post["images"][0]
    if dest.exists() and dest.stat().st_size >= 1000:
        return
    url = IMAGE_URLS.get(post["asset_dir"])
    if url and download_image(url, dest):
        print("downloaded", dest.name)
        return
    if FALLBACK.exists():
        shutil.copy(FALLBACK, dest)
        print("fallback", dest.name)


POSTS: list[dict] = [
    {
        "slug": "therapeutic-drug-monitoring-ibd",
        "title": "Therapeutic Drug Monitoring in IBD: Drug Levels and Antibodies Explained",
        "description": (
            "Therapeutic drug monitoring (TDM) for IBD biologics: trough levels, "
            "antidrug antibodies, proactive vs reactive testing, and clinic questions. Education only."
        ),
        "category": "Treatment · November 2026",
        "date_display": DATE_DISPLAY,
        "date_iso": DATE_ISO,
        "asset_dir": "therapeutic-drug-monitoring-ibd",
        "images": ["therapeutic-drug-monitoring-ibd_1.jpg"],
        "alts": ["Clinician reviewing lab results for IBD biologic monitoring education"],
        "share": "TDM for IBD biologics: drug levels and antibodies in plain language. Education only.",
        "resource_category": "treatment",
        "match_terms": [
            "therapeutic drug monitoring",
            "tdm ibd",
            "biologic drug levels",
            "antidrug antibodies",
            "drug level biologic",
            "infliximab level",
            "adalimumab level",
            "antibody to biologic",
        ],
        "tags": [
            "TDM",
            "therapeutic drug monitoring",
            "biologics",
            "antibodies",
            "drug levels",
            "Crohn's",
            "colitis",
            "treatment",
        ],
        "body": """
<p>People searching <strong>therapeutic drug monitoring</strong>, <strong>drug levels</strong>, or <strong>antidrug antibodies</strong> usually want to understand why their clinic draws blood around biologic infusions or injections. This page explains the ideas in plain language for Crohn's disease and ulcerative colitis. It is education only, not a lab order or dosing plan.</p>
<p>Pair this with <a href="/blog/understanding-biologics-ibd">understanding biologics</a>, <a href="/blog/starting-biologic-first-12-weeks">starting a biologic</a>, and <a href="/blog/when-ibd-biologic-stops-working">when a biologic stops working</a>.</p>

<h2>What therapeutic drug monitoring means</h2>
<p><strong>Therapeutic drug monitoring (TDM)</strong> means measuring how much biologic medicine is in your blood (often called a trough level) and sometimes checking whether your immune system has made antibodies against that medicine. Clinics use the results with symptoms, calprotectin, endoscopy, and imaging. A single number rarely decides everything.</p>

<h2>Trough levels in everyday words</h2>
<p>A trough is the lowest medicine level just before the next dose. Timing matters. Drawing the lab on the wrong day can look artificially high or low. Ask your nurse when to schedule the blood draw relative to your infusion or injection.</p>
<ul class="blog-list">
<li><strong>Higher levels</strong> may support keeping the current dose if you feel well and objective inflammation is quiet</li>
<li><strong>Lower levels</strong> may prompt questions about missed doses, rapid clearance, or dose interval changes</li>
<li><strong>Target ranges</strong> differ by drug, assay, and clinical goal. Do not copy a number from a forum</li>
</ul>

<h2>Antidrug antibodies</h2>
<p>Some people develop antibodies that bind the biologic. Antibodies can lower drug levels or contribute to infusion reactions for certain medicines. Not every antibody means the drug has failed. Your gastroenterologist interprets antibody results with the drug level and your clinical story.</p>

<h2>Proactive versus reactive TDM</h2>
<ul class="blog-list">
<li><strong>Reactive TDM:</strong> testing when symptoms return, labs worsen, or a scope looks inflamed</li>
<li><strong>Proactive TDM:</strong> scheduled checks even when you feel better, to catch low levels early</li>
</ul>
<p>Neither approach replaces communication. Bring a symptom and dose log. Note any delayed injections, insurance gaps, or infections.</p>

<h2>Common myths</h2>
<ul class="blog-list">
<li><strong>"A low level always means I failed the drug."</strong> Sometimes the dose, interval, or adherence is the first conversation.</li>
<li><strong>"Antibodies mean I can never use that class again."</strong> Decisions depend on the antibody type, drug level, and alternatives. Ask your team.</li>
<li><strong>"TDM replaces scopes and calprotectin."</strong> Monitoring is a package, not a single blood test.</li>
</ul>

<h2>Questions for your gastroenterologist</h2>
<ul class="blog-list">
<li>Are we using proactive or reactive TDM for my biologic?</li>
<li>When should I draw the trough relative to my next dose?</li>
<li>What would change if my level is low with or without antibodies?</li>
<li>How do TDM results fit with my calprotectin and last endoscopy?</li>
</ul>

<h2>How IBDPal can help visits</h2>
<p>Log dose dates, delayed fills, symptoms, and infection days. Bring that timeline when TDM labs return. Patterns make it easier to separate missed doses from true pharmacokinetic issues.</p>

<h2>When to seek prompt care</h2>
<p>Contact your clinic for severe abdominal pain, high fever, heavy bleeding, or signs of a serious reaction during or after an infusion. TDM education cannot triage emergencies. See <a href="/flare-help">flare help</a> and <a href="/blog/when-to-go-er-ibd">when to go to the ER</a>.</p>

<p>Related reading: <a href="/blog/insurance-biologics-ibd">insurance and biologics</a> · <a href="/blog/prior-authorization-biologics-timeline">prior authorization timeline</a> · <a href="/guides/biologics-crohns-colitis">biologics guide</a>.</p>
<p>Education supports shared decisions. It does not replace your gastroenterologist. Ask for the exact assay name and timing instructions before comparing your results with anyone else's numbers online.</p>
<p>Kids and teens may need different targets and scheduling. Pediatric IBD teams set those plans. Bring caregivers to the TDM conversation when dose changes affect school or sports.</p>
<p>If your insurer delays a refill and your trough looks low, tell the clinic. Coverage gaps are clinical data, not a personal failure.</p>


<h2>How TDM fits with other IBD monitoring</h2>
<p>Drug levels are one slice of the monitoring pie. Clinics also watch symptoms, stool frequency, rectal bleeding scores, calprotectin or other stool markers, blood counts, C-reactive protein, imaging, and endoscopy. A person can feel better while inflammation continues quietly, or feel miserable while labs look quiet because of IBS-like symptoms, bile acid diarrhea, strictures, or infection. That is why teams rarely treat a trough number in isolation.</p>
<p>If your calprotectin rises and your trough is low, the conversation may focus on exposure and adherence. If calprotectin rises and your trough is solid without antibodies, the conversation may shift toward true inflammatory breakthrough or another mechanism. If you feel worse but objective markers are calm, the team may look for non-inflammatory causes before declaring drug failure.</p>

<h2>Assay differences patients should know exist</h2>
<p>Not every lab measures biologic levels the same way. Homogeneous mobility shift assays, ELISA-based tests, and other platforms can report numbers that are not interchangeable. Some reports include free drug, some handle antibodies differently, and reference ranges vary. If you change hospitals or specialty pharmacies, bring the prior report with the assay name printed on it. Asking "is this the same assay we used last time?" is a fair question.</p>
<p>Timing instructions also differ by medicine. An infusion trough is usually drawn immediately before the next infusion. Injection timing may depend on whether you inject every other week or every week. Drawing early because it was convenient for work can create a misleadingly high level. Drawing late after a missed dose can look like rapid clearance when the real story was a coverage gap.</p>

<h2>Missed doses, gaps, and "low level" stories</h2>
<p>Insurance interruptions, specialty pharmacy shipping delays, travel, fear of side effects, and cost-sharing surprises all create gaps. A low trough after a gap does not always mean your body clears the drug unusually fast. Tell the clinic the truth about delayed doses. Honest timelines protect you from unnecessary switches and help the team decide whether to re-induce, shorten intervals, or investigate antibodies.</p>
<p>Combination therapy with an immunomodulator is sometimes used to reduce immunogenicity for certain biologics. That decision involves infection risk, cancer history, age, and preference. TDM results may inform whether combination therapy is still adding value. Do not start or stop an immunomodulator based on a forum post about antibodies.</p>

<h2>What TDM usually does not do</h2>
<ul class="blog-list">
<li>It does not diagnose Crohn's versus ulcerative colitis</li>
<li>It does not replace cancer surveillance colonoscopy timing</li>
<li>It does not prove a food trigger</li>
<li>It does not justify stopping therapy the day a number looks "good enough"</li>
</ul>
<p>Some people want to space doses after a reassuring level. Dose changes belong to the prescribing clinician because disease history and endoscopy matter as much as pharmacokinetics.</p>

<h2>Practical visit prep for TDM results day</h2>
<p>Print or screenshot the lab PDF. Circle the collection date and time. Write your last dose date and time next to it. Note any infections, antibiotics, new vaccines, or hospital stays since the prior level. List symptoms with dates rather than a single adjective like "worse." If you use IBDPal, export or summarize dose and symptom streaks for the same window.</p>
<p>Ask whether the result will be reviewed by a nurse protocol, pharmacist, or physician, and how you will hear about changes. Portal silence after an abnormal antibody result is a common frustration. Agree on a follow-up rule before you leave the lab draw.</p>

<h2>Special situations</h2>
<p>During a severe flare requiring hospitalization, teams may prioritize stabilizing disease over waiting for outpatient TDM logistics. In pregnancy, monitoring goals and medicine choices can differ. In pediatrics, weight-based dosing and assay availability vary. After surgery, drug plans may pause or restart on a surgical timeline that is separate from your old infusion calendar.</p>
<p>If you previously had an infusion reaction, tell every new infusion center. Antibody history and reaction history should travel with you between health systems.</p>

<h2>Bottom line for patients</h2>
<p>Therapeutic drug monitoring is a conversation tool. Trough levels and antibodies help explain exposure and immunogenicity. They work best beside symptoms, stool markers, scopes, and a truthful dose timeline. Bring questions, bring dates, and ask what decision the result will support. Education prepares you for that visit. Your gastroenterologist still owns the plan.</p>

<h2>Clinic script you can copy</h2>
<p>"I want to understand therapeutic drug monitoring for my biologic. Please explain my trough level, any antibodies, when to redraw, and what options you are considering if the level is low."</p>
""",
    },
    {
        "slug": "when-ibd-biologic-stops-working",
        "title": "What Happens When an IBD Biologic Stops Working?",
        "description": (
            "Primary nonresponse and secondary loss of response to IBD biologics: "
            "what those terms mean, TDM questions, and next-step conversations. Education only."
        ),
        "category": "Treatment · November 2026",
        "date_display": DATE_DISPLAY,
        "date_iso": DATE_ISO,
        "asset_dir": "when-ibd-biologic-stops-working",
        "images": ["when-ibd-biologic-stops-working_1.jpg"],
        "alts": ["Patient discussing IBD treatment options with a clinician"],
        "share": "When an IBD biologic stops working: primary vs secondary loss of response. Education only.",
        "resource_category": "treatment",
        "match_terms": [
            "biologic stops working",
            "loss of response biologic",
            "secondary loss of response",
            "primary nonresponse",
            "biologic failing",
            "biologic not working anymore",
            "switch biologic crohn",
        ],
        "tags": [
            "biologics",
            "loss of response",
            "nonresponse",
            "treatment",
            "Crohn's",
            "colitis",
        ],
        "body": """
<p>Searches like <strong>biologic stops working</strong> or <strong>loss of response</strong> are common after months or years on therapy. Feeling worse again is frightening. This page explains the language clinics use and the questions that help visits stay concrete. It is not advice to stop or switch medicines on your own.</p>
<p>Pair this with <a href="/blog/therapeutic-drug-monitoring-ibd">therapeutic drug monitoring</a>, <a href="/blog/understanding-biologics-ibd">understanding biologics</a>, and <a href="/blog/ibd-treatment-comparison-guide">treatment comparison guide</a>.</p>

<h2>Primary nonresponse versus secondary loss of response</h2>
<ul class="blog-list">
<li><strong>Primary nonresponse:</strong> the medicine never clearly helped after an adequate trial</li>
<li><strong>Secondary loss of response:</strong> the medicine helped for a while, then symptoms or objective inflammation returned</li>
</ul>
<p>Those labels guide what your team investigates next. They are not judgments about your effort.</p>

<h2>What clinics check before calling a drug a failure</h2>
<ul class="blog-list">
<li>Are doses arriving on time? Insurance delays matter.</li>
<li>Is inflammation confirmed with calprotectin, imaging, or endoscopy?</li>
<li>Could infection, bile acid diarrhea, strictures, or IBS-like symptoms mimic a flare?</li>
<li>Do drug levels and antibodies (TDM) suggest low exposure or immunogenicity?</li>
</ul>

<h2>Possible next-step conversations</h2>
<p>Depending on findings, teams may discuss optimizing the current drug, bridging with other therapies short term, switching within a class, changing mechanism, or surgery evaluation. There is no universal order that fits every patient. Ask what evidence supports each option for your disease location and history.</p>

<h2>Questions worth bringing</h2>
<ul class="blog-list">
<li>Do my symptoms match active inflammation or another cause?</li>
<li>Should we check drug level and antibodies before switching?</li>
<li>If we switch, what is the plan for bridging and infection screening?</li>
<li>How will we measure success at 8 to 16 weeks?</li>
</ul>

<h2>Emotional load is real</h2>
<p>Losing response after a hard-won remission can feel like starting over. Ask about nurse educator support, Foundation resources, and mental health care. Logging with IBDPal can make the "what changed" story clearer at the next visit.</p>

<h2>When to seek prompt care</h2>
<p>Seek urgent evaluation for severe pain, persistent vomiting, high fever, dehydration, or heavy bleeding. Drug-failure education cannot replace emergency assessment. See <a href="/flare-help">flare help</a>.</p>

<p>Related reading: <a href="/blog/starting-biologic-first-12-weeks">first 12 weeks on a biologic</a> · <a href="/blog/insurance-biologics-ibd">insurance and biologics</a> · <a href="/blog/ibd-insurance-denial-appeal-toolkit">appeal toolkit</a>.</p>
<p>Education supports shared decisions. It does not replace your gastroenterologist. Never stop a biologic abruptly without a clinic plan, especially if you use steroids or combination therapy.</p>
<p>If symptoms return during pregnancy planning or pregnancy itself, call your IBD team early. Medication choices may differ from non-pregnant plans.</p>
<p>Bring a one-page timeline: when you felt best, when symptoms returned, dose dates, and recent labs. That timeline is more useful than a vague "it stopped working."</p>


<h2>Why "stopped working" needs a definition</h2>
<p>Patients often say a biologic stopped working when urgency returned, fatigue crashed, joint pain flared, or a scope looked worse. Clinicians usually want a clearer definition: are we talking clinical symptoms, biochemical markers, endoscopic healing, or all three? You can help by bringing specifics. "I went from one formed stool to eight watery stools with blood over three weeks" is more actionable than "it is not working."</p>
<p>Also separate steroid dependence from biologic failure. If you only feel well on repeated prednisone while the biologic continues in the background, that pattern still deserves a structured review. It may still be loss of response, incomplete response, or a dosing problem. Naming the pattern accurately changes the next test.</p>

<h2>Mechanistic versus pharmacokinetic problems</h2>
<p>In plain language, two broad stories appear often. In a pharmacokinetic story, not enough active drug is available. Causes include antibodies, rapid clearance from high inflammation, missed doses, or an interval that is too long for your body. In a mechanistic story, plenty of drug is present, but the disease is driven by pathways the medicine does not control well enough anymore. Therapeutic drug monitoring helps sort those stories. It does not answer every question alone.</p>
<p>That sorting matters because the next step differs. Low levels may lead to optimization discussions. Therapeutic levels with ongoing inflammation may lead to switching mechanism discussions. Treating every flare as "need a new drug tomorrow" can skip useful optimization. Treating every low level as "antibodies ruined everything" can skip adherence and access fixes.</p>

<h2>Confirm inflammation before major switches</h2>
<p>Infections such as C. difficile, viral gastroenteritis, and other GI infections can mimic flares. Strictures can cause pain and obstructive symptoms without the same lab pattern as mucosal inflammation. Bile acid diarrhea after ileal resection can look like urgency. IBS-like symptoms are common in IBD and need a different toolkit. Asking for a plan to confirm inflammation is not delaying care. It is targeting care.</p>
<p>Your team may use calprotectin, CRP, imaging, or flexible sigmoidoscopy or colonoscopy depending on your history. Cross-sectional imaging matters more when penetrating or stricturing Crohn's disease is suspected. Say if pain is post-prandial, nocturnal, or associated with vomiting. Those details change urgency.</p>

<h2>Switching, cycling, and combination strategies</h2>
<p>When a switch is appropriate, clinicians consider prior classes used, why they failed, antibody history, extraintestinal disease, fistula disease, pregnancy plans, infection risk, and insurance sequencing. Some people cycle to another drug in a related group. Others move to a different mechanism such as anti-integrin, anti-interleukin, or a small molecule where labeled and appropriate. Combination approaches are individualized.</p>
<p>Ask what success will look like and when you will reassess. A written 8 to 16 week checkpoint reduces the anxiety of waiting without a plan. Ask whether steroids or another bridge will be used, how long the bridge should last, and what monitoring accompanies it.</p>

<h2>Surgery is a treatment option, not a moral failure</h2>
<p>For some phenotypes, surgical consultation belongs in the same conversation as drug switches. Recurrent obstruction, dysplasia, medically refractory colitis, or septic complications can make surgery the safer path. Asking for a surgical opinion does not mean you failed medical therapy as a person. It means your team is using the full IBD toolbox.</p>

<h2>Work, school, and mental health during uncertainty</h2>
<p>Loss of response often arrives with work absences, school stress, and fear about running out of options. Ask about disability paperwork timing, infusion schedule flexibility, and counseling resources. Peer support through Foundation communities can help, especially if you are facing your first switch after years on one medicine.</p>
<p>Keep logging. A clean timeline of dose dates, symptom scores, steroid bursts, and infections makes peer-to-peer insurance calls and clinic decisions faster.</p>

<h2>Bottom line for patients</h2>
<p>When a biologic seems to stop working, slow the story down just enough to define failure, confirm inflammation, and interpret drug exposure. Then discuss optimization, switching, or surgery with clear checkpoints. You deserve a plan that names next steps, not only a reassurance that "we will figure it out." Bring your timeline and ask for that plan in writing.</p>

<h2>Clinic script you can copy</h2>
<p>"I think I may have secondary loss of response. Can we confirm inflammation, review TDM if appropriate, and outline options with pros, cons, and monitoring plans?"</p>
""",
    },
    {
        "slug": "ibd-medication-monitoring-checklist",
        "title": "IBD Medication Monitoring Checklist: Labs, Screens, and Follow-Up Questions",
        "description": (
            "Practical IBD medication monitoring checklist: baseline screens, labs on "
            "immunomodulators and biologics, vaccines, and visit questions. Education only."
        ),
        "category": "Treatment · November 2026",
        "date_display": DATE_DISPLAY,
        "date_iso": DATE_ISO,
        "asset_dir": "ibd-medication-monitoring-checklist",
        "images": ["ibd-medication-monitoring-checklist_1.jpg"],
        "alts": ["Checklist and lab tubes representing IBD medication monitoring education"],
        "share": "IBD medication monitoring checklist for labs and screens. Education only.",
        "resource_category": "treatment",
        "match_terms": [
            "medication monitoring ibd",
            "biologic lab monitoring",
            "ibd lab checklist",
            "immunosuppressant monitoring",
            "tb test before biologic",
            "hepatitis screen biologic",
        ],
        "tags": [
            "monitoring",
            "labs",
            "biologics",
            "vaccines",
            "checklist",
            "treatment",
        ],
        "body": """
<p>People looking for an <strong>IBD medication monitoring checklist</strong> want a practical list of screens and labs that often appear before and during treatment. Exact schedules belong to your gastroenterologist. This page helps you ask complete questions and track what was already done.</p>
<p>Pair this with <a href="/blog/vaccines-biologics-immunosuppressants-ibd">vaccines on immunosuppressants</a>, <a href="/blog/therapeutic-drug-monitoring-ibd">TDM</a>, and <a href="/guides/foundation-ibd-medication-guide">Foundation medication guide</a>.</p>

<h2>Before starting many advanced therapies</h2>
<ul class="blog-list">
<li>Infection history and travel exposures</li>
<li>Tuberculosis screening when indicated</li>
<li>Hepatitis B and sometimes hepatitis C testing</li>
<li>Vaccine status review (live versus non-live timing)</li>
<li>Baseline blood counts, liver enzymes, and kidney function as ordered</li>
<li>Pregnancy plans and contraception conversations when relevant</li>
</ul>

<h2>While on therapy: themes by medicine class</h2>
<p>Different medicines need different rhythms. Thiopurines, methotrexate, JAK inhibitors, S1P modulators, anti-TNF agents, and other biologics each have their own labels and clinic protocols. Ask for a written monitoring calendar instead of memorizing internet lists.</p>
<ul class="blog-list">
<li><strong>Blood counts and chemistries:</strong> common for several immunosuppressants</li>
<li><strong>Lipids or other specialty labs:</strong> may apply to some small molecules</li>
<li><strong>Drug levels / antibodies:</strong> see TDM for selected biologics</li>
<li><strong>Skin and infection vigilance:</strong> report fevers, cough, shingles symptoms, or new skin lesions promptly</li>
</ul>

<h2>Build your personal checklist</h2>
<ul class="blog-list">
<li>Drug name, dose, and next due date</li>
<li>Last TB / hepatitis screens and results</li>
<li>Last vaccine dates</li>
<li>Upcoming lab dates and who reviews them</li>
<li>Portal message plan if a lab is abnormal</li>
</ul>

<h2>Questions for clinic and pharmacy</h2>
<ul class="blog-list">
<li>Which labs are required at baseline, week 4 to 12, then ongoing?</li>
<li>Who calls me if a result needs action?</li>
<li>Which vaccines should I complete before immunosuppression intensifies?</li>
<li>What symptoms should trigger holding a dose and calling?</li>
</ul>

<h2>When to seek prompt care</h2>
<p>Fever with immunosuppression, severe headache with neurologic symptoms, chest pain, uncontrolled bleeding, or rapidly worsening abdominal pain need urgent evaluation. A checklist does not replace triage. See <a href="/flare-help">flare help</a>.</p>

<p>Related reading: <a href="/blog/starting-biologic-first-12-weeks">starting a biologic</a> · <a href="/blog/rinvoq-patient-questions-ibd">Rinvoq patient questions</a> · <a href="/blog/ibd-treatment-comparison-guide">treatment comparison</a>.</p>
<p>Education supports shared decisions. It does not replace your gastroenterologist or pharmacist. Keep one shared note that caregivers and teens can both update.</p>
<p>If labs are drawn at an outside facility, confirm the clinic receives results. Missing faxed labs are a common delay.</p>
<p>Traveling? Ask how to time labs and infusions across time zones before tickets are booked.</p>


<h2>Why monitoring checklists prevent quiet harm</h2>
<p>Many IBD medicines reduce immune activity or change immune signaling. That can be life-changing for inflammation and still require structured safety watching. Problems are often silent at first: blood count changes, liver enzyme rises, lipid shifts for some medicines, infection risk, or delayed vaccine protection. A checklist turns vague advice into dated tasks you can verify in the portal.</p>
<p>Monitoring is also how teams catch secondary issues early, such as steroid side effects during bridges, iron deficiency during ongoing blood loss, or nutrient gaps after surgery. Your checklist can include disease monitoring and medicine safety monitoring in one place so nothing depends on memory alone.</p>

<h2>Baseline screens before advanced therapy</h2>
<p>Before many biologics or small molecules, clinicians review infection risk. Tuberculosis screening methods vary by history and local practice. Hepatitis B testing matters because reactivation risk exists with some immunosuppressive strategies. Additional viral testing may be ordered based on risk. Vaccine review should happen early because live vaccines may be timed differently once immunosuppression intensifies.</p>
<p>Baseline labs often include blood counts and comprehensive metabolic panels. Some medicines need specialty baselines such as lipid panels. Pregnancy testing may be appropriate before teratogenic medicines. Eye history can matter for selected older therapies. Dermatologic history matters if skin cancer risk counseling is part of the plan. Ask for a written list of what was already completed versus still pending so prior-authorization timing does not outrun safety steps.</p>

<h2>Ongoing labs: ask for cadence, not folklore</h2>
<p>Internet schedules are often wrong for your exact medicine and dose. Ask your clinic for cadence in writing: weekly, biweekly, monthly, then spaced out. Clarify whether local lab chains are acceptable and whether you must use a health-system lab for protocol consistency. Ask who reviews results within how many business days. If you travel for work, ask how to keep the cadence without missing doses.</p>
<p>For selected biologics, therapeutic drug monitoring joins the checklist. For immunomodulators, metabolite monitoring may be used in some practices. For JAK inhibitors and other small molecules, label-based labs and infection vigilance are essential. Your pharmacist can help reconcile the label with the clinic protocol when instructions seem to conflict.</p>

<h2>Vaccines, dental care, and procedures</h2>
<p>Put vaccine dates on the same checklist as labs. Inactivated vaccines are often encouraged, but timing around therapy starts can matter. Live vaccines need individualized decisions. Dental procedures, colonoscopies, and surgeries may need medicine-timing plans. Write the plan down before the procedure day so on-call staff are not guessing.</p>
<p>If you are due for cervical cancer screening, skin checks, or bone density testing because of steroid history, add those preventive items. Medicine monitoring is broader than a single CBC.</p>

<h2>Infection and symptom watch list</h2>
<ul class="blog-list">
<li>Fever, productive cough, or shortness of breath</li>
<li>Shingles-like rash pain</li>
<li>Severe headache with vision changes or neurologic symptoms</li>
<li>Unexplained bruising or bleeding</li>
<li>Dark urine, jaundice, or intense right-upper abdominal pain</li>
<li>Signs of dehydration during flares while on therapy</li>
</ul>
<p>Ask which symptoms mean hold the dose and call today versus message the portal. Holding decisions should come from your care team, especially if stopping abruptly is risky in your situation.</p>

<h2>Caregiver and teen versions of the checklist</h2>
<p>Families do better with one shared note that lists drug name, specialty pharmacy phone, next lab date, next infusion or injection date, and emergency contacts. Teens transitioning to adult care should practice requesting their own lab results and explaining their medicine list. Bring the checklist to every specialty visit, including dermatology and primary care, so duplicate immunosuppressants or interacting medicines are caught.</p>

<h2>Bottom line for patients</h2>
<p>An IBD medication monitoring checklist is a living document: baseline screens, ongoing labs, vaccines, procedure timing, and symptom triggers. Ask for cadence in writing, confirm who reviews results, and keep dose dates honest. Education helps you organize. Your gastroenterologist and pharmacist set the medical rules for your exact therapy.</p>

<h2>Clinic script you can copy</h2>
<p>"Please give me a written monitoring checklist for my medicine: baseline screens already done, upcoming labs, vaccine plan, and symptoms that mean I should call before the next dose."</p>
""",
    },
    {
        "slug": "ibd-insurance-denial-appeal-toolkit",
        "title": "IBD Insurance Denial Appeal Toolkit: A Practical Patient Worksheet",
        "description": (
            "IBD insurance denial appeal toolkit: worksheet for prior auth denials, "
            "peer-to-peer, Foundation letter resources, and clinic talking points. Education only."
        ),
        "category": "Insurance · November 2026",
        "date_display": DATE_DISPLAY,
        "date_iso": DATE_ISO,
        "asset_dir": "ibd-insurance-denial-appeal-toolkit",
        "images": ["ibd-insurance-denial-appeal-toolkit_1.jpg"],
        "alts": ["Desk with documents representing an IBD insurance appeal worksheet"],
        "share": "IBD insurance denial appeal toolkit and worksheet. Education only.",
        "resource_category": "getting-started",
        "match_terms": [
            "insurance denial appeal ibd",
            "biologic denial appeal",
            "appeal letter crohn",
            "prior authorization denied",
            "peer to peer biologic",
            "insurance appeal toolkit",
        ],
        "tags": [
            "insurance",
            "appeal",
            "prior authorization",
            "biologics",
            "denial",
        ],
        "body": """
<p>An <strong>insurance denial</strong> for an IBD medicine or procedure is stressful and time sensitive. This toolkit turns general prior-authorization education into a practical worksheet you can fill with your clinic. It is not legal advice and not a guarantee of coverage.</p>
<p>Pair this with <a href="/blog/prior-authorization-biologics-timeline">prior authorization timeline</a>, <a href="/blog/insurance-biologics-ibd">insurance and biologics</a>, and the Foundation bridge guide on <a href="/guides/foundation-ibd-appeal-letters">appeal letters</a>.</p>

<h2>Worksheet: capture the denial facts</h2>
<ul class="blog-list">
<li>Medicine or procedure denied, dose, and date of denial letter</li>
<li>Denial reason codes in the letter (step therapy, not medically necessary, quantity limit)</li>
<li>Member ID, group number, and appeals fax/portal address</li>
<li>Deadline for internal appeal and any external review rights listed</li>
<li>Clinic contact who owns the peer-to-peer call</li>
</ul>

<h2>Evidence packet checklist</h2>
<ul class="blog-list">
<li>Clinic note summarizing diagnosis, phenotype, and prior drug failures</li>
<li>Scopes, imaging, and calprotectin trends that support need</li>
<li>Hospitalizations or steroid courses related to uncontrolled disease</li>
<li>Guideline or labeling excerpts your clinician chooses to cite</li>
<li>Foundation or payer-specific appeal templates when appropriate</li>
</ul>

<h2>Peer-to-peer and next levels</h2>
<p>A peer-to-peer review is a clinician-to-clinician call. Ask when it is scheduled and what talking points your GI will use. If the internal appeal fails, ask about external review timelines in your state and whether a specialty pharmacy can escalate concurrently.</p>

<h2>Patient actions that help without doing the clinic's job</h2>
<ul class="blog-list">
<li>Upload the denial letter to the portal the same day</li>
<li>Confirm the pharmacy has not canceled the order</li>
<li>Ask about samples, bridge programs, or temporary alternatives only through your clinician</li>
<li>Keep a dated call log with names and reference numbers</li>
</ul>

<h2>Questions for your care team</h2>
<ul class="blog-list">
<li>What is the exact denial reason we are appealing?</li>
<li>Who submits the appeal packet and by what deadline?</li>
<li>Should we request an expedited appeal because of disease severity?</li>
<li>What is plan B if this appeal fails?</li>
</ul>

<h2>When medical risk rises while paperwork waits</h2>
<p>If you are flaring, on high-dose steroids, or losing weight while coverage is delayed, tell the clinic immediately. Appeals and emergency medical care can run in parallel. See <a href="/flare-help">flare help</a>.</p>

<p>Related reading: <a href="/guides/step-therapy-safe-step-act-ibd">step therapy and Safe Step Act</a> · <a href="/#news-advocacy">advocacy news</a> · <a href="/blog/when-ibd-biologic-stops-working">when a biologic stops working</a>.</p>
<p>Education supports shared decisions. It does not replace your gastroenterologist, specialty pharmacy, or benefits counselor. Employer HR or a patient advocate may help with paperwork, not medical choices.</p>
<p>Keep digital and paper copies of every letter. Appeals often ask for the same attachments twice.</p>
<p>If English is not your preferred language, ask for interpreter support on payer calls so deadlines are not missed.</p>


<h2>Know the denial type before you write anything</h2>
<p>Not every adverse coverage letter is the same. Prior authorization denials, step-therapy requirements, quantity-limit denials, site-of-care redirects, and formulary exclusions can look similar in the patient portal and still need different responses. Read the letter for the stated reason and the appeals address. If the letter is vague, call the number on the back of your insurance card and ask for the denial reason in plain language, then document the representative name and reference number.</p>
<p>Also separate pharmacy benefit denials from medical benefit denials. Infused biologics are often processed as medical benefits. Self-injected medicines may run through specialty pharmacy benefits. Appeals sent to the wrong channel waste days. Ask the specialty pharmacy which benefit owns the claim.</p>

<h2>Build a one-page clinical story with your clinic</h2>
<p>Reviewers respond to concise narratives: diagnosis and phenotype, objective disease activity, prior medicines tried and why they stopped, hospitalizations or steroid dependence, and the clinical rationale for the requested therapy. Your clinician writes the medical necessity language. You can help by providing accurate dates of prior drugs, including samples and short bridge courses that may not appear cleanly in claims data.</p>
<p>Attach supporting documents rather than hoping the reviewer opens every chart tab. Useful attachments often include recent clinic notes, endoscopy reports, imaging summaries, calprotectin trends, and hospitalization discharge summaries. Your clinician decides which guidelines or label sections to cite. Foundation appeal resources can help with structure when your clinic wants a template starting point.</p>

<h2>Deadlines, expedited review, and peer-to-peer</h2>
<p>Mark the internal appeal deadline on a calendar with reminders two days earlier. Ask whether your clinical situation qualifies for expedited review. Severe flares, hospitalization risk, or inability to eat may support urgency, but the clinic must frame that medically. Peer-to-peer review is often the fastest clinician-level conversation. Confirm the appointment time and provide a one-page bullet list your GI can use.</p>
<p>If internal appeals fail, ask about external review rights. Rules vary by state and plan type (employer-sponsored, marketplace, Medicaid, Medicare Advantage). A benefits counselor, hospital financial advocate, or Foundation guidance resources may help you navigate paperwork without giving medical advice.</p>

<h2>Bridge planning while you wait</h2>
<p>Appeals can take days to weeks. Ask your clinician about safe bridge options if appropriate, manufacturer support programs, hospital outpatient options, or alternative covered therapies that will not burn future sequencing options carelessly. Do not start leftover steroids from an old bottle without instructions. Do not ration injections without telling the clinic.</p>
<p>Specialty pharmacies sometimes cancel orders after a denial. Call to keep the prescription active so approval can move immediately if the appeal succeeds. Confirm shipping addresses and refrigeration plans in advance.</p>

<h2>Documentation habits that win time</h2>
<ul class="blog-list">
<li>Save PDFs of every denial, approval, and call reference number</li>
<li>Use one folder named by medicine and year</li>
<li>Note every portal message date</li>
<li>Track missed work or school if functional impact supports urgency language your clinician may use</li>
<li>Keep infusion center and pharmacy contacts in the same note</li>
</ul>

<h2>Employer and school angles</h2>
<p>If you have an employer plan, HR can sometimes clarify carve-outs or specialty vendor contacts, but they cannot override medical necessity decisions. Students may need temporary disability or attendance letters while coverage is unstable. Ask clinic social work or nursing what letter templates already exist.</p>

<h2>Bottom line for patients</h2>
<p>An IBD insurance denial appeal toolkit is a worksheet: identify the denial type, gather a clinical packet with your team, meet deadlines, pursue peer-to-peer when offered, and create a bridge plan for disease control while paperwork moves. Persistence helps. Panic dosing does not. Pair this toolkit with your clinician and specialty pharmacy rather than fighting the payer alone.</p>

<h2>Clinic script you can copy</h2>
<p>"I received a denial for my IBD therapy. Here is the letter and deadline. Can we open an appeal packet today, schedule peer-to-peer if needed, and confirm a bridge plan while we wait?"</p>
""",
    },
    {
        "slug": "ibd-treatment-comparison-guide",
        "title": "IBD Treatment Comparison Guide: Classes, Not Brand Pitches",
        "description": (
            "Patient-level comparison of IBD treatment classes: aminosalicylates, "
            "steroids, immunomodulators, biologics, and small molecules. Education only."
        ),
        "category": "Treatment · November 2026",
        "date_display": DATE_DISPLAY,
        "date_iso": DATE_ISO,
        "asset_dir": "ibd-treatment-comparison-guide",
        "images": ["ibd-treatment-comparison-guide_1.jpg"],
        "alts": ["Assorted medicine bottles representing IBD treatment classes education"],
        "share": "IBD treatment classes compared in plain language. Education only.",
        "resource_category": "treatment",
        "match_terms": [
            "ibd treatment comparison",
            "biologic vs jak inhibitor",
            "crohn treatment options",
            "ulcerative colitis medicine classes",
            "compare ibd drugs",
            "treatment classes ibd",
        ],
        "tags": [
            "treatment",
            "biologics",
            "JAK",
            "steroids",
            "comparison",
            "Crohn's",
            "colitis",
        ],
        "body": """
<p>An <strong>IBD treatment comparison</strong> should explain medicine classes without crowning a winner. The right choice depends on disease location, severity, prior failures, safety factors, pregnancy plans, and access. This guide supports questions for your gastroenterologist. It does not recommend a specific drug.</p>
<p>Pair this with <a href="/blog/understanding-biologics-ibd">understanding biologics</a>, <a href="/blog/rinvoq-patient-questions-ibd">JAK therapy questions</a>, and <a href="/guides/foundation-ibd-medication-guide">Foundation medication guide</a>.</p>

<h2>Big buckets you will hear</h2>
<ul class="blog-list">
<li><strong>Aminosalicylates (5-ASA):</strong> often discussed in mild to moderate ulcerative colitis</li>
<li><strong>Corticosteroids:</strong> fast inflammation control, not long-term maintenance for most people</li>
<li><strong>Immunomodulators:</strong> thiopurines or methotrexate in selected plans, with lab monitoring</li>
<li><strong>Biologics:</strong> antibody therapies targeting pathways such as TNF, integrins, or interleukins</li>
<li><strong>Small molecules:</strong> oral agents such as JAK inhibitors or S1P modulators in labeled settings</li>
<li><strong>Surgery:</strong> a treatment option, not a failure, for some disease patterns</li>
</ul>

<h2>How clinicians compare options</h2>
<ul class="blog-list">
<li>How quickly control is needed</li>
<li>Fistulizing, stricturing, or extensive disease features</li>
<li>Infection risk, cancer history, heart failure, or clotting risk factors</li>
<li>Infusion center versus home injection versus oral preference</li>
<li>Insurance step edits and prior authorization realities</li>
</ul>

<h2>Questions that clarify without asking for a miracle ranking</h2>
<ul class="blog-list">
<li>What are the top two options for my phenotype and why?</li>
<li>What monitoring does each option require?</li>
<li>What happens if the first choice fails within 3 to 6 months?</li>
<li>How do pregnancy or infection risks change the ranking?</li>
</ul>

<h2>Common myths</h2>
<ul class="blog-list">
<li><strong>"Stronger always means better."</strong> Fit matters more than internet potency rankings.</li>
<li><strong>"Biologics are last resort forever."</strong> Many people start advanced therapy earlier based on risk.</li>
<li><strong>"Pills are automatically safer than infusions."</strong> Safety depends on the mechanism and your history.</li>
</ul>

<p>Related reading: <a href="/blog/when-ibd-biologic-stops-working">when a biologic stops working</a> · <a href="/blog/ibd-medication-monitoring-checklist">monitoring checklist</a> · <a href="/blog/ibd-clinical-trials-patient-decision-guide">clinical trials guide</a>.</p>
<p>Education supports shared decisions. It does not replace your gastroenterologist. Bring your goals (steroid-free remission, work travel, school sports) so comparisons stay personal.</p>
<p>If two options look similar medically, ask about logistics: travel to infusions, cold-chain storage, and lab frequency.</p>
<p>Kids, older adults, and people with transplants or cancer histories need tailored comparisons from specialists.</p>


<h2>Start with goals, not brand names</h2>
<p>Useful comparisons begin with goals: induce remission, stay steroid-free, heal mucosa, control fistulas, protect joints or skin, preserve school and work function, and match your risk tolerance. Two people with "Crohn's disease" can need different first advanced therapies because one has isolated ileal strictures and another has extensive colitis with extraintestinal disease. Ask your clinician to restate your goals before listing products.</p>
<p>Also separate induction from maintenance. Steroids may induce improvement quickly for some people and still be poor maintenance tools because of side effects. A comparison chart that only lists "works fast" without maintenance and monitoring context is incomplete.</p>

<h2>Class-by-class patient lens</h2>
<p><strong>Aminosalicylates</strong> are often discussed for mild to moderate ulcerative colitis and selected situations. They are not interchangeable with biologics for higher-risk disease. <strong>Corticosteroids</strong> reduce inflammation quickly for many flares but bring metabolic, bone, mood, and infection costs when repeated. <strong>Immunomodulators</strong> may appear as steroid-sparing or combination strategies with careful labs. <strong>Anti-TNF and other biologics</strong> target immune pathways with infusion or injection logistics and infection screening. <strong>Anti-integrin and anti-interleukin biologics</strong> offer additional pathway choices with their own monitoring and timing profiles. <strong>Oral small molecules</strong> such as JAK inhibitors or S1P modulators can appeal for convenience and still require serious safety conversations around infections, lab monitoring, and cardiovascular or clotting risk factors where relevant.</p>
<p>Surgery belongs on the comparison board for stricturing disease, dysplasia, toxic colitis risk, or refractory disease. Comparing "medicine versus medicine" while ignoring a needed operation can delay safer care.</p>

<h2>Safety and lifestyle filters that change rankings</h2>
<ul class="blog-list">
<li>Prior tuberculosis, hepatitis B, or recurrent infections</li>
<li>Personal or family history considerations your clinician flags for specific classes</li>
<li>Heart failure history for some anti-TNF discussions</li>
<li>Pregnancy now or within a year</li>
<li>Needle phobia versus pill preference versus infusion center access</li>
<li>Cold-chain storage limits at home or dorms</li>
<li>Ability to complete frequent lab monitoring</li>
</ul>
<p>A medicine that looks perfect on social media can be a poor fit after these filters. Ask your clinician to score options against your filters out loud.</p>

<h2>Access reality is part of comparison</h2>
<p>Step therapy, prior authorization, and specialty pharmacy networks shape what you can start this month. A comparison guide that ignores access is incomplete for real life. Ask which option is medically preferred and which is most likely to clear insurance quickly. Sometimes the sequence is a short bridge plus the preferred advanced therapy rather than an endless fight that leaves inflammation untreated.</p>

<h2>How to compare without getting lost</h2>
<p>Request a two-option comparison rather than a ten-drug spreadsheet. For each option ask: expected benefit timeline, major risks, monitoring burden, administration, escape plan if it fails, and whether future options are narrowed. Write the answers down. Bring a caregiver if processing speed is reduced by steroids, anemia, or sleep loss.</p>

<h2>Pediatric, older adult, and complex history notes</h2>
<p>Children and adolescents need growth, school, and long-horizon safety framed differently. Older adults may have different infection and cancer risk tradeoffs. People with prior cancer, transplants, or multiple autoimmune diseases need specialists to co-manage comparisons. Do not borrow a ranking from someone with a dissimilar history.</p>

<h2>Bottom line for patients</h2>
<p>IBD treatment comparison is class-aware, goal-based, safety-filtered, and access-aware. It is not a crowd-sourced potency contest. Use this guide to prepare questions, then ask your gastroenterologist for a personalized two-option comparison with monitoring and contingency plans included.</p>

<h2>Clinic script you can copy</h2>
<p>"Please compare two treatment classes for my situation: expected benefits, key risks, monitoring, and what we would do if the first choice does not work."</p>
""",
    },
    {
        "slug": "after-ibd-surgery-first-30-days",
        "title": "After IBD Surgery: Your First 30 Days at Home",
        "description": (
            "First 30 days at home after IBD surgery: wound and ostomy themes, diet "
            "advances, red flags, and clinic follow-up questions. Education only."
        ),
        "category": "Surgery · November 2026",
        "date_display": DATE_DISPLAY,
        "date_iso": DATE_ISO,
        "asset_dir": "after-ibd-surgery-first-30-days",
        "images": ["after-ibd-surgery-first-30-days_1.jpg"],
        "alts": ["Calm home recovery setting after hospital discharge education image"],
        "share": "First 30 days at home after IBD surgery. Education only.",
        "resource_category": "wellness",
        "match_terms": [
            "after ibd surgery",
            "first 30 days after crohn surgery",
            "recovery after colectomy",
            "home after bowel surgery",
            "ostomy first month",
            "post op ibd recovery",
        ],
        "tags": [
            "surgery",
            "recovery",
            "ostomy",
            "J-pouch",
            "post-op",
            "Crohn's",
            "colitis",
        ],
        "body": """
<p>The <strong>first 30 days after IBD surgery</strong> are about healing, learning new routines, and knowing which symptoms need a call. Every operation differs (resection, colectomy, ostomy, J-pouch stages). Follow your surgeon's written discharge plan first. This page adds patient-level structure, not a substitute protocol.</p>
<p>Pair this with <a href="/blog/ostomy-basics-ibd">ostomy basics</a>, <a href="/blog/j-pouch-basics-ibd">J-pouch basics</a>, <a href="/blog/enteral-nutrition-after-ibd-surgery">enteral nutrition after surgery</a>, and <a href="/guides/foundation-ibd-surgery-ostomy">Foundation surgery and ostomy bridge</a>.</p>

<h2>Week 1 themes</h2>
<ul class="blog-list">
<li>Pain control, walking, and breathing exercises as cleared</li>
<li>Wound or ostomy appliance checks taught by nursing</li>
<li>Diet advances exactly as written (often liquids toward soft foods)</li>
<li>Medication list: which IBD drugs restart and when</li>
</ul>

<h2>Weeks 2 to 4 themes</h2>
<ul class="blog-list">
<li>Energy may lag even when wounds look fine</li>
<li>Output patterns for ostomy or new bowel anatomy can fluctuate</li>
<li>Follow-up visits with surgery and GI teams</li>
<li>Mental health check: surgery recovery is emotional as well as physical</li>
</ul>

<h2>Red flags that need prompt contact</h2>
<ul class="blog-list">
<li>Fever, spreading redness, or drainage from incisions</li>
<li>Persistent vomiting or inability to pass gas or stool when unexpected</li>
<li>Severe abdominal distension or escalating pain</li>
<li>Ostomy stoma color changes, severe leakage with skin breakdown, or dehydration</li>
<li>Chest pain, shortness of breath, or calf swelling</li>
</ul>

<h2>Questions for your surgical team</h2>
<ul class="blog-list">
<li>When can I shower, drive, and lift again?</li>
<li>What diet stages should I follow this week?</li>
<li>Which warning signs mean ER versus office call?</li>
<li>When does GI resume or adjust IBD medicines?</li>
</ul>

<p>Related reading: <a href="/blog/hospital-feeding-ibd-enteral-parenteral">hospital feeding</a> · <a href="/blog/ibd-surgery-peer-support">surgery peer support</a> · <a href="/flare-help">flare help</a>.</p>
<p>Education supports shared decisions. It does not replace your surgeon or wound/ostomy nurse. Keep a daily log of intake, output, pain scores, and questions.</p>
<p>Caregivers: agree on one person who manages appliance supplies and one who manages medications to reduce missed steps.</p>
<p>If you live far from the hospital, ask about local urgent care versus return-to-center criteria before discharge.</p>


<h2>Discharge day: make the plan portable</h2>
<p>Before you leave the hospital, photograph or request printed copies of wound care instructions, diet stages, medicine lists, emergency numbers, and ostomy supply brands if relevant. Ask who to call after hours for surgical questions versus IBD medicine questions. Confirm the date of the first outpatient surgical follow-up and whether staples or dressings need nursing review sooner.</p>
<p>Clarify which IBD medicines are paused and which restart dates are tentative pending healing. If you use steroids, ask for a taper schedule in writing. If anticoagulation or antibiotics are prescribed, add alarms. Caregivers should know where supplies live at home before the car ride.</p>

<h2>Pain, mobility, and sleep</h2>
<p>Walking short distances several times daily often helps recovery more than staying in bed, within your surgeon's limits. Use incentive spirometry if provided. Pain control should allow deep breaths and walks without heavy sedation. Track bowel function or ostomy output while on opioids because constipation or output changes can confuse the picture. Sleep may be fragmented. Short rests count. Ask when driving and lifting restrictions lift so work planning is realistic.</p>

<h2>Diet advances without improvising</h2>
<p>Post-operative diets are anatomy-specific. A person with a new ileostomy has different priorities than someone after a colectomy with anastomosis or a J-pouch stage. Follow the written stages. Chew thoroughly, separate liquids from large meals if instructed, and introduce fiber only when cleared. Dehydration risk is real with high ostomy output. Ask for output thresholds that should trigger a call, and whether oral rehydration solutions are recommended.</p>
<p>If nausea prevents intake, call early rather than waiting for weakness. After some operations, enteral nutrition support is part of the plan. See related IBDPal education on post-surgical nutrition rather than inventing shakes from social media.</p>

<h2>Wound and ostomy learning curve</h2>
<p>Expect a learning curve with appliance changes. Schedule a home health or outpatient ostomy nurse visit if offered. Watch stoma color, output consistency, and peri-stomal skin. Leakage that destroys skin needs faster help than "wait until the next appointment." Keep a spare appliance kit in the car and bathroom. For incision care, follow cleansing instructions and avoid bathtub soaking until cleared.</p>

<h2>Emotions in the first month</h2>
<p>Body image changes, fear of recurrence, and grief after organ removal are common. Peer support and counseling help. Partners and parents need roles that do not become round-the-clock surveillance. Agree on check-in times. Celebrate small milestones: first shower, first walk around the block, first independent appliance change.</p>

<h2>Returning to IBD medical therapy</h2>
<p>GI and surgery teams should coordinate restarting biologics or other therapies. Ask who owns that decision and what healing checkpoints are required. Infection signs can be subtler on immunosuppression, so know the fever threshold your team wants reported.</p>

<h2>Work, school, and intimacy conversations</h2>
<p>Ask for a letter describing lifting limits and expected recovery windows. Students may need temporary accommodations for bathroom access and missed exams. Intimacy questions after pelvic surgery or ostomy creation are valid; ask for referrals to clinicians comfortable with those discussions rather than waiting in silence.</p>
<p>Supply planning matters too. Estimate appliance use for the first month and confirm how to reorder before you run out. Keep a overnight bag with spare clothes and supplies for unexpected leaks during the learning curve.</p>

<h2>Bottom line for patients</h2>
<p>The first 30 days at home after IBD surgery succeed with a portable written plan, honest output and symptom logging, early calls for red flags, and coordinated medicine restarts. Education prepares you. Your surgeon, ostomy nurse, and gastroenterologist still set your personal protocol.</p>

<h2>Clinic script you can copy</h2>
<p>"For my first 30 days at home, please confirm diet stages, activity limits, medicine restarts, and the exact symptoms that mean I should call or go to the ER."</p>
""",
    },
    {
        "slug": "understanding-ibd-pathology-report",
        "title": "Understanding Your IBD Pathology Report: Beyond the Colonoscopy Note",
        "description": (
            "How to read IBD pathology language: inflammation, chronicity, dysplasia, "
            "and questions to ask after biopsies. Education only, not DIY diagnosis."
        ),
        "category": "Diagnostics · November 2026",
        "date_display": DATE_DISPLAY,
        "date_iso": DATE_ISO,
        "asset_dir": "understanding-ibd-pathology-report",
        "images": ["understanding-ibd-pathology-report_1.jpg"],
        "alts": ["Microscope representing IBD pathology report education"],
        "share": "Understanding IBD pathology reports in plain language. Education only.",
        "resource_category": "wellness",
        "match_terms": [
            "ibd pathology report",
            "read pathology report colitis",
            "biopsy results crohn",
            "dysplasia ibd pathology",
            "chronic colitis pathology",
            "understanding biopsy report ibd",
        ],
        "tags": [
            "pathology",
            "biopsy",
            "colonoscopy",
            "dysplasia",
            "diagnostics",
        ],
        "body": """
<p>An <strong>IBD pathology report</strong> describes what pathologists see under the microscope after biopsies. It complements the endoscopist's colonoscopy note. This page goes deeper than a procedure summary so you can ask clearer questions. It is not a tool to diagnose yourself.</p>
<p>Pair this with <a href="/blog/how-to-read-colonoscopy-report-ibd">how to read a colonoscopy report</a> and <a href="/guides/foundation-ibd-colonoscopy-cancer-surveillance">surveillance education</a>.</p>

<h2>What pathology adds</h2>
<ul class="blog-list">
<li>Patterns of acute and chronic inflammation</li>
<li>Architectural changes that support chronic colitis</li>
<li>Granulomas or other features sometimes discussed in Crohn's evaluations</li>
<li>Dysplasia language during cancer surveillance exams</li>
<li>Infection stains when ordered (for example CMV in selected cases)</li>
</ul>

<h2>Words you may see</h2>
<ul class="blog-list">
<li><strong>Active inflammation:</strong> neutrophils and related activity</li>
<li><strong>Chronicity:</strong> longer-standing injury patterns</li>
<li><strong>Quiescent:</strong> less active inflammation in the sampled tissue</li>
<li><strong>Dysplasia:</strong> abnormal cell changes that need specialist interpretation</li>
<li><strong>Indefinite for dysplasia:</strong> uncertain category that often needs discussion and follow-up</li>
</ul>

<h2>How to prepare for the results visit</h2>
<ul class="blog-list">
<li>Bring both the endoscopy report and pathology report</li>
<li>Ask which segments were biopsied and why</li>
<li>Ask how pathology changes medicines, surveillance interval, or surgery talks</li>
<li>Request a plain-language summary in the portal</li>
</ul>

<h2>Questions for your gastroenterologist</h2>
<ul class="blog-list">
<li>Does pathology confirm my IBD type or mainly show chronic colitis?</li>
<li>Is there dysplasia, and what is the next step if so?</li>
<li>Do results match what you saw during the scope?</li>
<li>Should any infection studies change treatment timing?</li>
</ul>

<p>Related reading: <a href="/blog/colonoscopy-prep-ibd">colonoscopy prep</a> · <a href="/blog/high-calprotectin-what-next">high calprotectin</a> · <a href="/visit-prep">visit prep</a>.</p>
<p>Education supports shared decisions. It does not replace your gastroenterologist or pathologist. Online forums often over-interpret single phrases.</p>
<p>If you change clinics, hand-carry pathology PDFs. New teams need the microscopic history, not only the discharge summary.</p>
<p>Pediatric wording can differ. Ask the pediatric GI to translate categories used in kids' reports.</p>


<h2>Pathology is a second camera on the same procedure</h2>
<p>During colonoscopy or sigmoidoscopy, the endoscopist describes what the mucosa looks like. Pathology describes what the tissue shows under the microscope. The two reports should be read together. Mild-looking mucosa can still show microscopic activity. Dramatic endoscopic ulcers usually have matching active inflammation, but infection or medication injury can complicate interpretation. Ask your gastroenterologist to reconcile both documents rather than reading pathology alone at midnight.</p>

<h2>Sampling limits you should respect</h2>
<p>Biopsies are tiny samples. Patchy Crohn's disease can be under-sampled. Ulcerative colitis distribution can evolve. A report that says "no dysplasia in these samples" does not mean the entire colon was proven free of every future risk. Surveillance quality also depends on bowel prep, withdrawal time, and whether raised lesions were resected or sampled adequately. Pathology cannot fix a poorly prepped exam.</p>

<h2>Chronicity versus activity</h2>
<p>Activity language often reflects neutrophils and epithelial injury happening now. Chronicity language reflects architectural distortion and other longer-standing changes. You can have chronic changes with little current activity, or active inflammation without every chronic feature in early disease. That nuance matters when someone online claims a single adjective proves you are "not in remission." Remission definitions used in clinic combine symptoms, biomarkers, endoscopy, and sometimes histology. Ask which definition your team is using.</p>

<h2>Dysplasia conversations without panic</h2>
<p>Dysplasia wording requires specialist interpretation. Categories and follow-up pathways have evolved, and visible lesions are handled differently from invisible flat dysplasia historically described in random biopsies. If you see "indefinite for dysplasia," ask what confounding inflammation is present and when repeat evaluation is planned. If definitive dysplasia is reported, ask whether gastroenterology and potentially colorectal surgery will review together. Bring a caregiver to that visit.</p>
<p>Do not skip surveillance because a prior pathology report was reassuring years ago. Intervals depend on disease extent, prior dysplasia, primary sclerosing cholangitis, family history, and exam quality.</p>

<h2>Infection and special stains</h2>
<p>In selected inpatients or refractory cases, pathologists may evaluate for CMV or other infections. A negative stain does not always close the question if clinical suspicion remains high. Ask whether microbiology tests from stool or tissue are pending alongside histology.</p>

<h2>Getting usable copies</h2>
<p>Request the full pathology report PDF, not only a portal snippet. If you move cities, hand-carry prior dysplasia reports and operative pathology from resections. Second opinions on dysplasia may include sending slides. Ask how to initiate that process early rather than during a compressed surgical decision window.</p>

<h2>Resection pathology after surgery</h2>
<p>If you had bowel removed, surgical pathology describes margins, lymph nodes when relevant, and disease features in the resected specimen. That report can refine Crohn's versus indeterminate discussions and guide postoperative medicine decisions. Ask for a copy even if you feel done with hospital paperwork. Future clinicians will thank you.</p>
<p>If medical therapy decisions hinge on granulomas, margin status, or unexpected dysplasia in the specimen, ask for a joint review between surgery and GI. Portal snippets often omit the explanatory comments pathologists add for clinicians. Keep both the gross description and the microscopic summary when you archive files.</p>

<h2>Bottom line for patients</h2>
<p>Understanding an IBD pathology report means reading activity, chronicity, dysplasia, and infection comments beside the endoscopy note, while respecting sampling limits. Use this page to prepare questions. Your gastroenterologist and, when needed, a multidisciplinary team translate the microscope into a plan.</p>

<h2>Clinic script you can copy</h2>
<p>"Please walk me through my pathology report in plain language, especially activity, chronicity, and any dysplasia wording, and tell me how it changes my plan."</p>
""",
    },
    {
        "slug": "ibd-clinical-trials-patient-decision-guide",
        "title": "IBD Clinical Trials: A Patient Decision Guide",
        "description": (
            "IBD clinical trials patient guide: phases, eligibility, informed consent, "
            "risks and benefits questions, and how to search responsibly. Education only."
        ),
        "category": "Research · November 2026",
        "date_display": DATE_DISPLAY,
        "date_iso": DATE_ISO,
        "asset_dir": "ibd-clinical-trials-patient-decision-guide",
        "images": ["ibd-clinical-trials-patient-decision-guide_1.jpg"],
        "alts": ["Research discussion representing IBD clinical trial education"],
        "share": "IBD clinical trials: a patient decision guide. Education only.",
        "resource_category": "clinical",
        "match_terms": [
            "ibd clinical trial guide",
            "crohn clinical trial questions",
            "should i join ibd study",
            "informed consent ibd trial",
            "clinical trial eligibility ulcerative colitis",
            "patient guide clinical trials ibd",
        ],
        "tags": [
            "clinical trials",
            "research",
            "informed consent",
            "Crohn's",
            "colitis",
        ],
        "body": """
<p>Considering an <strong>IBD clinical trial</strong> is a personal decision. Trials can expand options and advance science. They also involve protocols, visits, and uncertainty. This guide helps you prepare questions. It is not recruitment for any study.</p>
<p>Pair this with the Foundation bridge on <a href="/guides/foundation-ibd-clinical-trials">clinical trials education</a>, NIDDK trial pages in our <a href="/research">research hub</a>, and <a href="https://clinicaltrials.gov/search?cond=%22Inflammatory%20Bowel%20Diseases%22" rel="noopener noreferrer">ClinicalTrials.gov</a>.</p>

<h2>Trial phases in plain language</h2>
<ul class="blog-list">
<li><strong>Phase 1:</strong> early safety and dosing focus in small groups</li>
<li><strong>Phase 2:</strong> more signals on benefit and side effects</li>
<li><strong>Phase 3:</strong> larger comparisons that often support regulatory review</li>
<li><strong>Phase 4:</strong> after-approval learning in broader use</li>
</ul>

<h2>Eligibility and informed consent</h2>
<p>Eligibility rules may include disease type, prior medicines, lab values, and pregnancy status. Informed consent should explain procedures, risks, benefits, alternatives, and your right to withdraw. Take the document home. Ask for a second conversation if needed.</p>

<h2>Questions before you say yes</h2>
<ul class="blog-list">
<li>What is the study trying to learn, and what phase is it?</li>
<li>What treatments might I receive, including placebo if used?</li>
<li>How many visits, scopes, and blood draws are required?</li>
<li>What happens to my care if I leave the study early?</li>
<li>Who pays for study procedures versus standard care?</li>
<li>How are side effects monitored and reported?</li>
</ul>

<h2>Working with your own GI team</h2>
<p>Even if a research center runs the trial, keep your treating gastroenterologist informed. Ask how rescue therapy works if disease worsens and how trial participation affects insurance authorizations for standard drugs later.</p>

<h2>Red flags in online "trial" offers</h2>
<ul class="blog-list">
<li>Pressure to enroll the same day without documents</li>
<li>Claims of guaranteed remission</li>
<li>Requests for payment to join a drug study</li>
<li>Unclear institutional review board oversight</li>
</ul>

<p>Related reading: <a href="/blog/ibd-treatment-comparison-guide">treatment comparison</a> · <a href="/blog/when-ibd-biologic-stops-working">when a biologic stops working</a> · <a href="/ask">reader Q&amp;A</a>.</p>
<p>Education supports shared decisions. It does not replace your gastroenterologist or the study team. Bring a caregiver to consent visits when possible.</p>
<p>Search ClinicalTrials.gov with your clinician. Filters for recruiting status and location reduce outdated listings.</p>
<p>If you are a teen or young adult, ask how school or work absences will be handled in the visit schedule.</p>


<h2>Why people consider trials</h2>
<p>Patients look at IBD clinical trials when standard options have failed, when side effects limit current therapy, when a convenient oral agent is being studied, or when they want to contribute to research that may help others. Some trials include active comparators. Others include placebo periods with rescue rules. Understanding the design matters more than the brand name of the investigational product.</p>
<p>Trials are not always "last resort only." Sometimes earlier-line studies exist. Eligibility screens are strict. Feeling motivated does not override inclusion criteria, and that can be disappointing. Ask research coordinators how screening failures are handled and whether other studies might fit.</p>

<h2>What informed consent should make obvious</h2>
<p>Consent documents are long on purpose. They should explain procedures, visit calendars, known risks, unknown risks, alternatives including not joining, costs, compensation, and withdrawal rights. You can take the document home. You can ask for a teach-back conversation where the coordinator asks you to explain the study back in your own words. If anyone rushes you, pause.</p>
<p>Ask whether you will learn your treatment assignment during or after the study. Blinded designs exist for good scientific reasons and can be emotionally harder. Clarify rescue therapy if disease worsens and whether open-label extension exists after the controlled period.</p>

<h2>Practical burden checklist</h2>
<ul class="blog-list">
<li>Travel time and parking for frequent visits</li>
<li>Number of endoscopies and bowel preps</li>
<li>Blood volume and diary requirements</li>
<li>Work or school absences</li>
<li>Contraception requirements</li>
<li>Restrictions on other medicines or vaccines</li>
<li>Who covers injury-related care if a study-related adverse event occurs</li>
</ul>
<p>A scientifically exciting study can still be a poor personal fit if the visit burden will break your job or caregiving responsibilities.</p>

<h2>How trials interact with your regular GI care</h2>
<p>Tell your treating gastroenterologist before enrollment. Ask how flares will be co-managed, whether standard drug authorizations pause, and how information flows between the research site and your clinic. If you leave the study, ask how quickly standard therapy can restart and whether washout periods apply before the next medicine.</p>

<h2>Finding studies without getting scammed</h2>
<p>Start with ClinicalTrials.gov, academic centers, and Foundation trial finders. Be skeptical of social ads promising guaranteed remission for a fee. Legitimate drug trials do not charge patients to receive investigational product as a purchase. Confirm institutional review board oversight. Bring listings to your clinician before traveling for screening.</p>

<h2>Equity and support questions</h2>
<p>Ask whether travel stipends, parking coverage, or flexible visit windows exist. Ask how non-English speakers are supported. Ask whether reproductive counseling is available. These questions are appropriate and do not make you a difficult patient.</p>

<h2>After you enroll</h2>
<p>Keep a folder with consent pages, visit calendars, coordinator contacts, and adverse-event notes. Report symptoms early even if you are unsure they relate to the study drug. Missing diary entries can threaten data quality and sometimes protocol continuation, so ask for reminder tools that fit your phone habits.</p>
<p>If you feel pressure from social media communities to stay in a study despite worsening disease, return to the consent language about withdrawal and rescue. Your health comes first.</p>

<h2>Bottom line for patients</h2>
<p>An IBD clinical trial decision is a structured comparison of scientific purpose, phase, visit burden, risks, alternatives, and fit with your life and regular GI plan. Use this guide to slow the decision down enough to be informed. No article can consent for you. The study team and your gastroenterologist share the counseling role while you keep the final yes or no.</p>

<h2>Clinic script you can copy</h2>
<p>"I am considering an IBD clinical trial. Can we review eligibility, consent risks and benefits, visit burden, and how it fits my current treatment plan before I decide?"</p>
""",
    },
]


def patch_vercel(slugs: list[str]) -> None:
    text = VERCEL.read_text(encoding="utf-8")
    inserts = []
    for slug in slugs:
        if f'"/blog/{slug}"' in text:
            continue
        inserts.append(
            f'    {{\n      "source": "/blog/{slug}",\n'
            f'      "destination": "/blogs/{slug}.html"\n    }}'
        )
    if not inserts:
        return
    text = text.replace('"rewrites": [\n', '"rewrites": [\n' + ",\n".join(inserts) + ",\n")
    VERCEL.write_text(text, encoding="utf-8")
    print("patched vercel.json")


def patch_sitemap(slugs: list[str]) -> None:
    today = date.today().isoformat()
    text = SITEMAP.read_text(encoding="utf-8")
    for slug in slugs:
        if f"/blog/{slug}" in text:
            continue
        entry = (
            f"  <url>\n    <loc>{SITE}/blog/{slug}</loc>\n"
            f"    <lastmod>{today}</lastmod>\n"
            f"    <changefreq>monthly</changefreq>\n"
            f"    <priority>0.85</priority>\n  </url>\n"
        )
        text = text.replace("</urlset>", entry + "</urlset>")
    SITEMAP.write_text(text, encoding="utf-8")
    print("patched sitemap.xml")


def update_search_gap(posts: list[dict]) -> None:
    data = {"posts": []}
    if SEARCH_GAP.exists():
        data = json.loads(SEARCH_GAP.read_text(encoding="utf-8"))
        if isinstance(data, list):
            data = {"posts": data}
    by_slug = {p["slug"]: p for p in data.get("posts", [])}
    for post in posts:
        by_slug[post["slug"]] = {
            "slug": post["slug"],
            "match_terms": post.get("match_terms", []),
            "title": post["title"],
            "description": post["description"],
            "category": post["category"],
            "date_display": post["date_display"],
            "date_iso": post["date_iso"],
            "asset_dir": post["asset_dir"],
            "resource_category": post.get("resource_category", "wellness"),
            "tags": post.get("tags", []),
        }
    data["posts"] = list(by_slug.values())
    SEARCH_GAP.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("updated search-gap-posts.json")


def update_aliases(posts: list[dict]) -> None:
    data = json.loads(ALIASES.read_text(encoding="utf-8"))
    for post in posts:
        canonical = post["match_terms"][0]
        for term in post.get("match_terms", []):
            data[term.lower()] = canonical
    ALIASES.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("updated search-aliases.json")


def main() -> None:
    slugs = []
    for post in POSTS:
        ensure_image(post)
        wc = word_count(post["body"])
        if wc < MIN_WORDS:
            raise SystemExit(f"too short: {post['slug']} ({wc})")
        out = BLOGS / f"{post['slug']}.html"
        out.write_text(render_post(post), encoding="utf-8")
        slugs.append(post["slug"])
        print(f"wrote {out.name} (~{wc} words)")
    patch_vercel(slugs)
    patch_sitemap(slugs)
    update_search_gap(POSTS)
    update_aliases(POSTS)
    print("Done.", len(slugs), "posts")


if __name__ == "__main__":
    main()
