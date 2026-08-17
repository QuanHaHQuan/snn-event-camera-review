#!/usr/bin/env python3
"""Regenerate V2 summary indexes for the Survey and Advisor tracks."""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SELECTION = ROOT / "00-index" / "paper-selection.csv"
V2_ROOT = ROOT / "06-reading-summaries" / "v2"
PAPERS = V2_ROOT / "papers"

EXTERNAL_ADVISOR_ROWS = [
    {
        "title": "Scalable Event Cloud Network for Event-based Classification (SECNet)",
        "year": "2026",
        "venue": "ICML oral",
        "reading_status": "advisor_focus",
        "_assignment": "focus",
        "advisor_reason": (
            "Focus paper for the TPAMI extension. SECNet already contains Spatial-FA and "
            "Temporal-FA FFT-filter-iFFT modules; read their exact signals, axes, and interfaces "
            "before assessing how the existing frequency path can be refined and coupled to SNNs."
        ),
    },
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def values(value: str) -> set[str]:
    return {item for item in value.split(";") if item}


def normalize_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", title.lower())


def extract_title(path: Path) -> str:
    for line in path.read_text(errors="replace").splitlines():
        if not line.startswith("# "):
            continue
        title = line[2:].strip()
        if title.startswith("Summary V2｜"):
            title = title.removeprefix("Summary V2｜")
        if title.endswith("｜Summary V2"):
            title = title.removesuffix("｜Summary V2")
        return title.strip()
    raise ValueError(f"No level-one heading found in {path.relative_to(ROOT)}")


def scan_v2_files() -> dict[str, dict[str, str]]:
    papers: dict[str, dict[str, str]] = {}
    for path in sorted(PAPERS.glob("*-v2.md")):
        title = extract_title(path)
        key = normalize_title(title)
        if key in papers:
            raise ValueError(f"Duplicate V2 title: {title}")
        papers[key] = {
            "title": title,
            "filename": path.name,
        }
    return papers


def summary_link(filename: str, depth: str = "../papers") -> str:
    return f"[{filename}]({depth}/{filename})"


def write_track_index(
    path: Path,
    title: str,
    intro: str,
    rows: list[dict[str, str]],
    v2_files: dict[str, dict[str, str]],
    assignment_label: str,
    assignment_value,
    reason_field: str,
) -> tuple[int, int]:
    rows = sorted(rows, key=lambda row: (-int(row["year"]), row["title"].lower()))
    completed = sum(normalize_title(row["title"]) in v2_files for row in rows)
    lines = [
        f"# {title}",
        "",
        intro,
        "",
        f"Progress: **{completed}/{len(rows)} complete**, **{len(rows) - completed} missing**.",
        "",
        "A V2 paper has one canonical file in `../papers/`. This index records its track-specific purpose; it does not duplicate the summary.",
        "",
        f"| # | Paper | Year | Venue | {assignment_label} | Status | V2 | Track purpose |",
        "| ---: | --- | ---: | --- | --- | --- | --- | --- |",
    ]
    for number, row in enumerate(rows, start=1):
        key = normalize_title(row["title"])
        summary = v2_files.get(key)
        status = "complete" if summary else "missing"
        link = summary_link(summary["filename"]) if summary else "-"
        lines.append(
            f"| {number} | {row['title']} | {row['year']} | {row['venue']} | "
            f"{assignment_value(row)} | {status} | {link} | {row[reason_field]} |"
        )
    path.write_text("\n".join(lines).rstrip() + "\n")
    return completed, len(rows)


def write_papers_index(
    rows: list[dict[str, str]], v2_files: dict[str, dict[str, str]]
) -> None:
    metadata = {normalize_title(row["title"]): row for row in rows}
    external_advisor = {
        normalize_title(row["title"]): row for row in EXTERNAL_ADVISOR_ROWS
    }
    lines = [
        "# V2 Paper Index",
        "",
        "Canonical human-guided V2 summaries. Each paper exists once; Survey and Advisor indexes link to the same file.",
        "",
        f"Current V2 files: **{len(v2_files)}**.",
        "",
        "| Paper | Year | Venue | Survey | Advisor | V2 |",
        "| --- | ---: | --- | --- | --- | --- |",
    ]
    items = []
    for key, summary in v2_files.items():
        row = metadata.get(key)
        survey = "core" if row and "survey_core" in values(row["reading_status"]) else "reference"
        advisor_statuses = values(row["reading_status"]) if row else set()
        external = external_advisor.get(key)
        advisor = (
            "required" if "advisor_required" in advisor_statuses
            else "helpful" if "advisor_helpful" in advisor_statuses
            else external["_assignment"] if external
            else "reference"
        )
        year = row["year"] if row else summary["filename"].split("-", 1)[0]
        venue = row["venue"] if row else summary["filename"].split("-", 2)[1]
        title = row["title"] if row else summary["title"]
        items.append((int(year), title.lower(), title, year, venue, survey, advisor, summary["filename"]))
    for _, _, title, year, venue, survey, advisor, filename in sorted(items, key=lambda item: (-item[0], item[1])):
        lines.append(
            f"| {title} | {year} | {venue} | {survey} | {advisor} | "
            f"[{filename}](papers/{filename}) |"
        )
    (V2_ROOT / "index.md").write_text("\n".join(lines).rstrip() + "\n")


def main() -> None:
    rows = read_csv(SELECTION)
    v2_files = scan_v2_files()
    for folder in (V2_ROOT / "survey", V2_ROOT / "advisor"):
        folder.mkdir(parents=True, exist_ok=True)
    survey_rows = [row for row in rows if "survey_core" in values(row["reading_status"])]
    advisor_rows = [
        row
        for row in rows
        if values(row["reading_status"]) & {"advisor_required", "advisor_helpful"}
    ] + EXTERNAL_ADVISOR_ROWS
    known_titles = {
        normalize_title(row["title"])
        for row in rows + EXTERNAL_ADVISOR_ROWS
    }
    unmatched = [summary["title"] for key, summary in v2_files.items() if key not in known_titles]

    write_papers_index(rows, v2_files)
    survey_completed, survey_total = write_track_index(
        V2_ROOT / "survey" / "index.md",
        "Survey V2 Index",
        "Human-guided reading progress for the `Spiking Neural Networks for Event Cameras` Survey Core.",
        survey_rows,
        v2_files,
        "Survey role",
        lambda row: row["survey_role"],
        "survey_reason",
    )
    advisor_completed, advisor_total = write_track_index(
        V2_ROOT / "advisor" / "index.md",
        "Advisor V2 Index",
        "Human-guided reading progress for the SECNet to TPAMI extension direction: Event Camera + frequency/Fourier + SNN.",
        advisor_rows,
        v2_files,
        "Assignment",
        lambda row: row.get("_assignment") or (
            "required"
            if "advisor_required" in values(row["reading_status"])
            else "helpful"
        ),
        "advisor_reason",
    )
    print(
        f"v2={len(v2_files)} survey={survey_completed}/{survey_total} "
        f"advisor={advisor_completed}/{advisor_total} external_or_archived={len(unmatched)}"
    )


if __name__ == "__main__":
    main()
