# Adding a new journal

Four files are involved when you add a new outlet:

1. `journal_configs/<key>.yaml` — the format spec the pipeline reads
2. `templates/<key>-reference.docx` — generated from the YAML
3. `references/journal-specs/<key>.md` — human-facing "hard official vs. soft advice" breakdown with verification sources
4. (optional) `examples/sample-paper-<key>.docx` — smoke-test output to eyeball in Word

The whole process takes ~15 minutes if you have the journal's author guidelines handy.

The journal-spec doc in step 3 is what keeps the YAML honest. Without it, anyone reading the YAML later doesn't know which knobs are official requirements and which are sensible defaults you chose. [`references/journal-specs/strategy-science.md`](journal-specs/strategy-science.md) is the canonical template.

---

## Step 1 — Create the YAML config

Copy an existing config that's close to the new journal and rename:

```bash
cd /Users/caojiaying/Desktop/yiyuan\ mai/论文专家agent/skills/markdown-word
cp journal_configs/jbr.yaml journal_configs/<new-key>.yaml
```

Replace `<new-key>` with a short slug (kebab-case, no spaces). Examples: `amj`, `asq`, `smj`, `organization-science`, `mis-quarterly`, `research-policy`.

Edit the new YAML. Update at minimum:

```yaml
name: <new-key>                # must match filename
display_name: <human name>
publisher: <publisher>
guideline_url: <URL of author guidelines>
notes: |
  Free-form notes about this journal's quirks.
```

Then walk through every section (`page`, `body`, `headings`, `tables`, …) and adjust values per the author guidelines. The schema is documented in [`../journal_configs/_schema.md`](../journal_configs/_schema.md).

Common values to verify against guidelines:

| Section | Value | Where to look in guidelines |
|---|---|---|
| `page.size` | letter vs a4 | "Manuscript preparation → Paper size" |
| `page.margin_*_cm` | usually 2.54 (1") | "Margins" |
| `page.line_numbers` | most journals want them on for review | "Line numbers" or implicit from submission template |
| `body.font_*` | usually TNR 12 | "Font" |
| `body.line_spacing` | 2.0 (double) at submission; 1.5 occasionally | "Line spacing" |
| `abstract.word_limit` | varies widely (150–300) | "Abstract" |
| `keywords.min/max_count` | usually 4–6 | "Keywords" |
| `tables.style` | default `apa` for management journals | "Tables" |
| `tables.caption_*` | check examples in the journal | published article PDFs |
| `references.style_note` | informational; cite tooling lives upstream | "References" |

---

## Step 1b — Write the verified-spec doc

Create `references/journal-specs/<key>.md`. Use [`references/journal-specs/strategy-science.md`](journal-specs/strategy-science.md) as the template. Sections:

- **A. Hard official requirements** — table with columns: Item / Requirement / Where encoded. Cite the live submission page for each row.
- **B. Submission strategy / advice (NOT official)** — clearly labeled. Things like "typically 4–5 main tables" or "cover letter ~500 words" go here, not in section A.
- **C. What the skill handles vs. what the author handles** — splits responsibility.
- **D. Verification sources** — links to the live submission pages you used.

This separation is the whole point. Submitting to journals where you've mistaken your own habit for an official rule wastes desk-review time and can be embarrassing. The doc forces you to cite.

---

## Step 2 — Generate the reference docx

```bash
python3 scripts/build_reference_docx.py <new-key>
```

This creates `templates/<new-key>-reference.docx`. You don't edit this file directly; the YAML is the source of truth.

---

## Step 3 — Smoke test

Run the sample paper through the new config:

```bash
python3 scripts/md_to_docx.py examples/sample-paper.md <new-key>
```

This produces `examples/sample-paper-<new-key>.docx` next to the source. Open it in Word and check:

- [ ] Page margins match the spec
- [ ] Body is the right font at the right size
- [ ] Line spacing is correct
- [ ] Line numbers appear in the left margin
- [ ] Page numbers appear in the correct corner
- [ ] H1 / H2 / H3 are numbered correctly (1, 1.1, 1.1.1)
- [ ] The table at the bottom of the sample has three-line APA borders
- [ ] The table caption is "Table 1" (renumbered) and styled per the YAML

Also read the compliance report (`examples/sample-paper-<new-key>-report.md`). All checks should PASS.

If something's wrong, iterate: edit the YAML, re-run `md_to_docx.py` (which auto-rebuilds the reference docx because the YAML is newer), re-check.

---

## Step 4 — Document any quirks

If the journal has unusual requirements that this skill can't yet handle, leave a note in the YAML's `notes:` block AND open a tracking item (TODO in this file, or a comment in `references/troubleshooting.md`). Examples of currently-unsupported quirks:

- Two-column body layout (some methods journals)
- Embedded line numbers per page that restart at each page (`line_number_restart: each_page` is in the schema but not yet implemented end-to-end in the validator)
- Author-Year reference formatting via citeproc with custom CSL — supported but you must supply the CSL file via `--csl`

---

## A worked example — adding AMJ

```bash
# 1. copy
cp journal_configs/jbr.yaml journal_configs/amj.yaml

# 2. edit journal_configs/amj.yaml:
#    - name: amj
#    - display_name: Academy of Management Journal
#    - publisher: Academy of Management
#    - guideline_url: https://aom.org/research/journals/journal-style-guide
#    - notes: AMJ uses APA 7 style. Abstract 250 words. Headings unnumbered in
#      submitted manuscripts; the post-processor's heading numbering may need
#      to be disabled for AMJ:
#         headings:
#           numbering: none

# 3. generate the reference docx and smoke-test
python3 scripts/build_reference_docx.py amj
python3 scripts/md_to_docx.py examples/sample-paper.md amj

# 4. open examples/sample-paper-amj.docx in Word, verify, iterate.
```

That's it. The next user invocation `md_to_docx.py paper.md amj` will use the new config.
