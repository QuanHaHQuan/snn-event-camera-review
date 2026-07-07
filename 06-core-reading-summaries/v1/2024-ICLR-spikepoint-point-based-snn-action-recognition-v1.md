---
title: "SpikePoint: An Efficient Point-based Spiking Neural Network for Event Cameras Action Recognition"
authors: ["Hongwei Ren", "Yue Zhou", "Xiaopeng Lin", "Yulong Huang", "Haotian Fu", "Jie Song", "Bojun Cheng"]
year: 2024
venue: "ICLR"
level: "A"
priority: "P0"
advisor_track: "yes"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/ICLR2024/A/2024-ICLR-A-spikepoint-an-efficient-point-based-spiking-neural-network-for-event-cameras-action-recogn.md"
official_page: "https://proceedings.iclr.cc/paper_files/paper/2024/hash/75f1a165c7561e028c41d42fa6286a76-Abstract-Conference.html"
pdf_link: "https://proceedings.iclr.cc/paper_files/paper/2024/file/75f1a165c7561e028c41d42fa6286a76-Paper-Conference.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["SNN", "event camera", "action recognition", "point cloud", "SpikePoint", "DVS128 Gesture", "Daily DVS", "UCF101-DVS"]
---

# Summary V1｜SpikePoint: An Efficient Point-based Spiking Neural Network for Event Cameras Action Recognition

## 1. One-sentence Summary

SpikePoint 提出 point-based end-to-end SNN，把 event camera action data 表示为 pseudo point cloud，并用 singular-stage SNN 同时提取 local/global features，实现高精度、低参数和低功耗的 event-based action recognition。

## 2. Research Problem

本文解决 event camera action recognition 中“事件表示与 SNN 计算范式不匹配”的问题。许多方法把 asynchronous events 转成 frames / voxels，再用 ANN 或 frame-oriented SNN 处理，这会带来额外 mapping cost，并损失 event sparsity。

对 SNN + event cameras 来说，理想方法应直接利用 sparse event cloud，避免把事件数据变成 dense frames。SpikePoint 的目标是用 point cloud-style representation 保留事件的稀疏性，同时用 SNN 进行低功耗识别。

## 3. Background and Motivation

event cameras 只在亮度变化时产生事件，天然形成稀疏时空点集。Point Cloud 形式能保留 `(x, y, t)` 信息，并减少 dense rasterization。SNN 通过 spike-based communication 适合低功耗处理，但常见 deep hierarchical point network 结构不适合 SNN，因为 spike features 会随深度变得稀疏且难训练。

因此作者设计 singular-stage SNN architecture，并专门处理 rate encoding 下负相对坐标的问题。

## 4. Method Overview

SpikePoint 的 pipeline 是：将 event stream 转成 pseudo Point Cloud；随机采样固定数量的 points；用 FPS 和 KNN 做 grouping；构造相对位置与 centroid/min-coordinate 分支；对 point coordinates 进行 rate encoding；用 SNN local feature extractor 和 global feature extractor 提取特征；最终 classifier 输出 action class。

输入是 event cloud data，主要包含 spatial coordinates 和 time information。输出是 action recognition label。模型是 full spike event-based network，训练使用 surrogate training / BPTT，而不是 ANN-to-SNN conversion。

## 5. Technical Details

### Event Representation

事件被表示为 pseudo point cloud，每个点包含 `(x, y, t)`。模型用 random sampling 统一输入点数，再用 Farthest Point Sampling (FPS) 选 group centroid，并用 KNN 取 group members。

### Spiking Neuron / SNN Module

论文使用 LIF neurons，并给出 spike firing、synaptic summation 和 membrane potential update 公式。输入 coordinates 通过 rate encoding 转为 binary spikes。

### Network Architecture

SpikePoint 采用 singular-stage structure，而不是多阶段 hierarchical PointNet++ 风格结构。它包含 local feature extractor 与 global feature extractor。local extractor 用双分支处理 `[|dx|, |dy|, |dt|, xmin, ymin, zmin]` 和 centroid information；global extractor 通过 ResF units 和 max pooling 建模 group-level features。

### Training Strategy

模型使用 surrogate gradient / BPTT 训练。作者提出 ResF / ResFB residual feature units，缓解 SNN 中 gradient vanishing 和 overfitting。对于 small / large datasets 使用相同架构但不同 feature dimension scale。

### Loss Function

正文主要是 standard classification training，未把新 loss 作为核心贡献。关键技术在 point grouping、negative-value handling、singular-stage architecture 和 residual SNN feature extractor。

### Inference Process

推理时输入固定数量采样点，在 16 timesteps 下进行 rate-encoded SNN inference。Table 7 还报告了 IBM gesture / DVS128 Gesture 上的 operation、dynamic/static energy comparison。

## 6. Experiments

数据集包括 DVS128 Gesture、Daily DVS、DVS Action、HMDB51-DVS 和 UCF101-DVS。Table 1 给出每个数据集类别数、sensor、平均长度、train/test split、sliding window 和 overlap。

