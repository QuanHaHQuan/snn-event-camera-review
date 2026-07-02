---
title: "TimeLens-XL: Real-time Event-based Video Frame Interpolation with Large Motion"
authors: ["Shi Guo", "Yutian Chen", "Tianfan Xue", "Jinwei Gu", "Yongrui Ma"]
conference: "ECCV"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/11208.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/1003"
tags: []
abstract: "Video Frame Interpolation (VFI) aims to predict intermediate frames between consecutive low frame rate inputs. To handle the real-world complex motion between frames, event cameras, which capture high-frequency brightness changes at micro-second temporal resolution, are used to aid interpolation, denoted as Event-VFI. One critical step of Event-VFI is optical flow estimation. Prior methods that adopt either a two-segment formulation or a parametric trajectory model cannot correctly recover large and complex motions between frames, which suffer from accumulated error in flow estimation. To solve this problem, we propose TimeLens-XL, a physically grounded lightweight network that decomposes large motion between two frames into a sequence of small motions for better accuracy. It estimates the entire motion trajectory recursively and samples the bi-directional flow for VFI. Benefiting from the accurate and robust flow prediction, intermediate frames can be efficiently synthesized with simple warping and blending. As a result, the network is extremely lightweight, with only 1/5~1/10 computational cost and model size of prior works, while also achieving state-of-the-art performance on several challenging benchmarks. To our knowledge, TimeLens-XL is the first real-time (27fps) Event-VFI algorithm at a resolution of 1280x720 using a single RTX 3090 GPU. Furthermore, we have collected a new RGB+Event dataset (HQ-EVFI) consisting of more than 100 challenging scenes with large complex motions and accurately synchronized high-quality RGB-EVS streams. HQ-EVFI addresses several limitations presented in prior datasets and can serve as a new benchmark. Both the code and dataset will be released upon publication."
status: "auto-generated; brief scan note"
---

## Core Problem

Video Frame Interpolation (VFI) aims to predict intermediate frames between consecutive low frame rate inputs.

## Core Method

To handle the real-world complex motion between frames, event cameras, which capture high-frequency brightness changes at micro-second temporal resolution, are used to aid interpolation, denoted as Event-VFI.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context; brightness change visual-event context; event-based video visual-event context; event dataset visual-event context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
