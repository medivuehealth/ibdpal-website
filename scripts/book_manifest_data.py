"""Chapter manifest for Eating With IBD book compiler."""

AUTHOR_NAME = "Aryan Shashi Kumar"

BOOK_TITLE = "Eating With IBD"
BOOK_SUBTITLE = (
    "A Practical Guide to Nutrition, Deficiencies, and Food Choices for "
    "Crohn's Disease and Ulcerative Colitis"
)

PARTS = [
    {"num": 1, "title": "IBD, the Gut, and Why Nutrition Matters"},
    {"num": 2, "title": "Flare, Remission, and Everyday Eating"},
    {"num": 3, "title": "Deficiencies, DRI, and Micronutrients"},
    {"num": 4, "title": "Diet Patterns and FODMAP"},
    {"num": 5, "title": "Enteral Nutrition and EEN"},
    {"num": 6, "title": "Food Reference Library"},
    {"num": 7, "title": "Supplements, Probiotics, and Myths"},
    {"num": 8, "title": "Life Situations"},
    {"num": 9, "title": "Tracking, Teams, and Your Next Visit"},
]

# Each chapter: part, num, title, intro, bridge, sources (site paths), stub (optional new prose)
CHAPTERS = [
    {
        "part": 1,
        "num": 1,
        "title": "What IBD Does to Eating",
        "intro": (
            "If you live with Crohn's disease or ulcerative colitis, food is never just food. "
            "Inflammation, scarring, surgery, and medication side effects can change appetite, "
            "absorption, and tolerance overnight. This chapter maps those changes in plain language "
            "so later chapters about flare meals and labs make sense."
        ),
        "bridge": (
            "Crohn's and colitis are both IBD, but they do not always affect digestion the same way. "
            "The next chapter compares how disease location shapes food risk."
        ),
        "rewrite": True,
        "sources": [],
    },
    {
        "part": 1,
        "num": 2,
        "title": "Crohn's vs Colitis: Different Guts, Different Food Risks",
        "intro": (
            "Small bowel Crohn's, colonic disease, prior resection, and strictures each create "
            "different nutrition priorities. Compare your pattern to general education here, "
            "then personalize with your gastroenterologist."
        ),
        "bridge": (
            "Location explains part of the story; inflammation and surgery explain more. "
            "Chapter 3 covers malabsorption, weight change, and when ostomy or resection "
            "changes what you can eat."
        ),
        "sources": [
            "/guides/crohns-disease-diet-nutrition.html",
            "/guides/ulcerative-colitis-diet-foods.html",
        ],
    },
    {
        "part": 1,
        "num": 3,
        "title": "Inflammation, Malabsorption, and Surgery",
        "intro": (
            "Active inflammation steals energy and nutrients. Surgery and short bowel change "
            "what you absorb even when appetite returns. This chapter connects symptoms "
            "to the labs and food strategies in Part III."
        ),
        "bridge": (
            "IBD sits in a wider autoimmune landscape online. Chapter 4 separates helpful "
            "context from viral 'autoimmune diet' myths."
        ),
        "rewrite": True,
        "sources": [],
    },
    {
        "part": 1,
        "num": 4,
        "title": "Autoimmune Overlap Without Autoimmune Diet Myths",
        "intro": (
            "Many people encounter 'autoimmune diet' advice after an IBD diagnosis. Some overlap "
            "conditions are real; most one-size elimination protocols are not. This chapter "
            "keeps the science and drops the marketing."
        ),
        "bridge": (
            "You now know why IBD changes nutrition needs. Part II turns that into "
            "day-to-day choices, starting with the question most patients ask first: "
            "'What should I eat this week?'"
        ),
        "sources": [
            "/guides/autoimmune-nutrition-basics.html",
            "/blog/autoimmune-diet-myths.html",
        ],
    },
    {
        "part": 1,
        "num": 5,
        "title": "What Good IBD Nutrition Care Looks Like",
        "intro": (
            "Good care pairs medical therapy with practical food skills. It uses dietitians, "
            "labs, and realistic goals, not fear-based restriction. This chapter summarizes "
            "patterns aligned with major IBD education sources."
        ),
        "bridge": (
            "Part II opens with the honest answer to 'What should I eat?', because no "
            "single internet list fits every patient or every season of disease."
        ),
        "rewrite": True,
        "sources": [],
    },
    {
        "part": 2,
        "num": 6,
        "title": "What Should I Eat? The Honest Answer",
        "intro": (
            "There is no universal IBD diet. What you eat this month depends on whether "
            "inflammation is active, where disease sits, and what you tolerate. This chapter "
            "gives an honest framework before flare-specific lists."
        ),
        "bridge": (
            "When symptoms escalate, gentler textures and smaller portions often help. "
            "Chapter 7 focuses on flare-first eating."
        ),
        "sources": [
            "/guides/what-should-i-eat-crohns-colitis.html",
        ],
    },
    {
        "part": 2,
        "num": 7,
        "title": "Flare-First Eating",
        "intro": (
            "During flares the goal is enough calories, protein, and fluids with foods that "
            "do not worsen urgency or pain. This chapter brings together practical strategies "
            "meant to be temporary, not permanent."
        ),
        "bridge": (
            "As inflammation quiets, variety returns. Chapter 8 covers remission eating "
            "without rushing reintroduction."
        ),
        "sources": [
            "/guides/foods-to-eat-crohns-flare.html",
        ],
    },
    {
        "part": 2,
        "num": 8,
        "title": "Remission: Expanding Variety Safely",
        "intro": (
            "Remission does not mean that every food will suddenly be tolerated. It creates "
            "an opportunity to rebuild dietary variety gradually and identify what works for you."
        ),
        "bridge": (
            "Not every symptom after eating proves a trigger. Chapter 9 separates irritant "
            "responses from inflammatory flares."
        ),
        "rewrite": True,
        "sources": [],
    },
    {
        "part": 2,
        "num": 9,
        "title": "Triggers vs Inflammation",
        "intro": (
            "Food logs help when you interpret them with labs and scopes. A bad week after "
            "dairy differs from rising calprotectin. Learn to tell them apart."
        ),
        "bridge": (
            "Hydration and electrolytes underpin every meal plan in IBD. Chapter 10 covers "
            "fluids when diarrhea, heat, or vomiting increase losses."
        ),
        "sources": [
            "/guides/crohns-food-triggers.html",
        ],
    },
    {
        "part": 2,
        "num": 10,
        "title": "Hydration and Electrolytes",
        "intro": (
            "Diarrhea and fever quietly drain fluid and sodium. This chapter covers daily "
            "hydration, oral rehydration, and when losses need urgent attention."
        ),
        "bridge": (
            "Protein supports healing when inflammation is active. Chapter 11 translates "
            "that into plates you can actually eat."
        ),
        "sources": [
            "/guides/ibd-hydration-fluids.html",
        ],
    },
    {
        "part": 2,
        "num": 11,
        "title": "Protein for Healing",
        "intro": (
            "Protein needs may increase during active inflammation, recovery, surgery, or "
            "malnutrition. Spread intake across the day when appetite is low and choose tender "
            "preparations during flares."
        ),
        "bridge": (
            "Fiber is the most debated macronutrient in IBD. Chapter 12 explains timing, "
            "strictures, and reintroduction."
        ),
        "sources": [
            "/guides/protein-healing-ibd-flare.html",
        ],
    },
    {
        "part": 2,
        "num": 12,
        "title": "Fiber: Friend, Foe, and Timing",
        "intro": (
            "Soluble and insoluble fiber behave differently. Strictures and active colitis "
            "change what is safe. Do not copy fiber rules from general wellness blogs."
        ),
        "bridge": (
            "Day-to-day meals depend on symptoms. Part III zooms out to labs, DRIs, and "
            "deficiencies, the numbers behind fatigue and bone loss."
        ),
        "sources": [
            "/blog/fiber-and-ibd-diet.html",
        ],
    },
    {
        "part": 3,
        "num": 13,
        "title": "How to Read Nutrition Labs",
        "intro": (
            "Calprotectin and CRP reflect inflammation; ferritin and B12 reflect stores. "
            "This chapter explains what nutrition labs mean, not to self-diagnose, but to "
            "ask better questions."
        ),
        "bridge": (
            "Dietary Reference Intakes provide population nutrition benchmarks. Chapter 14 "
            "connects those baselines to IBD realities."
        ),
        "rewrite": True,
        "sources": [],
    },
    {
        "part": 3,
        "num": 14,
        "title": "DRI Basics for IBD Patients",
        "intro": (
            "DRI tables describe population targets. IBD may raise needs or block absorption. "
            "Use DRIs as a conversation starter with your team, not a self-prescription."
        ),
        "bridge": (
            "Iron is the most common deficiency patients feel. Chapter 15 goes deep on "
            "anemia, oral iron, and IV repletion."
        ),
        "sources": [],
        "append_dri": True,
    },
    {
        "part": 3,
        "num": 15,
        "title": "Iron and Anemia",
        "intro": (
            "Bleeding, inflammation, and restricted diets drain iron. Symptoms may appear "
            "before you notice blood in stool."
        ),
        "bridge": (
            "Bone health depends on vitamin D and calcium, especially on steroids. "
            "Chapter 16 covers both."
        ),
        "sources": [
            "/guides/iron-deficiency-nutrition-ibd.html",
        ],
        "append_food_sources": ["iron"],
    },
    {
        "part": 3,
        "num": 16,
        "title": "Vitamin D, Calcium, and Bone Health",
        "intro": (
            "Steroids, inflammation, and malabsorption threaten bone density. Nutrition and "
            "monitoring work together over years, not weeks."
        ),
        "bridge": (
            "B12 and folate explain some fatigue when iron is normal. Chapter 17 connects "
            "neurologic symptoms to absorption."
        ),
        "sources": [
            "/guides/vitamin-d-bone-nutrition-ibd.html",
        ],
        "append_food_sources": ["vitamin-d", "calcium"],
    },
    {
        "part": 3,
        "num": 17,
        "title": "B12, Folate, and Fatigue",
        "intro": (
            "Terminal ileum disease and resection raise B12 risk. Folate matters for blood "
            "and medication interactions. Fatigue rarely has one cause."
        ),
        "bridge": (
            "Zinc, magnesium, and potassium losses often hide in plain sight during flares. "
            "Chapter 18 covers them together."
        ),
        "rewrite": True,
        "sources": [],
        "append_food_sources": ["folate", "vitamin-b12"],
    },
    {
        "part": 3,
        "num": 18,
        "title": "Zinc, Magnesium, Potassium, and Electrolytes",
        "intro": (
            "Chronic diarrhea and restricted diets deplete minerals. Replacement should follow "
            "labs when possible."
        ),
        "bridge": (
            "Fat-soluble vitamins and omega-3s round out the micronutrient picture in Chapter 19."
        ),
        "sources": [
            "/blog/zinc-ibd.html",
            "/blog/magnesium-ibd.html",
            "/blog/potassium-ibd.html",
        ],
        "append_food_sources": ["zinc", "magnesium", "potassium"],
    },
    {
        "part": 3,
        "num": 19,
        "title": "Vitamins A, C, Omega-3, and Selenium",
        "intro": (
            "These nutrients support immunity, healing, and inflammation modulation. Food "
            "first; supplements only when your team agrees."
        ),
        "bridge": (
            "Sometimes food and pills are not enough. Chapter 20 discusses IV iron, shakes, "
            "and when to escalate."
        ),
        "sources": [
            "/blog/vitamin-a-ibd.html",
            "/blog/vitamin-c-ibd.html",
            "/blog/omega-3-ibd.html",
        ],
        "append_food_sources": ["vitamin-c", "omega-3", "selenium"],
    },
    {
        "part": 3,
        "num": 20,
        "title": "When Food Is Not Enough: Supplements and Infusions",
        "intro": (
            "Oral supplements fail for some patients. IV iron, liquid nutrition, and "
            "prescription repletion have roles, under medical supervision."
        ),
        "bridge": (
            "Labs tell you what you need. Part IV explores named diet patterns: FODMAP, "
            "low-residue, and elimination trials."
        ),
        "rewrite": True,
        "sources": [],
    },
    {
        "part": 4,
        "num": 21,
        "title": "No Single IBD Diet",
        "intro": (
            "Carnivore, cleanse, and juice protocols circulate online. This chapter states "
            "what evidence supports, and what it does not."
        ),
        "bridge": (
            "Low-residue and gentle textures remain useful tools for selected patients. "
            "Chapter 22 explains how and when."
        ),
        "rewrite": True,
        "sources": [],
    },
    {
        "part": 4,
        "num": 22,
        "title": "Low-Residue and Gentle Textures",
        "intro": (
            "Lower fiber and softer textures can reduce bulk during flares. This is a "
            "bridge diet, not a life sentence."
        ),
        "bridge": (
            "FODMAP trials address fermentable carbohydrates when gas and bloating dominate. "
            "Chapter 23 introduces the basics."
        ),
        "sources": [
            "/guides/low-residue-diet-ibd.html",
        ],
    },
    {
        "part": 4,
        "num": 23,
        "title": "FODMAP: Basics and Limits",
        "intro": (
            "Low FODMAP is a supervised tool for symptom relief, not a treatment for "
            "inflammation. Understand limits before you start."
        ),
        "bridge": (
            "Restriction without reintroduction stalls progress. Chapter 24 covers "
            "systematic FODMAP reintroduction."
        ),
        "sources": [
            "/blog/fodmap-diet-crohns-colitis.html",
            "/blog/onion-garlic-ibd-fodmap.html",
        ],
    },
    {
        "part": 4,
        "num": 24,
        "title": "FODMAP Reintroduction",
        "intro": (
            "Elimination is only half the process. Reintroduction maps your personal "
            "tolerance so nutrition stays adequate."
        ),
        "bridge": (
            "Broader elimination diets need exit plans too. Chapter 25 covers when to stop."
        ),
        "rewrite": True,
        "stub": True,
    },
    {
        "part": 4,
        "num": 25,
        "title": "Elimination Diets: When to Start and Stop",
        "intro": (
            "Structured elimination can clarify triggers under supervision. Staying on "
            "minimal lists too long risks malnutrition."
        ),
        "bridge": (
            "Mediterranean and anti-inflammatory patterns offer positive food choices "
            "without extreme rules. Chapter 26 explores them."
        ),
        "sources": [
            "/guides/elimination-diet-when-to-stop-ibd.html",
        ],
    },
    {
        "part": 4,
        "num": 26,
        "title": "Mediterranean and Anti-Inflammatory Patterns",
        "intro": (
            "These patterns emphasize plants, olive oil, and fish. They fit many remission "
            "plates when fiber tolerance allows."
        ),
        "bridge": (
            "Dairy, gluten, and cultural staples deserve their own chapter, Chapter 27."
        ),
        "sources": [
            "/guides/anti-inflammatory-diet-ibd.html",
            "/blog/mediterranean-diet-autoimmune.html",
            "/blog/salmon-fish-ibd.html",
        ],
    },
    {
        "part": 4,
        "num": 27,
        "title": "Dairy, Gluten, and Cultural Staples",
        "intro": (
            "Lactose intolerance can flare with inflammation. Gluten matters for celiac "
            "screening, not everyone with IBD. Cultural foods belong in realistic plans."
        ),
        "bridge": (
            "Some patients need formula-based nutrition. Part V covers enteral nutrition "
            "and EEN."
        ),
        "sources": [
            "/blog/dairy-lactose-ibd.html",
            "/blog/gluten-wheat-ibd.html",
            "/blog/chapati-roti-ibd.html",
            "/blog/dal-lentils-ibd.html",
            "/blog/congee-rice-porridge-ibd.html",
        ],
    },
    {
        "part": 5,
        "num": 28,
        "title": "Enteral Nutrition: What It Is and Who Uses It",
        "intro": (
            "Liquid formula can rest the bowel while delivering calories and protein. "
            "It is medicine-adjacent nutrition, not a wellness shake."
        ),
        "bridge": (
            "Exclusive and partial regimens differ in goals and duration. Chapter 29 compares them."
        ),
        "sources": ["/blog/enteral-nutrition-ibd.html"],
    },
    {
        "part": 5,
        "num": 29,
        "title": "Exclusive vs Partial Enteral Nutrition",
        "intro": (
            "EEN is a defined Crohn's therapy in many centers. Partial regimens support "
            "growth and bridging. Know which you are discussing with your team."
        ),
        "bridge": (
            "Formula type and delivery route affect daily life. Chapter 30 covers tubes, "
            "taste fatigue, and school or work logistics."
        ),
        "sources": [
            "/blog/exclusive-vs-partial-enteral-nutrition-crohns.html",
            "/blog/adult-een-crohns-what-to-expect.html",
        ],
    },
    {
        "part": 5,
        "num": 30,
        "title": "Formulas, Tubes, and Practical Life",
        "intro": (
            "Elemental vs polymeric formulas, NG tubes, and overnight feeds each come with "
            "tradeoffs. Practical questions matter as much as biochemistry."
        ),
        "bridge": (
            "Hospital and post-surgery feeding raise additional issues. Chapter 31 addresses them."
        ),
        "sources": [
            "/blog/elemental-vs-polymeric-formula-ibd.html",
            "/blog/nasogastric-tube-feeds-ibd-practical.html",
            "/blog/taste-fatigue-enteral-formula-ibd.html",
        ],
    },
    {
        "part": 5,
        "num": 31,
        "title": "EEN After Surgery and in Hospital",
        "intro": (
            "Surgery changes anatomy; hospital stays disrupt routines. Reintroduction to "
            "solids should be staged with your surgical and GI teams."
        ),
        "bridge": (
            "When you return to solids, Part VI is your food reference, organized by category."
        ),
        "sources": [
            "/blog/hospital-feeding-ibd-enteral-parenteral.html",
            "/blog/food-reintroduction-after-een-ibd.html",
        ],
    },
    {
        "part": 6,
        "num": 32,
        "title": "Gentle Starches and Breads",
        "intro": "Starches anchor many flare-friendly plates. The entries below summarize how common starches fit flare and remission eating.",
        "bridge": "Protein foods in Chapter 33 pair with these starches for balanced meals.",
        "sources": [
            "/blog/white-rice-ibd-flare.html",
            "/blog/white-bread-ibd.html",
            "/blog/potato-ibd-white.html",
            "/blog/sweet-potato-ibd.html",
            "/blog/oatmeal-ibd.html",
            "/blog/tortillas-ibd.html",
            "/blog/couscous-ibd.html",
            "/blog/congee-rice-porridge-ibd.html",
        ],
    },
    {
        "part": 6,
        "num": 33,
        "title": "Proteins",
        "intro": "Adequate protein supports mucosal repair. Choose tender preparations during active symptoms.",
        "bridge": "Fruits in Chapter 34 add potassium and gentle calories when tolerated.",
        "sources": [
            "/blog/chicken-protein-ibd.html",
            "/blog/turkey-protein-ibd.html",
            "/blog/eggs-ibd-nutrition.html",
            "/blog/salmon-fish-ibd.html",
            "/blog/tuna-ibd.html",
            "/blog/lean-beef-ibd.html",
            "/blog/tofu-soy-ibd.html",
            "/blog/paneer-ibd.html",
        ],
    },
    {
        "part": 6,
        "num": 34,
        "title": "Fruits",
        "intro": "Fruit tolerance varies by ripeness, fiber, and FODMAP content.",
        "bridge": "Vegetables in Chapter 35 often need cooking or peeling during flares.",
        "sources": [
            "/blog/banana-ibd-crohns-colitis.html",
            "/blog/apple-ibd-cooked-vs-raw.html",
            "/blog/blueberries-ibd.html",
            "/blog/avocado-ibd.html",
            "/blog/melon-ibd.html",
            "/blog/grapes-ibd.html",
            "/blog/strawberries-ibd.html",
            "/blog/oranges-citrus-ibd.html",
            "/blog/dates-ramadan-ibd.html",
            "/blog/plantain-ibd.html",
        ],
    },
    {
        "part": 6,
        "num": 35,
        "title": "Vegetables",
        "intro": "Texture and fiber type matter more than the vegetable's reputation.",
        "bridge": "Legumes and fermented foods appear in Chapter 36.",
        "sources": [
            "/blog/carrots-ibd.html",
            "/blog/zucchini-ibd.html",
            "/blog/cucumber-ibd.html",
            "/blog/spinach-leafy-greens-ibd.html",
            "/blog/broccoli-ibd.html",
            "/blog/tomatoes-ibd.html",
            "/blog/corn-ibd.html",
            "/blog/potato-ibd-white.html",
        ],
    },
    {
        "part": 6,
        "num": 36,
        "title": "Legumes and Cultural Staples",
        "intro": "Dal, flatbreads, and fermented foods carry culture and protein, adapt prep for tolerance.",
        "bridge": "Beverages in Chapter 37 affect urgency and hydration.",
        "sources": [
            "/blog/dal-lentils-ibd.html",
            "/blog/chapati-roti-ibd.html",
            "/blog/miso-soup-ibd.html",
            "/blog/kimchi-fermented-ibd.html",
        ],
    },
    {
        "part": 6,
        "num": 37,
        "title": "Beverages",
        "intro": "Caffeine, acidity, and alcohol interact with symptoms and hydration.",
        "bridge": "Snacks and treats in Chapter 38 finish the food reference section.",
        "sources": [
            "/blog/coffee-ibd.html",
            "/blog/tea-ibd.html",
            "/blog/hydration-tips-ibd.html",
        ],
    },
    {
        "part": 6,
        "num": 38,
        "title": "Snacks, Fats, and Treats",
        "intro": "Calorie-dense snacks help when appetite is low. Portion and ingredients still matter.",
        "bridge": "Chapter 39 suggests sample flare-day combinations using prior entries.",
        "sources": [
            "/blog/peanut-butter-ibd.html",
            "/blog/chocolate-ibd.html",
            "/blog/greek-yogurt-ibd.html",
            "/blog/bone-broth-gut-healing-ibd.html",
        ],
    },
    {
        "part": 6,
        "num": 39,
        "title": "Flare-Day Sample Combinations",
        "intro": "These sample days illustrate gentle combinations, not prescriptions.",
        "bridge": "Whole foods come first; supplements second. Part VII separates evidence from marketing.",
        "rewrite": True,
        "stub": True,
    },
    {
        "part": 7,
        "num": 40,
        "title": "Supplements: A Cautious Framework",
        "intro": (
            "Supplements fill gaps; they rarely replace IBD therapy. Discuss brands, doses, "
            "and interactions with your team."
        ),
        "bridge": "Probiotics and microbiome tests dominate headlines. Chapter 41 addresses them.",
        "sources": [
            "/guides/foundation-complementary-medicine-ibd.html",
        ],
    },
    {
        "part": 7,
        "num": 41,
        "title": "Probiotics and Microbiome Tests",
        "intro": (
            "Some probiotic regimens have research in specific settings. Direct-to-consumer "
            "microbiome kits are not clinical pathways."
        ),
        "bridge": "Collagen, cleanses, and fasting protocols are covered in Chapter 42.",
        "sources": [
            "/blog/probiotics-ibd-gut-health.html",
            "/blog/probiotics-ibd-practical-guide.html",
            "/blog/microbiome-lab-testing-ibd.html",
        ],
    },
    {
        "part": 7,
        "num": 42,
        "title": "Collagen, Cleanses, and Viral Diets",
        "intro": "Marketing often outruns evidence. This chapter states what is known and unknown.",
        "bridge": "Medications change appetite and absorption. Chapter 43 connects steroids and biologics to food.",
        "sources": [
            "/blog/collagen-supplements-ibd.html",
            "/blog/juice-cleanse-detox-ibd.html",
            "/blog/intermittent-fasting-ibd.html",
        ],
    },
    {
        "part": 7,
        "num": 43,
        "title": "Steroids, Biologics, and Appetite",
        "intro": (
            "Prednisone hunger, post-infusion fatigue, and infection caution each affect "
            "nutrition choices."
        ),
        "bridge": "Life outside the kitchen matters too. Part VIII begins with dining out and travel.",
        "sources": [
            "/blog/prednisone-diet-hunger-ibd.html",
        ],
    },
    {
        "part": 8,
        "num": 44,
        "title": "Dining Out and Travel",
        "intro": "Restaurants and travel require planning, menus, restrooms, and medication storage.",
        "bridge": "Teens face growth and school constraints. Chapter 45 addresses them.",
        "sources": [
            "/guides/dining-out-with-ibd.html",
            "/blog/dining-out-ibd-restaurants.html",
            "/blog/travel-with-ibd.html",
            "/blog/summer-travel-ibd-restrooms-meds-food-heat.html",
        ],
    },
    {
        "part": 8,
        "num": 45,
        "title": "Teens, Growth, and School",
        "intro": "Adolescents need calories for growth while managing symptoms and privacy at school.",
        "bridge": "Pregnancy planning adds folate, iron, and medication questions. Chapter 46 covers basics.",
        "sources": [
            "/blog/teen-nutrition-ibd-growth.html",
            "/blog/high-school-ibd-survival-guide.html",
        ],
    },
    {
        "part": 8,
        "num": 46,
        "title": "Pregnancy and Family Planning",
        "intro": "Nutrition and medication decisions should be coordinated with GI and OB teams early.",
        "bridge": "Holidays and religious fasting need individualized plans. Chapter 47 discusses cultural meals.",
        "rewrite": True,
        "sources": [],
    },
    {
        "part": 8,
        "num": 47,
        "title": "Ramadan, Holidays, and Cultural Meals",
        "intro": "Celebrations center on food. Plan portions, timing, and hydration with your team.",
        "bridge": "Ostomy and short bowel change rules again. Chapter 48 addresses post-surgery eating.",
        "sources": [
            "/blog/dates-ramadan-ibd.html",
            "/blog/icn-ibd-holidays-special-occasions.html",
        ],
    },
    {
        "part": 8,
        "num": 48,
        "title": "Ostomy, Short Bowel, and Post-Surgery Eating",
        "intro": "Output, hydration, and salt needs shift after surgery. Reintroduce foods in stages.",
        "bridge": "Tracking helps visits go better. Part IX opens with food, symptom logs.",
        "sources": [
            "/guides/living-with-ostomy-ibd.html",
            "/blog/j-pouch-basics-ibd.html",
        ],
    },
    {
        "part": 9,
        "num": 49,
        "title": "Food and Symptom Tracking That Helps Your GI",
        "intro": "Logs work when they are short, honest, and paired with labs, not guilt.",
        "bridge": "Chapter 50 aggregates clinic questions from across the book.",
        "sources": [
            "/guides/track-ibd-symptoms-food.html",
            "/blog/bristol-stool-chart-ibd.html",
        ],
    },
    {
        "part": 9,
        "num": 50,
        "title": "Questions for Your Dietitian and GI",
        "intro": "Bring structured questions to limited appointment time.",
        "bridge": "Chapter 51 helps you draft a personal plan from what you have learned.",
        "sources": ["/guides/crohns-doctor-visit-prep.html"],
    },
    {
        "part": 9,
        "num": 51,
        "title": "Building Your Personal Nutrition Plan",
        "intro": "Combine labs, triggers, cultural foods, and flare staples into one page you can update.",
        "bridge": "The conclusion reflects on long-term eating with IBD, not perfection, but progress.",
        "rewrite": True,
        "stub": True,
    },
]