Table 2 在 DVS128 Gesture 上报告 SpikePoint 0.58M params，98.74% accuracy，高于多种 SNN baselines，低于 TBR+I3D 的 99.6%，但参数远少于 TBR+I3D 的 12.25M。

Table 3 在 Daily DVS 上报告 SpikePoint 0.16M params，97.92% accuracy，超过 I3D、TANet、VMV-GCN 和 SNN baselines。Table 4 在 DVS Action 上达到 90.6%，高于 ST-EVNet 88.7% 和 SNN baselines。

Table 5 在 HMDB51-DVS 上达到 55.6%，0.79M params，高于 RG-CNN 51.5%。Table 6 在 UCF101-DVS 上达到 68.46%，1.05M params，是 SNN methods 中最强，但低于 ECSNet-SES 的 70.2%。

Table 7 报告 DVS128 Gesture energy：SpikePoint 16 timesteps，98.7% accuracy，0.9G OPs，0.82 mJ dynamic energy，0.58M params，0.756 mJ static energy；相比 TBR+I3D 178.6 mJ dynamic、160.23 mJ static 显著更低。

Table 8/9 做 grouping 和 timesteps ablation。DailyDVS 在 16 timesteps 达到 97.92%，DVS Action 在 16 timesteps 达到 90.6%；更多 timesteps 不一定更好。

## 7. Main Contributions

1. 提出 point-based SNN architecture，直接处理 event cloud data。
2. 设计适配 SNN rate encoding 的 point grouping 和 negative-value handling。
3. 提出 singular-stage SNN structure，避免 hierarchical SNN point features 过度稀疏。
4. 设计 local/global feature extractors 和 ResF/ResFB units。
5. 在五个 event-based action recognition datasets 上展示高精度、低参数和低功耗。

## 8. Limitations and Risks

SpikePoint 对 random sampling 依赖较强；作者在 DVS Action 分析中指出背景噪声过多时 random sampling 会采到很多 noise，需要 preprocessing。

UCF101-DVS 上 SpikePoint 低于强 ANN ECSNet-SES，因此不能说在所有方法上全面 SOTA。

energy 计算细节在 appendix，V1 只确认正文 Table 7 值，硬件实测和部署结论需进一步核验。

Point cloud representation 是否适合 detection / tracking / dense prediction 仍未验证。

## 9. Relation to SNN for Event Cameras

分类：A: SNN + Event Camera core paper，advisor-track support。

它是非常典型的 event camera + SNN core paper：输入是 event cloud，模型是 point-based SNN，任务是 event-based action recognition，并明确围绕 sparsity、timesteps、energy 展开。

## 10. Relation to Survey Taxonomy

- Event representations for SNNs：point cloud / event cloud。
- SNN architectures for event cameras：singular-stage point-based SNN。
- Event-based action recognition：五个 action datasets。
- Efficiency, latency, and energy：operation、dynamic/static energy、timesteps。
- Open challenges：noise-sensitive sampling、extension to other tasks。

## 11. Key Terms and Concepts

- SpikePoint：point-based SNN for event camera action recognition。
- pseudo Point Cloud：把 event stream 组织为 `(x, y, t)` 点集。
- FPS / KNN：point grouping 方法。
- ResF / ResFB：SNN residual feature extraction units。
- Rate encoding：把 coordinates 转为 spike input。
- Dynamic/static energy：推理计算和参数存储相关能耗。

## 12. Questions for Human Deep Reading

1. random sampling 在高噪声数据上的失败模式有多严重？
2. preprocessing 对 DVS Action 的提升是否影响公平性？
3. Table 7 energy 如何计算，是否包含 memory access？
4. point grouping 参数 N、M、N' 如何设置？
5. singular-stage 结构是否限制深层语义建模？
6. SpikePoint 是否可用于 event-based detection/tracking？
7. 16 timesteps 是全局最优还是经验选择？
8. advisor-track 中为什么重点关注此文：是 point representation 还是 low-power SNN？

## 13. Evidence Notes

- Abstract：说明 point-based SNN、16 timesteps、0.3% params / 0.5% power claims。
- Section 3.2-3.3，第 4-6 页：sampling/grouping、singular-stage、LIF/ResF。
- Table 1，第 6 页：datasets。
- Table 2-7，第 7-8 页：main benchmark and energy。
- Table 8-9，第 9 页：grouping/timestep ablation。
- Conclusion，第 9 页：总结 full spike event-based network。

## 14. Draft Survey-Usable Sentences

Draft material: SpikePoint is a strong example of preserving event sparsity by treating event streams as point clouds rather than dense frames.

Draft material: Its singular-stage design reflects a practical architectural adaptation for SNNs, where hierarchical point networks may suffer from sparse and indistinguishable spike features.

Draft material: The method is especially relevant to low-power event-based action recognition, though its robustness to noisy sampling needs careful discussion.

