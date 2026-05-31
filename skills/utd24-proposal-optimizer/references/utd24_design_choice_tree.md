# UTD24 Design Choice Tree — ex-ante research design consultation

This file supports **DESIGN mode** (and is also referenced in IDEA mode for methods-route suggestion). It is the **decision authority** for matching:

- (a) the user's theoretical claim type → (b) the strongest method tier → (c) the identification strategy → (d) the sample design → (e) the measurement requirements → (f) the endogeneity checks → (g) outlet fit.

Unlike Dim 5 in `utd24_methods_identification.md` (which audits a design after the fact), this file walks the user through choices **before** data collection or analysis commits.

---

## How DESIGN mode uses this file

The user enters DESIGN mode when:

- They have a research question and parent theory, but have not yet committed to a method
- They have data access constraints (e.g., "I have access to firm X's archival data; what design can I do?")
- They are rebuilding a paper after a UTD24 rejection where Dim 5 was the killer

DESIGN mode output structure:

```
## Design consultation summary
RQ: <user's question>
Parent theory: <user's theory>
Hypothesis architecture: <from utd24_hypothesis_patterns.md>
Claim type: <causal / process / boundary / mechanism unpacking / pattern>
Data accessibility: <archival public / archival proprietary / accessible orgs / lab subjects / no data yet>
Target outlet: <SMJ / AMJ / ASQ / OS / MS / AMR / Strategy Science / undecided>

## Strongest design path
Method tier: ...
Identification strategy: ...
Sample design: ...
Measurement requirements: ...
Endogeneity checks needed (with priority): ...
Outlet fit: ...
Why this is strongest: <one paragraph>

## Second-best design path (if strongest is infeasible)
... same fields ...

## Designs to avoid (and why)
- ... method tier — why misfit

## Pre-registration / pre-analysis plan recommendation
... (if applicable to method)

## Cross-skill handoff
- For deeper sample-size / power analysis: ...
- For measurement scale development: ...
- For preregistration template: ...
```

---

## Decision Tree A — by claim type

Start here. Match the user's primary theoretical claim to one of these branches.

### Branch A1 — Causal effect of X on Y (no mediator decomposed)

User wants to claim "X causes Y" (or "X drives Y", "X produces Y").

| Data accessibility | Strongest design | Second-best | Avoid |
|---|---|---|---|
| Archival panel + clear exogenous shock (policy / regulation / natural experiment) | **DiD** with parallel-trends evidence + placebo + alternative control-group construction | RDD if cutoff is sharp; IV if exclusion is credible | OLS without identification → causal claim not supported |
| Archival panel without shock | IV (if instrument satisfies exclusion and relevance) OR matched-sample analysis (PSM, CEM) with sensitivity to unobservables (Oster bounds) | GMM dynamic panel if reverse causality is plausible | Causal verbs at all (use "associated with") |
| Accessible orgs (can manipulate / observe close) | Field experiment with randomization | Quasi-experiment with regression discontinuity exploiting org's internal cutoff | Self-report-only causal claim |
| Lab subjects (executives, MBAs, students) | RCT with stratified random assignment | Vignette experiment with realistic manipulation | Vignette with student sample claiming causal effect on real firm outcomes |
| No data yet | Re-route to identifying *which* of the above is feasible; do not commit to a design with no data path | — | Designing the paper without a data-feasibility plan |

**Outlet fit per design**:
- DiD with policy shock → SMJ ✓✓ / AMJ ✓ / MS ✓✓
- RDD → SMJ ✓✓ / MS ✓
- IV (credible exclusion) → SMJ ✓✓ / AMJ ✓ / MS ✓✓
- Field experiment → AMJ ✓✓ / ASQ ✓
- Lab RCT with executives → Strategy Science ✓✓ / OS ✓ / AMJ △
- Lab RCT with students → AMR ✓ (theory test) / OS △

### Branch A2 — Mechanism specification (X → M → Y; opening the black box)

User wants to claim "X causes Y via M".

| Data accessibility | Strongest design | Second-best | Avoid |
|---|---|---|---|
| Archival panel + shock + measurable M | DiD on X with mediation analysis on M (with sensitivity to sequential ignorability — Imai et al. 2010 bounds) | Two-stage: shock → M established, then M → Y with separate identification | Mediation econometrics without theoretical defense of pathway direction (X → M → Y vs M → X) |
| Survey with X, M, Y measurable | SEM with bootstrapped mediation (Preacher-Hayes) + multi-source data for X and Y to avoid common-method bias | Conditional process model (Hayes PROCESS) with multi-wave data | Single-source cross-sectional mediation (common-method-bias reject) |
| Lab experiment | Manipulate X, measure M, measure Y; report mediation with sensitivity analysis | Manipulate X and M independently (causal-chain experimental design — Spencer, Zanna & Fong 2005 *JPSP*) | Mediation on lab data without manipulation check on M |
| Mixed methods | Quan establishes X → Y; qual traces M longitudinally (process tracing) | Sequential exploratory: qual identifies M, quan tests | Quan-only mediation without qual scaffolding when M is hard to measure |

