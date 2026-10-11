#!/usr/bin/env python3
"""Compile oct11_seo_bodies/*.py from structured content (unique paragraphs only)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent / "oct11_seo_bodies"

TEMPLATE = '''from oct11_seo_bodies._html import assemble, related


def body() -> str:
    return assemble(
        intro={intro!r},
        sections={sections!r},
        clinic_quote={clinic!r},
        faqs={faqs!r},
        related_html=related(
{related}
        ),
        closing={closing!r},
    )
'''


def rel(pairs: list[tuple[str, str]]) -> str:
    return "\n".join(f'            ("{a}", "{b}"),' for a, b in pairs)


def write_module(filename: str, **kw) -> None:
    text = TEMPLATE.format(
        intro=kw["intro"],
        sections=kw["sections"],
        clinic=kw["clinic"],
        faqs=kw["faqs"],
        related=rel(kw["related"]),
        closing=kw.get("closing", []),
    )
    (ROOT / filename).write_text(text, encoding="utf-8")


def S(title: str, *paragraphs: str) -> tuple[str, list[str]]:
    return (title, list(paragraphs))


# --- ulcerative colitis diet ---
UC_SECTIONS = [
    S(
        "Why ulcerative colitis diet searches spike",
        "People with ulcerative colitis often search diet the week bleeding returns or when every restaurant menu feels like a trap. They want permission to eat without betraying their colon.",
        "A useful overview separates inflammation treatment from comfort food choices while mucosa heals. Meals matter, yet they rarely replace endoscopy proven disease control.",
        "This page speaks to left sided disease, extensive colitis, and pouch life without pretending one list fits every rectum.",
        "Start from your disease extent and current labs, then compare tips here with your team plan.",
    ),
    S(
        "Flare eating when urgency dominates",
        "Flare plates prioritize calories, protein, fluids, and gentle textures. Large raw salads and greasy feasts usually wait until stools calm and blood fades.",
        "Split daily intake into five or six small meals if fullness triggers runs to the bathroom. Well cooked carrots, rice, eggs, and broth based soups appear on many clinic handouts.",
        "Keep a short list of safe foods you can shop for on bad days. Predictability lowers anxiety when appetite is low.",
        "If nausea blocks eating, ask about anti nausea options and whether temporary formula support fits your case.",
    ),
    S(
        "Remission eating and expanding variety",
        "Quiet inflammation opens the door to Mediterranean style variety: olive oil, fish, yogurt if lactose is tolerated, legumes in modest portions, and fruit spaced through the day.",
        "Reintroduce fiber with a dietitian when possible. Jumping from zero plants to giant salads overnight invites avoidable cramps.",
        "Calcium and vitamin D routines protect bone health, especially if steroids recently tapered.",
        "Celebrate remission meals without treating any single superfood as a cure.",
    ),
    S(
        "Protein, iron, and rectal bleeding",
        "Slow rectal bleeding can drop ferritin before hemoglobin looks alarming. Include tolerated protein each meal and ask about iron labs when fatigue persists.",
        "Fish, eggs, poultry, tofu, and prescribed supplements each have fans. Vegetarian patients need explicit B12 and iron monitoring plans.",
        "Cooking in cast iron pans is a small trick some use; it does not replace medical iron when stores are empty.",
        "Heavy monthly cycles plus colitis bleeding stack losses in some women; mention both to clinic.",
    ),
    S(
        "Fiber types without jargon piles",
        "Soluble fiber forms gel like textures in oats, peeled cooked apples, and some ground seeds. Many flare plans start there before crunchy insoluble loads.",
        "Insoluble fiber adds speed and bulk: popcorn, kale stems, whole nuts. Those often return in remission with portion trials.",
        "Even UC patients with long segments should ask about strictures before crunchy experiments.",
        "Log stool changes 48 hours after fiber shifts so visits show patterns, not guesses.",
    ),
    S(
        "FODMAP style trials done safely",
        "Fermentable carbohydrates can drive gas and urgency when inflammation is quiet yet bowels remain irritable. Low FODMAP style trials are timed and reversible, not lifelong bans by default.",
        "Work with <a href=\"/blog/fodmap-diet-crohns-colitis\">FODMAP education</a> and a dietitian when you can. DIY forever restriction risks calcium and fiber gaps.",
        "Separate FODMAP trials from alcohol, coffee, and spice experiments so you know what actually moved symptoms.",
        "Reintroduction phases belong on the calendar. Skipping them leaves you stuck in unnecessary elimination.",
    ),
    S(
        "Hydration beyond plain water",
        "Watery stools plus summer heat deplete sodium and potassium faster than thirst signals. Sip through the day; ask whether oral rehydration solutions fit kidney and blood pressure history.",
        "Very sweet sports drinks may worsen urgency for some people. Trial small amounts on stay home days first.",
        "Soups and broths count toward fluids when chewing feels exhausting during flares.",
        "Weigh weekly if diarrhea is heavy; five pounds lost without trying deserves a portal message.",
    ),
    S(
        "Dairy, lactose, and calcium",
        "Lactose intolerance overlaps IBD but is not universal. Yogurt and hard cheese often tolerate better than tall glasses of milk.",
        "If dairy is limited, ask about fortified alternatives and whether vitamin D labs are due.",
        "Calcium goals differ for teens, postmenopausal women, and steroid exposed bones; personalize rather than copy labels.",
        "Lactose free milk is an option for some coffee rituals without abandoning caffeine entirely.",
    ),
    S(
        "Pouch, ostomy, and surgical anatomy",
        "J pouch patients juggle pouchitis flares, nighttime leaks, and different fiber timing than intact colons. Ostomy patients may prioritize output volume and chewing thoroughly.",
        "Bring surgical history to every nutrition visit. Online UC lists rarely mention pouches or stomas.",
        "Skin protection around appliances matters as much as meal choice on high output days.",
        "Surgeon and dietitian messages should align before major texture experiments post op.",
    ),
    S(
        "Tracking meals with IBDPal",
        "Log meal time, portion, cooking method, and symptoms within 24 to 48 hours. Patterns beat memory when calprotectin rises and clinicians ask what changed.",
        "Photo labels of safe pantry items save time when brain fog hits during flares.",
        "See <a href=\"/blog/tracking-food-symptoms-ibdpal\">tracking food and symptoms</a> for practical fields.",
        "Export a one page summary before visits instead of scrolling months of notes.",
    ),
    S(
        "Myths that waste precious energy",
        "Myth: zero fiber forever prevents flares. Reality: treat inflammation medically; reintroduce fiber strategically in remission.",
        "Myth: gluten free automatically heals UC. Reality: benefit appears mainly when celiac or proven intolerance exists.",
        "Myth: juice cleanses reset the colon. Reality: cleanses risk electrolyte imbalance without treating mucosal disease.",
        "Myth: one bad meal caused the flare. Reality: flares usually reflect immune activity; food modulates symptoms around it.",
    ),
    S(
        "Pediatric, pregnancy, and older adult nutrition",
        "Children need growth monitoring during restrictive trials. Parents should avoid unsupervised elimination during growth spurts.",
        "Pregnancy coordinates OB and GI goals for folate, iron, and weight gain. Never start restrictive diets without team approval.",
        "Older adults may need higher protein targets to preserve muscle when flares reduce intake.",
        "School nurses appreciate written safe snack lists when trials are active.",
    ),
    S(
        "Restaurant, travel, and social meals",
        "Scan menus for simple grilled proteins, plain rice, and cooked vegetables. Sauces hide dairy, garlic, and sweeteners that trigger experiments you never planned.",
        "Pack backup snacks you tolerate when flights delay. Airport fiber bars are not automatic friends.",
        "Tell hosts you appreciate simple sides without shame. Most people prefer clarity over surprise bathroom exits.",
        "Time zone shifts change meal rhythm; expect temporary stool changes and log them.",
    ),
    S(
        "When nutrition questions need urgent care",
        "Contact care for inability to keep fluids down, fainting, severe pain unlike baseline, rapid weight loss, or bloody stools with fever.",
        "Use <a href=\"/flare-help\">flare help</a> and <a href=\"/blog/when-to-go-er-ibd\">when to go to the ER</a> for red flag lists.",
        "Malnutrition signs include dizziness standing, hair thinning, and menstrual loss; report them early.",
        "Do not wait for perfect food logs if red flags appear tonight.",
    ),
    S(
        "Alcohol, caffeine, and evening rituals",
        "Beer and wine may irritate lining or speed transit for some UC patients even in remission.",
        "Caffeine timing experiments belong on weekends when bathroom access is easy.",
        "Evening large meals correlate with nocturnal stools; shift calories earlier if sleep suffers.",
        "Discuss alcohol with GI when on methotrexate, thiopurines, or recent flares.",
    ),
    S(
        "Micronutrients clinicians sometimes monitor",
        "Vitamin D, B12, iron, zinc, and magnesium deserve periodic labs when intake is narrow.",
        "Supplement only after blood work; mega doses can harm.",
        "Dietitians translate lab numbers into food first plans before pill stacks.",
        "Keep supplement bottles labeled for anesthesia and surgery medication reviews.",
    ),
    S(
        "Partner and caregiver communication",
        "Housemates can learn your safe foods without policing every bite.",
        "Ask for practical help grocery shopping on fatigue days rather than vague sympathy.",
        "Children in the home benefit from simple explanations that colitis is not contagious.",
        "Caregiver burnout is real; respite meals from friends help.",
    ),
    S(
        "Workplace lunch and break planning",
        "Scout office microwave lines and nearest restrooms before committing to cafeteria experiments.",
        "Pack duplicate safe lunches during flare months to avoid vending machine desperation.",
        "Explain break needs to HR using functional language rather than graphic detail.",
        "Hybrid schedules reduce commute stress when mornings are urgent heavy.",
    ),
    S(
        "Reading labels without obsession",
        "Scan for sweeteners, sugar alcohols, and inulin that surprise sensitive colons.",
        "Serving sizes on labels differ from restaurant portions; log what you actually ate.",
        "Gluten free packaged foods can still be high FODMAP or greasy.",
        "Stop if label reading becomes compulsive; dietitians can simplify rules.",
    ),
    S(
        "Bridging to professional dietitian visits",
        "Bring this overview marked up with questions and three day food photos if allowed.",
        "Ask for written flare and remission targets after each scope season.",
        "Request referral if weight drifts despite appetite you consider normal.",
        "Telehealth dietitian visits count; distance should not block structured help.",
    ),
    S(
        "Sample gentle flare day menu sketch",
        "Breakfast might be scrambled eggs, white toast, and decaf tea if caffeine bothers you.",
        "Midday could be chicken rice soup blended smooth with peeled zucchini.",
        "Afternoon snack might be applesauce and crackers you already trust.",
        "Dinner could be baked salmon flaked small with mashed potatoes and cooked carrots.",
    ),
    S(
        "Sample remission variety day sketch",
        "Breakfast Greek yogurt with blueberries may work if lactose is tolerated.",
        "Lunch salad with olive oil, chickpeas, and tuna varies texture gradually.",
        "Snack almonds in small measured portions if crunch trials succeeded.",
        "Dinner grilled vegetables, quinoa, and herbs keeps plants on the plate without shock loading.",
    ),
]

UC_INTRO = (
    "If you searched <strong>ulcerative colitis diet</strong>, you likely want a calm map for flares and remission without diet cult noise. "
    "Food does not cause ulcerative colitis, and no plate cures inflammation alone. Meals still shape urgency, weight, and confidence leaving home. "
    "This overview pairs with <a href=\"/blog/crohns-diet-overview-ibd\">Crohn's diet overview</a>, "
    "<a href=\"/guides/ulcerative-colitis-diet-foods\">UC diet foods guide</a>, "
    "<a href=\"/blog/flare-foods-ibd\">flare foods</a>, "
    "<a href=\"/blog/mediterranean-diet-autoimmune\">Mediterranean notes</a>, "
    "<a href=\"/blog/fodmap-diet-crohns-colitis\">FODMAP education</a>, and "
    "<a href=\"/ibd-nutrition\">IBD nutrition hub</a>. Education only."
)

def main() -> None:
    from compile_oct11_sections_part2 import ALL_SPECS
    from compile_oct11_sections_part3 import ALL_SPECS as ALL_SPECS_P3

    specs = {
        "ulcerative_colitis_diet.py": dict(
            intro=UC_INTRO,
            sections=UC_SECTIONS,
            clinic=(
                "I want a ulcerative colitis diet plan for flare versus remission. Given my disease extent and recent labs, "
                "what protein, fiber, and hydration targets should I use this month, and when should I see an IBD dietitian?"
            ),
            faqs=[
                (
                    "Is UC diet different from Crohn's diet?",
                    "Themes overlap, yet UC often emphasizes rectal bleeding iron needs and colon fiber timing. Small bowel Crohn's adds malabsorption concerns.",
                ),
                (
                    "Should I cut all raw vegetables in a flare?",
                    "Many teams prefer well cooked produce first, not permanent raw bans. Duration depends on inflammation control.",
                ),
                (
                    "Can diet replace biologics when I feel better?",
                    "No. Quiet symptoms do not always mean quiet inflammation. Stay on the plan unless your GI adjusts it.",
                ),
                (
                    "What if every meal causes urgency?",
                    "That may reflect active inflammation, infection, or bile acid diarrhea. Message clinic before starving yourself.",
                ),
            ],
            related=[
                ("UC diet foods guide", "/guides/ulcerative-colitis-diet-foods"),
                ("Crohn's diet overview", "/blog/crohns-diet-overview-ibd"),
                ("Flare foods", "/blog/flare-foods-ibd"),
                ("Eating With IBD book", "/eating-with-ibd"),
            ],
            closing=[
                "Repeatable safe meals during flares protect weight while medicines work. Expand variety in remission with professional guidance rather than social media elimination spirals.",
            ],
        ),
        **ALL_SPECS,
        **ALL_SPECS_P3,
    }
    from compile_oct11_sections_part4 import EXTRA_BY_FILE
    from compile_oct11_sections_part5 import MORE
    from compile_oct11_sections_part6 import FINAL

    for filename, kw in specs.items():
        merged = dict(kw)
        extra = EXTRA_BY_FILE.get(filename, [])
        more = MORE.get(filename, [])
        final = FINAL.get(filename, [])
        if extra or more or final:
            merged["sections"] = list(merged["sections"]) + extra + more + final
        write_module(filename, **merged)
    print("compiled", len(specs), "body modules")


if __name__ == "__main__":
    main()
