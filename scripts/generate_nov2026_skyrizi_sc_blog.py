#!/usr/bin/env python3
# Prose style: do not use em dash. Use periods, commas, colons, or "|" in titles.
"""Generate Nov 2026 Skyrizi subcutaneous induction explainer for adult Crohn's."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
VERCEL = ROOT / "vercel.json"
SEARCH_GAP = ROOT / "data" / "search-gap-posts.json"
ALIASES = ROOT / "data" / "search-aliases.json"
DATA = ROOT / "data" / "nov2026-skyrizi-sc-induction.json"
FALLBACK = BLOGS / "assets" / "skyrizi-ibd" / "skyrizi-ibd_1.jpg"

sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402

DATE_ISO = "2026-11-01T23:30:00Z"
DATE_DISPLAY = "November 1, 2026"
MIN_WORDS = 1000
SLUG = "skyrizi-subcutaneous-induction-crohns"

POST = {
    "slug": SLUG,
    "title": "Skyrizi Subcutaneous Induction for Crohn's: What the FDA Change Means",
    "description": (
        "FDA approved subcutaneous Skyrizi induction for adults with moderate to severe "
        "Crohn's disease (Oct 2026). Home on-body injector, AFFIRM results, TB label update, "
        "and clinic questions. Education only."
    ),
    "category": "Treatment · November 2026",
    "date_display": DATE_DISPLAY,
    "date_iso": DATE_ISO,
    "asset_dir": "skyrizi-ibd",
    "images": ["skyrizi-ibd_1.jpg"],
    "alts": ["Medication education image for Skyrizi and Crohn's disease questions"],
    "share": (
        "Skyrizi SC induction for adult Crohn's: home start option, trial results, "
        "and clinic questions. Education only."
    ),
    "resource_category": "treatment",
    "match_terms": [
        "skyrizi subcutaneous induction",
        "skyrizi sc induction",
        "skyrizi home induction",
        "skyrizi on body injector",
        "risankizumab subcutaneous induction",
        "skyrizi start at home",
        "skyrizi affirm trial",
        "skyrizi crohn's induction",
    ],
    "tags": [
        "Skyrizi",
        "risankizumab",
        "IL-23",
        "Crohn's",
        "biologic",
        "subcutaneous",
        "induction",
        "FDA",
    ],
    "body": """
<p>On <strong>October 23, 2026</strong>, the FDA approved a <strong>subcutaneous induction regimen</strong> of <strong>SKYRIZI (risankizumab-rzaa)</strong> for adults with moderately to severely active Crohn's disease. That means some people may start Skyrizi at home with an on-body injector pack, then continue every-eight-week subcutaneous maintenance, instead of beginning with intravenous (IV) induction in an infusion center. IV induction remains an option. This page translates the label change into plain patient language. It is education only, not prescribing advice, and it is not a reason to change your dose without your gastroenterology team.</p>
<p>Read alongside <a href="/blog/skyrizi-patient-questions-ibd">Skyrizi patient questions</a>, <a href="/blog/starting-biologic-what-to-expect-ibd">starting a biologic</a>, <a href="/blog/infusion-day-what-to-expect">infusion day expectations</a>, <a href="/blog/prior-authorization-biologics-timeline">prior authorization timing</a>, and the <a href="/#news">latest IBD news</a> card on this approval.</p>

<h2>What changed in plain words</h2>
<p>Before this update, many adults with Crohn's who started Skyrizi began with IV induction doses in a clinic, then moved to subcutaneous maintenance. The new approval adds an alternative induction path that uses subcutaneous doses delivered with an on-body injector (OBI) induction pack. After induction, maintenance continues with an OBI every eight weeks for people on that pathway.</p>
<p>Why patients care: fewer early infusion-chair hours, more flexibility for work and school schedules, and a clearer home-start story when insurance and training align. Why clinicians still decide: disease severity, prior therapy failure, infection risk, teaching needs, and coverage rules can favor IV or SC induction for a given person.</p>

<h2>Who this FDA update applies to</h2>
<ul class="blog-list">
<li><strong>Adults</strong> with moderately to severely active Crohn's disease</li>
<li>People whose team is considering Skyrizi as an advanced therapy</li>
<li>Not a guarantee that every pharmacy, insurer, or clinic will offer the home induction pack immediately</li>
<li>Not automatic permission to self-start without training, labs, and a written plan</li>
</ul>
<p>Pediatric Crohn's and ulcerative colitis labeling questions are separate conversations. If you are under 18, ask your pediatric IBD team which products and routes are labeled for your age and disease.</p>

