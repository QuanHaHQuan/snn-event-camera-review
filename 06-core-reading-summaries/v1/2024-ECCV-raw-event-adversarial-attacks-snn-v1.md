---
title: "Exploring Vulnerabilities in Spiking Neural Networks: Direct Adversarial Attacks on Raw Event Data"
authors: ["Yanmeng Yao", "Xiaohan Zhao", "Bin Gu"]
year: 2024
venue: "ECCV"
level: "A"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/ECCV2024/A/2024-ECCV-A-exploring-vulnerabilities-in-spiking-neural-networks-direct-adversarial-attacks-on-raw-eve.md"
official_page: "https://eccv.ecva.net/virtual/2024/poster/1447"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/09164.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["SNN", "DVS", "raw event data", "adversarial attack", "Gumbel-Softmax", "CIFAR10-DVS", "DVS Gesture", "N-MNIST"]
---

# Summary V1｜Exploring Vulnerabilities in Spiking Neural Networks: Direct Adversarial Attacks on Raw Event Data

## 1. One-sentence Summary

本文提出一种直接攻击 raw event data 的 SNN adversarial attack，通过 Gumbel-Softmax / probabilistic sampling 和 efficient position selection，把离散三值事件优化转化为可优化过程，并在多个 DVS 数据集上显著提高 targeted attack success rate。

## 2. Research Problem

论文研究 SNN 在处理 event camera / DVS 数据时的安全性，核心问题是：现有 adversarial attacks 多攻击 grid-based event representation，而真实 pipeline 可能只暴露 raw event data 接口，攻击者无法访问中间 grid representation。

raw event data 由事件坐标、timestamp 和 polarity 组成，具有高时间分辨率、稀疏性和离散取值。直接在 raw event 上攻击比在 image 或 grid representation 上更难，因为优化空间巨大，并且事件值是离散的，扰动还要保持 sparsity 和 imperceptibility。

## 3. Background and Motivation

DVS 输出异步事件，常以 COO format 存储。SNN 适合处理 binary spike sequences，因此 DVS + SNN 是低功耗视觉系统的重要组合。许多 SNN pipeline 会把 raw events 转为 binary / continuous grid representation，但这个转换步骤在真实系统里可能不可访问。

已有 SpikeFool、Spike-Compatible 等方法主要面向 binary grid representation。论文认为这会造成攻击面错位：如果模型接口只接收 raw events，那么攻击 grid 的方法无法直接使用，也难以保证从 grid 反推到 raw events 后的 sparsity 与有效性。

## 4. Method Overview

方法直接对 raw event indices 和 event values 进行 targeted adversarial attack。输入是原始事件集合 E，包含 event indices I 和 values V。作者把离散事件值视为 categorical distribution 的 samples，用 soft probability alpha 进行连续优化，forward 时采样 hard values，backward 时用 straight-through estimator 传播梯度。

为了避免全事件空间优化，方法把 original events 与 target-label sample 的 positions 合并，只在这个较小的 candidate position set 上优化。最后通过 sparsity norm / event-count constraint 控制 adversarial event data 与原始事件的差异。

## 5. Technical Details

### Event Representation

raw event data 以 COO-like format 存储，每个事件包含 spatial-temporal index 和 polarity value。论文区分 continuous grid representation、binary grid representation 和 raw event data；本文贡献集中在 raw events。

### Spiking Neuron / SNN Module

被攻击模型包括 SEW ResNet-34 和 Spiking ResNet-18。论文介绍 SNN 的 temporal forward、SEW ResNet residual block，以及 binary spikes across time 的处理方式。

### Network Architecture

论文不是提出新 SNN architecture，而是构造针对已有 SNN classifier 的 attack pipeline。SNN classifier 接收 raw events 或 grid representation，输出类别预测。

### Training Strategy

攻击优化使用 sampled event values 和 straight-through estimator。Algorithm 1 描述 adversarial sample generation：初始化 alpha，合并 original / target indices，多次采样 forward，计算 attack loss，backward 更新 alpha，若达到 target label 则返回 adversarial sample。

### Loss Function

攻击目标包含 classification loss 与 dense representation distance penalty。MSE 被用来衡量 adversarial sample 和 original sample 在 dense representation 上的差异。论文还约束 adversarial event count 在合理范围内，以保持 raw event sparsity。

### Inference Process

在攻击时，生成的 adversarial raw event data 直接送入 SNN model，无需访问 grid representation。对于 binary grid representation，论文也给出对比实验，以说明方法在更简单表示上仍有效。

## 6. Experiments

数据集包括 CIFAR10-DVS、DVS Gesture 和 N-MNIST。论文从每个数据集中随机选择 100 个 correctly classified samples 进行 targeted attacks。模型包括 SEW ResNet-34 和 Spiking ResNet-18；grid representation 使用 16 frames。

