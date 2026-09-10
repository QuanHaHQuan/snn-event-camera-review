# Index Ownership

Editable corpus decision source:

- `candidate-screening-audit.csv`: complete official title/abstract evidence, hashes, dual-track roles, and reading assignments.

Taxonomy discovery layer:

- `taxonomy-census-batches.csv`: fixed 572-paper batch manifest;
- `taxonomy-census.csv`: lightweight title/abstract census joined to the source by `paper_id`.

The census is governed by [`taxonomy-census-protocol.md`](../03-review-draft/taxonomy-census-protocol.md). It does not replace or write back to the corpus decision source.

Generated views:

- `retained-papers.csv`: metadata for retained A/B/C conference-provenance rows;
- `paper-selection.csv`: active dual-track corpus;
- `reading-plan-survey-core.md`;
- `survey-reference-pool.csv`;
- `reading-plan-advisor-core.md`;
- `conferences.md`.

Do not manually synchronize generated files. After editing the audit or adding a fully reviewed venue, run the three commands documented in [`scripts/README.md`](../scripts/README.md).

A/B/C and the paper cards remain in each venue folder only as search provenance. P0/P1/P2/P3 and the former global Level indexes are retired.
