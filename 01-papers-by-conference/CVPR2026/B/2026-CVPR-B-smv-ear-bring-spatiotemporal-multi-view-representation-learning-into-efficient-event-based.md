---
title: "SMV-EAR: Bring Spatiotemporal Multi-View Representation Learning into Efficient Event-Based Action Recognition"
authors: ["Rui Fan", "Weidong Hao", "Juntao Guan", "Lai Rui", "Tong Wu", "Fanhong Zeng", "Lin Gu"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Fan_SMV-EAR_Bring_Spatiotemporal_Multi-View_Representation_Learning_into_Efficient_Event-Based_Action_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Fan_SMV-EAR_Bring_Spatiotemporal_Multi-View_Representation_Learning_into_Efficient_Event-Based_Action_CVPR_2026_paper.html"
tags: []
abstract: "Event cameras action recognition (EAR) offers compelling privacy-protecting and efficiency advantages, where temporal motion dynamics is of great importance. Existing spatiotemporal multi-view representation learning (SMVRL) methods for event-based object recognition (EOR) offer promising solutions by projecting H-W-T events alone spatial axis H and W, yet are limited by its translation-variant spatial binning representation and naive early concatenation fusion architecture. This paper reexamines the key SMVRL design stages for EAR and propose: (i) a principled spatiotemporal multi-view representation through translation-invariant dense conversion of sparse events, (ii) a dual-branch, dynamic fusion architecture that models sample-wise complementarity between motion features from different views, and (iii) a bio-inspired temporal warping augmentation that mimics speed variability of real-world human actions. On three challenging EAR datasets of HARDVS, DailyDVS-200 and THU-EACT-50-CHL, we show +7.0%, +10.7%, and +10.2% Top-1 accuracy gains over existing SMVRL EOR method with surprising 30.1% reduced parameters and 35.7% lower computations, establishing our framework as a novel and powerful EAR paradigm. Code are avaliable in https://github.com/Fineshawray/SMV-EAR."
status: "auto-generated; brief scan note"
---

## Core Problem

Event cameras action recognition (EAR) offers compelling privacy-protecting and efficiency advantages, where temporal motion dynamics is of great importance.

## Core Method

Existing spatiotemporal multi-view representation learning (SMVRL) methods for event-based object recognition (EOR) offer promising solutions by projecting H-W-T events alone spatial axis H and W, yet are limited by its translation-variant spatial binning representation and naive early concatenation fusion architecture.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

严格两阶段复扫：标题宽召回命中 `event cameras; event camera visual-event context; event cameras visual-event context; dvs visual-event context; event-based object visual-event context; event-based action visual-event context; event-based with event-camera context`，官方摘要/页面证据为 `Official abstract/page strictly confirms event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.`。该卡片为草稿笔记，引用前必须核对官方论文。
