---
file: ss_submission_workflow.md
purpose: The end-to-end Strategy Science / INFORMS submission process — what happens, when, what the user needs to prepare. Used in PACKAGE mode and as background for AUDIT/REVIEW.
last_verified: 2026-05-31
---

# Strategy Science Submission Workflow

## Contents

- Stage 1: Pre-submission preparation
- Stage 2: Submission
- Stage 3: Senior Editor screening
- Stage 4: External review
- Stage 5: First-round decision
- Stage 6: Revision window (within 3 months; no later than 1 year)
- Stage 7: Subsequent review rounds
- Stage 8: Final acceptance and final files
- Appeals
- Special Issue submissions
- Common timing benchmarks (from the 4 exemplars)
- Withdrawal
- Resubmission to SS after rejection
- Targeting another INFORMS journal after rejection


This file describes the INFORMS submission process for Strategy Science. It is descriptive (what happens) rather than prescriptive (what to write); for writing guidance, see other reference files.

> Verify current portal URLs and policies at https://pubsonline.informs.org/page/stsc/submission-guidelines and file-preparation rules at https://pubsonline.informs.org/authorportal/file-preparation before final submission. INFORMS updates submission systems periodically.

---

## Stage 1: Pre-submission preparation

### Materials to assemble

1. **Blinded manuscript source file** (the body of the paper without author identifiers)
   - PDF upload is required for ScholarOne proofing; `.doc` and `.docx` are also allowed
   - Double-spaced, 11-point standard font such as Times New Roman
   - 1-inch margins on all sides
   - Standard fonts embedded; no custom fonts
   - All-inclusive length <=35 pages unless the cover letter explicitly explains the exception
   - Numbered lines (optional but reviewer-friendly)
   - All identifying information removed (see `ss_disclosures.md` and `ss_scope_and_format.md`)

2. **Author-identifying metadata / title-page file if requested**
   - Title
   - Authors with affiliations
   - Corresponding author email
   - Submitting author's ORCID iD (required by the current Strategy Science ScholarOne instructions); collect coauthor ORCID iDs where the portal requests them
   - Funding sources (full institutional names)
   - Acknowledgments (full)
   - Author contributions, if requested or planned for final files
   - Conflict of interest disclosure
   - Keep this material out of the blinded manuscript

3. **Online appendix / supplementary materials** (if applicable)
   - Detailed methodology
   - Robustness checks
   - Pre-registration materials
   - Code (often hosted on OSF or GitHub)

4. **Figure source-file readiness** (for production and accepted-file packaging)
   - Editable vector source for graphs/drawings where possible
   - Images at least 300 dpi; high-quality PDFs at 600 dpi or higher with embedded fonts
   - Standard fonts only
   - EPS/TIFF/PDF/Word/PowerPoint/Illustrator/Excel files prepared as appropriate
   - Grayscale conversion checked for all color figures intended for online color / print grayscale
   - Permission/copyright status confirmed for reused figures

5. **Cover letter** (see `cover_letter_and_response.md`)
   - Addressed to the Editor (or Guest Editors for SI)
   - States the journal target (regular issue or SI)
   - Summarizes the contribution
   - States novelty and lack of prior submission overlap
   - Confirms compliance with submission requirements (blinding, conflicts/overlap disclosures, funding, and other portal prompts)
   - Includes any brief justification if the manuscript exceeds 35 pages

6. **Pre-registration link** (if applicable)
   - For blinded review: anonymized OSF view link
   - For final acceptance: full URL

7. **Disclosures** (see `ss_disclosures.md`)
   - Possible conflicts of interest
   - Funding
   - Prior/substantially overlapping work and use of the same database
   - AI-use transparency if AI assisted the manuscript or served as a measurement/coding tool
   - Data access/retention plan if data may be requested or a data statement is needed
   - IRB approval

### Pre-submission QA

