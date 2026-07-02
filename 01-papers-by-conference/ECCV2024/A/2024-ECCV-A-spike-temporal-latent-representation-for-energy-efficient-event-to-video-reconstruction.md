---
title: "Spike-Temporal Latent Representation for Energy-Efficient Event-to-Video Reconstruction"
authors: ["Jianxiong Tang", "Jian-Huang Lai", "Lingxiao Yang", "Xiaohua Xie"]
conference: "ECCV"
year: 2024
level: "A"
category: "SNN + Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05843.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/1446"
tags: []
abstract: "Event-to-Video (E2V) reconstruction is to recover grayscale video from the neuromorphic event streams, and Spiking Neural Networks (SNNs) are the potential energy-efficient models to solve the reconstruction problem. Event voxels are an efficient representation for compressing event streams for E2V reconstruction, but their temporal latent representation is rarely considered in SNN-based reconstruction. In this paper, we propose a spike-temporal latent representation (STLR) model for SNN-based E2V reconstruction. The STLR solves the temporal latent coding of event voxels for video frame reconstruction. It is composed of two cascaded SNNs: a) Spike-based Voxel Temporal Encoder (SVT) and b) U-shape SNN Decoder. The SVT is a spike-driven spatial unfolding network with a specially designed coding dynamic. It encodes the event voxel into the layer-wise spiking features for latent coding, approximating the fixed point of the Iterative Shrinkage-Thresholding Algorithm. Then, the U-shape SNN decoder reconstructs the video based on the encoded spikes. Experimental results show that the STLR achieves comparable performance to the popular SNNs on IJRR, HQF, and MVSEC, and significantly improves energy efficiency. For example, the STLR achieves comparable performance under 13.20% parameters and 3.33%~ 5.03% energy cost of the PA-EVSNN."
status: "auto-generated; needs human review"
---

## Core Problem

Event-to-Video (E2V) reconstruction is to recover grayscale video from the neuromorphic event streams, and Spiking Neural Networks (SNNs) are the potential energy-efficient models to solve the reconstruction problem.

## Core Method

Event voxels are an efficient representation for compressing event streams for E2V reconstruction, but their temporal latent representation is rarely considered in SNN-based reconstruction.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event-to-video visual-event context; event voxel visual-event context; event voxels visual-event context; neuromorphic event streams visual-event context; event stream with event-camera context; spiking neural networks; snns; spike-driven`，官方摘要/页面证据为 `Official abstract/page strictly confirms both event-camera/DVS/visual-event-sensor evidence and SNN/spiking neural computation.`。该卡片为草稿笔记，引用前必须核对官方论文。

## Method Details

摘要显示该论文同时触及事件相机/DVS/视觉事件数据与 SNN 或脉冲神经计算；更细的模型结构、编码方式和训练细节需要人工阅读全文确认。

## Experimental Analysis

需要人工检查实验任务、数据集、baselines、消融、延迟、能耗和硬件条件，避免把摘要级信息当作最终结论。

## Related Work Connections

应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认其在综述中的交叉位置。

## Survey-Usable Points

可作为 SNN 与事件相机交叉方向的候选核心论文；最终综述观点需在人工阅读全文后整理。
