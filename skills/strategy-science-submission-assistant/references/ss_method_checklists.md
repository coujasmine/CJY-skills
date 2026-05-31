---
file: ss_method_checklists.md
purpose: Per-method evaluation criteria for Strategy Science submissions. High-level checklists; method-specific deep dives are in references/methods/.
last_verified: 2026-05-21
---

# Strategy Science Method Checklists

## Contents

- 1. Archival Panel (e.g., Asghar et al., Qu et al.)
- 2. Experiment (e.g., Kanis et al.)
- 3. Pure Theory / Formal Modeling (e.g., Clough)
- 4. Computational / Simulation
- 5. Qualitative / Case Study
- 6. Mixed Methods
- 7. Meta-Analysis
- 8. LLM-as-Measurement / LLM-as-Coder
- 9. ML-as-Prediction (e.g., Qu et al.)
- Cross-cutting checklist (all methods)
- When the method tier is ambiguous


Strategy Science publishes across a wide method range. This file provides a high-level checklist for each method tier. Use the relevant tier's checklist in AUDIT mode and as a Stage 4 supplement in POLISH mode. Deeper method-specific files are in `references/methods/`.

---

## 1. Archival Panel (e.g., Asghar et al., Qu et al.)

### Core checklist

- [ ] Sample period and source clearly identified (e.g., "S&P 500 firms making product introduction announcements between 2016 and 2018")
- [ ] Unit of analysis explicit (manager-product introduction announcement dyad; acquisition transaction; firm-year)
- [ ] Construct definitions precede measures
- [ ] Variable measurement procedures replicable
- [ ] Independent variables operationalized with proper data sources
  - BoardEx, Capital IQ, Compustat, CRSP, Refinitiv typical
- [ ] Control variables justified theoretically (not kitchen-sink)
- [ ] Identification strategy clearly stated (firm + year FE, lagged DVs, IV, DiD, RDD as appropriate)
- [ ] Clustering of standard errors appropriate to data structure
- [ ] Robustness checks address specific threats
- [ ] Reverse causality addressed
- [ ] Selection threats (e.g., sample-attrition, non-response) discussed

### SS-specific norms

- Teachman entropy index for breadth/diversity measures is the SS norm (Asghar uses it for industry/firm/function knowledge breadth)
- BHAR (buy-and-hold abnormal returns) for long-term outcomes (Asghar)
- CAR (cumulative abnormal returns) with Fama-French model for short-term outcomes (Qu)
- ML-derived measures must include train-test split + benchmark comparison (Qu uses RF vs. OLS vs. elastic net vs. gradient-boosted)
- Effect sizes reported, not just significance
- Coefficient tables show SE in parentheses, NOT t-statistics

### Detailed methods file

See `methods/archival_panel_checklist.md` for full audit.

---

## 2. Experiment (e.g., Kanis et al.)

### Core checklist

- [ ] Design type stated (between-subjects, within-subjects, mixed; 2×2 or other factorial)
- [ ] Random assignment described
- [ ] Pre-registration link, if registered (anonymized for review)
- [ ] G*Power calculation for sample size justified
- [ ] Recruitment platform stated (Prolific, MTurk, lab, etc.)
- [ ] Participant qualifications stated
- [ ] Exclusion criteria stated explicitly before exclusions are applied
- [ ] Exclusion rates reported
- [ ] Manipulation check reported with statistical test
- [ ] Attention check or care-quality check
- [ ] Demographic characteristics reported
- [ ] Dependent variable measurement (scales, items, established sources)
- [ ] Inter-rater reliability for coded responses
- [ ] LLM-coded responses: multi-LLM consistency, Krippendorff α against humans
- [ ] Power analysis or sensitivity analysis if nulls reported (Kanis 2026)
- [ ] Procedure described in enough detail to replicate
- [ ] IRB approval cited (Kanis 2026 cites TU Bergakademie Freiberg)

### SS-specific norms

