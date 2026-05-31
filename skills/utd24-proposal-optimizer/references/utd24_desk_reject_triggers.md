# UTD24 Desk-Reject Triggers — 30-second kill signals

This file lists triggers that, if detected, push the verdict to **DESK-REJECT-LEVEL** regardless of other strengths. UTD24 outlets (SMJ / AMJ / ASQ / OS / MS / AMR) desk-reject 40-60% of submissions; these are the most common signals AEs use in the 5-15 minute screen.

For each trigger:
- **Detection cue** — how to spot it in the manuscript
- **Severity** — HIGH (desk-reject likely) / MEDIUM (sent for review but R1-level major-revision) / LOW (revise recommended)
- **Affected dimension(s)** — which Dim it pulls down
- **Quick fix or commit-to-rebuild signal**

---

## T1 — Parent theory not named (HIGH severity)

**Detection cue**: The introduction lists "the strategy literature", "the innovation literature", or 3+ literatures without committing to a specific lineage. No 2-3 anchor papers in a single lineage.

**Affected**: Dim 2.1 = 0 or 1, drags total below 60.

**Quick fix**: Re-read `utd24_strategy_innovation_entrepreneurship_lineages.md`. Pick one lineage. Cite 2-3 anchor papers. Rewrite the contribution as a movement within that lineage.

If the user genuinely cannot commit to a lineage: the project is pre-paradigmatic and not yet ready for UTD24. Suggest going back to `theory-positioning` skill or sketching candidate lineages with mentors.

---

## T2 — Gap-fill framing as the contribution claim (HIGH severity)

**Detection cue**: Phrases in intro or contribution paragraph:
- "We fill a gap in the literature on..."
- "No prior study has examined..."
- "Despite extensive research on X, [our specific angle] has been overlooked..."
- "We address this gap by..."

**Affected**: Dim 2.3 = 0 or 1.

**Quick fix**: Replace gap-fill with a *theoretical movement*:
- EXTENSION: "We extend [theory] by..."
- INTEGRATION: "We bridge [theory A] and [theory B] by..."
- RECONCILIATION: "We reconcile the conflicting findings of [X] and [Y] by..."
- BOUNDARY: "We identify a boundary condition for [theory's prediction] when..."
- MECHANISM: "We open the black box of [theory's outcome] by specifying [mechanism]..."

If the contribution actually is a gap-fill and no theoretical movement is plausible, the paper is not UTD24.

---

## T3 — Analogy substituting for mechanism (HIGH severity, per Hard Rule 4)

**Detection cue**: In the mechanism / theory development section, the causal logic is carried by phrases:
- "similar to" / "akin to" / "as in [other phenomenon]"
- "parallels" / "mirrors" / "analogous to"
- "by extension from [other literature]"

Test: remove the analogy. Does the mechanism stand alone? If no, this trigger fires.

**Affected**: Dim 3.4 = 0, often Dim 3.1 ≤ 1 too.

**Quick fix**: Rewrite the mechanism so the causal logic stands on its own (named construct, direction, falsifiable prediction). The analogy becomes optional illustration *after* the standalone mechanism is stated.

---

## T4 — Cross-sectional design with "causes" claims (HIGH severity, per Hard Rule 3)

**Detection cue**: Abstract / intro / discussion uses verbs *causes*, *leads to*, *produces*, *drives*, *determines*, but methods section reports cross-sectional survey or panel without identification (no DiD, no IV, no RDD, no RCT).

**Affected**: Dim 5.1 = 0, often Dim 5.4 ≤ 1.

**Quick fix**: Either:
- Calibrate verbs throughout to "associated with" / "predicts" / "positively correlated with", OR
- Add a credible identification strategy (IV with defensible exclusion; DiD with parallel-trends evidence; RDD with bandwidth/falsification tests)

If neither is possible: the paper is not UTD24 as currently designed; consider repositioning to JBR / MOR / LRP.

---

