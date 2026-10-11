#!/usr/bin/env python3
"""Write oct11_seo_bodies/*.py with unique long form content. Run once from scripts/."""
from __future__ import annotations

from pathlib import Path

OUT = Path(__file__).resolve().parent / "oct11_seo_bodies"

HEADER = '''from oct11_seo_bodies._html import assemble, related


def body() -> str:
    intro = {intro!r}
    sections = {sections!r}
    return assemble(
        intro,
        sections,
        clinic_quote={clinic!r},
        faqs={faqs!r},
        related_html=related(
{related}
        ),
        closing={closing!r},
    )
'''


def rel(*pairs: tuple[str, str]) -> str:
    lines = []
    for label, href in pairs:
        lines.append(f'            ("{label}", "{href}"),')
    return "\n".join(lines)


# Each post: intro, sections list of (h2, [paras...]), clinic, faqs, related, closing


def write(name: str, **kwargs) -> None:
    text = HEADER.format(
        intro=kwargs["intro"],
        sections=kwargs["sections"],
        clinic=kwargs["clinic"],
        faqs=kwargs["faqs"],
        related=rel(*kwargs["related"]),
        closing=kwargs.get("closing", []),
    )
    (OUT / name).write_text(text, encoding="utf-8")
    print("wrote", name)


def para(*parts: str) -> str:
    return " ".join(parts)


