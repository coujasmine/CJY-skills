---
file: ss_disclosures.md
purpose: Strategy Science / INFORMS disclosure requirements — AI use, author contributions, data availability, conflicts of interest, IRB, funding. Used in PACKAGE and POLISH Stage 8.
last_verified: 2026-05-21
---

# Strategy Science Disclosure Requirements

## Contents

- 1. AI / LLM use disclosure
- 2. Author contribution statement
- 3. Data Availability Statement (DAS)
- 4. Conflict of Interest (COI) statement
- 5. Funding statement
- 6. Ethics / IRB statement
- 7. Pre-registration
- 8. Open Access (OA) declaration
- 9. Acknowledgments (non-disclosure)
- Disclosure checklist (use in PACKAGE mode)
- Post-acceptance vs. blinded-review differences


INFORMS journals (including Strategy Science) require explicit disclosures across multiple categories. This file lists each, gives template language, and flags when each is required.

> Source: INFORMS PubsOnline policies and observed patterns in published SS articles (2026 issues). Verify the current Author Guide and submission portal before final submission, as INFORMS updates policies periodically.

---

## 1. AI / LLM use disclosure

### When required

ALWAYS, if the manuscript was prepared with any assistance from generative AI tools (including ChatGPT, Claude, Gemini, Mistral, Llama, or domain-specific models).

This includes:
- **Writing assistance**: drafting, editing, language polish, summarization — even partial
- **Measurement / coding**: using LLMs to classify text, code variables, label cases
- **Analysis assistance**: using LLMs to suggest code, interpret outputs, or generate visualizations
- **Idea generation**: using LLMs in literature search, hypothesis brainstorming
- **This skill**: counts as AI assistance and must be disclosed

### Template language (writing assistance only)

> The authors used [model name and version, e.g., "GPT-4 (OpenAI)" or "Claude 3 Sonnet (Anthropic)"] to assist with [specific task, e.g., "language polishing of the introduction and discussion sections"] in [year]. The authors reviewed and edited all AI-generated text and take full responsibility for the content of this manuscript. No AI tools were used to generate research ideas, design the study, conduct analyses, or interpret results.

### Template language (LLM-as-measurement, Kanis-style)

> To classify [construct] in our [experiment / archival text analysis], we used [model names and version pins] with consistency assessed via [metric] and validation against human coders on a subset of [N] items. We document our prompts in Appendix [X] and our validation procedure in Section [X.Y]. We additionally used [model name and version] for language polishing of [sections]; the authors reviewed and edited all AI-assisted text and take full responsibility for the manuscript content.

### Template language (no AI use)

> The authors did not use generative AI tools in the preparation of this manuscript.

### Placement

- In the manuscript: typically at the end of the Methods section, or in an "AI Use Statement" sub-section before Acknowledgments. Some authors place it in Acknowledgments.
- On the submission portal: INFORMS may require a checkbox + free-text statement at submission.
- In the blinded manuscript: include the model details and procedure, but omit anything that identifies the authors.

---

## 2. Author contribution statement

### When required

When there are 2+ authors. INFORMS does not mandate CRediT taxonomy specifically, but expects clear delineation of contributions.

### Template options

**CRediT-style (preferred for clarity):**

> **Author contributions:**
> - **[Name 1]:** Conceptualization, Methodology, Investigation, Formal analysis, Writing — original draft, Writing — review and editing.
> - **[Name 2]:** Conceptualization, Methodology, Investigation, Writing — review and editing.
> - **[Name 3]:** Methodology, Software, Validation, Writing — review and editing.
> - **[Name 4]:** Supervision, Writing — review and editing.

**Equal-contribution statement (Asghar et al. pattern):**

> All authors contributed equally and are listed in alphabetical order.

**Lead-author pattern:**

> [Name 1] led the project, conducted the analyses, and drafted the manuscript. [Name 2] and [Name 3] contributed to the conceptual framework, methodological design, and revisions.

### Placement

- In the blinded manuscript: omit (it would identify authors). Place in Title Page document.
- After acceptance: include in the final published manuscript.

---

## 3. Data Availability Statement (DAS)

### When required

ALWAYS. INFORMS expects an explicit statement even when data are not publicly available.

### Template language options

**Publicly available:**

> The data that support the findings of this study are publicly available. Specifically, [dataset] is available at [URL/DOI]. Analysis code is available at [URL/OSF DOI].

**Available upon request:**

> The data that support the findings of this study are available from the corresponding author upon reasonable request. Restrictions apply to [confidentiality, proprietary terms, etc.].

**Proprietary or restricted:**

> Data used in this study were obtained from [proprietary source, e.g., "Capital IQ Key Developments database", "BoardEx", "Refinitiv"]. The data are not publicly available due to licensing restrictions. Aggregated/derived data are available from the corresponding author upon reasonable request.

**Pre-registered experiment:**

> The pre-registration, study materials, and de-identified data are available at [OSF or aspredicted URL]. Analysis code is available upon request.

### Placement

- In the manuscript, typically at the end of the Methods section or in a dedicated "Data Availability" subsection.
- On the submission portal: INFORMS submission may have a separate data field.

---

## 4. Conflict of Interest (COI) statement

### When required

ALWAYS. Even when there is no conflict, state it explicitly.

### Template language

**No conflict:**

> The authors declare no conflict of interest.

**Disclosed conflict:**

> [Name 1] is a [paid consultant / shareholder / employee] at [Company]. [Name 2] has received [grant / honorarium / equity] from [Source] related to this research. These relationships did not influence the design, conduct, or reporting of this study.

