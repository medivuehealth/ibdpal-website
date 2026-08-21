#!/usr/bin/env python3
# Prose style: do not use em dash.
"""Generate Eureka Top-5 traffic blogs: decoder, drug×life, mythbusters, world staples."""
from __future__ import annotations

import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
DATA = ROOT / "data" / "eureka-top5-posts.json"
SITEMAP = ROOT / "sitemap.xml"
VERCEL = ROOT / "vercel.json"
SITE = "https://www.ibdpal.org"
FALLBACK = BLOGS / "assets" / "low-residue" / "low-residue_1.jpg"

sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402

IMAGE_URLS = {
    "yellow-stool": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&w=1200&q=80",
    "green-stool": "https://images.unsplash.com/photo-1581594693700-67d5ffa0a1b3?auto=format&w=1200&q=80",
    "black-stool": "https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&w=1200&q=80",
    "floating-stool": "https://images.unsplash.com/photo-1576091160550-2173dba999ef?auto=format&w=1200&q=80",
    "pencil-stool": "https://images.unsplash.com/photo-1631815588090-d4bfec5b1ccb?auto=format&w=1200&q=80",
    "bristol-ibd": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&w=1200&q=80",
    "mucus-stool": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&w=1200&q=80",
    "calprotectin-high": "https://images.unsplash.com/photo-1579154204601-01588f351e67?auto=format&w=1200&q=80",
    "crp-normal": "https://images.unsplash.com/photo-1576671081837-49000212a370?auto=format&w=1200&q=80",
    "pale-stool": "https://images.unsplash.com/photo-1581595220892-b0739db3b8c5?auto=format&w=1200&q=80",
    "humira-fatigue": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&w=1200&q=80",
    "stelara-diet": "https://images.unsplash.com/photo-1490645935967-10de6ba17061?auto=format&w=1200&q=80",
    "skyrizi-ibd": "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?auto=format&w=1200&q=80",
    "rinvoq-ibd": "https://images.unsplash.com/photo-1471864190281-a93a3070b6de?auto=format&w=1200&q=80",
    "remicade-tips": "https://images.unsplash.com/photo-1516549655169-df83a0774514?auto=format&w=1200&q=80",
    "prednisone-diet": "https://images.unsplash.com/photo-1498837167922-ddd27525d352?auto=format&w=1200&q=80",
    "mtx-alcohol": "https://images.unsplash.com/photo-1471864190281-a93a3070b6de?auto=format&w=1200&q=80",
    "biologics-travel": "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?auto=format&w=1200&q=80",
    "carnivore-myth": "https://images.unsplash.com/photo-1558030006-450675393462?auto=format&w=1200&q=80",
    "bone-broth": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&w=1200&q=80",
    "juice-detox": "https://images.unsplash.com/photo-1622597467836-f3285f2131b8?auto=format&w=1200&q=80",
    "if-fasting": "https://images.unsplash.com/photo-1490645935967-10de6ba17061?auto=format&w=1200&q=80",
    "collagen-ibd": "https://images.unsplash.com/photo-1556228578-0d85b1a4d571?auto=format&w=1200&q=80",
    "leaky-gut": "https://images.unsplash.com/photo-1559757175-5700dde675bc?auto=format&w=1200&q=80",
    "chapati-ibd": "https://images.unsplash.com/photo-1565557623262-b51c2513a641?auto=format&w=1200&q=80",
    "dal-ibd": "https://images.unsplash.com/photo-1546833999-b9f581a1996d?auto=format&w=1200&q=80",
    "congee-ibd": "https://images.unsplash.com/photo-1536304993881-ff6e9eefa2a6?auto=format&w=1200&q=80",
    "miso-ibd": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&w=1200&q=80",
    "kimchi-ibd": "https://images.unsplash.com/photo-1583224964978-240ee87d0b6b?auto=format&w=1200&q=80",
    "plantain-ibd": "https://images.unsplash.com/photo-1603833665858-e61d17a86224?auto=format&w=1200&q=80",
    "tortilla-ibd": "https://images.unsplash.com/photo-1565299585323-38d6b0865b47?auto=format&w=1200&q=80",
    "couscous-ibd": "https://images.unsplash.com/photo-1516684668137-632fa0f0a5a0?auto=format&w=1200&q=80",
    "dates-ibd": "https://images.unsplash.com/photo-1606313564200-e75d5e30476c?auto=format&w=1200&q=80",
    "paneer-ibd": "https://images.unsplash.com/photo-1631452180519-c014fe946bc7?auto=format&w=1200&q=80",
}


