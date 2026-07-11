---
title: "P-SPIKESSM: HARNESSING PROBABILISTIC SPIKING STATE SPACE MODELS FOR LONG-RANGE DEPENDENCY TASKS"
authors: ["Malyaban Bal", "Abhronil Sengupta"]
year: 2025
venue: "ICLR"
level: "C"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/ICLR2025/C/2025-ICLR-C-p-spikessm-harnessing-probabilistic-spiking-state-space-models-for-long-range-dependency-t.md"
official_page: "https://proceedings.iclr.cc/paper_files/paper/2025/hash/b75ce884441c983f7357a312ffa02a3c-Abstract-Conference.html"
pdf_link: "https://proceedings.iclr.cc/paper_files/paper/2025/file/b75ce884441c983f7357a312ffa02a3c-Paper-Conference.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["SNN", "State Space Model", "long-range dependency", "probabilistic spiking"]
---

# Summary V1｜P-SPIKESSM: HARNESSING PROBABILISTIC SPIKING STATE SPACE MODELS FOR LONG-RANGE DEPENDENCY TASKS

## 1. One-sentence Summary

P-SpikeSSM 将每个 spiking neuron 的 membrane state 扩展为 State Space Model (SSM) 的多维 hidden state，以 Bernoulli SpikeSampler、stochastic surrogate、SpikeMixer 和 ClampFuse 构成可并行训练的 long-range sequence SNN。

## 2. Research Problem

传统 LIF neuron 只有 scalar membrane potential，且其 Heaviside firing 和 recurrent state update 通常要求按 time step 顺序处理及 Backpropagation Through Time (BPTT)。作者认为这使 SNN 难以学习 Long Range Arena (LRA) 一类长上下文依赖，也削弱其训练可扩展性。

论文要解决的问题不是 event-camera perception，而是如何在保持 spike communication 的前提下，让 SNN 获得 SSM 对长序列的建模和 parallel computation 能力。它将现有“SSM 输出后再接 LIF”的路线视为仍有 sequential bottleneck 或 real-valued MAC overhead 的方案。

## 3. Background and Motivation

SSM 以 hidden state 的线性 dynamics 表达序列，常可把 recurrence 重写为 convolution；LIF 则通过 leak、integration 和 threshold firing 表达时间状态。作者的动机是把前者的高维 memory 与卷积形式移到 neuron 内部，而非把它当作一个 ANN-like preprocessor。

对于本 survey，论文的价值在于解释一个可能适配 event stream 的 temporal SNN building block：event 的时间尺度长、稀疏且动态跨度大时，scalar LIF state 未必足以编码长依赖。该论文本身没有 event camera dataset 或 event-specific representation。

## 4. Method Overview

real-valued input sequence 先被 encoder 转换为 `N` spike trains。每个 P-SpikeSSM neuron 对应一条 spike train，并以自身的 SSM parameters 计算 firing probability；SpikeSampler 按该概率采样 binary spike。层内 spike population 经 SpikeMixer 交换信息，ClampFuse 做聚合和 residual fusion，再产生下一层的 spike probability；decoder 将最后的 spiking features 映射到 task output。

核心设计是把 hidden-state recurrence 等价为对 spike sequence 的 non-circular convolution，因此 time dimension 可以并行计算。模型输入是一般 sequence，不是 event camera 的 `(x, y, t, p)`；输出随任务而变，为 classification prediction。

## 5. Technical Details

### Spiking Neuron / SSM Module

每个 neuron 以 input spike `x_s(t)` 驱动连续 SSM：`h_dot(t) = A h(t) + B x_s(t)`，并由 `p_s(t) = clamp(a C h(t) + b)` 给出 firing probability。`h(t)` 是 `n`-dimensional state，不同 neuron 可学习不同的 `A, B, C`，因此其 temporal memory 比 LIF 的单一 membrane value 更丰富。

离散化后，`h[t] = A_bar h[t-1] + B_bar x_s[t]`。作者将它展开为 kernel `K = (CB, CAB, ..., CA^(L-1)B)` 与输入 spike sequence 的 convolution；其意义是把 sequential recurrence 改成可并行的 convolution，且 sparse zero spikes 理论上可跳过不必要运算。

### SpikeSampler and Surrogate

SpikeSampler 令 `S_t` 为 Bernoulli random variable：当 uniform random value 小于 `p_s[t]` 时发放 spike。它可同时在 neuron population 和 sequence positions 上采样。由于 stochastic binary sampling 不可微，作者用其 expectation `E[S_t] = p_s[t]` 构造面向随机采样的 surrogate gradient，而不是直接对 deterministic Heaviside 求导。

### Network Architecture

SpikeMixer 对同层 neuron population 的 spikes 做 mixing，补足独立 neuron 之间的 communication；ClampFuse 在 fusion 后以 clamped probability 生成供下一 P-SpikeSSM layer 使用的 spike sequence，并加入 residual connection。Figure 1 给出 `K` 个 P-SpikeSSM encoder layers、encoder/decoder 和 layer-wise activity sparsity。

### Training and Efficiency

论文以 convolutional formulation 避免完整 BPTT 的 sequential execution，并报告标准 gradient-based training。其效率主张主要是 sparse spike-driven convolution 可减少 floating-point MAC、改用 ACC，以及没有额外 simulation time steps；论文没有在 neuromorphic chip 上实测 end-to-end energy。

## 6. Experiments

### Tasks and Baselines

实验覆盖 LRA 的 long-range sequence tasks、permuted sequential MNIST (psMNIST)、Speech Commands 的 SC10 subset，并在 appendix 报告 sequential CIFAR-10。比较对象包含 spiking 和 non-spiking Transformer/SSM/LMU-style sequence models。

### Main Results

