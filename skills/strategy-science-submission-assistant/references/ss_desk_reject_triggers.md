---
file: ss_desk_reject_triggers.md
purpose: 30-second hard-check list for Strategy Science. Any HIGH trigger fires → flag immediately to the user. Used at Stage 1 of the polishing pipeline and as the AUDIT mode core.
last_verified: 2026-05-21
---

# Strategy Science Desk-Reject Triggers

## Contents

- A. Scope & Fit
- B. Format (mechanical)
- C. Disclosures (INFORMS post-2024)
- D. Argument Spine & Theoretical Movement (the SS-critical layer)
- E. Method ↔ Claim (cross-check with `ss_claim_evidence_matrix.md`)
- F. Originality & Overlap
- G. Special Issue Specific (if SI submission)
- H. SS-specific Theoretical Anchoring
- How to use this list
- Severity grading rubric for the AUDIT score


These are the hard, mechanical checks that catch the most common reasons SS editors return a manuscript without external review. Run them **first**, before any spine or theory analysis. Each trigger lists:

- **Test**: the specific binary check
- **Severity**: HIGH (likely desk-reject) / MEDIUM (likely sent back for revision before review) / LOW (cosmetic)
- **Fix**: the minimum action to clear the trigger

If **any** HIGH trigger fires, surface it at the top of the verdict block. Polish can still proceed, but the trigger must be resolved before submission.

> **SS is theory-forward.** Many SS desk-rejects come from manuscripts that would survive at SMJ/JBR — they have a phenomenon and a result, but no theoretical movement. The triggers below place extra weight on theoretical contribution clarity (D-section) compared to JBR's equivalent.

---

## A. Scope & Fit

| # | Test | Severity | Fix |
|---|---|---|---|
| A1 | Manuscript has no strategic outcome (decision, mechanism, architecture, foresight, capability, competitive advantage) — pure OB/HR/marketing/finance with bolted-on strategy framing | HIGH | Reframe with a primary strategic-management mechanism, OR redirect to a non-SS outlet |
| A2 | Contribution is "we test X in setting Y" or "geographic novelty" only, with no theoretical refinement | HIGH | Add a theoretical movement: mechanism specification, boundary refinement, integration, reconciliation, or new construct (see ss_introduction_and_contribution.md) |
| A3 | Empirical setting chosen for convenience, with no argument for why this setting reveals the strategic mechanism | HIGH | Add a setting-rationale paragraph in methods; tie to the phenomenon (Asghar et al. justify insider trading as a "fruit fly" setting for foresight; do the equivalent) |
| A4 | Practical implications are generic ("managers should pay attention to X") and disconnected from the empirical findings | MEDIUM | Rewrite implications as specific actions tied to the mechanism the study identified (Qu et al. 2026 §5.2 is a model) |
| A5 | Paper is "interesting data, no theory" — a description of a dataset with no theoretical claim | HIGH | Add a primary theoretical conversation and a contribution beyond description |
| A6 | The "theory" section is a generic literature review with no named primary theoretical lineage | HIGH | Name one primary lineage (Carnegie / behavioral / mental representations / ecosystems / TCE / etc.) and route through it; supporting theories must be clearly auxiliary |
| A7 | The paper contributes to a literature SS does not publish (e.g., pure marketing-research, pure HR-selection, pure finance-anomaly) | HIGH | Retarget to the field's home journal; do not force-fit |
| A8 | Pure formal model or simulation with no strategic-management implication | HIGH | Add an explicit strategic-management positioning (Clough 2026 ties game-theoretic coordination to ecosystem-architecture strategy) |

## B. Format (mechanical)

| # | Test | Severity | Fix |
|---|---|---|---|
| B1 | Manuscript abstract >200 words, or ScholarOne metadata abstract >250 words | HIGH | Trim to <=200 words for the manuscript; keep portal text <=250 words |
| B2 | Abstract is extremely short (<100 words) or missing theory/design/contribution elements | MEDIUM | Expand for substance; SS has no official minimum, but a thin abstract weakens editorial screening |
| B3 | Keywords <3 or >10 | HIGH | Adjust to the official 3-10 keyword range |
| B4 | Title page is not separate from blinded manuscript, OR blinded manuscript contains author identifiers | HIGH | Move author info to a separate title page; redact from MS |
| B5 | Self-citations phrased as "in our earlier work" or "our previous paper" | HIGH | Rewrite as third-person citation, OR remove until acceptance |
| B6 | Hypotheses not labeled in INFORMS bold-italic style (e.g., **Hypothesis 1.** *...*) | LOW | Reformat to match SS convention |
| B7 | Citations use comma between author and year (e.g., "Csaszar, 2018" instead of "Csaszar 2018") | MEDIUM | Apply INFORMS author-year convention throughout |
| B8 | References inconsistent or in non-INFORMS style (mixed APA/Harvard/Chicago/AMA) | MEDIUM | Apply INFORMS-style consistently (see ss_scope_and_format.md) |
| B9 | Acknowledgements include identifying information (grant numbers, institutional thanks, specific reviewer names) in blinded MS | HIGH | Remove from blinded MS; place on title page |
| B10 | Tables show t-statistics instead of standard errors in parentheses | LOW | Convert to SE per SS norm |
| B11 | Pre-registration link visible in blinded MS (e.g., contains author name in URL) | HIGH | Use anonymous OSF view link or omit until acceptance |

