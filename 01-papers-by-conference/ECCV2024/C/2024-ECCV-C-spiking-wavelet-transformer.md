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

Spiking neural networks (SNNs) offer an energy-efficient alternative to conventional deep
learning by mimicking the event-driven processing of the brain.

## Core Method

Incorporating the Transformers with SNNs has shown promise for accuracy, yet it is
incompetent to capture high-frequency patterns like moving edge and pixel-level brightness
changes due to their reliance on global self-attention operations.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking official cross-check。自动分类理由：Official abstract confirms Spiking Wavelet
Transformer / SNN; no clear event-camera/DVS evidence.。