Run through:
- `scripts/check_abstract_word_count.py` -> manuscript abstract <=200 words; ScholarOne abstract field <=250 words
- `scripts/check_keywords_count.py` -> 3-10 keywords
- `scripts/scan_causal_verbs.py` → no over-claiming
- `scripts/scan_ai_style_markers.py` → no systemic AI-style markers
- Disclosure checklist from `ss_disclosures.md` → required ethics/funding/COI/overlap items ready; recommended AI/data transparency language prepared when applicable
- Figure/file preparation checklist from `ss_scope_and_format.md` → fonts embedded; no custom fonts; image/vector files meet INFORMS production specifications
- Desk-reject triggers checklist from `ss_desk_reject_triggers.md` → no HIGH triggers

---

## Stage 2: Submission

1. Visit https://pubsonline.informs.org/page/stsc/submission-guidelines and use the Strategy Science ScholarOne Manuscripts link
2. Create account or sign in
3. Step 1: choose manuscript type (e.g., Original Manuscript), enter title, and paste the abstract
4. Step 2: enter attributes:
   - 3-10 keywords describing the paper's theoretical and methodological orientation
5. Step 3: enter authors and institutions:
   - Authors and affiliations
   - Submitting author's ORCID iD
6. Step 4: enter preferred/nonpreferred reviewers and any Senior Editor recommendations
   - Authors may nominate up to three reviewers with suitable expertise
   - Do not suggest reviewers or Senior Editors with conflicts of interest: major professor/student relationships, same institution, or coauthors on completed/in-progress work during the last three years
7. Step 5: details and comments
   - Add the cover letter in the text box or as a separate file
   - The cover letter/comments are viewed by the Editor-in-Chief and Senior Editor, not by reviewers
   - Denote funding
   - Certify compliance with journal and INFORMS ethical policies
   - Disclose possible perceived conflicts, prior/substantially overlapping work, related conference proceedings/book chapters/journal submissions, and use of the same database where relevant
   - Conference submission at the same time is allowed; simultaneous review at another journal is not
8. Step 6: upload files
   - Upload as many files as needed; ScholarOne combines them into a single PDF for peer review
   - For revisions, include only the latest set of files
9. Step 7: review and submit
   - Review all prior steps
   - View the generated PDF proof; this is required
   - Select "Submit" when complete

You will receive an automated email confirmation with a submission ID.

---

## Stage 3: Senior Editor screening

The Editor-in-Chief or a designated Senior Editor reviews the submission:

- **Format compliance**: blinding, disclosures, length
- **Scope fit**: does the paper fit SS's scope?
- **Quality threshold**: is the paper coherent enough for external review?

Possible outcomes:
- **Desk reject**: paper does not pass the editorial screen. Common reasons: mis-fit for SS, fundamental contribution issues, format violations. The author receives a brief reject letter from the editor.
- **Desk-reject with encouragement to retarget**: editor suggests an alternative outlet (rare but happens).
- **Send out for review**: the Senior Editor manages reviewer input and retains decision authority.

Do not report desk-reject percentages unless the user supplies a verified source. Treat desk rejection as a qualitative risk, not a numeric prediction.

---

## Stage 4: External review

The Senior Editor typically invites expert reviewers from the Editorial Review Board or the broader field. Do not report exact timing unless the user supplies a verified source.

Reviewers see:
- Blinded manuscript
- Cover letter/comments are for the Editor-in-Chief and Senior Editor; reviewers do not see the Step 5 cover-letter text according to the current official guide
- Online appendix

Reviewers do NOT see:
- Author-identifying metadata/title-page file
- Author identities (in normal cases)

Each reviewer submits:
- A free-text review (typically 2-5 pages)
- A confidential note to the Senior Editor (sometimes)
- A recommendation (Accept / Minor / Major / Reject)

The Senior Editor incorporates reviewer evaluations, but the ultimate decision is the Senior Editor's rather than a vote of the reviewers.

---

## Stage 5: First-round decision

The Senior Editor or Editor-in-Chief issues one of:

