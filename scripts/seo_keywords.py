"""SEO keyword phrases for ibdpal.org pages (meta keywords + structured data hints)."""
from __future__ import annotations

import re
from pathlib import Path

# Site-wide fallback
DEFAULT_KEYWORDS = (
    "IBD, Crohn's disease, ulcerative colitis, inflammatory bowel disease, "
    "IBD support, IBD nutrition, IBD app, IBDPal, MediVue"
)

PATH_KEYWORDS: dict[str, str] = {
    "/": (
        "IBD support, Crohn's disease, ulcerative colitis, free IBD app, "
        "IBD nutrition tracker, IBD community map, patient education, IBDPal"
    ),
    "/about": "IBDPal, MediVue nonprofit, IBD education, Crohn's colitis nonprofit, patient resources",
    "/news": (
        "IBD policy, Crohn's advocacy, colitis legislation, prior authorization, "
        "Safe Step Act, Crohn's and Colitis Foundation, IBD news"
    ),
    "/site-updates": "IBDPal updates, IBD website changelog, patient education site, MediVue",
    "/library": "IBD library, Crohn's guides, colitis articles, patient education, IBDPal resources",
    "/blog": "IBD blog, Crohn's nutrition, colitis flare tips, ulcerative colitis diet, patient stories",
    "/guides": "IBD patient guides, Crohn's checklist, colitis visit prep, IBD tools, printable guides",
    "/support": "IBD support groups, Crohn's chapter, colitis foundation, state IBD resources",
    "/faq": "IBD FAQ, Crohn's questions, ulcerative colitis diet, IBD flare, Crohn's vs colitis",
    "/newly-diagnosed": "newly diagnosed IBD, Crohn's diagnosis, ulcerative colitis first steps, GI questions",
    "/visit-prep": "IBD doctor visit, Crohn's appointment checklist, colitis visit prep, gastroenterologist",
    "/ibd-crohns-support": "IBD support, Crohn's helpline, colitis foundation, IBD peer support",
    "/ibd-nutrition": (
        "IBD nutrition, Crohn's diet, colitis food triggers, IBD meal planning, "
        "enteral nutrition, EEN, exclusive enteral nutrition, tube feeding IBD"
    ),
    "/crohns-disease": "Crohn's disease, Crohn's symptoms, Crohn's diet, Crohn's treatment education",
    "/ulcerative-colitis": "ulcerative colitis, UC diet, colitis flare, colitis symptoms education",
    "/teens-and-school": "teen IBD, Crohn's school 504, colitis accommodations, pediatric IBD",
    "/flare-help": "IBD flare, Crohn's flare diet, colitis flare help, urgent IBD symptoms",
    "/pediatric-caregivers": "pediatric IBD, Crohn's caregiver, child colitis, parent IBD resources",
    "/patient-stories": "IBD patient stories, Crohn's experience, colitis journey, peer support",
    "/research": (
        "IBD research sources, PubMed IBD, Crohn's clinical trials, colitis evidence, "
        "extraintestinal research, autoimmune IBD associations, AGA ACG guidance"
    ),
    "/resources": "IBD resource library, Crohn's links, colitis education, Crohn's & Colitis Foundation, Camp Oasis, prior authorization, patient tools",
    "/ibd-autoimmune-associations": (
        "IBD autoimmune associations, extraintestinal manifestations, PSC IBD, "
        "psoriasis Crohn's, celiac colitis overlap, ankylosing spondylitis IBD"
    ),
    "/guides/anti-inflammatory-diet-ibd": (
        "anti-inflammatory diet IBD, Mediterranean diet Crohn's, colitis nutrition pattern"
    ),
    "/guides/iron-deficiency-nutrition-ibd": (
        "iron deficiency IBD diet, anemia Crohn's food, colitis iron nutrition"
    ),
    "/guides/vitamin-d-bone-nutrition-ibd": (
        "vitamin D IBD, bone health Crohn's, calcium colitis nutrition"
    ),
    "/guides/protein-healing-ibd-flare": (
        "protein IBD flare, healing protein Crohn's, colitis muscle nutrition"
    ),
    "/guides/elimination-diet-when-to-stop-ibd": (
        "elimination diet IBD, when to stop elimination diet, food reintroduction Crohn's"
    ),
    "/crohns-colitis-foundation-resources": (
        "Crohn's & Colitis Foundation resources, IBD Help Center, Camp Oasis, "
        "Foundation diet education, prior authorization IBD, CCF chapters, licensed Foundation education"
    ),
    "/guides/camp-oasis-kids-ibd": (
        "Camp Oasis IBD, Crohn's camp for kids, colitis summer camp, Foundation youth resources"
    ),
    "/guides/ibd-prior-authorization-foundation": (
        "IBD prior authorization, Crohn's insurance approval, colitis step therapy, Foundation prior auth guide"
    ),
    "/guides/foundation-diet-nutrition-ibd": (
        "Foundation diet nutrition IBD, Crohn's Colitis Foundation diet, IBD dietitian resources"
    ),
    "/blog/banana-ibd-crohns-colitis": (
        "banana Crohn's disease, bananas colitis, banana IBD diet, potassium flare food"
    ),
    "/blog/apple-ibd-cooked-vs-raw": (
        "apples Crohn's, applesauce colitis flare, cooked vs raw apple IBD, pectin fiber"
    ),
    "/blog/blueberries-ibd": (
        "blueberries Crohn's disease, blueberries ulcerative colitis, berries IBD diet"
    ),
    "/blog/strawberries-ibd": (
        "strawberries Crohn's, strawberries colitis, vitamin C IBD fruit"
    ),
    "/blog/melon-ibd": (
        "watermelon Crohn's, cantaloupe colitis, melon IBD hydration, potassium fruit"
    ),
    "/blog/avocado-ibd": (
        "avocado Crohn's disease, avocado ulcerative colitis, avocado FODMAP IBD"
    ),
    "/blog/oranges-citrus-ibd": (
        "oranges Crohn's, orange juice colitis, citrus IBD, vitamin C acidity"
    ),
    "/blog/grapes-ibd": (
        "grapes Crohn's disease, grapes ulcerative colitis, grape skins IBD diet"
    ),
    "/blog/chicken-protein-ibd": (
        "chicken Crohn's diet, chicken ulcerative colitis, lean protein IBD poultry"
    ),
    "/blog/eggs-ibd-nutrition": (
        "eggs Crohn's disease, eggs ulcerative colitis, egg protein IBD breakfast"
    ),
    "/blog/white-rice-ibd-flare": (
        "white rice Crohn's flare, rice ulcerative colitis diet, low residue rice IBD"
    ),
    "/blog/turkey-protein-ibd": (
        "turkey Crohn's disease, turkey colitis protein, lean poultry IBD"
    ),
    "/blog/carrots-ibd": (
        "carrots Crohn's disease, cooked carrots colitis, carrot puree IBD"
    ),
    "/blog/potato-ibd-white": (
        "potato Crohn's disease, mashed potatoes colitis flare, white potato IBD"
    ),
    "/blog/sweet-potato-ibd": (
        "sweet potato Crohn's, sweet potato ulcerative colitis, vitamin A IBD"
    ),
    "/blog/spinach-leafy-greens-ibd": (
        "spinach Crohn's disease, leafy greens colitis, spinach iron IBD"
    ),
    "/blog/broccoli-ibd": (
        "broccoli Crohn's disease, broccoli ulcerative colitis gas, cruciferous IBD"
    ),
    "/blog/zucchini-ibd": (
        "zucchini Crohn's disease, zucchini colitis diet, summer squash IBD"
    ),
    "/blog/cucumber-ibd": (
        "cucumber Crohn's disease, cucumber ulcerative colitis, peeled cucumber IBD"
    ),
    "/blog/tomatoes-ibd": (
        "tomatoes Crohn's disease, tomato sauce colitis, tomato acidity IBD"
    ),
    "/blog/onion-garlic-ibd-fodmap": (
        "onion garlic Crohn's, garlic FODMAP colitis, onion IBD bloating"
    ),
    "/blog/corn-ibd": (
        "corn Crohn's disease, corn ulcerative colitis, corn kernels stricture IBD"
    ),
    "/blog/calcium-ibd": (
        "calcium Crohn's disease, calcium ulcerative colitis bones, calcium IBD steroids"
    ),
    "/blog/zinc-ibd": (
        "zinc deficiency Crohn's, zinc ulcerative colitis, zinc IBD diarrhea"
    ),
    "/blog/magnesium-ibd": (
        "magnesium Crohn's disease, magnesium deficiency colitis, magnesium IBD cramps"
    ),
    "/blog/potassium-ibd": (
        "potassium Crohn's diarrhea, low potassium colitis, potassium IBD electrolytes"
    ),
    "/blog/vitamin-c-ibd": (
        "vitamin C Crohn's disease, vitamin C ulcerative colitis, ascorbic acid IBD"
    ),
    "/blog/folate-ibd": (
        "folate Crohn's methotrexate, folic acid ulcerative colitis, folate IBD pregnancy"
    ),
    "/blog/vitamin-a-ibd": (
        "vitamin A Crohn's disease, vitamin A deficiency colitis, beta-carotene IBD"
    ),
    "/blog/omega-3-ibd": (
        "omega-3 Crohn's disease, fish oil ulcerative colitis, EPA DHA IBD"
    ),
    "/glossary": "IBD glossary, Crohn's terms, colitis definitions, biologics IBD",
    "/impact": "IBDPal impact, IBD education nonprofit, MediVue mission, patient outcomes",
    "/founder": "IBDPal founder, IBDPal mission, IBD education, Crohn's colitis education",
    "/contact": "contact IBDPal, MediVue IBD, patient education feedback",
    "/for-clinicians": "IBD clinicians, gastroenterology education, patient engagement tools",
    "/clinical-partnerships": "IBD clinical partnerships, GI education, nonprofit collaboration",
    "/executive-summary": "MediVue executive summary, IBDPal nonprofit, IBD program overview",
    "/terms": "IBDPal terms of service, IBD app terms, MediVue user agreement",
    "/privacy": "IBDPal privacy policy, IBD app privacy, health data nonprofit",
    "/es/recursos": "EII español, Crohn colitis recursos, enfermedad inflamatoria intestinal",
    "/es/preguntas-frecuentes": "preguntas EII, Crohn colitis FAQ español, dieta EII",
}

