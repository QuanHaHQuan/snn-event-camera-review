---
title: "Bilateral Event Mining and Complementary for Event Stream Super-Resolution"
authors: ["Zhilin Huang", "Quanmin Liang", "Yijie Yu", "Chujun Qin", "Xiawu Zheng", "Kai Huang", "Zikun Zhou", "Wenming Yang"]
conference: "CVPR"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Huang_Bilateral_Event_Mining_and_Complementary_for_Event_Stream_Super-Resolution_CVPR_2024_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Huang_Bilateral_Event_Mining_and_Complementary_for_Event_Stream_Super-Resolution_CVPR_2024_paper.html"
tags: []
abstract: "Event Stream Super-Resolution (ESR) aims to address the challenge of insufficient spatial resolution in event streams which holds great significance for the application of event cameras in complex scenarios. Previous works for ESR often process positive and negative events in a mixed paradigm. This paradigm limits their ability to effectively model the unique characteristics of each event and mutually refine each other by considering their correlations. In this paper we propose a bilateral event mining and complementary network (BMCNet) to fully leverage the potential of each event and capture the shared information to complement each other simultaneously. Specifically we resort to a two-stream network to accomplish comprehensive mining of each type of events individually. To facilitate the exchange of information between two streams we propose a bilateral information exchange (BIE) module. This module is layer-wisely embedded between two streams enabling the effective propagation of hierarchical global information while alleviating the impact of invalid information brought by inherent characteristics of events. The experimental results demonstrate that our approach outperforms the previous state-of-the-art methods in ESR achieving performance improvements of over 11% on both real and synthetic datasets. Moreover our method significantly enhances the performance of event-based downstream tasks such as object recognition and video reconstruction. Our code is available at https://github.com/Lqm26/BMCNet-ESR."
status: "auto-generated; brief scan note"
---
## Core Problem

Event Stream Super-Resolution (ESR) aims to address the challenge of insufficient spatial
resolution in event streams which holds great significance for the application of event
cameras in complex scenarios.

## Core Method

Previous works for ESR often process positive and negative events in a mixed paradigm.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event stream; event。自动分类理由：Official abstract/page strictly confirms event-
camera/DVS/visual-event-stream evidence; no clear SNN evidence found.。 备注：CVPR 2024 official
CVF page inspected under broad high-recall title workflow.。
