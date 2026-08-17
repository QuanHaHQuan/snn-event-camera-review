---
tags: [SNN, quantization, efficiency, bit-budget, QSNN, neuromorphic-hardware, event-data]
---

# Summary V2｜Are Conventional SNNs Really Efficient? A Perspective from Network Quantization

## 1. Core Understanding

本文重新审视“conventional SNN 天然比 ANN 高效”这一常见判断。作者指出，既有工作常以 firing rate、timestep 和 Synaptic Operations（SOPs/SynOps）估计 SNN 成本，却忽略 weight precision、spike/state precision 与真实硬件实现；同时又经常把 SNN 与未经 quantization 或 pruning 的 full-precision ANN 比较，因此未必公平。

论文从 network quantization 建立统一视角：QANN activation 可拆成多个 binary bit planes，每个 bit plane 与 weight 的运算，在算术形式上类似 SNN 每个 timestep 的 binary spike-weight operation。二者都执行多个 binary partial computations 后再 integration；区别是 QANN 沿 bit-width 累积并带有 $2^t$ 的 bit significance，SNN 则沿 time 累积，并包含 membrane recurrence、threshold、leak 和 reset。因此论文建立的是 representation decomposition 与 operation accounting 层面的对应，不是神经动力学、信息容量或真实能耗的完全等价。

基于此，作者提出 Bit Budget：

$$
\mathrm{BB}
=
T\cdot b_w\cdot b_s,
$$

其中 $T$、$b_w$、$b_s$ 分别是 timestep、weight bit-width 和 spike-pattern bit-width。作者进一步提出 Quantitative SNN（QSNN），在固定 BB 下重新分配 temporal resolution 与 multi-bit spike/state representation，并用 S-ACE 与 NS-ACE 估计通用和 neuromorphic 场景的计算开销。

本文属于 **SNN efficiency evaluation、network quantization、spike coding/state representation、efficiency and hardware、open challenges**。SNN 是核心研究对象，但论文不是 event-camera architecture：neuromorphic datasets 主要用于验证 bit allocation，未提出 event representation、raw-event processing 或 event-specific downstream model。

## 2. Problem and Motivation

Binary spikes 和 event-driven execution 使 SNN 具备潜在硬件优势，但 binary communication 不等于整个模型只有 1-bit 成本。Weights、membrane states、normalization、memory access 和 repeated timesteps 仍可能使用较高精度。传统 SOP 通常近似依赖连接数、firing rate 与 $T$，却把 synaptic weight precision 视为固定；同样的 SOP 数在 1-bit 与 16-bit weights 下并不意味着相同 arithmetic 或 storage cost。

另一方面，modern ANN 已广泛使用 quantization、binary networks 和 pruning。如果 SNN 只与未优化 ANN 比较，所谓 efficiency advantage 可能来自不对称配置。随着 direct-trained SNN 已能在一两个 timesteps 上工作，SNN 与 quantized-activation ANN 的边界也更模糊：当 $T=1$ 且输出不再依赖长期 temporal dynamics 时，模型可能更像带 neuron state 和 threshold 的 quantized ANN。

作者由此提出两个问题：第一，如何在统一 precision-aware framework 中比较 SNN 与 QANN；第二，在固定计算/存储资源下，应把 bits 分配给更多 timesteps、更丰富 spike patterns，还是更高 weight precision。

## 3. Method Overview

### 3.1 SNN 与 QANN 的 bit-wise 对应

QANN 的 pre-activation 可写为：

$$
a_{\mathrm{pre},j}
=
\sum_{t=0}^{B-1}
2^t a_{\mathrm{pre},j}^{(t)},
\qquad
a_{\mathrm{pre},j}^{(t)}\in\{0,1\}.
$$

代入 weighted sum 并交换求和顺序：

$$
\sum_j w_j a_{\mathrm{pre},j}
=
\sum_{t=0}^{B-1}
2^t
\sum_j w_j a_{\mathrm{pre},j}^{(t)}.
$$

