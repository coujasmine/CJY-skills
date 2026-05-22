---
file: archival_panel_checklist.md
purpose: >
  Deep audit checklist for archival/panel-data methods at Strategy Science.
  Calibrated against Asghar et al. (insider trading + entropy index + BHAR)
  and Qu et al. 2026 (ML + event study + acquisitions). Used when method tier
  is archival/panel.
last_verified: 2026-05-21
---

# Archival/Panel Method Audit — Strategy Science

## Contents

- 1. Sample construction
- 2. Data sources and merging
- 3. Variable construction
- 4. Identification and econometric specification
- 5. ML-augmented archival (Qu pattern)
- 6. Results reporting
- 7. Robustness section
- 8. Additional analyses
- 9. SS-specific concerns
- Common SS Reviewer 2 concerns (archival panel)
- Calibration anchors


This file is the deep-dive checklist for archival/panel-data submissions to Strategy Science. Apply during AUDIT, REVIEW (Reviewer 2), and POLISH Stage 4.

---

## 1. Sample construction

- [ ] Sampling frame justified (e.g., why S&P 500? Why all public acquirers 1976-2022?)
- [ ] Sample period justified (data availability + relevance + variation)
- [ ] Sample size adequate for the design and effects expected
- [ ] Attrition/missingness handled and disclosed
- [ ] Final sample N reported clearly, with breakdowns (e.g., 1,803 managers across 257 firms with 2,863 product introductions = 18,263 observations)
- [ ] Inclusion/exclusion criteria explicit (Qu: U.S. acquirers, 100% ownership, transactions ≥ $10M, no buybacks, no financial services targets)
- [ ] Multiple-deal-same-day or other unique-observation issues addressed
- [ ] Survivorship bias addressed when relevant

## 2. Data sources and merging

- [ ] Each data source named and version-stamped (e.g., "BoardEx accessed [date]", "Capital IQ Key Developments database")
- [ ] Merging procedure across sources described
- [ ] Manual coding/validation steps disclosed (Asghar: 1,000 observations manually coded to train an ML algorithm that achieved 92.3% accuracy)
- [ ] Missing-data patterns checked for systematicity
- [ ] Cross-checks across sources reported

## 3. Variable construction

### Dependent variable

- [ ] Construct definition precedes measurement
- [ ] Measurement formula explicit (e.g., "We measured foresight as the 18-month buy-and-hold abnormal returns (BHAR) associated with firms' product introduction announcements.")
- [ ] Source(s) for component data cited
- [ ] Validation against alternative measures (e.g., correlation with related constructs)
- [ ] Justification for the measurement window (e.g., why 18 months for BHAR?)

### Independent variables

- [ ] Each IV constructed transparently
- [ ] For entropy-based measures: cite Teachman 1980; show formula
  - Teachman entropy: $$\sum_{j=1}^{N} P_j \ln(1/P_j)$$
- [ ] For event-study CARs: cite Fama-French model; show window choice (Qu: (-1, +1) days)
- [ ] For ML-derived measures: train-test split, algorithms compared, R² reported
- [ ] Time-period of measurement matches conceptual definition

### Control variables

- [ ] Each control justified theoretically (not kitchen-sink)
- [ ] Categories: firm-level (size, profitability, leverage, growth), individual-level (gender, age, tenure), governance (board size, independence), market-level (volatility, industry concentration), deal-level (size, payment type, FTC scrutiny)
- [ ] Industry and year fixed effects acknowledged but not over-relied
- [ ] Control variables not on the causal path of the IV→DV relationship (over-controlling)
- [ ] Reporting: descriptive stats and correlations in a table

## 4. Identification and econometric specification

### Model specification

- [ ] Estimator named (OLS, logit, fixed-effects, etc.)
- [ ] Fixed-effects structure: firm, year, industry, manager, deal as appropriate
- [ ] Standard errors: clustering level stated and justified
- [ ] Robust SE if heteroskedasticity expected
- [ ] Multi-level structure addressed if applicable

### Identification strategy

For causal claims (Stage 4 of POLISH must check):

- [ ] Identification strategy clearly stated
- [ ] If FE-only: claim language must be "association" or "within-firm" (no "causes")
- [ ] If IV: relevance + exclusion + monotonicity defended
- [ ] If DiD: parallel trends tested
- [ ] If RDD: McCrary density test, bandwidth justification
- [ ] If matching: balance tables, sensitivity to caliper

### Common threats

- [ ] Reverse causality: temporal precedence, lagged DVs, identification arguments
- [ ] Omitted variables: FE structure, identification, sensitivity bounds (Oster 2019)
- [ ] Selection: sample selection model if applicable; Heckman correction
- [ ] Measurement error: alternative measures, robustness
- [ ] Endogeneity in moderators: discuss

## 5. ML-augmented archival (Qu pattern)

When ML is used to construct a measure (e.g., predicted CAR):

