# Workflow Simplification Audit

Date: 2026-08-13

## Objective

Reduce repository complexity without changing the bounded Survey and Advisor goals, and make complete official-title/abstract evidence the single semantic source.

## Structural Changes

- `00-index/candidate-screening-audit.csv` is now the only editable semantic/evidence table.
- `paper-selection.csv`, both reading plans, the Survey reference pool, venue search reports, and V2 indexes are generated views.
- `all-papers.csv` was renamed to `retained-papers.csv` to state that it is not a proceedings mother list.
- Retired P0/P1/P2/P3 files, global Level A/B/C Markdown indexes, the old advisor redirect files, the override YAML, placeholder topic/manuscript files, and their compatibility generator were removed.
- Unsafe or obsolete generic automation scripts for keyword classification, shallow card generation, generic scraping, and `git add -A` syncing were removed.
- The Core deep-reading protocol moved from the repository root to `docs/core-reading-workflow.md`.
- Historical automated V1 summaries were retained but explicitly marked as non-input artifacts.
- `work/` is ignored and remains local scratch/cache.

## Candidate/Audit Reconciliation

The old workflow had 473 current candidate IDs but only 418 audit rows. It also contained 99 historical audited exclusions that had been removed from venue candidate files.

The reconciliation restored the original high-recall candidate records, fetched or reused the complete official abstract for every missing candidate, and reviewed all boundary cases. The final sets are exact:

- high-recall candidates: 572;
- complete official-title/abstract audit rows: 572;
- missing candidate audits: 0;
- stale audit rows outside the candidate set: 0;
- retained A/B/C provenance and active corpus: 298;
- dual-track exclusions: 274.

Eleven event-camera papers had been incorrectly discarded by the old D/E boundary workflow and were restored as Survey background references: `CVPR2024-0885`, `CVPR2026-0806`, `CVPR2026-2758`, `CVPR2026-3325`, `CVPR2026-3467`, `ECCV2024-1397`, `ECCV2024-1943`, `ICCV2025-2426`, `ICML2024-1996`, `NeurIPS2025-0321`, and `NeurIPS2025-2457`.

No restored paper entered Survey Core or Advisor Core automatically.

## Current Reading Outputs

- Survey Core: 25 papers;
- Survey reference pool: 260 papers;
- Advisor Core: 12 proceedings papers (`8 required + 4 helpful`);
- complete Advisor knowledge chain: 14 papers after SECNet and TTPOINT;
- V2 progress: Survey `10/25`, Advisor `3/14`;
- unresolved `needs_pdf_check=yes`: 0.

## Maintained Commands

```bash
python3 scripts/update_index.py
python3 scripts/update_selection.py
python3 scripts/update_v2_indexes.py
```

The generators validate candidate/audit coverage, abstract hashes, NeurIPS tracks, controlled vocabularies, the active partition, retained card existence, and V2 progress. They do not classify papers, download proceedings, commit, or push.
