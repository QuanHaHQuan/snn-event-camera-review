---
title: "Spiking Vision Transformer with Saccadic Attention"
authors: ["Shuai Wang", "Malu Zhang", "Dehao Zhang", "Ammar Belatreche", "Yichen Xiao", "Yu Liang", "Yimeng Shan", "Qian Sun", "Enqi Zhang", "Yang Yang"]
year: 2025
venue: "ICLR"
level: "C"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/ICLR2025/C/2025-ICLR-C-spiking-vision-transformer-with-saccadic-attention.md"
official_page: "https://proceedings.iclr.cc/paper_files/paper/2025/hash/3c85f70d3fd83f4fba47e117e5429f35-Abstract-Conference.html"
pdf_link: "https://proceedings.iclr.cc/paper_files/paper/2025/file/3c85f70d3fd83f4fba47e117e5429f35-Paper-Conference.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["SNN", "Spiking Vision Transformer", "saccadic attention", "neuromorphic vision"]
---

# Summary V1｜Spiking Vision Transformer with Saccadic Attention

## 1. One-sentence Summary

Spiking Vision Transformer with Saccadic Attention 提出 Saccadic Spike Self-Attention (SSSA)，以 spike-distribution relevance 和 saccadic spiking neuron 建模 spatial-temporal attention，并以 SSSA-V2 将 attention 化为 linear-complexity、spike-driven computation。

## 2. Research Problem

SNN-based Vision Transformer 常沿用 ANN self-attention：binary sparse `Q`、`K` 的 magnitude distribution 不匹配，dot product 难可靠衡量 spatial relevance；同时多数 spike attention 将各 timestep 独立处理，仅依赖 LIF leak/reset，难保留 long-range temporal interaction。

已有显式 spatio-temporal attention 可缓解第二点，却有高达 `O(T^2 N^2 D)` 的 cost。论文试图同时改善 attention quality 和 edge-friendly compute，而不是为某个 event-camera task 专门设计网络。

## 3. Background and Motivation

SNN 用 multiple simulation timesteps 和 binary spikes 表达视觉输入。对 static image，常将同一 image repeat 后 spike encode；对 event stream，则将 `(x,y,t,p)` 以 temporal binning 转为 event frames。Vanilla ViT 的 `QK^T` 对连续 normalized features 有效，但 spike `Q/K` 的 firing-rate distribution 会破坏这一假设。

作者借鉴 biological saccade：视觉系统在不同瞬间关注 subset of salient patches，再随时间形成完整 context。该类 temporal selection 与 event-camera/SNN 的 asynchronous processing 有概念关联，但论文的主要 task 仍是 image/event-frame classification。

## 4. Method Overview

SNN-ViT 由 Global-Local Spiking Patch Splitting (GL-SPS) embedding、若干 SSSA-based Transformer blocks、GAP 和 classification head 组成。GL-SPS 用 standard convolution 和 dilated convolution 提取 multi-scale tokens；blocks 采用 SSSA-V2 和 linear/MLP residual path。

SSSA 先对 spike `Q/K` 的 firing distributions 计算 cross-entropy-inspired relevance，再对 patch salience 进行 saccadic temporal interaction；其 saccadic neuron 用 learnable lower-triangular temporal matrix。SSSA-V2 将 matrix terms 重新结合为 threshold scaling，推理时只依赖当前 timestep，输出仍为 spikes。

## 5. Technical Details

### Event Representation / Input

event input `e=[x,y,t,p]` 先按 target temporal resolution 聚合：连续 `alpha` 个 raw bins 的 events 相加为一个 two-polarity event frame。static image 则重复 `T` times 并经 Spiking_Embed 转为 spike sequence。论文未提出新的 raw-event encoding；这种 binning 会把 asynchronous events 变为 discrete frame sequence。

### Problem Analysis