SLUG_TOPIC_WORDS = {
    "flare": "IBD flare, Crohn's flare, colitis symptoms",
    "nutrition": "IBD nutrition, Crohn's diet, colitis food",
    "crohn": "Crohn's disease, IBD Crohn's",
    "colitis": "ulcerative colitis, IBD colitis",
    "diet": "IBD diet, Crohn's nutrition, colitis meal plan",
    "food": "IBD food triggers, Crohn's diet, colitis nutrition",
    "stress": "IBD stress, Crohn's mental health, colitis coping",
    "exercise": "IBD exercise, Crohn's activity, colitis fitness",
    "sleep": "IBD sleep, Crohn's fatigue, colitis rest",
    "teen": "teen IBD, adolescent Crohn's, school colitis",
    "college": "college IBD, Crohn's campus, student colitis",
    "caregiver": "IBD caregiver, Crohn's parent, colitis family",
    "biologic": "IBD biologics, Crohn's medication, colitis treatment",
    "icn": "ImproveCareNow, IBD toolkit, patient education",
    "visit": "IBD doctor visit, gastroenterology appointment",
    "hydration": "IBD hydration, Crohn's fluids, colitis electrolytes",
    "fiber": "IBD fiber, Crohn's low residue, colitis diet",
    "enteral": "enteral nutrition, EEN, exclusive enteral nutrition, entereal, Crohn's formula feeding",
    "prebiotic": "prebiotic formula, scFOS, formula fiber, enteral prebiotics, IBD microbiome nutrition",
    "dysbiosis": "gut dysbiosis, leaky gut education, gut barrier IBD, microbiome imbalance Crohn's",
    "barrier": "gut barrier IBD, intestinal barrier, microbiome inflammation, dysbiosis education",
    "parenteral": "parenteral nutrition, TPN IBD, hospital feeding, IV nutrition Crohn's",
    "hospital": "hospital feeding IBD, NPO IBD, post surgery nutrition Crohn's, tube feeds hospital",
    "partial": "partial enteral nutrition, PEN Crohn's, exclusive vs partial EEN",
    "fever": "IBD fever, flare vs infection, biologics fever, Crohn's fever education",
    "dehydration": "IBD dehydration, colitis fluids, Crohn's rehydration, flare dehydration",
    "electrolyte": "IBD electrolytes, flare electrolytes, Crohn's sodium potassium",
    "vomiting": "IBD vomiting, bowel obstruction Crohn's, stricture nausea education",
    "obstruction": "IBD obstruction, Crohn's stricture, bowel blockage education",
    "sacroiliitis": "IBD sacroiliitis, axial arthritis Crohn's, back pain colitis",
    "calprotectin": "fecal calprotectin, IBD labs, CRP Crohn's, colitis bloodwork",
    "constipation": "IBD constipation, Crohn's stricture constipation, hard stools colitis",
    "diarrhea": "chronic diarrhea IBD, Crohn's diarrhea causes, colitis loose stools",
    "bleeding": "blood in stool IBD, rectal bleeding Crohn's, colitis bleeding education",
    "vaccine": "IBD vaccines, biologics immunization, immunosuppressant vaccines",
    "biologic": "IBD biologics, Crohn's medication, colitis treatment",
    "entyvio": "Entyvio, vedolizumab IBD, gut-selective biologic education",
    "steroid": "IBD steroids, prednisone taper Crohn's, budesonide colitis",
    "taper": "steroid taper IBD, prednisone taper Crohn's, adrenal recovery education",
    "autoimmune": "IBD autoimmune, autoimmune overlap Crohn's, immune-mediated IBD",
    "symptoms": "IBD flare symptoms, Crohn's flare signs, colitis symptoms education",
    "autoimmune": "IBD autoimmune, autoimmune overlap Crohn's, immune-mediated IBD",
    "extraintestinal": "extraintestinal manifestations IBD, EIM Crohn's, colitis outside the gut",
    "psc": "PSC IBD, primary sclerosing cholangitis colitis, bile duct IBD",
    "psoriasis": "psoriasis IBD, Crohn's psoriasis, colitis skin inflammation",
    "celiac": "celiac IBD, celiac screening Crohn's, gluten ulcerative colitis",
    "spondylitis": "ankylosing spondylitis IBD, axial spondyloarthritis Crohn's",
    "osteoporosis": "osteoporosis IBD, bone health Crohn's, steroid bone loss colitis",
    "thrombosis": "IBD clot risk, thrombosis Crohn's, VTE ulcerative colitis",
    "vitamin": "vitamin D IBD, micronutrients Crohn's, colitis vitamins",
    "elimination": "elimination diet IBD, food reintroduction Crohn's, colitis trigger diet",
    "iron": "iron deficiency IBD, anemia Crohn's diet, colitis iron",
    "protein": "protein IBD flare, protein Crohn's healing, colitis nutrition protein",
    "banana": "banana IBD, banana Crohn's, bananas colitis, potassium flare food",
    "apple": "apple IBD, applesauce Crohn's, cooked apple colitis, apple fiber",
    "blueberry": "blueberries IBD, blueberries Crohn's, berries colitis diet",
    "strawberry": "strawberries IBD, strawberries Crohn's, vitamin C colitis",
    "melon": "melon IBD, watermelon Crohn's, cantaloupe colitis, hydrating fruit",
    "avocado": "avocado IBD, avocado Crohn's, avocado colitis, healthy fats FODMAP",
    "orange": "oranges IBD, citrus Crohn's, orange juice colitis, vitamin C",
    "citrus": "citrus IBD, oranges Crohn's, citrus colitis acidity",
    "grape": "grapes IBD, grapes Crohn's, grape skins colitis diet",
    "chicken": "chicken IBD, chicken Crohn's diet, poultry colitis protein",
    "egg": "eggs IBD, eggs Crohn's, eggs colitis protein, choline nutrition",
    "rice": "white rice IBD, rice Crohn's flare, white rice colitis diet",
    "turkey": "turkey IBD, turkey Crohn's protein, poultry colitis nutrition",
    "carrot": "carrots IBD, cooked carrots Crohn's, carrot puree colitis",
    "potato": "potato IBD, mashed potato Crohn's flare, white potato colitis",
    "spinach": "spinach IBD, leafy greens Crohn's, spinach iron colitis",
    "broccoli": "broccoli IBD, broccoli Crohn's gas, cruciferous colitis",
    "zucchini": "zucchini IBD, zucchini Crohn's, summer squash colitis",
    "cucumber": "cucumber IBD, cucumber Crohn's, peeled cucumber colitis",
    "tomato": "tomatoes IBD, tomato sauce Crohn's, tomato acidity colitis",
    "onion": "onion IBD, onion FODMAP Crohn's, onion garlic colitis",
    "garlic": "garlic IBD, garlic FODMAP Crohn's, garlic colitis bloating",
    "corn": "corn IBD, corn Crohn's stricture, corn kernels colitis",
    "calcium": "calcium IBD, calcium Crohn's bones, calcium colitis steroids",
    "zinc": "zinc IBD, zinc deficiency Crohn's, zinc colitis",
    "magnesium": "magnesium IBD, magnesium Crohn's, magnesium colitis cramps",
    "potassium": "potassium IBD, potassium Crohn's diarrhea, potassium colitis",
    "folate": "folate IBD, folic acid Crohn's methotrexate, folate colitis",
    "omega": "omega-3 IBD, fish oil Crohn's, omega-3 colitis",
}


