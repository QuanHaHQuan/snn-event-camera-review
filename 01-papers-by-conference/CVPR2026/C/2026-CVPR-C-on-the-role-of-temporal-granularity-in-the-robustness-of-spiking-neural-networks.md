---
title: "On the Role of Temporal Granularity in the Robustness of Spiking Neural Networks"
authors: ["Mengting Xu", "Shi Gu", "Peng Lin", "De Ma", "Huajin Tang", "Qian Zheng", "Gang Pan"]
conference: "CVPR"
year: 2026
level: "C"
category: "SNN"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_On_the_Role_of_Temporal_Granularity_in_the_Robustness_of_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Xu_On_the_Role_of_Temporal_Granularity_in_the_Robustness_of_CVPR_2026_paper.html"
tags: []
abstract: "As the third generation of neural networks, Spiking Neural Networks (SNNs) have demonstrated remarkable potential across diverse applications owing to their unique temporal dynamics. In recent years, analyzing the robustness of SNNs from a temporal perspective has become an emerging research focus. However, most existing works examine only the overall temporal behavior of SNNs, typically applying adversarial attacks that rely on time-averaged gradients. In this study, we revisit SNN robustness through the lens of temporal granularity, emphasizing the distinct behaviors that occur at individual time steps. We first introduce a Temporal Granularity Attack (TG-Attack), which selectively perturbs gradients at specific time steps. This approach enables a finer-grained evaluation of SNN robustness across time and demonstrates higher attack success rates than traditional gradient-averaging methods. Furthermore, we theoretically show that the robustness of SNNs at a given time step is determined by the Hessian of the input-output gradient at that step, which we define as Temporal Sensitivity (TS). By calculating the Temporal Sensitivity Value (TSV) for each time step, robustness can be effectively estimated without generating adversarial examples. Finally, we propose a Temporal Granularity Regularization (TG-Reg) term that constrains the TSV across all time steps, thereby improving the model's overall robustness. Experimental evaluations confirm that our framework consistently outperforms existing state-of-the-art methods."
status: "auto-generated; brief scan note"
---

## Core Problem

论文聚焦 SNN 在时间维度上的鲁棒性评估，核心问题是现有方法只看整体时间行为，忽略了逐时刻差异。

## Core Method

提出 Temporal Granularity Attack、Temporal Sensitivity 与 Temporal Granularity
Regularization，从更细时间粒度分析和约束 SNN 鲁棒性。

## Key Metrics and Findings

摘要声称该框架比时间平均梯度攻击更强，并能在不生成对抗样本时估计鲁棒性。

## Personal Notes

可作为 SNN 鲁棒性章节的背景论文，和事件相机方向没有直接交叉。

