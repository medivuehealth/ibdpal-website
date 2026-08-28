"""Generate blog-expansions-batch2.json for slugs 76-149 in _thin_blogs.tsv."""
from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TSV_PATH = ROOT / "scripts" / "_thin_blogs.tsv"
OUT_PATH = ROOT / "data" / "blog-expansions-batch2.json"
TARGET_TOTAL = 800
GENERIC_PADS = [
    "Bring a written symptom and medication list to each gastroenterology visit so limited appointment time is used well.",
    "Patient education supports shared decision making; it does not replace individual medical assessment by your IBD team.",
    "Track patterns over one to two weeks before clinic visits because single-day snapshots can mislead both you and your clinician.",
    "Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift unexpectedly.",
    "Medication adherence and follow-up labs are as important as diet changes for many people living with Crohn's disease or ulcerative colitis.",
    "Discuss how this topic applies to your current disease activity with your gastroenterologist rather than relying on general online advice alone.",
    "Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment you are already following.",
    "Children, older adults, and post-surgical patients may need modified guidance from specialists familiar with their full history.",
    "Logging patterns in IBDPal or a simple notebook helps clinicians see trends beyond a single urgent care or telehealth visit.",
    "If symptoms worsen while you try these steps, contact your clinic using the flare pathway your team has given you.",
]
BATCH_START = 76
BATCH_END = 149


class VisibleTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.chunks: list[str] = []

    def handle_data(self, data: str) -> None:
        text = data.strip()
        if text:
            self.chunks.append(text)


def html_word_count(fragment: str) -> int:
    parser = VisibleTextParser()
    parser.feed(fragment)
    return len(re.findall(r"\b[\w']+\b", " ".join(parser.chunks)))


def build(sections: list[tuple[str, list[str]]], faqs: list[tuple[str, str]]) -> str:
    parts: list[str] = []
    for title, paragraphs in sections:
        parts.append(f"<h2>{title}</h2>")
        for p in paragraphs:
            parts.append(f"<p>{p}</p>")
    parts.append("<h2>Common questions</h2>")
    for question, answer in faqs:
        parts.append(f"<h3>{question}</h3>")
        parts.append(f"<p>{answer}</p>")
    return "\n".join(parts)


def pad_to_target(html: str, target: int, extras: list[str]) -> str:
    current = html_word_count(html)
    pool = list(extras) + GENERIC_PADS
    i = 0
    while current < target and i < len(pool) * 3:
        extra = pool[i % len(pool)]
        html += f"\n<p>{extra}</p>"
        current = html_word_count(html)
        i += 1
    return html


def trim_to_target(html: str, target: int) -> str:
    """Remove trailing paragraphs if over target."""
    while html_word_count(html) > target + 30:
        parts = html.rsplit("<p>", 1)
        if len(parts) < 2:
            break
        html = parts[0].rstrip()
    return html


def entry(sections: list[tuple[str, list[str]]], faqs: list[tuple[str, str]], pads: list[str]) -> dict:
    return {"sections": sections, "faqs": faqs, "pads": pads}


