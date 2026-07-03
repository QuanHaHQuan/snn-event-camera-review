# SNN Event Camera Review Workflow Instructions

This document is the shareable, formal instruction set for initializing and using a GitHub-backed literature review repository for the survey topic:

**Spiking Neural Networks for Event Cameras**

The workflow is designed for venue-specific, auditable literature screening. It prioritizes official proceedings, preserves full venue mother lists before filtering, and uses high-recall title screening followed by strict official abstract/page confirmation.

Current scope is intentionally narrow:

* SNN / Spiking Neural Networks;
* Event Camera / DVS / visual event streams;
* SNN for Event Camera.

Do not broaden the repository into generic event-based systems, event logs, event-triggered control, temporal point processes, general asynchronous systems, biological spike sorting, or broad neuromorphic computing without clear SNN or event-camera evidence.

The current pre-enrollment reading strategy is maintained as a separate reading-plan layer:

* `00-index/reading-plan-core.md` = `unique(P0 papers + advisor_track papers)`;
* target size is about 60 papers;
* if fewer than 60 genuinely strong papers are available, do not pad the list;
* `P1` is optional reading;
* `P2` is for automatic summaries;
* `P3` is retained but inactive;
* `advisor_track` is only for understanding the uploaded SECNet / ICML 2026 method chain and selected SECNet references;
* do not encode or speculate about future TPAMI extension ideas.

## Part 1: Repository Initialization Instruction

Use this instruction when creating a fresh review repository.

