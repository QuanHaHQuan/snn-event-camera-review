---
title: "Temporal Residual Guided Diffusion Framework for Event-Driven Video Reconstruction"
authors: ["Lin Zhu", "Yunlong Zheng", "Yijun Zhang", "Xiao Wang", "Lizhi Wang", "Hua Huang"]
conference: "ECCV"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05690.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/1241"
tags: []
abstract: "Event-based video reconstruction has garnered increasing attention due to its advantages, such as high dynamic range and rapid motion capture capabilities. However, current methods often prioritize the extraction of temporal information from continuous event flow, leading to an overemphasis on low-frequency texture features in the scene, resulting in over-smoothing and blurry artifacts. Addressing this challenge necessitates the integration of conditional information, encompassing temporal features, low-frequency texture, and high-frequency events, to guide the Denoising Diffusion Probabilistic Model (DDPM) in producing accurate and natural outputs. To tackle this issue, we introduce a novel approach, the Temporal Residual Guided Diffusion Framework, which effectively leverages both temporal and frequency-based event priors. Our framework incorporates three key conditioning modules: a pre-trained low-frequency intensity estimation module, a temporal recurrent encoder module, and an attention-based high-frequency prior enhancement module. In order to capture temporal scene variations from the events at the current moment, we employ a temporal-domain residual image as the target for the diffusion model. Through the combination of these three conditioning paths and the temporal residual framework, our framework excels in reconstructing high-quality videos from event flow, mitigating issues such as artifacts and over-smoothing commonly observed in previous approaches. Extensive experiments conducted on multiple benchmark datasets validate the superior performance of our framework compared to prior event-based reconstruction methods. Our code will be released upon acceptance."
status: "auto-generated; brief scan note"
---

## Core Problem

Event-based video reconstruction has garnered increasing attention due to its advantages, such as high dynamic range and rapid motion capture capabilities.

## Core Method

However, current methods often prioritize the extraction of temporal information from continuous event flow, leading to an overemphasis on low-frequency texture features in the scene, resulting in over-smoothing and blurry artifacts.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event flow visual-event context; event-based video visual-event context; event-based reconstruction visual-event context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
