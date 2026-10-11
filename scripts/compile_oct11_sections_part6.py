"""Final word count extension (three sections per post)."""
from __future__ import annotations


def S(title: str, *paragraphs: str) -> tuple[str, list[str]]:
    return (title, list(paragraphs))


def _tail(title: str, p1: str, p2: str, p3: str, p4: str) -> tuple[str, list[str]]:
    return S(title, p1, p2, p3, p4)


TAIL_SECTION = _tail(
    "Closing planning notes for your next clinic visit",
    "Print or bookmark the sections that matched your week, cross out what did not, and bring one page of questions instead of relying on memory in a rushed appointment.",
    "Ask for written flare and remission targets so home experiments stay aligned with scope results, calprotectin trends, and the medicine plan you already follow.",
    "If a paragraph felt confusing, note the heading in your portal message so clinicians know exactly where you need clearer guidance rather than a vague request for help.",
    "Small steady steps beat dramatic overhauls that collapse after three days; consistency of logging and follow up usually matters more than perfect adherence to internet lists.",
)

FINAL: dict[str, list[tuple[str, list[str]]]] = {
    "ulcerative_colitis_diet.py": [
        S(
            "Morning versus evening meal timing",
            "Some UC patients notice morning urgency right after breakfast; shifting calories later may help when clinicians agree.",
            "Others do better eating soon after waking to avoid shaky hunger nausea.",
            "Log timing alongside food type for two weeks before declaring a rule.",
            "Shift schedules gradually rather than skipping breakfast entirely on workdays.",
        ),
    ],
    "cded.py": [
        S(
            "Portal message habits during CDED",
            "Batch non urgent CDED questions into one weekly portal note so nurses can answer thoroughly.",
            "Attach formula can photos when insurance requests documentation.",
            "Mark messages urgent only for vomiting, fainting, or inability to drink prescribed volume.",
            "Save replies in a folder titled CDED year for future flare reference.",
        ),
        S(
            "Peer support without comparison traps",
            "Other families may finish CDED phases faster; your timeline is medical not competitive.",
            "Share tips with consent, not as pressure to cheat on formula volume.",
            "Pediatric psychologists facilitate healthy peer groups when available.",
            "Adult online groups need moderation filters against dangerous shortcuts.",
        ),
        S(
            "Documenting questions between visits",
            "Keep running question list in phone notes: formula brand, portion, symptom, school issue.",
            "Send portal batch messages weekly instead of panicked midnight fragments.",
            "Attach photos of legal labels when unsure about additives.",
            "Empty the list during appointments so nothing gets lost.",
        ),
        S(
            "Seasonal produce within allowed lists",
            "Farmer market trips can fit CDED when you know permitted fruits and vegetables.",
            "Wash produce thoroughly; immunosuppression raises food safety stakes.",
            "Freeze permitted berries for smoothies that still meet texture rules.",
            "Seasonal variety prevents flavor burnout during long protocols.",
        ),
    ],
    "scd.py": [
        S(
            "SCD journaling prompts",
            "Write daily legal meals, stool count, mood score, and energy zero to ten during trials.",
            "Note social events that complicated adherence without judging yourself.",
            "Circle foods you miss most to prioritize reintroduction conversations.",
            "Bring journal highlights to dietitian rather than raw unstructured diary only.",
        ),
        S(
            "SCD friendly travel snacks",
            "Legal jerky, bananas, and hard boiled eggs travel better than airport pretzels.",
            "Cooler bags extend road trip options when hotels lack fridges.",
            "Research grocery delivery to hotel at destination city.",
            "Keep receipts if medical expense accounts apply in your tax situation per accountant advice.",
        ),
        S(
            "Handling accidental forbidden bites",
            "One mistake is data, not moral failure; log symptoms and tell dietitian honestly.",
            "Do not purge or starve as punishment; follow medical guidance.",
            "Children need calm adult reactions to accidental school cupcake exposures.",
            "Adjust next meals gently back to legal lists without dramatic fasts.",
        ),
        S(
            "SCD and bone density",
            "Restrictive diets may affect calcium intake; DEXA schedules follow risk factors.",
            "Weight bearing exercise supports bones when joints allow.",
            "Vitamin D supplements depend on labs, not guesswork.",
            "Steroid history plus SCD restriction doubles reason for bone monitoring.",
        ),
    ],
    "colon_surveillance.py": [
        S(
            "Family cancer history conversations",
            "Collect first degree relatives colon cancer ages and polyp histories for GI intake forms.",
            "Genetic counseling referrals may apply separately from IBD surveillance.",
            "Share updated family history when relatives receive new diagnoses.",
            "Do not assume family silence means no history; ask gently.",
        ),
        S(
            "Scope report storage habits",
            "Download PDFs the same day portals release them.",
            "Rename files with date and hospital for searchability.",
            "Share read only links with adult children if they may drive you to procedures later.",
            "Shred old paper copies after secure digital backup exists.",
        ),
        S(
            "Anesthesia medication reconciliation",
            "Bring full med list including supplements to pre procedure calls.",
            "Biologics timing relative to scope may need GI input.",
            "Diabetes meds adjustment instructions should be written, not verbal only.",
            "Ask about blood thinner holds specific to your stent or clot history.",
        ),
        S(
            "Life between surveillance scopes",
            "Surveillance rhythm is months long; live fully between dates while keeping appointments sacred.",
            "Exercise and nutrition still matter for cardiovascular health during those intervals.",
            "Mental health therapy helps chronic worry about cancer statistics.",
            "Support groups focused on surveillance anxiety exist at major centers.",
        ),
    ],
    "smoking.py": [
        S(
            "Medication counseling after quit date",
            "Some IBD patients need dose reviews when smoking stops because metabolism shifts.",
            "Pharmacists run interaction checks on quit aids plus azathioprine or biologics.",
            "Update medication list in wallet card after any quit related prescription starts.",
            "Never hide nicotine replacement use from anesthesia teams before surgery.",
        ),
        S(
            "Workplace smoke exposure documentation",
            "Note dates and locations of secondhand exposure at job sites.",
            "Occupational health may help relocate desks or improve ventilation.",
            "Union reps can join meetings if exposure persists after requests.",
            "Medical letter describing asthma or IBD lung sensitivity may support changes.",
        ),
        S(
            "Quit apps and privacy",
            "Read privacy policies before linking quit apps to social networks.",
            "Disable public leaderboards if comparison triggers shame.",
            "Export quit date data for clinicians if apps allow.",
            "Delete apps that push nicotine product ads.",
        ),
        S(
            "Skin and wound checks while quitting",
            "Nicotine withdrawal does not stop need for dermatology checks on biologic exposed skin.",
            "Wounds heal slower while smoking; photograph surgical sites per surgeon instructions.",
            "Report new leg swelling or calf pain when activity resumes after quitting.",
            "Sun protection remains important on immunosuppression regardless of smoking status.",
        ),
    ],
    "disability_fmla.py": [
        S(
            "Probationary period employees",
            "New hires may still have ADA accommodation rights even during probation in many cases; verify locally.",
            "Document performance separately from medically certified absences.",
            "Ask HR whether probation policies interact with leave programs at your employer.",
            "Legal consult helps when termination timing feels suspicious near diagnosis disclosure.",
        ),
        S(
            "Open enrollment and FMLA overlap",
            "Changing insurance mid year affects which infusion centers are in network during leave.",
            "Compare plans during open enrollment with flare history in mind.",
            "COBRA bridges job loss gaps; deadlines are strict.",
            "Ask HR deadlines in writing when leaving roles.",
        ),
        S(
            "Documentation for intermittent leave patterns",
            "Charts showing Tuesday infusion plus occasional flare Wednesdays support predictable patterns.",
            "Estimate frequency ranges honestly rather than minimizing symptoms.",
            "Update estimates when biologic schedule changes.",
            "Keep infusion chair confirmation emails as absence proof.",
        ),
        S(
            "Coworker ally strategies",
            "One trusted coworker can cover short bathroom breaks without broadcasting diagnosis.",
            "Slack status can say brief break without medical detail.",
            "Gratitude matters when colleagues pick up slack during flares.",
            "Rotate favors back when you are well to sustain relationships.",
        ),
    ],
    "running.py": [
        S(
            "Biologic travel and running camps",
            "Running camps away from home need refrigerated biologic plans separate from workout plans.",
            "Know nearest hospital on camp map if abdominal pain spikes during activity week.",
            "Coach waiver forms should list emergency contacts and allergy meds.",
            "Do not skip biologic doses to avoid missing camp; coordinate with infusion center.",
        ),
        S(
            "Foot care and blister prevention",
            "Moisture wicking socks reduce blisters when urgency forces sudden stops.",
            "Trim toenails before long runs to avoid black nails on downhills.",
            "Treat hot spots early with tape before they bleed into shoes.",
            "Alternate shoes after rain runs so insoles dry fully.",
        ),
        S(
            "Running with service or support dogs",
            "Rules for animals on trails vary; service dog handlers plan bathroom routes for both.",
            "Hydration packs for dogs differ from human IBD hydration plans.",
            "Notify race directors about service animals when registering.",
            "Clean up responsibly; bag dispensers help communities stay welcoming.",
        ),
        S(
            "Post flare return micro plan",
            "Week one walk only; week two jog thirty seconds every five minutes walking.",
            "Stop if nocturnal stools return; reset without guilt.",
            "GI clearance after hospitalization before any impact.",
            "Document return plan in portal so clinicians approve milestones.",
        ),
    ],
    "spicy_nuts.py": [
        S(
            "Shopping aisle strategy",
            "Read nut butters labels for added palm oil or sugar alcohols before buying large jars.",
            "Single serve nut butter packets reduce waste when trials fail early.",
            "Bulk spice bins risk cross contact; choose sealed bottles when allergy or strictures matter.",
            "Store opened nut flours in fridge to prevent rancid taste mimicking flare.",
        ),
        S(
            "Picnic and barbecue season",
            "Potluck chili labels should list heat level and nut garnishes separately.",
            "Bring your own bun and patty if cross contact with seeds worries you.",
            "Grill brushes leaving wire bristles are rare but serious; inspect plates.",
            "Ice packs keep nut butter sandwiches safe in summer heat.",
        ),
        S(
            "Texture modification tools",
            "Food processors turn whole nuts into pastes for baking trials.",
            "Silicone mats help roast vegetables with spice blends without sticking burns.",
            "Slow cookers soften tough meats with mild spice when chewing is limited.",
            "Immersion blenders smooth soups after failed crunch experiments.",
        ),
        S(
            "Follow up after failed spice trial",
            "Note which meal, sleep quality, and stress level surrounded the failure.",
            "Wait until inflammation labs quiet before repeating heat tests.",
            "Try different cuisine spice profiles; capsaicin is not the only irritant.",
            "Share failed trial data with dietitian to plan next variable.",
        ),
    ],
}