因此 multi-bit GeMM 可展开为多组 binary-input–weight operations，再通过 shift 和 accumulation 恢复结果。SNN 则在每个 timestep 计算 $\sum_j w_js_j[t]$ 并沿时间更新 membrane state。论文把 QANN bit plane 类比为 SNN timestep。原文用 $T$ 同时表示 bit indexing 和 timestep，且 Eq. (3) 写成 $t=0,\ldots,T$，与“$T$-bit”存在 $T+1$ 项的 indexing inconsistency：`Needs further check`。

### 3.2 QSNN 的输入、状态与输出

Conventional SNN 每步输出 $s\in\{0,1\}$；QSNN 将 membrane potential 量化为 multi-level spike pattern：

$$
s
=
\operatorname{round}
\left(
\frac{v}{v_{\mathrm{th}}}
\right)
v_{\mathrm{th}}.
$$

于是 $b_s>1$ 时，一个 timestep 可传递多个 discrete states，而不只表示 fire/no-fire。该输出更准确地说是 multi-bit quantized spike/state，并非 conventional binary neuronal spike。网络仍保留 membrane integration 和 temporal recurrence，但通信与 synaptic arithmetic 不再严格是 1-bit；因此 QSNN 是 SNN–QANN continuum 上的模型，不能把它无条件归为 conventional fully binary-spiking network。

在固定 BB 下，典型 allocation 包括 $T/b_s=4/1$、$2/2$ 和 $1/4$。前者强调 temporal resolution，后者强调单步 state precision。Eq. (6) 中时间范围含未在正文清楚定义的 $N$，且 reset 与 Eq. (7) quantization 的执行顺序不明确：`Needs further check`。

### 3.3 Weight quantization 与优化

Weights 通过 symmetric quantization 从 high-precision $w$ 映射到 $w_q$。论文目标不是提出新 quantizer，而是将 $b_w$ 纳入统一资源配置；训练仍优化原 task loss。正文声称 $\Delta=2^{T-1}$ 可使 $w_q\in[-1,1]$，但若 $T$ 仍是 timestep，该式缺少 clipping、归一化或 code-range 条件，可能存在符号复用或排版问题：`Needs further check`。

## 4. Key Components and Mechanisms

### 4.1 Bit Budget

BB 把单 synapse 的 temporal repetitions、weight precision 与 spike precision 相乘。它比 SOP 更适合比较 $1/4/1$、$1/2/2$、$1/1/4$ 等 allocation，但仍是简化 proxy：未显式包含 SRAM/DRAM access、routing、buffer、control logic、static power、并行度和 hardware utilization。Fig. 3 在作者测试的多个 Xilinx FPGA/frequency 上显示 single-synapse energy 与 BB 近似线性，但不同设备的斜率不同，因此不能外推为所有硬件上的通用 energy law。

### 4.2 S-ACE 与 NS-ACE

通用 Synaptic Arithmetic Computation Effort 为：

$$
\mathrm{S\text{-}ACE}
=
\sum_{w\in W,\,s\in S}
n_{w,s}\,\mathrm{BB},
$$

其中 $n_{w,s}$ 是对应 bit-width pair 的 MAC count。它是 **bit-aware theoretical arithmetic count/model-level proxy**，不是 runtime 或 joule measurement。

Neuromorphic variant 加入 firing rate：

$$
\mathrm{NS\text{-}ACE}
=
\sum_{w\in W,\,s\in S}
fr_s n_{w,s}\,\mathrm{BB}.
$$

它假设只有 spike event 触发显著 synaptic energy，适合可利用 sparsity 的 event-driven hardware；不能直接代表 dense GPU/CPU execution。Fig. 6 直接测量的是 firing rate，能效提升则是依赖该假设的推断。

### 4.3 数据类型决定 allocation

Static images 没有新的真实时间信息，重复更多 timesteps 可能不如提高单步 state precision。Neuromorphic data 则包含真实 temporal structure，过度减少 $T$ 会丢失事件动态。因此论文的设计原则不是固定使用 $T=1$，而是根据数据 temporal content 在 $T$ 与 $b_s$ 之间分配资源。

