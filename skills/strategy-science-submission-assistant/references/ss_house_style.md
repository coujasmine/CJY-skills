---
file: ss_house_style.md
purpose: Strategy Science (INFORMS) house style — voice, sentence-level norms, citation conventions, formatting idioms. Used in POLISH Stage 7 and SECTION rewrites.
last_verified: 2026-05-21
---

# Strategy Science House Style

## Contents

- Voice
- Citation style (INFORMS)
- Hypothesis labeling
- Mathematical notation
- Tables
- Figures
- Footnotes vs. Endnotes
- Sentence-level patterns
- Section-heading style
- Length and proportionality
- Section-opening idioms
- Acknowledgments idioms


Calibrated against 4 published SS articles (Asghar et al.; Kanis, Mann & Stumpf-Wollersheim 2026; Qu, Kumar & Tong 2026; Clough 2026). The patterns below are observed regularities, not ad-hoc rules.

---

## Voice

### Empirical papers (Kanis, Qu, Asghar)

- **First-person plural ("we")** is standard. "We investigate", "we hypothesize", "we find", "we conduct."
- "We" is acceptable in single-author papers when reporting standard scientific work, though Clough (single author) uses "I" throughout. Both are acceptable; consistency within paper matters.
- Past tense for what the study did ("We tested our hypotheses using..."); present tense for theoretical claims ("Mental representations are simplified models...").
- Restrained tone. Avoid hype words ("revolutionary", "groundbreaking", "unprecedented", "novel" used sparingly). Asghar uses "fresh contributions"; Qu uses "novel measure"; Kanis avoids overclaim altogether.

### Pure-theory papers (Clough)

- **"I"** if single author, **"we"** if multi-author.
- "We propose / I propose / I argue / the framework predicts / the typology identifies."
- Avoid empirical verbs ("we find", "our results show") — these don't belong in a theory paper.
- Use deliberate qualifying language: "to a first approximation", "as a first cut", "with some caveats."

---

## Citation style (INFORMS)

### In-text

- Author-year **without comma**: `(Csaszar 2018)` not `(Csaszar, 2018)`.
- Two authors: `(Gavetti and Levinthal 2000)` — "and", not "&".
- Three+ authors: `(Csaszar et al. 2024b)` — italicize "et al."? Some publishers do; INFORMS does not. Plain "et al." is standard.
- Multiple cites in same parenthesis: separated by comma, ordered by year: `(Csaszar 2018, Gavetti and Menon 2016, Kapoor and Wilde 2023)`. NOT semicolons.
- Page citations: `(Csaszar et al. 2024b, p. 325)` — uses "p." with period and space.
- Suffix on year for same-author same-year: `2024a`, `2024b`. Order by appearance in text.
- Year ranges or "forthcoming": `(El-Zayaty and Ganco forthcoming)`.

### Reference list (INFORMS journal-name abbreviations)

```
Csaszar FA, Laureiro-Martínez D (2018) Individual and organizational
  antecedents of strategic foresight: A representational approach. Strategy
  Sci. 3(3):513–532.

Gavetti G, Levinthal D (2000) Looking forward and looking backward:
  Cognitive and experiential search. Admin. Sci. Quart. 45(1):113–137.

Williamson OE (1991) Comparative economic organization: The analysis of
  discrete structural alternatives. Admin. Sci. Quart. 36(2):269–296.

Adner R (2017) Ecosystem as structure: An actionable construct for strategy.
  J. Management 43(1):39–58.

Cyert RM, March JG (1963) A Behavioral Theory of the Firm, 2nd ed.
  (Wiley-Blackwell, New York).
```

Key conventions:
- Author surnames with initials (no first names spelled out): "Csaszar FA, Laureiro-Martínez D"
- Year in parentheses immediately after authors
- Article title with sentence case (only first word and proper nouns capitalized)
- Journal name abbreviated INFORMS-style and italicized
- Volume(issue):page-page
- Em-dash between page numbers (–), not hyphen (-)
- For books: Title in italic title case, (Publisher, City)

Common INFORMS journal abbreviations:
- Strategy Sci. (Strategy Science)
- Strategic Management J. (Strategic Management Journal)
- Acad. Management J. (Academy of Management Journal)
- Acad. Management Rev. (Academy of Management Review)
- Admin. Sci. Quart. (Administrative Science Quarterly)
- Manage. Sci. (Management Science)
- Organ. Sci. (Organization Science)
- J. Management (Journal of Management)
- J. Management Stud. (Journal of Management Studies)
- Res. Policy (Research Policy)
- Harvard Bus. Rev. (Harvard Business Review)
- J. Financ. Econ. (Journal of Financial Economics)
- J. Finance (Journal of Finance)

