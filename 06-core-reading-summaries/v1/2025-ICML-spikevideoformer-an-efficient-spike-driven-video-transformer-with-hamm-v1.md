---
title: "SpikeVideoFormer: An Efficient Spike-Driven Video Transformer with Hamming Attention and $\\mathcalO(T)$ Complexity"
authors: ["Shihao Zou", "Qingfeng Li", "Wei Ji", "Jingjing Li", "Yongkui Yang", "Guoqi Li", "Chao Dong"]
year: 2025
venue: "ICML"
level: "C"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/ICML2025/C/2025-ICML-C-spikevideoformer-an-efficient-spike-driven-video-transformer-with-hamming-attention-and-ma.md"
official_page: "https://proceedings.mlr.press/v267/zou25b.html"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v267/main/assets/zou25b/zou25b.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["SNN", "tracking", "Transformer"]
---

# Summary V1｜SpikeVideoFormer: An Efficient Spike-Driven Video Transformer with Hamming Attention and $\\mathcalO(T)$ Complexity

## 1. One-sentence Summary

本文围绕 SpikeVideoFormer: An Efficient Spike-Driven Video Transformer with Hamming Attention and $\\mathcalO(T)$ Complexity，基于论文 PDF 中的方法与实验描述，总结其在 SNN 方法背景方向 的主要问题、方法和证据。

## 2. Research Problem

Spiking Neural Networks (SNNs) have shown competitive performance to Artificial Neural Networks (ANNs) in various vision tasks, while offering superior energy efficiency. However, existing SNN-based Transformers primarily focus on single-image tasks, emphasizing spatial features while not effectively leveraging SNNs’ efficiency in video-based vision tasks.

这对本项目的意义在于：它提供了 通用 SNN 架构/训练/效率背景，可用于后续 survey 中建立问题边界和比较基线。

## 3. Background and Motivation

However, existing SNN-based Transformers primarily focus on single-image tasks, emphasizing spatial features while not effectively leveraging SNNs’ efficiency in video-based vision tasks. In this paper, we introduce SpikeVideoFormer, an efficient spike-driven video Transformer, featuring linear temporal complexity $\\mathcal{O}(T)$.

从 survey 角度看，需要关注它是否真正利用 event data 的 asynchronous / sparse / high-temporal-resolution 特性，或是否主要是把已有视觉/SNN 模型迁移到相关任务上。

## 4. Method Overview

In this paper, we introduce SpikeVideoFormer, an efficient spike-driven video Transformer, featuring linear temporal complexity $\\mathcal{O}(T)$. Specifically, we design a spike-driven Hamming attention (SDHA) which provides a theoretically guided adaptation from traditional real-valued attention to spike-driven attention.

整体 pipeline、输入输出和模块边界已经在 PDF 中出现；本 V1 先记录高层结构，V2 阶段应逐图核对 architecture figure 和 method equations。

## 5. Technical Details

### Event Representation / Input

论文不以 event camera 输入为核心，主要作为 SNN side background。

### Spiking Neuron / SNN Module

PDF/abstract 明确涉及 SNN/spiking/spike-driven design；具体 neuron model、surrogate gradient 或 spike conversion 需要在 V2 中逐式核验。

### Network Architecture

In this paper, we introduce SpikeVideoFormer, an efficient spike-driven video Transformer, featuring linear temporal complexity $\\mathcal{O}(T)$. Specifically, we design a spike-driven Hamming attention (SDHA) which provides a theoretically guided adaptation from traditional real-valued attention to spike-driven attention.

### Training Strategy

训练设置、pretraining/fine-tuning、augmentation 和 optimization 细节已在 PDF 中出现，但本轮只做自动抽取，精确超参数需要人工核验。

### Loss Function

若论文包含专门 loss 或 objective，本 V1 只记录其作用；公式符号和权重请在 V2 阶段结合 PDF 原文核对。

### Inference Process

推理过程需要结合模型 pipeline、event aggregation window 和硬件/软件环境进一步核验。

