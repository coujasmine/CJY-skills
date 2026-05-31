# Troubleshooting

If something looks wrong in the output, find the symptom in §1 and follow the diagnosis. If the symptom isn't listed, see §2 for a step-by-step bisection.

---

## 1. Symptom catalog

### "Body font is Calibri, not Times New Roman"
- **Root cause:** Pandoc emitted runs without an explicit font, so Word fell back to its default.
- **Fix:** Step 4 (`postprocess_docx.py`) should be forcing the body font on every run. Re-run it standalone:
  ```bash
  python3 scripts/postprocess_docx.py <file>.docx <journal>
  ```
- **Persists?** The `apply_body_font` function only touches non-heading paragraphs. If a heading is wrong, check the heading style in the reference docx — the YAML's `headings.hX.font_name` must be set.

### "Headings aren't numbered" (or are wrong)
- **Root cause:** The post-processor only numbers paragraphs whose style name is literally `Heading 1`, `Heading 2`, … If Pandoc applied a different style (e.g., `Heading1` no-space, or `My Heading`), the regex doesn't match.
- **Fix:** Open the docx in Word, click into the heading, check the style name in the Styles pane. If it's not `Heading 1`/`2`/`3`/`4`, the issue is upstream in the reference docx.
- **Workaround:** Set `headings.numbering: none` in the YAML and number manually in Markdown.

### "Line numbers don't appear in the left margin"
- **Root cause:** `page.line_numbers` is `false` in the YAML, OR `apply_line_numbers` was skipped.
- **Diagnosis:** Validate the docx — `validate_format.py` reports "line numbers enabled: PASS/FAIL".
- **Fix:** Re-run `postprocess_docx.py`.

### "Page numbers in the wrong corner / missing"
- **Root cause:** `page.page_number_position` mismatch, or the orchestrator skipped step 4.
- **Diagnosis:** Validate. The report has "page-number field present" check.
- **Fix:** Edit YAML, re-run `md_to_docx.py`.

### "Tables have a full grid, not three-line"
- **Root cause:** Step 5 (`format_apa_tables.py`) didn't run, OR Pandoc's table style is overriding cell borders.
- **Fix:**
  ```bash
  python3 scripts/format_apa_tables.py <file>.docx <journal>
  ```
  The script first zeros all table-level borders, then sets per-cell ones, which should win. If it still looks wrong, the cell borders may be set but a stale table-level border is rendering — open the docx, select the table, and confirm "No Border" at the Table Design level. If that fixes it visually, your `clear_table_inner_borders` is being overridden somewhere; report as a bug.

### "Table captions aren't numbered" or "numbered wrong"
- **Root cause:** The caption recognition is fuzzy. The post-processor looks for a paragraph immediately before each table whose text starts with `Table\s*\d*\s*[:.]?` or whose style name contains "Caption".
- **Diagnosis:** Run `format_apa_tables.py` standalone — it prints `Tables without a recognized caption (numbers): [X, Y, Z]`.
- **Fix:** In the Markdown, add a paragraph immediately before the table:
  ```markdown
  Table: My table description.

  | Col | ... |
  ```
  Then re-run `md_to_docx.py`.

### "Renumbering replaced my correct table number"
- **Root cause:** The script renumbers tables in document order. If you have appendix tables that should be A1, A2 instead of 7, 8, the default behavior doesn't know.
- **Fix:** Either (a) accept the linear numbering and rename in Word, or (b) split the document at the appendix boundary into two .md files, convert each, then combine in Word.

