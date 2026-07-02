---
title: "P-SPIKESSM: HARNESSING PROBABILISTIC SPIKING STATE SPACE MODELS FOR LONG-RANGE DEPENDENCY TASKS"
authors: ["Malyaban Bal", "Abhronil Sengupta"]
conference: "ICLR"
year: 2025
level: "C"
category: "SNN"
pdf_link: "https://proceedings.iclr.cc/paper_files/paper/2025/file/b75ce884441c983f7357a312ffa02a3c-Paper-Conference.pdf"
official_page: "https://proceedings.iclr.cc/paper_files/paper/2025/hash/b75ce884441c983f7357a312ffa02a3c-Abstract-Conference.html"
tags: []
abstract: "Spiking neural networks (SNNs) are posited as a computationally efficient and biologically plausible alternative to conventional neural architectures, with their core computational framework primarily using the leaky integrate-and-fire (LIF) neuron model. However, the limited hidden state representation of LIF neurons, characterized by a scalar membrane potential, and sequential spike generation process, poses challenges for effectively developing scalable spiking models to address long-range dependencies in sequence learning tasks. In this study, we develop a scalable probabilistic spiking learning framework for long-range dependency tasks leveraging the fundamentals of state space models. Unlike LIF neurons that rely on the deterministic Heaviside function for a sequential process of spike generation, we introduce a SpikeSampler layer that samples spikes stochastically based on an SSM-based neuronal model while allowing parallel computations. To address non-differentiability of the spiking operation and enable effective training, we also propose a surrogate function tailored for the stochastic nature of the SpikeSampler layer. To enhance inter-neuron communication, we introduce the SpikeMixer block, which integrates spikes from neuron populations in each layer. This is followed by a ClampFuse layer, incorporating a residual connection to capture complex dependencies, enabling scalability of the model. Our models attain state-of-the-art performance among SNN models across diverse long-range dependency tasks, encompassing the Long Range Arena benchmark, permuted sequential MNIST, and the Speech Command dataset and demonstrate sparse spiking pattern highlighting its computational efficiency."
status: "auto-generated; brief scan note"
---

## Core Problem

Spiking neural networks (SNNs) are posited as a computationally efficient and biologically plausible alternative to conventional neural architectures, with their core computational framework primarily using the leaky integrate-and-fire (LIF) neuron model.

## Core Method

However, the limited hidden state representation of LIF neurons, characterized by a scalar membrane potential, and sequential spike generation process, poses challenges for effectively developing scalable spiking models to address long-range dependencies in sequence learning tasks.

## Key Metrics and Findings

自动流程未深读 PDF；具体指标、数据集、对比方法和数值结论需要人工核验。

## Personal Notes

检索命中关键词：spiking。自动分类理由：Official abstract/page strictly confirms SNN/spiking neural computation; no clear event-camera/DVS evidence found.。该卡片为草稿笔记，引用前必须核对官方论文。
