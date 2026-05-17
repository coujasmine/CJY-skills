# Changelog — jbr-submission-assistant

All notable changes to this skill are listed here. The skill follows a date-based versioning scheme (`YYYY.MM` minor releases; YYYY major).

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