---

## Hypothesis labeling

```
**Hypothesis 1a (H1a).** *Managers with greater industry knowledge breadth are
associated with less foresight regarding the performance of product introductions
than those who have narrower industry knowledge breadth.*
```

- Bold: `**Hypothesis 1a (H1a).**`
- Italic body
- Indent or block style; clearly set off from running text
- Use full sentence, period at end
- Sub-letters (1a, 1b, 1c) for sub-hypotheses under a parent prediction

For propositions in theory papers (Clough does not number propositions but states them as numbered theorems or in prose); SS accepts either:

```
**Proposition 1.** *Under conditions of high environmental dynamism, centralized
governance structures outperform decentralized governance structures.*
```

---

## Mathematical notation

- Variables and parameters in math italic: *X*, *β*, *α*
- Vectors in bold: **W**, **x**
- Standard expectation: E[·]
- Use the standardized regression-table format:

```
Net Purchases_ijk = P_ijk + (SA_ijk − SB_ijk)
```

with subscripts in italics, operators in regular weight.

For equations:

```
CAR_{i,t} = ∑_{t=−1}^{1} (R_{i,t} − R̂_{i,t}),    (1)
```

Equation numbers right-aligned in parentheses.

---

## Tables

### Regression tables

- Coefficient first, **standard error in parentheses immediately below**, NOT t-statistic.
- Significance with † p<0.10, * p<0.05, ** p<0.01, *** p<0.001. State one-sided or two-sided in the note.
- Notes below table starting with `*Notes.*` (italic).

```
Variable                Model 1
Predicted CAR           0.707***
                        (0.171)
Public Target           0.003
                        (0.005)
...
N                       2,647
Adjusted R²             0.493

*Notes.* Dependent variable is CAR. Standard errors in parentheses. ***p<0.001;
**p<0.01; *p<0.05; †p<0.10.
```

### Descriptive / correlation tables

- "Table 2. Descriptive Statistics and Correlations Among Key Variables" centered
- All variables numbered (1, 2, 3, ...) on left
- Correlations as lower-triangular matrix
- Mean, SD, Min, Max, N below

### Experimental-design tables

```
Table 1. Experimental Design and Results for Strategic Foresight

                          No LLM              LLM
No time constraints       N = 87              N = 85
                          SF: 62.07%          SF: 65.88%
Time constraints          N = 105             N = 71
                          SF: 54.29%          SF: 64.79%

*Note.* We found no statistically significant differences in strategic foresight
across the experimental conditions.
```

---

## Figures

- "Figure 1. <Descriptive Title>" centered below the figure (some issues place above)
- Notes below figure starting with `*Notes.*` italic
- Letters or symbols defined in notes
- Black-and-white or color (color allowed in online version; check print rules)
- Vector preferred (PDF/EPS) for plots; high-res raster acceptable

---

## Footnotes vs. Endnotes

- **Footnotes**: numbered superscripts within the page; used for substantive asides.
- **Endnotes**: numbered, appear after Acknowledgments and before References. Used at SS for longer methodological clarifications or peripheral notes.
- Both used in practice; Clough uses 17 endnotes; Asghar uses 14+ footnotes; Kanis uses 2 endnotes.

---

## Sentence-level patterns

### Topic-sentence-first paragraphs

SS paragraphs typically open with a theoretical or empirical claim, then justify it. Compare:

❌ "There has been growing interest in AI..." (literature-gap opening — generic)
✓ "Strategic foresight is the ability of managers to predict how their actions will create a competitive advantage (Barney 1986, Ahuja et al. 2005, Gavetti and Menon 2016, Csaszar and Laureiro-Martinez 2018)." (anchored-claim opening — Asghar et al.)

### Theoretical-anchor sentences

Each major theoretical subsection (2.1, 2.2, ...) opens with an anchor citation cluster. Pattern:

✓ "Following the Carnegie tradition of incorporating theories from cognitive science and psychology (see, e.g., Newell and Simon 1972, Simon 1997), the representational approach to strategic decision-making draws on Brunswik's (1952) lens model (Csaszar and Laureiro-Martinez 2018)." (Kanis et al. opening of Theoretical Background)

### Hedging language

SS hedges precisely. Common patterns:

- "may", "can", "is likely to", "tends to" — soft claims
- "the framework predicts", "the theory implies", "consistent with" — theory-paper claims
- "we suggest", "we propose" — claim-introduction
- "additional analyses indicate" / "additional analyses suggest" — mechanism explanations (Kanis idiom)
- "tentative evidence that..." — secondary findings (Asghar idiom)

