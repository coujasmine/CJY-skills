---
file: jbr_disclosures_2024.md
purpose: Required disclosure statements for JBR/Elsevier submissions post-2024 (AI use, CRediT, Data Availability, COI, funding, ethics). Used in PACKAGE mode and at Stage 7 of POLISH.
last_verified: 2026-05-17
note: Elsevier policy evolves. If last_verified > 6 months from submission date, spot-check the current JBR Guide for Authors and Elsevier policies.
---

# Required Disclosures (Post-2024 Elsevier)

Elsevier has tightened submission disclosure requirements since 2023–2024. Missing or boilerplate disclosures can trigger a return-for-revision before peer review even begins. This file lists the **six standard disclosures** that JBR submissions need, with template language, common mistakes, and validation criteria.

For each disclosure, the polishing assistant should:

1. Check whether the user's draft already contains it
2. If missing or boilerplate → produce a draft tailored to the user's manuscript
3. Flag any disclosure that cannot be completed without user input (funding, IRB, CRediT roles, AI specifics)

---

## 1. AI-Use Disclosure (REQUIRED if any AI tool was used at any stage)

### What Elsevier requires (as of 2024)

Authors must declare:
- **Which AI tool(s)** were used (model name, version if relevant)
- **At which stage(s)** of the manuscript (idea generation, literature review, data analysis, writing/editing, image generation, code generation)
- An explicit affirmation that the authors **take full responsibility** for the content

AI must **not** be listed as an author.

### When this skill triggers a disclosure

This `jbr-submission-assistant` skill counts as AI assistance for any of the following purposes: diagnosis, rewriting prose, drafting cover letters, drafting response letters, audit. **Any user who polishes through this skill must add an AI-use disclosure.**

### Template

```
During the preparation of this manuscript, the authors used [Tool name and 
version, e.g., "Claude (Anthropic, claude-opus-4-7)"] to [specific use, e.g., 
"polish prose, calibrate claim language, and harmonize the abstract with the 
discussion section"]. After using this tool, the authors reviewed and edited 
the content as needed and take full responsibility for the content of the 
published article.
```

### Common mistakes to avoid

- Listing the AI tool as an author (forbidden by Elsevier)
- Vague "AI was used in the preparation of this paper" (must specify stages)
- Claiming no AI was used when polishing through this skill (false statement)
- Including AI-use disclosure in the title page only (must appear in the manuscript, before References)

### Placement

- Section heading: "Declaration of generative AI and AI-assisted technologies in the writing process"
- Position: **at the end of the manuscript, before the References list**

---

## 2. CRediT Contributor Statement (REQUIRED)

### What it is

The Contributor Roles Taxonomy (CRediT) requires every author's role(s) to be listed using the 14 standardized roles:

```
Conceptualization, Methodology, Software, Validation, Formal analysis, 
Investigation, Resources, Data curation, Writing - Original draft, 
Writing - Review & Editing, Visualization, Supervision, Project administration, 
Funding acquisition.
```

### Template

```
CRediT authorship contribution statement:

[Author A]: Conceptualization, Methodology, Writing - Original draft, 
Writing - Review & Editing.
[Author B]: Data curation, Formal analysis, Visualization, Writing - Review & 
Editing.
[Author C]: Supervision, Funding acquisition, Writing - Review & Editing.
```

### Validation criteria

- Every author appears
- Every author has **at least one** role
- "Writing - Original draft" appears for at least one author
- "Supervision" appears for the senior author(s)
- "Funding acquisition" appears if the work was funded

### Common mistakes

- Generic "all authors contributed to all aspects" — does not satisfy CRediT
- Missing a role for a junior author (every name needs at least one)
- Inflated role list (e.g., assigning all 14 roles to every author)

### Cannot be drafted by AI

This requires user input. Flag and ask: "Please specify each author's CRediT roles."

---

## 3. Data Availability Statement (REQUIRED)

### What Elsevier requires

Every paper needs a Data Availability Statement (DAS), even if data are not shared. The DAS clarifies whether and how data underlying the findings can be accessed.

### Template variants

**Variant A — Data publicly available**:
```
Data Availability Statement: The data that support the findings of this study 
are openly available at [repository name] (DOI: [DOI]).
```

**Variant B — Data available on request**:
```
Data Availability Statement: The data that support the findings of this study 
are available from the corresponding author upon reasonable request.
```

**Variant C — Data not available (with reason)**:
```
Data Availability Statement: The data that support the findings of this study 
are not publicly available due to [specific reason: e.g., confidentiality 
agreements with participating firms, third-party licensing restrictions, 
privacy regulations]. The data may be requested from the corresponding author 
subject to [conditions].
```

