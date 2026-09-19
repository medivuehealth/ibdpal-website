/**
 * Answer + publish the 5 new ask_page reader questions (ids 15-19).
 * Target: ~10-minute read each (under 12,000 char API/DB cap).
 * Usage: node scripts/publish_new_reader_qa_batch.cjs
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

function wordCount(text) {
  return String(text || '')
    .trim()
    .split(/\s+/)
    .filter(Boolean).length;
}

const ITEMS = [
  {
    id: 15,
    slug: 'glp-1-ozempic-mounjaro-ibd-diarrhea-nausea',
    title: 'Will a GLP-1 like Ozempic or Mounjaro make IBD diarrhea or nausea worse?',
    answer: `Short answer: a GLP-1 medicine can change gut speed, fullness, and nausea for almost anyone who takes it. That does not automatically mean it is “bad for IBD,” and it does not automatically mean it will calm gut inflammation either. For people with Crohn’s disease or ulcerative colitis, the honest frame is this: GLP-1 drugs (semaglutide, tirzepatide, and related medicines sold under names such as Ozempic, Wegovy, Mounjaro, and Zepbound) act mainly on appetite, gastric emptying, and metabolic pathways. They are not IBD biologics. Some people with IBD feel better overall after weight loss and steadier blood sugar. Others notice more nausea, constipation, or diarrhea and wonder whether the drug is flaring their disease. Those two stories can both be true in different people, and only your gastroenterologist can sort which pattern is yours.

Start with what the medicine is designed to do. GLP-1 receptor agonists slow how quickly the stomach empties, increase satiety, and often reduce calorie intake. Slow emptying is useful for weight and glucose control. It is also the reason early weeks commonly bring nausea, early fullness, burping, and sometimes vomiting if doses climb too fast or meals are large and fatty. Diarrhea can appear too, especially when people change diet sharply, use sugar alcohols, or have an underlying bowel that already runs loose. Constipation is also reported. So if you already live with urgency, liquid stools, or post-resection bowel habits, a new GLP-1 can amplify symptoms that feel “IBD-ish” without proving that mucosal inflammation is rising.

That distinction matters. IBDPal readers often ask whether a GLP-1 “helps gut inflammation.” Right now, patient education should stay careful: interesting research and clinic anecdotes are not the same as an approved IBD indication. Do not start, stop, or dose-escalate a GLP-1 to treat Crohn’s or colitis on your own. If you and your clinicians choose a GLP-1 for obesity, diabetes, or another labeled reason, treat IBD monitoring as a parallel track. Keep your flare plan, calprotectin schedule, and biologic or small-molecule therapy exactly as prescribed unless your IBD team changes them.

How do you tell side effect from flare? Use a two-week pattern log, not a single bad afternoon. Track dose day, meal size, fat content, stool form (Bristol scale helps), night stools, blood, mucus, fever, abdominal pain location, and whether symptoms cluster in the hours after injection or after large meals. GLP-1 nausea often peaks after dose increases and eases when titration slows. Active IBD more often brings progressive urgency, night waking, blood, weight drop, or a rising fecal calprotectin. Neither rule is perfect. Overlap is common after ileal resection, with bile acid diarrhea, with IBS-like symptoms, and when anxiety about a new drug is high. Bring the log to both the prescribing clinician and your GI nurse. Ask explicitly: “Do we need a calprotectin now, or is this expected GLP-1 gut slowing?”

Practical ways people reduce GLP-1 gut misery without abandoning therapy (always confirm with your prescriber): smaller meals, less grease, slower eating, careful alcohol limits, and not jumping dose weeks early because a friend “felt fine.” Stay hydrated. Report persistent vomiting, inability to keep fluids down, severe upper abdominal pain, or signs of dehydration the same day. Those are not “wait and see if IBD calms down” symptoms. If you are on immunosuppression, fever plus worsening diarrhea still belongs on your IBD red-flag list.

Insurance, compounding, and “research peptides” deserve a clear warning. Stick to pharmacy-dispensed, clinician-prescribed products. Unregulated pens and online powders add dosing and sterility risk on top of IBD complexity. If cost is the barrier, ask about manufacturer support and covered alternatives rather than gray-market substitutes.

If diarrhea was already your baseline, ask whether bile acid diarrhea, infections, medication timing, or diet changes coincide with the GLP-1 start. A falling calprotectin with ongoing liquid stools can still mean a functional or post-surgical problem rather than uncontrolled IBD—see our companion answer on that pattern. If calprotectin climbs, blood returns, or night stools surge after you were stable, treat that as possible disease activity until your team says otherwise.

Related education: [Should I be on a GLP-1 if I have IBD?](/ask/glp-1-if-i-have-ibd), [Reading IBD labs](/blog/reading-ibd-labs-calprotectin-crp), [CRP normal but still sick](/blog/crp-normal-still-symptoms-ibd), and [When to call GI vs ER](/blog/when-to-call-gi-vs-er-ibd).`
  },
  {
    id: 16,
    slug: 'iv-biologic-to-home-injection-insurance',
    title: 'Can I switch from an IV biologic infusion to a home injection of the same drug?',
    answer: `Often yes in clinical terms—and often “not automatically” in insurance terms. Many IBD medicines begin as clinic infusions and later offer a subcutaneous (under-the-skin) maintenance option for some patients. Vedolizumab (Entyvio), risankizumab (Skyrizi), and other advanced therapies have pathways where IV induction is followed by injections at home or in clinic, depending on the label, your disease, and your team’s judgment. Infliximab biosimilars and other agents have their own IV-versus-subcut stories. The medical question and the pharmacy-benefit question are related but not identical. Your gastroenterologist decides whether a switch is appropriate for disease control. Your insurer and specialty pharmacy decide whether that new form is covered as a continuation or treated like a fresh authorization.

Clinically, a switch is usually considered after induction when disease is settling, lab trends look favorable, and you (or a caregiver) can learn injection technique, storage, and what to do if a dose is missed. Infusion chairs provide observation time and nursing support. Home pens trade that for convenience, travel flexibility, and fewer work absences. They also shift responsibility: refrigeration, sharps disposal, timing around travel, and recognizing injection-site reactions. Ask for teach-back training before your first solo dose. Ask what to do if the pen misfires, if you travel across time zones, or if a dose lands during a fever or infection workup.

Insurance is where people get blindsided. Medical benefit (Part B–style buy-and-bill infusions) and pharmacy benefit (specialty pharmacy pens) are different buckets. Moving from IV to subcut can change which department pays, which prior authorization form is required, which copay assistance applies, and whether step therapy resets. Some plans treat the subcutaneous product as a new request even when the active molecule is the same family. Others approve a “site of care” or “formulation change” more smoothly if your clinic’s authorization team submits clinical notes showing stable response and medical necessity for home administration. Do not assume the infusion approval letter covers the pen.

Before you celebrate leaving the infusion center, ask your clinic’s prior-auth or specialty pharmacy coordinator these concrete questions: Will this be billed under medical or pharmacy benefit? Is a new prior authorization required? What is the expected turnaround? Is there a bridge supply if approval lags? Does manufacturer support change when the NDC or formulation changes? Will my deductible reset mid-year? Get the answers in writing or in the patient portal when possible. If you have Medicare, Medicaid, or an employer carve-out specialty vendor, rules vary again. International readers should translate this into local hospital pharmacy and national formulary language rather than U.S. fax-prior-auth folklore.

Timing the switch matters for disease control. Avoid a gap between the last infusion and the first injection unless your team planned it. Ask whether drug levels, antibodies, calprotectin, or a clinic visit should land near the transition. If symptoms creep back during a coverage delay, call early—waiting weeks “hoping the pen arrives” can cost remission. Some teams keep one more infusion scheduled as a safety net until the first home shipments are in your fridge.

Side effects and monitoring do not disappear because the route changed. Injection-site redness is common; spreading rash, facial swelling, wheezing, or chest tightness is urgent. Keep vaccinations, TB and hepatitis screening history, and infection precautions on the same page you used for infusions. Travel with a cooling plan and a clinician letter if airport security may question refrigerated pens.

If the insurer denies the subcutaneous version, that is not the end. Ask for the denial reason code, submit peer-to-peer review, and use appeal language that ties home administration to adherence, work or school constraints, and documented response to the molecule. Manufacturer hubs sometimes help with temporary supply during appeal. Meanwhile, do not stop therapy without a written interim plan from your IBD team.

Related education: [Entyvio patient guide](/blog/entyvio-patient-guide-ibd), [Skyrizi patient questions](/blog/skyrizi-patient-questions-ibd), [Infusion day expectations](/blog/infusion-day-what-to-expect), [Prior authorization timeline](/blog/prior-authorization-biologics-timeline), and [Insurance and biologics](/blog/insurance-biologics-ibd).`
  },
  {
    id: 17,
    slug: 'calprotectin-down-still-liquid-stools-ibs-or-flare',
    title: 'If calprotectin drops but I still have liquid stools, is it IBS instead of an IBD flare?',
    answer: `A falling fecal calprotectin is genuinely good news about gut inflammation. It is not a full verdict that every loose stool is now “just IBS.” Think of calprotectin as a stool marker that often tracks neutrophilic inflammation in the intestine. When it falls into your personal target range, the odds of active mucosal IBD usually improve. Liquid stools can still continue for many other reasons: irritable bowel syndrome overlap, bile acid diarrhea after ileal disease or resection, diet change, infection, pelvic floor dysfunction, medication effects, microscopic inflammation below the radar of one test, or incomplete healing in a skip area. The useful clinical question is not “IBD or IBS forever?” It is “What is driving today’s liquid stool while inflammation markers look quieter?”

First, confirm the trend, not a single printout. Labs have cutoffs that vary by assay. A drop from very high to mid-range is progress even if the number is not yet “perfect.” Ask your team what target they use for you, whether the sample was collected correctly, and whether a repeat is needed before rewriting your whole diagnosis. Blood markers such as CRP can be quiet while the gut is active, and the reverse story also happens: symptoms roar while calprotectin settles. That is why many IBD programs still use scopes, imaging, or structured symptom scores alongside stool tests.

IBS-like symptoms are common in people who already have Crohn’s or ulcerative colitis. After inflammation cools, the bowel can remain hypersensitive. Urgency, loose stools with stress or meals, and bloating without blood or night fever can fit IBS overlap. Labeling it IBS does not mean the original IBD vanished or that you imagined years of disease. It means the treatment plan may shift toward diet structure, fiber titration when appropriate, gut-directed behavioral strategies, and careful medication choices—while you still keep IBD surveillance on the calendar.

Bile acid diarrhea deserves special mention after terminal ileum inflammation or resection. Excess bile acids in the colon pull water and cause urgent liquid stools even when calprotectin looks reassuring. Clinicians may trial a bile acid binder when the story fits. Do not start binders as a self-experiment without guidance if you have fat-soluble vitamin issues or complex medication lists. Pancreatic enzyme problems, small intestinal bacterial overgrowth after surgery, and overflow around partial obstruction are other “loose stool with quieter calprotectin” possibilities that need a clinician, not a forum poll.

How should you act this week? Keep a seven-day diary: stool form, night stools, blood, mucus, meal triggers, caffeine, artificial sweeteners, new medicines (including antibiotics or GLP-1 drugs), and stress load. Note whether urgency is meal-related or random. Share whether you ever feel incomplete emptying or pelvic pressure. Bring the diary plus your calprotectin numbers to the visit and ask three direct questions: Do we repeat stool testing? Do we need imaging or a scope despite the drop? Should we evaluate bile acid diarrhea, infection, or IBS overlap next?

Red flags still override a pretty lab value. New heavy bleeding, nocturnal stools that are escalating, fever, weight loss, severe pain, or dehydration needs same-week or urgent contact even if last month’s calprotectin looked better. A reassuring lab is a snapshot. Your body can change between draws.

Do not stop IBD therapy because stools remain loose. Mucosal healing and symptom healing are related but not identical clocks. Many people need months of stable therapy after calprotectin improves before anyone discusses de-escalation. Stopping a biologic because “it must be IBS now” is a common way silent inflammation returns.

Related education: [Does one calprotectin mean I am getting worse?](/ask/calprotectin-one-result-getting-worse), [High calprotectin: what next](/blog/high-calprotectin-what-next), [Reading IBD labs](/blog/reading-ibd-labs-calprotectin-crp), [Normal CRP but still sick](/blog/crp-normal-still-symptoms-ibd), and [Flare or bad few days](/ask/flare-or-bad-few-days).`
  },
  {
    id: 18,
    slug: 'acne-eczema-on-advanced-ibd-therapy',
    title: 'Severe acne or eczema on advanced IBD therapy: drug side effect or another autoimmune issue?',
    answer: `Both are possible—and you should not guess alone from a bathroom mirror. Advanced IBD therapies (biologics and targeted small molecules) can be associated with skin changes in some people. IBD itself also links to extraintestinal skin disease. Steroid tapers, antibiotics, nutrition gaps, and everyday eczema triggers muddy the picture further. The practical approach is to describe the rash clearly, photograph it, note timing against dose changes, and get the right clinician eyes on it quickly when it is severe, painful, blistering, or near the eyes.

Start by separating common patterns patients report. Acne-like bumps on the face, chest, or back can appear or worsen with certain therapies and with steroid exposure. Eczema-like dry, itchy patches can flare when the skin barrier is stressed, when immunosuppression shifts immune tone, or when a person already had atopic dermatitis. Psoriasiform rashes are discussed with some anti-TNF and other pathways; paradoxical inflammation is a known clinic conversation, not a personal failure. None of these labels are DIY diagnoses. A dermatologist familiar with IBD medicines and an IBD clinician who knows your drug history should share the story.

Timing is one of your best clues. Did the skin change within days of a steroid burst, a new induction dose, or a biologic class switch? Did it appear after months of stable maintenance? Did antibiotics for a fistula or pouchitis precede it? Write a one-page timeline: drug names, dates, skin onset, itch versus pain, distribution, and whether gut symptoms moved in parallel. Bring prior photos. Clinics make better decisions with a timeline than with “my skin has been crazy.”

When is skin an urgent problem? Rapidly spreading painful ulcers, fever with rash, facial swelling, trouble breathing, blistering that looks like a burn, eye involvement, or skin breaking down over joints needs same-day care—ER or urgent dermatology depending on severity. Do not wait for the next infusion nurse visit. For itchy but stable patches, same-week primary care or dermatology triage plus a message to your GI team is usually the path.

Do not stop your IBD drug the night a pimple cluster appears. Abrupt cessation can jeopardize gut remission. Ask whether the plan is topical care, a dermatology referral, a temporary bridge, lab checks, or—only if specialists agree—a class change. Sometimes the gut is quiet and the skin still needs separate treatment. Sometimes bowel and skin flare together as extraintestinal activity. Sometimes the “acne” is steroid-related and improves as the taper continues under supervision.

Infection risk deserves respect on immunosuppression. What looks like acne can occasionally be folliculitis or another infection. What looks like eczema can be superinfected. If lesions are warm, draining, or exquisitely tender, say so. Avoid borrowing someone else’s oral steroid cream pack without guidance, especially on the face.

Lifestyle supports are adjuncts, not cures: gentle cleansers, fragrance-light moisturizers, not picking, sun care that matches your photosensitivity risk, and nutrition adequate in protein and micronutrients while you heal. If you are exploring diet changes for skin, keep IBD realities in view—extreme elimination during active gut disease can backfire.

Ask your team these questions at the next contact: Is this a known reaction pattern for my medicine? Do I need dermatology now or watchful waiting? Could this be paradoxical inflammation, infection, steroid effect, or an extraintestinal manifestation? If we change therapy, what is the gut monitoring plan during the switch?

Related education: [Extraintestinal manifestations](/blog/ibd-extraintestinal-manifestations), [Pyoderma and erythema nodosum](/blog/pyoderma-erythema-nodosum-ibd), [Joint aches, eyes, and skin Q&A](/ask/joint-aches-eye-pain-skin-ibd), and [Understanding biologics](/blog/understanding-biologics-ibd).`
  },
  {
    id: 19,
    slug: 'j-pouch-ostomy-cure-or-inflammation-return',
    title: 'Does a J-pouch or ostomy cure IBD, or can inflammation return?',
    answer: `Surgery can be life-changing and medically necessary. It is not a magic eraser that guarantees “cured forever” for every person with inflammatory bowel disease. The honest answer depends on which disease you have, which operation you had, and what “cure” means to you—no more colon, no more symptoms, or no chance of future inflammation anywhere.

Ulcerative colitis primarily affects the colon and rectum. When the entire colon and rectum are removed, the original UC disease target is gone. Many people do extremely well after restorative proctocolectomy with ileal pouch–anal anastomosis (J-pouch) or after a permanent ileostomy. That said, pouches can develop pouchitis—inflammation of the pouch—with urgency, frequency, and discomfort that feel painfully familiar. Some people develop cuffitis in remaining rectal tissue. A smaller group is later recognized as Crohn’s disease of the pouch when the pattern does not behave like simple pouchitis. So even after “the colon is gone,” inflammation can still need antibiotics, advanced therapy, or further procedures. Calling UC surgery a cure is shorthand that leaves out pouchitis and quality-of-life work.

Crohn’s disease can involve any part of the GI tract. Removing a diseased segment—or diverting stool with an ostomy—treats complications like obstruction, abscess, fistula, or refractory colitis. It does not remove the immune tendency that defines Crohn’s. Inflammation can return at the anastomosis, in the small bowel, in the perineum, or elsewhere. Ostomy surgery can dramatically improve life when disease or complications demand it, and many people thrive with a stoma. It is still Crohn’s afterward, which means ongoing surveillance, medication decisions, and nutrition planning remain part of care for a large share of patients.

What should you ask before surgery so expectations are clear? What is the primary goal—cancer risk, refractory bleeding, dysplasia, toxic colitis, stricture, fistula, or medication failure? Is the plan a temporary diversion, a permanent stoma, or a pouch reconstruction in stages? What are pouchitis rates and Crohn’s-of-the-pouch discussions in your center’s experience? Who will manage pouch care long term? What sexual function, fertility, body-image, and return-to-work counseling is available? Surgery teams that answer these without hype are doing you a favor.

After a J-pouch, learn the difference between expected adaptation and warning signs. Early months often mean frequent stools while the pouch learns capacity. Escalating blood, night accidents that worsen after a stable baseline, fever, dehydration, or obstruction symptoms need prompt contact. After an ostomy, learn appliance fit, high-output rules, skin care, and when output volume or consistency changes signal dehydration or active disease. High-output ileostomy is a medical issue, not a personal failure at “getting used to it.”

Medications after surgery are not a moral judgment. Some people need prophylaxis or continued advanced therapy based on risk factors. Others step down under close watch. Do not stop medicines because surgery “should have finished this.” Confirm the plan in writing: who checks calprotectin, who scopes the pouch, who adjusts therapy if pouchitis repeats.

Emotionally, the word “cure” can create loneliness when symptoms persist. You are not ungrateful for wanting relief and still needing care. Peer ostomy and pouch nurses, wound-ostomy-continence specialists, and IBD mental health support help as much as surgical technique for long-term living.

If you are deciding between pouch and permanent ostomy, there is no universal winner. Body anatomy, sphincter function, prior surgeries, fertility plans, and personal preference all matter. Second opinions at high-volume IBD surgery centers are reasonable for big irreversible choices.

Related education: [J-pouch basics](/blog/j-pouch-basics-ibd), [Ostomy basics](/blog/ostomy-basics-ibd), [ICN pediatric ostomy toolkit](/blog/icn-ostomy-toolkit-pediatric), and [Swimming and activity with an ostomy](/blog/swimming-pool-beach-ibd-ostomy).`
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

  for (const item of ITEMS) {
    const len = item.answer.length;
    const words = wordCount(item.answer);
    if (len < 40 || len > 12000) {
      throw new Error(`Answer length out of range for #${item.id} ${item.slug}: ${len} chars`);
    }
    const existing = await client.query(
      `SELECT question_id, status, question_text
       FROM ibdpal_reader_questions WHERE question_id = $1`,
      [item.id]
    );
    if (!existing.rows.length) {
      throw new Error(`Missing question_id ${item.id}`);
    }
    const result = await client.query(
      `UPDATE ibdpal_reader_questions
       SET title = $2,
           answer_text = $3,
           slug = $4,
           status = 'answered',
           published_at = COALESCE(published_at, NOW()),
           updated_at = NOW()
       WHERE question_id = $1
       RETURNING question_id, slug, status, published_at`,
      [item.id, item.title, item.answer, item.slug]
    );
    const row = result.rows[0];
    console.log(
      JSON.stringify({
        id: row.question_id,
        slug: row.slug,
        status: row.status,
        published_at: row.published_at,
        chars: len,
        words,
        approx_min_read: Math.round((words / 220) * 10) / 10,
        url: `/ask/${row.slug}`
      })
    );
  }

  const counts = await client.query(
    `SELECT status, COUNT(*)::int AS n FROM ibdpal_reader_questions GROUP BY status ORDER BY n DESC`
  );
  const pending = await client.query(
    `SELECT COUNT(*)::int AS n FROM ibdpal_reader_questions WHERE status = 'new'`
  );
  console.log('counts', JSON.stringify(counts.rows));
  console.log('remaining_new', pending.rows[0].n);
  await client.end();
})().catch((err) => {
  console.error(err);
  process.exit(1);
});
