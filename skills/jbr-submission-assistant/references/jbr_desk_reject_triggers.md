---
file: jbr_desk_reject_triggers.md
purpose: 30-second hard-check list. Any HIGH trigger fires → flag immediately to the user. Used at Stage 1 of the polishing pipeline and as the AUDIT mode core.
last_verified: 2026-05-17
---

# JBR Desk-Reject Triggers

These are the hard, mechanical checks that catch the most common reasons editors return a manuscript without external review. Run them **first**, before any spine or theory analysis. Each trigger lists:

- **Test**: the specific binary check
- **Severity**: HIGH (likely desk-reject) / MEDIUM (likely sent back for revision before review) / LOW (cosmetic)
- **Fix**: the minimum action to clear the trigger

If **any** HIGH trigger fires, surface it at the top of the verdict block. Polish can still proceed, but the trigger must be resolved before submission.

---

## A. Scope & Fit

| # | Test | Severity | Fix |
|---|---|---|---|
| A1 | Manuscript has no business decision, organization, market, or stakeholder anchoring (e.g., pure cognitive psychology lab, pure methodology paper, pure macroeconomics) | HIGH | Reframe with a business decision context, OR redirect to a non-JBR outlet |
| A2 | Contribution is "geographic novelty" only (e.g., "first study of X in [country]") with no theoretical refinement | HIGH | Add theoretical contribution: mechanism, boundary, or contextual modification of a known theory |
| A3 | Empirical setting chosen for convenience, with no argument for why this setting reveals the theoretical mechanism | HIGH | Add setting-rationale paragraph in method; tie to the phenomenon |
| A4 | Practical implications are generic ("managers should pay attention to X") and disconnected from the empirical findings | MEDIUM | Rewrite implications as specific actions tied to the mechanism the study identified |
| A5 | Paper is "interesting data, no theory" — a description of a dataset with no theoretical claim | HIGH | Add a primary theoretical conversation and a contribution beyond description |

## B. Format (mechanical)

| # | Test | Severity | Fix |
|---|---|---|---|
| B1 | Abstract length outside 100–150 words | HIGH | Trim or expand to ≤150 words (JBR ceiling) |
| B2 | Submission manuscript > 45 double-spaced pages (incl. figs/tables/refs) | HIGH | Trim; move material to online supplement |
| B3 | Keywords < 4 or > 6 | MEDIUM | Adjust to 4–6 |
| B4 | Title page is not separate from blinded manuscript, OR blinded manuscript contains author identifiers | HIGH | Move author info to a separate title page; redact from MS |
| B5 | Self-citations phrased as "in our earlier work" or "our previous paper" | HIGH | Rewrite as third-person citation, OR remove until acceptance |
| B6 | Figures/tables embedded mid-text rather than placed at the end (check JBR current guideline; varies by stage) | LOW | Move to end per current Author Guidelines |
| B7 | References inconsistent (mixed APA/Harvard/Chicago) | MEDIUM | Apply Elsevier-Harvard or APA consistently per current JBR guideline |
| B8 | Acknowledgements include identifying information (grant numbers, institutional thanks) in blinded MS | HIGH | Remove from blinded MS; place on title page |

## C. Disclosures (post-2024 Elsevier)

| # | Test | Severity | Fix |
|---|---|---|---|
| C1 | No AI-use disclosure paragraph | HIGH | Add a disclosure statement (see `jbr_disclosures_2024.md`); this skill counts as AI assistance |
| C2 | No CRediT contributor statement | MEDIUM | Add one (Conceptualization, Methodology, Investigation, Writing, etc.) |
| C3 | No Data Availability Statement | MEDIUM | Add a DAS even if "data not publicly available" — Elsevier requires an explicit statement |
| C4 | No Conflict of Interest statement | MEDIUM | Add one, even if "the authors declare none" |
| C5 | Human-subjects work without IRB / ethics statement | HIGH | Add IRB approval reference, OR explain exemption |
| C6 | Funding source not disclosed | MEDIUM | Add funding statement |