## C. Disclosures (INFORMS post-2024)

| # | Test | Severity | Fix |
|---|---|---|---|
| C1 | No AI-use disclosure paragraph | HIGH | Add a disclosure statement (see `ss_disclosures.md`); this skill counts as AI assistance |
| C2 | No author-contribution statement (when 2+ authors) | MEDIUM | Add a CRediT-style or "All authors contributed equally" statement (Asghar et al. used the equal-contribution model) |
| C3 | No Data Availability Statement | MEDIUM | Add a DAS even if "data not publicly available" — INFORMS expects this |
| C4 | No Conflict of Interest statement | MEDIUM | Add one, even if "the authors declare none" |
| C5 | Human-subjects work without IRB / ethics statement | HIGH | Add IRB approval reference (Kanis et al. cite TU Bergakademie Freiberg Project ID 2024-08), OR explain exemption |
| C6 | Funding source not disclosed | MEDIUM | Add funding statement |
| C7 | Pre-registration claim without OSF/aspredicted link | MEDIUM | Add the link OR remove the claim |

## D. Argument Spine & Theoretical Movement (the SS-critical layer)

| # | Test | Severity | Fix |
|---|---|---|---|
| D1 | Research question is not visible by page 2 of the introduction | HIGH | Move RQ to intro paragraph 2 or 3 |
| D2 | Introduction opens with a generic "literature gap" trope ("Few studies have examined…", "Little is known about…") instead of a strategic problem or theoretical tension | MEDIUM | Replace literature-gap opening with a strategic-tension opening (Asghar opens with "Strategic foresight is the ability of managers to predict..."; Kanis opens with "Because of rapid environmental changes...") |
| D3 | No primary theoretical lineage named in the introduction (Carnegie / mental representations / TCE / ecosystem / formal coordination / etc.) | HIGH | Name one primary lineage; supporting theories must be auxiliary |
| D4 | Hypotheses lack named mechanism (only direction) | HIGH | Add mechanism sentence to each hypothesis — SS does not accept "X is positively associated with Y" without a stated cognitive/structural/strategic reason |
| D5 | "Contribution" paragraph in intro lists three+ vague items ("we contribute to the literature on…") | HIGH at SS | Rewrite as one or two specific theoretical movements (extension / mechanism / boundary / integration / reconciliation / new construct). SS reviewers reject contribution lists that read like JBR boilerplate. |
| D6 | Hypotheses tested in different direction or grain from how they were stated | HIGH | Align hypothesis wording with the actual test |
| D7 | Findings paragraph in abstract differs from findings paragraph in discussion | HIGH | Harmonize |
| D8 | Pure-theory paper (no empirics) without a clear theoretical contribution table or framework summary | HIGH | Add a typology table or framework summary (Clough 2026 Table 6 and Figure 1 are the model) |
| D9 | The "theoretical contribution" is just "we add a moderator" or "we test in a new context" — no movement | HIGH | Either reframe to a genuine movement or retarget |
| D10 | Discussion does not engage the parent theory's known counter-arguments | MEDIUM | Add a paragraph in Discussion §5.1 or §5.2 engaging the most prominent counter-position |

## E. Method ↔ Claim (cross-check with `ss_claim_evidence_matrix.md`)

