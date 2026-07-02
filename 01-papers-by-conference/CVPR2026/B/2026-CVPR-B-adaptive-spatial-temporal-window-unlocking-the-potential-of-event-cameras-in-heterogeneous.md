---
title: "Adaptive Spatial-Temporal Window: Unlocking the Potential of Event Cameras in Heterogeneous Velocity Scenarios"
authors: ["Zhipeng Sui", "Haiqing Hao", "Weihua He", "Seng-Hong Lee", "Wenhui Wang"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Sui_Adaptive_Spatial-Temporal_Window_Unlocking_the_Potential_of_Event_Cameras_in_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Sui_Adaptive_Spatial-Temporal_Window_Unlocking_the_Potential_of_Event_Cameras_in_CVPR_2026_paper.html"
tags: []
abstract: "Most event-based algorithms typically split the event stream into fixed groups (e.g., fixed time or fixed count) for downstream processing, lacking adaptivity to scene dynamics. Several adaptive partitioning strategies have been proposed, but they are unable to cope well with heterogeneous velocity scenarios (HVS) involving both fast- and slow-moving objects. To address this issue, we propose Adaptive Spatial-Temporal Window (ASTW) strategy, which simultaneously achieves temporal adaptivity and spatial locality in event partitioning. Based on the principle of maximum entropy, we derive a patch-level time window determination criterion and efficiently implement it based on event density and vectorized calculations. Experiments on publicly available event-based object detection and tracking datasets demonstrate that ASTW significantly outperforms existing state-of-the-art partitioning strategies. We also construct HetVel, the first RGB-event dual-modality dataset for HVS, and further highlight the advantages of ASTW on this challenging benchmark. We believe that our ASTW strategy and the constructed HetVel dataset will advance the field of neuromorphic vision."
status: "auto-generated; brief scan note"
---
## Core Problem

Most event-based algorithms typically split the event stream into fixed groups (e.g., fixed
time or fixed count) for downstream processing, lacking adaptivity to scene dynamics.

## Core Method

Several adaptive partitioning strategies have been proposed, but they are unable to cope
well with heterogeneous velocity scenarios (HVS) involving both fast- and slow-moving
objects.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; event stream; rgb-event。自动分类理由：Official abstract/page confirms event-
camera/DVS/event-stream evidence; no clear SNN evidence.。