```text
I want to build a reusable GitHub-backed research workflow for my survey project.

Project topic:
"Spiking Neural Networks for Event Cameras"

Goal:
Create a local Git repository named `snn-event-camera-review` that will store systematic venue-specific literature search results, paper cards, review notes, and future survey drafts.

Do not process any conference yet. First initialize the repository structure, templates, scripts, documentation, and Git setup.

Remote GitHub repository:
I plan to use SSH, not GitHub CLI.

If I provide a remote SSH URL, use it as the Git remote:
`[REPLACE_WITH_SSH_REMOTE_URL_OR_LEAVE_EMPTY]`

Example:
`git@github.com:USERNAME/snn-event-camera-review.git`

Rules:

* Do not use GitHub CLI.
* Do not create a GitHub repository through CLI/API.
* If a remote SSH URL is provided, add it as `origin` and push the initial commit through Git over SSH.
* If no remote SSH URL is provided, initialize only a local Git repository and tell me how to add the remote later.

Repository structure:

snn-event-camera-review
├── README.md
├── 00-index
│   ├── all-papers.csv
│   ├── level-A-papers.md
│   ├── level-B-event-camera.md
│   ├── level-C-snn.md
│   ├── conferences.md
│   └── datasets.md
├── 01-papers-by-conference
├── 02-topic-notes
│   ├── event-camera-representations.md
│   ├── snn-training-methods.md
│   ├── snn-event-camera-intersection.md
│   ├── datasets-and-benchmarks.md
│   └── efficiency-latency-energy.md
├── 03-review-draft
│   ├── outline.md
│   ├── introduction.md
│   ├── related-work.md
│   └── open-challenges.md
├── 04-templates
│   ├── paper-card-A.md
│   ├── paper-card-BC.md
│   ├── conference-report.md
│   └── paper-summary-schema.yaml
├── 05-logs
│   ├── search-logs
│   └── codex-runs
├── docs
│   └── workflow-instructions.md
└── scripts
    ├── conference_scraper.py
    ├── classify_candidates.py
    ├── generate_card.py
    ├── update_index.py
    └── github_sync.py

Repository requirements:

1. README.md

Create a clear README explaining:

* project purpose,
* research topic,
* repository structure,
* A/B/C/D/E classification rules,
* the high-recall title-screening and strict official-confirmation strategy,
* how conference-level searches are stored,
* how paper cards are generated,
* how global indexes are updated,
* limitations of automated literature search,
* principle: official proceedings are the primary source of truth,
* principle: automated summaries are draft notes and require human verification.

2. Global index files

Initialize these files:

* `00-index/all-papers.csv`
* `00-index/level-A-papers.md`
* `00-index/level-B-event-camera.md`
* `00-index/level-C-snn.md`
* `00-index/conferences.md`
* `00-index/datasets.md`

`00-index/all-papers.csv` should have these columns:

id,title,authors,conference,year,level,category,pdf_link,official_page,card_path,notes

Do not include citation count, dataset, task, or code fields in the global index unless they are already obvious and easy to extract. The goal is to keep the index stable and maintainable.

3. Paper card templates

Create `04-templates/paper-card-A.md`.

Important:
This is a template, not final content. When generating actual paper cards later, fill in title, authors, abstract, links, tags, and all detailed sections.

A-card template:

---
title: ""
authors: []
conference: ""
year:
level: "A"
category: "SNN + Event Camera"
pdf_link: ""
official_page: ""
tags: []
abstract: ""
status: "auto-generated; needs human review"
---

## Core Problem

## Core Method

## Key Metrics and Findings

## Personal Notes

## Method Details

## Experimental Analysis

## Related Work Connections

## Survey-Usable Points

Create `04-templates/paper-card-BC.md`.

Important:
This is a template, not final content. When generating actual paper cards later, fill in title, authors, abstract, links, tags, and the short scan-note sections.

B/C-card template:

---
title: ""
authors: []
conference: ""
year:
level: "B or C"
category: ""
pdf_link: ""
official_page: ""
tags: []
abstract: ""
status: "auto-generated; brief scan note"
---

## Core Problem

## Core Method

## Key Metrics and Findings

## Personal Notes

B/C cards should remain shorter than A cards, but they should contain paper-specific content in all four sections.

4. Conference report template

Create `04-templates/conference-report.md` with these sections:

* Search Summary
* Official Source
* Mother List Statistics
* Candidate Retrieval Keywords
* External Cross-check
* A/B/C/D/E Counts
* High-priority Reading List
* Limitations
* Manual Verification Needed

The template must mention the broad title retrieval pool:

* precise event-camera/DVS/SNN terms
* broad recall terms such as `event`, `event-based`, `spike`, and `spiking`

It must state that every title hit requires official abstract or official-page inspection before A/B/C promotion, and that title keywords are retrieval triggers, not classification evidence. Broad umbrella terms such as event-based vision, neuromorphic computing, event-driven, asynchronous, low latency, and spike camera do not count as A/B/C evidence by themselves.

5. Scripts

Create initial versions of the scripts. They can be functional skeletons with clear TODOs if full implementation is not possible yet.

The scripts should be designed for this workflow:

* `conference_scraper.py`
  Purpose: identify the official venue source, parse the official main-conference paper list, and save the full mother list.
  Output: `mother-list.csv`

* `classify_candidates.py`
  Purpose: apply broad high-recall title retrieval and strict A/B/C/D/E classification rules.
  Output: `candidates.csv` and `abc-reviewed.csv`

* `generate_card.py`
  Purpose: generate filled Markdown paper cards from `abc-reviewed.csv`.
  Rule: A papers use the A-card template; B/C papers use the short BC-card template.
  Important: generated cards must contain actual summaries, not template placeholder text.

* `update_index.py`
  Purpose: update global index files in `00-index`.

* `github_sync.py`
  Purpose: commit changes and optionally push to the configured SSH remote.

6. Classification rules

Use these rules throughout the repository:

A = Intersection / core paper:
Explicitly combines SNN/spiking neural computation with event cameras, DVS, visual event sensors, visual event streams, or event-camera datasets/data. Broad labels such as event-based vision or neuromorphic vision count only when the official abstract/page explicitly confirms event-camera/DVS/visual-event-stream data.

B = Event-camera-side paper:
Clearly about event cameras, DVS, dynamic vision sensors, visual event streams, event-camera datasets, or event-camera tasks, but does not clearly use SNN/spiking neural networks.

C = SNN-side paper:
Clearly about SNNs, spiking neural networks, spiking transformers, ANN-to-SNN conversion, surrogate gradients, spike trains, LIF/IF neurons, or SNN training/inference, but does not clearly involve event cameras/DVS/event-camera data.

D = Adjacent/background paper:
Related to asynchronous processing, temporal sparsity, event-driven computation, low-latency vision, neuromorphic ideas, spike cameras, or broad event-based vision, but not clearly about event cameras/DVS/visual-event-stream data or SNNs.

E = False positive:
Keyword match is unrelated.

Important:
B and C are equally important background categories. Do not assume one is more important than the other.

7. Git behavior

Initialize a local Git repository.

Make an initial commit with the message:
`Initialize SNN Event Camera review workflow`

If a remote SSH URL was provided:

* run `git remote add origin [SSH_REMOTE_URL]`,
* push the initial commit to `origin`,
* report whether the push succeeded.

If no remote SSH URL was provided:

* do not create a remote,
* report the exact commands I should run later:
  `git remote add origin git@github.com:USERNAME/snn-event-camera-review.git`
  `git push -u origin main`

After completing setup, report:

* repository path,
* created files,
* scripts created,
* whether Git was initialized,
* whether a remote was configured,
* whether the initial commit was pushed,
* how to run the next step,
* what input I should give you to process the first conference.
```