## T5 — "First study to" / "no prior study has" without evidence (HIGH severity, per Hard Rule 5)

**Detection cue**: The contribution paragraph claims novelty via "first", "only", "no prior", "never been examined" without:
- A systematic search log
- A recent published review
- An explicit reviewer concession

**Affected**: Dim 2.3 = 0 or 1, also Dim 2.4 (no conversation visibility).

**Quick fix**: Drop the primacy claim. Replace with a *theoretical-movement* claim that doesn't require primacy ("we extend X by..." doesn't require being first).

UTD24 reviewers are deeply embedded in these literatures; an unsupported primacy claim is an instant credibility hit and often a one-line desk-reject reason.

---

## T6 — HARKing pattern in hypothesis section (HIGH severity, per Hard Rule 12)

**Detection cue**: Any of:
- Interaction terms or mediator paths with no a priori theoretical justification in the theory section, but happen to be strongest empirical results
- Theory section written in past tense ("we found", "we documented")
- Predicted directions in pre-registration (if any) don't match manuscript
- Unusual moderator suddenly elevated to a main hypothesis with one sentence of justification

**Affected**: Dim 4.4 = 0.

**Quick fix**: Identify retrofitted hypotheses, label them as exploratory, separate from confirmatory predictions. Rewrite theory section in present tense.

---

## T7 — 6+ hypotheses with redundancy (MEDIUM severity)

**Detection cue**: Manuscript lists 6, 7, 8, or more hypotheses. Multiple hypotheses appear to test the same underlying mechanism with different operationalizations or sub-samples.

**Affected**: Dim 4.2 ≤ 3.

**Quick fix**: Consolidate redundant hypotheses. Either:
- Drop redundant variants
- Reframe as one hypothesis with multiple operationalizations (move alternative operationalizations to robustness section)

3-5 hypotheses is the UTD24 norm.

---

## T8 — Critical construct freshly invented without validation (HIGH severity)

**Detection cue**: A key construct (especially DV or main IV) is introduced for the first time in this manuscript with no:
- Prior published validation
- Convergent + discriminant validity evidence in this paper
- Inter-rater agreement (for coded data)

**Affected**: Dim 5.2 = 0 or 1.

**Quick fix**: Add validation evidence. For coded measures: report inter-rater agreement (κ or Krippendorff α). For survey scales: report Cronbach α and convergent / discriminant evidence. For text-based measures: report human-benchmark validation. For LLM-based measures: see Kanis et al. 2026 multi-LLM α benchmark.

If no validation evidence can be added: the construct is not ready for UTD24.

---

## T9 — Vague mediator (e.g., "legitimacy", "cognition", "learning") (MEDIUM severity)

**Detection cue**: Mediator is named with a single-word generic construct (legitimacy / cognition / learning / trust / culture / capabilities) without specifying which sub-dimension.

**Affected**: Dim 3.1 ≤ 3.

**Quick fix**: Specify the sub-dimension:
- Legitimacy → pragmatic / normative / cognitive / regulative
- Cognition → mental representations / attention / heuristics / mental models
- Learning → vicarious / experiential / superstitious / inferential
- Trust → competence / benevolence / integrity
- Capabilities → operational / dynamic / managerial cognitive

---

## T10 — No engagement with recent (last 5 years) UTD24 literature in the lineage (MEDIUM severity)

**Detection cue**: All anchor papers are 10+ years old. The introduction does not cite any paper from the last 5 years in the named lineage.

**Affected**: Dim 2.2 ≤ 1.

**Quick fix**: Add 1-2 recent (last 5 years) UTD24 papers in the lineage. Engage substantively (state agreement / disagreement / extension), not just cite.

If the user can find no recent UTD24 papers in their claimed lineage, the lineage may be inactive or the user has mis-anchored. Re-check parent theory.

---

## T11 — Scope misfit: pure OB micro / marketing / finance / accounting (HIGH severity, per Hard Rule 9)

