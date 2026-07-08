---
title: "TTFSFormer: A TTFS-based Lossless Conversion of Spiking Transformer"
authors: ["Lusen Zhao", "Zihan Huang", "Jianhao Ding", "Zhaofei Yu"]
year: 2025
venue: "ICML"
level: "C"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/ICML2025/C/2025-ICML-C-ttfsformer-a-ttfs-based-lossless-conversion-of-spiking-transformer.md"
official_page: "https://proceedings.mlr.press/v267/zhao25n.html"
pdf_link: "https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25n/zhao25n.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["SNN", "spiking transformer", "ANN-to-SNN conversion", "TTFS", "ImageNet"]
---

# Summary V1｜TTFSFormer: A TTFS-based Lossless Conversion of Spiking Transformer

## 1. One-sentence Summary

TTFSFormer 提出一种面向 Transformer 的 time-to-first-spike ANN-to-SNN conversion 方法，通过 generalized TTFS neurons 和 nonlinear layer designs 在保持 ANN accuracy 的同时降低 spike-based inference energy。

## 2. Research Problem

论文关注 Spiking Transformer 的 ANN-to-SNN conversion。已有 ANN-to-SNN conversion 可把预训练 ANN 参数映射到 SNN，避免从头训练，但 TTFS coding 过去主要适用于 MLP/CNN，对 Transformer 中 attention 和 nonlinear layers 处理不足。

这个问题对综述的 SNN side 很重要，因为 event-camera SNN 也常借助 ANN-to-SNN conversion、spiking transformer 或 TTFS coding 来提高精度和降低能耗。虽然该论文不处理 event cameras，但它为 spiking transformer conversion 提供背景。

## 3. Background and Motivation

SNN 使用 spike events 传递信息，理论上可减少 MAC operations，并在 neuromorphic hardware 上节能。TTFS coding 让每个 neuron 最多发放一个 spike，用 spike latency 表示数值，具有较低 spike count。

Transformer 的 self-attention、MLP 和 nonlinear activations 更复杂，直接用传统 TTFS neuron 可能造成精度损失。论文动机是设计适合 Transformer layers 的 TTFS neuron 和转换规则，实现近似 lossless conversion。

## 4. Method Overview

输入是预训练 Transformer ANN，例如 ViT 和 EVA；输出是 TTFS-coded Spiking Transformer。方法把每层转换为 receiving stage 和 emitting stage：receiving stage 接收上一层 spike times 并积累 membrane potential，emitting stage 在阈值触发后向下一层发出 spike time。论文提出 generalized neurons 扩展 TTFS 表达范围，并为 Transformer nonlinear layers 设计对应 neuron structures。

该方法是 SNN side background，不涉及 event camera input。

## 5. Technical Details

### Event Representation

无 event-camera representation。这里的“event”是 SNN spike timing，而不是 event camera sensor event。

### Spiking Neuron / SNN Module

核心是 TTFS neuron。每个 neuron 用 first spike time 表示 activation value。论文把 layer computation 拆成 receiving/emitting 两阶段，以避免上一层过早 spike 干扰当前层完整处理。Figure 1 展示 receiving and emitting stages。

### Network Architecture

TTFSFormer 针对 Transformer architecture 进行 conversion，测试 ViT-S/ViT-B/ViT-L 和 EVA-S/EVA-L 等预训练模型。它不是新建视觉 backbone，而是 conversion framework。

### Training Strategy

方法主要是 conversion，不需要重新训练。权重来自 Hugging Face public repositories，使用 Algorithm 1 将 ANN 转为 SNN。

### Loss Function

无常规训练 loss；核心是保持转换后 SNN 输出接近 ANN。论文关注 conversion accuracy 和 energy estimation。

### Inference Process

推理时每层通过 spike time 传播信息。精确 TTFS timing 下，论文报告转换后 accuracy loss 低于 0.1%。能耗估计使用 AC/MAC energy assumptions：`E_AC = 0.9 pJ`、`E_MAC = 4.6 pJ`。

## 6. Experiments

主要 dataset 是 ImageNet-1k。Table 1 比较 direct training、CNN-to-SNN、Transformer-to-SNN 和 TTFSFormer。论文报告 ViT/EVA 系列转换后 SNN accuracy 与 ANN accuracy 基本一致；摘要称 precise TTFS representation 下 ViT/EVA 不同规模 accuracy loss 低于 0.1%。