Table 2 报告模型 clean accuracy：例如 CIFAR10-DVS 上 SEW ResNet-34 为 67.20%，Spiking ResNet-18 为 68.36%；DVS Gesture 上分别为 89.06% 和 93.75%；N-MNIST 上分别为 99.06% 和 98.95%。binary-frame trained variants 也列出。

Table 3 是 raw event attack 结果。相比 FGSM，本文方法在三个数据集和两个模型上均显著提高 ASR，同时降低 event modification ratio Δ。例如 CIFAR10-DVS 上，SEW ResNet-34 的 FGSM ASR 为 19.70%，本文方法为 72.23%；Spiking ResNet-18 上 FGSM 为 16.90%，本文为 64.79%。DVS Gesture 上 SEW ResNet-34 达到 86.67% ASR，N-MNIST 上 Spiking ResNet-18 达到 78.57% ASR。

Table 4 是 binary grid representation attack comparison。本文方法与 Spike-Compatible 接近，并明显优于 SpikeFool；但作者强调 binary grid attack 比 raw event attack 更简单。

Table 5 分析 straight-through estimator：soft continuous values 能达到更高 ASR，但 hard binary values 才符合真实 event value 约束，显示连续优化和离散可执行扰动之间存在 gap。

## 7. Main Contributions

1. 首次系统研究直接针对 raw event data 的 SNN adversarial attack。
2. 用 probabilistic sampling / Gumbel-Softmax 思路处理 raw event values 的离散三值优化。
3. 通过 target-position merging 减小优化空间并保留攻击有效性。
4. 引入 sparsity-aware constraints，使 adversarial raw events 不至于破坏事件流稀疏特征。
5. 在 CIFAR10-DVS、DVS Gesture、N-MNIST 上展示 raw event attack 明显优于 FGSM baseline。

## 8. Limitations and Risks

实验只选取每个数据集 100 个 correctly classified samples，统计稳定性和更大规模评估需要人工核验。

方法主要是 targeted attack，实际安全风险需要结合 threat model：攻击者是否能插入 target-label sample positions、是否能访问模型梯度、是否能控制 raw event stream。

clean accuracy 在 CIFAR10-DVS 上不高，攻击结果可能受模型强弱影响。

直接攻击 raw events 的可感知性难以用 image-domain imperceptibility 完全衡量；MSE 和 Δ 只是近似指标。

## 9. Relation to SNN for Event Cameras

分类：A: SNN + Event Camera core paper。

论文不提出 event-camera perception model，但直接研究 DVS raw event data 上的 SNN vulnerability，是 SNN for event cameras 综述中 robustness / security / adversarial risks 的核心支撑。

## 10. Relation to Survey Taxonomy

- SNN training methods：surrogate gradient / BPTT 作为攻击背景。
- Event representations for SNNs：raw events vs grid representations。
- Open challenges：SNN robustness and adversarial security。
- Datasets and benchmarks：CIFAR10-DVS、DVS Gesture、N-MNIST。
- Efficiency, latency, and energy：间接相关，攻击保持 sparsity 以避免明显事件数量变化。

## 11. Key Terms and Concepts

- Raw event data：事件坐标、时间和 polarity 的原始表示。
- Grid-based representation：把事件聚合成 frame/grid 后输入模型。
- Gumbel-Softmax / probabilistic sampling：把离散事件值转为可优化概率。
- Straight-through estimator：forward 用 hard value，backward 近似传梯度。
- ASR：Attack Success Rate。
- Delta / Δ：相对事件增删比例。

## 12. Questions for Human Deep Reading

1. target-label sample positions 的使用是否符合现实 attack threat model？
2. Gumbel-Softmax 的具体温度或采样参数如何影响 ASR？
3. raw event attack 对 event timing 是否做修改，还是主要修改 polarity / candidate positions？
4. Δ 与视觉/事件可感知性之间是否有更直观的可视化？
5. 100 samples 是否足以支持结论？
6. Table 4 中本文方法略低于 Spike-Compatible 的场景如何解释？
7. 防御方法是否能检测 event count 或 polarity distribution 异常？
8. 代码能否复现 Table 3 的 ASR/MSE/Δ？

## 13. Evidence Notes

- Section 3.1，第 6-8 页：formulate grid and raw event attacks。
- Figure 3，第 7 页：展示 raw event attack pipeline。
- Algorithm 1，第 9 页：adversarial sample generation。
- Section 4.1，第 10 页：datasets、models、baseline。
- Table 2，第 11 页：model accuracy。
- Table 3-5，第 12-14 页：raw event attack、binary grid attack、straight-through estimator analysis。
- Conclusion，第 14 页：总结 direct raw event attack。

## 14. Draft Survey-Usable Sentences

Draft material: This work shows that SNNs for DVS inputs can be vulnerable not only at grid-based representations but also at the raw event interface.

Draft material: By optimizing probabilistic event values and selecting a compact attack position set, the method exposes a security risk specific to sparse asynchronous event streams.

Draft material: For survey writing, this paper should be used cautiously as a robustness paper rather than a perception architecture paper.

