# Product Ideas Backlog

## Global Guardrails for Health Tools

### Strict Non-Diagnostic Disclaimer
- Do not tell a user they "have" Crohn's disease, ulcerative colitis, IBD, or any other condition.
- Market these tools as management aids, symptom loggers, educational trackers, or clinician-conversation aids.
- Use language like "possible pattern," "symptom trend," "baseline change," or "worth discussing with your care team."
- Avoid diagnostic, predictive-certainty, or treatment-decision language.

### Data Privacy & Security
- Health data is highly sensitive.
- If data is stored on a server, the product may need HIPAA, GDPR, and other privacy/security compliance review.
- For early prototypes or hobby projects, prefer anonymous/local-only tracking with browser `localStorage` or on-device storage.
- Do not collect unnecessary identifiers.
- Make it clear whether data stays on the device or is sent to a server.
- Avoid raw diary text, stool images, or detailed health logs in cloud storage unless there is a strong privacy model.

### Emergency Red Flags
- If a user enters severe symptoms, the tool should stop scoring or analysis and show a prominent urgent-care message.
- Red flags include high fever, persistent or heavy bleeding, severe or unbearable abdominal pain, fainting, confusion, dehydration, rapid heartbeat, inability to keep fluids down, or black/tarry stool.
- The message should direct the user to contact their gastroenterologist, urgent care, emergency services, or local emergency number as appropriate.
- Red-flag handling should happen before any gamified score, risk label, or ML output is shown.

## Idea #1: The "Food Detective" Quest

### Concept
A mystery-themed portal where users log meals and symptoms to unmask their personal "culprit" foods. The experience should feel like a detective notebook rather than a chore-based food diary.

### Fun Elements
- Detective notebook visual style.
- "Suspect list" of foods, ingredients, meals, or patterns the user thinks may be linked to symptoms.
- Case-style language: clues, suspects, evidence, patterns, case notes.
- Gentle progress feedback for consistent logging.

### Possible Features
- Interactive suspect list where users rank foods they think may be causing issues.
- Meal and symptom timeline that surfaces co-occurrence patterns.
- "Evidence strength" labels that stay non-medical: weak, possible, worth discussing.
- Case notes for users to record context like stress, sleep, travel, medications, or flare status.
- Exportable summary for gastroenterology or dietitian visits.

### Feasibility
This is possible, but it should be scoped carefully because food-symptom correlation is not the same as diagnosis. The feature should avoid declaring foods as proven triggers. It should frame patterns as observations to discuss with a care team.

### Suggested Implementation Path
1. Prototype as a website demo or static interactive mockup.
2. Add a local-only "suspect ranking" UI with sample data.
3. Define safe language for pattern labels and disclaimers.
4. If the product direction feels right, bring the concept into the iOS app as a guided logging mode.
5. Add export support only after the data model is stable.

### Safety / Compliance Notes
- Do not label any food as definitively causing a flare.
- Include educational disclaimers and encourage clinician/dietitian review.
- Account for confounders: disease activity, medications, stress, sleep, infection, menstrual cycle, travel, and meal timing.
- Avoid encouraging overly restrictive diets.

## Idea #2: Natural Language Symptom & Mood Journal Miner

### Concept
A free-form daily journal where users write how they feel in plain language, such as "Tired, bloated, stressed about work." The system extracts symptom and mood signals from the text and turns them into structured trends.

### Model / Technical Direction
- Natural language processing for symptom and mood extraction.
- Possible approaches:
  - Lightweight rules and keyword dictionaries for an early prototype.
  - Sentiment analysis for general emotional tone.
  - Transformer models (for example, BERT-style variants) for more advanced entity extraction.
  - On-device inference where possible to reduce privacy risk.

### Possible Outputs
- Extracted symptom entities: pain, fatigue, bloating, urgency, nausea, blood, appetite, sleep.
- Extracted mood/stress signals: anxiety, sadness, irritability, overwhelm, work/school stress.
- Daily summary cards: "You mentioned fatigue 4 times this week" or "Stress language increased before symptom-heavy days."
- Timeline overlays comparing journal tone with logged stool frequency, pain, sleep, and meals.
- Exportable journal trend summary for clinicians, without raw diary text by default.

