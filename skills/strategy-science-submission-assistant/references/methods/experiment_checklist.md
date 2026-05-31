---
file: experiment_checklist.md
purpose: >
  Deep audit checklist for experimental methods at Strategy Science.
  Calibrated against Kanis, Mann & Stumpf-Wollersheim (2026): 2×2 between-subjects
  online experiment on Prolific, with LLM treatment and time-constraint
  manipulation, N=348, pre-registered. Used when method tier is experiment.
last_verified: 2026-05-21
---

# Experiment Method Audit — Strategy Science

## Contents

- 1. Experimental design
- 2. Pre-registration
- 3. Sample
- 4. Procedure
- 5. Manipulation checks
- 6. Exclusion criteria
- 7. Measures
- 8. Analysis
- 9. LLM-as-measurement (when LLMs are used to code responses)
- 10. SS-specific concerns
- 11. IRB and ethics
- Common SS Reviewer 2 concerns (experiment)
- Calibration anchor


This file is the deep-dive checklist for experimental submissions to Strategy Science. Apply during AUDIT, REVIEW (Reviewer 2), and POLISH Stage 4.

---

## 1. Experimental design

### Design type

- [ ] Design clearly specified: between-subjects / within-subjects / mixed
- [ ] Factorial structure named (Kanis: 2 [time constraints] × 2 [LLM use])
- [ ] All conditions enumerated with cell sizes
- [ ] Counterbalancing (for within-subjects)
- [ ] Order/sequence effects addressed (Kanis: randomized order of two startup videos)

### Random assignment

- [ ] Random assignment to conditions described
- [ ] Randomization mechanism (e.g., platform-level randomization, randomization seed)
- [ ] Balance across conditions on key covariates checked and reported

### Manipulation

- [ ] Manipulation operationalized in detail (e.g., "we set the time available for each evaluation to three minutes")
- [ ] Manipulation justified theoretically and empirically (Kanis cites Benson & Beach 1996; Ordóñez & Benson 1997)
- [ ] Pilot/pretest informing the manipulation parameters (Kanis: pretest with N=35 to set time limit)
- [ ] Manipulation salience (visible cues — Kanis used red countdown timers)

## 2. Pre-registration

- [ ] Pre-registered? At which platform (aspredicted.org, OSF)?
- [ ] Pre-registration URL provided (anonymized for review)
- [ ] Hypotheses pre-specified
- [ ] Design pre-specified
- [ ] Sample size pre-specified (with G*Power calculation)
- [ ] Exclusion criteria pre-specified
- [ ] Analysis plan pre-specified
- [ ] Deviations from pre-registration disclosed transparently

## 3. Sample

### Sample size

- [ ] G*Power calculation reported (Kanis: medium effect size d=0.50, power=0.80, α=0.05 → N=256; recruited 410 to allow for smaller effects)
- [ ] Sample size adequate for the design
- [ ] Sample size adjustments (e.g., over-recruiting to allow for exclusions) explained

### Recruitment platform

- [ ] Platform named (Prolific, MTurk, Lab, Field)
- [ ] Recruitment criteria (Kanis: 98% approval rate, ≥200 prior tasks, English fluency, residing in AU/CA/IE/NZ/UK/US, prior business-strategy decision-making position)
- [ ] Compensation rate disclosed (Kanis: £3.50/$4.66)
- [ ] Data collection date / duration

### Participant characteristics

- [ ] Demographic summary (Kanis: age 42.06, 52.59% male, 47.13% female, 75.86% college degree)
- [ ] Domain expertise (Kanis: 13.27 years average professional experience; 31.32% had taken business-strategy course)
- [ ] Sample relative to target population

## 4. Procedure

### Participant flow

- [ ] Each step of participant experience described in order
- [ ] Informed consent procedure
- [ ] Audio/video checks if relevant
- [ ] Manipulation introduced at the right moment
- [ ] Task completion procedure clear

### Task description

- [ ] Task validly operationalizes the target construct
- [ ] Task replicates / adapts an established task (Kanis adapts Csaszar & Laureiro-Martínez 2018 + Heshmati & Csaszar 2023)
- [ ] Task adaptations explained and justified (Kanis: 5 specific adaptations vs. original)
- [ ] Task duration appropriate for the manipulation

### Stimuli

- [ ] Stimuli described in detail (Kanis: two startup pitch videos from Kickstarter)
- [ ] Selection of stimuli justified (5 criteria for stimulus pair: same Kickstarter category, same period, similar length, different outcomes, not in LLM training data, not trivially identifiable)
- [ ] Stimuli pre-tested (Kanis: pretest with N=165 showing 63.03% correct foresight — verifies task validity)

## 5. Manipulation checks

### Time-constraint manipulation

- [ ] Manipulation-check measure validated (Kanis adapts Denovan & Dagnall 2019 chronic time pressure inventory; α = 0.97)
- [ ] Manipulation-check results reported (Kanis: M=2.05 vs. M=4.26 in no-LLM condition; t-test p<0.01)
- [ ] Both treated and untreated cells checked

### LLM-use manipulation

