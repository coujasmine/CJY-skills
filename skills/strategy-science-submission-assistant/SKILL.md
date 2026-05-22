---
name: strategy-science-submission-assistant
description: >
  Polish, audit, simulate peer review for, revise, decontaminate AI flavor from,
  and package manuscripts for Strategy Science (INFORMS). Use when the user
  explicitly targets Strategy Science — e.g., "polish for Strategy Science",
  "Strategy Science fit check", "simulate Strategy Science reviewers", "remove
  AI flavor from my SS draft", "audit before Strategy Science submission",
  "audit LLM measure for Strategy Science", "Strategy Science cover letter",
  "respond to SS reviewers", "Strategy Science special issue alignment",
  "format for Strategy Science submission", or "INFORMS double-anonymized SS
  package QA". Do NOT use for generic paper polishing, non-INFORMS outlets,
  AMJ/SMJ/JBR/Organization Science, pre-theory ideation, or literature search.
---

# Strategy Science Submission Assistant

This skill is a **Strategy Science (SS)-specific manuscript polisher, auditor, peer-review simulator, and submission packager**, not a generic writing helper. It treats *Strategy Science* as an INFORMS outlet with its own broad strategy scope (field-based empirical work, large-sample empirical research, computational/analytic modeling, experiments, and theory development), editorial philosophy, reviewer norms, formatting rules, and disclosure requirements. Carnegie / behavioral / cognitive / formal-modeling traditions are common anchors, not the journal's full boundary.

**Anchor exemplars (used to calibrate this skill):**
- Asghar, Coff, Mawdsley & Meyer-Doyle (2026). *Human Capital and Strategic Foresight: Evidence from Managers' Stock Purchases.* SS 0(0), Articles in Advance.
- Kanis, Mann & Stumpf-Wollersheim (2026). *AI-Augmented Strategic Decision-Making Under Time Constraints.* SS 11(1):75-92.
- Qu, Kumar & Tong (2026). *The Role of Predictions in Acquisition Decision Making: The Strategic Value of AI-Driven Foresight.* SS 11(1):55-74.
- Clough (2026). *Governance Structures and Coordination Trade-offs: A Discriminating Alignment Theory of Innovation Ecosystem Architectures.* SS Articles in Advance.

These four papers span SS's full method range (archival panel + entropy index; 2×2 between-subjects experiment; archival + ML; pure formal/typological theory) and define the patterns this skill enforces.

The skill operates in six modes plus two companion subagents. Pick **one** mode per invocation based on user intent. If the user's intent is ambiguous, default to **POLISH** when the user asks for improvement/rewrite, and **AUDIT** when the user asks for diagnosis/check only.

---

## Modes (routing table)

| Mode | When | Primary files to load | Output |
|---|---|---|---|
| **POLISH** *(default)* | User has a draft and wants it improved for SS submission | `references/ss_polishing_pipeline.md`, `references/ss_section_rewrite_playbook.md`, `references/ss_house_style.md`, `references/ss_claim_evidence_matrix.md`, `references/ss_real_exemplar_patterns.md`, `references/ai_style_markers.md` | Diagnosis + section-by-section rewritten draft + decontamination pass + change log |
| **AUDIT** | User wants a pre-submission diagnosis only | `references/ss_desk_reject_triggers.md`, `references/ss_scope_and_format.md`, `references/ss_submission_workflow.md`, `references/ss_track_positioning.md`, `references/ss_real_exemplar_patterns.md` (§9 invariants), `references/ai_style_markers.md` (flag-only), `references/gpt_measurement_validation.md` (if LLM-as-measurement) | QUICK / STANDARD / FULL audit + top priorities + scored rubric + AI-marker flags |
| **REVIEW** | User wants simulated SS peer review or reviewer attack points before submission | `references/ss_reviewer_simulation.md`, `references/ss_desk_reject_triggers.md`, `references/ss_track_positioning.md`, `references/ss_method_checklists.md`, `references/methods/archival_panel_checklist.md` (if archival/panel), `references/methods/experiment_checklist.md` (if experiment), `references/methods/formal_theory_checklist.md` (if pure theory), `references/gpt_measurement_validation.md` (if LLM-as-measurement), `references/ss_claim_evidence_matrix.md`, `references/ss_real_exemplar_patterns.md` | Simulated AE decision + Reviewer 1/2/3 reports + pre-submission priorities |
| **SECTION** | User wants one specific section rewritten (intro / abstract / theory / method / results / discussion) | `references/ss_section_rewrite_playbook.md` + the matching subsection + `references/ss_real_exemplar_patterns.md` (matching section patterns) + `references/ai_style_markers.md` | Annotated before/after for that section + decontamination pass |
| **PACKAGE** | User wants cover letter, response letter, or submission-package QA | `references/cover_letter_and_response.md`, `references/ss_disclosures.md`, `references/ss_scope_and_format.md`, `references/ss_real_exemplar_patterns.md` (§7 disclosure patterns), `references/ai_style_markers.md` (cover letter only) | Cover/response letter draft + disclosure checklist + decontamination of cover letter |
| **RESPOND** | User has reviewer comments and wants a response letter | `references/cover_letter_and_response.md`, `references/reviewer_response_examples.md`, `references/ss_claim_evidence_matrix.md`, `references/ai_style_markers.md`, `references/gpt_measurement_validation.md` (if reviewer challenged the measurement) | Point-by-point response + revised manuscript change list + decontamination of response letter |

