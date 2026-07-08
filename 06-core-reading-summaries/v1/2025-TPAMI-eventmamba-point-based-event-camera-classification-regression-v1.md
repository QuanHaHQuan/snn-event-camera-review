---
title: "Rethinking Efficient and Effective Point-based Networks for Event Camera Classification and Regression"
authors: ["Hongwei Ren", "Yue Zhou", "Jiadong Zhu", "Xiaopeng Lin", "Haotian Fu", "Yulong Huang", "Yuetong Fang", "Fei Ma", "Hao Yu", "Bojun Cheng"]
year: 2025
venue: "TPAMI"
level: "B"
priority: "SECNet reference-only"
advisor_track: "yes"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "SECNet references / 00-index/reading-plan-core.md"
official_page: "https://arxiv.org/abs/2405.06116"
pdf_link: "https://arxiv.org/pdf/2405.06116"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["event camera", "EventMamba", "point cloud", "Mamba", "action recognition", "camera pose relocalization", "eye tracking", "SECNet reference"]
---

# Summary V1｜Rethinking Efficient and Effective Point-based Networks for Event Camera Classification and Regression

## 1. One-sentence Summary

EventMamba 重新审视 Event Cloud 与 Point Cloud 的差异，在 point-based hierarchical network 中加入 temporal aggregation 和 Mamba block，以低参数和低 FLOPs 处理 event-based action recognition、Camera Pose Relocalization 和 eye-tracking regression。

## 2. Research Problem

本文关注 event camera data 如何在不转成 dense frames 的情况下高效建模。frame-based methods 会把 sparse asynchronous events 堆叠成图像或体素帧，容易损失 fine-grained temporal information，并增加 event-free regions 的计算负担。

point-based methods 可以直接处理 `(x, y, t, p)` Event Cloud，但以往直接借用 Point Cloud network 时，往往忽略 Event Cloud 中时间维度的特殊语义。作者认为 Event Cloud 不是普通 3D geometry，时间既是 point coordinate，又是动作、pose、tracking 等任务的动态线索。

## 3. Background and Motivation

event cameras 以微秒级时间分辨率记录亮度变化，天然输出 sparse Event Cloud。Point Cloud representation 能保留稀疏性，也能避免 frame stacking 的预处理延迟。

但 Point Cloud methods 通常强调 permutation invariance 和 spatial geometry；event streams 则需要 chronologically ordered temporal modeling。本文延续 TTPOINT / PEPNet 一类 point-based event camera work，核心动机是把 explicit temporal feature extraction 放进 hierarchical structure，并用 SSM-based Mamba 替代更重或更慢的 temporal module。

## 4. Method Overview

输入是 raw Event Cloud `E = (x, y, t, p)`。pipeline 包括 sliding window segmentation、point sampling、hierarchical local/global feature extraction、temporal aggregation、Mamba block 和 task-specific head。

EventMamba 先把 event stream 按时间窗口切分，并采样固定数量 points；然后通过 staged modules 提取 implicit spatiotemporal features；在 global extractor 中加入 temporal aggregation 和 Mamba，用于 long sequence event features 的 explicit temporal modeling。输出根据任务不同分别是 action class、camera pose regression 或 pupil coordinate regression。

该方法不是 SNN；它是 event-camera side / Mamba-style point representation background，对 SECNet 的 event cloud processing 和 Mamba comparison 很关键。

## 5. Technical Details

### Event Representation

论文把 event camera output 定义为 Event Cloud `(x, y, t, p)`。作者强调不能把 Event Cloud 仅当作 Point Cloud，因为 `t` 不是普通 spatial dimension，而是时序索引和动态信息来源。

### Spiking Neuron / SNN Module

本文没有提出 SNN 或 spiking neuron module。出现 SNN 主要是在 baselines 或相关工作中，例如 Motion-based SNN / HMAX SNN。Survey 使用时应把它归为 event-camera point/Mamba background，而不是 SNN core method。

### Network Architecture

EventMamba 使用 hierarchical structure，包括 staged local/global feature extraction。与 TTPOINT 相比，它显式加入 temporal aggregation 和 SSM-based Mamba block；与 PEPNet 相比，它用更 hardware-friendly 的 Mamba 处理 sequence events，而不是 A-Bi-LSTM。

### Training Strategy

论文按不同任务训练 classification / regression heads。分类任务使用多个 action recognition datasets；regression 任务覆盖 IJRR Camera Pose Relocalization 和 SEET eye-tracking。具体 optimizer/loss 细节需人工复核全文设置。

### Loss Function

核心贡献不是新 loss。classification 使用 accuracy 评估，regression 使用 translation/rotation error、p3/p5/p10 和 MSE(px) 等指标。

### Inference Process

推理时对每个 event stream/window 采样固定数量 points，通过 EventMamba backbone 和 task head 输出结果。Table 13 报告服务器上的 P5/P50/P95 inference time，显示各 action datasets 的 P50 多在 6.0-14.4 ms 范围。

## 6. Experiments

Action recognition datasets 包括 Daily DVS、DVS128 Gesture、DVS Action、HMDB51-DVS、UCF101-DVS 和 THU E-ACT-50-CHL。Table 1 给出 classes、sensor resolution、train/test samples、point number、sliding window 和 overlap。

在 DVS128 Gesture 上，EventMamba 报告 0.29M params、0.219 GFLOPs、99.2% accuracy；在 Daily DVS 上为 0.905M params、0.953 GFLOPs、99.1% accuracy；在 DVS Action 上为 89.1%，低于 TTPOINT 的 92.7%，作者把这与 small dataset overfitting 风险联系起来。