def edu_body(p: dict) -> str:
    bullets = lambda key: "".join(f"<li>{x}</li>" for x in p[key])
    myths = "".join(f"<li><strong>{a}</strong> {b}</li>" for a, b in p["myths"])
    related = " · ".join(f'<a href="{u}">{t}</a>' for u, t in p["related"])
    return f"""
<p>{p['lead']}</p>
<h2>{p['h2_context']}</h2>
<p>{p['context']}</p>
<ul class="blog-list">{bullets('points')}</ul>
<h2>{p['h2_action']}</h2>
<ul class="blog-list">{bullets('actions')}</ul>
<p>{p['action_note']}</p>
<h2>When to seek care promptly</h2>
<ul class="blog-list">{bullets('urgent')}</ul>
<p>This page cannot diagnose you. Severe bleeding, black tarry stools, fainting, fever with rapid decline, or inability to keep fluids down need urgent evaluation. See <a href="/blog/when-to-go-er-ibd">when to go to the ER</a> and <a href="/flare-help">flare help</a>.</p>
<h2>Common myths</h2>
<ul class="blog-list">{myths}</ul>
<h2>Questions for your gastroenterologist</h2>
<ul class="blog-list">{bullets('questions')}</ul>
<p>Track patterns in IBDPal and bring a one-week log to visits. Related: {related}. Hub: <a href="/stool-labs-decoder">stool and labs decoder</a>.</p>
""".strip()


def food_body(f: dict) -> str:
    macros = "".join(f"<li><strong>{k}:</strong> {v}</li>" for k, v in f["macros"])
    micros = "".join(f"<li><strong>{k}:</strong> {v}</li>" for k, v in f["micros"])
    flare = "".join(f"<li>{x}</li>" for x in f["flare_tips"])
    rem = "".join(f"<li>{x}</li>" for x in f["remission_tips"])
    myths = "".join(f"<li><strong>{a}</strong> {b}</li>" for a, b in f["myths"])
    qs = "".join(f"<li>{x}</li>" for x in f["questions"])
    related = " · ".join(f'<a href="{u}">{t}</a>' for u, t in f["related"])
    name_l = f["name"].lower()
    return f"""
<p>Searches like <strong>{f['primary_kw']}</strong> and <strong>{f['secondary_kw']}</strong> are common worldwide. Tolerance with Crohn's or ulcerative colitis is individual. Education only, not a prescription to eat or avoid {name_l}.</p>
<h2>Nutrition snapshot: {f['name']}</h2>
<p>{f['nutrition_intro']}</p>
<ul class="blog-list">{macros}</ul>
<ul class="blog-list">{micros}</ul>
<h2>Flare versus remission</h2>
<p>{f['tolerance_intro']}</p>
<h3>During a flare</h3>
<ul class="blog-list">{flare}</ul>
<h3>In remission</h3>
<ul class="blog-list">{rem}</ul>
<h2>Prep ideas</h2>
<p>{f['prep']}</p>
<h2>Myths</h2>
<ul class="blog-list">{myths}</ul>
<h2>Questions for your care team</h2>
<ul class="blog-list">{qs}</ul>
<p>Log form and portion in IBDPal. Related: {related}. Hub: <a href="/ibd-nutrition">IBD nutrition</a>.</p>
""".strip()


def post(meta: dict, body: str) -> dict:
    return {
        **meta,
        "images": [f"{meta['asset_dir']}_1.jpg"],
        "alts": [meta.get("alt") or meta["title"]],
        "body": body,
        "share": meta.get("share") or meta["description"][:120],
    }


