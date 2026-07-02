---
title: "Event-guided HDR Reconstruction with Diffusion Priors"
authors: ["Yixin Yang", "Jiawei Zhang", "Yang Zhang", "Yunxuan Wei", "Dongqing Zou", "Jimmy S. Ren", "Boxin Shi"]
conference: "ICCV"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "Unknown"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Yang_Event-guided_HDR_Reconstruction_with_Diffusion_Priors_ICCV_2025_paper.html"
tags: []
abstract: "Events provide High Dynamic Range (HDR) intensity change which can guide Low Dynamic Range (LDR) image for HDR reconstruction. However, events only provide temporal intensity differences and it is still ill-posed in over-/under-exposed areas due to missing initial reference brightness and color information. With strong generation ability, diffusion models have shown their potential for tackling ill-posed problems. Therefore, we introduce conditional diffusion models to hallucinate missing information. Whereas, directly adopting events and LDR image as conditions is complicated for diffusion models to sufficiently utilize their information. Thus we introduce a pretrained events-image encoder tailored for HDR reconstruction and a pyramid fusion module to provide HDR conditions, which can be efficiently and effectively utilized by the diffusion model. Moreover, the generation results of diffusion models usually exhibit distortion, particularly for fine-grained details. To better preserve fidelity and suppress distortion, we propose a fine-grained detail recovery approach using a histogram-based structural loss. Experiments on real and synthetic data show the effectiveness of the proposed method in terms of both detail preservation and information hallucination."
status: "auto-generated; brief scan note"
---
## Core Problem

Events provide High Dynamic Range (HDR) intensity change which can guide Low Dynamic Range
(LDR) image for HDR reconstruction.

## Core Method

However, events only provide temporal intensity differences and it is still ill-posed in
over-/under-exposed areas due to missing initial reference brightness and color information.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：events; events-image encoder; event-guided HDR。自动分类理由：Official abstract confirms
events and an events-image encoder for HDR reconstruction; no clear SNN evidence.。