在大规模 converted datasets 上，EventMamba 在 HMDB51-DVS 达到 86.4%，在 UCF101-DVS 达到 97.9%。在 THU E-ACT-50-CHL 上达到 59.4%，对比 EV-ACT 的 58.5%，同时参数和 GFLOPs 明显更低。

Camera Pose Relocalization 使用 IJRR CPR dataset。Table 6 报告 EventMamba 平均 0.012m / 0.831 degree，0.904M params，0.476G FLOPs，5.5ms inference time。Table 7 显示 point sampling preprocessing 平均 0.065ms，低于 event stacking 的 0.457ms。

Eye tracking 使用 SEET dataset。Table 10 报告 EventMamba p3=0.944、p5=0.992、p10=0.999、MSE=1.48px；EventMambalite 只有 0.27M params / 62.6M FLOPs，并保持接近表现。

Ablation 显示 temporal module 很关键：Table 11 中 HMDB51-DVS 2048 points、dimension `[64,128,256]` 的完整模型为 82.1%，w/o Mamba 为 57.5%，w/ LSTM 为 70.8%。Table 12 中 CPR average error 从 w/o Mamba 的 0.018m / 1.239 degree 改善到 EventMamba 的 0.012m / 0.831 degree。

## 7. Main Contributions

1. 将 Event Cloud 与 Point Cloud 的差异明确化，强调 event temporal ordering 的重要性。
2. 提出 EventMamba，在 point-based hierarchical event network 中加入 temporal aggregation 和 Mamba block。
3. 在 action recognition、Camera Pose Relocalization 和 eye-tracking regression 三类任务上验证 point-based event processing。
4. 展示低参数、低 FLOPs 和低 preprocessing time 的优势。
5. 为 SECNet / EventMamba-style event cloud representation 提供直接前序背景。

## 8. Limitations and Risks

本文不是 SNN，因此不能直接作为 SNN architecture evidence，只能作为 event camera representation / Mamba background。

作者自己指出增强 temporal representation 后，小数据集如 DVS Action 和 Daily DVS 可能更容易 overfitting。

部分结果非常强，例如 UCF101-DVS 97.9%，需要人工复核 split、window voting 和 converted dataset protocol 是否与 prior work 完全一致。

arXiv PDF 首页仍显示 journal latex template 信息，正式 TPAMI bibliographic metadata 需要人工核验。

## 9. Relation to SNN for Event Cameras

分类：B: Event Camera side background；advisor-track support。

它不提出 SNN，但对 survey 很重要，因为它说明 event streams 可以通过 point/event cloud 和 Mamba-style temporal modeling 直接处理，构成 SNN event representation 和 hybrid/alternative architecture 的对照背景。

## 10. Relation to Survey Taxonomy

- Event representations for SNNs：Event Cloud / point-based event representation。
- Hybrid ANN-SNN models：可作为 non-spiking ANN/Mamba baseline。
- Event-based action recognition：多个 DVS action datasets。
- Efficiency, latency, and energy：params、GFLOPs、preprocessing time、inference time。
- Open challenges：small dataset overfitting、fair protocol、event-specific temporal modeling。

## 11. Key Terms and Concepts

- EventMamba：point-based event camera backbone with Mamba temporal modeling。
- Event Cloud：event camera output as `(x, y, t, p)` sparse point sequence。
- Temporal aggregation：在 hierarchical feature extraction 中显式聚合时序特征。
- Mamba / SSM：用于 long sequence event feature modeling 的 selective state-space backbone。
- CPR：Camera Pose Relocalization regression task。
- SEET：event-based eye-tracking evaluation dataset。

## 12. Questions for Human Deep Reading

1. TPAMI 正式版本与 arXiv v4 是否完全一致？
2. UCF101-DVS / HMDB51-DVS 的 train/test split 是否与所有 baselines 一致？
3. Table 11 中 82.1% 与 Table 5 中 86.4% 的设置差异是什么？
4. temporal aggregation 与 Mamba block 的边界如何定义？
5. EventMamba 是否依赖 voting 或 multi-window aggregation？
6. small dataset overfitting 是否可以通过 tensor decomposition 或 regularization 缓解？
7. 对 SECNet 来说，本文和 TTPOINT / SpikePoint 的继承关系具体是什么？
8. inference time 是否包含 preprocessing？

## 13. Evidence Notes

- Abstract，第 1 页：提出 EventMamba、point-based representation、Mamba temporal extraction 和三类任务。
- Introduction，第 2 页：列出四条 contributions。
- Section 4.1 / Table 1，第 8-9 页：datasets 与 preprocessing settings。
- Table 2-5，第 9 页：action recognition main results。
- Table 6-7，第 10 页：CPR results 和 preprocessing time。
- Table 10-13，第 11 页：eye tracking、ablation 和 inference time。

## 14. Draft Survey-Usable Sentences

Draft material: EventMamba treats event streams as temporally ordered Event Clouds rather than ordinary Point Clouds, highlighting that the event timestamp should be modeled as an explicit dynamic signal.

Draft material: Although non-spiking, EventMamba provides a useful point-based Mamba baseline for evaluating whether SNN architectures can preserve event sparsity while matching modern sequence models.

Draft material: Its reported gains on action recognition and regression tasks suggest that explicit temporal modeling is important for point-based event representations, but the evaluation protocol should be checked carefully before strong survey claims.
