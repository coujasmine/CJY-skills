---
file: writing_quality_check.md
purpose: >
  Aggregate writing-quality audit protocol for Strategy Science manuscripts.
  Used in WRITING_CHECK mode and by scripts/check_writing_quality.py.
last_verified: 2026-05-23
---

# Writing Quality Check - Strategy Science

Use this file when the user asks for a prose self-check, AI-style audit, or
line-level writing quality report before revision. This protocol is diagnostic:
it locates risks and suggests actions, but it does not rewrite the manuscript.

## Core distinction

- **WRITING_CHECK**: diagnose only. Report locations, severity, and suggested
  actions. Do not rewrite.
- **POLISH / SECTION**: diagnose, then rewrite and run AI decontamination.

## Five diagnostic surfaces

1. **AI high-frequency terms**
   - Load `references/ai_style_markers.md`.
   - Run `scripts/scan_ai_style_markers.py`.
   - Treat the script as a locator. Preserve SS-protected vocabulary and
     technical uses.

2. **Punctuation pattern**
   - Count em dashes, semicolons, parenthetical asides, and long comma chains.
   - Flag em-dash overuse when there are more than 3 in a manuscript excerpt or
     more than 1 per 1,000 words in a full manuscript.
   - Recommendation is usually "replace with comma, parentheses, or a separate
     sentence," not automatic deletion.

3. **Throat-clearing openers**
   - Flag openers such as "It is important to note that," "In recent years,"
     "There has been growing interest in," and generic transitions.
   - Action: replace with the concrete phenomenon or claim.

4. **Structural pattern warnings**
   - Flag vague three-contribution structures.
   - Flag repeated paragraph templates such as claim -> however -> implication.
   - Flag generic paragraph endings that only say the point has implications.
   - SS introductions should present one or two precise theoretical movements,
     not a generic "three contributions" list.

5. **Sentence-length variation**
   - Calculate mean sentence length, standard deviation, and coefficient of
     variation.
   - Low variation is a marker of AI-polished prose, especially when most
     sentences cluster between 20 and 30 words.
   - Action: vary sentence length only where the paragraph reads monotonously.

## Severity calibration

Use the highest justified severity:

| Severity | Meaning | Typical action |
|---|---|---|
| LOW | Isolated marker or likely technical use | Inspect; preserve or lightly edit |
| MEDIUM | Repeated markers that may affect reader trust | Revise locally |
| HIGH | Systemic AI flavor or SS desk-reject pattern | Rewrite affected section before submission |

## Protected zones

Never flag these as writing-quality problems without context:

- statistical notation, model names, variable names, hypothesis labels
- citation strings and reference-list entries
- formal-theory definitions and propositions
- SS-protected vocabulary listed in `ai_style_markers.md`
- user-provided quotes, reviewer comments, or editor letters

## Output contract

```
## Writing Quality Report
Scope: ABSTRACT / INTRODUCTION / FULL MANUSCRIPT / EXCERPT
Confidence: LOW / MEDIUM / HIGH

## Overall risk
AI-style risk: LOW / MEDIUM / HIGH
Readability risk: LOW / MEDIUM / HIGH
SS positioning risk from prose alone: LOW / MEDIUM / HIGH

## Mechanical summary
| Check | Count / value | Risk | Action |
|---|---:|---|---|
| AI high-frequency terms | ... | ... | ... |
| Em dashes | ... | ... | ... |
| Throat-clearing openers | ... | ... | ... |
| Structural templates | ... | ... | ... |
| Sentence-length variation | ... | ... | ... |

## Line-level flags
- [line/paragraph]: "..." - rule - severity - suggested action

## Protected terms preserved
- "..." - reason

## Do-not-rewrite notice
This is a diagnostic report. No manuscript text has been rewritten.
```

