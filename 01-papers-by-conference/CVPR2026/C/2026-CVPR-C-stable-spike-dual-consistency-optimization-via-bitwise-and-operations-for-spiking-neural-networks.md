---
title: "Stable Spike: Dual Consistency Optimization via Bitwise AND Operations for Spiking Neural Networks"
authors: ["Yongqi Ding", "Kunshan Yang", "Linze Li", "Yiyang Zhang", "Mengmeng Jing", "Lin Zuo"]
conference: "CVPR"
year: 2026
level: "C"
category: "SNN"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Ding_Stable_Spike_Dual_Consistency_Optimization_via_Bitwise_AND_Operations_for_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Ding_Stable_Spike_Dual_Consistency_Optimization_via_Bitwise_AND_Operations_for_CVPR_2026_paper.html"
tags: []
abstract: "Although the temporal spike dynamics of spiking neural networks (SNNs) enable low-power temporal capture capabilities, they also incur inherent inconsistencies that severely compromise representation. In this paper, we perform dual consistency optimization via Stable Spike to mitigate this problem, thereby improving the recognition performance of SNNs. With the hardware-friendly \"AND\" bit operation, we efficiently decouple the stable spike skeleton from the multi-timestep spike maps, which captures critical semantics and reduces the inconsistency from variable noise spikes. Enforcing the unstable spike maps to converge to the stable spike skeleton significantly improves the inherent consistency across timesteps. Furthermore, we inject amplitude-aware spike noise into the stable spike skeleton to diversify the representations while preserving consistent semantics. The SNN is encouraged to produce perturbation-consistent predictions, thereby contributing to generalization. Extensive experiments across multiple architectures and datasets validate the effectiveness and versatility of our method. In particular, our method significantly advances neuromorphic object recognition under ultra-low latency, improving accuracy by up to 8.33%. This will help unlock the full power consumption and speed potential of SNNs."
status: "auto-generated; brief scan note"
---

## Core Problem

SNN 的时间脉冲不一致会削弱表征稳定性。

## Core Method

通过 Stable Spike 的双一致性优化与位级 AND 运算，将稳定脉冲骨架和多时刻脉冲图分离。

## Key Metrics and Findings

摘要称该策略能提升识别性能并降低不一致噪声。

## Personal Notes

适合放在 SNN 稳定性与训练策略章节。

