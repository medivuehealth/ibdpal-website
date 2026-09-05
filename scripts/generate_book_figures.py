#!/usr/bin/env python3
"""Generate print-ready diagrams for Eating With IBD (300 DPI PNG + SVG)."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIGURES_DIR = ROOT / "content" / "ibd-nutrition-book" / "FIGURES"

# Book visual identity
NAVY = "#1A3A4A"
CORAL = "#C45C3E"
UC_BLUE = "#3A6B7C"
GRAY = "#8A9BA8"
LIGHT = "#F7F9FA"
ACCENT_RED = "#B85C5C"
FONT = "DejaVu Sans"

DPI = 300


def _save(fig, stem: str) -> None:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    png = FIGURES_DIR / f"{stem}.png"
    svg = FIGURES_DIR / f"{stem}.svg"
    fig.savefig(png, dpi=DPI, bbox_inches="tight", facecolor="white")
    fig.savefig(svg, bbox_inches="tight", facecolor="white")
    print(f"Wrote {png}")
    print(f"Wrote {svg}")


def figure_1_1() -> None:
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyBboxPatch, Rectangle

    fig, ax = plt.subplots(figsize=(6, 9), facecolor="white")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 14)
    ax.axis("off")

    ax.text(5, 13.4, "FIGURE 1.1", ha="center", fontsize=11, fontweight="bold", color=NAVY)
    ax.text(5, 12.9, "DIGESTIVE TRACT OVERVIEW", ha="center", fontsize=10, fontweight="bold", color=NAVY)

    segments = [
        ("Mouth", 12.2),
        ("Esophagus", 11.5),
        ("Stomach", 10.6),
        ("Duodenum", 9.7),
        ("Jejunum", 8.8),
        ("Ileum", 7.9),
        ("Colon", 6.7),
        ("Rectum", 5.8),
    ]
    cx = 5.0
    for name, y in segments:
        w = 2.2 if name == "Colon" else 1.4
        h = 0.55 if name == "Colon" else 0.45
        box = FancyBboxPatch(
            (cx - w / 2, y - h / 2),
            w,
            h,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            linewidth=1.2,
            edgecolor=NAVY,
            facecolor=LIGHT,
        )
        ax.add_patch(box)
        ax.text(cx, y, name, ha="center", va="center", fontsize=9, fontweight="semibold", color=NAVY)
        if name != "Rectum":
            ax.plot([cx, cx], [y - h / 2 - 0.05, y - h / 2 - 0.35], color=GRAY, lw=1.2)

    # Crohn's — scattered highlights (not entire tract)
    for y in (10.6, 9.0, 7.9):
        ax.add_patch(Rectangle((3.05, y - 0.18), 0.35, 0.36, facecolor=CORAL, alpha=0.35, edgecolor=CORAL, lw=1))
    ax.text(1.3, 9.5, "Crohn's disease", fontsize=9, fontweight="bold", color=CORAL)
    ax.text(1.3, 8.95, "Can affect different\nparts of the GI tract", fontsize=8, color=NAVY, va="top")
    ax.annotate("", xy=(3.0, 9.7), xytext=(2.5, 9.2), arrowprops=dict(arrowstyle="->", color=CORAL, lw=1))

    # UC — colon + rectum
    ax.add_patch(Rectangle((6.55, 5.55), 1.5, 1.35, facecolor=UC_BLUE, alpha=0.3, edgecolor=UC_BLUE, lw=1.2))
    ax.text(8.0, 6.5, "Ulcerative colitis", fontsize=9, fontweight="bold", color=UC_BLUE)
    ax.text(8.0, 5.95, "Involves the colon\nand rectum", fontsize=8, color=NAVY, va="top")
    ax.annotate("", xy=(7.0, 6.2), xytext=(7.6, 6.2), arrowprops=dict(arrowstyle="->", color=UC_BLUE, lw=1))

    _save(fig, "Figure_1_1_Digestive_Tract")
    plt.close(fig)


def figure_1_2() -> None:
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyBboxPatch, Circle

    fig, ax = plt.subplots(figsize=(6, 7), facecolor="white")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    ax.text(5, 9.5, "FIGURE 1.2", ha="center", fontsize=11, fontweight="bold", color=NAVY)
    ax.text(5, 9.0, "SYMPTOMS VERSUS INFLAMMATION", ha="center", fontsize=10, fontweight="bold", color=NAVY)

    def panel(x, title, subtitle, items, color):
        box = FancyBboxPatch((x, 3.2), 3.6, 5.2, boxstyle="round,pad=0.05", edgecolor=color, facecolor=LIGHT, lw=1.5)
        ax.add_patch(box)
        ax.text(x + 1.8, 7.9, title, ha="center", fontsize=10, fontweight="bold", color=color)
        ax.text(x + 1.8, 7.45, subtitle, ha="center", fontsize=8, color=NAVY)
        for i, item in enumerate(items):
            ax.text(x + 0.25, 6.9 - i * 0.55, f"• {item}", fontsize=8.5, color=NAVY)

    panel(0.6, "SYMPTOMS", "What you notice or feel", ["Pain", "Urgency", "Bloating", "Stool changes", "Nausea"], CORAL)
    panel(5.8, "INFLAMMATION", "What testing helps assess", ["Laboratory markers", "Stool inflammatory markers", "Endoscopy", "Imaging when appropriate"], UC_BLUE)

    # Center overlap
    c1 = Circle((4.2, 5.8), 0.55, facecolor=CORAL, alpha=0.25, edgecolor=CORAL)
    c2 = Circle((5.8, 5.8), 0.55, facecolor=UC_BLUE, alpha=0.25, edgecolor=UC_BLUE)
    ax.add_patch(c1)
    ax.add_patch(c2)
    ax.text(5, 5.8, "Overlap", ha="center", va="center", fontsize=7.5, fontweight="bold", color=NAVY)

    ax.text(5, 2.6, "They may overlap, but do not always match.", ha="center", fontsize=9, fontweight="semibold", color=NAVY)
    ax.text(5, 2.05, "Symptoms alone do not prove whether intestinal inflammation changed.", ha="center", fontsize=8, color=NAVY)
    ax.text(5, 1.5, "Inflammation can sometimes be present even when symptoms are limited.", ha="center", fontsize=8, color=NAVY)

    _save(fig, "Figure_1_2_Symptoms_vs_Inflammation")
    plt.close(fig)


def figure_2_1() -> None:
    """Anatomy schematic: tract segments on the right, absorption notes on the left."""
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

    fig, ax = plt.subplots(figsize=(6, 9.5), facecolor="white")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 13)
    ax.axis("off")

    ax.text(5, 12.55, "FIGURE 2.1", ha="center", fontsize=12, fontweight="bold", color=NAVY)
    ax.text(
        5, 12.05, "DISEASE LOCATION AND ABSORPTION",
        ha="center", fontsize=10, fontweight="bold", color=NAVY,
    )

    tract_x = 7.6
    segments = [
        (10.2, "Proximal small intestine"),
        (8.0, "Terminal ileum"),
        (5.8, "Colon"),
    ]
    for y, label in segments:
        box = FancyBboxPatch(
            (tract_x - 1.2, y - 0.42),
            2.4,
            0.84,
            boxstyle="round,pad=0.03,rounding_size=0.1",
            edgecolor=NAVY,
            facecolor=LIGHT,
            lw=1.4,
        )
        ax.add_patch(box)
        ax.text(
            tract_x, y, label,
            ha="center", va="center", fontsize=8.5, fontweight="semibold", color=NAVY,
        )
        if y > 5.8:
            ax.plot([tract_x, tract_x], [y - 0.42, y - 0.72], color=GRAY, lw=1.2)

    notes = [
        (10.2, "Important site for absorption\nof many nutrients."),
        (8.0, "Primary site for vitamin B12\nabsorption; disease or resection\nmay affect B12 status."),
        (5.8, "Important for fluid and\nelectrolyte handling."),
    ]
    for y, note in notes:
        ax.text(
            0.35, y, note,
            ha="left", va="center", fontsize=8.5, color=NAVY, linespacing=1.25,
        )
        ax.add_patch(
            FancyArrowPatch(
                (3.55, y),
                (tract_x - 1.25, y),
                arrowstyle="-|>",
                color=UC_BLUE,
                lw=1.2,
                mutation_scale=11,
            )
        )

    ax.text(
        5,
        1.35,
        "Disease location, inflammation, and prior surgery can change nutritional risk.\n"
        "Individual needs require clinical interpretation.",
        ha="center",
        va="top",
        fontsize=8.5,
        color=NAVY,
        style="italic",
    )

    _save(fig, "Figure_2_1_Disease_Location_Absorption")
    plt.close(fig)


def main() -> int:
    try:
        import matplotlib  # noqa: F401
    except ImportError:
        print("matplotlib is required: pip install matplotlib")
        return 1
    figure_1_1()
    figure_1_2()
    figure_2_1()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
