# Advisor / Survey Boundary Cleanup

Date: 2026-08-20

## Reason

Earlier Advisor V2 work used the shared literature-relation backfill workflow. This created Survey-style edges for papers whose only role was Advisor or historical SECNet context. The reading workflow was changed so Advisor reading no longer changes Survey taxonomy, outline, registry, matrix, or evidence matrix.

## Cleanup

- Removed 12 matrix edges whose source track was `advisor_core`.
- Removed 8 registry nodes that were introduced only by those Advisor edges.
- Kept Advisor V2 files and the Advisor V2 index.
- Kept TTPOINT, PointNet++, and related nodes when they remained targets of valid Survey edges, especially the SpikePoint relation.
- Kept `survey_advisor_core` edges for papers that are genuinely Survey Core sources; these are Survey evidence, not Advisor-only relations.
- No changes were required in `03-review-draft/outline.md` or the taxonomy audit.

## Validation

```text
literature_graph_ok registry=80 matrix=69 v2_edges=69 backward_search=19
```

The validator now checks V2 relation bullets only for papers that occur as sources in the relation matrix. A V2 file that is only a related-paper target, such as a historical reference, does not need to invent its own relation edge.
