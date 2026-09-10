#!/usr/bin/env python3
"""Generate the active dual-track indexes from the complete abstract audit."""

from __future__ import annotations

import csv
import hashlib
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "00-index"
AUDIT = INDEX / "candidate-screening-audit.csv"
METADATA = INDEX / "retained-papers.csv"
SELECTION = INDEX / "paper-selection.csv"
CONFERENCE_ROOT = ROOT / "01-papers-by-conference"

SURVEY_ROLES = {"anchor", "included", "background", "exclude"}
ADVISOR_ROLES = {"method_chain", "discussion", "watch", "exclude"}
ACTIVE_READING_STATUSES = {
    "survey_core",
    "advisor_required",
    "advisor_helpful",
    "retained_reference",
}

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
    "spike_encoding": "Event-to-spike interfaces and encoding",
    "neuron_dynamics": "Spiking neuron dynamics",
    "snn_architecture": "SNN architecture and spike-native operators",
    "snn_training": "Direct, surrogate-gradient and online SNN training",
    "temporal_modeling": "Temporal interaction, state and delay",
    "frequency": "Frequency-aware modeling",
    "fourier_fft": "Fourier transform and FFT",
    "wavelet_time_frequency": "Wavelet and localized time-frequency analysis",
    "scalability_efficiency": "Scalability and efficiency",
    "hardware": "Hardware and deployment",
    "deployment": "Asynchronous and memory-aware deployment",
    "task_generalization": "Task and domain generalization",
    "snn_hybrid": "SNN and hybrid extensions",
    "datasets": "Datasets and evaluation",
}

EXTERNAL_ADVISOR_CHAIN = [
    {
        "title": "Scalable Event Cloud Network for Event-based Classification",
        "year": "2026",
        "venue": "ICML oral",
        "assignment": "focus",
        "link": "",
        "reason": (
            "The TPAMI extension starts from SECNet and asks how to implement its ordered "
            "Event Cloud hierarchy as an accurate, trainable, and genuinely efficient SNN. "
            "Its existing Spatial-FA and Temporal-FA modules remain part of the baseline, "
            "but frequency is no longer the Advisor admission criterion."
        ),
    },
]

