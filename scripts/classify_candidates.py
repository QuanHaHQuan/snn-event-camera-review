#!/usr/bin/env python3
"""Retrieve and classify narrow event-camera/SNN candidates from a mother list."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

EVENT_KEYWORDS = [
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
    "event stream",
    "event streams",
    "visual event stream",
    "visual event streams",
    "event data",
    "event-based vision",
    "event vision",
    "neuromorphic vision",
]

SNN_KEYWORDS = [
    "spiking neural network",
    "spiking neural networks",
    "SNN",
    "SNNs",
    "spiking neural model",
    "spiking neural models",
    "spiking neuron",
    "spiking neurons",
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
    "neuromorphic computing",
]

SECONDARY_TERMS = [
    "asynchronous",
    "event-driven",
    "low latency",
    "temporal sparsity",
    "sparse temporal",
    "high-speed vision",
    "event representation",
    "event frame",
    "event volume",
    "voxel grid",
    "temporal coding",
    "rate coding",
]

TASK_LABELS = [
    "object detection",
    "tracking",
    "recognition",
    "reconstruction",
    "optical flow",
    "depth estimation",
    "semantic segmentation",
    "video interpolation",
    "stereo",
    "pose estimation",
    "3D detection",
    "SLAM",
    "Gaussian Splatting",
]

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
    "level",
    "category",
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


def classify(row: dict[str, str]) -> tuple[str, list[str], str, str]:
    text = searchable_text(row)
    event_matches = matched_keywords(text, EVENT_KEYWORDS)
    snn_matches = matched_keywords(text, SNN_KEYWORDS)
    secondary_matches = matched_keywords(text, SECONDARY_TERMS)
    task_matches = matched_keywords(text, TASK_LABELS)
    matched = event_matches + snn_matches + secondary_matches + task_matches

    lower_text = text.lower()
    has_spike_camera = "spike camera" in lower_text or "spike cameras" in lower_text
    if has_spike_camera and not event_matches and not snn_matches:
        return "D", ["spike camera"], "adjacent", "Spike camera mention without explicit event-camera/DVS or SNN evidence"

    axes: list[str] = []
    if event_matches:
        axes.append("event_camera")
    if snn_matches:
        axes.append("snn")

    if event_matches and snn_matches:
        return "A", matched, ";".join(axes), "Explicit event-camera/DVS and SNN/spiking evidence found"
    if event_matches:
        return "B", matched, "event_camera", "Event-camera/DVS-side paper; no clear SNN evidence found"
    if snn_matches:
        return "C", matched, "snn", "SNN/spiking-side paper; no clear event-camera/DVS evidence found"
    return "E", matched, "none", "No core event-camera/DVS or SNN/spiking evidence found"


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_rows(path: Path, rows: list[dict[str, str]], columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def build_candidate_row(row: dict[str, str], level: str, keywords: list[str], axis: str, reason: str) -> dict[str, str]:
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
        "level": level,
        "category": CATEGORY_BY_LEVEL[level],
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
    candidates: list[dict[str, str]] = []
    abc_rows: list[dict[str, str]] = []
    counts = {level: 0 for level in "ABCDE"}

    for row in read_rows(args.input):
        level, keywords, axis, reason = classify(row)
        counts[level] += 1
        if level == "E":
            continue
        candidate = build_candidate_row(row, level, keywords, axis, reason)
        candidates.append(candidate)
        if level in {"A", "B", "C"}:
            abc_rows.append(build_abc_row(row, candidate))

    write_rows(output_dir / "candidates.csv", candidates, CANDIDATE_COLUMNS)
    write_rows(output_dir / "abc-reviewed.csv", abc_rows, ABC_COLUMNS)
    print(f"Wrote {len(candidates)} raw candidates and {len(abc_rows)} A/B/C rows to {output_dir}")
    print("Counts: " + ", ".join(f"{level}={counts[level]}" for level in "ABCDE"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
