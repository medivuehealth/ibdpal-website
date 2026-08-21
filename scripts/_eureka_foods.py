# --- 4) World staples Wave 5 (10) ---
FOODS = [
    dict(
        slug="chapati-roti-ibd", name="Chapati / roti",
        title="Chapati and Roti With IBD: Flatbread Tips for Flare and Remission",
        description="Chapati and roti with Crohn's or colitis: refined vs whole wheat, soft texture tips, oil notes, and dietitian questions. Education only.",
        category="Nutrition · September 2026", date_display="September 6, 2026", date_iso="2026-09-06T16:00:00Z",
        asset_dir="chapati-ibd", resource_category="nutrition",
        tags=["chapati", "roti", "flatbread", "wheat", "South Asian", "Crohn's", "colitis", "nutrition"],
        share="Chapati and roti with IBD: soft flatbread tips. Education only.",
        primary_kw="chapati Crohn's disease", secondary_kw="roti ulcerative colitis",
        nutrition_intro=(
            "Chapati and roti are everyday wheat flatbreads that deliver carbohydrate and some protein. "
            "Softer, well-cooked white or mixed flours often feel different from dense, dry whole-wheat stack breads during flares."
        ),
        macros=[
            ("Serving", "1 medium chapati (~40 g)"),
            ("Calories", "~120"),
            ("Carbohydrate", "~18 to 20 g"),
            ("Fiber", "~1 to 3 g (higher with whole wheat)"),
            ("Protein", "~3 to 4 g"),
            ("Fat", "~2 to 4 g depending on oil or ghee"),
        ],
        micros=[
            ("B vitamins and iron", "Higher when flour is enriched or atta is fortified"),
            ("Sodium", "Usually low unless salted dough or store brands add more"),
            ("Added fat", "Brush of oil or ghee changes calories quickly"),
        ],
        tolerance_intro=(
            "Many people tolerate soft, fresh chapati better than fried puri or bread with seeds. "
            "During strict low-residue phases, some teams prefer refined grains temporarily; reintroduction is individualized."
        ),
        flare_tips=[
            "Choose soft, freshly cooked roti without dry edges if chewing feels hard",
            "Prefer refined or finely milled flour if bran irritates you right now",
            "Limit heavy ghee or oily smears if fat worsens urgency",
            "Skip stuffed parathas with raw vegetable fillings during severe flares",
        ],
        remission_tips=[
            "Trial whole-wheat or multigrain atta in small portions if fiber goals allow",
            "Pair with dal, yogurt, or soft vegetables you already tolerate",
            "Watch restaurant breads that add butter or garlic butter",
        ],
        prep=(
            "Roll thin, cook evenly on a tawa until soft, and keep covered so they do not dry out. "
            "Leftover dry roti can be warmed with a little moisture or turned into soft crumbs in soups if that sits better."
        ),
        myths=[
            ("Wheat flatbread is banned in all Crohn's diets.", "Many patients use soft chapati; tolerance is individual."),
            ("Only gluten-free wraps are safe for UC.", "Gluten-free is required for celiac disease, not automatically for IBD."),
            ("Chapati causes flares by itself.", "Portion, fat, spice sides, and disease activity all matter."),
        ],
        questions=[
            "Should I use refined or whole-wheat flour on my current plan?",
            "How many rotis fit my calorie and fiber targets?",
            "Any stricture-related texture limits for denser breads?",
        ],
        related=[
            ("/blog/white-rice-ibd-flare", "white rice"),
            ("/blog/fiber-and-ibd-diet", "fiber and IBD"),
            ("/blog/white-bread-ibd", "white bread"),
        ],
    ),
    dict(
        slug="dal-lentils-ibd", name="Dal (lentils)",
        title="Dal and Lentils With IBD: Protein, FODMAPs, and Softer Prep",
        description="Dal and lentils with Crohn's or colitis: protein benefits, gas and FODMAP notes, blended soups, and clinic questions. Education only.",
        category="Nutrition · September 2026", date_display="September 6, 2026", date_iso="2026-09-06T17:00:00Z",
        asset_dir="dal-ibd", resource_category="nutrition",
        tags=["dal", "lentils", "legumes", "protein", "FODMAP", "South Asian", "Crohn's", "colitis", "nutrition"],
        share="Dal and lentils with IBD: soft prep and FODMAP tips. Education only.",
        primary_kw="dal Crohn's disease", secondary_kw="lentils ulcerative colitis",
        nutrition_intro=(
            "Dal is a staple lentil or pulse dish that provides plant protein, carbohydrate, fiber, and iron. "
            "Well-cooked, blended, or skinned preparations behave differently in the gut than al dente beans with skins."
        ),
        macros=[
            ("Serving", "1 cup cooked plain dal (~200 g)"),
            ("Calories", "~230"),
            ("Carbohydrate", "~40 g"),
            ("Fiber", "~15 g (varies by lentil type and skimming)"),
            ("Protein", "~18 g"),
            ("Fat", "~1 g before tadka oil"),
        ],
        micros=[
            ("Iron and folate", "Useful plant sources; absorption improves with vitamin C foods if tolerated"),
            ("Potassium", "Helpful for many eating patterns; watch if your clinician limits potassium"),
            ("FODMAP oligosaccharides", "Can drive gas when portions are large"),
        ],
        tolerance_intro=(
            "Lentils are often limited on strict low-residue or elimination FODMAP phases, then reintroduced in measured scoops. "
            "Moong dal and thoroughly blended khichdi-style meals are common gentler starting points for some people."
        ),
        flare_tips=[
            "Pause large bean portions if bloating and urgency spike",
            "If allowed, try small amounts of well-cooked, blended moong without heavy chili tadka",
            "Skim foam and cook until lentils fully break down",
            "Avoid whole chickpeas or firm kidney beans during severe flares or known strictures unless cleared",
        ],
        remission_tips=[
            "Reintroduce with a dietitian using measured portions",
            "Combine with rice for a softer mixed meal",
            "Limit fried tempering oils and raw onion-garlic loads if those trigger you",
        ],
        prep=(
            "Pressure-cook until creamy, then thin with water for a soup texture. "
            "Build flavor with cumin and turmeric if tolerated; hold large onion-garlic tempering when FODMAPs are limited."
        ),
        myths=[
            ("All lentils are impossible with IBD.", "Form, portion, and disease phase change tolerance."),
            ("Dal protein cannot help underweight patients.", "It can contribute when tolerated and paired with calories."),
            ("Spicy tadka is required for nutrition.", "Spice level is optional; protein is in the lentils."),
        ],
        questions=[
            "Which lentil types and portions fit my FODMAP or residue plan?",
            "Is blended dal okay while whole beans are restricted?",
            "How do we use dal toward iron and protein goals?",
        ],
        related=[
            ("/blog/fodmap-diet-crohns-colitis", "FODMAP overview"),
            ("/blog/onion-garlic-ibd-fodmap", "onion and garlic"),
            ("/blog/fiber-and-ibd-diet", "fiber and IBD"),
        ],
    ),
    dict(
        slug="congee-rice-porridge-ibd", name="Congee (rice porridge)",
        title="Congee and Rice Porridge With IBD: Soft Carbs for Flare Days",
        description="Congee with Crohn's or colitis: hydration, easy carbs, topping choices, and dietitian questions. Education only.",
        category="Nutrition · September 2026", date_display="September 6, 2026", date_iso="2026-09-06T18:00:00Z",
        asset_dir="congee-ibd", resource_category="nutrition",
        tags=["congee", "rice porridge", "juk", "soft foods", "East Asian", "Crohn's", "colitis", "nutrition"],
        share="Congee and IBD: soft rice porridge tips. Education only.",
        primary_kw="congee Crohn's", secondary_kw="rice porridge ulcerative colitis",
        nutrition_intro=(
            "Congee is rice cooked with ample water into a spoonable porridge. "
            "It is mostly carbohydrate and fluid, so protein toppings matter if you need more nutrition density."
        ),
        macros=[
            ("Serving", "1 to 1.5 cups plain congee"),
            ("Calories", "~150 to 220 depending on thickness"),
            ("Carbohydrate", "~30 to 45 g"),
            ("Fiber", "low when made with white rice"),
            ("Protein", "~3 to 5 g before toppings"),
            ("Fat", "low unless oil or egg is added"),
        ],
        micros=[
            ("Sodium", "Rises quickly with commercial broths and pickles"),
            ("Selenium and small B vitamins", "From rice; not a complete micronutrient meal alone"),
            ("Electrolytes", "Come more from broth bases and add-ins than from rice itself"),
        ],
        tolerance_intro=(
            "Smooth white-rice congee is a frequent comfort texture during flares when your team wants low residue. "
            "Brown rice, barley mixes, and crunchy toppings change the fiber and mechanical load."
        ),
        flare_tips=[
            "Use white rice cooked very soft with extra water",
            "Skip fried dough sticks, chili oil, and pickled vegetables if they trigger you",
            "Add egg ribbon, soft tofu, or shredded chicken if protein is approved",
            "Watch salty restaurant broth bases if you are dehydrated or retaining fluid",
        ],
        remission_tips=[
            "Thicken gradually and add tolerated vegetables in small soft pieces",
            "Trial brown rice congee only when fiber is welcome",
            "Use as a gentle meal when appetite is low even outside flares",
        ],
        prep=(
            "Simmer rice with a high water ratio, stirring until grains break down. "
            "Season lightly; keep toppings soft and simple while symptoms are active."
        ),
        myths=[
            ("Congee heals ulcers by itself.", "It supports intake; it is not anti-inflammatory drug therapy."),
            ("Only rice water is allowed forever.", "Most people re-expand foods as inflammation improves."),
            ("Brown rice congee is always better.", "Higher fiber is not automatically better during flares."),
        ],
        questions=[
            "Is white-rice congee appropriate on my current flare plan?",
            "Which protein add-ins should I use?",
            "How do we transition back to steamed rice and mixed meals?",
        ],
        related=[
            ("/blog/white-rice-ibd-flare", "white rice"),
            ("/blog/electrolytes-flare-ibd", "electrolytes"),
            ("/blog/tofu-soy-ibd", "tofu"),
        ],
    ),
    dict(
        slug="miso-soup-ibd", name="Miso soup",
        title="Miso Soup With IBD: Probiotics, Sodium, and Gentle Meals",
        description="Miso soup with Crohn's or colitis: fermented soybean paste, sodium, FODMAP notes, and clinic questions. Education only.",
        category="Nutrition · September 2026", date_display="September 6, 2026", date_iso="2026-09-06T19:00:00Z",
        asset_dir="miso-ibd", resource_category="nutrition",
        tags=["miso", "miso soup", "fermented", "sodium", "Japanese", "Crohn's", "colitis", "nutrition"],
        share="Miso soup and IBD: sodium and gentle sip tips. Education only.",
        primary_kw="miso soup Crohn's", secondary_kw="miso ulcerative colitis",
        nutrition_intro=(
            "Miso soup combines fermented soybean paste with dashi stock and soft add-ins like tofu or wakame. "
            "It is savory and hydrating for some people, but sodium and seaweed fiber deserve attention."
        ),
        macros=[
            ("Serving", "1 bowl (~240 ml)"),
            ("Calories", "~40 to 80 depending on miso amount and tofu"),
            ("Carbohydrate", "~4 to 8 g"),
            ("Protein", "~3 to 6 g with tofu"),
            ("Fat", "~1 to 3 g"),
            ("Sodium", "often 600 to 900+ mg per bowl"),
        ],
        micros=[
            ("Fermentation cultures", "Present in unpasteurized miso; soup heat reduces live counts"),
            ("Iodine", "Can rise with seaweed add-ins"),
            ("Isoflavones", "From soybean paste in modest amounts"),
        ],
        tolerance_intro=(
            "Clear, mild miso with soft tofu is usually easier than loaded restaurant bowls with corn, mushrooms, and scallions. "
            "People on low-FODMAP trials may limit certain miso types or portions; confirm with a dietitian."
        ),
        flare_tips=[
            "Sip a small bowl of mild miso if salty fluids sit well",
            "Choose soft tofu over crunchy vegetables",
            "Skip heavy seaweed salads on the side if residue is restricted",
            "Compare sodium if you have blood pressure or fluid concerns",
        ],
        remission_tips=[
            "Use as a light starter with rice and fish or eggs",
            "Trial different miso colors in small amounts",
            "Watch onion-garlic heavy broth bases in some recipes",
        ],
        prep=(
            "Dissolve miso off the boil to preserve flavor; boiling hard is unnecessary for safety once stock is hot. "
            "Keep add-ins soft and minimal while symptoms are loud."
        ),
        myths=[
            ("Miso probiotics cure IBD.", "Helpful comfort food for some; not a biologic replacement."),
            ("All fermented foods are mandatory for gut health.", "Tolerance and immunosuppression context matter."),
            ("Homemade miso soup is always low sodium.", "Paste amount drives salt more than the pot size."),
        ],
        questions=[
            "Is miso sodium acceptable with my medical history?",
            "Which fermented foods fit my current plan?",
            "Can I use miso as a fluid option during poor appetite?",
        ],
        related=[
            ("/blog/tofu-soy-ibd", "tofu and soy"),
            ("/blog/onion-garlic-ibd-fodmap", "onion and garlic"),
            ("/blog/greek-yogurt-ibd", "yogurt"),
        ],
    ),
    dict(
        slug="kimchi-fermented-ibd", name="Kimchi",
        title="Kimchi and Fermented Vegetables With IBD: Spice, Fiber, and Caution",
        description="Kimchi with Crohn's or colitis: fermentation claims, chili heat, FODMAP cabbage, and dietitian questions. Education only.",
        category="Nutrition · September 2026", date_display="September 7, 2026", date_iso="2026-09-07T12:00:00Z",
        asset_dir="kimchi-ibd", resource_category="nutrition",
        tags=["kimchi", "fermented", "cabbage", "spicy", "Korean", "Crohn's", "colitis", "nutrition"],
        share="Kimchi and IBD: fermentation, spice, and caution. Education only.",
        primary_kw="kimchi Crohn's disease", secondary_kw="kimchi ulcerative colitis",
        nutrition_intro=(
            "Kimchi is fermented napa cabbage (or other vegetables) with chili, garlic, ginger, and salt. "
            "It offers flavor, some fiber, and live cultures in unpasteurized jars, plus heat that can bother an inflamed gut."
        ),
        macros=[
            ("Serving", "1/4 to 1/2 cup"),
            ("Calories", "~20 to 40"),
            ("Carbohydrate", "~4 to 8 g"),
            ("Fiber", "~1 to 2 g"),
            ("Protein", "~1 to 2 g"),
            ("Sodium", "often high per small serving"),
        ],
        micros=[
            ("Vitamin C and K", "Present in cabbage-based kimchi"),
            ("Live cultures", "In refrigerated, unpasteurized products"),
            ("Capsaicin from chili", "Can increase urgency or pain for some people"),
        ],
        tolerance_intro=(
            "Spicy, high-fiber, garlic-forward kimchi is a common flare trigger even when fermentation is marketed as gut healthy. "
            "Mild, finely chopped, small tastes in remission are a different experiment than large banchan portions during active disease."
        ),
        flare_tips=[
            "Pause kimchi if chili and raw-fermented crunch worsen pain or bleeding",
            "Do not use spicy kimchi as a forced probiotic during severe colitis flares",
            "Watch sodium if stools are already watery",
            "Choose bland soft sides instead while inflammation is high",
        ],
        remission_tips=[
            "Trial a teaspoon of milder kimchi with rice if your team agrees",
            "Note garlic and onion intensity across brands",
            "Rinse or choose lower-chili styles if heat is the main issue",
        ],
        prep=(
            "Store refrigerated and use clean utensils. "
            "Serve tiny portions beside plain rice rather than as a large side when testing tolerance."
        ),
        myths=[
            ("Kimchi heals the microbiome so IBD disappears.", "Fermented foods are not disease-modifying therapy."),
            ("All patients should eat spicy ferments daily.", "Spice and FODMAPs often limit tolerance."),
            ("Pasteurized kimchi is useless.", "It may still be a vegetable side; live cultures are only one feature."),
        ],
        questions=[
            "Should I avoid chili ferments while my colon is inflamed?",
            "How do garlic-heavy kimchi brands fit a FODMAP trial?",
            "What milder fermented options are reasonable for me?",
        ],
        related=[
            ("/blog/fodmap-diet-crohns-colitis", "FODMAP overview"),
            ("/blog/onion-garlic-ibd-fodmap", "onion and garlic"),
            ("/blog/greek-yogurt-ibd", "yogurt"),
        ],
    ),
    dict(
        slug="plantain-ibd", name="Plantain",
        title="Plantain With IBD: Green Versus Ripe, Boiled Versus Fried",
        description="Plantain with Crohn's or colitis: starch when green, sweeter when ripe, frying fat notes, and clinic questions. Education only.",
        category="Nutrition · September 2026", date_display="September 7, 2026", date_iso="2026-09-07T13:00:00Z",
        asset_dir="plantain-ibd", resource_category="nutrition",
        tags=["plantain", "platano", "starch", "Caribbean", "Latin American", "Crohn's", "colitis", "nutrition"],
        share="Plantain and IBD: boiled soft starch tips. Education only.",
        primary_kw="plantain Crohn's", secondary_kw="plantain ulcerative colitis diet",
        nutrition_intro=(
            "Plantains are starchy banana relatives used across Latin American, Caribbean, and West African kitchens. "
            "Green plantains are more starch-forward; ripe yellow-black plantains are sweeter and softer when cooked."
        ),
        macros=[
            ("Serving", "1 medium plantain cooked (~150 to 180 g edible)"),
            ("Calories", "~200 boiled; much higher when fried"),
            ("Carbohydrate", "~50 g"),
            ("Fiber", "~3 to 4 g"),
            ("Protein", "~2 g"),
            ("Fat", "low boiled; high as tostones or maduros fritos"),
        ],
        micros=[
            ("Potassium and vitamin A precursors", "Higher as plantains ripen"),
            ("Vitamin C", "Present, reduced with long cooking"),
            ("Resistant starch", "More notable in green, cooled preparations for some nutrition contexts"),
        ],
        tolerance_intro=(
            "Soft boiled or mashed ripe plantain is often gentler than twice-fried tostones. "
            "Green firm pieces and heavy frying oil can feel harder during flares or with fat-triggered urgency."
        ),
        flare_tips=[
            "Prefer boiled or steamed ripe plantain mashed smooth",
            "Limit deep-fried chips and tostones if oil worsens symptoms",
            "Start with a small portion beside protein",
            "Avoid raw green plantain",
        ],
        remission_tips=[
            "Use plantain as a cultural starch swap for potato or rice",
            "Trial lightly pan-cooked ripe slices if fried food usually sits well in small amounts",
            "Watch sweet maduros portions if loose stools follow large sugar loads",
        ],
        prep=(
            "Peel, slice, and boil until fork-tender, then mash with a little salt. "
            "Bake instead of deep-fry when you want crisp edges with less oil."
        ),
        myths=[
            ("Plantain is the same as dessert banana for every gut.", "Starch and ripeness differ; test your own tolerance."),
            ("Fried plantain is required for nutrition.", "Boiled plantain still provides carbohydrate."),
            ("Green plantain fiber always calms IBD.", "Texture and fat matter as much as the fruit label."),
        ],
        questions=[
            "Is boiled plantain appropriate on my low-residue plan?",
            "How do fried foods fit my current symptoms?",
            "Can plantain help me hit calorie goals when appetite is low?",
        ],
        related=[
            ("/blog/banana-ibd-crohns-colitis", "bananas"),
            ("/blog/white-rice-ibd-flare", "white rice"),
            ("/blog/sweet-potato-ibd", "sweet potato"),
        ],
    ),
    dict(
        slug="tortillas-ibd", name="Tortillas",
        title="Tortillas With IBD: Corn Versus Flour, Soft Wraps, and Flare Tips",
        description="Corn and flour tortillas with Crohn's or colitis: residue, fat from frying, store additives, and dietitian questions. Education only.",
        category="Nutrition · September 2026", date_display="September 7, 2026", date_iso="2026-09-07T14:00:00Z",
        asset_dir="tortilla-ibd", resource_category="nutrition",
        tags=["tortillas", "corn tortilla", "flour tortilla", "Mexican", "wraps", "Crohn's", "colitis", "nutrition"],
        share="Tortillas and IBD: soft corn or flour tips. Education only.",
        primary_kw="tortillas Crohn's", secondary_kw="corn tortilla ulcerative colitis",
        nutrition_intro=(
            "Tortillas are thin corn or wheat wraps that carry fillings with relatively little bulk when soft. "
            "Corn masa tortillas are typically smaller and naturally gluten-free; flour tortillas are softer for some people but higher in fat when shortening is used."
        ),
        macros=[
            ("Serving", "1 small corn tortilla (~25 g) or 1 medium flour tortilla (~45 g)"),
            ("Calories", "~50 to 60 corn; ~130 to 150 flour"),
            ("Carbohydrate", "~10 to 12 g corn; ~20 to 25 g flour"),
            ("Fiber", "~1 to 2 g"),
            ("Protein", "~1 to 4 g"),
            ("Fat", "low for plain corn; higher for many flour brands"),
        ],
        micros=[
            ("Niacin from nixtamalized corn", "Traditional processing improves corn nutrition"),
            ("Sodium", "Varies by brand; check labels"),
            ("Additives", "Some wraps include gums or fibers that affect tolerance"),
        ],
        tolerance_intro=(
            "Soft, warm tortillas often beat crunchy fried taco shells during flares. "
            "Whole corn bits, wheat bran wraps, and heavy fried chimichangas change the mechanical and fat load."
        ),
        flare_tips=[
            "Choose soft corn or plain flour tortillas warmed, not fried crisp",
            "Keep fillings simple: egg, chicken, smooth refried beans only if already tolerated",
            "Limit chips and hard shells if residue or oil is a problem",
            "Read labels for inulin or polyols in low-carb wraps",
        ],
        remission_tips=[
            "Build balanced tacos with tolerated proteins and soft vegetables",
            "Trial whole-wheat tortillas if fiber goals allow",
            "Watch creamy sauces and raw onion toppings separately from the tortilla itself",
        ],
        prep=(
            "Warm on a dry skillet until pliable so they do not crack. "
            "For softer texture, briefly wrap in a damp cloth after heating."
        ),
        myths=[
            ("Corn tortillas are always high residue.", "Soft thin corn wraps are different from popcorn or corn kernels."),
            ("Flour tortillas are unhealthy for every IBD patient.", "Fat and portion matter; many people use them."),
            ("Hard shells are the same as soft tortillas.", "Frying changes fat and crunch substantially."),
        ],
        questions=[
            "Are soft corn or flour tortillas better on my current plan?",
            "Should I avoid fried shells with known strictures?",
            "Any brand additives I should skip?",
        ],
        related=[
            ("/blog/corn-ibd", "corn"),
            ("/blog/white-rice-ibd-flare", "white rice"),
            ("/blog/onion-garlic-ibd-fodmap", "onion and garlic"),
        ],
    ),
    dict(
        slug="couscous-ibd", name="Couscous",
        title="Couscous With IBD: Small Pasta Texture, Portions, and Prep",
        description="Couscous with Crohn's or colitis: refined wheat granules, soft texture tips, fiber add-ins, and clinic questions. Education only.",
        category="Nutrition · September 2026", date_display="September 7, 2026", date_iso="2026-09-07T15:00:00Z",
        asset_dir="couscous-ibd", resource_category="nutrition",
        tags=["couscous", "semolina", "North African", "wheat", "starch", "Crohn's", "colitis", "nutrition"],
        share="Couscous and IBD: soft starch portion tips. Education only.",
        primary_kw="couscous Crohn's", secondary_kw="couscous ulcerative colitis",
        nutrition_intro=(
            "Couscous is tiny steamed semolina granules, essentially a quick wheat pasta. "
            "Plain refined couscous is mostly carbohydrate with modest protein; whole-wheat versions raise fiber."
        ),
        macros=[
            ("Serving", "1 cup cooked (~160 g)"),
            ("Calories", "~170"),
            ("Carbohydrate", "~35 g"),
            ("Fiber", "~2 g refined; higher if whole wheat"),
            ("Protein", "~6 g"),
            ("Fat", "~0.5 g before oil"),
        ],
        micros=[
            ("Selenium and B vitamins", "Present in wheat products, higher if enriched"),
            ("Iron", "Modest unless fortified"),
            ("Sodium", "Low plain; rises with salty broths"),
        ],
        tolerance_intro=(
            "Fluffy refined couscous without chunky vegetable confetti is often easier during recovery than couscous salads packed with raw peppers and dried fruit. "
            "Pearl (Israeli) couscous is larger and chewier."
        ),
        flare_tips=[
            "Use fine refined couscous cooked soft with water or mild broth",
            "Skip large pearl couscous if chewing or residue is a concern",
            "Hold raw vegetable mix-ins and nuts",
            "Limit oily dressings if fat worsens urgency",
        ],
        remission_tips=[
            "Add soft cooked vegetables and lean protein",
            "Trial whole-wheat couscous in small servings",
            "Use as a travel-friendly starch when rice is unavailable",
        ],
        prep=(
            "Pour boiling water over couscous, cover, then fluff with a fork. "
            "Aim for tender separate grains rather than a dry, crunchy underhydrated bowl."
        ),
        myths=[
            ("Couscous is a whole grain automatically.", "Many packages are refined semolina."),
            ("Pasta-like foods are banned in IBD.", "Soft refined starches are commonly used in flare frameworks."),
            ("Larger pearl couscous is always gentler.", "Chewier pearls can be harder for some guts."),
        ],
        questions=[
            "Is refined couscous appropriate while I am on a low-residue plan?",
            "How does couscous compare with rice for my symptoms?",
            "When can I add vegetables back into couscous bowls?",
        ],
        related=[
            ("/blog/white-rice-ibd-flare", "white rice"),
            ("/blog/fiber-and-ibd-diet", "fiber and IBD"),
            ("/blog/white-bread-ibd", "white bread"),
        ],
    ),
    dict(
        slug="dates-ramadan-ibd", name="Dates",
        title="Dates and Ramadan Eating With IBD: Sugar, Fiber, and Fasting Notes",
        description="Dates with Crohn's or colitis: Ramadan iftar tips, fiber and sugar load, portion size, and clinic questions. Education only.",
        category="Nutrition · September 2026", date_display="September 7, 2026", date_iso="2026-09-07T16:00:00Z",
        asset_dir="dates-ibd", resource_category="nutrition",
        tags=["dates", "Ramadan", "iftar", "fruit", "fiber", "fasting", "Crohn's", "colitis", "nutrition"],
        share="Dates and IBD: Ramadan portions and flare tips. Education only.",
        primary_kw="dates Crohn's Ramadan", secondary_kw="dates ulcerative colitis",
        nutrition_intro=(
            "Dates are sweet dried fruits traditionally eaten to break the fast in Ramadan and as everyday snacks. "
            "They provide quick carbohydrate, fiber, potassium, and concentrated sugar in a small piece."
        ),
        macros=[
            ("Serving", "2 to 3 medium dates (~40 to 50 g)"),
            ("Calories", "~110 to 140"),
            ("Carbohydrate", "~30 g"),
            ("Fiber", "~3 g"),
            ("Protein", "~1 g"),
            ("Fat", "negligible"),
        ],
        micros=[
            ("Potassium and magnesium", "Notable for fruit servings"),
            ("Copper and manganese", "Small contributions"),
            ("Natural sugars", "Glucose and fructose concentrated by drying"),
        ],
        tolerance_intro=(
            "Soft, pitted dates in small numbers are different from large stuffed dates with nuts during a flare. "
            "Fasting and IBD need individualized medical advice; do not assume religious fasting is safe in active disease without clinician input."
        ),
        flare_tips=[
            "If eating dates, start with one soft date and notice stool changes",
            "Avoid nut-stuffed or fried date desserts when fat and fiber are limited",
            "Pair with protein and salt-containing foods at iftar if your team supports fasting",
            "Prioritize hydration when fasting is medically cleared",
        ],
        remission_tips=[
            "Use 1 to 3 dates as a planned sweet instead of large candy portions",
            "Combine with yogurt if dairy is tolerated",
            "Mind total FODMAP load if you are in an elimination phase",
        ],
        prep=(
            "Choose soft dates, remove pits, and chop finely into porridge or yogurt if whole sticky pieces bother you. "
            "For Ramadan meal planning, discuss medication timing and hydration with your care team early."
        ),
        myths=[
            ("Dates detox the gut at iftar.", "They are a carbohydrate source, not a medical detox."),
            ("Everyone with IBD must skip Ramadan fasting.", "Decisions are individualized with clinicians; this page cannot approve fasting."),
            ("Sugar from dates never affects diarrhea.", "Large sweet loads can loosen stools for some people."),
        ],
        questions=[
            "Is fasting medically appropriate for me this year?",
            "How should I time medicines around suhoor and iftar?",
            "What portion of dates fits my flare or remission plan?",
        ],
        related=[
            ("/blog/intermittent-fasting-ibd", "intermittent fasting education"),
            ("/blog/fodmap-diet-crohns-colitis", "FODMAP overview"),
            ("/blog/greek-yogurt-ibd", "yogurt"),
        ],
    ),
    dict(
        slug="paneer-ibd", name="Paneer",
        title="Paneer With IBD: Soft Cheese Protein, Lactose, and Cooking Tips",
        description="Paneer with Crohn's or colitis: protein density, lactose notes, soft cubes vs fried, and dietitian questions. Education only.",
        category="Nutrition · September 2026", date_display="September 7, 2026", date_iso="2026-09-07T17:00:00Z",
        asset_dir="paneer-ibd", resource_category="nutrition",
        tags=["paneer", "Indian cheese", "protein", "lactose", "dairy", "Crohn's", "colitis", "nutrition"],
        share="Paneer and IBD: soft cheese protein tips. Education only.",
        primary_kw="paneer Crohn's", secondary_kw="paneer ulcerative colitis",
        nutrition_intro=(
            "Paneer is a fresh pressed dairy cheese used in many South Asian meals. "
            "It offers concentrated protein and fat with a soft cube texture when not deep-fried."
        ),
        macros=[
            ("Serving", "100 g plain paneer"),
            ("Calories", "~260 to 300 depending on milk fat"),
            ("Protein", "~18 to 20 g"),
            ("Fat", "~20 to 25 g"),
            ("Carbohydrate", "~1 to 4 g"),
            ("Lactose", "often lower than milk but not zero for everyone"),
        ],
        micros=[
            ("Calcium", "Useful dairy contribution when tolerated"),
            ("Vitamin B12 and riboflavin", "Present in dairy paneer"),
            ("Sodium", "Usually modest in plain homemade styles; higher in some packaged products"),
        ],
        tolerance_intro=(
            "Soft, gently cooked paneer cubes in mild gravy are different from crispy fried paneer pakora. "
            "Lactose sensitivity and high-fat gravies are separate issues from the cheese itself."
        ),
        flare_tips=[
            "Try small amounts of soft paneer if dairy protein is allowed",
            "Avoid deep-fried pakoras and very spicy masalas during severe flares",
            "Choose milder gravies without heavy cream if fat worsens urgency",
            "Consider lactose-free dairy alternatives if milk usually triggers you",
        ],
        remission_tips=[
            "Use paneer to hit protein targets with roti or rice",
            "Grill or lightly pan-sear instead of deep-frying",
            "Pair with tolerated vegetables once residue limits ease",
        ],
        prep=(
            "Simmer cubes briefly in a mild tomato or yogurt-based sauce if those ingredients sit well, or eat warm plain cubes with soft starch. "
            "Do not over-fry until rubbery hard crusts form if texture is an issue."
        ),
        myths=[
            ("All dairy cheeses flare Crohn's.", "Many patients tolerate paneer or yogurt; test individually."),
            ("Paneer is probiotic like yogurt.", "It is primarily a protein food, not a live-culture yogurt equivalent."),
            ("Fried paneer is required for calories.", "Soft cooked paneer still provides substantial energy and protein."),
        ],
        questions=[
            "How does paneer fit my lactose tolerance?",
            "What portion helps my protein goals without excess fat symptoms?",
            "Should I prefer homemade paneer for sodium control?",
        ],
        related=[
            ("/blog/greek-yogurt-ibd", "Greek yogurt"),
            ("/blog/calcium-ibd", "calcium"),
            ("/blog/protein-shakes-ons-ibd", "protein and ONS"),
        ],
    ),
]


def build_food_posts():
    out = []
    for f in FOODS:
        meta = {k: f[k] for k in ("slug", "title", "description", "category", "date_display", "date_iso", "asset_dir", "resource_category", "tags")}
        meta["share"] = f.get("share") or f["description"][:110]
        meta["name"] = f["name"]
        out.append(post(meta, food_body(f)))
    return out
