---
title: "QP-SNN: Quantized and Pruned Spiking Neural Networks"
authors: ["Wenjie Wei", "Malu Zhang", "Zijian Zhou", "Ammar Belatreche", "Yimeng Shan", "Yu Liang", "Honglin Cao", "Jieyuan Zhang", "Yang Yang"]
year: 2025
venue: "ICLR"
level: "C"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/ICLR2025/C/2025-ICLR-C-qp-snn-quantized-and-pruned-spiking-neural-networks.md"
official_page: "https://proceedings.iclr.cc/paper_files/paper/2025/hash/f04aef8513b788a69229cede8c8cb5a8-Abstract-Conference.html"
pdf_link: "https://proceedings.iclr.cc/paper_files/paper/2025/file/f04aef8513b788a69229cede8c8cb5a8-Paper-Conference.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["SNN", "event camera", "quantization", "pruning"]
---

# Summary V1｜QP-SNN: Quantized and Pruned Spiking Neural Networks

## 1. One-sentence Summary

本文围绕 QP-SNN: Quantized and Pruned Spiking Neural Networks，基于论文 PDF 中的方法与实验描述，总结其在 SNN 方法背景方向 的主要问题、方法和证据。

## 2. Research Problem

Brain-inspired Spiking Neural Networks (SNNs) leverage sparse spikes to encode information and operate in an asynchronous event-driven manner, offering a highly energy-efficient paradigm for machine intelligence. However, the current SNN community focuses primarily on performance improvement by developing large-scale models, which limits the applicability of SNNs in resource-limited edge devices.

这对本项目的意义在于：它提供了 通用 SNN 架构/训练/效率背景，可用于后续 survey 中建立问题边界和比较基线。

## 3. Background and Motivation

However, the current SNN community focuses primarily on performance improvement by developing large-scale models, which limits the applicability of SNNs in resource-limited edge devices. In this paper, we propose a hardware-friendly and lightweight SNN, aimed at effectively deploying high-performance SNN in resource-limited scenarios.

从 survey 角度看，需要关注它是否真正利用 event data 的 asynchronous / sparse / high-temporal-resolution 特性，或是否主要是把已有视觉/SNN 模型迁移到相关任务上。

## 4. Method Overview

In this paper, we propose a hardware-friendly and lightweight SNN, aimed at effectively deploying high-performance SNN in resource-limited scenarios. Specifically, we first develop a baseline model that integrates uniform quantization and structured pruning, called QP-SNN baseline.

整体 pipeline、输入输出和模块边界已经在 PDF 中出现；本 V1 先记录高层结构，V2 阶段应逐图核对 architecture figure 和 method equations。

## 5. Technical Details

### Event Representation / Input

论文涉及 event streams / event camera data；具体表示形式请在 V2 阶段核对 PDF method section。

### Spiking Neuron / SNN Module

PDF/abstract 明确涉及 SNN/spiking/spike-driven design；具体 neuron model、surrogate gradient 或 spike conversion 需要在 V2 中逐式核验。

### Network Architecture

In this paper, we propose a hardware-friendly and lightweight SNN, aimed at effectively deploying high-performance SNN in resource-limited scenarios. Specifically, we first develop a baseline model that integrates uniform quantization and structured pruning, called QP-SNN baseline.

### Training Strategy

训练设置、pretraining/fine-tuning、augmentation 和 optimization 细节已在 PDF 中出现，但本轮只做自动抽取，精确超参数需要人工核验。

### Loss Function

若论文包含专门 loss 或 objective，本 V1 只记录其作用；公式符号和权重请在 V2 阶段结合 PDF 原文核对。

### Inference Process

推理过程需要结合模型 pipeline、event aggregation window 和硬件/软件环境进一步核验。

## 6. Experiments

PDF 自动抽取到以下实验相关证据线索：

