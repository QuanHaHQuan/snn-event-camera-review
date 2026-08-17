# SNN Event Camera Review

This repository maintains one auditable proceedings corpus for two bounded goals:

1. a survey on **Spiking Neural Networks for Event Cameras**;
2. the **SECNet (ICML 2026 oral) to TPAMI extension** direction: Event Camera + frequency/Fourier + SNN.

The survey and Advisor tracks share evidence but have separate roles and reading plans. Mamba/SSM is not an Advisor direction. A/B/C survives only inside venue folders as search provenance; P0/P1/P2/P3 is retired.

## Start Here

- [`candidate-screening-audit.csv`](00-index/candidate-screening-audit.csv): the only editable semantic/evidence source;
- [`paper-selection.csv`](00-index/paper-selection.csv): generated active corpus;
- [`Survey Core`](00-index/reading-plan-survey-core.md): human-guided deep-reading plan;
- [`Survey reference pool`](00-index/survey-reference-pool.csv): non-Core retrieval pool for later section-level screening;
- [`Advisor Core`](00-index/reading-plan-advisor-core.md): bounded SECNet/Fourier/SNN knowledge chain;
- [`Survey outline`](03-review-draft/outline.md) and [`Advisor reading map`](03-review-draft/advisor-frequency-reading-map.md);
- [`V2 index`](06-reading-summaries/v2/index.md), with separate [Survey](06-reading-summaries/v2/survey/index.md) and [Advisor](06-reading-summaries/v2/advisor/index.md) views.

`paper-selection.csv`, reading plans, reference pool, search reports, and V2 indexes are generated views. Do not edit them by hand.

## Evidence Model

Every high-recall title candidate must have one row in `candidate-screening-audit.csv` containing its complete official abstract, SHA256, dual-track roles, reading assignment, and decision reasons. Title keywords retrieve candidates; they never establish relevance.

Survey roles:

- `anchor`: direct SNN-event integration central to the survey;
- `included`: genuine but narrower intersection evidence;
- `background`: indispensable event-only or SNN-only foundation/comparator;
- `exclude`: no useful role in the strict survey.

Advisor roles:

- `method_chain`: direct SECNet predecessor or closest mechanism chain;
- `discussion`: concrete comparator or extension mechanism;
- `watch`: adjacent evidence worth retaining;
- `exclude`: no useful relation to Event Cloud + Fourier/FFT + SNN.

`reading_status` is the actual assignment. Only papers excluded from both tracks leave the active corpus; complete mother lists and the audit evidence remain preserved.

Important boundaries:

- DVS benchmark-only generic SNN work is background, not direct intersection evidence;
- event-camera-only work is not automatically Survey Core;
- spike cameras, event logs, temporal point processes, biological spikes, and generic asynchronous systems are outside scope unless the official abstract independently establishes a target-axis contribution;
- NeurIPS may include all official long-paper tracks, but each paper must retain its track and non-main-track Core enrollment faces a higher bar.

## Conference Intake

Allowed venues are CVPR, ICCV, ECCV, NeurIPS, ICML, and ICLR only. Add papers only as a complete official venue/year proceedings unit.

For each venue:

1. preserve the complete official `mother-list.csv`;
2. create a high-recall `candidates.csv`;
3. inspect the complete official title and abstract for every candidate;
4. retain A/B/C search provenance and cards for in-scope papers;
5. record every retained or excluded candidate in `candidate-screening-audit.csv`;
6. run the generators below and inspect their output before committing.

See [`docs/workflow-instructions.md`](docs/workflow-instructions.md) for the full contract.

## Generators

```bash
python3 scripts/update_index.py
python3 scripts/update_selection.py
python3 scripts/update_v2_indexes.py
```

The maintained scripts are documented in [`scripts/README.md`](scripts/README.md). They never classify papers automatically, download proceedings, commit, or push.

## Repository Layout

```text
00-index/                  Audit source and generated dual-track indexes
01-papers-by-conference/   Official mother lists, retrieval provenance, cards
03-review-draft/           Survey outline, checkpoints, Advisor reading map
04-templates/              Conference screening templates
05-logs/                   Immutable historical audit logs
06-core-reading-summaries/ Historical automated V1 summaries; not workflow input
06-reading-summaries/v2/  Canonical human-guided V2 files and generated views
docs/                      Selection and deep-reading workflow contracts
scripts/                   Three maintained deterministic generators
work/                      Ignored local scratch/cache; never repository input
```

Downloaded PDFs and parser caches remain local. Never force-push or push before the current changes have been reported and explicitly confirmed.
