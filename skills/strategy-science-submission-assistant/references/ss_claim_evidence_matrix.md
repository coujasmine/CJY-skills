---
file: ss_claim_evidence_matrix.md
purpose: Anti-overclaim calibration table tuned for Strategy Science designs. Maps empirical design to strongest defensible claim. Consulted in POLISH Stage 4 and every section rewrite involving causal or theoretical-claim language.
last_verified: 2026-05-21
---

# Strategy Science Claim-Evidence Calibration Matrix

## Contents

- Master matrix
- Verb swap table (common rewrites)
- Theory-paper claim language (SS-specific)
- Boundary / moderator claim language
- Mediation language
- Generalization language
- LLM-as-measurement claim language
- ML-as-prediction claim language
- Application in polishing


SS reviewers are especially demanding on claim-evidence calibration because the journal publishes alongside cognitive psychology, formal economics, and management — three traditions with different identification cultures. Manuscripts that overclaim get rejected on Reviewer 2's first read.

This file gives the **upper bound** of claim-strength for each common SS empirical design, plus recommended verbs and a "do-not-use" list.

When rewriting, **scan every causal-sounding verb** (causes, drives, leads to, produces, results in, generates, makes, gives rise to, induces, triggers) and check the design row. If the design does not support the verb, swap for a verb from the **Allowed** column.

---

## Master matrix

| Design | Strongest defensible claim | Allowed verbs | Do NOT use | Required hedges in discussion |
|---|---|---|---|---|
| Pure cross-sectional survey | Association | is associated with, correlates with, co-varies with | causes, leads to, produces, drives, results in, predicts (future) | "Cross-sectional design precludes causal inference." |
| Cross-sectional survey, multi-source | Association with reduced CMV | is associated with, is linked to, relates to | causes, drives | "Although multi-source data reduce common-method bias, the design remains cross-sectional." |
| Lagged survey (T1 IV, T2 DV) | Temporal precedence (weak causal) | predicts, is followed by, is linked over time to | causes, drives | "Temporal lag supports but does not establish causality; omitted variables may explain the association." |
| Cross-sectional archival, no identification | Association | is associated with, correlates with | causes, drives | Same as cross-sectional survey |
| Panel archival with firm + year FE (e.g., Asghar et al. on insider trading) | Within-firm association | within firms, X is associated with Y; X predicts within-firm changes in Y | causes (without IV/DiD/RDD) | "Firm fixed effects absorb time-invariant heterogeneity but not time-varying confounders." |
| Panel archival with firm + year FE + ML-derived measure (Qu et al. 2026) | Within-firm association; ML predictions correlate with outcomes | predictions are associated with; the disparity correlates with | causes; the ML predictions caused | "ML predictions capture cues correlated with outcomes; they do not establish causality between predictions and outcomes." |
| DiD with verified parallel trends | Quasi-causal (treatment effect) | the introduction of X is followed by a change in Y; X has an effect on Y in the treated group | causes (in general); replace with "treatment effect of X on Y" | "DiD identifies the treatment effect under the parallel-trends assumption; pre-trend test reported." |
| IV with credible exclusion + relevance | Causal (LATE on compliers) | X causally affects Y (for compliers); X has a causal effect on Y | causes (without naming the LATE) | "IV estimates identify a local average treatment effect under exclusion and relevance assumptions." |
| RDD with bandwidth and McCrary tests | Causal (local) | X causally affects Y at the cutoff; the local effect of X on Y is | causes (globally) | "RDD identifies a local causal effect near the cutoff; extrapolation beyond the bandwidth is not warranted." |
| Lab experiment, random assignment, single setting (rare at SS) | Causal (internal validity), bounded external validity | X causes Y; manipulating X changes Y | (the construct, not the manipulation) "X-in-general causes Y-in-general" | "External validity beyond the experimental setting requires further study." |
| Online experiment via Prolific/MTurk (Kanis et al. 2026 pattern) | Causal at the perception/decision level, bounded external validity | manipulating X changes Y in our sample; the 2×2 design shows that X affects Y | "X causally affects firm performance" (without behavioral firm-level data) | "Findings concern decision-makers in an online task; field validation is warranted. Excluding participants who failed manipulation checks is reported." |
| Vignette / scenario experiment | Causal at the perception/decision-intention level | manipulating X changes intended Y; perceptions of X cause intended Y | "X causes actual Y" (without behavioral data) | "Findings concern intentions/perceptions; translation to actual behavior requires field validation." |
| Field experiment (RCT) with attrition checks | Causal | the intervention causes; the program has a causal effect on | (over-generalize beyond the sample) | "Generalizability beyond the study sites is conditional on context similarity." |
| Qualitative case study (single) | Theory-extending illustration | suggest, illustrate, indicate, are consistent with, point to | causes, demonstrates, proves | "Single-case design supports analytic, not statistical, generalization." |
| Multi-case study | Theory-building / pattern across cases | suggest, indicate, build theory regarding, show a pattern of | causes (in a statistical sense) | "Analytic generalization to theory; statistical generalization to populations is not claimed." |
| Mixed-methods sequential (qual → quant) | Triangulated association; mechanism explanation | the qualitative phase identifies; the quantitative phase confirms an association | causes | "The qualitative mechanism is consistent with the quantitative association; causal status requires further design." |
| Meta-analysis | Aggregate association across studies | meta-analytic association; the pooled estimate suggests | causes | "Meta-analytic estimate is correlational; underlying study designs vary." |
| **Pure conceptual / theoretical paper (Clough 2026 style)** | Theoretical proposition | propose, theorize, conceptualize, argue, the framework predicts, the theory implies, the typology identifies | empirically demonstrate, show (in the data), find | "Empirical testing is required to evaluate the propositions. The framework yields testable predictions stated in §X." |
| Computational / simulation | Model-consistent prediction | the model implies, simulations show under stated assumptions, the analysis yields | causes (in the real world, without empirical link) | "Simulation results depend on the stated parameters; external validity requires empirical calibration." |
| Formal game-theoretic model (Clough §3 pattern) | Equilibrium-conditional prediction | in equilibrium; under condition X, the model predicts; the game yields | causes; demonstrates empirically | "Predictions are conditional on the model's assumptions; empirical relaxation of assumptions is future work." |

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
| We demonstrate that X causes Y | We argue that X shapes Y / The framework predicts that X conditions Y | Pure-theory paper |
| We prove that X | We show analytically that X / Under the stated assumptions, X | Formal theory |
| AI improves strategic decision-making | LLM use is associated with [breadth/depth/etc.] of mental representations | Online experiment with LLM treatment (Kanis 2026) |
| ML predictions cause better acquisition outcomes | ML predictions are correlated with positive market reactions; following predictions could have captured greater value | Archival + ML (Qu 2026) |

