# UTD24 Hypothesis Patterns — writing templates for 10+ architectures

This file is the **writing template authority** for hypothesis statements. Used in:

- IDEA mode (when sketching hypothesis structure for a proposed paper)
- DESIGN mode (when matching hypothesis architecture to identification strategy)
- MANUSCRIPT mode (when rewriting weak hypotheses)
- REVIEW mode (when R1 flags a hypothesis as missing structure)

Each pattern includes: **when to use it**, **canonical template**, **a worked sketch with 3-layer chain**, **common failure modes**, **method tier match**, **outlet fit**.

All worked sketches are **illustrative templates**, not real citations. Real citations come from the user.

---

## Section L — Linear patterns (the workhorses)

### Pattern L1 — Linear positive

**When**: X → Y is monotonically increasing within the empirical range; mechanism predicts a single direction.

**Template**:
> H_n: <X> is positively associated with <Y>.

**Worked sketch with 3-layer chain**:
> **H1: TMT cognitive diversity is positively associated with strategic novelty.**
>
> [Mechanism] Following the upper-echelons logic (Hambrick & Mason 1984; Hambrick 2007), cognitively diverse TMTs draw on a wider repertoire of mental models when interpreting strategic situations. This generates a broader set of candidate strategic options before commitment, increasing the probability that selected strategies depart from industry norms.
>
> [Boundary] This effect operates when the strategic decision context allows deliberation (i.e., not crisis-driven decisions where time pressure suppresses option generation). Outside that scope (e.g., under crisis time pressure), we expect a null effect because cognitive variety cannot translate into option breadth.
>
> [Counter-argument] An alternative prediction from the conflict literature is that cognitive diversity creates coordination costs that suppress novel-strategy selection — the "diversity-paralysis" view. We side with the upper-echelons prediction because [reason — e.g., recent meta-analytic evidence suggests deliberation-context moderation, which we make explicit].

**Common failure**: stating the direction without the boundary or counter-argument; the hypothesis reads as a univariate prediction with no theoretical scaffolding.

**Method tier match**: archival panel (with FE for unobserved firm heterogeneity); survey with TMT informants; lab experiment with simulated TMT roles.

**Outlet fit**: SMJ, AMJ (TMT-natural).

---

### Pattern L2 — Linear negative

**When**: mechanism predicts that increasing X *suppresses* Y; mirror of L1.

**Template**:
> H_n: <X> is negatively associated with <Y>.

**Worked sketch**:
> **H1: Founder educational homogeneity within the TMT is negatively associated with new-venture strategic experimentation.**
>
> [Mechanism] Educational homogeneity narrows the diversity of mental frames available to the TMT, restricting the candidate experiment set considered before commitment. The Carnegie behavioral tradition (Cyert & March 1963) predicts that narrower search sets produce fewer departures from current routines.
>
> [Boundary] This suppression operates in early-stage ventures where the TMT is the primary source of strategic option generation (no specialized scouting function exists). Outside that scope (e.g., growth-stage ventures with dedicated R&D scouting), we expect no effect.
>
> [Counter-argument] An alternative from the team-effectiveness literature is that homogeneity reduces coordination costs and *accelerates* experimentation execution. We argue this acceleration is downstream of option *generation*; without diverse option generation, faster execution does not translate to broader experimentation breadth.

**Common failure**: confusing "negative association" with "no association"; the prediction must commit to direction.

**Method tier match**: archival new-venture data; survey of early-stage TMTs.

**Outlet fit**: AMJ, ASQ, *Strategic Entrepreneurship J* (FT50 but not UTD24).

---

## Section M — Mediation patterns

### Pattern M1 — Simple mediation (X → M → Y)

**When**: theoretical claim is "X causes Y *via* M"; the paper's contribution is mechanism specification (opening the black box).

**Template**:
> H1: <X> is positively associated with <Y>.
> H2: <X> is positively associated with <M>.
> H3: <M> is positively associated with <Y>.
> H4 (optional but common): <M> mediates the relationship between <X> and <Y>.

**Worked sketch (one hypothesis, abbreviated)**:
> **H4: Attentional focus on competitor moves mediates the relationship between board independence and firm responsiveness to industry disruption.**
>
> [Mechanism] Independent boards expand the channels through which competitor information flows into the firm's attention structure (Ocasio 1997, 2011); this attentional channeling raises the probability that early disruption signals are interpreted as strategic threats requiring response.
>
> [Boundary] This mediation operates when the firm's existing attention structure leaves bandwidth for new signals — i.e., when current competitive demands are not at peak intensity. Under peak competitive demand, attention is fully consumed, and board independence's signaling channel is muted.
>
> [Counter-argument] An alternative is that independent boards demand more conservative responses to disruption (the agency-monitoring view) and thus reduce, not increase, responsiveness. We argue the attentional-channel mechanism dominates because the early-warning signal-flow precedes any board-level demand for conservatism.

