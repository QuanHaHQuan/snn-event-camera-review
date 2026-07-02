---
title: "Towards Persistence: Learning Topological Constraints for Event-based Small Object Detection"
authors: ["Shiman He", "Nuo Chen", "Xinyi Ying", "Yihang Luo", "Yangsi Shi", "Zaiping Lin", "Miao Li"]
conference: "CVPR"
year: 2026
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/He_Towards_Persistence_Learning_Topological_Constraints_for_Event-based_Small_Object_Detection_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/He_Towards_Persistence_Learning_Topological_Constraints_for_Event-based_Small_Object_Detection_CVPR_2026_paper.html"
tags: []
abstract: "Small object detection (SOD) plays a vital role in applications such as anti-UAV tasks, yet conventional image-based methods struggle in high-speed scenarios due to the limited frame rate. Event cameras offer a promising alternative by capturing spatiotemporal event streams with microsecond-level temporal resolution. To address the inherent sparsity of small objects in event data, existing methods typically formulate the detection task as semantic segmentation on spatiotemporal point clouds to leverage long-term contextual information. However, these methods often fail to enforce effective spatiotemporal consistency constraints, resulting in fragmented object trajectories. To mitigate these problems, we propose a topology-constrained sparse convolutional network (SpTopoNet), which models the topological structure of moving object trajectories in event point clouds. Our network comprises two key components: a Topology Learning Module (TLM) that discriminates local structures to separate genuine targets from noise, and a Spatial Consistency Module (SCM) that captures long-range spatiotemporal dependencies to enhance trajectory continuity. Additionally, we introduce an event topology-aware loss function that leverages topological correlations to guide the network to maintain structural integrity of target event patterns.Experiments on the benchmark dataset demonstrate the superiority of our method in both detection performance and trajectory completeness."
status: "auto-generated; brief scan note"
---
## Core Problem

Small object detection (SOD) plays a vital role in applications such as anti-UAV tasks, yet
conventional image-based methods struggle in high-speed scenarios due to the limited frame
rate.

## Core Method

Event cameras offer a promising alternative by capturing spatiotemporal event streams with
microsecond-level temporal resolution.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event camera; event stream; event data。自动分类理由：Official abstract/page confirms event-
camera/DVS/event-stream evidence; no clear SNN evidence.。