---

## Theory-paper claim language (SS-specific)

For pure-theory papers like Clough 2026, the claim ladder is different. Use:

| Claim level | Pattern | Example |
|---|---|---|
| Definitional | "I define X as Y" / "I use the term X to refer to Y" | Clough defines coordination speed and coordination scope |
| Conceptual | "I conceptualize X as Y" / "I distinguish X from Y" | Clough conceptualizes ecosystem architectures as assemblages of governance structures |
| Theoretical proposition | "I propose that X is associated with Y under condition Z" / "The framework predicts that X is more effective when Y" | Clough proposes that centralized governance outperforms in high-dynamism settings |
| Equilibrium claim | "In equilibrium, X holds" / "Under the stated assumptions, the game yields X" | "Pre-game cheap talk communication raises the likelihood of coordination" |
| Typological claim | "Architectures with property X align with environment Y" | Discriminating alignment between architecture and environment |
| Trilemma / trade-off claim | "X can deliver at most two of three of {A, B, C}" | Clough's architectural trilemma |

**Do NOT** use empirical verbs in a pure-theory paper:
- ❌ "We find that..." → ✓ "The framework predicts that..."
- ❌ "Our results show..." → ✓ "The analysis yields..."
- ❌ "We demonstrate that..." → ✓ "We show analytically that..." or "We argue that..."

---

## Boundary / moderator claim language

