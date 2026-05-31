# UTD24 Exemplar Patterns — pattern catalog (canonical anchors + user-supplied slots)

This file is a **pattern catalog**, not a citation list. Per Hard Rule 1 (Never invent citations), this skill does not fabricate recent exemplars to make the catalog look fresh. Instead:

- **Canonical anchor patterns** (Section A) — abstracted from widely-cited UTD24 papers whose patterns are stable across decades
- **User-supplied exemplar slots** (Section B) — where the user provides 3-5 recent UTD24 papers in their target lineage and the skill extracts and stores patterns

This file is read in MANUSCRIPT and REVIEW modes when the user's draft matches one of the catalog patterns (e.g., "this looks like an extension paper following Pattern E1 — here is what an exemplar Pattern E1 paper does").

---

## How the patterns are described

Each pattern includes:
- **Pattern ID** (e.g., E1, M2, H3)
- **Structural signature** — what the pattern looks like across sections
- **Where it fits in the rubric** — which Dim it scores high on, and why
- **Common imitation failures** — how user drafts miss the pattern

No prose is copied. Patterns describe *moves*, not text.

---

## Section A — Canonical anchor patterns

### A.1 Extension patterns (Dim 2.3 = EXTENSION)

#### Pattern E1 — "Specifying a previously unspecified moderator"
**Structural signature**:
- Intro frames the established main-effect prediction (X → Y) as well-known in the parent theory
- Identifies a moderator M that the original theorists implicitly assumed away or did not specify
- Theory section develops why M moderates, with the 3-layer chain
- Hypotheses: H1 = main effect (replication confirmation), H2 = moderation by M
- Empirics test both
- Contribution claim: "we extend [parent theory] by specifying when [main effect] holds"

**Where it fits**: Dim 2.3 ≥ 4 (clear movement), Dim 4.1 ≥ 4 if 3-layer chain present
**Common imitation failure**: skipping H1 main-effect replication, leaving the moderation to look like a stand-alone hypothesis without anchoring to the parent theory's main prediction

#### Pattern E2 — "Opening the black box (mechanism specification)"
**Structural signature**:
- Intro names a well-documented X → Y relationship and notes that the *mechanism* is under-specified or contested
- Theory specifies a mediator M and develops the X → M → Y pathway
- Methods include a mediation analysis (or qual case tracing the pathway in real time)
- Discussion explicitly states that the parent theory now has a more specific causal claim

**Where it fits**: Dim 3.1 = 5 (mechanism named), Dim 2.3 ≥ 4 (movement = MECHANISM)
**Common imitation failure**: testing the mediator econometrically without theoretical justification of why the pathway is X → M → Y rather than M → X or M as a confound

---

### A.2 Integration patterns (Dim 2.3 = INTEGRATION)

#### Pattern I1 — "Bridging two theories that predict the same outcome differently"
**Structural signature**:
- Intro names two parent theories (e.g., behavioral theory of the firm and attention-based view)
- Identifies that they predict outcome Y via different mechanisms
- Theory specifies a condition C under which Theory A's mechanism dominates, and not-C under which Theory B's mechanism dominates
- Hypotheses test the interaction
- Discussion claims the integration

**Where it fits**: Dim 2.3 = 5 (movement = INTEGRATION), Dim 3.3 = 5 (alternatives engaged because they ARE the bridged theories)
**Common imitation failure**: naming both theories but using them as parallel justifications for the same prediction (no integration, just heavier lit-review)

#### Pattern I2 — "Bridging two literatures that don't talk to each other"
**Structural signature**:
- Intro identifies that literature A discusses [phenomenon X] and literature B discusses [phenomenon Y], with no engagement between them
- Argues that X and Y are theoretically connected via mechanism M
- Theory develops the bridge
- Empirics show the connection
- Contribution: opening dialogue between the two literatures

**Where it fits**: Dim 2.3 = 5, Dim 1.2 ≥ 4 (why-care is naturally strong for genuine integration)
**Common imitation failure**: literature B is cited but its arguments are not actually integrated; the paper remains in literature A

---

### A.3 Reconciliation patterns (Dim 2.3 = RECONCILIATION)

#### Pattern R1 — "Resolving conflicting empirical findings"
**Structural signature**:
- Intro identifies two (or more) published studies with conflicting empirical findings on X-Y
- Identifies a moderator or boundary condition Z that explains when each finding holds
- Theory specifies why Z matters
- Empirics test the moderation
- Contribution: reconciling the conflict via Z

**Where it fits**: Dim 2.3 = 5, Dim 1.1 ≥ 4 (why-now via "ongoing tension")
**Common imitation failure**: framing one paper's finding as "we agree with X, not Y" without specifying the conditions under which Y is wrong

---

### A.4 Boundary patterns (Dim 2.3 = BOUNDARY)

#### Pattern B1 — "Identifying when a robust prediction fails"
**Structural signature**:
- Intro acknowledges that the parent theory's prediction holds widely
- Identifies a specific condition under which the prediction breaks
- Theory develops why the boundary matters
- Empirics demonstrate the prediction breaking at the boundary
- Contribution: specifying scope condition

**Where it fits**: Dim 2.3 = 5, Dim 3.2 = 5 (falsifiability via boundary)
**Common imitation failure**: claiming boundary but the empirical result is just attenuation of the main effect, not a sign flip or null at the boundary

