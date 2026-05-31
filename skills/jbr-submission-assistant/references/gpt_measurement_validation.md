---
file: gpt_measurement_validation.md
purpose: >
  Validation reference for manuscripts that use a generative LLM (GPT, Claude,
  Gemini, etc.) as a measurement instrument to construct a focal variable from
  text. Used by REVIEW mode (Reviewer 2 method audit) when method tier is
  archival/text/AI, and as the reference base for the jbr-gpt-measurement-auditor
  companion subagent.
last_verified: 2026-05-18
---

# GPT-as-Measurement Validation Reference

When the manuscript constructs a focal variable by sending text to a generative LLM, the measurement step itself becomes a target of methods review. Reviewers will not accept "we used GPT to classify the postings" without seeing the validation evidence. This reference defines the evidence base that JBR Reviewer 2 (Method and Evidence) will require.

---

## 1. Trigger conditions

Apply this reference when **at least one** focal variable is constructed by:

- LLM classification (binary, multi-class, ordinal) of text passages.
- LLM scoring (continuous or graded) of text on a construct dimension.
- LLM extraction of construct mentions from text (e.g., counting "discovery-oriented AI" sentences).
- LLM-assisted human coding where the LLM produces the first-pass label.

Do **not** apply when the measure is a traditional dictionary count, a fully supervised classifier trained on hand-labeled data, or pure LLM-based translation/summarization.

---

## 2. Eight evidence dimensions

The author must show evidence on each of the following. Missing evidence on any dimension is a legitimate Reviewer 2 concern.

### Dimension 1 — Construct definition before measurement

Required:
- Construct is defined theoretically **before** the measurement procedure.
- Construct is distinguished from neighboring concepts the LLM might conflate it with.
- The unit of analysis (sentence / paragraph / document / posting) is explicit.

Common failure: the construct is defined by the prompt rather than by the theory. A prompt that says "score how much this firm uses AI" is not a construct definition — it is a measurement instruction. The theory section must define "AI use" first.

### Dimension 2 — Prompt engineering hygiene

Required:
- The **exact prompt text** is reported (body, appendix, or supplementary).
- The prompt was **frozen** before validation/main analysis. If the prompt was iterated, the manuscript reports when iteration stopped.
- The prompt's task framing aligns with the construct definition (a prompt asking for "mentions" cannot validly measure "capability").
- **Model name and version** are reported (e.g., gpt-4-0125-preview, not "GPT-4").
- **Temperature, top-p, and other decoding parameters** are reported.
- **API access date** is reported (models update; same name ≠ same model).

### Dimension 3 — Development / validation set separation

Required:
- A **development set** for prompt iteration is separate from a **validation set** used to estimate performance.
- A **holdout set** unseen during iteration is used for the final performance estimate.
- The validation/holdout set is drawn from the same population as the main analysis sample.
- Validation set size is reported.

Reasonable floors:
- Binary classification with ~50% prevalence: at least 200–300 cases for stable F1.
- Imbalanced binary classification: enough positive cases for the rarer class (typical floor: 50 positives).
- Multi-class: at least 50 cases per class.
- Continuous/graded: at least 100–200 cases with adequate variance.

### Dimension 4 — Human benchmark and reliability

Required:
- A **human-coded subset** of the validation set.
- A **coding protocol** that operationalizes the construct for human coders.
- **Inter-coder reliability** on a double-coded subset (Cohen's κ, Krippendorff's α, or percentage agreement with chance correction).
- **LLM-vs-human agreement** on the full validation set.

Reporting:
- Binary: precision, recall, F1, confusion matrix counts, prevalence of positive class.
- Multi-class: per-class precision/recall, macro-F1, prevalence per class.
- Graded: ICC, Pearson/Spearman correlation, mean absolute error.

A single F1 number is **never** sufficient — F1 = 0.7 means very different things at 5% vs 50% positive-class prevalence.

### Dimension 5 — Convergent and discriminant validity

Required:
- At least one **convergent measure** the LLM-derived variable correlates with (a dictionary baseline, a supervised classifier, an external indicator, a survey-based measure).
- At least one **discriminant test** showing the LLM-derived variable diverges from a related but distinct construct.
- **Face-validity examples** drawn from the actual data (high-scoring and low-scoring exemplars).

For the specific case of measuring "AI capability" from text:
- Convergent: correlation with realized AI patents, AI-related capital expenditure, AI-related hiring counts from external sources.
- Discriminant: divergence from general digitalization, automation, or IT capability.

### Dimension 6 — Sensitivity of the measurement

Required (at least three of the following):
- **Prompt rewording**: a semantically equivalent prompt gives correlated scores (typical threshold: r > 0.85).
- **Model swap**: a different model family produces correlated scores.
- **Model version**: an older or newer version of the same family produces correlated scores.
- **Window size**: sentence vs paragraph vs document scoring gives consistent rankings.
- **Repeat-call stability**: if temperature > 0, scores are averaged across multiple calls (and the SD across calls is reported).

