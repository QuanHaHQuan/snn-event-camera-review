---
title: "Can we get the best of both Binary Neural Networks and Spiking Neural Networks for Efficient Computer Vision?"
authors: ["Gourav Datta, Zeyu Liu, Peter Beerel"]
conference: "ICLR"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://proceedings.iclr.cc/paper_files/paper/2024/file/ff521f7570d6ed23217ba5780753a1f7-Paper-Conference.pdf"
official_page: "https://proceedings.iclr.cc/paper_files/paper/2024/hash/ff521f7570d6ed23217ba5780753a1f7-Abstract-Conference.html"
tags: []
abstract: "Binary Neural networks (BNN) have emerged as an attractive computing paradigm for a wide range of low-power vision tasks. However, state-of-the-art (SOTA) BNNs do not yield any sparsity, and induce a significant number of non-binary operations. On the other hand, activation sparsity can be provided by spiking neural networks (SNN), that too have gained significant traction in recent times. Thanks to this sparsity, SNNs when implemented on neuromorphic hardware, have the potential to be significantly more power-efficient compared to traditional artifical neural networks (ANN). However, SNNs incur multiple time steps to achieve close to SOTA accuracy. Ironically, this increases latency and energy---costs that SNNs were proposed to reduce---and presents itself as a major hurdle in realizing SNNs’ theoretical gains in practice. This raises an intriguing question: Can we obtain SNN-like sparsity and BNN-like accuracy and enjoy the energy-efficiency benefits of both? To answer this question, in this paper, we present a training framework for sparse binary activation neural networks (BANN) using a novel variant of the Hoyer regularizer. We estimate the threshold of each BANN layer as the Hoyer extremum of a clipped version of its activation map, where the clipping value is trained using gradient descent with our Hoyer regularizer. This approach shifts the activation values away from the threshold, thereby mitigating the effect of noise that can otherwise degrade the BANN accuracy. Our approach outperforms existing BNNs, SNNs, and adder neural networks (that also avoid energy-expensive multiplication operations similar to BNNs and SNNs) in terms of the accuracy-FLOPs trade-off for complex image recognition tasks. Downstream experiments on object detection further demonstrate the efficacy of our approach. Lastly, we demonstrate the portability of our approach to SNNs with multiple time steps. Codes are publicly available here ."
status: "auto-generated; brief scan note"
---
## Core Problem

Binary Neural networks (BNN) have emerged as an attractive computing paradigm for a wide
range of low-power vision tasks.

## Core Method

However, state-of-the-art (SOTA) BNNs do not yield any sparsity, and induce a significant
number of non-binary operations.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural networks; spiking。自动分类理由：Manual boundary check: sparse binary
activation neural networks are compared with SNNs and portable to SNNs, but the paper is not
an event-camera method.。 备注：strict two-stage screening; official abstract/page inspected;
main conference; needs human verification。