## Part 2: Conference Processing Instruction

Use this instruction when processing one venue/year.

```text
Process one conference for the `snn-event-camera-review` repository.

Target venue and year:
"[VENUE YEAR]"

Scope:
"main conference only"

Research topic:
"Spiking Neural Networks for Event Cameras"

Official proceedings or accepted-paper URL:
"[OFFICIAL_MAIN_CONFERENCE_URL]"

Repository:
Use the existing local repository `snn-event-camera-review`.

Main objective:
Run a high-recall title-screening workflow with strict official-source confirmation:

1. identify and parse the official main-conference paper list,
2. save the complete mother list before filtering,
3. retrieve candidates with one broad high-recall title keyword pool,
4. inspect official abstracts or official paper pages for every retrieved title candidate,
5. promote only candidates whose official evidence strictly confirms event-camera/DVS/visual-event-stream data or SNN/spiking neural computation,
6. classify candidates into A/B/C/D/E,
7. generate conference-level CSVs and report,
8. generate filled Markdown paper cards for A/B/C papers,
9. update global indexes,
10. commit changes to Git,
11. push to the configured SSH remote if one exists.

Important workflow principle:
This is a high-recall title-screening workflow with strict official-source confirmation, not a full exhaustive systematic review. Do not download or save abstracts for every paper unless the official source already provides them cheaply and directly. Do not perform full-PDF search over all papers. Use title-based retrieval first, then inspect official abstracts or official paper pages for all retrieved candidate papers before A/B/C promotion.

Strict scope rule:
Only include main-conference papers from the target venue/year. Exclude workshop papers, challenge papers, demo papers, tutorials, invited talks, non-archival papers, workshop proceedings, and papers from other venues or years. If workshop or non-main-conference papers are discovered during cross-checking, list them separately as out-of-scope findings and do not mix them into the main result.

Primary source rule:
Use the official main-conference proceedings, official open-access repository, accepted-paper list, OpenReview page, CVF page, PMLR page, IEEE/ACM proceedings page, or other official venue source as the primary source of truth.

External databases such as OpenAlex, Semantic Scholar, arXiv, Google-like search, and Papers With Code may only be used for cross-checking and metadata enrichment. External results must be verified against the official target venue/year/main-conference scope before inclusion.

Do not perform or maintain systematic code availability checking in this workflow. If a code link is clearly visible on the official paper page or abstract, it may be noted in the paper card's Personal Notes section, but do not search for code links as a required step and do not add code columns to the CSV files.

Topic boundary:
This search should focus only on one or both of the following core areas:

1. Event cameras / DVS / visual event sensors.
2. Spiking neural networks / spike-based neural computation.

Do not broaden A/B/C inclusion to general event-based vision, event-driven algorithms, asynchronous processing, low-latency vision, temporal modeling, neuromorphic computing, efficient vision, temporal point processes, biological spikes, or spike cameras unless the official abstract/page explicitly confirms event cameras/DVS/visual event sensors/event-camera data or SNN/spiking neural networks.

Candidate retrieval strategy:

Use one broad, high-recall title keyword pool over the full mother list. This pool intentionally mixes precise terms and broad recall terms. A title hit only creates a raw candidate; it is not classification evidence.

Precise Event Camera / DVS title keywords:

* event camera
* event cameras
* event-camera
* event-based camera
* event-based cameras
* dynamic vision sensor
* dynamic vision sensors
* DVS
* visual event sensor
* visual event sensors
* event sensor
* event sensors
* event stream
* event streams

Precise SNN / Spiking title keywords:

* spiking neural network
* spiking neural networks
* SNN
* SNNs
* spiking neuron
* spiking neurons
* spiking neural model
* spiking neural models
* spike train
* spike trains
* LIF
* leaky integrate-and-fire
* integrate-and-fire
* surrogate gradient
* surrogate gradients
* ANN-to-SNN
* ANN2SNN
* spiking transformer
* spiking transformers
* spike-based neural network
* spike-based neural networks

Broad recall title keywords:

* event
* event-based
* event-based vision
* event vision
* event data
* event representation
* event frame
* event volume
* voxel grid
* neuromorphic vision
* neuromorphic computing
* event-driven
* asynchronous
* low latency
* temporal sparsity
* sparse temporal
* high-speed vision
* temporal coding
* rate coding
* spike
* spiking
* spike camera

Important:
All title keywords are retrieval triggers, not classification evidence. Because `event`, `event-based`, `spike`, and `spiking` are broad base terms, they will retrieve many false positives. A paper can be classified as A/B/C only after its official abstract or official page explicitly confirms event-camera/DVS/visual-event-sensor/event-camera-dataset data or SNN/spiking neural computation.

Second-stage evidence must be strict:

* `event stream`, `event data`, and `event-based vision` count as event-camera evidence only when the official abstract/page ties them to event cameras, DVS, visual event sensors, address-event representation, asynchronous brightness-change sensing, an event-camera dataset, or a clearly visual event-stream task such as RGB-Event/frame-event/image-event fusion, event-to-video reconstruction, event-based deblurring, event-based stereo, event-based optical flow, event-based object detection, or event-based action recognition.
* Generic event sequences, event logs, event-triggered control, time-to-event data, temporal point processes, event-level video understanding, and ordinary asynchronous algorithms do not count as event-camera evidence.
* `spike` and `spiking` count as SNN evidence only when they refer to spiking neural networks, spiking neurons, LIF/IF models, ANN-to-SNN conversion, surrogate gradients, spiking transformers, or comparable spike-based neural computation.
* Biological spikes, spike sorting, spike cameras, and generic neuromorphic language are not sufficient for SNN evidence by themselves.

Otherwise the paper should remain D/E or be listed as an unpromoted title-candidate finding in the report.

Task labels:
Use these only to label already retrieved candidates. Do not use these as retrieval keywords:

* object detection
* tracking
* recognition
* reconstruction
* optical flow
* depth estimation
* semantic segmentation
* video interpolation
* stereo
* pose estimation
* 3D detection
* SLAM
* Gaussian Splatting

Workflow details:

Step 1: Identify the official source
Find the official main-conference paper list for the target venue/year/scope.

Report:

* official source URL,
* source type,
* retrieval date,
* whether this source is main conference only,
* whether titles and authors are available,
* whether abstracts are available directly on the list or only on individual paper pages,
* whether PDFs are available,
* whether supplementary links are available,
* parsing/access limitations.

Important:
Step 1 is only for identifying and validating the official source. Do not filter papers in Step 1.

Step 2: Build the full mother list
Parse or collect all main-conference papers from the official source.

For every paper, extract if available:

* title,
* authors,
* official paper page,
* PDF link,
* award/oral/spotlight/poster status.

Do not fetch or save abstracts for every paper by default. Only include an abstract in the mother list if the official paper list already provides it directly and cheaply.

Save:
`01-papers-by-conference/[VENUEYEAR]/mother-list.csv`

Mother-list CSV should include:
id,title,authors,conference,year,official_page,pdf_link,status_or_award

Report the total number of papers in the mother list.

Important:
The mother list must be saved before any filtering. This is the source-of-truth record for the venue/year.

Step 3: High-recall title-based candidate retrieval
Search the full mother list titles using the unified broad title keyword pool. Include both precise terms and broad recall terms, but treat every title hit as an unverified raw candidate.

Save:
`01-papers-by-conference/[VENUEYEAR]/candidates.csv`

Candidate CSV should include:
id,title,authors,conference,year,official_page,pdf_link,matched_keywords,matched_axis,classification_reason

Matched axis should be one of:

* Event Camera axis
* SNN axis
* Both axes
* Ambiguous

Important:
Candidates should usually use `matched_axis = Ambiguous` until official abstract/page inspection confirms a true event-camera or SNN axis.

Step 4: Targeted abstract or page inspection
For each retrieved candidate, inspect the official abstract or official paper page before A/B/C promotion. This applies to every title hit, including hits from precise keywords and broad recall keywords.

Use targeted abstract/page inspection when:

* any title keyword match needs confirmation that the keyword is being used in the intended event-camera/DVS or SNN/spiking sense,
* the title contains a broad word such as "event", "asynchronous", "low latency", or "spiking" but the topic is unclear,
* the paper may be A but the title does not clearly show both axes,
* the paper may be a false positive,
* a broad-recall title hit needs confirmation before A/B/C promotion,
* external cross-check finds a candidate not captured by title search.

Do not inspect abstracts for all papers in the mother list.

If an abstract is inspected, save it only in:
`abc-reviewed.csv`
and in the generated paper card.

Step 5: External cross-check
Use available research tools such as OpenAlex, Semantic Scholar-like search, arXiv search, or web search only to cross-check the official results.

Run narrow queries:

* "[VENUE YEAR] event camera"
* "[VENUE YEAR] event cameras"
* "[VENUE YEAR] dynamic vision sensor"
* "[VENUE YEAR] DVS"
* "[VENUE YEAR] visual event sensor"
* "[VENUE YEAR] event stream"
* "[VENUE YEAR] spiking neural network"
* "[VENUE YEAR] spiking neural networks"
* "[VENUE YEAR] SNN"
* "[VENUE YEAR] surrogate gradient"
* "[VENUE YEAR] ANN-to-SNN"
* "[VENUE YEAR] spiking transformer"

Use broader queries only as secondary checks:

* "[VENUE YEAR] event-based vision"
* "[VENUE YEAR] neuromorphic vision"
* "[VENUE YEAR] neuromorphic computing"

Add externally discovered candidates only if they can be verified against the official venue/year/main-conference scope.

If an external candidate is not found in the official mother list, do not include it in the main candidate table. Instead, list it under "out-of-scope or unverified external findings" in the conference report.

Step 6: Classification
Classify candidates as A/B/C/D/E using the repository rules.

A = Intersection / core paper:
Explicitly combines SNN/spiking neural computation with event cameras, DVS, visual event sensors, visual event streams, or event-camera datasets/data. Broad labels such as event-based vision or neuromorphic vision count only when the official abstract/page explicitly confirms event-camera/DVS/visual-event-stream data.

B = Event-camera-side paper:
Clearly about event cameras, DVS, dynamic vision sensors, visual event streams, event-camera datasets, or event-camera tasks, but does not clearly use SNN/spiking neural networks.

C = SNN-side paper:
Clearly about SNNs, spiking neural networks, spiking transformers, ANN-to-SNN conversion, surrogate gradients, spike trains, LIF/IF neurons, or SNN training/inference, but does not clearly involve event cameras/DVS/event-camera data.

D = Adjacent/background paper:
Related to asynchronous processing, temporal sparsity, event-driven computation, low-latency vision, neuromorphic ideas, spike cameras, or broad event-based vision, but not clearly about event cameras/DVS/visual-event-stream data or SNNs.

E = False positive:
Keyword match is unrelated.

Special handling:

* "Spike camera" papers should not automatically be treated as event-camera/DVS papers. Mark them as D unless they explicitly involve event cameras/DVS or SNNs.
* "Event-driven" in SNN papers should not count as event-camera evidence unless the paper explicitly mentions event cameras, visual event streams, DVS, dynamic vision sensors, or event-camera data.
* "Event-based vision" should be treated as B only when the official abstract/page clearly uses event-camera/DVS/visual-event-stream data or event-camera datasets.
* `Event stream`, `event data`, and `event-based vision` count as event-camera evidence only when tied to event cameras, DVS, visual event sensors, address-event representation, asynchronous brightness-change sensing, event-camera datasets, or clearly visual event-stream tasks such as RGB-Event/frame-event/image-event fusion, event-to-video reconstruction, event-based deblurring, event-based stereo, event-based optical flow, event-based object detection, or event-based action recognition.
* Generic event sequences, event logs, event-triggered control, time-to-event data, temporal point processes, event-level video understanding, and ordinary asynchronous algorithms are D/E unless event-camera/DVS evidence is explicit.
* `Spike` and `spiking` count as SNN evidence only when tied to spiking neural networks, spiking neurons, LIF/IF models, ANN-to-SNN conversion, surrogate gradients, spiking transformers, or comparable spike-based neural computation.
* Biological spikes, spike sorting, spike cameras, and generic neuromorphic language are not sufficient for SNN evidence by themselves.
* Broad umbrella terms such as event-based vision, neuromorphic vision/computing, asynchronous, event-driven, low latency, spike, spiking, and spike camera are not sufficient for A/B/C evidence by themselves.
* Title keywords alone are not sufficient for A/B/C promotion without official abstract/page confirmation.
* B and C are equal background categories; do not rank B above C by default.

Save:
`01-papers-by-conference/[VENUEYEAR]/abc-reviewed.csv`

ABC-reviewed CSV should include:
id,title,authors,conference,year,level,category,official_page,pdf_link,abstract,matched_keywords,classification_reason,card_path,notes

The `abstract` field should be filled only if the abstract was inspected or easily available. Otherwise write `Unknown`.

Step 7: Generate filled paper cards
Generate Markdown cards for all A/B/C papers.

Output paths:

* A papers:
  `01-papers-by-conference/[VENUEYEAR]/A/[YEAR]-[VENUE]-A-[slug].md`
* B papers:
  `01-papers-by-conference/[VENUEYEAR]/B/[YEAR]-[VENUE]-B-[slug].md`
* C papers:
  `01-papers-by-conference/[VENUEYEAR]/C/[YEAR]-[VENUE]-C-[slug].md`

Card generation rules:

* A papers use `04-templates/paper-card-A.md`.
* B/C papers use `04-templates/paper-card-BC.md`.
* Do not copy template placeholder text into generated cards.
* Fill every field and section using available information from title, inspected abstract, official paper page, and PDF only when necessary.
* If a field cannot be verified, write `Unknown` or `Needs human review`.
* Preserve the YAML front matter format.
* The `abstract` field should contain the actual abstract if available. If no abstract was inspected or available, write `Unknown`.

Content rules for A papers:

* Fill in the basic information.
* Fill these sections:
  * Core Problem
  * Core Method
  * Key Metrics and Findings
  * Personal Notes
  * Method Details
  * Experimental Analysis
  * Related Work Connections
  * Survey-Usable Points
* If the PDF was not deeply read, mark:
  `status: "auto-generated; needs human review"`
* Do not overclaim results if the PDF was not fully read.

Content rules for B/C papers:

* Fill in the basic information.
* Fill these sections:
  * Core Problem
  * Core Method
  * Key Metrics and Findings
  * Personal Notes
* Keep B/C cards shorter than A cards, but make every section paper-specific.
* If information is insufficient, say so explicitly rather than leaving the section blank.

Language:
Use Chinese for generated paper-card summaries unless the original title or technical term is better kept in English.

Step 8: Generate conference report
Create:
`01-papers-by-conference/[VENUEYEAR]/search-report.md`

The report must include:

* Search Summary
* Official Source
* Mother List Statistics
* Candidate Retrieval Keywords
* External Cross-check
* A/B/C/D/E Counts
* High-priority Reading List
* Title Candidates Not Promoted
* Limitations
* Manual Verification Needed

The report must explicitly state:

* this workflow used one broad high-recall title keyword pool,
* precise event-camera/DVS/SNN terms and broad recall terms, including `event`, `event-based`, `spike`, and `spiking`, were run across the full mother list,
* title keywords are retrieval triggers, not classification evidence,
* official abstracts or official paper pages were inspected for all retrieved candidates before A/B/C promotion,
* full-PDF search was not performed over all papers,
* therefore the result is high-precision and systematic, but not guaranteed exhaustive.

Step 9: Update global indexes
Update:

* `00-index/all-papers.csv`
* `00-index/level-A-papers.md`
* `00-index/level-B-event-camera.md`
* `00-index/level-C-snn.md`
* `00-index/conferences.md`
* `00-index/datasets.md` only if datasets are obvious from titles or inspected abstracts

Global index rule:
Do not add hard-to-maintain fields such as citation counts or code availability. Keep the global index stable and lightweight.

Step 10: Git commit and SSH sync
Make a Git commit with message:
`Add [VENUE YEAR] literature search results`

If a Git remote named `origin` is configured:

* push the commit to `origin` over SSH,
* report whether the push succeeded.

If no remote is configured:

* do not use GitHub CLI,
* do not create a remote automatically,
* report the exact command I should run to add an SSH remote.

Final response:
After finishing, report:

* number of papers in mother list,
* total number of title-matched candidates,
* number of externally discovered verified candidates,
* number of A/B/C/D/E papers,
* number of generated paper cards,
* files created/updated,
* whether Git commit succeeded,
* whether SSH push succeeded,
* limitations,
* manual checks needed.
```

