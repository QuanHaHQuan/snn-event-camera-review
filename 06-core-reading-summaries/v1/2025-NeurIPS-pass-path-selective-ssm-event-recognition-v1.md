---
title: "PASS: Path-selective State Space Model for Event-based Recognition"
authors: ["Jiazhou Zhou", "Kanghao Chen", "Lei Zhang", "Lin Wang"]
year: 2025
venue: "NeurIPS"
level: "B"
priority: "P0"
advisor_track: "yes"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/NeurIPS2025/B/2025-NEURIPS-B-pass-path-selective-state-space-model-for-event-based-recognition.md"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/f5dbd98d426772945099ccace06418ba-Abstract-Conference.html"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/file/f5dbd98d426772945099ccace06418ba-Paper-Conference.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["event camera", "state space model", "event recognition", "Mamba", "frequency generalization"]
---

# Summary V1｜PASS: Path-selective State Space Model for Event-based Recognition

## 1. One-sentence Summary

PASS 用 Path-selective Event Aggregation and Scan (PEAS) 与 Multi-faceted Selection Guiding loss，把可变长度 event streams 编码为适合 SSM/Mamba 处理的序列特征，用于 event-based object/action recognition 和跨频率泛化。

## 2. Research Problem

论文关注 event-based recognition 中的长事件流和频率泛化问题。现有方法常按固定时间间隔或固定 event count 把 event stream 采样为 event frames，这限制了可处理的 event length，并导致 inference frequency 变化时性能下降。

这个问题对 SNN/Event Camera 综述重要，因为很多 SNN event models 也依赖固定时间步或固定窗口表示。PASS 虽不是 SNN，但它强调 event length、sampling frequency 和 temporal generalization，能帮助讨论 SNN 输入编码与时间步设计。

## 3. Background and Motivation

Event cameras 输出高时间分辨率事件，object recognition 的事件量可能约 `10^6`，action recognition 可到 `10^7`，更长场景可到 `10^9`。固定窗口方法难以同时适配短事件和超长事件。

SSM/Mamba 具备线性复杂度和长序列建模能力。PASS 的动机是用 adaptive selection 和 scan，让事件特征在不同 event lengths 和 inference frequencies 下都能被稳定编码。

## 4. Method Overview

PASS 的输入是 event stream，输出是 object/action recognition class。整体框架先把 raw events 采样/聚合为候选 event presentations，再用 PEAS 模块进行 path-selective aggregation and scan，选择并编码固定维度特征；随后输入 SSM/Mamba backbone 做 spatiotemporal modeling；训练中加入 MSG loss，约束 PEAS selection 的随机性和冗余。

它不是 SNN 方法，没有 spiking neuron component。它属于 event-camera recognition 的 SSM-based background paper。

## 5. Technical Details

### Event Representation

论文强调事件长度分布从 `10^6` 到 `10^9`，并使用 `K` 个 selected event frames/features 表示输入。PEAS 不是随机采样，而是学习选择对任务有用的 path/aggregation。

### Spiking Neuron / SNN Module

无。PASS 使用 SSM/Mamba 思路，不包含 spiking neuron。

### Network Architecture

模型有 Tiny/Small/Middle 三个规模。Table 1 显示 Tiny 为 24 layers、dim 192、约 7M params、1.1 GFLOPs、4.1 ms inference；Small 为 25M params、4.3 GFLOPs；Middle 为 74M params、12.7 GFLOPs。

### Training Strategy

论文使用 VideoMamba checkpoints 初始化，与 ViT 风格调整 depth 和 embedding dimension。Ablation 默认在 PAF dataset、0.8 Hz sampling frequency、16 selected event frames 上运行。

### Loss Function

MSG loss 用于减少 PEAS selection 的 randomness 和 redundancy。Table 6 中进一步拆分 MSG 组件，显示加入 LCLS、LIEM、ILW/EIE 等约束后 PAF Top-1 从 92.98% 提升到 94.83%。

### Inference Process

推理时 PASS 可在不同 frequency 下处理事件。论文重点报告模型在训练频率与推理频率不一致时的 accuracy drop，并与固定 Time Windows / Event count baseline 比较。

## 6. Experiments

论文在 five public datasets 和 three proposed datasets 上评估。Public datasets 包括 N-Caltech101、N-Imagenet、PAF、SeAct、HARDVS。自建/提出的数据集包括 ArDVS100、TemArDVS100 和 Real-ArDVS10，用于更长 event length 和现实泛化。

