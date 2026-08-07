#!/usr/bin/env python3
"""Append research paper / society source cards for traffic wave 1."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "data" / "research-sources.json"

NEW_SOURCES = [
    {
        "id": "pubmed-eim-overview",
        "title": "Extraintestinal Manifestations of Inflammatory Bowel Disease (PubMed)",
        "publisher": "PubMed / National Library of Medicine",
        "year": "Review literature",
        "url": "https://pubmed.ncbi.nlm.nih.gov/?term=extraintestinal+manifestations+inflammatory+bowel+disease",
        "topics": ["extraintestinal manifestations", "joints", "skin", "eyes", "autoimmune overlap"],
        "summary": "PubMed search gateway for peer-reviewed literature on IBD extraintestinal manifestations. Use with your clinician to interpret individual papers; IBDPal links rather than republishing full texts.",
        "license_note": "PubMed records and linked publisher full texts have mixed copyright. Link and summarize; do not scrape paywalled PDFs.",
    },
    {
        "id": "pubmed-psc-ibd",
        "title": "Primary Sclerosing Cholangitis and IBD (PubMed)",
        "publisher": "PubMed / National Library of Medicine",
        "year": "Research literature",
        "url": "https://pubmed.ncbi.nlm.nih.gov/?term=primary+sclerosing+cholangitis+inflammatory+bowel+disease",
        "topics": ["PSC", "liver", "bile ducts", "ulcerative colitis"],
        "summary": "Literature entry point for PSC-IBD association, surveillance themes, and hepatology research. Patient decisions require specialist care, not abstract reading alone.",
        "license_note": "Link to PubMed records; respect publisher copyright for full articles.",
    },
    {
        "id": "pubmed-as-ibd",
        "title": "Ankylosing Spondylitis / Spondyloarthritis and IBD (PubMed)",
        "publisher": "PubMed / National Library of Medicine",
        "year": "Research literature",
        "url": "https://pubmed.ncbi.nlm.nih.gov/?term=ankylosing+spondylitis+inflammatory+bowel+disease",
        "topics": ["ankylosing spondylitis", "spondyloarthritis", "axial joints", "rheumatology"],
        "summary": "Peer-reviewed research on axial spondyloarthritis overlapping with Crohn's and ulcerative colitis, including shared therapy discussions in the literature.",
        "license_note": "Link and summarize; do not republish full journal PDFs.",
    },
    {
        "id": "pubmed-psoriasis-ibd",
        "title": "Psoriasis and Inflammatory Bowel Disease (PubMed)",
        "publisher": "PubMed / National Library of Medicine",
        "year": "Research literature",
        "url": "https://pubmed.ncbi.nlm.nih.gov/?term=psoriasis+inflammatory+bowel+disease",
        "topics": ["psoriasis", "skin", "immune overlap", "dermatology"],
        "summary": "Research listings on psoriasis-IBD comorbidity and shared inflammatory pathways. Useful for readers preparing dermatology or GI questions.",
        "license_note": "PubMed/publisher copyrights vary; link out only.",
    },
    {
        "id": "pubmed-celiac-ibd",
        "title": "Celiac Disease and IBD Overlap (PubMed)",
        "publisher": "PubMed / National Library of Medicine",
        "year": "Research literature",
        "url": "https://pubmed.ncbi.nlm.nih.gov/?term=celiac+disease+inflammatory+bowel+disease",
        "topics": ["celiac", "gluten", "screening", "nutrition"],
        "summary": "Literature on celiac-IBD coexistence and diagnostic sequencing before long gluten-free trials.",
        "license_note": "Link and summarize abstracts; full texts follow publisher licenses.",
    },
    {
        "id": "pubmed-vte-ibd",
        "title": "Venous Thromboembolism Risk in IBD (PubMed)",
        "publisher": "PubMed / National Library of Medicine",
        "year": "Research literature",
        "url": "https://pubmed.ncbi.nlm.nih.gov/?term=venous+thromboembolism+inflammatory+bowel+disease",
        "topics": ["thrombosis", "clot risk", "hospitalization", "flare"],
        "summary": "Research on elevated clot risk during IBD flares and hospitalizations. Supports patient awareness articles; emergency symptoms still need urgent care.",
        "license_note": "Link to PubMed; do not copy full papers.",
    },
    {
        "id": "pubmed-bone-ibd",
        "title": "Osteoporosis and Bone Disease in IBD (PubMed)",
        "publisher": "PubMed / National Library of Medicine",
        "year": "Research literature",
        "url": "https://pubmed.ncbi.nlm.nih.gov/?term=osteoporosis+inflammatory+bowel+disease+vitamin+D",
        "topics": ["osteoporosis", "vitamin D", "steroids", "bone health"],
        "summary": "Peer-reviewed work on bone density, vitamin D, and corticosteroid exposure in Crohn's and colitis.",
        "license_note": "Link and summarize; respect journal copyright.",
    },
    {
        "id": "pubmed-diet-therapy-ibd",
        "title": "Diet Therapy and Nutrition Trials in IBD (PubMed)",
        "publisher": "PubMed / National Library of Medicine",
        "year": "Research literature",
        "url": "https://pubmed.ncbi.nlm.nih.gov/?term=diet+therapy+inflammatory+bowel+disease+randomized",
        "topics": ["diet therapy", "nutrition trials", "enteral nutrition", "Mediterranean diet"],
        "summary": "Entry point to diet and nutrition intervention studies in IBD, including enteral nutrition and patterned diets studied in trials.",
        "license_note": "Link to PubMed records; no full-text scraping.",
    },
    {
        "id": "pmc-eim-open",
        "title": "PMC Open-Access IBD Extraintestinal Reviews",
        "publisher": "PubMed Central (NIH)",
        "year": "Open-access corpus",
        "url": "https://www.ncbi.nlm.nih.gov/pmc/?term=extraintestinal+manifestations+IBD",
        "topics": ["open access", "EIM", "patient education support"],
        "summary": "PubMed Central hosts open-access full texts when authors or journals deposit them. Prefer PMC when you need free full-text reading of EIM reviews.",
        "license_note": "Each PMC article has its own license (often CC). Check the article license before reuse beyond linking and short quotation.",
    },
    {
        "id": "niddk-psc",
        "title": "Primary Sclerosing Cholangitis Overview",
        "publisher": "NIDDK, National Institutes of Health",
        "year": "NIH health information",
        "url": "https://www.niddk.nih.gov/health-information/liver-disease/primary-sclerosing-cholangitis",
        "topics": ["PSC", "liver disease", "bile ducts", "NIH"],
        "summary": "NIDDK patient-facing overview of PSC symptoms, diagnosis themes, and care concepts, including IBD association context on NIH pages.",
        "license_note": "U.S. government public health information; verify notices before reusing graphics.",
    },
    {
        "id": "medlineplus-ankylosing",
        "title": "Ankylosing Spondylitis",
        "publisher": "MedlinePlus, National Library of Medicine",
        "year": "Health topic",
        "url": "https://medlineplus.gov/ankylosingspondylitis.html",
        "topics": ["ankylosing spondylitis", "axial arthritis", "genetics", "treatments"],
        "summary": "MedlinePlus hub for AS definitions, treatments, and related genetics resources that patients can read beside IBD joint education.",
        "license_note": "MedlinePlus summaries are public domain; some linked content is copyrighted.",
    },
    {
        "id": "medlineplus-psoriasis",
        "title": "Psoriasis",
        "publisher": "MedlinePlus, National Library of Medicine",
        "year": "Health topic",
        "url": "https://medlineplus.gov/psoriasis.html",
        "topics": ["psoriasis", "skin", "immune disease", "treatments"],
        "summary": "Government health topic page on psoriasis symptoms and treatments for readers exploring skin-gut immune overlap.",
        "license_note": "MedlinePlus summaries are public domain; linked partner content may be copyrighted.",
    },
    {
        "id": "medlineplus-celiac",
        "title": "Celiac Disease",
        "publisher": "MedlinePlus, National Library of Medicine",
        "year": "Health topic",
        "url": "https://medlineplus.gov/celiacdisease.html",
        "topics": ["celiac disease", "gluten", "nutrition", "screening"],
        "summary": "MedlinePlus celiac overview covering testing and gluten-free diet basics useful before long elimination trials in IBD.",
        "license_note": "MedlinePlus summaries are public domain; verify linked encyclopedia licenses.",
    },
    {
        "id": "acg-ibd-guidelines",
        "title": "ACG IBD Clinical Guidelines Hub",
        "publisher": "American College of Gastroenterology",
        "year": "Society guidance",
        "url": "https://gi.org/guidelines/",
        "topics": ["clinical guidelines", "ACG", "Crohn's", "ulcerative colitis"],
        "summary": "ACG publishes clinician guidelines for IBD and related GI conditions. Patients can skim titles and discuss relevant recommendations with their gastroenterologist.",
        "license_note": "Professional society materials. Link and summarize; do not assume free republication rights.",
    },
    {
        "id": "aga-journals-ibd",
        "title": "AGA Journals: IBD Research and Clinical Updates",
        "publisher": "American Gastroenterological Association",
        "year": "Journal portfolio",
        "url": "https://gastro.org/journals/",
        "topics": ["AGA journals", "clinical research", "nutrition", "therapeutics"],
        "summary": "Gateway to AGA journal portfolios where clinicians publish IBD trials, nutrition updates, and practice guidance.",
        "license_note": "Journal copyright applies. Link to AGA; do not host PDFs.",
    },
    {
        "id": "nature-ibd-search",
        "title": "Nature Portfolio: Inflammatory Bowel Disease Research",
        "publisher": "Nature Portfolio",
        "year": "Research journal search",
        "url": "https://www.nature.com/search?q=inflammatory%20bowel%20disease",
        "topics": ["basic science", "translational research", "IBD mechanisms"],
        "summary": "Nature Portfolio search for IBD mechanistic and translational papers. Best used with clinician interpretation; many articles are paywalled.",
        "license_note": "Paywalled and open-access mix. Link only; no PDF hosting.",
    },
    {
        "id": "lancet-gastro-ibd",
        "title": "The Lancet Gastroenterology & Hepatology: IBD Topic Browse",
        "publisher": "The Lancet",
        "year": "Journal topic",
        "url": "https://www.thelancet.com/journals/langas/home",
        "topics": ["clinical trials", "gastroenterology", "hepatology", "IBD"],
        "summary": "Lancet specialty journal covering GI and liver clinical research, including IBD trials and reviews often discussed in academic clinics.",
        "license_note": "Publisher copyright. Link and short summary only.",
    },
    {
        "id": "nejm-ibd-search",
        "title": "NEJM: Inflammatory Bowel Disease Articles",
        "publisher": "New England Journal of Medicine",
        "year": "Journal search",
        "url": "https://www.nejm.org/search?q=inflammatory+bowel+disease",
        "topics": ["clinical medicine", "therapeutics", "landmark trials"],
        "summary": "NEJM search results for IBD clinical articles and reviews commonly cited in specialty care.",
        "license_note": "NEJM copyright. Link only; do not republish figures or full text.",
    },
]


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    data["title"] = (
        "IBD Research Sources | NIH, PubMed, AGA & Autoimmune Associations | IBDPal"
    )
    data["description"] = (
        "Trusted IBD research links: NIH/CDC, PubMed literature on extraintestinal and autoimmune associations, "
        "AGA/ACG guidance, and nutrition trial gateways. Education only."
    )
    data["h1"] = "IBD research and autoimmune association sources"
    data["intro"] = (
        "Government public health pages, society guidance, and publication gateways (PubMed, PMC, AGA, ACG, and major journals) "
        "for Crohn's disease, ulcerative colitis, extraintestinal manifestations, and related nutrition research. "
        "IBDPal links to originals and summarizes in patient-friendly language. Not medical advice."
    )
    existing = {s["id"] for s in data["sources"]}
    added = 0
    for src in NEW_SOURCES:
        if src["id"] not in existing:
            data["sources"].append(src)
            added += 1
    PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"sources={len(data['sources'])} added={added}")


if __name__ == "__main__":
    main()