if __name__ == "__main__":
    # ulcerative colitis already hand written; others below
    write(
        "cded.py",
        intro=(
            "The <strong>Crohn's Disease Exclusion Diet (CDED)</strong> is a research protocol that "
            "combines defined food exclusions with partial enteral nutrition for some Crohn's disease "
            "patients. Social media often strips away the supervision, formula math, and lab monitoring "
            "that make the protocol meaningful. This page explains phases, typical exclusions, PEN basics, "
            "and why CDED is not a home cure. Ulcerative colitis readers may compare options here but "
            "should not assume identical protocols. Education only."
        ),
        sections=[
            (
                "Where CDED came from and who it targets",
                [
                    para(
                        "CDED grew from pediatric Crohn's research asking whether specific dietary components ",
                        "plus formula support could calm inflammation alongside standard medicines. Adult programs ",
                        "exist at some centers but availability varies by city and insurance.",
                    ),
                    para(
                        "The diet is designed for Crohn's disease phenotypes under gastroenterology and dietitian ",
                        "oversight. Copying exclusion lists without PEN guidance can underfeed growing teens and ",
                        "frustrate adults who need adequate protein during active small bowel inflammation.",
                    ),
                    para(
                        "Ask whether your inflammation pattern matches studied populations before investing in ",
                        "expensive specialty groceries that your team never endorsed.",
                    ),
                ],
            ),
            (
                "Phase structure in everyday language",
                [
                    para(
                        "Early weeks usually pair strict permitted food lists with a prescribed formula that ",
                        "delivers part of daily calories. Later weeks widen allowed whole foods while symptoms, ",
                        "weight, and labs are tracked.",
                    ),
                    para(
                        "Exact calendars belong on your clinic handout, not a blog chart. Some centers adjust ",
                        "duration based on calprotectin, growth curves in children, or tolerance to formula volume.",
                    ),
                    para(
                        "Stopping early because social events feel hard can waste the effort already invested; ",
                        "message your dietitian about temporary bridges rather than quitting silently.",
                    ),
                ],
            ),
            (
                "What categories are typically excluded",
                [
                    para(
                        "Protocols commonly limit certain emulsifiers, thickeners, ultra processed snacks, and ",
                        "selected grains or dairy forms named in the official manual your team provides.",
                    ),
                    para(
                        "Permitted lists still include fruits, vegetables, proteins, and fats with portion ",
                        "guidance. The point is structure, not starvation.",
                    ),
                    para(
                        "Ingredient labels become homework. Restaurant meals are difficult during strict phases; ",
                        "plan simple home cooking windows when possible.",
                    ),
                ],
            ),
            (
                "Partial enteral nutrition without jargon walls",
                [
                    para(
                        "Partial enteral nutrition means a medical formula supplements meals you still eat from ",
                        "the allowed list. Volume and timing affect nausea, stool output, and adherence.",
                    ),
                    para(
                        "Formulas differ in osmolality, fiber content, and lactose. Swapping brands because a ",
                        "friend liked another can cause cramping or off labs.",
                    ),
                    para(
                        "Tube feeding variants exist for patients who cannot drink enough volume orally; that ",
                        "path is hospital managed, not a vlog tutorial.",
                    ),
                ],
            ),
            (
                "Supervision, labs, and growth monitoring",
                [
                    para(
                        "Expect weight checks, height velocity in kids, vitamin D, iron studies, and inflammatory ",
                        "markers on a schedule. Restrictive phases can drop calcium, zinc, or fiber intake without ",
                        "anyone noticing until labs flag it.",
                    ),
                    para(
                        "Dietitians adjust formula volume when school schedules, sports, or shift work block daytime ",
                        "drinking windows.",
                    ),
                    para(
                        "Mental health matters during restrictive trials. Screen for disordered eating patterns ",
                        "especially in adolescents who already feel body shame from IBD.",
                    ),
                ],
            ),
            (
                "CDED compared with Mediterranean eating",
                [
                    para(
                        "Mediterranean style patterns emphasize olive oil, fish, legumes, and whole grains with ",
                        "flexibility that many adults prefer in long remission.",
                    ),
                    para(
                        "CDED is more rigid early and tied to formula protocols. Compare goals: induction support ",
                        "versus lifelong variety.",
                    ),
                    para(
                        "Some patients use Mediterranean meals after supervised reintroduction while others never ",
                        "needed CDED at all.",
                    ),
                ],
            ),
            (
                "CDED compared with low FODMAP trials",
                [
                    para(
                        "Low FODMAP targets fermentable carbohydrates for symptom relief and uses systematic ",
                        "reintroduction. It is not the same additive exclusion focus as CDED.",
                    ),
                    para(
                        "Running both experiments at once blames the wrong foods when symptoms shift. Sequential ",
                        "trials with professional oversight prevent chaos.",
                    ),
                    para(
                        "See <a href=\"/blog/fodmap-diet-crohns-colitis\">FODMAP overview</a> for parallel reading.",
                    ),
                ],
            ),
            (
                "Who should not self start CDED",
                [
                    para(
                        "History of eating disorders, severe malnutrition, unstable flares, complex strictures, ",
                        "pregnancy, or breastfeeding requires individualized medical nutrition therapy first.",
                    ),
                    para(
                        "Patients awaiting surgery may need pre op optimization rather than sudden exclusion phases.",
                    ),
                    para(
                        "If you cannot afford formula copays, tell the team before day one so social work can help.",
                    ),
                ],
            ),
            (
                "Medicines still anchor treatment",
                [
                    para(
                        "CDED studies run alongside immunomodulators, biologics, and steroids when clinicians ",
                        "prescribe them. Diet does not automatically replace endoscopy proven healing.",
                    ),
                    para(
                        "Bring med changes to the dietitian so formula timing aligns with morning immunosuppression ",
                        "or post infusion nausea patterns.",
                    ),
                    para(
                        "Never stop IBD medicines because a blogger claimed diet alone cleared their skin photos.",
                    ),
                ],
            ),
            (
                "School, travel, and social life logistics",
                [
                    para(
                        "Pack labeled formula bottles, permission forms for nurses, and backup shelf stable options ",
                        "for bus trips.",
                    ),
                    para(
                        "Air travel may require medical letters for powder containers. Security rules change; carry ",
                        "prescription labels.",
                    ),
                    para(
                        "Friends do not need every detail, but hosts appreciate knowing you bring safe foods during ",
                        "strict weeks.",
                    ),
                ],
            ),
            (
                "When to pause and call the team",
                [
                    para(
                        "Vomiting, fainting, rapid weight loss, inability to keep formula down, or new severe pain ",
                        "needs same day outreach.",
                    ),
                    para(
                        "Psychological distress from food fear also counts as a reason to regroup with behavioral ",
                        "health support.",
                    ),
                    para(
                        "Use <a href=\"/flare-help\">flare help</a> for escalation paths your clinic published.",
                    ),
                ],
            ),
            (
                "Transitioning off strict phases",
                [
                    para(
                        "Reintroduction should be intentional: one new category at a time with symptom logs and ",
                        "scheduled visits rather than a holiday buffet.",
                    ),
                    para(
                        "Some foods remain optional long term if they never improved symptoms or labs.",
                    ),
                    para(
                        "Celebrate expanded variety without guilt about foods that still disagree with your gut.",
                    ),
                ],
            ),
            (
                "Insurance and formula coverage tips",
                [
                    para(
                        "Ask for prescription documentation and diagnosis codes early. Some plans treat formula as ",
                        "durable medical equipment while others need prior authorization.",
                    ),
                    para(
                        "Keep denial letters for appeals; gastroenterology offices often have template letters.",
                    ),
                    para(
                        "Manufacturer assistance programs exist for qualifying households; social workers know the ",
                        "phone numbers.",
                    ),
                ],
            ),
            (
                "Recording progress for clinic visits",
                [
                    para(
                        "Track formula volume, permitted meals, stool count, pain scores, and school or work absences.",
                    ),
                    para(
                        "Photos of labels help dietitians spot hidden emulsifiers you missed.",
                    ),
                    para(
                        "IBDPal logs can sit beside formula intake so providers see food and symptoms together.",
                    ),
                ],
            ),
        ],
        clinic=(
            "Is CDED appropriate for my Crohn's phenotype? If yes, who prescribes PEN, which formula fits "
            "my needs, and what labs will we track during each phase?"
        ),
        faqs=[
            (
                "Can CDED replace biologics?",
                "No. CDED is studied with standard IBD care, not as a guaranteed substitute for medicines your GI prescribed.",
            ),
            (
                "Can adults start CDED without a pediatric team?",
                "Some adult centers offer protocols. Ask an IBD dietitian whether a local supervised pathway exists.",
            ),
            (
                "Is CDED the same as SCD?",
                "No. Specific Carbohydrate Diet uses different rules and evidence. Compare separately with professionals.",
            ),
            (
                "What if I hate the formula taste?",
                "Flavor trials, temperature changes, and straw pacing help some people. Ask before abandoning prescribed volume.",
            ),
        ],
        related=(
            ("Crohn's diet overview", "/blog/crohns-diet-overview-ibd"),
            ("Mediterranean diet notes", "/blog/mediterranean-diet-autoimmune"),
            ("SCD overview", "/blog/specific-carbohydrate-diet-scd-ibd"),
            ("IBD nutrition hub", "/ibd-nutrition"),
        ),
        closing=[
            "CDED is a tool some Crohn's teams use with clear start and stop rules. It is not a moral test of willpower. ",
            "If the protocol fights your life, ask about alternatives rather than suffering alone.",
        ],
    )

    print("Done partial build; extend script for remaining posts.")
