# Dual-Track Literature Workflow

## Scope

This repository serves two goals only:

1. a review of **SNN for Event Cameras**, focused on the actual intersection;
2. the **SECNet ICML 2026 oral to TPAMI extension** method direction.

Do not expand the survey into generic event-based vision, generic SNNs, broad neuromorphic computing, asynchronous systems, event logs, temporal point processes, biological spike sorting, or spike-camera imaging.

## Proceedings Intake

- The conference allowlist is CVPR, ICCV, ECCV, NeurIPS, ICML, and ICLR only. Do not add AAAI, IJCAI, ACM MM, or another venue unless the user explicitly changes the scope.
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
paper_id,title,year,venue,official_track,
abstract_reviewed,abstract_sha256,abstract,official_page,
survey_role,survey_topics,survey_reason,
advisor_role,advisor_topics,advisor_reason,
survey_core_decision,advisor_core_decision,
reading_status,needs_pdf_check,evidence_basis,
pdf_boundary_check,pdf_boundary_finding
```

Use `needs_pdf_check=yes` only when the abstract cannot resolve a material boundary. Such a paper cannot enter survey core until checked.

For the current corpus, the committed `00-index/core-screening-audit.csv` records the complete title and official abstract, an abstract hash, both Core decisions, and every PDF boundary check for all 351 screened papers. Local files under `work/` may stage semantic review, but they are not the repository evidence source and do not need to be pushed. This audit is the evidence trail for inclusion and omission; it does not imply that an abstract can reveal implementation details absent from the paper.

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

The generated `00-index/survey-reference-pool.csv` contains every survey-relevant paper outside Survey Core. It is an automated-summary and citation-retrieval pool, not a requirement to deep-read every entry. Use PDF-based automated summaries for this pool in batches, and perform table/formula-level verification only for papers that are actually cited or promoted into Survey Core.

### Survey Reading Order

1. Read all 15 `anchor` papers in `reading-plan-survey-core.md` and produce a human-guided Summary V2 for each.
2. Read the remaining 10 Survey Core papers. The two `included` papers should normally receive full Summary V2; the eight selected `background` papers may use a focused V2 that covers only the survey-relevant mechanism, evidence, and limitations.
3. After all 25 Core papers have been read, finalize outline V1.0 and build a Core evidence matrix.
4. Use the final outline to classify and rank the 214 papers in `survey-reference-pool.csv` by section. Allow multiple section assignments and use `essential`, `useful`, and `omit`; do not impose one global ranking.
5. Select roughly 50--80 extended references according to section needs, then generate evidence-traceable structured cards only for the selected papers. Do not generate heavy V1 summaries for all 214 papers.
6. Draft claim by claim from Core V2 evidence and selected reference cards. Verify the official PDF before citing a central numerical or mechanism claim.

The current active-role counts are `anchor=15`, `included=4`, `background=220`, and `exclude=13`. They are corpus statistics, not four reading queues: only 25 papers have `reading_status=survey_core`, and the 214-paper reference pool is a later section-level retrieval pool.

### V2 Storage And Views

Store each human-guided Summary V2 exactly once in:

```text
06-reading-summaries/v2/papers/
```

Do not copy a V2 into separate Survey and Advisor folders when a paper belongs to both tracks. The paper-level understanding is the canonical source; track-specific purpose and progress are represented by generated indexes:

- `06-reading-summaries/v2/survey/index.md`;
- `06-reading-summaries/v2/advisor/index.md`;
- `06-reading-summaries/v2/index.md` for all completed V2 files.

After adding, renaming, or correcting a V2 file, run:

```bash
python3 scripts/update_v2_indexes.py
```

The script matches the official paper title in `paper-selection.csv` against the first level-one heading in each V2 file. It lists missing summaries but never creates or overwrites V2 paper content.

## Advisor Core

`00-index/reading-plan-advisor-core.md` supports SECNet's Event Cloud lineage and the confirmed **Event Camera + frequency/Fourier + SNN** extension direction, with FFT as the primary mechanism to understand. SECNet already contains Spatial-FA and Temporal-FA FFT-filter-iFFT modules, so the task is to understand and extend its existing frequency interface and couple it to SNN computation. Mamba and SSM are outside this extension and are retired from the Advisor taxonomy. Core enrollment is a separate, stricter decision than advisor-role labeling. Recency is a tiebreaker, not a substitute for relevance.

The active advisor reading assignment is intentionally narrower than the advisor-role candidate pool:

- `advisor_required`: necessary knowledge for understanding SECNet and the known extension direction;
- `advisor_helpful`: a small set of papers with a directly usable module or controlled contrast. Read only the mechanism named in the plan when the rest of the architecture is out of scope.

The complete bounded chain is 14 papers: SECNet as the focus paper, TTPOINT as an external predecessor, and 12 current proceedings-corpus assignments (`8 required + 4 helpful`). Only the latter 12 are counted as Advisor Core corpus papers.

`method_chain`, `discussion`, and `watch` remain searchable semantic labels. They do not mean that every matching paper must be read. Do not automatically place every `method_chain` paper into Advisor Core.

## Generation

Run:

```bash
python3 scripts/update_selection.py
```

This validates decision coverage, abstract hashes, NeurIPS track metadata, the active/dual-exclude partition, and vocabulary, then regenerates:

- `00-index/paper-selection.csv`;
- `00-index/reading-plan-survey-core.md`;
- `00-index/survey-reference-pool.csv`;
- `00-index/reading-plan-advisor-core.md`;
- deprecated redirects for the old Core/P0/P1/P2/advisor files;
- the dual-exclude audit.

`scripts/update_reading_plan.py` is now only a compatibility wrapper. `00-index/reading-plan-overrides.yaml` is archived and must not be maintained.

V2 indexes are generated separately with `python3 scripts/update_v2_indexes.py` because reading notes are user-authored artifacts rather than selection outputs.

## Reporting And Git

After each venue or reselection run, report:

- mother-list and candidate counts;
- active and dual-excluded counts;
- role distributions for both tracks;
- survey/advisor core totals;
- unresolved PDF checks;
- files changed and Git status.

Do not use GitHub CLI, force-push, overwrite user changes, or push before explicit confirmation.
