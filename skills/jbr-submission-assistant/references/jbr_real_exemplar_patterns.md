---
file: jbr_real_exemplar_patterns.md
purpose: >
  Pattern catalog extracted from five recent JBR articles (2024–2025), spanning
  international business, M&A/innovation, RBV-resilience, AI-workplace, and
  innovation/NPD. Used for outlet calibration in POLISH and SECTION modes.
  Patterns are observations from real published papers, paraphrased — the cited
  papers are the authority. Do not reuse the wording; reuse the structural moves.
last_verified: 2026-05-17
supersedes: jbr_exemplar_patterns_2025_ai.md (this file folds in P4 and P5, and adds P1, P2, P3)
copyright: All pattern descriptions are paraphrased; no quotation exceeds 15 words; full citations enable verification.
---

# JBR Real-Exemplar Pattern Catalog

This file extracts observable structural patterns from five recent JBR articles. Use these patterns to calibrate the polish output to JBR's editorial register. Each pattern carries a paper tag (`[P1]–[P5]`) for verification. **Do not quote the source papers at length.** Refer the user to the original article for full text.

The roster below intentionally covers method × topic diversity so that polishing advice is not over-fit to any single paper or domain.

---

## Contents

- **Source paper roster** — the five tagged JBR articles [P1]–[P5]
- **Section 1 — Introduction patterns** (Patterns 1.1–1.4)
- **Section 2 — Theoretical framework patterns** (Patterns 2.1–2.3)
- **Section 3 — Hypothesis statement patterns** (Patterns 3.1–3.3)
- **Section 4 — Method section patterns** (Patterns 4.1–4.4)
- **Section 5 — Results section patterns** (Patterns 5.1–5.4)
- **Section 6 — Discussion section patterns** (Patterns 6.1–6.5)
- **Section 7 — Disclosure patterns** (Patterns 7.1–7.4)
- **Section 8 — Cross-method synthesis** — which paper to use as a model for each design
- **Section 9 — Cross-paper structural commonalities** — the 20-invariant "JBR shape" checklist
- **How this file is used** — per-mode loading guidance

When polishing or auditing a specific section, jump to the matching Section above; for a structural audit, go straight to Section 9.

---

## Source paper roster

| Tag | Citation | Method tier | Topic |
|---|---|---|---|
| **P1** | Jiang, F., Liu, L. X., & Li, J. (2025). Headquarters–subsidiary exchanges and relationship quality: Moderating roles of subsidiary establishment mode and managers' identity with the subsidiary. *Journal of Business Research*, *200*, 115622. | Cross-sectional survey, two-stage data collection from 312 HQ–Sub dyads (Chinese MNEs); hierarchical moderated regression. | International business / MNE management |
| **P2** | Verginer, L., & Riccaboni, M. (2025). The impact of biotech acquisitions on inventor productivity. *Journal of Business Research*, *200*, 115573. | **Staggered Difference-in-Differences** on 1,375 biotech acquisitions, 15,318 inventors, 1990–2010; parallel-trends test reported. | M&A / R&D productivity / innovation |
| **P3** | Ran, R., Zhang, J., Yang, X., & Chen, Y. (2024). Can technological diversity drive firm resilience? Evidence from Chinese listed firms. *Journal of Business Research*, *183*, 114852. | Panel data 2009–2021 on 19,413 Chinese listed firm-years; multi-FE; mediation (Baron-Kenny + bootstrap); IV robustness with Kleibergen-Paap. | Strategy / resource-based view / resilience |
| **P4** | Valtonen, A., Saunila, M., Ukko, J., Treves, L., & Ritala, P. (2025). AI and employee wellbeing in the workplace: An empirical study. *Journal of Business Research*, *199*, 115584. | Cross-sectional telephone survey of 207 Finnish firms; SEM with CFA validity tests; reports a *null* direct effect honestly. | AI / organizational behavior / wellbeing |
| **P5** | Kyriakopoulos, N., Kim, E., Hultink, E. J., & Santema, S. (2025). The impact of design thinking and artificial intelligence capabilities on performance: The role of new product development decision-making agility. *Journal of Business Research*, *200*, 115633. | Online survey of 230 U.S. NPD-active firms; PLS-SEM with formative and reflective constructs; Johnson-Neyman floodlight. | Innovation / NPD / design thinking + AI capabilities |

