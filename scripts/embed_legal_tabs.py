#!/usr/bin/env python3
"""Embed privacy/support page body into index.html as tab panels."""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def inner_html(path: Path, class_name: str) -> str:
    text = path.read_text(encoding="utf-8")
    pattern = rf'<div class="{class_name}">(.*?)</div>\s*</main>'
    m = re.search(pattern, text, re.DOTALL)
    if not m:
        raise SystemExit(f"Could not extract .{class_name} from {path}")
    return m.group(1).strip()


def main():
    privacy_inner = inner_html(ROOT / "privacy.html", "legal-section")
    support_inner = inner_html(ROOT / "support.html", "support-section")

    privacy_block = f"""
            <!-- Privacy Tab -->
            <div class="tab-content" id="privacy">
                <div class="legal-section tab-page-section">
{privacy_inner}
                </div>
            </div>

            <!-- Support Tab -->
            <div class="tab-content" id="support">
                <div class="support-section tab-page-section">
{support_inner}
                </div>
            </div>

"""

    index = ROOT / "index.html"
    text = index.read_text(encoding="utf-8")
    marker = "            <!-- Contact Tab -->"
    if "id=\"privacy\"" in text and "tab-content" in text:
        text = re.sub(
            r"\s*<!-- Privacy Tab -->.*?<!-- Contact Tab -->",
            privacy_block + marker,
            text,
            count=1,
            flags=re.DOTALL,
        )
    else:
        text = text.replace(marker, privacy_block + marker, 1)

    text = text.replace(
        '<a href="/privacy" class="tab-button">Privacy</a>',
        '<button type="button" class="tab-button" data-tab="privacy">Privacy</button>',
    )
    text = text.replace(
        '<a href="/support" class="tab-button">Support</a>',
        '<button type="button" class="tab-button" data-tab="support">Support</button>',
    )

    index.write_text(text, encoding="utf-8")
    print("updated index.html with privacy and support tabs")


if __name__ == "__main__":
    main()
