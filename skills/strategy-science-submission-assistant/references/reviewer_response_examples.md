---
file: reviewer_response_examples.md
purpose: >
  Short worked examples of Strategy Science reviewer-response tone and structure
  (sharpening theoretical contribution, softening causal language, validating
  LLM measurement, engaging counter-arguments). Used in RESPOND mode alongside
  cover_letter_and_response.md.
last_verified: 2026-05-21
---

# Strategy Science Reviewer Response Examples

## Contents

- 1. Sharpening Theoretical Contribution
- 2. Softening Causal Language
- 3. Validating LLM Measurement
- 4. Engaging Counter-Arguments
- 5. Partial Adoption (declining a suggested analysis)
- 6. Pure-Theory Paper — Engagement with Empirical Tests


Use these examples for tone and structure when drafting responses to SS reviewers.

---

## 1. Sharpening Theoretical Contribution

**Comment R1.2:** *The contribution is unclear. The paper would benefit from a sharper articulation of what specifically the framework adds beyond Csaszar and Laureiro-Martínez (2018).*

**Response:** We thank Reviewer 1 for pressing us to articulate the contribution more sharply. In the revision, we have restructured the introduction's contribution paragraph (page 4, paragraphs 5-6) and the discussion's theoretical implications (Section 5.2, pages 24-25) to name two specific theoretical movements:

(a) We extend the representational approach (Csaszar and Laureiro-Martínez 2018) by showing that representational characteristics — whether induced by time constraints or LLM use — do not necessarily translate into changes in strategic foresight. This refines the link between representations and outcomes in the lens-model tradition.

(b) We identify boundary conditions under which LLMs do not improve strategic outcomes despite altering cognitive inputs, contributing to the emerging literature on AI in strategic decision-making ([verified AI-strategy anchors]).

We have removed the three-item "contributes to the literature on X, Y, and Z" formulation per the reviewer's implicit guidance.

**Manuscript change:** Introduction paragraphs 5-6 (pages 4-5); Section 5.2 (pages 24-25); abstract (page 75, sentence 7).

---

## 2. Softening Causal Language

**Comment R2.3:** *The manuscript repeatedly uses causal language ("X causes Y", "X drives Y") although the design is panel archival with firm fixed effects, which does not identify causality. Either tighten the identification (e.g., IV, DiD) or soften the claim language throughout.*

**Response:** We agree that our original phrasing implied stronger causal claims than our observational design supports. We have made two changes:

(a) Throughout the manuscript, we have softened causal language. We now use "is associated with" / "predicts" / "is followed by" rather than "causes" / "drives" / "leads to" (revised throughout — see track changes for the full sweep; key locations are abstract page 75 line 12, intro page 3 paragraph 2, and discussion page 24 paragraph 1).

(b) We have added a paragraph to the Limitations section (Section 5.4, pages 26-27) that explicitly discusses the identification limitations of our design and the conditions under which our findings would generalize causally.

We considered implementing an instrumental-variable analysis but found no plausible instrument that satisfies the exclusion restriction in our setting. We discuss this in the new limitations paragraph (page 27).

**Manuscript change:** Throughout (see track changes); new limitations paragraph at page 27.

---

## 3. Validating LLM Measurement

**Comment R2.5:** *The use of GPT-4 to classify mental representations into strategic categories is a methodological choice that requires validation. How do we know the LLM is reliable? What is the inter-rater agreement with human coders?*

**Response:** We appreciate Reviewer 2's careful attention to measurement validity. We have substantially strengthened our measurement procedure in three ways:

(a) We now report inter-rater reliability between LLM classifications and human coders. Three of the authors independently coded a random subset of 220 items from across all participants and startups following the same coding framework. Inter-rater reliability between the LLM-aggregated classification and human coding was Krippendorff's α = 0.89 (Section 3.X, page Y). Inter-coder reliability among human coders was α = 0.87, indicating a ceiling for the LLM measure.

(b) We added a multi-LLM sensitivity analysis. In addition to gpt-4.1, we now report results using claude-opus-4-1-20250805 and mistral-large-latest. Inter-rater agreement across the three LLMs was r = 0.93 (Section 3.X, page Y).

(c) We document the full LLM prompts, batching procedure, and disagreement-resolution procedure in a new Appendix A. We resolved disagreements by majority vote among LLMs; for the 1.44% of cases where all three LLMs disagreed, we resolved by author team discussion.

This validation procedure follows recent SS exemplars including the parallel approach used by [prior published work in SS].

**Manuscript change:** Methods Section 3.X (page Y); new Appendix A (page Z); AI-use disclosure updated.

---

