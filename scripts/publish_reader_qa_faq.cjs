/**
 * Publish core Reader Q&A answers (education only, not medical advice).
 * Usage: node scripts/publish_reader_qa_faq.cjs
 */
const { Client } = require('pg');
const fs = require('fs');
const path = require('path');

function readConfigEnv(filePath) {
  if (!fs.existsSync(filePath)) return {};
  return fs.readFileSync(filePath, 'utf8').split(/\r?\n/).reduce((values, line) => {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) return values;
    const idx = trimmed.indexOf('=');
    if (idx === -1) return values;
    values[trimmed.slice(0, idx).trim()] = trimmed
      .slice(idx + 1)
      .trim()
      .replace(/^["']|["']$/g, '');
    return values;
  }, {});
}

function normalizeDatabaseUrl(url) {
  const value = String(url || '').trim();
  if (!value) return value;
  if (/[?&]uselibpqcompat=/i.test(value)) return value;
  if (/[?&]sslmode=(prefer|require|verify-ca)\b/i.test(value)) {
    return value.replace(
      /([?&]sslmode=)(prefer|require|verify-ca)\b/i,
      '$1verify-full'
    );
  }
  return value;
}

const ITEMS = [
  {
    slug: 'flare-or-bad-few-days',
    title: 'How do I know if this is a flare or just a bad few days?',
    question:
      'How do I know if this is a flare or just a bad few days? I want a threshold, not a definition.',
    answer: `There is no lab number that labels a single night as “flare” vs “bad day.” A useful threshold many clinics teach is time plus red flags: if symptoms settle in about 24 to 48 hours after a known trigger (a meal, travel, menses, a missed dose, a virus), it is often a rough patch. If they last beyond 48 hours, keep worsening, or come with blood, night stools, fever, or weight drop, treat it as possible flare activity and contact your IBD team.

A practical checkpoint: write down stool count, blood, urgency, pain, fever, and what you ate or skipped. Compare today with your usual baseline, not with a perfect week. One extra bathroom trip after spicy food is different from three nights of waking to stool plus new blood.

Do not wait on the 48-hour clock if red flags appear. Heavy bleeding, fainting, high fever, a rigid belly, or inability to keep fluids down is urgent, not a wait-and-see experiment.

Related education: [Flare symptoms](/blog/flare-symptoms-ibd) and the [first 48 hours of a flare checklist](/blog/flare-first-48-hours).`
  },
  {
    slug: 'normal-bloodwork-still-sick',
    title: 'My symptoms are bad but my bloodwork came back normal. Does that mean I’m fine?',
    question:
      'My symptoms are bad but my bloodwork came back normal. Does that mean I’m fine? I feel dismissed.',
    answer: `Normal bloodwork does not mean you imagined this. CRP and other blood markers measure one slice of inflammation. Some people with active Crohn’s or colitis have quiet blood tests, especially with small-bowel or limited rectal disease. A normal CRP is good news on that one axis. It is not a verdict that you are “fine.”

Symptoms still need a plan. Fecal calprotectin, imaging, or endoscopy can show gut inflammation when blood looks calm. Overlap conditions (IBS-like symptoms, bile acid diarrhea, strictures, anemia, vitamin gaps) can also hurt with quiet CRP. None of those mean you should stop asking for help.

Bring a one-week log: night stools, blood, urgency, food, and fatigue. Ask whether calprotectin is next, whether drug levels or antibodies matter on a biologic, and whether a scope is warranted despite normal bloodwork. You are allowed to say, “I still cannot function,” even when the printout looks tidy.

Related education: [Normal CRP but still sick](/blog/crp-normal-still-symptoms-ibd), [reading IBD labs](/blog/reading-ibd-labs-calprotectin-crp), and [high calprotectin: what next](/blog/high-calprotectin-what-next).`
  },
  {
    slug: 'what-to-eat-during-a-flare',
    title: 'What can I actually eat during a flare?',
    question:
      'What can I actually eat during a flare? Please give me a list.',
    answer: `There is no universal “eat this, never that” list that fits every Crohn’s or colitis flare. Triggers are individual. What we can say honestly: many people do better for a short stretch on simpler, lower-residue textures (white rice, peeled cooked vegetables, eggs, yogurt if tolerated, smooth nut butters, oral nutrition drinks if appetite is low) while inflammation is loud. Fiber, skins, seeds, raw salads, and greasy takeout often feel worse during those days. That is a pattern, not a forever identity.

A list without your disease location, strictures, and current meds can miss the point. Someone with a narrowing may need a different texture than someone with ulcerative colitis. Exclusive enteral nutrition is a medical protocol for some Crohn’s patients, not a DIY juice cleanse.

Work with your GI and, when possible, an IBD-aware dietitian. Use a short flare window, then re-expand foods as symptoms settle. Do not stop prescribed medicine because a meal plan promised remission.

Related education: [Low-residue diet during a flare](/blog/low-residue-diet-flare), [best foods for a Crohn’s flare](/blog/best-foods-crohns-flare), and the [low-residue guide](/guides/low-residue-diet-ibd).`
  },
  {
    slug: 'diet-alone-stop-medication',
    title: 'Can diet alone put me in remission so I can stop my medication?',
    question:
      'Can diet alone put me in remission so I can stop my medication? I keep seeing carnivore, leaky gut, and juice cleanse claims.',
    answer: `Diet can support how you feel and how well you nourish yourself. It is not a substitute for prescribed IBD therapy for most people with Crohn’s or ulcerative colitis. AGA 2024 nutrition guidance frames diet and nutrition therapies as part of medical care (enteral nutrition, selected exclusion diets, micronutrients, dietitian involvement), not as a standalone cure that lets you abandon medicine on your own.

Carnivore, “leaky gut” protocols, and juice cleanses often sell a story: if you eat perfectly, you will not need a biologic. Uncontrolled inflammation is what leads to strictures, hospitalizations, and surgery. Stopping medication without your gastroenterologist is one of the highest-risk decisions patients make after reading online forums.

If a way of eating helps symptoms, tell your team. They can check whether the gut is actually healing (calprotectin, scope), watch nutrient gaps, and keep therapy on board. Feeling better for two weeks on an extreme diet is not mucosal healing.

Related education: [AGA 2024 diet and nutritional therapies](/research#aga-diet-2024), [autoimmune diet myths](/blog/autoimmune-diet-myths), and [carnivore diet and IBD](/blog/carnivore-diet-ibd-myths).`
  },
  {
    slug: 'nurse-line-vs-er',
    title: 'When do I call the nurse line vs. go to the ER?',
    question:
      'When do I call the nurse line vs. go to the ER? It is 11pm and I am not sure.',
    answer: `Go to the ER or call 911 now if you have: heavy rectal bleeding or bleeding with dizziness; severe abdominal pain, especially with a rigid or board-like belly; high fever with worsening pain; persistent vomiting and you cannot keep fluids down; confusion, fainting, or almost no urine. Those are not “wait for the morning nurse line” symptoms.

Call the GI nurse line or on-call number (or follow your clinic’s after-hours instructions) when symptoms are worse than baseline but you are stable: more urgency or moderate blood, a flare that matches your action plan, fever that is low-grade, dehydration you can still sip through, or you need guidance on holding a dose. Have your medication list, last biologic date, and a short symptom log ready.

If you are unsure and red flags are even possible, choose emergency care. Clinics would rather you be evaluated than wait overnight with bleeding, a rigid abdomen, or high fever on immunosuppression.

Related education: [When to call GI vs go to the ER](/blog/when-to-call-gi-vs-er-ibd) and [when to go to the ER](/blog/when-to-go-er-ibd).`
  },
  {
    slug: 'biologic-how-long-until-it-works',
    title: 'How long until my biologic starts working, and is it normal to feel worse first?',
    question:
      'How long until my biologic starts working, and is it normal to feel worse first? I am in weeks 2 to 6 of induction and anxious.',
    answer: `Induction is slow on purpose. Many teams look for meaningful change over weeks, not overnight. Some people notice less night stool or less urgency in the first month; others need the full loading schedule (often around 8 to 12 weeks) plus a maintenance dose before anyone judges “this drug failed.” Feeling tired after early infusions or injections is common. Feeling dramatically worse with fever, spreading rash, trouble breathing, chest pain, or a rigid belly is not “normal induction.” That needs same-day contact.

Do not stop steroids on your own because you started a biologic. Tapers run in parallel under your clinician. Keep a simple log so small wins are visible when anxiety is loud in weeks 2 to 6.

Around 12 weeks many teams reassess: continue, adjust dose or interval, or switch class if there is little response. Ask when they will check calprotectin or a scope, not only how you feel on a Tuesday.

Related education: [First 12 weeks on a biologic](/blog/starting-biologic-first-12-weeks), [Humira and fatigue](/blog/humira-fatigue-ibd), [Skyrizi patient questions](/blog/skyrizi-patient-questions-ibd), and [Entyvio patient guide](/blog/entyvio-patient-guide-ibd).`
  },
  {
    slug: 'insurance-denied-biologic',
    title: 'My insurance denied my biologic. What do I do now?',
    question:
      'My insurance denied my biologic. What do I do now?',
    answer: `A denial is a paperwork decision, not a medical one. Ask for the denial in writing, the exact reason, and the appeal deadline. Call your GI office the same day: they often own the prior authorization packet, peer-to-peer review, and expedited appeal if your clinician documents urgency.

Keep one folder: denial letter, reference numbers, diagnosis codes, prior drugs tried, labs, and colonoscopy notes. Manufacturer hubs and copay programs may help after approval; some offer bridge supply while appeals run. Ask about step-therapy documentation and whether CMS interoperability and prior-authorization rules (CMS-0057-F) affect how quickly your plan must respond.

If symptoms worsen while you wait, tell your clinician. Administrative delay should not silence bleeding, weight loss, or severe pain. Appeal letter templates and a realistic PA timeline exist so you are not inventing this from scratch at midnight.

Related education: [Prior authorization timeline](/blog/prior-authorization-biologics-timeline), [insurance and biologics](/blog/insurance-biologics-ibd), [appeal letters](/guides/foundation-ibd-appeal-letters), and [CMS-0057-F fact sheet](https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-and-prior-authorization-final-rule-cms-0057-f).`
  },
  {
    slug: 'iron-b12-vitamin-d-do-i-need',
    title: 'Do I need to take iron, B12, or vitamin D, and how do I know?',
    question:
      'Do I need to take iron, B12, or vitamin D, and how do I know?',
    answer: `You know from labs and symptoms interpreted with your clinician, not from a supplement aisle protocol. Iron, B12, and vitamin D deficiencies are common in IBD because of blood loss, small-bowel inflammation, restricted diets, and reduced sun or intake. Fatigue, dizziness, mouth sores, bone aches, or neuropathy can be clues. They are not a shopping list.

Ask which labs are already on file (CBC, ferritin, iron studies, B12, 25-OH vitamin D) and whether they need repeating. Dose, route (oral vs IV iron, B12 injections), and timing around inflammation are clinical decisions. Taking high-dose iron during an active flare can be poorly tolerated; taking vitamin D without a level can miss both deficiency and excess.

Bring your current supplements to the visit. “A multivitamin” is not the same as treating documented deficiency.

Related education: [Iron, B12, and vitamin D in IBD](/blog/iron-b12-vitamin-d-ibd) and [micronutrient deficiencies](/blog/micronutrients-ibd-deficiencies).`
  },
  {
    slug: 'child-just-diagnosed-first-month-school',
    title: 'My child was just diagnosed. What do I do in the first month, and what about school?',
    question:
      'My child was just diagnosed. What do I do in the first month, and what about school?',
    answer: `First month: you do not have to become an IBD expert overnight. Focus on the care team (pediatric GI, nurse, often a dietitian), the medication plan, a simple symptom and stool log, and red flags for when to call. Learn the names of drugs and the next appointment. Nutrition is “enough calories and protein while they feel awful,” not a perfect diet. Siblings need a short, honest explanation so the house is not only about the diagnosis.

School: in the U.S., a Section 504 plan can document bathroom access, water bottles, extra time, nurse storage for meds, and flare absences. Start the paperwork early with the school nurse and counselor. You do not have to share the entire chart. Functional needs are enough. Meet before a long absence becomes a crisis.

Give yourself permission to be scared and still make one next call. The first 30 days are about safety and a plan, not mastering every article.

Related education: [Newly diagnosed, first 30 days](/blog/newly-diagnosed-first-30-days), [workplace and school rights / 504](/blog/workplace-school-ibd-rights), [school planning](/blog/school-planning-ibd-before-august), and [siblings when a child has IBD](/blog/siblings-when-child-has-ibd).`
  },
  {
    slug: 'pregnancy-safe-stay-on-medication',
    title: 'Is it safe to get pregnant / stay on my medication during pregnancy?',
    question:
      'Is it safe to get pregnant, and is it safe to stay on my medication during pregnancy?',
    answer: `Many people with Crohn’s or ulcerative colitis have healthy pregnancies. The higher-stakes risk is often uncontrolled inflammation, not “being on a medicine.” Plan with your gastroenterologist and obstetric team before you try to conceive when you can. Active disease, poor nutrition, and sudden drug stops are what clinics work to avoid.

Do not stop a biologic or other IBD therapy because a forum said it was unsafe. Many therapies are continued in pregnancy under specialist oversight. A few drugs (for example methotrexate, and some others) need a planned washout. Your team will name those. Partners’ medications can matter too.

Ask for a preconception visit: medication list, recent labs, flare history, folate and iron status, and who to call if a flare starts while pregnant. This is shared decision-making with specialists, not a yes/no from a search result.

Related education: [IBD and pregnancy planning](/blog/ibd-pregnancy-planning) and [Foundation pregnancy resources](/guides/pregnancy-ibd-foundation-resources).`
  },
  {
    slug: 'glp-1-if-i-have-ibd',
    title: 'Should I be on a GLP-1 if I have IBD?',
    question:
      'Should I be on a GLP-1 (semaglutide, tirzepatide, etc.) if I have IBD?',
    answer: `IBDPal cannot tell you whether you should start a GLP-1. That is a decision with your gastroenterologist and the clinician who would prescribe it (often primary care or endocrinology), based on diabetes, weight, other medicines, and your IBD activity.

What is new: 2026 congress coverage reported observational signals that GLP-1 use in people with IBD was associated with lower steroid use, hospitalizations, and surgery in matched records. That is interesting, not a prescription. Observational data cannot prove the drug caused those outcomes. Side effects (nausea, delayed emptying, rare serious events) and nutrition still matter in Crohn’s and colitis.

If you are already on a GLP-1 or considering one, tell your GI. Ask how it might affect appetite, hydration, and flare vs delayed-emptying symptoms, and whether IBD therapy stays unchanged. Do not start or stop either class based on headlines.

Related education: [January 2026 congress notes on GLP-1s in IBD](/news) and the [AGA press release on evolving IBD care](https://gastro.org/press-releases/from-glp-1s-to-engineered-probiotics-new-research-highlights-evolving-ibd-care/).`
  },
  {
    slug: 'joint-aches-eye-pain-skin-ibd',
    title: 'Are these joint aches, eye pain, or skin lesions related to my IBD?',
    question:
      'Are these joint aches / eye pain / skin lesions related to my IBD? I did not realize they could be connected.',
    answer: `They can be. Crohn’s and ulcerative colitis are not only bowel diseases. Joints, eyes, and skin are among the most common extraintestinal manifestations. Peripheral joint pain, back stiffness, uveitis (red painful eye, light sensitivity, vision change), erythema nodosum, and pyoderma gangrenosum show up in clinic more often than patients expect.

That does not mean every ache is IBD. Viral illness, overuse, and other autoimmune overlap happen too. Eye pain with vision change is urgent: same-day ophthalmology, not a wait-for-GI-Friday plan. Rapidly worsening ulcers or spreading skin lesions also need prompt care.

Tell your gastroenterologist about joints, eyes, and skin even if the colonoscopy looks improved. Sometimes bowel and joints flare together; sometimes they do not. A photo of a rash and a one-line timeline help more than “I have been sore.”

Related education: [Extraintestinal manifestations](/blog/ibd-extraintestinal-manifestations), [IBD joint pain](/blog/ibd-joint-pain-arthritis), [uveitis](/blog/uveitis-eye-inflammation-ibd), and [pyoderma / erythema nodosum](/blog/pyoderma-erythema-nodosum-ibd).`
  }
];

(async () => {
  const root = path.resolve(__dirname, '..');
  const env = readConfigEnv(path.resolve(root, '..', 'ibdpal-server', 'config.env'));
  const url = normalizeDatabaseUrl(process.env.DATABASE_URL || env.DATABASE_URL || '');
  if (!url) {
    console.error('No DATABASE_URL');
    process.exit(1);
  }
  const client = new Client({
    connectionString: url,
    ssl: url.includes('localhost') ? false : { rejectUnauthorized: false }
  });
  await client.connect();

  let inserted = 0;
  let updated = 0;
  for (const item of ITEMS) {
    if (item.answer.length < 40 || item.answer.length > 12000) {
      throw new Error(`Answer length out of range for ${item.slug}: ${item.answer.length}`);
    }
    const exists = await client.query(
      'SELECT question_id FROM ibdpal_reader_questions WHERE slug = $1 LIMIT 1',
      [item.slug]
    );
    if (exists.rows.length) {
      await client.query(
        `UPDATE ibdpal_reader_questions
         SET question_text = $1, title = $2, answer_text = $3, updated_at = NOW()
         WHERE slug = $4`,
        [item.question, item.title, item.answer, item.slug]
      );
      updated += 1;
      console.log('updated:', item.slug);
      continue;
    }
    await client.query(
      `INSERT INTO ibdpal_reader_questions (
        question_text, title, answer_text, slug, source, status,
        published_at, created_at, updated_at
      ) VALUES ($1, $2, $3, $4, 'editorial', 'answered', NOW(), NOW(), NOW())`,
      [item.question, item.title, item.answer, item.slug]
    );
    inserted += 1;
    console.log('published:', item.slug);
  }

  const counts = await client.query(
    `SELECT status, COUNT(*)::int AS n FROM ibdpal_reader_questions GROUP BY status ORDER BY n DESC`
  );
  console.log('inserted', inserted, 'updated', updated);
  console.log('counts', JSON.stringify(counts.rows));
  await client.end();
})().catch((err) => {
  console.error(err);
  process.exit(1);
});
