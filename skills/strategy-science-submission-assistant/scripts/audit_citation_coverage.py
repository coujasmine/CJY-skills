#!/usr/bin/env python3
"""Audit in-text citation coverage against a reference list.

This script checks the mechanical reconciliation layer that sits between
``extract_citation_contexts.py`` and ``verify_references.py``:

1. Every in-text author-year citation should have a matching reference entry.
2. Every parsed reference entry should be cited in the manuscript body.
3. Duplicate first-author/year reference keys should be called out as ambiguous.

It does not judge whether a source supports a claim.

Usage:
  python scripts/audit_citation_coverage.py manuscript.txt references.txt
  python scripts/audit_citation_coverage.py manuscript.txt references.bib --json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

try:
    from extract_references import Reference, parse_references, slugify
except ImportError:  # pragma: no cover - fallback for unusual execution paths
    sys.path.append(str(Path(__file__).resolve().parent))
    from extract_references import Reference, parse_references, slugify


REFERENCE_HEADING_RE = re.compile(
    r"(?im)^\s*(?:#+\s*)?(?:references|bibliography|works cited)\s*$"
)
PAREN_WITH_YEAR_RE = re.compile(r"\((?P<content>[^()]{0,500}?(?:19|20)\d{2}[a-z]?[^()]*)\)")
AUTHOR_YEAR_IN_PAREN_RE = re.compile(
    r"(?P<authors>[A-Z][A-Za-z'`.-]+(?:\s+(?:and|&)\s+[A-Z][A-Za-z'`.-]+|\s+et\s+al\.)?)"
    r"\s*,?\s+(?P<year>(?:19|20)\d{2}[a-z]?)"
)
NARRATIVE_CITATION_RE = re.compile(
    r"\b(?P<authors>[A-Z][A-Za-z'`.-]+(?:\s+(?:and|&)\s+[A-Z][A-Za-z'`.-]+|\s+et\s+al\.)?)"
    r"\s*\(\s*(?P<year>(?:19|20)\d{2}[a-z]?)\s*\)"
)
PANDOC_CITATION_RE = re.compile(r"\[(?P<body>[^\]]*@[A-Za-z0-9_:\-][^\]]*)\]")
PANDOC_KEY_RE = re.compile(r"@(?P<key>[A-Za-z0-9_:\-]+)")


@dataclass(frozen=True)
class CitationMention:
    key: str
    display: str
    raw: str
    line: int
    context: str
    kind: str


@dataclass(frozen=True)
class ReferenceEntry:
    ref_slug: str
    display: str
    keys: tuple[str, ...]
    title: str | None
    authors: str | None
    year: str | None
    raw: str


def read_text(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8")
    return sys.stdin.read()


def manuscript_body(text: str) -> str:
    """Drop the reference section when a full manuscript is supplied."""
    match = REFERENCE_HEADING_RE.search(text)
    return text[: match.start()] if match else text


def line_number(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def line_context(text: str, pos: int, max_chars: int = 220) -> str:
    start = text.rfind("\n", 0, pos) + 1
    end = text.find("\n", pos)
    if end == -1:
        end = len(text)
    context = re.sub(r"\s+", " ", text[start:end]).strip()
    if len(context) <= max_chars:
        return context
    return context[: max_chars - 3].rstrip() + "..."


def normalize_surname(value: str | None) -> str:
    if not value:
        return ""
    value = re.sub(r"\bet\s+al\.?\b", "", value, flags=re.IGNORECASE)
    value = re.split(r"\s+(?:and|&)\s+", value, maxsplit=1, flags=re.IGNORECASE)[0]
    value = value.strip(" ,.;()[]")
    if "," in value:
        value = value.split(",", 1)[0]
    elif " and " in value.lower():
        value = value.split()[0]
    else:
        tokens = re.findall(r"[A-Za-z][A-Za-z'`.-]*", value)
        value = tokens[0] if tokens else value
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def citation_key(authors: str, year: str) -> str | None:
    surname = normalize_surname(authors)
    if not surname or not year:
        return None
    return f"ay:{surname}:{year.lower()}"


def display_author_year(authors: str, year: str) -> str:
    author = re.sub(r"\s+", " ", authors).strip(" ,.;")
    return f"{author} {year}"


def iter_author_year_mentions(text: str) -> Iterable[CitationMention]:
    body = manuscript_body(text)

    for paren_match in PAREN_WITH_YEAR_RE.finditer(body):
        content = paren_match.group("content")
        for inner_match in AUTHOR_YEAR_IN_PAREN_RE.finditer(content):
            authors = inner_match.group("authors")
            year = inner_match.group("year")
            key = citation_key(authors, year)
            if not key:
                continue
            start = paren_match.start() + inner_match.start()
            yield CitationMention(
                key=key,
                display=display_author_year(authors, year),
                raw=inner_match.group(0),
                line=line_number(body, start),
                context=line_context(body, start),
                kind="author_year",
            )

    for match in NARRATIVE_CITATION_RE.finditer(body):
        authors = match.group("authors")
        year = match.group("year")
        key = citation_key(authors, year)
        if not key:
            continue
        yield CitationMention(
            key=key,
            display=display_author_year(authors, year),
            raw=match.group(0),
            line=line_number(body, match.start()),
            context=line_context(body, match.start()),
            kind="narrative",
        )


def iter_pandoc_mentions(text: str) -> Iterable[CitationMention]:
    body = manuscript_body(text)
    for block in PANDOC_CITATION_RE.finditer(body):
        for key_match in PANDOC_KEY_RE.finditer(block.group("body")):
            raw_key = key_match.group("key")
            slug = slugify(raw_key, raw_key)
            start = block.start() + key_match.start()
            yield CitationMention(
                key=f"bib:{slug}",
                display=f"@{raw_key}",
                raw=f"@{raw_key}",
                line=line_number(body, start),
                context=line_context(body, start),
                kind="pandoc",
            )


def extract_citation_mentions(text: str) -> list[CitationMention]:
    mentions = list(iter_author_year_mentions(text))
    mentions.extend(iter_pandoc_mentions(text))
    mentions.sort(key=lambda item: (item.line, item.display, item.kind))
    return mentions


def first_reference_surname(authors: str | None) -> str:
    if not authors:
        return ""
    first = re.split(r"\s+and\s+|;", authors, maxsplit=1, flags=re.IGNORECASE)[0].strip()
    if "," in first:
        first = first.split(",", 1)[0]
    else:
        tokens = re.findall(r"[A-Za-z][A-Za-z'`.-]*", first)
        if len(tokens) >= 2 and " and " in authors.lower():
            first = tokens[-1]
        elif tokens:
            first = tokens[0]
    return normalize_surname(first)


def reference_keys(ref: Reference) -> tuple[str, ...]:
    keys: list[str] = []
    surname = first_reference_surname(ref.authors)
    if surname and ref.year:
        keys.append(f"ay:{surname}:{ref.year.lower()}")
    if ref.ref_slug:
        keys.append(f"bib:{ref.ref_slug}")
    return tuple(dict.fromkeys(keys))


def reference_display(ref: Reference) -> str:
    author = ref.authors or "[AUTHORS NOT PARSED]"
    year = ref.year or "[YEAR NOT PARSED]"
    title = ref.title or "[TITLE NOT PARSED]"
    return f"{author} {year}. {title}"


def build_reference_entries(reference_text: str) -> list[ReferenceEntry]:
    entries: list[ReferenceEntry] = []
    for ref in parse_references(reference_text):
        entries.append(
            ReferenceEntry(
                ref_slug=ref.ref_slug,
                display=reference_display(ref),
                keys=reference_keys(ref),
                title=ref.title,
                authors=ref.authors,
                year=ref.year,
                raw=ref.raw,
            )
        )
    return entries


def grouped_mentions(mentions: list[CitationMention]) -> dict[str, dict[str, object]]:
    grouped: dict[str, dict[str, object]] = {}
    for mention in mentions:
        item = grouped.setdefault(
            mention.key,
            {
                "key": mention.key,
                "display": mention.display,
                "kind": mention.kind,
                "count": 0,
                "locations": [],
            },
        )
        item["count"] = int(item["count"]) + 1
        item["locations"].append(
            {
                "line": mention.line,
                "raw": mention.raw,
                "context": mention.context,
            }
        )
    return grouped


def audit_coverage(manuscript_text: str, reference_text: str) -> dict[str, object]:
    mentions = extract_citation_mentions(manuscript_text)
    grouped = grouped_mentions(mentions)
    references = build_reference_entries(reference_text)

    index: dict[str, list[ReferenceEntry]] = {}
    for ref in references:
        for key in ref.keys:
            index.setdefault(key, []).append(ref)

    matched_ref_slugs: set[str] = set()
    missing: list[dict[str, object]] = []
    ambiguous: list[dict[str, object]] = []
    matched: list[dict[str, object]] = []

    for key, citation in grouped.items():
        candidates = index.get(key, [])
        if not candidates:
            missing.append(citation)
            continue
        if len(candidates) > 1:
            ambiguous.append(
                {
                    **citation,
                    "candidate_references": [asdict(candidate) for candidate in candidates],
                }
            )
            continue
        ref = candidates[0]
        matched_ref_slugs.add(ref.ref_slug)
        matched.append({**citation, "reference": asdict(ref)})

    uncited = [ref for ref in references if ref.ref_slug not in matched_ref_slugs]
    unparsed = [ref for ref in references if not any(key.startswith("ay:") for key in ref.keys)]

    return {
        "summary": {
            "citation_mentions": len(mentions),
            "unique_citations": len(grouped),
            "references": len(references),
            "matched_unique_citations": len(matched),
            "missing_reference_citations": len(missing),
            "uncited_references": len(uncited),
            "ambiguous_citations": len(ambiguous),
            "unparsed_reference_keys": len(unparsed),
        },
        "matched_citations": matched,
        "missing_reference_citations": missing,
        "uncited_references": [asdict(ref) for ref in uncited],
        "ambiguous_citations": ambiguous,
        "unparsed_reference_keys": [asdict(ref) for ref in unparsed],
    }


def print_issue_list(title: str, items: list[dict[str, object]]) -> None:
    print(title)
    if not items:
        print("- None")
        return
    for item in items:
        print(f"- {item['display']}")
        locations = item.get("locations") or []
        for location in locations[:3]:
            print(f"  line {location['line']}: {location['context']}")
        if len(locations) > 3:
            print(f"  ... {len(locations) - 3} more mention(s)")
        candidates = item.get("candidate_references") or []
        for candidate in candidates:
            print(f"  candidate: {candidate['display']}")


def print_reference_list(title: str, refs: list[dict[str, object]]) -> None:
    print(title)
    if not refs:
        print("- None")
        return
    for ref in refs:
        print(f"- {ref['display']}")
        print(f"  key(s): {', '.join(ref['keys']) if ref['keys'] else '[NO MATCHABLE KEY]'}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit citation/reference coverage.")
    parser.add_argument("manuscript", help="Manuscript text file.")
    parser.add_argument("references", help="Reference list or BibTeX file.")
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    args = parser.parse_args()

    result = audit_coverage(read_text(args.manuscript), read_text(args.references))
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0

    summary = result["summary"]
    print("Citation Coverage Audit")
    print(f"Citation mentions: {summary['citation_mentions']}")
    print(f"Unique citations: {summary['unique_citations']}")
    print(f"References: {summary['references']}")
    print(f"Matched unique citations: {summary['matched_unique_citations']}")
    print()
    print_issue_list("Cited in manuscript but missing from references:", result["missing_reference_citations"])
    print()
    print_reference_list("In references but not cited in manuscript:", result["uncited_references"])
    print()
    print_issue_list("Ambiguous citation matches:", result["ambiguous_citations"])
    print()
    print_reference_list("References without author-year match keys:", result["unparsed_reference_keys"])

    has_issues = any(
        summary[field]
        for field in (
            "missing_reference_citations",
            "uncited_references",
            "ambiguous_citations",
            "unparsed_reference_keys",
        )
    )
    return 1 if has_issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
