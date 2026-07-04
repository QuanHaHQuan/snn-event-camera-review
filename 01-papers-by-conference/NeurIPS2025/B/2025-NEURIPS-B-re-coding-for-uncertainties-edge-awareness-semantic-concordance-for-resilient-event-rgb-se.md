---
title: "Re-coding for Uncertainties: Edge-awareness Semantic Concordance for Resilient Event-RGB Segmentation"
authors: ["Nan Bao, Yifan Zhao, Lin Zhu, Jia Li"]
conference: "NeurIPS"
year: 2025
level: "B"
category: "Event Camera"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/hash/92c020da2740ec2ace29e8e7d69b4483-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/92c020da2740ec2ace29e8e7d69b4483-Abstract-Conference.html"
tags: []
abstract: "Semantic segmentation has achieved great success in ideal conditions. However, when facing extreme conditions (e.g., insufficient light, fierce camera motion), most existing methods suffer from significant information loss of RGB, severely damaging segmentation results. Several researches exploit the high-speed and high-dynamic event modality as a complement, but event and RGB are naturally heterogeneous, which leads to feature-level mismatch and inferior optimization of existing multi-modality methods. Different from these researches, we delve into the edge secret of both modalities for resilient fusion and propose a novel Edge-awareness Semantic Concordance framework to unify the multi-modality heterogeneous features with latent edge cues. In this framework, we first propose Edge-awareness Latent Re-coding, which obtains uncertainty indicators while realigning event-RGB features into unified semantic space guided by re-coded distribution, and transfers event-RGB distributions into re-coded features by utilizing a pre-established edge dictionary as clues. We then propose Re-coded Consolidation and Uncertainty Optimization, which utilize re-coded edge features and uncertainty indicators to solve the heterogeneous event-RGB fusion issues under extreme conditions. We establish two synthetic and one real-world event-RGB semantic segmentation datasets for extreme scenario comparisons. Experimental results show that our method outperforms the state-of-the-art by a 2.55% mIoU on our proposed DERS-XS, and possesses superior resilience under spatial occlusion. Our code and datasets are publicly available at https://github.com/iCVTEAM/ESC."
status: "auto-generated; brief scan note"
---
## Core Problem

Semantic segmentation has achieved great success in ideal conditions.

## Core Method

However, when facing extreme conditions (e.g., insufficient light, fierce camera motion),
most existing methods suffer from significant information loss of RGB, severely damaging
segmentation results.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event-rgb visual-event context。自动分类理由：Official abstract/page strictly confirms
event-camera/DVS/visual-event-sensor evidence; no clear SNN evidence found.。 备注：strict two-
stage rescan; official abstract/page inspected; needs human verification; Track: Main
Conference Track。
