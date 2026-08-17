#!/usr/bin/env python3
"""Generate retained-paper metadata and the conference inventory."""

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
    "official_track",
    "level",
    "category",
    "pdf_link",
    "official_page",
    "card_path",
    "notes",
]

OFFICIAL_PROCEEDINGS = {
    "CVPR2024": "https://openaccess.thecvf.com/CVPR2024?day=all",
    "CVPR2025": "https://openaccess.thecvf.com/CVPR2025?day=all",
    "CVPR2026": "https://openaccess.thecvf.com/CVPR2026?day=all",
    "ECCV2024": "https://eccv.ecva.net/virtual/2024/papers.html",
    "ICCV2025": "https://openaccess.thecvf.com/ICCV2025?day=all",
    "ICLR2024": "https://proceedings.iclr.cc/paper_files/paper/2024",
    "ICLR2025": "https://proceedings.iclr.cc/paper_files/paper/2025",
    "ICLR2026": "https://proceedings.iclr.cc/paper_files/paper/2026",
    "ICML2024": "https://proceedings.mlr.press/v235/",
    "ICML2025": "https://proceedings.mlr.press/v267/",
    "NeurIPS2024": "https://papers.nips.cc/paper_files/paper/2024",
    "NeurIPS2025": "https://papers.nips.cc/paper_files/paper/2025",
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


def normalize_track(value: str) -> str:
    return value.strip().removeprefix("Track: ")


def normalize_row(
    repo_root: Path,
    conference_dir: Path,
    row: dict[str, str],
    official_track: str,
) -> dict[str, str]:
    notes = row.get("notes", "").strip()
    reason = row.get("classification_reason", row.get("classification_notes", "")).strip()
    combined_notes = "; ".join(part for part in (notes, reason) if part)
    return {
        "id": row.get("id", ""),
        "title": row.get("title", ""),
        "authors": row.get("authors", ""),
        "conference": row.get("conference", ""),
        "year": row.get("year", ""),
        "official_track": official_track,
        "level": row.get("level", ""),
        "category": row.get("category", ""),
        "pdf_link": row.get("pdf_link", ""),
        "official_page": row.get("official_page", ""),
        "card_path": find_card_path(repo_root, row, conference_dir),
        "notes": combined_notes,
    }


def collect_reviewed_rows(repo_root: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    conference_root = repo_root / "01-papers-by-conference"
    for csv_path in sorted(conference_root.glob("*/abc-reviewed.csv")):
        conference_dir = csv_path.parent
        mother_path = conference_dir / "mother-list.csv"
        mother_by_id = {
            mother_row.get("id", ""): mother_row
            for mother_row in read_csv(mother_path)
        } if mother_path.exists() else {}
        for row in read_csv(csv_path):
            if row.get("level", "").upper() in {"A", "B", "C"}:
                mother_row = mother_by_id.get(row.get("id", ""), {})
                official_track = ""
                if row.get("conference", "") == "NeurIPS":
                    official_track = normalize_track(
                        mother_row.get("track", "")
                        or mother_row.get("status_or_award", "")
                    )
                rows.append(
                    normalize_row(repo_root, conference_dir, row, official_track)
                )
    rows.sort(key=lambda row: (-int(row.get("year", "0") or 0), row.get("conference", ""), row.get("title", "")))
    return rows


def write_all_papers(index_dir: Path, rows: list[dict[str, str]]) -> None:
    with (index_dir / "retained-papers.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=GLOBAL_COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_conferences(index_dir: Path, repo_root: Path) -> None:
    conference_root = repo_root / "01-papers-by-conference"
    lines = [
        "# Conferences",
        "",
        "Track venue/year searches here after processing.",
        "",
        "| Venue | Year | Official Source | Folder | Status | Notes |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for csv_path in sorted(conference_root.glob("*/mother-list.csv")):
        folder = csv_path.parent
        rows = read_csv(csv_path)
        first = rows[0] if rows else {}
        venue = first.get("conference", folder.name)
        year = first.get("year", "")
        source = first.get("source_url", "") or OFFICIAL_PROCEEDINGS.get(folder.name, "")
        status = "processed" if (folder / "abc-reviewed.csv").exists() else "mother-list only"
        notes = f"{len(rows)} papers" if rows else "No rows"
        rel_folder = folder.relative_to(repo_root).as_posix()
        source_link = f"[official proceedings]({source})" if source else "-"
        folder_link = f"[{folder.name}](../{rel_folder}/)"
        lines.append(
            f"| {venue} | {year} | {source_link} | {folder_link} | {status} | {notes} |"
        )
    (index_dir / "conferences.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Refresh 00-index from conference review outputs.")
    parser.add_argument("--repo-root", type=Path, default=Path.cwd(), help="Repository root")
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    index_dir = repo_root / "00-index"
    rows = collect_reviewed_rows(repo_root)
    write_all_papers(index_dir, rows)
    write_conferences(index_dir, repo_root)
    print(f"Updated retained-paper metadata with {len(rows)} A/B/C provenance rows.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