## 6. Experiments

PDF 自动抽取到以下实验相关证据线索：

- SNNs have emerged as an energy-efficient alternative to
- complex visual tasks, enabling high-speed, low-energy neu-
- larger datasets generally require large D to achieve a close
- Table 1. Comparison of complexity and parameters between ANN-
- phasis on maintaining accuracy during long-term tracking;
- fusion. Additionally, we conduct ablation studies to further
- C = 32, resulting in 15.1M parameters, and a large model
- with C = 64, resulting in 55.4M parameters. The architec-

本 V1 只引用这些可从 PDF 抽取到的实验线索；完整数值、baseline 顺序和显著性比较需要人工在 V2 中逐表核对。

## 7. Main Contributions

1. 提出或系统化研究了与 `SpikeVideoFormer: An Efficient Spike-Driven Video Transformer with Hamming Attention and $\\mathcalO(T)$ Complexity` 对应的核心方法/任务设定。
2. PDF 摘要和方法部分给出了主要模块设计，涉及 SNN, tracking, Transformer。
3. PDF 实验部分报告了数据集、指标或 ablation 线索，可作为后续人工深读的入口。
4. 对 survey 的价值在于补充 C: SNN side background 这一类证据，而不是直接作为未经核验的最终结论。

## 8. Limitations and Risks

- 本 V1 是自动 PDF-based 摘要，尚未逐式核验全部公式和表格数值。
- 若论文报告 efficiency / energy / latency，需要确认其是理论 operation count、GPU 测量还是 neuromorphic hardware 实测。
- 若论文属于 B/C 类，应避免在 survey 中把它误写成 SNN + Event Camera core method。
- 部分实验结论可能依赖特定 dataset split、pretraining 设置或 implementation details，需要人工复核。

## 9. Relation to SNN for Event Cameras

分类：C: SNN side background。

理由：reading plan 将该论文标为 level C；PDF 内容显示其关键词和任务与 `SNN, tracking, Transformer` 相关。最终归类仍应在 V2 阶段结合全文细读修正。

## 10. Relation to Survey Taxonomy

- SNN training methods
- Efficiency, latency, and energy
- Open challenges

## 11. Key Terms and Concepts

- SNN: 论文中相关的关键概念，V2 阶段需要结合原文定义进一步精读。
- Spiking Neural Network: 论文中相关的关键概念，V2 阶段需要结合原文定义进一步精读。
- Transformer: 论文中相关的关键概念，V2 阶段需要结合原文定义进一步精读。

## 12. Questions for Human Deep Reading

1. PDF 中 method section 对核心模块的数学定义是什么？
2. 实验使用的数据集、划分和评价指标是否与 baseline 完全一致？
3. 主要提升来自 representation、architecture、training strategy 还是 post-processing？
4. 效率、能耗或 latency 结论是理论估算还是硬件实测？
5. 该论文对 SNN for Event Cameras survey 的贡献应归入方法、数据集、训练还是挑战部分？
6. 该 SNN 方法是否真的在 event-camera dataset 上验证，还是只作为通用 SNN 背景？

## 13. Evidence Notes

- Local PDF parsed successfully: 2025-ICML-spikevideoformer-an-efficient-spike-driven-video-transformer-with-hamming-attention-and-ma.pdf, 17 pages.
- PDF headings observed: Abstract; 1. Introduction; 2. Related Works; CNN Block; Downsample; Separable; Channel; Joint Attention.
- PDF key experiment/evidence lines include datasets/metrics/table mentions listed in Section 6.

## 14. Draft Survey-Usable Sentences

Draft material: `SpikeVideoFormer: An Efficient Spike-Driven Video Transformer with Hamming Attention and $\\mathcalO(T)$ Complexity` can be cited cautiously as C: SNN side background evidence after its quantitative tables and method details are manually verified.

Draft material: The paper is useful for mapping how SNN, tracking, Transformer relates to event-camera/SNN survey taxonomy, but V2 should refine the exact claim boundaries.
