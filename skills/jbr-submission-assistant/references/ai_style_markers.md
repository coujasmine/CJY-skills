---
file: ai_style_markers.md
purpose: >
  Catalog of AI-generated style markers (lexical, structural, hedge) used by
  the skill in POLISH, SECTION, RESPOND, and PACKAGE modes to flag and neutralize
  AI flavor before producing the final rewrite. Also used as the reference base
  for the jbr-ai-decontaminator subagent.
last_verified: 2026-05-18
---

# AI Style Markers — JBR Calibration

This reference is **mandatory** during the rewrite stage of POLISH, SECTION, RESPOND, and PACKAGE modes. Apply markers from §1–§3 to the rewritten output, not to the user's original text. The user's original prose may have idiosyncrasies that are part of their voice; this reference targets only flavors introduced (or amplified) by AI-assisted writing.

Default philosophy: **modify only when necessary**. A clean rewrite needs no decontamination pass.

---

## 1. Lexical markers (English management prose)

### 1.1 Overused AI vocabulary

When the following words appear in the rewrite **outside their technical meaning**, replace them with the plain alternative. When the word has a defined technical meaning in the literature (e.g., "leverage" in capital structure, "robust" in robust standard errors), preserve it.

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

### 1.2 Filler openers (delete or replace)

These phrases inflate sentences without adding meaning. Default: delete and start with the substantive claim.

- "It is important to note that …"
- "It is worth noting that …"
- "It should be noted that …"
- "It is crucial to recognize that …"
- "In conclusion, …" (in body text — keep only in a Conclusion section)
- "Furthermore," / "Moreover," / "Additionally," at the start of a sentence — usually deletable
- "In recent years, there has been growing interest in …" — replace with the concrete phenomenon
- "In today's rapidly changing business environment, …" — delete entirely

### 1.3 Hedge stacks

When two or more hedges combine, reduce to one.

- "may potentially possibly suggest" → "suggests" or "may suggest"
- "appears to seemingly indicate" → "indicates"
- "is somewhat largely consistent with" → "is consistent with"

### 1.4 Vague attribution

Require either a citation or a deletion.

- "Various studies have shown …" → cite or delete the framing
- "It is widely accepted that …" → cite or delete
- "Some scholars argue …" → name the scholars

---

## 2. Structural markers (paragraph and sentence shapes)

### 2.1 Compulsive three-part lists

AI rewrites often produce: *"This study makes three contributions. First, … Second, … Third, …"* — even when the three items are not parallel.

Keep enumeration only when:
- Items share the same syntactic head (e.g., all start with a verb of the same type).
- Items are at the same level of abstraction.
- The reader will need to retrieve the items as a set (e.g., three contributions in the contribution paragraph).

Otherwise, convert to flowing prose where the logical relation (additive / causal / contrastive) carries the structure.

### 2.2 Em-dash overuse

JBR prose uses commas, parentheses, and full stops more than em-dashes. Replace many em-dashes with one of:

- Comma + clause
- Parenthetical aside
- Full stop + new sentence

Keep em-dashes when the dash genuinely marks a sharp aside or a syntactic break a comma cannot carry.

### 2.3 Balanced-sentence reflex

AI rewrites overuse:
- "not only X but also Y"
- "while X, Y" (as a contrastive frame)
- "on the one hand … on the other hand"

Use these only when X and Y are genuinely parallel and the contrast is theoretically meaningful. Otherwise, break the parallel: state X, then state Y in its own sentence.

### 2.4 Echo-summarizing transitions

Delete when redundant:
- "Having established X, we now turn to Y"
- "Building on the above discussion, we …"
- "As discussed earlier, …"

The section heading already signals the turn.

### 2.5 Sentence-length monotony

AI rewrites often produce sentences clustered in the 20–28 word range. Break up two or three to add natural variation — a short declarative (8–12 words) followed by a longer qualifier reads more human.

### 2.6 Closing-implication reflex

AI rewrites often append a generic implication sentence to every body paragraph ("This finding has important implications for managers."). Keep only when the implication advances the argument; delete when generic.

