---
title: "HPL-ESS: Hybrid Pseudo-Labeling for Unsupervised Event-based Semantic Segmentation"
authors: ["Linglin Jing", "Yiming Ding", "Yunpeng Gao", "Zhigang Wang", "Xu Yan", "Dong Wang", "Gerald Schaefer", "Hui Fang", "Bin Zhao", "Xuelong Li"]
conference: "CVPR"
year: 2024
level: "B"
category: "Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Jing_HPL-ESS_Hybrid_Pseudo-Labeling_for_Unsupervised_Event-based_Semantic_Segmentation_CVPR_2024_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Jing_HPL-ESS_Hybrid_Pseudo-Labeling_for_Unsupervised_Event-based_Semantic_Segmentation_CVPR_2024_paper.html"
tags: []
abstract: "Event-based semantic segmentation has gained popularity due to its capability to deal with scenarios under high-speed motion and extreme lighting conditions which cannot be addressed by conventional RGB cameras. Since it is hard to annotate event data previous approaches rely on event-to-image reconstruction to obtain pseudo labels for training. However this will inevitably introduce noise and learning from noisy pseudo labels especially when generated from a single source may reinforce the errors. This drawback is also called confirmation bias in pseudo-labeling. In this paper we propose a novel hybrid pseudo-labeling framework for unsupervised event-based semantic segmentation HPL-ESS to alleviate the influence of noisy pseudo labels. In particular we first employ a plain unsupervised domain adaptation framework as our baseline which can generate a set of pseudo labels through self-training. Then we incorporate offline event-to-image reconstruction into the framework and obtain another set of pseudo labels by predicting segmentation maps on the reconstructed images. A noisy label learning strategy is designed to mix the two sets of pseudo labels and enhance the quality. Moreover we propose a soft prototypical alignment module to further improve the consistency of target domain features. Extensive experiments show that our proposed method outperforms existing state-of-the-art methods by a large margin on the DSEC-Semantic dataset (+5.88% accuracy +10.32% mIoU) which even surpasses several supervised methods."
status: "auto-generated; brief scan note"
---
## Core Problem

Event-based semantic segmentation has gained popularity due to its capability to deal with
scenarios under high-speed motion and extreme lighting conditions which cannot be addressed
by conventional RGB cameras.

## Core Method

Since it is hard to annotate event data previous approaches rely on event-to-image
reconstruction to obtain pseudo labels for training.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：event; event-based。自动分类理由：Manual boundary check: official abstract confirms event-
based semantic segmentation and DSEC-Semantic event-camera data.。 备注：CVPR 2024 official CVF
page inspected under broad high-recall title workflow.。
