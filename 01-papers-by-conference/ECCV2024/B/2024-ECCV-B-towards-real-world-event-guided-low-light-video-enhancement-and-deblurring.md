---
title: "Towards Real-world Event-guided Low-light Video Enhancement and Deblurring"
authors: ["Taewoo Kim", "Jaeseok Jeong", "Hoonhee Cho", "Yuhwan Jeong", "KUK-JIN YOON"]
conference: "ECCV"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01982.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/651"
tags: []
abstract: "In low-light conditions, capturing videos with frame-based cameras often requires long exposure times, resulting in motion blur and reduced visibility. While frame-based motion deblurring and low-light enhancement have been studied, they still pose significant challenges. Event cameras have emerged as a promising solution for improving image quality in low-light environments and addressing motion blur. They provide two key advantages: capturing scene details well even in low light due to their high dynamic range, and effectively capturing motion information during long exposures due to their high temporal resolution. Despite efforts to tackle low-light enhancement and motion deblurring using event cameras separately, previous work has not addressed both simultaneously. To explore the joint task, we first establish real-world datasets for event-guided low-light enhancement and deblurring using a hybrid camera system based on beam splitters. Subsequently, we introduce an end-to-end framework to effectively handle these tasks. Our framework incorporates a module to efficiently leverage temporal information from events and frames. Furthermore, we propose a module to utilize cross-modal feature information to employ a low-pass filter for noise suppression while enhancing the main structural information. Our proposed method significantly outperforms existing approaches in addressing the joint task. Our project pages are available at https://github.com/intelpro/ELEDNet."
status: "auto-generated; brief scan note"
---

## Core Problem

In low-light conditions, capturing videos with frame-based cameras often requires long exposure times, resulting in motion blur and reduced visibility.

## Core Method

While frame-based motion deblurring and low-light enhancement have been studied, they still pose significant challenges.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
