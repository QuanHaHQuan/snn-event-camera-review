# ECCV 2024 Search Report

## Search Summary

- Research topic: Spiking Neural Networks for Event Cameras
- Scope: main conference only
- Workflow: strict two-stage screening. Stage 1 uses one broad high-recall title keyword pool; Stage 2 inspects the official abstract/page for every title hit and promotes only strictly confirmed event-camera/DVS or SNN papers.
- Full-PDF search over all papers was not performed.
- Mother list: 2387 official proceedings papers
- Total title-matched raw candidates: 47
- A/B/C promoted after strict official abstract/page inspection: 38
- External verified candidates: 0 in this strict rescan; official proceedings pages were used as source of truth.

## Official Source

- URL: https://eccv.ecva.net/virtual/2024/papers.html
- Source type: official ECVA virtual proceedings paper list
- Retrieval date: 2026-07-01
- Scope handling: main conference only
- Titles and authors available: yes
- Abstracts on the list: no; candidate abstracts were inspected on individual official paper pages
- PDFs available: yes when provided by the official source
- Supplementary links available: yes when provided by the official source; systematic code checking was not performed
- Parsing/access limitations: strict rescan used cached official paper pages for title-matched candidates; full-PDF search over all papers was not performed

## Mother List Statistics

- Total official proceedings papers: 2387
- Saved file: `01-papers-by-conference/ECCV2024/mother-list.csv`

## Candidate Retrieval Keywords

- Unified title keyword pool includes precise event-camera/DVS/SNN terms plus broad recall terms such as `event`, `event-based`, `spike`, and `spiking`.
- Title keywords are retrieval triggers only, not classification evidence.
- Every title hit was inspected through its official abstract/page before A/B/C promotion.
- `event stream`, `event data`, and `event-based vision` count as event-camera evidence only when tied to event cameras, DVS, visual event sensors, address-event representation, asynchronous brightness-change sensing, event-camera datasets, or clearly visual event-stream tasks such as RGB-Event/frame-event/image-event fusion, event-to-video reconstruction, event-based deblurring, event-based stereo, event-based optical flow, event-based object detection, or event-based action recognition.
- Generic event sequences, event logs, event-triggered control, time-to-event data, temporal point processes, ordinary asynchronous algorithms, biological spikes, spike sorting, spike cameras, and generic neuromorphic language are not sufficient for A/B/C evidence by themselves.

## External Cross-check

- External databases were not used for direct inclusion in this strict rescan.
- Out-of-scope or unverified external findings: none recorded in this pass.

## A/B/C/D/E Counts

- A: 4
- B: 28
- C: 6
- D: 1
- E: 8

## High-priority Reading List