- **Accept**: rare on first round
- **Minor revision**: small set of clearly addressable issues; revision typically returns in 1-2 months
- **Major revision**: substantive issues; revision typically returns in 3-6 months
- **Reject**: paper will not be revised further at SS
- **Reject with referral**: editor suggests resubmitting to an INFORMS sister journal (e.g., Organization Science)

The author receives:
- The EIC decision letter
- Reviewer reports (anonymized)
- The Senior Editor's letter (sometimes summarizing the reviewers)

---

## Stage 6: Revision window (within 3 months; no later than 1 year)

If a revision is invited, the official Strategy Science guide says authors should resubmit within three months and no later than one year from the revision request date.

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
   - Updated author metadata/title-page file if needed
   - Cover letter to the editor
   - Response letter (separate file, addressed to the Senior Editor and reviewers)
   - Tracked-changes or marked version if requested by ScholarOne/editorial instructions

---

## Stage 7: Subsequent review rounds

The original reviewers are typically re-invited. They evaluate:
- Whether each point was addressed substantively
- Whether new issues have emerged

The Senior Editor or Editor-in-Chief issues a subsequent decision:
- **Accept**: revisions satisfied reviewers
- **Minor revision**: small remaining cleanups
- **Major revision (rare at this stage)**: serious concerns not addressed; another round expected
- **Reject**: revisions did not satisfy reviewers; paper is unlikely to be accepted in further rounds

---

## Stage 8: Final acceptance and final files

When the paper is accepted:

The official guide asks authors to upload final files within 14 days of the acceptance decision letter. The acceptance decision is not considered binding until final files have been received.

1. **Final manuscript preparation**:
   - Author names and affiliations restored
   - Full Acknowledgments restored
   - Funding statement with institutional names restored
   - Pre-registration full URL restored
   - All disclosures finalized
   - If the paper is posted on a working paper website, remove the text or any link to the full text on acceptance and ensure any working-paper copyright can be transferred to INFORMS

2. **Final files uploaded through "Manuscripts Accepted for First Look"**:
   - Source file of the manuscript in Microsoft Word or LaTeX, with a cover page containing full author contact information and keywords
   - PDF of the main paper
   - PDF of online appendixes/e-companions (not edited; source files not needed)
   - Figure source files that meet INFORMS file-preparation specs: standard embedded fonts, no custom fonts, editable vector source where appropriate, original images at least 300 dpi, high-quality editable PDFs at 600 dpi or higher, EPS/TIFF/PDF/Word/PowerPoint/Illustrator/Excel formats as applicable
   - Signed copyright transfer form
   - Completed editorial checklist
   - Brief author biography for the published paper

3. **Copyediting and proofs**:
   - INFORMS production sends copyedited proofs
   - Author reviews and signs off
   - Open Access decision finalized; the current official guide lists a US$3,000 INFORMS Open Option fee and a separate IOO publication license
   - Color figures default to online color / print grayscale unless approved print color charges are paid; authors cannot replace black-and-white figures with color figures after production starts

4. **Online publication**:
   - "Articles in Advance" version posted (online, with DOI, before issue assignment)
   - Final issue assignment when ready

5. **DOI and citation**:
   - Use the DOI and citation information assigned by INFORMS production

---

## Appeals

Strategy Science considers appeals only for large technical errors that plausibly shaped the editorial judgment, not because authors believe the reviewers or editors undervalued the paper. Appeals should:

- Document the specific error and its magnitude
- Be directed to the Editor-in-Chief
- Be sent no sooner than 30 days and no later than 180 days after the decision date
- Copy all authors

Appealing authors should know that their identities become part of the journal record and may be known to future editors. The official guide notes that reversals are uncommon.

---

## Special Issue submissions

For SI submissions, the workflow is similar with these differences:

- Submission is through ScholarOne, with the SI name selected when the portal offers that option
- Guest Editors or designated editors may handle the editorial screening and review process, depending on the call
- Do not infer accelerated timelines unless the special-issue call states them
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
- Resubmissions are evaluated as new submissions; the prior review history may be shared with the Senior Editor

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
