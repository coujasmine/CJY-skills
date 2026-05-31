---
name: markdown-word
description: >
  Convert a Markdown manuscript into a Word (.docx) document formatted to a
  specific English-language journal's submission style (JBR, Strategy Science,
  AMJ, SMJ, etc.), with fine-grained typography control and APA three-line
  tables. Use when the user says "把 markdown 转成 word", "convert MD to docx",
  "format for JBR/Strategy Science/AMJ submission", "排版", "三线表", "生成投稿
  Word", "add a new journal template", or supplies a Markdown manuscript and
  names a target journal. Do NOT use for plain Markdown editing, PDF-only
  output, slide/spreadsheet generation, or generic Word reports unrelated to
  journal submission.
---

# Markdown → Word (Journal Submission Formatter)

A Markdown-to-DOCX pipeline tuned for **English management/business journal submissions**. It pairs Pandoc (structural conversion) with python-docx (fine-grained typography + APA three-line tables), driven by a per-journal YAML config so adding a new outlet is a single new file, not a rewrite.

The skill operates in **four modes**. Pick one per invocation. Default to **CONVERT** when the user supplies a manuscript and names a journal.

---

## Modes (routing table)

| Mode | When | Primary files to load | Output |
|---|---|---|---|
| **CONVERT** *(default)* | User has a `.md` manuscript and wants it as a `.docx` formatted for a named journal | `references/workflow.md`, `references/markdown-authoring-rules.md`, `references/apa-table-spec.md`, the matching `journal_configs/<journal>.yaml`, the matching `references/journal-specs/<journal>.md` if present | Generated `.docx`, format-compliance report, list of items needing manual review |
| **VALIDATE** | User has an existing `.docx` (or just-converted output) and wants a format-compliance check against a target journal | `references/workflow.md` (§Validate), the matching `journal_configs/<journal>.yaml`, the matching `references/journal-specs/<journal>.md` if present | Pass/fail rubric across page/font/spacing/heading/table/figure/reference categories |
| **ADD-JOURNAL** | User wants to add a new journal's format spec (e.g., "add SMJ", "add Organization Science") | `references/adding-new-journal.md`, `journal_configs/_schema.md`, an existing config as template, an existing journal-spec doc as template | New `journal_configs/<new>.yaml`, new `references/journal-specs/<new>.md`, generated `templates/<new>-reference.docx`, smoke-test report |
| **TROUBLESHOOT** | User reports an output formatting bug (tables broken, headings wrong, fonts mixed) | `references/troubleshooting.md`, relevant config and script | Root-cause diagnosis + fix (config edit, post-process tweak, or MD authoring change) |

> **Routing rule:** Read only the files listed for the active mode. Do not pre-load all references.

---

## Supported journals (current)

| Key | Display name | Publisher | Config file | Verified spec doc |
|---|---|---|---|---|
| `jbr` | Journal of Business Research | Elsevier | [`journal_configs/jbr.yaml`](journal_configs/jbr.yaml) | — (not yet user-verified) |
| `strategy-science` | Strategy Science | INFORMS | [`journal_configs/strategy-science.yaml`](journal_configs/strategy-science.yaml) | [`references/journal-specs/strategy-science.md`](references/journal-specs/strategy-science.md) |
| `generic` | Generic double-spaced APA submission | — | [`journal_configs/generic.yaml`](journal_configs/generic.yaml) | — |

A "verified spec doc" splits the journal's hard official requirements from soft submission advice and cites primary sources. Before each submission, re-read the spec doc to confirm nothing has changed at the publisher's portal.

To add a new journal, run **ADD-JOURNAL** mode (see `references/adding-new-journal.md`).

---

## The pipeline (CONVERT mode)

```
input.md
   │
   ├─► [1] check_dependencies.py     (pandoc? python-docx? PyYAML?)
   │
   ├─► [2] build_reference_docx.py   (YAML → templates/<journal>-reference.docx)
   │
   ├─► [3] pandoc input.md \
   │         --reference-doc=templates/<journal>-reference.docx \
   │         --output=raw.docx
   │
   ├─► [4] postprocess_docx.py raw.docx <journal>     (font sweep, line numbers,
   │                                                   heading numbering, page setup)
   │
   ├─► [5] format_apa_tables.py raw.docx <journal>    (three-line borders, caption
   │                                                   linkage, cross-page header
   │                                                   repeat, notes row styling)
   │
   ├─► [6] validate_format.py raw.docx <journal>      (compliance check)
   │
   └─► output.docx + format-report.md
```

`scripts/md_to_docx.py` is the orchestrator that invokes steps 1–6 in order. Users don't normally run individual scripts; the orchestrator handles it.

---

## Deterministic checks — run the bundled scripts

Six steps in this skill are mechanical. Estimating them by eye is unreliable.

| Script | What it does | Run in |
|---|---|---|
| `scripts/check_dependencies.py` | Verifies pandoc, python-docx, PyYAML; reports install commands if missing | CONVERT step 1; ADD-JOURNAL pre-flight |
| `scripts/build_reference_docx.py <journal>` | Generates `templates/<journal>-reference.docx` from `journal_configs/<journal>.yaml` (page size, margins, default font, line spacing, heading styles) | CONVERT step 2 (auto-rebuilds if YAML newer than docx); ADD-JOURNAL after YAML written |
| `scripts/md_to_docx.py <input.md> <journal> [-o out.docx]` | End-to-end orchestrator. Calls pandoc + post-process + validate | CONVERT (primary entry point) |
| `scripts/postprocess_docx.py <docx> <journal>` | Applies font sweep, heading numbering, line numbers, page-number footer | CONVERT step 4; standalone fix-up |
| `scripts/format_apa_tables.py <docx> <journal>` | APA three-line borders, caption numbering, cross-page header repeat, notes row | CONVERT step 5; standalone table fix |
| `scripts/validate_format.py <docx> <journal>` | Reads docx, checks against YAML spec, emits markdown report | CONVERT step 6; VALIDATE mode |

