# Workflow

End-to-end guide for CONVERT and VALIDATE modes. Read this first.

---

## The pipeline (six steps)

```
input.md ──► [1] check_dependencies.py
              │  pandoc? python-docx? PyYAML?
              ▼
            [2] build_reference_docx.py <journal>
              │  YAML → templates/<journal>-reference.docx
              ▼
            [3] pandoc input.md --reference-doc=<ref> -o raw.docx
              │  structural conversion (headings, paragraphs, lists, tables, math)
              ▼
            [4] postprocess_docx.py raw.docx <journal>
              │  body font sweep, heading numbering, line numbers, page-number footer,
              │  first-line indent
              ▼
            [5] format_apa_tables.py raw.docx <journal>
              │  three-line borders, header row bold, caption renumbering,
              │  cross-page header repeat, cantSplit on rows
              ▼
            [6] validate_format.py raw.docx <journal>
              │  PASS/FAIL per category, markdown report next to docx
              ▼
            output.docx + <stem>-report.md
```

`scripts/md_to_docx.py` orchestrates all six steps. Users normally only call the orchestrator.

---

## CONVERT mode — step by step

### Pre-flight (do this before invoking the skill on real manuscripts)

1. Confirm pandoc is installed: `pandoc --version`. If missing: `brew install pandoc`.
2. Confirm the target journal has a YAML: `ls journal_configs/<key>.yaml`. If missing, switch to ADD-JOURNAL mode.
3. Confirm the source Markdown follows the authoring rules in [`markdown-authoring-rules.md`](markdown-authoring-rules.md). The biggest gotchas:
   - Tables need a caption paragraph immediately before them (`Table: My descriptive statistics`).
   - Figures need `![Caption](path/to/image.png)` syntax — alt text becomes the caption.
   - Headings start at `#` (H1) and don't skip levels.

### Invocation

```bash
python3 scripts/md_to_docx.py path/to/paper.md jbr -o paper-jbr.docx
```

Options:

| Flag | Effect |
|---|---|
| `-o, --output PATH` | Output path (default: `<input-stem>-<journal>.docx` next to input) |
| `--bibliography PATH` | Enable Pandoc citeproc with the given `.bib` file |
| `--csl PATH` | CSL style for citeproc (e.g., `apa.csl`) |
| `--skip-validate` | Skip the final validation step (still emits report only if requested) |
| `--no-table-format` | Skip APA table formatting (use only if your tables are pre-styled) |

### Reading the format report

The orchestrator prints the report to stdout and saves it to `<stem>-report.md`. The structure:

```
# Format compliance report
**Overall: PASS** or **Overall: FAIL (N issue(s))**

## Page setup
| Check | Expected | Actual | Result |
| ...

## Body typography
...

## Headings
...

## Tables
...
```

If FAIL: open the report, find the FAIL rows, and consult [`troubleshooting.md`](troubleshooting.md) for the most common root causes.

---

## VALIDATE mode — when the user already has a docx

```bash
python3 scripts/validate_format.py existing.docx jbr
```

Same report format. This is useful when:
- The user has a docx from another tool and wants to know if it matches JBR's spec.
- A round of manual editing in Word may have introduced regressions.
- After a `--no-table-format` run, the user wants to confirm the rest still complies.

VALIDATE doesn't modify the file. To re-apply formatting, switch back to CONVERT (with the docx → not possible; only Markdown is the input) or run individual scripts (`postprocess_docx.py`, `format_apa_tables.py`).

---

## Why the pipeline is split into six scripts

Each step handles one concern, so debugging is easier:
- **Pandoc** is great at structural conversion, terrible at fine-grained typography in docx output. Don't fight it; let it do what it's good at.
- **python-docx** is the opposite. It can't parse Markdown, but it has precise control over OOXML.
- **Validation** is read-only, so it can't break anything.

If the user reports "the body font is wrong", the bug is in **step 4** (postprocess). If "the tables don't have three-line borders", the bug is in **step 5** (tables). If "the headings aren't numbered", the bug is also in step 4. This mental model is documented further in [`troubleshooting.md`](troubleshooting.md).

---

## When to rebuild the reference docx

The orchestrator auto-rebuilds when the YAML is newer than the docx. To force a rebuild:

```bash
python3 scripts/build_reference_docx.py jbr
```

You almost never need to invoke this manually — editing the YAML and re-running `md_to_docx.py` is enough.
