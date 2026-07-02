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

The employment of the event-based synthetic aperture imaging (E-SAI) technique, which has the capability to capture high-frequency light intensity variations, has facilitated its extensive application on scene de-occlusion reconstruction tasks.

## Core Method

However, existing methods usually require prior information and have strict restriction of camera motion on SAI acquisition methods.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `pure event streams visual-event context; event-based synthetic aperture visual-event context; event stream with event-camera context; event-based with event-camera context; snns`，官方摘要/页面证据为 `Official abstract/page strictly confirms both event-camera/DVS/visual-event-sensor evidence and SNN/spiking neural computation.`。该卡片为草稿笔记，引用前必须核对官方论文。

## Method Details

摘要显示该论文同时触及事件相机/DVS/视觉事件数据与 SNN 或脉冲神经计算；更细的模型结构、编码方式和训练细节需要人工阅读全文确认。

## Experimental Analysis

需要人工检查实验任务、数据集、baselines、消融、延迟、能耗和硬件条件，避免把摘要级信息当作最终结论。

## Related Work Connections

应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认其在综述中的交叉位置。

## Survey-Usable Points

可作为 SNN 与事件相机交叉方向的候选核心论文；最终综述观点需在人工阅读全文后整理。
