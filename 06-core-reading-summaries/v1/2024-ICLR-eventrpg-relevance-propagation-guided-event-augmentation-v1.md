---
title: "EventRPG: Event Data Augmentation with Relevance Propagation Guidance"
authors: ["Mingyuan Sun", "Donghao Zhang", "Zongyuan Ge", "Jiaxu Wang", "Jia Li", "Zheng Fang", "Renjing Xu"]
year: 2024
venue: "ICLR"
level: "A"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/ICLR2024/A/2024-ICLR-A-eventrpg-event-data-augmentation-with-relevance-propagation-guidance.md"
official_page: "https://proceedings.iclr.cc/paper_files/paper/2024/hash/19dbb86f771ddbf9986cf0c9b1c61c17-Abstract-Conference.html"
pdf_link: "https://proceedings.iclr.cc/paper_files/paper/2024/file/19dbb86f771ddbf9986cf0c9b1c61c17-Paper-Conference.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["SNN", "event camera", "data augmentation", "relevance propagation", "SLRP", "SLTRP", "CIFAR10-DVS", "N-Caltech101"]
---

# Summary V1｜EventRPG: Event Data Augmentation with Relevance Propagation Guidance

## 1. One-sentence Summary

EventRPG 提出 SLRP / SLTRP 为 SNN 生成 CAM 和 saliency maps，并用 relevance-guided Event Drop / Event Mix 改善 event-based SNN classification 的泛化能力。

## 2. Research Problem

论文解决 event-based classification 中 SNN overfitting 和 data augmentation 不够精准的问题。传统 event augmentation 如 random drop、geometric transforms、EventMix 不知道 SNN 真正关注哪些事件区域；而 image-domain saliency augmentation 不能直接用于 SNN，因为 SNN 的 spike dynamics 和时间维度使 CAM/saliency 计算更复杂。

## 3. Background and Motivation

event cameras 具备低延迟、低功耗和高动态范围。SNN 理论上适合异步事件数据，但在 event-based classification 中空间表示能力相对弱，容易过拟合。data augmentation 是缓解 overfitting 的简单有效手段，但对于 SNN，需要能解释 spike-based model attention 的 saliency tool。

本文动机是先解决“如何从 SNN 生成可靠 saliency map”，再用 saliency map 指导事件级 augmentation，使扰动集中在 label-related / model-attended regions。

## 4. Method Overview

方法包含两层：第一层是 Spiking Layer-Time-wise Relevance Propagation (SLTRP) 和 Spiking Layer-wise Relevance Propagation (SLRP)，用于在 SNN 中反向传播 relevance score 并生成 CAM/saliency maps。第二层是 EventRPG augmentation，包括 RPGDrop 和 RPGMix。

输入是 event streams，输出是 augmented event streams。RPGDrop 根据 saliency map 对高相关像素更高概率 drop events；RPGMix 用 relevance propagation 定位两个样本中的 label-related regions，通过 spatial translation 和 mask/mix 进行更少重叠的事件混合。

## 5. Technical Details

### Event Representation

实验覆盖由 event cameras 产生的 object recognition datasets 和 action recognition datasets，包括 N-Caltech101、CIFAR10-DVS、N-Cars、DVS-Gesture、SL-Animals 等。方法作用于 event stream 或其输入表示，并生成 drop/mix 后的 augmented events。

### Spiking Neuron / SNN Module

SLTRP 考虑 spiking layer 的 membrane potential 和 input current across time，用 relevance score 在 time steps 间分配贡献。SLRP 则把 time dimension 聚合，适合由静态图像转换来的事件数据，可降低计算时间。

### Network Architecture

EventRPG 不是新 backbone，而是 augmentation framework，可搭配 Spike-VGG11、SEW ResNet18 等 SNN 结构。CAM 可来自 intermediate layer 的 relevance scores，saliency map 则传播到 input level。

### Training Strategy

EventRPG 在每个 batch 中随机选择 policy 和 magnitude，并以 0.5 概率应用 RPGMix。它结合 NDA 中的一些 geometric augmentation，再加入 relevance-guided drop/mix。

### Loss Function

论文主要贡献不是新 classification loss，而是 relevance propagation rule 和 augmentation strategy。实验用已有 SNN training methods，如 TET、STBP-tdBN 等。

### Inference Process

EventRPG 主要用于训练期 augmentation。推理阶段使用训练好的 SNN classifier，不需要执行 augmentation；saliency generation 可作为解释工具。

## 6. Experiments

Table 1 评估 CAM/saliency 的 faithfulness，指标为 Average Increase (A.I.) 和 Average Drop (A.D.)。SLRP/SLTRP saliency 在 N-Caltech101、CIFAR10-DVS 和 DVS-Gesture 等数据集上通常取得较高 A.I. 和较低 A.D.。