### Feasibility
This is possible, but should start simple. A rules-based prototype is safer and more explainable than a black-box model. Advanced NLP can be added after the data model, privacy approach, and safety language are stable.

### Suggested Implementation Path
1. Prototype a local journal textbox with manual tags and optional suggested tags.
2. Add simple keyword extraction for common IBD symptoms and mood words.
3. Let users confirm or edit extracted tags before saving.
4. Add weekly trend summaries that avoid diagnosis or causal claims.
5. Explore on-device NLP for privacy-preserving entity extraction.
6. Only later consider server-side or transformer-based NLP if there is a strong privacy and consent model.

### Safety / Compliance Notes
- Do not claim to "prove" the brain-gut connection for an individual user.
- Use cautious language: "may be associated," "appears near," "worth discussing."
- Mood analysis can be sensitive; avoid mental health diagnosis.
- Provide crisis-resource language if users write self-harm or severe distress terms.
- Treat raw journal text as highly sensitive health data.
- Prefer user-confirmed tags and summaries over storing or exporting raw diary text.
- Be transparent about whether processing happens on-device or on a server.

## Idea #3: NLM Clinical Tables Condition Search

### Concept
Use the National Library of Medicine (NLM) Clinical Table Search Service to power autocomplete for symptoms, conditions, and clinical terms in IBDPal interfaces. Example entries could include "ulcerative colitis," "Crohn's disease," "diarrhea," "abdominal pain," and related condition names.

### Source / API
- Service: Clinical Table Search Service (CTSS), hosted by NLM.
- Conditions API base URL: `https://clinicaltables.nlm.nih.gov/api/conditions/v3/search`
- Minimum query parameter: `terms`
- Useful optional parameters:
  - `maxList` to limit results.
  - `sf` to specify searchable fields.
  - `df` to specify display fields.
  - `ef` to retrieve extra fields such as codes/text mappings.

### Possible Features
- Condition/symptom autocomplete in onboarding, profile setup, journal tagging, and symptom logs.
- Cleaner user-entered terminology by suggesting standard names.
- Optional display of mapped condition metadata when available.
- Local "recently used" terms so users can repeat common entries quickly.
- IBD-focused quick picks that sit above API results: Crohn's disease, ulcerative colitis, diarrhea, urgency, abdominal pain, fatigue, bloating.

### Feasibility
This is highly feasible as a web or app integration. The API is public and designed for autocomplete. It should still be wrapped carefully so the app does not feel like it is diagnosing or coding the user's condition.

### Suggested Implementation Path
1. Prototype a simple search box using the conditions endpoint.
2. Debounce requests and require at least 2-3 characters before querying.
3. Add a small curated IBD quick-pick list before external results.
4. Cache recent selections locally for speed and privacy.
5. Store selected display labels, not necessarily full API payloads.
6. Add fallback behavior if the NLM service is unavailable.

### Safety / Compliance Notes
- Label this as terminology lookup/autocomplete, not diagnosis.
- Avoid showing billing/coding language prominently to patients unless needed.
- Do not imply that a selected condition has been clinically confirmed.
- If used in symptom logging, separate "symptoms I feel" from "diagnoses confirmed by my clinician."
- Review NLM/Clinical Tables terms before production use and avoid overloading the public service with aggressive request rates.

## Idea #4: Gamified Flare-Risk and Symptom Pattern Lab

### Concept
An online, interactive flare-risk and symptom-pattern experience for people with known or suspected IBD symptoms. The tool should not tell users they "have IBD," Crohn's disease, or ulcerative colitis. Instead, it should help users understand symptom patterns, track flare warning signs, and know when to seek medical evaluation.

### Product Positioning
- Management aid for diagnosed patients.
- Educational symptom tracker for undiagnosed users.
- Pattern-awareness tool, not diagnosis.
- Clinician-conversation starter.

### Gamified / Fun-Based Concepts

