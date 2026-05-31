#!/usr/bin/env python3
"""Verify reference existence metadata for Strategy Science citation audits.

By default this performs an offline structural audit. Add --online to query
Crossref, OpenAlex, and Semantic Scholar public APIs. Online checks require
network access and may be rate-limited by the providers.

Usage:
  python scripts/verify_references.py references.txt
  python scripts/verify_references.py --online --json references.bib
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from dataclasses import asdict
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

try:
    from extract_references import Reference, parse_references
except ImportError:  # pragma: no cover - fallback for unusual execution paths
    sys.path.append(str(Path(__file__).resolve().parent))
    from extract_references import Reference, parse_references


USER_AGENT = "CJY-Skills-Strategy-Science-Citation-Audit/1.0 (mailto:example@example.com)"


def normalize_title(title: str | None) -> str:
    if not title:
        return ""
    title = re.sub(r"<[^>]+>", "", title)
    title = re.sub(r"[^A-Za-z0-9]+", " ", title.lower())
    return re.sub(r"\s+", " ", title).strip()


def title_similarity(a: str | None, b: str | None) -> float:
    na = normalize_title(a)
    nb = normalize_title(b)
    if not na or not nb:
        return 0.0
    return round(SequenceMatcher(None, na, nb).ratio(), 3)


def request_json(url: str) -> dict[str, Any] | None:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=12) as response:  # noqa: S310 - user-invoked metadata API
            return json.loads(response.read().decode("utf-8", errors="replace"))
    except Exception:
        return None


def crossref_lookup(ref: Reference) -> dict[str, Any]:
    if ref.doi:
        url = f"https://api.crossref.org/works/{urllib.parse.quote(ref.doi)}"
    elif ref.title:
        params = urllib.parse.urlencode({"query.title": ref.title, "rows": 1})
        url = f"https://api.crossref.org/works?{params}"
    else:
        return {"status": "NOT_CHECKED", "title": None, "doi": None, "similarity": 0.0}

    data = request_json(url)
    if not data:
        return {"status": "ERROR", "title": None, "doi": None, "similarity": 0.0}
    message = data.get("message", {})
    if "items" in message:
        items = message.get("items") or []
        message = items[0] if items else {}
    title_list = message.get("title") or []
    found_title = title_list[0] if title_list else None
    found_doi = message.get("DOI")
    sim = title_similarity(ref.title, found_title)
    status = "MATCHED" if (ref.doi and found_doi and ref.doi.lower() == found_doi.lower()) or sim >= 0.86 else "WEAK_MATCH"
    return {"status": status, "title": found_title, "doi": found_doi, "similarity": sim}


def openalex_lookup(ref: Reference) -> dict[str, Any]:
    if ref.doi:
        doi_url = f"https://doi.org/{ref.doi}"
        url = f"https://api.openalex.org/works/{urllib.parse.quote(doi_url, safe='')}"
    elif ref.title:
        params = urllib.parse.urlencode({"search": ref.title, "per-page": 1})
        url = f"https://api.openalex.org/works?{params}"
    else:
        return {"status": "NOT_CHECKED", "title": None, "doi": None, "similarity": 0.0}

    data = request_json(url)
    if not data:
        return {"status": "ERROR", "title": None, "doi": None, "similarity": 0.0}
    item = data
    if "results" in data:
        results = data.get("results") or []
        item = results[0] if results else {}
    found_title = item.get("title") or item.get("display_name")
    found_doi = (item.get("doi") or "").replace("https://doi.org/", "") or None
    sim = title_similarity(ref.title, found_title)
    status = "MATCHED" if (ref.doi and found_doi and ref.doi.lower() == found_doi.lower()) or sim >= 0.86 else "WEAK_MATCH"
    return {"status": status, "title": found_title, "doi": found_doi, "similarity": sim}


def semantic_scholar_lookup(ref: Reference) -> dict[str, Any]:
    fields = "title,year,externalIds"
    if ref.doi:
        url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{urllib.parse.quote(ref.doi)}?fields={fields}"
    elif ref.title:
        params = urllib.parse.urlencode({"query": ref.title, "limit": 1, "fields": fields})
        url = f"https://api.semanticscholar.org/graph/v1/paper/search?{params}"
    else:
        return {"status": "NOT_CHECKED", "title": None, "doi": None, "similarity": 0.0}

    data = request_json(url)
    if not data:
        return {"status": "ERROR", "title": None, "doi": None, "similarity": 0.0}
    item = data
    if "data" in data:
        results = data.get("data") or []
        item = results[0] if results else {}
    found_title = item.get("title")
    external_ids = item.get("externalIds") or {}
    found_doi = external_ids.get("DOI")
    sim = title_similarity(ref.title, found_title)
    status = "MATCHED" if (ref.doi and found_doi and ref.doi.lower() == found_doi.lower()) or sim >= 0.86 else "WEAK_MATCH"
    return {"status": status, "title": found_title, "doi": found_doi, "similarity": sim}


def offline_status(ref: Reference) -> dict[str, Any]:
    missing = []
    for field in ("title", "authors", "year"):
        if not getattr(ref, field):
            missing.append(field)
    risk = "MEDIUM" if missing else "LOW"
    if not ref.doi:
        risk = "MEDIUM"
    return {
        "missing_fields": missing,
        "metadata_risk": risk,
        "recommended_action": "Add DOI or source locator before submission." if not ref.doi else "Ready for online verification.",
    }


def audit_reference(ref: Reference, online: bool, sleep_seconds: float) -> dict[str, Any]:
    result: dict[str, Any] = {
        **asdict(ref),
        "crossref_status": "NOT_CHECKED",
        "openalex_status": "NOT_CHECKED",
        "semantic_scholar_status": "NOT_CHECKED",
        "doi_match": False,
        "title_similarity": 0.0,
        "metadata_risk": "MEDIUM",
        "recommended_action": "",
    }
    result.update(offline_status(ref))
    if not online:
        return result

    crossref = crossref_lookup(ref)
    time.sleep(sleep_seconds)
    openalex = openalex_lookup(ref)
    time.sleep(sleep_seconds)
    semantic = semantic_scholar_lookup(ref)

    result["crossref_status"] = crossref["status"]
    result["openalex_status"] = openalex["status"]
    result["semantic_scholar_status"] = semantic["status"]
    similarities = [crossref["similarity"], openalex["similarity"], semantic["similarity"]]
    result["title_similarity"] = max(similarities)

    found_dois = [item.get("doi") for item in (crossref, openalex, semantic) if item.get("doi")]
    result["doi_match"] = bool(ref.doi and any(ref.doi.lower() == str(doi).lower() for doi in found_dois))
    matched_count = sum(1 for item in (crossref, openalex, semantic) if item["status"] == "MATCHED")
    weak_count = sum(1 for item in (crossref, openalex, semantic) if item["status"] == "WEAK_MATCH")
    if matched_count >= 2 or result["doi_match"]:
        result["metadata_risk"] = "LOW"
        result["recommended_action"] = "Metadata appears consistent; add locator anchors for core claims."
    elif matched_count == 1 or weak_count >= 1:
        result["metadata_risk"] = "MEDIUM"
        result["recommended_action"] = "Check title, DOI, year, and author spelling manually."
    else:
        result["metadata_risk"] = "HIGH"
        result["recommended_action"] = "Treat as high-risk until the source is manually verified."
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify reference metadata.")
    parser.add_argument("path", nargs="?", help="Reference file; stdin if omitted.")
    parser.add_argument("--online", action="store_true", help="Query Crossref, OpenAlex, and Semantic Scholar.")
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    parser.add_argument("--sleep", type=float, default=0.2, help="Pause between online API calls.")
    args = parser.parse_args()

    text = Path(args.path).read_text(encoding="utf-8") if args.path else sys.stdin.read()
    refs = parse_references(text)
    results = [audit_reference(ref, args.online, args.sleep) for ref in refs]
    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return 0

    mode = "online" if args.online else "offline"
    print(f"Reference Existence Check ({mode})")
    print(f"References: {len(results)}")
    print()
    for item in results:
        print(f"- {item['ref_slug']}")
        print(f"  title: {item.get('title') or '[TITLE NOT PARSED]'}")
        print(
            "  status: "
            f"Crossref={item['crossref_status']}; "
            f"OpenAlex={item['openalex_status']}; "
            f"SemanticScholar={item['semantic_scholar_status']}"
        )
        print(f"  DOI match: {item['doi_match']}; title similarity: {item['title_similarity']}")
        print(f"  risk: {item['metadata_risk']}")
        print(f"  action: {item['recommended_action']}")
    return 1 if any(item["metadata_risk"] == "HIGH" for item in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())