# --- 1) Decoder (10) ---
DECODER = [
    dict(
        slug="yellow-stool-ibd", title="Yellow Stool With IBD: Fat Malabsorption and Other Causes",
        description="Yellow stool with Crohn's or colitis: bile, fat malabsorption, diet, infection clues, and when to call your GI. Education only.",
        category="Wellness · August 2026", date_display="August 31, 2026", date_iso="2026-08-31T16:00:00Z",
        asset_dir="yellow-stool", resource_category="wellness",
        tags=["yellow stool", "steatorrhea", "bile", "malabsorption", "Crohn's", "colitis"],
        lead="Yellow stool searches spike after one startling bathroom trip. Color alone does not diagnose Crohn's or colitis, but it can hint at diet, bile flow, infection, or fat malabsorption worth discussing with your team.",
        h2_context="What yellow stool can mean", context="Pale yellow, mustard, or greasy yellow stools have several everyday and medical explanations.",
        points=["Recent high-fat meals or food coloring", "Faster transit so bile pigments look different", "Fat malabsorption (steatorrhea), sometimes with oily film or hard-to-flush stool", "Infections or medication effects", "Less commonly, biliary or pancreatic issues that need clinician evaluation"],
        h2_action="What to track before your visit",
        actions=["Note color, oiliness, odor, and whether stools float", "List fatty meals, new supplements, and antibiotics", "Log urgency, pain, weight change, and pale stools lasting days", "Bring photos only if your clinic finds them useful; a written log is often enough"],
        action_note="Ileal Crohn's disease and resections can affect bile acid handling. Do not self-diagnose bile acid diarrhea from color alone.",
        urgent=["Yellow stools with severe pain, fever, vomiting, or black/red blood", "Unintentional weight loss or greasy stools for weeks", "Jaundice (yellow eyes/skin) with pale stools"],
        myths=[("Yellow stool always means celiac disease.", "Many causes exist; testing belongs with your clinician."),
               ("One yellow stool means a flare.", "A single change after diet is common; patterns matter."),
               ("Detox teas fix yellow stool.", "Marketing claims are not IBD care.")],
        questions=["Could fat malabsorption or bile acid issues fit my history?", "Should we check stool studies, elastase, or imaging?", "How do my surgeries affect stool color?"],
        related=[("/blog/reading-ibd-labs-calprotectin-crp", "calprotectin and CRP"), ("/stool-labs-decoder", "decoder hub"), ("/blog/chronic-diarrhea-ibd-causes", "chronic diarrhea")],
    ),
    dict(
        slug="green-stool-ibd", title="Green Stool With IBD: Transit Time, Diet, and When to Worry",
        description="Green stool with Crohn's or colitis: bile, leafy greens, transit time, infections, and clinic questions. Education only.",
        category="Wellness · August 2026", date_display="August 31, 2026", date_iso="2026-08-31T17:00:00Z",
        asset_dir="green-stool", resource_category="wellness",
        tags=["green stool", "bile", "transit", "diarrhea", "Crohn's", "colitis"],
        lead="Green stool looks alarming in photos online. Often it reflects bile that moved too quickly to turn brown, or green foods and dyes. With IBD, pair color notes with urgency and blood.",
        h2_context="Common reasons stool looks green", context="Brown color usually develops as bile pigments change during transit.",
        points=["Leafy greens, spirulina, green drinks, or food dyes", "Rapid transit / diarrhea leaving bile greener", "Some antibiotics or iron formulations (color varies)", "Infections that speed transit", "Less often, other GI conditions needing exam"],
        h2_action="Practical next steps",
        actions=["Pause green powders for 48 hours and note color change", "Hydrate if diarrhea is present", "Log Bristol type with color in IBDPal", "Message clinic if green stools persist with pain, fever, or bleeding"],
        action_note="Green plus severe urgency can still be a flare day even when color itself is not specific.",
        urgent=["Green stool with high fever, severe pain, or dehydration", "Bloody stools of any color with dizziness", "Symptoms after travel or raw foods suggesting infection"],
        myths=[("Green stool proves parasites.", "Many benign causes exist."),
               ("You must stop all vegetables.", "Cooked soft greens may still fit remission plates."),
               ("Green always means bile duct blockage.", "Blockage more often causes pale stools with jaundice; seek care for those signs.")],
        questions=["Is this transit speed from a flare or infection?", "Should we do stool pathogen testing?", "Any of my meds change stool color?"],
        related=[("/blog/bristol-stool-chart-ibd", "Bristol chart"), ("/blog/gas-bloating-ibd", "gas and bloating"), ("/blog/electrolytes-flare-ibd", "electrolytes")],
    ),
    dict(
        slug="black-stool-ibd", title="Black Stool With IBD: Melena, Iron, Pepto, and Red Flags",
        description="Black stool with Crohn's or colitis: melena vs iron or bismuth, when it is an emergency, and clinic questions. Education only.",
        category="Wellness · August 2026", date_display="August 31, 2026", date_iso="2026-08-31T18:00:00Z",
        asset_dir="black-stool", resource_category="wellness",
        tags=["black stool", "melena", "iron", "bismuth", "bleeding", "Crohn's", "colitis"],
        lead="Black, tarry, foul-smelling stool (melena) can signal digested upper GI bleeding and needs urgent medical attention. Black stool can also come from iron pills or bismuth (Pepto-Bismol). Knowing the difference matters.",
        h2_context="Melena versus harmless darkening", context="True melena is sticky and tar-like. Iron and bismuth often darken stool without the same sticky tar quality, but only a clinician can sort uncertain cases.",
        points=["Melena: black, tarry, strong odor; possible upper bleed", "Iron supplements and some foods can darken stool", "Bismuth products commonly turn stool black", "IBD bleeding is often brighter red from the lower gut, but mixed patterns happen", "Never assume black stool is 'just iron' if you feel faint or vomit coffee-ground material"],
        h2_action="What to do right now",
        actions=["If tarry black stool, dizziness, vomiting blood, or severe weakness: seek emergency care", "List iron, charcoal, and bismuth products you took", "Do not start new iron blindly to 'explain' black stool", "Call your IBD clinic's on-call line when unsure"],
        action_note="People on anticoagulants or with ulcers need a lower threshold for ER evaluation.",
        urgent=["Tarry black stools", "Fainting, chest pain, shortness of breath", "Vomiting blood or coffee-ground material", "Rapid heart rate with pale skin"],
        myths=[("Black stool is always Pepto.", "Only if you took bismuth and feel well; still confirm with a clinician when unsure."),
               ("IBD never causes black stool.", "Location and bleed rate vary."),
               ("Waiting a week is fine.", "Possible GI bleeding is time-sensitive.")],
        questions=["Was this melena or medication darkening?", "Do I need urgent endoscopy?", "Should I pause iron until evaluated?"],
        related=[("/blog/blood-in-stool-ibd-when-to-worry", "blood in stool"), ("/blog/when-to-go-er-ibd", "ER guidance"), ("/guides/iron-deficiency-nutrition-ibd", "iron nutrition")],
    ),
    dict(
        slug="floating-stool-ibd", title="Floating Stool With IBD: Gas, Fat, and Malabsorption Clues",
        description="Floating stools with Crohn's or colitis: gas vs fat malabsorption, odor and oiliness, and when to ask your GI. Education only.",
        category="Wellness · August 2026", date_display="September 1, 2026", date_iso="2026-09-01T12:00:00Z",
        asset_dir="floating-stool", resource_category="wellness",
        tags=["floating stool", "steatorrhea", "gas", "malabsorption", "Crohn's", "colitis"],
        lead="Floating stools are a classic internet worry. Often they reflect gas content. Persistent floating plus greasy film, weight loss, or foul odor can hint at fat malabsorption worth clinic review.",
        h2_context="Why stools float", context="Density changes with gas, fiber, and fat content.",
        points=["Extra gas from fermentation or rapid eating", "High-fiber days in remission", "Fat malabsorption making stools buoyant and oily", "Changes after bowel surgery", "Not every floater equals disease activity"],
        h2_action="Track the right details",
        actions=["Note oil droplets, toilet paper that will not wipe clean, or stools that stick", "Log weight trend and fat intake", "Mention floating stools with diarrhea lasting over a week", "Ask whether pancreatic enzymes or bile acid issues apply to you"],
        action_note="Floating alone rarely needs an ER visit. Pair with red-flag symptoms below.",
        urgent=["Floating greasy stools with rapid weight loss", "Severe pain or fever", "Black or bloody stools"],
        myths=[("Floating stool always means parasites.", "Gas is a common cause."),
               ("You must cut all fat forever.", "Fat needs are individual; severe restriction can backfire."),
               ("Floaters prove your biologic failed.", "Not a standalone marker of drug failure.")],
        questions=["Could this be steatorrhea?", "Do my labs or surgeries raise malabsorption risk?", "Should we adjust fat or add supervised enzymes?"],
        related=[("/blog/yellow-stool-ibd", "yellow stool"), ("/blog/gas-bloating-ibd", "gas"), ("/blog/omega-3-ibd", "dietary fats")],
    ),
    dict(
        slug="pencil-thin-stool-ibd", title="Pencil-Thin Stool With IBD: Strictures, Constipation, and Red Flags",
        description="Pencil-thin stools with Crohn's or colitis: stricture concerns, constipation, when imaging is discussed, and clinic questions. Education only.",
        category="Wellness · August 2026", date_display="September 1, 2026", date_iso="2026-09-01T14:00:00Z",
        asset_dir="pencil-stool", resource_category="wellness",
        tags=["pencil thin stool", "stricture", "narrow stool", "obstruction", "Crohn's", "colitis"],
        lead="Pencil-thin or ribbon stools worry people because online lists mention obstruction. Occasional thin stools happen with constipation. Persistent change, especially with pain, vomiting, or known stricturing Crohn's, needs prompt clinical advice.",
        h2_context="Possible explanations", context="Stool caliber reflects what the colon and rectum can pass.",
        points=["Constipation with soft leading edges looking thin", "Spasm or temporary narrowing", "Strictures in Crohn's disease", "Rectal inflammation changing shape", "Rarely, other structural problems needing evaluation"],
        h2_action="What your team may ask",
        actions=["How long has caliber changed?", "Any cramping after meals, vomiting, or inability to pass gas?", "Known strictures or prior resections?", "Avoid forcing high-residue foods if obstruction symptoms appear"],
        action_note="Do not ignore progressive thinning with obstructive symptoms. See obstruction education linked below.",
        urgent=["Thin stools plus vomiting, severe bloating, or no gas/stool", "Fever with severe pain", "Sudden complete constipation with swelling"],
        myths=[("One thin stool means cancer.", "Many benign causes exist; persistent change still deserves evaluation."),
               ("Laxatives fix strictures.", "Strictures need medical/surgical planning."),
               ("Fiber always helps narrow stools.", "With strictures, bulky fiber can worsen blockage risk.")],
        questions=["Do I need imaging for a stricture?", "Should I follow a low-residue plan temporarily?", "When is dilation or surgery discussed?"],
        related=[("/blog/vomiting-obstruction-ibd-warning-signs", "obstruction warning signs"), ("/blog/constipation-ibd-causes", "constipation"), ("/blog/corn-ibd", "corn and residue")],
    ),
    dict(
        slug="bristol-stool-chart-ibd", title="Bristol Stool Chart for IBD: How to Describe Stools to Your GI",
        description="Bristol stool scale for Crohn's and colitis: types 1 to 7, how to log flares, and how the chart helps clinic visits. Education only.",
        category="Wellness · August 2026", date_display="September 1, 2026", date_iso="2026-09-01T16:00:00Z",
        asset_dir="bristol-ibd", resource_category="wellness",
        tags=["Bristol stool chart", "Bristol scale", "stool type", "diarrhea", "constipation", "Crohn's", "colitis"],
        lead="The Bristol Stool Chart turns awkward bathroom descriptions into numbers clinicians understand. For IBD, types 6 to 7 often track flares, while type 1 to 2 may appear with pain meds, dehydration, or distal disease patterns.",
        h2_context="Quick tour of types 1 to 7", context="Type 1 is hard lumps; type 4 is smooth sausage-like; type 7 is entirely liquid.",
        points=["Types 1 to 2: constipation range", "Types 3 to 4: often goals in quiet disease for many people", "Types 5 to 7: looser to liquid, common in flares or infections", "Blood, mucus, urgency, and night stools add context beyond Bristol alone", "Use our interactive checker in Tools Lab to practice logging"],
        h2_action="How to use it well",
        actions=["Log the most representative stool of the day, not every variation", "Add urgency score and night waking", "Bring a 7-day Bristol log to infusions or clinic", "Try the <a href=\"/tools/bristol-flare-checker\">Bristol and flare checker</a>"],
        action_note="Bristol does not replace calprotectin, endoscopy, or exam findings.",
        urgent=["Sudden shift to type 7 with dehydration", "Bloody liquid stools with dizziness", "No stool plus severe bloating (possible obstruction pattern)"],
        myths=[("Only type 4 means remission.", "Remission is clinical and endoscopic; stool form helps but is not the whole story."),
               ("You must photograph every stool.", "Numbers and notes are enough for most visits."),
               ("Bristol diagnoses Crohn's.", "It is a communication tool.")],
        questions=["What Bristol range should I aim for on my therapy?", "How do we combine Bristol with calprotectin?", "Should I log separately during steroid tapers?"],
        related=[("/tools/bristol-flare-checker", "interactive checker"), ("/blog/mucus-urgency-tenesmus-ibd", "mucus and urgency"), ("/blog/tracking-food-symptoms-ibdpal", "tracking tips")],
    ),
    dict(
        slug="mucus-in-stool-ibd", title="Mucus in Stool With IBD: Inflammation, IBS Overlap, and Tracking",
        description="Mucus in stool with Crohn's or colitis: inflammation clues, IBS overlap, infection, and when to call your clinic. Education only.",
        category="Wellness · August 2026", date_display="September 1, 2026", date_iso="2026-09-01T18:00:00Z",
        asset_dir="mucus-stool", resource_category="wellness",
        tags=["mucus in stool", "mucus", "urgency", "inflammation", "Crohn's", "colitis"],
        lead="Mucus can look like clear jelly or white strings in the toilet. Small amounts can be normal. Larger amounts with blood, urgency, or tenesmus often travel with active colitis or rectal inflammation.",
        h2_context="Why mucus shows up", context="The gut lining produces mucus as a protective layer.",
        points=["Active inflammation increasing mucus discharge", "IBS overlap without large ulcers", "Infections", "Fistula drainage in some Crohn's phenotypes (different context)", "Dietary changes rarely are the only story when blood is present"],
        h2_action="Logging tips",
        actions=["Separate mucus-only days from mucus-plus-blood days", "Note tenesmus (feeling unfinished)", "Avoid assuming probiotics will clear mucus", "Ask about sigmoidoscopy or stool tests when mucus persists"],
        action_note="See also our urgency and tenesmus article for overlapping symptoms.",
        urgent=["Heavy mucus with fever", "Mucus plus heavy bleeding or clots", "Severe pain or dehydration"],
        myths=[("Mucus always means parasites.", "Inflammation is a common IBD reason."),
               ("Clear mucus is harmless forever.", "Persistent change still deserves a check-in."),
               ("Cutting dairy cures mucus.", "Only if lactose is a personal trigger.")],
        questions=["Is this active colitis or IBS overlap?", "Do we need stool infection testing?", "Should we adjust rectal therapies?"],
        related=[("/blog/mucus-urgency-tenesmus-ibd", "urgency and tenesmus"), ("/blog/blood-in-stool-ibd-when-to-worry", "blood in stool"), ("/flare-help", "flare help")],
    ),
    dict(
        slug="high-calprotectin-what-next", title="High Calprotectin: What It Means and What Happens Next",
        description="High fecal calprotectin with IBD: inflammation signal, false positives, scopes, and questions for your GI. Education only.",
        category="Wellness · August 2026", date_display="September 2, 2026", date_iso="2026-09-02T12:00:00Z",
        asset_dir="calprotectin-high", resource_category="wellness",
        tags=["calprotectin", "fecal calprotectin", "labs", "inflammation", "Crohn's", "colitis"],
        lead="A high fecal calprotectin result usually points toward intestinal inflammation, but it is not a complete diagnosis by itself. NSAIDs, infections, and sampling issues can raise values too.",
        h2_context="How clinicians use the number", context="Calprotectin is a neutrophil protein measured in stool.",
        points=["Helps distinguish inflammatory activity from some IBS-like symptoms", "Trends over time often matter more than one isolated value", "Cutoffs differ by lab; use your report's reference range", "May prompt endoscopy, imaging, or therapy changes", "Does not tell exact disease location alone"],
        h2_action="Smart patient steps after a high result",
        actions=["Ask whether to repeat after holding NSAIDs if appropriate", "List infections, recent colonoscopy prep, or incomplete samples", "Prepare symptom timeline for the follow-up visit", "Do not stop biologics on your own because of one number"],
        action_note="Pair with our broader labs article for CRP and bloodwork context.",
        urgent=["High calprotectin plus severe pain, obstruction signs, or heavy bleeding", "Fever on immunosuppression", "Inability to keep fluids down"],
        myths=[("High calprotectin always means surgery.", "Many medical options exist."),
               ("Normal calprotectin means you imagined symptoms.", "False negatives and other diseases occur."),
               ("Supplements lower calprotectin safely as treatment.", "Treat the disease with your team, not detox products.")],
        questions=["What threshold matters for my lab?", "Do we scope, image, or optimize medicine next?", "How often should I repeat calprotectin?"],
        related=[("/blog/reading-ibd-labs-calprotectin-crp", "reading IBD labs"), ("/blog/crp-normal-still-symptoms-ibd", "normal CRP still sick"), ("/blog/what-remission-means-ibd", "what remission means")],
    ),
    dict(
        slug="crp-normal-still-symptoms-ibd", title="Normal CRP but Still Sick With IBD: Why Labs Can Lag Symptoms",
        description="Normal CRP with ongoing IBD symptoms: limitations of blood tests, calprotectin, scopes, and advocacy tips. Education only.",
        category="Wellness · August 2026", date_display="September 2, 2026", date_iso="2026-09-02T14:00:00Z",
        asset_dir="crp-normal", resource_category="wellness",
        tags=["CRP", "normal CRP", "labs", "symptoms", "inflammation", "Crohn's", "colitis"],
        lead="Few results feel more invalidating than 'your CRP is normal' when you still have urgency, pain, or fatigue. CRP is useful, not omniscient. Some people with active IBD have modest blood marker changes.",
        h2_context="Limits of CRP", context="CRP rises with many inflammatory states and may miss localized gut activity.",
        points=["Blood markers can lag or stay modest in some patients", "Calprotectin or lactoferrin may better reflect gut inflammation", "IBS overlap, bile acid diarrhea, and strictures can hurt without high CRP", "Anemia and nutrient gaps cause fatigue with quiet CRP", "Endoscopic healing remains a gold-standard conversation"],
        h2_action="How to advocate without escalating conflict",
        actions=["Bring a symptom log, Bristol chart, and night-stool count", "Ask about fecal calprotectin if not done", "Request review of medication timing and adherence barriers", "Discuss whether imaging or endoscopy is warranted despite normal CRP"],
        action_note="Normal CRP is good news on one axis. It does not erase your lived symptoms.",
        urgent=["Normal CRP does not rule out emergency: obstruction, severe bleed, abscess signs still need urgent care", "High fever on biologics", "Fainting or chest pain"],
        myths=[("Normal CRP means you are fine.", "Not always."),
               ("You should stop seeking care.", "Persistent symptoms deserve a plan."),
               ("Only CRP matters for biologics.", "Clinicians use multiple endpoints.")],
        questions=["Which biomarkers fit my disease location?", "Could non-inflammatory complications explain this?", "When do we re-scope?"],
        related=[("/blog/high-calprotectin-what-next", "high calprotectin"), ("/blog/ibd-fatigue-brain-fog", "fatigue"), ("/blog/reading-ibd-labs-calprotectin-crp", "labs overview")],
    ),
    dict(
        slug="pale-clay-stool-ibd", title="Pale or Clay-Colored Stool: Bile Flow Questions With IBD",
        description="Pale or clay-colored stools: bile obstruction clues, meds, when jaundice matters, and IBD-related questions. Education only.",
        category="Wellness · August 2026", date_display="September 2, 2026", date_iso="2026-09-02T16:00:00Z",
        asset_dir="pale-stool", resource_category="wellness",
        tags=["pale stool", "clay colored stool", "bile", "jaundice", "PSC", "Crohn's", "colitis"],
        lead="Pale, clay, or putty-colored stools can mean less bile reaching the intestine. That pattern with dark urine or yellow eyes needs prompt medical evaluation. UC patients also hear about PSC risk in education materials.",
        h2_context="Why color goes pale", context="Bile pigments brown the stool. Blocked or reduced bile flow lightens it.",
        points=["Biliary obstruction or inflammation", "Medications and barium studies temporarily", "Prolonged liquid diets rarely look clay-like alone", "Overlap with PSC education in IBD communities", "Not the same as briefly pale stool after one fatty meal"],
        h2_action="Response plan",
        actions=["Note urine color and eye/skin yellowing", "List new medicines and supplements", "Contact clinic promptly for persistent pale stools", "Seek urgent care if jaundice, severe itching, fever, or RUQ pain appear"],
        action_note="PSC is uncommon but discussed more often with ulcerative colitis. Only specialists diagnose it.",
        urgent=["Pale stools plus jaundice", "Fever and right-upper abdominal pain", "Confusion or severe itching with color change"],
        myths=[("Pale stool is always PSC.", "Many causes exist; do not self-diagnose."),
               ("Turmeric fixes bile flow.", "Not a treatment for obstruction."),
               ("Waiting for it to brown again is always safe.", "Jaundice patterns need timely care.")],
        questions=["Do my symptoms suggest biliary evaluation?", "Should liver enzymes be checked now?", "How does this relate to my UC history?"],
        related=[("/blog/psc-ibd-liver", "PSC and IBD"), ("/blog/yellow-stool-ibd", "yellow stool"), ("/blog/when-to-call-gi-vs-er-ibd", "GI vs ER")],
    ),
]


