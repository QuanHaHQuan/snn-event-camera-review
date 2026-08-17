# Taxonomy Closure Audit

Status: **v0.1, external-survey evidence integrated; current Core progress 13/26 V2 papers**.

This audit asks whether the survey taxonomy is broad enough to discover relevant work. It does **not** turn every discovered branch into a Core-reading quota. `Spiking Transformer` is treated as one diagnostic example among many, not as the organizing center of the audit.

## 1. Scope and decision rule

The target remains **Spiking Neural Networks for Event Cameras**. The taxonomy must close three spaces:

1. the event-camera axis: how sensor events are organized, represented, enhanced, and evaluated;
2. the SNN axis: how information is coded, propagated, learned, scaled, and deployed;
3. the intersection axis: where event data becomes model spikes, what remains asynchronous, and what evidence supports the claimed advantage.

A branch belongs in the taxonomy when it is needed to describe or compare the intersection. A paper enters Survey Core only when it is one of:

- a direct event-camera + SNN method with representative mechanism or evidence;
- an indispensable foundation for a survey branch that cannot be explained from a closer intersection paper;
- a benchmark or critique that changes how intersection results must be interpreted.

Generic SNN work, generic event-based vision, and task breadth remain reference material unless they satisfy one of these conditions.

## 2. External evidence sources

| Source | Year / status | Primary use in this audit | Evidence weight | SHA256 |
| --- | --- | --- | --- | --- |
| *Deep Learning for Event-based Vision: A Comprehensive Survey and Benchmarks* | arXiv v3, 2024 | Event representation, quality enhancement, tasks, datasets, and research directions | primary for event-side taxonomy; bibliographic details still require official-source normalization | `212d306af8464afcae7a6dae068d0f2dc26b2af544802f00170665f741344e6f` |
| *Direct training high-performance deep spiking neural networks: a review of theories and methods* | Frontiers in Neuroscience, 2024 | Neuron models, coding, direct training, residual SNNs, Spiking Transformers, software and hardware | primary for modern directly trained SNN taxonomy | `46898d2708e367bd4388bb639a602874240e494099ac7feb7dd6773a8d1ec95e` |
| *Hardware, Algorithms, and Applications of the Neuromorphic Vision Sensor: A Review* | Sensors, 2025 | Sensor hardware, representations, classical/deep algorithms, applications, deployment gaps | supporting source for sensor-to-system coverage | `1a93de2386fcd89f1929fbc6d61e509b34c3ade269df45a56e249b0176a4c8db` |
| *Recent Event Camera Innovations: A Survey* | ECCV NeVi workshop, 2024 | Milestones, cameras, datasets, simulators, and backward search | supporting bibliography map, not a Core-admission authority by itself | `2e8df531d73b65cfbee98ce67111ba37e9dc1782eacdc1168c9c7ff5b28654c9` |
| *Spiking Neural Networks: A Comprehensive Survey of Training Methodologies, Hardware Implementations and Applications* | IEEE/SWU AI Science and Engineering, 2025 | Broad SNN cross-check: conversion, direct training, STDP, hybrid learning, hardware and applications | secondary gap check; claims require confirmation from primary papers | `a0f28939c8c633f94a75aa0d69a8fd8e49c0ba7894e7da1e85e176b2ae1020bc` |

The older TPAMI *Event-based Vision: A Survey* remains a writing and historical reference, but it is not counted as one of the five recent closure sources.

## 3. Closed taxonomy

### 3.1 Event-camera axis

| Dimension | Required branches | Current 26-paper Core | Closure status | Action |
| --- | --- | --- | --- | --- |
| Sensor semantics | logarithmic brightness change; polarity; timestamp; asynchronous address events; noise and refractory effects | represented indirectly across all intersection papers | partial | use a classic sensor/survey citation; no dedicated full V2 required |
| Temporal organization | fixed-duration; fixed-count; packetization; adaptive global/local slicing; event-by-event processing | ASTW, EAS-SNN, SpikeSlicer, SDA | strong | preserve slicing as distinct from representation |
| Representation family | image/event frame; time surface; voxel; point/Event Cloud; graph; learned representation; spike-native input | dense and point branches are strong; the promoted asynchronous graph paper adds current evidence, while classic surface/learned lineages remain thin | partial | add classic evidence cards for the historical lineage |
| Representation properties | dense/sparse; polarity retention; temporal precision; spatial context; preprocessing cost; information loss | distributed across SpikePoint, PEPNet, dense memory, EAS-SNN, STLR | strong as comparison axes | keep dense/sparse as a cross-cutting property, not the only taxonomy |
| Event quality and generation | denoising; super-resolution; simulation; domain shift; augmentation | EventRPG covers augmentation; denoising/simulation are reference-only | adequate for scope | discuss only when they change SNN input or evaluation |
| Sensor fusion | event-only; frame-event; RGB-event; multimodal sensor fusion | SFOD, ClearSight, SpikeFET and hybrid detector | strong | compare where fusion occurs and whether the fused path is spiking |

### 3.2 SNN axis