---

## Section 1 — Introduction patterns

### Pattern 1.1 — Open from phenomenon-and-tension, not from "few studies"

JBR introductions reliably open from a phenomenon plus an unresolved theoretical or practical tension. The literature-gap-as-opener pattern is absent in all five papers.

- **[P2]** opens with named acquirers (Microsoft, Roche, Google) using "acqui-hires" to absorb knowledge — concrete, contemporary, and immediately recognizable as a business decision; the theoretical puzzle follows.
- **[P5]** opens with the transience of competitive advantage in dynamic markets and named firm examples (Procter & Gamble, Infosys, BMW Group), then pivots to the unresolved theoretical question of how design thinking and AI capabilities translate into NPD performance.
- **[P4]** opens with the Industry 5.0 framing and the rapid expansion of generative and emotional AI — naming Walmart's "performance metric" bracelet and Amazon's Halo as concrete workplace AI applications.
- **[P1]** opens from the practitioner-relevant claim that HQ-Sub management is a long-recognized core MNE challenge, signaling the conversation rather than counting prior studies.
- **[P3]** opens with the macro tension of COVID-era volatility, supply chain shocks, and the Accenture survey statistic (3.6% revenue outperformance by resilient firms) before zooming to the theoretical gap.

**Polish rule:** Replace any "Little is known about…" / "Few studies have examined…" opener with one of three patterns: a firm-named example, a market dynamic, or a policy/regulatory tension.

### Pattern 1.2 — Theoretical conversation named by intro paragraph 2 or 3

All five papers name the primary theoretical lens early — typically the second or third intro paragraph.

- **[P1]** names "social exchange theory" and "social identity theory" by intro p. 2; supporting theories (transaction cost, agency, institutional, resource-based) are listed as alternatives explicitly rejected as insufficient.
- **[P2]** names the Knowledge-Based View (KBV) by intro p. 2.
- **[P3]** names the Resource-Based View (RBV) by intro p. 2; intangible-resource subtyping (people-dependent vs. people-independent) is the theoretical move.
- **[P4]** names Job Demands-Resources (JD-R) theory by intro p. 2.
- **[P5]** names dynamic capabilities by intro p. 2.

**Polish rule:** If the user's intro does not name a primary theory by page 2, this is a desk-reject risk (`jbr_desk_reject_triggers.md` D3). Insert the lens early; treat auxiliary theories as explicitly auxiliary.

### Pattern 1.3 — Research question stated explicitly, not implied

All five papers state RQs in plain question form within the intro.

- **[P1]** poses two numbered questions: (1) how managerial exchanges affect HQ-Sub relationship quality moderated by manager identity, and (2) how organizational exchanges affect HQ-Sub relationship quality moderated by establishment mode. Plain prose; both visible by intro p. 3.
- **[P5]** poses two RQs: (a) the through-what-mechanism question, (b) the under-what-structural-condition question.
- **[P4]** poses one RQ at intro p. 2: how AI adoption in the workplace affects employee wellbeing.

**Polish rule:** Always surface the RQ in a self-contained sentence within the intro. Avoid burying it inside a paragraph that also lists contributions.

### Pattern 1.4 — Contribution paragraph names three claims, each tied to a specific literature

All five papers' intros close with a contribution paragraph that names a small number (usually three) of specific theoretical movements, each anchored to a named literature stream.

- **[P1]** intro contribution: (i) HQ-Sub relationship literature via informal mechanisms; (ii) integration of social exchange + social identity into a contingency framework extending Flynn (2005); (iii) cross-level theoretical development (individual + organizational interactions).
- **[P3]** intro contribution: (i) clarify the value of technological resources for resilience (broadens intangible-resource lens); (ii) explore moderating mechanisms of people-dependent intangible resources; (iii) practical contributions for development strategy + financial budget management.
- **[P5]** intro contribution: (i) recast design thinking as organizational-level dynamic capability; (ii) position AI capabilities as tech-driven innovation enablers; (iii) treat NPD-DM agility as the conversion mediator.

