# APA three-line table spec

The reference for what `format_apa_tables.py` produces. Use this when diagnosing a table that "looks wrong" or when adjusting the YAML.

---

## Anatomy of an APA three-line table

```
                                                                  ← caption row (above table)
Table 1
Descriptive statistics for the analytic sample (N = 1,847)

═══════════════════════════════════════════════════════           ← TOP RULE (1.5 pt)
Variable              Mean      SD     Min    Max                 ← header row, BOLD
───────────────────────────────────────────────────────           ← HEADER RULE (0.5 pt)
Firm age               12.3     8.1     1.0   45.0
TMT size                7.2     2.6     3.0   15.0
R&D intensity           0.043   0.029   0.00   0.18
═══════════════════════════════════════════════════════           ← BOTTOM RULE (1.5 pt)

Note. Standard deviations in parentheses. Variables winsorized at the
1st and 99th percentiles.                                          ← notes row (below table)
```

Three rules total. No internal vertical lines, no internal horizontal lines except the one under the header.

---

## How the script builds it

For each table in document order:

1. **Clear inherited borders.** Pandoc applies a table style ("Table" or "Table Grid") that draws a full grid. `clear_table_inner_borders()` sets every border at the table level to `nil`.

2. **Set per-cell borders:**
   - Row 0 (header): `top = TOP_PT`, `bottom = HEADER_PT` (only if more than one row).
   - Last row: `bottom = BOTTOM_PT`.
   - Every other row: no top, no bottom.
   - All rows: `left = right = None` (no verticals).

3. **Bold the header row.** Every run in row 0 gets `bold = True`.

4. **Set the table font** on every cell run: `font_name` and `font_size_pt` from the YAML (typically TNR 11 — one point smaller than body to make wide tables fit).

5. **Repeat the header.** Add `<w:tblHeader/>` to the first row's `<w:trPr>`. Word will repeat row 0 at the top of every subsequent page the table spans.

6. **Prevent row splits.** Add `<w:cantSplit/>` to every row's `<w:trPr>`. Word keeps each row's content on a single page even if the row is tall.

7. **Renumber captions.** Scan body children. For each `<w:tbl>`, look at the immediately preceding paragraph. If it's a caption candidate (style name contains "Caption" OR text starts with "Table[:.]?\s*\d*"), rewrite it as `<prefix> <N><sep><title>` using the YAML's caption settings.

A "caption candidate" is intentionally fuzzy. The script will not invent captions for tables that have no preceding caption paragraph — it just lists those tables in its stdout output for the user to fix in the Markdown.

---

## YAML knobs (recap)

```yaml
tables:
  style: apa                  # apa | grid | simple
  font_name: Times New Roman
  font_size_pt: 11
  header_bold: true

  border_top_pt: 1.5          # top rule weight (points)
  border_header_bottom_pt: 0.5
  border_bottom_pt: 1.5

  caption_position: above
  caption_prefix: "Table"     # or "TABLE" for journals that want all-caps
  caption_separator: "\n"     # "\n" for stacked; ". " for inline
  caption_number_format: arabic
  caption_font_size_pt: 12
  caption_prefix_bold: false
  caption_title_italic: true

  notes:
    label: "Note."
    label_italic: true
    font_size_pt: 10

  repeat_header_across_pages: true
  allow_row_split: false
```

The script does NOT auto-format the notes paragraph — it preserves it as-is from the Markdown. The YAML's `notes` section is for VALIDATE-mode reporting only (future enhancement: post-process the notes paragraph too).

---

## Visual differences across journals

| Journal | Caption layout | Prefix bold | Title italic |
|---|---|---|---|
| JBR (Elsevier) | "Table 1" newline "Title" | no | yes |
| Strategy Science (INFORMS) | "Table 1. Title" inline | yes | no |
| Generic | "Table 1" newline "Title" | no | yes |

These map directly to `caption_separator` (`\n` vs `. `), `caption_prefix_bold`, and `caption_title_italic`.

---

## When NOT to use APA three-line

Some tables are genuinely matrix-like (e.g., a correlation matrix) and benefit from a grid. Set `tables.style: grid` in the YAML to keep all Pandoc-emitted borders. Most management journals expect APA three-line for descriptive and regression tables; correlation matrices are sometimes shown with grid lines in the published version but submission format is still typically three-line.

To override per-table (not per-journal), you have two options:
1. Run `md_to_docx.py` with `--no-table-format`, then style the table manually in Word.
2. Run the full pipeline (APA-styled), then manually re-add grid lines to specific tables in Word.

Option 1 is cleaner if most of your tables need custom styling. Option 2 is faster if you have one outlier.
