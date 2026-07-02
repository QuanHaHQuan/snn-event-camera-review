---
title: "Event-Guided Consistent Video Enhancement with Modality-Adaptive Diffusion Pipeline"
authors: ["Kanghao Chen, Zixin Zhang, Guoqiang Liang, Lutao Jiang, Zeyu Wang, Yingcong Chen"]
conference: "NeurIPS"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/dc3be1574e0f86d76e32a0229bb1f6be-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/dc3be1574e0f86d76e32a0229bb1f6be-Abstract-Conference.html"
tags: []
abstract: "Recent advancements in low-light video enhancement (LLVE) have increasingly leveraged both RGB and event cameras to improve video quality under challenging conditions. However, existing approaches share two key drawbacks. First, they are tuned for steady low-light scenes, so their performance drops when illumination varies. Second, they assume every sensing modality is always available, while real systems may lose or corrupt one of them. These limitations make the methods brittle in dynamic, real-world settings. In this paper, we propose EVDiffuser, a novel framework for consistent LLVE that integrates RGB and event data through a modality-adaptive diffusion pipeline. By harnessing the powerful priors of video diffusion models, EVDiffuser enables consistent video enhancement and generalization to diverse scenarios under varying illumination, where RGB or events may even be absent. Specifically, we first design a modality-agnostic conditioning mechanism based on a diffusion pipeline by treating the two modalities as optional conditions, which is fine-tuned using augmented and integrated datasets. Furthermore, we introduce a modality-adaptive guidance rescaling that dynamically adjusts the contribution of each modality according to sensor-specific characteristics. Additionally, we establish a benchmark that accounts for varying illumination and diverse real-world scenarios, facilitating future research on consistent event-guided LLVE. Our experiments demonstrate state-of-the-art performance across challenging scenarios (i.e., varying illumination) and sensor-based settings (e.g., event-only, RGB-only), highlighting the generalization of our framework."
status: "auto-generated; brief scan note"
---

## Core Problem

Recent advancements in low-light video enhancement (LLVE) have increasingly leveraged both RGB and event cameras to improve video quality under challenging conditions.

## Core Method

However, existing approaches share two key drawbacks.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