- [ ] Multiple ML algorithms compared (OLS baseline + elastic net + random forest + gradient-boosted tree — Qu Table 1)
- [ ] Train-test split with time-series respect (Qu: 1976-2012 train; 2012-2022 test)
- [ ] Cross-validation procedure stated (Qu: 5-fold)
- [ ] R² (in-sample and out-of-sample) reported
- [ ] Feature importance reported (impurity-based and permutation-based — Qu Table 2)
- [ ] Best model selected on out-of-sample performance
- [ ] Sensitivity to alternative train-test splits (Qu reports 85-15 and 75-25 alternatives)
- [ ] Construct interpretation: how does the ML output map to the theoretical construct?

## 6. Results reporting

### Standard reporting order

1. Descriptive statistics (means, SDs, mins, maxes; Asghar Table 1)
2. Correlation matrix (Asghar Table 2; Qu Table 7)
3. Main test (regression coefficients, SE in parentheses, significance stars)
4. Robustness checks
5. Additional analyses / mechanism exploration

### Table conventions (INFORMS)

```
Variable                Model 1
Predicted CAR           0.707***
                        (0.171)
Public Target           0.003
                        (0.005)
...
N                       2,647
Adjusted R²             0.493

*Notes.* Dependent variable is [DV]. SE in parentheses. Firm, industry, and
year fixed effects included. ***p<0.001; **p<0.01; *p<0.05; †p<0.10.
```

- Coefficients first, SE in parentheses below
- Significance stars (one-sided or two-sided stated)
- FE structure noted
- Clustering noted

### Effect size interpretation

- [ ] Effect sizes interpreted in substantive terms (e.g., "a one-SD increase in industry knowledge breadth is associated with an X% decrease in 18-month BHAR")
- [ ] Not just "the coefficient was significant"

## 7. Robustness section

Each robustness check should:

- [ ] Be tied to a specific threat
- [ ] Use a different approach (alternative measure, alternative model, alternative sample, alternative time window)
- [ ] Be reported with full results (in main text or appendix)
- [ ] Not contradict the main findings; if contradictions exist, explain

Typical SS robustness checks for archival panel:

- Alternative DV measures (Asghar uses BHAR; could test CAR, ROA, Tobin's Q)
- Alternative sample restrictions (e.g., excluding industry sectors)
- Alternative FE structures (firm-only, year-only, both)
- Alternative clustering levels
- Alternative time windows
- Alternative entropy / index formulations
- Manager or position fixed effects (in addition to firm fixed effects — Asghar adds these)
- Subsample analyses for boundary conditions (Asghar: high vs. low VIX)
- Placebo tests

## 8. Additional analyses

SS rewards exploring mechanisms in an "Additional Analyses" subsection:

- [ ] Mediation tests (with hedging — see ss_claim_evidence_matrix.md)
- [ ] Moderation by theoretically motivated variables
- [ ] Heterogeneity across subsamples
- [ ] Mechanism evidence (e.g., job-role differences in Asghar; deal-stage differences in Qu)

## 9. SS-specific concerns

### "Fruit fly" setting argument

The empirical setting should be argued to be a particularly clean / informative context for the strategic mechanism. Asghar et al. argue insider trading is a "fruit fly" setting for foresight because:
1. It involves managers placing bets on future outcomes (revealing belief)
2. Human capital affects belief formation
3. Trades are precisely measured and reported to SEC

Qu et al. argue M&A is the right context for predictions because managers have strong incentives to predict market reactions and stakeholders have long paid attention to these reactions.

A weak setting-fit argument is a HIGH desk-reject risk.

### Construct-measure mapping

SS reviewers pay special attention to whether the empirical measure truly captures the theoretical construct. For example:
- "Knowledge breadth" measured by Teachman entropy on career history — does this capture *knowledge* or just *exposure*?
- "Mental representations" measured by ML predictions — is the ML aggregating cues the way managers do?

Be explicit about the gap between concept and measure; acknowledge limitations.

### Limitations section requirements

For archival panel:
- Selection effects (e.g., S&P 500 firms differ from smaller firms)
- Time window (specific years may not generalize)
- Cross-sectional vs. causal identification
- Construct measurement limitations
- External validity concerns

These should be substantive, not generic boilerplate.

---

## Common SS Reviewer 2 concerns (archival panel)

1. **"Why this setting?"** — even with a clear contribution, the setting must be argued to be informative.
2. **"How is causality established?"** — FE alone does not identify causality; reviewers will ask for IV/DiD/RDD or claim softening.
3. **"What about [obvious confound]?"** — reviewers will name specific confounds; preempt with controls and robustness.
4. **"The construct measurement is weak"** — concept ↔ measure gap must be defended explicitly.
5. **"Effect sizes are economically small"** — interpret in substantive terms; defend with theoretical importance.
6. **"Robustness checks are not connected to specific threats"** — each check should be tied to a named threat.
7. **"The mediation is cross-sectional"** — soften causal claim about mediation; report as consistent with the mechanism.

---

## Calibration anchors

- **Asghar et al.**: Panel archival with Teachman entropy + BHAR + VIX moderation. Clean fixed-effects identification with sub-sample analyses.
- **Qu et al. 2026**: Panel archival + ML prediction + event study + downstream OLS regression. Multiple ML algorithms compared; predictions used as a strategy construct with theoretical (Brunswik) grounding.