## Current Rule Memory

For future venue processing in this repository, use the high-recall title-screening strategy with strict official-source confirmation:

1. Run one unified broad title keyword pool over the full mother list, including precise terms and broad recall terms such as `event`, `event-based`, `spike`, and `spiking`.
2. Inspect official abstracts or official paper pages for every title hit before A/B/C promotion.
3. Promote candidates to A/B/C only after official evidence confirms event-camera/DVS/visual-event-stream/event-camera-dataset data or SNN/spiking neural computation.
4. Keep false positives and adjacent papers in `candidates.csv` and report them under "Title Candidates Not Promoted" or equivalent unpromoted-candidate sections.
5. Never treat broad umbrella terms such as event-based vision, neuromorphic vision/computing, asynchronous, event-driven, low latency, spike, spiking, or spike camera as A/B/C evidence by themselves.
6. Never treat "spike camera" as event-camera/DVS evidence by default.

For the reading-plan layer, run:

```bash
python3 scripts/update_reading_plan.py
```

This script reads existing indexes, reviewed abstracts, cards, and the curated SECNet-reference subset. It generates:

* `00-index/reading-plan-core.md`
* `00-index/reading-plan-p1.md`
* `00-index/auto-summary-p2.md`
* `00-index/out-of-scope-x.md`
* `00-index/advisor-track.md`
* `00-index/uncertain-review.md`

It does not replace conference search, candidate classification, paper-card generation, or `scripts/update_index.py`.

Reading-plan refined levels:

* `A`: true SNN x Event Camera core paper.
* `B`: event-camera background.
* `C`: SNN background.
* `X`: out of scope / false positive.

Important correction: a generic SNN paper that only evaluates on CIFAR10-DVS, N-MNIST, DVS-Gesture, N-Caltech101, or similar event-camera benchmark datasets is `C`, not `A`, unless the method itself is clearly designed for event-camera / visual-event-stream data.
