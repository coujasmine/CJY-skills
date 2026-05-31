---
file: gpt_measurement_validation.md
purpose: >
  Eight-dimension scorecard for LLM-as-measurement studies submitting to
  Strategy Science. Calibrated against Kanis et al. 2026's multi-LLM coding
  approach (gpt-4.1, claude-opus-4-1-20250805, mistral-large-latest;
  Krippendorff α = 0.89 against human coders). Use this as a strong recent exemplar, not an official cutoff. Used in AUDIT and REVIEW modes
  whenever LLMs serve as measurement or coding instruments.
last_verified: 2026-05-31
---

# LLM-as-Measurement Validation Scorecard for Strategy Science

## Contents

- When this scorecard applies
- The eight dimensions
- Output format (use in AUDIT and REVIEW modes)
- LLM-Measurement Scorecard
- Common SS-specific concerns
- Reporting template for the methods section


When a strategy research design uses an LLM (GPT, Claude, Gemini, Mistral, Llama, or similar) as a *measurement instrument* — to code text, classify cases, extract structured information, or generate scores — the manuscript must demonstrate that the measurement is valid and reliable. This scorecard provides the eight dimensions SS reviewers (and especially Reviewer 2) check.

> **Calibration anchor:** Kanis, Mann & Stumpf-Wollersheim (2026) provide a strong recent SS precedent. They use three LLMs (gpt-4.1, claude-opus-4-1-20250805, mistral-large-latest) with classification consistency r = 0.93, validated against human coders on 220 items with Krippendorff's α = 0.89. Prompts and procedure are documented in their Appendix A. Do not copy these model names or thresholds unless they match the user's actual design.

> **Hard rule (from SKILL.md Hard Rule 12):** Do not estimate validation metrics the manuscript does not report. If a dimension is missing from the manuscript, flag it as [MEASUREMENT EVIDENCE NEEDED].

---

## When this scorecard applies

Apply this scorecard when the user's method tier involves:

- LLM classification of text into pre-defined categories (Kanis: pros/cons → 10 strategic categories)
- LLM coding of qualitative responses
- LLM extraction of structured information from documents
- LLM generation of quantitative scores or ratings
- LLM-augmented content analysis

Does NOT apply when:
- LLM is used only for writing/editing assistance
- ML model (random forest, neural net, etc.) is used for prediction but not for measurement (use `methods/archival_panel_checklist.md` instead)
- LLM is the *object of study* rather than a measurement tool

---

## The eight dimensions

### Dimension 1: Construct definition before measurement

**What to check:**
- Is the construct being measured defined explicitly with theoretical grounding?
- Does the definition precede the operationalization?
- Does the operationalization (LLM coding) match the definition?

**Failure modes:**
- Construct defined ad hoc from the LLM output ("the LLM identified these categories, so we call this X")
- Definition borrowed loosely from prior work without specifying which definition applies
- Definition shifts between theory section and measurement section

**SS norm:** The construct should map to a recognized SS theoretical lineage (see `ss_track_positioning.md`). E.g., "breadth of mental representations" maps to Csaszar & Laureiro-Martínez 2018; "knowledge breadth" maps to Custódio et al.

**Kanis example:** Breadth is defined as "the number of distinct categories in participants' mental representations" (Csaszar & Laureiro-Martínez 2018). The LLM coding operationalizes this by counting distinct categories the LLM assigns from the 10 pre-defined strategic categories.

**Status options:** ✓ Pass / ⚠ Weak (definition exists but loosely tied to operationalization) / ✗ Missing

---

### Dimension 2: Prompt engineering hygiene

**What to check:**
- Are the LLM prompts (system + user) documented in full, ideally in an appendix?
- Is the prompt version-controlled (e.g., dated, attached to a specific LLM version)?
- Are the LLM models named with version pins (not just "Claude" but "claude-opus-4-1-20250805")?
- Is the batching/inference procedure described (e.g., one item at a time, batches of N, with context limits)?
- Is the temperature or other inference parameter set (typically 0 for measurement to ensure determinism)?
- Are the LLM's instructions about hallucination explicit (e.g., "do not invent information")?

**Failure modes:**
- "We asked GPT to classify..." (no prompt detail)
- Generic "we used Claude" (no version pin)
- Different prompts used across LLMs without justification
- No mention of temperature or determinism settings

**SS norm:** Kanis 2026 reports the full system prompt in Appendix A. The skill expects this level of transparency.

**Status options:** ✓ Pass / ⚠ Weak (some detail; prompt not in appendix) / ✗ Missing

---

### Dimension 3: Development/validation set separation