| Pattern | Use when |
|---|---|
| The association between X and Y is stronger when M is high | Standard moderation, OLS |
| The relationship between X and Y depends on M | Moderation with theoretical contingency |
| The X–Y link is contingent on M | Conceptual phrasing |
| Under conditions of high M, X is more strongly associated with Y | Specific contingency statement |
| In equilibria with high M, the X-Y prediction holds more strongly | Formal-theory moderation |
| **Avoid**: M moderates the causal effect of X on Y (unless identification supports causal X→Y) | — |

---

## Mediation language

| Pattern | Use when |
|---|---|
| X is associated with Y, and this association is consistent with mediation by Z | Cross-sectional mediation test (Baron-Kenny, bootstrap) — **always hedge** |
| The indirect path X → Z → Y is significant in our model | Reporting the statistical pattern |
| Z is a candidate mechanism linking X and Y | Theoretical mechanism with statistical association |
| Our additional analyses suggest [mechanism Z]; e.g., LLM use increases information overload | "Additional analyses suggest" / "Additional analyses indicate" pattern (Kanis et al. 2026 idiom) |
| **Avoid**: X causes Y through Z (cross-sectional) | — |

---

## Generalization language

| Pattern | Use when |
|---|---|
| Within our sample of [N] [units] in [setting], we find… | Always — keep generalization bounded |
| These findings may extend to [setting] to the extent that [boundary condition] holds | Theoretical generalization |
| **Avoid**: "Firms in general" / "Managers everywhere" without scope conditions | — |
| Our use of [Kickstarter startups / S&P 500 firms / U.S. public acquirers] as the strategic decision-making context may raise questions of generalizability. However, this design has proven useful in… | SS limitations-paragraph idiom (Kanis 2026, Qu 2026) |

---

## LLM-as-measurement claim language

When the design uses LLMs to code constructs (e.g., classifying pros/cons into strategic categories à la Kanis et al. 2026):

| Pattern | Use when |
|---|---|
| We measured X using LLM-based coding with inter-rater reliability of [α/κ] = [value] | Standard reporting |
| The LLM classification was validated against human coders with [Krippendorff α] = [value] | Reliability statement |
| Across [N] LLMs (gpt-X, claude-X, mistral-X), agreement was [r/α] = [value] | Multi-LLM sensitivity (Kanis 2026 used three LLMs, r=0.93) |
| **Avoid**: The LLM accurately identified X | (Implies ground truth without validation) |
| **Avoid**: The LLM understood / knew / determined | (Anthropomorphizing language; SS reviewers flag) |

---

## ML-as-prediction claim language

When the design uses ML to predict an outcome and uses the prediction as a construct (Qu et al. 2026):

| Pattern | Use when |
|---|---|
| The trained ML model yields a predicted [outcome] with R² = [value] in the out-of-sample test set | Standard reporting |
| Predicted [outcome] is correlated with actual [outcome] at r = [value] | Validation against ground truth |
| We benchmark the ML model against an OLS baseline reporting R² = [value] | Baseline comparison (Qu et al. 2026 Table 1) |
| Predictions capture the wisdom of crowds reflected in [market/expert] reactions | Theoretical framing for ML-as-cue-aggregator |
| **Avoid**: The ML model knows / understands / decides | (Anthropomorphizing) |

---

## Application in polishing

1. **Pass 1 — Verb sweep**: scan abstract, intro, results, discussion. Flag every verb in the "Do NOT use" column.
2. **Pass 2 — Swap**: replace with the calibrated verb from the swap table.
3. **Pass 3 — Hedge**: ensure the required hedge appears in the discussion's limitations or claim-strength paragraph.
4. **Pass 4 — Audit consistency**: abstract claim verb ≡ discussion claim verb ≡ contribution claim verb. If not, harmonize down to the weakest defensible verb.
5. **Pass 5 — Theory-paper check**: if the paper is pure-theory (Clough pattern), all empirical verbs should be removed from the main text (results-language is only appropriate inside an "illustration" or "extension" subsection).

A common SS Reviewer 2 comment is "the empirical claims outrun the design." Running this matrix before submission catches that comment in ~80% of cases.
