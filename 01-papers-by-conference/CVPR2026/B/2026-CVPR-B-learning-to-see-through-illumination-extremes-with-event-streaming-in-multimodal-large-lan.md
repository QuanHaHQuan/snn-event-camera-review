---
title: "Learning to See through Illumination Extremes with Event Streaming in Multimodal Large Language Models"
authors: ["Baoheng Zhang", "Jiahui Liu", "Gui Zhao", "Weizhou Zhang", "Yixuan Ma", "Jun Jiang", "Yingxian Chen", "Wilton W.T. Fok", "Xiaojuan Qi", "Hayden Kwok-Hay So"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Learning_to_See_through_Illumination_Extremes_with_Event_Streaming_in_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Learning_to_See_through_Illumination_Extremes_with_Event_Streaming_in_CVPR_2026_paper.html"
tags: []
abstract: "Multimodal Large Language Models (MLLMs) perform strong vision-language reasoning under standard conditions but fail in extreme illumination, where RGB inputs lose irrevocable structure and semantics. We propose Event-MLLM, an event-enhanced model that performs all-light visual reasoning by dynamically fusing event streams with RGB frames. Two key components drive our approach: an Illumination Indicator -- a learnable signal derived from a DINOv2 branch that represents exposure degradation and adaptively modulates event-RGB fusion -- and an Illumination Correction Loss that aligns fused features with non-degraded (normal-light) semantics in the latent space, compensating for information lost in extreme lighting. We curate the first multi-illumination event-instruction corpus for MLLMs, with 2,241 event-RGB samples (around 6 QA pairs each) across diverse scenes and 17 brightness rates (0.05x - 20x), plus an instruct-following benchmark for reasoning, counting, and fine-grained recognition under extreme lighting. Experiments show that Event-MLLM markedly outperforms general-purpose, illumination-adaptive, and event-only baselines, setting a new state of the art in robust multimodal perception and reasoning under challenging illumination."
status: "auto-generated; brief scan note"
---

## Core Problem

Multimodal Large Language Models (MLLMs) perform strong vision-language reasoning under standard conditions but fail in extreme illumination, where RGB inputs lose irrevocable structure and semantics.

## Core Method

We propose Event-MLLM, an event-enhanced model that performs all-light visual reasoning by dynamically fusing event streams with RGB frames.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event-rgb visual-event context; event stream with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
