# Journal config schema

Each `journal_configs/<key>.yaml` is the **single source of truth** for one journal's submission format. The schema below is what `build_reference_docx.py`, `postprocess_docx.py`, `format_apa_tables.py`, and `validate_format.py` read.

Keep YAML files comment-rich. Reviewers later need to know *why* a value was chosen (e.g., "JBR guideline §3.2 mandates 12pt TNR double-spaced").

---

## Top-level keys

```yaml
name: <slug>                  # internal key; must match filename without .yaml
display_name: <human name>    # shown in reports
publisher: <publisher>        # informational only
guideline_url: <url>          # author guidelines source; for traceability
notes: |
  Multi-line free-form notes about the journal's quirks
  (e.g., "Allows tables embedded OR end-of-document").

page: { ... }
body: { ... }
headings: { ... }
title_page: { ... }
abstract: { ... }
keywords: { ... }
tables: { ... }
figures: { ... }
references: { ... }
blind: <bool>                 # if true, do not put author identifiers in headers/footers
```

---

## `page`

```yaml
page:
  size: letter                # 'letter' or 'a4'
  orientation: portrait       # 'portrait' or 'landscape'
  margin_top_cm: 2.54
  margin_bottom_cm: 2.54
  margin_left_cm: 2.54
  margin_right_cm: 2.54
  line_numbers: true          # continuous line numbers in left margin
  line_number_restart: continuous   # 'continuous' | 'each_page' | 'each_section'
  page_numbers: true
  page_number_position: bottom_center   # 'bottom_center' | 'bottom_right' | 'top_right'
```

## `body`

```yaml
body:
  font_name: Times New Roman
  font_size_pt: 12
  line_spacing: 2.0           # 2.0 double, 1.5, 1.15, 1.0
  space_before_pt: 0
  space_after_pt: 0
  first_line_indent_cm: 0     # 0 = no indent; some journals want 1.27
  alignment: left             # 'left' | 'justify' | 'center'
```

## `headings`

```yaml
headings:
  numbering: decimal          # 'decimal' (1, 1.1, 1.1.1) | 'none'
  max_level: 4                # how deep numbering goes
  h1:
    font_name: Times New Roman
    font_size_pt: 12
    bold: true
    italic: false
    all_caps: false
    alignment: left
    space_before_pt: 18
    space_after_pt: 12
  h2: { ... }
  h3: { ... }
  h4: { ... }
```

Per-level settings inherit from `body` unless overridden.

## `title_page`

```yaml
title_page:
  separate_page: true
  title:
    font_size_pt: 14
    bold: true
    alignment: center
  authors:
    font_size_pt: 12
    alignment: center
  affiliations:
    font_size_pt: 11
    italic: true
    alignment: center
```

## `abstract`

```yaml
abstract:
  separate_page: true
  word_limit: 150             # null = no limit
  heading_text: Abstract
  heading_bold: true
  heading_alignment: left
```

## `keywords`

```yaml
keywords:
  min_count: 4
  max_count: 6
  separator: "; "
  label: "Keywords: "
  label_bold: true
```

## `tables`

```yaml
tables:
  style: apa                  # 'apa' (three-line) | 'grid' | 'simple'
  alignment: center           # table block alignment on page
  font_name: Times New Roman
  font_size_pt: 11
  header_bold: true
  cell_padding_pt: 3

  # Borders (only used when style: apa)
  border_top_pt: 1.5
  border_header_bottom_pt: 0.5
  border_bottom_pt: 1.5
  border_other_pt: 0          # 0 = no other borders

  # Caption
  caption_position: above     # 'above' | 'below'
  caption_prefix: "Table"
  caption_separator: "\n"     # "\n" = title on new line under "Table 1"; ". " = inline
  caption_number_format: arabic  # 'arabic' | 'roman'
  caption_font_size_pt: 12
  caption_prefix_bold: false
  caption_title_italic: true

  # Notes row (below table)
  notes:
    label: "Note."
    label_italic: true
    font_size_pt: 10
    alignment: left
    space_before_pt: 6

  # Cross-page behavior
  repeat_header_across_pages: true
  allow_row_split: false      # false = keep rows together across page breaks
```

## `figures`

```yaml
figures:
  caption_position: below
  caption_prefix: "Figure"
  caption_separator: "\n"
  caption_number_format: arabic
  caption_font_size_pt: 12
  caption_prefix_bold: false
  caption_title_italic: true
  alignment: center
```

## `references`

```yaml
references:
  heading_text: References
  hanging_indent_cm: 1.27
  font_size_pt: 12
  line_spacing: 2.0
  space_after_entry_pt: 0
  style_note: |
    Free-form note about the citation style the journal wants
    (APA 7, Chicago author-date, etc.). This skill does not auto-format
    references; the user should pre-format or use Pandoc citeproc upstream.
```

---

## Style precedence

When converting, the pipeline applies styles in this order:

1. `build_reference_docx.py` writes page setup, default font, line spacing, heading style names into the reference.docx (so Pandoc respects them).
2. `postprocess_docx.py` re-applies body font (Pandoc sometimes leaks default Calibri into runs), heading numbering, line numbers, page-number footer.
3. `format_apa_tables.py` rewrites every table's borders and applies caption numbering.
4. `validate_format.py` reads the resulting docx and checks each spec value.

If you observe an output value differing from the YAML, the bug is in one of steps 2–4, not in Pandoc. See `references/troubleshooting.md`.
