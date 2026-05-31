# Dim 1 — Research Question: high/mid/low anchors + rewrite sketches

This file is loaded for IDEA mode (always) and MANUSCRIPT mode (when Dim 1 < 16/20). It complements the four 5-point sub-criteria in `utd24_rubric.md` with diagnostic patterns and rewrite templates.

---

## What a UTD24 research question looks like (4 patterns from recent literature)

UTD24 RQs almost always combine **a phenomenon hook** (why-now) with **a theoretical stake** (why-care). Four common pattern templates:

### Pattern P1 — Anomaly hook
> "Despite [established theoretical prediction], we observe [empirical anomaly] in [setting]. **Why?**"

Example shape: "Despite the prediction from the attention-based view that focal-firm attention shifts toward emerging competitors, we observe that large incumbents in [setting] systematically deflect attention away from [new competitor class]. Why?"

### Pattern P2 — Mechanism specification
> "When [established outcome] occurs, [established theory] is silent on [mechanism subdimension]. **How does [mechanism] operate?**"

Example shape: "When firms reconfigure resource portfolios after performance shortfalls, behavioral theory predicts search intensification but is silent on whether search distance is selected by managerial attention or by slack endowments. How do these two pathways interact?"

### Pattern P3 — Boundary refinement
> "[Established theory] predicts [outcome] under [implicit assumption]. Under [violated assumption], does [outcome] hold?"

Example shape: "Dynamic capabilities theory predicts that reconfiguration improves performance under environmental dynamism. Under conditions where reconfiguration triggers internal political conflict, does this prediction hold?"

### Pattern P4 — Integration / reconciliation
> "[Literature A] predicts X. [Literature B] predicts not-X. **Under what conditions does each apply, and what unified mechanism explains the boundary?**"

Example shape: "The Carnegie tradition predicts that performance shortfalls drive exploration; the attention-based view predicts that performance shortfalls narrow attention to exploitation. Under what conditions does each apply?"

**Pattern *not* allowed at UTD24:**
> "We examine the effect of X on Y in [setting]."

This is not a question — it's a data description. It scores ≤8/20 on Dim 1 by construction.

---

## Common Dim 1 failure modes (and how to fix them)

### Failure F1 — "We examine the effect of..." declarative

**Symptom**: Intro never poses a question. Reader cannot tell what is being asked.

**Score drop**: 1.4 → 1, 1.2 → 3.

**Fix sketch**:
- BEFORE: "We examine the effect of board AI literacy on firm digital transformation."
- AFTER: "How does the cognitive composition of the board — specifically, AI literacy among directors — shape the *pace* and *direction* of firm digital transformation, and under what governance conditions does this effect strengthen or attenuate?"

### Failure F2 — No why-now

**Symptom**: RQ is timeless. Could have been written in 1995.

**Score drop**: 1.1 → 1.

**Fix sketch**:
- BEFORE: "How does firm innovation depend on TMT diversity?"
- AFTER: "In the post-generative-AI era (2022-present), firms increasingly delegate exploration tasks to algorithmic systems. How does TMT cognitive diversity shape firm innovation when human cognitive variety competes with AI-generated alternatives as a source of exploration breadth?"
- Note: why-now must be *specific* (named event, named time window, named tech/regulatory change), not "the modern era".

### Failure F3 — No why-care

**Symptom**: Phenomenon is interesting, but the answer "X causes Y" doesn't change any theoretical position.

**Score drop**: 1.2 → 1.

**Fix sketch**:
- BEFORE: "How does CEO Twitter activity affect firm stock returns?" (Maybe answerable, but who cares theoretically?)
- AFTER: "Under what conditions does CEO public signaling — operationalized as CEO social-media activity — substitute for vs complement formal governance disclosures, and what does the answer imply for the [agency / stewardship / impression-management] tension in corporate communication theory?"

### Failure F4 — Scope sprawl

**Symptom**: RQ contains 2+ mechanisms × 2+ outcomes × 2+ moderators. Looks like a research program, not a paper.

**Score drop**: 1.3 → 1.

**Fix sketch**: Carve. Keep one mechanism × one boundary × one outcome. Move the other 80% to "future research".

### Failure F5 — Replication framing

**Symptom**: RQ is "does X effect Y hold in setting Z?" where Z is a new sample but not theoretically privileged.

**Score drop**: 1.3 → 1.

**Fix sketch**: Either elevate Z (e.g., Z is theoretically privileged because it isolates a mechanism) or reframe as a boundary-refinement question. "Does X hold in Z?" is JBR/MOR territory at best, not UTD24.

### Failure F6 — Fashion chase

**Symptom**: RQ couples a hot topic (AI, ESG, crypto) to a familiar DV without theoretical mechanism. Reads as marketing.

**Score drop**: 1.1 → 0, 1.2 → 1.

**Fix sketch**: Either drop the hot topic and use the underlying mechanism, or re-anchor the hot topic in a specific theoretical move (not "we study AI in strategy" but "AI as a substitute for managerial cognition introduces a new boundary on the attention-based view because...").

---

## Diagnostic questions to apply when reading a draft RQ

1. **Can I state in one sentence what changes theoretically if the answer is X vs Y?** If no → Dim 1.2 ≤ 1.
2. **Can I name the specific event / regulatory shift / technology / time window that makes this urgent *right now*?** If no → Dim 1.1 ≤ 1.
3. **Is this one mechanism × one boundary × one outcome?** If no → Dim 1.3 ≤ 3.
4. **Is the RQ phrased as a question with How / Why / When / Under what conditions?** If no → Dim 1.4 ≤ 3.
5. **Would I be embarrassed to read this RQ to an AMJ AE?** If yes → score does not exceed 12.

---

## IDEA mode: how to produce RQ rewrites

When generating RQ variants in IDEA mode, produce **2-3 variants that differ on *theoretical positioning*, not just wording**. Each variant should:

- Anchor a different parent theory (or the same theory at a different level — micro vs macro mechanism)
- State a different why-now / why-care
- Suggest a different methods route

Example: user's idea is "AI tools and TMT decision-making". Three variants:
- Variant A (attention-based view): "When AI-generated alternatives compete with human-generated alternatives for board attention, how is strategic decision quality shaped by attention allocation rules?" — natural outlet: SMJ / OS — natural method: archival + text analysis.
- Variant B (cognitive strategy, Csaszar-Gavetti): "Do AI-augmented mental models of strategic options change the *distribution* of choices managers consider, and does this translate into measurable strategy distinctiveness?" — natural outlet: Strategy Science / OS — natural method: lab experiment with executives.
- Variant C (TMT / upper echelons): "How does TMT AI literacy moderate the well-documented link between TMT demographic diversity and strategic novelty?" — natural outlet: SMJ — natural method: archival panel.

The user picks. Do not pick for them.

---

## MANUSCRIPT mode rewrite contract

When the RQ scores below 16/20, output:
- BEFORE (user's RQ verbatim)
- AFTER (rewritten RQ, satisfying all four sub-criteria)
- 3 bullets explaining what changed and why
- Flag if AFTER moves the paper to a different parent theory (Dim 2 may need realignment)

---

## REVIEW mode RQ attack patterns

R1 will attack on:
- Why-care vagueness: "the authors claim contribution to 'the strategy literature' — which conversation specifically?"
- Replication framing: "this is a single-setting test of an established prediction, not a theoretical advance"
- Scope sprawl: "the paper poses three questions; recommend cutting to one"

R3 will attack on:
- Why-now: "the introduction does not establish phenomenon-level urgency; the question could have been asked twenty years ago"
- Question vs aim: "the paper states what it will do but never asks a question"