- [ ] Were participants in the LLM condition required to use the LLM? (Kanis: excluded 13 participants who didn't use)
- [ ] Were participants in the no-LLM condition prevented from external AI? (Kanis: instruction not to use external AI; sample reliability check)
- [ ] LLM-use intensity measured (Kanis: average M=3.83 prompts to the LLM)

### Attention / quality checks

- [ ] Attention check items (Kanis: audio check, task-comprehension check)
- [ ] Pass rates reported

## 6. Exclusion criteria

- [ ] Pre-specified before data collection
- [ ] Exclusion rates reported per criterion (Kanis: 15.21% total excluded)
  - 13 did not use LLM (in LLM condition)
  - 40 failed to accomplish task
  - 9 did not watch startup videos
  - 1 failed to decide
  - 2 had prior knowledge
  - 5 reported technical issues
  - 1 used external AI
- [ ] Exclusion rates compared across conditions (Kanis flags higher exclusion in time-constraint LLM cell at 36.61% vs. <8% elsewhere → robustness check)
- [ ] Robustness analysis with included participants

## 7. Measures

### Dependent variables

- [ ] DV operationalization (Kanis: strategic foresight = binary [correct/incorrect] + continuous [likelihood difference])
- [ ] Multiple-item scales: items listed, reliability reported (Cronbach α)
- [ ] DV measurement procedure explicit
- [ ] Established scales cited (Kanis: Denovan & Dagnall 2019 for time pressure; Dennis & Vander Wal 2010 for cognitive flexibility; Van Dyne & Pierce 2004 for psychological ownership; Karr-Wisniewski & Lu 2010 for information overload)

### Independent variables

- [ ] Manipulation operationalized as a binary or categorical variable
- [ ] Covariates measured

### Mediating / mechanism variables

- [ ] Pre-registered as mechanisms or labeled as exploratory
- [ ] Validated scales used

## 8. Analysis

### Hypothesis tests

- [ ] One test per hypothesis
- [ ] Test type stated (t-test, ANOVA, regression)
- [ ] Effect size reported (Cohen's d, η², or comparable)
- [ ] Confidence intervals reported where possible
- [ ] Multiple-comparisons correction if applicable

### Reporting null results

- [ ] Nulls reported honestly (Kanis: H1d about time constraints reducing foresight is NOT supported; reported transparently)
- [ ] Equivalence testing if argued (when claiming "no effect")
- [ ] Confidence intervals around null

### Additional / exploratory analyses

- [ ] Labeled as exploratory (not pre-registered)
- [ ] Theoretical motivation given
- [ ] Multiple-testing concerns addressed

## 9. LLM-as-measurement (when LLMs are used to code responses)

See `references/gpt_measurement_validation.md` for full 8-dimension scorecard. Kanis uses three LLMs to classify pros/cons into 10 strategic categories with Krippendorff's α = 0.89 against humans.

## 10. SS-specific concerns

### Online experiment vs. lab vs. field

- [ ] Choice justified (Kanis: online experiment for ecological validity in business-decision context)
- [ ] External validity concerns acknowledged
- [ ] Online-specific concerns addressed (e.g., environmental distractions, attention)

### Task relevance to strategy

- [ ] Task involves a strategic decision (not pure cognitive task)
- [ ] Task replicates a setting relevant to managers (Kickstarter startup evaluation is a real investor decision)
- [ ] Findings have implications for strategic decision-making

### Sample relevance

- [ ] Participants have decision-making experience relevant to the task (Kanis: required prior business-strategy decision-making position)
- [ ] Sample limitations acknowledged (non-expert, online, possibly culturally homogeneous)

### Reproducibility

- [ ] Pre-registration with materials
- [ ] Materials (instructions, stimuli, measures) shared
- [ ] Code (analysis scripts) shared

## 11. IRB and ethics

- [ ] IRB approval cited with institution + project ID (Kanis: TU Bergakademie Freiberg Project ID 2024-08)
- [ ] Informed consent procedure described
- [ ] Compensation rate appropriate for time (Prolific minimum: £6/hour as of 2024)
- [ ] Debrief procedure if deception used

---

## Common SS Reviewer 2 concerns (experiment)

1. **"Why this task?"** — task-construct validity must be defended.
2. **"What is the manipulation check?"** — if missing or weak, the manipulation is suspect.
3. **"Why this sample?"** — Prolific samples are accepted at SS (Kanis 2026) but expertise and demographic concerns must be addressed.
4. **"Effect sizes are small / inconsistent with prior work"** — interpret in context; defend or qualify.
5. **"Pre-registration says X but the paper does Y"** — deviations must be disclosed transparently.
6. **"The LLM classification is unreliable"** — multi-LLM and human-validated coding needed.
7. **"The null finding is just under-powered"** — power analysis or sensitivity analysis required.
8. **"External validity to real strategic decisions is unclear"** — discuss; replicate in field if possible.

---

## Calibration anchor

**Kanis, Mann & Stumpf-Wollersheim (2026)**: 2×2 between-subjects experiment on Prolific (N=348 after exclusions), time-constraint × LLM-use manipulation, evaluating two startup pitch videos. Pre-registered at aspredicted.org. Manipulation checks at p<0.01. Three LLMs classified pros/cons into 10 strategic categories with Krippendorff α = 0.89 against humans. Reports nulls on main DV (strategic foresight) honestly while documenting representational shifts. IRB approval from TU Bergakademie Freiberg. Full materials and prompts in Appendices A, B, C.
