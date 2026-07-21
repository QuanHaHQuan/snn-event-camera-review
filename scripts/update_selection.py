#!/usr/bin/env python3
"""Validate the active dual-track index and regenerate its reading plans."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "00-index"
SELECTION = INDEX / "paper-selection.csv"

SURVEY_ROLES = {"anchor", "included", "background", "exclude"}
ADVISOR_ROLES = {"method_chain", "discussion", "watch", "exclude"}
READING_STATUSES = {"survey_core", "advisor_required", "advisor_helpful", "retained_reference"}

SURVEY_TOPICS = {
    "event_to_spike": "Events-to-spikes and direct input",
    "representation_slicing": "Event representation, slicing, voxel and Event Cloud",
    "architecture": "Fully spiking, hybrid and converted architectures",
    "temporal_modeling": "Temporal dynamics, state and memory",
    "learning": "Training SNNs for event streams",
    "classification_recognition": "Classification and recognition",
    "detection": "Object detection",
    "tracking": "Tracking",
    "reconstruction_restoration": "Reconstruction and restoration",
    "pose_depth_segmentation": "Pose, depth, flow and segmentation",
    "efficiency_hardware": "Latency, energy and hardware evidence",
    "robustness_open_challenges": "Robustness, limitations and open challenges",
    "datasets_benchmarks": "Datasets and benchmarks",
}

ADVISOR_TOPICS = {
    "event_cloud_point": "Event Cloud and point processing",
    "grouping_sampling": "Grouping, sampling and aggregation",
    "polarity": "Polarity-aware modeling",
    "frequency": "Frequency-aware modeling",
    "fourier_fft": "Fourier transform and FFT",
    "wavelet_time_frequency": "Wavelet and localized time-frequency analysis",
    "ssm_mamba_memory": "SSM, Mamba and long memory",
    "scalability_efficiency": "Scalability and efficiency",
    "hardware": "Hardware and deployment",
    "task_generalization": "Task and domain generalization",
    "snn_hybrid": "SNN and hybrid extensions",
    "datasets": "Datasets and evaluation",
}

OFFICIAL_PROCEEDINGS = {
    "CVPR2024": "https://openaccess.thecvf.com/CVPR2024?day=all",
    "CVPR2025": "https://openaccess.thecvf.com/CVPR2025?day=all",
    "CVPR2026": "https://openaccess.thecvf.com/CVPR2026?day=all",
    "ECCV2024": "https://eccv.ecva.net/virtual/2024/papers.html",
    "ICCV2025": "https://openaccess.thecvf.com/ICCV2025?day=all",
    "ICLR2024": "https://proceedings.iclr.cc/paper_files/paper/2024",
    "ICLR2025": "https://proceedings.iclr.cc/paper_files/paper/2025",
    "ICML2024": "https://proceedings.mlr.press/v235/",
    "ICML2025": "https://proceedings.mlr.press/v267/",
    "NeurIPS2024": "https://papers.nips.cc/paper_files/paper/2024",
    "NeurIPS2025": "https://papers.nips.cc/paper_files/paper/2025",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def values(value: str) -> set[str]:
    return {item for item in value.split(";") if item}


def validate(rows: list[dict[str, str]], metadata: dict[str, dict[str, str]]) -> None:
    ids = [row["paper_id"] for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate paper IDs in paper-selection.csv")
    if set(ids) != set(metadata):
        raise ValueError("paper-selection.csv and all-papers.csv contain different active IDs")
    for row in rows:
        if row["survey_role"] not in SURVEY_ROLES or row["advisor_role"] not in ADVISOR_ROLES:
            raise ValueError(f"Invalid role for {row['paper_id']}")
        if not values(row["survey_topics"]) <= set(SURVEY_TOPICS):
            raise ValueError(f"Invalid survey topic for {row['paper_id']}")
        if not values(row["advisor_topics"]) <= set(ADVISOR_TOPICS):
            raise ValueError(f"Invalid advisor topic for {row['paper_id']}")
        if not values(row["reading_status"]) <= READING_STATUSES:
            raise ValueError(f"Invalid reading status for {row['paper_id']}")
        if row["needs_pdf_check"] not in {"yes", "no"}:
            raise ValueError(f"Invalid PDF-check flag for {row['paper_id']}")
        if row["needs_pdf_check"] == "yes" and "survey_core" in values(row["reading_status"]):
            raise ValueError(f"Unresolved paper cannot enter Survey Core: {row['paper_id']}")


def plan_link(row: dict[str, str], metadata: dict[str, dict[str, str]]) -> str:
    return f"../{metadata[row['paper_id']]['card_path']}"


def write_plan(
    path: Path,
    title: str,
    intro: str,
    rows: list[dict[str, str]],
    metadata: dict[str, dict[str, str]],
    topic_field: str,
    role_field: str,
    reason_field: str,
    labels: dict[str, str],
) -> None:
    rows.sort(key=lambda row: (-int(row["year"]), row["title"].lower()))
    coverage = defaultdict(list)
    for row in rows:
        for topic in values(row[topic_field]):
            coverage[topic].append(row)
    lines = [f"# {title}", "", intro, "", f"Current core: **{len(rows)} papers**.", ""]
    if title.startswith("Survey"):
        counts = Counter(row["survey_role"] for row in rows)
        lines += [
            f"Composition: **{counts['anchor']} anchor + {counts['included']} included + "
            f"{counts['background']} selected background**. The global role counts are corpus statistics, "
            "not reading assignments.",
            "",
        ]
    if title.startswith("Advisor"):
        required_count = sum("advisor_required" in values(row["reading_status"]) for row in rows)
        helpful_count = sum("advisor_helpful" in values(row["reading_status"]) for row in rows)
        lines += [
            f"Composition: **{required_count} required + {helpful_count} helpful**. The broader "
            "`method_chain`, `discussion`, and "
            "`watch` counts in `paper-selection.csv` are candidate-pool labels, not reading assignments.",
            "",
            "## Focus Paper",
            "",
            "**Scalable Event Cloud Network for Event-based Classification (SECNet), ICML 2026 oral.** "
            "This advisor paper defines the extension target and is not counted as a proceedings-corpus entry below.",
            "",
        ]
    groups = [("Reading Order", rows)]
    if title.startswith("Advisor"):
        groups = [
            ("Required Knowledge", [row for row in rows if "advisor_required" in values(row["reading_status"])]),
            ("Helpful Inspiration", [row for row in rows if "advisor_helpful" in values(row["reading_status"])]),
        ]
    item_number = 0
    for heading, group_rows in groups:
        role_label = "Assignment" if title.startswith("Advisor") else "Role"
        lines += [f"## {heading}", "", f"| # | Paper | Year | Venue | {role_label} | Why it is core |", "| ---: | --- | ---: | --- | --- | --- |"]
        for row in group_rows:
            item_number += 1
            displayed_role = (
                "required" if "advisor_required" in values(row["reading_status"])
                else "helpful" if "advisor_helpful" in values(row["reading_status"])
                else row[role_field]
            ) if title.startswith("Advisor") else row[role_field]
            lines.append(
                f"| {item_number} | [{row['title']}]({plan_link(row, metadata)}) | {row['year']} | {row['venue']} | "
                f"{displayed_role} | {row[reason_field]} |"
            )
        lines.append("")
    lines += ["", "## Coverage Map", ""]
    for topic, label in labels.items():
        if not coverage[topic]:
            continue
        links = "; ".join(f"[{row['title']}]({plan_link(row, metadata)})" for row in coverage[topic])
        lines += [f"### {label}", "", links, ""]
    path.write_text("\n".join(lines).rstrip() + "\n")


def write_legacy_redirects() -> None:
    redirects = {
        "reading-plan-core.md": "# Deprecated Core Reading Plan\n\nUse [Survey Core](reading-plan-survey-core.md) and [Advisor Core](reading-plan-advisor-core.md).\n",
        "reading-plan-p0.md": "# Deprecated P0 Plan\n\nUse [Survey Core](reading-plan-survey-core.md).\n",
        "reading-plan-p1.md": "# Deprecated P1 Plan\n\nUse `paper-selection.csv` and filter `reading_status=retained_reference`.\n",
        "auto-summary-p2.md": "# Deprecated P2 Queue\n\nP0-P3 priorities are retired. Use `paper-selection.csv`.\n",
        "advisor-track.md": "# Deprecated Advisor Track\n\nUse [Advisor Core](reading-plan-advisor-core.md).\n",
        "uncertain-review.md": "# PDF Check Queue\n\nFilter `paper-selection.csv` by `needs_pdf_check=yes`.\n",
        "level-T-advisor-direction.md": "# Deprecated\n\nUse [Advisor Core](reading-plan-advisor-core.md).\n",
        "out-of-scope-x.md": "# Deprecated Out-of-Scope Index\n\nSee the [dual-exclude audit](../05-logs/codex-runs/2026-07-20-dual-track-reselection.md).\n",
    }
    for filename, content in redirects.items():
        (INDEX / filename).write_text(content)


def write_search_reports(rows: list[dict[str, str]]) -> None:
    by_id = {row["paper_id"]: row for row in rows}
    for folder in sorted((ROOT / "01-papers-by-conference").iterdir()):
        if not folder.is_dir() or not (folder / "mother-list.csv").exists():
            continue
        mother = read_csv(folder / "mother-list.csv")
        candidates = read_csv(folder / "candidates.csv")
        reviewed = read_csv(folder / "abc-reviewed.csv")
        active = [by_id[row["id"]] for row in reviewed]
        survey = Counter(row["survey_role"] for row in active)
        advisor = Counter(row["advisor_role"] for row in active)
        first = mother[0] if mother else {}
        venue = first.get("conference", folder.name.rstrip("0123456789"))
        year = first.get("year", "")
        tracks = Counter(row.get("track", "") for row in mother if row.get("track", ""))
        lines = [
            f"# {venue} {year} Search Report", "", "## Current Status", "",
            f"- Official mother list: {len(mother)} papers (preserved in full).",
            f"- Active title-candidate records: {len(candidates)}.",
            f"- Active retained reviewed papers: {len(reviewed)}.",
            "- Every active semantic role was reassessed from the complete official title and abstract.",
            "- Legacy A/B/C values in venue CSVs are search-stage provenance only.",
            "", "## Official Source", "", f"- URL: {OFFICIAL_PROCEEDINGS.get(folder.name, '')}",
            "- Full-PDF search over the complete mother list was not performed.",
        ]
        if tracks:
            lines += ["", "## Official Track Counts", ""] + [f"- {track}: {count}" for track, count in sorted(tracks.items())]
        lines += [
            "", "## Active Dual-Track Counts", "",
            f"- Survey: anchor={survey['anchor']}, included={survey['included']}, background={survey['background']}, exclude={survey['exclude']}.",
            f"- Advisor: method_chain={advisor['method_chain']}, discussion={advisor['discussion']}, watch={advisor['watch']}, exclude={advisor['exclude']}.",
            "", "## Active Entries", "", "| ID | Title | Survey role | Advisor role |", "| --- | --- | --- | --- |",
        ]
        for row in sorted(active, key=lambda item: item["title"].lower()):
            lines.append(f"| {row['paper_id']} | {row['title']} | {row['survey_role']} | {row['advisor_role']} |")
        lines += [
            "", "## Audit", "",
            "Dual-excluded titles and reasons are recorded in `05-logs/codex-runs/2026-07-20-dual-track-reselection.md`.",
            "Complete official proceedings remain available in this venue's `mother-list.csv`.",
        ]
        (folder / "search-report.md").write_text("\n".join(lines) + "\n")


def main() -> None:
    rows = read_csv(SELECTION)
    metadata_rows = read_csv(INDEX / "all-papers.csv")
    metadata = {row["id"]: row for row in metadata_rows}
    validate(rows, metadata)
    survey_core = [row for row in rows if "survey_core" in values(row["reading_status"])]
    advisor_core = [
        row for row in rows
        if values(row["reading_status"]) & {"advisor_required", "advisor_helpful"}
    ]
    write_plan(
        INDEX / "reading-plan-survey-core.md", "Survey Core Reading Plan",
        "Strictly serves the survey **Spiking Neural Networks for Event Cameras**. Anchor papers define the intersection; selected included/background papers cover indispensable representation, training, conversion, evaluation, and open-problem context.",
        survey_core, metadata, "survey_topics", "survey_role", "survey_reason", SURVEY_TOPICS,
    )
    write_plan(
        INDEX / "reading-plan-advisor-core.md", "Advisor Core Reading Plan",
        "Serves the **SECNet ICML 2026 oral to TPAMI extension** direction. It combines the direct method chain with a small set of concrete discussion papers; thematic similarity alone is insufficient.",
        advisor_core, metadata, "advisor_topics", "advisor_role", "advisor_reason", ADVISOR_TOPICS,
    )
    write_legacy_redirects()
    write_search_reports(rows)
    required = sum("advisor_required" in values(row["reading_status"]) for row in rows)
    helpful = sum("advisor_helpful" in values(row["reading_status"]) for row in rows)
    print(
        f"active={len(rows)} survey_core={len(survey_core)} "
        f"advisor_required={required} advisor_helpful={helpful} advisor_core={len(advisor_core)}"
    )
    print("survey_roles", dict(Counter(row["survey_role"] for row in rows)))
    print("advisor_roles", dict(Counter(row["advisor_role"] for row in rows)))


if __name__ == "__main__":
    main()
