---
file: jbr_claim_evidence_matrix.md
purpose: Anti-overclaim calibration table. Maps empirical design to the strongest defensible claim verb. Consulted in POLISH Stage 4 and in every section rewrite that involves causal language.
last_verified: 2026-05-17
---

# Claim–Evidence Calibration Matrix

JBR reviewers consistently flag manuscripts where the claim language outruns the design. This file gives the **upper bound** of claim-strength for each common empirical design, plus recommended verbs and a "do-not-use" list.

When rewriting, **scan every causal-sounding verb** (causes, drives, leads to, produces, results in, generates, makes, gives rise to, induces, triggers) and check the design row. If the design does not support the verb, swap for a verb from the **Allowed** column.

---

## Master matrix

| Design | Strongest defensible claim | Allowed verbs | Do NOT use | Required hedges in discussion |
|---|---|---|---|---|
| Pure cross-sectional survey (single-time, single-source) | Association | is associated with, correlates with, co-varies with | causes, leads to, produces, drives, results in, predicts (future) | "Cross-sectional design precludes causal inference." |
| Cross-sectional survey, multi-source (different respondents for IV and DV) | Association with reduced CMV | is associated with, is linked to, relates to | causes, drives | "Although multi-source data reduce common-method bias, the design remains cross-sectional." |
| Lagged survey (T1 IV, T2 DV) | Temporal precedence (weak causal) | predicts, is followed by, is linked over time to | causes, drives | "Temporal lag supports but does not establish causality; omitted variables may explain the association." |
| Cross-sectional archival, no identification | Association | is associated with, correlates with | causes, drives | Same as cross-sectional survey |
| Panel archival with firm + year FE | Within-firm association | within firms, X is associated with Y; X predicts within-firm changes in Y | causes (without IV/DiD/RDD) | "Firm fixed effects absorb time-invariant heterogeneity but not time-varying confounders." |
| DiD with verified parallel trends | Quasi-causal (treatment effect) | the introduction of X is followed by a change in Y; X has an effect on Y in the treated group | causes (in general); replace with "treatment effect of X on Y" | "DiD identifies the treatment effect under the parallel-trends assumption; pre-trend test reported." |
| IV with credible exclusion + relevance | Causal (LATE on compliers) | X causally affects Y (for compliers); X has a causal effect on Y | causes (without naming the LATE) | "IV estimates identify a local average treatment effect under exclusion and relevance assumptions." |
| RDD with bandwidth and McCrary tests | Causal (local) | X causally affects Y at the cutoff; the local effect of X on Y is | causes (globally) | "RDD identifies a local causal effect near the cutoff; extrapolation beyond the bandwidth is not warranted." |
| Lab experiment, random assignment, single setting | Causal (internal validity), bounded external validity | X causes Y; manipulating X changes Y | (the construct, not the manipulation) "X-in-general causes Y-in-general" | "External validity beyond the experimental setting requires further study." |
| Field experiment (RCT) with attrition checks | Causal | the intervention causes; the program has a causal effect on | (over-generalize beyond the sample) | "Generalizability beyond the study sites is conditional on context similarity." |
| Vignette / scenario experiment | Causal at the perception/decision-intention level | manipulating X changes intended Y; perceptions of X cause intended Y | "X causes actual Y" (without behavioral data) | "Findings concern intentions/perceptions; translation to actual behavior requires field validation." |
| Qualitative case study (single) | Theory-extending illustration | suggest, illustrate, indicate, are consistent with, point to | causes, demonstrates, proves | "Single-case design supports analytic, not statistical, generalization." |
| Multi-case study | Theory-building / pattern across cases | suggest, indicate, build theory regarding, show a pattern of | causes (in a statistical sense) | "Analytic generalization to theory; statistical generalization to populations is not claimed." |
| Mixed-methods sequential (qual → quant) | Triangulated association; mechanism explanation | the qualitative phase identifies; the quantitative phase confirms an association | causes | "The qualitative mechanism is consistent with the quantitative association; causal status requires further design." |
| Meta-analysis | Aggregate association across studies | meta-analytic association; the pooled estimate suggests | causes | "Meta-analytic estimate is correlational; underlying study designs vary." |
| Conceptual / theoretical paper | Theoretical proposition | propose, theorize, conceptualize, argue | empirically demonstrate, show, find | "Empirical testing is required to evaluate the propositions." |
| Computational / simulation | Model-consistent prediction | the model implies, simulations show under stated assumptions | causes (in the real world, without empirical link) | "Simulation results depend on the stated parameters; external validity requires empirical calibration." |

---

## Verb swap table (common rewrites)

| Original (too strong) | Replace with (calibrated) | Use when |
|---|---|---|
| X causes Y | X is associated with Y | Cross-sectional, no identification |
| X causes Y | X predicts Y | Lagged design |
| X causes Y | X has an effect on Y | DiD/IV/RDD/experiment with proper identification |
| X drives Y | X is linked to Y | Cross-sectional |
| X leads to Y | X is followed by Y | Time-lagged but not identified |
| X produces Y | X corresponds to higher Y | Cross-sectional |
| X improves Y | X is positively associated with Y | Cross-sectional |
| X harms Y | X is negatively associated with Y | Cross-sectional |
| X determines Y | X shapes Y (with hedge) OR X is a predictor of Y | Soft theoretical language without causal claim |
| X enables Y | X is positively related to Y | If no mechanism evidence |
| X explains Y | X accounts for variance in Y | Statistical without theory of mechanism |

---

## Boundary / moderator claim language

| Pattern | Use when |
|---|---|
| The association between X and Y is stronger when M is high | Standard moderation, OLS |
| The relationship between X and Y depends on M | Moderation with theoretical contingency |
| The X–Y link is contingent on M | Conceptual phrasing |
| Under conditions of high M, X is more strongly associated with Y | Specific contingency statement |
| **Avoid**: M moderates the causal effect of X on Y (unless identification supports causal X→Y) | — |

---

## Mediation language

| Pattern | Use when |
|---|---|
| X is associated with Y, and this association is consistent with mediation by Z | Cross-sectional mediation test (Baron-Kenny, bootstrap) — **always hedge** |
| The indirect path X → Z → Y is significant in our model | Reporting the statistical pattern |
| Z is a candidate mechanism linking X and Y | Theoretical mechanism with statistical association |
| **Avoid**: X causes Y through Z (cross-sectional) | — |

---

## Generalization language

| Pattern | Use when |
|---|---|
| Within our sample of [N] [units] in [setting], we find… | Always — keep generalization bounded |
| These findings may extend to [setting] to the extent that [boundary condition] holds | Theoretical generalization |
| **Avoid**: "Firms in general" / "Managers everywhere" without scope conditions | — |

---

## Application in polishing

1. **Pass 1 — Verb sweep**: scan abstract, intro, results, discussion. Flag every verb in the "Do NOT use" column.
2. **Pass 2 — Swap**: replace with the calibrated verb from the swap table.
3. **Pass 3 — Hedge**: ensure the required hedge appears in the discussion's limitations or claim-strength paragraph.
4. **Pass 4 — Audit consistency**: abstract claim verb ≡ discussion claim verb ≡ contribution claim verb. If not, harmonize down to the weakest defensible verb.

A common reviewer comment is "the manuscript over-claims causality." Running this matrix before submission catches that comment in ~80% of cases.
