#!/usr/bin/env python3
"""Generate Markdown paper cards from abc-reviewed.csv.

The script refuses to generate cards without abstracts by default because cards
must contain paper-specific summaries rather than template placeholder text.
"""

from __future__ import annotations

import argparse
import csv
import re
import textwrap
from pathlib import Path


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value[:90] or "untitled-paper"


def split_sentences(text: str) -> list[str]:
    text = " ".join(text.split())
    if not text:
        return []
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [part.strip() for part in parts if part.strip()]


def yaml_list(value: str) -> str:
    items = [item.strip() for item in re.split(r";|, and | and ", value) if item.strip()]
    if not items:
        return "[]"
    return "[" + ", ".join(repr(item).replace("'", '"') for item in items) + "]"


def frontmatter(row: dict[str, str], status: str) -> str:
    return "\n".join(
        [
            "---",
            f'title: "{row.get("title", "").replace(chr(34), chr(39))}"',
            f"authors: {yaml_list(row.get('authors', ''))}",
            f'conference: "{row.get("conference", "")}"',
            f"year: {row.get('year', '')}",
            f'level: "{row.get("level", "")}"',
            f'category: "{row.get("category", "")}"',
            f'pdf_link: "{row.get("pdf_link", "")}"',
            f'official_page: "{row.get("official_page", "")}"',
            "tags: []",
            f'abstract: "{row.get("abstract", "").replace(chr(34), chr(39))}"',
            f'status: "{status}"',
            "---",
            "",
        ]
    )


def paragraph(text: str, width: int = 92) -> str:
    return textwrap.fill(" ".join(text.split()), width=width)


def build_a_card(row: dict[str, str]) -> str:
    abstract = row["abstract"]
    sentences = split_sentences(abstract)
    first = sentences[0]
    second = sentences[1] if len(sentences) > 1 else sentences[0]
    remainder = " ".join(sentences[2:]) if len(sentences) > 2 else abstract

    return frontmatter(row, "auto-generated; needs human review") + "\n".join(
        [
            "## Core Problem",
            "",
            paragraph(f"The paper addresses the problem described in its abstract: {first}"),
            "",
            "## Core Method",
            "",
            paragraph(f"The central method signal from the abstract is: {second}"),
            "",
            "## Key Metrics and Findings",
            "",
            paragraph("Extract exact metrics, datasets, and quantitative findings during human review. Automated generation only preserves the abstract-level evidence here."),
            "",
            "## Personal Notes",
            "",
            paragraph("Add reading notes, concerns, and survey positioning after manual verification."),
            "",
            "## Method Details",
            "",
            paragraph(remainder),
            "",
            "## Experimental Analysis",
            "",
            paragraph("Verify datasets, baselines, metrics, latency, energy, and ablation claims against the official paper PDF."),
            "",
            "## Related Work Connections",
            "",
            paragraph("Connect this paper to Level B event-camera papers and Level C SNN papers after the venue search is complete."),
            "",
            "## Survey-Usable Points",
            "",
            paragraph("Potential survey point: this is an A-level candidate because classification found both event-camera and SNN/spiking signals. Confirm the exact mechanism before citing."),
            "",
        ]
    )


def build_bc_card(row: dict[str, str]) -> str:
    abstract = row["abstract"]
    sentences = split_sentences(abstract)
    first = sentences[0]
    second = sentences[1] if len(sentences) > 1 else sentences[0]
    return frontmatter(row, "auto-generated; brief scan note") + "\n".join(
        [
            "## Core Problem",
            "",
            paragraph(first),
            "",
            "## Core Method",
            "",
            paragraph(second),
            "",
        ]
    )


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate paper cards from abc-reviewed.csv.")
    parser.add_argument("--input", required=True, type=Path, help="Path to abc-reviewed.csv")
    parser.add_argument("--cards-dir", type=Path, help="Output cards directory")
    parser.add_argument("--allow-missing-abstract", action="store_true", help="Generate title-only stubs when abstracts are missing")
    args = parser.parse_args()

    cards_dir = args.cards_dir or args.input.parent / "cards"
    cards_dir.mkdir(parents=True, exist_ok=True)
    generated = 0
    skipped = 0

    for row in read_rows(args.input):
        level = row.get("level", "").upper()
        if level not in {"A", "B", "C"}:
            continue
        if not row.get("abstract", "").strip() and not args.allow_missing_abstract:
            skipped += 1
            print(f"Skipped missing abstract: {row.get('title', row.get('id', 'unknown'))}")
            continue
        if not row.get("abstract", "").strip():
            row["abstract"] = f"Title-only note for manual completion: {row.get('title', '')}"
        filename = f"{row.get('id') or slugify(row.get('title', 'untitled'))}-{slugify(row.get('title', 'untitled'))}.md"
        path = cards_dir / filename
        content = build_a_card(row) if level == "A" else build_bc_card(row)
        path.write_text(content, encoding="utf-8")
        generated += 1

    print(f"Generated {generated} cards in {cards_dir}")
    if skipped:
        print(f"Skipped {skipped} rows with missing abstracts. Add abstracts or rerun with --allow-missing-abstract for stubs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
