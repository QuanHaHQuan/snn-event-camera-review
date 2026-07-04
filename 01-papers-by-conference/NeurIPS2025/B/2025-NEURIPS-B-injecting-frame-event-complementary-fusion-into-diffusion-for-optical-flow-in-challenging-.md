---
title: "Injecting Frame-Event Complementary Fusion into Diffusion for Optical Flow in Challenging Scenes"
authors: ["Haonan Wang, Hanyu Zhou, Haoyue Liu, Luxin Yan"]
conference: "NeurIPS"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/2d7b46ab7623124c2705683dea36fbef-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/2d7b46ab7623124c2705683dea36fbef-Abstract-Conference.html"
tags: []
abstract: "Optical flow estimation has achieved promising results in conventional scenes but faces challenges in high-speed and low-light scenes, which suffer from motion blur and insufficient illumination. These conditions lead to weakened texture and amplified noise and deteriorate the appearance saturation and boundary completeness of frame cameras, which are necessary for motion feature matching. In degraded scenes, the frame camera provides dense appearance saturation but sparse boundary completeness due to its long imaging time and low dynamic range. In contrast, the event camera offers sparse appearance saturation, while its short imaging time and high dynamic range gives rise to dense boundary completeness. Traditionally, existing methods utilize feature fusion or domain adaptation to introduce event to improve boundary completeness. However, the appearance features are still deteriorated, which severely affects the mostly adopted discriminative models that learn the mapping from visual features to motion fields and generative models that generate motion fields based on given visual features. So we introduce diffusion models that learn the mapping from noising flow to clear flow, which is not affected by the deteriorated visual features. Therefore, we propose a novel optical flow estimation framework Diff-ABFlow based on diffusion models with frame-event appearance-boundary fusion. Inspired by the appearance-boundary complementarity of frame and event, we propose an Attention-Guided Appearance-Boundary Fusion module to fuse frame and event. Based on diffusion models, we propose a Multi-Condition Iterative Denoising Decoder. Our proposed method can effectively utilize the respective advantages of frame and event, and shows great robustness to degraded input. In addition, we propose a dual-modal optical flow dataset for generalization experiments. Extensive experiments have verified the superiority of our proposed method. The code is released at ."
status: "auto-generated; brief scan note"
---
## Core Problem

Optical flow estimation has achieved promising results in conventional scenes but faces
challenges in high-speed and low-light scenes, which suffer from motion blur and
insufficient illumination.

## Core Method

These conditions lead to weakened texture and amplified noise and deteriorate the appearance
saturation and boundary completeness of frame cameras, which are necessary for motion
feature matching.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event cameras; event camera visual-event context; frame-event visual-event
context。自动分类理由：Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor
evidence; no clear SNN evidence found.。 备注：strict two-stage rescan; official abstract/page
inspected; needs human verification; Track: Main Conference Track。
