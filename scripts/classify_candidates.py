#!/usr/bin/env python3
"""Retrieve and classify candidate papers from a mother list."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

EVENT_KEYWORDS = [
    "event camera",
    "event-camera",
    "dvs",
    "dynamic vision sensor",
    "visual event",
    "event stream",
    "event-based vision",
    "event based vision",
    "event voxel",
    "time surface",
    "neuromorphic vision dataset",
]

SNN_KEYWORDS = [
    "spiking neural network",
    "snn",
    "spiking transformer",
    "ann-to-snn",
    "ann to snn",
    "surrogate gradient",
    "spike train",
    "lif neuron",
    "if neuron",
    "leaky integrate-and-fire",
    "integrate-and-fire",
]

ADJACENT_KEYWORDS = [
    "asynchronous",
    "temporal sparsity",
    "event-driven",
    "event driven",
    "low-latency vision",
    "low latency vision",
    "neuromorphic sensor",
    "neuromorphic computing",
    "spike camera",
]

OUTPUT_COLUMNS = [
    "id",
    "title",
    "authors",
    "conference",
    "year",
    "level",
    "category",
    "pdf_link",
    "official_page",
    "abstract",
    "retrieved_keywords",
    "classification_notes",
]

CATEGORY_BY_LEVEL = {
    "A": "SNN + Event Camera",
    "B": "Event Camera",
    "C": "SNN",
    "D": "Adjacent / Background",
    "E": "False Positive",
}


def matched_keywords(text: str, keywords: list[str]) -> list[str]:
    lowered = text.lower()
    return [keyword for keyword in keywords if keyword in lowered]


def classify(row: dict[str, str]) -> tuple[str, list[str], str]:
    searchable = " ".join(
        [
            row.get("title", ""),
            row.get("abstract", ""),
            row.get("notes", ""),
        ]
    )
    event_matches = matched_keywords(searchable, EVENT_KEYWORDS)
    snn_matches = matched_keywords(searchable, SNN_KEYWORDS)
    adjacent_matches = matched_keywords(searchable, ADJACENT_KEYWORDS)
    all_matches = event_matches + snn_matches + adjacent_matches

    if event_matches and snn_matches:
        return "A", all_matches, "event-camera and SNN keywords both present; needs human verification"
    if event_matches:
        return "B", all_matches, "event-camera-side candidate; no clear SNN keyword match"
    if snn_matches:
        return "C", all_matches, "SNN-side candidate; no clear event-camera keyword match"
    if adjacent_matches:
        return "D", all_matches, "adjacent neuromorphic/asynchronous candidate"
    return "E", [], "no workflow keyword match"


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def normalize_row(row: dict[str, str], level: str, keywords: list[str], notes: str) -> dict[str, str]:
    return {
        "id": row.get("id", ""),
        "title": row.get("title", ""),
        "authors": row.get("authors", ""),
        "conference": row.get("conference", ""),
        "year": row.get("year", ""),
        "level": level,
        "category": CATEGORY_BY_LEVEL[level],
        "pdf_link": row.get("pdf_link", ""),
        "official_page": row.get("official_page", ""),
        "abstract": row.get("abstract", ""),
        "retrieved_keywords": "; ".join(keywords),
        "classification_notes": notes,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Classify mother-list rows into A/B/C/D/E candidates.")
    parser.add_argument("--input", required=True, type=Path, help="Path to mother-list.csv")
    parser.add_argument("--output-dir", type=Path, help="Directory for candidates.csv and abc-reviewed.csv")
    args = parser.parse_args()

    output_dir = args.output_dir or args.input.parent
    candidate_rows: list[dict[str, str]] = []
    abc_rows: list[dict[str, str]] = []

    for row in read_rows(args.input):
        level, keywords, notes = classify(row)
        normalized = normalize_row(row, level, keywords, notes)
        if level != "E":
            candidate_rows.append(normalized)
        if level in {"A", "B", "C"}:
            abc_rows.append(normalized)

    write_rows(output_dir / "candidates.csv", candidate_rows)
    write_rows(output_dir / "abc-reviewed.csv", abc_rows)
    print(f"Wrote {len(candidate_rows)} candidates and {len(abc_rows)} A/B/C rows to {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
