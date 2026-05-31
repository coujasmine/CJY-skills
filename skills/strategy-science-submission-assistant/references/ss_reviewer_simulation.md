---
file: ss_reviewer_simulation.md
purpose: Simulates Strategy Science Senior Editor + reviewer process for pre-submission stress-testing. Used in REVIEW mode.
last_verified: 2026-05-31
---

# Strategy Science Reviewer Simulation

## Contents

- The SS reviewing system
- The SS-specific review board
- The three reviewer archetypes
- Senior Editor archetype
- Review contract and editorial synthesis
- Running the simulation
- Format of each reviewer report
- Reviewer X: [Theme]
- What NOT to do
- Calibration against published exemplars
- Common SS reviewer patterns by submission stage


This file specifies how to simulate an SS peer-review process. Use in REVIEW mode to surface the most likely reviewer concerns before submission.

> **Hard rule:** Do not invent specific reviewer names, decision quotes, or Senior Editor remarks. Simulate the *type* of reviewer concern based on patterns observed in SS published papers and standard INFORMS reviewing practice.

---

## The SS reviewing system

- **Editor-in-Chief**: rotates; recent SI editors include Felipe Csaszar.
- **Senior Editor**: Strategy Science's official guide says Senior Editors have autonomy to accept, reject, or request revision and incorporate reviewer evaluations into their own judgment.
- **Reviewers**: expert reviewers, including Editorial Review Board members and field specialists.
- **Decision categories**: Desk Reject / Reject / Major Revision / Minor Revision / Accept.
- **Double-anonymous**: reviewers do not know authors; authors do not know reviewers.
- **Review timeline**: do not report exact expected timing unless the user supplies a verified source. If a revision is invited, the official guide asks for resubmission within three months and no later than one year.

---

## The SS-specific review board

REVIEW mode now uses a calibrated review board rather than only three generic
reviewer voices:

1. **SS EIC / Senior Editor screen**
   - Desk-reject risk, send-out risk, and fit with the journal's theory-forward
     strategy domain.

2. **Theory reviewer**
   - Theoretical lineage, theoretical movement, boundary conditions,
     counter-arguments, and novelty calibration.

3. **Methods reviewer**
   - Identification, construct validity, measurement validity, robustness,
     LLM-as-measurement reporting, and claim-evidence calibration.

4. **Style and positioning reviewer**
   - Abstract, introduction, contribution paragraph, SS house style, AI-style
     markers, and accessibility to a broad strategy audience.

5. **Devil's advocate**
   - The strongest desk-reject or reject-after-review path. This voice should
     attack the largest weakness, not accumulate minor copyedits.

6. **Editorial synthesizer**
   - Aggregates the above. It does not introduce new objections; it maps the
     case to a weighted SS score and next revision move.

---

## Review contract and editorial synthesis

Before reading paper-visible content, declare the review contract from
`ss_review_contract_protocol.md`:

- SS fit: 20 points
- Theoretical movement: 25 points
- Method-claim alignment: 25 points
- Writing and positioning: 15 points
- Citation integrity: 15 points

Fatal flaws must be declared before the review is applied. New criteria can
appear only as `Emergent issue`.

Decision mapping:

- 85-100: submission-ready after light polish
- 75-84: promising but needs one focused revision
- 60-74: major pre-submission revision needed
- below 60: not ready for Strategy Science

---

## The three reviewer archetypes

Based on patterns from published SS R&R correspondence and common reviewing structures:

### Reviewer 1: Theory and Contribution

This reviewer is typically a senior strategy scholar embedded in the primary theoretical lineage. They evaluate:

- **Theoretical positioning**: Is the paper anchored in a recognizable SS lineage? Does it cite the right anchors (Csaszar / Gavetti / Levinthal / Helfat / Adner / Williamson / etc.)?
- **Theoretical movement**: Is there a specific movement (mechanism / boundary / integration / new construct)? Or is the contribution a list of vague claims?
- **Engagement with prior work**: Does the paper engage substantively with the closest prior papers, not just cite them in passing?
- **Counter-arguments**: Are alternative theoretical accounts addressed?
- **Originality vs. existing literature**: Is the contribution genuinely distinct from prior work?