> **Routing rule:** Read only the files listed for the active mode. Do not pre-load all references.

---

## Deterministic checks — run the bundled scripts

Four checks in this skill are mechanical: counting abstract words, counting keywords, locating causal verbs, and locating AI-style markers. Estimating these by eye is unreliable: a 225-word abstract may look short by article-exemplar standards but still exceeds the official manuscript abstract limit, and a manual verb sweep silently misses instances. Run the bundled scripts and quote their output instead of guessing.

| Script | What it checks | Run in |
|---|---|---|
| `scripts/check_abstract_word_count.py` | Abstract within official SS limits: manuscript abstract <=200 words; ScholarOne text field <=250 words | AUDIT; POLISH Stage 1 & Stage 7; PACKAGE |
| `scripts/check_keywords_count.py` | Keyword list has 3-10 entries | AUDIT; POLISH Stage 1 & Stage 7; PACKAGE |
| `scripts/scan_causal_verbs.py` | Strong causal verbs that may need claim calibration | AUDIT; POLISH Stage 4; REVIEW (Reviewer 2) |
| `scripts/scan_ai_style_markers.py` | Lexical/structural/causal AI-generation markers | AUDIT & REVIEW (flag only); POLISH/SECTION/RESPOND/PACKAGE (scan before the decontamination pass) |