NEW_CHAPTER_STUBS = {
    24: (
        "FODMAP reintroduction is a structured experiment, not a test you pass or fail. "
        "After a short elimination phase supervised by your dietitian, you add one FODMAP "
        "group at a time while noting gas, bloating, stool pattern, and pain over three to "
        "seven days per group.\n\n"
        "**Common reintroduction order (individualized):** fructans (onion, wheat), lactose "
        "(milk, yogurt), polyols (stone fruits, sugar alcohols), galacto-oligosaccharides "
        "(legumes), excess fructose (honey, apples). Your dietitian may change the order based "
        "on your symptom history.\n\n"
        "**During a flare:** pause reintroduction. Symptom noise from inflammation can mimic "
        "FODMAP intolerance. Resume when your gastroenterologist agrees inflammation is quieter.\n\n"
        "**During remission:** keep portions small on test days. If symptoms flare, stop that group "
        "and retry later. If symptoms stay calm, add the food to your tolerated list and continue. "
        "The goal is the widest safe diet, not the shortest elimination list.\n\n"
        "**When to ask your care team:** How long should my elimination phase last? Which groups "
        "fit my current inflammation level? Should we pause reintroduction during a flare? Do I "
        "have strictures that change fiber or texture advice?"
    ),
    39: (
        "These sample days illustrate flare-friendly combinations only. Portions, textures, and "
        "food choices must match your anatomy, strictures, ostomy output, and care team's guidance.\n\n"
        "**Sample flare day A**\n"
        "Breakfast: congee or white rice porridge with soft-cooked egg\n"
        "Mid-morning: ripe banana\n"
        "Lunch: plain chicken broth with soft noodles\n"
        "Afternoon: oral rehydration sips per clinician advice\n"
        "Dinner: baked salmon with peeled mashed potato\n\n"
        "**Sample flare day B**\n"
        "Breakfast: oatmeal cooked extra soft with lactose-free yogurt\n"
        "Mid-morning: applesauce (peeled, smooth)\n"
        "Lunch: turkey with white rice\n"
        "Afternoon: decaffeinated tea plus hydration goal\n"
        "Dinner: scrambled eggs with white toast\n\n"
        "**Sample flare day C (cultural staples)**\n"
        "Breakfast: soft idli or khichdi with mild dal (well cooked, small portion)\n"
        "Lunch: plain rice with soft-cooked chicken and broth\n"
        "Dinner: congee-style rice porridge with tofu or egg\n\n"
        "Track stool frequency, blood, pain, sleep, and meals in a notebook or app your team "
        "recommends. Adjust any sample day to foods you already tolerate."
    ),
    51: (
        "Complete this worksheet after reading the book. Update it after medication changes, "
        "surgery, or sustained symptom shifts.\n\n"
        "**My IBD nutrition snapshot**\n"
        "Current disease state (flare / uncertain / remission): _______________\n"
        "Disease location: _______________\n"
        "Relevant surgeries: _______________\n"
        "Known strictures: _______________\n"
        "Current symptoms: _______________\n"
        "Main nutrition concerns: _______________\n\n"
        "**My flare backup plan**\n"
        "Tolerated starches: _______________\n"
        "Tolerated proteins: _______________\n"
        "Tolerated fluids: _______________\n"
        "Tolerated snacks: _______________\n"
        "Foods I temporarily modify: _______________\n"
        "Signs I should contact my care team: _______________\n\n"
        "**Nutrition lab tracker (most recent)**\n"
        "Iron / ferritin (date, result, clinician note): _______________\n"
        "Vitamin B12 (date, result): _______________\n"
        "Vitamin D (date, result): _______________\n"
        "Other: _______________\n\n"
        "**Food reintroduction tracker**\n"
        "Food | Preparation | Portion | Symptoms | Timing | Try again?\n\n"
        "**Questions for my GI / dietitian**\n"
        "Am I at risk for iron deficiency? _______________\n"
        "Do I need B12 monitoring? _______________\n"
        "Should I modify fiber? _______________\n"
        "Are any of my restrictions unnecessary? _______________\n"
        "Should I see an IBD-focused dietitian? _______________\n\n"
        "**Three safe staple meals that worked last month:**\n"
        "1. _______________\n"
        "2. _______________\n"
        "3. _______________\n\n"
        "**Three foods under trial or reintroduction:**\n"
        "1. _______________\n"
        "2. _______________\n"
        "3. _______________\n\n"
        "**Hydration goal and warning signs I watch for:** _______________"
    ),
}
