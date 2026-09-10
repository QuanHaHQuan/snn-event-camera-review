# Taxonomy Architecture Design

Date: 2026-09-10
Status: design v0.1 delivered; awaiting user confirmation before Sol High pilot

## Authorization and checkout safety

User requested Taxonomy Architect design work with Astra High reasoning responsibilities. No execution of pilot, batch annotation, final taxonomy, manuscript drafting, membership changes, commit, push, or concurrent agents/tasks was authorized for this turn. No subagents were launched. Only the five explicitly allowed design outputs were created.

cwd and git top-level both resolved to `/Users/haoquanchen/Documents/Codex/2026-07-01/i-want-to-build-a-reusable/snn-event-camera-review`. All four required recent files were present. Initial working tree contained 20 tracked modifications and 4 untracked files. Existing differences were read and characterized as project-state synchronization, Advisor SECNet-SNN reselection, and corresponding views/workflow/generator changes. Initial content hashes for all 24 existing changed/untracked paths were recorded in temporary scratch; final checks confirm unchanged bytes and unchanged status codes.

## Inputs and verification scope

Read the requested repository workflow, planning and index materials, recent logs, and recent Advisor files for safety/context. Parsed the complete audit/selection/reference/registry/matrix CSVs, checked identities, shared fields, counts and abstract hashes; inspected the complete stored official titles/abstracts used to select the pilot and additional counterexamples. This is corpus-level structural analysis and pilot design, not a new 572-paper semantic annotation pass. Old decisions remain evidence/navigation context, never new taxonomy labels. Source text stored in the audit was not re-fetched from all official sites in this turn.

Repository snapshot:

- candidate audit: 572 unique IDs; 572 stored complete-abstract hashes verified; 298 active, 274 inactive.
- old Survey roles: anchor 15, included 4, background 266, exclude 287.
- Survey Core: 26 (15 anchor, 2 included, 9 background).
- Survey reference pool: 259 (257 background, 2 included); active includes 13 Survey-excluded Advisor references.
- Survey V2: 16 complete, 10 missing; 29 canonical V2 files overall.
- Advisor: 6 required + 2 helpful in proceedings plus SECNet focus; assignments untouched.
- registry: 84 nodes; matrix: 72 edges; classic candidates: 25. Historical relation-track fields are not live membership.
- old audit needs_pdf_check=no for all 572; this must not be reused as a method-level PDF clearance.

## Reference survey inspection

Applied PDF skill for read-only extraction and visual inspection. Read all 20 pages including bibliography; rendered pp.1–15, inspected layout overviews and key full pages (taxonomy, synthesis, result table). `fitz` was unavailable in the bundled Python, so used available pypdf for text and Poppler for rendering; no dependency installation or source-file modification.

PDF: `/Users/haoquanchen/Downloads/A Comprehensive Survey on Event Camera Representation Learning.pdf`
SHA256: `f59d5c39110a65c7e7eaa469a90dcdec33c7ba8c36f39339f75bb86ab6158de7`
Visible version: arXiv 2606.23078v2, 20 Aug 2026.
Visible title says Comprehensive; metadata title says Systematic. Template journal header is not publication metadata.

Non-bibliography content spans 15 pages: 12 narrative/figure pages and 3 comparison-table pages; bibliography spans pp.16–20, with 167 numbered entries. Page-area estimates in the memo explicitly separate sensor background from the taxonomy definitions embedded in the Introduction. Core taxonomy including preview is roughly 60% of non-reference content. Transferable structure: fixed observation boundary at the principal feature extractor, taxonomy-to-section links, consistent mechanism diagrams, and task/dataset evidence tables separated from method taxonomy. No taxonomy or numerical result was copied into a final SNN-event classification.

## Deliverables and decisions

1. `03-review-draft/taxonomy-architecture-memo.md`: verified state, reference structure/page budget, critique of scope layering, four falsifiable role hypotheses, secondary axes, claim-based selection, search plan, convergence and handoff.
2. `03-review-draft/taxonomy-annotation-codebook.md`: 59 ordered fields with purpose/type/values/definitions/examples/boundaries/unknown/PDF/use; conditional applicability; sequential decision tree; field-level provenance and confidence; questions, issues, QC and version rules.
3. `03-review-draft/taxonomy-pilot-plan.md`: 30 actual audit papers, complete canonical titles/venues/years, abstract-grounded rationale, per-paper PDF questions, coverage limitations and success criteria.
4. `04-templates/taxonomy-paper-annotation-schema.csv`: one header row only, exactly 59 fields; zero actual annotation rows.
5. This new log. No old log changed.

Primary role hypotheses: event_interface, task_network, embedded_module, algorithmic_engine. They are tentative functional roles, not a purity or training taxonomy. Training/analysis-only contributions can have no new inference role. Reference-only is a selection disposition; unresolved is an evidence state. Generic SNN with a DVS benchmark is not automatically a core intersection, but a genuine generic neuron/training contribution can remain snn_foundation rather than being forced outside scope. Redundancy does not change a paper's factual scope.

