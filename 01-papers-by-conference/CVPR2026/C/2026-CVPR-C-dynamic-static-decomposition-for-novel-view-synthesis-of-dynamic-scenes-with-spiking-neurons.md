---
title: "Dynamic-Static Decomposition for Novel View Synthesis of Dynamic Scenes with Spiking Neurons"
authors: ["Lingyun Dai", "Zehao Chen", "Yan Liu", "Shi Gu", "Peng Lin", "De Ma", "Huajin Tang", "Qian Zheng", "Gang Pan"]
conference: "CVPR"
year: 2026
level: "C"
category: "SNN"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Dai_Dynamic-Static_Decomposition_for_Novel_View_Synthesis_of_Dynamic_Scenes_with_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Dai_Dynamic-Static_Decomposition_for_Novel_View_Synthesis_of_Dynamic_Scenes_with_CVPR_2026_paper.html"
tags: []
abstract: "Novel view synthesis for dynamic scenes remains challenging due to complex motion variations. Recent methods represent dynamic and static regions with separate Gaussians to improve efficiency and accuracy, but inaccurate assignment of static and dynamic Gaussian primitives still limits performance. We identify two key issues, namely inaccurate mask priors and improper tag representations, which lead to boundary artifacts, loss of fine-grained motion details, and overfitting on input views, resulting in degraded side-view synthesis. To address these problems, we propose a spatio-temporally fine-grained mask field and a discontinuous dynamic-static tagging field to achieve accurate assignment of dynamic and static Gaussian primitives, enabling high-quality novel view synthesis, especially in fine-grained motions, motion boundary regions, and side viewpoints. Experiments show that our method achieves state-of-the-art rendering quality and real-time performance."
status: "auto-generated; brief scan note"
---

## Core Problem

动态场景新视角合成中，动态与静态区域分配不准会带来边界伪影和细节丢失。

## Core Method

提出面向动态场景的 spatio-temporally fine-grained mask field 和 discontinuous dynamic-
static tagging field，并引入 spiking neurons。

## Key Metrics and Findings

摘要强调该方法缓解了边界伪影并提升了侧视图合成质量。

## Personal Notes

更像 SNN 参与的视觉几何方法，不涉及事件相机。

