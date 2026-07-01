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

单个事件相机的输出稀疏且噪声大，难以直接完成完整动态场景重建。

## Core Method

将 Deformable Gaussian Splatting 与单事件相机结合，面向 fast dynamic scenes 做高保真 4D 重建。

## Key Metrics and Findings

摘要强调摆脱了对额外帧相机或复杂标定的依赖。

## Personal Notes

可作为事件相机 + 3DGS 方向的背景论文。

