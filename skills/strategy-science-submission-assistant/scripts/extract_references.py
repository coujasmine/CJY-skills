#!/usr/bin/env python3
"""Extract likely references from a manuscript reference list or BibTeX file.

This is a heuristic parser for audit preparation. It does not verify that a
reference exists; pair it with scripts/verify_references.py.

Usage:
  python scripts/extract_references.py references.txt
  python scripts/extract_references.py --json references.bib
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Za-z0-9]+\b", re.IGNORECASE)
YEAR_RE = re.compile(r"\b(19|20)\d{2}[a-z]?\b")
BIB_ENTRY_RE = re.compile(r"@\w+\s*\{\s*([^,]+)\s*,(.*?)\n\}", re.DOTALL)
BIB_FIELD_RE = re.compile(r"(\w+)\s*=\s*[\{\"](.+?)[\}\"]\s*,?", re.DOTALL)


@dataclass
class Reference:
    ref_slug: str
    raw: str
    title: str | None = None
    authors: str | None = None
    year: str | None = None
    source: str | None = None
    doi: str | None = None


def slugify(value: str, fallback: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9]+", "-", value.lower()).strip("-")
    return cleaned[:80] or fallback


def read_text(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8")
    return sys.stdin.read()


def parse_bibtex(text: str) -> list[Reference]:
    refs: list[Reference] = []
    for key, body in BIB_ENTRY_RE.findall(text):
        fields = {name.lower(): re.sub(r"\s+", " ", value).strip() for name, value in BIB_FIELD_RE.findall(body)}
        year = fields.get("year")
        title = fields.get("title")
        authors = fields.get("author")
        doi = fields.get("doi")
        source = fields.get("journal") or fields.get("booktitle") or fields.get("publisher")
        refs.append(
            Reference(
                ref_slug=slugify(key, f"ref-{len(refs)+1}"),
                raw=f"@entry{{{key}, ...}}",
                title=title,
                authors=authors,
                year=year,
                source=source,
                doi=doi,
            )
        )
    return refs


def split_reference_lines(text: str) -> list[str]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return []
    refs: list[str] = []
    current: list[str] = []
    for line in lines:
        starts_new = bool(YEAR_RE.search(line)) and (
            not current
            or re.match(r"^[A-Z][A-Za-z'`-]+,?\s+[A-Z]", line)
            or re.match(r"^\[\d+\]", line)
        )
        if starts_new and current:
            refs.append(" ".join(current))
            current = [line]
        else:
            current.append(line)
    if current:
        refs.append(" ".join(current))
    return refs


def parse_plain_references(text: str) -> list[Reference]:
    refs: list[Reference] = []
    for idx, raw in enumerate(split_reference_lines(text), start=1):
        doi_match = DOI_RE.search(raw)
        year_match = YEAR_RE.search(raw)
        year = year_match.group(0) if year_match else None
        authors = raw[: year_match.start()].strip(" .") if year_match else None
        title = None
        source = None
        if year_match:
            after_year = raw[year_match.end() :].lstrip(". ")
            parts = [part.strip() for part in after_year.split(".") if part.strip()]
            if parts:
                title = parts[0]
            if len(parts) > 1:
                source = parts[1]
        slug_source = f"{authors or 'ref'}-{year or idx}-{title or ''}"
        refs.append(
            Reference(
                ref_slug=slugify(slug_source, f"ref-{idx}"),
                raw=raw,
                title=title,
                authors=authors,
                year=year,
                source=source,
                doi=doi_match.group(0) if doi_match else None,
            )
        )
    return refs


def parse_references(text: str) -> list[Reference]:
    if re.search(r"@\w+\s*\{", text):
        refs = parse_bibtex(text)
        if refs:
            return refs
    return parse_plain_references(text)


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract likely reference metadata.")
    parser.add_argument("path", nargs="?", help="Reference file; stdin if omitted.")
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    args = parser.parse_args()

    refs = parse_references(read_text(args.path))
    if args.json:
        print(json.dumps([asdict(ref) for ref in refs], indent=2, ensure_ascii=False))
        return 0

    print(f"Extracted {len(refs)} likely reference(s).")
    for ref in refs:
        print(f"- {ref.ref_slug}")
        print(f"  title: {ref.title or '[TITLE NOT PARSED]'}")
        print(f"  authors: {ref.authors or '[AUTHORS NOT PARSED]'}")
        print(f"  year: {ref.year or '[YEAR NOT PARSED]'}")
        print(f"  doi: {ref.doi or '[DOI NOT FOUND]'}")
    return 0 if refs else 1


if __name__ == "__main__":
    raise SystemExit(main())

