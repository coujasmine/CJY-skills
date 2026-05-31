#!/usr/bin/env python3
"""Generate templates/<journal>-reference.docx from journal_configs/<journal>.yaml.

Pandoc reads styles by NAME from the reference docx ("Normal", "Heading 1", ...).
This script writes page setup, the Normal style, and the Heading 1-4 styles so
that the Pandoc-emitted docx already has the right page geometry and default
typography. Tables, line numbers, page numbers, captions, and APA-style table
borders are handled later by postprocess_docx.py and format_apa_tables.py.
"""
import sys
from pathlib import Path

from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _lib import load_journal_config, reference_docx_path, TEMPLATE_DIR

ALIGN_MAP = {
    "left": WD_ALIGN_PARAGRAPH.LEFT,
    "right": WD_ALIGN_PARAGRAPH.RIGHT,
    "center": WD_ALIGN_PARAGRAPH.CENTER,
    "justify": WD_ALIGN_PARAGRAPH.JUSTIFY,
}


def configure_section(section, page_spec):
    if page_spec["size"] == "letter":
        section.page_width = Cm(21.59)
        section.page_height = Cm(27.94)
    elif page_spec["size"] == "a4":
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)
    section.top_margin = Cm(page_spec["margin_top_cm"])
    section.bottom_margin = Cm(page_spec["margin_bottom_cm"])
    section.left_margin = Cm(page_spec["margin_left_cm"])
    section.right_margin = Cm(page_spec["margin_right_cm"])


def _force_run_font(style, font_name):
    """Set the rFonts element so all four script types use the same font."""
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.insert(0, rfonts)
    rfonts.set(qn("w:ascii"), font_name)
    rfonts.set(qn("w:hAnsi"), font_name)
    rfonts.set(qn("w:cs"), font_name)
    rfonts.set(qn("w:eastAsia"), font_name)


def configure_style(style, spec, default_body):
    """Apply a YAML spec dict to a paragraph style (Normal or a Heading)."""
    font_name = spec.get("font_name", default_body["font_name"])
    style.font.name = font_name
    _force_run_font(style, font_name)
    style.font.size = Pt(spec.get("font_size_pt", default_body["font_size_pt"]))
    style.font.bold = spec.get("bold", False)
    style.font.italic = spec.get("italic", False)
    if spec.get("all_caps"):
        style.font.all_caps = True

    pf = style.paragraph_format
    pf.line_spacing = spec.get("line_spacing", default_body.get("line_spacing", 1.0))
    if "space_before_pt" in spec:
        pf.space_before = Pt(spec["space_before_pt"])
    if "space_after_pt" in spec:
        pf.space_after = Pt(spec["space_after_pt"])
    if "alignment" in spec:
        pf.alignment = ALIGN_MAP.get(spec["alignment"], WD_ALIGN_PARAGRAPH.LEFT)


def _get_or_create_style(doc, name, base="Normal"):
    """Return a paragraph style by name; create it (linked to base) if absent.

    Pandoc emits Title / Author / Abstract / AbstractTitle paragraphs when a
    YAML front matter is present; we want those styles to exist in the
    reference docx so the spec values are applied.
    """
    try:
        return doc.styles[name]
    except KeyError:
        pass
    from docx.enum.style import WD_STYLE_TYPE
    style = doc.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
    try:
        style.base_style = doc.styles[base]
    except KeyError:
        pass
    return style


def configure_title_styles(doc, title_page_spec, body):
    """Configure Title, Author, and Affiliation/Subtitle styles for Pandoc YAML front matter."""
    if not title_page_spec:
        return
    title_spec = title_page_spec.get("title")
    if title_spec:
        title_spec = {**body, **title_spec, "space_before_pt": 0, "space_after_pt": 12}
        configure_style(_get_or_create_style(doc, "Title"), title_spec, body)
    author_spec = title_page_spec.get("authors")
    if author_spec:
        author_spec = {**body, **author_spec, "space_before_pt": 0, "space_after_pt": 6}
        configure_style(_get_or_create_style(doc, "Author"), author_spec, body)
    affil_spec = title_page_spec.get("affiliations")
    if affil_spec:
        affil_spec = {**body, **affil_spec, "space_before_pt": 0, "space_after_pt": 12}
        # Pandoc doesn't always emit an affiliation style; we create a "Subtitle" alias
        # which is what some templates expect.
        configure_style(_get_or_create_style(doc, "Subtitle"), affil_spec, body)


def configure_abstract_styles(doc, abstract_spec, body):
    """Configure Abstract and AbstractTitle styles for Pandoc YAML abstract."""
    if not abstract_spec:
        return
    # Body of the abstract uses the same font/spacing as Normal.
    abstract_body = {**body, "first_line_indent_cm": 0}
    configure_style(_get_or_create_style(doc, "Abstract"), abstract_body, body)
    # Heading "Abstract" is bold.
    heading = {
        **body,
        "bold": abstract_spec.get("heading_bold", True),
        "alignment": abstract_spec.get("heading_alignment", "left"),
        "space_before_pt": 12,
        "space_after_pt": 6,
    }
    configure_style(_get_or_create_style(doc, "AbstractTitle"), heading, body)


def build(journal_key: str) -> Path:
    config = load_journal_config(journal_key)
    doc = Document()

    for section in doc.sections:
        configure_section(section, config["page"])

    body = config["body"]
    configure_style(doc.styles["Normal"], body, body)

    headings = config.get("headings", {})
    for level_key in ("h1", "h2", "h3", "h4"):
        if level_key not in headings:
            continue
        word_name = f"Heading {level_key[1:]}"
        try:
            style = doc.styles[word_name]
        except KeyError:
            continue
        configure_style(style, headings[level_key], body)

    configure_title_styles(doc, config.get("title_page"), body)
    configure_abstract_styles(doc, config.get("abstract"), body)

    TEMPLATE_DIR.mkdir(parents=True, exist_ok=True)
    out = reference_docx_path(journal_key)
    doc.save(out)
    return out


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: build_reference_docx.py <journal-key>", file=sys.stderr)
        return 2
    out = build(sys.argv[1])
    print(f"Generated reference docx: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
