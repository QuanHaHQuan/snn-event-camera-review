# SNN Event Camera Review

This repository stores a systematic, venue-specific literature review workflow for the survey topic **Spiking Neural Networks for Event Cameras**.

The purpose is to keep literature search results reproducible and auditable: each conference search should preserve the official paper list, candidate retrieval logic, classification decisions, generated paper cards, human review notes, and global indexes used for future survey drafting.

For the full shareable initialization and conference-processing prompt, see `docs/workflow-instructions.md`.

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

The project scope is deliberately narrow:

- SNN / Spiking Neural Networks;
- Event Camera / DVS / visual event streams;
- the intersection: SNN for Event Cameras.

The repository should not become a broad review of generic event-based systems, event logs, event-triggered control, temporal point processes, general asynchronous systems, biological spike sorting, or broad neuromorphic computing without clear SNN or event-camera evidence.

**A = Intersection / core paper**

Explicitly combines SNN/spiking neural computation with event cameras, DVS, visual event sensors, visual event streams, or event-camera datasets/data. Broad labels such as event-based vision or neuromorphic vision count only when the official abstract/page explicitly confirms event-camera/DVS/visual-event-stream data.

**B = Event-camera-side paper**

Clearly about event cameras, DVS, dynamic vision sensors, visual event streams, event-camera datasets, or event-camera tasks, but does not clearly use SNN/spiking neural networks.

**C = SNN-side paper**

Clearly about SNNs, spiking neural networks, spiking transformers, ANN-to-SNN conversion, surrogate gradients, spike trains, LIF/IF neurons, or SNN training/inference, but does not clearly involve event cameras/DVS/event-camera data.

**D = Adjacent/background paper**

Related to asynchronous processing, temporal sparsity, event-driven computation, low-latency vision, neuromorphic ideas, spike cameras, or broad event-based vision, but not clearly about event cameras/DVS/visual-event-stream data or SNNs.

**E = False positive**

Keyword match is unrelated.

B and C are equally important background categories. B papers supply the event-camera side of the survey; C papers supply the SNN side.

For the reading-plan layer, `refined_level` uses a smaller A/B/C/X scheme:

- `A`: true SNN x Event Camera core papers. Generic SNN papers that only report DVS-family benchmarks are not A.
- `B`: event-camera background papers.
- `C`: SNN background papers.
- `X`: out of scope or false positive for the current focus.

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

Candidate retrieval uses one broad, high-recall title keyword pool. The pool includes precise terms such as `event camera`, `DVS`, `event stream`, `spiking neural network`, and `SNN`, plus broad recall terms such as `event`, `event-based`, `spike`, and `spiking`.

All title-retrieved candidates require official abstract or official-page inspection before A/B/C promotion. Title keywords are retrieval triggers, not classification evidence. A paper can be classified as A/B/C only after its abstract or official page explicitly confirms event-camera/DVS/visual-event-sensor data or SNN/spiking neural computation.

The second stage is intentionally strict. `event stream`, `event data`, and `event-based vision` count as event-camera evidence only when the official abstract/page ties them to event cameras, DVS, visual event sensors, address-event representation, asynchronous brightness-change sensing, an event-camera dataset, or a clearly visual event-stream task such as RGB-Event/frame-event/image-event fusion, event-to-video reconstruction, event-based deblurring, event-based stereo, event-based optical flow, event-based object detection, or event-based action recognition. Generic event sequences, event logs, event-triggered control, time-to-event data, or temporal point processes do not count. Likewise, `spike` and `spiking` count as SNN evidence only when they refer to spiking neural networks, spiking neurons, LIF/IF models, ANN-to-SNN conversion, surrogate gradients, spiking transformers, or comparable spike-based neural computation. Biological spikes, spike sorting, spike cameras, and generic neuromorphic language are not enough by themselves.

Otherwise the paper should be marked D or E, or listed as an unpromoted title-candidate finding in the report.

## Paper Cards

Paper cards are generated from `abc-reviewed.csv` after candidate classification.

A-level cards use `04-templates/paper-card-A.md` and should contain detailed notes suitable for survey writing. B/C cards use `04-templates/paper-card-BC.md` and keep the same four visible sections: Core Problem, Core Method, Key Metrics and Findings, and Personal Notes.

B/C cards are intentionally shorter than A cards, but they are not placeholder-only notes. They should still contain paper-specific text in each section and remain ready for later review or expansion.

Generated cards must contain actual paper-specific summaries. Template headings alone are not acceptable final card content. Automated summaries are draft notes and require human verification before being cited in survey prose.

## Global Index Updates

The global CSV index is `00-index/all-papers.csv`. It keeps the original stable metadata fields and a lightweight reading-plan layer:

```text
id,title,authors,conference,year,level,category,pdf_link,official_page,card_path,notes,refined_level,priority,advisor_track,reason,evidence_source,uncertain
```

Do not add citation count, dataset, task, or code fields unless those values are already obvious and easy to extract. Detailed metadata belongs in paper cards or topic notes.

The Markdown level indexes in `00-index/` should be regenerated from `all-papers.csv` by `scripts/update_index.py` after new conference folders are reviewed.

The reading-plan files are generated by:

```bash
python3 scripts/update_reading_plan.py
```

This step does not replace venue search or A/B/C indexing. It only adds reading priorities:

- `P0`: 精读;
- `P1`: optional reading;
- `P2`: automatic-summary queue;
- `P3`: retained but not active now.

Before enrollment, the main reading file is `00-index/reading-plan-core.md`, defined as `unique(P0 papers + advisor_track papers)`. The target is roughly 60 papers; if the current repository and SECNet references produce fewer than 60 strong candidates, do not pad the list with weakly related papers.

`advisor_track` is only for understanding the uploaded SECNet / ICML 2026 method chain. It is built from current corpus papers plus selected SECNet references and does not encode future TPAMI extension ideas.

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
7. Run `scripts/update_reading_plan.py` to refresh the refined reading-plan layer.
8. Commit changes with `scripts/github_sync.py` or normal Git commands.

## GitHub Sync

This repository is designed for a normal Git-over-SSH remote. GitHub CLI is not required and should not be used by this workflow.

To add a remote later:

```bash
git remote add origin git@github.com:USERNAME/snn-event-camera-review.git
git push -u origin main
```
