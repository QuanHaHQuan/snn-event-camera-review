#!/usr/bin/env python3
"""Validate the active dual-track index and regenerate its reading plans."""

from __future__ import annotations

import csv
import hashlib
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "00-index"
SELECTION = INDEX / "paper-selection.csv"
AUDIT = INDEX / "core-screening-audit.csv"
DUAL_EXCLUDE_AUDIT = ROOT / "05-logs" / "codex-runs" / "2026-08-12-dual-exclude-audit.md"

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
    "scalability_efficiency": "Scalability and efficiency",
    "hardware": "Hardware and deployment",
    "task_generalization": "Task and domain generalization",
    "snn_hybrid": "SNN and hybrid extensions",
    "datasets": "Datasets and evaluation",
}

EXTERNAL_ADVISOR_CHAIN = [
    {
        "title": "Scalable Event Cloud Network for Event-based Classification (SECNet)",
        "year": "2026",
        "venue": "ICML oral",
        "assignment": "focus",
        "link": "",
        "reason": (
            "The TPAMI extension starts from SECNet. Its Event Cloud hierarchy already contains "
            "Spatial-FA and Temporal-FA FFT-filter-iFFT modules; the extension question is how to "
            "refine those frequency mechanisms and couple them to SNN computation."
        ),
    },
    {
        "title": "TTPOINT: A Tensorized Point Cloud Network for Lightweight Action Recognition with Event Cameras",
        "year": "2023",
        "venue": "ACMMM",
        "assignment": "predecessor",
        "link": (
            "../06-reading-summaries/v2/papers/"
            "2023-ACMMM-ttpoint-tensorized-point-cloud-event-action-recognition-v2.md"
        ),
        "reason": (
            "TTPOINT is an external advisor-group predecessor for tensorized sparse event-point "
            "processing and the architectural lineage leading to PEPNet and SECNet."
        ),
    },
]

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


def validate_audit_source(
    rows: list[dict[str, str]], metadata: dict[str, dict[str, str]]
) -> list[dict[str, str]]:
    """Validate the complete title/abstract audit against the active index."""
    audit_rows = read_csv(AUDIT)
    audit_ids = [row["paper_id"] for row in audit_rows]
    if len(audit_ids) != len(set(audit_ids)):
        raise ValueError("Duplicate paper IDs in core-screening-audit.csv")

    active_by_id = {row["paper_id"]: row for row in rows}
    for audit_row in audit_rows:
        paper_id = audit_row["paper_id"]
        abstract = audit_row["abstract"].strip()
        if audit_row["abstract_reviewed"] != "yes" or not abstract:
            raise ValueError(f"Missing reviewed abstract for {paper_id}")
        if not audit_row["official_page"]:
            raise ValueError(f"Missing official page for {paper_id}")
        if audit_row["venue"] == "NeurIPS" and not audit_row["official_track"]:
            raise ValueError(f"Missing NeurIPS track for {paper_id}")
        expected_hash = hashlib.sha256(abstract.encode()).hexdigest()
        if audit_row["abstract_sha256"] != expected_hash:
            raise ValueError(f"Abstract hash drift for {paper_id}")

        dual_excluded = (
            audit_row["survey_role"] == "exclude"
            and audit_row["advisor_role"] == "exclude"
        )
        should_be_active = not dual_excluded
        is_active = paper_id in active_by_id
        if should_be_active != is_active:
            raise ValueError(f"Active/dual-exclude partition drift for {paper_id}")
        expected_active_flag = "yes" if is_active else "no"
        if audit_row["in_active_corpus"] != expected_active_flag:
            raise ValueError(f"Audit active flag drift for {paper_id}")

        if not is_active:
            if audit_row["reading_status"] != "excluded_from_active_corpus":
                raise ValueError(f"Invalid excluded reading status for {paper_id}")
            continue

        active_row = active_by_id[paper_id]
        if metadata[paper_id].get("official_track", "") != audit_row["official_track"]:
            raise ValueError(f"Official-track drift for {paper_id}")
        semantic_fields = (
            "survey_role",
            "survey_topics",
            "survey_reason",
            "advisor_role",
            "advisor_topics",
            "advisor_reason",
            "needs_pdf_check",
        )
        for field in semantic_fields:
            if active_row[field] != audit_row[field]:
                raise ValueError(f"Audit drift for {paper_id} field {field}")
        if active_row["reading_status"] != audit_row["reading_status"]:
            raise ValueError(f"Audit reading-status drift for {paper_id}")

        statuses = values(active_row["reading_status"])
        expected_survey_decision = (
            "core"
            if "survey_core" in statuses
            else "exclude"
            if active_row["survey_role"] == "exclude"
            else "reference"
        )
        expected_advisor_decision = (
            "required"
            if "advisor_required" in statuses
            else "helpful"
            if "advisor_helpful" in statuses
            else "exclude"
            if active_row["advisor_role"] == "exclude"
            else "reference"
        )
        if audit_row["survey_core_decision"] != expected_survey_decision:
            raise ValueError(f"Survey Core audit drift for {paper_id}")
        if audit_row["advisor_core_decision"] != expected_advisor_decision:
            raise ValueError(f"Advisor Core audit drift for {paper_id}")

    if set(active_by_id) != {
        row["paper_id"]
        for row in audit_rows
        if not (row["survey_role"] == "exclude" and row["advisor_role"] == "exclude")
    }:
        raise ValueError("Audit and active index cover different paper IDs")
    return audit_rows


