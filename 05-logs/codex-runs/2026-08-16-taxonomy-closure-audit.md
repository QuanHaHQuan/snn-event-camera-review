# 2026-08-16 Taxonomy Closure Audit

## Goal

Use five recent external surveys to test whether the Survey taxonomy can recall all relevant event-camera, SNN, and intersection branches. `Spiking Transformer` was treated as a diagnostic example, not a privileged target.

## Inputs

- five local survey PDFs listed with SHA256 in `03-review-draft/taxonomy-closure-audit.md`;
- 572 complete official title-and-abstract audit rows in `00-index/candidate-screening-audit.csv`;
- the 25-paper pre-audit Survey Core and 13 available Core V2 summaries;
- the current outline and literature relation graph.

## Outputs

- `03-review-draft/taxonomy-closure-audit.md`;
- `03-review-draft/classic-literature-candidates.csv`;
- `03-review-draft/taxonomy-closure-corpus-rescreen.csv`;
- a minimal structure update to `03-review-draft/outline.md`;
- regenerated Survey reading plan, selection table, reference pool and V2 indexes.

## Findings

1. The current taxonomy already contains the correct high-level parallel axes and intersection topology.
2. The outline under-specified architecture families and treated dense/sparse too much like a complete representation tree.
3. Spiking Transformer is represented by HsVT, SDTrack and STEP, but its classic lineage needs pre-2024 backfill.
4. Other thin classic branches include time surfaces, EST/Matrix-LSTM, graph representations, residual SNNs, spike coding, and early event-SNN optical flow/reconstruction/tracking.
5. These are primarily classic-literature gaps. Generic recent SNN papers that merely use DVS benchmarks remain reference-only.

## Core change

Promoted one current-proceedings paper from reference to selected background:

- *Graph Neural Network Combining Event Stream and Periodic Aggregation for Low-Latency Event-based Vision* (CVPR 2025).

Reason: it directly compares asynchronous per-event graph processing and periodic aggregation, reports event-level latency and asynchronous-hardware evidence, and fills the event-side graph/execution comparator gap. It is explicitly labeled non-spiking.

Survey Core changes from 25 to 26 papers: 15 anchor, 2 included, 9 selected background. Current V2 progress is 13/26. The added paper is background, so the user's parallel anchor-reading sequence is unchanged.

## Validation

```text
python3 scripts/update_selection.py
audited=572 active=298 survey_core=26 survey_reference_pool=259 advisor_required=8 advisor_helpful=4 advisor_core=12 excluded=274

python3 scripts/update_index.py
Updated retained-paper metadata with 298 A/B/C provenance rows.

python3 scripts/update_v2_indexes.py
v2=20 survey=13/26 advisor=3/14 external_or_archived=3

python3 scripts/validate_literature_graph.py
literature_graph_ok registry=71 matrix=63 v2_edges=63 backward_search=19
```

No downloaded survey PDF or extracted PDF text is intended for Git.
