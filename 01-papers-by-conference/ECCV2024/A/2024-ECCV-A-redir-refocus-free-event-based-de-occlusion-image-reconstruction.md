---
title: "REDIR: Refocus-free Event-based De-occlusion Image Reconstruction"
authors: ["Qi Guo", "Hailong Shi", "Huan Li", "Jinsheng Xiao", "Xingyu Gao"]
conference: "ECCV"
year: 2024
level: "A"
category: "SNN + Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/10433.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/2118"
tags: []
abstract: "The employment of the event-based synthetic aperture imaging (E-SAI) technique, which has the capability to capture high-frequency light intensity variations, has facilitated its extensive application on scene de-occlusion reconstruction tasks. However, existing methods usually require prior information and have strict restriction of camera motion on SAI acquisition methods. This paper proposes a novel end-to-end refocus-free variable E-SAI de-occlusion image reconstruction approach REDIR, which can align the global and local features of the variable event data and effectively achieve high-resolution imaging of pure event streams. To further improve the reconstruction of the occluded target, we propose a perceptual mask-gated connection module to interlink information between modules, and incorporate a spatial-temporal attention mechanism into the SNN block to enhance target extraction ability of the model. Through extensive experiments, our model achieves state-of-the-art reconstruction quality on the traditional E-SAI dataset without prior information, while verifying the effectiveness of the variable event data feature registration method on our newly introduced V-ESAI dataset, which obviates the reliance on prior knowledge and extends the applicability of SAI acquisition methods by incorporating focus changes, lens rotations, and non-uniform motion."
status: "auto-generated; needs human review"
---
## Core Problem

The employment of the event-based synthetic aperture imaging (E-SAI) technique, which has
the capability to capture high-frequency light intensity variations, has facilitated its
extensive application on scene de-occlusion reconstruction tasks.

## Core Method

However, existing methods usually require prior information and have strict restriction of
camera motion on SAI acquisition methods.

## Key Metrics and Findings

自动流程尚未深读 PDF，不能可靠提取完整指标、数据集、对比方法和数值结论；需要人工核验后补充。

## Personal Notes

检索命中关键词：event data; pure event streams; SNN block。自动分类理由：Official abstract confirms pure
event streams/event data and an SNN block for de-occlusion reconstruction.。
该卡片用于优先阅读队列，引用前必须核对官方论文。

## Method Details

This paper proposes a novel end-to-end refocus-free variable E-SAI de-occlusion image
reconstruction approach REDIR, which can align the global and local features of the variable
event data and effectively achieve high-resolution imaging of pure event streams. To further
improve the reconstruction of the occluded target, we propose a perceptual mask-gated
connection module to interlink information between modules, and incorporate a spatial-
temporal attention mechanism into the SNN block to enhance target extraction ability of the
model. Through extensive experiments, our model achieves state-of-the-art reconstruction
quality on the traditional E-SAI dataset without prior information, while verifying the
effectiveness of the variable event data feature registration method on our newly introduced
V-ESAI dataset, which obviates the reliance on prior knowledge and extends the applicability
of SAI acquisition methods by incorporating focus changes, lens rotations, and non-uniform
motion.

## Experimental Analysis

需要人工检查实验数据集、任务设置、baselines、消融、延迟、能耗与硬件条件，避免把摘要级表述当成最终结论。

## Related Work Connections

该论文应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认它真正处在 SNN 与事件相机交叉点。

## Survey-Usable Points

可作为交叉方向候选核心论文；最终可用观点需要在人工阅读全文后再写入综述草稿。
