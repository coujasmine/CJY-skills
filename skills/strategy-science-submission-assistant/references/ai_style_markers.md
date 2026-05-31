---
file: ai_style_markers.md
purpose: >
  Catalog of AI-generated style markers (lexical, structural, hedge) used by
  the skill in POLISH, SECTION, RESPOND, and PACKAGE modes to flag and neutralize
  AI flavor before producing the final rewrite. Calibrated to Strategy Science
  prose norms. Also used as the reference base for the ss-ai-decontaminator subagent.
last_verified: 2026-05-21
---

# AI Style Markers — Strategy Science Calibration

## Contents

- 1. Lexical markers (English strategy-research prose)
- 2. Structural markers (paragraph and sentence shapes)
- 3. Argument-hedge markers (claim calibration)
- 4. Protected zones (never decontaminate)
- 5. SS-specific calibration on top of general decontamination
- 6. Self-check before delivery
- 7. How modes use this file


This reference is **mandatory** during the rewrite stage of POLISH, SECTION, RESPOND, and PACKAGE modes. Apply markers from §1-§3 to the rewritten output, not to the user's original text. The user's original prose may have idiosyncrasies that are part of their voice; this reference targets only flavors introduced (or amplified) by AI-assisted writing.

Default philosophy: **modify only when necessary**. A clean rewrite needs no decontamination pass.

> **SS-specific note:** Strategy Science prose is somewhat more abstract and theory-forward than JBR's manager-visible style. The "manager-visible framing" rewrite that JBR rewards is *not* always appropriate at SS — SS papers freely use terms like "mental representations", "cognitive flexibility", "governance structure", "coordination scope" without translation. The decontamination here is about removing AI-flavor *while preserving SS theoretical vocabulary*.

---

## 1. Lexical markers (English strategy-research prose)

### 1.1 Overused AI vocabulary

When the following words appear in the rewrite **outside their technical meaning**, replace them with the plain alternative. When the word has a defined technical meaning in the SS literature (e.g., "leverage" in capital structure, "robust" in robust standard errors, "myriad" in conflict literature, "navigate" in option-value strategy), preserve it.

| AI marker | Plain alternative |
|---|---|
| leverage (verb, non-financial) | use, draw on, apply |
| delve into | examine, investigate, study |
| dive deep into | analyze in detail |
| deep dive | detailed analysis |
| tapestry | combination, mix, set |
| pivotal (without governance theory) | important, central, key |
| underscore | emphasize, highlight, show |
| unveil | present, introduce, document |
| elucidate | explain, clarify |
| intricate | complex |
| robust (as praise, not statistical) | strong, well-supported |
| myriad | many, several |
| navigate (non-spatial) | address, manage, handle |
| testament to | evidence of |
| embark on / embark upon | begin, undertake |
| shed light on | clarify, explain |
| in the realm of | in, within |
| in the landscape of | in, across |
| ever-evolving / ever-changing | evolving, changing |
| paradigm shift (when not actually one) | change, shift |
| holistic (as filler) | integrated, comprehensive |
| nuanced (without specifying the nuance) | qualified, conditional |
| comprehensive (as filler) | thorough — or delete |
| seamlessly | smoothly — or delete |
| compelling (as praise) | strong, convincing — or delete |
| crucial (without warrant) | important — or delete |
| significant (non-statistical) | important, sizable — never as a synonym for "p < 0.05" outside results |
| harness | use |
| ushered in | began, started |
| at the forefront of | leading in |
| game-changer / game-changing | important, transformative |
| transformative (as filler) | significant change — or delete |
| cutting-edge | new, recent |
| state-of-the-art | current, leading |
| breakthroughs | advances |

### 1.2 Filler openers (delete or replace)

These phrases inflate sentences without adding meaning. Default: delete and start with the substantive claim.

- "It is important to note that …"
- "It is worth noting that …"
- "It should be noted that …"
- "It is crucial to recognize that …"
- "It is interesting to note that …"
- "In conclusion, …" (in body text — keep only in a Conclusion section)
- "Furthermore," / "Moreover," / "Additionally," at the start of a sentence — usually deletable
- "In recent years, there has been growing interest in …" — replace with the concrete phenomenon
- "In today's rapidly changing business environment, …" — delete entirely
- "As mentioned earlier, …" — delete; trust the reader
- "Building on the above, …" — delete; trust the structure
- "To put it simply, …" — delete or rephrase
- "Simply put, …" — delete

### 1.3 Hedge stacks

When two or more hedges combine, reduce to one.

- "may potentially possibly suggest" → "suggests" or "may suggest"
- "appears to seemingly indicate" → "indicates"
- "is somewhat largely consistent with" → "is consistent with"
- "could potentially be considered" → "may be"
- "tends to typically" → "typically"

### 1.4 Vague attribution

Require either a citation or a deletion.

- "Various studies have shown …" → cite or delete the framing
- "It is widely accepted that …" → cite or delete
- "Some scholars argue …" → name the scholars
- "Research has shown …" → cite specific research
- "Studies suggest …" → cite specific studies
- "Many researchers have noted …" → cite specific researchers