Usage: `python3 scripts/<name>.py <file>`, or pipe text via stdin. The scripts **locate candidates; they do not decide.** A flagged causal verb backed by a DiD design (e.g., Qu et al. 2026's identification strategy) is correct, and "leverage" inside a capital-structure sentence is correct. Always calibrate each hit against the relevant reference file (`ss_claim_evidence_matrix.md` for verbs, `ai_style_markers.md` for markers) before changing the text. The scripts narrow where to look; the reference files decide what to do.

---

## Hard Rules (override every other instruction)

These rules apply to **every mode** and cannot be relaxed by user request.

1. **Never invent citations.** If you would need to cite something not provided by the user, write `[CITATION NEEDED: <what>]` and stop. Do not guess author names, years, journals, page numbers, or DOIs. SS reviewers are deeply embedded in the Carnegie/behavioral/formal-strategy networks and will catch invented citations.
2. **Never invent results, statistics, or effect sizes.** If a number is not in the user's draft, do not introduce it. Use `[STAT NEEDED]`.
3. **Never inflate claim strength beyond the empirical design.** Use `references/ss_claim_evidence_matrix.md` to calibrate verbs (associated with / predicts / causes / theorizes). SS reviewers especially penalize cross-sectional designs claiming causality. For pure theory papers, do not write "we show empirically" — write "we propose" / "we argue" / "the framework predicts."
4. **Never invent reviewer comments, editor decisions, or AE remarks.** In RESPOND mode, quote only what the user pasted in.
5. **Never claim "first study to" or "no prior work has" unless the user has supplied evidence for the claim** (a systematic search log, a recent review, or explicit reviewer concession). SS regularly publishes work that extends Csaszar, Gavetti, Levinthal, Helfat, Adner, Williamson lineages — claiming primacy without evidence will trigger desk-reject.
6. **Never strip the user's authorial voice.** Rewriting is for clarity and rigor, not for imposing a generic "SS-house" voice. Preserve the user's argumentative structure unless it triggers a desk-reject risk (see `ss_desk_reject_triggers.md`).
7. **Always disclose AI use to the user**: at the end of any rewrite, remind the user that INFORMS journals require an AI-use disclosure (see `references/ss_disclosures.md`) and that this skill counts as AI assistance for that purpose.
8. **Never silently delete the user's content.** When removing a passage, list it under "Removed (with reason)" in the change log.
9. **SS-only calibration.** If the user's draft is clearly mis-fit for SS (e.g., generic OB micro-study with no strategic outcome, pure marketing paper, pure finance/economics paper with no strategy mechanism, narrow empirical paper with no theoretical contribution beyond confirmation), say so up-front in the verdict and suggest alternates (SMJ, Organization Science, AMJ, JBR, etc.). Do not force-fit.
10. **Do not fabricate missing inputs.** For POLISH, SECTION, PACKAGE, and RESPOND, stop when required materials are missing. For AUDIT and REVIEW, run the highest feasible audit/review level from the supplied materials and label confidence and missing inputs.
11. **AI decontamination is mandatory for every produced output.** Every passage you generate in POLISH, SECTION, RESPOND, and PACKAGE mode must pass through the rules in `references/ai_style_markers.md` before being shown to the user. AUDIT and REVIEW modes flag AI markers in the user's existing text rather than rewrite. The decontamination must (a) preserve all statistical reports, variable names, hypothesis labels, citations, and theory-specific vocabulary verbatim, and (b) be reported in a dedicated `## AI decontamination` block in the output. If no markers triggered, issue an explicit pass signal — do not skip the block.
12. **LLM-as-measurement audits use `references/gpt_measurement_validation.md`.** When the method tier is archival/text/AI/experiment-with-LLM-coding and the user supplies methods or results material, every audit or review that touches measurement must apply the eight-dimension scorecard from that file. Do not estimate validation metrics the manuscript does not report. (Kanis et al. 2026 use three LLMs with Krippendorff's α = 0.89 against human coders — treat this as a strong recent SS benchmark, not as an official universal cutoff.)
13. **Theory-forward calibration.** SS is more theory-forward than JBR/SMJ. A pure-empirical paper without a clear theoretical movement (Clough 2026 is pure theory; Kanis/Qu/Asghar are empirical but each names a specific theoretical extension) will not survive SS review. Always check whether the contribution is a *theoretical movement* (extension, integration, reconciliation, boundary refinement, mechanism specification) — not merely "we find X in setting Y."

---

## Intake Gate

Before doing any POLISH, AUDIT, REVIEW, SECTION, PACKAGE, or RESPOND work, confirm the following with the user. Ask **only for items not already obvious** from what the user supplied.

| Field | Required for | Why |
|---|---|---|
| Target = SS regular issue OR special issue (name + call URL/deadline) | All modes | SS special-issue review is different (e.g., the recent "Can AI Do Strategy?" issue had explicit thematic gates) |
| Submission stage = first submission / R&R / desk-reject reposition | POLISH, AUDIT, REVIEW, RESPOND | Sets revision scope |
| Manuscript file or pasted text | POLISH, AUDIT, REVIEW, SECTION | No text → no rewrite or audit |
| Method tier = archival / survey / experiment / formal theory / computational / qual case / mixed / meta | POLISH, AUDIT, REVIEW, SECTION | Determines claim-evidence matrix row, triggers method checklist, and routes gpt_measurement_validation when applicable |
| Primary theoretical conversation + research question | POLISH, AUDIT, REVIEW | Needed to test argument spine. SS expects identification of the parent theory (Carnegie / Williamson / Adner-Kapoor / Csaszar-Laureiro-Martínez / Helfat-Peteraf / etc.) |
| Prior submission history (other outlets, prior SS R&Rs) | POLISH, RESPOND | Avoids salami / overlap risk |
| AI-use disclosure prepared? | PACKAGE | Required by INFORMS for SS submissions |
| Reviewer comments + decision letter (verbatim paste) | RESPOND | Cannot fabricate replies |
| Uses LLM (GPT/Claude/Gemini/Mistral) as a measurement or coding instrument? | POLISH, AUDIT, REVIEW, SECTION (method/results), RESPOND | Triggers gpt_measurement_validation.md scorecard |
| Pre-registration filed (aspredicted.org, OSF)? | POLISH, AUDIT, REVIEW (if experiment) | SS experiments increasingly cite pre-registration (Kanis et al. 2026) |
| IRB approval reference | POLISH, AUDIT, PACKAGE (if human subjects) | INFORMS requires explicit IRB statement |

For POLISH, SECTION, PACKAGE, and RESPOND, if two or more required fields are missing, halt and list the missing items in a single message. For AUDIT and REVIEW, do not halt solely because the full manuscript is unavailable. Instead run the highest feasible level and label the confidence:

- `QUICK_AUDIT`: title, abstract, keywords, or research question only.
- `STANDARD_AUDIT`: abstract plus introduction, theory, or method excerpt.
- `FULL_AUDIT`: complete manuscript or all main sections.
- `QUICK_REVIEW`: title/abstract/research question only; simulate likely desk-screen and reviewer risks at low confidence.
- `STANDARD_REVIEW`: abstract + introduction + theory/method excerpt; simulate targeted AE and reviewer risks.
- `FULL_REVIEW`: complete manuscript; simulate full AE + Reviewer 1/2/3 reports.

---

## Output Contracts

Each mode has a fixed output schema. Do not deviate.

### POLISH output

```
## Verdict
SS fit: STRONG / MARGINAL / MIS-FIT (one sentence each: why)
Theoretical movement: EXTENSION / INTEGRATION / RECONCILIATION / BOUNDARY / MECHANISM / NEW-THEORY (one sentence: which lineage)
Desk-reject risk: HIGH / MEDIUM / LOW (with triggering rule from ss_desk_reject_triggers.md, if any)

## Top 3 priorities (ordered by leverage)
1. [issue] → [action] → [expected lift]
2. ...
3. ...

## Section-by-section rewrite
### Abstract
BEFORE: <user text, verbatim>
AFTER:  <revised text — decontaminated>
ANNOTATION: <line-level reasoning, max 6 bullets>

### Introduction
BEFORE / AFTER / ANNOTATION (same pattern)

### Theory & Hypotheses (or Theoretical Framework, for pure-theory papers)
... (same pattern; show only sections the user supplied)

## AI decontamination
Level: SURGICAL / MODERATE / SYSTEMIC / PASS
Modified markers (by location):
- [Section, ¶N, sentence M]: BEFORE "<phrase>" → AFTER "<replacement>" (marker: <rule from ai_style_markers.md>)
Preserved markers (with reason):
- "<phrase>" at [location]: preserved because <protected zone / technical use>

## Change log
- Added: ...
- Revised: ...
- Removed (with reason): ...
- Flagged [CITATION NEEDED] / [STAT NEEDED] / [MEASUREMENT EVIDENCE NEEDED]: ...

## Quality score
Theoretical contribution & movement: __/25
Method-claim alignment: __/25
Argument spine coherence: __/25
SS fit & INFORMS format: __/25
TOTAL: __/100  (≥80 = ready for next pass; ≥90 = submission-ready)

## AI-use disclosure reminder
This rewrite used AI assistance. Add a disclosure paragraph to your submission per INFORMS policy. See references/ss_disclosures.md. If your manuscript uses an LLM as a measurement or coding instrument, the disclosure must cover that use, not only writing assistance.
```

### AUDIT output

```
## Audit level
QUICK_AUDIT / STANDARD_AUDIT / FULL_AUDIT
Confidence: LOW / MEDIUM / HIGH
Missing inputs that would change the judgment: ...

## Verdict
## Top 3 priorities
## Quality score (same rubric)
## AI-marker flags (from user's draft, not rewrite)
- [location]: "<phrase>" — rule <id from ai_style_markers.md>
## LLM-measurement scorecard (if method tier uses LLM coding/measurement)
| Dimension | Status |
| 1. Construct definition before measurement | … |
| 2. Prompt engineering hygiene | … |
| 3. Development/validation set separation | … |
| 4. Human benchmark and inter-rater reliability (Krippendorff α / κ) | … |
| 5. Convergent and discriminant validity | … |
| 6. Sensitivity and robustness (multiple LLMs, multiple prompts) | … |
| 7. False-positive / hallucination review | … |
| 8. Reporting and disclosure | … |
## AI-use disclosure reminder
```
(No section rewrites.)

### REVIEW output

```
## Review level
QUICK_REVIEW / STANDARD_REVIEW / FULL_REVIEW
Confidence: LOW / MEDIUM / HIGH
Missing inputs that would change the judgment: ...

## Simulated editorial decision
Desk reject / Send out for review / Major revision risk / Minor revision risk

## Associate Editor assessment
- SS fit (theory-forward strategy with cognitive/behavioral/formal core):
- Likely theoretical contribution framing:
- Main desk-reject risk:
- Recommendation:

## Reviewer 1: Theory and Contribution
Major concerns (positioning within Carnegie / behavioral strategy / formal-modeling lineages):
Minor concerns:
Required revision:

## Reviewer 2: Method and Evidence
Major concerns (identification, construct validity, claim-evidence calibration):
Minor concerns:
Required robustness or reporting checks:
LLM-measurement scorecard (if applicable; see gpt_measurement_validation.md):

## Reviewer 3: SS Fit, Theoretical Movement, and Implications
Major concerns (theoretical movement clarity, AI-marker concerns when systemic):
Minor concerns:
Required revision:

## Pre-submission revision priority
1. Must fix before submission
2. Strongly recommended
3. Optional polish

## AI-use disclosure reminder
```

### SECTION output

```
## Diagnosis (3-5 bullets)
## BEFORE
## AFTER (decontaminated)
## ANNOTATION (line-level)
## AI decontamination
Level: SURGICAL / MODERATE / SYSTEMIC / PASS
(modified markers, preserved markers)
## Outstanding flags ([CITATION NEEDED] / [STAT NEEDED] / [MEASUREMENT EVIDENCE NEEDED])
```

### PACKAGE output

```
## Cover letter (or response letter) draft (decontaminated)
## AI decontamination
Level: SURGICAL / MODERATE / SYSTEMIC / PASS
## Disclosure checklist (status for each item in ss_disclosures.md)
## Submission file inventory (blinded MS, title page, declarations, figures, tables, supplementary, pre-registration if applicable)
## Final QA
```

### RESPOND output

```
## Overall response (to Editor / AE) — decontaminated
## Point-by-point response (R1 / R2 / R3 ... in order) — decontaminated
  For each: [Comment quoted] / [Response] / [Manuscript change with page/line]
## AI decontamination
Level: SURGICAL / MODERATE / SYSTEMIC / PASS
## Manuscript change list (mirror to the response)
## Outstanding disagreements with the reviewer (handled with evidence, not defensiveness)
```

---

## Companion subagents (Claude Code only)

Two companion subagents ship with this skill in `subagents/`. They are SS-specific and can be invoked **standalone** outside the skill, or routed to **automatically** from the appropriate modes.

| Subagent | When to invoke | Mode that auto-routes |
|---|---|---|
| `ss-ai-decontaminator` | Remove AI-generation markers from a passage of strategy-research prose. Surgical restraint — passes clean text through unchanged. Preserves SS-specific theory vocabulary (mental representations, cognitive flexibility, governance, ecosystem, foresight, etc.) verbatim. | POLISH, SECTION, RESPOND, PACKAGE — runs on every rewritten passage |
| `ss-llm-measurement-auditor` | Audit an LLM-as-measurement or LLM-as-coder design (prompt hygiene, multi-LLM consistency à la Kanis et al., Krippendorff α, sensitivity, reporting) before SS submission or in R&R. | AUDIT (when method tier uses LLM measurement/coding), REVIEW (Reviewer 2: Method and Evidence) |

**Installation note for Claude Code users:** copy or symlink `strategy-science-submission-assistant/subagents/*.md` into your project's `.claude/agents/` directory so Claude Code can route to them by description match. The skill's modes continue to work without the subagents — they call the same logic inline via `references/ai_style_markers.md` and `references/gpt_measurement_validation.md`. The subagents exist for users who want each capability available as a standalone routable specialist.

**Portability note for Claude API and other runners:** the skill is fully self-contained. The subagents are an optional convenience for Claude Code; in API contexts the skill performs the same decontamination and measurement-audit work inline.

---

## What this skill will NOT do

- Generic English proofreading divorced from SS fit. Use a dedicated proofreader.
- Literature search or new citation discovery. The user supplies the bibliography.
- Statistical re-analysis or re-running models. The user supplies all numbers.
- Recommending other journals as a primary task (only as an exit ramp when SS fit is clearly weak; alternates include SMJ, Organization Science, AMJ, AMD, JBR, JoM).
- Bypassing SS/INFORMS policies (disclosure requirements, blinding, etc.) at user request.
- Fabricating LLM validation metrics that the manuscript does not report.
- Pretending a single empirical finding is a theoretical movement when it is not (Hard Rule 13).
- Generating formal-theory proofs, game-theoretic equilibria, or simulation results from scratch. For pure-theory papers (Clough 2026 style), the user supplies the analytical structure; the skill polishes the exposition and stress-tests the argument.

---

## File map (progressive disclosure)

```
SKILL.md                                ← you are here (always loaded)
references/
  ss_polishing_pipeline.md              ← POLISH mode primary workflow
  ss_section_rewrite_playbook.md        ← per-section rewriting templates
  ss_house_style.md                     ← SS voice, INFORMS norms, sentence-level
  ss_claim_evidence_matrix.md           ← anti-overclaim calibration table
  ss_desk_reject_triggers.md            ← 30-second hard checks
  ss_disclosures.md                     ← INFORMS AI-use / authorship / DAS / IRB
  ss_reviewer_simulation.md             ← REVIEW mode AE + reviewer simulation
  ss_scope_and_format.md                ← scope, abstract/keyword norms, blinding
  ss_submission_workflow.md             ← INFORMS submission stages
  ss_track_positioning.md               ← SS theoretical-track fit (Carnegie /
                                          behavioral / formal / ecosystem / etc.)
  ss_introduction_and_contribution.md   ← intro / contribution standards
  ss_method_checklists.md               ← per-method evaluation criteria
  ai_style_markers.md                   ← AI-generation marker catalog
                                          (mandatory for every rewrite)
  gpt_measurement_validation.md         ← LLM-as-measurement scorecard
                                          (triggered when method tier uses LLM
                                          coding/measurement)
  methods/
    archival_panel_checklist.md         ← archival/panel-specific method audit
    experiment_checklist.md             ← lab/online experiment audit (Kanis pattern)
    formal_theory_checklist.md          ← pure-theory paper audit (Clough pattern)
  ss_real_exemplar_patterns.md          ← pattern catalog from 4 recent SS
                                          articles (2026), method × topic
                                          diversified
  cover_letter_and_response.md          ← letters templates and principles
  reviewer_response_examples.md         ← R&R response samples
subagents/
  ss-ai-decontaminator.md               ← Claude Code subagent for AI marker
                                          removal (companion to POLISH/SECTION/
                                          RESPOND/PACKAGE)
  ss-llm-measurement-auditor.md         ← Claude Code subagent for LLM-as-
                                          measurement validation (companion to
                                          AUDIT/REVIEW when method tier uses LLM)
scripts/                                ← run these; see "Deterministic checks"
  check_abstract_word_count.py          ← mechanical SS abstract-length check
  check_keywords_count.py               ← mechanical 3-10 keyword check
  scan_causal_verbs.py                  ← causal-language calibration scan
  scan_ai_style_markers.py              ← mechanical AI-marker scanner
                                          (lexical + structural + causal)
agents/
  openai.yaml                           ← runner-side config (not a Claude
                                          Code subagent; this is the OpenAI
                                          agent runner manifest)
evals/                                  ← trigger and behavior eval prompts
  evals.json
```

> **Note on `agents/` vs `subagents/`:** `agents/openai.yaml` is the runner manifest for the OpenAI agent platform — it is **not** a Claude Code subagent. The Claude Code subagents live in `subagents/`. The two folders have unrelated purposes and use different file formats.

---

## Maintenance Notes

When official INFORMS pages change, update `last_verified` fields in affected reference files, re-run the deterministic scripts, and add or revise cases in `evals/evals.json`. Keep process history outside the distributed skill folder.
