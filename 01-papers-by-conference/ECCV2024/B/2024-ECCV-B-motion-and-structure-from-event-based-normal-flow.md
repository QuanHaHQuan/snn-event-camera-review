---
title: "Motion and Structure from Event-based Normal Flow"
authors: ["Zhongyang Ren", "Bangyan Liao", "Delei Kong", "Jinghang Li", "Peidong Liu", "Laurent Kneip", "Guillermo Gallego", "Yi Zhou"]
conference: "ECCV"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07261.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/2480"
tags: []
abstract: "Recovering the camera motion and scene geometry from visual data is a fundamental problem in the field of computer vision. Its success in standard vision is attributed to the maturity of feature extraction, data association and multi-view geometry. The recent emergence of neuromorphic event-based cameras places great demands on approaches that use raw event data as input to solve this fundamental problem. Existing state-of-the-art solutions typically infer implicitly data association by iteratively reversing the event data generation process. However, the nonlinear nature of these methods limits their applicability in real-time tasks, and the constant-motion assumption leads to unstable results under agile motion. To this end, we rethink the problem formulation in a way that aligns better with the differential working principle of event cameras. We show that the event-based normal flow can be used, via the proposed geometric error term, as an alternative to the full flow in solving a family of geometric problems that involve instantaneous first-order kinematics and scene geometry. Furthermore, we develop a fast linear solver and a continuous-time nonlinear solver on top of the proposed geometric error term. Experiments on both synthetic and real data demonstrate the superiority of our linear solver in terms of accuracy and efficiency, and indicate its complementary feature as an initialization method for existing nonlinear solvers. Besides, our continuous-time non-linear solver exhibits exceptional capability in accommodating sudden variations in motion since it does not rely on the constant-motion assumption."
status: "auto-generated; brief scan note"
---

## Core Problem

Recovering the camera motion and scene geometry from visual data is a fundamental problem in the field of computer vision.

## Core Method

Its success in standard vision is attributed to the maturity of feature extraction, data association and multi-view geometry.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event-based cameras; event camera visual-event context; event cameras visual-event context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
