#!/usr/bin/env python3
"""Generate a compact reading-plan layer from the existing review corpus.

This script is intentionally separate from update_index.py. The original
workflow keeps harvesting and A/B/C indexing unchanged; this script adds a
repeatable reading-priority layer for the current research focus:

- SNN / Spiking Neural Networks
- Event Camera / DVS / visual event streams
- SNN for Event Cameras

It uses only existing metadata, reviewed abstracts, paper cards, and a curated
SECNet-reference subset derived from the uploaded SECNet paper. It does not
download PDFs or perform web search.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


BASE_COLUMNS = [
    "id",
    "title",
    "authors",
    "conference",
    "year",
    "level",
    "category",
    "pdf_link",
    "official_page",
    "card_path",
    "notes",
]

READING_COLUMNS = [
    "refined_level",
    "priority",
    "advisor_track",
    "reason",
    "evidence_source",
    "uncertain",
]

P3_TITLE_PATTERNS = [
    r"\bllm\b",
    r"large language model",
    r"language models?",
    r"brain auditory attention",
    r"neural decoding",
]


@dataclass(frozen=True)
class SecnetReference:
    title: str
    authors: str
    year: str
    venue: str
    why_read: str
    relation_to_secnet: str
    source: str = "SECNet references"
    whether_in_current_corpus: str = "no"


@dataclass(frozen=True)
class ReadingOverrides:
    advisor_ids: set[str]
    p0_extra_ids: set[str]
    p1_extra_ids: set[str]
    force_refined_c_ids: set[str]
    secnet_references: list[SecnetReference]


def parse_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def load_reading_overrides(path: Path) -> ReadingOverrides:
    """Load the small project-owned YAML subset without adding a dependency."""
    if not path.exists():
        raise FileNotFoundError(f"Reading-plan overrides file not found: {path}")

    list_sections = {
        "advisor_track": [],
        "p0_extra": [],
        "p1_extra": [],
        "force_refined_c": [],
    }
    references: list[dict[str, str]] = []
    current_section = ""
    current_reference: dict[str, str] | None = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if not line.startswith(" ") and stripped.endswith(":"):
            current_section = stripped[:-1]
            current_reference = None
            continue
        if current_section in list_sections and stripped.startswith("- "):
            list_sections[current_section].append(parse_scalar(stripped[2:]))
            continue
        if current_section == "secnet_references" and stripped.startswith("- "):
            current_reference = {}
            references.append(current_reference)
            key, value = stripped[2:].split(":", 1)
            current_reference[key.strip()] = parse_scalar(value)
            continue
        if current_section == "secnet_references" and current_reference is not None and ":" in stripped:
            key, value = stripped.split(":", 1)
            current_reference[key.strip()] = parse_scalar(value)

    return ReadingOverrides(
        advisor_ids=set(list_sections["advisor_track"]),
        p0_extra_ids=set(list_sections["p0_extra"]),
        p1_extra_ids=set(list_sections["p1_extra"]),
        force_refined_c_ids=set(list_sections["force_refined_c"]),
        secnet_references=[
            SecnetReference(
                title=ref.get("title", ""),
                authors=ref.get("authors", ""),
                year=ref.get("year", ""),
                venue=ref.get("venue", ""),
                why_read=ref.get("why_read", ""),
                relation_to_secnet=ref.get("relation_to_secnet", ""),
            )
            for ref in references
        ],
    )


EVENT_EXPLICIT_PATTERNS = [
    r"\bevent cameras?\b",
    r"\bevent-camera\b",
    r"\bevent based cameras?\b",
    r"\bevent-based cameras?\b",
    r"\bdynamic vision sensors?\b",
    r"\bdvs\b",
    r"\bvisual event sensors?\b",
    r"\bvisual event streams?\b",
    r"\bevent sensors?\b",
    r"\bevent camera data\b",
    r"\bevent-camera data\b",
    r"\bevent-camera datasets?\b",
    r"\baddress-event\b",
    r"\bevent-raw\b",
    r"\brgb-event\b",
    r"\bevent-rgb\b",
    r"\bevent-frame\b",
    r"\bframe-event\b",
    r"\bevent cloud\b",
    r"\bevent clouds\b",
    r"\braw events?\b",
]

EVENT_BENCHMARK_PATTERNS = [
    r"\bcifar10-dvs\b",
    r"\bdvs-cifar10\b",
    r"\bn-caltech101\b",
    r"\bn-caltech\b",
    r"\bn-mnist\b",
    r"\bdvs gesture\b",
    r"\bdvs128 gesture\b",
]

EVENT_CONTEXT_PATTERNS = [
    r"\bevent streams?\b",
    r"\bevent data\b",
    r"\bevent datasets?\b",
    r"\bevent-based vision\b",
    r"\bevent based vision\b",
    r"\bevent-based classification\b",
    r"\bevent-based recognition\b",
    r"\bevent-based action recognition\b",
    r"\bevent-based detection\b",
    r"\bevent-based object detection\b",
    r"\bevent-based tracking\b",
    r"\bevent-based object tracking\b",
    r"\bevent-based pose\b",
    r"\bevent-based stereo\b",
    r"\bevent-based optical flow\b",
    r"\bevent-based motion deblurring\b",
    r"\bevent-based deblurring\b",
    r"\bevent-based video reconstruction\b",
    r"\bevent-to-video\b",
]

SNN_PATTERNS = [
    r"\bspiking neural networks?\b",
    r"\bsnns?\b",
    r"\bsnn-based\b",
    r"\bspiking neurons?\b",
    r"\bspiking neural models?\b",
    r"\bspike trains?\b",
    r"\bleaky integrate-and-fire\b",
    r"\bintegrate-and-fire\b",
    r"\blif\b",
    r"\bif neurons?\b",
    r"\bsurrogate gradients?\b",
    r"\bann-to-snn\b",
    r"\bann2snn\b",
    r"\bspiking transformers?\b",
    r"\bspiking vision transformer\b",
    r"\bspike-based neural networks?\b",
    r"\bspike-driven\b",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def read_reviewed_metadata(repo_root: Path) -> dict[str, dict[str, str]]:
    metadata: dict[str, dict[str, str]] = {}
    for csv_path in sorted((repo_root / "01-papers-by-conference").glob("*/abc-reviewed.csv")):
        for row in read_csv(csv_path):
            metadata[row["id"]] = row
    return metadata


def pattern_hits(text: str, patterns: list[str]) -> list[str]:
    hits = []
    lower = text.lower()
    for pattern in patterns:
        if re.search(pattern, lower, flags=re.IGNORECASE):
            hits.append(pattern)
    return hits


def has_generic_bad_event_context(text: str) -> bool:
    lower = text.lower()
    return any(
        term in lower
        for term in [
            "event logs",
            "event log",
            "temporal point process",
            "time-to-event",
            "event-triggered control",
            "electronic health record",
            "ehr",
        ]
    )


def is_snn_dataset_only(text: str) -> bool:
    lower = text.lower()
    has_benchmark = bool(pattern_hits(lower, EVENT_BENCHMARK_PATTERNS))
    has_method_event = bool(pattern_hits(lower, EVENT_EXPLICIT_PATTERNS + EVENT_CONTEXT_PATTERNS))
    title = lower.split("\n", 1)[0]
    title_mentions_event = bool(pattern_hits(title, EVENT_EXPLICIT_PATTERNS + EVENT_CONTEXT_PATTERNS))
    return has_benchmark and not title_mentions_event and not any(
        phrase in lower
        for phrase in [
            "event cameras",
            "event camera",
            "event streams",
            "event stream",
            "raw event",
            "event data",
            "frame-event",
            "event-frame",
            "rgb-event",
        ]
    ) and not has_method_event


def classify_refined(row: dict[str, str], abstract: str, overrides: ReadingOverrides) -> tuple[str, str, str, str]:
    text = "\n".join([row.get("title", ""), abstract or ""])
    title = row.get("title", "")
    event_explicit = pattern_hits(text, EVENT_EXPLICIT_PATTERNS)
    event_bench = pattern_hits(text, EVENT_BENCHMARK_PATTERNS)
    event_context = [] if has_generic_bad_event_context(text) else pattern_hits(text, EVENT_CONTEXT_PATTERNS)
    snn = pattern_hits(text, SNN_PATTERNS)
    evidence_source = "abstract" if abstract else "metadata"

    if row["id"] in overrides.force_refined_c_ids and snn:
        return (
            "C",
            "Generic SNN method; event-camera evidence appears mainly as benchmark/dataset usage, so it is SNN background rather than A.",
            evidence_source,
            "no",
        )

    has_event = bool(event_explicit or event_context or event_bench)
    has_snn = bool(snn)

    title_has_event = bool(pattern_hits(title, EVENT_EXPLICIT_PATTERNS + EVENT_CONTEXT_PATTERNS))
    title_has_snn = bool(pattern_hits(title, SNN_PATTERNS))
    event_is_only_benchmark = bool(event_bench) and not title_has_event and not event_explicit and not event_context

    if row.get("level", "").upper() == "B":
        uncertain = "yes" if (not has_event or (event_context and not event_explicit and not event_bench)) else "no"
        return (
            "B",
            "Title/abstract indicate event-camera, DVS, visual event stream, or event-camera task background without clear SNN method.",
            evidence_source,
            uncertain,
        )

    if has_event and has_snn and not event_is_only_benchmark and (title_has_event or row.get("level", "").upper() == "A"):
        return (
            "A",
            "Title/abstract indicate both event-camera or visual-event-stream data and SNN/spiking modeling as part of the method.",
            evidence_source,
            "no",
        )
    if has_event and has_snn:
        return (
            "C",
            "SNN/spiking method with event-camera evidence mainly as benchmark or supporting context; not a clearly event-camera-specific method from title/abstract.",
            evidence_source,
            "no",
        )
    if has_event:
        uncertain = "yes" if event_context and not event_explicit and not event_bench else "no"
        return (
            "B",
            "Title/abstract indicate event-camera, DVS, visual event stream, or event-camera task background without clear SNN method.",
            evidence_source,
            uncertain,
        )
    if has_snn:
        return (
            "C",
            "Title/abstract indicate SNN, spiking neural networks, spiking transformers, surrogate gradients, ANN-to-SNN, or spike-driven learning without event-camera method.",
            evidence_source,
            "no",
        )
    return (
        "X",
        "Title/abstract do not clearly confirm event-camera/DVS/visual-event-stream data or SNN/spiking neural computation.",
        evidence_source,
        "yes",
    )


def high_value_b(row: dict[str, str], abstract: str) -> bool:
    text = f"{row.get('title', '')}\n{abstract}".lower()
    return any(
        term in text
        for term in [
            "event representation",
            "raw event",
            "event cloud",
            "point-based",
            "point cloud",
            "voxel",
            "graph",
            "transformer",
            "mamba",
            "state space",
            "classification",
            "recognition",
            "object detection",
            "tracking",
            "pose",
            "dataset",
            "benchmark",
            "efficient",
            "scalable",
            "latency",
            "deployment",
            "frequency",
        ]
    )


def high_value_c(row: dict[str, str], abstract: str) -> bool:
    text = f"{row.get('title', '')}\n{abstract}".lower()
    return any(
        term in text
        for term in [
            "spiking transformer",
            "spiking vision transformer",
            "spike-driven",
            "surrogate gradient",
            "ann-to-snn",
            "ann2snn",
            "conversion",
            "low-latency",
            "energy-efficient",
            "temporal",
            "lif",
            "quantized",
            "pruned",
        ]
    )


def assign_priority(row: dict[str, str], refined_level: str, abstract: str, overrides: ReadingOverrides) -> str:
    text = f"{row.get('title', '')}\n{abstract}".lower()
    if refined_level == "X":
        return "P3"
    if row["id"] in overrides.advisor_ids or row["id"] in overrides.p0_extra_ids:
        return "P0"
    if any(re.search(pattern, text) for pattern in P3_TITLE_PATTERNS):
        return "P3"
    is_neurips_non_main = (
        row.get("conference") == "NeurIPS"
        and "track: main conference track" not in row.get("notes", "").lower()
        and "track:" in row.get("notes", "").lower()
    )
    if refined_level == "A" and is_neurips_non_main:
        return "P1"
    if refined_level == "A":
        return "P0"
    if refined_level in {"B", "C"}:
        return "P1" if row["id"] in overrides.p1_extra_ids else "P2"
    return "P2"


def markdown_link(label: str, target: str) -> str:
    if target.startswith("01-papers-by-conference/"):
        target = "../" + target
    return f"[{label}]({target})" if target else ""


def table_escape(value: str) -> str:
    return (value or "").replace("\n", " ").replace("|", "\\|")


def current_row_to_md(row: dict[str, str]) -> str:
    card = markdown_link("card", row.get("card_path", ""))
    official = markdown_link("official", row.get("official_page", ""))
    return (
        f"| {table_escape(row.get('title', ''))} | {row.get('year', '')} | {row.get('conference', '')} | "
        f"{row.get('refined_level', '')} | {row.get('priority', '')} | {row.get('advisor_track', '')} | "
        f"current corpus | {table_escape(row.get('reason', ''))} | {card or official} |"
    )


def write_plan(path: Path, title: str, intro: list[str], rows: list[dict[str, str]]) -> None:
    lines = [f"# {title}", ""]
    lines.extend(intro)
    lines.append("")
    lines.extend(
        [
            "| Title | Year | Venue | Refined Level | Priority | Advisor Track | Source | Reason | Link |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    if rows:
        lines.extend(current_row_to_md(row) for row in rows)
    else:
        lines.append("| None |  |  |  |  |  |  |  |  |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def reference_to_md(ref: SecnetReference) -> str:
    return (
        f"| {table_escape(ref.title)} | {ref.authors} | {ref.year} | {ref.venue} | "
        f"{table_escape(ref.why_read)} | {table_escape(ref.relation_to_secnet)} | "
        f"{ref.source} | {ref.whether_in_current_corpus} |"
    )


def write_core_plan(path: Path, current_rows: list[dict[str, str]], overrides: ReadingOverrides) -> None:
    lines = [
        "# Core Reading Plan",
        "",
        "This file is the actual core reading package: `unique(P0 papers + advisor_track papers)` from the current corpus, plus selected SECNet reference-only entries.",
        "Use `reading-plan-p0.md` when you want the strict P0-only 精读 list without advisor-track-only or external SECNet references.",
        "The goal is roughly 60 core readings before enrollment; if the count is lower, do not pad it with weakly related papers.",
        "",
        "## Current Corpus: P0 + Advisor Track",
        "",
        "| Title | Year | Venue | Refined Level | Priority | Advisor Track | Source | Reason | Link |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    if current_rows:
        lines.extend(current_row_to_md(row) for row in current_rows)
    else:
        lines.append("| None |  |  |  |  |  |  |  |  |")
    lines.extend(
        [
            "",
            "## SECNet Reference-Only Entries",
            "",
            "| Title | Authors | Year | Venue | Why Read | Relation to SECNet | Source | In Current Corpus |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    lines.extend(reference_to_md(ref) for ref in overrides.secnet_references)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_advisor_track(path: Path, current_rows: list[dict[str, str]], overrides: ReadingOverrides) -> None:
    lines = [
        "# Advisor Track",
        "",
        "Advisor-track papers are for understanding the SECNet / ICML 2026 method chain before enrollment. This tag does not define a new survey category and does not include future TPAMI extension ideas.",
        "",
        "## In Current Corpus",
        "",
        "| Title | Year | Venue | Refined Level | Priority | Advisor Track | Source | Reason | Link |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    lines.extend(current_row_to_md(row) for row in current_rows if row["advisor_track"] == "yes")
    lines.extend(
        [
            "",
            "## From SECNet References",
            "",
            "| Title | Authors | Year | Venue | Why Read | Relation to SECNet | Source | In Current Corpus |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    lines.extend(reference_to_md(ref) for ref in overrides.secnet_references)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_uncertain(path: Path, rows: list[dict[str, str]]) -> None:
    write_plan(
        path,
        "Uncertain Review",
        [
            "Papers listed here need later human confirmation because title/abstract evidence is broad or insufficient.",
        ],
        [row for row in rows if row.get("uncertain") == "yes"],
    )


def write_level_t(path: Path, current_rows: list[dict[str, str]], overrides: ReadingOverrides) -> None:
    lines = [
        "# Deprecated: Level T Advisor-Direction Reading List",
        "",
        "Level T is no longer maintained as a separate reading category.",
        "",
        "Use `advisor_track` instead:",
        "",
        "- `00-index/advisor-track.md` for the advisor-track reading list.",
        "- `00-index/reading-plan-overrides.yaml` for manual advisor-track IDs and reading-priority overrides.",
        "- `00-index/reading-plan-core.md` for the current core reading plan, defined as `unique(P0 papers + advisor_track papers)` plus selected SECNet reference-only entries.",
        "",
        "This file is kept only as a redirect so older links do not break. Do not edit it by hand; it is regenerated by `scripts/update_reading_plan.py`.",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_rows(repo_root: Path, overrides: ReadingOverrides) -> list[dict[str, str]]:
    all_rows = read_csv(repo_root / "00-index" / "all-papers.csv")
    reviewed = read_reviewed_metadata(repo_root)
    enriched: list[dict[str, str]] = []
    for row in all_rows:
        merged = {column: row.get(column, "") for column in BASE_COLUMNS}
        meta = reviewed.get(row["id"], {})
        abstract = meta.get("abstract", "")
        refined_level, reason, evidence_source, uncertain = classify_refined(merged, abstract, overrides)
        priority = assign_priority(merged, refined_level, abstract, overrides)
        advisor_track = "yes" if row["id"] in overrides.advisor_ids else "no"
        merged.update(
            {
                "refined_level": refined_level,
                "priority": priority,
                "advisor_track": advisor_track,
                "reason": reason,
                "evidence_source": evidence_source,
                "uncertain": "yes" if priority == "P0" and uncertain == "yes" else uncertain,
            }
        )
        if merged["uncertain"] == "yes" and merged["priority"] == "P0":
            merged["priority"] = "P1"
        enriched.append(merged)
    return enriched


def sort_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    priority_order = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
    level_order = {"A": 0, "B": 1, "C": 2, "X": 3}
    return sorted(
        rows,
        key=lambda row: (
            priority_order.get(row.get("priority", ""), 9),
            level_order.get(row.get("refined_level", ""), 9),
            row.get("year", ""),
            row.get("conference", ""),
            row.get("title", ""),
        ),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate core reading-plan indexes.")
    parser.add_argument("--repo-root", type=Path, default=Path.cwd(), help="Repository root")
    parser.add_argument(
        "--overrides",
        type=Path,
        default=Path("00-index/reading-plan-overrides.yaml"),
        help="YAML file with reading-plan manual overrides",
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    overrides_path = args.overrides if args.overrides.is_absolute() else repo_root / args.overrides
    overrides = load_reading_overrides(overrides_path)
    index_dir = repo_root / "00-index"
    index_rows = build_rows(repo_root, overrides)
    rows = sort_rows(index_rows)
    columns = BASE_COLUMNS + READING_COLUMNS
    write_csv(index_dir / "all-papers.csv", index_rows, columns)

    current_advisor_rows = [row for row in rows if row["advisor_track"] == "yes"]
    core_current = [row for row in rows if row["priority"] == "P0" or row["advisor_track"] == "yes"]
    p0_rows = [row for row in rows if row["priority"] == "P0"]
    p1_rows = [row for row in rows if row["priority"] == "P1"]
    p2_rows = [row for row in rows if row["priority"] == "P2"]
    x_rows = [row for row in rows if row["refined_level"] == "X" or row["priority"] == "P3"]

    write_core_plan(index_dir / "reading-plan-core.md", core_current, overrides)
    write_plan(
        index_dir / "reading-plan-p0.md",
        "P0 精读 Reading",
        [
            "Strict P0-only list from the current corpus. This file excludes advisor-track-only papers and SECNet reference-only entries.",
        ],
        p0_rows,
    )
    write_plan(index_dir / "reading-plan-p1.md", "P1 Optional Reading", ["Important papers to read if time allows."], p1_rows)
    write_plan(index_dir / "auto-summary-p2.md", "P2 Auto-Summary Queue", ["Keep these papers for later LLM/Codex summaries rather than human精读."], p2_rows)
    write_plan(index_dir / "out-of-scope-x.md", "Out of Scope / P3", ["Papers retained for auditability but not active reading."], x_rows)
    write_advisor_track(index_dir / "advisor-track.md", rows, overrides)
    write_uncertain(index_dir / "uncertain-review.md", rows)
    write_level_t(index_dir / "level-T-advisor-direction.md", rows, overrides)

    current_core_ids = {row["id"] for row in core_current}
    total_core_unique = len(current_core_ids) + len(overrides.secnet_references)
    counts = Counter(row["refined_level"] for row in rows)
    priorities = Counter(row["priority"] for row in rows)
    uncertain_count = sum(1 for row in rows if row["uncertain"] == "yes")

    print(f"Total papers: {len(rows)}")
    print("Refined levels: " + ", ".join(f"{key}={counts.get(key, 0)}" for key in ["A", "B", "C", "X"]))
    print("Priorities: " + ", ".join(f"{key}={priorities.get(key, 0)}" for key in ["P0", "P1", "P2", "P3"]))
    print(f"P0 current corpus: {len(p0_rows)}")
    print(f"core current corpus (P0 + advisor_track): {len(current_core_ids)}")
    print(f"advisor_track current corpus: {len(current_advisor_rows)}")
    print(f"advisor_track SECNet references: {len(overrides.secnet_references)}")
    print(f"unique(P0 current + advisor_track current + SECNet references): {total_core_unique}")
    print(f"uncertain=yes: {uncertain_count}")
    if total_core_unique > 65:
        print("WARNING: core reading list is above the target range; consider downgrading B/C background papers.")
    elif total_core_unique < 55:
        print("NOTE: core reading list is below 60; do not pad unless later reading reveals a real gap.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
