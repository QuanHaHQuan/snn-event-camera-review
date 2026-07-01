#!/usr/bin/env python3
"""Update global indexes from reviewed venue CSV files."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

GLOBAL_COLUMNS = [
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

LEVEL_FILES = {
    "A": "level-A-papers.md",
    "B": "level-B-event-camera.md",
    "C": "level-C-snn.md",
}

LEVEL_TITLES = {
    "A": "Level A Papers",
    "B": "Level B Event-Camera Papers",
    "C": "Level C SNN Papers",
}

LEVEL_DESCRIPTIONS = {
    "A": "Core intersection papers combining SNN/spiking computation with event-camera data or event-based vision.",
    "B": "Event-camera-side background papers without clear SNN/spiking neural network use.",
    "C": "SNN-side background papers without clear event-camera or DVS data use.",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def find_card_path(repo_root: Path, row: dict[str, str], conference_dir: Path) -> str:
    explicit = row.get("card_path", "").strip()
    if explicit:
        return explicit
    cards_dir = conference_dir / "cards"
    if not cards_dir.exists():
        return ""
    paper_id = row.get("id", "")
    if paper_id:
        matches = sorted(cards_dir.glob(f"{paper_id}-*.md"))
        if matches:
            return matches[0].relative_to(repo_root).as_posix()
    return ""


def normalize_row(repo_root: Path, conference_dir: Path, row: dict[str, str]) -> dict[str, str]:
    return {
        "id": row.get("id", ""),
        "title": row.get("title", ""),
        "authors": row.get("authors", ""),
        "conference": row.get("conference", ""),
        "year": row.get("year", ""),
        "level": row.get("level", ""),
        "category": row.get("category", ""),
        "pdf_link": row.get("pdf_link", ""),
        "official_page": row.get("official_page", ""),
        "card_path": find_card_path(repo_root, row, conference_dir),
        "notes": row.get("classification_notes", row.get("notes", "")),
    }


def collect_reviewed_rows(repo_root: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    conference_root = repo_root / "01-papers-by-conference"
    for csv_path in sorted(conference_root.glob("*/abc-reviewed.csv")):
        conference_dir = csv_path.parent
        for row in read_csv(csv_path):
            if row.get("level", "").upper() in {"A", "B", "C"}:
                rows.append(normalize_row(repo_root, conference_dir, row))
    rows.sort(key=lambda row: (row.get("year", ""), row.get("conference", ""), row.get("level", ""), row.get("title", "")))
    return rows


def write_all_papers(index_dir: Path, rows: list[dict[str, str]]) -> None:
    with (index_dir / "all-papers.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=GLOBAL_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def markdown_link(label: str, path_or_url: str) -> str:
    if not path_or_url:
        return ""
    return f"[{label}]({path_or_url})"


def write_level_indexes(index_dir: Path, rows: list[dict[str, str]]) -> None:
    for level, filename in LEVEL_FILES.items():
        level_rows = [row for row in rows if row.get("level", "").upper() == level]
        lines = [f"# {LEVEL_TITLES[level]}", "", LEVEL_DESCRIPTIONS[level], ""]
        if not level_rows:
            lines.append("No papers indexed yet.")
        else:
            lines.extend(["| Year | Conference | Title | Card | Official Page | Notes |", "| --- | --- | --- | --- | --- | --- |"])
            for row in level_rows:
                card = markdown_link("card", row.get("card_path", ""))
                official = markdown_link("official", row.get("official_page", ""))
                lines.append(
                    "| {year} | {conference} | {title} | {card} | {official} | {notes} |".format(
                        year=row.get("year", ""),
                        conference=row.get("conference", ""),
                        title=row.get("title", ""),
                        card=card,
                        official=official,
                        notes=row.get("notes", ""),
                    )
                )
        (index_dir / filename).write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Refresh 00-index from conference review outputs.")
    parser.add_argument("--repo-root", type=Path, default=Path.cwd(), help="Repository root")
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    index_dir = repo_root / "00-index"
    rows = collect_reviewed_rows(repo_root)
    write_all_papers(index_dir, rows)
    write_level_indexes(index_dir, rows)
    print(f"Updated global indexes with {len(rows)} A/B/C papers.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
