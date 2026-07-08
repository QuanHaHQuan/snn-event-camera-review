---
title: "Rethinking Scale-Aware Temporal Encoding for Event-based Object Detection"
authors: ["Lin Zhu", "Tengyu Long", "Xiao Wang", "Lizhi Wang", "Hua Huang"]
year: 2025
venue: "NeurIPS"
level: "B"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/NeurIPS2025/B/2025-NEURIPS-B-rethinking-scale-aware-temporal-encoding-for-event-based-object-detection.md"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/d450dceeacd6083d1d550247377f2320-Abstract-Conference.html"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/file/d450dceeacd6083d1d550247377f2320-Paper-Conference.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["event camera", "object detection", "CNN-RNN", "temporal encoding", "Gen1", "1Mpx"]
---

# Summary V1｜Rethinking Scale-Aware Temporal Encoding for Event-based Object Detection

## 1. One-sentence Summary

这篇论文提出 CNN-RNN hybrid event detector，在低空间尺度引入 Decoupled Deformable-enhanced Recurrent Layers 和 scale-aware temporal encoding，以更早、更细地建模 event stream temporal dynamics。

## 2. Research Problem

论文处理 event-based object detection 中 temporal modeling 不足的问题。很多方法沿用 frame-based detection pipeline，只在高层语义特征上加入 temporal modules，导致事件最密集、细节最丰富的低层特征没有被充分时序建模。Transformer-based methods 虽能建模长程依赖，但复杂度较高，且可能忽略 fine-grained temporal cues。

这个问题与 SNN/Event Camera 综述相关，因为 SNN 的优势常被描述为早期、事件驱动、细粒度时间建模；该论文提供了一个非 SNN 的 CNN-RNN 对照，说明低层 temporal encoding 对事件检测也很重要。

## 3. Background and Motivation

Event cameras 异步记录像素亮度变化，具有 low latency、high dynamic range 和 sparse output。目标检测需要在 spatiotemporal event representation 上同时保留局部运动、尺度变化和目标语义。

现有 dense feed-forward detectors 往往先把事件转为 voxel grid，再用 CNN/Transformer 检测；sparsity-aware GNN/SNN 方法可直接处理事件，但优化或扩展存在挑战。论文动机是重新审视“temporal module 放在哪里”这一设计问题，认为低层/低尺度特征更适合捕捉事件密集区域的 temporal dynamics。

## 4. Method Overview

输入为 event representation，论文使用 50 ms time window 构造 5-channel voxel grid。整体 architecture 是 CNN-RNN hybrid detector：feature extractor 在较低 spatial scales 连续放置 recurrent layers；Decoupled Deformable-enhanced Recurrent Layer (DDRL/DDRB) decouple per-pixel motion estimation and feature fusion；多分支 backbone 独立做 temporal downsampling，最后通过 Feature Pyramid Network (FPN) 和 YOLOv6-style detection head 输出 bounding boxes/classes。

该方法不是 SNN，没有 spiking neuron。它是 event-based detection 的 dense CNN-RNN framework。

## 5. Technical Details

### Event Representation

事件被组织成 5-channel voxel grid，基于 50 ms time window。该 representation 保留一定时间结构，但仍是 dense tensor。

### Spiking Neuron / SNN Module

无。论文在 Related Work 和 Table 1 中包含 Spiking DenseNet 等 SNN baseline，但自身不是 spiking model。

### Network Architecture

关键是低层 recurrent temporal modeling。DDRL/DDRB 通过 deformable-enhanced mechanism 处理事件相机固有运动特性，分离 per-pixel motion estimation 和 feature fusion。多尺度分支分别下采样并保留不同尺度时序信息，最后用 FPN 融合。

### Training Strategy

训练使用 ADAM optimizer 和 OneCycle learning rate scheduler，采用 mixed batch training：部分样本用 standard BPTT，部分用 Truncated BPTT。数据增强包括 random horizontal flipping、zoom-in、zoom-out。Gen1 上 batch size 6、sequence length 21、learning rate 2e-4、400k iterations，单 RTX 3090 约 4 天。

### Loss Function

检测头使用 YOLOv6 detection head，包含 distribution focal loss、classification loss 和 regression loss。

### Inference Process

推理时 voxel grid sequence 经 CNN-RNN backbone 编码，低层 recurrent modules 保留细粒度 temporal information，多尺度特征经 FPN 融合后输出 detections。

## 6. Experiments

Datasets 包括 Gen1、1 Mpx 和 eTram。指标为 mAP 和 inference time。Gen1 为 304x240 event traffic dataset；1 Mpx 是高分辨率 automotive event dataset；eTram 为 roadside traffic monitoring dataset，约 10 小时、1280x720、约 2M bounding boxes、8 categories、30 Hz annotations。