## 5. Experiments and Main Evidence

实验覆盖 ImageNet、CIFAR10/100、CIFAR10-DVS、DVS128 Gesture 和 N-Caltech101，并测试 convolutional 与 Spikformer architectures。

Static CIFAR 消融给出较清晰的 matched-budget evidence。在约 $3.08$–$3.69$ G S-ACE 下，$1/4/1$、$1/2/2$、$1/1/4$ 的 CIFAR10 accuracy 分别为 $95.00\%$、$94.43\%$、$93.91\%$；CIFAR100 为 $76.90\%$、$75.91\%$、$74.13\%$。这支持在该静态任务和配置中，增加 $b_s$ 比增加 $T$ 更有效，但并非所有 budget 都由 $T=1$ 最优：$4/2/2$ 在 CIFAR100 达到 $80.71\%$，高于 $4/4/1$ 的 $80.13\%$。

Event-data 结果呈 dataset-specific trade-off。固定 $b_w=1$ 时，CIFAR10-DVS 从 $1/1/16$ 的 $79.8\%$ 降到 $1/4/4$ 的 $63.1\%$ 和 $1/16/1$ 的 $35.8\%$，说明 temporal resolution 不能被 multi-bit state 替代。DVS Gesture 的最佳配置是 $1/2/8$、$98.48\%$；N-Caltech101 则是 $1/4/4$、$82.64\%$。因此数据不支持统一的“event data 应设 $T=4$”，只支持针对 dataset 平衡时间与状态精度。

FPGA 是本文最接近真实部署的证据，但报告的是 fps/latency 与 accuracy，不是完整 system energy。CIFAR10 在 Bit Budget 32 下，$8/1/4$、$8/2/2$、$8/4/1$ 的 fps 均约 342–344，而 accuracy 从 $95.45\%$ 增至 $96.41\%$；DVS-CIFAR10 在 Bit Budget 128 下 latency 均约 49.6，但从 $8/1/16$ 到 $8/8/2$，accuracy 由 $80.30\%$ 降至 $51.31\%$。这同时验证了固定 BB 下 hardware throughput 可相近，以及 allocation 对任务精度并不等价。

论文提到若干 SNN benchmark SOTA，但明确声明目标不是 overall SOTA。跨论文 ImageNet table 混合 architecture、training 和 precision；最可靠证据是相同模型内的 bit-allocation trade-off，而不是无条件的 overall-best claim。

## 6. Strengths and Limitations

**Strengths**

- 把 timestep、weight precision 和 spike precision 放入同一 resource framework，纠正只用 SOP/firing rate 评价 SNN 的盲点。
- 同时覆盖静态与 neuromorphic data，实验清楚显示二者需要不同 allocation。
- FPGA 测量为 BB–synaptic energy 相关性和 fixed-budget throughput 提供了硬件证据。
- 明确比较 accuracy、model size、S-ACE/NS-ACE 与 sparsity，而非只报告单一 operation count。

**Limitations**

- $T$-step SNN 与 $T$-bit QANN 只是 bit-wise arithmetic analogy；论文对 “functional equivalence” 的表述偏强。
- Eq. (3) indexing、Eq. (5) 的 $\Delta$、Eq. (6) 的 $N$ 和 reset/quantization 顺序存在未澄清问题。
- QSNN 输出 multi-bit state，降低了 conventional binary-spike communication 的纯粹性；硬件支持和额外编码成本说明不足。
- S-ACE/NS-ACE 是 model-level proxies；NS-ACE 依赖 non-spiking activity 能耗可忽略的假设。
- FPGA 结果主要报告吞吐/延迟与 accuracy，未完整报告 end-to-end hardware-measured energy、memory transfer 或 static power。
- Fig. 6 证明 allocation 改变 firing rate，不足以证明所有平台上的真实 energy 按比例下降。
- Event experiments 是 benchmark-level temporal tensors，论文没有建立 raw asynchronous event execution 或 neuromorphic-chip deployment。

