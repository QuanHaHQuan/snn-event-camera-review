#!/usr/bin/env python3
"""Validate consistency across V2 relation notes and literature graph files.

This validator cannot decide whether a PDF semantically supports an edge. That
three-gate check remains a source-PDF review requirement. It prevents already
reviewed titles, relation types, citation markers, and keys from drifting across
the V2 files, registry, matrix, and backward-search queue.
"""

from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "03-review-draft" / "literature-node-registry.csv"
MATRIX = ROOT / "03-review-draft" / "core-relation-matrix.csv"
BACKWARD_SEARCH = ROOT / "03-review-draft" / "classic-backward-search.md"
RELATION_MARKERS = (
    "### PDF-verified literature relations",
    "### PDF-verified relation backfill",
)

ALLOWED_TRACKS = {
    "survey_core",
    "advisor_core",
    "survey_advisor_core",
    "historical_reference",
}
ALLOWED_TIERS = {"strict", "lightweight"}
ALLOWED_RELATIONS = {
    "foundation",
    "extends",
    "baseline",
    "alternative",
    "contrasts_with",
    "same_task_different_mechanism",
}
ALLOWED_RELATION_STATUS = {"verified_from_pdf", "needs_further_check"}
ALLOWED_METADATA_STATUS = {
    "verified_from_pdf",
    "verified_from_official_source",
    "partial",
    "unresolved",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def citation_markers(text: str) -> set[str]:
    return set(re.findall(r"\[(\d+)\]", text))


def validate_registry(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    keys = [row["paper_key"] for row in rows]
    titles = [row["canonical_title"] for row in rows]
    require(len(keys) == len(set(keys)), "duplicate registry paper_key")
    require(len(titles) == len(set(titles)), "duplicate registry canonical_title")

    for row in rows:
        key = row["paper_key"]
        require(key and " " not in key, f"invalid paper_key: {key!r}")
        require(bool(row["canonical_title"]), f"missing canonical title: {key}")
        require(bool(row["authors"]), f"missing authors: {key}")
        require(row["year"].isdigit(), f"invalid year: {key}")
        require(bool(row["venue"]), f"missing venue: {key}")
        require(row["in_current_corpus"] in {"yes", "no"}, f"invalid corpus flag: {key}")
        require(
            row["metadata_verification_status"] in ALLOWED_METADATA_STATUS,
            f"invalid metadata status: {key}",
        )
    return {row["paper_key"]: row for row in rows}


def validate_matrix(
    rows: list[dict[str, str]], registry: dict[str, dict[str, str]]
) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    seen: set[tuple[str, str, str]] = set()
    for row in rows:
        source_key = row["source_paper_key"]
        related_key = row["related_paper_key"]
        require(source_key in registry, f"unknown source paper_key: {source_key}")
        require(related_key in registry, f"unknown related paper_key: {related_key}")
        require(
            row["source_paper"] == registry[source_key]["canonical_title"],
            f"source title mismatch: {source_key}",
        )
        require(
            row["related_paper"] == registry[related_key]["canonical_title"],
            f"related title mismatch: {related_key}",
        )
        require(row["source_tracks"] in ALLOWED_TRACKS, f"invalid source_tracks: {source_key}")
        require(row["evidence_tier"] in ALLOWED_TIERS, f"invalid evidence_tier: {source_key}")
        require(row["relation_type"] in ALLOWED_RELATIONS, f"invalid relation_type: {source_key}")
        require(
            row["relation_verification_status"] in ALLOWED_RELATION_STATUS,
            f"invalid relation status: {source_key} -> {related_key}",
        )
        require(
            row["in_current_corpus"] == registry[related_key]["in_current_corpus"],
            f"corpus flag mismatch: {related_key}",
        )
        require(bool(row["evidence_location"]), f"missing evidence location: {source_key} -> {related_key}")
        edge = (source_key, related_key, row["relation_type"])
        require(edge not in seen, f"duplicate semantic edge: {edge}")
        seen.add(edge)
        grouped[source_key].append(row)
    return grouped


def validate_v2_relations(
    registry: dict[str, dict[str, str]], grouped: dict[str, list[dict[str, str]]]
) -> int:
    checked = 0
    source_nodes = [
        row
        for row in registry.values()
        if row["repository_path"].endswith("-v2.md")
    ]
    for source in source_nodes:
        source_key = source["paper_key"]
        path = ROOT / source["repository_path"]
        require(path.is_file(), f"missing V2 path: {source_key}: {path}")
        text = path.read_text(encoding="utf-8")
        present_markers = [marker for marker in RELATION_MARKERS if marker in text]
        marker_count = sum(text.count(marker) for marker in RELATION_MARKERS)
        require(marker_count == 1, f"V2 relation marker count is {marker_count}: {source_key}")
        marker = present_markers[0]
        section = text.split(marker, 1)[1].split("\n## 8.", 1)[0]
        bullets = [line for line in section.splitlines() if line.startswith("- **")]
        edges = grouped.get(source_key, [])
        require(
            len(bullets) == len(edges),
            f"V2/matrix edge count mismatch: {source_key}: {len(bullets)} != {len(edges)}",
        )
        for edge in edges:
            prefix = f"- **{edge['related_paper']} ("
            bullet = next((line for line in bullets if line.startswith(prefix)), None)
            require(bool(bullet), f"missing V2 related title: {source_key} -> {edge['related_paper_key']}")
            require(
                f"`{edge['relation_type']}`" in bullet,
                f"V2 relation type mismatch: {source_key} -> {edge['related_paper_key']}",
            )
            require(
                citation_markers(bullet or "") == citation_markers(edge["evidence_location"]),
                f"V2 citation marker mismatch: {source_key} -> {edge['related_paper_key']}",
            )
            checked += 1
    return checked


def validate_backward_search(
    registry: dict[str, dict[str, str]], matrix: list[dict[str, str]]
) -> int:
    if not BACKWARD_SEARCH.exists():
        return 0
    text = BACKWARD_SEARCH.read_text(encoding="utf-8")
    entries = re.split(r"(?=^### )", text, flags=re.MULTILINE)[1:]
    seen: set[str] = set()
    related_keys = {row["related_paper_key"] for row in matrix}
    for entry in entries:
        title = entry.splitlines()[0].removeprefix("### ").strip()
        match = re.search(r"Registry paper_key: `([^`]+)`", entry)
        require(bool(match), f"backward-search entry lacks paper_key: {title}")
        key = match.group(1) if match else ""
        require(key in registry, f"unknown backward-search paper_key: {key}")
        require(registry[key]["canonical_title"] == title, f"backward-search title mismatch: {key}")
        require(key in related_keys, f"backward-search paper has no matrix edge: {key}")
        require(key not in seen, f"duplicate backward-search paper_key: {key}")
        seen.add(key)
    return len(entries)


def main() -> None:
    registry_rows = read_csv(REGISTRY)
    matrix_rows = read_csv(MATRIX)
    registry = validate_registry(registry_rows)
    grouped = validate_matrix(matrix_rows, registry)
    checked_edges = validate_v2_relations(registry, grouped)
    backward_entries = validate_backward_search(registry, matrix_rows)
    print(
        f"literature_graph_ok registry={len(registry_rows)} matrix={len(matrix_rows)} "
        f"v2_edges={checked_edges} backward_search={backward_entries}"
    )


if __name__ == "__main__":
    main()