Table 1 显示该方法在 Gen1 上 mAP 52.7、time 8.80 ms；在 1Mpx 上 mAP 49.1、time 13.3 ms。它高于 S5-ViT-B 的 Gen1 47.7 / 1Mpx 47.8，也高于 SAST-CB 的 48.2 / 48.7。Table 2 在 eTram 上该方法 mAP 33.0、time 13.05 ms，高于 RVT-B 29.5、SAST-CB 30.0、S5-ViT-B 29.3。

Ablation Table 3 比较 temporal information reuse：Base 为 50.7 mAP；Direct fusion cell 为 52.0；DDConv cell 为 52.7；DDConv + SE cell 仍为 52.7。Table 5 比较 backbone placement：High-level Temporal Modeling 为 49.5，Single-branch Encoding 为 51.3，RVT backbone 为 48.0，Ours 为 52.7，说明低层、多分支 temporal encoding 更有效。

## 7. Main Contributions

- 提出 CNN-RNN hybrid event detector，把 recurrent temporal modeling 放在较低 spatial scales。
- 提出 decoupled deformable-enhanced recurrent design，将 motion estimation 和 feature fusion 分开。
- 提出 scale-specific spatiotemporal encoding，通过多分支独立 downsampling + FPN 融合多尺度特征。
- 在 Gen1、1Mpx、eTram 上报告优于多种 Transformer/RNN/SSM/SNN baselines 的 mAP。

## 8. Limitations and Risks

论文不是 event-by-event sparse model，而是 voxel grid + dense CNN-RNN pipeline，因此可能不能完全保留事件稀疏性。训练成本较高，Gen1 训练约 4 天单 RTX 3090。方法依赖 BPTT/TBPTT 和 dense detection head，低功耗硬件友好性需要进一步验证。

对综述风险：该论文可证明 early temporal modeling 重要，但不能证明 SNN 本身更优；应作为 event-based detection background 和 non-spiking baseline。

## 9. Relation to SNN for Event Cameras

分类：B: Event Camera side background。

理由是论文直接研究 event-based object detection，且与 SNN baseline 对比，但核心方法为 CNN-RNN，没有 spiking component。它支持 survey 中关于 event detector architectures 和 temporal encoding 的背景讨论。

## 10. Relation to Survey Taxonomy

可支持的章节包括：

- Event representations for SNNs
- Event-based object detection
- Hybrid ANN-SNN models
- Efficiency, latency, and energy
- Datasets and benchmarks
- Open challenges

## 11. Key Terms and Concepts

- Scale-aware temporal encoding：在不同 spatial scales 独立建模 temporal dynamics。
- DDRL/DDRB：Decoupled Deformable-enhanced Recurrent Layer/Block。
- 5-channel voxel grid：基于 50 ms time window 的 event tensor representation。
- Mixed BPTT/TBPTT：混合完整反向传播和截断反向传播的训练策略。
- FPN：Feature Pyramid Network，用于多尺度检测特征融合。

## 12. Questions for Human Deep Reading

1. DDRL/DDRB 的数学形式和 deformable offset 如何计算？
2. 为什么低层 recurrent placement 比高层 placement 更适合 event data？
3. 5-channel voxel grid 是否会损失 polarity/time detail？
4. Table 1 的 time 是否包括 voxelization？
5. Mixed BPTT/TBPTT 对性能和显存的影响有无 ablation？
6. eTram 上类别分布和稀疏性是否与 Gen1/1Mpx 差异很大？
7. 与 Spiking DenseNet 的比较是否公平，输入和任务设置是否一致？
8. 是否有夜间、高速或小目标的细分结果？

## 13. Evidence Notes

- Abstract：描述 CNN-RNN hybrid、low-scale recurrent modules、DDRL 和 FPN。
- Contributions 段：三条贡献，明确 low spatial scales 和 divide-and-conquer temporal fusion。
- Table 1：Gen1 和 1Mpx SOTA 对比。
- Table 2：eTram 对比。
- Table 3：temporal information reuse ablation。
- Table 5：backbone placement/type ablation。
- Experiments/Datasets 段：5-channel voxel grid、50 ms window、YOLOv6 head、BPTT/TBPTT 训练设置。

## 14. Draft Survey-Usable Sentences

草稿句 1：Rethinking Scale-Aware Temporal Encoding suggests that event-based detection benefits from temporal modeling at early, low-resolution feature stages rather than only at high-level semantic layers.

草稿句 2：Although the method is not spiking, it provides a useful non-SNN baseline for discussing why fine-grained temporal encoding matters in event-camera object detection.

草稿句 3：Its voxel-grid CNN-RNN pipeline should be contrasted with SNN approaches that aim to preserve sparsity and event-driven computation more directly.