Typical R1 concerns:
- "The contribution is not sharp enough — what specifically is new beyond [closest prior paper]?"
- "The paper engages [lineage X] but the closest related work is [lineage Y]; the positioning needs clarification."
- "The hypotheses are theoretically reasonable but the mechanism is under-specified."
- "The paper overclaims novelty given [existing literature]."

### Reviewer 2: Method and Evidence

This reviewer is typically a methodological specialist (econometrician, experimentalist, formal modeler, depending on the paper). They evaluate:

- **Identification strategy**: Is the causal logic supported by the design?
- **Construct validity**: Do the measures match the constructs?
- **Measurement validity**: Are LLM-coded or ML-derived measures validated against humans/ground truth?
- **Robustness**: Do robustness checks address the right threats?
- **Reporting transparency**: Are the right things reported (effect sizes, confidence intervals, sensitivity, code/data availability)?
- **Sample selection and external validity**

Typical R2 concerns:
- "Causal language overruns the design (cross-sectional + FE does not identify causality)."
- "The LLM-coded measure lacks inter-rater reliability against human coders; what is Krippendorff α?"
- "Why is the setting [the focal context]? The setting-mechanism alignment is not justified."
- "Manipulation check missing / failed / not reported."
- "Alternative explanations [X, Y, Z] should be ruled out before this finding can support the conclusion."
- "The exclusion rate of 36.61% in the time-constraints LLM condition raises selection concerns" (echoing a likely Kanis 2026 reviewer point).

### Reviewer 3: SS Fit, Theoretical Movement, and Implications

This reviewer is typically a strategy scholar evaluating fit and broader contribution. They evaluate:

- **SS fit**: Is the paper a fit for SS, or would it be better at SMJ, OS, AMJ?
- **Theoretical movement**: Does the contribution advance the conversation in a way SS readers value?
- **Practical implications**: Are managerial implications tied to the mechanism?
- **Writing and accessibility**: Is the paper readable to the broad SS audience (including formal modelers, cognitive scholars, and macro-strategy readers)?
- **AI-generation markers**: Increasingly, R3-style reviewers flag papers that read as LLM-written.

Typical R3 concerns:
- "This paper feels like a fit for SMJ rather than SS — the contribution is empirical extension, not theoretical movement."
- "The discussion engages the findings but does not explicitly engage the primary lineage's open questions."
- "The managerial implications read as boilerplate; tie to mechanism."
- "The prose has several AI-style markers (e.g., 'It is important to note that...', triadic lists, comprehensive coverage) that should be revised."
- "The paper would benefit from a sharper framing of the theoretical contribution in the abstract and conclusion."

---

## Senior Editor archetype

The Senior Editor synthesizes reviewer input and adds editor-level judgment:

- **Strategic fit with the journal**: Does this advance SS's intellectual program?
- **Theoretical contribution worth the publication slot**: Is this a "good paper" or a "good SS paper"?
- **R&R feasibility**: Can the issues raised by reviewers be addressed in a revision, or are they fundamental?

Typical Senior Editor recommendations:
- "Desk reject" — fit or contribution issues that cannot be fixed in revision
- "Reject after review" — multiple reviewers identify fundamental issues; revision unlikely to succeed
- "Major revision" — meaningful issues but a clear path to resolution
- "Minor revision" — clean paper with specific cleanup tasks
- "Conditional accept" — rare; clean paper with only formatting/disclosure issues

---

## Running the simulation

In REVIEW mode, produce the output specified in SKILL.md. Always run the
three-phase sequence:

1. **Review contract**: declare weights, fatal flaws, and evidence needed before
   paper-visible assessment.
2. **Paper-visible review**: apply Senior Editor + reviewer reports. If a criterion emerges
   only after reading, label it `Emergent issue`.
3. **Editorial synthesis**: aggregate, score, and prioritize. Do not introduce
   new objections here.

For each review level:

### QUICK_REVIEW (title + abstract + RQ only)

- Senior Editor assessment: 3-4 sentences on SS fit and likely desk-screen outcome
- R1: 2-3 concerns on theoretical positioning visible from the abstract
- R2: 2-3 concerns on method/design visible from the abstract (e.g., "the abstract claims causality but mentions only correlation")
- R3: 2-3 concerns on fit and contribution sharpness
- Pre-submission priorities: top 3 fixes