If sensitivity is poor on any axis, the measurement is **fragile** — the manuscript must either harden the measurement or restrict the claims accordingly.

### Dimension 7 — False-positive review

Required:
- A **sample of high-scoring observations** is manually reviewed.
- **Known false-positive patterns** are discussed (e.g., AI scoring high because the text discusses agricultural irrigation, or because "AI" appears in a boilerplate disclaimer).
- **Boundary cases** near the decision threshold are described.

For aggregate measures (e.g., share of postings that mention AI), the floor-level item-level error rate compounds at the firm-year level. A 5% per-item false-positive rate may yield substantial firm-year mismeasurement.

### Dimension 8 — Reporting and disclosure

Required:
- **AI use disclosure** per Elsevier 2024 policy, with model name, version, dates, and use case (measurement, not just writing assistance).
- **Prompt text** available for replication.
- **Validation data and code** available, or non-availability justified.
- **Construct contamination risk** acknowledged in limitations.
- **Claim language** calibrated to the measurement quality.

---

## 3. Special cases

### 3.1 LLM-as-measurement for managerial attention or capability

When the LLM scores corporate text (MD&A, earnings calls, annual reports, job postings, patent abstracts) for an organizational construct, add four checks:

1. **Construct-to-text mapping.** Does the text actually contain the construct, or is the LLM forced to infer something not in the text? Job postings contain *stated demand* for AI skills, not *realized AI capability*. The manuscript must defend the proxy.
2. **Source-firm selection.** Firms producing more text (more postings, longer MD&As) are more likely to be classified as having the construct. Is this bias addressed?
3. **Time anchoring.** Does the text reflect the construct at the time the construct is theorized to operate, or at a lag that breaks the causal chain?
4. **Adversarial framing.** Do firms have an incentive to write text that scores higher (AI-washing, ESG-washing, capability-washing)? Is this discussed?

### 3.2 Discovery-oriented vs general AI capability

For manuscripts distinguishing *discovery-oriented* AI capability from general AI adoption, the discriminant validity check is non-optional:

- The LLM must score *discovery-oriented* AI text differently from *automation-oriented* or *efficiency-oriented* AI text.
- Without this discrimination, the measure collapses into general AI adoption and the theoretical contribution evaporates.

Audit must verify the prompt definition draws a sharp distinction, the validation set contains examples of both types, and the LLM-human agreement on the **distinction** (not just on positive identification) is reported.

---

## 4. Claim calibration for LLM-derived measures

Map the measurement quality to claim language. Reviewer 2 will flag mismatches.

| Validation quality | Allowed claim verbs |
|---|---|
| F1 ≥ 0.85, ICC ≥ 0.85, multiple sensitivity passes | "measures," "captures," "identifies" |
| F1 0.70–0.85, ICC 0.70–0.85, partial sensitivity | "proxies for," "is an indicator of," "approximates" |
| F1 0.55–0.70, ICC 0.55–0.70 | "is correlated with," "suggests the presence of" |
| F1 < 0.55 or unvalidated | Measurement is not credible as a focal variable. Recommend supervised classifier, hand coding, or a different construct. |

Hedging in the *abstract* and *introduction* must match the measurement quality — overclaim there triggers rejection at the screen stage.

---

## 5. How modes use this file

- **REVIEW mode** (Reviewer 2: Method and Evidence): when method tier is archival/text/AI, load this file alongside `methods/archival_panel_checklist.md` and incorporate the eight-dimension scorecard into Reviewer 2's major concerns.
- **AUDIT mode**: when the user supplies enough of the methods section to assess measurement, run the eight-dimension scorecard at the appropriate confidence level (QUICK/STANDARD/FULL).
- **POLISH mode** and **SECTION mode**: when rewriting the methods section, use this file to identify missing reporting elements and flag them as `[MEASUREMENT EVIDENCE NEEDED: <dimension>]` rather than fabricating the validation results.
- **PACKAGE mode**: cross-check that the AI-use disclosure covers LLM measurement, not only LLM writing assistance.
- **RESPOND mode**: if reviewers challenged the LLM measurement, use this file to structure the response (which evidence is reported, what was added, what cannot be added and why).

For Claude Code users, this file is the reference base of the `jbr-gpt-measurement-auditor` companion subagent.

---

## 6. Hard rules

1. **Never estimate validation metrics that the manuscript does not report.** Say "Not reported."
2. **Never recommend a universal F1 threshold.** Acceptable performance depends on prevalence, construct difficulty, and downstream use.
3. **Never accept "GPT classification is reliable" without numbers.** That phrase is a red flag, not evidence.
4. **Never extrapolate one prompt's performance to another prompt.** Each prompt is a separate measurement instrument.
5. **Do not penalize the author for using LLMs.** Audit the validation, not the choice of method.