### 1.5 SS-protected vocabulary (do NOT touch)

The following terms are SS-specific theoretical or methodological vocabulary and must be preserved verbatim:

**Theoretical vocabulary:**
- mental representations, representational approach, lens model (Brunswik)
- strategic foresight, foresight, prediction error
- cognitive flexibility, cognitive overload, cognitive structure
- knowledge breadth, knowledge depth, generalist, specialist
- bounded rationality, satisficing, aspiration level
- behavioral theory of the firm, Carnegie tradition
- coordination speed, coordination scope, autonomous adaptation, coordinated adaptation
- hybrid governance, opt-in governance, reciprocal governance, consensus-based governance
- innovation ecosystem, platform, complementor, hub-and-spoke
- dynamic capabilities, microfoundations, ordinary capabilities
- transaction costs, asset specificity, hold-up
- modularity, integral architecture, technical interface
- analogical reasoning, mental model
- discriminating alignment, architectural trilemma
- absorptive capacity
- exploration-exploitation, ambidexterity
- wisdom of crowds, distributed cognition
- bounded discretion, managerial cognition
- human capital, strategic human capital
- entropy index, Teachman entropy
- cumulative abnormal returns (CAR), buy-and-hold abnormal returns (BHAR)

**Methodological vocabulary:**
- random forest, elastic net, gradient-boosted tree
- Krippendorff's alpha, inter-rater reliability, Cohen's kappa
- between-subjects, within-subjects, manipulation check
- firm fixed effects, year fixed effects, robust standard errors
- pre-registration, registered report
- pilot study, manipulation check

Do not "translate" these terms or substitute synonyms. They are the field's working vocabulary.

---

## 2. Structural markers (paragraph and sentence shapes)

### 2.1 Compulsive three-part lists

AI rewrites often produce: *"This study makes three contributions. First, … Second, … Third, …"* — even when the three items are not parallel.

For SS specifically: three-part contribution lists are a **HIGH desk-reject risk** (see `ss_desk_reject_triggers.md` D5). Reduce to one or two specific theoretical movements.

Keep enumeration only when:
- Items share the same syntactic head (e.g., all start with a verb of the same type).
- Items are at the same level of abstraction.
- The reader will need to retrieve the items as a set (e.g., three hypotheses in a section header).

Otherwise, convert to flowing prose where the logical relation (additive / causal / contrastive) carries the structure.

### 2.2 Em-dash overuse

SS prose uses commas, parentheses, and full stops more than em-dashes. Replace many em-dashes with one of:

- Comma + clause
- Parenthetical aside
- Full stop + new sentence

Keep em-dashes when the dash genuinely marks a sharp aside or a syntactic break a comma cannot carry. Note that *some* SS authors (Csaszar, for example) use em-dashes deliberately for emphasis — preserve the author's voice if em-dashes are deliberate.

### 2.3 Balanced-sentence reflex

AI rewrites overuse:
- "not only X but also Y"
- "while X, Y" (as a contrastive frame)
- "on the one hand … on the other hand"

Use these only when X and Y are genuinely parallel and the contrast is theoretically meaningful (Asghar et al. genuinely use "on one hand / on the other" for competing theoretical predictions, which is appropriate). Otherwise, break the parallel: state X, then state Y in its own sentence.

### 2.4 Echo-summarizing transitions

Delete when redundant:
- "Having established X, we now turn to Y"
- "Building on the above discussion, we …"
- "As discussed earlier, …"
- "Following our previous discussion, …"

The section heading already signals the turn.

### 2.5 Sentence-length monotony

AI rewrites often produce sentences clustered in the 20-28 word range. Break up two or three to add natural variation — a short declarative (8-12 words) followed by a longer qualifier reads more human.

### 2.6 Closing-implication reflex

AI rewrites often append a generic implication sentence to every body paragraph ("This finding has important implications for managers."). Keep only when the implication advances the argument; delete when generic.

### 2.7 Bullet-list reflex

AI rewrites tend to convert running prose into bullets. SS academic prose almost never uses bullets in main text; bullets appear in appendices, supplementary materials, or tables. Convert bulleted lists back to prose unless the user explicitly wants bullets.

---

## 3. Argument-hedge markers (claim calibration)

### 3.1 Overhedging causal claims (when design supports them)

If the design is experimental or quasi-experimental with credible identification, do not over-hedge:
- "may suggest a possible relationship" → "shows" or "demonstrates"

But: pure-theory papers (Clough pattern) should NEVER use empirical verbs. Even if the model "shows" something, use "the framework predicts" / "the analysis yields" / "we argue."

### 3.2 Underhedging association claims (when design is panel/cross-sectional)

If the design is observational without quasi-experimental identification, do not let AI-flavored verbs sneak in:
- "causes" / "drives" / "leads to" / "produces" → "is associated with" / "predicts" / "is followed by"

See `references/ss_claim_evidence_matrix.md` for the full matrix.