def _slug_keywords(slug: str) -> str:
    base = "IBD, Crohn's disease, ulcerative colitis, patient education"
    extra: list[str] = []
    lower = slug.lower().replace("-", " ")
    for token, phrase in SLUG_TOPIC_WORDS.items():
        if token in lower:
            extra.append(phrase)
    if extra:
        return f"{base}, {', '.join(dict.fromkeys(extra))}"
    readable = re.sub(r"[-_]+", " ", slug).strip()
    return f"{base}, {readable}"


def html_path_to_url(rel: Path) -> str | None:
    parts = rel.parts
    name = rel.name
    if name == "index.html":
        if len(parts) == 1:
            return "/"
        if parts[0] == "blogs":
            return "/blog"
        if parts[0] == "guides":
            return "/guides"
        if parts[0] == "support":
            return "/support"
        if parts[0] == "patient-stories":
            return "/patient-stories"
        if parts[0] == "es" and len(parts) > 2:
            return f"/es/{parts[1]}"
        return None
    if len(parts) == 1 and name.endswith(".html"):
        return f"/{name[:-5]}"
    if len(parts) == 2 and parts[0] == "blogs" and name.endswith(".html"):
        return f"/blog/{name[:-5]}"
    if len(parts) == 2 and parts[0] == "guides" and name.endswith(".html"):
        return f"/guides/{name[:-5]}"
    if len(parts) == 2 and parts[0] == "support" and name.endswith(".html"):
        return f"/support/{name[:-5]}"
    if len(parts) == 2 and parts[0] == "patient-stories" and name.endswith(".html"):
        return f"/patient-stories/{name[:-5]}"
    if len(parts) == 2 and parts[0] == "es" and name.endswith(".html"):
        return f"/es/{name[:-5]}"
    return None


def keywords_for_path(path: str) -> str:
    if path in PATH_KEYWORDS:
        return PATH_KEYWORDS[path]
    if path.startswith("/blog/"):
        return _slug_keywords(path.rsplit("/", 1)[-1])
    if path.startswith("/guides/"):
        return _slug_keywords(path.rsplit("/", 1)[-1])
    if path.startswith("/support/"):
        state = path.rsplit("/", 1)[-1].replace("-", " ")
        return f"IBD support {state}, Crohn's colitis {state}, IBD chapter {state}"
    if path.startswith("/patient-stories/"):
        return _slug_keywords(path.rsplit("/", 1)[-1]) + ", IBD patient story"
    if path.startswith("/es/"):
        return PATH_KEYWORDS.get(path, "EII, Crohn, colitis ulcerosa, educación pacientes español")
    return DEFAULT_KEYWORDS
