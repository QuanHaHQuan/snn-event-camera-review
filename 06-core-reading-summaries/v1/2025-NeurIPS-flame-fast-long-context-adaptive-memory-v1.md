---
title: "FLAME: Fast Long-context Adaptive Memory for Event-based Vision"
authors: ["Biswadeep Chakraborty", "Saibal Mukhopadhyay"]
year: 2025
venue: "NeurIPS"
level: "A"
priority: "P0"
advisor_track: "yes"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/NeurIPS2025/A/2025-NEURIPS-A-flame-fast-long-context-adaptive-memory-for-event-based-vision.md"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/1b71649968436c64a765e469ab6b615c-Abstract-Conference.html"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/file/1b71649968436c64a765e469ab6b615c-Paper-Conference.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["event camera", "SNN", "LIF", "state space model", "HiPPO", "event-by-event processing"]
---

# Summary V1｜FLAME: Fast Long-context Adaptive Memory for Event-based Vision

## 1. One-sentence Summary

FLAME 用 LIF-style Event Attention Layer 结合 Event-Aware HiPPO state-space memory，面向 asynchronous event streams 做 event-by-event 长上下文建模，并试图在 event-based vision 任务上取得 accuracy、FLOPs 和 latency 的折中。

## 2. Research Problem

这篇论文处理的问题是：event cameras 输出稀疏、异步、时间跨度可能很长的 event stream，传统 voxel/frame 聚合会牺牲 event-by-event 的时间精度并增加计算，而直接逐事件处理的方法又常常难以保持长程上下文和高精度。这个问题对 SNN + Event Camera 综述很关键，因为它正好位于 neuromorphic event sensing、spiking-style temporal dynamics 和 sequence modeling 的交叉处。

论文认为已有 GNN、Transformer、SNN 或 SSM 方法各有短板：一些方法需要把事件聚合成密集表示，一些方法缺少动态 memory retention，一些方法虽能异步更新但长上下文能力不足。FLAME 的动机是保留 event stream 的稀疏异步属性，同时用 state-space memory 处理远距离时序依赖。

## 3. Background and Motivation

Event cameras 只在像素亮度变化时输出事件，事件通常写成 `(x, y, t, p)`，其中 `p` 表示 polarity。它们适合高速、低延迟、低功耗视觉，但处理上不能简单套用固定帧率图像模型。

SNN 侧的背景是 LIF neuron 可以用膜电位积分和阈值发放来捕捉时序动态，天然适合事件流。SSM/HiPPO 侧的背景是 state-space methods 可以压缩历史输入、建模长序列，但标准 HiPPO 假设连续或规则采样输入，未必适合稀疏异步事件。FLAME 的动机就是把 LIF-style front-end 和 event-aware SSM memory 组合起来。

## 4. Method Overview

整体 pipeline 是：输入 raw asynchronous events `(x, y, t, p)`；先经过 Event Attention Layer (EAL)，用多分支 LIF dynamics 提取不同时间尺度的事件特征；再通过轻量 convolution/pooling 得到较小的 event feature vector；核心 EA-HiPPO Convolution Layer 根据 inter-event interval `Delta t` 动态调节 memory retention；最后用 LayerNorm 和 Readout Layer 输出分类结果。

该方法不是纯 SNN。它含有明确的 spiking/neuro-inspired component，即 EAL 中的 LIF dynamics；核心 memory 是 SSM/HiPPO 变体，并通过 NPLR decomposition 和 FFT-style computation 降低计算代价。因此它更准确地说是 SNN-inspired + SSM hybrid event model。

## 5. Technical Details

### Event Representation

论文强调直接处理 asynchronous event stream，而不是完全依赖固定窗口的 dense voxel representation。事件先被 EAL 转换成多尺度 spike-like feature，再进入后续 SSM。

### Spiking Neuron / SNN Module

EAL 使用 multi-branch Leaky Integrate-and-Fire (LIF) dynamics。不同 branch 对应不同 decay/time constant，用来对短期和长期事件变化做响应。这里的公式含义是：膜电位随时间泄漏，并在输入事件到达时被更新；不同时间常数可以看作不同的 temporal filters。

### Network Architecture

FLAME 包括 EAL、两个 convolutional blocks、spatial pooling、EA-HiPPO Convolution Layer、LayerNorm 和 fully connected readout。Table 4 给出 Tiny/Small/Normal 三个规模：EAL 分支数从 16 到 64，readout neurons 从 256 到 1024。

### Training Strategy

论文报告了 PyTorch 实现，并在 event vision benchmarks 上训练和评估。训练超参数主要放在 appendix；V1 阶段需要人工复核具体 optimizer、epoch 和 batch settings。

### Loss Function

主任务为分类，readout 使用 softmax；论文正文没有把 loss 作为核心创新点，默认可理解为 task-specific classification loss。细节需人工核对 appendix。

### Inference Process

推理时模型随事件到达更新 internal state，EA-HiPPO 根据 `Delta t` 调整状态转移。NPLR decomposition 将 dense state update 的复杂度从 `O(N^2)` 降到近似 `O(Nr)`，其中 `r << N`，用于降低逐事件长序列处理成本。

## 6. Experiments

论文在多个 event-based vision datasets 上评估，包括 CIFAR10-DVS、N-Caltech101、DVS128 Gesture、HAR-DVS 和 CeleX-HAR。任务以 event-based classification/action recognition 为主。

