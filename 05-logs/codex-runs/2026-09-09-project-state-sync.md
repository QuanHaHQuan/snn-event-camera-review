# Project State Synchronization

Date: 2026-09-09

## Reason

The repository contained two kinds of status drift:

- the SECNet V2 used the canonical paper title, while the external Advisor-focus rows appended `(SECNet)`, so exact normalized-title matching incorrectly reported the existing V2 as missing;
- the Survey outline, taxonomy-closure audit, and reading roadmap repeated the historical `13/26` progress value after the generated Survey index had advanced to `16/26`.

## Changes

- Standardized the SECNet external-focus title as `Scalable Event Cloud Network for Event-based Classification` in both maintained generators.
- Regenerated the Advisor reading plan and all V2 indexes. SECNet is now recognized as the Advisor focus paper, and the Advisor progress is `7/9` rather than `6/9`.
- Removed duplicated live progress counters from durable planning documents. They now link to the generated Survey V2 index as the live source; historical `13/26` references are explicitly labeled as snapshots or roadmap provenance.
- Preserved historical Codex run logs and Checkpoint 01 without rewriting their time-specific counts.

## Current Generated State

```text
audited=572 active=298 survey_core=26 survey_reference_pool=259
advisor_required=5 advisor_helpful=3 advisor_core=8 excluded=274
v2=29 survey=16/26 advisor=7/9 external_or_archived=4
```

## Validation

```text
literature_graph_ok registry=84 matrix=72 v2_edges=72 backward_search=19
git diff --check: passed
```
