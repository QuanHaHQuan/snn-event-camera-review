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

Recovering the camera motion and scene geometry from visual data is a fundamental problem in
the field of computer vision.

## Core Method

Its success in standard vision is attributed to the maturity of feature extraction, data
association and multi-view geometry.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event-based official cross-check。自动分类理由：Official abstract confirms neuromorphic
event-based cameras and raw event data; no clear SNN evidence.。
