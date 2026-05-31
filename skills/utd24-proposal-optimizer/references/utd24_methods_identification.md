# Dim 5 — Methods & Identification: identification, construct validity, robustness

This file deepens the four sub-criteria of Dim 5 in `utd24_rubric.md`.

---

## The identification ↔ claim verb matching table (Dim 5.1)

This table is the authority for whether a manuscript's causal language is supported by its design. Used by Hard Rule 3 and the `scan_causal_overclaim.py` script.

| Method tier | Acceptable claim verbs | Unacceptable claim verbs |
|---|---|---|
| Cross-sectional survey | associated with, correlated with, predicts (cross-sectionally) | causes, leads to, produces, drives, determines |
| Panel (no exogenous shock) | associated with, predicts, persistently associated with, jointly evolves with | causes, leads to, drives (without further identification) |
| Panel + DiD with parallel-trends evidence | causes (in the DiD sample), drives, produces | universal "causes" without sample qualifier |
| Panel + instrumental variable with credible exclusion restriction | causes (LATE interpretation), drives | unconditional "causes" |
| Regression discontinuity | causes (at the cutoff), drives (at the cutoff) | universal "causes" |
| RCT (lab / field) | causes (within ecological-validity caveats) | causes (without acknowledging external validity) |
| Vignette experiment | influences perceptions of, shifts intentions toward | causes [real outcomes], leads to actual behavior |
| Formal theory (analytical / agent-based) | proves (within model assumptions), proposes, model predicts | causes empirically |
| Computational simulation | model predicts, simulation suggests | causes empirically (without companion empirical work) |
| Qualitative case study | suggests, illuminates, develops theory about | causes, predicts, determines |
| Mixed methods | use the strongest qual + quant tier's allowed verbs jointly | overclaim from one component to whole |

### How to apply

Read the abstract, intro, hypothesis statements, and discussion. For each instance of an unacceptable verb given the method tier:

- Flag location (Section, paragraph, sentence)
- Suggest the closest acceptable verb from the table
- Score impact: Dim 5.1 drops 1 point per major overclaim instance, capped at 0

### Special cases

- **Mediation / moderation claims**: even in causal-identification designs, claims about *mediators* require additional identification (e.g., mediation analysis assumes no unmeasured confounders between mediator and outcome — a strong assumption). Flag and require explicit caveats.
- **Spillover claims**: claims about effects on units other than the treated (e.g., effects on competitors) require additional identification beyond DiD. Flag.

---

## Construct validity (Dim 5.2)

UTD24 reviewers require that every key construct (DV, key IV, moderator, mediator) be either:

- Measured with a scale validated in prior published work (with citation), OR
- A newly introduced measure with convergent + discriminant validity reported in the current manuscript

### Construct validity audit

For each key construct:

1. **What is the construct?** (theoretical definition)
2. **How is it measured?** (operationalization)
3. **Is the measure validated?**
   - Prior published validation: citation present and recent (within last 10-15 years)
   - New measure: convergent (correlation with related validated measure) + discriminant (low correlation with unrelated construct) reported
4. **Does the measure include reliability evidence?** (Cronbach α / composite reliability for multi-item scales; inter-rater agreement for coded data; Krippendorff α / κ for human or LLM coding)

### Common failures

- DV is a single-item measure of a multi-dimensional construct (e.g., "innovation" measured as a single binary). Construct validity score ≤ 1.
- Key IV is operationalized via word counts without theoretical defense of the dictionary
- Mediator is a single survey item buried among controls
- New measure introduced without any validation evidence (just face-validity argument)

### LLM-as-measurement note

If the manuscript uses an LLM (GPT / Claude / Gemini) to code text, the construct validity audit requires additional dimensions:
- Prompt engineering disclosure
- Development vs validation set separation
- Human-benchmark inter-rater agreement (κ or Krippendorff α)
- Multi-LLM consistency check
- Sensitivity to prompt variants

For UTD24 outlets, Kanis et al. 2026 (Strategy Science) set a strong recent benchmark: 3 LLMs, α = 0.89 vs humans. This is not an official cutoff but is the recent published norm.

---

## Robustness coverage (Dim 5.3)

UTD24 papers typically report 3-5 robustness checks targeting different threats:

| Threat | Robustness check |
|---|---|
| Alternative DV operationalization | Re-run with alternative DV (e.g., 1-year vs 3-year vs 5-year horizon for performance) |
| Alternative IV operationalization | Re-run with alternative IV (e.g., raw vs scaled vs binarized) |
| Sample selection | Re-run on subsamples, drop outliers, re-run with PSM or coarsened exact matching |
| Model misspecification | Re-run with alternative model (e.g., OLS vs Poisson vs logit; FE vs RE; alternative clustering) |
| Endogeneity | IV, Heckman correction, propensity score, GMM, DiD with placebo / parallel-trends checks |
| Alternative theoretical mechanism | Test the prediction of a competing mechanism on the same data |
| Outlier influence | Re-run dropping top/bottom percentile, dropping influential observations |
| Time-period sensitivity | Re-run on different time windows; check pre/post structural breaks |

### Audit

For each robustness check claimed:
- Is the threat it addresses named?
- Are results reported (coefficients, SEs)?
- Are results compared to main results (sign, significance, magnitude)?
- Is the comparison interpreted (e.g., "results are consistent in sign and significance, with magnitude X% smaller")?

### Common failures

- "Results are robust" stated without showing the alternative specification
- Robustness section is a list of model variants but none explicitly addresses a named threat
- All robustness checks address the same threat (e.g., 5 model variants for endogeneity but no construct-validity robustness)

---

## Empirical alternative-explanation rule-outs (Dim 5.4)

Dim 3.3 (theoretical alternative explanations) is mirrored at Dim 5.4 with the **empirical** test:

For each alternative theoretical mechanism named in Dim 3:
- Does the design or analysis empirically rule it out?
- If selection: was a Heckman / IV / matched-sample analysis done?
- If reverse causality: was a Granger test, IV, or DiD on lagged shock done?
- If confounding mechanism: was the competing mechanism's predicted moderator tested?

### Example

If Dim 3 says "we rule out selection theoretically because firms cannot anticipate the regulatory shock", Dim 5.4 should report:

- A formal test of selection (e.g., predicting treatment assignment from observable firm characteristics)
- An IV regression with a credible exclusion restriction
- A subsample analysis of firms that could not have anticipated the shock

If Dim 3 names alternatives but Dim 5.4 doesn't empirically test them, Dim 5.4 ≤ 1.

---

## Method tier × UTD24 outlet fit

| Method tier | Typical UTD24 outlet |
|---|---|
| Archival panel with clean identification (DiD, IV, RDD) | SMJ, AMJ, MS, ASQ |
| Archival panel without identification | reviewer-rejection-prone at SMJ/AMJ; may fit OS or behavioral-focused AMJ |
| Field experiment | AMJ (primary), ASQ, MS |
| Lab experiment with executives | Strategy Science, OS, AMJ (less common) |
| Lab experiment with students | AMR (if pure theory test), OS — reviewers will scrutinize ecological validity |
| Formal / analytical | AMR, MS, Strategy Science |
| Computational simulation | MS, OS, Strategy Science |
| Qualitative case (long-form ethnography) | ASQ (primary), AMJ |
| Mixed methods | AMJ, ASQ |

A clean DiD on a strategy question is more likely to survive SMJ than a beautifully theorized cross-sectional survey. The Dim 5 ↔ Dim 1-4 ratio matters: a paper with brilliant theory and weak identification will struggle at SMJ / AMJ regardless of Dim 1-4 scores.

---

## REVIEW mode R2 attack patterns

R2 will attack on:

- **Causal overclaim**: "the abstract and discussion use 'causes' / 'leads to' but the design is cross-sectional / panel-without-identification; calibrate claims downward"
- **Construct validity gap**: "the key IV (X) is operationalized via [measure] without validation evidence; reviewers in this lineage will reject"
- **Robustness thinness**: "robustness section reports model variants but does not address [obvious threat]; recommend [specific robustness test]"
- **Untested alternative**: "the paper theoretically rules out [alternative] but does not test it empirically; this is the obvious extension reviewers will demand"
- **Mediation strong assumptions**: "the mediation analysis assumes no unmeasured confounders between M and Y — a strong and unstated assumption; address explicitly or replace with bounds analysis"

---

## What scores ≥18/20 on Dim 5

The paper:
- Claim verbs match identification table everywhere
- All key constructs use validated measures (with citations) or include new-measure validation in the manuscript
- Robustness section reports 3+ checks targeting distinct named threats
- Empirically tests at least 2 alternative explanations named in Dim 3

What scores 0-8/20: cross-sectional design with "causes" claims, freshly invented critical construct without validation, no robustness section, no empirical engagement with alternatives.