## 4. Engaging Counter-Arguments

**Comment R1.4:** *The paper assumes that knowledge breadth uniformly improves foresight, but cognitive-overload theories (Dane 2010; Haas & Ham 2015) suggest the opposite. This counter-argument should be addressed explicitly, not buried in limitations.*

**Response:** Thank you for raising this important counter-argument. In the revision, we have moved the cognitive-overload discussion into the main theoretical argument rather than the limitations section. Specifically:

(a) We have added a paragraph to Section 2.4.1 (pages 8-9) that engages the cognitive-overload counter-argument directly, citing Dane (2010), Haas & Ham (2015), and Mannucci & Yong (2018). We state both the cognitive-flexibility argument (broader knowledge → better foresight) and the cognitive-overload counter-argument (broader knowledge → more linkages → potential overload).

(b) We use this tension to motivate our theoretical contribution: rather than assuming a uniform direction, we propose that different *dimensions* of knowledge breadth (industry, firm, function) heterogeneously affect foresight — sometimes in opposite directions. This produces the differentiated predictions in Hypotheses 1a, 1b, and 1c.

(c) The empirical findings (Section 4) are consistent with this differentiated view: industry breadth has a negative association with foresight (cognitive-overload mechanism dominant), while firm and function breadth have positive associations (cognitive-flexibility mechanism dominant).

We believe this revision substantially strengthens the theoretical contribution by treating the counter-argument as a productive theoretical tension rather than a limitation to acknowledge.

**Manuscript change:** Section 2.4.1, paragraphs 4-6 (pages 8-9); Hypothesis 1a-c (pages 10-13); Discussion Section 5.2 (page 25).

---

## 5. Partial Adoption (declining a suggested analysis)

**Comment R3.7:** *The authors should expand the experimental design to include a third condition with a non-LLM AI tool (e.g., a traditional search engine) to test whether LLM use specifically — vs. any AI augmentation — drives the effects.*

**Response:** We thank Reviewer 3 for this thoughtful suggestion. We considered adding a third experimental condition carefully and ultimately chose not to add it for the following reasons:

(a) The proposed condition (LLM vs. search-engine vs. no-AI) would require approximately 175 additional participants (to maintain ~85 per cell across three LLM-related conditions and two time-constraint conditions = 6 cells × 85 = 510, vs. our current 348). This is beyond the scope of this revision.

(b) The theoretical contribution of the current 2×2 design is specifically about the joint effect of time constraints and LLM use on mental representations, building on the recent literature framing LLMs as artifacts capable of providing interactive external representations (Csaszar et al. 2024a). A non-LLM AI comparison condition would shift the research question.

(c) We have added the proposed comparison to the Future Research section (Section 5.4, page 27, paragraph 3) as a direction we explicitly recommend for follow-up work. We frame it as a research question (what is unique about LLM-based augmentation vs. other AI augmentation forms?) that would justify a dedicated study.

We hope this approach addresses the spirit of the reviewer's concern while maintaining the focused scope of the current paper.

**Manuscript change:** Future Research section page 27, paragraph 3.

---

## 6. Pure-Theory Paper — Engagement with Empirical Tests

**Comment R1.6 (for a pure-theory paper):** *The framework is interesting but largely descriptive. What testable predictions does it generate that would distinguish it empirically from prior architectural theories?*

**Response:** We thank Reviewer 1 for pressing us to make the framework's predictive power more explicit. In the revision, we have added a new subsection 6.2 (page 19-20) titled "Testable Predictions and Future Empirical Work" that lists six specific predictions distinguishing our discriminating-alignment framework from prior architectural theories:

1. Under high environmental dynamism, firm-controlled platforms will outperform shared-governance platforms on speed of market entry but underperform on capability range.
2. Under high systemic uncertainty, shared-governance platforms will outperform firm-controlled platforms on coordination scope, leading to broader complementor participation.
3. Hub-and-spoke alliance networks will be more common in industries with intermediate levels of demand heterogeneity.
4. Symmetric populations ecosystems will emerge primarily in mature industries with stable interfaces and low autonomous-adaptation needs.
5. Architectural transitions over time will follow the pathways predicted by parameter shifts in environmental dynamism and systemic uncertainty (e.g., trajectories A, B, C in Figure 4).
6. The architectural trilemma should be detectable in cross-industry data: industries with multiple architectures should show clustering on at most two of the three adaptation attributes.

Each prediction is operationalized with a sketch of the relevant variables and a research design that would test it. We hope this addition demonstrates that the framework is generative rather than descriptive.

**Manuscript change:** New subsection 6.2 (pages 19-20); Figure 4 (page 20).
