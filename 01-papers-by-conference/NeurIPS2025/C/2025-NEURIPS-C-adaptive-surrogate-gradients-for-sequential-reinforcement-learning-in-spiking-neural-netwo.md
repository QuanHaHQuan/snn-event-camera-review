---
title: "Adaptive Surrogate Gradients for Sequential Reinforcement Learning in Spiking Neural Networks"
authors: ["Korneel Van den Berghe, Stein Stroobants, Vijay Janapa Reddi, Guido de Croon"]
conference: "NeurIPS"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/d94b46ec30adee2bbb134f813fc9dde0-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/d94b46ec30adee2bbb134f813fc9dde0-Abstract-Conference.html"
tags: []
abstract: "Neuromorphic computing systems are set to revolutionize energy-constrained robotics by achieving orders-of-magnitude efficiency gains, while enabling native temporal processing. Spiking Neural Networks (SNNs) represent a promising algorithmic approach for these systems, yet their application to complex control tasks faces two critical challenges: (1) the non-differentiable nature of spiking neurons necessitates surrogate gradients with unclear optimization properties, and (2) the stateful dynamics of SNNs require training on sequences, which in reinforcement learning (RL) is hindered by limited sequence lengths during early training, preventing the network from bridging its warm-up period. We address these challenges by systematically analyzing surrogate gradient slope settings, showing that shallower slopes increase gradient magnitude in deeper layers but reduce alignment with true gradients. In supervised learning, we find no clear preference for fixed or scheduled slopes. The effect is much more pronounced in RL settings, where shallower slopes or scheduled slopes lead to a $\\times2.1$ improvement in both training and final deployed performance. Next, we propose a novel training approach that leverages a privileged guiding policy to bootstrap the learning process, while still exploiting online environment interactions with the spiking policy. Combining our method with an adaptive slope schedule for a real-world drone position control task, we achieve an average return of 400 points, substantially outperforming prior techniques, including Behavioral Cloning and TD3BC, which achieve at most –200 points under the same conditions. This work advances both the theoretical understanding of surrogate gradient learning in SNNs and practical training methodologies for neuromorphic controllers demonstrated in real-world robotic systems."
status: "auto-generated; brief scan note"
---

## Core Problem

Neuromorphic computing systems are set to revolutionize energy-constrained robotics by achieving orders-of-magnitude efficiency gains, while enabling native temporal processing.

## Core Method

Spiking Neural Networks (SNNs) represent a promising algorithmic approach for these systems, yet their application to complex control tasks faces two critical challenges: (1) the non-differentiable nature of spiking neurons necessitates surrogate gradients with unclear optimization properties, and (2) the stateful dynamics of SNNs require training on sequences, which in reinforcement learning (RL) is hindered by limited sequence lengths during early training, preventing the network from bridging its warm-up period.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `spiking neural networks; snns; spiking neurons; surrogate gradients`，官方摘要/页面证据为 `Official abstract/page strictly confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
