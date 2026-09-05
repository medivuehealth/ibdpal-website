"""Publication helpers: reference validation, content lock, dual-edition preflight."""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from book_citations import CHAPTER_REFERENCES, REFERENCE_LIBRARY

ROOT = Path(__file__).resolve().parent.parent
BOOK_DIR = ROOT / "content" / "ibd-nutrition-book"
MASTER_DIR = BOOK_DIR / "MASTER_CONTENT"
ARCHIVE_DIR = BOOK_DIR / "ARCHIVE"
INTERIOR = BOOK_DIR / "Eating_With_IBD_Interior.docx"
KINDLE = BOOK_DIR / "KINDLE" / "Eating_With_IBD_Kindle.docx"


def validate_chapter_references() -> list[str]:
    """Return error messages for invalid chapter reference mappings."""
    errors: list[str] = []
    for ch_num, ref_ids in sorted(CHAPTER_REFERENCES.items()):
        if not ref_ids:
            errors.append(f"Chapter {ch_num}: no references assigned")
            continue
        for rid in ref_ids:
            if rid not in REFERENCE_LIBRARY:
                errors.append(f"Chapter {ch_num}: unknown reference id {rid}")
        seen: set[int] = set()
        for rid in ref_ids:
            if rid in seen:
                errors.append(f"Chapter {ch_num}: duplicate reference id {rid}")
            seen.add(rid)
    missing_chapters = set(range(1, 52)) - set(CHAPTER_REFERENCES)
    for ch in sorted(missing_chapters):
        errors.append(f"Chapter {ch}: missing from CHAPTER_REFERENCES")
    return errors


def archive_locked_masters() -> list[Path]:
    """Copy latest interior and Kindle builds to MASTER_CONTENT and ARCHIVE."""
    ts = datetime.now().strftime("%Y%m%d_%H%M")
    written: list[Path] = []
    MASTER_DIR.mkdir(parents=True, exist_ok=True)
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

    if INTERIOR.is_file():
        locked = MASTER_DIR / "Eating_With_IBD_Master_LOCKED.docx"
        shutil.copy2(INTERIOR, locked)
        archive = ARCHIVE_DIR / f"Eating_With_IBD_Interior_{ts}.docx"
        shutil.copy2(INTERIOR, archive)
        written.extend([locked, archive])

    kindle_archive_dir = ARCHIVE_DIR / "KINDLE"
    kindle_archive_dir.mkdir(parents=True, exist_ok=True)
    if KINDLE.is_file():
        locked_k = MASTER_DIR / "Eating_With_IBD_Kindle_LOCKED.docx"
        shutil.copy2(KINDLE, locked_k)
        archive_k = kindle_archive_dir / f"Eating_With_IBD_Kindle_{ts}.docx"
        shutil.copy2(KINDLE, archive_k)
        written.extend([locked_k, archive_k])

    return written


def validate_references_in_docx(path: Path) -> list[str]:
    """Flag incomplete reference lines in compiled chapters."""
    from docx import Document

    errors: list[str] = []
    doc = Document(str(path))
    in_refs = False
    for p in doc.paragraphs:
        text = p.text.strip()
        if text == "References":
            in_refs = True
            continue
        if in_refs and text.startswith("Key Takeaways"):
            in_refs = False
        if not in_refs:
            continue
        if not text or not re.match(r"^\d+\.\s", text):
            continue
        if "_______________" in text:
            continue
        if text.rstrip().endswith(","):
            errors.append(f"Incomplete reference: {text[:100]}")
        if len(text) < 40:
            errors.append(f"Suspiciously short reference: {text}")
        if "National Academies" in text and "Dietary Reference Intakes" not in text:
            errors.append(f"Truncated National Academies reference: {text[:100]}")
    return errors


def run_preflight(paths: list[Path]) -> int:
    """Run kdp_preflight_check on each path; return total hit count."""
    script = ROOT / "scripts" / "kdp_preflight_check.py"
    total = 0
    for path in paths:
        if not path.is_file():
            print(f"Preflight skip (missing): {path}")
            continue
        result = subprocess.run(
            [sys.executable, str(script), str(path)],
            capture_output=True,
            text=True,
        )
        print(result.stdout.rstrip())
        ref_errors = validate_references_in_docx(path)
        for err in ref_errors:
            print(f"Reference audit: {err}")
        if result.returncode != 0 or ref_errors:
            total += max(1, result.returncode)
    return total
