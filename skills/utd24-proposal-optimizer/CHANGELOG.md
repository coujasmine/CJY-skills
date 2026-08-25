# utd24-proposal-optimizer — Changelog

## 2026.08.a — Academic storytelling coherence upgrade

This release integrates academic storytelling as a cross-dimensional coherence
diagnostic. It does **not** add a sixth score or change the equal-weighted
five-dimension rubric.

### New reference

- **`references/utd24_storytelling_architecture.md`**: operationalizes the
  gap→knot distinction, theory-as-rising-tension structure, methods/results as
  credible resolution, and Discussion as a specific before→after change in
  theoretical understanding. Adds a five-part Story Coherence Gate, mode-specific
  IDEA/MANUSCRIPT/REVIEW workflows, pruning rules, and output templates. Based on
  Pollock (2021), Chapter 2, and the user-supplied Chinese interpretive article.

### New deterministic check

- **`scripts/check_story_coherence.py`**: bilingual English/Chinese candidate
  locator for gap-only, knot/tension, resolution/mechanism, and before-after
  signals. Marker counts never determine gate results; qualitative evaluation
  remains authoritative.

### SKILL.md integration

- Added storytelling/coherence discovery triggers.
- Added conditional routing for the new reference in IDEA, MANUSCRIPT, and REVIEW.
- Added a cross-dimensional Story Coherence Gate without changing `/100` scoring.
- Extended IDEA, MANUSCRIPT, and REVIEW output contracts with conditional story
  spine / gate blocks.
- Added Hard Rule 13: coherence never overrides evidence.
- Updated deterministic-check table, file map, and conditional-loading rules.

## 2026.06.a — P0 capability upgrade (ex-ante workflows + outlet calibration + context lineages)

This release closes the four largest gaps identified in the May 2026 audit: the skill was originally ex-post-only (audit after writing), outlet-uniform (one bar for all UTD24 outlets), and Western-mainstream-only (no Chinese-context or AI-strategy lineages). 2026.06.a adds ex-ante workflows and reorients the rubric to outlet-conditioned scoring.

### New mode: DESIGN

- **SKILL.md**: added DESIGN as the 2nd mode (between IDEA and MANUSCRIPT), with full routing table entry and output contract. Used when user has RQ + parent theory but no method commitment.

### New references

- **`references/utd24_design_choice_tree.md`** (P0-3a): ex-ante design choice tree — Decision Tree A (by claim type: causal / mechanism / boundary / process / theoretical), Decision Tree B (by data accessibility), Tree C (sample design), Tree D (measurement), Tree E (endogeneity decision matrix), plus pre-registration recommendations
- **`references/utd24_qual_mixed_design.md`** (P0-3b): qualitative and mixed-methods acceptance criteria for UTD24 outlets — Gioia method, Langley process-study strategies, Eisenhardt multi-case, mixed-methods designs MM1-MM4, outlet-specific calibration for ASQ / AMJ / OS / SMJ
- **`references/utd24_hypothesis_patterns.md`** (P0-4b): writing templates for 10+ hypothesis architectures — linear, mediation (M1, M2 serial), moderation (Mod1-Mod3 simple / moderated-mediation / dual-pathway), non-linear (NL1 inverted-U with Haans-Pieters-He checks, NL2 U, NL3 threshold), configurational (C1 congruence, C2 QCA), AMR propositions (P1-P3); outlet × pattern compatibility matrix
- **`references/utd24_chinese_context_lineage.md`** (P0-2a): 8 Chinese-context / emerging-market lineages (F1-F8) — institutional voids (Khanna-Palepu), state-firm relations / political ties, guanxi (Park-Luo, Xin-Pearce), family firms (Bertrand-Schoar, Carney), institutional transitions (Peng-Heath), network capitalism (Boisot-Child, Keister), EMNCs (Mathews, Luo-Tung), Confucian cultural values; plus "Chinese context risk" detection
- **`references/utd24_ai_strategy_lineage.md`** (P0-2b): 8 AI × Strategy emerging lineages (G1-G8) — human-AI complementarity (Raisch-Krakowski, Choudhury), algorithmic decision-making (Lindebaum, Murray), cognitive strategy in AI contexts (Csaszar extensions), TMT AI literacy (upper-echelons extension), digital strategy (Vial, Verhoef), platform strategy with AI, AI in innovation / R&D, AI-driven entrepreneurship; plus fashion-chase prevention 5-check

### Updated references

- **`references/utd24_rubric.md`** (P0-1): added "Outlet-conditioned floor" section — per-dim floor for SMJ / AMJ / ASQ / OS / MS / AMR / Strategy Science (e.g., SMJ Dim 5 floor 18; ASQ Dim 3 floor 18; AMR Dim 5 N/A with logical-consistency substitution; OS Dim 1 floor 17 for originality). Score interpretation now applies after outlet-floor check.
- **`references/utd24_hypothesis_architecture.md`** (P0-4a): added Mechanism→Hypothesis Derivation Workflow — 5-step ex-ante derivation (lock causal pathway → identify architecture from claim-type → predict directions → write 3-layer chain → audit). Cross-references new patterns file.
- **`references/utd24_strategy_innovation_entrepreneurship_lineages.md`** (P0-2c): added "Recent-anchor search guide" with per-lineage concept-term table; added pointers to Chinese context and AI strategy companion files; updated `[CITATION NEEDED]` notes to point to the search guide rather than leaving the user without direction.