<h2>What the AFFIRM trial reported</h2>
<p>Approval was supported by the Phase 3 <strong>AFFIRM</strong> study of subcutaneous Skyrizi versus placebo in adults with moderately to severely active Crohn's disease. In public summaries of the overall population, week-12 clinical remission was about <strong>55%</strong> with SC induction versus about <strong>30%</strong> with placebo, and endoscopic response was about <strong>44%</strong> versus about <strong>14%</strong>. Manufacturer materials also highlight especially strong results among people without prior advanced therapy failure (advanced therapy-naive), including clinical remission around three-quarters and endoscopic response several times higher than placebo in that subgroup.</p>
<p>How to read those numbers without over-promising:</p>
<ul class="blog-list">
<li>Trial averages are not your personal odds. Prior biologics, disease location, smoking, and steroids all matter.</li>
<li>Endoscopic response means the bowel looked better on scope criteria used in the trial. Feeling better and looking better can move on different clocks.</li>
<li>Placebo arms remind us that some people improve without the active drug. That is why controlled trials exist.</li>
<li>Safety in AFFIRM was described as generally consistent with the known Skyrizi profile in Crohn's, with no new safety risks called out in the manufacturer announcement. Your own infection and TB assessment still belongs in clinic.</li>
</ul>

<h2>IV induction versus subcutaneous induction</h2>
<ul class="blog-list">
<li><strong>Where doses start:</strong> IV induction happens in an infusion center. SC induction can start at home or in clinic teaching with an on-body injector pack.</li>
<li><strong>Early logistics:</strong> IV means travel, chair time, and IV access. SC means device training, storage, and injection-site planning.</li>
<li><strong>Maintenance:</strong> Many IV starters later move to SC every 8 weeks when appropriate. The SC induction pathway continues SC every 8 weeks on the labeled OBI schedule.</li>
<li><strong>Still required either way:</strong> baseline labs, infection screening as directed, and follow-up. SC adds device teaching.</li>
</ul>
<p>Neither route is "better" for every person. Some people prefer clinic observation for the first doses. Others need home induction to keep a job or caregiving schedule. Ask which route your team recommends for your disease pattern and support system.</p>

<h2>On-body injector: practical questions to ask</h2>
<ul class="blog-list">
<li>Who teaches the first application, and do I need a nurse visit or video teach-back?</li>
<li>Where on my body is preferred, and how do I rotate sites?</li>
<li>How is the induction pack shipped, stored, and warmed before use?</li>
<li>What do I do if the device fails to start, leaks, or falls off?</li>
<li>Who do I call after hours if a dose is missed or interrupted?</li>
<li>How does specialty pharmacy timing line up with my first clinic follow-up?</li>
</ul>
<p>Write the answers in your phone notes the same day. Device anxiety is common and solvable with repetition, not with silent guessing.</p>

<h2>Tuberculosis label update on the same letter</h2>
<p>Along with SC induction, the FDA also updated Skyrizi prescribing language on tuberculosis evaluation across indications. Public announcements describe more room for clinician judgment about whether TB testing is needed before starting, rather than framing a mandatory test for every start. That does not mean TB risk disappeared. It means your team may individualize screening based on your history, exposures, and local practice. Ask what screening they still want for you before dose one.</p>

<h2>Insurance, prior authorization, and pharmacy realities</h2>
<p>Labeling and coverage are related but not identical. A newly approved route can still take weeks to appear correctly on prior auth forms, specialty pharmacy inventories, and step-therapy rules. Bring these clinic script lines:</p>
<ul class="blog-list">
<li>"Is my authorization written for subcutaneous induction, IV induction, or both?"</li>
<li>"Will the specialty pharmacy ship the induction pack before my target start date?"</li>
<li>"If the SC pack is delayed, is IV induction still covered as a bridge?"</li>
<li>"What documentation do we need if the insurer prefers a different IL-23 or anti-TNF first?"</li>
</ul>
<p>See also <a href="/blog/insurance-biologics-ibd">insurance and biologics</a> and <a href="/guides/ibd-prior-authorization-foundation">Foundation prior authorization guidance</a> for process education.</p>

<h2>Safety themes to review with your team</h2>
<p>Skyrizi is an IL-23 pathway biologic used in IBD and other inflammatory diseases. Common teaching themes include infection risk awareness, vaccination timing before or during immunosuppression, injection-site reactions, and when to report fever, cough, unexplained weight loss, or new neurologic symptoms. Your personal risk depends on combination therapies (for example steroids), nutrition status, and other medical conditions. Do not stop or skip doses because of internet anecdotes. Call the clinic with specific symptoms.</p>

<h2>How to track the first 12 weeks</h2>
<p>Week 12 is the AFFIRM primary look, but your life is weekly. In IBDPal or a simple notebook, log:</p>
<ul class="blog-list">
<li>Stool frequency, night stools, blood, and urgency score</li>
<li>Pain location and energy</li>
<li>Weight trend and appetite</li>
<li>Injection dates, sites, and any device problems</li>
<li>Steroid dose if you are tapering</li>
<li>Questions for the next portal message</li>
</ul>
<p>Bring a one-page summary to the first follow-up after induction. Teams make better decisions with patterns than with a single dramatic day.</p>

