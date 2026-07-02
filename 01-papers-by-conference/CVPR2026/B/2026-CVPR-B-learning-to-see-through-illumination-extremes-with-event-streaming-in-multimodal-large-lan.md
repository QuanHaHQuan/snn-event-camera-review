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

Multimodal Large Language Models (MLLMs) perform strong vision-language reasoning under
standard conditions but fail in extreme illumination, where RGB inputs lose irrevocable
structure and semantics.

## Core Method

We propose Event-MLLM, an event-enhanced model that performs all-light visual reasoning by
dynamically fusing event streams with RGB frames.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event stream。自动分类理由：Official abstract/page confirms event-camera/DVS/event-stream
evidence; no clear SNN evidence.。
