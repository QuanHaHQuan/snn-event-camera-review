#!/usr/bin/env python3
"""Generate a conference-level search-report.md from workflow CSVs."""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from datetime import date
from pathlib import Path

NARROW_QUERIES = [
    "[VENUE YEAR] event camera",
    "[VENUE YEAR] event cameras",
    "[VENUE YEAR] dynamic vision sensor",
    "[VENUE YEAR] DVS",
    "[VENUE YEAR] visual event sensor",
    "[VENUE YEAR] event stream",
    "[VENUE YEAR] spiking neural network",
    "[VENUE YEAR] spiking neural networks",
    "[VENUE YEAR] SNN",
    "[VENUE YEAR] surrogate gradient",
    "[VENUE YEAR] ANN-to-SNN",
    "[VENUE YEAR] spiking transformer",
]

BROAD_CHECKS = [
    "[VENUE YEAR] event-based vision",
    "[VENUE YEAR] neuromorphic vision",
    "[VENUE YEAR] neuromorphic computing",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def count_levels(candidates: list[dict[str, str]], mother_count: int) -> Counter[str]:
    counts: Counter[str] = Counter(row.get("level", "E") or "E" for row in candidates)
    classified_non_e = sum(counts[level] for level in "ABCD")
    counts["E"] += max(0, mother_count - classified_non_e)
    return counts


def format_papers(rows: list[dict[str, str]]) -> list[str]:
    lines: list[str] = []
    for row in rows:
        card = row.get("card_path", "") or "Needs card generation"
        lines.append(f"- [{row.get('level', '')}] {row.get('title', 'Unknown')} ({row.get('conference', '')} {row.get('year', '')}) - {card}")
    return lines or ["- None yet."]


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate conference search-report.md.")
    parser.add_argument("--conference-dir", required=True, type=Path, help="Venue/year workflow directory")
    parser.add_argument("--venue", required=True, help="Venue name")
    parser.add_argument("--year", required=True, help="Venue year")
    parser.add_argument("--official-url", default="Unknown", help="Official source URL")
    parser.add_argument("--source-type", default="official proceedings or accepted-paper list", help="Official source type")
    parser.add_argument("--retrieval-date", default=date.today().isoformat(), help="Retrieval date")
    parser.add_argument("--main-conference-only", default="Needs human verification", help="Whether source is main conference only")
    parser.add_argument("--abstracts", default="Needs human verification", help="Abstract availability")
    parser.add_argument("--pdfs", default="Needs human verification", help="PDF availability")
    parser.add_argument("--supplementary", default="Needs human verification", help="Supplementary link availability")
    parser.add_argument("--limitations", default="Official-page parsing and automated keyword classification require human verification.")
    parser.add_argument("--external-cross-check", default="Not yet run or recorded.")
    args = parser.parse_args()

    conference_dir = args.conference_dir
    mother = read_csv(conference_dir / "mother-list.csv")
    candidates = read_csv(conference_dir / "candidates.csv")
    abc = read_csv(conference_dir / "abc-reviewed.csv")
    counts = count_levels(candidates, len(mother))
    venue_year = f"{args.venue} {args.year}"
    narrow_queries = [query.replace("[VENUE YEAR]", venue_year) for query in NARROW_QUERIES]
    broad_checks = [query.replace("[VENUE YEAR]", venue_year) for query in BROAD_CHECKS]

    lines = [
        f"# Search Report: {venue_year}",
        "",
        "## Search Summary",
        "",
        f"- Scope: main conference only",
        f"- Research topic: Spiking Neural Networks for Event Cameras",
        f"- Mother-list papers: {len(mother)}",
        f"- Raw candidates: {len(candidates)}",
        f"- A/B/C reviewed papers: {len(abc)}",
        "",
        "## Official Source",
        "",
        f"- URL: {args.official_url}",
        f"- Source type: {args.source_type}",
        f"- Retrieval date: {args.retrieval_date}",
        f"- Main conference only: {args.main_conference_only}",
        f"- Abstracts: {args.abstracts}",
        f"- PDFs: {args.pdfs}",
        f"- Supplementary links: {args.supplementary}",
        "",
        "## Mother List Statistics",
        "",
        f"- Total official main-conference papers collected: {len(mother)}",
        "- Mother list saved before filtering: yes" if mother else "- Mother list saved before filtering: no",
        "",
        "## Candidate Retrieval Keywords",
        "",
        "Narrow queries:",
        "",
        *[f"- {query}" for query in narrow_queries],
        "",
        "Secondary cross-check queries:",
        "",
        *[f"- {query}" for query in broad_checks],
        "",
        "## External Cross-check",
        "",
        args.external_cross_check,
        "",
        "## A/B/C/D/E Counts",
        "",
        "| Level | Count |",
        "| --- | --- |",
        *[f"| {level} | {counts[level]} |" for level in "ABCDE"],
        "",
        "## High-priority Reading List",
        "",
        *format_papers([row for row in abc if row.get("level") == "A"] or abc),
        "",
        "## Limitations",
        "",
        f"- {args.limitations}",
        "- External search results must be verified against the official venue/year/main-conference source before inclusion.",
        "- Generated paper-card summaries are draft notes and require human verification.",
        "",
        "## Manual Verification Needed",
        "",
        "- Confirm main-conference scope and remove any workshop/challenge/demo/tutorial/invited/non-archival results.",
        "- Verify A/B/C/D/E classification boundaries from abstracts and PDFs where needed.",
        "- Fill exact metrics, datasets, and experimental conclusions after reading the official PDFs.",
        "",
    ]

    output = conference_dir / "search-report.md"
    output.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
