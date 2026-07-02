#!/usr/bin/env python3
"""Retrieve and classify event-camera/SNN candidates from a mother list.

Title retrieval intentionally uses a broad, high-recall keyword pool. Every
title hit is only a raw candidate until an official abstract/page confirms one
of the two target axes: event cameras/DVS/visual event streams/event-camera
data, or SNN/spiking neural computation. Broader umbrella terms such as
event-based vision, neuromorphic computing, asynchronous, event-driven, spike,
or spiking are retrieval triggers only, not A/B/C evidence by themselves.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

CORE_EVENT_KEYWORDS = [
    "event camera",
    "event cameras",
    "event-camera",
    "event-based camera",
    "event-based cameras",
    "dynamic vision sensor",
    "dynamic vision sensors",
    "DVS",
    "visual event sensor",
    "visual event sensors",
    "event sensor",
    "event sensors",
    "event stream",
    "event streams",
]

CORE_SNN_KEYWORDS = [
    "spiking neural network",
    "spiking neural networks",
    "SNN",
    "SNNs",
    "spiking neuron",
    "spiking neurons",
    "spiking neural model",
    "spiking neural models",
    "spike train",
    "spike trains",
    "LIF",
    "leaky integrate-and-fire",
    "integrate-and-fire",
    "surrogate gradient",
    "surrogate gradients",
    "ANN-to-SNN",
    "ANN2SNN",
    "spiking transformer",
    "spiking transformers",
    "spike-based neural network",
    "spike-based neural networks",
]

EVENT_EVIDENCE_KEYWORDS = CORE_EVENT_KEYWORDS + [
    "visual event stream",
    "visual event streams",
    "event-camera dataset",
    "event-camera datasets",
    "event-camera data",
    "event camera data",
    "event-based camera data",
]

SNN_EVIDENCE_KEYWORDS = CORE_SNN_KEYWORDS + [
    "SNN training",
    "SNN inference",
    "IF neuron",
    "IF neurons",
]

AUXILIARY_KEYWORDS = [
    "event",
    "event-based",
    "event-based vision",
    "event vision",
    "event data",
    "event representation",
    "event frame",
    "event volume",
    "voxel grid",
    "neuromorphic vision",
    "neuromorphic computing",
    "event-driven",
    "asynchronous",
    "low latency",
    "temporal sparsity",
    "sparse temporal",
    "high-speed vision",
    "temporal coding",
    "rate coding",
    "spike",
    "spiking",
    "spike camera",
]

TITLE_RETRIEVAL_KEYWORDS = list(dict.fromkeys(CORE_EVENT_KEYWORDS + CORE_SNN_KEYWORDS + AUXILIARY_KEYWORDS))

CANDIDATE_COLUMNS = [
    "id",
    "title",
    "authors",
    "conference",
    "year",
    "official_page",
    "pdf_link",
    "matched_keywords",
    "matched_axis",
    "classification_reason",
]

ABC_COLUMNS = [
    "id",
    "title",
    "authors",
    "conference",
    "year",
    "level",
    "category",
    "official_page",
    "pdf_link",
    "abstract",
    "matched_keywords",
    "classification_reason",
    "card_path",
    "notes",
]

CATEGORY_BY_LEVEL = {
    "A": "SNN + Event Camera",
    "B": "Event Camera",
    "C": "SNN",
    "D": "Adjacent / Background",
    "E": "False Positive",
}


def keyword_pattern(keyword: str) -> re.Pattern[str]:
    escaped = re.escape(keyword.lower()).replace(r"\ ", r"[\s-]+")
    if keyword.isupper() or keyword in {"LIF", "DVS", "SNN", "SNNs"}:
        return re.compile(rf"(?<![a-z0-9]){escaped}(?![a-z0-9])", re.IGNORECASE)
    return re.compile(rf"(?<![a-z0-9]){escaped}(?![a-z0-9])", re.IGNORECASE)


def matched_keywords(text: str, keywords: list[str]) -> list[str]:
    return [keyword for keyword in keywords if keyword_pattern(keyword).search(text)]


def searchable_text(row: dict[str, str]) -> str:
    fields = [
        row.get("title", ""),
        row.get("abstract", ""),
        row.get("notes", ""),
        row.get("official_page_text", ""),
    ]
    return "\n".join(fields)


def has_inspection_context(row: dict[str, str]) -> bool:
    return any(
        row.get(field, "").strip()
        for field in ("abstract", "notes", "official_page_text")
    )


def title_retrieval(row: dict[str, str]) -> tuple[list[str], str, str]:
    title = row.get("title", "")
    matched = matched_keywords(title, TITLE_RETRIEVAL_KEYWORDS)
    if matched:
        return matched, "Ambiguous", "Broad title keyword match; requires official abstract or official-page inspection before A/B/C classification"
    return [], "", ""


def classify(row: dict[str, str]) -> tuple[str, list[str], str, str]:
    text = searchable_text(row)
    event_matches = matched_keywords(text, EVENT_EVIDENCE_KEYWORDS)
    snn_matches = matched_keywords(text, SNN_EVIDENCE_KEYWORDS)
    auxiliary_matches = matched_keywords(text, AUXILIARY_KEYWORDS)
    matched = event_matches + snn_matches + auxiliary_matches

    lower_text = text.lower()
    has_spike_camera = "spike camera" in lower_text or "spike cameras" in lower_text
    if has_spike_camera and not event_matches and not snn_matches:
        return "D", ["spike camera"], "Ambiguous", "Spike camera mention without explicit event-camera/DVS or SNN evidence"

    axes: list[str] = []
    if event_matches:
        axes.append("event_camera")
    if snn_matches:
        axes.append("snn")

    if event_matches and snn_matches:
        return "A", matched, "Both axes", "Official abstract/page confirms both event-camera/DVS/visual-event-stream data and SNN/spiking neural computation"
    if event_matches:
        return "B", matched, "Event Camera axis", "Official abstract/page confirms event-camera/DVS/visual-event-stream data; no clear SNN evidence found"
    if snn_matches:
        return "C", matched, "SNN axis", "Official abstract/page confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found"
    if auxiliary_matches:
        return "D", matched, "Ambiguous", "Auxiliary keyword match without clear event-camera/DVS or SNN evidence"
    return "E", matched, "none", "Keyword match is unrelated or no workflow keyword match was found"


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_rows(path: Path, rows: list[dict[str, str]], columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def build_candidate_row(row: dict[str, str], keywords: list[str], axis: str, reason: str) -> dict[str, str]:
    return {
        "id": row.get("id", ""),
        "title": row.get("title", ""),
        "authors": row.get("authors", ""),
        "conference": row.get("conference", ""),
        "year": row.get("year", ""),
        "official_page": row.get("official_page", ""),
        "pdf_link": row.get("pdf_link", ""),
        "matched_keywords": "; ".join(dict.fromkeys(keywords)),
        "matched_axis": axis,
        "classification_reason": reason,
    }


def build_abc_row(row: dict[str, str], candidate: dict[str, str]) -> dict[str, str]:
    return {
        "id": candidate["id"],
        "title": candidate["title"],
        "authors": candidate["authors"],
        "conference": candidate["conference"],
        "year": candidate["year"],
        "level": candidate["level"],
        "category": candidate["category"],
        "official_page": candidate["official_page"],
        "pdf_link": candidate["pdf_link"],
        "abstract": row.get("abstract", "") or "Unknown",
        "matched_keywords": candidate["matched_keywords"],
        "classification_reason": candidate["classification_reason"],
        "card_path": "",
        "notes": "auto-classified; needs human verification",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Classify mother-list rows into A/B/C/D/E candidates.")
    parser.add_argument("--input", required=True, type=Path, help="Path to mother-list.csv")
    parser.add_argument("--output-dir", type=Path, help="Directory for candidates.csv and abc-reviewed.csv")
    args = parser.parse_args()

    output_dir = args.output_dir or args.input.parent
    candidate_rows: list[dict[str, str]] = []
    abc_rows: list[dict[str, str]] = []
    counts = {level: 0 for level in "ABCDE"}

    for row in read_rows(args.input):
        retrieval_keywords, retrieval_axis, retrieval_reason = title_retrieval(row)
        if not retrieval_keywords:
            continue
        candidate_rows.append(build_candidate_row(row, retrieval_keywords, retrieval_axis, retrieval_reason))
        if retrieval_axis == "Ambiguous" and not has_inspection_context(row):
            counts["D"] += 1
            continue
        level, keywords, axis, reason = classify(row)
        counts[level] += 1
        if level in {"A", "B", "C"}:
            candidate = build_candidate_row(row, keywords, axis, reason)
            candidate["level"] = level
            candidate["category"] = CATEGORY_BY_LEVEL[level]
            abc_rows.append(build_abc_row(row, candidate))

    write_rows(output_dir / "candidates.csv", candidate_rows, CANDIDATE_COLUMNS)
    write_rows(output_dir / "abc-reviewed.csv", abc_rows, ABC_COLUMNS)
    print(f"Wrote {len(candidate_rows)} raw candidates and {len(abc_rows)} A/B/C rows to {output_dir}")
    print("Counts: " + ", ".join(f"{level}={counts[level]}" for level in "ABCDE"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
