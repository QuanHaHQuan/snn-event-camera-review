---
title: "Rethinking Spiking Self-Attention Mechanism: Implementing a-XNOR Similarity Calculation in Spiking Transformers"
authors: ["Yichen Xiao", "Shuai Wang", "Dehao Zhang", "Wenjie Wei", "Yimeng Shan", "Xiaoli Liu", "Yulin Jiang", "Malu Zhang"]
conference: "CVPR"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Xiao_Rethinking_Spiking_Self-Attention_Mechanism_Implementing_a-XNOR_Similarity_Calculation_in_Spiking_CVPR_2025_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Xiao_Rethinking_Spiking_Self-Attention_Mechanism_Implementing_a-XNOR_Similarity_Calculation_in_Spiking_CVPR_2025_paper.html"
tags: []
abstract: "Transformers significantly raise the performance limits across various tasks, spurring research into integrating them into spiking neural networks. However, a notable performance gap remains between existing spiking Transformers and their artificial neural network counterparts. Here, we first analyze the cause of this gap and attribute it to the dot product's ineffectiveness in measuring similarity between spiking queries and keys, due to numerous non-spiking events. To address this, we propose a novel a-XNOR similarity measure tailored for spike trains. It redefines the correlation between non-spike pairs as a specific value a, effectively overcoming the limitations of dot-product similarity. Furthermore, considering the sparse nature of spike trains where spikes carry more information than non-spikes, the a-XNOR similarity correspondingly highlights the distinct importance of spikes over non-spikes. Extensive experiments demonstrate that a-XNOR similarity significantly improves performance across different spiking Transformer architectures on various static and neuromorphic datasets, further revealing the potential of spiking Transformers."
status: "auto-generated; brief scan note"
---
## Core Problem

Transformers significantly raise the performance limits across various tasks, spurring
research into integrating them into spiking neural networks.

## Core Method

However, a notable performance gap remains between existing spiking Transformers and their
artificial neural network counterparts.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking transformers; spiking。自动分类理由：Official abstract/page strictly confirms
SNN/spiking neural computation; no clear event-camera/DVS evidence found.。 备注：CVPR 2025
official CVF page inspected under broad high-recall title workflow.。
