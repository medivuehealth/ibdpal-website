"""Unique Oct 11 2026 SEO gap blog bodies."""
from __future__ import annotations

from importlib import import_module

BODY_MODULES: dict[str, str] = {
    "ulcerative-colitis-diet-overview-ibd": "oct11_seo_bodies.ulcerative_colitis_diet",
    "cded-crohns-exclusion-diet-ibd": "oct11_seo_bodies.cded",
    "specific-carbohydrate-diet-scd-ibd": "oct11_seo_bodies.scd",
    "ibd-colon-cancer-risk-surveillance": "oct11_seo_bodies.colon_surveillance",
    "smoking-ibd-crohns-colitis": "oct11_seo_bodies.smoking",
    "disability-fmla-work-ibd": "oct11_seo_bodies.disability_fmla",
    "running-jogging-ibd": "oct11_seo_bodies.running",
    "spicy-foods-nuts-seeds-ibd": "oct11_seo_bodies.spicy_nuts",
}


def build_body(slug: str) -> str:
    mod_name = BODY_MODULES[slug]
    mod = import_module(mod_name)
    return mod.body()
