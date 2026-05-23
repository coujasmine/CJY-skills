---
file: claim_citation_alignment_protocol.md
purpose: >
  Protocol for auditing whether manuscript claims are actually supported by
  their citations. Used in CITATION_AUDIT mode and by the
  ss-claim-citation-auditor subagent.
last_verified: 2026-05-23
---

# Claim-Citation Alignment Protocol

Use this protocol after reference existence has been checked. The goal is to
separate three issues that are often conflated:

1. The reference exists.
2. The citation has a locator anchor.
3. The source supports the exact claim made in the manuscript.

## Claim extraction

Extract claims that contain citations or clearly require citations:

- novelty claims
- theoretical lineage claims
- causal claims
- boundary-condition claims
- measurement-validity claims
- statements about what Strategy Science or INFORMS favors
- "first study" or "no prior work" claims

## Alignment labels

| Label | Meaning |
|---|---|
| SUPPORTS | Source directly supports the manuscript claim |
| PARTIAL | Source supports a narrower version of the claim |
| BACKGROUND_ONLY | Source is relevant but does not support the asserted relationship |
| CONTRADICTS | Source conflicts with the manuscript claim |
| UNKNOWN | No locator or source excerpt was supplied |

## Required evidence

Use one of these evidence types:

- quoted source excerpt
- page or section locator plus user-supplied note
- annotated PDF excerpt
- author-provided literature matrix

When evidence is absent, mark `UNKNOWN`; do not infer support from memory.

## Recommended actions

- `keep`: claim and citation align.
- `narrow`: source supports a narrower claim.
- `move`: citation belongs in background, not support.
- `replace`: user needs a better citation.
- `delete`: claim is unsupported and not essential.
- `add_locator`: citation may be appropriate but lacks a locator.
- `add_citation`: claim needs support.

## Output contract

```
## Claim-Citation Alignment Audit

| Claim | Citation | Exists? | Locator? | Supports claim? | Risk | Action |
|---|---|---|---|---|---|---|
| ... | ... | YES / NO / NOT_CHECKED | YES / NO | SUPPORTS / PARTIAL / BACKGROUND_ONLY / CONTRADICTS / UNKNOWN | LOW / MEDIUM / HIGH | ... |

## High-risk citations
- [claim/citation]: issue -> action

## Missing locators
- [citation]: locator needed -> page / section / quote / paragraph

## Missing citations
- [claim]: [CITATION NEEDED: ...]
```

