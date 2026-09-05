"""Extract and embed free-license images for the book compiler."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup

SUPPORTED_SUFFIXES = {".jpg", ".jpeg", ".png", ".gif"}

DECORATIVE_PATH_MARKERS = (
    "helpcenter",
    "flare-48h/flare_1",
    "er-ibd/er_1",
    "joint-pain-ibd/joint-pain",
)

DECORATIVE_ALT_MARKERS = (
    "calm rest setup",
    "calm setting for learning",
    "clinical setting reminding",
    "person reviewing health information",
    "support desk materials",
    "support materials for understanding",
    "gut health education context",
)

FOOD_ALT_MARKERS = (
    "nutrition education",
    "meal",
    "plate",
    "food",
    "fish",
    "rice",
    "vegetable",
    "fruit",
    "drink",
    "fluid",
    "hydration",
    "soup",
    "bread",
    "egg",
    "chicken",
    "salmon",
    "oatmeal",
    "potato",
    "yogurt",
    "lentil",
    "congee",
    "dal",
    "chapati",
    "roti",
    "olive oil",
    "mediterranean",
    "shake",
    "supplement",
    "water and fluids",
    "balanced drinks",
)

FREE_LICENSE_MARKERS = (
    "unsplash",
    "pexels",
    "free use",
    "free educational use",
    "educational food illustration",
    "cc0",
    "public domain",
    "creativecommons",
    "creative commons",
)


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def parse_license_label(credit_text: str) -> str:
    lower = credit_text.lower()
    if "unsplash" in lower:
        return "Unsplash License (free to use)"
    if "pexels" in lower:
        return "Pexels License (free to use)"
    if "free use" in lower:
        return _normalize(credit_text.replace("Photos:", "Photo:"))
    if "creative commons" in lower or "cc0" in lower:
        return _normalize(credit_text)
    return "Licensed for free use (see site image credits)"


def article_allows_images(soup: BeautifulSoup) -> bool:
    credit_el = soup.select_one("p.blog-photo-credit")
    if credit_el:
        text = credit_el.get_text().lower()
        if any(marker in text for marker in FREE_LICENSE_MARKERS):
            return True
    article = soup.select_one("div.blog-content") or soup.select_one("article")
    if article and article.select("div.blog-figure-grid img"):
        return True
    return False


def src_to_path(src: str, root: Path) -> Path | None:
    if not src or src.startswith(("http://", "https://", "data:")):
        return None
    rel = src.lstrip("/")
    path = root / rel
    if path.suffix.lower() not in SUPPORTED_SUFFIXES:
        return None
    return path if path.is_file() else None


def is_decorative_image(path: Path, alt: str) -> bool:
    path_lower = str(path).lower().replace("\\", "/")
    alt_lower = alt.lower()
    if any(marker in path_lower for marker in DECORATIVE_PATH_MARKERS):
        return True
    return any(marker in alt_lower for marker in DECORATIVE_ALT_MARKERS)


def is_food_education_image(path: Path, alt: str) -> bool:
    if is_decorative_image(path, alt):
        return False
    path_lower = str(path).lower().replace("\\", "/")
    # Part VI sources are food articles under blogs/assets with free-license credits.
    if "blogs/assets/" in path_lower:
        return True
    alt_lower = alt.lower()
    return any(marker in alt_lower for marker in FOOD_ALT_MARKERS)


def extract_licensed_images(
    soup: BeautifulSoup,
    root: Path,
    max_images: int = 3,
    *,
    food_only: bool = True,
) -> list[dict[str, Any]]:
    if not article_allows_images(soup):
        return []

    credit_el = soup.select_one("p.blog-photo-credit")
    credit_text = _normalize(credit_el.get_text()) if credit_el else ""
    license_label = parse_license_label(credit_text) if credit_text else "Unsplash or Pexels (free use)"

    article = soup.select_one("div.blog-content") or soup.select_one("article.support-section") or soup.select_one("article")
    if article is None:
        return []

    imgs: list[dict[str, Any]] = []
    seen_paths: set[str] = set()

    figure_imgs = article.select("div.blog-figure-grid img")
    thumb_imgs = [] if figure_imgs else article.select("img.blog-header-thumb")

    for img in [*figure_imgs, *thumb_imgs]:
        if len(imgs) >= max_images:
            break
        src = img.get("src") or ""
        path = src_to_path(src, root)
        if path is None:
            continue
        key = str(path.resolve())
        if key in seen_paths:
            continue
        seen_paths.add(key)
        alt = _normalize(img.get("alt") or "")
        if not alt or len(alt) < 8:
            fig = img.find_parent("figure")
            if fig:
                cap = fig.find("figcaption")
                if cap:
                    alt = _normalize(cap.get_text())
        if not alt:
            alt = _normalize(path.stem.replace("-", " ").replace("_", " "))
        if food_only and not is_food_education_image(path, alt):
            continue
        imgs.append(
            {
                "path": path,
                "alt": alt,
                "credit": license_label,
                "src": src,
            }
        )

    return imgs