**Common failure**: testing the mediator with mediation econometrics without first justifying why X → M → Y rather than M → X (reverse) or M as confound.

**Method tier match**: archival panel with measurable M (e.g., 10-K attention text analysis); survey with M items; lab experiment with M as manipulation check.

**Outlet fit**: SMJ, AMJ, OS.

---

### Pattern M2 — Serial mediation (X → M₁ → M₂ → Y)

**When**: theoretical claim is "X causes Y via a chained pathway", where M₁ produces M₂, which then produces Y.

**Template**:
> H1: <X> is positively associated with <M₁>.
> H2: <M₁> is positively associated with <M₂>.
> H3: <M₂> is positively associated with <Y>.
> H4: <M₁> and <M₂> serially mediate the <X>-<Y> relationship.

**Common failure**: presenting M₁ and M₂ as parallel mediators when the theoretical logic actually demands sequence (or vice versa). The serial vs parallel decision must come from theory.

**Method tier match**: structural equation modeling with multi-wave data; lab experiment with sequential measurement.

**Outlet fit**: AMJ (SEM-friendly); OS; rare at SMJ unless identification is strong throughout.

---

## Section Mod — Moderation patterns

### Pattern Mod1 — Simple moderation (interaction)

**When**: theoretical claim is "X causes Y, but the strength depends on Z"; the paper's contribution is boundary specification.

**Template**:
> H1: <X> is positively associated with <Y>.
> H2: <Z> moderates the relationship between <X> and <Y> such that the relationship is [stronger / weaker / sign-reversed] when <Z> is [high / low].

**Worked sketch (H2 only, abbreviated)**:
> **H2: Industry digital intensity strengthens the positive relationship between TMT AI literacy and strategic experimentation breadth, such that the relationship is stronger in high-digital-intensity industries.**
>
> [Mechanism] In high-digital-intensity industries, the strategic option set itself is broader because digital tools enable rapid prototyping of more alternatives; TMT AI literacy converts more of this broader option set into actually-considered alternatives. In low-digital-intensity industries, the strategic option set is narrower regardless of TMT literacy.
>
> [Boundary] This moderation operates within the contemporary period (post-2020 generative-AI deployment); pre-period evidence is unlikely to show the moderation because AI tools were not yet integrated into strategic option-generation workflows.
>
> [Counter-argument] An alternative is that high-digital-intensity industries already converge on AI-driven decision norms, suppressing literacy-based variation. We argue this convergence happens at the routinization layer (e.g., RPA), not the strategic-decision layer, where TMT-level literacy still discriminates between firms.

**Common failure**: predicting moderation without committing to the direction (strengthening / weakening / sign-reversing); R1 will flag and require commitment.

**Method tier match**: archival panel with interaction term; vignette experiment with 2x2 design.

**Outlet fit**: SMJ, AMJ.

---

### Pattern Mod2 — Moderated mediation (conditional indirect effect)

**When**: theoretical claim is "X causes Y via M, but the M pathway is conditional on Z".

**Template**:
> H1: <M> mediates the relationship between <X> and <Y>.
> H2: <Z> moderates the [first-stage / second-stage] of the mediation, such that the indirect effect of <X> on <Y> via <M> is stronger when <Z> is [high / low].

Two sub-patterns:
- **First-stage moderation**: Z moderates X → M (the front of the chain)
- **Second-stage moderation**: Z moderates M → Y (the back of the chain)

The paper must commit to which sub-pattern theoretically.

**Common failure**: testing both first- and second-stage moderation econometrically without theoretically justifying which one the mechanism predicts; reviewers see this as hypothesis fishing.

**Method tier match**: SEM with conditional process modeling (Hayes PROCESS macro for survey work; appropriate panel methods for archival).

**Outlet fit**: AMJ, OS.

---

### Pattern Mod3 — Competing mediation / dual pathway

**When**: theoretical claim is "two different mechanisms could produce Y from X; their relative strength depends on Z".