### Placement

- In the manuscript: typically in a "Declarations" section before Acknowledgments.

---

## 5. Funding statement

### When required

ALWAYS. Disclose funding sources, even if none.

### Template language

**Funded:**

> This study received [partial/full] funding from [Source, e.g., "Freunde und Förderer der TU Bergakademie Freiberg e.V., Faculty of Business Administration at the TU Bergakademie Freiberg"]. The funder had no role in the design, conduct, analysis, or reporting of this research.

**Not funded:**

> This study did not receive specific funding.

**Salary-only:**

> This study was supported by the authors' institutional salaries. No external funding was received.

### Placement

- In the blinded manuscript: include but in generic form ("Funding was received from a faculty fund"); do not name the institution.
- After acceptance: include with full institutional names.

---

## 6. Ethics / IRB statement

### When required

When the manuscript involves human or animal subjects:
- Online experiments (Kanis 2026 cites TU Bergakademie Freiberg IRB Project ID 2024-08)
- Survey studies
- Field experiments
- Qualitative interviews
- Archival data with identifiable individuals (unusual but possible)

Pure-archival studies using public databases (Asghar, Qu) typically do not require IRB, but the manuscript should state this.

### Template language

**Approved:**

> This study was approved by the institutional review board (IRB) of [Institution Name] (Approval Number: [XXX-YYYY-ZZ]) on [Date]. All participants provided informed consent.

**Exempt:**

> This study used publicly available [archival / firm-level] data and did not involve human subjects research as defined by [Institution Name]'s IRB; therefore, IRB review was not required.

**Pre-registered:**

> This study was pre-registered at [URL] on [Date], prior to data collection. Hypotheses, design, and analysis plan were specified in the pre-registration.

### Placement

- In the Methods section, typically before or in the Participants subsection.
- In the blinded manuscript: include but anonymize institution name ("IRB approval was obtained from the authors' institution; project ID [redacted for review]").

---

## 7. Pre-registration

### When required

When the study was pre-registered at OSF, aspredicted.org, or a registered report platform.

### Template language

> This study was pre-registered at [OSF or aspredicted URL]. The pre-registration specifies the hypotheses, design, sample size, exclusion criteria, and analysis plan. All deviations from the pre-registration are reported in [section].

### Placement

- Methods section
- For blinded review: use an anonymized OSF view link. Do not include URLs that reveal the authors.

---

## 8. Open Access (OA) declaration

### When applicable

When the authors choose INFORMS gold open access (CC BY 4.0). Some SS articles are published OA; verify the current article status and fee policy before advising.

### Template language

This is added by INFORMS production; authors do not write it themselves. But authors should:
- Decide on OA vs. subscription publication at submission
- If choosing OA, ensure funding for the OA fee
- Confirm CC BY 4.0 license terms align with co-author requirements and funder mandates

---

## 9. Acknowledgments (non-disclosure)

Distinct from formal disclosures. Acknowledgments typically:

- Thank the editor (e.g., "We thank Felipe Csaszar, the Editor, for the highly constructive comments...")
- Thank anonymous reviewers
- Name conference/seminar audiences ("We benefited from comments at the Academy of Management Annual Meeting in [year]")
- Name specific colleagues for feedback
- Name dissertation advisors / committee (for papers based on dissertations, like Clough's INSEAD dissertation)
- Mention pre-registration link (final version only)
- Reference IRB approval (final version only)

### Template

```
The authors thank the anonymous reviewers and the Editor, [Name], for the
highly constructive comments and suggestions we received in the review process.
The authors are grateful to the participants of the [Conference/Seminar Name]
([Year]) for valuable feedback, especially on [specific topic]. We thank
[Specific Names] for detailed comments on earlier versions of this paper.
[Optional: This paper benefited from feedback received at the [Other Venue]
in [Year].] This study received approval from the institutional review board
of [Institution Name] (Project ID: [Number]). We preregistered our study at
[URL].
```

For the blinded manuscript, REMOVE all of the above (it identifies the authors). Move to Title Page or post-acceptance.

---

## Disclosure checklist (use in PACKAGE mode)

| Item | Status | Notes |
|---|---|---|
| AI / LLM use disclosure | ✓ / ✗ / N/A | Include model name(s) and use case(s) |
| Author contributions | ✓ / ✗ / N/A | CRediT or alternative |
| Data Availability Statement | ✓ / ✗ | Required even if data not public |
| Conflict of Interest | ✓ / ✗ | Required even if none |
| Funding statement | ✓ / ✗ | Required even if none |
| IRB / ethics statement | ✓ / ✗ / N/A | Required for human-subjects work |
| Pre-registration link | ✓ / ✗ / N/A | When applicable; anonymized for review |
| Open Access decision | ✓ / ✗ | Subscription or gold OA |
| Acknowledgments scrubbed for blinding | ✓ / ✗ | All identifying info to Title Page |
| Title Page separate document | ✓ / ✗ | Standard INFORMS requirement |

---

## Post-acceptance vs. blinded-review differences

| Item | Blinded review version | Post-acceptance version |
|---|---|---|
| Authors and affiliations | Removed (in MS) / on Title Page | In MS |
| Acknowledgments | Removed (in MS) / on Title Page | In MS |
| Funding (institution-named) | Generic ("a faculty fund") | Full institutional name |
| IRB project ID | Anonymized ("[redacted]") | Full ID |
| Pre-registration URL | Anonymous OSF view link | Full URL |
| Self-citations | Third-person citation only | Full citation as normal |

This skill's PACKAGE mode produces both versions when needed.
