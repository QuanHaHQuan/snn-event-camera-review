---
title: "Event-based Video Super-Resolution via State Space Models"
authors: ["Zeyu Xiao", "Xinchao Wang"]
conference: "CVPR"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Xiao_Event-based_Video_Super-Resolution_via_State_Space_Models_CVPR_2025_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Xiao_Event-based_Video_Super-Resolution_via_State_Space_Models_CVPR_2025_paper.html"
tags: []
abstract: "Exploiting temporal correlations is crucial for video super-resolution (VSR). Recent approaches enhance this by incorporating event cameras. In this paper, we introduce MamEVSR, a Mamba-based network for event-based VSR that leverages the selective state space model, Mamba. MamEVSR stands out by offering global receptive field coverage with linear computational complexity, thus addressing the limitations of convolutional neural networks and Transformers. The key components of MamEVSR include: (1) The interleaved Mamba (iMamba) block, which interleaves tokens from adjacent frames and applies multidirectional selective state space modeling, enabling efficient feature fusion and propagation across bi-directional frames while maintaining linear complexity. (2) The crossmodality Mamba (cMamba) block facilitates further interaction and aggregation between event information and the output from the iMamba block. The cMamba block can leverage complementary spatio-temporal information from both modalities and allows MamEVSR to capture finermotion details. Experimental results show that the proposed MamEVSR achieves superior performance on various datasets quantitatively and qualitatively."
status: "auto-generated; brief scan note"
---
## Core Problem

Exploiting temporal correlations is crucial for video super-resolution (VSR).

## Core Method

Recent approaches enhance this by incorporating event cameras.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event; event-based。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：CVPR 2025 official
CVF page inspected under broad high-recall title workflow.。