**Template**:
> H1a: <X> is positively associated with <Y> via <M_A> (Theory A's mechanism).
> H1b: <X> is positively associated with <Y> via <M_B> (Theory B's mechanism).
> H2: <Z> determines which mediator dominates, such that <M_A> dominates when <Z> is [high / low] and <M_B> dominates otherwise.

**Common failure**: presenting both pathways as parallel mediators without testing dominance; the contribution claim INTEGRATION requires the dominance test.

**Method tier match**: lab experiment with manipulation of Z to isolate each pathway; multi-method (mediation in one study, manipulation in another).

**Outlet fit**: OS (originality-friendly); ASQ (richness-friendly); SMJ if identification is clean throughout.

---

## Section NL — Non-linear patterns

### Pattern NL1 — Inverted-U (∩)

**When**: theoretical claim is "X is beneficial up to a point, then harmful"; the mechanism predicts opposing forces at low and high X.

**Template**:
> H_n: The relationship between <X> and <Y> is inverted-U-shaped, such that <Y> initially increases with <X> and then decreases beyond an inflection point.

**Worked sketch**:
> **H1: The relationship between TMT cognitive diversity and strategic decision quality is inverted-U-shaped.**
>
> [Mechanism] At low-to-moderate diversity, additional cognitive variety expands the option set (option-generation effect) and dominates. Beyond an inflection point, coordination and integration costs (coordination-cost effect) rise faster than the marginal option-generation benefit, suppressing decision quality.
>
> [Boundary] This inverted-U operates in TMTs without a dedicated integration role (e.g., a strong COO or strategy office). With strong integration, the coordination-cost slope flattens and the relationship may stay positive throughout the empirical range.
>
> [Counter-argument] An alternative is that the relationship is monotonically positive throughout the empirical range observed in modern TMTs (which rarely exceed the inflection point in real data). We argue the inflection is observable in our sample because [reason — e.g., the sample spans full diversity distribution including outlier-high-diversity TMTs].

**Common failure**: testing curvilinear effects without theorizing both forces (the up-slope mechanism AND the down-slope mechanism); reviewers will demand both. Also: testing X + X² without reporting whether the inflection lies inside the empirical range (Haans, Pieters & He 2016 *SMJ* style checks).

**Method tier match**: panel with X, X² (and Haans-Pieters-He robustness — inflection location, sample coverage of inflection, alternative functional forms).

**Outlet fit**: SMJ, AMJ.

---

### Pattern NL2 — U-shaped (∪)

**When**: theoretical claim is "X is harmful at moderate levels but beneficial at low or high extremes"; opposite of NL1.

**Template**:
> H_n: The relationship between <X> and <Y> is U-shaped, such that <Y> initially decreases with <X> and then increases beyond an inflection point.

**Common failure**: same as NL1; also confusing U with inverted-U directionally — must commit explicitly.

**Method tier match**: same as NL1.

**Outlet fit**: same as NL1.

---

### Pattern NL3 — Threshold / regime switch

**When**: theoretical claim is "X has no effect on Y until X crosses a threshold T, after which Y switches regimes (e.g., from null to positive)".

**Template**:
> H_n: <Y> exhibits a discontinuity at <X> = <T>, such that <Y> is [constant / linear] for <X> below <T> and [different regime] for <X> above <T>.

**Common failure**: testing threshold effects via interaction with a binarized X without theorizing why the discontinuity is at T (not at T-1 or T+1); without a theoretical T, the test is data-mining.

**Method tier match**: panel with threshold regression (Hansen 1999); RDD around T if T is policy-determined; structural change tests.

**Outlet fit**: SMJ (when T is policy-determined and RDD is clean); MS.

---

## Section C — Configuration patterns

### Pattern C1 — Congruence / fit

**When**: theoretical claim is "X and Z must match for high Y; mismatch produces lower Y"; common in strategy-environment, person-organization fit, technology-task fit research.

**Template**:
> H_n: The absolute difference between <X> and <Z> is negatively associated with <Y>; or equivalently, the polynomial response surface of <X> and <Z> on <Y> exhibits a ridge along the X = Z line.

**Common failure**: testing |X - Z| as a single regressor without polynomial response-surface analysis (Edwards 1995-2007 critique); UTD24 reviewers in this lineage will reject single-difference operationalizations.

**Method tier match**: polynomial response-surface regression; multi-source data (different informants for X and Z to avoid common-method bias).

**Outlet fit**: AMJ, OS.

---

### Pattern C2 — Configurational / set-theoretic (QCA)

**When**: theoretical claim is "outcome Y arises from specific combinations of conditions, not from any single condition"; the contribution is identifying *configurations*, not isolated effects.

**Template** (propositions, not hypotheses, since QCA generates pattern claims):
> P_n: Configuration [C₁ ∧ C₂ ∧ ¬C₃] is sufficient for <Y>.
> P_n+1: Configuration [C₂ ∧ C₄] is also sufficient for <Y> (equifinality).

**Common failure**: claiming QCA findings as causal; QCA identifies sufficient combinations, not causal effects. Verb calibration must be "sufficient for" or "consistently associated with", not "causes".

**Method tier match**: fuzzy-set QCA or crisp-set QCA (Ragin 2008).

**Outlet fit**: AMJ (most QCA-receptive UTD24 outlet); OS; rare at SMJ.

---

## Section AMR-P — Proposition patterns (for AMR / theory papers)

AMR papers state **propositions**, not hypotheses. Propositions describe expected relationships at the theoretical-construct level, without committing to empirical operationalization. AMR papers typically have 5-10 propositions.

### Pattern P1 — Theoretical proposition

**Template**:
> P_n: Under conditions [C₁, C₂, ...], <theoretical construct X> is [positively / negatively / curvilinearly] related to <theoretical construct Y> through <mechanism M>.

**Difference from hypothesis**:
- Propositions reference theoretical constructs, not measured variables
- Propositions specify scope conditions in the statement itself (rather than in the surrounding prose)
- Propositions are *generative*: each should produce multiple testable hypotheses for downstream empirical work

**Worked sketch**:
> **P1: Under conditions of algorithmic opacity in strategic decision support, the relationship between TMT AI literacy and strategic option breadth is positive when AI is used as deliberation support, and null when AI is used as decision substitute, through the mechanism of cognitive complementarity vs substitution between human and algorithmic judgment.**

**Common failure**: writing propositions as hypotheses (with measurable variables); AMR reviewers reject this as "not theoretical enough".

**Outlet fit**: AMR (primary); occasionally early-section of empirical paper as "theoretical proposition" before "empirical hypothesis".

---

### Pattern P2 — Boundary / scope proposition

**Template**:
> P_n: <Theory T>'s prediction that <X → Y> does not hold under conditions [C₁ ∧ C₂ ∧ ¬C₃], because <mechanism M> is suspended.

**Use**: when the AMR paper's contribution is identifying a scope boundary for an existing theory.

---

### Pattern P3 — Integration proposition

**Template**:
> P_n: <Theory A> and <Theory B>, which predict <Y> via different mechanisms <M_A> and <M_B> respectively, are integrated by condition <Z>: when Z is [high / low], <M_A> dominates; when Z is [low / high], <M_B> dominates.

---

## Outlet × hypothesis pattern compatibility matrix

| Pattern | SMJ | AMJ | ASQ | OS | MS (Strategy) | AMR | Strategy Science |
|---|---|---|---|---|---|---|---|
| L1 / L2 (linear) | ✓✓ | ✓✓ | ✓ | ✓ | ✓✓ | ✗ (use P) | ✓ |
| M1 (simple mediation) | ✓ (if identification clean) | ✓✓ | ✓ | ✓ | ✓ | ✗ (use P) | ✓ |
| M2 (serial mediation) | △ (identification harder) | ✓ | ✓ | ✓ | △ | ✗ (use P) | △ |
| Mod1 (simple moderation) | ✓✓ | ✓✓ | ✓ | ✓ | ✓✓ | ✗ (use P) | ✓ |
| Mod2 (moderated mediation) | △ | ✓ | ✓ | ✓ | △ | ✗ (use P) | △ |
| Mod3 (competing mediation) | △ | ✓ | ✓ | ✓✓ | △ | ✗ (use P) | ✓✓ |
| NL1 / NL2 (inverted-U / U) | ✓ (with Haans checks) | ✓ | ✓ | ✓✓ | ✓ | ✗ (use P) | ✓ |
| NL3 (threshold) | ✓ (if RDD) | △ | △ | △ | ✓✓ | ✗ (use P) | ✓ |
| C1 (congruence) | △ | ✓✓ | ✓ | ✓ | △ | ✗ (use P) | △ |
| C2 (QCA / configurational) | ✗ | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ |
| P1-P3 (propositions) | ✗ (empirical only) | △ (rare) | △ (theory section only) | △ | ✗ | ✓✓ | △ |

Legend: ✓✓ = highly fitting / common; ✓ = fitting; △ = possible but rare or extra justification needed; ✗ = misfit, do not use.

---

## How to use this file

### IDEA mode
After Mechanism→Hypothesis Derivation Workflow Step 2 (architecture selection), point to the matching pattern in this file. Walk through the template with the user.

### DESIGN mode
When the user is choosing between mediation vs moderation vs both, this file's patterns + the outlet matrix help decide which architecture is identifiable at their target outlet.

### MANUSCRIPT mode
When a hypothesis scores below 4/5 on Dim 4.1, retrieve the matching pattern's template and propose a BEFORE / AFTER rewrite.

### REVIEW mode
R1 may flag a hypothesis as "missing 3-layer chain" or "wrong architecture for the theoretical claim"; this file provides the correct template for the rewrite demand.

---

## Cross-references

- Mechanism specification before pattern choice → `utd24_mechanism_audit.md`
- Per-hypothesis 3-layer audit details → `utd24_hypothesis_architecture.md` (Dim 4.1)
- HARKing avoidance → `utd24_hypothesis_architecture.md` (Dim 4.4)
- Identification strategy per hypothesis → `utd24_methods_identification.md`
- Ex-ante method choice for a chosen hypothesis architecture → `utd24_design_choice_tree.md`
- Outlet floor per dim → `utd24_rubric.md` (Outlet-conditioned floor table)