- A: EAS-SNN: End-to-End Adaptive Sampling and Representation for Event-based Detection with Recurrent Spiking Neural Networks; REDIR: Refocus-free Event-based De-occlusion Image Reconstruction; Exploring Vulnerabilities in Spiking Neural Networks: Direct Adversarial Attacks on Raw Event Data; Spike-Temporal Latent Representation for Energy-Efficient Event-to-Video Reconstruction
- B: Motion and Structure from Event-based Normal Flow; LiDAR-Event Stereo Fusion with Hallucinations; Towards Real-world Event-guided Low-light Video Enhancement and Deblurring; BeNeRF:Neural Radiance Fields from a Single Blurry Image and Event Stream; Temporal Event Stereo via Joint Learning with Stereoscopic Flow; CMTA: Cross-Modal Temporal Alignment for Event-guided Video Deblurring; Event Camera Data Dense Pre-training; Motion Aware Event Representation-driven Image Deblurring; Event Trojan: Asynchronous Event-based Backdoor Attacks; Temporal Residual Guided Diffusion Framework for Event-Driven Video Reconstruction; Revisit Event Generation Model: Self-Supervised Learning of Event-to-Video Reconstruction with Implicit Neural Representations; FARSE-CNN: Fully Asynchronous, Recurrent and Sparse Event-Based CNN; Event-Aided Time-To-Collision Estimation for Autonomous Driving; Event-Adapted Video Super-Resolution; Finding Meaning in Points: Weakly Supervised Semantic Segmentation for Event Cameras; Event-Based Motion Magnification; Event-based Head Pose Estimation: Benchmark and Method; Towards Robust Event-based Networks for Nighttime via Unpaired Day-to-Night Event Translation; Efficient Learning of Event-based Dense Representation using Hierarchical Memories with Adaptive Update; DailyDVS-200: A Comprehensive Benchmark Dataset for Event-Based Action Recognition; TimeLens-XL: Real-time Event-based Video Frame Interpolation with Large Motion; EDformer: Transformer-Based Event Denoising Across Varied Noise Levels; Physical-Based Event Camera Simulator; UniINR: Event-guided Unified Rolling Shutter Correction, Deblurring, and Interpolation; Event-based Mosaicing Bundle Adjustment; Temporal-Mapping Photography for Event Cameras; Edge-Guided Fusion and Motion Augmentation for Event-Image Stereo; Un-EVIMO: Unsupervised Event-based Independent Motion Segmentation
- C: Asynchronous Bioplausible Neuron for Spiking Neural Networks for Event-Based Vision; Integer-Valued Training and Spike-driven Inference Spiking Neural Network for High-performance and Energy-efficient Object Detection; Efficient Training of Spiking Neural Networks with Multi-Parallel Implicit Stream Architecture; BKDSNN: Enhancing the Performance of Learning-based Spiking Neural Networks Training with Blurred Knowledge Distillation; FTBC: Forward Temporal Bias Correction for Optimizing ANN-SNN Conversion; Spiking Wavelet Transformer


## Title Candidates Not Promoted

- ECCV2024-0213 `Label-anticipated Event Disentanglement for Audio-Visual Video Parsing` -> E. Official abstract/page inspection did not strictly confirm event-camera/DVS or SNN relevance.
- ECCV2024-0268 `Learning to Robustly Reconstruct Dynamic Scenes from Low-light Spike Streams` -> D. Official abstract/page mentions spike camera but not event camera/DVS or SNN.
- ECCV2024-1138 `ScaleDreamer: Scalable Text-to-3D Synthesis with Asynchronous Score Distillation` -> E. Official abstract/page inspection did not strictly confirm event-camera/DVS or SNN relevance.
- ECCV2024-1144 `EA-VTR: Event-Aware Video-Text Retrieval` -> E. Official abstract/page inspection did not strictly confirm event-camera/DVS or SNN relevance.
- ECCV2024-1397 `EventBind: Learning a Unified Representation to Bind Them All for Event-based Open-world Understanding` -> E. Official abstract/page inspection did not strictly confirm event-camera/DVS or SNN relevance.
- ECCV2024-1752 `Asynchronous Large Language Model Enhanced Planner for Autonomous Driving` -> E. Official abstract/page inspection did not strictly confirm event-camera/DVS or SNN relevance.
- ECCV2024-1943 `3D Hand Sequence Recovery from Real Blurry Images and Event Stream` -> E. Official abstract/page inspection did not strictly confirm event-camera/DVS or SNN relevance.
- ECCV2024-2022 `Fine-grained Dynamic Network for Generic Event Boundary Detection` -> E. Official abstract/page inspection did not strictly confirm event-camera/DVS or SNN relevance.
- ECCV2024-2263 `MEVG : Multi-event Video Generation with Text-to-Video Models` -> E. Official abstract/page inspection did not strictly confirm event-camera/DVS or SNN relevance.

## Limitations

- This strict rescan improves precision but is still not guaranteed exhaustive because retrieval is title-first and full-PDF search over all papers was not performed.
- Some papers may require human reading to decide whether an A-level label reflects a true method-level intersection or an SNN method evaluated on an event-camera dataset.
- Generated cards remain draft notes and require human verification before citation.

## Manual Verification Needed

- Manually verify all Level A papers before treating them as survey-core intersection papers.
- Confirm dataset names, metrics, baselines, latency, energy, and hardware claims from PDFs before using them in survey prose.
- Re-check any title candidates where official abstracts were unavailable or unusually terse.
