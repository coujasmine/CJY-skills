---
file: full_intro_before_after.md
purpose: One complete introduction (six paragraphs) rewritten end-to-end with line-level annotation. Used in POLISH and SECTION modes when the user requests an introduction rewrite, or as a worked example of the section-rewrite playbook.
last_verified: 2026-05-17
---

# Full Introduction Rewrite — Worked Example

This is an end-to-end before/after rewrite of a full introduction, applying every move in `references/jbr_section_rewrite_playbook.md` §2. The substantive content (AI capability building → managerial temporal myopia) is illustrative; do not reuse the AFTER text. Reuse the **structural moves** and the **annotation rationale**.

---

## BEFORE (1,180 words; reads like a literature review pretending to be an intro)

**Paragraph 1.** With the rapid development of artificial intelligence (AI) technologies, AI has been widely adopted in various industries and has attracted significant attention from both academia and practice. Many studies have explored the role of AI in firms (Brynjolfsson & McAfee, 2017; Wamba-Taguimdje et al., 2020). Despite the importance of this topic, the literature on AI and managerial decision-making remains underdeveloped.

**Paragraph 2.** Managerial myopia, also known as short-termism, refers to the tendency of managers to overweight short-term outcomes at the expense of long-term value creation. This phenomenon has been studied extensively in finance and strategy (Stein, 1989; Souder & Bromiley, 2012; Marginson & McAulay, 2008). Various antecedents have been proposed, including incentive structures, ownership types, information asymmetry, and analyst coverage. However, technology-based antecedents have not been examined.

**Paragraph 3.** AI may affect managerial myopia through several channels. First, AI provides better information processing capabilities. Second, AI can automate routine decisions, freeing up cognitive resources. Third, AI changes organizational attention structures. Despite these possibilities, no prior study has empirically examined whether and how AI affects managerial myopia. This study aims to fill this gap.

**Paragraph 4.** Using data from Chinese listed firms during 2014–2024, we examine the impact of AI on managerial temporal myopia. We construct a novel measure of AI capability based on firm recruitment text. We control for firm size, leverage, age, and other firm characteristics. We use firm and year fixed effects.

**Paragraph 5.** Our results show that AI causes a significant reduction in managerial myopia. We also find that this effect is moderated by short-horizon incentives, data infrastructure, and industry competition. These results are robust to various alternative specifications and a shift-share IV identification strategy.

**Paragraph 6.** This study makes several important contributions. First, we contribute to the literature on AI by showing that AI matters for managerial decision-making. Second, we contribute to the literature on managerial myopia by introducing a technological antecedent. Third, we extend the attention-based view. Fourth, our findings have important implications for managers, policymakers, regulators, and other stakeholders concerned about the long-term performance of firms in the age of AI.

---

## Diagnosis (before the rewrite)

Running the BEFORE through `references/jbr_desk_reject_triggers.md`:

- **D1** (RQ not visible by page 2): RQ is buried — paragraph 3 says "examine whether and how" but never poses a clear question
- **D2** (literature-gap opening): Paragraph 1 opens with "rapid development of AI" — phenomenon framing without tension
- **D3** (no primary theory in intro): Three potential theories implied (information processing, cognitive resource, attention-based view); none named as primary until contribution paragraph
- **D4** (no mechanism): Paragraph 3 lists three channels in one sentence each; no mechanism developed
- **D5** (vague contribution): Paragraph 6 has four bullets, all generic ("matters for," "introducing," "extends")
- **E1** (causal language on panel data): "AI causes" in paragraph 5 — panel FE supports association, not causation
- **F3** ("first paper to" claim): "no prior study has empirically examined" without supporting evidence

**Top 3 priorities for the rewrite**:
1. Replace literature-gap opening with business-tension opening
2. Name attention-based view as primary; develop the attention-infrastructure mechanism
3. Calibrate "causes" → "is associated with" + sharpen contribution paragraph

---

## AFTER (1,210 words; six-paragraph JBR-calibrated intro)

**Paragraph 1 — Phenomenon paragraph.**
Top managers at large firms increasingly face a temporal trade-off: pressure from quarterly earnings calls and short-term performance metrics pulls strategic attention toward the immediate, while the structural shifts required by digitalization demand a multi-year planning horizon. The mismatch is visible in firm behavior. Cisco's 2023 annual report describes the firm's reallocation of half of its R&D budget toward AI-related projects with payback horizons of five-plus years (Cisco Systems, 2023), while a recent survey of 1,500 Chinese listed-firm executives finds that 62% report being "constrained by short-term performance pressure even when long-term opportunities are visible" ([CITATION NEEDED: source for this survey statistic — provided by user]). Why some firms appear able to extend their managers' temporal attention while others remain trapped in short-termism remains unclear.