---

### A.5 Method-side patterns

#### Pattern M1 — "Clean DiD on policy / regulatory shock"
**Structural signature**:
- Identification = DiD around a specific policy / regulatory event
- Pre-period parallel-trends evidence shown
- Placebo tests on non-affected groups
- Robustness includes alternative control-group construction (matching, synthetic controls)

**Where it fits**: Dim 5.1 = 5 (causal claims allowed), Dim 5.3 = 5 (robustness covers identification threats)
**Common imitation failure**: DiD without parallel-trends evidence; placebo absent; control group chosen by convenience

#### Pattern M2 — "Multi-LLM text measurement (Kanis et al. 2026 style)"
**Structural signature**:
- Construct measured via LLM coding of text
- 3 LLMs used (e.g., GPT-4, Claude, Gemini)
- Human-benchmark inter-rater agreement reported (Krippendorff α typically ≥ 0.7)
- Multi-LLM agreement reported separately
- Sensitivity to prompt variants reported
- Pre-registered measurement protocol if possible

**Where it fits**: Dim 5.2 = 5 if executed; Dim 5.3 = 5
**Common imitation failure**: single-LLM coding, no human benchmark, no sensitivity tests, no validation set separation

#### Pattern M3 — "Lab experiment with executives (rare but ASQ/SS-favored)"
**Structural signature**:
- Subject pool is actual executives (not students)
- Vignette grounded in a realistic strategic decision
- Manipulation checks
- Triangulation with behavioral measure (not just self-report)
- External validity discussion grounded in the executive sample, not generic

**Where it fits**: Dim 5.2 ≥ 4, Dim 5.4 ≥ 4
**Common imitation failure**: student sample with hypothetical scenarios, no executives, no manipulation check

---

### A.6 Intro hook patterns

#### Pattern H1 — "Anomaly hook"
- Para 1: Established theoretical prediction stated cleanly
- Para 2: Empirical anomaly that the prediction does not accommodate
- Para 3: Stakes of resolving the anomaly
- Para 4: Our approach in one paragraph
- Para 5: Contribution sentence

#### Pattern H2 — "Phenomenon-first hook"
- Para 1: A specific recent phenomenon described concretely
- Para 2: Why standard theory cannot fully account for it
- Para 3: Theoretical question that the phenomenon raises
- Para 4: Our approach
- Para 5: Contribution

#### Pattern H3 — "Tension hook"
- Para 1: Two published findings or theories in tension
- Para 2: Stakes of resolution
- Para 3: Our resolution sketched
- Para 4: Approach
- Para 5: Contribution

---

### A.7 Contribution paragraph patterns

UTD24 contribution paragraphs (in intro and again in discussion) typically contain:

- 1 sentence naming the movement type (extends / integrates / reconciles / bounds / mechanism-specifies / new-theory)
- 1 sentence naming what specifically changes in the parent theory
- 1 sentence naming the empirical setting and identification (so reader knows the contribution is empirically supported)
- 1 sentence naming the broader implication for the lineage

Total: 3-5 sentences. No "implications for theory and practice" buzzword endings.

---

## Section B — User-supplied exemplar slots

When the user supplies recent UTD24 papers (PDFs or detailed summaries), the skill extracts and stores patterns here. Each entry:

```
### User exemplar U1
- Citation: [user-supplied — verify before relying]
- Outlet: SMJ / AMJ / ASQ / OS / MS / AMR
- Year: ...
- Parent theory: ...
- Movement type: EXTENSION / INTEGRATION / RECONCILIATION / BOUNDARY / MECHANISM / NEW-THEORY
- Method tier: ...
- Intro pattern: H1 / H2 / H3 / other (describe)
- Hypothesis architecture: count + 3-layer compliance
- Identification pattern: M1 / M2 / M3 / other (describe)
- Contribution paragraph pattern: ...
- Patterns this exemplar demonstrates well: ...
- Patterns absent: ...
```

> **Maintenance protocol**: when a new exemplar is added, re-confirm the citation (DOI / outlet / year), record date of confirmation, and update patterns demonstrated. Stale exemplar slots (no re-confirmation in 24 months) should be re-verified.

Slots remain empty until populated by the user.

---

## How this file is used

### MANUSCRIPT mode
When scoring a draft, identify which pattern(s) the draft is *trying* to follow. Compare to the pattern signature. Specific mismatches become Dim-specific actions.

Example: "Your draft is attempting Pattern E1 (specifying an unspecified moderator), but the manuscript skips H1 (the main-effect replication) and jumps directly to the moderation hypothesis. This weakens the connection to the parent theory and triggers Dim 2.3 down. Either add H1 explicitly or reframe the contribution as Pattern E2 (mechanism specification) — but then you need to add a mediator analysis."

### REVIEW mode
R1 can attack on pattern mismatch: "the paper appears to attempt Pattern I1 (theory bridging) but the second theory is cited rather than used; the integration is gestural."

### IDEA mode
Pattern catalog can suggest possible structural moves for the user's idea. Example: "Your idea about TMT AI literacy might fit Pattern E1 if you specify which moderator from the upper-echelons literature you are adding, or Pattern E2 if you specify the cognitive mechanism that the upper-echelons literature has black-boxed."
