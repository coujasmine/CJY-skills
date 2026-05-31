# Strategy Science — submission-format reference

Companion to [`journal_configs/strategy-science.yaml`](../../journal_configs/strategy-science.yaml). The YAML drives the conversion; this file is the human-facing checklist.

**Status:** user-verified 2026-05 against the live INFORMS pages cited at the bottom.

The key discipline: this skill turns Markdown into a docx whose format matches the **hard official requirements** of Strategy Science. Everything else — manuscript organization, table count, cover-letter length, etc. — is advice, not format spec. The two are deliberately separated below so you can quote the official ones with confidence and treat the rest as judgment calls.

---

## A. Hard official requirements

These are explicitly stated on the Strategy Science / INFORMS submission pages and are encoded in the YAML config or enforced by the skill's pipeline.

| Item | Requirement | Where encoded |
|---|---|---|
| Manuscript length | ≤ 35 pages all-inclusive. If you go over, **briefly explain in the cover letter**. Use online supplements / e-companion to offload bulk. | Not in YAML (organization choice); flag in cover letter |
| Font size | **11 pt**, standard font (Times New Roman is INFORMS's example, not the only acceptable face) | `body.font_size_pt: 11` |
| Line spacing | Double-spaced | `body.line_spacing: 2.0` |
| Margins | 1 inch (2.54 cm) on all sides | `page.margin_*_cm: 2.54` |
| File type | .doc / .docx accepted at submission; any software that can produce PDF is fine | n/a (this skill emits .docx) |
| Review type | Double-blind. **Remove** author names, affiliations, acknowledgments from the manuscript itself. Self-citations stay but written neutrally (e.g., "Jones (2018) shows…" rather than "we show in earlier work…"). | Author's responsibility in the Markdown source. `blind: true` is informational. |
| Abstract | ≤ **200 words**, text-only, no references, no math. (ScholarOne Step 1 caps at 250 but 200 is the safe ceiling for the manuscript itself.) | `abstract.word_limit: 200` |
| Keywords | 3–10 keywords (ScholarOne Step 2). Final source cover page should include them once accepted; at initial submission they live in ScholarOne and putting them on page 1 of the manuscript is the safe default. | `keywords.min_count: 3`, `max_count: 10` |
| References | Alphabetical by first-author surname, author–year style (INFORMS reference style — see official PDF style guide) | Author's responsibility (or via Pandoc citeproc with an INFORMS-compatible CSL) |
| Footnotes / endnotes | **Avoid**. Move necessary content into the main text. | Author's responsibility in the Markdown source |
| Tables / figures | Continuously numbered. Placed **after the references**, not embedded throughout. Cited from the body text. | Author's responsibility in MD organization. Caption renumbering: `format_apa_tables.py`. |
| Submission system | ScholarOne — 7-step workflow | n/a |
| ScholarOne Step 5 / cover letter disclosures | Conflicts of interest, overlapping papers (incl. working papers), papers using the **same database**, funding sources. The same-database disclosure is unusually strict for INFORMS — don't omit it. | n/a (handle at submission time) |
| ORCID | Submitting author must have an ORCID at submission. All authors need one before final publication. | n/a (handle in ScholarOne) |
| Final files (post-acceptance) | 14 days to submit: editable source (Word/LaTeX), main paper PDF, online appendix PDF, figure source files, copyright form, editorial checklist, author biography. | n/a |

---

## B. Submission strategy / advice (NOT official)

These items aid acceptance probability but are not stated by Strategy Science as format requirements. Treat them as guidance, not as compliance checks.

| Topic | Common practice | Why |
|---|---|---|
| Section structure | Intro / Theory / Methods / Results / Discussion (empirical); Intro / Argument / Implications (theoretical) | Genre conventions, not journal rule |
| Page budget within 35 pages | Roughly Intro 4, Theory 8–10, Methods 5–7, Results 6–8, Discussion 5–7 | Editor-readability heuristic |
| Number of main tables | Typically 4–5 main-text tables; robustness tables to the appendix | Reviewer-load convention |
| Regression table styling | APA three-line; significance markers `*p < .10, **p < .05, ***p < .01`; coefficient + SE in cells; pseudo-R² / N at bottom | Discipline norm |
| Winsorization / outlier note | If applied, state in Methods and note in table footers | Reviewer expectation, not journal rule |
| Cover-letter length | ~400–700 words: positioning, novelty, fit, disclosures | INFORMS doesn't specify; this is editor preference |
| Data / code at initial submission | Not required by the live submission page as of 2026-05. May change — verify on ScholarOne at the time of submission. | Confirmed against current submission page |
| Reproducibility appendix | Strongly encouraged for empirical work, especially with same-database disclosures | Discipline norm |

The skill's `validate_format.py` checks **only the section A items it can mechanically verify** (margins, font, line spacing, line numbers, page numbers, table styling). It does not score the section B items.

---

## C. What the skill handles vs. what the author handles

| Concern | Handled by the skill | Handled by the author |
|---|---|---|
| 11-pt double-spaced TNR body | ✓ via YAML + reference.docx | — |
| 1-inch margins, line numbers, page numbers | ✓ | — |
| Heading numbering (decimal) | ✓ | — |
| APA three-line tables, header bold, header repeat across pages | ✓ | — |
| Caption numbering (Table 1, 2, 3…) | ✓ | — |
| Removing author identity from manuscript | — | ✓ (blinding is the author's job) |
| Cover-letter disclosures | — | ✓ (ScholarOne Step 5) |
| Same-database disclosure | — | ✓ — flag explicitly even if it overlaps with a paper not yet under review |
| 35-page check | — | ✓ — count the rendered PDF |
| Keyword selection (3–10) | — | ✓ |
| Abstract ≤200 words | — | ✓ (the YAML's `word_limit` is informational; not auto-truncated) |
| Reference list formatting per INFORMS style | — | ✓ (pre-format or use citeproc with an INFORMS CSL) |
| Moving tables/figures after references | — | ✓ in the Markdown source |

If validation passes but a section A item is in column 3, double-check before submitting.

---

## D. Verification sources

- [Strategy Science — Submission Guidelines](https://pubsonline.informs.org/page/stsc/submission-guidelines)
- [INFORMS Author Portal — File Preparation](https://pubsonline.informs.org/authorportal/file-preparation)
- [INFORMS Reference Style (PDF)](https://pubsonline.informs.org/pb-assets/INFORMSReferencesStyle.pdf)
- [INFORMS ORCID Policy](https://pubsonline.informs.org/authorportal/orcid)

Last verified: 2026-05. INFORMS occasionally tightens its policies (especially around data, code, and AI-use disclosures); re-check before each submission, and trust the **live ScholarOne portal** over this file when they conflict.
