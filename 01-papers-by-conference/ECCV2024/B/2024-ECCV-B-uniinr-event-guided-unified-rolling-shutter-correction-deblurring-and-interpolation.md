---
title: "UniINR: Event-guided Unified Rolling Shutter Correction, Deblurring, and Interpolation"
authors: ["Yunfan Lu", "Guoqiang Liang", "Yusheng Wang", "LIN WANG", "Hui Xiong"]
conference: "ECCV"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01346.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/2483"
tags: []
abstract: "Video frames captured by rolling shutter (RS) cameras during fast camera movement frequently exhibit RS distortion and blur simultaneously. These RS frames can be modeled as a row-wise combination of global shutter (GS) frames within the exposure period. Naturally, recovering high-frame-rate GS sharp frames from an RS blur image must simultaneously consider RS correction, deblur, and frame interpolation. A naive way is to decompose the whole process into separate tasks and cascade existing methods; however, this results in cumulative errors and noticeable artifacts. Event cameras enjoy many advantages, \\eg, high temporal resolution, making them potential for our problem. To this end, we propose the \\textbf{first} and novel approach, named \\textbf{UniINR}, to recover arbitrary frame-rate sharp GS frames from an RS blur image and paired event data. Our key idea is unifying spatial-temporal implicit neural representation (INR) to directly map the position and time coordinates to RGB values to address the interlocking degradations in the image restoration process. Specifically, we introduce spatial-temporal implicit encoding (STE) to convert an RS blur image and events into a spatial-temporal representation (STR). To query a specific sharp frame (GS or RS), we embed the exposure time into STR and decode the embedded features pixel-by-pixel to recover a sharp frame. Our method features a lightweight model with only \\textbf{$0.379 M$} parameters, and it also enjoys high inference efficiency, achieving $2.83 ms/frame$ in $31 \\times$ frame interpolation of an RS blur frame. Extensive experiments show that our method significantly outperforms prior methods."
status: "auto-generated; brief scan note"
---

## Core Problem

Video frames captured by rolling shutter (RS) cameras during fast camera movement frequently exhibit RS distortion and blur simultaneously.

## Core Method

These RS frames can be modeled as a row-wise combination of global shutter (GS) frames within the exposure period.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