- Online experiments via Prolific are acceptable when sample is appropriate (Kanis recruited Prolific participants with prior business-strategy decision experience)
- Multiple LLMs for content coding raises confidence; single-LLM is acceptable with high human-LLM agreement
- Null results on the main DV are publishable if the theoretical contribution is sharp (Kanis 2026 reports nulls on strategic foresight while documenting representational shifts)
- Pre-registration is increasingly cited and expected for confirmatory work
- Adaptation of established tasks (e.g., Csaszar & Laureiro-Martínez 2018's startup evaluation) is welcomed

### Detailed methods file

See `methods/experiment_checklist.md` for full audit.

---

## 3. Pure Theory / Formal Modeling (e.g., Clough)

### Core checklist

- [ ] Theoretical building blocks defined formally and explicitly
- [ ] Assumptions stated transparently (and defended substantively)
- [ ] Conceptual splits motivated (Clough splits coordination into "speed" and "scope"; this is a deliberate move)
- [ ] Typology or framework summarized in a table or figure
- [ ] Trade-offs / trilemmas / impossibility results identified clearly
- [ ] Examples / illustrations from real-world cases (Clough uses Windows, iOS, Linux, blockchain)
- [ ] Testable predictions stated for future empirical work
- [ ] Engagement with existing theoretical lineages (Williamson, game theory)
- [ ] Boundary conditions of the framework discussed
- [ ] Limitations of the theoretical approach acknowledged

### SS-specific norms

- Pure-theory papers are accepted (Clough 2026), but the framework must offer a substantive movement
- Formal proofs are NOT required if the theoretical argument is rigorous and the typology is clear
- Game-theoretic backbone is valued (Schelling, Farrell-Saloner, Cooper et al.)
- Integration of two literatures is a strong contribution form (Clough integrates Williamson + game-theoretic coordination)
- "Trilemma" / "trade-off" / "alignment" framings are persuasive
- Empirical verbs ("we find", "we show empirically") should be absent

### Detailed methods file

See `methods/formal_theory_checklist.md` for full audit.

---

## 4. Computational / Simulation

### Core checklist

- [ ] Model structure described formally (e.g., NK landscape, agent-based, system dynamics)
- [ ] Parameter values and ranges justified
- [ ] Initial conditions stated
- [ ] Simulation runs (number, randomization) reported
- [ ] Sensitivity analysis to parameter changes
- [ ] Robustness to alternative model specifications
- [ ] Comparison to analytical or empirical benchmarks where possible
- [ ] Code availability statement
- [ ] Clear statement of what the simulation can and cannot test

### SS-specific norms

- NK simulation tradition (Levinthal 1997, Rivkin 2000) is well-represented at SS
- Computational results are propositions, not "findings" — use theory-paper claim language (`ss_claim_evidence_matrix.md`)
- Empirical calibration of parameters strengthens the contribution

---

## 5. Qualitative / Case Study

### Core checklist

- [ ] Theoretical case-selection logic (not convenience)
- [ ] Number and type of cases justified for the theoretical contribution
- [ ] Data sources described (interviews, archival, observation)
- [ ] Coding procedure described
- [ ] Inter-coder reliability for category coding (if multiple coders)
- [ ] Theoretical saturation discussed
- [ ] Tables linking data to theoretical claims (informant quotes ↔ first-order codes ↔ second-order themes ↔ aggregate dimensions; Gioia methodology)
- [ ] Limitations of generalizability discussed
- [ ] Trustworthiness/credibility evidence (member checks, triangulation)

### SS-specific norms

- Pure case studies are less common at SS than at AMJ; theoretical contribution must be sharp
- Multi-case theory-building (Eisenhardt & Graebner 2007) is the standard reference
- Strong analytical generalization (not statistical generalization) is appropriate

---

## 6. Mixed Methods

### Core checklist

- [ ] Mixed-methods rationale: why mix?
- [ ] Sequencing (qual → quant, quant → qual, parallel)
- [ ] Integration of phases (where and how)
- [ ] Each phase meets the standards of its method
- [ ] Findings from each phase reported separately and then integrated

### SS-specific norms

- Mixed methods are accepted but the value of mixing must be clear
- "Triangulation" alone is insufficient; the qualitative and quantitative phases should answer different parts of the research question

---

## 7. Meta-Analysis

### Core checklist

- [ ] Search strategy reported (databases, dates, keywords)
- [ ] Inclusion/exclusion criteria explicit
- [ ] Coding procedure with inter-coder reliability
- [ ] Effect-size calculation method
- [ ] Random-effects vs. fixed-effects justification
- [ ] Heterogeneity analysis (I², τ²)
- [ ] Publication bias analysis (funnel plot, Egger's test, trim-and-fill)
- [ ] Moderator analyses with theoretical motivation

### SS-specific norms

- Meta-analyses are publishable at SS when the theoretical contribution beyond aggregating effect sizes is sharp
- Meta-analytic estimate is correlational; underlying study designs vary — claim language must reflect this

---

## 8. LLM-as-Measurement / LLM-as-Coder

### When this applies

When the paper uses one or more LLMs to:
- Classify text into pre-defined categories (e.g., Kanis et al. 2026 classifies pros/cons into strategic categories)
- Extract structured information from unstructured text
- Generate quantitative measures from qualitative inputs
- Score or rate content

### Core checklist

See `references/gpt_measurement_validation.md` for the full 8-dimension scorecard:

1. Construct definition before measurement
2. Prompt engineering hygiene (system prompts, batching, version pinning)
3. Development/validation set separation
4. Human benchmark and inter-rater reliability (Krippendorff α or κ)
5. Convergent and discriminant validity
6. Sensitivity to alternative LLMs and prompts
7. False-positive / hallucination review
8. Reporting and disclosure

### SS-specific norms (calibrated against Kanis et al. 2026)

- **Multi-LLM consistency**: Kanis uses three LLMs (gpt-4.1, claude-opus-4-1-20250805, mistral-large-latest) with consistency r = 0.93. Single-LLM is acceptable only with strong human-LLM agreement.
- **Human benchmark**: Krippendorff's α = 0.89 between LLM and human coders on a validation subset of 220 items is the demonstrated bar.
- **Prompt transparency**: Full prompts in Appendix (Kanis Appendix A).
- **Version pinning**: Specific model versions cited (claude-opus-4-1-20250805) — not just "Claude".
- **Disclosure**: AI use must be disclosed in the methods AND in the AI-use disclosure statement.

---

## 9. ML-as-Prediction (e.g., Qu et al.)

### When this applies

When ML models are trained to predict an outcome, and the prediction is used as a strategic construct.

### Core checklist

- [ ] Train-test split clearly stated (Qu uses 80-20 with time-series cross-validation)
- [ ] Multiple algorithm comparison (Qu reports OLS, elastic net, random forest, gradient-boosted tree)
- [ ] Baseline benchmark (e.g., OLS) reported alongside ML
- [ ] R² (in-sample and out-of-sample) reported
- [ ] Hyperparameter tuning procedure stated
- [ ] Feature importance reported (Qu reports impurity-based and permutation-based importance)
- [ ] Construct validity of the prediction: does the ML output meaningfully capture the construct?
- [ ] Cross-validation procedure stated
- [ ] Sensitivity to alternative train-test splits

### SS-specific norms

- ML models are tools to operationalize constructs (e.g., "predicted market reactions" as a proxy for managerial mental models). The construct interpretation must be defended.
- Cross-validation procedure should respect time-series structure when applicable
- Comparison against simpler benchmarks is expected, not optional
- Theoretical framing of the ML output is essential (Qu et al. frame predictions as the Brunswik lens model's *ŷ*)

---

## Cross-cutting checklist (all methods)

- [ ] Method-claim calibration consistent (see `ss_claim_evidence_matrix.md`)
- [ ] Construct validity demonstrated (not assumed)
- [ ] Confounders / alternative explanations addressed
- [ ] Effect sizes interpreted, not just reported
- [ ] Limitations honest and substantive
- [ ] Replication materials available (code, data, materials) — gold OA papers should host these on OSF/GitHub

---

## When the method tier is ambiguous

If the user does not specify a clear method tier:
1. Ask which tier applies
2. If user is unsure, use the section labels in their manuscript:
   - "Experimental Design" → experiment
   - "Sample" / "Panel" / "Identification" → archival
   - "Propositions" / "Framework" without empirics → pure theory
   - "Simulation" / "Agent-Based" → computational
   - "Interviews" / "Cases" → qualitative
3. If still ambiguous, treat as mixed and apply both checklists

This list is non-exhaustive; SS publishes other methods (e.g., field experiments, registered reports, lab + field, network analysis). For methods not covered, use the closest applicable checklist and flag the gap to the user.