**Outlet fit per design**:
- DiD + mediation → SMJ ✓ / AMJ ✓
- SEM mediation + multi-source → AMJ ✓✓ / OS ✓
- Lab experimental causal chain → Strategy Science ✓✓ / OS ✓
- Mixed methods with process tracing → AMJ ✓✓ / ASQ ✓✓

**Mediation strong-assumption caveat**: even with clean identification of X on Y, the mediator's role assumes no unmeasured M-Y confounders (sequential ignorability). UTD24 reviewers expect this to be acknowledged. Imai et al. (2010, 2011) sensitivity analysis or Cinelli-Hazlett (2020) bounds are the current expected response.

### Branch A3 — Boundary / scope condition (when does X → Y hold?)

User wants to claim "X → Y holds under condition Z, fails under not-Z".

| Data accessibility | Strongest design | Second-best | Avoid |
|---|---|---|---|
| Panel data with variance in Z across firms / years | Interaction term X × Z with FE + heterogeneous-effects analysis (Athey-Imbens machine-learning extensions if Z is high-dimensional) | Split-sample analysis with formal Wald test for coefficient equality | Claiming boundary without empirical variance in Z (boundary is asserted, not tested) |
| Lab experiment | 2×2 factorial (X × Z) with manipulation of both | Mediation-moderation hybrid if Z operates through a mediator | Single-cell test of one condition with implied claim about untested cell |
| Mixed methods | Quan establishes X → Y in pooled sample; qual identifies Z and shows mechanism breakdown in not-Z cases | Sequential: qual generates Z, quan tests | Boundary claim without testing both sides of Z |

**Outlet fit per design**:
- Interaction with FE + heterogeneity → SMJ ✓✓ / AMJ ✓✓
- 2×2 lab → Strategy Science ✓✓ / OS ✓ / AMJ ✓
- Mixed methods boundary → ASQ ✓✓ / AMJ ✓

**Common failure**: claiming a boundary that is actually just attenuation of a main effect (e.g., "the effect is weaker under Z") rather than a sign-reversal or null at not-Z. UTD24 boundary papers should show null or sign-flip at the boundary, not just smaller effect.

### Branch A4 — Process / how-it-unfolds-over-time

User wants to claim "Y is the result of process P unfolding over time, involving sequence of events / interactions / interpretations".

| Data accessibility | Strongest design | Second-best | Avoid |
|---|---|---|---|
| Accessible orgs over time | Longitudinal qualitative case (24+ months observation, multi-source data: interviews, archival, real-time observation, documents) | Multi-case comparison (Eisenhardt 1989 method) with theoretical replication | Single retrospective interview-only study |
| Already-archived sequence data (event histories) | Event-history / sequence-analysis methods (Abbott 1995); optimal matching | Discrete-time hazard models | Cross-sectional snapshot with implied process claim |
| Mixed methods | Qual traces process; quan tests measurable predictions from the process model | Sequential: qual identifies process steps; quan generalizes | Pure quan with retrospective process claim |

**Outlet fit per design**:
- Longitudinal qual case → ASQ ✓✓ (natural home) / AMJ ✓ / OS ✓
- Event-history → AMJ ✓ / OS ✓ / SMJ △
- Multi-case Eisenhardt → AMJ ✓✓ / ASQ ✓
- Mixed-methods process → ASQ ✓✓ / AMJ ✓

See companion file `utd24_qual_mixed_design.md` for the full qual / mixed evaluation criteria UTD24 outlets apply.

### Branch A5 — Theoretical / formal contribution (no empirics)

User wants to claim "this new theoretical framework / formal model better explains <phenomenon>".

| Sub-type | Strongest design | Second-best | Avoid |
|---|---|---|---|
| Pure conceptual (AMR-style) | Conceptual paper with explicit propositions, boundary conditions, generative implications, and engagement with rival frameworks | Conceptual paper with one anchor empirical exemplar | Conceptual paper that rehashes a literature review |
| Formal analytical model | Analytical model with: stated assumptions; comparative statics; testable predictions; engagement with rival models | Formal model + companion empirical study (mixed-method) | Formal model without comparative statics or with assumptions that immediately produce the result |
| Computational simulation | Agent-based or system-dynamics simulation with: clearly stated micro-rules; sensitivity analysis on parameters; comparison to closed-form benchmark where possible | Simulation + empirical validation of key parameters | Simulation as black-box without rule justification |

