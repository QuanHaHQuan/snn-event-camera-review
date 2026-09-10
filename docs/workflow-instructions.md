# Dual-Track Literature Workflow

## 1. Scope

This repository serves two goals only:

1. **Survey:** the strict intersection `Spiking Neural Networks for Event Cameras`;
2. **Advisor:** SECNet to TPAMI, centered on implementing SECNet as an accurate, trainable, and deployable SNN.

Do not expand into generic event-based vision, generic SNN application catalogues, broad neuromorphic computing, asynchronous systems, event logs, temporal point processes, biological spike processing, or spike-camera imaging. Generic SNN papers may enter the Advisor evidence pool only when they contribute a reusable neuron, architecture, training, temporal, efficiency, or deployment mechanism. Mamba/SSM is outside the planned first implementation.

The venue allowlist is CVPR, ICCV, ECCV, NeurIPS, ICML, and ICLR. Add a venue/year only when complete official proceedings are available and process it as one unit.

## 2. Data Ownership

There is one editable semantic source:

```text
00-index/candidate-screening-audit.csv
```

It records complete official abstract evidence and every Survey/Advisor decision. The following are generated and must not be edited manually:

```text
00-index/retained-papers.csv
00-index/conferences.md
00-index/paper-selection.csv
00-index/reading-plan-survey-core.md
00-index/survey-reference-pool.csv
00-index/reading-plan-advisor-core.md
01-papers-by-conference/*/search-report.md
06-reading-summaries/v2/index.md
06-reading-summaries/v2/survey/index.md
06-reading-summaries/v2/advisor/index.md
```

Venue `mother-list.csv`, `candidates.csv`, `abc-reviewed.csv`, and paper cards are conference-search provenance. A/B/C does not determine reading priority.

## 3. Proceedings Intake

Use official proceedings or official accepted-paper pages: CVF, PMLR, ICLR Proceedings/OpenReview, or NeurIPS Proceedings.

For one venue/year:

1. preserve the complete accepted long-paper list as `mother-list.csv`;
2. exclude workshops, demos, challenges, tutorials, and invited talks;
3. for NeurIPS only, include all official long-paper tracks and preserve `official_track`;
4. run high-recall retrieval over the complete official title and, whenever available, the complete official abstract; do not rely on title-only retrieval;
5. reverse-search `spiking neuron`, `LIF`, `PLIF`, `surrogate gradient`, `STBP`, `online training`, `spiking transformer`, `spike-driven`, `point SNN`, `temporal delay`, `spike sparsity`, and `neuromorphic deployment` for the Advisor direction;
6. inspect the complete official title and abstract for every candidate, including retrieval false positives;
7. do not run full-PDF search over the mother list;
8. use PDF review only when an abstract cannot resolve a material boundary.

Every current candidate must have an audit row. Excluded false positives remain in the audit even though they do not enter `abc-reviewed.csv` or the active corpus.

## 4. Audit Schema And Rules

Required audit evidence:

```text
paper_id,title,year,venue,official_track,
in_active_corpus,abstract_reviewed,abstract_sha256,abstract,official_page,
survey_role,survey_topics,survey_core_decision,survey_reason,
advisor_role,advisor_topics,advisor_core_decision,advisor_reason,
reading_status,needs_pdf_check,evidence_basis,
pdf_boundary_check,pdf_boundary_finding
```

The abstract must be complete official text. Set `abstract_reviewed=yes`, calculate SHA256 over the stored abstract string, and provide a concrete reason for each track.

Survey roles:

- `anchor`: direct SNN-event integration central to the survey;
- `included`: genuine but narrower intersection evidence;
- `background`: indispensable event-only or SNN-only foundation/comparator;
- `exclude`: no useful role in the strict survey.

Advisor roles:

- `method_chain`: direct Event Cloud/point-SNN predecessor or reusable SECNet-SNN implementation mechanism;
- `discussion`: controlled evaluator, comparator, or second-stage optimization mechanism;
- `watch`: adjacent retained evidence;
- `exclude`: no useful relation to implementing SECNet as an SNN.

