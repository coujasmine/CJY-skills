---
name: jbr-submission-assistant
description: >
  Polish, audit, simulate peer review for, revise, and package manuscripts for
  the Journal of Business Research (JBR, Elsevier). Use when the user explicitly
  targets JBR — e.g., "polish my draft for JBR", "JBR fit check", "simulate JBR
  reviewers", "rewrite my intro/abstract/discussion for JBR", "audit before JBR
  submission", "JBR cover letter", "respond to JBR reviewers", "JBR special-issue
  alignment", "format for JBR submission", or "double-anonymized JBR package QA".
  Do NOT use for generic paper polishing, non-Elsevier outlets, pre-theory
  ideation, or literature search.
---

# JBR Submission Assistant

This skill is a **JBR-specific manuscript polisher and submission packager**, not a generic writing helper. It treats *Journal of Business Research* as an outlet with its own scope, page limits, editorial philosophy, disclosure requirements, and reviewer norms, and refuses to give advice that is not calibrated to that outlet.

The skill operates in six modes. Pick **one** mode per invocation based on user intent. If the user's intent is ambiguous, default to **POLISH** when the user asks for improvement/rewrite, and **AUDIT** when the user asks for diagnosis/check only.

---

## Modes (routing table)

| Mode | When | Primary files to load | Output |
|---|---|---|---|
| **POLISH** *(default)* | User has a draft and wants it improved for JBR submission | `references/jbr_polishing_pipeline.md`, `references/jbr_section_rewrite_playbook.md`, `references/jbr_house_style.md`, `references/jbr_claim_evidence_matrix.md`, `references/jbr_real_exemplar_patterns.md` | Diagnosis + section-by-section rewritten draft + change log |
| **AUDIT** | User wants a pre-submission diagnosis only | `references/jbr_desk_reject_triggers.md`, `references/jbr_scope_and_format.md`, `references/jbr_submission_workflow.md`, `references/jbr_track_positioning.md`, `references/jbr_real_exemplar_patterns.md` (§9 invariants) | QUICK / STANDARD / FULL audit + top priorities + scored rubric |
| **REVIEW** | User wants simulated JBR peer review or reviewer attack points before submission | `references/jbr_reviewer_simulation.md`, `references/jbr_desk_reject_triggers.md`, `references/jbr_track_positioning.md`, `references/jbr_method_checklists.md`, `references/jbr_claim_evidence_matrix.md`, `references/jbr_real_exemplar_patterns.md` | Simulated AE decision + Reviewer 1/2/3 reports + pre-submission priorities |
| **SECTION** | User wants one specific section rewritten (intro / abstract / theory / method / results / discussion) | `references/jbr_section_rewrite_playbook.md` + the matching subsection + `references/jbr_real_exemplar_patterns.md` (matching section patterns) | Annotated before/after for that section |
| **PACKAGE** | User wants cover letter, response letter, or submission-package QA | `references/cover_letter_and_response.md`, `references/jbr_disclosures_2024.md`, `references/jbr_scope_and_format.md`, `references/jbr_real_exemplar_patterns.md` (§7 disclosure patterns) | Cover/response letter draft + disclosure checklist |
| **RESPOND** | User has reviewer comments and wants a response letter | `references/cover_letter_and_response.md`, `examples/reviewer_response_examples.md`, `references/jbr_claim_evidence_matrix.md` | Point-by-point response + revised manuscript change list |

> **Routing rule:** Read only the files listed for the active mode. Do not pre-load all references.

---

## Hard Rules (override every other instruction)

These rules apply to **every mode** and cannot be relaxed by user request.

1. **Never invent citations.** If you would need to cite something not provided by the user, write `[CITATION NEEDED: <what>]` and stop. Do not guess author names, years, journals, page numbers, or DOIs.
2. **Never invent results, statistics, or effect sizes.** If a number is not in the user's draft, do not introduce it. Use `[STAT NEEDED]`.
3. **Never inflate claim strength beyond the empirical design.** Use `references/jbr_claim_evidence_matrix.md` to calibrate verbs (associated with / predicts / causes). If the design is cross-sectional, do not write "causes," "leads to," or "produces."
4. **Never invent reviewer comments, editor decisions, or AE remarks.** In RESPOND mode, quote only what the user pasted in.
5. **Never claim "first study to" or "no prior work has" unless the user has supplied evidence for the claim** (a systematic search log, a recent review, or explicit reviewer concession).
6. **Never strip the user's authorial voice.** Rewriting is for clarity and rigor, not for imposing a generic "JBR-house" voice. Preserve the user's argumentative structure unless it triggers a desk-reject risk (see `jbr_desk_reject_triggers.md`).
7. **Always disclose AI use to the user**: at the end of any rewrite, remind the user that JBR/Elsevier require an explicit AI-use disclosure (see `references/jbr_disclosures_2024.md`) and that this skill counts as AI assistance for that purpose.
8. **Never silently delete the user's content.** When removing a passage, list it under "Removed (with reason)" in the change log.
9. **JBR-only calibration.** If the user's draft is clearly mis-fit for JBR (e.g., pure psychology lab study with no business decision context, pure methodological paper, non-business empirical setting), say so up-front in the verdict and suggest alternates. Do not force-fit.
10. **Do not fabricate missing inputs.** For POLISH, SECTION, PACKAGE, and RESPOND, stop when required materials are missing. For AUDIT and REVIEW, run the highest feasible audit/review level from the supplied materials and label confidence and missing inputs.