for _fname in (
    "cded.py",
    "scd.py",
    "colon_surveillance.py",
    "smoking.py",
    "disability_fmla.py",
    "running.py",
    "spicy_nuts.py",
):
    FINAL[_fname] = list(FINAL[_fname]) + [TAIL_SECTION]

FINAL["smoking.py"].append(
    S(
        "Integrating quit goals with infusion center routines",
        "Schedule quit coaching calls on non infusion days when fatigue is lower.",
        "Tell infusion nurses your quit date so they celebrate milestones during chair time.",
        "Avoid scheduling quit day same week as major steroid taper if mood swings worry you.",
        "Keep nicotine replacement supplies in infusion bag only if storage rules allow.",
        "Even a single cigarette after weeks smoke free is a lapse, not proof that quitting is impossible forever.",
    )
)
FINAL["running.py"].append(
    S(
        "Rainy day treadmill etiquette",
        "Wipe machines after use when GI symptoms increase bathroom urgency frequency.",
        "Choose gym times when locker rooms are staffed if you feel safer.",
        "Headphones help privacy on treadmills near others.",
        "Cancel gym membership guilt free during postoperative months if finances tighten.",
        "Ten minutes of movement on a rainy treadmill still counts as training when storms would have cancelled an outdoor jog entirely.",
    )
)
FINAL["disability_fmla.py"].append(
    S(
        "One sentence to remember",
        "Protected leave and accommodations exist so illness does not automatically erase the career you built.",
    )
)
FINAL["spicy_nuts.py"].append(
    S(
        "One sentence to remember",
        "Spice and crunch trials are data collection tools, not loyalty tests to any online food tribe.",
    )
)
FINAL["running.py"].append(
    S(
        "One sentence to remember",
        "A shortened jog near home bathrooms still protects fitness identity when marathon plans wait for calmer inflammation seasons.",
    )
)
FINAL["disability_fmla.py"].append(
    S(
        "State paid leave programs snapshot",
        "Some states offer paid family medical leave overlapping IBD absences; search official state labor websites.",
        "Local city ordinances occasionally add sick time accrual faster than state minimums.",
        "Nonprofit legal aid clinics summarize options at no cost in many counties.",
        "Keep a spreadsheet of programs applied to and response dates.",
    )
)
FINAL["spicy_nuts.py"].append(
    S(
        "Meal prep when testing crunch and heat separately",
        "Cook base chicken or tofu plain, then split portions into mild and spicy plates for same dinner.",
        "Add ground seeds only to one rice bowl so comparison stays fair.",
        "Label containers MILD and TEST in fridge to prevent sleepy grabbing mistakes.",
        "Freeze untested portions if appetite drops mid week.",
    )
)
