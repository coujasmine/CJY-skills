---
title: TMT Myopia and AI Adoption in U.S. Public Firms, 2015–2024
author:
  - Author One, University of Somewhere
  - Author Two, Another University
abstract: |
  This paper examines how top management team (TMT) temporal orientation affects the adoption of artificial intelligence in U.S. public firms over the 2015–2024 period. Drawing on the attention-based view, we hypothesize that TMTs exhibiting greater short-term orientation — what we term TMT myopia — are less likely to invest in AI initiatives, but more likely to abandon them prematurely once initiated. We test the hypotheses on a panel of 1,847 firm-year observations using a difference-in-differences design exploiting variation in board composition shocks. Results support the abandonment hypothesis but show mixed support for the adoption hypothesis. We contribute to the literature on TMT cognition and firm innovation by introducing a behavioral mechanism into the AI-strategy nexus.
keywords: TMT cognition; AI adoption; temporal orientation; attention-based view; longitudinal
---

# Introduction

The diffusion of artificial intelligence (AI) across U.S. firms has been uneven. Some firms commit early and persist, others enter late, and a non-trivial share start and then abandon. Existing explanations focus on resource endowments and competitive pressures, but a behavioral account remains underdeveloped.

This paper proposes that top management team (TMT) temporal orientation — the time horizon over which executives evaluate strategic options — is a first-order determinant of AI investment behavior. We focus on TMT myopia: the tendency to weight near-term outcomes disproportionately.

## Research question

Does TMT myopia explain heterogeneity in AI adoption and abandonment among large U.S. firms?

# Theory and Hypotheses

## Theoretical background

We draw on the attention-based view of the firm and on prospect-theoretic accounts of managerial decision-making.

## Hypothesis 1: Adoption

> H1: Firms with more myopic TMTs are less likely to initiate AI investments.

The argument: AI investments have front-loaded costs and back-loaded returns. Myopic TMTs over-weight the cost side.

## Hypothesis 2: Abandonment

> H2: Conditional on adoption, firms with more myopic TMTs are more likely to abandon AI initiatives within three years.

The argument: even after initiation, myopic TMTs face ongoing temptation to redeploy resources to near-term projects.

# Methods

## Sample

Our sample includes 1,847 firm-year observations covering 312 U.S. public firms in NAICS sectors 31–33 and 51 over 2015–2024. We compiled the panel from Compustat, ExecuComp, and a hand-coded set of AI-investment announcements drawn from 10-K filings.

## Measures

Table: Construct definitions and data sources.

| Construct        | Measure                                                  | Source                  |
|------------------|----------------------------------------------------------|-------------------------|
| TMT myopia       | Average of CEO and CFO 2-yr equity vesting ratios        | ExecuComp               |
| AI adoption      | First-time AI capex disclosure in 10-K                   | Hand-coded from EDGAR   |
| AI abandonment   | Cessation of AI capex disclosure for ≥ 2 consecutive yrs | Hand-coded from EDGAR   |
| Firm size        | log(total assets)                                        | Compustat               |
| R&D intensity    | R&D / total assets                                       | Compustat               |

*Note.* All firm-level controls are lagged one year. Industry fixed effects are at the 4-digit NAICS level.

## Identification

We exploit exogenous board-composition shocks (deaths and forced retirements identified from 8-K filings) as a source of variation in TMT myopia. The identifying assumption is that the timing of such shocks is uncorrelated with unobserved determinants of AI adoption.

# Results

## Main results

Table: Logit estimates of AI adoption (N = 1,847).

| Variable          | Model 1        | Model 2        | Model 3        |
|-------------------|----------------|----------------|----------------|
| TMT myopia        | −0.214 (0.142) | −0.198 (0.139) | −0.176 (0.144) |
| Firm size         |                | 0.087** (0.031)| 0.082** (0.031)|
| R&D intensity     |                |                | 1.42** (0.51)  |
| Industry FE       | Yes            | Yes            | Yes            |
| Year FE           | Yes            | Yes            | Yes            |
| Pseudo R²         | 0.043          | 0.061          | 0.078          |

*Note.* Standard errors clustered by firm in parentheses. *p* < .10, **p* < .05, ***p* < .01.

The TMT myopia coefficient on adoption is negative as predicted but does not reach statistical significance at conventional thresholds.

## Abandonment

Table: Cox proportional hazards estimates of AI abandonment.

| Variable          | Hazard ratio | 95% CI         |
|-------------------|--------------|----------------|
| TMT myopia        | 1.83**       | [1.21, 2.78]   |
| Firm size         | 0.91         | [0.78, 1.06]   |
| R&D intensity     | 0.42**       | [0.22, 0.81]   |

*Note.* N = 412 firms initiating AI investment between 2015 and 2021.

Abandonment results are consistent with H2. Myopic TMTs face an 83% higher abandonment hazard, holding firm size and R&D intensity constant.

# Discussion

The pattern of results — null on adoption, strong on abandonment — is consistent with a behavioral account in which the cost of starting AI is salient and computable at the adoption decision, but the cost of abandonment is silent until ongoing pressures expose it.

## Contributions

We contribute to (a) the literature on TMT cognition and innovation by isolating temporal orientation as a mechanism, and (b) the AI-strategy literature by drawing attention to abandonment as distinct from adoption.

## Limitations

Our myopia proxy relies on equity-vesting horizons, which are noisy. Future work could triangulate with text-based measures from earnings-call transcripts.

# References

The reference list goes here. Replace this paragraph with your actual references, pre-formatted in the journal's required style, or supply a `.bib` file to `md_to_docx.py` via `--bibliography` and `--csl`.