#### 1. Gut Weather Forecast
- Users enter daily symptoms, sleep, stress, medication adherence, food notes, and hydration.
- Output is a non-threatening "gut weather" report, such as "Sunny," "Cloudy," or "Storm watch."
- Fun UI: clouds, sunshine, rain, lightning, weekly forecast cards.
- Safe language: "Your recent logs suggest a rougher day may be possible," not "you will flare."

#### 2. Tamagotchi-Style Virtual Organ
- A retro digital pet represents gut wellness habits.
- Hydration, sleep, medication reminders, gentle meals, and tracking keep the avatar calm or glowing.
- Stress, skipped logs, poor sleep, or symptom-heavy days make the avatar tired or cranky.
- Rewards: streaks, badges, gentle reminders.
- Avoid shame-based design; the avatar should never punish users for being sick.

#### 3. Food Detective Quest
- Already captured as Idea #1.
- Can be part of this larger "Pattern Lab" umbrella.

### ML-Based Concepts

#### 1. Biomarker and Wearable Sync Engine
- Possible model types: time-series anomaly detection, LSTM/RNN, simpler baseline deviation rules for MVP.
- Inputs: Apple Health/Fitbit sleep, resting heart rate, step count, temperature trends, HRV if available.
- Output: "baseline shift" or "recovery strain" indicators.
- Safer MVP: rules-based anomaly detection before complex neural models.

#### 2. Stool and Bristol Scale Classifier
- Possible model type: CNN/image classifier.
- Privacy risk is very high because stool images are sensitive.
- Safer alternative: interactive Bristol Stool Scale slider or illustrated selector.
- If image classification is ever used, prefer on-device processing and do not upload images by default.

#### 3. Natural Language Symptom and Mood Journal Miner
- Already captured as Idea #2.
- Can feed into flare-risk summaries if users consent.

#### 4. Multi-Factor Flare Probability Calculator
- Possible model types: Random Forest, XGBoost, calibrated logistic regression.
- Inputs: stool frequency, blood, pain, urgency, fever, missed medication, sleep, stress, joint pain, appetite, hydration.
- Output should be tiered and cautious: "low concern," "watch closely," "contact your care team," "urgent red flags."
- Avoid exact percentages unless validated on a suitable dataset.

### Free / Low-Cost Technical Options
- Frontend prototype: Streamlit, Gradio, or React/Tailwind.
- ML hosting/prototyping: Hugging Face Spaces, local browser inference, or lightweight FastAPI on Render/Railway.
- Data standards/autocomplete: NLM Clinical Tables API (see Idea #3).
- Text extraction: simple rules first, then BioBERT/clinical transformer experiments only after privacy review.
- Classic ML: scikit-learn Random Forest, XGBoost, or logistic regression for local experiments.

### Data / Model Reality Check
There is no free, validated API that can diagnose Crohn's disease, ulcerative colitis, or IBD from symptoms. Public models and Hugging Face tools can support NLP, coding, and classification experiments, but they should not be used as medical diagnosis engines. Any flare-risk model needs validation, calibration, disclaimers, and red-flag handling.

### Suggested Implementation Path
1. Build a local-only rules-based MVP: symptom questionnaire + gut weather output.
2. Add red-flag interruption before any score is shown.
3. Add local history so users can compare today with their own baseline.
4. Add clinician-friendly export.
5. Add wearable data only after privacy and consent design is complete.
6. Experiment with ML after enough safe, user-consented, structured data exists.
7. Keep all outputs educational until clinically validated.

### Critical Medical Guardrails
- Never tell a user they have Crohn's, UC, or IBD.
- Never tell a diagnosed user they are definitely entering a flare.
- Stop scoring and show urgent guidance for severe symptoms: heavy bleeding, high fever, severe pain, dehydration, fainting, confusion, or inability to keep fluids down.
- Store health data locally unless there is a clear HIPAA/GDPR-grade privacy model.
- Avoid collecting stool photos unless absolutely necessary.
- Use "possible pattern," "baseline change," and "worth discussing" language.
- Include a clear disclaimer: for education and tracking only; not medical advice, diagnosis, or treatment.