**Detection cue**: The phenomenon and DV belong to:
- Pure OB micro (individual-level affect / motivation / personality without organizational-strategic outcomes)
- Pure marketing (consumer behavior, brand, advertising, without strategy mechanism)
- Pure finance (asset pricing, capital structure, without strategic mechanism)
- Pure accounting (earnings management, audit, without strategic mechanism)
- Pure methodological paper

**Affected**: This skill cannot calibrate. Verdict should be OUT-OF-SCOPE.

**Quick fix**: Suggest alternates:
- OB micro → JAP, Personnel Psychology, AMJ (if linkable to strategic outcome)
- Marketing → JM, JMR, JCR
- Finance → JF, JFE, RFS
- Accounting → JAR, JAE, TAR
- Methodological → Organizational Research Methods, Journal of Management Methods

If user insists the paper has a strategy hook: re-foreground the strategy mechanism in introduction and theory, demote the micro/marketing/finance/accounting elements to control variables.

---

## T12 — Abstract / intro overclaim asymmetric with methods (MEDIUM severity)

**Detection cue**: Abstract or intro says the paper "shows" / "demonstrates" / "establishes" a causal effect, but methods are cross-sectional, qual case, or non-identified panel.

**Affected**: Dim 5.1 ≤ 3, Dim 1.2 (why-care framing) ≤ 3.

**Quick fix**: Calibrate abstract and intro verbs to match methods. Even if methods are strong, hyperbolic abstracts trigger reviewer skepticism.

---

## T13 — Two papers stitched into one (MEDIUM severity)

**Detection cue**: The introduction makes two distinct theoretical claims with two distinct mechanisms and two distinct sets of hypotheses. The paper is trying to do too much.

**Affected**: Dim 1.3 ≤ 1, Dim 4.2 ≤ 3.

**Quick fix**: Split. Keep the stronger contribution. Move the secondary into a future paper.

---

## T14 — No falsifiable prediction (HIGH severity)

**Detection cue**: All hypotheses accommodate any plausible result. The theory makes no commitment.

**Affected**: Dim 3.2 = 0 or 1.

**Quick fix**: Commit to a sign for each hypothesis. State an opposite outcome that would force theory revision.

---

## T15 — Vague abstract / no clear contribution sentence (MEDIUM severity)

**Detection cue**: Abstract does not contain a sentence of the form "We extend / integrate / reconcile / bound / mechanism-specify [parent theory] by [specific move]". Abstract ends with "implications for theory and practice" without naming them.

**Affected**: Dim 1.2 ≤ 3, Dim 2.3 ≤ 3.

**Quick fix**: Rewrite abstract with a clear contribution sentence. Use the template in `utd24_lit_conversation.md` contribution framing.

---

## T16 — Discussion does not engage the parent theory (MEDIUM severity)

**Detection cue**: Discussion section talks about findings but does not state what changes in the parent theory as a result. No "boundaries we identify", no "mechanism we open", no "tension we reconcile".

**Affected**: Dim 2.3 ≤ 3.

**Quick fix**: Add a "Theoretical implications" subsection (1-2 paragraphs) that explicitly states the contribution to the parent theory in movement-type language.

---

## How to use this file

In MANUSCRIPT and REVIEW modes:
1. Scan for each trigger above
2. For each detected trigger, report:
   - Trigger ID + name
   - Location in manuscript (section, paragraph)
   - Severity
   - Affected dimensions
   - Quick fix or rebuild signal
3. If 2+ HIGH-severity triggers fire → desk-reject risk HIGH
4. If 1 HIGH-severity trigger or 3+ MEDIUM → desk-reject risk MEDIUM
5. If 0 HIGH and ≤2 MEDIUM → desk-reject risk LOW (but still revise per Top 3 priorities)

In IDEA mode:
- T1, T2, T11 apply. T3, T6, T8, T14 are too premature to assess. Note them as "to watch for" once a manuscript exists.