**Paragraph 2 — Tension paragraph.**
The attention-based view of the firm (Ocasio, 1997) treats managerial attention as a scarce organizational resource shaped by the firm's structure, situated contexts, and procedural channels. Within this lens, managerial temporal myopia is not simply a behavioral trait of individuals but a structural property of how attention is distributed across organizational time horizons. Prior empirical work has identified incentive structures, ownership types, and information environments as antecedents of myopia (Stein, 1989; Souder & Bromiley, 2012). What remains theoretically and empirically open is whether and how **technological infrastructure** — specifically the AI capabilities that firms build for forward-looking discovery, as distinct from AI used for backward-looking automation — reshapes the structural distribution of attention that the attention-based view identifies as central. This gap matters because the mechanism through which an organization extends its managers' planning horizons is the locus of any potential intervention.

**Paragraph 3 — Research question + theory + supporting theories.**
We pose a focused research question: **does discovery-oriented AI capability building reduce managerial temporal myopia, and through what attentional pathway?** We answer it through the attention-based view as our primary theoretical lens, drawing on the exploration–exploitation distinction (March, 1991) as an auxiliary frame to define "discovery-oriented" as distinct from automation-oriented AI activity. Our central proposition is that discovery-oriented AI capability building functions as an *attention-infrastructure*: it reshapes the procedural channels through which long-horizon information reaches top management, alters the situated contexts in which strategic deliberation occurs, and broadens the focus of attention away from short-term cues. Three boundary conditions follow from the structural logic: the effect should weaken when CEOs face short-horizon equity-vesting incentives that bias attention toward the near term; it should strengthen when the firm's data infrastructure provides the information capacity for the AI's attention-redirection effect to operate; and it should strengthen under industry competition that increases the marginal value of longer planning horizons.

**Paragraph 4 — Study design.**
We test the proposition using panel data on 2,100 Chinese A-share listed firms from 2014 to 2024 — a setting in which both AI investment and short-term performance pressure are documented to be intense, and in which firm-year-level disclosure provides comparable measures of managerial temporal orientation. We construct a sentence-level measure of *discovery-oriented* AI capability building from firm recruitment texts, applying the Wang & Wu (2024) co-occurrence approach to identify postings that combine AI-related skills with discovery-oriented job content. We measure managerial temporal myopia using a 57-term purified dictionary applied to the MD&A section of annual reports, following [CITATION NEEDED: dictionary source]. The empirical strategy combines progressive fixed-effects panel regressions with a shift-share instrumental variables design that uses regional supply of AI talent to address remaining endogeneity concerns.

**Paragraph 5 — Findings preview.**
We find that discovery-oriented AI capability building is negatively associated with managerial temporal myopia, with the association robust to firm fixed effects, year fixed effects, industry-by-year fixed effects, and a shift-share IV specification. The association is weaker when CEOs face concentrated short-horizon equity vesting, stronger when firms have well-developed data infrastructure, and stronger under high industry competition — three boundary patterns consistent with the attention-infrastructure mechanism. In downstream analyses, the reduction in myopia is associated with subsequent increases in the firm's exploratory patent count (lagged two years), suggesting that the attention shift translates into observable longer-horizon innovation activity.

**Paragraph 6 — Contribution paragraph.**
This study contributes to the attention-based view (Ocasio, 1997) by specifying an *attention-infrastructure* mechanism that links technological capability building to managers' temporal orientation. Prior research on managerial myopia has identified incentive and ownership antecedents (Stein, 1989; Souder & Bromiley, 2012); we add an organizational-structural antecedent that operates through the attentional pathway the theory specifies — bringing the technology question inside the theory rather than alongside it. The contribution is not that AI affects firm outcomes, but that discovery-oriented AI capability building affects managerial attention *through* a measurable infrastructure that firms can design, audit, and manage. For managers seeking to extend their planning horizons, the practical implication is operational: build AI capabilities for forward-looking discovery, ensure the data infrastructure that lets those capabilities reach top management, and avoid bundling them with short-horizon incentive structures that pull attention back toward the immediate.

---

## ANNOTATION (paragraph-by-paragraph)

### Paragraph 1 (phenomenon)