Object recognition：Table 2 显示 PASS-M-K(2) 在 N-Caltech101 上 94.60%，比 EventDance 高 +2.25；在 N-Imagenet 上 61.32%，比 MEM 高 +3.43。Action recognition：Table 3 显示 PASS-M-K(8) 在 PAF 上 98.28%，PASS-M-K(16) 在 SeAct 上 66.38%，PASS-S-K(16) 在 HARDVS 上 98.41%，其中 HARDVS 比 ExACT 高 +8.31。

Long event recognition：Table 4 显示 PASS-M-K(32) 在 ArDVS100 上 97.35%，Real-ArDVS10 上 100.00%，TemArDVS100 上 82.50；PASS-T-K(32) 在 TemArDVS100 上达到 89.00，但不同模型表现并不完全单调。

Frequency generalization：论文报告 PASS 最大 accuracy drop 为 -8.62%，而 baseline Time Windows 在某些训练/测试频率组合下可达到 -18.96%、-20.69%、-29.32%。Table 5 ablation 显示 PEAS + MSG 在 PAF K(16) 上 94.83%，ArDVS100 K(16) 上 93.85%，优于 No Sampling、Random Sampling 和单独 PEAS。

## 7. Main Contributions

- 提出 PASS，用于宽 event length 分布和 varying inference frequencies 下的 event recognition。
- 提出 PEAS，把 asynchronous events 自适应聚合和扫描为固定维度序列特征。
- 提出 MSG loss，约束选择过程中的随机性和冗余。
- 提出/使用长事件识别数据设置 ArDVS100、TemArDVS100、Real-ArDVS10。
- 在 object/action recognition 和 frequency generalization 上报告较强结果。

## 8. Limitations and Risks

论文报告了 broad event length，但自建数据集的采集、合成或动作设计需要人工核查，避免过度推广到所有真实场景。PASS 使用 VideoMamba 初始化，因此部分性能可能来自预训练 backbone，而不只是 PEAS/MSG。模型 Middle 规模达到 74M params，对低功耗部署不一定友好。

对综述风险：PASS 不是 SNN，不应放入 SNN architecture 主线；更适合用于讨论 event representation、temporal encoding 和 frequency generalization。

## 9. Relation to SNN for Event Cameras

分类：B: Event Camera side background；advisor-track support。

理由是 PASS 直接处理 event camera recognition，但核心为 SSM/Mamba，不含 spiking neuron。它可为 SNN 的时间编码、窗口选择和跨频率泛化提供背景与对照。

## 10. Relation to Survey Taxonomy

可支持的章节包括：

- Event representations for SNNs
- SNN architectures for event cameras
- Event-based object detection
- SNN training methods
- Datasets and benchmarks
- Open challenges

## 11. Key Terms and Concepts

- PASS：Path-selective State Space Model for event recognition。
- PEAS：Path-selective Event Aggregation and Scan，用于自适应选择/扫描事件表示。
- MSG loss：Multi-faceted Selection Guiding loss，用于减少 selection randomness/redundancy。
- Inference frequency generalization：训练和推理频率不一致时维持性能。
- ArDVS100 / TemArDVS100 / Real-ArDVS10：用于长事件/action transition 评估的数据设置。

## 12. Questions for Human Deep Reading

1. PEAS 的 selection 是否可解释？是否会丢失关键少数事件？
2. MSG loss 的每个子项具体约束什么，是否有稳定 ablation？
3. VideoMamba initialization 对性能贡献多大？
4. ArDVS100、TemArDVS100、Real-ArDVS10 的构建方式是否足够真实？
5. Table 4 中 TemArDVS100 上不同模型的非单调结果如何解释？
6. Frequency generalization 是否只在 PAF 上验证，还是跨多数据集？
7. PASS 能否与 SNN backbone 组合，替代固定 time-step event encoding？
8. 计算成本与 event-by-event SNN 方法相比如何？

## 13. Evidence Notes

- Abstract：定义 PASS、PEAS、MSG、-8.62% vs -20.69% frequency drop。
- Figure 3：展示 PASS framework overview。
- Table 1：Tiny/Small/Middle model settings、params、FLOPs、inference time。
- Table 2：N-Caltech101 和 N-Imagenet object recognition。
- Table 3：PAF、SeAct、HARDVS action recognition。
- Table 4：ArDVS100、Real-ArDVS10、TemArDVS100 long event recognition。
- Table 5/6：PEAS 与 MSG ablation。

## 14. Draft Survey-Usable Sentences

草稿句 1：PASS shows that temporal encoding choices, especially event selection and inference frequency, can substantially affect event-based recognition performance.

草稿句 2：Although PASS is an SSM-based rather than spiking model, its analysis of fixed-window limitations is relevant to SNN event-camera systems that discretize event streams into fixed time steps.

草稿句 3：For survey writing, PASS can be used as background for event representation and temporal generalization, not as a core SNN architecture.