**Outlet fit per design**:
- Pure conceptual → AMR ✓✓
- Analytical model → MS ✓✓ / Strategy Science ✓✓ / AMR (if no empirics) ✓
- Computational simulation → MS ✓✓ / OS ✓ / Strategy Science ✓✓

---

## Decision Tree B — by data accessibility (when claim type is flexible)

If the user has a fixed data source and is exploring what RQ to ask, reverse the tree:

### Branch B1 — Have access to a clean exogenous shock (policy, regulation, natural experiment)

Strongest claim types: causal (A1), boundary (A3), mechanism with DiD-mediation (A2).
Strongest outlets: SMJ, AMJ, MS.
Common failure: treating "policy implementation" as a shock without verifying parallel pre-trends, anticipation effects, or selection into treatment.

### Branch B2 — Have access to accessible orgs over time (longitudinal field site)

Strongest claim types: process (A4), mechanism (A2 with mixed methods).
Strongest outlets: ASQ, AMJ.
Common failure: under-investing in real-time data collection (interviews and observation early, not retrospective); ASQ reviewers reject post-hoc qualitative reconstructions.

### Branch B3 — Have access to executive subjects for lab work

Strongest claim types: causal (A1 RCT), mechanism (A2 lab experiment), boundary (A3 factorial).
Strongest outlets: Strategy Science, OS, AMJ.
Common failure: weak manipulation, no manipulation check, weak ecological-validity defense.

### Branch B4 — Have access to large archival panel without exogenous shock

Strongest claim types: pattern / association (not causal), boundary (A3), mechanism (A2 with IV).
Strongest outlets: SMJ (only if IV is clean), AMJ, MS.
Common failure: claiming causal effects without an identification strategy; UTD24 reviewers will reject. Calibrate to "associated with" or find an IV / shock embedded in the panel.

### Branch B5 — No data yet (designing from scratch)

Do not commit to a design without a data-feasibility check. Re-route to:
- What data is feasible to collect / acquire within paper's timeline?
- What budget for fielding survey, recruiting experimental subjects, accessing proprietary archives?
- What collaborations enable accessible orgs?

Only after data feasibility is established, return to Tree A.

---

## Decision Tree C — sample design considerations

For each design path above, the following sample design questions apply.

### C.1 Sample size & statistical power
- For RCT / experiment: a priori power analysis (G*Power, Cohen 1988; for SEM, Soper calculator or MacCallum-Browne-Sugawara 1996)
- For panel with FE: rule-of-thumb 30 firms × 5 years for basic FE; more if interactions or non-linear; explicit power calc for treatment effects in DiD
- For survey: Cochran's formula or two-step (CFA needs N ≥ 200 typically); inflate for multi-level SEM
- For QCA: minimum 12-18 cases for crisp-set; 20+ for fuzzy-set

If a paper is power-underpowered, R2 will catch it. Pre-compute power and report.

### C.2 Sample frame
- **Random**: gold standard for survey; rare in strategy due to access constraints
- **Stratified**: necessary when key strata (industry, size, age) have unequal selection probabilities
- **Theoretical**: required for qual (Eisenhardt-Graebner 2007 theoretical-replication logic)
- **Convenience**: weakest; UTD24 reviewers will demand explicit defense and limitations discussion
- **Census** (entire population in a defined boundary): strong; defend the boundary

### C.3 Selection bias prevention
- Identify the population from which the sample is drawn; show overlap or note non-overlap
- For accessible-org studies: document non-participating orgs' characteristics
- For panel data with attrition: report retention rates; test for selection on observables; consider IPW (inverse probability weighting) if attrition is non-random

### C.4 Theoretical sampling (qual)
- For grounded theory: theoretical-replication logic (Eisenhardt 1989; Yin 2018)
- For process studies: longitudinal access; minimum 24 months observation typical for ASQ
- For multi-case: literal-replication (similar cases) and theoretical-replication (contrasting cases)

---

## Decision Tree D — measurement design

### D.1 If construct has a validated scale in prior published work

Use it. Cite the validation paper. Report reliability (Cronbach α / composite reliability) in the current manuscript even with a previously-validated scale.

### D.2 If construct has no validated scale or you need a domain-specific adaptation

Develop a new measure via:
1. **Item generation** — theoretical definition → item pool → expert review (3-5 domain experts)
2. **Pilot study** — N ≥ 30 for initial reliability and item refinement
3. **Validation study** — CFA on N ≥ 200; report convergent validity (correlation with related validated measure) and discriminant validity (low correlation with unrelated construct + HTMT ratio < 0.85)
4. **Replication study** if possible — second sample, CFA invariance test

