---
title: "A generalized neural tangent kernel for surrogate gradient learning"
authors: ["Luke Eilers, Raoul-Martin Memmesheimer, Sven Goedeke"]
conference: "NeurIPS"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://papers.nips.cc/paper_files/paper/2024/file/10f1737aa6347ccc555ac068e1b45523-Paper-Conference.pdf"
official_page: "https://papers.nips.cc/paper_files/paper/2024/hash/10f1737aa6347ccc555ac068e1b45523-Abstract-Conference.html"
tags: []
abstract: "State-of-the-art neural network training methods depend on the gradient of the network function. Therefore, they cannot be applied to networks whose activation functions do not have useful derivatives, such as binary and discrete-time spiking neural networks. To overcome this problem, the activation function's derivative is commonly substituted with a surrogate derivative, giving rise to surrogate gradient learning (SGL). This method works well in practice but lacks theoretical foundation.The neural tangent kernel (NTK) has proven successful in the analysis of gradient descent. Here, we provide a generalization of the NTK, which we call the surrogate gradient NTK, that enables the analysis of SGL. First, we study a naive extension of the NTK to activation functions with jumps, demonstrating that gradient descent for such activation functions is also ill-posed in the infinite-width limit. To address this problem, we generalize the NTK to gradient descent with surrogate derivatives, i.e., SGL. We carefully define this generalization and expand the existing key theorems on the NTK with mathematical rigor. Further, we illustrate our findings with numerical experiments. Finally, we numerically compare SGL in networks with sign activation function and finite width to kernel regression with the surrogate gradient NTK; the results confirm that the surrogate gradient NTK provides a good characterization of SGL."
status: "auto-generated; brief scan note"
---
## Core Problem

State-of-the-art neural network training methods depend on the gradient of the network
function.

## Core Method

Therefore, they cannot be applied to networks whose activation functions do not have useful
derivatives, such as binary and discrete-time spiking neural networks.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：surrogate gradient。自动分类理由：Official abstract/page strictly confirms SNN/spiking
neural computation; no clear event-camera/DVS evidence found.。 备注：strict two-stage rescan;
official abstract/page inspected; Track: Main Conference Track; needs human verification.。
