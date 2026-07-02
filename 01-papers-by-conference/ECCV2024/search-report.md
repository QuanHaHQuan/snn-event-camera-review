# ECCV 2024 Search Report

## Search Summary

- Research topic: Spiking Neural Networks for Event Cameras
- Scope: main conference only
- Workflow: two-pass title-first candidate retrieval plus official mother-list cross-check for narrow event-based/spiking terms; abstracts inspected only for retrieved or cross-check candidates; no full-PDF search over all papers
- Mother list: 2387 main-conference papers from the official ECCV virtual proceedings papers page
- Core title candidates: 13
- Auxiliary title candidates: 6
- Official mother-list cross-check candidates: 14
- Total raw candidates: 33
- External verified candidates: 0 from external databases; all included candidates were verified against the official ECCV main-conference list

## Official Source

- URL: https://eccv.ecva.net/virtual/2024/papers.html
- Source type: ECCV official virtual main-conference papers list
- Retrieval date: 2026-07-01
- Main conference only: yes, per user-provided official main-conference link and page navigation under Main Conference / Papers
- Titles and authors available: titles on the list page; authors on individual official poster pages
- Abstracts on the list: no, only on individual official poster pages
- PDFs available: yes, via individual official poster pages linking to ECVA PDFs
- Supplementary links available: yes, for many papers on individual poster pages
- Parsing limitations: the list page is JavaScript-oriented but contains static paper links; author/PDF/abstract fields require visiting official poster pages. Some official poster pages did not expose a parseable abstract, but all candidate abstracts used here were available from official poster pages.

## Mother List Statistics

- Total main-conference papers: 2387
- Saved file: `01-papers-by-conference/ECCV2024/mother-list.csv`
- Abstracts were not stored in the mother list

## Candidate Retrieval Keywords

- Core Event Camera / DVS title keywords: event camera, event cameras, event-camera, event-based camera, event-based cameras, dynamic vision sensor, dynamic vision sensors, DVS, visual event sensor, visual event sensors, event sensor, event sensors, event stream, event streams
- Core SNN / Spiking title keywords: spiking neural network, spiking neural networks, SNN, SNNs, spiking neuron, spiking neurons, spiking neural model, spiking neural models, spike train, spike trains, LIF, leaky integrate-and-fire, integrate-and-fire, surrogate gradient, surrogate gradients, ANN-to-SNN, ANN2SNN, spiking transformer, spiking transformers, spike-based neural network, spike-based neural networks
- Auxiliary recall title keywords: event-based vision, event vision, event data, event representation, event frame, event volume, voxel grid, neuromorphic vision, neuromorphic computing, event-driven, asynchronous, low latency, temporal sparsity, sparse temporal, high-speed vision, temporal coding, rate coding, spike camera
- Auxiliary keywords were used as retrieval triggers, not classification evidence. Auxiliary-only and cross-check candidates were promoted to A/B/C only after official abstract/page evidence confirmed event-camera/DVS/event-stream data or SNN/spiking neural computation.

## External Cross-check

- External databases were not used for inclusion because the official ECCV source was sufficient and complete for the venue scope.
- A narrow official mother-list cross-check was run for event-based/spiking variants not fully captured by the core title list, including titles containing event-based, event based, neuromorphic, spiking, SNN, spike, and ANN-SNN.
- Cross-check candidates were included only if they were present in the official ECCV 2024 main-conference mother list and confirmed by official poster-page abstracts.
- Notable cross-check additions include `Motion and Structure from Event-based Normal Flow`, `EventBind`, `Spiking Wavelet Transformer`, `DailyDVS-200`, `TimeLens-XL`, `REDIR`, and `Spike-Temporal Latent Representation`.

## A/B/C/D/E Counts

- A: 5
- B: 20
- C: 5
- D/E raw candidates not promoted to A/B/C: 3

## High-priority Reading List