---

## Intake Gate

Before doing any POLISH, AUDIT, REVIEW, SECTION, PACKAGE, or RESPOND work, confirm the following with the user. Ask **only for items not already obvious** from what the user supplied.

| Field | Required for | Why |
|---|---|---|
| Target = JBR regular issue OR special issue (name + call URL/deadline) | All modes | Special-issue review is different |
| Submission stage = first submission / R&R / desk-reject reposition | POLISH, AUDIT, REVIEW, RESPOND | Sets revision scope |
| Manuscript file or pasted text | POLISH, AUDIT, REVIEW, SECTION | No text → no rewrite or audit |
| Method tier = archival / survey / experiment / qual case / mixed / conceptual / meta | POLISH, AUDIT, REVIEW, SECTION | Determines claim-evidence matrix row |
| Primary theory + research question | POLISH, AUDIT, REVIEW | Needed to test argument spine |
| Prior submission history (other outlets, prior JBR R&Rs) | POLISH, RESPOND | Avoids salami / overlap risk |
| AI-use disclosure prepared? | PACKAGE | Required by Elsevier post-2024 |
| Reviewer comments + decision letter (verbatim paste) | RESPOND | Cannot fabricate replies |

For POLISH, SECTION, PACKAGE, and RESPOND, if two or more required fields are missing, halt and list the missing items in a single message. For AUDIT and REVIEW, do not halt solely because the full manuscript is unavailable. Instead run the highest feasible level and label the confidence:

- `QUICK_AUDIT`: title, abstract, keywords, or research question only.
- `STANDARD_AUDIT`: abstract plus introduction, theory, or method excerpt.
- `FULL_AUDIT`: complete manuscript or all main sections.
- `QUICK_REVIEW`: title/abstract/research question only; simulate likely desk-screen and reviewer risks at low confidence.
- `STANDARD_REVIEW`: abstract + introduction + theory/method excerpt; simulate targeted AE and reviewer risks.
- `FULL_REVIEW`: complete manuscript; simulate full AE + Reviewer 1/2/3 reports.

---

## Output Contracts

Each mode has a fixed output schema. Do not deviate.

### POLISH output

```
## Verdict
JBR fit: STRONG / MARGINAL / MIS-FIT (one sentence each: why)
Desk-reject risk: HIGH / MEDIUM / LOW (with triggering rule from jbr_desk_reject_triggers.md, if any)

## Top 3 priorities (ordered by leverage)
1. [issue] → [action] → [expected lift]
2. ...
3. ...

## Section-by-section rewrite
### Abstract
BEFORE: <user text, verbatim>
AFTER:  <revised text>
ANNOTATION: <line-level reasoning, max 6 bullets>

### Introduction
BEFORE / AFTER / ANNOTATION (same pattern)

### Theory & Hypotheses
... (same pattern; show only sections the user supplied)

## Change log
- Added: ...
- Revised: ...
- Removed (with reason): ...
- Flagged [CITATION NEEDED] / [STAT NEEDED]: ...

## Quality score
Theory coherence: __/25
Method-claim alignment: __/25
Contribution clarity: __/25
JBR fit & format: __/25
TOTAL: __/100  (≥80 = ready for next pass; ≥90 = submission-ready)

## AI-use disclosure reminder
This rewrite used AI assistance. Add a disclosure paragraph to your submission per Elsevier 2024 policy. See references/jbr_disclosures_2024.md.
```

### AUDIT output

```
## Audit level
QUICK_AUDIT / STANDARD_AUDIT / FULL_AUDIT
Confidence: LOW / MEDIUM / HIGH
Missing inputs that would change the judgment: ...

## Verdict
## Top 3 priorities
## Quality score (same rubric)
## AI-use disclosure reminder
```
(No section rewrites.)

### REVIEW output