| # | Test | Severity | Fix |
|---|---|---|---|
| E1 | Cross-sectional design + causal verbs ("causes," "drives," "leads to," "produces") in abstract/intro/discussion | HIGH | Replace with association-based language (matrix row for cross-sectional design) |
| E2 | Mediation tested in cross-sectional data, claimed as causal mechanism | HIGH | Soften to "consistent with the proposed mechanism"; add limitation |
| E3 | Single-source archival or survey for both IV and DV without remedies | MEDIUM | Add procedural + statistical remedies, OR acknowledge in limitations |
| E4 | Experiment without manipulation check, attention check, or randomization-success report | HIGH | Add the checks (Kanis et al. 2026 reports a perceived-time-pressure manipulation check at p < 0.01 — this is the bar) |
| E5 | Qualitative study without theoretical case-selection logic | MEDIUM | Add case-selection rationale |
| E6 | Robustness section adds analyses unconnected to plausible reviewer concerns | LOW | Tie each robustness check to a specific threat |
| E7 | Pure-theory paper makes claims that require empirical evidence (e.g., "we show empirically...") | HIGH | Replace with "we propose / we argue / the framework predicts" |
| E8 | LLM-as-measurement (e.g., GPT-coded constructs) without inter-rater reliability against humans (Krippendorff α or Cohen's κ) | HIGH | Run the validation; if α < 0.80, redo the coding; report transparently per gpt_measurement_validation.md |
| E9 | Single LLM used for measurement without sensitivity to alternative LLMs | MEDIUM | Run a second LLM and report consistency where feasible (Kanis et al. report three LLMs with inter-LLM consistency r = 0.93 and human validation α = 0.89) |
| E10 | ML-as-prediction (e.g., random forest for predicted CAR) without an OLS or simpler baseline benchmark | MEDIUM | Add the baseline (Qu et al. 2026 Table 1 reports OLS, elastic net, RF, gradient-boosted tree side-by-side) |
| E11 | ML predictions used as a strategy construct without train-test split disclosure | HIGH | Disclose the split (Qu et al. use 80-20 with time-series cross-validation) |

## F. Originality & Overlap

| # | Test | Severity | Fix |
|---|---|---|---|
| F1 | Substantial text overlap (>30%) with a prior paper by same authors (working paper, conference, prior publication) | HIGH | Disclose to editor; rewrite the overlapping content; or withdraw |
| F2 | Same dataset used in a prior publication without distinct theoretical contribution here | HIGH | Either kill this manuscript, or distinguish the contribution sharply and disclose |
| F3 | "First paper to study X" claim without supporting search log or recent review | HIGH at SS | Soften to "we contribute to an emerging literature on X by…", OR provide search evidence. SS reviewers are deeply embedded in the relevant networks. |
| F4 | Salami-sliced from a larger study without independent theoretical core | HIGH | Restore the integrated study, OR reposition to a fully distinct contribution |

## G. Special Issue Specific (if SI submission)

| # | Test | Severity | Fix |
|---|---|---|---|
| G1 | Paper does not explicitly cite the SI call's stated themes | HIGH | Map RQ/theory/method/implications to the call's themes; cite the call in the cover letter |
| G2 | SI deadline already passed | HIGH | Check whether late submissions are accepted; if not, retarget to regular SS issue |
| G3 | Guest editor list not acknowledged in cover letter | LOW | Address cover letter to "Guest Editors of the [SI title]" |
| G4 | SI is on a topic the manuscript only tangentially engages | MEDIUM | Either substantively reframe to engage the SI's core problem, or submit to regular SS |

## H. SS-specific Theoretical Anchoring

| # | Test | Severity | Fix |
|---|---|---|---|
| H1 | Paper engages "mental representations" or "strategic foresight" without citing Csaszar 2018 or Csaszar & Laureiro-Martínez 2018 | HIGH | Anchor in the relevant exemplar (this is the foundational SS reference for representational/foresight work) |
| H2 | Paper engages "innovation ecosystems" or "platform architecture" without citing Adner & Kapoor 2010 or Jacobides, Cennamo & Gawer 2018 | HIGH | Anchor in the relevant exemplar |
| H3 | Paper engages "behavioral theory of the firm" without citing Cyert & March 1963 (or Gavetti, Greve, Levinthal & Ocasio 2012) | HIGH | Anchor in the relevant exemplar |
| H4 | Paper claims "Carnegie tradition" without engaging Simon 1947/1997 and at least one of Gavetti/Levinthal/Ocasio | MEDIUM | Add the proper Carnegie anchors |
| H5 | Paper engages "strategic human capital" without citing Castanias & Helfat 2001 or Helfat & Peteraf 2015 | HIGH | Anchor in the relevant exemplar |
| H6 | Paper engages "hybrid governance" without citing Williamson 1985, 1991 | HIGH | Anchor in the relevant exemplar |
| H7 | Paper engages "AI and strategic decision-making" without citing Csaszar et al. 2024a,b or Felin & Holweg 2024 | HIGH | Anchor in the recent SS-published exemplars on this topic |

---

## How to use this list

1. **AUDIT mode**: run all triggers; produce a verdict block + remediation list + score.
2. **POLISH mode**: run at Stage 1; surface HIGH triggers at the top of the output; continue polish but flag.
3. Do **not** invent a desk-reject reason that is not on this list. If you spot a likely issue not covered, raise it as "Potential issue (not on standard checklist)" so the user can judge.

### Run the bundled scripts for the mechanical triggers

Triggers B1, B3, and E1 are countable — do not eyeball them. Run the scripts and quote their output in the verdict:

- B1 (abstract length): `python3 scripts/check_abstract_word_count.py <abstract>`
- B3 (keyword count): `python3 scripts/check_keywords_count.py "<kw1; kw2; …>"`
- E1 (causal verbs in observational designs): `python3 scripts/scan_causal_verbs.py <manuscript>` — then confirm each hit against `ss_claim_evidence_matrix.md`; a causal verb is only a trigger when the design cannot support it.

---

## Severity grading rubric for the AUDIT score

```
HIGH triggers fired:     each -10 to SS-fit-and-format sub-score (out of 25)
MEDIUM triggers fired:   each -3
LOW triggers fired:      each -1
Floor at 0; do not go negative.

ALSO: For D-section (theoretical movement) HIGH triggers, deduct -10 from the
"Theoretical contribution & movement" sub-score in addition to the format
sub-score. SS desk-rejects most often on D-issues.
```