### 3.3 Triple-contribution restatement

AI rewrites often state contributions three times: in the abstract, in the introduction, and again in the discussion. Keep one strong statement in each location, but do not duplicate wording verbatim. The contribution sentence in the abstract, intro ¶6, and discussion §5.2 should be the same *substantive* movement, but worded differently.

### 3.4 Anthropomorphizing LLMs / ML

AI rewrites tend to anthropomorphize LLMs:
- "The LLM understood..."
- "The model decided..."
- "The algorithm knew..."

Rewrite to:
- "The LLM produced an output that classified..."
- "The model predicted..."
- "The algorithm assigned..."

SS reviewers actively flag anthropomorphizing language as it overstates ML capabilities.

---

## 4. Protected zones (never decontaminate)

The following content must be preserved verbatim, even if a flagged AI marker appears inside:

- **Statistical reports**: "β = 0.123 (SE = 0.045), p < 0.01" and similar.
- **Variable names**: ForesightIndex, IndustryKnowledgeBreadth, CAR-Predicted-CAR-Disparity, etc.
- **Hypothesis statements** (H1a, H1b, H2, …): preserve directional claim and operative verb.
- **Citations** in any form (parenthetical, narrative, in tables, in figure notes).
- **Quoted material**.
- **Section headings** matching SS conventions.
- **SS theoretical vocabulary** (see §1.5).
- **Equation numbers and equation content**.
- **Table and figure labels**.

---

## 5. SS-specific calibration on top of general decontamination

SS rewards three stylistic moves AI rarely produces well:

### 5.1 Lineage-anchored opening sentences

SS theory subsections open with a lineage-anchored sentence with a citation cluster. AI rewrites often open with a "topic introduction" sentence. Rewrite when:
- AFTER: "Cognitive flexibility refers to the ability to switch between different cognitive styles..."
- BEFORE (with anchor): "Cognitive flexibility refers to the ability to switch between different cognitive styles (Laureiro-Martínez and Brusoni 2018) and enables decision-makers to incorporate a greater breadth of cues in their mental representations by attending to less familiar cues (Kiss et al. 2020)."

The presence of an anchor citation cluster in the opening sentence of a subsection is an SS signature; AI-generated theory sections often lack this.

### 5.2 Mechanism specification (not just direction)

AI rewrites tend toward "X is positively related to Y" framings without naming the mechanism. SS rewards "X shapes [cognitive/structural/strategic mechanism] that produces Y."

When rewriting, do **not** invent a mechanism. Only restate the mechanism the author already named in the theory section. If no mechanism is stated, flag this as a theory-development issue, not a decontamination issue.

### 5.3 Theoretical-movement language (not just contribution list)

AI-generated contribution paragraphs default to "we contribute to the literature on X, Y, and Z." SS rewards: "We extend [specific lineage with citation] by [specific theoretical movement: mechanism / boundary / integration / new construct]."

When rewriting, identify the actual movement(s) the user is making and articulate them. Do not invent movements the manuscript does not support.

---

## 6. Self-check before delivery

For every rewrite that triggered decontamination:

1. **Necessity** — did each change neutralize an actual marker, or was it cosmetic?
2. **Protected zones** — did you preserve every variable, statistic, hypothesis, and citation?
3. **SS-vocabulary preservation** — did you preserve the field's working theoretical vocabulary (§1.5)?
4. **Voice continuity** — does the rewritten passage match the voice of nearby untouched sentences?
5. **Mechanism integrity** — did any rewrite weaken or distort the author's stated mechanism?
6. **Lineage anchoring** — did each theoretical claim retain its citation anchor?
7. **Pass signal** — if no markers triggered, did you issue the pass signal rather than inventing changes?

If any check fails, revert and try again. A partial decontamination with intact substance beats a thorough decontamination that drifts the argument.

---

## 7. How modes use this file

Before applying this catalog by hand, run `python3 scripts/scan_ai_style_markers.py <text>` to get a fast, complete list of lexical/structural/causal marker candidates with line numbers. The scan is a locator, not a decision-maker: it cannot tell whether "leverage" is financial-leverage usage or AI filler, or whether "navigate" is option-value strategy usage. Use its output to target the manual pass described below; the catalog and the protected-zone rules in §4 + §1.5 decide what actually changes.

- **POLISH mode**: load this file before producing the AFTER block. Every AFTER passage is decontaminated before being shown to the user.
- **SECTION mode**: same as POLISH, but only the targeted section.
- **RESPOND mode**: applies to the response letter prose and any revised manuscript passages mentioned in the response.
- **PACKAGE mode**: applies to the cover letter only.
- **AUDIT mode**: does **not** rewrite; instead flags AI markers in the user's draft as part of the diagnosis.
- **REVIEW mode**: does **not** rewrite; the Reviewer 3 (SS Fit, Theoretical Movement, and Implications) role may cite AI markers as a writing concern.

For Claude Code users, this file is the reference base of the `ss-ai-decontaminator` companion subagent. The subagent is invokable standalone outside the skill.