# fmt: off
TOPICS: dict[str, dict] = {
"psc-ibd-liver": entry([
    ("Long-term monitoring when PSC and IBD overlap", [
        "Primary sclerosing cholangitis often needs coordinated follow-up between gastroenterology and hepatology. Your GI team may order liver tests at regular intervals even when bowel symptoms feel stable.",
        "MRCP or other bile-duct imaging may be scheduled on a timeline your clinicians set. Understanding the schedule helps you prepare questions before each visit rather than reacting to surprise orders.",
        "Colon cancer surveillance can differ when PSC and colitis travel together. Ask whether your colonoscopy interval should change and who coordinates scheduling between specialties.",
    ]),
    ("Symptoms that deserve prompt outreach", [
        "New or worsening itching, especially on the palms or soles, can signal changing bile flow. Yellowing of the eyes, dark urine, or pale stool also warrant same-day or urgent contact per your clinic plan.",
        "Fever with right-upper abdominal pain may suggest a bile-duct infection called cholangitis. Patients with PSC sometimes need antibiotics and hospital-level care quickly.",
        "Fatigue alone is nonspecific, but sudden energy collapse with jaundice or fever is different. Keep a short symptom log so you can describe timing accurately.",
    ]),
    ("Medications and lifestyle themes patients discuss", [
        "Ursodeoxycholic acid is commonly prescribed in PSC, though benefits vary by person. Take medicines exactly as directed and report side effects rather than stopping on your own.",
        "Alcohol guidance may be stricter when bile-duct disease is present. Ask your hepatologist how this intersects with social drinking and medication lists.",
        "Vaccinations, including hepatitis A and B when not immune, are frequent topics in PSC education. Bring your immunization record to multidisciplinary visits.",
    ]),
    ("Preparing for multidisciplinary appointments", [
        "Bring printed lab trends for ALT, AST, alkaline phosphatase, and bilirubin. A simple table with dates helps specialists see direction, not just single numbers.",
        "List all IBD medications, supplements, and hospitalizations. PSC management may influence how aggressively colitis is treated and vice versa.",
        "Ask what symptoms should trigger the on-call line versus waiting for the next routine slot. Written plans reduce anxiety during uncertain weeks.",
    ]),
], [
    ("Can PSC be cured?", "There is no universal cure yet. Treatment focuses on monitoring, symptom management, and preparing for possible transplant evaluation in advanced cases. Your team personalizes goals."),
    ("If my colon is quiet, can I skip liver tests?", "Many clinicians still monitor the liver on a schedule because PSC can progress without dramatic gut symptoms. Follow the plan you agree on with your specialists."),
    ("Does every person with ulcerative colitis need PSC screening?", "Not always, but many IBD centers screen selected patients based on risk factors. Ask whether baseline imaging or labs make sense for you."),
], [
    "Patient foundations publish PSC checklists that pair well with clinic conversations.",
    "Second opinions at transplant centers are sometimes arranged early for education, not because transplant is imminent.",
]),
"uveitis-eye-inflammation-ibd": entry([
    ("Building a proactive eye care plan", [
        "People with IBD on immunosuppression may benefit from a standing relationship with ophthalmology even when eyes feel fine. Baseline exams create a comparison point if redness or pain appears later.",
        "Tell eye specialists every biologic, steroid, and immunomodulator you use. Some systemic IBD therapies also treat eye inflammation; others require careful coordination.",
        "Keep a card or phone note listing your IBD diagnosis and rheumatology or GI contacts. Emergency eye visits go faster when records are easy to share.",
    ]),
    ("Differentiating urgent eye symptoms", [
        "Anterior uveitis can cause deep aching pain, light sensitivity, and blurred vision. Episcleritis may look scary but is often less vision-threatening; only an exam can tell them apart.",
        "Do not borrow steroid eye drops from family members. Wrong drops can worsen certain infections or glaucoma risk.",
        "If one eye is painful and red while you feel systemically ill, treat it as urgent. Same-day ophthalmology assessment protects vision.",
    ]),
    ("Tracking eye and gut symptoms together", [
        "Some patients notice eye flares when bowel symptoms worsen; others see independent timing. A one-line daily log for eyes and stools helps your clinicians spot patterns.",
        "Joint pain and eye inflammation sometimes cluster in IBD. Mention back stiffness or swollen knees when discussing eye symptoms.",
        "Bring photos of redness only as supplements, not replacements for professional exams. Lighting distorts color and severity.",
    ]),
    ("Treatment coordination with your GI team", [
        "Eye drops may be enough for mild inflammation, while recurrent uveitis can require systemic therapy changes. Ask how eye findings influence your overall IBD plan.",
        "If vision symptoms appear after starting a new medicine, report it promptly. Causality is not always clear, but timelines matter.",
        "Sunglasses and dim lighting can reduce discomfort during flares. Resting screens helps when photophobia is present.",
    ]),
], [
    ("Is red eye always uveitis?", "No. Allergies, dry eye, infections, and contact lens problems mimic redness. Examination and history distinguish causes."),
    ("Should I stop my biologic if my eye flares?", "Never stop systemic IBD medicines without guidance. Often your team intensifies eye treatment while maintaining gut therapy."),
    ("Can children with IBD get uveitis?", "Yes. Pediatric patients may need routine eye screening even without symptoms. Parents should know urgent warning signs."),
], [
    "Emergency rooms with ophthalmology coverage are preferable when same-day clinic access is unavailable.",
    "Carry artificial tears only if your eye doctor approves them during active inflammation.",
]),
"ibd-autoimmune-overlap": entry([
    ("Why immune conditions cluster in some families", [
        "Genes and environmental triggers influence many autoimmune diseases. Having Crohn's disease or ulcerative colitis does not guarantee another diagnosis, but risk is higher than in the general population.",
        "Shared pathways explain why skin, joint, liver, and eye problems appear in IBD clinics. Understanding overlap reduces the feeling that new symptoms are unrelated bad luck.",
        "Family history of lupus, thyroid disease, psoriasis, or type 1 diabetes is worth documenting in your chart. Patterns help specialists prioritize screening.",
    ]),
    ("Common overlap themes in IBD practice", [
        "Psoriasis and joint disease are frequent discussion topics. Skin plaques or morning back stiffness should be reported even when intestines feel stable.",
        "Thyroid autoimmunity can affect energy, weight, and mood. Anemia and fatigue workups sometimes uncover Hashimoto's disease alongside IBD.",
        "Primary sclerosing cholangitis and autoimmune hepatitis sit in the liver overlap space. Abnormal liver tests deserve structured follow-up.",
    ]),
    ("How to avoid diagnostic delays", [
        "Bring a timeline when new symptoms start: what improved with IBD therapy and what did not. Overlap conditions may need their own labs and imaging.",
        "Ask whether rheumatology, dermatology, or endocrinology referral makes sense. Multidisciplinary clinics exist at many academic centers.",
        "Do not assume every new symptom is a flare. Steroid courses that help colitis but not joints hint at separate disease activity.",
    ]),
    ("Living well with multiple labels", [
        "Medication lists grow with overlap conditions. Use one updated list for all specialists and check for interactions at each change.",
        "Mental health support helps when diagnoses accumulate. You are managing complex chronic disease, not failing at wellness.",
        "Patient organizations publish overlap guides that translate specialist language into everyday planning.",
    ]),
], [
    ("Does having one autoimmune disease mean I will get many more?", "Not necessarily. Risk rises, but many people live with IBD alone. Screening and symptom awareness are the practical responses."),
    ("Can one medicine treat overlapping conditions?", "Sometimes. Certain biologics target both gut and joint inflammation. Your clinician balances benefits and risks across organs."),
    ("Should I see a rheumatologist if I only have mild joint aches?", "Mention joint symptoms to your GI first. They may order initial tests or refer based on pattern and severity."),
], [
    "Keep copies of specialty consult notes in a folder your GI team can access.",
    "Wearable step counts sometimes drop before formal joint flares; share trends if relevant.",
]),
"steroid-taper-what-to-expect-ibd": entry([
    ("Why tapering is its own phase of treatment", [
        "Prednisone and budesonide calm inflammation quickly, but your body adapts to higher steroid levels. Tapering too fast can cause rebound symptoms; tapering too slowly prolongs side effects.",
        "Your GI team sets a schedule based on response, history, and whether steroid-sparing medicines are on board. Follow the plan even if you feel well mid-taper.",
        "Write the taper on a calendar with pill counts. Pharmacy blisters help prevent accidental double doses on confusing days.",
    ]),
    ("Physical and mood changes during taper", [
        "Joint aches, fatigue, nausea, or dizziness can appear as doses drop. These symptoms are common enough to mention at visits, not to hide.",
        "Mood swings, anxiety, and sleep disruption sometimes worsen during taper. Tell your clinician if functioning at work or school becomes difficult.",
        "Appetite may fall as steroid hunger fades. Plan protein-rich snacks so unintentional weight loss does not add stress.",
    ]),
    ("Protecting bone health and metabolism", [
        "Calcium, vitamin D, and weight-bearing exercise are frequent recommendations during and after steroid courses. Ask whether bone density monitoring is due.",
        "Blood pressure and blood sugar can shift on steroids and during withdrawal. Home monitoring may be advised for higher doses or longer courses.",
        "Carry a medical alert note if adrenal suppression is a concern after prolonged use. Emergency providers need to know recent steroid timing.",
    ]),
    ("When to call before the next scheduled step", [
        "Return of bloody diarrhea, high fevers, or severe abdominal pain may mean slowing the taper or adding therapy. Use your clinic flare pathway.",
        "Vomiting that prevents taking oral steroids needs urgent input. Missing doses can complicate adrenal recovery.",
        "If withdrawal symptoms feel unmanageable, ask about slower taper steps or temporary support medicines rather than quitting cold turkey.",
    ]),
], [
    ("Can I speed up the taper if I feel great?", "Only with clinician approval. Faster tapers risk rebound inflammation or adrenal problems."),
    ("Why do my joints hurt while my gut improves?", "Steroid withdrawal aches are common and differ from active Crohn's flares. Your team can help sort them out."),
    ("Do topical steroids count for adrenal risk?", "Systemic absorption varies. Tell all prescribers about oral steroid tapers you are following."),
], [
    "Pill organizers labeled by week reduce taper errors during busy seasons.",
    "Light walking may ease joint stiffness when energy allows.",
]),
"high-school-ibd-survival-guide": entry([
    ("504 plans and bathroom access", [
        "Schools in the United States often provide 504 accommodations for chronic illness. Unlimited bathroom access, locker near restrooms, and excused tardies are common requests.",
        "Meet with the school nurse before the semester starts. Share a clinician letter that explains IBD without oversharing private details.",
        "Identify staff allies who understand urgent exits from class. A discreet pass or code word reduces embarrassment.",
    ]),
    ("Managing missed class and makeup work", [
        "Flares, infusions, and appointments cause absences. Ask teachers for a predictable makeup workflow early, not after grades slip.",
        "Home instruction or hospital teachers may be available during prolonged illness. Social workers at children's hospitals often know district policies.",
        "Prioritize essential assignments during bad weeks. Your GI team can document medical necessity for reduced workload temporarily.",
    ]),
    ("Social life, sports, and privacy", [
        "You choose how much to share with friends. Close friends can help cover bathroom runs or explain sudden departures.",
        "Sports may need modified conditioning during active disease or after surgery. Coaches and athletic trainers appreciate written clearance and symptom plans.",
        "Online spaces can be supportive or stressful. Curate who knows your diagnosis to protect mental health.",
    ]),
    ("Transition skills before college", [
        "Practice scheduling refills and describing symptoms in your own words before leaving pediatric care. Parents can step back gradually.",
        "Learn infusion or injection logistics if applicable. Independence reduces anxiety when dorm life begins.",
        "Keep a copy of your medication list and insurance card in your backpack. Emergencies happen on field trips too.",
    ]),
], [
    ("Do I have to tell everyone I have Crohn's?", "No. Tell people on a need-to-know basis. Accommodations staff need medical documentation; peers deserve only what you choose."),
    ("Can I be penalized for bathroom breaks during tests?", "With proper accommodations, timed tests should include bathroom access. Work with disability services before exam season."),
    ("What if the school resists accommodations?", "Pediatric GI social workers and patient advocacy groups can help. Document requests in writing."),
], [
    "ImproveCareNow teen resources include scripts for talking with teachers.",
    "A small go-bag in your locker prevents panic when symptoms start mid-day.",
]),
"gas-bloating-ibd": entry([
    ("Separating inflammation from functional bloating", [
        "Gas and bloating occur in active IBD, but they also appear during remission when the gut is sensitive. Calprotectin, CRP, and symptom timing help your clinician separate flare from irritable bowel overlap.",
        "Sudden worsening with fever, blood, or weight loss suggests inflammation until proven otherwise. Gradual bloating after specific meals points toward dietary triggers.",
        "Track whether bloating improves overnight or persists all day. Patterns guide testing and treatment choices.",
    ]),
    ("Food and eating habits that influence gas", [
        "Carbonated drinks, sugar alcohols, beans, and large high-FODMAP meals are frequent culprits. Smaller portions and slower eating reduce swallowed air.",
        "Lactose intolerance can develop during flares. A brief lactose trial with your dietitian's input may clarify symptoms.",
        "Chewing gum and drinking through straws increase gas for some people. Simple habit changes are low-risk experiments.",
    ]),
    ("Medications and motility", [
        "Antibiotics, probiotics, and fiber supplements change gas production. Note start dates when symptoms shift.",
        "Opioids and some antispasmodics slow motility and can worsen bloating. Discuss alternatives if constipation or distension increase.",
        "Partial bowel obstruction or strictures may present with bloating and nausea. Report vomiting or inability to pass gas promptly.",
    ]),
    ("Comfort strategies while you investigate", [
        "Gentle walking and heat packs soothe some patients. Aggressive abdominal massage is not recommended during active inflammation.",
        "Loose clothing reduces pressure when distension is high. Hydration supports motility unless your team advises fluid restriction.",
        "Mental stress can amplify bloating perception. Brief relaxation practices may help alongside medical care.",
    ]),
], [
    ("Is bloating always a flare?", "Not always. Diet, stress, and IBS-like sensitivity can cause bloating with quiet inflammation. Labs and exam findings help clarify."),
    ("Should I take simethicone daily?", "Occasional use is common, but daily reliance without evaluation can mask changing disease. Ask your clinician if symptoms persist."),
    ("Do probiotics reduce gas?", "Responses vary. Some patients feel worse on certain strains. Discuss brands and goals with your GI team."),
], [
    "A food and symptom app makes clinic visits more productive.",
    "Peppermint tea helps some patients but worsens reflux in others.",
]),
"constipation-ibd-causes": entry([
    ("IBD-specific reasons constipation appears", [
        "Crohn's strictures can narrow the bowel and slow transit. New constipation with bloating and vomiting needs urgent evaluation for obstruction.",
        "Rectal inflammation in ulcerative colitis sometimes causes tensemus without frequent stools. The sensation of blockage differs from simple slow transit.",
        "Prior surgery, adhesions, and short bowel anatomy change bowel habits. Tell your team about every abdominal operation.",
    ]),
    ("Medication and lifestyle contributors", [
        "Iron supplements, opioids, anticholinergics, and some anti-nausea medicines worsen constipation. Review over-the-counter products at each visit.",
        "Dehydration and low movement during flares reduce stool water content. Gentle fluids and walking may help when safe.",
        "Pelvic floor dysfunction is common and treatable with pelvic therapy. Difficulty evacuating despite soft stools suggests this overlap.",
    ]),
    ("Safe relief strategies to discuss", [
        "Osmotic laxatives like polyethylene glycol are often preferred over stimulant laxatives in IBD, but choices depend on disease location and activity.",
        "Fiber is not always appropriate with strictures. Ask before adding bran or bulk-forming agents.",
        "Enemas and suppositories may help proctitis-related constipation when prescribed. Random strong laxatives can irritate inflamed tissue.",
    ]),
    ("Red flags that change the plan", [
        "Severe abdominal distension, fever, and vomiting could signal obstruction. Go to emergency care per your clinic instructions.",
        "Nighttime pain waking you from sleep, unintended weight loss, or blood with new constipation deserve prompt outreach.",
        "Pencil-thin stools plus progressive constipation warrant imaging discussion. Do not wait months to mention changing shape.",
    ]),
], [
    ("Can constipation mean my colitis is flaring?", "Sometimes. Inflammation in the rectum can reduce stool passage even without diarrhea. Calprotectin and exam help clarify."),
    ("Is miralax safe long term in IBD?", "Many clinicians use it, but personalization matters. Strictures and active inflammation change risk."),
    ("Should I do a colon cleanse at home?", "Avoid unsupervised cleanses. They can dehydrate you and obscure symptoms your team needs to see."),
], [
    "Squatty stools and unhurried bathroom time help pelvic floor issues.",
    "Track bowel movements weekly so gradual changes are obvious.",
]),
}

