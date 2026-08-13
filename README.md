# SNN Event Camera Review

This repository maintains an auditable conference-paper corpus for two related goals:

1. a strict survey on **Spiking Neural Networks for Event Cameras**;
2. the advisor direction **SECNet (ICML 2026 oral) to a future TPAMI extension**.

The two goals share one proceedings corpus but have separate semantic roles and reading plans. The retired A/B/C and P0-P3 labels remain only as conference-screening provenance; they no longer determine active selection or reading priority.

## Active Indexes

- `00-index/paper-selection.csv`: active dual-track paper index and source of truth;
- `00-index/reading-plan-survey-core.md`: focused survey reading plan;
- `00-index/survey-reference-pool.csv`: survey-relevant non-Core papers for automated summaries and section-level retrieval;
- `00-index/reading-plan-advisor-core.md`: SECNet/advisor method-chain reading plan;
- `00-index/core-screening-audit.csv`: 351-paper title/abstract evidence and both Core decisions;
- `05-logs/codex-runs/2026-08-12-dual-exclude-audit.md`: current audit of papers removed from both tracks;
- `00-index/all-papers.csv`: retained conference metadata, not a reading-priority index.

## Selection Roles

Survey roles:

- `anchor`: direct SNN-event integration central to the survey;
- `included`: genuine intersection evidence with a narrower or supporting role;
- `background`: event-only or SNN-only work needed for comparison or foundations;
- `exclude`: no useful role in the strict survey.

Advisor roles:

- `method_chain`: direct SECNet predecessor or closest representation/architecture chain;
- `discussion`: concrete comparator or TPAMI extension idea;
- `watch`: adjacent work worth monitoring;
- `exclude`: no useful relation to the advisor direction.

Only papers with `survey_role=exclude` and `advisor_role=exclude` are removed from the active corpus. Complete venue `mother-list.csv` files are always preserved.

`reading_status` is the actual reading assignment. Advisor Core is split into `advisor_required` and `advisor_helpful`; the broader `method_chain`, `discussion`, and `watch` roles are searchable corpus labels, not instructions to read every paper carrying that label.

## Evidence Rule

Every semantic decision must inspect the complete official title and abstract. Title keywords are retrieval triggers only. Regex or keyword scripts must not assign survey/advisor roles. PDF review is reserved for genuine abstract-level boundary cases and is recorded in `needs_pdf_check`. The 2026-08-12 Core audit records all 351 title/abstract decisions, abstract hashes, and PDF boundary findings in `00-index/core-screening-audit.csv`.

Important boundaries:

- a generic SNN paper using CIFAR10-DVS, N-MNIST, DVS-Gesture, or N-Caltech101 only as a benchmark is SNN-side background, not direct intersection work;
- an event-camera-only paper is not automatically survey core;
- `event-driven`, generic asynchronous systems, spike cameras, biological spike processing, and event logs do not automatically qualify;
- advisor relevance must be tied to SECNet's Event Cloud lineage or the confirmed Event Camera + frequency/Fourier + SNN extension direction;
- Mamba/SSM is outside the confirmed Advisor extension and is not an Advisor taxonomy topic. A directly relevant hybrid such as FLAME may still support the Survey boundary analysis; that does not make it Advisor reading.

## Conference Workflow

The conference allowlist is limited to CVPR, ICCV, ECCV, NeurIPS, ICML, and ICLR. Do not add AAAI, IJCAI, ACM MM, or another venue unless the user explicitly changes this scope.

1. Process one official venue/year proceedings at a time.
2. Preserve the complete official `mother-list.csv`.
3. Retrieve title candidates with high recall.
4. Verify candidates using official pages and complete abstracts.
5. Generate `candidates.csv`, `abc-reviewed.csv`, cards, and the conference report as search provenance.
6. Run `python3 scripts/update_index.py`.
7. Record the complete title, official abstract, abstract hash, dual-track decision, and reason in `00-index/core-screening-audit.csv`. Local `work/` files may stage the review but are not repository inputs.
8. Update `00-index/paper-selection.csv`, then run `python3 scripts/update_selection.py`; the generator rejects drift from the committed audit evidence.
9. Inspect both reading plans, the PDF-check queue, and Git status.
10. Report before any push. Never force-push.

NeurIPS is the only venue where all official long-paper tracks are admitted into the mother list. Non-main-track papers must retain track metadata and face a higher bar for survey `anchor` or advisor `method_chain` status.

## Repository Layout

```text
00-index/                  Active selection and generated reading plans
01-papers-by-conference/   Official venue snapshots, screening CSVs, and cards
02-topic-notes/            Cross-paper notes
03-review-draft/           Survey outline and manuscript drafts
04-templates/              Search/card templates
05-logs/                   Search and reselection audits
06-core-reading-summaries/ Existing automated V1 artifacts and V2 redirect
06-reading-summaries/v2/  Canonical V2 papers plus Survey/Advisor views
docs/                      Formal workflow instructions
scripts/                   Deterministic index generation
work/                      Local scratch data; not required by committed generators
```

Downloaded PDFs and temporary parser outputs must remain local and must not be committed.

## V2 Reading Notes

Every human-guided V2 summary has one canonical file in `06-reading-summaries/v2/papers/`.
Do not copy a V2 when one paper belongs to both tracks. Maintain the two reading views instead:

- `06-reading-summaries/v2/survey/index.md`: Survey Core progress and survey-specific purpose;
- `06-reading-summaries/v2/advisor/index.md`: Advisor Core progress and advisor-specific purpose;
- `06-reading-summaries/v2/index.md`: all canonical V2 files, including retained historical reading results.

After adding or renaming a V2 file, run `python3 scripts/update_v2_indexes.py`.
