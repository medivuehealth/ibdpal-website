"""Shared E-E-A-T disclaimer blocks and schema helpers for ibdpal.org."""
from __future__ import annotations

SITE = "https://www.ibdpal.org"
REVIEW_ISO = "2026-06-16"
REVIEW_DISPLAY = "June 2026"


def reviewed_by_org() -> dict:
    return {
        "@type": "Organization",
        "name": "MediVue Health Education",
        "url": SITE + "/",
    }


def page_review_props() -> dict:
    return {"lastReviewed": REVIEW_ISO, "reviewedBy": reviewed_by_org()}


def content_note_en() -> str:
    return (
        '<p class="blog-medical-review"><strong>Content note:</strong> '
        "Educational content aligned with publicly available patient materials from the "
        '<a href="https://www.crohnscolitisfoundation.org/" rel="noopener noreferrer">'
        "Crohn's &amp; Colitis Foundation</a> and other major IBD education sources. "
        "IBDPal is not affiliated with or endorsed by the Foundation. "
        f"Last reviewed {REVIEW_DISPLAY}. Not individual medical advice.</p>\n"
    )


def edu_disclaimer_en() -> str:
    return (
        '<p class="blog-edu-disclaimer"><strong>Educational use only.</strong> '
        "IBDPal does not provide medical advice, diagnosis, or treatment. "
        "Always consult your gastroenterologist or IBD care team for personal decisions.</p>\n"
    )


def hub_header_footnote_en() -> str:
    return (
        f'<p class="hub-header-footnote"><small>'
        f"Educational only · Reviewed {REVIEW_DISPLAY} · Not medical advice"
        f"</small></p>\n"
    )


def guide_disclaimer_en() -> str:
    return (
        '<p class="community-edu-disclaimer"><strong>Educational only.</strong> '
        "IBDPal does not provide medical advice, diagnosis, or treatment. "
        "Always consult your gastroenterologist or IBD care team for personal decisions.</p>"
    )


def hub_disclaimer_en() -> str:
    return (
        '<p class="community-edu-disclaimer"><strong>Educational only.</strong> '
        "Not medical advice. Verify organization details before you rely on them.</p>"
    )


def blog_medical_footer_en() -> str:
    return (
        "                        <h2>Medical Disclaimer</h2>\n"
        "                        <p>This article is for educational purposes only and should not replace "
        "professional medical advice, diagnosis, or treatment. Always consult your healthcare provider regarding "
        "dietary, medication, or lifestyle decisions.</p>\n"
    )


def icn_attribution_block(source_title: str, source_url: str) -> str:
    """Compact Creative Commons attribution for ImproveCareNow resources."""
    return (
        '                        <p class="icn-attribution" role="note">'
        "<em>Source: "
        f'<a href="{source_url}" rel="noopener noreferrer">{source_title}</a> '
        'by <a href="https://www.improvecarenow.org/" rel="noopener noreferrer">ImproveCareNow</a> '
        '(<a href="https://creativecommons.org/licenses/" rel="noopener noreferrer">CC license</a>). '
        "IBDPal is not an ICN partner.</em>"
        "</p>\n"
    )


def content_note_es() -> str:
    return (
        '<p class="blog-medical-review"><strong>Nota de contenido:</strong> '
        "Contenido educativo alineado con materiales públicos para pacientes de la "
        "Crohn's &amp; Colitis Foundation y otras fuentes educativas sobre EII. "
        "IBDPal no está afiliado ni respaldado por la Foundation. "
        f"Última revisión: {REVIEW_DISPLAY}. No es consejo médico individual.</p>\n"
    )


def ccf_nonaffiliation_about_en() -> str:
    return (
        '<p><strong>Independent education.</strong> IBDPal is a MediVue nonprofit patient '
        "education project. We are not affiliated with, endorsed by, or a partner of the "
        '<a href="https://www.crohnscolitisfoundation.org/" rel="noopener noreferrer">'
        "Crohn's &amp; Colitis Foundation</a>.</p>\n"
    )


