#!/usr/bin/env python3
"""Add international biologic guides and US-only disclaimers on prior-auth content."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
SEO_PAGES = DATA / "seo-landing-pages.json"
GUIDE_EXP = DATA / "guide-expansions.json"
SEO_EXP = DATA / "seo-expansion.json"
KEYWORDS = DATA / "ibd-resource-keywords.json"
BLOG_EXP = DATA / "blog-expansions.json"
BLOGS = ROOT / "blogs"
PYTHON = sys.executable

INTL_NOTE = (
    "Reading outside the United States? This page describes U.S. private insurance and employer "
    "plan workflows. For country-neutral questions about biologics and accessing therapy abroad, "
    "see our biologic questions for your doctor guide and biologic access outside the U.S. guide "
    "at ibdpal.org/guides."
)

US_BLOG_CALLOUT = (
    '<p class="blog-region-note"><strong>Outside the United States?</strong> '
    "This article describes U.S. insurance workflows. For country-neutral biologic questions "
    'and accessing therapy abroad, see our <a href="/guides/biologics-questions-for-your-doctor">'
    "biologic questions for your doctor</a> guide and "
    '<a href="/guides/ibd-biologic-access-outside-us">biologic access outside the U.S.</a> guide.</p>'
)

INTL_BLOG_CALLOUT = (
    '<p class="blog-region-note"><strong>Biologics and access abroad.</strong> '
    "Pair this article with our "
    '<a href="/guides/biologics-questions-for-your-doctor">questions for your doctor about biologics</a> '
    "and "
    '<a href="/guides/ibd-biologic-access-outside-us">biologic access outside the U.S.</a> '
    'guides when you need therapy decisions or help after a denial.</p>'
)

NEW_GUIDES = {
    "biologics-questions-for-your-doctor": {
        "slug": "biologics-questions-for-your-doctor",
        "category": "treatment",
        "keywords": [
            "which biologic for IBD",
            "biologic questions doctor",
            "ask gastroenterologist biologic",
            "IBD biologic choice",
            "infliximab vedolizumab questions",
        ],
        "title": "Biologic Questions for Your Doctor | IBD Shared Decision | IBDPal",
        "description": "Country-neutral questions to ask your gastroenterologist about biologic therapy in Crohn's and colitis. Not a drug picker. Education only.",
        "h1": "Biologic questions for your doctor",
        "intro": (
            "Patients in Lagos, London, Mumbai, and everywhere else ask the same question: "
            "which biologic should I request? IBDPal cannot answer that for you online. "
            "Drug choice belongs to you and your local IBD team, based on your disease, history, "
            "infection risk, and what is actually available where you live. This guide gives "
            "country-neutral questions and vocabulary so you can partner in that conversation. "
            "It is educational only and does not recommend starting, stopping, or switching any medicine."
        ),
        "sections": [
            {
                "heading": "Why no website can pick your biologic",
                "paragraphs": [
                    "Biologics and advanced small molecules are not interchangeable pills. "
                    "Anti-TNF drugs, integrin inhibitors, IL-12/23 blockers, and JAK inhibitors "
                    "work on different immune pathways. What helped a friend in another country "
                    "may not fit your disease location, prior failures, pregnancy plans, or local formulary.",
                    "Social media threads often name brand favorites. Clinicians instead match "
                    "class to inflammation pattern, strictures, fistulas, extraintestinal symptoms, "
                    "and monitoring capacity at your hospital. Your job is not to arrive with a "
                    "demanded drug name but to understand why a class is proposed and what success looks like.",
                    "If you read U.S.-centric articles about prior authorization, translate the "
                    "clinical parts (questions, monitoring, side effects) and ignore payer steps that "
                    "do not apply locally. Our biologic access outside the U.S. guide covers formulary "
                    "and denial topics for international readers.",
                ],
            },
            {
                "heading": "What your gastroenterologist weighs",
                "paragraphs": [
                    "Disease type and extent matter. Ulcerative colitis limited to the left colon "
                    "may follow different escalation paths than Crohn's with small-bowel strictures "
                    "or perianal disease. Prior colonoscopy, MRI, or calprotectin trends help your team "
                    "see whether inflammation is deep or mainly symptomatic.",
                    "Treatment history is central. Failure or intolerance of mesalamine, thiopurines, "
                    "methotrexate, or steroids shapes which biologic class is next. Some pathways "
                    "avoid repeating the same target after primary non-response.",
                    "Infection and vaccine status affect safety. Tuberculosis screening, hepatitis "
                    "history, and live vaccine timing are standard before many biologics worldwide. "
                    "Pregnancy plans, surgery dates, and joint or skin manifestations also steer choice.",
                    "Access is part of medicine, not a separate conversation. Ask early which "
                    "agents your hospital stocks, whether infusion chairs exist, and whether home "
                    "injection training is available. A perfect-on-paper drug helps no one if it "
                    "cannot be delivered locally.",
                ],
            },
            {
                "heading": "Generic names worth knowing",
                "paragraphs": [
                    "Brand names differ by country. Carry generic (INN) names on your medication list "
                    "so any clinic understands your history. Examples patients often discuss with "
                    "their teams include infliximab and adalimumab (anti-TNF), vedolizumab (integrin), "
                    "ustekinumab (IL-12/23), risankizumab (IL-23), and tofacitinib or upadacitinib (JAK inhibitors).",
                    "Biosimilars use the same generic stem as reference biologics with a manufacturer suffix. "
                    "Switching between biosimilar and reference product may be required by cost or policy. "
                    "Ask how your team monitors response after any switch.",
                    "Write both generic and local brand on a one-page summary. Photograph your pens or "
                    "infusion schedule. Translators at embassy clinics or telehealth visits rely on "
                    "accurate drug names, not marketing labels alone.",
                ],
            },
            {
                "heading": "Questions to bring to your appointment",
                "paragraphs": [
                    "Why is this class a fit for my disease type and severity right now? "
                    "What alternatives did you consider and rule out?",
                    "How will we know it is working, and on what timeline? Will we repeat "
                    "colonoscopy, calprotectin, CRP, or symptom scores at set intervals?",
                    "What monitoring labs or tests do I need before and during therapy? "
                    "Which infection symptoms should trigger a same-day call?",
                    "Infusion or injection: who teaches me, where do doses happen, and what are "
                    "missed-dose rules if travel or stock delays occur?",
                    "How does this interact with pregnancy plans, surgery, other autoimmune conditions, "
                    "or vaccines I still need?",
                    "If this fails or causes side effects, what is our next step and how long do we "
                    "wait before switching?",
                    "What does this cost locally, and who in your office helps with approvals or "
                    "patient assistance if I cannot pay out of pocket?",
                ],
            },
            {
                "heading": "When you are switching or starting after a failure",
                "paragraphs": [
                    "Secondary loss of response is common on long-term biologics. Drug levels, "
                    "antibodies, and adherence review precede switching. Do not stop doses without "
                    "a taper or replacement plan; rebound flares are real.",
                    "Bring a timeline of prior drugs, dates stopped, and why (side effect, non-response, "
                    "access gap). Gaps from insurance or import delays should be documented; they "
                    "affect how aggressively your team re-escalates.",
                    "Ask whether a washout period is needed between classes and how flare symptoms "
                    "will be bridged with steroids or other short-term tools.",
                ],
            },
            {
                "heading": "Tracking symptoms between visits",
                "paragraphs": [
                    "Week-by-week logs beat memory at short appointments. Note stool frequency, blood, "
                    "urgency, pain, fatigue, joint flares, and mood. IBDPal or a simple notebook works.",
                    "Photograph rashes or mouth ulcers if extraintestinal symptoms appear. They may "
                    "influence class choice even when gut symptoms seem stable.",
                    "Share logs before visits through portal upload or printed PDF so your clinician "
                    "sees trends, not only how you feel on appointment day.",
                ],
            },
        ],
        "tips": [
            "Print generic drug names alongside local brands on your medication card.",
            "Ask for a written induction and maintenance schedule before your first dose.",
            "Request a clinic contact for fever or infection symptoms on immunosuppression.",
            "Bring prior endoscopy reports when seeing a new IBD specialist.",
            "If access blocks your prescribed drug, ask the same questions about the next available agent.",
        ],
        "related": [
            {"label": "Biologic access outside the U.S.", "url": "/guides/ibd-biologic-access-outside-us"},
            {"label": "Biologics overview", "url": "/guides/biologics-crohns-colitis"},
            {"label": "Foundation medication guide", "url": "/guides/foundation-ibd-medication-guide"},
            {"label": "Understanding biologics article", "url": "/blog/understanding-biologics-ibd"},
            {"label": "IBD care outside the United States", "url": "/blog/ibd-care-outside-united-states"},
            {"label": "Doctor visit prep", "url": "/guides/crohns-doctor-visit-prep"},
        ],
        "faq": [
            {
                "q": "Should I ask for the newest biologic?",
                "a": "Ask why any proposed drug fits your case. Newer is not automatically better for every patient or budget.",
            },
            {
                "q": "Can I demand a specific brand I saw online?",
                "a": "Share what you read, but expect your clinician to explain local availability, evidence, and safety for you.",
            },
            {
                "q": "What if only one biologic is available locally?",
                "a": "Focus questions on monitoring, response timelines, and backup plans if it fails or is denied.",
            },
        ],
    },
    "ibd-biologic-access-outside-us": {
        "slug": "ibd-biologic-access-outside-us",
        "category": "treatment",
        "keywords": [
            "IBD biologics international",
            "biologic access abroad",
            "formulary denial IBD",
            "NHIS biologic Crohn's",
            "prior authorization outside US",
        ],
        "title": "IBD Biologic Access Outside the U.S. | Formulary & Denials | IBDPal",
        "description": "When U.S. insurance guides do not apply: formulary limits, denials, cost, biosimilars, and patient assistance for Crohn's and colitis abroad. Education only.",
        "h1": "Biologic access outside the United States",
        "intro": (
            "Much of the English-language IBD internet assumes American private insurance, specialty "
            "pharmacies, and Crohn's and Colitis Foundation appeal templates. If you live elsewhere, "
            "those steps may not exist or may look completely different. This guide explains how to "
            "navigate access, denials, and cost for biologics and advanced therapies when U.S. prior "
            "authorization articles do not match your system. It is educational only, not legal or "
            "financial advice, and cannot list every country's rules."
        ),
        "sections": [
            {
                "heading": "Why U.S. prior auth guides do not translate",
                "paragraphs": [
                    "U.S. articles describe employer plans, Medicare Part D, specialty pharmacies, "
                    "fax appeals, and state laws like step-therapy exceptions. Other countries may use "
                    "national formularies, hospital drug committees, single-payer reviews, private "
                    "insurers with different forms, or mostly out-of-pocket payment at pharmacies.",
                    "Denial in one system is not the end of conversation. It may mean requesting "
                    "hospital exception, submitting extra documentation to a national body, paying "
                    "privately, joining a clinical trial, or switching to a biosimilar on formulary.",
                    "Use U.S. guides for vocabulary (medical necessity, step therapy, biosimilar) "
                    "but follow local staff who know which forms and timelines actually apply.",
                ],
            },
            {
                "heading": "How access differs by health system",
                "paragraphs": [
                    "Single-payer or national insurance programs often publish approved drug lists. "
                    "If your biologic is not listed, clinicians may apply for exceptional funding with "
                    "evidence from scopes, labs, and prior drug trials.",
                    "Private insurance in many countries still requires pre-approval, but call centers, "
                    "languages, and appeal windows differ. Keep policy numbers, denial letters, and "
                    "reference IDs exactly as issued.",
                    "Cash payment or partial hospital subsidy may be the only route in some settings. "
                    "Ask social workers or patient navigators about charitable funds, manufacturer "
                    "programs, and nonprofit assistance before assuming a drug is unreachable.",
                    "Rural or low-resource areas may lack infusion centers. Home injection training "
                    "or traveling to a tertiary hospital may be required even after approval.",
                ],
            },
            {
                "heading": "What to ask your local IBD team",
                "paragraphs": [
                    "Which biologics and advanced small molecules can this hospital actually procure?",
                    "What documentation does our payer or ministry require for first-line versus "
                    "second-line biologic use?",
                    "Who submits requests: the doctor, hospital pharmacy, or me as the patient?",
                    "Typical wait times after submission, and who do I call if symptoms worsen during the wait?",
                    "If denied, what is the formal appeal path here (internal review, external panel, "
                    "patient ombudsman, judicial complaint)?",
                    "Are biosimilars mandatory before reference brands, and how is switching monitored?",
                    "Is there a bridge supply, sample program, or trial option while paperwork processes?",
                ],
            },
            {
                "heading": "When a plan or hospital denies therapy",
                "paragraphs": [
                    "Save every denial letter, email, and call log with dates and staff names. "
                    "Missing deadlines resets many appeals worldwide.",
                    "Gather objective records: diagnosis codes, colonoscopy summaries, imaging, "
                    "calprotectin or CRP trends, hospitalizations, and prior medications with dates "
                    "and reasons stopped.",
                    "Your clinician's letter should state harm risk if treatment is delayed, not only "
                    "that you prefer a brand. Patient impact statements (work, school, caregiving loss) "
                    "supplement but rarely replace clinical evidence.",
                    "If appeals fail, ask about formulary alternatives in the same class, clinical trials, "
                    "or compassionate use programs run by manufacturers. Second opinions at university "
                    "hospitals sometimes unlock pathways community clinics cannot access.",
                ],
            },
            {
                "heading": "Cost, biosimilars, and import questions",
                "paragraphs": [
                    "Biosimilars can reduce cost with similar efficacy for many IBD patients. Policy "
                    "may force biosimilar first even when reference brands dominate social media.",
                    "Importing biologics by mail carries legal, customs, and cold-chain risks that vary "
                    "by country. Manufacturer travel or relocation programs are safer when available.",
                    "Compare total cost: drug, infusion fees, labs, and travel. A cheaper pen on paper "
                    "may cost more if monitoring requires distant city visits monthly.",
                ],
            },
            {
                "heading": "When biologics are not on formulary yet",
                "paragraphs": [
                    "Some patients face months or years before advanced therapy is funded. During that window, optimize "
                    "conventional immunomodulators, nutrition support, and flare plans with your team. Document every "
                    "hospitalization and failed drug trial; those records become the backbone of later exceptional funding requests.",
                    "University hospitals and IBD centers in major cities often participate in trials or early-access "
                    "programs before national formularies update. Ask whether your referral center has research nurses who "
                    "track open studies for Crohn's disease and ulcerative colitis.",
                    "Patient advocacy groups in your country may publish translated explainers on how to navigate "
                    "ministries of health or private appeals. They cannot prescribe, but they sometimes know which "
                    "documents local reviewers expect.",
                ],
            },
            {
                "heading": "Build a portable record kit",
                "paragraphs": [
                    "Keep PDF or paper copies of diagnosis, surgeries, generic drug names with doses, "
                    "allergies, last colonoscopy summary, and clinician contact. Translate key pages if "
                    "you cross language borders.",
                    "Download portal records before travel; apps may not work abroad. An IBD passport "
                    "style summary helps emergency rooms and new specialists act quickly.",
                    "When relocating permanently, request referral letters and histology slides early. "
                    "Formulary changes often force brand switches; plan refills before you move.",
                ],
            },
        ],
        "tips": [
            "Photograph denial letters and insurance cards; store encrypted backups.",
            "Ask for generic drug names on every prescription.",
            "Contact manufacturer patient support lines for travel or relocation logistics.",
            "Never stop a biologic without a clinician plan while waiting on approvals.",
            "Pair this guide with country-neutral questions for your doctor before every switch.",
        ],
        "related": [
            {"label": "Biologic questions for your doctor", "url": "/guides/biologics-questions-for-your-doctor"},
            {"label": "IBD care outside the United States", "url": "/blog/ibd-care-outside-united-states"},
            {"label": "U.S. prior authorization guide", "url": "/guides/ibd-prior-authorization-foundation"},
            {"label": "Biologics overview", "url": "/guides/biologics-crohns-colitis"},
            {"label": "Foundation clinical trials guide", "url": "/guides/foundation-ibd-clinical-trials"},
            {"label": "Travel planning guide", "url": "/guides/ibd-travel-planning"},
        ],
        "faq": [
            {
                "q": "Is Humira or Entyvio available everywhere?",
                "a": "No. Brand availability and approval status differ by country and hospital. Use generic names and ask locally.",
            },
            {
                "q": "What if my country has no biologics on formulary?",
                "a": "Discuss steroids, immunomodulators, nutrition therapy, trials, and exceptional funding routes with your IBD center.",
            },
            {
                "q": "Can I use U.S. appeal letter templates abroad?",
                "a": "Use them as structure for clinical facts, but your doctor must adapt to local payer or hospital requirements.",
            },
        ],
    },
}


def word_count(page: dict) -> int:
    parts: list[str] = [page.get("intro", "")]
    for sec in page.get("sections", []):
        parts.append(sec.get("heading", ""))
        parts.extend(sec.get("paragraphs", []))
    parts.extend(page.get("tips", []) or [])
    for item in page.get("faq", []) or []:
        parts.append(item.get("q", ""))
        parts.append(item.get("a", ""))
    return len(re.findall(r"\b[\w']+\b", " ".join(parts)))


def insert_after_slug(pages: list[dict], after: str, new_pages: list[dict]) -> list[dict]:
    out: list[dict] = []
    inserted = False
    for p in pages:
        out.append(p)
        if p["slug"] == after and not inserted:
            out.extend(new_pages)
            inserted = True
    if not inserted:
        out.extend(new_pages)
    return out


def patch_guide_expansion(slug: str, patch_fn) -> None:
    expansions = json.loads(GUIDE_EXP.read_text(encoding="utf-8"))
    if slug not in expansions:
        raise KeyError(slug)
    patch_fn(expansions[slug])
    GUIDE_EXP.write_text(json.dumps(expansions, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def patch_blog_html(slug: str, callout: str) -> None:
    path = BLOGS / f"{slug}.html"
    text = path.read_text(encoding="utf-8")
    marker = 'class="blog-edu-disclaimer"'
    if "blog-region-note" in text:
        return
    idx = text.find(marker)
    if idx == -1:
        print(f"WARN: no disclaimer in {slug}")
        return
    end = text.find("</p>", idx)
    if end == -1:
        return
    insert_at = end + len("</p>")
    text = text[:insert_at] + "\n" + callout + text[insert_at:]
    path.write_text(text, encoding="utf-8")
    print(f"Patched blog {slug}")


def main() -> None:
    # --- seo-landing-pages.json stubs ---
    data = json.loads(SEO_PAGES.read_text(encoding="utf-8"))
    existing = {p["slug"] for p in data["pages"]}
    stubs = []
    for slug, guide in NEW_GUIDES.items():
        if slug in existing:
            continue
        stubs.append({k: guide[k] for k in ("slug", "category", "keywords", "title", "description", "h1", "intro")})
        stubs[-1]["sections"] = []
        stubs[-1]["related"] = []
        stubs[-1]["faq"] = []
    if stubs:
        data["pages"] = insert_after_slug(data["pages"], "biologics-crohns-colitis", stubs)
        SEO_PAGES.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Added {len(stubs)} guide stubs to seo-landing-pages.json")

    # --- guide-expansions.json ---
    expansions = json.loads(GUIDE_EXP.read_text(encoding="utf-8"))
    for slug, guide in NEW_GUIDES.items():
        expansions[slug] = {
            "intro": guide["intro"],
            "sections": guide["sections"],
            "tips": guide["tips"],
            "faq": guide["faq"],
            "related": guide["related"],
            "description": guide["description"],
        }
        wc = word_count(guide)
        print(f"  {slug}: {wc} words")
        if wc < 750:
            print(f"WARN: {slug} under 750 words", file=sys.stderr)

    # US disclaimers on prior-auth cluster
    def patch_pa_intro(entry: dict) -> None:
        intro = entry.get("intro", "")
        if "Reading outside the United States" not in intro:
            entry["intro"] = intro + " " + INTL_NOTE

    def patch_biologics_insurance(entry: dict) -> None:
        for sec in entry.get("sections", []):
            if sec.get("heading", "").startswith("Insurance"):
                sec["heading"] = "Insurance, prior auth, and appeals (United States)"
                note = (
                    "Readers outside the United States should use our biologic access outside the U.S. "
                    "and biologic questions for your doctor guides instead of U.S. payer steps below."
                )
                if note not in " ".join(sec.get("paragraphs", [])):
                    sec["paragraphs"] = [note] + sec["paragraphs"]
        related = entry.get("related") or []
        for link in (
            {"label": "Biologic questions for your doctor", "url": "/guides/biologics-questions-for-your-doctor"},
            {"label": "Biologic access outside the U.S.", "url": "/guides/ibd-biologic-access-outside-us"},
        ):
            if not any(r.get("url") == link["url"] for r in related):
                related.insert(0, link)
        entry["related"] = related

    for slug in (
        "ibd-prior-authorization-foundation",
        "foundation-ibd-appeal-letters",
        "step-therapy-safe-step-act-ibd",
    ):
        if slug in expansions:
            patch_pa_intro(expansions[slug])

    if "biologics-crohns-colitis" in expansions:
        patch_biologics_insurance(expansions["biologics-crohns-colitis"])

    GUIDE_EXP.write_text(json.dumps(expansions, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # --- seo-expansion.json hubs ---
    seo_exp = json.loads(SEO_EXP.read_text(encoding="utf-8"))
    for hub in seo_exp["hubs"]:
        if hub["slug"] != "crohns-disease":
            continue
        guides = hub.setdefault("guides", [])
        for link in (
            {"url": "/guides/biologics-questions-for-your-doctor", "label": "Biologic questions for your doctor"},
            {"url": "/guides/ibd-biologic-access-outside-us", "label": "Biologic access outside the U.S."},
        ):
            if not any(g.get("url") == link["url"] for g in guides):
                guides.insert(3, link)
        blog_slugs = hub.setdefault("blog_slugs", [])
        if "ibd-care-outside-united-states" not in blog_slugs:
            blog_slugs.append("ibd-care-outside-united-states")
    SEO_EXP.write_text(json.dumps(seo_exp, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # --- keywords ---
    kw = json.loads(KEYWORDS.read_text(encoding="utf-8"))
    kw["guides/biologics-questions-for-your-doctor"] = NEW_GUIDES["biologics-questions-for-your-doctor"]["keywords"]
    kw["guides/ibd-biologic-access-outside-us"] = NEW_GUIDES["ibd-biologic-access-outside-us"]["keywords"]
    KEYWORDS.write_text(json.dumps(kw, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # --- blog expansions: prepend US note to insurance posts ---
    blog_exp = json.loads(BLOG_EXP.read_text(encoding="utf-8"))
    us_note_html = (
        '<h2>United States focus</h2>'
        "<p>This article describes U.S. insurance, prior authorization, and appeal workflows. "
        "If you live outside the U.S., start with our "
        '<a href="/guides/ibd-biologic-access-outside-us">biologic access outside the U.S.</a> '
        "guide and "
        '<a href="/guides/biologics-questions-for-your-doctor">biologic questions for your doctor</a> '
        "guide instead.</p>"
    )
    for slug in ("insurance-biologics-ibd", "prior-authorization-biologics-timeline"):
        entry = blog_exp.setdefault(slug, {})
        append = entry.get("append_body", "")
        if "United States focus" not in append:
            entry["append_body"] = us_note_html + append
    ibd_intl = blog_exp.get("ibd-care-outside-united-states", {})
    append = ibd_intl.get("append_body", "")
    intl_links = (
        '<h2>Biologic therapy decisions abroad</h2>'
        "<p>When readers ask which biologic to request or what to do after a denial, pair this article with "
        'our <a href="/guides/biologics-questions-for-your-doctor">biologic questions for your doctor</a> '
        'and <a href="/guides/ibd-biologic-access-outside-us">biologic access outside the U.S.</a> guides.</p>'
    )
    if "Biologic therapy decisions abroad" not in append:
        ibd_intl["append_body"] = intl_links + append
        blog_exp["ibd-care-outside-united-states"] = ibd_intl
    BLOG_EXP.write_text(json.dumps(blog_exp, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # Regenerate
    for script in ("apply_guide_expansions.py", "generate_seo_landings.py"):
        subprocess.run([PYTHON, str(ROOT / "scripts" / script)], check=True, cwd=ROOT)

    # Patch blog HTML (expansion marker may block re-merge; patch directly)
    for slug in ("insurance-biologics-ibd", "prior-authorization-biologics-timeline"):
        patch_blog_html(slug, US_BLOG_CALLOUT)
    patch_blog_html("ibd-care-outside-united-states", INTL_BLOG_CALLOUT)

    subprocess.run([PYTHON, str(ROOT / "scripts" / "sync_all_seo.py")], check=True, cwd=ROOT)
    print("\nDone. Two international biologic guides added and prior-auth pages updated.")


if __name__ == "__main__":
    main()
