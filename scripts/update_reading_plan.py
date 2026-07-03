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

CURRENT_ADVISOR_IDS = {
    "ICCV2025-1060",
    "ICCV2025-1983",
    "NeurIPS2025-5608",
    "ICML2025-0323",
    "NeurIPS2025-2692",
    "NeurIPS2025-4086",
    "CVPR2026-1228",
    "CVPR2026-2918",
    "CVPR2026-1312",
    "ECCV2024-1631",
    "ICCV2025-1879",
    "ICCV2025-1798",
    "ICLR2025-1232",
    "NeurIPS2025-0641",
    "ICML2025-2762",
}

P0_EXTRA_IDS = {
    # A-level survey-core papers not necessarily in advisor_track.
    "ECCV2024-1168",
    "ECCV2024-1740",
    "ECCV2024-1778",
    "ICCV2025-1790",
    "CVPR2026-1798",
    "CVPR2026-1873",
    "CVPR2026-3630",
    "NeurIPS2025-4041",
    # High-value event-camera representation/background papers.
    "ICCV2025-0082",
    "ICCV2025-1538",
    "CVPR2026-0479",
    "ECCV2024-1591",
    "NeurIPS2025-4822",
    "CVPR2026-3561",
    "CVPR2026-2514",
    "CVPR2026-1573",
    "CVPR2026-0881",
    "NeurIPS2025-2978",
    "NeurIPS2025-2173",
    # High-value SNN background papers.
    "ICLR2025-0872",
    "ICLR2025-0522",
    "ICLR2025-2660",
    "ICLR2025-3479",
    "ICML2025-3117",
    "ICML2025-3251",
    "NeurIPS2025-3401",
    "NeurIPS2025-3455",
    "NeurIPS2025-5334",
}

P1_EXTRA_IDS = {
    # Representative event-camera background to read only if time allows.
    "ECCV2024-0732",
    "ECCV2024-0945",
    "ECCV2024-1083",
    "ECCV2024-1102",
    "ECCV2024-1328",
    "ECCV2024-1636",
    "ECCV2024-1737",
    "ECCV2024-1884",
    "ECCV2024-2251",
    "ECCV2024-2318",
    "ICCV2025-0953",
    "ICCV2025-1066",
    "ICCV2025-1773",
    "ICCV2025-1940",
    "ICCV2025-2463",
    "ICCV2025-2618",
    "ICLR2025-0595",
    "NeurIPS2025-0035",
    "NeurIPS2025-1018",
    "NeurIPS2025-1126",
    "NeurIPS2025-1159",
    "NeurIPS2025-1835",
    "NeurIPS2025-4192",
    "NeurIPS2025-4786",
    "CVPR2026-0298",
    "CVPR2026-0516",
    "CVPR2026-0912",
    "CVPR2026-1239",
    "CVPR2026-1824",
    "CVPR2026-2084",
    "CVPR2026-2308",
    "CVPR2026-2511",
    "CVPR2026-3465",
    # Representative SNN background to read after the core set.
    "ECCV2024-0537",
    "ECCV2024-1361",
    "ECCV2024-1484",
    "ICCV2025-1096",
    "ICLR2025-1551",
    "ICLR2025-2158",
    "ICML2025-0988",
    "ICML2025-1579",
    "ICML2025-1843",
    "ICML2025-2813",
    "ICML2025-2940",
    "NeurIPS2025-1514",
    "NeurIPS2025-2213",
    "NeurIPS2025-3724",
    "NeurIPS2025-5098",
    "NeurIPS2025-5157",
    "NeurIPS2025-5700",
    "CVPR2026-0399",
    "CVPR2026-2929",
}

FORCE_REFINED_C = {
    # Generic SNN methods with event-camera datasets used as benchmarks only.
    "ECCV2024-1484",
    "ICLR2025-1232",
    "ICLR2025-1551",
    "ICLR2025-2158",
    "ICML2025-2813",
    "ICML2025-2940",
    "NeurIPS2025-3724",
    "NeurIPS2025-5098",
    "NeurIPS2025-2213",
}

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