```
## Review level
QUICK_REVIEW / STANDARD_REVIEW / FULL_REVIEW
Confidence: LOW / MEDIUM / HIGH
Missing inputs that would change the judgment: ...

## Simulated editorial decision
Desk reject / Send out for review / Major revision risk / Minor revision risk

## Associate Editor assessment
- JBR fit:
- Likely contribution framing:
- Main desk-reject risk:
- Recommendation:

## Reviewer 1: Theory and Contribution
Major concerns:
Minor concerns:
Required revision:

## Reviewer 2: Method and Evidence
Major concerns:
Minor concerns:
Required robustness or reporting checks:

## Reviewer 3: JBR Fit, Writing, and Implications
Major concerns:
Minor concerns:
Required revision:

## Pre-submission revision priority
1. Must fix before submission
2. Strongly recommended
3. Optional polish

## AI-use disclosure reminder
```

### SECTION output

```
## Diagnosis (3–5 bullets)
## BEFORE
## AFTER
## ANNOTATION (line-level)
## Outstanding flags ([CITATION NEEDED] / [STAT NEEDED])
```

### PACKAGE output

```
## Cover letter (or response letter) draft
## Disclosure checklist (status for each item in jbr_disclosures_2024.md)
## Submission file inventory (blinded MS, title page, declarations, figures, tables, supplementary)
## Final QA
```

### RESPOND output

```
## Overall response (to Editor / AE)
## Point-by-point response (R1 / R2 / R3 ... in order)
  For each: [Comment quoted] / [Response] / [Manuscript change with page/line]
## Manuscript change list (mirror to the response)
## Outstanding disagreements with the reviewer (handled with evidence, not defensiveness)
```

---

## What this skill will NOT do

- Generic English proofreading divorced from JBR fit. Use a dedicated proofreader.
- Literature search or new citation discovery. The user supplies the bibliography.
- Statistical re-analysis or re-running models. The user supplies all numbers.
- Recommending other journals as a primary task (only as an exit ramp when JBR fit is clearly weak).
- Bypassing JBR's policies (page limit, abstract limit, disclosure requirements) at user request.

---

## File map (progressive disclosure)

```
SKILL.md                                ← you are here (always loaded)
references/
  jbr_polishing_pipeline.md             ← POLISH mode primary workflow
  jbr_section_rewrite_playbook.md       ← per-section rewriting templates
  jbr_house_style.md                    ← JBR voice, sentence-level norms
  jbr_claim_evidence_matrix.md          ← anti-overclaim calibration table
  jbr_desk_reject_triggers.md           ← 30-second hard checks
  jbr_disclosures_2024.md               ← AI use / CRediT / DAS / COI
  jbr_reviewer_simulation.md            ← REVIEW mode AE + reviewer simulation
  jbr_scope_and_format.md               ← scope, page/word limits, blinding
  jbr_submission_workflow.md            ← 8-stage submission process
  jbr_track_positioning.md              ← JBR disciplinary-track fit
  jbr_introduction_and_contribution.md  ← intro / contribution standards
  jbr_method_checklists.md              ← per-method evaluation criteria
  methods/
    archival_panel_checklist.md         ← archival/panel-specific method audit
  jbr_real_exemplar_patterns.md         ← pattern catalog from 5 recent JBR
                                          articles (2024–2025), method ×
                                          topic diversified; supersedes the
                                          earlier AI-only exemplar file
  cover_letter_and_response.md          ← letters templates and principles
examples/
  reviewer_response_examples.md         ← R&R response samples
scripts/
  check_abstract_word_count.py          ← mechanical 150-word abstract check
  check_keywords_count.py               ← mechanical 4–6 keyword check
  scan_causal_verbs.py                  ← causal-language calibration scan
agents/
  openai.yaml                           ← runner-side config
CHANGELOG.md                            ← skill version history
```

> **Note on `examples/`:** earlier versions of this skill included three synthetic before/after example files (`abstract_revision_examples.md`, `contribution_statement_examples.md`, `full_intro_before_after.md`). These were removed in v2026.05.b because (a) synthetic examples carry "this-is-my-opinion" risk and (b) their topic content over-fitted to one research domain, harming the skill's reusability. The real-exemplar pattern catalog in `references/jbr_real_exemplar_patterns.md` replaces them with patterns extracted from five published JBR articles, cited for verifiability.

---

## Versioning

This skill is updated as JBR Author Guidelines and Elsevier policy evolve. Each `references/*.md` file carries a `last_verified` date in its header. If a `last_verified` date is older than 6 months and the user is doing a real submission, advise them to spot-check the current JBR Author Guidelines page before sending.
