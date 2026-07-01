# CVPR 2026 Search Report

## Search Summary

- Research topic: Spiking Neural Networks for Event Cameras
- Scope: main conference only
- Workflow: two-pass title-first candidate retrieval; abstracts inspected for all core/auxiliary title hits; no full-PDF search over all papers
- Mother list: 4068 main-conference papers from the official CVF Open Access all-day proceedings page
- Title-matched candidates: 32
- External verified candidates: 0

## Official Source

- URL: https://openaccess.thecvf.com/CVPR2026?day=all
- Source type: CVF Open Access all-day main-conference proceedings list
- Retrieval date: 2026-07-01
- Main conference only: yes
- Titles and authors available: yes
- Abstracts on the list: no, only on individual paper pages
- PDFs available: yes
- Supplementary links available: yes, for many papers
- Parsing limitations: page HTML is heterogeneous; paper pages use different link combinations for PDF and supplemental files, so lightweight parsing was used and a few link fields may remain blank when the official page omits them

## Mother List Statistics

- Total main-conference papers: 4068
- Saved file: `01-papers-by-conference/CVPR2026/mother-list.csv`
- Abstracts were not stored in the mother list

## Candidate Retrieval Keywords

- Core Event Camera / DVS title keywords: event camera, event cameras, event-camera, event-based camera, event-based cameras, dynamic vision sensor, dynamic vision sensors, DVS, visual event sensor, visual event sensors, event sensor, event sensors, event stream, event streams
- Core SNN / Spiking title keywords: spiking neural network, spiking neural networks, SNN, SNNs, spiking neuron, spiking neurons, spiking neural model, spiking neural models, spike train, spike trains, LIF, leaky integrate-and-fire, integrate-and-fire, surrogate gradient, surrogate gradients, ANN-to-SNN, ANN2SNN, spiking transformer, spiking transformers, spike-based neural network, spike-based neural networks
- Auxiliary recall title keywords: event-based vision, event vision, event data, event representation, event frame, event volume, voxel grid, neuromorphic vision, neuromorphic computing, event-driven, asynchronous, low latency, temporal sparsity, sparse temporal, high-speed vision, temporal coding, rate coding, spike camera
- Auxiliary keywords were used as the second-stage title retrieval pass across the full mother list. They trigger targeted abstract/page inspection, but they are not classification evidence by themselves.

## External Cross-check

- External databases were not needed for inclusion because the official CVF source was already sufficient for the two-pass title-first scan.
- No externally discovered candidate was verified beyond the official mother list.
- The auxiliary recall pass was run across all 4068 mother-list titles.
- Auxiliary recall pass findings promoted after official-page inspection:
  - CVPR2026-2758 `Texvent: Asynchronous Event Data Simulation via Text Prompt` -> B
  - CVPR2026-3325 `FlashCap: Millisecond-Accurate Human Motion Capture via Flashing LEDs and Event-Based Vision` -> B

## A/B/C/D/E Counts

- A: 2
- B: 15
- C: 8
- D/E raw candidates not promoted to A/B/C: 7

## High-priority Reading List

- A: SpikeTrack and SDTrack
- B: Event Structural Valley, Adaptive Spatial-Temporal Window, FastEventDGS, Unsupervised 3D Motion Estimation Using Event Camera, From Corners to Fiducial Tags, EventGait, DarkShake-DVS, eRetinexGS, EventDrive, Event Stream Filtering via Probability Flux Estimation
- C: Temporal Granularity in the Robustness of Spiking Neural Networks, Temporal Interaction in Spiking Transformers with Multi-Delay Mixer, Robust Spiking Neural Networks by Temporal Mutual Information, Towards Reliable Evaluation of Adversarial Robustness for Spiking Neural Networks, Stable Spike, Rethinking SNN Online Training and Deployment, Reconstructing Spiking Neural Networks Using a Single Neuron with Autapses, Dynamic-Static Decomposition for Novel View Synthesis of Dynamic Scenes with Spiking Neurons

## Auxiliary Findings Not Promoted

- CVPR2026-0005 `Spk2VidNet: A Hierarchical Recurrent Architecture for High-Fidelity Video Reconstruction from Long Spike-Camera Streams` -> D: Spike-camera streams paper; not event camera/DVS and not SNN computation.
- CVPR2026-0586 `Semantics Lead the Way: Harmonizing Semantic and Texture Modeling with Asynchronous Latent Diffusion` -> E: Auxiliary title match only; official title/abstract does not confirm event-camera/DVS or SNN evidence.
- CVPR2026-0639 `APEX: A Decoupled Memory-based Explorer for Asynchronous Aerial Object Goal Navigation` -> E: Auxiliary title match only; official title/abstract does not confirm event-camera/DVS or SNN evidence.
- CVPR2026-0891 `Mesh-Pro: Asynchronous Advantage-guided Ranking Preference Optimization for Artist-style Quadrilateral Mesh Generation` -> E: Auxiliary title match only; official title/abstract does not confirm event-camera/DVS or SNN evidence.
- CVPR2026-2018 `Asynchronous Temporal Modeling with Two-Agent Framework for Streaming Dense Video Captioning` -> E: Auxiliary title match only; official title/abstract does not confirm event-camera/DVS or SNN evidence.
- CVPR2026-2568 `Gallant: Voxel Grid-based Humanoid Locomotion and Local-navigation across 3-D Constrained Terrains` -> E: Auxiliary title match only; official title/abstract does not confirm event-camera/DVS or SNN evidence.
- CVPR2026-3529 `VAR RL Done Right: Tackling Asynchronous Policy Conflicts in Visual Autoregressive Generation` -> E: Auxiliary title match only; official title/abstract does not confirm event-camera/DVS or SNN evidence.

## Limitations

- This workflow used two title-first retrieval passes: a core keyword pass and an auxiliary recall pass.
- Abstracts were inspected only for candidates where needed, using official paper pages cached from CVF Open Access.
- Full-PDF search was not performed over all papers.
- Therefore the result is high-precision and systematic, but not guaranteed exhaustive.
- Some candidate cards remain auto-generated draft notes and require human review before being cited in survey prose.

## Manual Verification Needed

- Confirm the final A/B/C boundaries before citation.
- Verify any paper whose abstract or title might overstate event-camera relevance.
- Check whether any later workshop or challenge paper should be tracked separately outside this main-conference folder.
