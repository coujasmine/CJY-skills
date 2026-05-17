---
file: jbr_section_rewrite_playbook.md
purpose: Section-by-section rewriting templates with explicit DO/DON'T, opening moves, and JBR calibration. Used in POLISH and SECTION modes.
last_verified: 2026-05-17
---

# JBR Section Rewrite Playbook

For each section, this playbook gives:

- **Function**: what the section must achieve at JBR
- **Opening move**: the first 2–3 sentences pattern
- **Required elements**: must be present
- **Forbidden moves**: things that trigger reviewer pushback
- **Length budget**: word/page count for a 45-page JBR submission
- **Calibration note**: which claim-strength to use

Every rewrite must preserve the user's authorial voice and substantive content. Polish for **rigor, clarity, and JBR fit**, not for stylistic uniformity.

---

## 1. Abstract (≤150 words; rewrite LAST so it harmonizes with final intro/discussion)

**Function**: Six moves in 150 words — (1) business problem, (2) research question, (3) theoretical lens, (4) data/method, (5) calibrated findings, (6) theoretical + practical contribution.

**Opening move**: Start with the business decision tension, not with the literature.

| DO | DON'T |
|---|---|
| Open with a concrete business problem ("Firms increasingly invest in AI capabilities, yet performance returns vary widely") | Open with "Despite growing interest in X, little is known about Y" |
| State the RQ explicitly ("We ask how X shapes Y through Z") | Bury the RQ |
| Name the primary theory in one phrase | Name three theories competing for primacy |
| Specify data ("Using a panel of 2,000 Chinese listed firms, 2014–2024…") | Be vague ("Using firm-level data…") |
| Calibrate findings to the design (see `jbr_claim_evidence_matrix.md`) | Use "causes" with cross-sectional data |
| Two contributions: one theoretical (mechanism / boundary / integration / clarification / reconciliation / contextualization), one practical | One vague contribution ("enriches the literature") |

**Length budget**: 130–150 words.

**Calibration**: Match the strongest claim in the body. If the body says "associated with," the abstract must not say "causes."

---

## 2. Introduction (≈1,000–1,500 words; 3–5 pages)

**Function**: Establish the business problem, the theoretical insufficiency, the research question, the study design, and the contribution — in that order.

**Opening move**: Sentence 1 names the phenomenon as a business concern; sentence 2 makes the tension visible.

### Six-paragraph template (JBR-typical)

1. **Phenomenon paragraph** — concrete business setting; numbers / firm examples / market dynamics. Show, do not tell.
2. **Tension paragraph** — why this phenomenon is theoretically puzzling; what is unresolved (mechanism / boundary / contradiction / contextual variant)
3. **Research question paragraph** — RQ stated explicitly; primary theory named; auxiliary theories signaled
4. **Study design paragraph** — context, data, method, in one or two sentences; why this design fits the theory
5. **Findings preview paragraph** — calibrated to design; one or two key results, not all of them
6. **Contribution paragraph** — one specific theoretical movement, framed as "We contribute to [literature] by [specific verb] [specific construct/mechanism/boundary]"

### Required elements

- RQ visible by **page 2**
- Primary theory named by **page 2**
- A real business example (firm name, market, decision) by **page 1**
- "We contribute…" sentence by **last paragraph of intro**

### Forbidden moves

- "Little is known about…" / "Few studies have examined…" as opening
- Three vague contributions instead of one sharp one
- Promising findings the data do not deliver
- Long literature review embedded in the intro (push that to Theory section)
- "First paper to…" claim without a search log

**Length budget**: 1,000–1,500 words. If the intro exceeds 1,800, cut.

---

## 3. Theory & Hypotheses (≈2,000–3,000 words; 5–8 pages)

**Function**: Build the theoretical scaffolding that the hypotheses sit on. Each hypothesis must name a mechanism.

### Structure

- **3.1 Primary theory subsection** — define the theory, name its core mechanism, cite seminal + recent applications (3–5 citations max, not a literature dump)
- **3.2 Construct definitions** — define every focal construct **before** any hypothesis uses it
- **3.3 Hypothesis development** — one subsection per hypothesis; each subsection has:
  - the **mechanism sentence** (how/why the relation holds)
  - **boundary signal** (when the relation is stronger/weaker)
  - **counter-argument acknowledgment** (one sentence on a rival prediction, then why this paper expects the stated direction)
  - the **hypothesis statement** in italics or boxed, with direction explicit (H1: X is positively related to Y)

### Required elements

- One **primary** theoretical conversation throughout (the same theory cited in §3.1 must be the one closing the contribution in the discussion)
- Every hypothesis has a stated **mechanism**
- Every hypothesis is **falsifiable** (rejectable by data)

### Forbidden moves

- Three competing primary theories
- "Mechanism" that is just a restatement of the direction (e.g., "AI improves performance because AI helps firms perform better")
- Hypotheses that mix levels of analysis (e.g., individual-level mechanism, firm-level hypothesis test)
- Hidden tautologies

**Length budget**: 2,000–3,000 words.

---

## 4. Method (≈1,500–2,500 words; 4–6 pages)

**Function**: Convince the reviewer that the design can carry the claim. Transparency over comprehensiveness.

### Structure