---

## 3. Argument-hedge markers (claim calibration)

### 3.1 Overhedging causal claims (when design supports them)

If the design is experimental or quasi-experimental with credible identification, do not over-hedge:
- "may suggest a possible relationship" → "shows" or "demonstrates"

### 3.2 Underhedging association claims (when design is panel/cross-sectional)

If the design is observational without quasi-experimental identification, do not let AI-flavored verbs sneak in:
- "causes" / "drives" / "leads to" / "produces" → "is associated with" / "predicts" / "is followed by"

See `references/jbr_claim_evidence_matrix.md` for the full matrix.

### 3.3 Triple-contribution restatement

AI rewrites often state contributions three times: in the abstract, in the introduction, and again in the discussion. Keep one strong statement in each location, but do not duplicate wording verbatim.

---

## 4. Protected zones (never decontaminate)

The following content must be preserved verbatim, even if a flagged AI marker appears inside:

- **Statistical reports**: "β = 0.123 (SE = 0.045), p < 0.01" and similar.
- **Variable names**: DiscoveryAIIndex, TemporalMyopia, ExploratoryInnovation, etc.
- **Hypothesis statements** (H1, H2, …): preserve directional claim and operative verb.
- **Citations** in any form.
- **Quoted material**.
- **Section headings** matching JBR conventions.
- **Theory-specific vocabulary** with a fixed literature meaning.

---

## 5. JBR-specific calibration on top of general decontamination

JBR rewards two stylistic moves AI rarely produces:

### 5.1 Manager-visible framing

Replace abstract organizational phrasing with manager-visible language **when the substantive meaning is preserved**.

- "organizational dynamics" → "how top managers allocate attention," when the paragraph is about TMT attention
- "firm-level outcomes" → "what the firm does next" or "subsequent strategic action," when the section discusses behavior
- "institutional context" → "the regulatory environment managers face," when relevant

Do **not** rewrite when the abstract phrasing is the correct level of analysis.

### 5.2 Mechanism over performance

AI rewrites tend toward "X improves Y" framings. JBR rewards "X reshapes the [mechanism] that produces Y."

When rewriting, do **not** invent a mechanism. Only restate the mechanism the author already named in the theory section. If no mechanism is stated, flag this as a theory-development issue, not a decontamination issue.

---

## 6. Self-check before delivery

For every rewrite that triggered decontamination:

1. **Necessity** — did each change neutralize an actual marker, or was it cosmetic?
2. **Protected zones** — did you preserve every variable, statistic, hypothesis, and citation?
3. **Voice continuity** — does the rewritten passage match the voice of nearby untouched sentences?
4. **Mechanism integrity** — did any rewrite weaken or distort the author's stated mechanism?
5. **Pass signal** — if no markers triggered, did you issue the pass signal rather than inventing changes?

If any check fails, revert and try again. A partial decontamination with intact substance beats a thorough decontamination that drifts the argument.

---

## 7. How modes use this file

Before applying this catalog by hand, run `python3 scripts/scan_ai_style_markers.py <text>` to get a fast, complete list of lexical/structural/causal marker candidates with line numbers. The scan is a locator, not a decision-maker: it cannot tell whether "leverage" is financial-leverage usage or AI filler. Use its output to target the manual pass described below; the catalog and the protected-zone rules in §4 decide what actually changes.

- **POLISH mode**: load this file before producing the AFTER block. Every AFTER passage is decontaminated before being shown to the user.
- **SECTION mode**: same as POLISH, but only the targeted section.
- **RESPOND mode**: applies to the response letter prose and any revised manuscript passages mentioned in the response.
- **PACKAGE mode**: applies to the cover letter only.
- **AUDIT mode**: does **not** rewrite; instead flags AI markers in the user's draft as part of the diagnosis.
- **REVIEW mode**: does **not** rewrite; the Reviewer 3 (JBR Fit, Writing, Implications) role may cite AI markers as a writing concern.

For Claude Code users, this file is the reference base of the `jbr-ai-decontaminator` companion subagent. The subagent is invokable standalone outside the skill.
