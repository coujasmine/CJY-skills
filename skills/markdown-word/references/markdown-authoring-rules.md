# Markdown authoring rules

How to write Markdown so this skill produces clean journal-formatted Word. None of these rules are this skill's invention — they're either standard Pandoc Markdown or the minimum hooks the post-processor needs to recognize tables/figures/captions.

---

## 0. YAML front matter (strongly recommended)

Put the title, authors, abstract, and keywords in a YAML block at the very top of the file. Pandoc maps these to dedicated Word styles (`Title`, `Author`, `Abstract`, `AbstractTitle`) — which means the title is **not** numbered as "1. Your Title" and the abstract heading is **not** numbered as "1.1. Abstract".

```yaml
---
title: TMT Myopia and AI Adoption in U.S. Public Firms, 2015–2024
author:
  - Author One, University of Somewhere
  - Author Two, Another University
abstract: |
  Single-paragraph abstract here. Keep within the journal's word limit
  (see the YAML config: `abstract.word_limit`).
keywords: TMT cognition; AI adoption; temporal orientation; longitudinal
---

# Introduction

First body section starts here. This becomes "1. Introduction".
```

Without YAML front matter, the first `# Title` line becomes "Heading 1" and gets numbered "1. Title …" — almost never what you want. The sample paper at [`examples/sample-paper.md`](../examples/sample-paper.md) shows the correct pattern.

---

## 1. Structure

### Heading levels
Use ATX-style headings (`#`, `##`, `###`, `####`). With YAML front matter (recommended), start at `#` for the first body section (Introduction). Don't skip levels:

```markdown
# Introduction

## Background

### Prior literature

## Hypotheses
```

The post-processor numbers H1–H4 in document order: `1.`, `1.1.`, `1.1.1.`, `1.1.1.1.`. Don't write the numbers yourself — they'll be stripped and replaced.

If you do write them and they disagree with the counter (e.g., you skipped a section), the script silently rewrites to its own count. To opt out of auto-numbering, set `headings.numbering: none` in the journal YAML.

### Paragraphs and emphasis
Standard Markdown:
- Blank line between paragraphs.
- `*italic*` or `_italic_` for italic; `**bold**` for bold.
- `> quote` for blockquotes.

---

## 2. Tables

### Pipe tables
Always use pipe tables (the most common Markdown table syntax):

```markdown
| Variable | Mean | SD   | Min  | Max  |
|----------|------|------|------|------|
| Age      | 35.2 | 8.1  | 22   | 65   |
| Income   | 48.5 | 12.3 | 18.0 | 95.0 |
```

The first row is treated as the header. The post-processor will:
- Bold the header row.
- Apply APA three-line borders (top + under-header + bottom; no verticals).
- Repeat the header row across page breaks.
- Prevent rows from splitting across pages.

### Table captions

Put a caption paragraph **immediately before** the table. Two equivalent forms:

```markdown
Table: Descriptive statistics for the analytic sample (N = 1,847).

| Variable | Mean | SD |
| ...
```

or the Pandoc-native form (caption AFTER, prefixed with a colon):

```markdown
| Variable | Mean | SD |
| ...

: Descriptive statistics for the analytic sample (N = 1,847).
```

Both work. The post-processor renumbers all captions in document order, so don't write "Table 1:", just "Table:".

### Table notes
Add a paragraph immediately after the table starting with "Note." or "Notes." — it's preserved as-is. Example:

```markdown
| ...table... |

*Note.* Standard errors clustered by firm in parentheses. *p* < .05.
```

This skill does not auto-format the notes paragraph (other than the APA convention is that `Note.` is italic, which you write yourself).

### Wide tables
For very wide tables, switch the section to landscape in Word manually after conversion, or split the table. The skill does not auto-rotate.

---

## 3. Figures

### Image syntax
```markdown
![Conceptual model linking TMT myopia to AI adoption.](figures/model.png)
```

- The alt text **is** the figure caption.
- Pandoc places the image and creates a caption paragraph below it.
- Captions are numbered "Figure 1", "Figure 2", … by document order (handled by `format_apa_tables.py` for tables; figures are renumbered by Pandoc's `--number-sections` if used, or kept as-is. Future enhancement: figure-renumber in `postprocess_docx.py`).

### Image paths
Use relative paths from where you run `md_to_docx.py`. Or absolute paths. Pandoc resolves them.

### Vector vs raster
- `.png`, `.jpg` work universally. For vector quality at any zoom, use `.pdf` or `.eps` (Pandoc embeds them; reviewers see crisp images).

---

## 4. Math

Inline: `$y = \beta_0 + \beta_1 x + \epsilon$`. Display:

```markdown
$$
y_{it} = \alpha_i + \beta x_{it} + \gamma z_{it} + \epsilon_{it}
$$
```

Pandoc converts both to Word's native equation editor (OMML). The post-processor does not touch math.

---

## 5. References / bibliography

### Option A — pre-format
Write the reference list in the Markdown manually under a `# References` heading, formatted per journal style. Easiest path.

### Option B — Pandoc citeproc
Cite with `[@key]` or `@key` and pass a `.bib` file:

```bash
python3 scripts/md_to_docx.py paper.md jbr \
    --bibliography refs.bib --csl apa.csl
```

You need a CSL file. Get APA 7: https://github.com/citation-style-language/styles/blob/master/apa.csl

After conversion, the reference list appears under whatever heading is named in the YAML's `references.heading_text` (default `References`).

---

## 6. Footnotes

```markdown
This is a sentence with a footnote.[^1]

[^1]: The note text. Can span multiple paragraphs if indented.
```

Pandoc handles these correctly. No post-processing needed.

---

## 7. Things this skill does NOT do

- **Citations**: you must either pre-format them or supply a .bib + .csl.
- **Spell/grammar check**: use Word or another tool after conversion.
- **Content editing**: this is a formatter, not a polisher. See sibling skill `jbr-submission-assistant` for content polishing.
- **PDF output**: use Word's Save As PDF after conversion.
- **Chinese typography**: the East Asian font fields are set defensively, but the format specs target English manuscripts.

---

## 8. The minimum viable manuscript

```markdown
---
title: Title of the Manuscript
author:
  - Author One, Affiliation
  - Author Two, Affiliation
abstract: |
  A short abstract within the journal's word limit.
keywords: strategy; innovation; AI adoption; longitudinal
---

# Introduction

The opening paragraph...

# Theory and Hypotheses

## Construct A

...

## Construct B

...

Table: Key constructs and definitions.

| Construct | Definition | Source |
|-----------|------------|--------|
| Foo       | ...        | ...    |

# Methods

...

# Results

...

# Discussion

...

# References

Reference 1...
Reference 2...
```

Run:

```bash
python3 scripts/md_to_docx.py manuscript.md jbr
```

Open the resulting `manuscript-jbr.docx` in Word, scroll through, and check the `manuscript-jbr-report.md` for any FAIL rows.