Table 2 报告 FLAME-Normal 与 SOTA 的 accuracy/FLOPs 对比：CIFAR10-DVS 上 FLAME-Normal 为 80.5% / 0.43 GFLOPs；N-Caltech101 为 70.5% / 1.34 GFLOPs；DVS128 Gesture 为 96.5% / 0.43 GFLOPs；HAR-DVS 为 88.29% / 0.41 GFLOPs；CeleX-HAR 为 72.2% / 0.41 GFLOPs。论文特别强调在 CeleX-HAR 上接近 EVMamba 72.3% accuracy，但计算量从 37.2 GFLOPs 降到 0.41 GFLOPs。

Table 3 对 HAR-DVS 做更细比较：FLAME-Tiny 65.42%、FLAME-Small 79.36%、FLAME-Normal 88.29%，低于 ExACT 的 90.10%，但计算量更低。Figure 2 和 Figure 3 用 accuracy-vs-GFLOPs、accuracy-vs-latency 展示效率折中。Ablation 部分讨论移除 EAL、替换 EA-HiPPO 等会带来 accuracy drop。

## 7. Main Contributions

- 提出 FLAME，把 LIF-based Event Attention Layer 和 Event-Aware HiPPO SSM memory 组合用于 event stream。
- 提出 EA-HiPPO，用 inter-event interval 动态调节 memory retention，以适配异步、稀疏事件。
- 使用 NPLR decomposition 降低 SSM state update 的计算复杂度。
- 在多个 event datasets 上展示 accuracy-efficiency trade-off，尤其强调高分辨率 CeleX-HAR 上的低 GFLOPs。

## 8. Limitations and Risks

论文自己在 Conclusion 中指出：当前 FLAME 虽然在 GPU 上有较高吞吐，但还不能满足 CPU-only real-time constraints；模型偏 static offline training，缺少 on-device continual learning；event-driven 模型仍可能受 sensor noise 影响；EA-HiPPO 不是纯 spiking neuromorphic mechanism，因此不能直接等同于端到端 native SNN。

对综述使用的风险是：论文把 FLAME 归入 SNN + Event Camera 时要谨慎，因为核心 memory 是 SSM 而非纯 SNN；它更适合作为 hybrid neuro-inspired event model，而不是完全 spike-only architecture。

## 9. Relation to SNN for Event Cameras

分类：A: SNN + Event Camera core paper。

理由是论文明确处理 event camera stream，并含有 LIF-based Event Attention Layer；但同时需要标注它是 SNN-inspired + SSM hybrid，不是纯 SNN。它能支持综述中“事件流上 spiking dynamics 与 SSM/long-context modeling 的结合”这一方向。

## 10. Relation to Survey Taxonomy

可支持的章节包括：

- Event representations for SNNs
- SNN architectures for event cameras
- Hybrid ANN-SNN models
- SNN training methods
- Efficiency, latency, and energy
- Open challenges

## 11. Key Terms and Concepts

- Event Attention Layer (EAL)：使用多分支 LIF dynamics 从 raw event stream 中提取多时间尺度特征。
- LIF neuron：通过泄漏积分和阈值发放建模时序事件响应。
- Event-Aware HiPPO (EA-HiPPO)：将 HiPPO/SSM 的 memory mechanism 改造成对 inter-event interval 敏感的形式。
- NPLR decomposition：Normal Plus Low Rank decomposition，用于降低 state update 复杂度。
- Event-by-event processing：不把事件完全聚合成固定帧，而是在事件到达时更新模型状态。
- CeleX-HAR：高分辨率 event-based human action recognition benchmark。

## 12. Questions for Human Deep Reading

1. EAL 中 LIF dynamics 是否真正产生 binary spikes，还是主要作为 continuous filter 使用？
2. EA-HiPPO 与标准 S4/HiPPO 的数学差异是否足够清晰？
3. Table 2 中不同 baselines 的 FLOPs 计算口径是否一致？
4. FLAME 在 N-Caltech101 上 accuracy 明显低于 SOTA，论文如何解释？
5. 论文中的 latency 是 GPU latency、per-event latency 还是 per-sequence latency？
6. Ablation 中 EAL、EA-HiPPO、NPLR 各自贡献是否稳定跨 dataset？
7. 该方法是否能部署到 neuromorphic hardware，还是主要面向 conventional GPU？
8. 对 noisy event streams 的鲁棒性有没有实验支持？

## 13. Evidence Notes

- Abstract：定义 FLAME、EAL、EA-HiPPO 和 NPLR complexity claim。
- Figure 1：展示整体 architecture、EAL、EA-HiPPO 和 NPLR/FFT-based convolution。
- Table 1：定性比较 FLAME 与 GNN、Transformer、SNN、SSM methods。
- Table 2：CIFAR10-DVS、N-Caltech101、DVS128 Gesture、HAR-DVS、CeleX-HAR 的 accuracy/FLOPs。
- Table 3：HAR-DVS 上 FLAME variants 与 video/action baselines。
- Conclusion：明确列出 CPU-only real-time、continual learning、noise sensitivity、非纯 spiking algorithm 等限制。

## 14. Draft Survey-Usable Sentences

草稿句 1：FLAME illustrates a hybrid route for event-camera SNN research: a LIF-based event front-end can be paired with event-aware state-space memory to retain long temporal context while preserving event-by-event processing.

草稿句 2：Although FLAME is not a fully spiking architecture, its Event Attention Layer makes it relevant to neuromorphic event processing and highlights the growing overlap between SNN-inspired dynamics and SSM-based sequence modeling.

草稿句 3：For survey use, FLAME should be discussed cautiously as a hybrid SNN-inspired/SSM method rather than as evidence that purely spiking networks alone solve long-context event modeling.