**What to check:**
- Was the prompt engineered on a development set separate from the validation/main analysis set?
- If the prompt was tuned (e.g., by trial-and-error on the data), is the development set clearly separated from the rest?
- Is there a "frozen" prompt used for the main analysis?

**Failure modes:**
- Iterative prompt tuning on the entire dataset (overfitting risk)
- No separation between prompt development and prompt application
- "We refined the prompt until results matched expectations" (confirmation bias)

**SS norm:** Less explicitly tested in Kanis 2026 (the prompt is the prompt across all items), but for studies where prompts evolve, separation is essential.

**Status options:** ✓ Pass / ⚠ Weak (separation implied but not stated) / ✗ Missing / N/A (if single fixed prompt across all data)

---

### Dimension 4: Human benchmark and inter-rater reliability

**What to check:**
- Is there a human-coded benchmark subset?
- What is the inter-rater reliability between LLM and humans (Krippendorff's α, Cohen's κ, or comparable)?
- What is the inter-rater reliability between human coders themselves (to establish a ceiling)?
- Is the subset size adequate (Kanis: 220 of total items)?
- Are disagreements resolved transparently?

**Failure modes:**
- No human benchmark at all
- Human benchmark too small (e.g., N=20)
- Reported "agreement" without statistical reliability measure
- Reliability measured against author judgment (circular)

**Reliability benchmark:** Krippendorff's α >= 0.80 against human coders is commonly treated as acceptable in content analysis; α >= 0.90 is excellent. Kanis reports 0.89, which is a strong recent SS precedent.

**Status options:** ✓ Pass (α ≥ 0.80 against humans on N ≥ 100) / ⚠ Weak (α between 0.65-0.80, or small N) / ✗ Failing (α < 0.65 or no human benchmark)

---

### Dimension 5: Convergent and discriminant validity

**What to check:**
- Does the LLM-coded measure correlate with related constructs (convergent)?
- Does it diverge from unrelated constructs (discriminant)?
- Does the measure predict downstream outcomes consistent with theory?

**Failure modes:**
- LLM-coded measure used in main analysis without external validity check
- Measure correlates strongly with everything (no discrimination)
- Measure does not correlate with theoretically related external constructs

**SS norm:** Kanis 2026 reports the breadth measure correlates negatively with depth (r = -0.30, p < 0.01) and negatively with consensus (r = -0.80, p < 0.01) — both theoretically expected. This pattern-matching validates the construct.

**Status options:** ✓ Pass / ⚠ Weak (one validity check but not both) / ✗ Missing

---

### Dimension 6: Sensitivity and robustness

**What to check:**
- Does the conclusion hold under alternative LLM choices?
- Does it hold under alternative prompts?
- Does it hold under alternative coding thresholds?
- Is variance across LLMs reported (Kanis: three LLMs with inter-rater r = 0.93)?

**Failure modes:**
- Single LLM used; no robustness to alternative LLMs
- Single prompt; no sensitivity analysis
- Results highly dependent on prompt or LLM choice (suggests overfitting to a specific configuration)

**Strong-design benchmark:** Prefer two or more LLMs with reported inter-LLM agreement, plus validation against human coders when the LLM output is a core measure. Treat any numeric cutoff as a reviewer-facing convention to justify, not as an official SS rule.

**Kanis approach:** Three LLMs; agreement r = 0.93; if any LLM-pair disagreement, resolved by majority vote; ambiguous cases resolved by author team discussion.

**Status options:** ✓ Pass / ⚠ Weak (sensitivity check exists but limited) / ✗ Missing

---

### Dimension 7: False-positive / hallucination review

**What to check:**
- Were LLM outputs manually reviewed for hallucinations or invented content?
- For classification: were "ambiguous" or "uncertain" outputs handled transparently?
- For extraction: were "not found" or "I don't know" responses preserved (not coerced into a value)?
- Is the hallucination rate reported, if assessed?

**Failure modes:**
- LLM outputs treated as ground truth without review
- Coerced answers (LLM forced to pick a category when it would say "uncertain")
- No transparency about ambiguous cases

**SS norm:** Kanis 2026 system prompt includes an instruction: "We instructed the LLM to only provide information from the videos to avoid false information (resulting from hallucinations), which could have negatively influenced participant performance." This is the right disposition: structural prompt design to minimize hallucination, plus reported handling of ambiguous cases.

**Status options:** ✓ Pass / ⚠ Weak (some attention but not systematic) / ✗ Missing

---

### Dimension 8: Reporting and disclosure

**What to check:**
- Is the LLM use disclosed in the methods?
- Is it reported in the methods/appendixes and covered by an AI-use transparency statement if the portal, cover letter, editor, or funder requests one (see `ss_disclosures.md`)?
- Are prompts in an appendix?
- Is the validation procedure described in detail?
- Are model versions named?
- Is replicability addressed (note: LLM measurements may not be exactly replicable due to model updates; this should be acknowledged)?