Usage example for CONVERT mode:
```bash
python3 scripts/md_to_docx.py path/to/paper.md jbr -o paper-jbr.docx
```

---

## Hard Rules (override every other instruction)

These rules apply to **every mode** and cannot be relaxed by user request.

1. **Do not invent journal format requirements.** If a target journal has no YAML config in `journal_configs/`, halt and offer ADD-JOURNAL mode. Do not pretend to know AMJ/SMJ/MISQ formatting if no config exists.
2. **Do not silently modify Markdown content.** This skill is a *formatter*, not an editor. The conversion may normalize whitespace and unify quote characters, but it must not delete, reorder, or paraphrase the user's prose, citations, tables, or numbers. If a structural fix is needed (e.g., a Markdown table is malformed and won't convert), surface it as a `[NEEDS FIX]` note in the report — do not silently rewrite.
3. **Do not invent missing inputs.** If the user supplies a Markdown file with no tables, do not fabricate Table 1. If the abstract is missing, do not write one. Surface the gap in the format report.
4. **Pandoc must be installed.** This pipeline's first step is `check_dependencies.py`. If pandoc is missing, halt with the install command (`brew install pandoc` on macOS) — do not silently fall back to a worse converter.
5. **The reference.docx is generated, not hand-edited.** Never instruct users to manually edit `templates/<journal>-reference.docx`. The source of truth is `journal_configs/<journal>.yaml`. If a format change is needed, edit the YAML and rebuild.
6. **Format reports must be machine-readable.** `validate_format.py` emits a markdown report with a clear PASS/FAIL per category. Do not hide failures in prose; list them as a table.
7. **APA three-line tables are the default.** All tables get top/header-bottom/bottom borders only, with no internal verticals unless the YAML explicitly overrides (`tables.style: grid`). The first row is treated as the header and bolded.
8. **Auto-numbered captions are skill-applied, not author-applied.** Authors write `Table: Descriptive Statistics` (no number). The post-processor assigns `Table 1`, `Table 2`, … in document order. If the user pre-numbered, the skill warns and uses author numbering.
9. **Preserve the manuscript's blind status.** If the YAML says `blind: true` (default for most journals' initial submission), the skill does not insert author identity into headers/footers. Author names in the title page itself are the author's responsibility.

---

## Intake Gate

Before running CONVERT, VALIDATE, or ADD-JOURNAL, confirm the following. Ask **only for items not already obvious**.

| Field | Required for | Why |
|---|---|---|
| Markdown file path (or pasted content saved to temp file) | CONVERT, VALIDATE (if .docx not yet generated) | No source → no conversion |
| Target journal key (must match a file in `journal_configs/`) | CONVERT, VALIDATE | Selects format spec |
| Submission stage = first submission / R&R / camera-ready | CONVERT | Camera-ready may want blind=false, embedded figures, etc. |
| New journal name + URL of author guidelines | ADD-JOURNAL | Cannot fabricate format requirements |
| Specific symptom + section affected | TROUBLESHOOT | Narrows root cause |

If pandoc is not installed, halt and instruct: `brew install pandoc` (macOS), `apt install pandoc` (Linux), or `choco install pandoc` (Windows).

---

## Output Contracts

### CONVERT mode output
```
✓ Generated: <output.docx>
✓ Format report: <output-report.md>

Compliance summary:
- Page setup: PASS / FAIL
- Body typography: PASS / FAIL
- Headings: PASS / FAIL
- Tables (N tables found): PASS / FAIL
- Figures (M figures found): PASS / FAIL
- References: PASS / FAIL

Manual review items:
- <list anything the skill couldn't auto-fix>
```

### VALIDATE mode output
A markdown table with one row per check, PASS/FAIL, and the offending location (paragraph index or table index) if FAIL.

### ADD-JOURNAL mode output
```
✓ Created: journal_configs/<key>.yaml
✓ Generated: templates/<key>-reference.docx
✓ Smoke test: converted examples/sample-paper.md → /tmp/<key>-smoke.docx

Next steps:
- Edit journal_configs/<key>.yaml to fine-tune <list the items the user
  could not specify from the guidelines URL alone>
- Re-run smoke test: python3 scripts/md_to_docx.py examples/sample-paper.md <key>
```

### TROUBLESHOOT mode output
A short root-cause diagnosis + the exact file edit (config YAML key, script function, or MD authoring change) that fixes it.

---

## Quick start (for the user)

```bash
# 1. Install pandoc once
brew install pandoc

# 2. Convert a manuscript to JBR-formatted Word
cd /Users/caojiaying/Desktop/yiyuan\ mai/论文专家agent/skills/markdown-word
python3 scripts/md_to_docx.py /path/to/your-paper.md jbr -o your-paper-jbr.docx

# 3. (optional) Validate an existing docx
python3 scripts/validate_format.py your-paper-jbr.docx jbr
```

For Markdown authoring conventions that produce the cleanest Word output (especially tables and figures), see [`references/markdown-authoring-rules.md`](references/markdown-authoring-rules.md).