SECNET_REFERENCES = [
    SecnetReference(
        title="Rethinking Efficient and Effective Point-based Networks for Event Camera Classification and Regression",
        authors="Hongwei Ren et al.",
        year="2025",
        venue="TPAMI",
        why_read="Direct predecessor from the advisor group and the closest conceptual parent of SECNet.",
        relation_to_secnet="Point-based event-camera classification/regression and EventMamba-style method chain.",
    ),
    SecnetReference(
        title="SpikePoint: An Efficient Point-based Spiking Neural Network for Event Cameras Action Recognition",
        authors="Hongwei Ren et al.",
        year="2024",
        venue="ICLR",
        why_read="Advisor-group point-based SNN bridge between the survey topic and SECNet's event-cloud direction.",
        relation_to_secnet="Point-based event-camera action recognition and SNN/event-camera intersection.",
    ),
    SecnetReference(
        title="TTPOINT: A Tensorized Point Cloud Network for Lightweight Action Recognition with Event Cameras",
        authors="Hongwei Ren et al.",
        year="2023",
        venue="ACM MM",
        why_read="Advisor-group lightweight point/event representation baseline.",
        relation_to_secnet="Tensorized point-cloud processing for event-camera action recognition.",
    ),
    SecnetReference(
        title="Event Voxel Set Transformer for Spatiotemporal Representation Learning on Event Streams",
        authors="B. Xie et al.",
        year="2024",
        venue="TCSVT",
        why_read="Recent event-stream voxel/set-transformer baseline.",
        relation_to_secnet="Voxel/set-transformer contrast against SECNet's Event Cloud representation.",
    ),
    SecnetReference(
        title="Voxel-based Multi-Scale Transformer Network for Event Stream Processing",
        authors="D. Liu, T. Wang, and C. Sun",
        year="2023",
        venue="TCSVT",
        why_read="VMST-Net is a direct SECNet comparison target.",
        relation_to_secnet="Voxel-based transformer baseline for event stream processing.",
    ),
    SecnetReference(
        title="Action Recognition and Benchmark Using Event Cameras",
        authors="Y. Gao et al.",
        year="2023",
        venue="TPAMI",
        why_read="Important event-camera action-recognition benchmark context.",
        relation_to_secnet="THUE-ACT-50 and recognition benchmark context used around SECNet.",
    ),
    SecnetReference(
        title="Mamba: Linear-Time Sequence Modeling with Selective State Spaces",
        authors="Albert Gu and Tri Dao",
        year="2023",
        venue="arXiv / core architecture",
        why_read="Core sequence-modeling architecture behind Mamba-style event networks.",
        relation_to_secnet="Background for state-space sequence modeling comparisons.",
    ),
]


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


def classify_refined(row: dict[str, str], abstract: str) -> tuple[str, str, str, str]:
    text = "\n".join([row.get("title", ""), abstract or ""])
    title = row.get("title", "")
    event_explicit = pattern_hits(text, EVENT_EXPLICIT_PATTERNS)
    event_bench = pattern_hits(text, EVENT_BENCHMARK_PATTERNS)
    event_context = [] if has_generic_bad_event_context(text) else pattern_hits(text, EVENT_CONTEXT_PATTERNS)
    snn = pattern_hits(text, SNN_PATTERNS)
    evidence_source = "abstract" if abstract else "metadata"

    if row["id"] in FORCE_REFINED_C and snn:
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

    if has_event and has_snn and not event_is_only_benchmark and title_has_event:
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


def assign_priority(row: dict[str, str], refined_level: str, abstract: str) -> str:
    text = f"{row.get('title', '')}\n{abstract}".lower()
    if refined_level == "X":
        return "P3"
    if row["id"] in CURRENT_ADVISOR_IDS or row["id"] in P0_EXTRA_IDS:
        return "P0"
    if any(re.search(pattern, text) for pattern in P3_TITLE_PATTERNS):
        return "P3"
    if refined_level == "A":
        return "P0"
    if refined_level in {"B", "C"}:
        return "P1" if row["id"] in P1_EXTRA_IDS else "P2"
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


def write_advisor_track(path: Path, current_rows: list[dict[str, str]]) -> None:
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
    lines.extend(reference_to_md(ref) for ref in SECNET_REFERENCES)
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