The MacKenzie, Podsakoff & Podsakoff (2011, MISQ) and Hinkin (1998, ORM) procedures are the published norm.

For UTD24 outlets, an entire paper section (typically 2-3 pages) is needed to document new measure development. If the new measure is the paper's primary IV or DV, consider a separate methods note paper for the measure development to off-load the validation burden.

### D.3 Text-as-data measurement (10-K, transcripts, news, patents)

- Dictionary methods: cite the dictionary's published validation (LM, Henry, Diction, etc.); document any custom additions and validate
- Topic models: report coherence metrics; human-validated topic labels
- LLM coding (GPT / Claude / Gemini): see Pattern M2 in `utd24_exemplar_patterns.md` for the Kanis et al. 2026 Strategy Science benchmark (3 LLMs, human inter-rater α ≥ 0.7, sensitivity to prompts, validation set separation, pre-registered protocol)

### D.4 Coded archival data (CEO biographies, M&A deals, etc.)

- Multiple coders (≥ 2)
- Inter-rater agreement: κ (categorical) or ICC (continuous) reported; UTD24 norm κ ≥ 0.7, ICC ≥ 0.8
- Coder training documented
- Discrepancies resolved with explicit procedure (third coder, discussion to consensus)

### D.5 LLM-as-coder (rising standard since 2024)

Beyond the Kanis benchmark, current expectations:
- Disclose prompt verbatim
- Separate development set from validation set
- Multi-LLM consistency check (3 models minimum at UTD24)
- Sensitivity analysis with prompt perturbation
- Pre-register the coding protocol if possible

---

## Decision Tree E — endogeneity decision matrix

Given your design + your claim, which endogeneity checks are required?

| Threat | Detection signal | Required check |
|---|---|---|
| **Unobserved confounders** (Z affects both X and Y) | Cross-sectional or panel without exogenous variation in X | Sensitivity analysis (Oster 2019; Cinelli-Hazlett 2020); IV if available; FE if Z is time-invariant |
| **Reverse causality** (Y affects X) | Theoretical plausibility of reverse direction | Granger causality test (panel); lagged DV regression; IV with timing exclusion; DiD on a shock to X |
| **Selection** (firms / individuals choose into X) | Treatment is not randomly assigned; X choice is endogenous to firm characteristics | Heckman 2-stage; PSM; CEM; IV with exclusion |
| **Simultaneity** (X and Y jointly determined) | Both are firm-level strategic choices that respond to common factors | Simultaneous-equations model (3SLS); GMM dynamic panel; structural model |
| **Measurement error in X** | X is operationalized via proxy or noisy measure | IV with separate measure of X; SIMEX (simulation-extrapolation) for known error variance |
| **Common-method bias** | Same source provides X, M, Y (survey) | Multi-source data; multi-wave separation; Harman single-factor + CFA marker variable; ULMC |
| **Survivorship / attrition** | Panel with non-random exit | Heckman selection; IPW; sensitivity to alternative attrition assumptions |
| **Spillover / SUTVA violation** | Treated units interact with control units | Test for spillover (geographic / network distance interaction); randomization at cluster level |

Match the threats to your design before submission. UTD24 R2 will rank-order these and demand the top 2-3 be addressed.

---

## Pre-registration recommendations

| Design type | Pre-register? | Where | What to include |
|---|---|---|---|
| Lab / field experiment | YES (highly recommended) | OSF or AsPredicted | Hypotheses, sample size, exclusion criteria, primary analyses, secondary analyses, planned interaction tests |
| Survey with planned hypotheses | YES (recommended) | OSF | Hypotheses, sample frame, planned analyses, planned robustness |
| Archival panel with planned analyses | YES if data has not been touched | OSF Registered Reports format | Analysis plan, sample selection rules, hypotheses, robustness plan |
| Archival with pre-existing exploration | NO (would be misleading) | — | Use exploratory labeling for findings without pre-specified hypotheses |
| Qual / process study | Optional | OSF | Pre-register theoretical sampling logic and data-collection protocol; coding protocols can evolve (note evolution in methods) |

Registered Reports (where reviewers approve methods before data collection / analysis) are accepted at AMR (rare), AMJ (Registered Reports section), MS (occasional). Worth considering for ambitious designs.

---

## Cross-references

- After choosing a design here, audit it against Dim 5 → `utd24_methods_identification.md`
- Hypothesis architecture choice that affects design → `utd24_hypothesis_patterns.md`
- Qual / mixed design details → `utd24_qual_mixed_design.md`
- Outlet floor per dim (Dim 5 floor varies by outlet) → `utd24_rubric.md`
- Robustness coverage post-design → `utd24_methods_identification.md` Dim 5.3
- LLM measurement validation → `utd24_methods_identification.md` LLM-as-measurement section
