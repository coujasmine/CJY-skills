# Changelog — jbr-submission-assistant

All notable changes to this skill are listed here. The skill follows a date-based versioning scheme (`YYYY.MM` minor releases; YYYY major).

---

## 2026.05.c — Add review simulation and graded audit workflow

### Why this change
The prior polish-primary release made the skill useful for rewrite work, but pre-submission quality control still needed two capabilities:

1. **Simulated peer review** — users often need to know how a JBR Associate Editor, theory reviewer, methods reviewer, and outlet-fit reviewer may attack a manuscript before submission.
2. **Partial-input diagnosis** — users often provide only an abstract, introduction, or method excerpt. The skill should run the highest feasible audit instead of halting whenever the full manuscript is unavailable.

### Added
- `REVIEW` mode in `SKILL.md`, with a fixed output contract for simulated editorial decision, AE assessment, Reviewer 1/2/3 reports, and pre-submission revision priorities.
- Graded `AUDIT` / `REVIEW` levels:
  - `QUICK_AUDIT` / `QUICK_REVIEW` for title, abstract, keywords, or research question only.
  - `STANDARD_AUDIT` / `STANDARD_REVIEW` for abstract + introduction + theory or method excerpt.
  - `FULL_AUDIT` / `FULL_REVIEW` for complete manuscripts.
- `references/jbr_reviewer_simulation.md` for REVIEW-mode reviewer-role protocol.
- `references/jbr_track_positioning.md` for JBR disciplinary-track fit and positioning.
- `references/methods/archival_panel_checklist.md` for archival/panel-data method scrutiny.
- Lightweight deterministic scripts:
  - `scripts/check_abstract_word_count.py`
  - `scripts/check_keywords_count.py`
  - `scripts/scan_causal_verbs.py`

### Updated
- `SKILL.md` description, routing table, Intake Gate, Hard Rule 10, output contracts, and file map.
- `references/jbr_method_checklists.md` now routes archival/panel manuscripts to the dedicated archival checklist.
- `references/jbr_real_exemplar_patterns.md` no longer points to the removed synthetic `examples/contribution_statement_examples.md` file.
- `agents/openai.yaml` simplified to supported interface fields and a shorter default prompt.

### Behavioral effect
- The skill can now simulate likely JBR review risk without rewriting the manuscript.
- Abstract-only and section-only inputs produce appropriately labeled low/medium-confidence audits rather than immediate stops.
- Archival/panel manuscripts receive finer checks for sample construction, panel timing, fixed effects, endogeneity, text/AI-measure validation, robustness sequencing, and claim calibration.
- UI metadata is cleaner and no longer depends on non-standard `modes` entries.

---

## 2026.05.b — Replace synthetic examples with real-exemplar pattern catalog

### Why this change
The first 2026.05 release added three synthetic before/after example files (`abstract_revision_examples.md`, `contribution_statement_examples.md`, `full_intro_before_after.md`) where I (the skill author / LLM assistant) wrote both the BEFORE and the AFTER text. Two problems with that:

1. **Authority problem** — my AFTER text was my opinion of what JBR rewards, not what JBR has actually published. Synthetic examples carry the "model-author-as-authority" risk.
2. **Reusability problem** — the synthetic content was anchored to one research domain (AI / managerial attention / temporal myopia / exploration-exploitation), so the skill would over-fit to that domain when used for unrelated JBR submissions.

The user identified both issues and provided five real JBR articles spanning five method tiers and topics.

### Removed
- `examples/abstract_revision_examples.md` (synthetic, domain-overfit)
- `examples/contribution_statement_examples.md` (synthetic, domain-overfit)
- `examples/full_intro_before_after.md` (synthetic, single-domain)
- `references/jbr_exemplar_patterns_2025_ai.md` (AI-only; superseded by broader catalog)

### Added
- `references/jbr_real_exemplar_patterns.md` — pattern catalog extracted from five published JBR articles (2024–2025), each tagged `[P1]–[P5]`:
  - **P1** Jiang, Liu & Li (2025) — IB / HQ-Sub dyadic survey, social exchange + identity theory integration
  - **P2** Verginer & Riccaboni (2025) — M&A / staggered DiD on biotech inventors, KBV
  - **P3** Ran, Zhang, Yang & Chen (2024) — strategy / Chinese panel + multi-FE, RBV with mediators and opposite-sign moderators
  - **P4** Valtonen et al. (2025) — AI–wellbeing survey, JD-R, honest null direct effect
  - **P5** Kyriakopoulos et al. (2025) — DT+AI / NPD, PLS-SEM, opposite-sign moderation as contribution
- Patterns are organized into nine sections (intro, theory, hypotheses, method, results, discussion, disclosures, method-tier routing, structural invariants).
- Every pattern carries a paper tag for verification; paraphrased per Elsevier copyright (no quotation >15 words).

