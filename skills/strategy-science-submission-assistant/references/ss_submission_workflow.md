---
file: ss_submission_workflow.md
purpose: The end-to-end Strategy Science / INFORMS submission process — what happens, when, what the user needs to prepare. Used in PACKAGE mode and as background for AUDIT/REVIEW.
last_verified: 2026-05-21
---

# Strategy Science Submission Workflow

## Contents

- Stage 1: Pre-submission preparation
- Stage 2: Submission
- Stage 3: Editorial screening (Days 1-21)
- Stage 4: External review (Weeks 4-12)
- Stage 5: First-round decision (Week 12-16)
- Stage 6: Revision (1-6 months, author-driven)
- Stage 7: Second-round review (Weeks ~4-10)
- Stage 8: Final acceptance (typical R&R cycles: 1-3)
- Special Issue submissions
- Common timing benchmarks (from the 4 exemplars)
- Withdrawal
- Resubmission to SS after rejection
- Targeting another INFORMS journal after rejection


This file describes the INFORMS submission process for Strategy Science. It is descriptive (what happens) rather than prescriptive (what to write); for writing guidance, see other reference files.

> Verify current portal URLs and policies at https://pubsonline.informs.org/journal/stsc before final submission. INFORMS updates submission systems periodically.

---

## Stage 1: Pre-submission preparation

### Materials to assemble

1. **Blinded manuscript source file** (the body of the paper without author identifiers)
   - MS Word source file for text material
   - Double-spaced, 12-point Times Roman
   - All-inclusive length <=35 pages unless the cover letter explicitly explains the exception
   - Numbered lines (optional but reviewer-friendly)
   - All identifying information removed (see `ss_disclosures.md` and `ss_scope_and_format.md`)

2. **Title page** (separate document)
   - Title
   - Authors with affiliations
   - Corresponding author email
   - ORCID iDs (encouraged)
   - Funding sources (full institutional names)
   - Acknowledgments (full)
   - Author contributions
   - Conflict of interest disclosure

3. **Online appendix / supplementary materials** (if applicable)
   - Detailed methodology
   - Robustness checks
   - Pre-registration materials
   - Code (often hosted on OSF or GitHub)

4. **Cover letter** (see `cover_letter_and_response.md`)
   - Addressed to the Editor (or Guest Editors for SI)
   - States the journal target (regular issue or SI)
   - Summarizes the contribution
   - States novelty and lack of prior submission overlap
   - Confirms compliance with submission requirements (blinding, disclosures, etc.)

5. **Pre-registration link** (if applicable)
   - For blinded review: anonymized OSF view link
   - For final acceptance: full URL

6. **Disclosures** (see `ss_disclosures.md`)
   - AI use
   - Data availability
   - IRB approval
   - COI
   - Funding

### Pre-submission QA

Run through:
- `scripts/check_abstract_word_count.py` -> manuscript abstract <=200 words; ScholarOne abstract field <=250 words
- `scripts/check_keywords_count.py` -> 3-10 keywords
- `scripts/scan_causal_verbs.py` → no over-claiming
- `scripts/scan_ai_style_markers.py` → no systemic AI-style markers
- Disclosure checklist from `ss_disclosures.md` → all required disclosures prepared
- Desk-reject triggers checklist from `ss_desk_reject_triggers.md` → no HIGH triggers

---

## Stage 2: Submission

1. Visit https://pubsonline.informs.org/journal/stsc and click "Submit" / "Submit a Paper" -> ScholarOne Manuscripts
2. Create account or sign in
3. Select article type (Original Research, Special Issue, etc.)
4. Fill in metadata:
   - Title
   - Authors and affiliations
   - Abstract (paste in plain text; portal field <=250 words)
   - Keywords (3-10)
   - Article classification
5. Upload files:
   - Blinded manuscript source file (Word)
   - Separate title page
   - Cover letter
   - Tables and figure captions in Word when requested
   - Figures as separate editable/high-resolution files when requested
   - Supplementary materials / online appendix (separate files)
6. Confirm disclosures via portal checkboxes:
   - AI use
   - Author contributions
   - Data availability
   - COI
   - Funding
   - IRB
   - Pre-registration
   - Originality (not under review elsewhere)
7. Confirm corresponding author and consent
8. Submit

You will receive an automated email confirmation with a submission ID.

---

## Stage 3: Editorial screening (Days 1-21)

The Editor-in-Chief or a designated Senior Editor reviews the submission:

- **Format compliance**: blinding, disclosures, length
- **Scope fit**: does the paper fit SS's scope?
- **Quality threshold**: is the paper coherent enough for external review?

Possible outcomes:
- **Desk reject**: paper does not pass the editorial screen. Common reasons: mis-fit for SS, fundamental contribution issues, format violations. The author receives a brief reject letter from the editor.
- **Desk-reject with encouragement to retarget**: editor suggests an alternative outlet (rare but happens).
- **Send out for review**: paper is assigned to an Associate Editor (AE), who in turn assigns reviewers.

Do not report desk-reject percentages unless the user supplies a verified source. Treat desk rejection as a qualitative risk, not a numeric prediction.

---

## Stage 4: External review (Weeks 4-12)

The AE typically invites 2-3 reviewers. Reviewers have ~4-6 weeks to complete their review.

Reviewers see:
- Blinded manuscript
- Cover letter (sometimes with author info redacted)
- Online appendix

Reviewers do NOT see:
- Title page
- Author identities (in normal cases)

Each reviewer submits:
- A free-text review (typically 2-5 pages)
- A confidential note to the AE (sometimes)
- A recommendation (Accept / Minor / Major / Reject)

