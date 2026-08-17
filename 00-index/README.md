# Index Ownership

Editable corpus decision source:

- `candidate-screening-audit.csv`: complete official title/abstract evidence, hashes, dual-track roles, and reading assignments.

Generated views:

- `retained-papers.csv`: metadata for retained A/B/C conference-provenance rows;
- `paper-selection.csv`: active dual-track corpus;
- `reading-plan-survey-core.md`;
- `survey-reference-pool.csv`;
- `reading-plan-advisor-core.md`;
- `conferences.md`.

Do not manually synchronize generated files. After editing the audit or adding a fully reviewed venue, run the three commands documented in [`scripts/README.md`](../scripts/README.md).

A/B/C and the paper cards remain in each venue folder only as search provenance. P0/P1/P2/P3 and the former global Level indexes are retired.