## 7. Relation to Other Papers and Survey Taxonomy

本文主要路线是以 quantized-network bit decomposition 重构 SNN efficiency accounting，并把 multi-bit spike pattern、weight quantization 与 timestep 统一到 Bit Budget。对综述而言，它属于 Section 6 的 efficiency evaluation/open challenges，并连接 Section 3 的 spike coding 与 neuron representation；它不是 event representation 或 event-camera task architecture。

### PDF-verified literature relations

- **DoReFa-Net: Training Low Bitwidth Convolutional Neural Networks with Low Bitwidth Gradients (Shuchang Zhou et al., arXiv 2016)** — `foundation`。该工作代表 QANN 的 low-bit weights/activations/gradients 路线；本文将其 precision-aware 视角扩展到 SNN，并把 timestep 与 spike bit-width 纳入统一预算。对应 Section 6: efficiency evaluation。证据：Related Work, PDF p.2, citation/bibliography [43]。当前 active corpus 未覆盖。`candidate for backward search`。
- **Binarized Neural Networks: Training Deep Neural Networks with Weights and Activations Constrained to +1 or -1 (Matthieu Courbariaux et al., arXiv 2016)** — `foundation`。BNN 是单比特 weight/activation 的极端 QANN；本文以其为参照，说明 binary representation 并非 SNN 独有，并进一步比较 bit planes 与 temporal spikes。对应 Sections 3 and 6: spike coding and efficiency。证据：Related Work, PDF p.2, citation/bibliography [3]。当前 active corpus 未覆盖。`candidate for backward search`。
- **Spiking Deep Residual Networks (Yangfan Hu et al., TNNLS 2021)** — `baseline`。该工作既是 conventional deep SNN comparator，也是本文所批评的 SOP-based efficiency accounting 代表；本文增加 weight/spike precision 并在 Table 1 重新计算 S-ACE。对应 Section 6: efficiency metrics。证据：Related Work, PDF p.2, citation/bibliography [13]; Table 1, PDF p.7。当前 active corpus 未覆盖。`candidate for backward search`。
- **Exploiting High Performance Spiking Neural Networks with Efficient Spiking Patterns (Guobin Shen et al., arXiv 2023)** — `foundation`。该工作提供 burst/multi-state spike-pattern 基础；本文把这一表示与 timestep、weight bits 联合为可分配 Bit Budget。对应 Section 3: spike coding/state representation。证据：Method 3.2 Step-State Bit Allocation, PDF p.5, citation/bibliography [33]。当前 active corpus 未覆盖。`candidate for backward search`。
- **PokeBNN: A Binary Pursuit of Lightweight Accuracy (Yichi Zhang et al., CVPR 2022)** — `foundation`。本文明确借鉴其 computation-effort paradigm，并将 bit-aware arithmetic effort 改写为 S-ACE/NS-ACE，以覆盖 temporal repetitions 和 firing sparsity。对应 Section 6: quantized computation metrics。证据：Method 3.2 Computational Effort Estimates, PDF p.5, citation/bibliography [40]。当前 active corpus 未覆盖。`candidate for backward search`。
- **Spikformer: When Spiking Neural Network Meets Transformer (Zhaokun Zhou et al., arXiv 2022)** — `baseline`。Spikformer 是论文 Transformer-scale conventional SNN comparator；本文对其进行 weight/spike quantization 与 Bit Budget allocation，比较 accuracy、SOP、S-ACE 和 NS-ACE。对应 Sections 3 and 6: spiking architecture and efficiency。证据：Introduction/Related Work, PDF pp.1–2, citation/bibliography [44]; Table 1, PDF p.7。当前 active corpus 未覆盖。`candidate for backward search`。

## 8. Survey-Usable Takeaways