def build_decoder_posts() -> list[dict]:
    out = []
    for d in DECODER:
        meta = {k: d[k] for k in ("slug", "title", "description", "category", "date_display", "date_iso", "asset_dir", "resource_category", "tags")}
        meta["share"] = d["description"][:110]
        out.append(post(meta, edu_body(d)))
    return out


def _load_satellite(filename: str) -> dict:
    ns: dict = {
        "post": post,
        "edu_body": edu_body,
        "food_body": food_body,
        "dict": dict,
    }
    code = (Path(__file__).resolve().parent / filename).read_text(encoding="utf-8")
    exec(code, ns, ns)
    return ns


def download_image(url: str, dest: Path) -> bool:
    import ssl
    import urllib.request

    for ctx in (ssl.create_default_context(), ssl._create_unverified_context()):
        try:
            with urllib.request.urlopen(url, context=ctx, timeout=45) as resp:
                data = resp.read()
            if len(data) > 5000 and data[:2] == b"\xff\xd8":
                dest.write_bytes(data)
                return True
        except Exception:
            continue
    return False


def ensure_image(p: dict) -> None:
    asset = BLOGS / "assets" / p["asset_dir"]
    asset.mkdir(parents=True, exist_ok=True)
    dest = asset / p["images"][0]
    if dest.exists() and dest.stat().st_size >= 5000:
        return
    url = IMAGE_URLS.get(p["asset_dir"])
    if url and download_image(url, dest):
        print("downloaded", dest.name)
        return
    if FALLBACK.exists():
        shutil.copy(FALLBACK, dest)
        print("fallback", dest.name)


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
    print("patched vercel.json (+", len(inserts), "rewrites)")


