# Dim 4 — Hypothesis Architecture: per-hypothesis audit + HARKing

This file deepens the four sub-criteria of Dim 4 in `utd24_rubric.md`.

It serves two flows:

- **Ex-post audit** (MANUSCRIPT / REVIEW mode): user already wrote hypotheses → this file scores them
- **Ex-ante derivation** (IDEA / DESIGN / MANUSCRIPT-stage-rewriting): user has a mechanism but no hypotheses yet → this file's "Mechanism → Hypothesis Derivation Workflow" below walks the user through deriving them

For non-linear patterns (curvilinear, threshold, serial mediation, moderated mediation, congruence-misfit, AMR propositions), see the companion file `utd24_hypothesis_patterns.md`.

---

## Mechanism → Hypothesis Derivation Workflow (ex-ante)

When the user has a parent theory + a mechanism but no formal hypotheses yet, do **not** skip to assessing rough hypothesis drafts. Walk through this 5-step workflow first. Skipping derivation produces hypotheses that fail Dim 4.1 (no 3-layer chain) and Dim 4.3 (mechanism-outcome misalignment).

### Step 1 — Lock the core causal pathway

Force the user to write out the mechanism as a path:
```
X (named construct, named operationalization)
   ↓ via M (named theoretical mediator from parent theory, with sub-dimension specified — e.g., "pragmatic legitimacy" not "legitimacy")
   ↓
Y (named outcome construct, named operationalization)
```

If the user cannot fill in M with a specific sub-dimension, halt. Return to `utd24_mechanism_audit.md` Dim 3.1 (Common failure: M = "legitimacy" / "cognition" / "learning" alone).

If X → Y is direct (no mediator), the paper is doing a different theoretical move (boundary, not mechanism). Re-route to a boundary hypothesis (Pattern B below) rather than a mediation hypothesis.

### Step 2 — Identify variable layers and decide the hypothesis architecture

Given the mechanism path, decide which hypothesis architecture matches the theoretical claim:

| User's theoretical claim | Hypothesis architecture | Required hypotheses |
|---|---|---|
| "X causes Y via M" | Mediation chain | H1: X → Y (main); H2: X → M; H3: M → Y; H4 (optional): indirect effect of X on Y via M (Sobel / bootstrap) |
| "X causes Y, but only when Z" | Moderation | H1: X → Y; H2: Z moderates X → Y (with direction) |
| "X causes Y via M, but the mediation strength depends on Z" | Moderated mediation | H1: X → M → Y; H2: Z moderates X → M (first-stage moderation) OR M → Y (second-stage moderation) |
| "X causes Y via M₁, which then causes M₂, which then causes Y" | Serial mediation | H1: X → M₁ → M₂ → Y (with each link justified) |
| "Two mechanisms operate simultaneously; their relative weight depends on Z" | Competing mediation / dual-pathway | H1a: X → M_A → Y (Theory A path); H1b: X → M_B → Y (Theory B path); H2: Z determines which path dominates |
| "X has a U-shaped / inverted-U effect on Y" | Curvilinear | H1: curvilinear X → Y; H2 (often): mechanism explains the curvature (low-X-driver vs high-X-driver) |
| "X crosses a threshold T, after which Y changes regime" | Threshold | H1: discontinuity in Y at X = T; H2: mechanism that creates the discontinuity |
| "X and Z must be matched for high Y; mismatch reduces Y" | Congruence / fit | H1: |X - Z| negatively related to Y (or polynomial response surface) |

Lock the architecture **before** writing prose. If the user is uncertain whether their claim is mediation or moderation, re-read `utd24_mechanism_audit.md` until the mediator's role is unambiguous.

### Step 3 — Predict directions with theoretical commitment

For each hypothesis identified in Step 2, force a directional commitment:

- **Positive linear**: "H1: X is positively associated with Y" → must defend why not negative
- **Negative linear**: "H1: X is negatively associated with Y" → must defend why not positive
- **Curvilinear**: must commit to U or inverted-U (not "we expect a non-linear relationship") and specify which side dominates at the inflection
- **Moderation**: must commit to strengthening vs weakening (not "Z moderates")

If the user wants to predict "X may have a positive or negative effect on Y depending on...", that is the **theoretical motivation** for a moderation hypothesis (H1 positive, H2 moderator flips it), not a single hypothesis.

### Step 4 — Write the 3-layer chain for each hypothesis

For each hypothesis from Step 3, write the three layers (see Dim 4.1 below for the architecture):

- **Mechanism layer**: name the parent theory's logic that makes this direction theoretically necessary
- **Boundary layer**: name when the mechanism applies (and ideally name when it does *not* apply, predicting a null outside scope — this is the falsifiability commitment)
- **Counter-argument layer**: name the strongest rival prediction (often from a competing parent theory or from a different mechanism within the same theory) and state why the authors stake the prediction in the chosen direction

### Step 5 — Audit the derived hypotheses against the architecture

Cross-check the derived hypotheses against:

