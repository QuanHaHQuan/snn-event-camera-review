# ICCV 2025 Search Report

## Search Summary

- Research topic: Spiking Neural Networks for Event Cameras
- Scope: main conference only
- Workflow: two-pass title-first candidate retrieval; abstracts inspected for all core/auxiliary title hits; no full-PDF search over all papers
- Mother list: 2701 main-conference papers from the official CVF Open Access all-day proceedings page
- Title-matched candidates: 19
- External verified candidates: 0

## Official Source

- URL: https://openaccess.thecvf.com/ICCV2025?day=all
- Source type: CVF Open Access all-day main-conference proceedings list
- Retrieval date: 2026-07-01
- Main conference only: yes
- Titles and authors available: yes
- Abstracts on the list: no, only on individual paper pages
- PDFs available: yes
- Supplementary links available: yes
- Parsing limitations: titles and authors are available in a heterogeneous HTML layout; paper pages are the reliable source for abstracts

## Mother List Statistics

- Total main-conference papers: 2701
- Saved file: `01-papers-by-conference/ICCV2025/mother-list.csv`
- Abstracts were not stored in the mother list

## Candidate Retrieval Keywords

- Core Event Camera / DVS title keywords: event camera, event cameras, event-camera, event-based camera, event-based cameras, dynamic vision sensor, dynamic vision sensors, DVS, visual event sensor, visual event sensors, event sensor, event sensors, event stream, event streams
- Core SNN / Spiking title keywords: spiking neural network, spiking neural networks, SNN, SNNs, spiking neuron, spiking neurons, spiking neural model, spiking neural models, spike train, spike trains, LIF, leaky integrate-and-fire, integrate-and-fire, surrogate gradient, surrogate gradients, ANN-to-SNN, ANN2SNN, spiking transformer, spiking transformers, spike-based neural network, spike-based neural networks
- Auxiliary recall title keywords: event-based vision, event vision, event data, event representation, event frame, event volume, voxel grid, neuromorphic vision, neuromorphic computing, event-driven, asynchronous, low latency, temporal sparsity, sparse temporal, high-speed vision, temporal coding, rate coding, spike camera
- Auxiliary keywords were used as the second-stage title retrieval pass across the full mother list. They trigger targeted abstract/page inspection, but they are not classification evidence by themselves.

## External Cross-check

- External web queries were used only as a light cross-check and did not add verified main-conference candidates beyond the official CVF list.
- The auxiliary recall pass was run across all 2701 mother-list titles. Auxiliary-only findings were promoted only when official-page abstracts confirmed event-camera/DVS/event-stream or SNN/spiking evidence.
- Out-of-scope or unverified external findings were not promoted into the main candidate table.

## A/B/C/D/E Counts

- A: 1
- B: 14
- C: 1
- D/E raw candidates not promoted to A/B/C: 3

## High-priority Reading List

- A: SpiLiFormer: Enhancing Spiking Transformers with Lateral Inhibition
- B: Simultaneous Motion And Noise Estimation with Event Cameras; EvaGaussians; EventUPS; Continuous-Time Human Motion Field from Event Cameras; Unsupervised Joint Learning of Optical Flow and Intensity with Event Cameras; PRE-Mamba; Efficient Event Camera Data Pretraining; TESPEC; Depth Any Event Stream; From Sharp to Blur; Asynchronous Event Error-Minimizing Noise; A Linear N-Point Solver; Unleashing the Temporal Potential of Stereo Event Cameras; EvRT-DETR
- C: SpikePack: Enhanced Information Flow in Spiking Neural Networks with High Hardware Compatibility

## Auxiliary Findings Not Promoted

- ICCV2025-0109 `Event-Driven Storytelling with Multiple Lifelike Humans in a 3D Scene` -> E: Auxiliary title match only; official title/abstract does not confirm event-camera/DVS or SNN evidence.
- ICCV2025-1338 `Hierarchical Event Memory for Accurate and Low-latency Online Video Temporal Grounding` -> E: online video temporal grounding paper where "event" means temporal activity segment/proposal, not event-camera/DVS data or SNN computation.
- ICCV2025-1389 `SpikeDiff: Zero-shot High-Quality Video Reconstruction from Chromatic Spike Camera and Sub-millisecond Spike Streams` -> D: Spike camera / spike streams paper; not event camera/DVS and not SNN computation.

## Limitations

- This workflow used two title-first retrieval passes: a core keyword pass and an auxiliary recall pass.
- Abstracts were inspected only for the selected candidates.
- Full-PDF search was not performed over all papers.
- Therefore the result is high-precision and systematic, but not guaranteed exhaustive.

## Manual Verification Needed

- Verify whether any of the B-side papers should be split into more specific subtopics in later notes.
- Confirm the final survey relevance of each B/C paper before quoting it in prose.
- If later workshop or challenge papers are to be tracked, keep them outside this main-conference folder.