- **4.1 Setting / sample** — why this context reveals the mechanism (theoretical sampling, not convenience)
- **4.2 Data sources** — provenance, period, granularity; for survey, the sampling frame and response rate; for archival, the merge logic
- **4.3 Measures** — for each construct: definition, operationalization, source, validation (CFA, prior validation, inter-rater agreement)
- **4.4 Analytical strategy** — model specification, identification assumptions, robustness plan
- **4.5 Common-method bias / endogeneity / selection** — procedural and statistical remedies; for archival, identification strategy (FE, IV, DiD, matching)

### Required elements

- Sampling rationale tied to the theory
- Construct definition **before** the measure
- Level-of-analysis consistency check (theory ↔ measures ↔ model)
- Sufficient detail to replicate (or a clear pointer to a replication appendix)

### Forbidden moves

- "We followed standard practice" without naming the practice
- Measures introduced before constructs are defined
- Endogeneity addressed only with "we acknowledge endogeneity in limitations"
- CMV addressed only with "Harman's single-factor test" (this is widely critiqued; add procedural remedies)

**Length budget**: 1,500–2,500 words.

---

## 5. Results (≈1,500–2,500 words; 4–6 pages)

**Function**: Present evidence in the order the reader can follow: descriptive → correlations → main test → robustness → supplementary.

### Structure

- **5.1 Descriptive statistics and correlations** (Table 1 + Table 2)
- **5.2 Hypothesis tests** — in the order H1, H2, H3…; one paragraph per hypothesis with effect size, significance, and a sentence interpreting the magnitude
- **5.3 Robustness checks** — each tied to a specific threat ("To address [threat X], we [analysis Y]; results hold")
- **5.4 Supplementary / exploratory analyses** — clearly labeled as exploratory; do not conflate with hypothesis tests

### Required elements

- Effect sizes reported, not just p-values
- Coefficient interpretation in substantive units (e.g., "a one-standard-deviation increase in X is associated with a 7% change in Y")
- Tables and figures cited in sequence
- Robustness checks tied to plausible reviewer threats

### Forbidden moves

- "Significant at p<0.05" as the only result language
- Burying nulls (report them; nulls often refine the mechanism)
- Mixing hypothesis tests with exploratory analyses
- Tables that report many models without telling the reader which to read

**Length budget**: 1,500–2,500 words.

---

## 6. Discussion (≈1,500–2,500 words; 4–6 pages)

**Function**: Interpret, do not restate. Move from findings → theoretical implications → practical implications → limitations → future research → conclusion.

### Structure

- **6.1 Summary of findings** (≤1 paragraph; the rest of the section interprets)
- **6.2 Theoretical implications** — what the findings change for the primary theoretical conversation; each implication tied to a specific finding
- **6.3 Practical implications** — specific managerial / policy / stakeholder actions tied to the mechanism the study identified
- **6.4 Limitations** — design constraints, not generic disclaimers; tie each limitation to a future-research direction
- **6.5 Future research** — directions that follow from the limitations or the unresolved counter-arguments
- **6.6 Conclusion** — one paragraph that returns to the opening business problem and states what this study now lets us say about it

### Required elements

- Theoretical implications **named and bounded** (do not over-generalize)
- Practical implications **specific**, not "managers should consider X"
- Limitations include the **claim-strength ceiling** of the design
- Calibrated language throughout (see `jbr_claim_evidence_matrix.md`)

### Forbidden moves

- "Our findings suggest" used as a hedge for an over-strong claim
- Practical implications disconnected from the actual mechanism
- Limitations that say "future research should use a different method" without explaining what that method would reveal
- Discussion that introduces new constructs or new theory not built up in §3

**Length budget**: 1,500–2,500 words.

---

## 7. Title (≤15 words)

**Function**: Signal phenomenon, mechanism, and contribution type — without hype.

### Patterns that work at JBR

- "How [phenomenon] shapes [outcome]: The mediating role of [mechanism]"
- "When [phenomenon] [verb] [outcome]: [Boundary condition] as a [moderator type]"
- "[Mechanism] under [contextual condition]: Evidence from [setting]"
- "[Theoretical lens] and the [phenomenon]: A [method] study of [setting]"

### Forbidden moves

- "A study of…" (every paper is a study of something)
- "Towards a model of…" (no, propose the model)
- Marketing-style hype: "Unlocking," "Decoding," "The dark side of"
- Question titles unless the paper genuinely poses an open question

### Keywords (4–6)

- Mix construct names + theory + setting + method
- Use terms reviewers will search for, not idiosyncratic acronyms
- Verify the JBR keyword taxonomy if the user is targeting a special issue

---

## 8. Section harmonization checklist (final pass)

Before declaring the polish complete, verify:

- [ ] Abstract claim wording ≡ Discussion claim wording (no inflation)
- [ ] Intro RQ ≡ Theory hypotheses (same construct names)
- [ ] Theory mechanism ≡ Discussion theoretical implication (closed loop)
- [ ] Method ↔ Claim Matrix passes for every causal verb
- [ ] Contribution paragraph in intro ≡ Discussion §6.2 (same wording or near-paraphrase)
- [ ] Title ↔ Abstract ↔ Keywords are mutually consistent

If any of these fails, return to the relevant section and reharmonize. Do not ship a draft with an internally inconsistent claim chain.