### Updated
- `SKILL.md` routing table — modes POLISH, AUDIT, SECTION, PACKAGE now point to `jbr_real_exemplar_patterns.md` instead of synthetic `examples/*` files.
- `SKILL.md` file map — reflects the new structure with a note explaining why synthetic examples were removed.

### Behavioral effect
- **POLISH and SECTION mode outputs now anchor to observed JBR patterns**, not to invented examples. The skill will say "this matches Pattern 1.3 observed in [P1] and [P5]" rather than "this matches my proposed Example 2."
- **The skill is now genuinely reusable across domains.** A user polishing a marketing paper, an M&A paper, or an AI-management paper will pull from the same multi-domain exemplar pool.
- **Hard Rule 1 (no fabricated citations)** is now reinforced by the exemplar file itself: all patterns cite back to verifiable published papers.

---

## 2026.05 — Polish-mode pivot (breaking change to invocation model)

### Reframed
- **Primary purpose** changed from *diagnostic-only* to *polish-then-package*. The skill now produces a section-by-section rewritten draft by default, not just an audit.
- Skill operates in **five explicit modes** (POLISH default, AUDIT, SECTION, PACKAGE, RESPOND), each with a fixed output schema.

### Added (new reference files)
- `references/jbr_polishing_pipeline.md` — seven-stage primary workflow for POLISH mode.
- `references/jbr_desk_reject_triggers.md` — mechanical 30-second hard-check list (A–G categories: scope, format, disclosures, spine, method-claim, originality, special-issue).
- `references/jbr_section_rewrite_playbook.md` — per-section templates with DO/DON'T, opening moves, length budgets, forbidden moves.
- `references/jbr_claim_evidence_matrix.md` — design-to-claim calibration table; verb swap table; mediation/moderation/generalization language.
- `references/jbr_house_style.md` — sentence-level and paragraph-level JBR conventions; style red-flag list.
- `references/jbr_disclosures_2024.md` — six standard disclosures (AI use, CRediT, DAS, COI, funding, ethics) with templates and validation criteria.

### Rewritten (existing files)
- `SKILL.md` — full rewrite: progressive-disclosure file map, ten Hard Rules (anti-fabrication, anti-overclaim, anti-voice-erasure), Intake Gate with required fields, mode-specific output contracts, "what this skill will NOT do" boundary.
- `agents/openai.yaml` — default prompt rewritten for POLISH default; modes listed.
- `examples/abstract_revision_examples.md` — replaced abstract pattern-description with three full before/after rewrites (panel archival, cross-sectional survey, multi-case qualitative), each annotated line-by-line.
- `examples/contribution_statement_examples.md` — replaced template fragments with six full before/after paragraphs covering all six contribution types (mechanism, boundary, integration, reconciliation, contextualization, clarification).

### Added (new examples)
- `examples/full_intro_before_after.md` — one complete six-paragraph introduction rewritten end-to-end with paragraph-level annotation, quality scoring, and explicit `[CITATION NEEDED]` flags.

### Maintained (no change)
- `references/jbr_scope_and_format.md`
- `references/jbr_submission_workflow.md`
- `references/jbr_introduction_and_contribution.md`
- `references/jbr_method_checklists.md`
- `references/jbr_exemplar_patterns_2025_ai.md`
- `references/cover_letter_and_response.md`
- `examples/reviewer_response_examples.md`

These remain useful but are no longer the primary entry points — they are loaded conditionally by the routing table in `SKILL.md`.

### Key behavioral changes vs. prior version

| Behavior | Before (2026.04) | After (2026.05) |
|---|---|---|
| Default action on invocation | Audit / diagnose | Polish (diagnose + rewrite) |
| Output shape | Free-form prose | Mode-specific fixed schema with quality score |
| Citation fabrication | Possible (no hard rule) | Forbidden (Hard Rule 1; `[CITATION NEEDED]` placeholder) |
| Causal language calibration | Implicit | Explicit matrix (`jbr_claim_evidence_matrix.md`) |
| Post-2024 Elsevier disclosures | Not covered | Required (`jbr_disclosures_2024.md`) |
| Desk-reject screening | Implicit in workflow | Stage 1 mechanical check (`jbr_desk_reject_triggers.md`) |
| Examples format | Pattern descriptions | Full before/after with annotation |

### Migration notes for users

- If you previously invoked the skill with "audit my paper," it now produces a **full rewrite by default**. To get the old behavior, request AUDIT mode explicitly.
- If you use the skill in an automated pipeline, switch the entry point to the routing table in `SKILL.md` and read only the files for your active mode (not all references).
- Add an AI-use disclosure to any submission that passed through this skill, per Elsevier post-2024 policy. See `references/jbr_disclosures_2024.md` for the template.

---

## 2026.04 — Initial release

- Created the skill as a JBR-oriented manuscript diagnostician.
- Six reference files; three example files; OpenAI agent config.
- Single-mode invocation; free-form output.
