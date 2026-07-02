# ICLR 2025 Search Report

## Search Summary

- Research topic: Spiking Neural Networks for Event Cameras
- Scope: official ICLR 2025 proceedings page
- Workflow: broad high-recall title keyword retrieval followed by strict official abstract/page confirmation for every title hit
- Full-PDF search over all papers was not performed
- Mother list: 3703 official proceedings papers
- Total title-matched raw candidates: 26
- A/B/C promoted after official abstract/page inspection: 12
- External verified candidates: 0; all included candidates were verified against the official ICLR proceedings list

## Official Source

- URL: https://proceedings.iclr.cc/paper_files/paper/2025
- Source type: official ICLR proceedings page
- Retrieval date: 2026-07-02
- Main conference only: yes, the saved proceedings list uses `data-track="conference"` and visible track badges `Conference`
- Titles and authors available: yes
- Abstracts on the list: no; abstracts are available on individual official paper pages
- PDFs available: yes
- Supplementary links available: not systematically captured in this pass
- Parsing/access limitations: candidate abstracts were downloaded only for title-matched candidates; full-PDF search over all papers was not performed

## Mother List Statistics

- Total official proceedings papers: 3703
- Saved file: `01-papers-by-conference/ICLR2025/mother-list.csv`

## Candidate Retrieval Keywords

- Unified title keyword pool includes precise event-camera/DVS/SNN terms plus broad recall terms such as `event`, `event-based`, `spike`, and `spiking`.
- Title keywords are retrieval triggers only, not classification evidence.
- A/B/C promotion requires official abstract/page evidence for event-camera/DVS/visual-event-stream/event-camera-dataset data or SNN/spiking neural computation.
- Broad umbrella terms such as event-based vision, neuromorphic computing, event-driven, asynchronous, low latency, spike, spiking, and spike camera are not sufficient by themselves.

## External Cross-check

- External databases were not used for direct inclusion in this pass; the official ICLR proceedings page was used as the source of truth.
- Out-of-scope or unverified external findings: none recorded in this pass.

## A/B/C/D/E Counts

- A: 3
- B: 1
- C: 8
- D: 0
- E: 14

## High-priority Reading List

- A: Rethinking Spiking Neural Networks from an Ensemble Learning Perspective; DeepTAGE: Deep Temporal-Aligned Gradient Enhancement for Optimizing Spiking Neural Networks; Temporal Flexibility in Spiking Neural Networks: Towards Generalization Across Time Steps and Deployment Friendliness
- B: RGB-Event ISP: The Dataset and Benchmark
- C: Quantized Spike-driven Transformer; Spiking Vision Transformer with Saccadic Attention; TS-LIF: A Temporal Segment Spiking Neuron Network for Time Series Forecasting; SpikeLLM: Scaling up Spiking Neural Network to Large Language Models via Saliency-based Spiking; P-SPIKESSM: HARNESSING PROBABILISTIC SPIKING STATE SPACE MODELS FOR LONG-RANGE DEPENDENCY TASKS; Improving Generalization and Robustness in SNNs Through Signed Rate Encoding and Sparse Encoding Attacks; Improving the Sparse Structure Learning of Spiking Neural Networks from the View of Compression Efficiency; QP-SNN: Quantized and Pruned Spiking Neural Networks

## Title Candidates Not Promoted

- ICLR2025-0145 `Asynchronous RLHF: Faster and More Efficient Off-Policy RL for Language Models` -> E. Official abstract/page inspection did not confirm event-camera/DVS or SNN relevance.
- ICLR2025-0844 `No Need to Talk: Asynchronous Mixture of Language Models` -> E. Official abstract/page inspection did not confirm event-camera/DVS or SNN relevance.
- ICLR2025-1030 `Rare event modeling with self-regularized normalizing flows: what can we learn from a single failure?` -> E. Official abstract/page inspection did not confirm event-camera/DVS or SNN relevance.
- ICLR2025-1399 `Enabling Realtime Reinforcement Learning at Scale with Staggered Asynchronous Inference` -> E. Official abstract/page inspection did not confirm event-camera/DVS or SNN relevance.
- ICLR2025-1688 `An Asynchronous Bundle Method for Distributed Learning Problems` -> E. Official abstract/page inspection did not confirm event-camera/DVS or SNN relevance.
- ICLR2025-1758 `SPAM: Spike-Aware Adam with Momentum Reset for Stable LLM Training` -> E. Official abstract/page inspection did not confirm event-camera/DVS or SNN relevance.
- ICLR2025-2653 `Asynchronous Federated Reinforcement Learning with Policy Gradient Updates: Algorithm Design and Convergence Analysis` -> E. Official abstract/page inspection did not confirm event-camera/DVS or SNN relevance.
- ICLR2025-2657 `Event-Driven Online Vertical Federated Learning` -> E. Official abstract/page inspection did not confirm event-camera/DVS or SNN relevance.
- ICLR2025-2693 `DistRL: An Asynchronous Distributed Reinforcement Learning Framework for On-Device Control Agent` -> E. Official abstract/page inspection did not confirm event-camera/DVS or SNN relevance.
- ICLR2025-2840 `RESuM: A Rare Event Surrogate Model for Physics Detector Design` -> E. Official abstract/page inspection did not confirm event-camera/DVS or SNN relevance.
- ICLR2025-3019 `Robotouille: An Asynchronous Planning Benchmark for LLM Agents` -> E. Official abstract/page inspection did not confirm event-camera/DVS or SNN relevance.
- ICLR2025-3030 `Time-to-Event Pretraining for 3D Medical Imaging` -> E. Official abstract/page inspection did not confirm event-camera/DVS or SNN relevance.
- ICLR2025-3136 `ACES: Automatic Cohort Extraction System for Event-Stream Datasets` -> E. Official abstract/page inspection did not confirm event-camera/DVS or SNN relevance.
- ICLR2025-3226 `TRACE: Temporal Grounding Video LLM via Causal Event Modeling` -> E. Official abstract/page inspection did not confirm event-camera/DVS or SNN relevance.

## Limitations

- This workflow favors high recall at title retrieval, so raw candidates include false positives from generic event sequences, event-triggered methods, asynchronous optimization, biological spikes, and non-SNN spike terminology.
- Every raw title hit was checked against official ICLR abstracts/pages before A/B/C promotion, but the result is still not guaranteed exhaustive because full-PDF search was not performed over all papers.
- Generated cards remain draft notes and require human verification before citation.

## Manual Verification Needed

- Manually verify any Level A papers before treating them as survey-core intersection papers.
- Confirm dataset names, metrics, baselines, latency, energy, and hardware claims from PDFs before using them in survey prose.
- Re-check ambiguous spike/event terminology if later full-text reading suggests a missed event-camera or SNN connection.
