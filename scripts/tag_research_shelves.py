#!/usr/bin/env python3
"""Tag research sources into Sources vs Research Publications shelves; add CCF + Wave 2 pubs."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "data" / "research-sources.json"

PUBLICATION_HINTS = (
    "pubmed",
    "pmc",
    "nature",
    "lancet",
    "nejm",
    "journal",
    "congress",
)

NEW_SOURCES = [
    {
        "id": "ccf-patients-caregivers",
        "title": "Crohn's & Colitis Foundation: Patients and Caregivers",
        "publisher": "Crohn's & Colitis Foundation",
        "year": "Patient education",
        "url": "https://www.crohnscolitisfoundation.org/patientsandcaregivers",
        "topics": ["Foundation", "patient education", "support", "IBD"],
        "summary": "Foundation patient and caregiver education hub covering disease basics, diet, support programs, and navigating care. Selected Foundation Marks and education appear on IBDPal under license; the Foundation does not endorse IBDPal.",
        "license_note": "Selected Foundation content and Marks used on IBDPal under license. Link to originals; logo unmodified. No endorsement claim.",
        "shelf": "sources",
    },
    {
        "id": "ccf-what-is-ibd",
        "title": "Crohn's & Colitis Foundation: What is IBD?",
        "publisher": "Crohn's & Colitis Foundation",
        "year": "Patient education",
        "url": "https://www.crohnscolitisfoundation.org/what-is-ibd",
        "topics": ["IBD basics", "Crohn's", "ulcerative colitis", "Foundation"],
        "summary": "Foundation overview of inflammatory bowel disease for patients and families. Use as a trusted education starting point beside clinic advice.",
        "license_note": "Foundation education under license on IBDPal where selected; always prefer current Foundation pages as originals.",
        "shelf": "sources",
    },
    {
        "id": "ccf-diet-nutrition",
        "title": "Crohn's & Colitis Foundation: Diet and Nutrition",
        "publisher": "Crohn's & Colitis Foundation",
        "year": "Patient education",
        "url": "https://www.crohnscolitisfoundation.org/patientsandcaregivers/ibd-and-you/diet-and-nutrition",
        "topics": ["diet", "nutrition", "Foundation", "IBD"],
        "summary": "Foundation diet and nutrition education for IBD. Pair with dietitian care; diet does not replace medication for inflammation.",
        "license_note": "Link and attribute Foundation pages. Do not mirror full Foundation site content.",
        "shelf": "sources",
    },
    {
        "id": "pubmed-lupus",
        "title": "Systemic Lupus Erythematosus Research (PubMed)",
        "publisher": "PubMed / National Library of Medicine",
        "year": "Research literature",
        "url": "https://pubmed.ncbi.nlm.nih.gov/?term=systemic+lupus+erythematosus",
        "topics": ["lupus", "SLE", "autoimmune", "research"],
        "summary": "PubMed gateway for peer-reviewed SLE research. Use with clinician interpretation; IBDPal summarizes themes only.",
        "license_note": "Link to PubMed; do not scrape paywalled PDFs.",
        "shelf": "publications",
    },
    {
        "id": "pubmed-rheumatoid-arthritis",
        "title": "Rheumatoid Arthritis Research (PubMed)",
        "publisher": "PubMed / National Library of Medicine",
        "year": "Research literature",
        "url": "https://pubmed.ncbi.nlm.nih.gov/?term=rheumatoid+arthritis",
        "topics": ["rheumatoid arthritis", "autoimmune", "joints", "research"],
        "summary": "Literature entry point for RA pathogenesis, therapeutics, and comorbidity research.",
        "license_note": "Link and summarize; respect journal copyright.",
        "shelf": "publications",
    },
    {
        "id": "pubmed-hashimotos",
        "title": "Hashimoto's Thyroiditis Research (PubMed)",
        "publisher": "PubMed / National Library of Medicine",
        "year": "Research literature",
        "url": "https://pubmed.ncbi.nlm.nih.gov/?term=hashimoto+thyroiditis",
        "topics": ["Hashimoto's", "thyroid", "autoimmune", "research"],
        "summary": "PubMed listings on autoimmune thyroiditis diagnosis and management themes.",
        "license_note": "Link only; no full-text hosting.",
        "shelf": "publications",
    },
    {
        "id": "pubmed-autoimmune-diet",
        "title": "Diet and Autoimmune Disease Research (PubMed)",
        "publisher": "PubMed / National Library of Medicine",
        "year": "Research literature",
        "url": "https://pubmed.ncbi.nlm.nih.gov/?term=diet+autoimmune+disease",
        "topics": ["diet", "autoimmune", "nutrition research", "Mediterranean diet"],
        "summary": "Research gateway for diet interventions and observational nutrition studies across autoimmune conditions.",
        "license_note": "Link to PubMed records; verify publisher licenses for reuse.",
        "shelf": "publications",
    },
    {
        "id": "medlineplus-lupus",
        "title": "Lupus",
        "publisher": "MedlinePlus, National Library of Medicine",
        "year": "Health topic",
        "url": "https://medlineplus.gov/lupus.html",
        "topics": ["lupus", "autoimmune", "MedlinePlus"],
        "summary": "Government health topic page on lupus symptoms, diagnosis themes, and treatments for patient-friendly reading.",
        "license_note": "MedlinePlus summaries are public domain; linked partner content may be copyrighted.",
        "shelf": "sources",
    },
    {
        "id": "medlineplus-ra",
        "title": "Rheumatoid Arthritis",
        "publisher": "MedlinePlus, National Library of Medicine",
        "year": "Health topic",
        "url": "https://medlineplus.gov/rheumatoidarthritis.html",
        "topics": ["rheumatoid arthritis", "joints", "MedlinePlus"],
        "summary": "MedlinePlus RA hub for definitions, treatments, and related genetics resources.",
        "license_note": "MedlinePlus summaries are public domain; verify linked encyclopedia licenses.",
        "shelf": "sources",
    },
]


def infer_shelf(src: dict) -> str:
    if src.get("shelf"):
        return src["shelf"]
    blob = " ".join(
        [
            src.get("id", ""),
            src.get("publisher", ""),
            src.get("title", ""),
            " ".join(src.get("topics", [])),
        ]
    ).lower()
    if any(h in blob for h in PUBLICATION_HINTS):
        return "publications"
    if "webmd" in blob:
        return "sources"
    return "sources"


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    existing = {s["id"] for s in data["sources"]}
    for s in data["sources"]:
        s["shelf"] = infer_shelf(s)
    added = 0
    for src in NEW_SOURCES:
        if src["id"] not in existing:
            data["sources"].append(src)
            added += 1
        else:
            for s in data["sources"]:
                if s["id"] == src["id"]:
                    s["shelf"] = src.get("shelf", infer_shelf(s))
    data["title"] = (
        "IBD & Autoimmune Research Sources | Foundation, NIH, PubMed | IBDPal"
    )
    data["description"] = (
        "Trusted organizational sources (including Crohn's & Colitis Foundation, NIH, AGA) and research publication gateways "
        "(PubMed, journals) for IBD and autoimmune education."
    )
    data["h1"] = "Research sources and publications"
    data["intro"] = (
        "Organizational education sources and peer-reviewed publication gateways for Crohn's disease, ulcerative colitis, "
        "extraintestinal associations, and broader autoimmune topics. IBDPal links to originals and summarizes in patient-friendly language. Not medical advice."
    )
    PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    pubs = sum(1 for s in data["sources"] if s.get("shelf") == "publications")
    srcs = sum(1 for s in data["sources"] if s.get("shelf") != "publications")
    print(f"sources_total={len(data['sources'])} shelf_sources={srcs} shelf_pubs={pubs} added={added}")


if __name__ == "__main__":
    main()