| Dimension | Required branches | Current 26-paper Core | Closure status | Action |
| --- | --- | --- | --- | --- |
| Spike coding and input | rate; temporal/latency; direct current/input; learned event-to-spike mapping | implicit in application papers, not explicit as a foundation | thin | add a focused foundation note; do not equate camera events with neuronal spikes |
| Neuron dynamics | IF/LIF; learnable/adaptive LIF; recurrent/gated; multi-compartment or parallel neurons | CLIF, EAS-SNN, SpikeTrack, SDA | strong for representative mechanisms | avoid cataloguing every neuron variant |
| Architecture families | convolutional/residual SNN; recurrent/stateful SNN; Spiking Transformer/attention/mixer; point/graph SNN; hybrid ANN-SNN | application coverage is broad; generic deep residual and early Spiking Transformer lineage is thin | partial | make these families explicit in the outline and backfill selected classics |
| Learning paradigms | ANN-to-SNN conversion; direct surrogate-gradient training; BPTT/STBP; online/local learning; STDP; distillation; normalization and stabilization | conversion, direct training, STDP and task-specific learning are present; online/local and normalization are reference-level | partial but sufficient for Core | use classic/focused cards instead of adding one Core paper per optimizer |
| Temporal capability | recurrent state; long-range memory; delay; multi-timescale dynamics; timestep flexibility; temporal credit assignment | EAS-SNN, CLIF, temporal flexibility, FLAME and several task methods | strong | SSM/Mamba remains a comparator or hybrid component, not a taxonomy branch |
| Efficiency mechanism | sparse spikes; addition-only claims; timestep/firing rate; state/memory cost; pruning/quantization; asynchronous compatibility | STEP, quantization critique, conversion, deployed hybrid detector, multiple anchors | strong | distinguish operation proxy, runtime, chip estimate and measured hardware |
| Hardware and software | simulation frameworks; synchronous accelerators; asynchronous neuromorphic hardware; co-design | current Core emphasizes evidence rather than hardware history | partial by design | cite Loihi/other hardware surveys; do not turn the survey into a chip catalogue |

### 3.3 Intersection axis

| Dimension | Required branches | Current 26-paper Core | Closure status | Action |
| --- | --- | --- | --- | --- |
| Event-to-spike boundary | raw event; grouped events; dense tensor; sparse points/graph; model input spikes; internal spikes; continuous output | well represented | strong | require every V2 to state the exact boundary |
| SNN role | backbone/task network; temporal module; representation/slicing controller; optimization/inference engine | all four roles have representatives | strong | retain the role-based topology in Chapter 4 |
| Network boundary | fully spiking backbone; fully spiking task model; hybrid pipeline; converted SNN; non-spiking comparator | well represented | strong | avoid using `fully spiking` without naming the boundary |
| Task coverage | recognition; detection; tracking; reconstruction/restoration; pose/depth/flow/segmentation | recognition, detection, tracking and reconstruction are strong; event-SNN optical flow/depth history is thin | partial | backfill classic intersection papers; task parity is not a Core quota |
| Robustness | sensor noise; lighting/domain shift; adversarial event perturbation; temporal retiming; representation sensitivity | direct raw-event attack and several robust task methods | adequate | keep as evidence/open-problem thread, not a dominant chapter |
| Evaluation | accuracy/quality; latency; energy; firing rate; timesteps; operations; memory; hardware deployment | multiple anchors plus STEP and efficiency critique | strong | use an evidence hierarchy and record measurement type |

## 4. What the Spiking Transformer example actually revealed

The current Core did not omit the whole family: HsVT covers an event-camera hybrid Spiking Vision Transformer, SDTrack uses a fully spike-driven Transformer in tracking, and STEP covers comparative evaluation. The omission was structural: Chapter 3 did not explicitly name the architecture families, and the Core lacked a clean historical bridge from residual SNNs to Spikformer and spike-driven attention.

The same audit therefore checked all sibling branches rather than only Transformer variants. The other meaningful weaknesses are:

1. classic event representation lineage: time surfaces, EST/Matrix-LSTM, voxel and graph representations;
2. classic SNN scaling lineage: surrogate gradients, STBP/SLAYER, residual SNNs and modern Spiking Transformers;
3. event-SNN task history outside recent proceedings, especially optical flow, depth and early reconstruction/tracking;
4. a sharper distinction between sensor sparsity, spike sparsity, operation estimates and actual asynchronous hardware execution.

These are primarily **classic-literature and synthesis gaps**, not evidence that dozens of recent generic SNN papers should enter Core.

## 5. Current-proceedings re-screen policy

The complete `candidate-screening-audit.csv` remains the source of truth: every row has a complete official title, complete official abstract, and an abstract SHA256. Closure re-screening uses that table in two passes:

1. taxonomy recall pass: retrieve every abstract matching any closed branch, including architecture synonyms and ambiguous `event`/`spike` language;
2. semantic boundary pass: reject spike-camera imaging, non-visual event terminology, generic SNN papers that only evaluate on DVS datasets, and generic event-camera papers that do not supply indispensable intersection evidence.

Results and borderline decisions are recorded in `taxonomy-closure-corpus-rescreen.csv`. A branch being underrepresented does not lower the semantic admission threshold.

## 6. Implications for the reading workflow

- Continue reading the existing anchors in parallel; this audit does not invalidate completed V2 files.
- Use full V2 for direct intersection anchors and genuinely indispensable foundations.
- Use focused V2 or evidence cards for selected classic foundations.
- Do not deep-read every generic Spiking Transformer, neuron, optimizer, event task, dataset, or hardware paper.
- At the next V2 checkpoint, update claims and chapter proportions from the accumulated evidence matrix; do not reopen taxonomy from scratch unless a new external survey or proceedings exposes an uncovered branch.

## 7. Closure conclusion

The taxonomy is now broad enough for high-recall screening across the present scope. It is not historically complete because the repository is still concentrated in 2024-2026 proceedings. The remaining risk is therefore **bibliographic depth before 2024**, handled by `classic-literature-candidates.csv`, rather than an unidentified modern architecture family hidden inside the current corpus.