**Variant D — Archival data (CSMAR, WIND, Compustat, etc.)**:
```
Data Availability Statement: This study uses data from [CSMAR / WIND / Compustat / 
etc.], which are available through subscription. The processed analytical dataset 
and replication code are available from the corresponding author upon reasonable 
request.
```

### Common mistakes

- Omitting the DAS entirely
- "Data not available" without a reason
- Claiming "openly available" but providing no link or DOI

---

## 4. Conflict of Interest / Declaration of Competing Interests (REQUIRED)

### Template

**If no conflicts**:
```
Declaration of competing interest: The authors declare that they have no known 
competing financial interests or personal relationships that could have appeared 
to influence the work reported in this paper.
```

**If conflicts exist**:
```
Declaration of competing interest: [Author A] reports financial support from 
[organization]. [Author B] serves on the advisory board of [organization]. The 
remaining authors declare that they have no known competing financial interests 
or personal relationships that could have appeared to influence the work 
reported in this paper.
```

### Validation criteria

- Statement is present (do not omit, even if "none")
- Specific conflicts are named (organization, role)
- Statement appears in the manuscript, not only in the submission portal

---

## 5. Funding Statement (REQUIRED)

### Template

**If funded**:
```
Funding: This work was supported by [funding agency] under Grant [number]; and 
[funding agency 2] under Grant [number]. The funding sources had no role in the 
study design, data collection, analysis, interpretation, or in the decision to 
submit the article for publication.
```

**If unfunded**:
```
Funding: This research did not receive any specific grant from funding agencies 
in the public, commercial, or not-for-profit sectors.
```

### Common mistakes

- "Funded by [University]" without specifying program or grant ID
- Omitting the "had no role" sentence (recommended by ICMJE)
- Listing grants that did not support this specific paper

---

## 6. Ethics Statement / IRB Approval (REQUIRED for human-subjects research)

### Template

**Human-subjects research (survey, interview, experiment)**:
```
Ethics: This study received ethical approval from the [IRB name / Institutional 
Ethics Committee], reference number [number], on [date]. All participants 
provided informed consent prior to participation.
```

**Archival / secondary data, no human subjects**:
```
Ethics: This study uses secondary archival data and did not require ethical 
approval. The data are publicly available and contain no individually 
identifiable information.
```

**Qualitative interview research**:
```
Ethics: This study received ethical approval from the [IRB / Ethics Committee], 
reference number [number]. All interviewees provided informed consent. Names of 
individuals and organizations have been anonymized.
```

### Common mistakes

- Claiming "no human subjects" when running surveys or interviews
- Omitting the IRB reference number
- Forgetting to anonymize identifying details in qualitative work

---

## Submission Disclosure Checklist (use in PACKAGE mode)

For each item, mark ✓ ready / ✗ missing / ⚠ needs user input:

```
[ ] 1. AI-Use Disclosure (per Elsevier 2024 policy)
[ ] 2. CRediT Authorship Contribution Statement
[ ] 3. Data Availability Statement
[ ] 4. Declaration of Competing Interest
[ ] 5. Funding Statement
[ ] 6. Ethics / IRB Statement (if applicable)
[ ] 7. ORCID iDs for all authors (required by many Elsevier journals)
[ ] 8. Reviewer suggestions (optional but recommended; some SIs require 3)
[ ] 9. Cover letter (separate file or portal field)
[ ] 10. Title page (separate from blinded MS, with full author info)
[ ] 11. Blinded manuscript (no author identifiers anywhere in MS body)
[ ] 12. Highlights (3–5 bullets, ≤85 chars each — JBR convention)
[ ] 13. Graphical abstract (optional but encouraged)
[ ] 14. Supplementary materials (if applicable)
```

### Highlights template (item 12 — JBR-specific)

JBR uses Elsevier's Highlights feature: 3–5 bullets, ≤85 characters each, appearing in search results.

Pattern:
```
• [Phenomenon] is [verb with calibrated claim] [outcome]
• [Mechanism] mediates the [phenomenon]–[outcome] relationship
• [Boundary condition] moderates the effect of [X] on [Y]
• Implications for [managers / policy / stakeholders] include [specific action]
```

---

## Final disclosure-pass procedure

1. **Scan** the user's draft for each of the 6 disclosure types
2. **Score** each as ✓ / ✗ / ⚠
3. **For ✗**: draft the missing disclosure from the template, using info already in the manuscript
4. **For ⚠**: ask the user (CRediT roles, IRB numbers, funding details cannot be invented)
5. **For ✓**: validate against the "common mistakes" lists; flag if boilerplate

Hard rule: **never invent** IRB numbers, funding details, ORCID IDs, or contributor roles. Always flag and ask.
