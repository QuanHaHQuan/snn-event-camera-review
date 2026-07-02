---
title: "Reconstructing Spiking Neural Networks Using a Single Neuron with Autapses"
authors: ["Wuque Cai", "Hongze Sun", "Quan Tang", "Shifeng Mao", "Zhenxing Wang", "Jiayi He", "Duo Chen", "Dezhong Yao", "Daqing Guo"]
conference: "CVPR"
year: 2026
level: "C"
category: "SNN"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Cai_Reconstructing_Spiking_Neural_Networks_Using_a_Single_Neuron_with_Autapses_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Cai_Reconstructing_Spiking_Neural_Networks_Using_a_Single_Neuron_with_Autapses_CVPR_2026_paper.html"
tags: []
abstract: "Spiking neural networks (SNNs) are promising for neuromorphic computing, but high-performing models still rely on dense multilayer architectures with substantial communication and state-storage costs. Inspired by autapses, we propose TDA-SNN, a framework that reconstructs SNN architectures using a single leaky integrate-and-fire neuron with time-delayed autapses and a prototype-learning-based training strategy. By reorganizing internal temporal states, TDA-SNN can realize reservoir, multilayer perceptron, and convolution-like spiking architectures within a unified framework. Experiments on sequential, event-based, and image benchmarks show competitive performance in reservoir and MLP settings, while convolutional results reveal a clear space--time trade-off. Compared with standard SNNs, TDA-SNN greatly reduces neuron count and state memory while increasing per-neuron information capacity, at the cost of additional temporal latency in extreme single-neuron settings. These findings highlight the potential of temporally multiplexed single-neuron models as compact computational units for brain-inspired computing."
status: "auto-generated; brief scan note"
---
## Core Problem

Spiking neural networks (SNNs) are promising for neuromorphic computing, but high-performing
models still rely on dense multilayer architectures with substantial communication and
state-storage costs.

## Core Method

Inspired by autapses, we propose TDA-SNN, a framework that reconstructs SNN architectures
using a single leaky integrate-and-fire neuron with time-delayed autapses and a prototype-
learning-based training strategy.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural network; LIF。自动分类理由：Official abstract/page confirms SNN/spiking
neural computation; no clear event-camera/DVS evidence.。