Table 2 报告 saliency/CAM generation time。SLRP-CAM 和 SLTRP-CAM 与 SAM、RelCAM 等在同一速度层级；SLTRP-Saliency Map 更慢，但在 SEW ResNet18 上仍有竞争力。

Table 3 的 object recognition 结果显示，EventRPG 在 N-Caltech101 达到 85.62%，在 CIFAR10-DVS 达到 85.55%，在 N-Cars 达到 96.00%。其中 N-Caltech101 和 CIFAR10-DVS 为论文报告 SOTA；N-Cars 上略低于 EventMix 的 96.29%。

Table 4 的 action recognition 结果显示，EventRPG 在 DVS-Gesture 上最高 96.53%，在 SL-Animals 4 sets / 3 sets 上最高 91.59% / 93.75%。论文称在 SL-Animals 上相对第二好 augmentation 分别提升 3.82% 和 4.2%。

Figure 5 说明 EventRPG 的 relevance propagation computation 可随 batch size 并行加速；当 batch size per GPU 超过 4 时，SLRP/SLTRP 速度接近 NDA 和 EventDrop。

## 7. Main Contributions

1. 提出 SLRP 和 SLTRP，使 SNN 能生成稳定 CAM 和 saliency maps。
2. 提出 RPGDrop，用 saliency map 指导 event dropping。
3. 提出 RPGMix，用 relevance localization 指导 event mix，减少 label-related object overlap。
4. 构建 EventRPG augmentation pipeline，并在多个 event classification/action recognition datasets 上提升性能。
5. 明确指出当前 EventRPG 主要适用于 classification tasks。

## 8. Limitations and Risks

作者在 Section 6 明确写出 limitation：EventRPG 目前只能用于 classification tasks。对于 detection、tracking、segmentation 等任务如何使用仍未解决。

EventRPG 需要 relevance propagation，因此训练时有额外计算成本；虽然 batch 并行可缓解，但大模型或高分辨率事件数据上成本仍需核验。

Saliency-guided augmentation 的效果依赖 saliency quality；当数据集如 N-Cars 只有 binary label 且 background 样本缺少明确 label-related object 时，效果会下降。

## 9. Relation to SNN for Event Cameras

分类：A: SNN + Event Camera core paper。

本文直接针对 event camera datasets 上的 SNN classification，解决 SNN saliency 和 augmentation 问题。它适合作为“SNN training / data augmentation for event cameras”的代表，而不是 detection architecture。

## 10. Relation to Survey Taxonomy

- SNN training methods：SNN-specific relevance propagation and augmentation。
- Event representations for SNNs：event stream drop/mix augmentation。
- Datasets and benchmarks：N-Caltech101、CIFAR10-DVS、DVS-Gesture、SL-Animals。
- Open challenges：classification-only limitation、SNN interpretability。

## 11. Key Terms and Concepts

- SLRP：Spiking Layer-wise Relevance Propagation，聚合时间维度。
- SLTRP：Spiking Layer-Time-wise Relevance Propagation，保留 time-step saliency。
- RPGDrop：基于 saliency 的 event dropping。
- RPGMix：基于 relevance localization 的 event mixing。
- CAM / saliency map：模型关注区域解释工具。
- A.I. / A.D.：attention map faithfulness metrics。

## 12. Questions for Human Deep Reading

1. SLRP 与 SLTRP 在动态数据上的差异是否显著？
2. RPGDrop 是否可能删掉过多关键事件，造成 label noise？
3. RPGMix 的 bounding box localization 是否鲁棒？
4. classification-only limitation 能否通过 detection loss 扩展？
5. Table 3/4 的训练 settings 是否完全公平？
6. relevance propagation 的显存和时间开销是多少？
7. saliency map 是否可用于 human interpretability in survey？
8. 是否有代码复现全部 datasets？

## 13. Evidence Notes

- Section 3.2-3.3，第 4-5 页：SLTRP / SLRP。
- Figure 2，第 5 页：RPGDrop / RPGMix。
- Section 4，第 5-6 页：EventRPG augmentation。
- Table 1-2，第 6-7 页：faithfulness and time cost。
- Table 3-4，第 8-9 页：object/action recognition accuracy。
- Section 6，第 9 页：conclusion and limitation。

## 14. Draft Survey-Usable Sentences

Draft material: EventRPG addresses event-based SNN overfitting by first making SNN attention measurable through spiking relevance propagation and then using that attention to guide event augmentation.

Draft material: Its main survey relevance is training and augmentation rather than architecture design.

Draft material: The paper explicitly limits the current method to classification tasks, which should be preserved in survey wording.