- A: Asynchronous Bioplausible Neuron for Spiking Neural Networks for Event-Based Vision; EAS-SNN: End-to-End Adaptive Sampling and Representation for Event-based Detection with Recurrent Spiking Neural Networks; Exploring Vulnerabilities in Spiking Neural Networks: Direct Adversarial Attacks on Raw Event Data; REDIR: Refocus-free Event-based De-occlusion Image Reconstruction; Spike-Temporal Latent Representation for Energy-Efficient Event-to-Video Reconstruction
- B: BeNeRF:Neural Radiance Fields from a Single Blurry Image and Event Stream; Event Camera Data Dense Pre-training; Motion Aware Event Representation-driven Image Deblurring; Event Trojan: Asynchronous Event-based Backdoor Attacks; Temporal Residual Guided Diffusion Framework for Event-Driven Video Reconstruction; FARSE-CNN: Fully Asynchronous, Recurrent and Sparse Event-Based CNN; Finding Meaning in Points: Weakly Supervised Semantic Segmentation for Event Cameras; Physical-Based Event Camera Simulator; 3D Hand Sequence Recovery from Real Blurry Images and Event Stream; Temporal-Mapping Photography for Event Cameras; Motion and Structure from Event-based Normal Flow; Event-Based Motion Magnification; Event-based Head Pose Estimation: Benchmark and Method; Towards Robust Event-based Networks for Nighttime via Unpaired Day-to-Night Event Translation; EventBind: Learning a Unified Representation to Bind Them All for Event-based Open-world Understanding; Efficient Learning of Event-based Dense Representation using Hierarchical Memories with Adaptive Update; DailyDVS-200: A Comprehensive Benchmark Dataset for Event-Based Action Recognition; TimeLens-XL: Real-time Event-based Video Frame Interpolation with Large Motion; Event-based Mosaicing Bundle Adjustment; Un-EVIMO: Unsupervised Event-based Independent Motion Segmentation
- C: Integer-Valued Training and Spike-driven Inference Spiking Neural Network for High-performance and Energy-efficient Object Detection; Efficient Training of Spiking Neural Networks with Multi-Parallel Implicit Stream Architecture; BKDSNN: Enhancing the Performance of Learning-based Spiking Neural Networks Training with Blurred Knowledge Distillation; FTBC: Forward Temporal Bias Correction for Optimizing ANN-SNN Conversion; Spiking Wavelet Transformer

## Auxiliary Findings Not Promoted

- ECCV2024-1138 `ScaleDreamer: Scalable Text-to-3D Synthesis with Asynchronous Score Distillation` -> E: Auxiliary title match only; official abstract is text-to-3D score distillation, not event-camera/DVS or SNN.
- ECCV2024-1752 `Asynchronous Large Language Model Enhanced Planner for Autonomous Driving` -> E: Auxiliary title match only; official abstract is LLM planning for autonomous driving, not event-camera/DVS or SNN.
- ECCV2024-0268 `Learning to Robustly Reconstruct Dynamic Scenes from Low-light Spike Streams` -> D: Spike camera / spike streams paper; not event camera/DVS and not SNN computation.

## Limitations

- This workflow used two title-first retrieval passes plus a narrow official mother-list cross-check; it is systematic and high precision, but not guaranteed exhaustive.
- Abstracts were inspected only for retrieved or cross-check candidates.
- Full-PDF search was not performed over all papers. One targeted PDF check was used for `Asynchronous Bioplausible Neuron for Spiking Neural Networks for Event-Based Vision` to verify event-camera dataset evidence.
- Some A/B/C boundaries require human review, especially papers where event-camera evidence comes from datasets or event-based benchmark context rather than the main method title.
- Generated paper cards are draft notes and should be checked against the official PDFs before citation.

## Manual Verification Needed

- Verify whether Level A papers are truly core intersection papers or should be downgraded if event-camera evidence is only a benchmark axis.
- Review `REDIR` and `Asynchronous Bioplausible Neuron` carefully because their A classification depends on abstract/PDF evidence beyond the title.
- Confirm dataset names and quantitative metrics before using them in survey prose.
- Keep any ECCV workshop/challenge/tutorial papers outside this main-conference folder.
