"""HTML helpers for Oct 11 2026 SEO gap posts. No dash characters in helper output."""
from __future__ import annotations


def p(text: str) -> str:
    return f"<p>{text.strip()}</p>"


def h2(title: str) -> str:
    return f"<h2>{title}</h2>"


def h3(title: str) -> str:
    return f"<h3>{title}</h3>"


def ul(items: list[str]) -> str:
    rows = "\n".join(f'<li>{item}</li>' for item in items)
    return f'<ul class="blog-list">\n{rows}\n</ul>'


def assemble(
    intro: str,
    sections: list[tuple[str, list[str]]],
    *,
    clinic_quote: str,
    faqs: list[tuple[str, str]],
    related_html: str,
    closing: list[str] | None = None,
) -> str:
    parts: list[str] = [p(intro)]
    for heading, paras in sections:
        parts.append(h2(heading))
        for para in paras:
            parts.append(p(para))
    parts.append(h2("Clinic script"))
    parts.append(p(f"&quot;{clinic_quote}&quot;"))
    parts.append(h2("Questions people search"))
    for question, answer in faqs:
        parts.append(h3(question))
        parts.append(p(answer))
    if closing:
        for para in closing:
            parts.append(p(para))
    parts.append(related_html)
    parts.append(
        p(
            "Education supports shared decisions with your gastroenterologist, surgeon, "
            "dietitian, or employer team. It does not replace emergency care. Seek help "
            "for severe pain, heavy bleeding, fever, vomiting that will not stop, fainting, "
            "or a sudden abdominal change unlike your usual IBD pattern."
        )
    )
    return "\n".join(parts)


def related(*links: tuple[str, str]) -> str:
    bits = " · ".join(f'<a href="{href}">{label}</a>' for label, href in links)
    return p(f"Related: {bits} · <a href=\"/resources\">resource library</a>.")
