---
file: jbr_polishing_pipeline.md
purpose: Primary workflow for POLISH mode. Defines the seven-stage pipeline that turns a user draft into a JBR-submission-ready manuscript.
last_verified: 2026-05-17
---

# JBR Polishing Pipeline (POLISH mode)

This is the **primary workflow** of the skill. When the user invokes POLISH mode, run these stages in order. Each stage has a gate: do not advance until the gate is met. If a stage fails the gate, halt and surface the failure to the user rather than papering over it.

> Polishing here means **rigor-first revision**: the goal is to make the argument, evidence, and contribution tighter and JBR-calibrated, not to make the prose prettier. Sentence-level polish happens last, in Stage 6.

---

## Stage 0 — Intake & Routing (≤2 minutes of model time)

Confirm the Intake Gate (SKILL.md). Required minimum:

- Target = JBR regular OR specific special issue (with call URL/deadline if SI)
- Submission stage = first / R&R / reposition
- Manuscript (full or section) + method tier + primary theory + research question

If any required item is missing, **halt and ask**. Do not infer.

Then classify what is supplied:
- Full manuscript? → run all stages
- Single section (intro, abstract, theory, method, results, discussion)? → skip to Stage 5 SECTION mode (see `jbr_section_rewrite_playbook.md`); but still flag scope/fit issues at Stage 1 if visible

**Gate:** Intake satisfied. If not, halt.

---

## Stage 1 — Desk-Reject Triage (≤30 seconds)

Run `references/jbr_desk_reject_triggers.md` as a fast hard-check. Any single trigger fires → escalate to user immediately.

Common triggers:
- Abstract > 150 words or < 100 words
- Manuscript > 45 double-spaced pages (full submission)
- No business decision / managerial / market / organizational anchoring
- No identifiable primary theory in introduction
- Convenience sample with no theoretical justification
- AI-use disclosure missing (post-2024 Elsevier requirement)
- Significant overlap with a prior published paper by the same authors (>30% text/data)
- Method ↔ claim mismatch (e.g., cross-sectional design making "causes" claim)

**Gate:** No HIGH-severity trigger fires, or user has confirmed they will fix the trigger before submission.