The AE synthesizes the reviews and writes their own recommendation to the EIC.

---

## Stage 5: First-round decision (Week 12-16)

The EIC issues one of:

- **Accept**: rare on first round
- **Minor revision**: small set of clearly addressable issues; revision typically returns in 1-2 months
- **Major revision**: substantive issues; revision typically returns in 3-6 months
- **Reject**: paper will not be revised further at SS
- **Reject with referral**: editor suggests resubmitting to an INFORMS sister journal (e.g., Organization Science)

The author receives:
- The EIC decision letter
- Reviewer reports (anonymized)
- The AE's letter (sometimes summarizing the reviewers)

---

## Stage 6: Revision (1-6 months, author-driven)

For Major Revision:

1. **Read all reviewer comments carefully.** Identify points of agreement, disagreement, and clarification needed.
2. **Revise the manuscript** to address substantive concerns. Use this skill's POLISH mode on individual sections.
3. **Draft a response letter** (see `cover_letter_and_response.md`).
   - Point-by-point response to each reviewer comment
   - Quote each comment verbatim
   - State what was changed in the manuscript (with page/line/section references)
   - Politely engage disagreements with evidence, not defensiveness
4. **Re-run pre-submission QA** on the revised manuscript.
5. **Submit the revision** via ScholarOne:
   - Updated blinded manuscript
   - Updated title page (if needed)
   - Cover letter to the editor
   - Response letter (separate file, addressed to reviewers and AE)
   - Track-changes version of the manuscript (typically required)

---

## Stage 7: Second-round review (Weeks ~4-10)

The original reviewers are typically re-invited. They evaluate:
- Whether each point was addressed substantively
- Whether new issues have emerged

The EIC issues a second-round decision:
- **Accept**: revisions satisfied reviewers
- **Minor revision**: small remaining cleanups
- **Major revision (rare at this stage)**: serious concerns not addressed; another round expected
- **Reject**: revisions did not satisfy reviewers; paper is unlikely to be accepted in further rounds

---

## Stage 8: Final acceptance (typical R&R cycles: 1-3)

When the paper is accepted:

1. **Final manuscript preparation**:
   - Author names and affiliations restored
   - Full Acknowledgments restored
   - Funding statement with institutional names restored
   - Pre-registration full URL restored
   - All disclosures finalized

2. **Copyediting and proofs**:
   - INFORMS production sends copyedited proofs
   - Author reviews and signs off
   - Open Access decision finalized

3. **Online publication**:
   - "Articles in Advance" version posted (online, with DOI, before issue assignment)
   - Final issue assignment when ready

4. **DOI and citation**:
   - DOI is assigned at acceptance
   - Citation format: "Author, A., Author, B. (2026) Title. *Strategy Sci.* Forthcoming. https://doi.org/10.1287/stsc.XXXX.XXXX"

---

## Special Issue submissions

For SI submissions, the workflow is similar with these differences:

- Submission is through ScholarOne, with the SI name selected when the portal offers that option
- Guest Editors handle the editorial screening and review process
- Timelines are typically accelerated
- SI calls often have explicit thematic gates; papers failing the gate are desk-rejected or referred to the regular issue
- The cover letter should be addressed to "Guest Editors of [SI Title]"

Recent SS Special Issue: "Can AI Do Strategy?" (Vol. 11 No. 1, March 2026), guest edited by Felipe A. Csaszar, Gwendolyn Lee, Peter Zemsky, and Todd Zenger.

---

## Common timing benchmarks (from the 4 exemplars)

| Paper | Received | Revised | Accepted | Online | Cycle |
|---|---|---|---|---|---|
| Kanis et al. 2026 | May 1, 2025 | Sept 20, 2025 / Oct 13, 2025 | Nov 24, 2025 | Feb 4, 2026 | ~7 months |
| Qu et al. 2026 | Apr 29, 2025 | Sept 19, 2025 | Dec 14, 2025 | Feb 9, 2026 | ~8 months |
| Clough 2026 | Oct 28, 2024 | Jul 14, 2025 | Dec 20, 2025 | Mar 19, 2026 | ~14 months |

These are article-history examples only. Do not infer typical review speed, desk-reject probability, or expected acceptance timing from this small set.

---

## Withdrawal

Authors may withdraw a manuscript at any stage:
- Before submission decision: notify the editor through ScholarOne or the editorial office
- After Major Revision invitation but before resubmission: notify the editor (this is acceptable practice)
- After resubmission but before final decision: requires editor agreement
- After acceptance: very strongly discouraged (and ethically dubious)

---

## Resubmission to SS after rejection

If a paper is rejected from SS:
- The same paper cannot be resubmitted without substantial revision (typically a new RQ or new contribution framing)
- A meaningfully revised paper *can* be submitted later, but the cover letter should disclose the prior submission and explain how the manuscript has changed
- Resubmissions are evaluated as new submissions; the prior review history is sometimes shared with the AE

---

## Targeting another INFORMS journal after rejection

If SS rejects with referral or you decide to retarget:
- **Organization Science** — closest overlap; macro-OB and cognition-friendly
- **Management Science** — broader (OR/OM/marketing); formal modeling welcome
- **Information Systems Research** — for IT/AI-system papers
- **Manufacturing & Service Operations Management** — for operations-strategy work

Outside INFORMS:
- **SMJ** — broader empirical strategy; less Carnegie-specific
- **AMJ** — empirical management; lower theoretical-movement bar
- **AMD** — phenomenon-driven discoveries; lower theory bar
- **AMR** — pure theory; higher bar than SS for theory-only papers
- **JBR** — broader business scope; lower theoretical-movement bar
