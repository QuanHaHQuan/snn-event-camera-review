# Repository Generators

Only three maintained generators belong to the active workflow:

1. `python3 scripts/update_index.py`
   - reads each venue's retained `abc-reviewed.csv`;
   - generates `00-index/retained-papers.csv` and `00-index/conferences.md`.
2. `python3 scripts/update_selection.py`
   - treats `00-index/candidate-screening-audit.csv` as the only editable semantic source;
   - validates complete current-candidate title/abstract coverage and SHA256 values;
   - generates `paper-selection.csv`, both reading plans, the Survey reference pool, and venue search reports.
3. `python3 scripts/update_v2_indexes.py`
   - scans canonical V2 files in `06-reading-summaries/v2/papers/`;
   - generates the shared, Survey, and Advisor V2 indexes.

The scripts do not download proceedings, classify papers automatically, commit, or push. Venue ingestion remains an explicit official-source audit because proceedings formats and boundary cases differ.

Reusable prompts for adding a new official venue/year are documented in:

- `docs/proceedings-intake-agent-prompt.md`: official mother list, high-recall title/abstract retrieval, provenance, and handoff evidence;
- `docs/proceedings-semantic-integration-prompt.md`: command-window dual-track screening, Core decisions, generation, and validation.

## Taxonomy Census Validation

`python3 scripts/validate_taxonomy_census.py` validates the separate lightweight taxonomy census, its exact join to the 572-paper source, and its fixed ten-batch manifest. Use `--show-batch B001` for a title/abstract-only JSONL view that omits prior Survey/Advisor decisions, `--require-batch B001` at a batch handoff, and `--require-all` at census completion. This validator does not classify papers, read PDFs, or run the 59-field codebook validator.

## Literature Graph Validation

Run this after generating a V2, relation backfill, or bibliographic normalization:

```bash
python3 scripts/validate_literature_graph.py
```

It validates registry uniqueness, matrix foreign keys and enums, V2-to-matrix titles/relation types/citation markers, and backward-search keys. It cannot determine whether a source PDF semantically supports an edge; that requires the three-gate PDF check in `docs/core-reading-workflow.md`.