**Polish rule:** Replace any "we enrich the literature" / "we contribute to research on X" with one specific theoretical movement per bullet. Use the six contribution moves directly: mechanism, boundary, integration, reconciliation, contextualization, and clarification. Do not point to the removed synthetic examples; infer the move from the user's theory, evidence, and target JBR conversation.

---

## Section 2 — Theoretical framework patterns

### Pattern 2.1 — Primary + auxiliary theory with explicit division of labor

JBR integration papers do not run parallel theories; they assign distinct roles.

- **[P1]** uses social exchange theory for the relational/transactional logic and social identity theory for in-group/out-group attachment — explicitly different roles in the same framework. Notably, the intro contains a hinge sentence asking whether social exchange theory *alone* is sufficient, then answers no and brings in social identity.
- **[P5]** uses dynamic capabilities as the *primary* lens for capability-to-performance conversion and structural alignment perspective as the *boundary* lens for organizational formalization — different theories play different roles.

**Polish rule:** When the manuscript uses two theories, force the writer to name what each theory *does* in the argument. "We integrate X and Y" is not enough; "X explains [path A], Y explains [path B]" is what JBR rewards.

### Pattern 2.2 — Construct definitions precede measures (and the measure echoes the definition)

All five papers define focal constructs in the theoretical framework section, before any measure is named.