## D. Argument Spine (catches most "deeper" desk-rejects)

| # | Test | Severity | Fix |
|---|---|---|---|
| D1 | Research question is not visible by page 2 of the introduction | HIGH | Move RQ to intro paragraph 2 or 3 |
| D2 | Introduction opens with "Few studies have examined…" or "Little is known about…" instead of a business problem | MEDIUM | Replace literature-gap opening with a business-tension opening |
| D3 | No primary theoretical lens named in the introduction | HIGH | Name one primary theory; supporting theories must be auxiliary |
| D4 | Hypotheses lack named mechanism (only direction) | HIGH | Add mechanism sentence to each hypothesis |
| D5 | "Contribution" paragraph in intro lists three+ vague items ("we enrich the literature on…") | MEDIUM | Rewrite as one specific theoretical movement (mechanism / boundary / integration / clarification / reconciliation / contextualization) |
| D6 | Hypotheses tested in different direction or grain from how they were stated | HIGH | Align hypothesis wording with the actual test |
| D7 | Findings paragraph in abstract differs from findings paragraph in discussion | HIGH | Harmonize |

## E. Method ↔ Claim (cross-check with `jbr_claim_evidence_matrix.md`)

| # | Test | Severity | Fix |
|---|---|---|---|
| E1 | Cross-sectional design + causal verbs ("causes," "drives," "leads to," "produces") in abstract/intro/discussion | HIGH | Replace with association-based language |
| E2 | Mediation tested in cross-sectional data, claimed as causal mechanism | HIGH | Soften to "consistent with the proposed mechanism"; add limitation |
| E3 | Single informant for both IV and DV without CMV remedies | MEDIUM | Add procedural + statistical CMV remedies, OR acknowledge in limitations |
| E4 | Survey study without justification of informant choice (e.g., why this role can answer this question) | MEDIUM | Add informant rationale to method |
| E5 | Qualitative study without theoretical case selection logic | MEDIUM | Add case-selection rationale |
| E6 | Robustness section adds analyses unconnected to plausible reviewer concerns | LOW | Tie each robustness check to a specific threat |

## F. Originality & Overlap

| # | Test | Severity | Fix |
|---|---|---|---|
| F1 | Substantial text overlap (>30%) with a prior paper by same authors (working paper, conference, prior publication) | HIGH | Disclose to editor; rewrite the overlapping content; or withdraw |
| F2 | Same dataset used in a prior publication without distinct theoretical contribution here | HIGH | Either kill this manuscript, or distinguish the contribution sharply and disclose |
| F3 | "First paper to study X" claim without supporting search log or recent review | MEDIUM | Soften to "we contribute to an emerging literature on X by…", OR provide search evidence |
| F4 | Salami-sliced from a larger study without independent theoretical core | HIGH | Restore the integrated study, OR reposition to a fully distinct contribution |

## G. Special Issue Specific (if SI submission)

| # | Test | Severity | Fix |
|---|---|---|---|
| G1 | Paper does not explicitly cite the SI call's stated themes | HIGH | Map RQ/theory/method/implications to the call's themes; cite the call in the cover letter |
| G2 | SI deadline already passed | HIGH | Check whether late submissions are accepted; if not, retarget to regular issue |
| G3 | Guest editor list not acknowledged in cover letter | LOW | Address cover letter to "Guest Editors of the [SI title]" |

---

## How to use this list

1. **AUDIT mode**: run all triggers; produce a verdict block + remediation list + score.
2. **POLISH mode**: run at Stage 1; surface HIGH triggers at the top of the output; continue polish but flag.
3. Do **not** invent a desk-reject reason that is not on this list. If you spot a likely issue not covered, raise it as "Potential issue (not on standard checklist)" so the user can judge.

---

## Severity grading rubric for the AUDIT score

```
HIGH triggers fired:     each -10 to JBR-fit-and-format sub-score (out of 25)
MEDIUM triggers fired:   each -3
LOW triggers fired:      each -1
Floor at 0; do not go negative.
```
