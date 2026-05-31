---
file: ss_section_rewrite_playbook.md
purpose: Per-section rewriting templates for SS POLISH and SECTION modes. Modeled on patterns from Asghar, Kanis, Qu, and Clough.
last_verified: 2026-05-21
---

# SS Section Rewrite Playbook

## Contents

- 1. Abstract
- 2. Introduction
- 3. Theory & Hypotheses (or Theoretical Background / Framework for theory papers)
- 4. Methods (or Sample and Methods)
- 5. Results
- 6. Discussion (or Discussion and Conclusion)
- 7. Title
- 8. Keywords


This playbook gives section-by-section rewriting templates calibrated to Strategy Science. Each section has (a) a diagnostic checklist, (b) a target structure, and (c) common rewrites.

---

## 1. Abstract

### Diagnostic checklist

- [ ] Length <=200 words for manuscript submission; <=250 words for ScholarOne metadata (use `scripts/check_abstract_word_count.py`)
- [ ] Opens with the strategic problem or theoretical motivation (not "this paper examines...")
- [ ] Names the theoretical framework or lens
- [ ] Describes the empirical design (or analytical approach for theory papers)
- [ ] Reports the key finding(s) — including nulls/surprises if relevant
- [ ] States the theoretical contribution in 1-2 specific moves (not a list of three vague items)
- [ ] No undefined acronyms (or define on first use)
- [ ] No citations (SS abstracts typically have zero citations)
- [ ] No first-person introductions ("In this paper, we...") — go directly to substance

### Target structure (<=200 manuscript words)

```
[2-3 sentences: theoretical motivation / strategic problem.]
[1-2 sentences: theoretical lens or mechanism.]
[2-4 sentences: empirical design or analytical approach.]
[3-5 sentences: key findings or framework outputs.]
[1-2 sentences: theoretical contribution (one or two specific moves).]
```

### Exemplar (Kanis et al. 2026, ~260 words)

> Strategic foresight — that is, the ability to predict strategic outcomes — depends on how decision-makers represent strategic problems. Time constraints and large language models (LLMs) are increasingly salient factors shaping this process. We study how both jointly affect mental representations and strategic foresight in a startup evaluation task (N = 348). Using a 2 × 2 experimental design, we show that both time constraints and LLM use significantly alter the characteristics of mental representations. Despite these representational shifts, neither time constraints nor LLM use are found to significantly change strategic foresight. Additional analyses indicate, for instance, that LLM use increases information overload and reduces psychological ownership. Our findings can be viewed as a cautionary case for the effectiveness of LLM use in strategic decision-making. Thus, our findings suggest several avenues for future research on LLM use and strategic foresight, particularly regarding the interplay between individual cognitive processes and the contextual factors of strategic decisions.

### Common rewrites

| BEFORE | AFTER | Why |
|---|---|---|
| "In this paper, we examine..." | (Delete; start with the substantive claim) | SS abstracts open with content, not framing |
| "Few studies have studied X" | "X is a key driver of [strategic outcome]..." | Anchor in the phenomenon, not the gap |
| "We make three main contributions..." | "We extend [lineage] by [specific move 1] and [specific move 2]" | Specific, not a vague list |
| "Results show that..." | "We find that..." or "Our analysis shows..." | Active voice, INFORMS norm |
| "Our findings have important theoretical and practical implications" | (Delete; the contribution sentence already covers this, or be specific about which implication) | Boilerplate |

---

## 2. Introduction

See `references/ss_introduction_and_contribution.md` for the full ¶1-¶7 structure.

### Diagnostic checklist (in addition to lineage-anchoring file)

- [ ] ¶1 opens with anchored claim, not literature gap
- [ ] Primary theoretical lineage named with anchor citation cluster
- [ ] Theoretical tension visible by ¶2
- [ ] Research question explicit by ¶3
- [ ] Method/setting-fit explained in ¶4
- [ ] Headline findings (or framework outputs) in ¶5
- [ ] Contribution paragraph: ONE OR TWO specific moves (not a list)
- [ ] Total length 4-6 pages double-spaced
- [ ] Citations dense in early paragraphs (anchoring) and thin in later (after the lineage is established)

### Common rewrites for the contribution paragraph

| Pattern | Rewrite to |
|---|---|
| "Our paper makes the following three contributions..." (list) | "Our paper offers primary contributions to two literatures. First, we extend..." (two specific moves) |
| "We contribute to the [literature] by [generic claim]" | "We extend [specific lineage, with anchor citation] by [specific theoretical movement]" |
| "We are the first to..." (without evidence) | "We add to an emerging stream of work on X (cite 3-5 anchors) by..." |
| "Our practical implications include..." (boilerplate) | "Our findings may guide managers to [specific action tied to the mechanism]" |

---

## 3. Theory & Hypotheses (or Theoretical Background / Framework for theory papers)

### Diagnostic checklist (empirical papers)

