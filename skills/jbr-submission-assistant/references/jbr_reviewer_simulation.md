---
file: jbr_reviewer_simulation.md
purpose: >
  REVIEW-mode protocol for simulating a JBR editorial screen and three peer
  reviewers before submission. Use to identify likely desk-reject triggers,
  theory/contribution attacks, method-evidence attacks, and outlet-fit risks.
last_verified: 2026-05-18
---

# JBR Reviewer Simulation

Use this file only in **REVIEW** mode. The goal is not to rewrite the manuscript. The goal is to simulate how a JBR Associate Editor and three reviewers would read the current draft, given the evidence supplied by the user.

## Review Levels

Choose the highest feasible level from available material. Always report the level and confidence.

| Level | Minimum input | What can be judged | What cannot be judged |
|---|---|---|---|
| `QUICK_REVIEW` | Title, abstract, keywords, or research question | JBR fit, opening problem, likely theory/contribution risk, obvious desk-reject risk | Method credibility, results-evidence fit, full contribution execution |
| `STANDARD_REVIEW` | Abstract + introduction + theory or methods excerpt | Argument spine, theory conversation, contribution promise, method-claim plausibility | Full robustness, full results narrative, discussion/implications quality |
| `FULL_REVIEW` | Complete manuscript or all main sections | AE decision risk, reviewer-specific objections, method-evidence fit, section-level revision priorities | Only items absent from the draft or unavailable data files |

If the user provides partial material, do not fabricate missing sections. Name the missing inputs and calibrate the confidence downward.

## Editorial Screen

Simulate the Associate Editor first. Decide whether the paper is likely to be desk-rejected, sent out for review, or sent out with major revision risk.

Check:

- **Outlet fit**: Does the manuscript address a business, managerial, organizational, market, innovation, consumer, or societal problem in JBR's scope?
- **JBR track fit**: Use `jbr_track_positioning.md` to name the most plausible disciplinary track and the competing track, if any.
- **Theory spine**: Is there one primary theoretical conversation, or only a list of related literatures?
- **Contribution specificity**: Does the draft name a theoretical movement: mechanism, boundary condition, integration, reconciliation, clarification, or contextualization?
- **Evidence sufficiency**: Does the method tier support the claim strength?
- **Submission hygiene**: Any obvious formatting, disclosure, anonymity, abstract, or keyword problem from `jbr_scope_and_format.md` or `jbr_disclosures_2024.md`.

Do not recommend "accept." Pre-submission simulation should estimate desk-screen and review risks, not final publication outcome.

## Reviewer Roles

### Reviewer 1: Theory and Contribution

This reviewer asks whether the manuscript changes understanding in a named literature.

Likely major concerns:

- The manuscript opens from "few studies" rather than a business phenomenon or theoretical tension.
- The primary theory is named late or used decoratively.
- Constructs are introduced through measures before definitions.
- Hypotheses state relationships without mechanism.
- Moderators or mediators are generic rather than theoretically necessary.
- Contributions are phrased as "we enrich/extend" without specifying the movement in understanding.
- The discussion repeats results rather than translating findings into theoretical implications.

Required revision language should identify the exact location: abstract, intro paragraph, theory subsection, hypothesis paragraph, or discussion contribution paragraph.

### Reviewer 2: Method and Evidence

This reviewer asks whether the design can support the claims.

Likely major concerns:

- Construct-to-measure mismatch.
- Unclear sample construction, exclusion criteria, or time window.
- Weak setting rationale: the empirical context is convenient rather than theoretically informative.
- Causal language without a defended identification strategy.
- Missing fixed effects, time ordering, robustness, or alternative measurement logic for archival/panel designs.
- Survey designs with weak validity or common-method-bias treatment.
- Mechanism claims without direct mechanism evidence.
- Robustness checks that add tables but do not answer named threats.

For archival panel manuscripts, load `references/methods/archival_panel_checklist.md` before writing Reviewer 2.

### Reviewer 3: JBR Fit, Writing, and Implications

This reviewer asks whether the paper reads like a JBR article rather than a generic management manuscript.

Likely major concerns:

- The business relevance is implicit or appears only in the discussion.
- The paper is over-technical, under-theorized, or framed as a methods paper.
- The introduction lacks a recognizable JBR shape: phenomenon, theory, question, design, contributions.
- Results are reported as significance tables rather than evidence for a mechanism.
- Practical implications are generic and not tied to the findings.
- Limitations are boilerplate rather than design-bounded.

## Output Rules

- Report **major concerns** only when they would plausibly affect review outcome.
- Keep **minor concerns** limited to issues that are easy to fix and do not change the argument.
- Do not invent reviewer identities, journal decisions, scores, or comments.
- Do not fabricate missing results, robustness tests, or citations.
- Separate **must-fix before submission** from **recommended strengthening**.
- Include an AI-use disclosure reminder because REVIEW mode uses AI assistance to evaluate manuscript preparation.

## Recommended Decision Calibration

Use these labels:

- **Desk reject likely**: JBR scope is weak, no clear theory conversation, or claim-evidence mismatch is severe.
- **Send out with high major-revision risk**: JBR fit is plausible but theory contribution or method credibility is underdeveloped.
- **Send out with moderate major-revision risk**: JBR fit is clear, but one reviewer role has a serious concern.
- **Send out with manageable revision risk**: JBR fit, theory contribution, and method-claim alignment are broadly coherent; remaining issues are presentation, calibration, or missing robustness explanation.

Never present the simulation as fact. Use "likely," "would probably," and "may" where uncertainty remains.
