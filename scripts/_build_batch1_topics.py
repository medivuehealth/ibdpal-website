"""One-time builder: writes _batch1_topics_data.py with all 75 topic definitions."""
from __future__ import annotations

from pathlib import Path

OUT = Path(__file__).resolve().parent / "_batch1_topics_data.py"

# slug -> (sections, faqs, extras)
# sections: list of (h2, [p1, p2, p3])
# faqs: list of (question, answer)
# extras: optional padding paragraphs

TOPICS: dict[str, tuple] = {}

def add(slug, sections, faqs, extras=None):
    TOPICS[slug] = (sections, faqs, extras or [])


add("partner-caregiver-ibd",
    [("Understanding the invisible side of IBD", [
        "Many symptoms of Crohn's disease and ulcerative colitis happen behind closed doors. Urgency, fatigue, and pain may not be visible during a dinner out or a family visit. Partners and caregivers who learn this early often feel less frustrated when plans change at the last minute.",
        "Your role is not to fix the disease. It is to create a home environment where the person with IBD can rest, eat safely, and speak honestly about how they feel. Ask open questions and accept that answers may change day to day.",
        "If you live together, agree on signals for bad days. A simple text like \"low energy day\" can prevent misunderstandings about canceled plans or skipped chores.",
    ]), ("Communication that protects dignity", [
        "Avoid commenting on weight, bathroom habits, or food choices in front of others unless your loved one invites that conversation. Public remarks, even well meant, can increase shame and stress.",
        "During clinic visits, let the patient lead. They may want you in the room for support or may prefer privacy for certain topics. Either choice is valid.",
        "When conflict arises, name the stress, not the disease. \"I am worried and do not know how to help\" lands better than blaming the disease for every canceled plan.",
    ]), ("Medical boundaries caregivers should respect", [
        "Do not adjust medications, supplements, or infusion schedules without explicit instruction from the GI team. Even over-the-counter products can interact with IBD therapies.",
        "You can help by maintaining a shared calendar of appointments, refills, and lab dates. Bring a written list of new symptoms if your loved one asks you to attend.",
        "Know the clinic after-hours line and what counts as an emergency for their specific history. Your clinician can clarify red-flag symptoms during a routine visit.",
    ]), ("Protecting your own wellbeing", [
        "Caregiver fatigue is common when a partner or child has a chronic illness. Schedule time for sleep, exercise, and social connection that is not centered on medical tasks.",
        "Peer groups for IBD families and partners exist through national foundations and hospital programs. Hearing from others normalizes the emotional load.",
        "If you feel resentful, burned out, or depressed, talk with your own clinician or a counselor. Supporting someone with IBD is long-term work, and your health matters too.",
    ])],
    [("Should I attend every GI appointment?", "Ask your loved one what they prefer. Some patients want a second set of ears; others want privacy. Respect their choice and revisit it over time."),
     ("How do I help without being controlling?", "Offer specific help: \"I can pick up prescriptions today\" works better than vague criticism. Follow their yes or no."),
     ("What if I feel guilty when I need a break?", "Rest makes you a steadier supporter. Short breaks prevent burnout that can strain the relationship more than a quiet afternoon alone.")],
    ["Many couples find it useful to set a weekly check-in that is not about symptoms, so the relationship stays bigger than the disease.",
     "School and workplace paperwork for children with IBD often requires parent signatures; keeping copies organized reduces last-minute stress."])

