#!/usr/bin/env python3
"""Validate the lightweight taxonomy census or print a blinded batch view."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "00-index" / "candidate-screening-audit.csv"
MANIFEST = ROOT / "00-index" / "taxonomy-census-batches.csv"
CENSUS = ROOT / "00-index" / "taxonomy-census.csv"

SOURCE_COUNT = 572
BATCH_IDS = tuple(f"B{i:03d}" for i in range(1, 11))
MANIFEST_HEADER = ["batch_id", "batch_position", "paper_id"]
CENSUS_HEADER = [
    "paper_id",
    "scope",
    "intersection_directness",
    "contribution_type",
    "pipeline_position",
    "provisional_snn_role",
    "task_application",
    "cross_cutting_topics",
    "emergent_code",
    "taxonomy_use",
    "abstract_basis",
    "pdf_trigger_question",
    "confidence",
    "annotator",
    "review_status",
    "review_note",
]

SINGLE_ENUMS = {
    "scope": {
        "core_intersection",
        "event_camera_only",
        "snn_only",
        "out_of_scope",
        "uncertain",
    },
    "intersection_directness": {
        "method_coupled",
        "event_specific_training_analysis",
        "benchmark_only",
        "single_axis",
        "neither_axis",
        "uncertain",
    },
    "confidence": {"high", "medium", "low"},
    "review_status": {
        "mid_complete",
        "high_reviewed",
        "high_corrected",
        "high_escalated",
    },
}

MULTI_ENUMS = {
    "contribution_type": [
        "inference_method",
        "event_representation",
        "neuron_or_dynamics",
        "training_or_conversion",
        "analysis_or_robustness",
        "dataset_or_benchmark",
        "hardware_or_deployment",
        "survey_or_theory",
        "other",
        "uncertain",
    ],
    "provisional_snn_role": [
        "event_interface",
        "task_network",
        "embedded_module",
        "algorithmic_engine",
        "other_candidate",
        "not_applicable",
        "unknown",
    ],
    "cross_cutting_topics": [
        "training",
        "conversion",
        "augmentation",
        "robustness_or_attack",
        "efficiency",
        "hardware_or_deployment",
        "dataset_or_evaluation",
        "temporal_modeling",
        "representation_learning",
        "generalization",
        "none",
        "other",
    ],
    "taxonomy_use": [
        "taxonomy_anchor",
        "representative_method",
        "boundary_case",
        "background_context",
        "cross_cutting_evidence",
        "dataset_or_evaluation",
        "exclude_candidate",
        "undetermined",
    ],
}

EXCLUSIVE_SENTINELS = {
    "contribution_type": {"uncertain"},
    "provisional_snn_role": {"not_applicable", "unknown"},
    "cross_cutting_topics": {"none"},
    "taxonomy_use": {"undetermined"},
}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def parse_multivalue(field: str, value: str, paper_id: str, errors: list[str]) -> list[str]:
    values = value.split(";") if value else []
    allowed_order = MULTI_ENUMS[field]
    require(bool(values), f"{paper_id}: {field} is blank", errors)
    require(len(values) == len(set(values)), f"{paper_id}: duplicate {field} value", errors)
    invalid = [item for item in values if item not in allowed_order]
    require(not invalid, f"{paper_id}: invalid {field}: {invalid}", errors)
    expected = sorted(values, key=allowed_order.index) if not invalid else values
    require(values == expected, f"{paper_id}: {field} is not in codebook order", errors)
    sentinels = EXCLUSIVE_SENTINELS[field].intersection(values)
    require(
        not sentinels or len(values) == 1,
        f"{paper_id}: {field} sentinel must stand alone",
        errors,
    )
    return values


def load_and_validate() -> tuple[dict[str, dict[str, str]], dict[str, list[dict[str, str]]], list[dict[str, str]], list[str]]:
    errors: list[str] = []

    source_header, source_rows = read_csv(SOURCE)
    required_source = {
        "paper_id",
        "title",
        "year",
        "venue",
        "official_track",
        "abstract_reviewed",
        "abstract_sha256",
        "abstract",
        "official_page",
        "survey_core_decision",
    }
    require(required_source.issubset(source_header), "source audit is missing required columns", errors)
    source_by_id = {row["paper_id"]: row for row in source_rows}
    require(len(source_rows) == SOURCE_COUNT, f"source row count is {len(source_rows)}, expected {SOURCE_COUNT}", errors)
    require(len(source_by_id) == len(source_rows), "source audit contains duplicate paper_id", errors)
    for row in source_rows:
        paper_id = row["paper_id"]
        require(row["abstract_reviewed"] == "yes", f"{paper_id}: abstract_reviewed is not yes", errors)
        require(bool(row["abstract"]), f"{paper_id}: abstract is blank", errors)
        require(len(row["abstract_sha256"]) == 64, f"{paper_id}: abstract_sha256 is not 64 characters", errors)

    manifest_header, manifest_rows = read_csv(MANIFEST)
    require(manifest_header == MANIFEST_HEADER, "manifest header does not match contract", errors)
    manifest_ids = [row["paper_id"] for row in manifest_rows]
    require(len(manifest_rows) == SOURCE_COUNT, f"manifest row count is {len(manifest_rows)}, expected {SOURCE_COUNT}", errors)
    require(len(set(manifest_ids)) == len(manifest_ids), "manifest contains duplicate paper_id", errors)
    require(set(manifest_ids) == set(source_by_id), "manifest IDs do not exactly match source audit", errors)

    by_batch: dict[str, list[dict[str, str]]] = {batch_id: [] for batch_id in BATCH_IDS}
    for row in manifest_rows:
        batch_id = row["batch_id"]
        require(batch_id in by_batch, f"invalid batch_id: {batch_id}", errors)
        if batch_id in by_batch:
            by_batch[batch_id].append(row)
    for batch_id, rows in by_batch.items():
        positions = sorted(int(row["batch_position"]) for row in rows)
        require(57 <= len(rows) <= 58, f"{batch_id}: size {len(rows)} is outside 57–58", errors)
        require(positions == list(range(1, len(rows) + 1)), f"{batch_id}: positions are not contiguous", errors)

    if by_batch["B001"]:
        batch_one_sources = [source_by_id[row["paper_id"]] for row in by_batch["B001"]]
        for field in ("year", "venue", "survey_core_decision"):
            all_values = {row[field] for row in source_rows}
            batch_values = {row[field] for row in batch_one_sources}
            require(batch_values == all_values, f"B001 does not cover every source {field}", errors)

    census_header, census_rows = read_csv(CENSUS)
    require(census_header == CENSUS_HEADER, "census header does not match contract", errors)
    census_ids = [row["paper_id"] for row in census_rows]
    require(len(set(census_ids)) == len(census_ids), "census contains duplicate paper_id", errors)
    for row in census_rows:
        paper_id = row["paper_id"] or "<blank-paper-id>"
        require(paper_id in source_by_id, f"{paper_id}: not found in source audit", errors)
        for field in CENSUS_HEADER[1:-1]:
            require(bool(row[field]), f"{paper_id}: {field} is blank", errors)
        for field, allowed in SINGLE_ENUMS.items():
            require(row[field] in allowed, f"{paper_id}: invalid {field}: {row[field]!r}", errors)
        parsed = {
            field: parse_multivalue(field, row[field], paper_id, errors)
            for field in MULTI_ENUMS
        }
        if "other_candidate" in parsed["provisional_snn_role"]:
            require(
                row["emergent_code"] not in {"", "none", "unknown"},
                f"{paper_id}: other_candidate requires a concrete emergent_code",
                errors,
            )
        require(bool(row["emergent_code"]), f"{paper_id}: emergent_code is blank", errors)
        require(bool(row["pdf_trigger_question"]), f"{paper_id}: pdf_trigger_question is blank", errors)
        if row["review_status"] == "mid_complete":
            require(not row["review_note"], f"{paper_id}: Mid must leave review_note blank", errors)

    return source_by_id, by_batch, census_rows, errors


def show_batch(batch_id: str, source_by_id: dict[str, dict[str, str]], by_batch: dict[str, list[dict[str, str]]]) -> None:
    rows = sorted(by_batch[batch_id], key=lambda row: int(row["batch_position"]))
    keys = (
        "paper_id",
        "title",
        "year",
        "venue",
        "official_track",
        "abstract_sha256",
        "abstract",
        "official_page",
    )
    for manifest_row in rows:
        source = source_by_id[manifest_row["paper_id"]]
        payload = {"batch_position": int(manifest_row["batch_position"])}
        payload.update({key: source[key] for key in keys})
        print(json.dumps(payload, ensure_ascii=False, sort_keys=False))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--show-batch", choices=BATCH_IDS)
    parser.add_argument("--require-batch", choices=BATCH_IDS)
    parser.add_argument("--require-all", action="store_true")
    args = parser.parse_args()

    source_by_id, by_batch, census_rows, errors = load_and_validate()
    census_by_id = {row["paper_id"]: row for row in census_rows}

    if args.require_batch:
        required_ids = {row["paper_id"] for row in by_batch[args.require_batch]}
        missing = sorted(required_ids - set(census_by_id))
        require(not missing, f"{args.require_batch}: {len(missing)} census rows missing", errors)
    if args.require_all:
        missing = sorted(set(source_by_id) - set(census_by_id))
        require(not missing, f"full census: {len(missing)} rows missing", errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    if args.show_batch:
        show_batch(args.show_batch, source_by_id, by_batch)
        return 0

    batch_sizes = ", ".join(f"{batch_id}={len(rows)}" for batch_id, rows in by_batch.items())
    print(f"PASS: source={len(source_by_id)}, census={len(census_rows)}, columns={len(CENSUS_HEADER)}")
    print(f"PASS: manifest IDs are exact and unique; {batch_sizes}")
    print("PASS: B001 covers all source years, venues, and survey decisions")
    if census_rows:
        print("scope:", dict(sorted(Counter(row["scope"] for row in census_rows).items())))
        print("review_status:", dict(sorted(Counter(row["review_status"] for row in census_rows).items())))
    else:
        print("INFO: census is header-only; no papers were annotated in setup")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
