---
file: ss_polishing_pipeline.md
purpose: Primary workflow for POLISH mode. Defines the eight-stage pipeline that turns a user draft into a Strategy Science submission-ready manuscript.
last_verified: 2026-05-21
---

# Strategy Science Polishing Pipeline (POLISH mode)

## Contents

- Stage 0 — Intake & Routing (≤2 minutes of model time)
- Stage 1 — Desk-Reject Triage (≤30 seconds)
- Stage 2 — Argument Spine Audit
- Stage 2.5 — Lineage Anchoring Check (SS-specific)
- Stage 3 — Theory & Theoretical Movement Strengthening
- Stage 4 — Method ↔ Claim Calibration
- Stage 5 — LLM-Measurement Audit (conditional)
- Stage 6 — Section-by-Section Rewrite
- Stage 7 — SS House-Style Pass (sentence-level)
- Stage 8 — Disclosures, Format, Submission Sanity
- Output Assembly
- Iteration Discipline


This is the **primary workflow** of the skill. When the user invokes POLISH mode, run these stages in order. Each stage has a gate: do not advance until the gate is met. If a stage fails the gate, halt and surface the failure to the user rather than papering over it.

> Polishing here means **rigor-first revision**: the goal is to make the argument, evidence, and theoretical movement tighter and SS-calibrated, not to make the prose prettier. Sentence-level polish happens last, in Stage 7.

> **SS-specific emphasis:** Compared to JBR's pipeline, SS polishing places extra weight on (a) theoretical-movement clarity (Stage 3) and (b) lineage anchoring (Stage 2.5). A manuscript that would clear JBR with a clean phenomenon and finding will not clear SS without a stated theoretical movement against a named lineage.

---

## Stage 0 — Intake & Routing (≤2 minutes of model time)

Confirm the Intake Gate (SKILL.md). Required minimum:

- Target = SS regular OR specific special issue (with call URL/deadline if SI)
- Submission stage = first / R&R / reposition
- Manuscript (full or section) + method tier + primary theoretical lineage + research question
- AI/LLM use declared (writing vs. measurement vs. both)

If any required item is missing, **halt and ask**. Do not infer.

Then classify what is supplied:
- Full manuscript? → run all stages
- Single section (intro, abstract, theory, method, results, discussion)? → skip to Stage 6 SECTION mode (see `ss_section_rewrite_playbook.md`); but still flag scope/fit issues at Stage 1 if visible
- Pure-theory paper (no empirics)? → skip Stage 4 method↔claim; instead run `methods/formal_theory_checklist.md` at Stage 4

**Gate:** Intake satisfied. If not, halt.

---

## Stage 1 — Desk-Reject Triage (≤30 seconds)

Run `references/ss_desk_reject_triggers.md` as a fast hard-check. Any single HIGH trigger fires → escalate to user immediately.

Run the mechanical checks with the bundled scripts rather than estimating by eye — a 310-word abstract reads as "about 300" but still trips the format trigger:

- `python3 scripts/check_abstract_word_count.py <abstract>` — manuscript abstract <=200 words; ScholarOne field <=250 words
- `python3 scripts/check_keywords_count.py "<kw1; kw2; ...>"` — official 3-10 keywords

Common SS triggers (full list in `ss_desk_reject_triggers.md`):
- Manuscript abstract >200 words or ScholarOne abstract field >250 words
- No primary theoretical lineage named in introduction
- "Contribution" paragraph lists 3+ vague items
- Cross-sectional design making "causes" claim
- LLM-as-measurement without inter-rater reliability against humans
- Pure-theory paper without typology/framework summary
- Mis-fit lineage (paper would be at home at another outlet)
- AI-use disclosure missing
- IRB statement missing (for human-subjects work)

**Gate:** No HIGH-severity trigger fires, or user has confirmed they will fix the trigger before submission.

