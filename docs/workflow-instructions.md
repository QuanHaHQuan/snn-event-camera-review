# Dual-Track Literature Workflow

## Scope

This repository serves two goals only:

1. a review of **SNN for Event Cameras**, focused on the actual intersection;
2. the **SECNet ICML 2026 oral to TPAMI extension** method direction.

Do not expand the survey into generic event-based vision, generic SNNs, broad neuromorphic computing, asynchronous systems, event logs, temporal point processes, biological spike sorting, or spike-camera imaging.

## Proceedings Intake

- Use official proceedings, accepted-paper lists, CVF, PMLR, OpenReview, or NeurIPS Proceedings.
- Process exactly one specified venue/year/scope.
- Exclude workshops, demos, challenges, tutorials, and invited talks unless explicitly requested.
- Preserve the complete official main list as `mother-list.csv` before filtering.
- NeurIPS alone may include all official long-paper tracks. Preserve its track label; non-main-track papers require stronger evidence for core roles.
- Future papers are added only when a complete official proceedings is available and the venue is processed as a unit.

## Search Stage

The conference A/B/C files are search provenance, not the active review taxonomy.

1. Run high-recall title retrieval.
2. Inspect the complete official abstract/page for every candidate.
3. Do not search every PDF in the mother list.
4. Generate `candidates.csv`, `abc-reviewed.csv`, paper cards, and a search report.
5. Run `python3 scripts/update_index.py`.

Title matches never constitute semantic evidence. A generic SNN paper using a DVS-family dataset only as a benchmark is not direct SNN-event integration.

## Active Dual-Track Selection

The active source of truth is `00-index/paper-selection.csv`.

Survey roles:

- `anchor`: direct SNN-event integration central to the survey narrative;
- `included`: genuine but narrower intersection evidence;
- `background`: indispensable event-only or SNN-only foundation/comparator;
- `exclude`: no useful strict-survey role.

Advisor roles:

- `method_chain`: direct SECNet predecessor or closest method chain;
- `discussion`: concrete extension mechanism, task, dataset, or comparator;
- `watch`: adjacent inspiration with weaker evidence;
- `exclude`: no useful advisor relation.

Delete a paper from the active corpus only when both roles are `exclude`. Preserve every `mother-list.csv`. Record every removal in the dual-exclude audit.

## Semantic Decision Standard

Each decision must be based on the complete title and abstract. No regex, keyword count, title-only rule, legacy A/B/C label, or old P0-P3 priority may generate the role.

Record:

```text
paper_id,title,year,venue,
survey_role,survey_topics,survey_reason,
advisor_role,advisor_topics,advisor_reason,
reading_status,evidence_source,needs_pdf_check
```

Use `needs_pdf_check=yes` only when the abstract cannot resolve a material boundary. Such a paper cannot enter survey core until checked.

## Survey Core

`00-index/reading-plan-survey-core.md` supports:

- events-to-spikes and direct SNN input;
- slicing, voxel, point/Event Cloud and spike relationships;
- fully spiking, hybrid ANN-SNN, and conversion designs;
- temporal state, memory, and long-context processing;
- SNN training for event streams;
- recognition, detection, tracking, reconstruction, pose, depth, flow, and segmentation;
- latency, energy, and hardware evidence;
- datasets, robustness, limitations, and open problems.

All `anchor` papers enter unless unresolved. Add `included` or `background` papers only when they fill a non-redundant argument or evidence gap. Do not impose a fixed quota per topic.

## Advisor Core

`00-index/reading-plan-advisor-core.md` supports SECNet's Event Cloud, point processing, grouping/sampling, polarity, frequency, SSM/Mamba memory, scalability, hardware, and task/domain generalization. Core enrollment is a separate, stricter decision than advisor-role labeling. Recency is a tiebreaker, not a substitute for relevance.

The active advisor reading assignment is intentionally narrower than the advisor-role candidate pool:

- `advisor_required`: necessary knowledge for understanding SECNet and the known extension direction;
- `advisor_helpful`: a small set of papers that may provide directly usable mechanisms or comparisons.

`method_chain`, `discussion`, and `watch` remain searchable semantic labels. They do not mean that every matching paper must be read. Do not automatically place every `method_chain` paper into Advisor Core.

## Generation

Run:

```bash
python3 scripts/update_selection.py
```

This validates decision coverage and vocabulary, then regenerates:

- `00-index/paper-selection.csv`;
- `00-index/reading-plan-survey-core.md`;
- `00-index/reading-plan-advisor-core.md`;
- deprecated redirects for the old Core/P0/P1/P2/advisor files;
- the dual-exclude audit.

`scripts/update_reading_plan.py` is now only a compatibility wrapper. `00-index/reading-plan-overrides.yaml` is archived and must not be maintained.

## Reporting And Git

After each venue or reselection run, report:

- mother-list and candidate counts;
- active and dual-excluded counts;
- role distributions for both tracks;
- survey/advisor core totals;
- unresolved PDF checks;
- files changed and Git status.

Do not use GitHub CLI, force-push, overwrite user changes, or push before explicit confirmation.
