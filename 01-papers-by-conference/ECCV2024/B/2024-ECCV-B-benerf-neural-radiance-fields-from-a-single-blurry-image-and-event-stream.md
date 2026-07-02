---
title: "BeNeRF:Neural Radiance Fields from a Single Blurry Image and Event Stream"
authors: ["Wenpu Li", "Pian Wan", "Peng Wang", "Jinghang Li", "Yi Zhou", "Peidong Liu"]
conference: "ECCV"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/04596.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/553"
tags: []
abstract: "Neural implicit representation of visual scenes has attracted a lot of attention in recent research of computer vision and graphics. Most prior methods focus on how to reconstruct 3D scene representation from a set of images. In this work, we demonstrate the possibility to recover the neural radiance fields (NeRF) from a single blurry image and its corresponding event stream. We model the camera motion with a cubic B-Spline in SE(3) space. Both the blurry image and the brightness change within a time interval, can then be synthesized from the 3D scene representation given the 6-DoF poses interpolated from the cubic B-Spline. Our method can jointly learn both the implicit neural scene representation and recover the camera motion by minimizing the differences between the synthesized data and the real measurements without pre-computed camera poses from COLMAP. We evaluate the proposed method with both synthetic and real datasets. The experimental results demonstrate that we are able to render view-consistent latent sharp images from the learned NeRF and bring a blurry image alive in high quality."
status: "auto-generated; brief scan note"
---

## Core Problem

Neural implicit representation of visual scenes has attracted a lot of attention in recent research of computer vision and graphics.

## Core Method

Most prior methods focus on how to reconstruct 3D scene representation from a set of images.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `brightness change visual-event context; event stream with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