def markdown_cell(value: str) -> str:
    return " ".join(value.split()).replace("|", "\\|")


def neurips_track(row: dict[str, str]) -> str:
    if row.get("conference", "") != "NeurIPS":
        return ""
    value = row.get("track", "") or row.get("status_or_award", "")
    return value.strip().removeprefix("Track: ")


def write_dual_exclude_audit(audit_rows: list[dict[str, str]]) -> int:
    excluded = [
        row
        for row in audit_rows
        if row["survey_role"] == "exclude" and row["advisor_role"] == "exclude"
    ]
    excluded.sort(
        key=lambda row: (-int(row["year"]), row["venue"], row["title"].lower())
    )
    lines = [
        "# Dual-Exclude Audit",
        "",
        "These papers were reviewed from their complete official title and abstract and have no retained role in either active track. Complete venue `mother-list.csv` files remain untouched.",
        "",
        f"Total: **{len(excluded)} papers**.",
        "",
        "This table is generated from `00-index/core-screening-audit.csv`; every row has a non-empty official abstract and a verified SHA256 hash.",
        "",
        "| ID | Title | Year | Venue | Track | Survey reason | Advisor reason | Official evidence |",
        "| --- | --- | ---: | --- | --- | --- | --- | --- |",
    ]
    for row in excluded:
        lines.append(
            f"| {row['paper_id']} | {markdown_cell(row['title'])} | {row['year']} | "
            f"{row['venue']} | {row['official_track'] or '-'} | "
            f"{markdown_cell(row['survey_reason'])} | "
            f"{markdown_cell(row['advisor_reason'])} | "
            f"[official page]({row['official_page']}) |"
        )
    DUAL_EXCLUDE_AUDIT.write_text("\n".join(lines).rstrip() + "\n")
    return len(excluded)


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
    core_label = "Current proceedings core" if title.startswith("Advisor") else "Current core"
    lines = [f"# {title}", "", intro, "", f"{core_label}: **{len(rows)} papers**.", ""]
    if title.startswith("Survey"):
        counts = Counter(row["survey_role"] for row in rows)
        lines += [
            f"Composition: **{counts['anchor']} anchor + {counts['included']} included + "
            f"{counts['background']} selected background**. The global role counts are corpus statistics, "
            "not reading assignments.",
            "The table below is a newest-first inventory, not a prescribed reading sequence. "
            "Read by method cluster using `03-review-draft/outline.md` and checkpoint plans.",
            "",
        ]
    if title.startswith("Advisor"):
        required_count = sum("advisor_required" in values(row["reading_status"]) for row in rows)
        helpful_count = sum("advisor_helpful" in values(row["reading_status"]) for row in rows)
        lines += [
            f"Composition: **{required_count} required + {helpful_count} helpful**. The broader "
            "`method_chain`, `discussion`, and "
            "`watch` counts in `paper-selection.csv` are candidate-pool labels, not reading assignments.",
            "Helpful assignments are focused mechanism reads: extract only the module named in "
            "the row, and do not treat the paper's full architecture as part of the Advisor direction.",
            "",
            f"The complete Advisor knowledge chain is **{len(rows) + len(EXTERNAL_ADVISOR_CHAIN)} "
            f"papers**: the {len(rows)} proceedings-corpus assignments below plus "
            f"{len(EXTERNAL_ADVISOR_CHAIN)} separately listed focus/predecessor papers.",
            "",
            "## Focus And External Predecessor",
            "",
            "| Paper | Year | Venue | Assignment | Why it is required |",
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
        lines += [f"## {heading}", "", f"| # | Paper | Year | Venue | Track | {role_label} | Why it is core |", "| ---: | --- | ---: | --- | --- | --- | --- |"]
        for row in group_rows:
            item_number += 1
            displayed_role = (
                "required" if "advisor_required" in values(row["reading_status"])
                else "helpful" if "advisor_helpful" in values(row["reading_status"])
                else row[role_field]
            ) if title.startswith("Advisor") else row[role_field]
            lines.append(
                f"| {item_number} | [{row['title']}]({plan_link(row, metadata)}) | {row['year']} | {row['venue']} | "
                f"{metadata[row['paper_id']].get('official_track') or '-'} | "
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
        "out-of-scope-x.md": "# Deprecated Out-of-Scope Index\n\nSee the [current dual-exclude audit](../05-logs/codex-runs/2026-08-12-dual-exclude-audit.md).\n",
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
        track_by_id = {row["id"]: neurips_track(row) for row in mother}
        tracks = Counter(track for track in track_by_id.values() if track)
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
            non_main_core = [
                row
                for row in active
                if track_by_id.get(row["paper_id"], "") != "Main Conference Track"
                and values(row["reading_status"])
                & {"survey_core", "advisor_required", "advisor_helpful"}
            ]
            lines += [
                "",
                "## Official Track Counts",
                "",
                *[f"- {track}: {count}" for track, count in sorted(tracks.items())],
                "- NeurIPS special handling: all official accepted tracks are eligible, but non-main-track papers require stronger evidence for Core enrollment.",
                f"- Current non-main-track Core assignments: {len(non_main_core)}.",
            ]
            for row in non_main_core:
                lines.append(
                    f"  - {row['title']} ({track_by_id[row['paper_id']]}; {row['reading_status']})"
                )
        lines += [
            "", "## Active Dual-Track Counts", "",
            f"- Survey: anchor={survey['anchor']}, included={survey['included']}, background={survey['background']}, exclude={survey['exclude']}.",
            f"- Advisor: method_chain={advisor['method_chain']}, discussion={advisor['discussion']}, watch={advisor['watch']}, exclude={advisor['exclude']}.",
            "", "## Active Entries", "",
        ]
        if tracks:
            lines += [
                "| ID | Title | Official track | Survey role | Advisor role |",
                "| --- | --- | --- | --- | --- |",
            ]
        else:
            lines += [
                "| ID | Title | Survey role | Advisor role |",
                "| --- | --- | --- | --- |",
            ]
        for row in sorted(active, key=lambda item: item["title"].lower()):
            if tracks:
                lines.append(
                    f"| {row['paper_id']} | {row['title']} | "
                    f"{track_by_id[row['paper_id']]} | {row['survey_role']} | "
                    f"{row['advisor_role']} |"
                )
            else:
                lines.append(
                    f"| {row['paper_id']} | {row['title']} | "
                    f"{row['survey_role']} | {row['advisor_role']} |"
                )
        lines += [
            "", "## Audit", "",
            "Current dual-excluded titles and reasons are recorded in `05-logs/codex-runs/2026-08-12-dual-exclude-audit.md`.",
            "Complete official proceedings remain available in this venue's `mother-list.csv`.",
        ]
        (folder / "search-report.md").write_text("\n".join(lines) + "\n")


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
    with (INDEX / "survey-reference-pool.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in reference_rows:
            source = metadata[row["paper_id"]]
            writer.writerow(
                {
                    **{field: row[field] for field in fields[:7]},
                    "official_track": source.get("official_track", ""),
                    "pdf_link": source["pdf_link"],
                    "official_page": source["official_page"],
                    "card_path": source["card_path"],
                }
            )
    return len(reference_rows)


def main() -> None:
    rows = read_csv(SELECTION)
    metadata_rows = read_csv(INDEX / "all-papers.csv")
    metadata = {row["id"]: row for row in metadata_rows}
    validate(rows, metadata)
    audit_rows = validate_audit_source(rows, metadata)
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
        "Serves the **SECNet ICML 2026 oral to TPAMI extension** direction: Event Camera + frequency/Fourier + SNN. SECNet already applies Spatial-FA and Temporal-FA FFT modules to Event Cloud features, so this plan targets the existing frequency interface and its SNN extension. Mamba/SSM similarity alone does not justify enrollment; a detachable Fourier mechanism may justify focused reading.",
        advisor_core, metadata, "advisor_topics", "advisor_role", "advisor_reason", ADVISOR_TOPICS,
    )
    survey_reference_count = write_survey_reference_pool(rows, metadata)
    dual_excluded_count = write_dual_exclude_audit(audit_rows)
    write_legacy_redirects()
    write_search_reports(rows)
    required = sum("advisor_required" in values(row["reading_status"]) for row in rows)
    helpful = sum("advisor_helpful" in values(row["reading_status"]) for row in rows)
    print(
        f"active={len(rows)} survey_core={len(survey_core)} "
        f"survey_reference_pool={survey_reference_count} advisor_required={required} "
        f"advisor_helpful={helpful} advisor_core={len(advisor_core)} "
        f"dual_excluded={dual_excluded_count}"
    )
    print("survey_roles", dict(Counter(row["survey_role"] for row in rows)))
    print("advisor_roles", dict(Counter(row["advisor_role"] for row in rows)))


if __name__ == "__main__":
    main()
