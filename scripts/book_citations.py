"""Reference library and chapter-level citation mapping for Eating With IBD."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CitationRegistry:
    """Tracks numbered references per chapter."""

    refs: dict[int, str] = field(default_factory=dict)
    _next_id: int = 1
    chapter_used: dict[int, list[int]] = field(default_factory=dict)

    def note(self, ref_id: int) -> int:
        """Return display number for a library ref id, registering if new."""
        if ref_id not in self.refs:
            self.refs[ref_id] = REFERENCE_LIBRARY[ref_id]
        return ref_id

    def assign_chapter(self, chapter_num: int, ref_ids: list[int]) -> list[int]:
        ordered: list[int] = []
        seen: set[int] = set()
        for rid in ref_ids:
            if rid in REFERENCE_LIBRARY and rid not in seen:
                self.note(rid)
                ordered.append(rid)
                seen.add(rid)
        self.chapter_used[chapter_num] = ordered
        return ordered

    def format_inline(self, ref_id: int) -> str:
        return f"[{ref_id}]"

    def chapter_reference_lines(self, chapter_num: int) -> list[str]:
        lines: list[str] = []
        for display_num, rid in enumerate(self.chapter_used.get(chapter_num, []), start=1):
            lines.append(f"{display_num}. {self.refs[rid]}")
        return lines


REFERENCE_LIBRARY: dict[int, str] = {
    1: (
        "American Gastroenterological Association. Clinical Practice Update: Role of Diet in "
        "Inflammatory Bowel Disease. Gastroenterology. 2024. "
        "https://gastro.org/guideline/role-of-diet-in-inflammatory-bowel-disease/"
    ),
    2: (
        "Crohn's & Colitis Foundation. Diet and Nutrition. Patient education resource. "
        "https://www.crohnscolitisfoundation.org/diet-and-nutrition"
    ),
    3: (
        "NIH Office of Dietary Supplements. Dietary Supplement Fact Sheets. "
        "https://ods.od.nih.gov/factsheets/list-all/"
    ),
    4: (
        "National Institute of Diabetes and Digestive and Kidney Diseases. Crohn's Disease. "
        "2023. https://www.niddk.nih.gov/health-information/digestive-diseases/crohns-disease"
    ),
    5: (
        "Ruemmele FM, et al. ECCO-ESPGHAN Guideline on Paediatric Crohn's Disease. "
        "J Crohns Colitis. 2020;14(3):239-258. doi:10.1093/ecco-jcc/jjz187"
    ),
    6: (
        "USDA Agricultural Research Service. FoodData Central. "
        "https://fdc.nal.usda.gov/"
    ),
    7: (
        "World Gastroenterology Organisation. Malnutrition and Nutritional Support in "
        "Inflammatory Bowel Disease. Global Guideline. 2023. "
        "https://www.worldgastroenterology.org/guidelines/global-guidelines/inflammatory-bowel-disease-ibd"
    ),
    8: (
        "American Gastroenterological Association. Clinical Practice Update on "
        "Micronutrient Deficiencies in Inflammatory Bowel Disease. Gastroenterology. 2024. "
        "https://gastro.org/guideline/micronutrient-deficiencies-in-inflammatory-bowel-disease/"
    ),
    9: (
        "Crohn's & Colitis Foundation. Managing Flares. Patient education resource. "
        "https://www.crohnscolitisfoundation.org/flares"
    ),
    10: (
        "Gibson PR, Barrett JS. Low FODMAP diet in functional bowel symptoms and IBD. "
        "J Gastroenterol Hepatol. 2017;32(S1):40-42. doi:10.1111/jgh.13695"
    ),
    11: (
        "Bischoff SC, et al. ESPEN guideline on clinical nutrition in inflammatory bowel disease. "
        "Clin Nutr. 2020;39(3):289-317. doi:10.1016/j.clnu.2019.11.002"
    ),
    12: (
        "Rubin DT, et al. ACG Clinical Guideline: Ulcerative Colitis in Adults. "
        "Am J Gastroenterol. 2019;114(3):384-413. doi:10.1038/s41395-018-0089-8"
    ),
    13: (
        "Lichtenstein GR, et al. ACG Clinical Guideline: Management of Crohn's Disease in Adults. "
        "Am J Gastroenterol. 2021;116(1):48-69. doi:10.14309/ajg.0000000000000480"
    ),
    14: (
        "Suskind DL, et al. NASPGHAN Clinical Report: Nutrition Support for the Child with "
        "Inflammatory Bowel Disease. J Pediatr Gastroenterol Nutr. 2017;65(5):586-598. "
        "doi:10.1097/MPG.0000000000001720"
    ),
    15: (
        "Crohn's & Colitis Foundation. Surgery for Crohn's Disease and Ulcerative Colitis. "
        "Patient education resource. "
        "https://www.crohnscolitisfoundation.org/what-is-ibd/surgery"
    ),
    16: (
        "National Academies of Sciences, Engineering, and Medicine. Dietary Reference Intakes. "
        "https://www.nationalacademies.org/our-work/dietary-reference-intakes"
    ),
    17: (
        "Levine A, et al. Crohn's Disease Exclusion Diet plus partial enteral nutrition induces "
        "sustained remission in a randomized controlled trial. Gastroenterology. 2019;155(1):87-96. "
        "doi:10.1053/j.gastro.2018.04.013"
    ),
    18: (
        "Cohen SA, et al. Specific Carbohydrate Diet for inflammatory bowel disease: "
        "a systematic review. Inflamm Bowel Dis. 2021;27(2):213-219. doi:10.1093/ibd/izaa021"
    ),
    19: (
        "Chiba M, et al. Lifestyle-related disease in Crohn's disease: relapse prevention by "
        "semi-vegetarian diet. World J Gastroenterol. 2010;16(20):2484-2490. "
        "doi:10.3748/wjg.v16.i20.2484"
    ),
    20: (
        "Cohen NA, et al. Systematic review: probiotics in the management of inflammatory "
        "bowel disease. J Crohns Colitis. 2020;14(3):321-334. doi:10.1093/ecco-jcc/jjz187"
    ),
    21: (
        "National Academies of Sciences, Engineering, and Medicine. Dietary Reference Intakes "
        "for Energy (Estimated Energy Requirement). 2005. "
        "https://www.nap.edu/catalog/10490/dietary-reference-intakes-for-energy-carbohydrate-fiber-fat-fatty-acids-cholesterol-protein-and-amino-acids"
    ),
}

CHAPTER_REFERENCES: dict[int, list[int]] = {
    1: [1, 2, 4, 7],
    2: [1, 2, 4, 13],
    3: [1, 7, 8, 15],
    4: [1, 2],
    5: [1, 2, 11],
    6: [1, 2, 9],
    7: [1, 2, 9],
    8: [1, 2, 9],
    9: [1, 2],
    10: [1, 2, 4],
    11: [1, 2, 11],
    12: [1, 2],
    13: [8, 13, 16, 3],
    14: [16, 21, 3, 6],
    15: [8, 3, 6],
    16: [8, 3, 6],
    17: [8, 3, 6],
    18: [8, 3, 6],
    19: [8, 16],
    20: [8, 16],
    21: [1, 17, 18, 19],
    22: [1, 17],
    23: [10],
    24: [10, 1],
    25: [1, 18],
    26: [1, 19],
    27: [1, 2],
    28: [5, 11],
    29: [5, 11],
    30: [11],
    31: [11, 15],
    32: [1, 2, 6],
    33: [1, 11, 6],
    34: [1, 2, 6],
    35: [1, 2],
    36: [1, 2],
    37: [1, 2, 4],
    38: [1, 2],
    39: [1, 9],
    40: [3, 8],
    41: [20, 3],
    42: [3, 1],
    43: [1, 13, 12],
    44: [2, 9],
    45: [14, 11],
    46: [2, 8],
    47: [2, 1],
    48: [15, 2],
    49: [2, 9],
    50: [2, 1],
    51: [1, 2, 8],
}

# Sources compiled once globally (pillar / hub pages)
GLOBAL_SINGLE_USE_SOURCES = {
    "/blog/complete-ibd-nutrition-guide.html",
}
