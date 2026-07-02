# Codex Run Log: Initial Workflow and Strict Rescan

Date: 2026-07-02

Project: SNN Event Camera Review

Local repository:
`/Users/haoquanchen/Documents/Codex/2026-07-01/i-want-to-build-a-reusable/snn-event-camera-review`

Remote:
`git@github.com:QuanHaHQuan/snn-event-camera-review.git`

## Purpose

This repository supports a GitHub-backed literature review workflow for the survey topic:

**Spiking Neural Networks for Event Cameras**

The repository stores official venue mother lists, title-screened candidates, strict A/B/C/D/E classifications, generated paper cards, global indexes, topic notes, and future survey drafts.

## Current Workflow Rule

Use the strict two-stage screening workflow documented in:

- `README.md`
- `docs/workflow-instructions.md`

The core rule is:

1. Stage 1 uses a broad, high-recall title keyword pool.
2. Stage 2 inspects the official abstract or official paper page for every title hit.
3. A/B/C promotion requires strict official evidence.

Title keywords are retrieval triggers only. They are not classification evidence.

Event-camera evidence requires explicit event cameras, DVS, visual event sensors, address-event representation, asynchronous brightness-change sensing, event-camera datasets, or clearly visual event-stream tasks such as RGB-Event/frame-event/image-event fusion, event-to-video reconstruction, event-based deblurring, event-based stereo, event-based optical flow, event-based object detection, or event-based action recognition.

Generic event sequences, event logs, event-triggered control, time-to-event data, temporal point processes, audio-visual event parsing, ordinary asynchronous algorithms, biological spikes, spike sorting, spike cameras, and generic neuromorphic language are not sufficient for A/B/C evidence by themselves.

SNN evidence requires explicit SNNs, spiking neural networks, spiking neurons, LIF/IF models, ANN-to-SNN conversion, surrogate gradients, spiking transformers, or comparable spike-based neural computation.

## Classification Meaning

- A: Explicit intersection of event-camera/DVS/visual-event data and SNN/spiking neural computation.
- B: Event-camera-side paper without clear SNN evidence.
- C: SNN-side paper without clear event-camera evidence.
- D: Adjacent/background or ambiguous paper.
- E: False positive.

B and C are equally important background categories.

## Processed Venues

The following venue/year folders have been processed and then strict-rescanned:

- `CVPR2026`
- `ICCV2025`
- `ECCV2024`
- `NeurIPS2025`
- `ICML2025`

Each folder contains:

- `mother-list.csv`
- `candidates.csv`
- `abc-reviewed.csv`
- `search-report.md`
- generated A/B/C paper cards

## Current Global Counts

After the strict two-stage rescan:

| Venue | A | B | C | Total |
| --- | ---: | ---: | ---: | ---: |
| CVPR 2026 | 4 | 44 | 11 | 59 |
| ECCV 2024 | 6 | 28 | 4 | 38 |
| ICCV 2025 | 2 | 34 | 2 | 38 |
| ICML 2025 | 4 | 3 | 14 | 21 |
| NeurIPS 2025 | 5 | 17 | 20 | 42 |
| **Total** | **21** | **126** | **51** | **198** |

The global index is:

`00-index/all-papers.csv`

## Important Commits

- `cac1c2d Apply strict two-stage screening audit to processed venues`
- `ec1f42a Add ICML 2025 literature search results`
- `db45c85 Add NeurIPS 2025 literature search results`

## Notes for Future Codex Chats

When starting a new Codex chat for this project, use the local repository as the project folder and ask Codex to read the repository files before acting.

Recommended opening prompt:

```text
This is the `snn-event-camera-review` project.

Please use the current repository as the source of truth. Before making changes, run `git status` and read:

- README.md
- docs/workflow-instructions.md
- 05-logs/codex-runs/2026-07-02-initial-workflow-and-strict-rescan.md

Then continue the requested task while following the strict two-stage screening workflow.
```

For a new conference-processing task, add:

```text
Process [VENUE YEAR] using the official proceedings URL: [URL].
Use broad title screening first, inspect official abstracts/pages for every title hit, and promote only strictly confirmed A/B/C papers.
Do not perform full-PDF search over all papers.
Do not use GitHub CLI.
Commit and push through Git over SSH after verification.
```

## Maintenance Principle

Future chats should not rely on memory from any previous chat. They should rely on repository files, Git history, and this run log.