| Change | Why |
|---|---|
| Replaced "With the rapid development of AI" with a temporal trade-off framing | Opens with business tension, not technology hype (`jbr_house_style.md` §10) |
| Added Cisco 2023 R&D reallocation example | Firm-specific evidence makes the phenomenon real; satisfies `jbr_section_rewrite_playbook.md` §2 "business example by page 1" |
| Used `[CITATION NEEDED]` for the 62% survey statistic | Hard Rule 1 — do not invent a citation. User must supply the source. |
| Closed paragraph with "remains unclear" rather than "has not been studied" | Tension framing, not gap-counting framing |

### Paragraph 2 (tension)

| Change | Why |
|---|---|
| Named the attention-based view (Ocasio, 1997) explicitly | Hard rule: primary theory by page 2 (`jbr_section_rewrite_playbook.md` §2 / desk-reject trigger D3) |
| Reframed myopia as a structural property, not a behavioral trait | Sets up the contribution: technology can reshape structure |
| Distinguished discovery-oriented AI from automation AI in bold | Pre-empts the construct contamination reviewer comment |
| Closed with "the mechanism is the locus of any potential intervention" | Makes the practical relevance explicit without leaving the theoretical lane |

### Paragraph 3 (RQ + theory)

| Change | Why |
|---|---|
| Posed the RQ in bold, two-part form: existence + mechanism | RQ explicit, no longer buried |
| Named attention-based view as primary; March 1991 as auxiliary | Avoids the three-theory salad that the BEFORE implicitly carried |
| Developed the mechanism in three concrete operations (channels, contexts, focus) | Mechanism sentence per `jbr_section_rewrite_playbook.md` §3 |
| Stated three boundary conditions with directional logic | Pre-empts the "you just added moderators" reviewer comment |

### Paragraph 4 (design)

| Change | Why |
|---|---|
| Replaced "Using data from Chinese listed firms" with "2,100 Chinese A-share listed firms 2014–2024" | Replication-sufficient detail |
| Added rationale for the setting (both AI investment and short-term pressure intense) | Setting must be theoretically informative, not convenient (desk-reject trigger A3) |
| Specified the construct measurement approach with citation to Wang & Wu (2024) | Concrete operationalization, not vague "novel measure" |
| Flagged `[CITATION NEEDED]` for the dictionary source | Hard Rule 1 |
| Named the shift-share IV strategy explicitly | Signals identification awareness |

### Paragraph 5 (findings preview)

| Change | Why |
|---|---|
| Replaced "AI causes a significant reduction" with "is negatively associated with" | Panel FE row in `jbr_claim_evidence_matrix.md` — no causal claim from FE alone |
| Listed all four FE specifications + IV | Signals robustness depth without listing every table |
| Reported the three boundary patterns as consistent with the mechanism | Ties findings to the mechanism, not just to moderators |
| Added the downstream exploratory-patent finding | Strengthens the contribution claim that attention shift has consequences |

### Paragraph 6 (contribution)

| Change | Why |
|---|---|
| Cut the four-bullet list | JBR rewards one specific theoretical movement |
| Named the specific theoretical movement (mechanism specification) | Per `examples/contribution_statement_examples.md` Example 1 |
| Distinguished from prior incentive/ownership work explicitly | Shows what is added, not just that something is added |
| "Bringing the technology question inside the theory rather than alongside it" | Pre-empts the "you just correlate AI with another variable" reviewer comment |
| Tied the practical implication to the mechanism (build → ensure infrastructure → avoid bundling) | Specific managerial actions, not generic stakeholder hand-wave |

---

## Quality score (BEFORE vs. AFTER)

| Sub-score | BEFORE | AFTER |
|---|---|---|
| Theory coherence (out of 25) | 8 | 22 |
| Method-claim alignment | 6 | 23 |
| Contribution clarity | 5 | 22 |
| JBR fit & format | 9 | 21 |
| **TOTAL (out of 100)** | **28** | **88** |

A BEFORE intro at 28/100 would be a high-risk desk-reject. The AFTER at 88/100 is in the "submission-ready" band per `SKILL.md` quality score thresholds.

---

## Outstanding flags for the user

- `[CITATION NEEDED]`: 62% short-term-pressure survey statistic in paragraph 1
- `[CITATION NEEDED]`: temporal myopia dictionary source in paragraph 4
- `[CONFIRM]`: Wang & Wu (2024) citation — verify the year and exact attribution before submission
- `[CONFIRM]`: Cisco 2023 annual report claim — verify the exact figure ("half of R&D toward AI")
- `[CONFIRM]`: the downstream patent finding in paragraph 5 — present in the user's manuscript? If only in robustness, soften the claim

These flags must be cleared by the user before the manuscript is sent.