Table 2 报告 energy consumption：ViT-S/16 SNN energy 4.9 mJ，约为 ANN 的 22.3%；ViT-B/16 为 17 mJ，约 21.0%；ViT-L/16 为 59 mJ，约 20.7%。Figure 4 分析不同 time precision 下 ViT-S/ViT-B accuracy，说明 timing precision 会影响转换精度。

Robustness 实验探索 spike timing precision 和误差对 accuracy 的影响；具体数值需要人工复核图表。

## 7. Main Contributions

- 首个聚焦 TTFS-based Spiking Transformer conversion 的方法之一。
- 提出 generalized TTFS neuron structure，增强表示范围和 nonlinear processing 能力。
- 为 Transformer 中 attention/nonlinear layers 设计转换机制。
- 在 ImageNet-1k 上报告接近 ANN 的 accuracy，并估计约 20%-22% 的 ANN energy consumption。

## 8. Limitations and Risks

论文不涉及 event camera，也不验证 temporal event streams。能耗是基于 operation count 和文献能耗常数估计，并非真实硬件测量。TTFS coding 依赖 spike timing precision，实际硬件上的时间分辨率、noise 和 latency 可能影响性能。方法依赖已有高性能 ANN Transformer，因此不是低数据或端到端 SNN training 方案。

对综述使用时，应把它放在 SNN training/conversion 或 Spiking Transformer 背景，不应作为 event-camera method。

## 9. Relation to SNN for Event Cameras

分类：C: SNN side background。

理由是 TTFSFormer 明确属于 SNN/Spiking Transformer/ANN-to-SNN conversion，但没有 event camera 数据或任务。它可为 survey 中 Spiking Transformer 和 conversion-based SNN training 提供背景。

## 10. Relation to Survey Taxonomy

可支持的章节包括：

- SNN architectures for event cameras
- SNN training methods
- Surrogate gradient and temporal credit assignment
- Hybrid ANN-SNN models
- Efficiency, latency, and energy
- Open challenges

## 11. Key Terms and Concepts

- TTFS coding：Time-to-first-spike coding，每个 neuron 最多用一个 spike time 表示数值。
- ANN-to-SNN conversion：把预训练 ANN 映射为 SNN 的训练/部署策略。
- Receiving stage / emitting stage：TTFSFormer 中每层接收 spike 与发放 spike 的两阶段机制。
- Spiking Transformer：将 Transformer computation 改造为 spike-driven 或 spike-coded computation。
- AC/MAC energy：用加法累积和乘加操作的能耗估算 SNN/ANN 能耗。

## 12. Questions for Human Deep Reading

1. Generalized TTFS neuron 的数学定义如何扩展传统 TTFS 表示范围？
2. Attention 中 Q/K/V、Softmax 或 nonlinear layers 如何被 TTFS conversion？
3. Table 1 中哪些模型达到低于 0.1% accuracy loss？
4. Energy estimation 是否包含 memory access 和 spike routing？
5. Time precision 对 latency 和 hardware feasibility 的影响是什么？
6. 该方法能否处理 event-camera temporal input，还是仅适合 static image Transformer？
7. 与 surrogate-gradient trained Spiking Transformer 相比优缺点是什么？
8. 是否有真实 neuromorphic hardware 验证？

## 13. Evidence Notes

- Abstract：定义 problem、TTFS coding、generalized neuron、accuracy/energy claim。
- Figure 1：receiving and emitting stages pipeline。
- Table 1：ImageNet-1k 上与 previous SNN works 对比。
- Table 2：ViT-S/B/L energy consumption 和 SNN/ANN energy ratio。
- Figure 4：不同 TTFS time precision 下 accuracy。
- Conclusion：说明 TTFS-based spiking transformer conversion 和 future training framework。

## 14. Draft Survey-Usable Sentences

草稿句 1：TTFSFormer is relevant to SNN-event-camera surveys as SNN-side background, especially for discussing ANN-to-SNN conversion and spike-timing codes in Transformer architectures.

草稿句 2：Its results should not be treated as event-camera evidence, but they suggest that TTFS coding may be a useful design space for energy-aware Spiking Transformers.

草稿句 3：When comparing with event-camera SNNs, TTFSFormer should be framed as a conversion method for static vision Transformers rather than a native event-stream model.