def write_level_t(path: Path, current_rows: list[dict[str, str]]) -> None:
    advisor = [row for row in current_rows if row["advisor_track"] == "yes"]
    t0 = advisor[:8]
    t1 = advisor[8:]
    lines = [
        "# Level T Advisor-Direction Reading List",
        "",
        "Level T is now maintained as the `advisor_track` tag. This file is a compact view only; the full source of truth is `advisor-track.md` and the fields in `all-papers.csv`.",
        "",
        "## T0: Read First",
        "",
        "| Title | Year | Venue | Refined Level | Priority | Link |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in t0:
        lines.append(
            f"| {table_escape(row['title'])} | {row['year']} | {row['conference']} | {row['refined_level']} | {row['priority']} | {markdown_link('card', row.get('card_path', ''))} |"
        )
    lines.extend(["", "## T1: Read After T0", "", "| Title | Year | Venue | Refined Level | Priority | Link |", "| --- | --- | --- | --- | --- | --- |"])
    for row in t1:
        lines.append(
            f"| {table_escape(row['title'])} | {row['year']} | {row['conference']} | {row['refined_level']} | {row['priority']} | {markdown_link('card', row.get('card_path', ''))} |"
        )
    lines.extend(
        [
            "",
            "## SECNet Reference-Only Papers",
            "",
            "| Title | Year | Venue | Why Read |",
            "| --- | --- | --- | --- |",
        ]
    )
    for ref in SECNET_REFERENCES:
        lines.append(f"| {table_escape(ref.title)} | {ref.year} | {ref.venue} | {table_escape(ref.why_read)} |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_rows(repo_root: Path) -> list[dict[str, str]]:
    all_rows = read_csv(repo_root / "00-index" / "all-papers.csv")
    reviewed = read_reviewed_metadata(repo_root)
    enriched: list[dict[str, str]] = []
    for row in all_rows:
        merged = {column: row.get(column, "") for column in BASE_COLUMNS}
        meta = reviewed.get(row["id"], {})
        abstract = meta.get("abstract", "")
        refined_level, reason, evidence_source, uncertain = classify_refined(merged, abstract)
        priority = assign_priority(merged, refined_level, abstract)
        advisor_track = "yes" if row["id"] in CURRENT_ADVISOR_IDS else "no"
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
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    index_dir = repo_root / "00-index"
    index_rows = build_rows(repo_root)
    rows = sort_rows(index_rows)
    columns = BASE_COLUMNS + READING_COLUMNS
    write_csv(index_dir / "all-papers.csv", index_rows, columns)

    current_advisor_rows = [row for row in rows if row["advisor_track"] == "yes"]
    core_current = [row for row in rows if row["priority"] == "P0" or row["advisor_track"] == "yes"]
    p1_rows = [row for row in rows if row["priority"] == "P1"]
    p2_rows = [row for row in rows if row["priority"] == "P2"]
    x_rows = [row for row in rows if row["refined_level"] == "X" or row["priority"] == "P3"]

    write_plan(
        index_dir / "reading-plan-core.md",
        "Core Reading Plan",
        [
            "This file lists `unique(P0 papers + advisor_track papers)` from the current corpus, followed by compact SECNet reference-only entries in `advisor-track.md`.",
            "The goal is roughly 60 core readings before enrollment; if the count is lower, do not pad it with weakly related papers.",
        ],
        core_current,
    )
    write_plan(index_dir / "reading-plan-p1.md", "P1 Optional Reading", ["Important papers to read if time allows."], p1_rows)
    write_plan(index_dir / "auto-summary-p2.md", "P2 Auto-Summary Queue", ["Keep these papers for later LLM/Codex summaries rather than human精读."], p2_rows)
    write_plan(index_dir / "out-of-scope-x.md", "Out of Scope / P3", ["Papers retained for auditability but not active reading."], x_rows)
    write_advisor_track(index_dir / "advisor-track.md", rows)
    write_uncertain(index_dir / "uncertain-review.md", rows)
    write_level_t(index_dir / "level-T-advisor-direction.md", rows)

    current_core_ids = {row["id"] for row in core_current}
    total_core_unique = len(current_core_ids) + len(SECNET_REFERENCES)
    counts = Counter(row["refined_level"] for row in rows)
    priorities = Counter(row["priority"] for row in rows)
    uncertain_count = sum(1 for row in rows if row["uncertain"] == "yes")

    print(f"Total papers: {len(rows)}")
    print("Refined levels: " + ", ".join(f"{key}={counts.get(key, 0)}" for key in ["A", "B", "C", "X"]))
    print("Priorities: " + ", ".join(f"{key}={priorities.get(key, 0)}" for key in ["P0", "P1", "P2", "P3"]))
    print(f"advisor_track current corpus: {len(current_advisor_rows)}")
    print(f"advisor_track SECNet references: {len(SECNET_REFERENCES)}")
    print(f"unique(P0 current + advisor_track current + SECNet references): {total_core_unique}")
    print(f"uncertain=yes: {uncertain_count}")
    if total_core_unique > 65:
        print("WARNING: core reading list is above the target range; consider downgrading B/C background papers.")
    elif total_core_unique < 55:
        print("NOTE: core reading list is below 60; do not pad unless later reading reveals a real gap.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