| Check | What it catches |
|---|---|
| Count check | If >5 hypotheses emerged from Steps 1-4, scope creep is happening — return to Step 1 and either narrow the mechanism or split into two papers |
| Mechanism-outcome alignment check | Is the construct measured for Y the same construct M predicts? If proxy distance is large, either bring the measure closer or defend the mapping explicitly |
| HARKing check | Did any hypothesis emerge from "the data showed this and we wrote a hypothesis to match"? If yes, label it `exploratory`, do not retrofit as confirmatory |
| Outlet floor check | If target outlet is ASQ or AMR with qual/theory orientation, check whether some hypotheses should be propositions instead. AMR papers use propositions; SMJ/AMJ/MS use hypotheses; OS/ASQ allow both |
| Cross-skill handoff | If hypotheses still feel thin after this workflow, delegate to global `hypothesis-builder` skill for deeper 3-layer audit |

### Derivation workflow output template

When walking the user through derivation, produce:

```
## Mechanism (locked)
X = ...
M = ... (sub-dimension specified: ...)
Y = ...

## Hypothesis architecture chosen
[Mediation / Moderation / Moderated mediation / Serial / Competing / Curvilinear / Threshold / Congruence]
Justification (one sentence): ...

## Derived hypotheses
H1: <statement>
  [Mechanism layer]: ...
  [Boundary layer]: ...
  [Counter-argument layer]: ...

H2: ...

H3: ...

(... up to 5 max)

## Audit pass
- Count: __/5 ✓ or scope-creep flag
- Alignment: ✓ for each (or proxy-distance defended)
- HARKing: no indicators / exploratory-labeled
- Outlet floor: hypotheses vs propositions decision documented

## What the user should do next
- If outlet = AMR: rewrite as propositions (see utd24_hypothesis_patterns.md Section AMR-P)
- If outlet = SMJ/MS: ensure each hypothesis ties to an identification-amenable test
- If hypothesis count was reduced from >5: document what was cut and why (for future-research section)
```

---

## The 3-layer hypothesis chain (Dim 4.1)

Every UTD24 hypothesis must have three layers:

### Layer 1 — Mechanism (why this causal direction)
Names the causal pathway from independent to dependent construct. Should reference the parent theory's logic.

### Layer 2 — Boundary (under what conditions)
States when the mechanism applies. UTD24 reviewers expect at least one boundary statement per hypothesis — if the mechanism is "universal", it's probably too vague.

### Layer 3 — Counter-argument (why the opposite might be expected, and why we predict the stated direction)
The hypothesis must explicitly state why a thoughtful reader might predict the opposite, and then explain why the authors stake their claim on the stated direction.

### Example of all three layers present

> "**H1**: TMT AI literacy is positively associated with firm exploration breadth.
> 
> [Mechanism] Following the cognitive strategy literature (Csaszar & Eklund 2026), AI literacy expands the mental representation space available to top managers, increasing the number of strategic alternatives considered before commitment.
>
> [Boundary] This effect operates only when AI tools are used in *deliberation* rather than as decision-replacement; in decision-replacement use, AI literacy adds no further breadth because the managerial mental representation step is bypassed.
>
> [Counter-argument] An alternative prediction from the attention-based view (Ocasio 1997) is that AI literacy narrows attention by elevating algorithmic salience over human-generated alternatives, thus *reducing* exploration breadth. We side with the cognitive-strategy prediction because [reason — e.g., recent evidence in Kanis et al. 2026 shows that managers with AI exposure increasingly use AI as deliberation support rather than as decision substitute, making the cognitive-strategy mechanism the dominant one in current practice]."

### Common Layer 1 failures
- Mechanism layer is just a restatement of the prediction ("we expect a positive effect because... we expect a positive effect")
- Mechanism layer cites the parent theory without specifying which mechanism within the theory
- Mechanism layer uses analogy (see `utd24_mechanism_audit.md`)

### Common Layer 2 failures
- Boundary missing entirely
- Boundary stated as "in our sample" (this is a scope condition of the data, not a theoretical boundary)
- Boundary is symmetric ("under high X, positive; under low X, negative" without theoretical reason)

### Common Layer 3 failures
- No counter-argument considered
- Counter-argument named but dismissed without reason
- Counter-argument stated symmetrically, leaving the prediction unmotivated

---

## Hypothesis count (Dim 4.2)

UTD24 papers most commonly run 3-5 hypotheses. Why this range:

- **<3**: under-developed; suggests the theory does not produce multiple commitments
- **3-5**: each hypothesis does theoretical work; readers can hold them in working memory
- **6-7**: scope creep visible; some hypotheses are usually redundant or under-motivated
- **8+**: usually a scope-creep paper, or a "kitchen sink" exploration disguised as theory testing
- **1-2 with no sub-hypotheses**: usually under-developed; common in early drafts

### Count diagnostic

When the user's draft has 6+ hypotheses, ask:

1. **Are any of them restatements of the same prediction in different operationalizations?** (e.g., H2a, H2b, H2c testing the same mechanism with different DVs). Consolidate to one H with multiple operationalizations as robustness.
2. **Are any of them "throwaway" controls or descriptive statistics dressed as hypotheses?** Cut them or move to descriptive analysis.
3. **Are any of them about secondary mechanisms that distract from the primary contribution?** Cut to the spine.

### Mediator / moderator hypothesis hygiene

- One mediator: state as H_M with the 3-layer chain
- One moderator: state as H_X with the 3-layer chain, including direction of moderation
- More than 2 mediators or 2 moderators: scope creep flag; likely the paper is trying to be two papers

---

## Mechanism-outcome alignment (Dim 4.3)

The construct measured for the outcome must match the construct the mechanism predicts.

### Alignment audit

For each hypothesis, ask:
- What construct does the mechanism predict? (e.g., "exploration breadth")
- What construct is measured? (e.g., "patent class count")
- Is the measurement a defensible operationalization of the mechanism's construct?
- Does the authors defend the mapping explicitly?

### Common alignment failures

- Mechanism predicts "decision quality"; outcome measured is "ROA over the next year". Decision quality and ROA are different constructs; the mapping needs defense.
- Mechanism predicts "managerial cognitive flexibility"; outcome measured is "the number of strategic actions taken". Cognitive flexibility may produce more or fewer actions depending on context.
- Mechanism predicts "exploration"; outcome measured is "number of new product launches". Exploration is broader than product launches.

### Fix

Either:
- Bring the outcome measure closer to the mechanism construct, OR
- Add a more direct outcome measure as the primary DV, with the original as a robustness, OR
- Defend the mapping explicitly in the manuscript ("we use [proxy] as an indicator of [construct] because [theoretical bridge]") and acknowledge limitations.

---

## HARKing-risk indicators (Dim 4.4)

HARKing = Hypothesizing After Results are Known. UTD24 reviewers are sensitized to this and will flag any of the following:

### Hard indicators (score 0)
1. The paper includes interaction terms or mediator paths that have no a priori theoretical reason in the theory section, but happen to be the strongest empirical results
2. The theory section uses past tense ("we found", "we documented") as if writing after analysis
3. Pre-registration claimed but predicted directions in pre-registration don't match the manuscript's stated predictions
4. Unusual moderator suddenly elevated to a main hypothesis when its theoretical justification is one sentence

### Soft indicators (score 1-3 depending on count)
1. Hypotheses listed with "we expected" rather than "we expect" / "we predict"
2. Discussion section opens with "our surprising finding that..." — implies post-hoc interpretation
3. Multiple "interesting" sub-effects highlighted in results without prior hypothesis
4. Hypothesis order in theory section doesn't match the empirical flow; some hypotheses appear retrofitted

### Fixes
- For experiments: pre-register. State pre-registration in the methods section. Manuscript predictions must match pre-registration.
- For archival: state in methods section the order of analyses. If exploratory analyses are reported, label them "exploratory" — do not retrofit them into hypotheses.
- For all: write the theory section *first*. Once the manuscript is "complete", do not go back and edit the hypotheses to match the results.

### What to do when HARKing is flagged
- DESK-REJECT-LEVEL flag in MANUSCRIPT/REVIEW output
- Recommend: identify which hypotheses are retrofitted, label them as exploratory in a separate section, and rewrite the theoretical sections to reflect what was actually predicted a priori

---

## Hypothesis-statement style at UTD24

UTD24 hypotheses are typically:

- **Stated in bold or italics**, separately from prose
- **Numbered** (H1, H2, ... or H1a, H1b, ...)
- **Phrased as predictions** with directional language ("positively associated", "increases", "moderates positively")
- **Followed by a 1-2 paragraph development** that contains the 3-layer chain
- **Free of method language** ("we hypothesize X, which we test using Y" is bad — hypotheses are theoretical statements, not method statements)

---

## REVIEW mode R1 attack patterns (hypotheses)

R1 will attack on:

- **3-layer chain missing**: "H3 is stated as a prediction with no boundary condition or counter-argument; the reader cannot tell why the authors predict the stated direction over the opposite"
- **Scope creep**: "the paper presents 7 hypotheses; several appear to test the same underlying mechanism with different operationalizations; recommend consolidating"
- **Mechanism-outcome mismatch**: "H2 predicts 'decision quality' but the DV is firm-level performance; the mapping is not defended"
- **HARKing**: "the moderation hypothesis H4 has no a priori theoretical justification beyond a single sentence; given that it produces the strongest empirical result, this raises HARKing concerns"
- **Symmetric predictions**: "the boundary condition in H3 states 'when X is high, positive; when X is low, negative' — this is not a directional commitment"

---

## What scores ≥18/20 on Dim 4

The paper:
- Has 3-5 hypotheses (4 modal)
- Each hypothesis has all three layers (mechanism / boundary / counter-argument)
- Each hypothesis aligns mechanism-construct to measured-construct
- No HARKing indicators
- Hypotheses are properly stated and separately numbered

What scores 0-8/20: 8+ hypotheses, missing layers, hard HARKing indicators, or major mechanism-outcome mismatch on the primary hypothesis.
