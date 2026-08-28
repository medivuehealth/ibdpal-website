"""Two additional h2 sections per slug to reach append word targets."""
from __future__ import annotations

EXTRA_SECTIONS: dict[str, list[tuple[str, list[str]]]] = {}

def E(slug, s1, s2):
    EXTRA_SECTIONS[slug] = [s1, s2]

E("partner-caregiver-ibd",
  ("Navigating infusion and procedure days together", [
      "Infusion appointments can last hours. Bring snacks, chargers, and a quiet activity for yourself if you attend. Ask the nurse what reactions to watch for so you can alert staff confidently.",
      "After colonoscopy or surgery, follow written discharge instructions about diet and activity. Do not interpret vague social media advice when hospital papers conflict.",
      "Keep a shared folder of insurance cards, prior authorization numbers, and pharmacy contacts so the patient is not alone during billing surprises.",
  ]),
  ("Long-term partnership resilience with chronic illness", [
      "Schedule date nights or friend time that is not about IBD quarterly. Relationships need joy unrelated to clinics to stay strong over decades.",
      "If you disagree about treatment choices, defer to the patient and their licensed clinicians rather than debating in front of extended family.",
      "Consider couples counseling when medical stress repeats the same arguments. Therapy is maintenance for caregivers too, not a sign of failure.",
  ]))

E("stress-autoimmune-symptoms",
  ("Sleep and circadian rhythm as stress medicine", [
      "Poor sleep amplifies pain sensitivity and next-day urgency for many IBD patients. Fixed wake times, dim screens before bed, and morning light exposure help more than occasional sleep-in days.",
      "Night sweats or frequent bathroom trips deserve medical review rather than assuming they are only anxiety. Treating inflammation sometimes improves sleep indirectly.",
      "Discuss melatonin or prescription sleep aids with your clinician if insomnia persists beyond two weeks during stable disease.",
  ]),
  ("Building a flare-season stress plan", [
      "Before exam periods or holidays, write a one-page plan listing who to call, safe foods, and rest breaks. Predictable structure lowers cortisol when symptoms are unpredictable.",
      "Delegate one non-medical task weekly to a partner or friend so your energy budget includes recovery, not only obligations.",
      "Return to this plan after stressful events and note what helped. Your GI team can reinforce successful coping at follow-up visits.",
  ]))

# Auto-load remaining extensions
from _batch1_extra_sections_rest import register  # noqa: E402
register(E)