### Avoid

- Hype words: "groundbreaking", "revolutionary", "paradigm-shifting", "unprecedented", "first ever", "remarkable"
- Vague intensifiers: "very", "really", "highly important", "extremely"
- Verbal nouns when verbs work: "the utilization of" → "using"
- "The fact that" → just delete it
- Redundant qualifiers: "completely unique", "totally novel"

---

## Section-heading style

```
1. Introduction

2. Theory and Hypotheses

2.1. Human Capital and Knowledge Breadth

2.2. Strategic Foresight and Its Antecedents

2.3. Stock Purchases Ahead of Product Introduction Announcements

2.4. Strategic Foresight Reflected Through Managers' Stock Purchases

2.4.1. Industry Knowledge Breadth and Strategic Foresight.

2.4.2. Firm Knowledge Breadth and Strategic Foresight.

2.5. Financial Market Volatility and Strategic Foresight

3. Sample and Methods

3.1. Dependent Variable

3.2. Independent Variables

3.3. Control Variables

3.4 Econometric Model

4. Results

5. Discussion and Conclusion

5.1. Overview

5.2. Theoretical Implications

5.3. Managerial Implications

5.4. Limitations and Future Research
```

Conventions:
- Period after section number (`2.` not `2`)
- Section title in title case
- Sub-sub-sections (2.4.1) often appear inline with a period and bold (`2.4.1. Industry Knowledge Breadth and Strategic Foresight.`)
- For theory papers (Clough): `4. From Governance Structures to Ideal-Type Ecosystem Architectures` — title-case, no period at end

---

## Length and proportionality

Official submission constraint: the assembled manuscript should not exceed 35 pages all-inclusive, including title page, abstract, reference list, figures, and tables. A paper above the limit needs an explicit cover-letter explanation and should be treated as a format risk before review.

Approximate targets under the 35-page all-inclusive cap:

- Introduction: 3-5 pages
- Theory & Hypotheses: 6-10 pages
- Methods: 3-6 pages (empirical), 0-2 pages (pure theory)
- Results: 3-6 pages (empirical), N/A (pure theory)
- Discussion: 3-5 pages
- References, tables, and figures must be budgeted into the same 35-page limit; move extensive robustness checks, derivations, stimuli, and coding details to online supplements when allowed.

Published articles may appear longer after production formatting. For submission QA, enforce the official guide rather than article-PDF length.

---

## Section-opening idioms

### Introduction opening
- Start with the strategic problem or theoretical tension (NOT a literature gap)
- Examples:
  - "Strategic foresight is the ability of managers to predict..." (Asghar)
  - "Because of rapid environmental changes, managers must often make strategic decisions under time constraints..." (Kanis)
  - "In recent years, the rise of artificial intelligence (AI) has sparked growing interest..." (Qu)
  - "A large and growing share of economic activity takes place in innovation ecosystems..." (Clough)

### Theory section opening
- Start with the named primary lineage and anchor citations
- Example: "Following the Carnegie tradition of incorporating theories from cognitive science and psychology (see, e.g., Newell and Simon 1972, Simon 1997), the representational approach to strategic decision-making..." (Kanis)

### Method section opening
- Start with the sample, the setting, the time window
- Example: "We tested our hypotheses using a sample of public companies listed in the S&P 500 that made product introduction announcements between 2016 and 2018..." (Asghar)

### Discussion section opening
- Start with a one-paragraph overview of what was done and found
- Example: "We investigated the role of predictions in acquisition decision making using a set of propositions grounded in behavioral decision-making theory..." (Qu)

---

## Acknowledgments idioms

```
The authors thank the anonymous reviewers and the Editor, Felipe Csaszar, for
the highly constructive comments and suggestions that we received in the review
process. The authors are also grateful to the participants of the 2025 CSOL
Conference who shared valuable thoughts, especially on the framing of this study.
This study received approval from the institutional review board of the TU
Bergakademie Freiberg (Project ID: 2024-08). We preregistered our study at
https://aspredicted.org/fvq9-7kty.pdf.
```

Pattern:
- Specifically name the editor (if known)
- Thank anonymous reviewers
- Name conference/seminar audiences
- Name specific colleagues by name (no honorifics)
- IRB approval reference (institution + project ID)
- Pre-registration link (after acceptance only; anonymized during review)
- Funding source

For double-anonymous review, **strip everything that identifies authors** and place it in a separate Title Page document.
