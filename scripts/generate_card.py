#!/usr/bin/env python3
"""Generate filled Markdown paper cards from abc-reviewed.csv.

B/C cards intentionally keep the same four visible sections as A cards in this
workflow: Core Problem, Core Method, Key Metrics and Findings, and Personal
Notes.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import textwrap
from pathlib import Path

ABC_COLUMNS = [
    "id",
    "title",
    "authors",
    "conference",
    "year",
    "level",
    "category",
    "official_page",
    "pdf_link",
    "abstract",
    "matched_keywords",
    "classification_reason",
    "card_path",
    "notes",
]


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value[:90] or "untitled-paper"


def split_sentences(text: str) -> list[str]:
    text = " ".join(text.split())
    if not text or text == "Unknown":
        return []
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [part.strip() for part in parts if part.strip()]


def yaml_string(value: str) -> str:
    return json.dumps(value or "Unknown", ensure_ascii=False)


def yaml_list(value: str) -> str:
    if not value or value == "Unknown":
        return "[]"
    parts = [item.strip() for item in re.split(r";|, and | and ", value) if item.strip()]
    return "[" + ", ".join(json.dumps(part, ensure_ascii=False) for part in parts) + "]"


def paragraph(text: str, width: int = 92) -> str:
    return textwrap.fill(" ".join(text.split()), width=width)


def frontmatter(row: dict[str, str], status: str) -> str:
    return "\n".join(
        [
            "---",
            f"title: {yaml_string(row.get('title', 'Unknown'))}",
            f"authors: {yaml_list(row.get('authors', ''))}",
            f"conference: {yaml_string(row.get('conference', 'Unknown'))}",
            f"year: {row.get('year') or 'Unknown'}",
            f"level: {yaml_string(row.get('level', 'Unknown'))}",
            f"category: {yaml_string(row.get('category', 'Unknown'))}",
            f"pdf_link: {yaml_string(row.get('pdf_link', 'Unknown'))}",
            f"official_page: {yaml_string(row.get('official_page', 'Unknown'))}",
            "tags: []",
            f"abstract: {yaml_string(row.get('abstract', 'Unknown'))}",
            f"status: {yaml_string(status)}",
            "---",
            "",
        ]
    )


def evidence_summary(row: dict[str, str]) -> str:
    keywords = row.get("matched_keywords", "") or "Unknown"
    reason = row.get("classification_reason", "") or "Needs human review"
    return f"检索命中关键词：{keywords}。自动分类理由：{reason}。"


def abstract_sentence(row: dict[str, str], index: int, fallback: str) -> str:
    sentences = split_sentences(row.get("abstract", ""))
    if index < len(sentences):
        return sentences[index]
    return fallback


def build_a_card(row: dict[str, str]) -> str:
    title = row.get("title", "Unknown")
    problem = abstract_sentence(row, 0, f"官方摘要不足，需要人工阅读论文确认 {title} 的核心问题。")
    method = abstract_sentence(row, 1, "方法细节需要从官方论文 PDF 或论文页面进一步核验。")
    detail = " ".join(split_sentences(row.get("abstract", ""))[2:]) or "摘要信息不足，暂不能可靠提取更细的方法细节。"

    return frontmatter(row, "auto-generated; needs human review") + "\n".join(
        [
            "## Core Problem",
            "",
            paragraph(f"{problem}"),
            "",
            "## Core Method",
            "",
            paragraph(f"{method}"),
            "",
            "## Key Metrics and Findings",
            "",
            paragraph("自动流程尚未深读 PDF，不能可靠提取完整指标、数据集、对比方法和数值结论；需要人工核验后补充。"),
            "",
            "## Personal Notes",
            "",
            paragraph(evidence_summary(row) + " 该卡片用于优先阅读队列，引用前必须核对官方论文。"),
            "",
            "## Method Details",
            "",
            paragraph(detail),
            "",
            "## Experimental Analysis",
            "",
            paragraph("需要人工检查实验数据集、任务设置、baselines、消融、延迟、能耗与硬件条件，避免把摘要级表述当成最终结论。"),
            "",
            "## Related Work Connections",
            "",
            paragraph("该论文应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认它真正处在 SNN 与事件相机交叉点。"),
            "",
            "## Survey-Usable Points",
            "",
            paragraph("可作为交叉方向候选核心论文；最终可用观点需要在人工阅读全文后再写入综述草稿。"),
            "",
        ]
    )


def build_bc_card(row: dict[str, str]) -> str:
    title = row.get("title", "Unknown")
    problem = abstract_sentence(row, 0, f"官方摘要不足，需要人工确认 {title} 的研究问题。")
    method = abstract_sentence(row, 1, "方法信息不足，需要人工从官方页面或 PDF 补充。")
    metrics = "尚未深读 PDF，指标、数据集和定量结果需要人工核验。"
    notes = evidence_summary(row)
    return frontmatter(row, "auto-generated; brief scan note") + "\n".join(
        [
            "## Core Problem",
            "",
            paragraph(problem),
            "",
            "## Core Method",
            "",
            paragraph(method),
            "",
            "## Key Metrics and Findings",
            "",
            paragraph(metrics),
            "",
            "## Personal Notes",
            "",
            paragraph(notes),
            "",
        ]
    )


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    columns = list(dict.fromkeys(list(rows[0].keys()) + ABC_COLUMNS)) if rows else ABC_COLUMNS
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def card_path_for(row: dict[str, str], conference_dir: Path, repo_root: Path) -> Path:
    level = row.get("level", "").upper()
    venue = row.get("conference", "VENUE").upper().replace(" ", "")
    year = row.get("year", "YEAR")
    title_slug = slugify(row.get("title", "untitled"))
    filename = f"{year}-{venue}-{level}-{title_slug}.md"
    return conference_dir / level / filename


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate A/B/C paper cards from abc-reviewed.csv.")
    parser.add_argument("--input", required=True, type=Path, help="Path to abc-reviewed.csv")
    parser.add_argument("--repo-root", type=Path, default=Path.cwd(), help="Repository root")
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    conference_dir = args.input.parent.resolve()
    rows = read_rows(args.input)
    generated = 0

    for row in rows:
        level = row.get("level", "").upper()
        if level not in {"A", "B", "C"}:
            continue
        row["abstract"] = row.get("abstract", "") or "Unknown"
        path = card_path_for(row, conference_dir, repo_root)
        path.parent.mkdir(parents=True, exist_ok=True)
        content = build_a_card(row) if level == "A" else build_bc_card(row)
        path.write_text(content, encoding="utf-8")
        row["card_path"] = path.relative_to(repo_root).as_posix()
        generated += 1

    write_rows(args.input, rows)
    print(f"Generated {generated} cards and updated card_path in {args.input}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