add("stress-autoimmune-symptoms",
    [("Why stress and symptoms often rise together", [
        "Stress does not cause autoimmune disease, but it can amplify how symptoms feel. Pain, fatigue, and bowel urgency may seem louder when sleep is poor or anxiety is high.",
        "The nervous system and immune system communicate constantly. During high stress, some people notice more flares or flare-like symptoms even when labs are stable.",
        "This pattern is common in Crohn's disease, ulcerative colitis, rheumatoid arthritis, lupus, and other immune-mediated conditions. It is biology, not weakness.",
    ]), ("Separating disease activity from stress load", [
        "Track symptoms alongside stressors in a simple log. Note sleep, work deadlines, infections, and menstrual cycles if relevant. Patterns help your clinician interpret changes.",
        "If diarrhea, bleeding, or weight loss appear with stress, do not assume it is only stress. Contact your GI team for guidance, especially when red-flag symptoms are present.",
        "Calprotectin, CRP, and imaging sometimes stay normal while you feel awful. That does not mean your experience is invalid. It means more than one system may need attention.",
    ]), ("Practical stress tools that fit chronic illness", [
        "Short breathing exercises, gentle stretching, and brief walks can lower physiological arousal without requiring a perfect meditation practice.",
        "Cognitive behavioral therapy and gut-directed hypnosis have evidence in IBD for improving coping and sometimes symptom burden. Ask your clinician for referrals.",
        "Protect sleep when possible. Late-night scrolling and irregular meals can worsen both mood and gut symptoms the next day.",
    ]), ("Talking with your care team", [
        "Bring stress and mood symptoms to medical visits the same way you bring abdominal pain. Integrated clinics increasingly screen for anxiety and depression.",
        "If stress is high during a flare, ask whether a short-term plan for rest, nutrition, and medication timing makes sense. Small structure can reduce decision fatigue.",
        "Medication for anxiety or depression does not mean you failed at coping. For many patients it is one tool among several.",
    ])],
    [("Does reducing stress cure autoimmune disease?", "No. Stress management supports quality of life and may reduce symptom perception, but it does not replace disease-directed treatment from your specialist."),
     ("My family says it is all in my head. What can I say?", "Autoimmune disease is real inflammation with measurable markers in many cases. Stress can worsen symptoms without being the root cause."),
     ("When should I seek mental health care?", "Consider it when worry, low mood, panic, or sleep loss persist for weeks or interfere with treatment, work, or relationships.")],
    ["Peer support groups can reduce isolation, which itself lowers stress for many people living with IBD.",
     "If you use alcohol to cope, discuss safer strategies with your clinician because alcohol can worsen gut symptoms and interact with medications."])

add("alcohol-caffeine-ibd",
    [("How alcohol affects the gut in IBD", [
        "Alcohol can irritate the digestive tract and may trigger symptoms in some people with Crohn's disease or ulcerative colitis, even in remission.",
        "Beer, wine, and spirits affect people differently. Carbonation and sugar in mixed drinks can add bloating on top of alcohol effects.",
        "If you drink, small amounts with food and good hydration are common patient strategies, but your GI team should guide what is safe for your history.",
    ]), ("Caffeine, urgency, and sleep", [
        "Caffeine is a stimulant that can speed bowel motility. Coffee may increase urgency for some patients with colitis, especially on an empty stomach.",
        "Tea and chocolate also contain caffeine. Track whether morning coffee correlates with bathroom trips or cramping later in the day.",
        "Poor sleep from late caffeine can worsen fatigue and stress, which may indirectly worsen gut symptoms the next day.",
    ]), ("Medication and liver considerations", [
        "Methotrexate, some immunosuppressants, and certain biologics come with specific alcohol guidance. Liver labs may change how strictly your team advises avoidance.",
        "Never assume social drinking is fine because a friend with IBD tolerates it. Your medication list and disease location matter.",
        "Bring an honest drinking log to appointments if symptoms fluctuate on weekends or holidays.",
    ]), ("Safer social strategies", [
        "Order mocktails, sparkling water, or decaf options when you want to participate without triggers. You do not owe strangers a medical explanation.",
        "Eat before events and identify bathroom access early. Planning reduces anxiety that can mimic flare symptoms.",
        "If you choose to drink, set a personal limit in advance and plan a ride home. Fatigue and dehydration compound quickly during active disease.",
    ])],
    [("Is one glass of wine always unsafe?", "Not for everyone, but safety depends on disease activity, medications, and liver health. Ask your clinician rather than relying on general rules."),
     ("Does decaf coffee still cause urgency?", "Some patients react to coffee acids or temperature rather than caffeine alone. Trial and tracking help clarify your pattern."),
     ("Should I stop caffeine before a colonoscopy?", "Follow your prep instructions exactly. Caffeine rules vary by center; call the endoscopy team if unsure.")])

# Continue with remaining topics - use exec to load rest from string
exec(open(Path(__file__).with_name("_batch1_topics_rest.py"), encoding="utf-8").read())

lines = [
    '"""Topic-specific expansion content for batch 1 blog posts."""',
    "from __future__ import annotations",
    "",
    "def T(sections, faqs, extras=None):",
    '    return {"sections": sections, "faqs": faqs, "extras": extras or []}',
    "",
    "TOPIC_REGISTRY: dict[str, dict] = {",
]
for slug in sorted(TOPICS.keys()):
    sections, faqs, extras = TOPICS[slug]
    lines.append(f'    "{slug}": T(')
    lines.append("        " + repr(sections) + ",")
    lines.append("        " + repr(faqs) + ",")
    if extras:
        lines.append("        " + repr(extras) + ",")
    lines.append("    ),")
lines.append("}")
lines.append("")

text = "\n".join(lines)
if "\u2014" in text or "—" in text:
    raise SystemExit("em dash found")
OUT.write_text(text, encoding="utf-8")
print(f"Wrote {len(TOPICS)} topics to {OUT}")
