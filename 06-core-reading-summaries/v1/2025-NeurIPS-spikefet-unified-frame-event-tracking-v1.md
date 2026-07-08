---
title: "Fully Spiking Neural Networks for Unified Frame-Event Object Tracking"
authors: ["Jingjun Yang", "Liangwei Fan", "Jinpu Zhang", "Xiangkai Lian", "Hui Shen", "Dewen Hu"]
year: 2025
venue: "NeurIPS"
level: "A"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/NeurIPS2025/A/2025-NEURIPS-A-fully-spiking-neural-networks-for-unified-frame-event-object-tracking.md"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/af752cfbdcc6fd3e4cd0eea9f1ad0fab-Abstract-Conference.html"
pdf_link: "https://arxiv.org/pdf/2505.20834"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["SNN", "event camera", "tracking", "Transformer"]
---

# Summary V1｜Fully Spiking Neural Networks for Unified Frame-Event Object Tracking

## 1. One-sentence Summary

本文围绕 Fully Spiking Neural Networks for Unified Frame-Event Object Tracking，基于论文 PDF 中的方法与实验描述，总结其在 SNN/event camera 交叉方向 的主要问题、方法和证据。

## 2. Research Problem

The integration of image and event streams offers a promising approach for achieving robust visual object tracking in complex environments. However, current fusion methods achieve high performance at the cost of significant computational overhead and struggle to efficiently extract the sparse, asynchronous information from event streams, failing to leverage the energy-efficient advantages of event-driven spiking paradigms.

这对本项目的意义在于：它提供了 直接的 SNN + event camera 方法证据，可用于后续 survey 中建立问题边界和比较基线。

## 3. Background and Motivation

However, current fusion methods achieve high performance at the cost of significant computational overhead and struggle to efficiently extract the sparse, asynchronous information from event streams, failing to leverage the energy-efficient advantages of event-driven spiking paradigms. To address this challenge, we propose the first fully Spiking Frame-Event Tracking framework called SpikeFET.

从 survey 角度看，需要关注它是否真正利用 event data 的 asynchronous / sparse / high-temporal-resolution 特性，或是否主要是把已有视觉/SNN 模型迁移到相关任务上。

## 4. Method Overview

To address this challenge, we propose the first fully Spiking Frame-Event Tracking framework called SpikeFET. This network achieves synergistic integration of convolutional local feature extraction and Transformer-based global modeling within the spiking paradigm, effectively fusing frame and event data.

整体 pipeline、输入输出和模块边界已经在 PDF 中出现；本 V1 先记录高层结构，V2 阶段应逐图核对 architecture figure 和 method equations。

## 5. Technical Details

### Event Representation / Input

论文涉及 event streams / event camera data；具体表示形式请在 V2 阶段核对 PDF method section。

### Spiking Neuron / SNN Module

PDF/abstract 明确涉及 SNN/spiking/spike-driven design；具体 neuron model、surrogate gradient 或 spike conversion 需要在 V2 中逐式核验。

### Network Architecture

To address this challenge, we propose the first fully Spiking Frame-Event Tracking framework called SpikeFET. This network achieves synergistic integration of convolutional local feature extraction and Transformer-based global modeling within the spiking paradigm, effectively fusing frame and event data.

### Training Strategy

训练设置、pretraining/fine-tuning、augmentation 和 optimization 细节已在 PDF 中出现，但本轮只做自动抽取，精确超参数需要人工核验。

### Loss Function

若论文包含专门 loss 或 objective，本 V1 只记录其作用；公式符号和权重请在 V2 阶段结合 PDF 原文核对。

### Inference Process

推理过程需要结合模型 pipeline、event aggregation window 和硬件/软件环境进一步核验。

## 6. Experiments

PDF 自动抽取到以下实验相关证据线索：

