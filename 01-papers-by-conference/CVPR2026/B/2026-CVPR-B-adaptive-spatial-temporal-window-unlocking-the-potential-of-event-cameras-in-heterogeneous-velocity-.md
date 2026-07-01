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

固定时间窗或固定事件数的切分策略难以适应快慢目标并存的异速场景。

## Core Method

提出自适应空间-时间窗口，通过最大熵准则与事件密度估计确定局部时间窗。

## Key Metrics and Findings

摘要强调该策略同时兼顾时间自适应与空间局部性。

## Personal Notes

可作为事件流切分和前处理章节的背景工作。

