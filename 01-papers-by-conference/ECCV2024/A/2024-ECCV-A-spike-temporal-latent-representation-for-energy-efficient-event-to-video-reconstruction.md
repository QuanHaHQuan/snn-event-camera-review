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

Event-to-Video (E2V) reconstruction is to recover grayscale video from the neuromorphic
event streams, and Spiking Neural Networks (SNNs) are the potential energy-efficient models
to solve the reconstruction problem.

## Core Method

Event voxels are an efficient representation for compressing event streams for E2V
reconstruction, but their temporal latent representation is rarely considered in SNN-based
reconstruction.

## Key Metrics and Findings

自动流程尚未深读 PDF，不能可靠提取完整指标、数据集、对比方法和数值结论；需要人工核验后补充。

## Personal Notes

检索命中关键词：event stream; neuromorphic event; event-to-video; spiking neural network; spike-
driven。自动分类理由：Official abstract/page confirms both event-camera/DVS/event-stream evidence
and SNN/spiking neural computation.。 该卡片用于优先阅读队列，引用前必须核对官方论文。

## Method Details

In this paper, we propose a spike-temporal latent representation (STLR) model for SNN-based
E2V reconstruction. The STLR solves the temporal latent coding of event voxels for video
frame reconstruction. It is composed of two cascaded SNNs: a) Spike-based Voxel Temporal
Encoder (SVT) and b) U-shape SNN Decoder. The SVT is a spike-driven spatial unfolding
network with a specially designed coding dynamic. It encodes the event voxel into the layer-
wise spiking features for latent coding, approximating the fixed point of the Iterative
Shrinkage-Thresholding Algorithm. Then, the U-shape SNN decoder reconstructs the video based
on the encoded spikes. Experimental results show that the STLR achieves comparable
performance to the popular SNNs on IJRR, HQF, and MVSEC, and significantly improves energy
efficiency. For example, the STLR achieves comparable performance under 13.20% parameters
and 3.33%~ 5.03% energy cost of the PA-EVSNN.

## Experimental Analysis

需要人工检查实验数据集、任务设置、baselines、消融、延迟、能耗与硬件条件，避免把摘要级表述当成最终结论。

## Related Work Connections

该论文应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认它真正处在 SNN 与事件相机交叉点。

## Survey-Usable Points

可作为交叉方向候选核心论文；最终可用观点需要在人工阅读全文后再写入综述草稿。
