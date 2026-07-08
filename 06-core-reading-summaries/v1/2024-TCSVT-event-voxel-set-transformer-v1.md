---
title: "Event Voxel Set Transformer for Spatiotemporal Representation Learning on Event Streams"
authors: ["Bochen Xie", "Yongjian Deng", "Zhanpeng Shao", "Qingsong Xu", "Youfu Li"]
year: 2024
venue: "TCSVT"
level: "B"
priority: "SECNet reference-only"
advisor_track: "yes"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "SECNet references / 00-index/reading-plan-core.md"
official_page: "https://doi.org/10.1109/TCSVT.2024.3448615"
pdf_link: "https://arxiv.org/pdf/2303.03856"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["event camera", "EVSTr", "voxel set", "transformer", "action recognition", "object classification", "NeuroHAR", "SECNet reference"]
---

# Summary V1｜Event Voxel Set Transformer for Spatiotemporal Representation Learning on Event Streams

## 1. One-sentence Summary

EVSTr 将 event streams 表示为 event voxel sets，并用 MNEL、VSAL 和 S2TM 组成的 transformer-style architecture 学习 local-to-global spatiotemporal representations，用于 event-based object classification 和 action recognition。

## 2. Research Problem

本文解决 event-based recognition 中 sparse event representation 的高效建模问题。frame-based methods 把 events 投影为 dense frames，计算复杂度高且破坏 sparse/asynchronous nature；point/graph methods 虽然更稀疏，但可能缺少 robust local aggregation 和 long-range feature interaction。

作者目标是在保持 sparse representation 的同时，引入 transformer-style global modeling 和 multi-scale local aggregation，让 event voxel representation 同时适合 short-duration object classification 和 long-duration action recognition。

## 3. Background and Motivation

event cameras 输出 sparse asynchronous events，每个 event 包含 spatial location、timestamp 和 polarity。对于 recognition tasks，短时事件可用于 object classification，长时事件需要建模 motion dynamics。

existing point-based / voxel-wise methods 多关注 local graph convolution，可能没有充分利用 neighbor positional/semantic relations，也缺少全局 feature interaction。EVSTr 的动机是把 event voxel set 作为稀疏输入，再用 attention-aware encoder 从 local 到 global 学习表示。

## 4. Method Overview

EVSTr pipeline 是：将 event stream 转成 event voxel set；用 event voxel transformer encoder 处理每个 voxel set；encoder 由 Multi-Scale Neighbor Embedding Layer (MNEL)、voxel sampling 和 Voxel Self-Attention Layer (VSAL) 构成；对于 object classification，encoder output 直接进入 classification head；对于 action recognition，先把长 event stream 切成多个 segments，每个 segment 转成 voxel set，再用 Stream-Segment Temporal Modeling Module (S2TM) 聚合长程时间动态。

输入是 event stream / event voxel set。输出是 object class 或 action class。本文不是 SNN，而是 sparse voxel-set transformer。

## 5. Technical Details

### Event Representation

EVSTr 采用 event voxel set representation。事件流先被划分到 3D voxel grid，保留 non-empty voxels；每个 voxel 包含 feature `f_i` 和 spatiotemporal coordinate `c_i`。这种表示比单点更稳健，能在 voxel 内聚合局部事件语义。

### Spiking Neuron / SNN Module

本文没有 spiking neuron 或 SNN module。MotionSNN 只作为 action recognition baseline 出现。

### Network Architecture

MNEL 对每个 voxel 的 k-nearest neighbors 做 multi-scale neighbor embedding，并结合 positional 和 semantic relations 生成 attention scores，实现 local information aggregation。VSAL 在 voxel tokens 之间做 self-attention，并加入 absolute positional embedding 和 relative position bias，提升 global feature interaction。

S2TM 用于 action recognition：长 event stream 被切分为 `K` 个 segments，每段由共享 encoder 提取 feature，然后用 temporal modeling function 聚合。默认使用 self-attention。

### Training Strategy

Object classification 使用 cross-entropy loss、SGD with momentum、batch size 32、250 epochs、cosine annealing。Action recognition 使用 300 epochs、batch size 16、cross-entropy loss 和 cosine annealing。

### Loss Function

论文主要使用 standard cross-entropy classification loss。创新集中在 representation、encoder 和 temporal modeling，不在新 loss。

### Inference Process

推理时 object classification 将整段或 substream 转成 single voxel set；action recognition 将 stream 切为多个 voxel sets，通过 shared encoder 和 S2TM 产生 final action prediction。

## 6. Experiments

Object classification 数据集包括 N-Caltech101、CIFAR10-DVS、N-Cars 和 ASL-DVS。Table I 报告 EVSTr 在 N-Caltech101 79.7%、CIFAR10-DVS 73.1%、N-Cars 94.1%、ASL-DVS 99.7%。在 no pre-training point-based comparison 中，它在 N-Caltech101、CIFAR10-DVS 和 ASL-DVS 上表现很强，但 N-Cars 低于若干 baselines。

Table II 报告 object classification complexity：EVSTr 为 0.93M params、0.34G MACs、6.62ms average inference time，在 N-Caltech101 上保持高 accuracy 和低 complexity。