### STANDARD_REVIEW (+ intro/theory/method excerpt)

- Senior Editor assessment: 5-7 sentences with specific desk-reject triggers cross-referenced
- R1: 5-7 concerns from theory section, including missing anchor citations
- R2: 5-7 concerns from method section, including identification and measurement
- R3: 4-6 concerns from fit and contribution
- Pre-submission priorities: top 5 fixes

### FULL_REVIEW (complete manuscript)

- Senior Editor assessment: full memo (10-15 sentences) including recommended decision
- R1: full review (10-15 concerns; major + minor + required revisions)
- R2: full review (10-15 concerns; method + identification + measurement + robustness)
- R3: full review (8-12 concerns; fit + contribution + writing + AI-markers)
- LLM-measurement scorecard if applicable
- Pre-submission priorities: tiered (must fix / strongly recommended / optional polish)

---

## Format of each reviewer report

```
## Reviewer X: [Theme]

### Summary of the paper [optional, 2-3 sentences]
The authors examine [paraphrased RQ] using [paraphrased design] and find [paraphrased findings].

### Major concerns
1. [Concern 1 — specific to the paper, anchored in the SS norm being violated]
   - Recommended action: [what the authors should do]
   - Evidence: [page/section reference if FULL_REVIEW]

2. [Concern 2 ...]

### Minor concerns
1. [Minor point]
2. [Minor point]

### Required revisions for resubmission
- [Required revision 1, with priority]
- [Required revision 2, with priority]
```

---

## What NOT to do

1. **Do not invent reviewer names or Senior Editor names.** Use "Reviewer 1", "Reviewer 2", "Reviewer 3", "Senior Editor".
2. **Do not invent quotes from real reviewers.** The simulation gives the *type* of concern, not actual paste from any specific review.
3. **Do not predict acceptance.** Predict "desk reject risk" / "major revision risk" / "minor revision risk" — never claim a paper will be accepted.
4. **Do not soft-pedal serious issues.** If the lineage is mis-fit or the contribution is vague, R3 will say so; the simulation should say so.
5. **Do not invent journal-specific information not in this skill's references.** E.g., do not invent acceptance rates, editor names, or special-issue deadlines.

---

## Calibration against published exemplars

The four exemplar papers show what a successful SS submission looks like after reviewer engagement:

- **Kanis et al. 2026** explicitly thanks Felipe Csaszar (editor) for "highly constructive comments." The paper reports null effects on the main DV — a sign that reviewers pushed for honest reporting, not headline-chasing. The "Additional analyses indicate" pattern likely emerged from reviewer requests to explore mechanisms.
- **Qu et al. 2026** thanks specific colleagues for insights. The paper has a Hypothesis 1 + Hypothesis 2 structure (relatively simple), suggesting the original submission may have been more complex and was trimmed during revision.
- **Asghar et al.** uses a "fruit fly" justification for the empirical setting — a phrase Asghar attributes to the foresight literature but also a common reviewer-anticipating move.
- **Clough 2026** is single-authored pure theory; the reviewer process likely involved demands for typology clarity (the trilemma and 2×2 matrix in Table 6 and Figure 1 may be artifacts of revision).

These exemplars are calibration anchors. A simulated review should produce concerns of comparable specificity and rigor.

---

## Common SS reviewer patterns by submission stage

### First submission to SS

- High likelihood of major revision if the paper is fundamentally a fit
- Most common concerns: contribution sharpness, identification, measurement validity, LLM-style writing
- Desk-reject risk should be described qualitatively from fit, theory, evidence, and format problems; do not state numeric likelihoods unless the user supplies a verified source

### R&R (1st round) to SS

- Reviewers will check whether each point was addressed substantively
- "Cosmetic" responses (changing wording without addressing the underlying concern) trigger second-round major revision or reject
- New analyses typically requested in 1st R&R; new theory typically requested in 2nd R&R

### R&R (2nd round) to SS

- At this stage, reviewers expect the paper to be near-final
- Major new concerns at 2nd round usually indicate the reviewer or Senior Editor has lost confidence
- Minor revision is the typical positive outcome

### Special issue submission

- Thematic fit becomes a separate gate before standard concerns
- SI reviewers often include guest editors and SI-specific experts
- Timelines are accelerated; turnaround is faster