论文称 P-SpikeSSM 在所列 LRA tasks 上达到 SNN model 中的 strongest results，并在 psMNIST、SC10 上比较长依赖建模。正文还报告：在 psMNIST，stochastic P-SpikeSSM 为 `98.4%`，将同一输入转给 LIF-based spike generation 的对照为 `97.7%`；其一次训练约 `1.5 minutes`，对照 LIF model 约 `6.1 minutes`。这些是论文设置内的比较，不应概括为任何 sequence task 的普适速度倍率。

### Ablations and Efficiency

Table 5 检查 stochastic surrogate、SpikeMixer、GELU-to-ReLU 的 hardware-friendly variant 和可学习 `sigma`。Figure 1(b,c) 展示 ListOps 上 single neuron 与 layer-wise active neuron ratio 的稀疏 firing pattern。论文的 energy analysis 是 operation-level estimate，不包括完整 memory I/O 或 chip implementation。

## 7. Main Contributions

1. 提出以 SSM multi-dimensional hidden state 表示 membrane dynamics 的 probabilistic spiking neuron。
2. 将该 dynamics 改写成 spike-sequence convolution，并以 Bernoulli SpikeSampler 支持 parallel spike generation。
3. 提出 stochastic surrogate、SpikeMixer 和 ClampFuse，使 P-SpikeSSM 可堆叠为多层 sequence model。
4. 在 LRA、psMNIST 和 SC10 上验证 long-range sequence performance，并报告 activity sparsity 与训练时间对比。

## 8. Limitations and Risks

论文没有直接处理 event camera，因而不能以其 LRA/psMNIST evidence 推断 event-based detection 或 tracking effectiveness。SSM kernel 的实际 implementation、sequence length 增长时的 memory/FFT cost、随机采样 variance 与 hardware mapping 仍需结合 code 进一步核验。

其 energy discussion 是基于 MAC/ACC 与 sparsity 的分析，并非 measured device energy；SpikeMixer、ClampFuse、random sampling 和 memory transfer 的系统代价没有完整计入。与 LIF 的训练时间比较也只在特定 psMNIST configuration 上成立。

## 9. Relation to SNN for Event Cameras

分类：C: SNN side background。

P-SpikeSSM 不使用 event camera，但为“如何让 SNN 保留长程 temporal context”提供 neuron/architecture 设计参考。对 event-camera SNN，可作为 LIF memory limitation、SSM-inspired spiking dynamics 和 parallel temporal learning 的背景文献，而非 event-camera method evidence。

## 10. Relation to Survey Taxonomy

- SNN architectures for event cameras：可作为 SSM-inspired spiking neuron 的架构背景。
- SNN training methods：parallel convolutional training、stochastic surrogate 和 BPTT alternative。
- Surrogate gradient and temporal credit assignment：stochastic SpikeSampler 的 gradient treatment。
- Efficiency, latency, and energy：sparsity、MAC-to-ACC argument 与其证据边界。
- Open challenges：long-range memory、randomness、hardware realization。

## 11. Key Terms and Concepts

- P-SpikeSSM：Probabilistic Spiking State Space Model，本文的 neuron/model family。
- SSM：State Space Model，以 state transition 表达 temporal dynamics。
- SpikeSampler：按 learned firing probability 作 Bernoulli sampling 的 layer。
- SpikeMixer：对 neuron population spikes 进行 inter-neuron mixing 的模块。
- ClampFuse：聚合 features、限制到 probability range 并提供 residual fusion 的模块。
- LRA：Long Range Arena，长上下文 sequence benchmark。
- BPTT：Backpropagation Through Time，recurrent/SNN 的 standard temporal gradient procedure。

## 12. Questions for Human Deep Reading

1. Appendix 中 `A, B, C` 的 parameterization 是否采用 S4/Mamba-style structured kernel，计算复杂度具体为何？
2. SpikeSampler 的 randomness 在训练和 inference 是否共享 seed、是否使用 reparameterization 或 variance reduction？
3. stochastic surrogate 的精确公式与 gradient stability range 是什么？
4. SpikeMixer 和 ClampFuse 的 channel dimension、activation、normalization 和 parameter cost 分别是多少？
5. LRA 每个 task 的 exact scores、model size、sequence length 与 baseline 是否完全可比？
6. 1.5 versus 6.1 minutes 是否包含 data loading、compile/warm-up，hardware 是什么？
7. 是哪一种 operation-level energy model 支撑其 efficiency figures，是否计入 SSM kernel storage？
8. 若输入为 raw event stream，如何把 irregular timestamps 编码为 input spike trains，是否仍能保留异步性？

## 13. Evidence Notes

- Abstract 与 Section 1，第 1-2 页：问题、SpikeSampler、surrogate、SpikeMixer/ClampFuse、LRA/psMNIST/SC10 的总体声明。
- Figure 1，第 3 页：encoder-layer pipeline 与 ListOps layer-wise spike sparsity。
- Section 3.1 / Eq. (1)-(7)，第 4-6 页：SSM neuron、convolution reformulation、Bernoulli sampling。
- Section 4 与 Table 1-5，第 7-10 页：benchmarks、performance、ablation 与 training comparison。
- Appendix D，第 16 页附近：sequential CIFAR-10 追加结果；正文应避免把它当主要 benchmark。

## 14. Draft Survey-Usable Sentences

Draft material: P-SpikeSSM replaces the scalar LIF state with an SSM state and samples spikes from a learned probability, offering a parallelizable route to long-context spiking sequence modeling.

Draft material: Although the method is not event-camera-specific, its convolutional formulation of spike-state dynamics is relevant to the long-range temporal-memory problem in event-stream SNNs.

Draft material: The reported efficiency evidence is operation-level and task-specific; it should not be presented as a measured energy advantage on event-camera hardware.