### SKILL.md restructuring

- **Modes table**: expanded to 4 modes; updated file-loading list per mode with conditional companion-lineage loading
- **Calibration baseline**: added Strategy Science to outlet list; reorganized lineages to mention Chinese and AI companion files; added "Outlet-conditioned per-dim floor" sub-section pointing to rubric
- **Intake Gate**: added "Hypothesis architecture", "Data accessibility" fields; expanded "Target outlet preference" to include Strategy Science; added "Project context detection" sub-section for scanning `venue-stage/`, `研究项目/`, etc.
- **Output Contracts**: added DESIGN output template
- **Cross-skill Handoff**: new section — explicit routing to `theory-positioning`, `hypothesis-builder`, `contribution-stress-test`, `venue-fit`, `research-lit`, `auto-review-loop`, `paper-plan`, `jbr-submission-assistant`, `strategy-science-submission-assistant`, `research-wiki`; with handoff etiquette and reverse-handoff notes
- **File map**: updated to reflect 5 new reference files; added conditional-loading rules

### Hard Rule status

All 12 Hard Rules from 2026.05.a unchanged and continue to apply. P0-2 deliberately does not fabricate "recent UTD24 anchors" for lineages — instead provides search-query templates so the user supplies them, respecting Hard Rule 1.

### Migration notes

- Existing IDEA / MANUSCRIPT / REVIEW invocations: backward compatible. The new outlet-conditioned floor adds an extra check step but does not change rubric scoring. The new conditional-lineage loading triggers when phenomenon involves China or AI; otherwise behaves as before.
- New DESIGN mode: must be invoked explicitly by user signal ("how should I design", "DiD vs PSM", etc.) or by the skill noticing the user is pre-data-commitment in IDEA.

### Known limitations of 2026.06.a (deferred to 2026.07 / P1)

- No `utd24_lit_review_workflow.md` yet (P1-5): no ex-ante anchor-paper identification workflow, no gap-type diagnostic table, no interlocutor mapping template
- Scripts not expanded (P1-8): construct-validity scan, discussion-engagement scan, abstract-contribution scan deferred
- No `utd24_outlet_method_matrix.md` (P1-9): cross-cutting outlet × method tier matrix only embedded in design tree, not standalone
- No worked examples (P2-10): BEFORE → AFTER full case studies deferred
- Project-context detection is documented in SKILL.md but no helper script yet; the skill scans manually

---

## 2026.05.a — initial release

- **SKILL.md**: 3 modes (IDEA / MANUSCRIPT / REVIEW), 12 Hard Rules, Intake Gate, 5-dim rubric structure, output contracts, file map
- **references/utd24_rubric.md**: 5 dimensions × 4 sub-criteria, scoring anchors, total-score interpretation
- **references/utd24_strategy_innovation_entrepreneurship_lineages.md**: 14 parent-theory lineages across strategy / behavioral / innovation / entrepreneurship; mis-application warnings; integration patterns
- **references/utd24_rq_criteria.md**: Dim 1 deep-dive — patterns P1-P4, failure modes F1-F6, IDEA-mode variant generation guidance
- **references/utd24_lit_conversation.md**: Dim 2 deep-dive — anchoring tests, contribution-framing template, conversation-visibility patterns V1-V3
- **references/utd24_mechanism_audit.md**: Dim 3 deep-dive — mechanism 4-property test, falsifiability tests F1-F3, analogy-as-mechanism rewrite template
- **references/utd24_hypothesis_architecture.md**: Dim 4 deep-dive — 3-layer chain, count diagnostic, alignment audit, HARKing indicators
- **references/utd24_methods_identification.md**: Dim 5 deep-dive — identification↔verb matching table, construct-validity audit, robustness coverage, alternative-explanation empirical engagement
- **references/utd24_desk_reject_triggers.md**: 16 triggers T1-T16 with detection cues, severity, affected dimensions, quick fixes
- **references/utd24_reviewer_simulation.md**: AE / R1 (Theory) / R2 (Method) / R3 (Positioning) / Devil's Advocate personas + synthesis schema
- **references/utd24_exemplar_patterns.md**: pattern catalog (extension / integration / reconciliation / boundary patterns; method patterns; intro hook patterns; contribution paragraph patterns) + user-supplied exemplar slot schema
- **scripts/scan_causal_overclaim.py**: regex-based scan for causal verbs (causes / leads to / drives / etc.)
- **scripts/scan_analogy_markers.py**: regex-based scan for analogy markers (similar to / akin to / mirrors / etc.)
- **scripts/check_hypothesis_count.py**: hypothesis label detection (H1, Hypothesis 2a, etc.) + UTD24-norm scope-creep flag

### Calibration baseline at release
- Outlets: SMJ (core), AMJ, ASQ, OS, MS (Strategy/Innovation/Entrepreneurship sections), AMR
- Topic scope: strategy / innovation / entrepreneurship management research
- Out of scope: pure OB micro, pure marketing, pure finance, pure accounting, methodological papers
