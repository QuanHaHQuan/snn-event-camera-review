---
title: "Spiking Wavelet Transformer"
authors: ["Yuetong Fang", "Ziqing Wang", "Lingfeng Zhang", "Jiahang Cao", "Honglei Chen", "Renjing Xu"]
conference: "ECCV"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/09680.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/2545"
tags: []
abstract: "Spiking neural networks (SNNs) offer an energy-efficient alternative to conventional deep learning by mimicking the event-driven processing of the brain. Incorporating the Transformers with SNNs has shown promise for accuracy, yet it is incompetent to capture high-frequency patterns like moving edge and pixel-level brightness changes due to their reliance on global self-attention operations. Porting frequency representations in SNN is challenging yet crucial for event-driven vision. To address this issue, we propose the Spiking Wavelet Transformer (SWformer), an attention-free architecture that effectively learns comprehensive spatial-frequency features in a spike-driven manner by leveraging the sparse wavelet transform. The critical component is a Frequency-aware Spiking Token Mixer (FSTM) with three branches: 1) spiking wavelet learner for spatial-frequency domain learning, 2) convolution-based learner for spatial feature extraction, and 3) spiking pointwise convolution for cross-channel information aggregation. We also adopt negative spike dynamics to strengthen the frequency representation further. This enables the SWformer to outperform vanilla spiking Transformers in capturing high-frequency visual components, as evidenced by our empirical results. Experiments on both static and neuromorphic datasets demonstrate SWformer's effectiveness in capturing spatial-frequency patterns in a multiplication-free, event-driven fashion, outperforming state-of-the-art SNNs. SWformer achieves an over 50 reduction in energy consumption, a 21.1 reduction in parameter count, and a 2.40 performance improvement on the ImageNet dataset compared to vanilla Spiking Transformers."
status: "auto-generated; brief scan note"
---

## Core Problem

Spiking neural networks (SNNs) offer an energy-efficient alternative to conventional deep learning by mimicking the event-driven processing of the brain.

## Core Method

Incorporating the Transformers with SNNs has shown promise for accuracy, yet it is incompetent to capture high-frequency patterns like moving edge and pixel-level brightness changes due to their reliance on global self-attention operations.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `brightness change visual-event context; spiking neural networks; snns; spiking transformers; spike-driven`，官方摘要/页面证据为 `Official abstract/page strictly confirms both event-camera/DVS/visual-event-sensor evidence and SNN/spiking neural computation.`。该卡片为草稿笔记，引用前必须核对官方论文。

## Method Details

摘要显示该论文同时触及事件相机/DVS/视觉事件数据与 SNN 或脉冲神经计算；更细的模型结构、编码方式和训练细节需要人工阅读全文确认。

## Experimental Analysis

需要人工检查实验任务、数据集、baselines、消融、延迟、能耗和硬件条件，避免把摘要级信息当作最终结论。

## Related Work Connections

应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认其在综述中的交叉位置。

## Survey-Usable Points

可作为 SNN 与事件相机交叉方向的候选核心论文；最终综述观点需在人工阅读全文后整理。