<h2>Questions people are already searching</h2>
<h3>Can I start Skyrizi at home now?</h3>
<p>Only if your clinician chooses the SC induction pathway, you complete required screening and teaching, and the pharmacy supplies the correct induction pack. Home start is an option, not an automatic switch.</p>
<h3>Is SC induction as strong as IV induction?</h3>
<p>AFFIRM tested the SC induction regimen against placebo and met its co-primary endpoints. Your team still chooses between labeled IV and SC starts based on your case. Ask them how they weigh chair time, prior failures, and monitoring needs for you.</p>
<h3>Does this change ulcerative colitis dosing?</h3>
<p>This October 2026 headline is about Crohn's SC induction. UC labeling and your own indication are separate. Confirm the indication on your prescription bottle and authorization letter.</p>
<h3>What if I already finished IV induction?</h3>
<p>Most people already on maintenance do not "redo" induction because a new route was approved. Ask only if your team is changing strategy after a loss of response or a coverage shift.</p>

<h2>When to seek prompt care</h2>
<p>Contact your IBD team urgently for high fever, severe abdominal pain, persistent vomiting, inability to keep fluids down, heavy bleeding, signs of dehydration, or any symptom that feels medically wrong after a dose. Device problems that leave you unsure whether a full dose was delivered also deserve a same-day call so the team can advise next steps.</p>

<h2>Clinic checklist before dose one</h2>
<ul class="blog-list">
<li>Confirm Crohn's indication and adult status on the order</li>
<li>Confirm IV versus SC induction on the written plan</li>
<li>Review infection and TB screening decisions for you</li>
<li>Schedule device teaching and a teach-back</li>
<li>Align specialty pharmacy ship date with your calendar</li>
<li>Set the first follow-up and lab plan</li>
<li>Save after-hours numbers before the first home dose</li>
</ul>

<p>Related reading: <a href="/blog/skyrizi-patient-questions-ibd">Skyrizi questions</a> · <a href="/blog/stelara-patient-guide-ibd">Stelara guide</a> · <a href="/blog/humira-fatigue-ibd">adalimumab fatigue notes</a> · <a href="/blog/biologics-flying-travel-ibd">biologics and travel</a> · <a href="/#news-partners">manufacturer support programs</a> · <a href="/ask">Ask</a>.</p>
<p>Education supports shared decisions. It does not replace your gastroenterologist, specialty pharmacist, or emergency services. If your symptoms escalate, use your clinic's urgent pathway rather than waiting for the next scheduled infusion teaching slot.</p>
""".strip(),
}


def word_count(html_body: str) -> int:
    text = html_body
    for tag in ("</p>", "</li>", "</h2>", "</h3>", "</td>", "</th>"):
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


def ensure_image() -> None:
    asset = BLOGS / "assets" / POST["asset_dir"]
    asset.mkdir(parents=True, exist_ok=True)
    dest = asset / POST["images"][0]
    if dest.exists() and dest.stat().st_size >= 1000:
        return
    if FALLBACK.exists():
        shutil.copy(FALLBACK, dest)


def patch_vercel(slug: str) -> None:
    text = VERCEL.read_text(encoding="utf-8")
    needle = f'"/blog/{slug}"'
    if needle in text:
        return
    insert = (
        f'    {{\n      "source": "/blog/{slug}",\n'
        f'      "destination": "/blogs/{slug}.html"\n    }},'
    )
    text = text.replace('"rewrites": [\n', '"rewrites": [\n' + insert + "\n")
    VERCEL.write_text(text, encoding="utf-8")
    print("patched vercel.json")


def update_search_gap() -> None:
    data = {"posts": []}
    if SEARCH_GAP.exists():
        data = json.loads(SEARCH_GAP.read_text(encoding="utf-8"))
        if isinstance(data, list):
            data = {"posts": data}
    by_slug = {p["slug"]: p for p in data.get("posts", [])}
    by_slug[POST["slug"]] = {
        "slug": POST["slug"],
        "match_terms": POST["match_terms"],
        "title": POST["title"],
        "description": POST["description"],
        "category": POST["category"],
        "date_display": POST["date_display"],
        "date_iso": POST["date_iso"],
        "asset_dir": POST["asset_dir"],
        "resource_category": POST["resource_category"],
        "tags": POST["tags"],
    }
    data["posts"] = list(by_slug.values())
    SEARCH_GAP.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("updated search-gap-posts.json")


def update_aliases() -> None:
    data = json.loads(ALIASES.read_text(encoding="utf-8"))
    extras = {
        "skyrizi subcutaneous induction": "skyrizi",
        "skyrizi sc induction": "skyrizi",
        "skyrizi home induction": "skyrizi",
        "skyrizi on body injector": "skyrizi",
        "risankizumab subcutaneous induction": "skyrizi",
        "skyrizi start at home": "skyrizi",
        "skyrizi affirm": "skyrizi",
        "skyrizi crohn's induction": "skyrizi",
    }
    data.update(extras)
    ALIASES.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("updated search-aliases.json")


def main() -> None:
    ensure_image()
    wc = word_count(POST["body"])
    if wc < MIN_WORDS:
        raise SystemExit(f"too short: {POST['slug']} ({wc})")
    DATA.write_text(json.dumps(POST, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    out = BLOGS / f"{POST['slug']}.html"
    out.write_text(render_post(POST), encoding="utf-8")
    print(f"wrote {out.name} (~{wc} words)")
    patch_vercel(POST["slug"])
    update_search_gap()
    update_aliases()
    print("Done.")


if __name__ == "__main__":
    main()
