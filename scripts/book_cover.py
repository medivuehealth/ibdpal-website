"""Hardcover dust-jacket and case-wrap copy for Eating With IBD."""

from __future__ import annotations

from pathlib import Path

TRIM_WIDTH_IN = 6.0
TRIM_HEIGHT_IN = 9.0
INTERIOR_PAGE_ESTIMATE = 330
SPINE_WIDTH_IN_EST = 1.1

PUBLISHER_NAME = "MediVue Health Education"
PUBLISHER_IMPRINT = "An educational imprint of MediVue, a 501(c)(3) nonprofit organization"
PUBLISHER_LEGAL = "MediVue"
PUBLISHER_LOCATION = "North Carolina, USA"
PUBLISHER_EMAIL = "info@ibdpal.org"

AUTHOR_NAME = "Aryan Shashi Kumar"
AUTHOR_LINE = AUTHOR_NAME
AUTHOR_BYLINE = "Founder, MediVue"

ISBN_13_LABEL = "ISBN, assign at KDP upload (KDP ISBN or your own)"
PRICE_US = "US $34.95"
PRICE_CAN = "CAN $44.95"

BISAC_PRIMARY = "HEALTH & FITNESS / Diseases / Crohn's & Colitis"
BISAC_SECONDARY = "MEDICAL / Nutrition"

COVER_IMAGE_REL = "blogs/assets/gut-nutrition/ulcerative-colitis-crohns-nutrition_1.jpg"
COVER_IMAGE_ALT = "Balanced meal setup illustrating IBD nutrition"
COVER_IMAGE_CREDIT = "Unsplash License (free to use)"

NONPROFIT_LINE = PUBLISHER_IMPRINT

BACK_HEADLINE = "Clear nutrition guidance when IBD makes every meal complicated."

BACK_BLURB = """Living with Crohn's disease or ulcerative colitis can turn ordinary food decisions into difficult questions. What should change during a flare? How do you rebuild variety afterward? Which deficiencies matter? And how do you separate useful nutrition strategies from unnecessary restriction?

In Eating With IBD, Aryan Shashi Kumar, founder of the nonprofit MediVue, organizes carefully sourced IBD nutrition education into a practical reference for everyday use.

This is a patient-education guide, not a meal prescription or clinical handbook. Always personalize decisions with your gastroenterologist and IBD dietitian."""

BACK_BULLETS = [
    "Adapt eating during flares and remission",
    "Understand common nutrient deficiencies and laboratory basics",
    "Compare major IBD diet approaches honestly",
    "Navigate protein, fiber, hydration, and supplements",
    "Modify everyday and cultural foods based on tolerance",
    "Prepare better nutrition questions for your GI or dietitian",
    "Build a personal nutrition plan without chasing a universal \"IBD diet\"",
]

BACK_DISCLAIMER = (
    "This book is for educational purposes only. It does not provide medical advice, diagnosis, "
    "or treatment. Individual nutrition and medical decisions should be made with qualified "
    "healthcare professionals."
)

SPINE_TEXT = "Eating With IBD"
SPINE_AUTHOR = "Aryan Shashi Kumar"


def cover_image_path(root: Path) -> Path | None:
    path = root / COVER_IMAGE_REL
    return path if path.is_file() else None
