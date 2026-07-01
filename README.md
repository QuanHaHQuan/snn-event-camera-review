# SNN Event Camera Review

This repository stores a systematic, venue-specific literature review workflow for the survey topic **Spiking Neural Networks for Event Cameras**.

The purpose is to keep literature search results reproducible and auditable: each conference search should preserve the official paper list, candidate retrieval logic, classification decisions, generated paper cards, human review notes, and global indexes used for future survey drafting.

## Repository Structure

```text
00-index/                  Global paper indexes and topic lists
01-papers-by-conference/   Venue/year search outputs and paper cards
02-topic-notes/            Cross-paper notes organized by survey theme
03-review-draft/           Draft survey outline and manuscript sections
04-templates/              Reusable paper card and report templates
05-logs/                   Search logs and Codex run notes
scripts/                   Workflow automation scripts
```

## Classification Rules

Use the same A/B/C/D/E rules across reports, cards, scripts, and indexes.

**A = Intersection / core paper**

Explicitly combines SNN/spiking neural computation with event cameras, DVS, visual event streams, event-camera datasets, or event-based vision based on event-camera data.

**B = Event-camera-side paper**

Clearly about event cameras, DVS, dynamic vision sensors, visual event streams, event-camera datasets, or event-camera tasks, but does not clearly use SNN/spiking neural networks.

**C = SNN-side paper**

Clearly about SNNs, spiking neural networks, spiking transformers, ANN-to-SNN conversion, surrogate gradients, spike trains, LIF/IF neurons, or SNN training/inference, but does not clearly involve event cameras/DVS/event-camera data.

**D = Adjacent/background paper**

Related to asynchronous processing, temporal sparsity, event-driven computation, low-latency vision, neuromorphic sensors, or spike cameras, but not clearly about event cameras/DVS or SNNs.

**E = False positive**

Keyword match is unrelated.

B and C are equally important background categories. B papers supply the event-camera side of the survey; C papers supply the SNN side.

## Conference-Level Searches

Each venue/year should receive its own directory under `01-papers-by-conference/`, for example:

```text
01-papers-by-conference/CVPR-2025/
|-- mother-list.csv
|-- candidates.csv
|-- abc-reviewed.csv
|-- conference-report.md
`-- cards/
```

The mother list should come from the official proceedings whenever possible. External sources such as OpenAlex, Semantic Scholar, arXiv, project pages, or search engines may be used for cross-checking, but they are not the primary source of truth.

## Paper Cards

Paper cards are generated from `abc-reviewed.csv` after candidate classification.

A-level cards use `04-templates/paper-card-A.md` and should contain detailed notes suitable for survey writing. B/C cards use `04-templates/paper-card-BC.md` and should stay short unless a deeper read is requested.

Generated cards must contain actual paper-specific summaries. Template headings alone are not acceptable final card content. Automated summaries are draft notes and require human verification before being cited in survey prose.

## Global Index Updates

The global CSV index is `00-index/all-papers.csv`. It intentionally stays compact and stable:

```text
id,title,authors,conference,year,level,category,pdf_link,official_page,card_path,notes
```

Do not add citation count, dataset, task, or code fields unless those values are already obvious and easy to extract. Detailed metadata belongs in paper cards or topic notes.

The Markdown level indexes in `00-index/` should be regenerated from `all-papers.csv` by `scripts/update_index.py` after new conference folders are reviewed.

## Automation Limits

Automated literature search is useful for coverage and consistency, but it has limits:

- venue websites differ in format and may change without notice;
- keyword retrieval misses papers that use unusual terminology;
- keyword retrieval can include false positives;
- abstracts may not reveal whether a method truly uses event-camera data or SNN computation;
- generated summaries can be incomplete or wrong;
- official records may omit late updates, workshops, withdrawn papers, or corrected PDFs.

The working principle is simple: **official proceedings are the primary source of truth**, and **automated summaries are draft notes that require human verification**.

## Typical Workflow

1. Create a venue/year folder under `01-papers-by-conference/`.
2. Run `scripts/conference_scraper.py` to save `mother-list.csv` from the official source.
3. Run `scripts/classify_candidates.py` to produce `candidates.csv` and `abc-reviewed.csv`.
4. Manually review classifications, especially A/B/C boundaries.
5. Run `scripts/generate_card.py` to create paper cards.
6. Run `scripts/update_index.py` to refresh `00-index/`.
7. Commit changes with `scripts/github_sync.py` or normal Git commands.

## GitHub Sync

This repository is designed for a normal Git-over-SSH remote. GitHub CLI is not required and should not be used by this workflow.

To add a remote later:

```bash
git remote add origin git@github.com:USERNAME/snn-event-camera-review.git
git push -u origin main
```
