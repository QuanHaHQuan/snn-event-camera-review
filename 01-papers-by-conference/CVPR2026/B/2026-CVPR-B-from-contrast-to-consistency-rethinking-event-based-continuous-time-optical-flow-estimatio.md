---
title: "From Contrast to Consistency: Rethinking Event-based Continuous-Time Optical Flow Estimation"
authors: ["Rui Hu", "Song Wu", "Wen Yang", "Jinjian Wu"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_From_Contrast_to_Consistency_Rethinking_Event-based_Continuous-Time_Optical_Flow_Estimation_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Hu_From_Contrast_to_Consistency_Rethinking_Event-based_Continuous-Time_Optical_Flow_Estimation_CVPR_2026_paper.html"
tags: []
abstract: "Estimating continuous optical flow is a fundamental yet challenging problem in dynamic visual perception. Event-based cameras, with microsecond latency and high dynamic range, capture brightness changes asynchronously, offering a unique opportunity to model motion with fine temporal precision. However, the scarcity of temporally dense ground-truth annotations limits the effectiveness of supervised learning, while contrast maximization (CM) frameworks, focused on sharpening the Image of Warped Events (IWE), often neglect temporal continuity and structural coherence, leading to distorted trajectories under complex motion.To overcome these challenges, we propose a hybrid-supervised framework for continuous-time optical flow estimation, grounded in the principle of Spatio-temporal Structural Consistency (STSC). This paradigm jointly enforces local structural stability and trajectory continuity, ensuring physically coherent motion across time. To further enhance representation and robustness, we design a bidirectionally complementary multi-scale architecture and employ a curriculum-guided hybrid training strategy, enabling a smooth transition from supervised point constraints to self-supervised manifold regularization.Comprehensive experiments across multiple benchmarks show that our method achieves state-of-the-art performance in both continuous-time and standard optical flow estimation, demonstrating the effectiveness of the proposed learning paradigm."
status: "auto-generated; brief scan note"
---
## Core Problem

Estimating continuous optical flow is a fundamental yet challenging problem in dynamic
visual perception.

## Core Method

Event-based cameras, with microsecond latency and high dynamic range, capture brightness
changes asynchronously, offering a unique opportunity to model motion with fine temporal
precision.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event-based camera。自动分类理由：Official abstract/page confirms event-camera/DVS/event-
stream evidence; no clear SNN evidence.。