def patch_sitemap(slugs: list[str]) -> None:
    today = date.today().isoformat()
    text = SITEMAP.read_text(encoding="utf-8")
    marker = "<!-- eureka-top5-blogs -->"
    if marker in text:
        text = re.sub(
            rf"\n  {re.escape(marker)}.*?(?=\n  <!-- |\n</urlset>)",
            "",
            text,
            flags=re.DOTALL,
        )
    entries = [
        f"  <url>\n    <loc>{SITE}/blog/{slug}</loc>\n    <lastmod>{today}</lastmod>\n"
        f"    <changefreq>monthly</changefreq>\n    <priority>0.86</priority>\n  </url>"
        for slug in slugs
    ]
    block = f"  {marker}\n" + "\n".join(entries)
    for anchor in (
        "  <!-- wave4-food-nutrition-blogs -->",
        "  <!-- wave3-food-nutrition-blogs -->",
        "  <!-- seo-wellness-blogs -->",
    ):
        if anchor in text:
            text = text.replace(anchor, block + "\n" + anchor)
            break
    else:
        text = text.replace("</urlset>", block + "\n</urlset>")
    SITEMAP.write_text(text, encoding="utf-8")
    print("patched sitemap.xml (+", len(slugs), "urls)")


def main() -> None:
    drugs_ns = _load_satellite("_eureka_drugs.py")
    myths_ns = _load_satellite("_eureka_myths.py")
    foods_ns = _load_satellite("_eureka_foods.py")
    posts = (
        build_decoder_posts()
        + drugs_ns["build_drug_posts"]()
        + myths_ns["build_myth_posts"]()
        + foods_ns["build_food_posts"]()
    )
    DATA.write_text(
        json.dumps({"bundle": "eureka-top5", "posts": posts}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print("wrote", DATA.relative_to(ROOT), len(posts), "posts")
    slugs = []
    for p in posts:
        ensure_image(p)
        (BLOGS / f"{p['slug']}.html").write_text(render_post(p), encoding="utf-8")
        slugs.append(p["slug"])
        print("wrote", p["slug"] + ".html")
    patch_vercel(slugs)
    patch_sitemap(slugs)
    print("Done.", len(slugs), "Eureka Top-5 posts.")


if __name__ == "__main__":
    main()
