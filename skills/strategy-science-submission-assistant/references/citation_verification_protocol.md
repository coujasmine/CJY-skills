---
file: citation_verification_protocol.md
purpose: >
  Reference existence and metadata verification protocol for Strategy Science
  manuscripts. Used in CITATION_AUDIT mode and scripts/verify_references.py.
last_verified: 2026-05-23
---

# Citation Verification Protocol

Use this protocol when the user asks whether references exist, whether citation
metadata is trustworthy, or whether the manuscript contains citation risks before
Strategy Science submission.

## What the audit can and cannot prove

This protocol can check whether a reference appears to exist and whether its
metadata is internally consistent. It cannot, by itself, prove that the cited
source supports a manuscript claim. Claim support requires a locator anchor and
alignment audit (see `claim_citation_alignment_protocol.md`).

## Verification tiers

### Tier 1: Reference existence

For each reference, verify as many fields as possible:

- DOI
- title
- author list
- year
- journal / source

Recommended sources, when network access is available:

- Crossref REST API for DOI/title metadata
- OpenAlex Works API for DOI/title metadata and source metadata
- Semantic Scholar Academic Graph API for paper-level metadata

If online access is unavailable, run an offline structural audit and mark
external status as `NOT_CHECKED`.

### Tier 2: Locator anchor

Every important theoretical or empirical citation should have at least one
locator:

- **quote anchor**: short source quote, no more than 25 words
- **page anchor**: page number or page range
- **section anchor**: section name
- **paragraph anchor**: paragraph number or source-note location
- **none**: mark `LOW_CONFIDENCE`

Do not invent locators. If the user did not provide one, write
`[LOCATOR NEEDED]`.

### Tier 3: Claim-citation alignment

Evaluate whether the cited source supports the manuscript claim only from:

- user-provided PDF excerpts
- user-provided notes
- quote/page/section/paragraph anchors
- metadata verified by external databases, for existence only

Do not use model memory to decide that a citation supports a claim.

## Risk levels

| Risk | Trigger |
|---|---|
| LOW | DOI/title/author/year align across one or more sources; locator present |
| MEDIUM | Reference likely exists but metadata differs or locator is missing |
| HIGH | No match, impossible year/source combination, invented-looking title, or claim has no support anchor |

## Output fields

Use these fields in JSON or table output:

```
ref_slug
provided_title
provided_authors
provided_year
provided_doi
crossref_status
openalex_status
semantic_scholar_status
doi_match
title_similarity
metadata_risk
locator_status
claim_alignment_risk
recommended_action
```

## Hard stop

If a manuscript needs a citation and the user did not provide one, write:

`[CITATION NEEDED: <claim needing support>]`

Never fill in a citation from memory.