**Failure modes:**
- Methods section glosses over LLM use ("we coded the data using LLM-assisted classification")
- No AI-use transparency language where requested, or no methods disclosure for LLM-as-measurement/coding
- Prompts not shared
- Generic model names without version pins

**Strong SS precedent:** Kanis 2026 documents LLMs by name and version, includes the system prompt in Appendix A, reports the Krippendorff α, names the human-coder subset, and reports LLM use in the methods and transparency materials.

**Status options:** ✓ Pass / ⚠ Weak (some elements documented; others missing) / ✗ Missing

---

## Output format (use in AUDIT and REVIEW modes)

When this scorecard is triggered, produce:

```
## LLM-Measurement Scorecard

| Dimension | Status | Comment |
|---|---|---|
| 1. Construct definition before measurement | ✓/⚠/✗ | [Brief observation] |
| 2. Prompt engineering hygiene | ✓/⚠/✗ | [Brief observation] |
| 3. Development/validation set separation | ✓/⚠/✗/N/A | [Brief observation] |
| 4. Human benchmark and inter-rater reliability | ✓/⚠/✗ | [α/κ value if reported; N of benchmark] |
| 5. Convergent and discriminant validity | ✓/⚠/✗ | [Brief observation] |
| 6. Sensitivity and robustness | ✓/⚠/✗ | [Number of LLMs / prompts; agreement] |
| 7. False-positive / hallucination review | ✓/⚠/✗ | [Brief observation] |
| 8. Reporting and disclosure | ✓/⚠/✗ | [Brief observation] |

### Overall measurement validity verdict
[2-4 sentences. STRONG / ADEQUATE / WEAK / UNACCEPTABLE for SS submission]

### Required actions before submission
1. [Most critical missing element]
2. ...
```

---

## Common SS-specific concerns

### LLM-as-coder of qualitative data

When LLMs code qualitative responses (interviews, open-ended survey responses), reviewers will compare against established qualitative coding practices (e.g., Gioia methodology, grounded theory). The LLM does not replace theoretical coding judgment; it provides a first-pass classification that humans validate.

**Required:**
- Theoretical coding framework defined before LLM application
- Humans coding a subset to validate LLM
- Disagreement resolution procedure
- Acknowledgment of what the LLM cannot do (e.g., emergent theme discovery)

### LLM-as-extractor of structured information

When LLMs extract structured info (e.g., from 10-K filings, conference call transcripts), reviewers will check:
- Ground-truth comparison: humans extract the same info from a subset
- Hallucination rate
- Coverage rate (how often does the LLM correctly identify presence vs. absence?)

### LLM-as-rater for complex constructs

When LLMs rate complex constructs (e.g., "strategic dynamism" of a firm), reviewers will be skeptical:
- The construct should be defined precisely enough that disagreement is meaningful
- Multiple LLMs should agree at high levels
- Human validation should be substantial (≥ 100 items)
- Sensitivity to prompt phrasing should be tested

### Cost-benefit framing

SS reviewers occasionally ask: why LLM rather than human? Common acceptable reasons:
- Scale (10,000+ documents not feasible for humans)
- Consistency (LLM applies the same prompt; humans drift)
- Replicability (with version pinning)

Unacceptable reasons:
- "It was faster" (without scale justification)
- "It was cheaper" (without scale justification)
- "Other papers use LLMs" (appeal to authority)

---

## Reporting template for the methods section

```
**Measurement of [Construct] Using LLMs**

We measured [construct] using LLM-based classification. Specifically, we used
[N] LLMs ([model 1] version [X], [model 2] version [Y], [model 3] version [Z])
to classify [units] into [number] pre-defined categories. The construct was
defined as [definition with theoretical anchor citation]. The classification
categories were drawn from [source].

The system prompt and user prompt are provided in Appendix [X]. For each
[unit], we submitted the [content] to each LLM individually using a temperature
of 0 for determinism. When the [N] LLMs disagreed on classification, we
resolved by [majority vote / author discussion / re-prompting].

To validate the LLM classification, [two/three] of the authors independently
coded a subset of [N=] [units], following the same coding framework. Inter-rater
reliability between the LLM-aggregated classification and human classification
was Krippendorff's α = [value]. Inter-coder reliability among humans was
α = [value], indicating a [ceiling] for the LLM measure.

We additionally tested sensitivity to alternative [prompt phrasings / LLM
versions / classification thresholds] and found [results were robust / minor
variation reported in Appendix Y].
```

This template, when filled in honestly, produces a methods section that satisfies all eight dimensions of the scorecard.