- [ ] Section opens with the primary lineage and anchor citations
- [ ] Subsections (2.1, 2.2, ...) each begin with a lineage-anchor sentence
- [ ] Each hypothesis is preceded by 1-3 paragraphs of mechanism-building
- [ ] Each hypothesis names the cognitive/structural/strategic mechanism
- [ ] Counter-arguments are addressed (not buried in limitations)
- [ ] Boundary conditions are stated explicitly
- [ ] Hypothesis labels in bold-italic INFORMS style: `**Hypothesis 1a (H1a).** *...*`
- [ ] Each hypothesis is falsifiable
- [ ] Total length 8-15 pages double-spaced

### Diagnostic checklist (pure-theory papers, Clough pattern)

- [ ] Building blocks defined precisely with formal precision (Clough §3 defines coordination speed and scope)
- [ ] Assumptions stated transparently
- [ ] Argument proceeds in stages, with each stage clearly labeled
- [ ] Framework/typology summarized in a table or figure
- [ ] Testable predictions stated for future empirical work

### Common rewrites

| BEFORE | AFTER | Why |
|---|---|---|
| "Researchers have noted..." | "Following [specific anchor citation], we view X as..." | Anchor the claim |
| "X may affect Y" (no mechanism) | "X affects Y because [stated cognitive/structural mechanism]" | Mechanism specification |
| "We hypothesize that X is positively related to Y" | "We hypothesize that X is positively related to Y because [mechanism]. Hypothesis: ..." | SS hypotheses require a stated mechanism |
| Hypothesis stated as a research question | Hypothesis stated as a falsifiable proposition with direction | Hypotheses ≠ RQs |
| Hypothesis numbered without bold-italic | Bold-italic per INFORMS norm | Formatting |

### Hypothesis-paragraph template

```
[Anchor citation cluster: the relevant prior work that supports the prediction.]

[Mechanism paragraph: WHY does X affect Y? Name the cognitive/structural/
strategic mechanism. 1-2 paragraphs.]

[Counter-argument paragraph (when applicable): What is the competing
prediction or boundary case? Address it briefly. Asghar opens H1a with both
the cognitive-flexibility argument and the cognitive-overload counter-argument
before stating the prediction.]

[Boundary statement: Under what conditions is the prediction stronger or
weaker?]

**Hypothesis 1a (H1a).** *Italicized statement of the prediction.*
```

---

## 4. Methods (or Sample and Methods)

### Diagnostic checklist

- [ ] Section opens with the sample, the setting, the time window
- [ ] Setting-fit rationale: why this setting reveals the mechanism (the "fruit fly" argument)
- [ ] Unit of analysis is named explicitly
- [ ] Construct definitions precede measures
- [ ] DV, IVs, controls each in a separate subsection
- [ ] Measurement procedure detailed enough to replicate
- [ ] Validity evidence for novel measures (Krippendorff α for LLM-coded; train-test R² for ML-predicted)
- [ ] Econometric model specified (e.g., "We estimated our models using OLS regression with firm fixed effects...")
- [ ] Clustering of SE described
- [ ] Robustness checks foreshadowed

### Section structure (archival panel — Asghar pattern)

```
3. Sample and Methods
3.1. [Brief sample description, time window, data sources]
3.2. Dependent Variable [definition + measurement + validity evidence]
3.3. Independent Variables [each construct + measurement, often using Teachman entropy index]
3.4. Control Variables [grouped by category: firm-level, individual-level, governance, etc.]
3.5. Econometric Model [model specification, FE structure, clustering]
```

### Section structure (experiment — Kanis pattern)

```
Methods
Task [description of the experimental task]
Design and Manipulation [2×2 or other design; manipulation procedure]
Procedure [participant flow]
Measures [DVs, manipulation checks; cite established scales]
Participants [G*Power justification, recruitment platform, demographics, exclusion criteria]
```

### Section structure (archival + ML — Qu pattern)

```
3. Methods
3.1. Data and Sample
3.2. Predictions of Market Reactions
   3.2.1. Overview [ML approach, comparison algorithms]
   3.2.2. Output Variable [the outcome being predicted]
   3.2.3. Input Variables [feature set]
3.3. Regression Analyses of [downstream outcome]
   3.3.1. Dependent Variable
   3.3.2. Independent and Control Variables
```

### Common rewrites

| BEFORE | AFTER | Why |
|---|---|---|
| "We collected data from..." | "We tested our hypotheses using a sample of [N] [units] [from source] over [time window]." | Front-load the design |
| "We measured X using a 7-point scale" (alone) | "We measured X using a 7-point scale (Author year, α = 0.XX). [Brief content rationale.]" | Cite the source and report reliability |
| "We ran OLS regressions" (alone) | "We estimated our models using OLS regression with [FE structure] and robust standard errors clustered at [level]." | Full specification |
| "Our LLM coded the responses" | "We used [N] LLMs (gpt-X, claude-X, mistral-X) with Krippendorff's α = 0.89 against human coders on a subset of 220 items..." | Multi-LLM and reliability evidence |

---

## 5. Results

### Diagnostic checklist