作者认为 LIF reset/decay 导致 historical information 很快遗忘，且 spike vector magnitude 的强波动使 dot-product relevance 失真。SSSA 以每个 patch 的 firing-rate distribution 近似其 Bernoulli distribution，用 cross entropy 的 negative value 表示 relevance；为避免 log/nonlinear cost，进一步用 spike sums `Q'`、`K'` 给出可计算的近似。

### Saccadic Spiking Neuron

由 `CroAtt(Q,K)` row sum 得到每 patch 的 salience。训练时，saccadic neuron 以 learnable lower-triangular `M_w` 对所有 timestamps 做 `H = M_w Patch`，再 threshold firing；`M_w` 让不同历史 timestep 有可学习的 contribution，并规避普通 LIF reset/decay 的 temporal forgetting。

inference 时，论文将 `M_w^{-1}` 并入 threshold，使 `H[t]` 只取 current `Patch[t]`，从而不必保持完整 history。该 decoupling 是其“asynchronous inference”论据，但训练时的 parallel matrix operation 和 threshold inversion 的 numerical details需要 V2 进一步核验。

### SSSA-V2 and Architecture

原 SSSA 仍会计算 `Q' K'^T`。SSSA-V2 利用 associative rearrangement：将 `K'^T L` 视为 threshold 的 scaling factor `alpha`，只对 `M_w Q'` 和 current threshold 操作，论文给出 total attention complexity `O(2D+N)`。GL-SPS 将 standard and dilated convolution features 相加；完整 SNN-ViT 用 SSSA-V2 block 后接 GAP/classifier。

### Training / Output

模型是 direct-trained SNN-ViT，论文未在主文逐项列出 surrogate function 或 total loss beyond classification setup，需核对 appendix/code。输出为 image/event-frame classification label；remote-sensing experiments 另将 SNN-ViT 用作 YOLO-v3 backbone。

## 6. Experiments

### Datasets and Metrics

image classification 包括 CIFAR-10、CIFAR-100、ImageNet-1K、CIFAR10-DVS；另在 NWPU VHR-10 和 SSDD 做 remote object detection。主要报告 accuracy、parameter count、computational complexity 与 theoretical energy；ImageNet setting 使用 `224 x 224` inputs、batch size 128、310 epochs。

### Main Results

Table 1：SNN-ViT 在 CIFAR-10、CIFAR-100、CIFAR10-DVS 分别为 `96.1%`、`80.1%`、`82.3%`，model sizes 分别为 `5.57M`、`5.57M`、`1.52M`。CIFAR10-DVS 相比 Table 1 中的 STSA `79.9%` higher，但不同 architecture/setting 的公平性仍需核查。

ImageNet Table 2 报告 SNN-ViT-8-384 为 `30.4M` parameters、`20.83 mJ`、`76.87%`，SNN-ViT-8-512 为 `53.7M`、`35.75 mJ`、`80.23%`，均用 `T=4`。作者主张 SSSA-V2 使模型以 linear attention complexity 达到 competitive/SOTA SNN-ViT results。

### Ablations

正文 ablation 表明：将 baseline attention 换为 SSSA 约增加 `2.65%`，GL-SPS 约增加 `0.93%`，两者同时替换约增加 `3.15%`（论文在对应 setting 中的 summary）。这支持 modules 的联合效应，但完整 baseline configuration、seeds 和 variance 应由人工读表核验。

## 7. Main Contributions

1. 分析 vanilla dot-product attention 对 spike `Q/K` 的 spatial relevance mismatch 与 temporal-interaction deficit。
2. 提出 SSSA，以 distribution-based relevance 和 saccadic temporal selection 面向 spatio-temporal spikes。
3. 提出 SSSA-V2，用 threshold scaling 获得 `O(2D+N)` linear attention form 和 current-timestep inference。
4. 构建 GL-SPS + SSSA-V2 的 SNN-ViT，并在 static/neuromorphic classification 和 detection 评估。

## 8. Limitations and Risks