### "First-line indent is missing / unwanted"
- **Root cause:** `body.first_line_indent_cm` in the YAML.
- **Fix:** Set to `0` (no indent) or `1.27` (0.5", APA default). Re-run `md_to_docx.py`.

### "Pandoc threw an error during step 3"
- **Common causes:**
  - The Markdown has a malformed pipe table (column count mismatch between header and divider rows).
  - An image path doesn't exist.
  - A YAML metadata block at the top of the .md is malformed.
- **Fix:** Read the pandoc stderr message; it points to the line number.

### "Math equations look like raw $$"
- **Root cause:** Pandoc didn't recognize the math because of stray whitespace inside the dollars, or you used single `$` for display math instead of `$$`.
- **Fix:** Inline math: `$x = y$`. Display math: `$$\n... \n$$`. No leading space inside the `$`s.

### "The output is missing a section that was in the Markdown"
- **Root cause:** Almost always a Markdown structural issue — e.g., a fenced code block or a comment that swallowed text.
- **Diagnosis:** Run `pandoc input.md -o /tmp/raw.docx --reference-doc=templates/jbr-reference.docx` standalone. If text is missing in `/tmp/raw.docx` too, it's the source Markdown.

---

## 2. Bisection — when the symptom isn't above

The pipeline has six steps. Bisect them.

```bash
# 1. Dependency check — should print "All dependencies present"
python3 scripts/check_dependencies.py

# 2. Reference docx — rebuild and confirm it exists, ~10-40 KB
python3 scripts/build_reference_docx.py <journal>
ls -la templates/<journal>-reference.docx

# 3. Pandoc — convert without any post-processing
pandoc input.md --reference-doc=templates/<journal>-reference.docx \
    -o /tmp/raw.docx --standalone
# Open /tmp/raw.docx in Word. Does the structure match the Markdown (headings,
# paragraphs, tables, figures all present)?
#   Yes → bug is in step 4 or 5. Continue.
#   No  → bug is in the Markdown or in the reference docx. Stop and inspect.

# 4. Post-process
cp /tmp/raw.docx /tmp/step4.docx
python3 scripts/postprocess_docx.py /tmp/step4.docx <journal>
# Open /tmp/step4.docx. Are the body font, headings, line numbers, page numbers
# all correct?
#   Yes → bug is in step 5.
#   No  → bug is in step 4. Read the relevant function in postprocess_docx.py.

# 5. Tables
cp /tmp/step4.docx /tmp/step5.docx
python3 scripts/format_apa_tables.py /tmp/step5.docx <journal>
# Open /tmp/step5.docx. Are tables now three-line and captioned?

# 6. Validate
python3 scripts/validate_format.py /tmp/step5.docx <journal>
# Read the report. Failures point at the responsible step.
```

If you find a step where the symptom first appears, that's where the bug is. Read the relevant script.

---

## 3. Known limitations (not bugs)

| Limitation | Why | Workaround |
|---|---|---|
| Figure captions aren't auto-renumbered | `format_apa_tables.py` only handles tables; figure renumbering is a future enhancement | Use Pandoc's `--number-figures` (where supported) or accept the alt-text-as-caption ordering |
| Notes paragraph formatting (italic "Note.") is not auto-applied | Skill preserves user content; user writes `*Note.*` manually in Markdown | Write `*Note.*` in the Markdown |
| Cross-references (Table \ref{tab:foo}) aren't auto-rewired | Pandoc handles its own refs; this skill doesn't add a layer | Use Pandoc's `pandoc-crossref` filter upstream |
| Line numbering doesn't restart per page when `line_number_restart: each_page` | Currently the post-processor only writes `continuous` mode reliably | Set `continuous` and ignore the per-page option for now |
| Equation numbering | Pandoc's responsibility, varies by version | Use raw Word equation editor for complex numbering |
| Multi-column layout | Out of scope | Apply in Word after conversion |

---

## 4. When to report a bug vs fix it yourself

- **Single-paper workaround:** Open the output in Word and adjust manually. Don't change the skill.
- **Recurring across papers** in the same journal: edit the journal YAML.
- **Recurring across journals** (the script logic is wrong): edit the relevant script function and re-run.
- **Adding a feature** (e.g., figure renumbering): see `references/adding-new-journal.md` for the pattern, or write a new script and call it from `md_to_docx.py`.
