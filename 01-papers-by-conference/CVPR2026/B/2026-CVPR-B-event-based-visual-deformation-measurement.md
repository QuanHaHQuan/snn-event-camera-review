---
title: "Event-based Visual Deformation Measurement"
authors: ["Yuliang Wu", "Wei Zhai", "Yuxin Cui", "Tiesong Zhao", "Yang Cao", "Zheng-Jun Zha"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_Event-based_Visual_Deformation_Measurement_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Event-based_Visual_Deformation_Measurement_CVPR_2026_paper.html"
tags: []
abstract: "Visual Deformation Measurement (VDM) aims to recover dense deformation fields by tracking surface motion from camera observations. Traditional image-based methods rely on minimal inter-frame motion to constrain the correspondence search space, which limits their applicability to highly dynamic scenes or necessitates high-speed cameras at the cost of prohibitive storage and computational overhead. We propose an event-frame fusion framework that exploits events for temporally dense motion cues and frames for spatially dense precise estimation. Revisiting the solid elastic modeling prior, we propose an Affine Invariant Simplicial (AIS) framework. It partitions the deformation field into linearized sub-regions with low-parametric representation, effectively mitigating motion ambiguities arising from sparse and noisy events. To speed up optimization and reduce error accumulation, a neighborhood-greedy optimization strategy is introduced, enabling well-converged sub-regions to guide their poorly-converged neighbors, effectively suppress local error accumulation in long-term dense tracking. To evaluate the proposed method, a benchmark dataset with temporally aligned event streams and frames is established, encompassing over 120 sequences spanning diverse deformation scenarios. Experimental results show that our method outperforms the state-of-the-art baseline by 1.6x in survival rate. Remarkably, it achieves this using only 18.9% of the data storage and processing resources of high-speed video methods."
status: "auto-generated; brief scan note"
---
## Core Problem

Visual Deformation Measurement (VDM) aims to recover dense deformation fields by tracking
surface motion from camera observations.

## Core Method

Traditional image-based methods rely on minimal inter-frame motion to constrain the
correspondence search space, which limits their applicability to highly dynamic scenes or
necessitates high-speed cameras at the cost of prohibitive storage and computational
overhead.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event stream。自动分类理由：Official abstract/page confirms event-camera/DVS/event-stream
evidence; no clear SNN evidence.。
