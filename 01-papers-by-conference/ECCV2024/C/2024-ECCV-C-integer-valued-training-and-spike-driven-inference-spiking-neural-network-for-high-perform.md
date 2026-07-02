---
title: "Integer-Valued Training and Spike-driven Inference Spiking Neural Network for High-performance and Energy-efficient Object Detection"
authors: ["Xinhao Luo", "Man Yao", "Yuhong Chou", "Bo Xu", "Guoqi Li"]
conference: "ECCV"
year: 2024
level: "C"
category: "SNN"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/04704.pdf"
official_page: "https://eccv.ecva.net/virtual/2024/poster/150"
tags: []
abstract: "Brain-inspired Spiking Neural Networks (SNNs) have bio-plausibility and low-power advantages over Artificial Neural Networks (ANNs). Applications of SNNs are currently limited to simple classification tasks because of their poor performance. In this work, we focus on bridging the performance gap between ANNs and SNNs on object detection. Our design revolves around network architecture and spiking neuron. First, the overly complex module design causes spike degradation when the YOLO series is converted to the corresponding spiking version. We design a SpikeYOLO architecture to solve this problem by simplifying the vanilla YOLO and incorporating meta SNN blocks. Second, object detection is more sensitive to quantization errors in the conversion of membrane potentials into binary spikes by spiking neurons. To address this challenge, we design a new spiking neuron that activates Integer values during training while maintaining spike-driven by extending virtual timestep during inference. The proposed method is validated on both static and neuromorphic object detection datasets. On the static COCO dataset, we obtain 66.2% mAP@50 and 48.9% mAP@50:95, which is +15.0% and +18.7% higher than the prior state-of-the-art SNN, respectively. On the neuromorphic Gen1 dataset, we achieve 67.2% mAP@50, which is +8.2% and +2.5% greater than the existing best SNN model and ANN with equivalent architecture, respectively, and the energy efficiency is improved by 5.7 times."
status: "auto-generated; brief scan note"
---
## Core Problem

Brain-inspired Spiking Neural Networks (SNNs) have bio-plausibility and low-power advantages
over Artificial Neural Networks (ANNs).

## Core Method

Applications of SNNs are currently limited to simple classification tasks because of their
poor performance.

## Key Metrics and Findings

尚未深读 PDF，指标、数据集和定量结果需要人工核验。

## Personal Notes

检索命中关键词：spiking neural network。自动分类理由：Official abstract confirms SNN object detection; no
clear event-camera/DVS evidence.。