from blog_expansion_batch2_entries_part2 import TOPICS_PART2  # noqa: E402
from blog_expansion_batch2_entries_part3 import TOPICS_PART3  # noqa: E402

TOPICS.update(TOPICS_PART2)
TOPICS.update(TOPICS_PART3)


def load_batch_slugs() -> list[tuple[str, int]]:
    rows: list[tuple[int, str, int]] = []
    for i, line in enumerate(TSV_PATH.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        slug, wc, _title, _path = line.split("\t", 3)
        rows.append((i, slug, int(wc)))
    batch = [(slug, wc) for i, slug, wc in rows if BATCH_START <= i <= BATCH_END]
    return batch


def main() -> None:
    batch = load_batch_slugs()
    missing = [s for s, _ in batch if s not in TOPICS]
    if missing:
        print("Missing topics:", ", ".join(missing), file=sys.stderr)
        sys.exit(1)

    out: dict[str, dict[str, str]] = {}
    for slug, wc in batch:
        topic = TOPICS[slug]
        html = build(topic["sections"], topic["faqs"])
        append_target = max(280, TARGET_TOTAL - wc)
        html = pad_to_target(html, append_target, topic["pads"])
        out[slug] = {"append_body": html}

    OUT_PATH.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(out)} expansions to {OUT_PATH}")
    counts = [html_word_count(v["append_body"]) for v in out.values()]
    print(f"append words min={min(counts)} max={max(counts)} avg={sum(counts)//len(counts)}")


if __name__ == "__main__":
    main()
