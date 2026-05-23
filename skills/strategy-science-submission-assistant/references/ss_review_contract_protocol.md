---
file: ss_review_contract_protocol.md
purpose: >
  Paper-content-blind review contract used to make Strategy Science reviewer
  simulation more calibrated and less post-hoc.
last_verified: 2026-05-23
---

# Strategy Science Review Contract Protocol

Use this protocol in REVIEW mode before generating paper-visible reviewer
reports. The contract makes the simulated review less arbitrary by declaring the
review dimensions and fatal flaws before applying them to the manuscript.

## Phase 1: Review contract

Declare the review standards before reading paper details beyond the intake
metadata.

```
## Review Contract
Scope: QUICK_REVIEW / STANDARD_REVIEW / FULL_REVIEW
Method tier: archival / survey / experiment / formal theory / computational / qual case / mixed / meta / unknown

Weights:
- SS fit: __/20
- Theoretical movement: __/25
- Method-claim alignment: __/25
- Writing and positioning: __/15
- Citation integrity: __/15

Fatal flaws:
- Mis-fit with Strategy Science strategy domain
- No theoretical movement beyond empirical extension
- Causal language unsupported by design
- Invalid or undisclosed LLM-as-measurement pipeline
- Invented, missing, or misaligned citations for core theoretical claims
- Systemic AI-style prose that weakens credibility

Evidence needed:
- ...
```

## Phase 2: Paper-visible review

Apply the declared contract. New issues may be added only when labeled
`Emergent issue`.

## Phase 3: Editorial synthesis

Use this decision mapping:

| Total score | Simulation label |
|---:|---|
| 85-100 | Submission-ready after light polish |
| 75-84 | Promising but needs one focused revision |
| 60-74 | Major pre-submission revision needed |
| <60 | Not ready for Strategy Science |

Do not predict acceptance. Use risk language: desk-reject risk, review
probability, and revision burden.