If a trigger fires, write a short "Desk-reject risk" note at the top of the output (this satisfies the POLISH output schema's "Verdict" block) and continue with the rest of the polish — but flag clearly that the trigger must be resolved before submission, regardless of polish quality.

---

## Stage 2 — Argument Spine Audit

Test whether one stable storyline runs through the manuscript:

```
Strategic problem / theoretical tension
  ↓
Named primary theoretical lineage
  ↓
Research question (RQ)
  ↓
Theoretical framework + hypotheses (or propositions for theory papers)
  ↓
Empirical design (data + method) or Analytical design (model + assumptions)
  ↓
Findings (empirical) or Predictions (theory)
  ↓
Theoretical movement claim (extension/integration/boundary/mechanism/new-construct)
  ↓
Practical implications
```

For each adjacent pair, ask: **does the lower follow from the upper?**

Common spine breaks at SS:
- Intro problem ≠ RQ (e.g., intro frames AI capability, but RQ asks about user behavior)
- RQ ≠ hypotheses (e.g., RQ asks "how" but hypotheses test "whether")
- Hypotheses ≠ design (e.g., H3 is a within-firm mechanism, but data is cross-firm)
- Findings ≠ theoretical movement (e.g., null direct effect, but contribution still says "we show AI improves performance" — Kanis et al. 2026 handles this honestly by reframing nulls as "a cautionary case for LLM effectiveness")
- Theoretical movement ≠ implications (e.g., movement is a boundary refinement, but implications are unrelated managerial advice)
- Findings present but no theoretical movement articulated (the "JBR-pattern" desk-reject for SS)

**Gate:** The spine holds end-to-end. If not, name the broken link and the minimum revision needed. Do not proceed to section rewriting until the user either fixes the spine or explicitly accepts the break.

---

## Stage 2.5 — Lineage Anchoring Check (SS-specific)

Use `references/ss_track_positioning.md` to verify the primary theoretical lineage:

1. Identify the primary lineage (Carnegie, mental representations, strategic human capital, ecosystems, dynamic capabilities, TCE, formal/game-theoretic, AI in strategy, acquisitions).
2. Confirm that the lineage's anchor citations appear in the introduction's first 2-3 pages.
3. Confirm that the supporting theories (if any) are clearly auxiliary, not parallel primary lineages.
4. Cross-check lineage vs. method: e.g., a mental-representations paper using a single-source CEO survey is a method-theory mismatch.

If the lineage is unclear or mis-fit:
- HIGH issue → mark as desk-reject risk
- Propose re-anchoring (5-10 anchor citations from the closest SS lineage)
- If re-anchoring is impossible, propose retargeting to SMJ / OS / AMJ / AMD

**Gate:** Primary lineage is named, anchored, and consistent with method.

---

## Stage 3 — Theory & Theoretical Movement Strengthening

Use `references/ss_introduction_and_contribution.md` and `references/ss_track_positioning.md`.

Checks:
- **Primary theoretical lineage** is named and visible by page 2 of the intro
- **Supporting lineages** are clearly auxiliary (not parallel primaries)
- **Mechanisms** are explicit: every hypothesis (or proposition for theory papers) names the cognitive/structural/strategic logic, not just the direction
- **Boundary conditions** appear when the paper has moderators or contextual contingencies (Asghar et al. introduce financial market volatility; Clough introduces environmental dynamism, systemic uncertainty, demand heterogeneity)
- **Counter-arguments** are addressed (not buried in limitations). Both Kanis and Asghar engage cognitive-overload counter-arguments before stating their predictions.
- **Hypotheses are falsifiable** (can be rejected by the data; not tautological)
- **Theoretical movement** is named explicitly in the contribution paragraph: extension / mechanism specification / boundary refinement / integration / reconciliation / new construct. SS rejects vague "we contribute to the literature on X" framings.

For each weak hypothesis, propose a rewrite that adds the missing element (mechanism, boundary, counter-argument). Do not invent theory the user has not signaled they want.

For pure-theory papers, this stage becomes:
- Are the building blocks defined precisely (Clough defines coordination speed and coordination scope)?
- Are the assumptions of the formal model stated?
- Does the typology / framework have a parsimonious summary (table or figure)?
- Are the testable predictions stated for future empirical work?

**Gate:** Each hypothesis has a stated mechanism; the contribution paragraph names one or two specific theoretical movements (not a list of three vague claims).

---

## Stage 4 — Method ↔ Claim Calibration

Use `references/ss_claim_evidence_matrix.md` to verify each claim is matched to its design's claim-strength ceiling.

Run `python3 scripts/scan_causal_verbs.py <manuscript>` first so no causal verb is missed in a manual sweep. For every verb the scan flags (causes, leads to, produces, drives, generates, results in, enables, determines, demonstrates), check the design row in the matrix. The scan only locates candidates — a verb backed by credible identification (DiD, IV, RDD, well-randomized experiment) is correct and should be kept. If the design does not support the verb, propose a softened verb.

Other method checks (see `references/ss_method_checklists.md` and method-specific files):
- Construct definitions precede measures
- Level-of-analysis consistency across theory / variables / models
- Sampling rationale tied to the phenomenon, not convenience (the "fruit fly" argument — Asghar et al. justify insider trading as a foresight context)
- Robustness checks target plausible threats (alt measures, alt models, alt lag structures, alt samples), not arbitrary additions
- Reporting order: descriptive stats → correlations → main test → robustness → additional analyses
- For experimental work: manipulation checks, attention checks, randomization checks, exclusion criteria, pre-registration link
- For archival panel: identification strategy, FE structure, clustering, alternative IVs/lags
- For LLM-as-measurement: multi-LLM sensitivity, Krippendorff α against human coders, validation set separation (see `gpt_measurement_validation.md`)
- For ML-as-prediction: train-test split, baseline benchmarks (OLS or simpler), feature importance reporting, hyperparameter tuning
- For pure-theory: assumption clarity, equilibrium uniqueness, sensitivity to assumptions

**Gate:** No claim exceeds what the design can support; flagged issues are listed for user review.

For pure-theory papers, this stage uses `methods/formal_theory_checklist.md` instead:
- Are propositions stated formally (or as clearly identifiable conjectures)?
- Are proofs in main text or appendix (Clough uses typology arguments rather than formal proofs)?
- Are the assumptions defended substantively, not just stipulated?

---

## Stage 5 — LLM-Measurement Audit (conditional)

If the user reports using LLMs to code, classify, or measure a construct (Kanis et al. used three LLMs to classify pros/cons into strategic categories), run the eight-dimension scorecard in `references/gpt_measurement_validation.md`:

1. Construct definition before measurement
2. Prompt engineering hygiene (system prompts, batching, version pinning)
3. Development/validation set separation
4. Human benchmark and inter-rater reliability (Krippendorff α or κ)
5. Convergent and discriminant validity
6. Sensitivity to alternative LLMs and prompts
7. False-positive / hallucination review
8. Reporting and disclosure

If any dimension is missing or below threshold (e.g., α < 0.80), flag as HIGH for SS submission. The skill does not estimate metrics the manuscript does not report.

**Gate:** Scorecard is complete; either all dimensions pass, or the missing dimensions are flagged as [MEASUREMENT EVIDENCE NEEDED].

---

## Stage 6 — Section-by-Section Rewrite

Now run each section through `references/ss_section_rewrite_playbook.md`. Order:

1. Abstract (rewrite **last** in practice — but list first in the output since readers see it first; loop back after Stage 6.6 to harmonize the abstract with the final intro/discussion)
2. Introduction
3. Theory & Hypotheses (or Theoretical Background / Theoretical Framework for theory papers)
4. Method
5. Results
6. Discussion (overview, theoretical implications, managerial/practical implications, limitations, future research)
7. Title + keywords (last; mirror the final abstract)

For each section:
- BEFORE = user's text, verbatim
- AFTER = rewritten text
- ANNOTATION = up to 6 bullets explaining why each substantive change was made
- Preserve voice (Hard Rule 6); preserve all of the user's own citations; flag missing or weak citations as `[CITATION NEEDED: <what>]`

**Gate:** Every supplied section has a BEFORE / AFTER / ANNOTATION block.

---

## Stage 7 — SS House-Style Pass (sentence-level)

Apply `references/ss_house_style.md` to the AFTER text:
- INFORMS citation style (Author year, no comma)
- Hypotheses in bold-italic with "(H1a)" labels
- Standard errors in parentheses, not t-statistics
- Theory-paper voice: "we propose / we argue / the framework predicts" — not "we show empirically"
- Empirical-paper voice: "we find" only in results; "we argue" / "we theorize" in theory section
- Sentence-level: short topic sentences; named-theory anchors in first sentence of each theoretical subsection
- Definitions on first use; consistent terminology thereafter
- Numerals follow INFORMS conventions
- Hedging only where the design requires it (not as default insurance)

**Gate:** The AFTER text reads like SS prose (calibrated against the 4 exemplars), not generic management dissertation prose.

---

## Stage 8 — Disclosures, Format, Submission Sanity

Verify (see `references/ss_disclosures.md` and `references/ss_scope_and_format.md`):
- AI-use disclosure paragraph drafted (this skill counts as AI assistance)
- Author-contribution statement (CRediT-style or "All authors contributed equally")
- Data Availability Statement
- Conflict of interest statement
- Funding statement
- IRB/ethics statement (if human/animal subjects)
- Pre-registration link, anonymized (if pre-registered)
- Manuscript abstract <=200 words; ScholarOne abstract field <=250 words
- Keywords 3-10
- Blinded manuscript (no author identifiers, no acknowledgements that reveal identity, no self-citations in the form "in our earlier work, X")
- Title page separate, with full author info
- Tables/figures with SE in parentheses, INFORMS-style notes
- References in INFORMS author-year style
- Hypothesis labels in bold-italic INFORMS style

Re-run the mechanical scripts on the final draft so the format checklist reflects the polished text:

- `python3 scripts/check_abstract_word_count.py <final abstract>`
- `python3 scripts/check_keywords_count.py "<final keywords>"`

**Gate:** A "Disclosure & Format Checklist" is produced with status (✓ ready / ✗ missing) for each item.

---

## Output Assembly

Assemble the final POLISH output per the schema in SKILL.md:

1. Verdict (fit, theoretical movement, desk-reject risk)
2. Top 3 priorities
3. Section-by-section BEFORE / AFTER / ANNOTATION
4. AI decontamination block
5. Change log
6. Quality score (0-100, four sub-scores: theoretical contribution & movement / method-claim alignment / argument spine coherence / SS fit & INFORMS format)
7. AI-use disclosure reminder

---

## Iteration Discipline

Polishing is iterative. Each invocation of POLISH should produce one **complete** pass. If the user wants a second pass:

- Pass 2: focus only on issues unresolved in pass 1's change log (do not re-touch sections that scored ≥22/25 on their relevant sub-score)
- Pass 3 (rare): final harmonization — abstract ↔ intro ↔ discussion ↔ cover letter

Hard stop at 3 passes. If the manuscript still scores < 80, the problem is not polish-able; it requires re-running Stages 2-4 (spine + lineage + theoretical movement + method-claim), which is a substantive revision the user must lead.
