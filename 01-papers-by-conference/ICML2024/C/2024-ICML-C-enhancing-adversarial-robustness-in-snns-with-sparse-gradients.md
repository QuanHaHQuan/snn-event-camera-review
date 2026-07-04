---
title: "Enhancing Adversarial Robustness in SNNs with Sparse Gradients"
authors: ["Yujia Liu, Tong Bu, Jianhao Ding, Zecheng Hao, Tiejun Huang, Zhaofei Yu"]
conference: "ICML"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24f/liu24f.pdf"
official_page: "https://proceedings.mlr.press/v235/liu24f.html"
tags: []
abstract: "Spiking Neural Networks (SNNs) have attracted great attention for their energy-efficient operations and biologically inspired structures, offering potential advantages over Artificial Neural Networks (ANNs) in terms of energy efficiency and interpretability. Nonetheless, similar to ANNs, the robustness of SNNs remains a challenge, especially when facing adversarial attacks. Existing techniques, whether adapted from ANNs or specifically designed for SNNs, exhibit limitations in training SNNs or defending against strong attacks. In this paper, we propose a novel approach to enhance the robustness of SNNs through gradient sparsity regularization. We observe that SNNs exhibit greater resilience to random perturbations compared to adversarial perturbations, even at larger scales. Motivated by this, we aim to narrow the gap between SNNs under adversarial and random perturbations, thereby improving their overall robustness. To achieve this, we theoretically prove that this performance gap is upper bounded by the gradient sparsity of the probability associated with the true label concerning the input image, laying the groundwork for a practical strategy to train robust SNNs by regularizing the gradient sparsity. We validate the effectiveness of our approach through extensive experiments on both image-based and event-based datasets. The results demonstrate notable improvements in the robustness of SNNs. Our work highlights the importance of gradient sparsity in SNNs and its role in enhancing robustness."
status: "auto-generated; brief scan note"
---
## Core Problem

Spiking Neural Networks (SNNs) have attracted great attention for their energy-efficient
operations and biologically inspired structures, offering potential advantages over
Artificial Neural Networks (ANNs) in terms of energy efficiency and interpretability.

## Core Method

Nonetheless, similar to ANNs, the robustness of SNNs remains a challenge, especially when
facing adversarial attacks.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：SNNs。自动分类理由：Official abstract/page strictly confirms SNN/spiking neural computation;
no clear event-camera/DVS evidence found.。 备注：strict two-stage screening; official
abstract/page inspected; main conference; needs human verification。