event stream 首先 temporal binning，故不是 strictly event-by-event asynchronous pipeline。论文没有证明 SSSA 的 inference decoupling 在真实 neuromorphic hardware、variable-rate event stream 下的 latency/energy，也未给出完整 device measurements。

cross-entropy-to-linear-spike-sum 的 approximation 是方法假设；其对 firing rate calibration、rare spikes 和 long sequences 的误差需要额外分析。主要 benchmark 是 classification，不能直接推出 event tracking/detection robustness。

## 9. Relation to SNN for Event Cameras

分类：C: SNN side background。

论文在 CIFAR10-DVS 处理 event frames，且关注 SNN temporal attention，因此可支持 event-camera SNN 的 Transformer/attention taxonomy；但它没有针对 raw event stream 或具体 event-camera application 提出核心机制，属于可迁移的 SNN architecture background。

## 10. Relation to Survey Taxonomy

- SNN architectures for event cameras：SSSA/SSSA-V2 的 spike-based attention。
- Event representations for SNNs：temporal binning 为 two-polarity event frames。
- SNN training methods：parallel temporal training 与 threshold-decoupled inference。
- Efficiency, latency, and energy：linear-complexity attention、theoretical energy。
- Surrogate gradient and temporal credit assignment：learnable temporal matrix 取代单纯 LIF memory。
- Open challenges：event-frame conversion、long-context stability、hardware validation。

## 11. Key Terms and Concepts

- SSSA：Saccadic Spike Self-Attention，本文 attention mechanism。
- SSSA-V2：SSSA 的 linear-complexity, threshold-scaled variant。
- CroAtt：cross-entropy-inspired relevance computation for spike `Q/K`。
- saccadic spiking neuron：以 `M_w` 建模 temporal patch interaction 的 neuron。
- `M_w`：learnable lower-triangular temporal interaction matrix。
- GL-SPS：Global-Local Spiking Patch Splitting，多尺度 spiking patch embedding。
- CIFAR10-DVS：event-camera classification benchmark。

## 12. Questions for Human Deep Reading

1. `Q'`、`K'` 的 sum dimension、normalization 和 firing-rate estimate 在 code 中如何实现？
2. `M_w` 是否要求可逆，如何 regularize its inverse and threshold stability？
3. SSSA-V2 的“linear scaling mapping”是 exact equivalence、proportional approximation 还是只保持 ranking？
4. saccadic patch mask 是否采用 hard spike、soft training surrogate，salient-patch sparsity 实际是多少？
5. CIFAR10-DVS 的 time bins、T=16、augmentation 和 prior methods是否一致？
6. ImageNet mJ 如何计算，是否计入 GL-SPS、residual addition、BN、threshold scaling？
7. remote-sensing detection 的 SNN-ViT-YOLO training recipe 与 conventional YOLO baseline如何比较？
8. 若输入是 irregular event timestamps 而非 binned frames，SSSA 的 temporal matrix 如何适配？

## 13. Evidence Notes

- Abstract 与 Section 1，第 1-2 页：attention mismatch、SSSA、SSSA-V2、overall claims。
- Section 3，第 3-4 页：`Q/K` magnitude mismatch、LIF temporal forgetting、existing complexity。
- Section 4.1-4.3 / Eq. (5)-(11)，第 5-7 页：distribution relevance、saccadic neuron、linear attention derivation。
- Section 5 / Eq. (12)-(16)，第 7-8 页：GL-SPS 和 SNN-ViT pipeline。
- Section 6 / Tables 1-4，第 8-10 页：classification, ImageNet, detection and ablations。

## 14. Draft Survey-Usable Sentences

Draft material: SSSA is a spike-attention design that replaces vanilla dot-product relevance with a firing-distribution-based approximation and uses saccadic temporal selection.

Draft material: Its SSSA-V2 formulation illustrates one approach to linearizing spike attention by moving temporal interaction into an adaptive firing threshold.

Draft material: Since its event input is temporally binned before SNN processing, the paper should be cited as an SNN-attention background method rather than evidence of fully asynchronous event-camera inference.