- a highly energy-efficient paradigm for machine intelligence. However, the current
- energy efficiency potential of SNNs. Despite these advantages, the application scenarios and perfor-
- the cost of large model parameters, high memory consumption, and increased computational com-
- plexity (Yan et al. (2024); Liu et al. (2024); Cao et al. (2025)). This undermines the inherent energy
- Existing methods to improve SNN energy efficiency primarily fall into two categories: (1) reducing
- the precision of parameter representations and (2) reducing redundant parameters within the model.
- Pruning is one of the effective methods for reducing redundant parameters in a model, which reduces
- (2021)) adopt unstructured pruning. Secondly, despite significant energy efficiency, these studies

本 V1 只引用这些可从 PDF 抽取到的实验线索；完整数值、baseline 顺序和显著性比较需要人工在 V2 中逐表核对。

## 7. Main Contributions

1. 提出或系统化研究了与 `QP-SNN: Quantized and Pruned Spiking Neural Networks` 对应的核心方法/任务设定。
2. PDF 摘要和方法部分给出了主要模块设计，涉及 SNN, event camera, quantization, pruning。
3. PDF 实验部分报告了数据集、指标或 ablation 线索，可作为后续人工深读的入口。
4. 对 survey 的价值在于补充 C: SNN side background 这一类证据，而不是直接作为未经核验的最终结论。

## 8. Limitations and Risks

- 本 V1 是自动 PDF-based 摘要，尚未逐式核验全部公式和表格数值。
- 若论文报告 efficiency / energy / latency，需要确认其是理论 operation count、GPU 测量还是 neuromorphic hardware 实测。
- 若论文属于 B/C 类，应避免在 survey 中把它误写成 SNN + Event Camera core method。
- 部分实验结论可能依赖特定 dataset split、pretraining 设置或 implementation details，需要人工复核。

## 9. Relation to SNN for Event Cameras

分类：C: SNN side background。

理由：reading plan 将该论文标为 level C；PDF 内容显示其关键词和任务与 `SNN, event camera, quantization, pruning` 相关。最终归类仍应在 V2 阶段结合全文细读修正。

## 10. Relation to Survey Taxonomy

- SNN training methods
- Efficiency, latency, and energy
- Open challenges

## 11. Key Terms and Concepts

- SNN: 论文中相关的关键概念，V2 阶段需要结合原文定义进一步精读。
- Spiking Neural Network: 论文中相关的关键概念，V2 阶段需要结合原文定义进一步精读。
- LIF: 论文中相关的关键概念，V2 阶段需要结合原文定义进一步精读。

## 12. Questions for Human Deep Reading

1. PDF 中 method section 对核心模块的数学定义是什么？
2. 实验使用的数据集、划分和评价指标是否与 baseline 完全一致？
3. 主要提升来自 representation、architecture、training strategy 还是 post-processing？
4. 效率、能耗或 latency 结论是理论估算还是硬件实测？
5. 该论文对 SNN for Event Cameras survey 的贡献应归入方法、数据集、训练还是挑战部分？
6. 该 SNN 方法是否真的在 event-camera dataset 上验证，还是只作为通用 SNN 背景？

## 13. Evidence Notes

- Local PDF parsed successfully: 2025-ICLR-qp-snn-quantized-and-pruned-spiking-neural-networks.pdf, 26 pages.
- PDF headings observed: NEURAL NETWORKS; ABSTRACT; 1 I NTRODUCTION; Bit width for weight; 2 R ELATED WORK; 3 Q UANTIZED AND PRUNED SNN BASELINE; 4 M ETHOD; Wasted.
- PDF key experiment/evidence lines include datasets/metrics/table mentions listed in Section 6.

## 14. Draft Survey-Usable Sentences

Draft material: `QP-SNN: Quantized and Pruned Spiking Neural Networks` can be cited cautiously as C: SNN side background evidence after its quantitative tables and method details are manually verified.

Draft material: The paper is useful for mapping how SNN, event camera, quantization relates to event-camera/SNN survey taxonomy, but V2 should refine the exact claim boundaries.