def edu_disclaimer_es() -> str:
    return (
        '<p class="blog-edu-disclaimer"><strong>Solo fines educativos.</strong> '
        "IBDPal no ofrece consejo médico, diagnóstico ni tratamiento. "
        "Consulte siempre a su gastroenterólogo o equipo de atención de EII.</p>\n"
    )


def patch_blog_vote_icons(blogs_dir) -> int:
    """Replace corrupted emoji thumbs (??) with inline SVG icons."""
    import re

    from ui_snippets import BLOG_VOTE_THUMB_DOWN_SVG, BLOG_VOTE_THUMB_UP_SVG

    up_pat = re.compile(
        r'(<button type="button" class="blog-vote-btn blog-vote-btn--up"[^>]*>)\s*'
        r'(?:<span class="blog-vote-icon"[^>]*>.*?</span>|' + re.escape(BLOG_VOTE_THUMB_UP_SVG) + r')\s*',
        re.S,
    )
    down_pat = re.compile(
        r'(<button type="button" class="blog-vote-btn blog-vote-btn--down"[^>]*>)\s*'
        r'(?:<span class="blog-vote-icon"[^>]*>.*?</span>|' + re.escape(BLOG_VOTE_THUMB_DOWN_SVG) + r')\s*',
        re.S,
    )
    count = 0
    for path in blogs_dir.glob("*.html"):
        text = path.read_text(encoding="utf-8")
        new_text = up_pat.sub(rf"\1\n                                {BLOG_VOTE_THUMB_UP_SVG}\n                                ", text, count=1)
        new_text = down_pat.sub(rf"\1\n                                {BLOG_VOTE_THUMB_DOWN_SVG}\n                                ", new_text, count=1)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            count += 1
    return count


def patch_blog_back_links(blogs_dir) -> int:
    """Fix corrupted left-arrow (? or mojibake) and middle-dot separators in blog posts."""
    import re

    from ui_snippets import BLOG_BACK_LINK_HTML

    back_pat = re.compile(
        r'^\s*<p class="blog-back"><a href="[^"]*" class="blog-back-link">[^<]*All posts</a></p>',
        re.I | re.M,
    )
    back_repl = '                ' + BLOG_BACK_LINK_HTML
    date_pat = re.compile(
        r'(<p class="blog-date">Posted on [^<]+?)\s*(?:\?|←|·|\u00b7|\ufffd)\s*([^<]+)</p>',
        re.I,
    )
    count = 0
    for path in blogs_dir.glob("*.html"):
        text = path.read_text(encoding="utf-8")
        new_text = back_pat.sub(back_repl, text, count=1)
        new_text = date_pat.sub(r"\1 &middot; \2</p>", new_text)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            count += 1
    return count


def patch_content_notes(*dirs) -> int:
    """Refresh content note + edu disclaimer blocks (e.g. after CCF link update)."""
    import re

    count = 0
    top = content_note_en() + edu_disclaimer_en()
    pat = re.compile(
        r'<p class="blog-medical-review">.*?</p>\s*<p class="blog-edu-disclaimer">.*?</p>',
        re.S,
    )
    for base in dirs:
        for path in base.glob("*.html"):
            text = path.read_text(encoding="utf-8")
            new_text = pat.sub(top.strip(), text, count=1)
            if new_text != text:
                path.write_text(new_text, encoding="utf-8")
                count += 1
    return count


def patch_blog_eeat(blogs_dir) -> int:
    import re

    count = 0
    top = content_note_en() + edu_disclaimer_en()
    footer = blog_medical_footer_en()
    for path in blogs_dir.glob("*.html"):
        text = path.read_text(encoding="utf-8")
        new_text = re.sub(
            r'<p class="blog-medical-review">.*?</p>\s*<p class="blog-edu-disclaimer">.*?</p>',
            top.strip(),
            text,
            count=1,
            flags=re.S,
        )
        new_text = re.sub(
            r"<h2>Medical Disclaimer</h2>\s*<p>.*?</p>",
            footer.strip(),
            new_text,
            count=1,
            flags=re.S,
        )
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            count += 1
    return count


def hub_disclaimer_es() -> str:
    return (
        '<p class="community-edu-disclaimer"><strong>Solo educación.</strong> '
        "No es consejo médico. Verifique los datos de cada organización antes de confiar en ellos.</p>"
    )
