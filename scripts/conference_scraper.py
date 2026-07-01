#!/usr/bin/env python3
"""Create a venue/year mother list from an official proceedings source.

This script is intentionally conservative. Official proceedings are the primary
source of truth, but proceedings websites vary a lot. The current version can:

- normalize an existing CSV into this workflow's mother-list schema;
- perform a generic HTML anchor scan for likely paper pages;
- leave clear TODOs for venue-specific parsers as they are needed.
"""

from __future__ import annotations

import argparse
import csv
import html.parser
import sys
import urllib.parse
import urllib.request
from pathlib import Path

MOTHER_COLUMNS = [
    "id",
    "title",
    "authors",
    "conference",
    "year",
    "pdf_link",
    "supplementary_link",
    "official_page",
    "abstract",
    "session_type",
    "presentation_status",
    "source_url",
    "notes",
]


class AnchorCollector(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._current_href: str | None = None
        self._current_text: list[str] = []
        self.links: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        attrs_dict = dict(attrs)
        href = attrs_dict.get("href")
        if href:
            self._current_href = href
            self._current_text = []

    def handle_data(self, data: str) -> None:
        if self._current_href is not None:
            self._current_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "a" and self._current_href is not None:
            text = " ".join(" ".join(self._current_text).split())
            self.links.append((self._current_href, text))
            self._current_href = None
            self._current_text = []


def read_text_from_source(url: str | None, html_file: Path | None) -> tuple[str, str]:
    if html_file:
        return html_file.read_text(encoding="utf-8"), str(html_file)
    if not url:
        raise SystemExit("Provide either --official-url or --html-file.")
    with urllib.request.urlopen(url) as response:  # nosec: user-provided research source URL
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace"), url


def normalize_csv(input_csv: Path, output_csv: Path, venue: str, year: str) -> None:
    with input_csv.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = []
        for idx, row in enumerate(reader, start=1):
            normalized = {column: "" for column in MOTHER_COLUMNS}
            normalized.update({key: value for key, value in row.items() if key in normalized})
            normalized["id"] = normalized["id"] or f"{venue}-{year}-{idx:04d}"
            normalized["conference"] = normalized["conference"] or venue
            normalized["year"] = normalized["year"] or year
            rows.append(normalized)
    write_rows(output_csv, rows)


def parse_generic_html(source_text: str, source_url: str, venue: str, year: str) -> list[dict[str, str]]:
    parser = AnchorCollector()
    parser.feed(source_text)
    rows: list[dict[str, str]] = []
    seen_titles: set[str] = set()

    for href, text in parser.links:
        if not text or len(text) < 8:
            continue
        href_lower = href.lower()
        likely_paper_page = any(token in href_lower for token in ("paper", "/html/", "content/"))
        likely_nonpaper = any(token in href_lower for token in ("supp", "supplement", "bibtex", "program"))
        if not likely_paper_page or likely_nonpaper:
            continue
        title = " ".join(text.split())
        if title.lower() in seen_titles:
            continue
        seen_titles.add(title.lower())
        official_page = urllib.parse.urljoin(source_url, href)
        rows.append(
            {
                "id": f"{venue}-{year}-{len(rows) + 1:04d}",
                "title": title,
                "authors": "",
                "conference": venue,
                "year": year,
                "pdf_link": "",
                "supplementary_link": "",
                "official_page": official_page,
                "abstract": "",
                "session_type": "",
                "presentation_status": "",
                "source_url": source_url,
                "notes": "generic HTML parse; verify against official proceedings",
            }
        )
    return rows


def write_rows(output_csv: Path, rows: list[dict[str, str]]) -> None:
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    with output_csv.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=MOTHER_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build mother-list.csv from an official venue source.")
    parser.add_argument("--venue", required=True, help="Venue name, e.g. CVPR")
    parser.add_argument("--year", required=True, help="Venue year, e.g. 2025")
    parser.add_argument("--output-dir", required=True, type=Path, help="Conference output directory")
    parser.add_argument("--official-url", help="Official proceedings URL")
    parser.add_argument("--html-file", type=Path, help="Saved official proceedings HTML file")
    parser.add_argument("--input-csv", type=Path, help="Existing paper list CSV to normalize")
    args = parser.parse_args()

    output_csv = args.output_dir / "mother-list.csv"
    if args.input_csv:
        normalize_csv(args.input_csv, output_csv, args.venue, args.year)
        print(f"Wrote normalized mother list: {output_csv}")
        return 0

    source_text, source_url = read_text_from_source(args.official_url, args.html_file)
    rows = parse_generic_html(source_text, source_url, args.venue, args.year)
    write_rows(output_csv, rows)
    print(f"Wrote {len(rows)} tentative rows to {output_csv}")
    if not rows:
        print("TODO: add a venue-specific parser for this proceedings format.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