Pilot composition: 19 old Core + 11 non-Core; 27 active + 3 inactive; 27 targeted PDF-required + 3 conditional abstract-only scope/use controls. Includes two different CVPR 2026 SpikeTrack titles (RGB versus event input), point/dense/graph controls, interface and algorithmic methods, hybrid/multimodal, integer training/spike inference, conversion foundation, training/security, dataset authority, and misleading terminology. No pilot annotation executed. Graph event ANN plus generic graph SNN is not claimed as proof of a true graph-event-SNN intersection family; event-specific conversion and classic dense-task coverage remain open.

Proposed non-bibliography writing budget: 6% introduction/scope/search, 14% two-axis background, 58% core intersection, 12% tasks/evidence, 10% open problems/conclusion. The 150–180 usable expectation is not a quota; retain by concrete claim, unique mechanism/evidence/authority and version-aware deduplication.

## Validation

- Complete CSV parsing, active/reference joins and all 572 abstract SHA256 checks passed.
- Pilot IDs, canonical titles and venue/year exactly match the audit; 30 unique papers.
- Header-only schema matches the codebook field names/order exactly; 59 unique fields; all 59 have the required definition clauses.
- The synthetic JSON format example parses and is explicitly not a real paper annotation.
- Read-only graph validator: `literature_graph_ok registry=84 matrix=72 v2_edges=72 backward_search=19`.
- `git diff --check` plus explicit no-index whitespace checks for all five new/untracked outputs passed.
- Preexisting 24 changed/untracked files retain their starting content hashes and Git status; only five permitted new paths were added.

Mechanical checks do not establish semantic inter-rater agreement, pilot correctness or final taxonomy coverage. Those are future pilot/checkpoint work. No generators were run.

## Open issues and handoff

Astra must later decide whether contribution-based primary selection is reproducible, whether interface/module and algorithmic/task boundaries survive counterexamples, how training/analysis evidence belongs in the final outline, and whether thin graph/conversion/historical families require additional calibration before v1.0. Sol High will do pilot PDF reading and evidence preparation only after user confirmation. Sol Mid will handle frozen-codebook clear cases, extraction, validation and deterministic outputs; Astra owns rule changes and final corpus selection. No other task was started.

本轮没有批量标注572篇论文；没有冻结最终taxonomy；没有修改现有Survey/Advisor membership；没有commit；没有push。下一步应由用户确认codebook，再交给Sol High执行pilot。设计交付后暂停。

## Initial git status --short

```text
 M 00-index/candidate-screening-audit.csv
 M 00-index/paper-selection.csv
 M 00-index/reading-plan-advisor-core.md
 M 01-papers-by-conference/CVPR2026/search-report.md
 M 01-papers-by-conference/ICLR2024/search-report.md
 M 01-papers-by-conference/ICLR2026/search-report.md
 M 01-papers-by-conference/ICML2024/search-report.md
 M 03-review-draft/advisor-frequency-reading-map.md
 M 03-review-draft/core-reading-roadmap-13-to-26.md
 M 03-review-draft/outline.md
 M 03-review-draft/taxonomy-closure-audit.md
 M 06-reading-summaries/v2/advisor/index.md
 M 06-reading-summaries/v2/index.md
 M README.md
 M docs/core-reading-workflow.md
 M docs/proceedings-intake-agent-prompt.md
 M docs/proceedings-semantic-integration-prompt.md
 M docs/workflow-instructions.md
 M scripts/update_selection.py
 M scripts/update_v2_indexes.py
?? 03-review-draft/advisor-secnet-snn-implementation-shortlist.md
?? 03-review-draft/advisor-secnet-snn-reading-map.md
?? 05-logs/codex-runs/2026-09-09-project-state-sync.md
?? 05-logs/codex-runs/2026-09-10-secnet-snn-advisor-reselection.md
```

## Final git status --short

```text
 M 00-index/candidate-screening-audit.csv
 M 00-index/paper-selection.csv
 M 00-index/reading-plan-advisor-core.md
 M 01-papers-by-conference/CVPR2026/search-report.md
 M 01-papers-by-conference/ICLR2024/search-report.md
 M 01-papers-by-conference/ICLR2026/search-report.md
 M 01-papers-by-conference/ICML2024/search-report.md
 M 03-review-draft/advisor-frequency-reading-map.md
 M 03-review-draft/core-reading-roadmap-13-to-26.md
 M 03-review-draft/outline.md
 M 03-review-draft/taxonomy-closure-audit.md
 M 06-reading-summaries/v2/advisor/index.md
 M 06-reading-summaries/v2/index.md
 M README.md
 M docs/core-reading-workflow.md
 M docs/proceedings-intake-agent-prompt.md
 M docs/proceedings-semantic-integration-prompt.md
 M docs/workflow-instructions.md
 M scripts/update_selection.py
 M scripts/update_v2_indexes.py
?? 03-review-draft/advisor-secnet-snn-implementation-shortlist.md
?? 03-review-draft/advisor-secnet-snn-reading-map.md
?? 03-review-draft/taxonomy-annotation-codebook.md
?? 03-review-draft/taxonomy-architecture-memo.md
?? 03-review-draft/taxonomy-pilot-plan.md
?? 04-templates/taxonomy-paper-annotation-schema.csv
?? 05-logs/codex-runs/2026-09-09-project-state-sync.md
?? 05-logs/codex-runs/2026-09-10-secnet-snn-advisor-reselection.md
?? 05-logs/codex-runs/2026-09-10-taxonomy-architecture-design.md
```