If a trigger fires, write a short "Desk-reject risk" note at the top of the output (this satisfies the POLISH output schema's "Verdict" block) and continue with the rest of the polish — but flag clearly that the trigger must be resolved before submission, regardless of polish quality.

---

## Stage 2 — Argument Spine Audit

Test whether one stable storyline runs through the manuscript:

```
Business problem
  ↓
Theoretical tension / unresolved mechanism
  ↓
Research question (RQ)
  ↓
Theory + hypotheses (or propositions)
  ↓
Empirical design (data + method)
  ↓
Findings
  ↓
Contribution claims
  ↓
Practical implications
```

For each adjacent pair, ask: **does the lower follow from the upper?**

Common spine breaks:
- Intro problem ≠ RQ (e.g., intro frames AI ethics, but RQ asks about AI capability ROI)
- RQ ≠ hypotheses (e.g., RQ asks "how" but hypotheses test "whether")
- Hypotheses ≠ design (e.g., H3 is a within-firm mechanism, but data is cross-firm)
- Findings ≠ contribution claim (e.g., null direct effect, but contribution still says "we show AI improves performance")
- Contribution ≠ implications (e.g., contribution is theoretical, but implications are unrelated practitioner advice)

**Gate:** The spine holds end-to-end. If not, name the broken link and the minimum revision needed. Do not proceed to section rewriting until the user either fixes the spine or explicitly accepts the break.

---

## Stage 3 — Theory & Hypotheses Strengthening

Use `references/jbr_introduction_and_contribution.md` and JBR's editorial philosophy (`references/jbr_scope_and_format.md`).

Checks:
- **Primary theoretical conversation** is named and visible by page 2 of the intro
- **Supporting theories** are clearly auxiliary (not parallel primaries)
- **Mechanisms** are explicit: every hypothesis names the causal/mediating logic, not just the direction
- **Boundary conditions** appear when the paper has moderators or contextual contingencies
- **Counter-arguments** are addressed (not buried in limitations)
- **Hypotheses are falsifiable** (can be rejected by the data; not tautological)

For each weak hypothesis, propose a rewrite that adds the missing element (mechanism, boundary, counter-argument). Do not invent theory the user has not signaled they want.

**Gate:** Each hypothesis has a stated mechanism and is consistent with the chosen theory.

---

## Stage 4 — Method ↔ Claim Calibration

Use `references/jbr_claim_evidence_matrix.md` to verify each claim is matched to its design's claim-strength ceiling.

For every causal-sounding verb in the manuscript (causes, leads to, produces, drives, generates, results in, makes, gives rise to), check the design row in the matrix. If the design does not support the verb, propose a softened verb (associated with, predicts, is linked to, conditional on, consistent with).

Other method checks (see `references/jbr_method_checklists.md`):
- Construct definitions precede measures
- Level-of-analysis consistency across theory / variables / models
- Sampling rationale tied to the phenomenon, not convenience
- Robustness checks target plausible threats (alt measures, alt models, alt lag structures, alt samples), not arbitrary additions
- Reporting order: descriptive stats → correlations → main test → robustness
- For survey work: CMV remedies (procedural + statistical), informant rationale
- For experimental work: manipulation checks, attention checks, randomization checks
- For qualitative work: theoretical case selection, triangulation, coding ladder

**Gate:** No claim exceeds what the design can support; flagged issues are listed for user review.

---

## Stage 5 — Section-by-Section Rewrite

Now run each section through `references/jbr_section_rewrite_playbook.md`. Order:

1. Abstract (rewrite **last** in practice — but list first in the output since readers see it first; loop back after Stage 5.6 to harmonize the abstract with the final intro/discussion)
2. Introduction
3. Theory & Hypotheses
4. Method
5. Results
6. Discussion (theoretical implications, practical implications, limitations, future research)
7. Title + keywords (last; mirror the final abstract)

For each section:
- BEFORE = user's text, verbatim
- AFTER = rewritten text
- ANNOTATION = up to 6 bullets explaining why each substantive change was made
- Preserve voice (Hard Rule 6); preserve all of the user's own citations; flag missing or weak citations as `[CITATION NEEDED: <what>]`

**Gate:** Every supplied section has a BEFORE / AFTER / ANNOTATION block.

---

## Stage 6 — JBR House-Style Pass (sentence-level)

Apply `references/jbr_house_style.md` to the AFTER text:
- Business-relevant vocabulary; minimize abstract academic jargon
- Active voice in introduction and discussion; passive acceptable in methods
- Short topic sentences; consequence-first paragraph structure
- Definitions on first use; consistent terminology thereafter
- Numerals follow APA/Elsevier conventions
- Hedging only where the design requires it (not as default insurance)

**Gate:** The AFTER text reads like JBR prose, not generic dissertation prose.

---

## Stage 7 — Disclosures, Format, Submission Sanity

Verify (see `references/jbr_disclosures_2024.md` and `references/jbr_scope_and_format.md`):
- AI-use disclosure paragraph drafted (this skill counts as AI assistance)
- CRediT contributor statement structure
- Data Availability Statement
- Conflict of interest statement
- Funding statement
- ICMJE-style ethics/IRB statement (if human/animal subjects)
- Page/word limits respected
- Blinded manuscript (no author identifiers, no acknowledgements that reveal identity, no self-citations in the form "in our earlier work, X")
- Title page separate, with full author info
- Figures/tables placed per JBR convention
- Keywords: 4–6, mapped to JBR's audience

**Gate:** A "Disclosure & Format Checklist" is produced with status (✓ ready / ✗ missing) for each item.

---

## Output Assembly

Assemble the final POLISH output per the schema in SKILL.md:

1. Verdict (fit, desk-reject risk)
2. Top 3 priorities
3. Section-by-section BEFORE / AFTER / ANNOTATION
4. Change log
5. Quality score (0–100, four sub-scores)
6. AI-use disclosure reminder

---

## Iteration Discipline

Polishing is iterative. Each invocation of POLISH should produce one **complete** pass. If the user wants a second pass:

- Pass 2: focus only on issues unresolved in pass 1's change log (do not re-touch sections that scored ≥22/25 on their relevant sub-score)
- Pass 3 (rare): final harmonization — abstract ↔ intro ↔ discussion ↔ cover letter

Hard stop at 3 passes. If the manuscript still scores < 80, the problem is not polish-able; it requires re-running Stages 2–4 (spine + theory + method), which is a substantive revision the user must lead.
