---
title: "FastEventDGS: Deformable Gaussian Splatting for Fast Dynamic Scenes from a Single Event Camera"
authors: ["Zijia Dai", "Nico Messikommer", "Rong Zou", "Nikola Zubic", "Davide Scaramuzza", "Laurent Kneip"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Dai_FastEventDGS_Deformable_Gaussian_Splatting_for_Fast_Dynamic_Scenes_from_a_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Dai_FastEventDGS_Deformable_Gaussian_Splatting_for_Fast_Dynamic_Scenes_from_a_CVPR_2026_paper.html"
tags: []
abstract: "The demand for dynamic 3D assets in AR/VR has recently popularized Deformable Gaussian Splatting. However, traditional RGB cameras are limited in their ability to reconstruct high-speed scenes due to motion blur and low temporal resolution. While event cameras offer a promising alternative, reconstructing a complete scene from their sparse and noisy output is a significant challenge. Existing event-based methods rely on an auxiliary sensor, such as a frame camera, thereby inducing tedious hardware and calibration challenges.We introduce FastEventDGS, a novel Deformable Gaussian Splatting-based framework that leverages a single event camera for high-fidelity 4D reconstruction. Our method utilizes a continuous camera trajectory parametrization and integrates two event generation models to provide both photometric and geometric constraints. We further propose a local patch event motion loss to constrain object motion, effectively mitigating overfitting. To ensure robust reconstruction, we employ an off-the-shelf model for depth correction and apply noise regularization terms in the final stage. We demonstrate robust results on both new synthetic and real-world datasets, highlighting our framework's ability to provide a simplified, event-only solution for high-fidelity 4D reconstruction in dynamic scenes."
status: "auto-generated; brief scan note"
---

## Core Problem

The demand for dynamic 3D assets in AR/VR has recently popularized Deformable Gaussian Splatting.

## Core Method

However, traditional RGB cameras are limited in their ability to reconstruct high-speed scenes due to motion blur and low temporal resolution.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