- [ ] Standard reporting order: descriptives → correlations → main test → robustness → additional analyses
- [ ] Tables follow INFORMS style (SE in parentheses)
- [ ] Effect sizes reported, not just significance
- [ ] Each hypothesis is tested and the result stated explicitly
- [ ] Null results reported honestly
- [ ] Robustness checks tied to specific threats
- [ ] Additional analyses explore mechanisms (Kanis 2026 has an extensive "Additional Analyses" subsection)

### Section structure (Kanis pattern)

```
Results
Manipulation Check [for experiments]
Descriptive Statistics and Correlations
Time Constraints [tests of H1a-H1d]
LLMs [tests of H2a-H2d]
Additional Analyses [mechanism exploration]
```

### Common rewrites

| BEFORE | AFTER | Why |
|---|---|---|
| "The results were significant" | "We found that [variable] was significantly associated with [outcome] (β = 0.XX, SE = 0.XX, p < 0.0X)" | Full reporting |
| "H1 was confirmed" | "In line with Hypothesis 1, [specific evidence]" | SS reports evidence, not "confirmation" |
| Coefficient tables without notes | Coefficient tables with `*Notes.*` describing dependent variable, FE structure, SE clustering, significance levels | INFORMS norm |
| Robustness checks listed without rationale | Each check named with the threat it addresses | Reviewer signals |

---

## 6. Discussion (or Discussion and Conclusion)

### Diagnostic checklist

- [ ] Opens with a one-paragraph overview of what was done and found
- [ ] Theoretical implications section: explicitly engage the lineages cited in the introduction
- [ ] Each theoretical implication is tied to a specific finding
- [ ] Managerial implications are specific and tied to the mechanism
- [ ] Limitations are substantive (not generic "single-context", "single-time-point" boilerplate)
- [ ] Future research directions follow from the limitations
- [ ] No new findings introduced

### Section structure

```
5. Discussion and Conclusion
5.1. Overview [1 paragraph summarizing the project]
5.2. Theoretical Implications [engages primary lineage(s) cited in intro]
5.3. Managerial/Practical Implications [specific actions tied to the mechanism]
5.4. Limitations and Future Research [substantive limitations + corresponding research directions]
```

For Qu (more discursive structure):
```
5. Discussion and Conclusion
5.1. Overview
5.2. Implications for AI and Prediction Capabilities
5.3. Future Directions
```

For Clough (theory paper):
```
6. Discussion
6.1. [Theoretical placement]
6.2.1. [Implication]
6.2.2. Ecosystem Dynamics and Transitions Between Architectures
6.2.3. Architectures, Capabilities, and Competition
6.3. Conclusion
```

### Common rewrites

| BEFORE | AFTER | Why |
|---|---|---|
| "Our study has limitations" (generic list) | Specific limitations tied to design and mechanism (Kanis 2026 has 7 specific limitations) | SS expects substantive limitations |
| "Future research could explore..." (generic) | "Future research could [specific direction] given [the specific gap identified]" | Tied to limitations |
| "Our findings have managerial implications" | "Our findings suggest that managers should [specific action] because [mechanism finding]" | Specific actions |
| Restating the findings | Engaging the theoretical implications | Discussion ≠ summary |

---

## 7. Title

### Diagnostic checklist

- [ ] Names the strategic phenomenon
- [ ] Names the theoretical mechanism or framework
- [ ] Not too generic ("Strategy in the AI Era")
- [ ] Not too narrow (matches the empirical setting only)
- [ ] Subtitle (after colon) often used to clarify

### Exemplar title patterns

- "Human Capital and Strategic Foresight: Evidence from Managers' Stock Purchases" (Asghar) — phenomenon-and-theory : evidence-context
- "AI-Augmented Strategic Decision-Making Under Time Constraints: An Experimental Study on Mental Representations and Strategic Foresight" (Kanis) — phenomenon : study-type-and-mechanism
- "The Role of Predictions in Acquisition Decision Making: The Strategic Value of AI-Driven Foresight" (Qu) — phenomenon : theoretical-claim
- "Governance Structures and Coordination Trade-offs: A Discriminating Alignment Theory of Innovation Ecosystem Architectures" (Clough) — phenomenon-and-trade-off : framework-name

### Title length

40-100 characters typical for the main title (before colon); subtitles add 30-80 characters.

---

## 8. Keywords

### Diagnostic checklist

- [ ] 3-10 keywords
- [ ] Match the abstract's vocabulary
- [ ] Anchor in the primary lineage (e.g., "strategic foresight", "mental representations", "ecosystem", "governance")
- [ ] Mix theoretical and methodological keywords
- [ ] No vague single-word keywords ("strategy", "performance" alone)

### Exemplar keyword sets

- "artificial intelligence • large language models • mental representations • strategic foresight • strategic decision-making • time constraints" (Kanis)
- "artificial intelligence • strategic decision making • acquisitions • strategic foresight • machine learning • market reactions" (Qu)
- "architecture • coordination • decentralization • ecosystem • governance • network • organization design • platform" (Clough — 8, high end)
- "human capital • knowledge breadth • strategic foresight • insider trading • new product introductions" (Asghar)