SELECTION_FIELDS = [
    "paper_id",
    "title",
    "year",
    "venue",
    "survey_role",
    "survey_topics",
    "survey_reason",
    "advisor_role",
    "advisor_topics",
    "advisor_reason",
    "reading_status",
    "evidence_source",
    "needs_pdf_check",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def values(value: str) -> set[str]:
    return {item for item in value.split(";") if item}


def candidate_rows() -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for path in sorted(CONFERENCE_ROOT.glob("*/candidates.csv")):
        for row in read_csv(path):
            paper_id = row.get("id", "")
            if not paper_id:
                raise ValueError(f"Candidate without ID in {path.relative_to(ROOT)}")
            if paper_id in result:
                raise ValueError(f"Duplicate candidate ID: {paper_id}")
            result[paper_id] = row
    return result


def validate_audit(rows: list[dict[str, str]]) -> None:
    ids = [row["paper_id"] for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate paper IDs in candidate-screening-audit.csv")

    candidates = candidate_rows()
    current_candidates = set(candidates)
    audited_ids = set(ids)
    missing_candidates = current_candidates - audited_ids
    if missing_candidates:
        sample = ", ".join(sorted(missing_candidates)[:10])
        raise ValueError(
            f"{len(missing_candidates)} current candidates lack title/abstract audit: {sample}"
        )
    stale_audits = audited_ids - current_candidates
    if stale_audits:
        sample = ", ".join(sorted(stale_audits)[:10])
        raise ValueError(
            f"{len(stale_audits)} audit rows are absent from current candidates: {sample}"
        )

    for row in rows:
        paper_id = row["paper_id"]
        candidate = candidates[paper_id]
        identity_fields = {
            "title": "title",
            "year": "year",
            "venue": "conference",
        }
        for audit_field, candidate_field in identity_fields.items():
            if row[audit_field].strip() != candidate[candidate_field].strip():
                raise ValueError(
                    f"Candidate/audit {audit_field} drift for {paper_id}"
                )
        abstract = row["abstract"].strip()
        if row["abstract_reviewed"] != "yes" or not abstract:
            raise ValueError(f"Missing reviewed abstract for {paper_id}")
        if not row["official_page"]:
            raise ValueError(f"Missing official page for {paper_id}")
        if row["venue"] == "NeurIPS" and not row["official_track"]:
            raise ValueError(f"Missing NeurIPS track for {paper_id}")
        if row["abstract_sha256"] != hashlib.sha256(abstract.encode()).hexdigest():
            raise ValueError(f"Abstract hash drift for {paper_id}")
        if row["survey_role"] not in SURVEY_ROLES:
            raise ValueError(f"Invalid Survey role for {paper_id}")
        if row["advisor_role"] not in ADVISOR_ROLES:
            raise ValueError(f"Invalid Advisor role for {paper_id}")
        if not values(row["survey_topics"]) <= set(SURVEY_TOPICS):
            raise ValueError(f"Invalid Survey topic for {paper_id}")
        if not values(row["advisor_topics"]) <= set(ADVISOR_TOPICS):
            raise ValueError(f"Invalid Advisor topic for {paper_id}")
        if row["needs_pdf_check"] not in {"yes", "no"}:
            raise ValueError(f"Invalid PDF-check flag for {paper_id}")

        dual_excluded = row["survey_role"] == "exclude" and row["advisor_role"] == "exclude"
        expected_active = "no" if dual_excluded else "yes"
        if row["in_active_corpus"] != expected_active:
            raise ValueError(f"Active-corpus flag drift for {paper_id}")
        if dual_excluded:
            if row["reading_status"] != "excluded_from_active_corpus":
                raise ValueError(f"Invalid excluded status for {paper_id}")
            continue

        statuses = values(row["reading_status"])
        if not statuses or not statuses <= ACTIVE_READING_STATUSES:
            raise ValueError(f"Invalid reading status for {paper_id}")
        if row["needs_pdf_check"] == "yes" and "survey_core" in statuses:
            raise ValueError(f"Unresolved paper cannot enter Survey Core: {paper_id}")

        expected_survey_decision = (
            "core"
            if "survey_core" in statuses
            else "exclude"
            if row["survey_role"] == "exclude"
            else "reference"
        )
        expected_advisor_decision = (
            "required"
            if "advisor_required" in statuses
            else "helpful"
            if "advisor_helpful" in statuses
            else "exclude"
            if row["advisor_role"] == "exclude"
            else "reference"
        )
        if row["survey_core_decision"] != expected_survey_decision:
            raise ValueError(f"Survey decision drift for {paper_id}")
        if row["advisor_core_decision"] != expected_advisor_decision:
            raise ValueError(f"Advisor decision drift for {paper_id}")


def evidence_source(row: dict[str, str]) -> str:
    parts = [row["evidence_basis"]]
    if row["pdf_boundary_check"] != "not_needed":
        parts.append(row["pdf_boundary_check"])
    return "; ".join(part for part in parts if part)


def generate_selection(
    audit_rows: list[dict[str, str]], metadata: dict[str, dict[str, str]]
) -> list[dict[str, str]]:
    active = [row for row in audit_rows if row["in_active_corpus"] == "yes"]
    active_ids = {row["paper_id"] for row in active}
    if active_ids != set(metadata):
        missing_metadata = sorted(active_ids - set(metadata))
        stale_metadata = sorted(set(metadata) - active_ids)
        raise ValueError(
            "Audit/retained-papers active set drift: "
            f"missing_metadata={missing_metadata[:5]} stale_metadata={stale_metadata[:5]}"
        )
    active.sort(key=lambda row: (-int(row["year"]), row["venue"], row["title"].lower()))
    generated = []
    for row in active:
        generated.append(
            {
                "paper_id": row["paper_id"],
                "title": row["title"],
                "year": row["year"],
                "venue": row["venue"],
                "survey_role": row["survey_role"],
                "survey_topics": row["survey_topics"],
                "survey_reason": row["survey_reason"],
                "advisor_role": row["advisor_role"],
                "advisor_topics": row["advisor_topics"],
                "advisor_reason": row["advisor_reason"],
                "reading_status": row["reading_status"],
                "evidence_source": evidence_source(row),
                "needs_pdf_check": row["needs_pdf_check"],
            }
        )
    write_csv(SELECTION, SELECTION_FIELDS, generated)
    return generated


def validate_retained_cards(metadata: dict[str, dict[str, str]]) -> None:
    for paper_id, row in metadata.items():
        card_path = row["card_path"]
        if not card_path:
            raise ValueError(f"Missing retained card path for {paper_id}")
        if not (ROOT / card_path).is_file():
            raise ValueError(f"Missing retained card file for {paper_id}: {card_path}")


def markdown_cell(value: str) -> str:
    return " ".join(value.split()).replace("|", "\\|")


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
    coverage: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        for topic in values(row[topic_field]):
            coverage[topic].append(row)

    core_label = "Current proceedings core" if title.startswith("Advisor") else "Current core"
    lines = [f"# {title}", "", intro, "", f"{core_label}: **{len(rows)} papers**.", ""]
    if title.startswith("Survey"):
        counts = Counter(row["survey_role"] for row in rows)
        lines += [
            f"Composition: **{counts['anchor']} anchor + {counts['included']} included + "
            f"{counts['background']} selected background**.",
            "This newest-first inventory is not a prescribed reading sequence. Read by method "
            "cluster using `03-review-draft/outline.md` and its checkpoints.",
            "",
        ]
    if title.startswith("Advisor"):
        required_count = sum("advisor_required" in values(row["reading_status"]) for row in rows)
        helpful_count = sum("advisor_helpful" in values(row["reading_status"]) for row in rows)
        lines += [
            f"Composition: **{required_count} required + {helpful_count} helpful**.",
            "Helpful assignments are focused mechanism reads. They do not enroll an entire "
            "architecture or make Mamba/SSM part of the Advisor direction.",
            "",
            f"The bounded Advisor reading set is **{len(rows) + len(EXTERNAL_ADVISOR_CHAIN)} "
            f"papers**: {len(rows)} proceedings-corpus assignments and "
            f"{len(EXTERNAL_ADVISOR_CHAIN)} external focus paper.",
            "",
            "## Focus Paper",
            "",
            "| Paper | Year | Venue | Assignment | Why it is included |",
            "| --- | ---: | --- | --- | --- |",
        ]
        for external in EXTERNAL_ADVISOR_CHAIN:
            title_text = external["title"]
            if external["link"]:
                title_text = f"[{title_text}]({external['link']})"
            lines.append(
                f"| {title_text} | {external['year']} | {external['venue']} | "
                f"{external['assignment']} | {external['reason']} |"
            )
        lines.append("")

    groups = [("Core Inventory", rows)]
    if title.startswith("Advisor"):
        groups = [
            ("Required Knowledge", [row for row in rows if "advisor_required" in values(row["reading_status"])]),
            ("Focused Helpful Mechanisms", [row for row in rows if "advisor_helpful" in values(row["reading_status"])]),
        ]
    item_number = 0
    for heading, group_rows in groups:
        role_label = "Assignment" if title.startswith("Advisor") else "Role"
        lines += [
            f"## {heading}",
            "",
            f"| # | Paper | Year | Venue | Track | {role_label} | Why it is core |",
            "| ---: | --- | ---: | --- | --- | --- | --- |",
        ]
        for row in group_rows:
            item_number += 1
            displayed_role = row[role_field]
            if title.startswith("Advisor"):
                displayed_role = (
                    "required"
                    if "advisor_required" in values(row["reading_status"])
                    else "helpful"
                )
            lines.append(
                f"| {item_number} | [{row['title']}]({plan_link(row, metadata)}) | "
                f"{row['year']} | {row['venue']} | "
                f"{metadata[row['paper_id']].get('official_track') or '-'} | "
                f"{displayed_role} | {markdown_cell(row[reason_field])} |"
            )
        lines.append("")

    lines += ["## Coverage Map", ""]
    for topic, label in labels.items():
        if not coverage[topic]:
            continue
        links = "; ".join(
            f"[{row['title']}]({plan_link(row, metadata)})" for row in coverage[topic]
        )
        lines += [f"### {label}", "", links, ""]
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_survey_reference_pool(
    rows: list[dict[str, str]], metadata: dict[str, dict[str, str]]
) -> int:
    reference_rows = [
        row
        for row in rows
        if row["survey_role"] != "exclude"
        and "survey_core" not in values(row["reading_status"])
    ]
    role_order = {"included": 0, "background": 1}
    reference_rows.sort(
        key=lambda row: (
            role_order.get(row["survey_role"], 2),
            -int(row["year"]),
            row["title"].lower(),
        )
    )
    fields = [
        "paper_id",
        "title",
        "year",
        "venue",
        "survey_role",
        "survey_topics",
        "survey_reason",
        "official_track",
        "pdf_link",
        "official_page",
        "card_path",
    ]
    output_rows = []
    for row in reference_rows:
        source = metadata[row["paper_id"]]
        output_rows.append(
            {
                **{field: row[field] for field in fields[:7]},
                "official_track": source.get("official_track", ""),
                "pdf_link": source["pdf_link"],
                "official_page": source["official_page"],
                "card_path": source["card_path"],
            }
        )
    write_csv(INDEX / "survey-reference-pool.csv", fields, output_rows)
    return len(reference_rows)


def write_search_reports(
    audit_rows: list[dict[str, str]], active_rows: list[dict[str, str]]
) -> None:
    audit_by_id = {row["paper_id"]: row for row in audit_rows}
    active_by_id = {row["paper_id"]: row for row in active_rows}
    for folder in sorted(CONFERENCE_ROOT.iterdir()):
        if not folder.is_dir() or not (folder / "mother-list.csv").exists():
            continue
        mother = read_csv(folder / "mother-list.csv")
        candidates = read_csv(folder / "candidates.csv")
        reviewed = read_csv(folder / "abc-reviewed.csv")
        candidate_audits = [audit_by_id[row["id"]] for row in candidates]
        retained = [active_by_id[row["id"]] for row in reviewed]
        first = mother[0] if mother else {}
        venue = first.get("conference", folder.name.rstrip("0123456789"))
        year = first.get("year", "")
        survey = Counter(row["survey_role"] for row in retained)
        advisor = Counter(row["advisor_role"] for row in retained)
        excluded = sum(row["in_active_corpus"] == "no" for row in candidate_audits)
        tracks = Counter(
            row["official_track"] for row in candidate_audits if row["official_track"]
        )
        lines = [
            f"# {venue} {year} Search Report",
            "",
            "## Current Status",
            "",
            f"- Official mother list: {len(mother)} papers.",
            f"- High-recall title/abstract candidates: {len(candidates)}.",
            f"- Candidates with complete official-title/abstract audit: {len(candidate_audits)}.",
            f"- Retained A/B/C provenance records: {len(reviewed)}.",
            f"- Dual-track exclusions among current candidates: {excluded}.",
            "- A/B/C is conference-search provenance only; active reading assignments come from the dual-track audit.",
            "",
            "## Scope And Evidence",
            "",
            "- Every title candidate is represented in `00-index/candidate-screening-audit.csv` with its complete official abstract and SHA256.",
            "- Full-PDF search over the complete mother list was not performed.",
        ]
        if tracks:
            lines += [
                "- NeurIPS includes all official long-paper tracks; the official track is retained for every audited candidate.",
                "",
                "## Official Track Counts",
                "",
                *[f"- {track}: {count}" for track, count in sorted(tracks.items())],
            ]
        lines += [
            "",
            "## Retained Dual-Track Counts",
            "",
            f"- Survey: anchor={survey['anchor']}, included={survey['included']}, background={survey['background']}, exclude={survey['exclude']}.",
            f"- Advisor: method_chain={advisor['method_chain']}, discussion={advisor['discussion']}, watch={advisor['watch']}, exclude={advisor['exclude']}.",
            "",
            "## Retained Entries",
            "",
            "| ID | Title | Survey role | Advisor role |",
            "| --- | --- | --- | --- |",
        ]
        for row in sorted(retained, key=lambda item: item["title"].lower()):
            lines.append(
                f"| {row['paper_id']} | {markdown_cell(row['title'])} | "
                f"{row['survey_role']} | {row['advisor_role']} |"
            )
        lines += [
            "",
            "## Audit Source",
            "",
            "Use `00-index/candidate-screening-audit.csv` for every retained or excluded candidate decision and its official abstract evidence.",
        ]
        (folder / "search-report.md").write_text(
            "\n".join(lines).rstrip() + "\n", encoding="utf-8"
        )


def main() -> None:
    audit_rows = read_csv(AUDIT)
    validate_audit(audit_rows)
    metadata_rows = read_csv(METADATA)
    metadata = {row["id"]: row for row in metadata_rows}
    validate_retained_cards(metadata)
    rows = generate_selection(audit_rows, metadata)

    survey_core = [row for row in rows if "survey_core" in values(row["reading_status"])]
    advisor_core = [
        row
        for row in rows
        if values(row["reading_status"]) & {"advisor_required", "advisor_helpful"}
    ]
    write_plan(
        INDEX / "reading-plan-survey-core.md",
        "Survey Core Reading Plan",
        "Strictly serves the survey **Spiking Neural Networks for Event Cameras**. "
        "Event representation and SNN computation are parallel foundations; the Core focuses "
        "on their explicit intersection and indispensable supporting evidence.",
        survey_core,
        metadata,
        "survey_topics",
        "survey_role",
        "survey_reason",
        SURVEY_TOPICS,
    )
    write_plan(
        INDEX / "reading-plan-advisor-core.md",
        "Advisor Core Reading Plan",
        "Serves the **SECNet ICML 2026 oral to TPAMI extension** direction: implement SECNet "
        "as an accurate, trainable, and deployable SNN while preserving its ordered Event "
        "Cloud hierarchy. Existing frequency modules are baseline components, not the Core "
        "admission criterion. Mamba/SSM is outside the planned first implementation.",
        advisor_core,
        metadata,
        "advisor_topics",
        "advisor_role",
        "advisor_reason",
        ADVISOR_TOPICS,
    )
    reference_count = write_survey_reference_pool(rows, metadata)
    write_search_reports(audit_rows, rows)
    required = sum("advisor_required" in values(row["reading_status"]) for row in rows)
    helpful = sum("advisor_helpful" in values(row["reading_status"]) for row in rows)
    excluded = sum(row["in_active_corpus"] == "no" for row in audit_rows)
    print(
        f"audited={len(audit_rows)} active={len(rows)} survey_core={len(survey_core)} "
        f"survey_reference_pool={reference_count} advisor_required={required} "
        f"advisor_helpful={helpful} advisor_core={len(advisor_core)} excluded={excluded}"
    )


if __name__ == "__main__":
    main()
