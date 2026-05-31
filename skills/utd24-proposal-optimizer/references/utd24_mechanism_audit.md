# Dim 3 — Theoretical Mechanism: audit framework

This file deepens the four sub-criteria of Dim 3 in `utd24_rubric.md`. The mechanism is the single most-attacked element in UTD24 review.

---

## What a UTD24 mechanism looks like

A mechanism, at UTD24 standard, has **four properties**:

1. **Named** — the causal construct linking X and Y is explicitly identified, not "the relationship between X and Y"
2. **Directional** — predicts X → M → Y, not "X and Y are jointly related"
3. **Falsifiable** — at least one observation would force theory revision
4. **Scope-conditioned** — boundaries of when it applies are explicit

A typical UTD24 mechanism statement:

> "We argue that [boundary condition], increasing [X] leads to [M] because [causal logic with named theoretical construct]. This in turn shapes [Y] because [second causal logic]. The mechanism operates only when [scope condition]; outside that scope, we expect [alternative outcome]."

---

## Audit checklist (Dim 3.1 — pathway named and directional)

For each predicted relationship, the audit asks:

- Is M (the mediator / intervening construct) named?
- Is M's role specified — is it cognitive (an interpretation), structural (a position), behavioral (an action), affective (an emotion), or institutional (a norm)?
- Is the direction X → M → Y, or is M described symmetrically?
- Could a reader reproduce a path diagram from the prose?

**Common failure**: M = "legitimacy" / "cognition" / "learning" / "trust" without specifying which dimension. "Legitimacy" alone is not a mechanism — pragmatic legitimacy is, normative legitimacy is, cognitive legitimacy is, regulative legitimacy is. Specify which.

---

## Falsifiability (Dim 3.2)

A mechanism is falsifiable if there exists an observable outcome that would force theory revision. Tests:

**Test F1 — Symmetric prediction**:
> "When firms have more X, they will have more Y because [mechanism]. When firms have less X, they will have less Y because [absence of mechanism]."

This is unfalsifiable (or trivially satisfied) because both directions are accommodated. UTD24 papers should *commit to a sign* with a defensible reason.

**Test F2 — Boundary-aware prediction**:
> "Under condition C, we expect a positive effect of X on Y. Under not-C, we expect *no* effect (not 'a different effect')."

Predicting a null outside the scope is a UTD24 hallmark — it commits to a falsifiable boundary.

**Test F3 — Both signs accommodated**:
> "X may lead to Y if Z, or to not-Y if not-Z. We thus expect a relationship."

This is unfalsifiable — any result confirms the theory. Flag and require commitment.

---

## Alternative-explanation engagement (Dim 3.3)

UTD24 mechanisms must engage at least 2 alternative explanations. Alternative explanations are *competing mechanisms* — not just confounds.

Common alternative-explanation categories:
- **Selection** — could the X-Y correlation arise from selection of certain firms / individuals into X?
- **Reverse causality** — could Y cause X rather than vice versa?
- **Confounding theoretical mechanism** — could a different theory predict the same pattern (e.g., RBV vs Carnegie BTF both predict performance heterogeneity)?
- **Cognitive vs structural** — could the mechanism be cognitive interpretation vs structural position vs both?
- **Institutional vs strategic** — could the mechanism be institutional pressure rather than strategic choice?

For each named alternative, the paper should specify:
- Why is the proposed mechanism distinct?
- What empirical pattern would distinguish them?
- What does the design / data do to rule out the alternative?

---

## Analogy-as-mechanism (Dim 3.4) — DESK-REJECT trigger

Per Hard Rule 4 in SKILL.md, analogy substituting for mechanism is a desk-reject-level flag.

### Analogy markers to detect

Phrases that frequently signal analogy-as-mechanism:

- "similar to" / "similarly"
- "akin to"
- "as in [other setting]"
- "parallels" / "mirrors"
- "like" + comparison + "we expect"
- "analogous to"
- "by extension from"

These phrases are **fine in literature review** (drawing parallels to motivate a question) but are **fatal in the mechanism section** (where the causal logic is supposed to be carried).

### Diagnostic

Read each mechanism paragraph. Ask:
- Does the paragraph survive *without* the analogy?
- Does the causal logic stand on its own — naming constructs, specifying direction, addressing alternatives — even if you delete every "similar to" / "akin to" / "as in"?

If yes: analogy is illustration. Dim 3.4 = 5.
If no: analogy is substitute. Dim 3.4 = 1 or 0, flag as DESK-REJECT-LEVEL.

### Rewrite template when analogy is detected

- BEFORE: "Similar to how attention-based view scholars find that focal attention narrows in turbulent environments (Ocasio 1997), we expect AI-augmented attention systems to similarly narrow focus when input data is volatile."
- AFTER: "AI-augmented attention systems narrow focus when input data is volatile because [first-order causal mechanism: e.g., algorithmic confidence thresholds rise with input noise, leading to fewer candidate alternatives passing the threshold]. This mechanism is theoretically distinct from the human attention narrowing identified by Ocasio (1997), which operates through [Ocasio's mechanism]; the two mechanisms have different boundary conditions, namely [boundaries]."

The rewrite removes the analogy and *names* the AI-side causal logic on its own. The Ocasio reference becomes a literature signpost, not the mechanism.

---

## REVIEW mode R1 attack patterns (mechanism)

R1 will attack on:

- **Black-box mechanism**: "the paper says X affects Y but never specifies the intervening construct; the reader cannot reproduce a path diagram from the prose"
- **Analogy substituting for mechanism**: "the entire mechanism is carried by the analogy to [other phenomenon]; if the analogy is removed, no causal logic remains"
- **Symmetric prediction (unfalsifiable)**: "the mechanism accommodates both positive and negative effects of X on Y; this is not a testable prediction"
- **No alternative explanations**: "the paper does not engage selection / reverse causality / confounding mechanism; any reviewer can raise [obvious alternative]"
- **Construct vagueness**: "the mediator is named as 'legitimacy', but pragmatic / normative / cognitive / regulative legitimacy generate different predictions; specify which"

---

## What scores ≥18/20 on Dim 3

The paper:
- Names a specific mediator with theoretical lineage
- Predicts X → M → Y with explicit direction
- Commits to a sign with reason
- States falsifiable predictions, including null predictions outside scope
- Engages 2+ named alternative explanations, theoretically and empirically
- Uses analogies only as illustration after the mechanism is fully specified

What scores 0-8/20: black-box mediator, symmetric predictions, no alternatives engaged, analogy-as-mechanism, or "we argue X is related to Y because [theory] says so" without further specification.