1. Binary spikes、低 firing rate、少 timesteps 或低 SOPs 都不足以单独证明真实 energy efficiency；至少还应报告 weight/state precision、memory cost、硬件和比较对象的 quantization status。
2. QANN bit plane 与 SNN timestep 都可形成 binary-input–weight operation，但 integration semantics 不同；不要把 arithmetic analogy 写成完整模型等价。
3. QSNN 将传统 binary spike 扩展为 multi-bit state，以更少 timesteps换取更强单步表示；这是一种 accuracy–temporal-resolution–communication-cost trade-off，而不是免费增益。
4. Static images 通常更受益于增加 spike/state precision；event data 必须保留足够 temporal resolution，最佳 allocation 具有 dataset specificity。
5. S-ACE 是 bit-aware arithmetic proxy，NS-ACE 是 firing-rate-adjusted neuromorphic proxy；二者都不能直接等同于 hardware-measured energy。
6. FPGA 数据支持相同 Bit Budget 下 throughput/latency 可接近，但也显示 event accuracy 可能因减少 $T$ 大幅下降；固定预算不意味着表示能力相同。
7. SNN sparsity 是可设计、可变化的 activity property，而不是看到 “SNN” 标签即可假定的固定能效优势。

## Supplement Points

### Questions and Clarifications

#### 1. QANN 中的 quantization step、bits 和 SNN timestep 分别怎样对应？

必须区分三个概念：$B$-bit activation 通常可编码至多 $2^B$ 个 quantization levels；quantization step size $\Delta_a$ 是相邻 levels 的数值间隔；bit plane 则是 binary code 中的单个位置。论文真正建立的是：

$$
\text{one QANN activation bit plane}
\longleftrightarrow
\text{one SNN timestep binary operation}.
$$

Quantization step size $\Delta_a$ 没有与 timestep 严格对应的变量；更接近 SNN threshold 或 state-quantization interval，但本文没有证明等价。论文写 “summation over $T$ quantization levels” 不严谨，Eq. (3) 实际分解的是 bit planes。若有 $B$ bits，应通常索引 $t=0,\ldots,B-1$；原文 $0,\ldots,T$ 与 “$T$-bit”不一致。

#### 2. Eq. (3) 的 bit-plane decomposition 如何工作？

以 $a_{\mathrm{pre}}=5=(101)_2$ 为例：

$$
5
=
1\cdot2^2+0\cdot2^1+1\cdot2^0.
$$

若 $w=3$，原始乘法为 $3\times5=15$；bit-wise 展开后：

$$
3\times5
=
2^2(3\times1)
+2^1(3\times0)
+2^0(3\times1)
=
12+0+3.
$$

对多个 inputs，把每个 activation 的同一 bit plane 收集起来：

$$
\sum_j w_j a_{\mathrm{pre},j}
=
\sum_t2^t\sum_jw_ja_{\mathrm{pre},j}^{(t)}.
$$

内层是 binary input 与 weight 的运算，外层用 $2^t$ shift-and-accumulate。SNN 每步同样计算 binary spike 与 weight，但 conventional temporal accumulation 没有天然 $2^t$ significance，并还有 leak/reset。因此两者局部运算相似，数值语义不等价。

#### 3. “Potential quantization 使 spike 携带更多信息”是什么意思？

Conventional spike 每步只有：

$$
s\in\{0,1\}.
$$

QSNN 对 membrane potential 分级量化，使单步输出可成为：

$$
s\in\{0,1,2,3\},
$$

或更多离散 states。四种状态需要 $b_s=2$ bits，因此每个 timestep 能区分更多 membrane levels。固定 $T\cdot b_s=4$ 时，可以选择 $T=4,b_s=1$、$T=2,b_s=2$ 或 $T=1,b_s=4$：资源从 temporal resolution 转移到 per-step state precision。

这类输出数学上是 multi-level quantized state，而非 conventional binary spike。它提高单步表示能力，同时增加 communication/arithmetic bit-width；论文通过 $b_s$ 将该成本计入 Bit Budget。对 static images 可能有利，但对 event data 过度减少 $T$ 会丢失真实时间信息。Eq. (6) 先写 reset、Eq. (7) 再量化的顺序也不清晰；若先 reset，高幅值信息会消失，因此实际代码顺序仍为 `Needs further check`。