Reading assignments:

- `survey_core`;
- `advisor_required`;
- `advisor_helpful`;
- `retained_reference`;
- `excluded_from_active_corpus` only when both roles are `exclude`.

Use `needs_pdf_check=yes` only for an unresolved semantic boundary. An unresolved paper cannot enter Survey Core.

## 5. Survey Workflow

The Survey uses parallel foundations and an explicit intersection:

1. event-camera data organization and representation;
2. SNN computation, temporal learning, training, and efficiency;
3. their interface and integration topology;
4. task/evidence comparison and open problems.

`reading-plan-survey-core.md` contains the papers selected for human-guided V2 reading. Read by mechanism cluster, not mechanically by year. Update the provisional outline after roughly every ten newly completed Core papers. After all current Core papers have V2 evidence, finalize outline V1.0 and build a Core evidence matrix.

Then use the final outline to rank `survey-reference-pool.csv` separately for each section as `essential`, `useful`, or `omit`. A paper may support multiple sections. Select only the references needed by the argument, generate compact evidence-traceable cards for those papers, and verify PDFs for central mechanism or numerical claims. Do not generate heavy V1 summaries for the entire pool.

## 6. Advisor Workflow

`reading-plan-advisor-core.md` is intentionally bounded:

- `advisor_required`: necessary to define the SECNet-SNN input interface, point hierarchy, neuron, aggregation, temporal block, or controlled evaluation;
- `advisor_helpful`: second-stage training-memory, asynchronous-deployment, or efficiency optimization reading;
- SECNet is the separately listed focus paper. TTPOINT and other historical Event Cloud papers are optional references, not automatic Advisor Core assignments.

Advisor roles in the broader corpus are retrieval labels, not reading assignments. Do not enroll every `method_chain`, `discussion`, or `watch` paper. Use `03-review-draft/advisor-secnet-snn-reading-map.md` to read in implementation order and extract: SECNet insertion point, signal/state type, spike boundary, neuron/operator, temporal axis, training path, deployment compatibility, and evidence type. Frequency/Fourier papers remain historical references unless they answer one of those live implementation questions.

Advisor and Survey are separate evidence workflows. An Advisor-only V2 may explain how a paper informs SECNet, but it must not automatically create Survey paper relations, update `core-relation-matrix.csv`, update `literature-node-registry.csv`, change `outline.md`, alter Survey taxonomy, or add entries to the Survey evidence matrix. A paper assigned to both Survey and Advisor still follows the Survey evidence rules and may add a separate SECNet-context subsection; its Advisor role must not erase valid Survey evidence. The Advisor track is for the TPAMI extension and has no authority to reshape the Survey.

## 7. V2 Storage

Store each human-guided V2 once in:

```text
06-reading-summaries/v2/papers/
```

Do not duplicate a paper across Survey and Advisor folders. Generated indexes represent track-specific purpose and progress. The interactive deep-reading protocol is [`docs/core-reading-workflow.md`](core-reading-workflow.md).

## 8. Generation And Validation

After a new venue or semantic audit update, run:

```bash
python3 scripts/update_index.py
python3 scripts/update_selection.py
python3 scripts/update_v2_indexes.py
python3 scripts/validate_literature_graph.py
git diff --check
```

`update_selection.py` fails if:

- a current candidate lacks complete audit evidence;
- an abstract hash drifts;
- a NeurIPS track is missing;
- a role/topic/status is invalid;
- the active audit set differs from retained A/B/C metadata;
- a dual-excluded paper remains active.

## 9. Reporting And Git

After each venue or reselection, report:

- mother-list and candidate counts;
- retained A/B/C and dual-excluded counts;
- Survey and Advisor role distributions;
- Survey Core, reference pool, and Advisor Core totals;
- unresolved PDF checks;
- changed files and `git status`.

Never use GitHub CLI, force-push, delete mother lists, stage local PDFs or `work/`, overwrite user changes, or push before explicit confirmation.