Action recognition 数据集包括 UCF101-DVS、HMDB51-DVS、DvsGesture、DailyAction 和作者新提出的 NeuroHAR。NeuroHAR 包含 1584 samples、18 classes、3 modalities，在 low-light illumination 和 camera motion 条件下采集。

Table IV 报告 action recognition：EVSTr 在 UCF101-DVS 73.5%、HMDB51-DVS 60.7%、DvsGesture 98.6%、DailyAction 99.6%、NeuroHAR 89.4%。在 real-world datasets 上超过多种 frame-based 和 point-based methods；在 converted datasets 上对 heavyweight frame-based methods 是 competitive。

Table V 在 DailyAction 上报告 complexity：EVSTr 为 2.88M params、1.38G MACs、41 samples/s；比 I3D/TANet/TimeSformer 轻得多，但比 VMV-GCN 更重且 throughput 更低。

Ablation：Table VI 显示 multi-scale embedding 和 attentive feature aggregation 都有贡献；Table VII 显示 absolute-relative positional encoding 最好；Table VIII 显示 S2TM 对 action recognition 关键，self-attention 在 NeuroHAR 上最佳；Table IX 显示在 NeuroHAR 上 EVSTr event-only 无 pre-training 达到 89.4%，参数和 MACs 明显低于 I3D event input。

## 7. Main Contributions

1. 提出 EVSTr，用 event voxel set 保持 event sparsity 并进行 spatiotemporal representation learning。
2. 设计 MNEL，用 multi-scale attentive neighbor aggregation 学习 robust local voxel features。
3. 设计 VSAL，用 absolute-relative positional encoding 支持 voxel-level global self-attention。
4. 提出 S2TM，把 segmented voxel sets 用于 long-duration action recognition。
5. 提出 NeuroHAR dataset，用 low-light 和 camera motion 条件评估 event-based action recognition。

## 8. Limitations and Risks

本文不是 SNN；survey 中不能把 EVSTr 归为 spiking model。

EVSTr 在 action recognition 中比 VMV-GCN 更重，DailyAction throughput 也更低；“low complexity”主要相对 frame-based heavy models 成立。

NeuroHAR 是作者新数据集，虽然设计更实际，但需要人工核验公开可用性、split 和是否被后续工作采用。

Table I 中 N-Cars 结果不是所有方法中最高，survey 需按 dataset 分别陈述。

## 9. Relation to SNN for Event Cameras

分类：B: Event Camera side background；advisor-track support。

EVSTr 提供了 voxel-set transformer baseline，可用于和 SNN / point-SNN / SECNet 比较 event representation、local/global aggregation 和 long-range temporal modeling。它不是 SNN，但属于 event-camera representation and architecture background。

## 10. Relation to Survey Taxonomy

- Event representations for SNNs：event voxel set。
- SNN architectures for event cameras：作为 non-spiking sparse transformer 对照。
- Event-based action recognition：DvsGesture、DailyAction、NeuroHAR 等。
- Datasets and benchmarks：NeuroHAR。
- Efficiency, latency, and energy：params、MACs、throughput、inference time。
- Open challenges：sparse attention cost、dataset realism、long-range temporal modeling。

## 11. Key Terms and Concepts

- EVSTr：Event Voxel Set Transformer。
- Event voxel set：non-empty voxels with features and spatiotemporal coordinates。
- MNEL：Multi-Scale Neighbor Embedding Layer，用于 local aggregation。
- VSAL：Voxel Self-Attention Layer，用于 global feature interaction。
- S2TM：Stream-Segment Temporal Modeling Module，用于 action recognition。
- NeuroHAR：包含 event/RGB/depth 的 challenging human action dataset。

## 12. Questions for Human Deep Reading

1. EVSTr 的 voxel set construction 与 VMV-GCN / Voxel Graph CNN 的差异是什么？
2. MNEL 的 attention score 如何融合 positional 和 semantic relations？
3. VSAL 的 absolute positional embedding 与 relative position bias 具体如何定义？
4. Table IV 中 converted datasets 的 random 20% split 是否可复现？
5. NeuroHAR 的 public link 当前是否仍有效？
6. EVSTr 与 SECNet 比较时，应该强调 voxel set 还是 transformer encoder？
7. 0.34G MACs 和 6.62ms 是否包含 voxelization？
8. S2TM 的 self-attention 在更长 event streams 上是否仍高效？

## 13. Evidence Notes

- Abstract，第 1 页：提出 EVSTr、MNEL、VSAL、S2TM 和 NeuroHAR。
- Section I，第 2 页：列出三条 contributions。
- Fig. 3，第 5 页：object classification / action recognition pipeline。
- Section IV-A / Table I-II，第 8 页：object classification results and complexity。
- Section IV-B / Table IV-V，第 10-11 页：action recognition results and complexity。
- Table VI-IX，第 11-12 页：MNEL、VSAL、S2TM 和 modality ablations。

## 14. Draft Survey-Usable Sentences

Draft material: EVSTr is a representative sparse voxel-set transformer that keeps event data in a non-dense representation while adding both local neighbor aggregation and global attention.

Draft material: For SNN surveys, EVSTr is useful as a non-spiking baseline showing how voxelized event streams can support both object classification and action recognition.

Draft material: Its NeuroHAR dataset contribution is also relevant for discussing evaluation under low-light and camera-motion conditions, although dataset adoption should be checked before making broad claims.
