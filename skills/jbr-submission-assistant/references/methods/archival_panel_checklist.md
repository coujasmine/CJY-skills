---
file: archival_panel_checklist.md
purpose: >
  Archival and panel-data method checklist for JBR manuscripts. Use with
  method/results/robustness audits, REVIEW mode Reviewer 2, and claim-evidence
  calibration for panel designs.
last_verified: 2026-05-18
---

# Archival Panel Checklist

Use this file when the manuscript relies on archival, panel, text-derived, database-derived, patent, financial, or firm-year data. It supplements `references/jbr_method_checklists.md`; it does not replace the universal method-fit checks.

## 1. Sample Construction

Check whether the method section reports:

- Data sources and database names.
- Observation level: firm-year, firm-quarter, manager-year, patent-year, subsidiary-year, etc.
- Sample window and rationale for the start/end years.
- Inclusion and exclusion rules.
- Industry, country, exchange, ownership, or listing restrictions.
- Missing-data handling and winsorization/trimming rules.
- Final sample size in firms, years, and observations.
- Why the empirical setting is theoretically informative, not merely convenient.

For China-listed-firm samples, require a short rationale for why the Chinese context reveals the focal mechanism, such as rapid AI diffusion, regulatory disclosure variation, capital-market pressure, state ownership, regional digital infrastructure, or manager-governance features.

## 2. Construct and Measure Alignment

For every focal construct, check:

- The construct is defined before the measure is introduced.
- The measure captures the construct, not a neighboring concept.
- The level of the measure matches the level of theory.
- The time window of the measure matches the hypothesized process.
- Text-based or AI-based measures include dictionary/model logic, preprocessing choices, and validation evidence.

For AI-capability manuscripts, require distinction among:

- AI adoption or investment.
- AI capability as organizational capability.
- Discovery-oriented AI capability.
- Automation-oriented AI or efficiency-focused digitalization.
- General digital transformation.

If the manuscript uses text or GPT-assisted coding, require at least one of:

- Human validation on a sampled subset.
- Inter-coder reliability for hand labels.
- Convergent validity with external indicators.
- Sensitivity to alternative dictionaries/prompts/models.
- False-positive review of high-scoring observations.

## 3. Panel Timing

Check:

- Independent variables are lagged where theory implies temporal ordering.
- Dependent variables are measured after the focal predictor where possible.
- Mediators are temporally located between predictor and outcome when claiming a mechanism.
- Moderators are pre-treatment or plausibly stable if interpreted as boundary conditions.
- The paper does not interpret same-year associations as temporal effects without justification.

## 4. Fixed Effects and Model Architecture

Match fixed effects to the claim and data structure:

- Firm fixed effects: controls for time-invariant firm heterogeneity.
- Year fixed effects: controls for common shocks.
- Industry-year fixed effects: controls for industry-specific temporal shocks.
- Province-year or region-year fixed effects: useful when regional policy, infrastructure, or market development may drive the effect.
- Manager fixed effects: only when the same managers are observed across firms or years and the research question supports it.

Report whether standard errors are clustered at the right level. Firm-level clustering is common for firm-year panels; two-way clustering may be needed when shocks are shared across firms and years.

## 5. Endogeneity Threats

Name the threats proportionately. Do not require every design to claim causality, but do require transparent limits.

Common threats:

- Reverse causality: strategic orientation or performance may drive AI capability.
- Omitted variables: unobserved management quality, governance, resources, digital infrastructure, regional policy, or industry turbulence.
- Selection: firms adopting AI may differ systematically before adoption.
- Simultaneity: attention allocation and AI capability may co-evolve.
- Measurement error: text-based proxies may capture disclosure style rather than the construct.
- Common shocks: policy, industry cycles, or capital-market pressure may affect both predictor and outcome.

## 6. Robustness Sequencing

Robustness checks should map to named threats:

| Threat | Useful checks |
|---|---|
| Alternative measurement | Alternative dependent variable, alternative independent variable, alternative dictionary/model, hand-validated measure |
| Timing and reverse causality | Lagged predictors, future predictor placebo, lead-lag checks |
| Omitted variables | Rich controls, firm FE, industry-year FE, region-year FE, Oster-type sensitivity where appropriate |
| Selection | PSM, entropy balancing, coarsened exact matching, pre-trend comparison |
| Influential observations | Winsorization choices, excluding high-leverage industries/firms/years |
| Common shocks | Exclude shock years, add policy/region-year controls, industry-year FE |
| Causal identification | DiD, IV, RDD, event study only when the setting genuinely supports it |

Do not ask for IV, DiD, or RDD mechanically. If the design does not support credible identification, recommend claim softening rather than pseudo-causal overreach.

## 7. Mechanism and Attention Evidence

For manuscripts using attention-based view or managerial attention arguments, check whether the evidence speaks to attention allocation rather than only firm outcomes.

Possible attention evidence:

- TMT speech, MD&A, annual-report, earnings-call, or meeting-text attention measures.
- Changes in resource allocation consistent with the attention mechanism.
- Mediators that directly capture temporal horizon, exploration/exploitation, innovation attention, or short-term performance pressure.
- Moderators that theoretically affect information processing or attention allocation, such as TMT background, governance pressure, analyst scrutiny, digital infrastructure, or environmental dynamism.

If mechanism evidence is indirect, use "evidence consistent with the theorized mechanism" rather than "demonstrates the mechanism."

## 8. Results Reporting

Require:

- Descriptives and correlations before models.
- Model sequence that follows the hypotheses.
- Coefficients, standard errors or t-statistics, significance, and substantive interpretation.
- Interaction plots or marginal effects for moderation.
- Direct/indirect effect intervals for mediation where applicable.
- Robustness explained by threat, not just listed.

## 9. Claim Calibration

Use this language:

- Strong identification: "provides evidence that X affects Y" only when design supports causal interpretation.
- Panel FE without quasi-experimental shock: "is associated with," "predicts," or "is followed by."
- Mechanism not directly measured: "consistent with the proposed mechanism."
- Narrow setting: "in this context," "among [sample]," or "for [period/setting]."

Flag any manuscript that uses "causes," "drives," "leads to," "produces," or "demonstrates" when the method only supports association.