- streams, failing to leverage the energy-efficient advantages of event-driven spiking
- demonstrate that the proposed framework achieves superior tracking accuracy over
- and ultra-low energy consumption advantages in event stream processing through their bio-inspired
- tracking, it suffers from compromised energy efficiency. Notably, SDTrack [16] implements a fully
- bias introduced by padding [17, 18] in the convolution module on tracking accuracy, we propose a
- higher AUC score on the FE108 [8] dataset compared to the state-of-the-art SDSTrack [19], while
- enhancing the tracking accuracy and stability of the model.
- computational power consumption and performance and parameters, as shown in Fig. 1.

本 V1 只引用这些可从 PDF 抽取到的实验线索；完整数值、baseline 顺序和显著性比较需要人工在 V2 中逐表核对。

## 7. Main Contributions

1. 提出或系统化研究了与 `Fully Spiking Neural Networks for Unified Frame-Event Object Tracking` 对应的核心方法/任务设定。
2. PDF 摘要和方法部分给出了主要模块设计，涉及 SNN, event camera, tracking, Transformer。
3. PDF 实验部分报告了数据集、指标或 ablation 线索，可作为后续人工深读的入口。
4. 对 survey 的价值在于补充 A: SNN + Event Camera core paper 这一类证据，而不是直接作为未经核验的最终结论。

## 8. Limitations and Risks

- 本 V1 是自动 PDF-based 摘要，尚未逐式核验全部公式和表格数值。
- 若论文报告 efficiency / energy / latency，需要确认其是理论 operation count、GPU 测量还是 neuromorphic hardware 实测。
- 若论文属于 B/C 类，应避免在 survey 中把它误写成 SNN + Event Camera core method。
- 部分实验结论可能依赖特定 dataset split、pretraining 设置或 implementation details，需要人工复核。

## 9. Relation to SNN for Event Cameras

分类：A: SNN + Event Camera core paper。

理由：reading plan 将该论文标为 level A；PDF 内容显示其关键词和任务与 `SNN, event camera, tracking, Transformer` 相关。最终归类仍应在 V2 阶段结合全文细读修正。

## 10. Relation to Survey Taxonomy

- Event-based tracking
- SNN architectures for event cameras
- Open challenges

## 11. Key Terms and Concepts

- SNN: 论文中相关的关键概念，V2 阶段需要结合原文定义进一步精读。
- event camera: 论文中相关的关键概念，V2 阶段需要结合原文定义进一步精读。
- Spiking Neural Network: 论文中相关的关键概念，V2 阶段需要结合原文定义进一步精读。
- Transformer: 论文中相关的关键概念，V2 阶段需要结合原文定义进一步精读。

## 12. Questions for Human Deep Reading

1. PDF 中 method section 对核心模块的数学定义是什么？
2. 实验使用的数据集、划分和评价指标是否与 baseline 完全一致？
3. 主要提升来自 representation、architecture、training strategy 还是 post-processing？
4. 效率、能耗或 latency 结论是理论估算还是硬件实测？
5. 该论文对 SNN for Event Cameras survey 的贡献应归入方法、数据集、训练还是挑战部分？

## 13. Evidence Notes

- Local PDF parsed successfully: 2025-NeurIPS-fully-spiking-neural-networks-for-unified-frame-event-object-tracking.pdf, 25 pages.
- PDF headings observed: Fully Spiking Neural Networks for Unified; National University of Defense Technology; Abstract; 1 Introduction; HRCEUTrack; OSTrack; CEUTrack; Model Size.
- PDF key experiment/evidence lines include datasets/metrics/table mentions listed in Section 6.

## 14. Draft Survey-Usable Sentences

Draft material: `Fully Spiking Neural Networks for Unified Frame-Event Object Tracking` can be cited cautiously as A: SNN + Event Camera core paper evidence after its quantitative tables and method details are manually verified.

Draft material: The paper is useful for mapping how SNN, event camera, tracking relates to event-camera/SNN survey taxonomy, but V2 should refine the exact claim boundaries.