- **[P1]** defines organizational exchange ("the degree or level of information exchanges between HQ and Subs… coordination between them") and managerial exchange ("the quality of the social exchange relations… mutual interpersonal-level trust, commitment, confidence") before the measurement section. The 5-item information-exchange scale and 11-item managerial-exchange scale then map back to these definitions.
- **[P3]** defines technological diversity (degree of diversification of the technological base accumulated through long-term cumulative learning) before the entropy-index operationalization.
- **[P5]** defines AI capabilities (organization's integration of cognitive computing, custom data analytics, ML, interactive dashboards within organizational processes) before the four-item scale.

**Polish rule:** If the manuscript introduces a measure before the construct it measures, swap the order. The reader needs to know *what* is being measured before *how* it is measured.

### Pattern 2.3 — Counter-arguments addressed inside the hypothesis development, not buried

JBR papers acknowledge competing predictions where they exist, then resolve them.

- **[P1]** acknowledges that the agency-theory tradition predicts goal incongruence and conflict, which would harm relationship quality — then argues that the social-exchange/identity lens predicts the opposite under specified conditions.
- **[P3]** acknowledges that political connections may have positive effects (subsidies, preferential treatment) before arguing the negative-moderation prediction (resource diversion, distorted allocations).

**Polish rule:** Every counter-prediction worth a reviewer's time should be addressed in the hypothesis development paragraph, not in the limitations.

---

## Section 3 — Hypothesis statement patterns

### Pattern 3.1 — Direction is explicit; mechanism is named in the preceding paragraph

All five papers state directional hypotheses preceded by a mechanism sentence.

- **[P1] H1:** *HQ-sub organizational exchange is positively associated with HQ-Sub relationship quality.* The preceding paragraph argues the mechanism through three named channels (cooperation/coordination from increased exchange, ideological alignment, information-asymmetry reduction).
- **[P2] H1.1 / H1.2:** Paired hypotheses (turnover increase; productivity decline) with explicit pre-paragraph mechanism (acquisitions disrupt tacit-knowledge networks → inventor exit → productivity loss for remaining inventors).
- **[P3] H1:** *Technological diversity has a positive effect on firm resilience.* The mechanism is developed across the absorptive path (redundancy / cost-benefit balance) and adaptive path (resourcefulness / reallocation).

**Polish rule:** Each hypothesis sentence states **direction**; the preceding paragraph(s) name the **mechanism**. If your hypothesis says "X is associated with Y" without a mechanism in the prior paragraph, the hypothesis is decorative.

### Pattern 3.2 — Moderation hypotheses specify the direction of the contingency, not just its existence

- **[P1] H3:** Greenfield *weakens*, M&A *strengthens* — directional contingency, not just "establishment mode moderates."
- **[P5] H5 / H6:** Organizational formalization *attenuates* the design thinking → agility link but *strengthens* the AI → agility link — **opposite-sign moderation across two capabilities**, which generates the paper's theoretical bite. This pattern is rewarded by JBR reviewers because it shows the moderation is structural, not generic.

**Polish rule:** Avoid "X moderates the Y–Z relationship" as a hypothesis form. State *how* (stronger/weaker, positive/negative shift) and *why* (the structural or contextual mechanism behind the moderation).

### Pattern 3.3 — Mediation hypotheses follow Baron-Kenny or PROCESS, paired with bootstrap

- **[P3]** mediates via three parallel mediators (product / customer / market diversity); bootstrap for indirect effects following Preacher & Hayes (2008).
- **[P5]** uses PLS-SEM-internal indirect-effect testing with bias-corrected confidence intervals (BCCI).
- **[P4]** uses SEM with explicit indirect-effect paths; the *direct effect is null* and is reported as such — the contribution comes from the indirect path.

**Polish rule:** Always report indirect-effect confidence intervals (bootstrap-based), not just sign-and-significance.

---

## Section 4 — Method section patterns

### Pattern 4.1 — Setting-rationale paragraph ties the empirical context to the theoretical mechanism

- **[P1]** justifies the Chinese-MNE setting on three grounds: institutional environment with strong informal-mechanism reliance; current global presence of Chinese MNEs; relational-mechanism prominence in the Chinese cultural context. Setting is theoretically informative, not convenient.
- **[P2]** justifies the biotech-acquisition setting: knowledge-intensive industry, large M&A wave 1990–2010, individual-inventor traceability via patents.
- **[P4]** justifies the Finnish sample: Finland ranks third globally in AI development intensity (Global AI Index 2024); strong work-life balance focus enables observing AI–wellbeing interactions cleanly.

**Polish rule:** Replace "We collected data from [country/industry]" with a paragraph explaining *why* this setting reveals the theoretical mechanism.

### Pattern 4.2 — Two-stage / multi-source data collection used to address CMV

- **[P1]** collects DV from HQ managers and IV+moderators from subsidiary managers — separate respondents, separate stages, two weeks apart. This is the procedural CMV remedy.
- **[P4]** keeps procedural remedies (confidentiality, dispersed item placement) plus the latent-method-factor statistical test.
- **[P5]** uses procedural remedies (pretesting, separation, varied anchoring) and statistical remedies (full collinearity test with VIF threshold 3.3; latent marker variable using social desirability scale).

**Polish rule:** For any survey paper, the method section must explain both procedural and statistical CMV remedies. Harman's single-factor test alone is not sufficient.

### Pattern 4.3 — Identification strategy paragraph (for causal claims)

- **[P2]** uses staggered Difference-in-Differences with the Callaway & Sant'Anna (2021) estimator; reports the parallel-trends test (p = 0.35, no evidence of pre-trends); uses not-yet-treated firms as the control group; acknowledges the Heckman correction in a referenced companion paper to address selection.
- **[P3]** uses panel multi-FE for the main test, plus IV regression for robustness (with Kleibergen-Paap LM and Wald F statistics) and propensity-score conditional regression with quadratic generalized propensity scores.

**Polish rule:** Every causal verb in the manuscript needs a defended identification strategy. The discussion language should match the strength of identification — see `jbr_claim_evidence_matrix.md`.

### Pattern 4.4 — PLS-SEM justification triple-check

When PLS-SEM is used, JBR papers explicitly justify it on three grounds.

- **[P5]** justifies PLS-SEM with three reasons: prediction-oriented goal, relatively complex model, presence of formative constructs (Hair et al. 2019).

**Polish rule:** Manuscripts using PLS-SEM without justifying these three (or alternatives) commonly receive reviewer pushback. The CB-SEM vs. PLS-SEM choice should be defended once, briefly, in the method section.

---

## Section 5 — Results section patterns

### Pattern 5.1 — Reporting order: descriptives → correlations → main → robustness

All five papers follow this order without exception.

- **[P1]**: Table 2 (descriptives + correlations) → Table 3 (main HQ-side regressions, Models 1–5) → Table 4 (subsidiary-side robustness, same model structure) → Figures 2 and 3 (simple-slope visualization of moderation).
- **[P3]**: Descriptives → benchmark regression → mediation tests → moderation tests → multiple robustness specifications (Appendix B Tables B.1–B.4).

**Polish rule:** Never present hypothesis tests before descriptives. Reviewers read the descriptive table first to spot suspicious distributions.

### Pattern 5.2 — Effect-size-first reporting, p-values are secondary

- **[P2]** reports magnitudes: +13.5% turnover, +6.3% R&D inactivity, –13.6% patents, –35% citation-weighted patents — substantive units before significance.
- **[P3]** reports β = 0.4642 (t = 11.6720) with R²_yd.x partial = 0.0070 for sensitivity-analysis robustness.
- **[P5]** reports β = 0.17 (p < 0.05) for DT → NPD-DM agility; β = 0.30 (p < 0.001) for AI → NPD-DM agility — coefficient and significance reported together.

**Polish rule:** Replace "significant at p<0.05" used alone with "[coefficient] (p<value)" or "[X-percent shift] (p<value)".

### Pattern 5.3 — Moderation visualized with simple-slope plots; Johnson-Neyman points reported when relevant

- **[P1]** Figures 2 and 3 visualize moderation by establishment mode and manager identity respectively — text reports both the interaction term coefficient and the figure.
- **[P5]** reports Johnson-Neyman points explicitly: formalization values above 6.24 cross the significance threshold for DT → agility; AI → agility becomes significant for formalization values above 5.02.

**Polish rule:** Moderation reported only as an interaction-term coefficient is incomplete. Add (a) a simple-slope plot, (b) the J-N range or critical points where relevant.

### Pattern 5.4 — Nulls reported as findings, not buried

- **[P4]** finds AI adoption is not directly associated with employee wellbeing (path estimate = −0.111, p = 0.107). The paper does not bury this. Instead, the null is the pivot to the indirect-effect contribution: AI's benefits operate through task optimization and workplace safety. This honesty makes the contribution stronger, not weaker.

**Polish rule:** If the manuscript has a null finding for a hypothesized effect, lead with it and use it to sharpen the mechanism contribution. Burying nulls is a common reviewer-flagged misstep.

---

## Section 6 — Discussion section patterns

### Pattern 6.1 — Structured subsections: Major findings → Theoretical contributions → Practical implications → Limitations and future research → Conclusion

All five papers follow this exact subsection order.

- **[P1]** §6.1 Major findings → §6.2 Theoretical contributions (3 numbered) → §6.3 Managerial implications (3 numbered) → §6.4 Limitations and future research → §6.5 Conclusion. Self-contained subsection headings; reader can navigate by skim.
- **[P3]** identical structure: contribution → moderating-role explanation → practical implications → limitations and future research.

**Polish rule:** Use explicit subsection headings. Reviewers and editors should be able to find each component without re-reading the section.

### Pattern 6.2 — Theoretical contribution paragraphs are numbered and each one names a specific literature

- **[P1] §6.2 contribution 1:** Advances HQ-Sub relationship literature by linking quality to informal mechanisms (relational + legitimacy perspectives), complementing the formal-systems literature (Williamson 1985).
- **[P1] §6.2 contribution 2:** Integrates social exchange and social identity theories' contrasting viewpoints into an integrated framework that extends Flynn (2005).
- **[P1] §6.2 contribution 3:** Cross-level theoretical development — examines individual + organizational interactions simultaneously, extending Flynn (2005) from individual to organizational level.
- **[P2] Theoretical implications paragraph:** Findings resonate with the KBV — competitive advantage from tacit, context-specific knowledge held by individuals, not just codified IP. The contribution is to specify *how* acquisitions can undermine the tacit-knowledge layer.

**Polish rule:** Each theoretical contribution paragraph names a literature, names a specific movement (mechanism / boundary / integration / reconciliation / contextualization / clarification), and ties to the empirical evidence in the paper.

### Pattern 6.3 — Practical implications are specific and mechanism-tied

- **[P1] §6.3:** Three specific implications, each grounded in the findings: (i) the dual nature of relationships (HQ-Sub depends on both organizational and individual exchanges); (ii) MNEs should plan establishment mode carefully — M&A may offer advantages; (iii) subsidiary managers should cultivate dual identity to balance internal/external legitimacy.
- **[P4]** practical-implications paragraph explicitly translates findings into managerial actions: identify tasks where AI benefits employees, communicate AI goals, train employees to mitigate adverse use, audit for over-reliance.
- **[P5]** managerial implications recommend that NPD managers (a) use visualization techniques for complex artefacts, (b) foster experimentation culture with rapid feedback loops, (c) balance structure-vs-flexibility (more structure helps AI capability adoption; less helps DT).

**Polish rule:** Replace generic "managers should consider X" with "managers in [context Y] should [specific action Z] because [mechanism evidenced in the paper]."

### Pattern 6.4 — Limitations are design-bounded, each paired with future-research direction

- **[P1] §6.4:** (i) Perception-based measures can't reflect actual exchange frequency — future research should incorporate objective measures; (ii) establishment mode as proxy for subsidiary identity has limited validity beyond Chinese MNEs — future research should test in other settings; (iii) single-respondent data per organization — future research should use multiple informants.
- **[P2] Future research directions:** Examines team-level dynamics; matched employee-employer datasets; extends to other high-innovation industries; inventor-firm matching for heterogeneity; killer acquisitions for regulatory implications.
- **[P3] §6.4:** (i) Chinese-only sample; (ii) only patent-based diversity measure; (iii) need for broader technology-ecosystem indicator.
- **[P4] §5.3:** Six numbered limitations, each tied to a future-research direction. Notable transparency: "the inability to directly assess non-response bias" is admitted.

**Polish rule:** Every limitation should name a specific design feature and the type of follow-up study that would resolve it. "Future research should use a different method" without naming the method is inadequate.

### Pattern 6.5 — Conclusion paragraph mirrors the opening

- **[P1] §6.5 Conclusion:** Returns to the social-exchange + social-identity integration, restates the contingency framework, and closes on the managerial implication of balancing external/internal legitimacy.
- **[P2] §6 Conclusion:** Returns to the killer-acquisitions framing from the intro, summarizes the empirical contribution, and closes with the regulatory-implication hook.

**Polish rule:** The conclusion should return to the opening business problem. If the conclusion reads like a results restatement rather than an interpretation echoing the intro, rewrite.

---

## Section 7 — Disclosure patterns observed

### Pattern 7.1 — AI-use disclosure paragraph (post-2024 Elsevier requirement)

- **[P4]** includes a clear AI declaration: "During the preparation of this work the authors used ChatGPT to improve the language and readability of the manuscript. After using this tool, the authors reviewed and edited the content as needed and take full responsibility for the content of the published article." (≤15 word fragments paraphrased per copyright policy.)

This is the gold-standard format. Three components: (1) tool name (ChatGPT), (2) specific purpose (language and readability improvement), (3) responsibility statement (authors reviewed and take full responsibility).

**Polish rule:** Every submission going through this skill must add an analogous paragraph. See `jbr_disclosures_2024.md` for the template.

### Pattern 7.2 — CRediT contributor statement is standard, every author appears

- **[P1]** CRediT statement: all three authors named, each assigned multiple roles. First author: Writing-review&editing, Writing-original draft, Supervision, Methodology, Investigation, Funding acquisition, Formal analysis, Data curation, Conceptualization.
- **[P2]** CRediT: both authors share Writing roles and Conceptualization; differentiated by Software, Visualization (first author) vs. Validation (second author).
- **[P5]** CRediT: all five authors assigned roles; senior authors (Hultink, Santema) named with Supervision and Resources.

**Polish rule:** No author should have only one role unless they genuinely contributed to only one thing. Senior authors should carry Supervision.

### Pattern 7.3 — Data availability statement is specific

- **[P1] Data availability:** "The data that has been used is confidential."
- **[P2] Data availability:** Supplementary material linked via DOI to the JBR article.
- **[P3] Data availability:** "The data that support the findings of this study are available from the corresponding author upon reasonable request."
- **[P4] Data statement:** "Authors do not have permission to share data." (Concise, honest.)

**Polish rule:** A DAS is non-optional. Even "data are confidential" is a valid DAS — silence is not.

### Pattern 7.4 — Funding and competing-interest disclosures named explicitly

- **[P4]** funding: "Research was financially supported by Business Finland, project 'SANTTU — To reduce stress from machine & operator'." (Funder + project name.)
- **[P2]** funding: "The authors received no specific funding for this work." (Clear null statement.)
- **[P1] competing interest:** Not explicit in the visible portions; but other papers (P2, P3, P4, P5) all carry "The authors declare no conflict of interest" or equivalent.

**Polish rule:** Both funding and competing-interest statements must appear, even if "none" or "no specific funding." Silence is interpreted as omission.

---

## Section 8 — Cross-method synthesis: when to use which paper as a model

When polishing a user's draft, route to the closest-method exemplar:

| User's design | Closest exemplar | What to learn from it |
|---|---|---|
| Cross-sectional survey, single source | **P5** (PLS-SEM, single survey) | Strict CMV remedies; J-N floodlight for moderation; capability-construct precision |
| Cross-sectional survey, multi-source / dyadic | **P1** (HQ-Sub dyads) | Two-stage data collection; integrated theory contribution structure; figure-based moderation visualization |
| Cross-sectional survey reporting a null direct effect | **P4** (AI–wellbeing) | Honest null reporting; pivot to indirect-effect contribution; explicit AI-use disclosure |
| Panel data, multi-FE | **P3** (tech diversity) | Mediation through multiple parallel paths; IV + propensity-score robustness; appendix-heavy robustness reporting |
| Quasi-causal identification (DiD, IV, RDD) | **P2** (staggered DiD) | Identification-strategy paragraph; parallel-trends test reported; effect-size-first reporting (+13.5%, –35%) |
| Mixed: capability + moderator | **P5** (DT + AI + formalization) | Opposite-sign moderation across two capabilities = theoretical bite |

When the user's manuscript spans methods, use the closest method-tier exemplar for the language of claim-calibration and discussion, but synthesize across all five for the structural moves (intro, hypothesis statements, contribution paragraph format).

---

## Section 9 — Cross-paper structural commonalities (the "JBR shape")

After reading all five papers, these are the **invariants** of JBR-published manuscripts:

1. Intro opens with phenomenon-and-tension, not literature-gap.
2. Primary theory named by intro p. 2.
3. RQ stated explicitly in the intro, in plain question form.
4. Contribution paragraph in the intro names 2–4 specific theoretical movements, each tied to a literature.
5. Construct definitions precede measures.
6. Counter-arguments addressed in hypothesis development, not in limitations.
7. Hypotheses state direction; mechanism is named in the preceding paragraph.
8. Moderation hypotheses specify the direction of the contingency, not just its existence.
9. Method section justifies setting on theoretical grounds.
10. CMV remedies (procedural + statistical) for surveys; identification strategy paragraph for causal claims.
11. Results in order: descriptives → correlations → main → robustness.
12. Effect sizes reported alongside p-values; significance alone is insufficient.
13. Moderation visualized with simple-slope plots; J-N points where relevant.
14. Nulls reported honestly and used to refine the mechanism contribution.
15. Discussion has five subsections: findings → theoretical contributions → practical implications → limitations → conclusion.
16. Each theoretical contribution names a specific literature and a specific movement.
17. Practical implications are mechanism-tied and audience-specific.
18. Limitations are design-bounded; each paired with a future-research direction.
19. Conclusion returns to the opening business problem.
20. Required disclosures: AI use (per Elsevier 2024), CRediT, DAS, conflicts, funding.

When a user's manuscript deviates from one of these 20 invariants, surface the deviation in the POLISH-mode output's "Top 3 priorities" block.

---

## How this file is used

- **POLISH mode**: Load at Stages 5 (section-by-section rewrite) and 6 (house-style pass) of `jbr_polishing_pipeline.md` to anchor the rewrite to observed JBR conventions.
- **SECTION mode**: Load whichever section's patterns apply.
- **AUDIT mode**: Use Section 9 as the 20-invariant checklist for desk-reject + structural-quality scoring, and label the audit level as QUICK, STANDARD, or FULL based on available inputs.
- **REVIEW mode**: Use Section 9 as the structural baseline and Section 8 for closest-method calibration before applying `jbr_reviewer_simulation.md`.
- **PACKAGE mode**: Use Section 7 for disclosure validation alongside `jbr_disclosures_2024.md`.
- **RESPOND mode**: Patterns inform reviewer-response wording when reviewers ask about identification, CMV, or claim calibration.

Citations are provided so the user can verify any pattern by reading the source article. **Never quote the source papers at length when applying these patterns in a polish.**
