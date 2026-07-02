---
title: "EvFocus: Learning to Reconstruct Sharp Images from Out-of-Focus Event Streams"
authors: ["Lin Zhu", "Xiantao Ma", "Xiao Wang", "Lizhi Wang", "Hua Huang"]
conference: "ICML"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25n/zhu25n.pdf"
official_page: "https://proceedings.mlr.press/v267/zhu25n.html"
tags: []
abstract: "Event cameras are innovative sensors that capture brightness changes as asynchronous events rather than traditional intensity frames. These cameras offer substantial advantages over conventional cameras, including high temporal resolution, high dynamic range, and the elimination of motion blur. However, defocus blur, a common image quality degradation resulting from out-of-focus lenses, complicates the challenge of event-based imaging. Due to the unique imaging mechanism of event cameras, existing focusing algorithms struggle to operate efficiently on sparse event data. In this work, we propose EvFocus, a novel architecture designed to reconstruct sharp images from defocus event streams for the first time. Our work includes the development of an event-based out-of-focus camera model and a simulator to generate realistic defocus event streams for robust training and testing. EvDefous integrates a temporal information encoder, a blur-aware two-branch decoder, and a reconstruction and re-defocus module to effectively learn and correct defocus blur. Extensive experiments on both simulated and real-world datasets demonstrate that EvFocus outperforms existing methods across varying lighting conditions and blur sizes, proving its robustness and practical applicability in event-based defocus imaging."
status: "auto-generated; brief scan note"
---

## Core Problem

Event cameras are innovative sensors that capture brightness changes as asynchronous events rather than traditional intensity frames.

## Core Method

These cameras offer substantial advantages over conventional cameras, including high temporal resolution, high dynamic range, and the elimination of motion blur.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

检索命中关键词：event streams; event。自动分类理由：Official abstract/page confirms event-camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。该卡片为草稿笔记，引用前必须核对官方论文。
