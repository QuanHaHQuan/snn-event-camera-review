---
tags: [SNN, neuron-model, CLIF, temporal-modeling, surrogate-gradient, BPTT, neuromorphic-classification]
---

# Summary V2｜CLIF: Complementary Leaky Integrate-and-Fire Neuron for Spiking Neural Networks

## 1. Core Understanding

CLIF 是一种面向 surrogate gradient（SG）direct training 的 SNN neuron model。论文的核心问题不是重新设计 surrogate function，而是解释：即使已经用 surrogate gradient 绕过 binary spike function 不可微的问题，vanilla Leaky Integrate-and-Fire（LIF）neuron 的 temporal gradient 为什么仍难以跨越较多 timesteps，并由此限制 SNN 的训练效果。

作者将 LIF 的 temporal-gradient vanishing 分成两个来源。第一，membrane leak 使每一步状态 derivative 都带有 $0 < \gamma < 1$ 的衰减系数，跨越 $t' - t$ 个 timesteps 后形成 $\gamma^{t' - t}$。第二，在论文采用的 soft reset 和 rectangular surrogate gradient 下，相邻 membrane states 的 total derivative 可能精确变为零，使包含该 timestep 的整条 temporal path 被截断。

为此，作者提出 Complementary Leaky Integrate-and-Fire（CLIF）neuron。CLIF 在传统 membrane potential $u[t]$ 之外引入连续内部状态 complementary potential $m[t]$。$m[t]$ 同时受近期 membrane potential 和 spike activity 影响，并控制 firing 后的额外 reset strength。在 forward 中，这产生类似 spike-frequency adaptation 的动力学并降低 firing rate；在 backward 中，$m[t]$ 形成不完全依赖 LIF membrane-only recurrence 的额外 temporal-gradient paths。

CLIF 对下一层仍输出 binary spike $s[t] \in \{0, 1\}$，不增加 learnable neuron parameters，也不改变分类 loss；network weights 仍通过 SG+BPTT 优化。因此本文属于 **Core SNN、SNN neuron dynamics、temporal modeling 和 training method**。论文明确确认了 binary spike communication，但没有对所有实验配置的 input encoder、readout 和 classifier 是否都严格 spiking 给出统一说明，因此整个网络在所有设置中是否严格 fully spiking 为 `Needs further check`。

## 2. Problem and Motivation

SNN 的 spiking mechanism 使用 Heaviside function：

$$
s^l[t]
=
\Theta\left(u^l[t] - V_{\mathrm{th}}\right),
$$

其 forward output 是离散 spike。真实 derivative 在 threshold 之外几乎处处为零，并在 threshold 处不可微，所以普通 backpropagation 无法直接训练。SG 在 backward 中以连续近似 $H(u)$ 替代 $\partial s / \partial u$，从而使 SNN 可由 BPTT direct training。

然而，“局部 spike derivative 可用”不等于“远程 temporal gradient 可用”。在展开的 SNN 计算图中，loss 对早期 membrane potential $u^l[t]$ 的 gradient 一方面来自同一 timestep 的后续 layers，另一方面来自未来 states $u^l[t + 1], \ldots, u^l[T]$。后者必须连续穿过每个 timestep 的 leak、fire 和 reset。只要每步 derivative 持续小于 1，远程 gradient 就会衰减；只要某一步 derivative 为零，特定 temporal path 就会完全消失。

作者用 truncated BPTT 实验支持这一动机：训练 vanilla LIF 时，仅保留少量 temporal-gradient steps 已能获得与完整 BPTT 接近的 accuracy；增加允许回传的 temporal range 并没有持续带来收益。对于 5-layer SNN，vanilla LIF 的 accuracy 随总 timestep 增长在 $T = 32$ 达到峰值，随后下降。实验直接表明较远 gradient paths 在这些配置中没有产生明显额外收益；“原因就是 temporal-gradient vanishing”则是作者结合后续理论作出的机制解释。

已有 long-term dependency 方法包括 spiking LSTM、spiking ConvLSTM、spikeGRU、trainable parallel connections 和 bio-inspired neurons。这些方法可引入 gating、额外 learnable parameters 或更复杂结构。CLIF 的设计目标更受约束：保留 LIF 的 integrate、leak、fire 和 reset，保持 binary output，不增加 learnable parameters，并能作为 LIF 的 drop-in replacement 应用于 VGG、ResNet 和 Spike-Driven Transformer。

## 3. Method Overview

### 3.1 输入、状态、输出与维度

在 layer $l$、timestep $t$，CLIF neuron 接收上一层 spike $s^{l - 1}[t]$，经 synaptic weights 形成 postsynaptic current：

$$
c^l[t]
=
W^l * s^{l - 1}[t].
$$

$*$ 表示 fully connected 或 convolutional synaptic operation。对于 convolutional layer，可将 $c^l[t]$、reset 前后的 $u^l[t]$、$m^l[t]$ 和 $s^l[t]$ 理解为同形 tensors，例如 $C_l \times H_l \times W_l$；对于 fully connected layer，它们是长度为 $N_l$ 的 vectors。论文没有统一列出每个 backbone 各层 tensor shape，因此具体 channel 和 spatial dimensions 为 `Needs further check`。

单个 neuron 或 feature position 在当前 timestep 的输入与状态为：

- postsynaptic current $c^l[t]$；
- previous membrane potential $u^l[t - 1]$；
- previous complementary potential $m^l[t - 1]$。

其层间输出是 binary spike $s^l[t]$，内部持续保存 $u^l[t]$ 与 $m^l[t]$。$m[t]$ 不是 spike、不是 learnable threshold，也不直接作为下一层 synaptic input。

### 3.2 完整 forward process

CLIF 在每个 timestep 依次执行四步：

$$
u^l[t]
=
\left(1 - \frac{1}{\tau}\right)u^l[t - 1]
+
c^l[t],
$$

$$
s^l[t]
=
\Theta\left(u^l[t] - V_{\mathrm{th}}\right),
$$

$$
m^l[t]
=
m^l[t - 1]
\odot
\sigma\left(\frac{1}{\tau}u^l[t]\right)
+
s^l[t],
$$

$$
u^l[t]
\leftarrow
u^l[t]
-
s^l[t]
\odot
\left(
V_{\mathrm{th}} + \sigma\left(m^l[t]\right)
\right).
$$

第一步执行 leak and integration；第二步产生 binary spike；第三步更新 complementary potential；第四步执行 adaptive soft reset。PDF 中 Algorithm 1 和 Eq. (19) 的正确符号是 $+ s^l[t]$，不是 parsed text 中损坏的负号。

若近期输入和 firing 较密集，$m[t]$ 会增大；下一次 firing 时，reset 不仅减去 $V_{\mathrm{th}}$，还减去 $\sigma(m[t])$，从而抑制连续 firing。作者将其类比为 biological hyperpolarization 或 refractory behavior。严格地说，CLIF 调整的是 reset strength，而不是 firing threshold 本身。

### 3.3 Backward 与优化目标

论文没有提出新的 task loss。对于 classification，网络仍最小化原分类 objective $\mathcal L$，并计算：

$$
\nabla_{W^l}\mathcal L
=
\sum_{t = 1}^{T}
\frac{\partial\mathcal L}{\partial u^l[t]}
\frac{\partial u^l[t]}{\partial W^l}.
$$

Binary spike 的 derivative 使用 rectangular surrogate：

$$
\frac{\partial s^l[t]}{\partial u^l[t]}
\approx
H\left(u^l[t]\right)
=
\frac{1}{\alpha}
\mathbf 1
\left(
\left|u^l[t] - V_{\mathrm{th}}\right|
<
\frac{\alpha}{2}
\right),
$$

其中论文设置 $\alpha = V_{\mathrm{th}}$。Rectangle 是作者沿用已有 SG 工作的简单设置，并使 temporal derivative 可解析为 $0$ 或 $\gamma$；论文没有证明它是最佳 surrogate，也没有验证 CLIF 是否对其他 surrogate functions 保持相同优势：`Needs further check`。

## 4. Key Components and Mechanisms

### 4.1 LIF 的 spatial 与 temporal gradient

LIF gradient error 可写成：

$$
\frac{\partial\mathcal L}{\partial u^l[t]}
=
\mathcal P^l[t]
+
\sum_{t' = t + 1}^{T}
\mathcal T^l[t, t'],
$$

其中 spatial term 为：

$$
\mathcal P^l[t]
=
\frac{\partial\mathcal L}{\partial s^l[t]}
\frac{\partial s^l[t]}{\partial u^l[t]},
$$

而来自未来 timestep $t'$ 的 temporal term 包含：

$$
\mathcal T^l[t, t']
=
\frac{\partial\mathcal L}{\partial s^l[t']}
\frac{\partial s^l[t']}{\partial u^l[t']}
\prod_{r = t}^{t' - 1}
\epsilon^l[r].
$$

$\epsilon^l[t]$ 是 $u^l[t]$ 到 $u^l[t + 1]$ 的 total derivative，同时包括 direct membrane recurrence 和经 spike/reset 的间接路径。对 soft-reset LIF：

$$
\epsilon^l[t]
=
\gamma
\left(
1 - V_{\mathrm{th}}H\left(u^l[t]\right)
\right),
\qquad
\gamma
=
1 - \frac{1}{\tau}.
$$

因此 $\mathcal T^l[t, t']$ 中包含 $\gamma^{t' - t}$。当 $0 < \gamma < 1$ 时，该项随时间距离指数衰减。

### 4.2 Rectangular surrogate 引起的 path truncation

当 $\alpha = V_{\mathrm{th}}$ 时：

$$
\epsilon[t]
=
\begin{cases}
0,
&
0.5V_{\mathrm{th}} < u[t] < 1.5V_{\mathrm{th}},\\
\gamma,
&
\text{otherwise}.
\end{cases}
$$

只要从未来 $t'$ 返回 $t$ 的乘积中存在一个零因子，该条 temporal path 就被截断。但这不等于整个 network 没有 gradient：当前 spatial term、其他 temporal paths 和其他 layers 仍可能提供训练信号。

作者文字将零因子概括为“中间发生一次 firing”，但严格条件是 reset 前 membrane potential 进入 rectangular surrogate support。Firing 条件为 $u[t] \geq V_{\mathrm{th}}$，两者并不等价：未 firing 的 $0.5V_{\mathrm{th}} < u[t] < V_{\mathrm{th}}$ 也产生零因子；$u[t] \geq 1.5V_{\mathrm{th}}$ 时即使 firing，$\epsilon[t]$ 仍为 $\gamma$。Appendix D 还混用了 $1 - s[t]H(u[t])$ 与由 soft-reset 链式法则得到的 $1 - V_{\mathrm{th}}H(u[t])$，相关结论应以 Eq. (9) 的严格推导为准。

### 4.3 Complementary state 如何形成额外路径

CLIF 有两个递归状态：

$$
u[t],
\qquad
m[t].
$$

局部 forward dependency 不再只有 $u[t] \rightarrow u[t + 1]$，还包括：

$$
u[t]
\rightarrow
m[t]
\rightarrow
u[t + 1],
$$

以及：

$$
m[t]
\rightarrow
m[t + 1].
$$

论文将 CLIF temporal gradient 分成 $\mathcal T_{M1}$ 与 $\mathcal T_{M2}$。$\mathcal T_{M1}$ 主要沿 membrane recurrence 传播，但相邻 derivative $\xi[t]$ 已加入经 $m[t]$ 返回 $u[t + 1]$ 的局部旁路。它仍包含逐 timestep 的 $\xi$ 连乘，因此仍可能长期衰减。

$\mathcal T_{M2}$ 则先进入 complementary-state chain：

$$
u[t]
\rightarrow
m[t]
\rightarrow
m[t + 1]
\rightarrow
\cdots
\rightarrow
m[t' - 1]
\rightarrow
u[t']
\rightarrow
\mathcal L.
$$

$u[t]$ 对 $m[t]$ 的 total derivative 为：

$$
\psi[t]
=
\frac{d m[t]}{d u[t]}
=
\frac{1}{\tau}m[t - 1]
\sigma'\left(\frac{u[t]}{\tau}\right)
+
H\left(u[t]\right).
$$

第一项来自 $u[t]$ 对 complementary decay 的影响，第二项来自 $u[t] \rightarrow s[t] \rightarrow m[t]$。$\mathcal T_{M2}$ 不完全依赖 LIF 原有的 $\prod\epsilon$，所以 membrane-only path 很小或被截断时仍可能提供额外 gradient。不过它仍包含 sigmoid derivative 和 complementary recurrence 的连乘，论文没有证明其在任意时间长度和状态下都不会衰减。CLIF 是补充 temporal-gradient paths，而不是从理论上彻底消除 gradient vanishing。

### 4.4 Forward adaptation 与 backward improvement 的耦合

CLIF 同时改变 forward 和 backward。Forward 中 adaptive reset 改变 membrane trajectory、spike timing 与 firing rate；backward 中新增 $m$-related derivatives。实验观察到更低 loss 和更高 accuracy，与作者的 temporal-gradient explanation 一致，但论文没有使用 stop-gradient、custom backward 或 gradient-norm ablation 将两类作用严格分离。因此“额外 temporal paths 是全部性能提升的原因”尚未得到直接证明。

## 5. Experiments and Main Evidence

### 5.1 Ablation：loss convergence 与 timestep

作者在相同 optimizer、random seed、architecture、loss、initialization 和 hyperparameters 下比较 LIF 与 CLIF。Spiking ResNet-18、$T = 6$ 的 neuron-exchange 实验先用 LIF 训练，再分别在 epoch 19、49、99 或 149 切换为 CLIF。切换后 loss 在数个 epochs 内进一步下降，且最终 loss 低于持续使用 LIF 的模型。Appendix H 在其他 tasks 和 backbones 上报告相同趋势。

该实验直接支持 CLIF 改变 optimization trajectory 并获得更低 training loss。作者将其解释为更精确、高效地捕获 error information，但没有测量 true gradient error、gradient norm、GPU time 或训练能耗，因此这里的 “training efficiency” 是收敛曲线层面的 author claim，不是 wall-clock benchmark。

Temporal ablation 使用 CIFAR-10 与 Spiking ResNet-18。当 $T = 1$ 时，没有跨 membrane state 的 temporal recurrence，LIF 与 CLIF 均为 $92.7\%$。当 $T > 1$ 时，CLIF 始终优于 LIF，说明收益确实依赖多 timestep dynamics；但由于 forward adaptive reset 也只在多 timestep 下产生作用，该实验仍不能单独证明提升只来自 backward temporal gradient。

### 5.2 相同配置下的 neuron comparison

Figure 4 自行实现 LIF、PLIF、KLIF、GLIF 和 CLIF，并固定 backbone、random seed 与 hyperparameters，因此比跨论文 SOTA table 更能隔离 neuron model。

- CIFAR-10、Spiking ResNet-18、$T = 8$：CLIF 为 $95.68\%$，LIF 为 $94.66\%$，提升 $1.02$ 个百分点；ReLU ANN 为 $95.62\%$，CLIF 数值上高 $0.06$ 个百分点。
- CIFAR-100、Spiking ResNet-18、$T = 6$：CLIF 为 $78.36\%$，LIF 为 $76.23\%$，提升 $2.13$ 个百分点；ReLU ANN 为 $78.14\%$，CLIF 数值上高 $0.22$ 个百分点。

这支持 CLIF 相对相同配置 LIF 的明确提升。相对 ANN 的差距很小，Figure 4 没有 error bars 或 significance test，因此只能称 configuration-specific numerical advantage，不能称普遍或统计显著地超过 ANN。

### 5.3 Static image datasets 与跨论文比较

Table 1 覆盖 CIFAR-10、CIFAR-100 和 Tiny-ImageNet，但不同方法可能使用不同 architecture、timestep 和 augmentation，不能完全隔离 neuron contribution。

- CIFAR-10：增强配置 CLIF、ResNet-18、$T = 8$ 为 $96.69\%$，对应 ANN 为 $96.65\%$，高 $0.04$ 个百分点。
- CIFAR-100：增强配置 CLIF、$T = 8$ 与 ANN 均为 $80.89\%$，两者持平，不是 CLIF 超过 ANN。
- Tiny-ImageNet：CLIF、VGG-13、$T = 6$ 为 $64.13\%$，对应 ANN 为 $59.77\%$，高 $4.36$ 个百分点；但表中没有列出作者同配置实现的 VGG-13 LIF，无法由该表单独计算 CLIF-to-LIF gain。

因此实验整体支持 CLIF 与对应 ANN comparable，并在部分 configuration 中数值更高；Abstract 的“略微超过 superior ANNs”必须限制到具体表格设置。

### 5.4 Neuromorphic event datasets

Table 2 在 DVS-Gesture 和 CIFAR10-DVS 上验证 CLIF：

- DVS-Gesture：Spiking-VGG11 中 CLIF 为 $97.92\%$、LIF 为 $97.57\%$，提高 $0.35$ 个百分点；Spike-Driven Transformer 中为 $99.31\%$ 对 $98.26\%$，提高 $1.05$ 个百分点。
- CIFAR10-DVS：Spiking-VGG11 中为 $79.00\%$ 对 $78.05\%$，提高 $0.95$ 个百分点；VGGSNN 中为 $86.10\%$ 对 $84.90\%$，提高 $1.20$ 个百分点。

$86.10\%$ 是论文 Table 2 所列 CIFAR10-DVS methods/configurations 中的最高 accuracy，可称 table-specific best；表格覆盖范围不足以据此无条件声称 overall SOTA。

Appendix I 明确说明 DVS-Gesture events 通过 SpikingJelly 积分为 frames 后输入 SNN，因此不是逐 event asynchronous execution。CIFAR10-DVS 的具体 temporal slicing、polarity channels 和 tensor construction 在已读正文中没有完整说明：`Needs further check`。Event experiments 证明 CLIF 对 frame-integrated neuromorphic classification 有效，不能直接外推到 raw-event processing 或 neuromorphic hardware deployment。

### 5.5 Firing rate 与 energy evidence

CLIF 在五个 tasks 上的平均 firing rate 均低于 LIF：CIFAR-10 为 $11.86\%$ 对 $14.73\%$，CIFAR-100 为 $10.25\%$ 对 $11.25\%$，Tiny-ImageNet 为 $13.08\%$ 对 $17.71\%$，CIFAR10-DVS 为 $4.86\%$ 对 $6.03\%$，DVS-Gesture 为 $1.64\%$ 对 $1.79\%$。这与更强 adaptive reset 抑制连续 firing 的机制一致。

Energy 不是 chip measurement、GPU runtime 或 wall-clock latency，而是基于 spike sparsity、AC/MAC counts、文献给出的 32-bit operation energy，以及进一步的 memory read/write 和 addressing 成本构建的 **SOP/MAC/AC and memory-access based model-level estimate**。

CLIF 降低 firing rate 和 ACs，但增加 sigmoid、complementary-state floating-point computation 与 memory traffic。Table 6 中 CLIF 的 synaptic-operation energy 在 CIFAR-10 和 Tiny-ImageNet 略低于 LIF，在 CIFAR-100、DVS-Gesture 和 CIFAR10-DVS 略高。因此数据支持“CLIF 与 LIF 的估算 energy 处于相近量级，同时 CLIF accuracy 更高”，不支持“CLIF 普遍比 LIF 更节能”。

## 6. Strengths and Limitations

**Strengths**

- 从 soft-reset LIF 的 BPTT 递推式分析 temporal-gradient exponential decay 与 exact path truncation，问题定义具体。
- CLIF 只增加 complementary state 和固定 dynamics，不增加 learnable neuron parameters，并保持 binary spike output。
- 可将 LIF 替换为 CLIF，覆盖 VGG、ResNet 和 Spike-Driven Transformer，多种 backbone 上均观察到 gain。
- 同时验证 static images 与 neuromorphic event datasets，说明方法不限于单一输入类型。
- Energy appendix 同时考虑 AC/MAC 与 memory access，没有仅用 spike sparsity 直接宣称真实能效。

**Limitations**

- 作者关于“发生 spike 即使 Part II 为零”的文字结论与 rectangular surrogate 的严格 support 条件不完全一致。
- Forward adaptive reset 和 backward extra paths 同时变化，缺少分离二者贡献的 causal ablation。
- 更低 loss 没有直接证明 gradient 更准确，也没有给出 temporal gradient norm 随距离的系统测量。
- $\mathcal T_{M2}$ 仍可能因 sigmoid derivative 和 $\rho$ 连乘衰减，CLIF 没有从理论上消除所有 vanishing-gradient cases。
- ANN 对比中的部分差异极小且缺少统计显著性；跨论文 table 还混合了不同 architecture、timestep 和 augmentation。
- CLIF 增加连续 state、sigmoid、MAC 与 memory traffic；binary output 不等于整个 neuron 只有廉价 AC computation。
- Event 数据采用 frame integration，未验证 raw asynchronous event、on-chip training 或 neuromorphic hardware inference。
- 所有实验网络是否严格 fully spiking，以及不同 backbone 的 input/readout 实现为 `Needs further check`。

## 7. Relation to Other Papers and Survey Taxonomy

本文主要属于：

- **SNN architecture / neuron model**：直接修改 LIF state dynamics 与 reset；
- **temporal modeling**：用 complementary state 保存近期 membrane 与 firing history；
- **training method**：针对 SG+BPTT 的 temporal-gradient flow；
- **event-based classification**：在 DVS-Gesture 和 CIFAR10-DVS 上验证；
- **efficiency analysis**：报告 firing rate 和 model-level operation/memory estimate，但不是 hardware result。

与 PLIF、KLIF、GLIF 相比，CLIF 不依赖新增 learnable neuron parameters；与 spiking LSTM、ConvLSTM 和 spikeGRU 相比，它不引入 parameterized gates；与 e-prop、SLTT 相比，它不是舍弃 temporal gradients，而是为 BPTT 增加 complementary paths；与 adaptive-threshold neuron 相比，CLIF 使用 latent state 调整 reset strength，而不是动态改变 threshold。

对 event-camera 综述而言，本文提供的关键视角是：event-based SNN 的 temporal capability 不只由 event representation、slicing 或 backbone 决定，neuron recurrence 和 backward gradient topology 同样限制模型能否利用较长时间信息。它不是 event representation、detection、optical flow、dense prediction 或 neuromorphic hardware implementation 工作。

### PDF-verified relation backfill

主要路线是在 LIF 上增加无可学习参数的 complementary state，为 BPTT 建立额外 temporal-gradient path。

- **Incorporating Learnable Membrane Time Constant to Enhance Learning of Spiking Neural Networks (Wei Fang et al., ICCV 2021)** — `alternative`。两者都处理 trainable versus complementary neuron dynamics，但采用不同 representation、state 或 computation route。 对应 Section 3: neuron dynamics and training。证据：Related Work 2 and Experiments 5.2, PDF pp.3 and 7, Fang et al. 2021b bibliography entry。 当前 active corpus 未覆盖。
- **GLIF: A Unified Gated Leaky Integrate-and-Fire Neuron for Spiking Neural Networks (Xinyu Yao et al., NeurIPS 2022)** — `alternative`。两者都处理 gated versus parameter-free temporal dynamics，但采用不同 representation、state 或 computation route。 对应 Section 3: neuron dynamics and training。证据：Related Work 2 and Experiments 5.2, PDF pp.3 and 7, Yao et al. 2022 bibliography entry。 当前 active corpus 未覆盖。
- **Spatial Learning Through Time: Efficient Training of Deep Spiking Neural Networks (Qiang Meng et al., NeurIPS 2023)** — `contrasts_with`。两者都面向 temporal-gradient handling in BPTT，但优化方向相反或训练假设不同。 对应 Section 3: temporal credit assignment。证据：Related Work 2, PDF p.3, Meng et al. 2023 bibliography entry。 当前 active corpus 未覆盖。 值得 backward search。

## 8. Survey-Usable Takeaways

1. SG 只解决 spike function 的局部不可微问题；vanilla LIF 的远程 temporal gradient 仍会因 leak 连乘衰减，并可能被 surrogate/reset derivative 的零因子截断。
2. CLIF 增加 complementary potential $m[t]$，用近期 membrane potential 与 spike activity 控制 adaptive reset，并在 BPTT 中形成额外 temporal-gradient paths。
3. CLIF 保持 binary spike output 且不增加 learnable neuron parameters，但增加 continuous-state computation、sigmoid 和 memory access，不能仅凭 spike sparsity 推断真实能效。
4. 相同配置下 CLIF 相对 LIF 的 accuracy gain 在静态和 event datasets、VGG/ResNet/Transformer backbones 上较一致；这比跨论文 SOTA comparison 更能支持 neuron replacement 的有效性。
5. “超过 ANN”应限定到 configuration-specific result：CIFAR-10 仅高 $0.04$ 至 $0.06$ 个百分点，CIFAR-100 最佳结果持平，Tiny-ImageNet 的数值优势更明显。
6. Event evidence 限于 frame-integrated neuromorphic classification；$86.10\%$ 是论文表格中的 configuration-specific best，不等于已证明所有 event methods 的 overall SOTA。
7. CLIF 增加了 extra gradient terms，但 forward adaptation 与 backward improvement 尚未被独立消融，因此其完整性能机制仍是 open question。

## Supplement Points

### Questions and Clarifications

#### 1. Eq. (5) 是如何从 BPTT 得到的？

在展开的 SNN 中，$u^l[t]$ 通过当前 spike 和下一时刻 state 两条路径影响 loss：

$$
\frac{\partial\mathcal L}{\partial u^l[t]}
=
\frac{\partial\mathcal L}{\partial s^l[t]}
\frac{\partial s^l[t]}{\partial u^l[t]}
+
\frac{\partial\mathcal L}{\partial u^l[t + 1]}
\epsilon^l[t].
$$

对下一时刻继续展开：

$$
\frac{\partial\mathcal L}{\partial u^l[t + 1]}
=
\frac{\partial\mathcal L}{\partial s^l[t + 1]}
\frac{\partial s^l[t + 1]}{\partial u^l[t + 1]}
+
\frac{\partial\mathcal L}{\partial u^l[t + 2]}
\epsilon^l[t + 1].
$$

代回后：

$$
\begin{aligned}
\frac{\partial\mathcal L}{\partial u^l[t]}
= {}&
\frac{\partial\mathcal L}{\partial s^l[t]}
\frac{\partial s^l[t]}{\partial u^l[t]}\\
&+
\frac{\partial\mathcal L}{\partial s^l[t + 1]}
\frac{\partial s^l[t + 1]}{\partial u^l[t + 1]}
\epsilon^l[t]\\
&+
\frac{\partial\mathcal L}{\partial u^l[t + 2]}
\epsilon^l[t + 1]\epsilon^l[t].
\end{aligned}
$$

递归展开到 $T$，得到：

$$
\frac{\partial\mathcal L}{\partial u^l[t]}
=
\frac{\partial\mathcal L}{\partial s^l[t]}
\frac{\partial s^l[t]}{\partial u^l[t]}
+
\sum_{t' = t + 1}^{T}
\frac{\partial\mathcal L}{\partial s^l[t']}
\frac{\partial s^l[t']}{\partial u^l[t']}
\prod_{r = t}^{t' - 1}
\epsilon^l[r].
$$

例如来自 $t + 3$ 的 gradient 必须乘 $\epsilon[t + 2]\epsilon[t + 1]\epsilon[t]$。任一项为零，这条从 $t + 3$ 返回 $t$ 的 path 就为零；当前 timestep 的 spatial gradient 和不经过该零因子的其他 paths 并不会因此全部消失。

#### 2. Eq. (6) 与 Eq. (7) 是怎么得到的？

Appendix B 将 soft-reset LIF 重写为：

$$
u^l[t + 1]
=
\gamma
\left(
u^l[t] - V_{\mathrm{th}}s^l[t]
\right)
+
W^ls^{l - 1}[t + 1].
$$

$u^l[t]$ 对 $u^l[t + 1]$ 有 direct path，也有 $u^l[t] \rightarrow s^l[t] \rightarrow \text{reset} \rightarrow u^l[t + 1]$ 的 indirect path。多变量链式法则给出：

$$
\epsilon^l[t]
\equiv
\frac{d u^l[t + 1]}{d u^l[t]}
=
\frac{\partial u^l[t + 1]}{\partial u^l[t]}
+
\frac{\partial u^l[t + 1]}{\partial s^l[t]}
\frac{\partial s^l[t]}{\partial u^l[t]}.
$$

这就是 Eq. (6)。两个 partial derivatives 在计算时暂时把 $u[t]$ 和 $s[t]$ 看作独立变量，随后第二项再补上 spike 对 membrane 的依赖。

Eq. (7) 描述同一 timestep 的 layer-wise gradient。中间层 spike 通过：

$$
u^{l + 1}[t]
=
W^{l + 1}s^l[t]
+
\cdots
$$

影响下一层和 loss，所以：

$$
\frac{\partial\mathcal L}{\partial s^l[t]}
=
\begin{cases}
\dfrac{\partial\mathcal L}{\partial s^L[t]},
& l = L,\\
\dfrac{\partial\mathcal L}{\partial u^{l + 1}[t]}
\left(W^{l + 1}\right)^\top,
& l < L.
\end{cases}
$$

对 convolution，$\left(W^{l + 1}\right)^\top$ 表示 convolution operator 的 adjoint/backward operation，不是简单转置 kernel array。

#### 3. Eq. (6) 如何得到 Eq. (9)，为什么选择 rectangular function？

由 soft-reset recurrence：

$$
\frac{\partial u^l[t + 1]}{\partial u^l[t]}
=
\gamma,
\qquad
\frac{\partial u^l[t + 1]}{\partial s^l[t]}
=
-\gamma V_{\mathrm{th}}.
$$

再以 surrogate $H(u^l[t])$ 近似 $\partial s^l[t] / \partial u^l[t]$，代入 Eq. (6)：

$$
\begin{aligned}
\epsilon^l[t]
&=
\gamma
-
\gamma V_{\mathrm{th}}H\left(u^l[t]\right)\\
&=
\gamma
\left(
1 - V_{\mathrm{th}}H\left(u^l[t]\right)
\right).
\end{aligned}
$$

负项来自 soft reset：spike 越容易随 $u[t]$ 改变，reset 对下一状态 derivative 的抵消就越强。

Rectangular function 只在 threshold 邻域提供常数 gradient，在其他区域为零。其优点是计算简单，并把训练信号集中在小幅变化可能改变 firing decision 的区域。本文主要沿用已有 SG 工作，并设置 $\alpha = V_{\mathrm{th}}$；该设置还使 $\epsilon$ 变成 $0$ 或 $\gamma$，便于解析 gradient path。论文没有比较 triangular、sigmoid derivative、arctangent 等 alternatives，也未证明 rectangle 最优或 CLIF 必须依赖它：`Needs further check`。

#### 4. 为什么 Part II 的零值条件不等于 firing 条件？

当 $\alpha = V_{\mathrm{th}}$ 时，四种情况为：

| Reset 前的 $u[t]$ | 是否 firing | Surrogate 是否激活 | $\epsilon[t]$ |
|---|---:|---:|---:|
| $u[t] \leq 0.5V_{\mathrm{th}}$ | 否 | 否 | $\gamma$ |
| $0.5V_{\mathrm{th}} < u[t] < V_{\mathrm{th}}$ | 否 | 是 | $0$ |
| $V_{\mathrm{th}} \leq u[t] < 1.5V_{\mathrm{th}}$ | 是 | 是 | $0$ |
| $u[t] \geq 1.5V_{\mathrm{th}}$ | 是 | 否 | $\gamma$ |

因此：

$$
\text{firing}
\not\Longleftrightarrow
\epsilon[t] = 0.
$$

真正决定零因子的条件，是 reset 前 membrane potential 是否进入 surrogate support，而不是是否 firing。假设未来 $t + 3$ 的 contribution 为：

$$
\mathcal T[t, t + 3]
=
A_{t + 3}
\epsilon[t + 2]
\epsilon[t + 1]
\epsilon[t].
$$

若 $u[t + 1]$ 进入 support，则 $\epsilon[t + 1] = 0$，这条 contribution 为零。但当前 spatial term、来自较近时刻的其他 terms、其他 layers 和其他 samples 的 gradients 仍可能非零，所以 path truncation 不等于整个 network 停止训练。

Appendix D 的 Eq. (38) 还出现含 $s[t]H(u[t])$ 的表达，而正文 Eq. (9)、Eq. (13) 与 Appendix Eq. (39) 使用 $V_{\mathrm{th}}H(u[t])$。从 Appendix B 的 soft-reset recurrence 直接求导得到的是后者，因此作者将 “spike generated” 与 “$u$ 位于 surrogate support”合并描述并不严谨。

#### 5. $\mathcal T_{M1}$ 与 $\mathcal T_{M2}$ 两类路径具体是什么？

CLIF 的 forward graph 包含：

$$
u[t]
\rightarrow
\left\{
s[t],
u[t + 1],
m[t]
\right\},
$$

$$
m[t]
\rightarrow
\left\{
u[t + 1],
m[t + 1]
\right\}.
$$

$\mathcal T_{M1}$ 主要经过 membrane recurrence：

$$
u[t]
\rightarrow
u[t + 1]
\rightarrow
\cdots
\rightarrow
u[t']
\rightarrow
\mathcal L.
$$

不过 CLIF 的相邻 total derivative 为：

$$
\xi[t]
=
\epsilon[t]
+
\frac{\partial u[t + 1]}{\partial m[t]}
\psi[t],
$$

所以其中还包含 $u[t] \rightarrow m[t] \rightarrow u[t + 1]$ 的局部旁路。$\mathcal T_{M1}$ 仍要连续乘 $\xi$，因此作者承认 leak-induced long-range decay 仍适用于它。

$\mathcal T_{M2}$ 先进入 complementary recurrence：

$$
u[t]
\rightarrow
m[t]
\rightarrow
m[t + 1]
\rightarrow
\cdots
\rightarrow
m[t' - 1]
\rightarrow
u[t']
\rightarrow
\mathcal L.
$$

以两步路径为例，LIF contribution 包含：

$$
\frac{\partial\mathcal L}{\partial u[t + 2]}
\frac{d u[t + 2]}{d u[t + 1]}
\frac{d u[t + 1]}{d u[t]}.
$$

CLIF 还可能包含：

$$
\frac{\partial\mathcal L}{\partial u[t + 2]}
\frac{\partial u[t + 2]}{\partial m[t + 1]}
\frac{d m[t + 1]}{d m[t]}
\frac{d m[t]}{d u[t]}.
$$

即使 membrane-only derivative 很小，后者仍可能提供非零 signal。$d m[t] / d u[t]$ 同时包含 membrane-dependent decay 与 spike 两条路径：

$$
\psi[t]
=
\frac{1}{\tau}m[t - 1]
\sigma'\left(\frac{u[t]}{\tau}\right)
+
H\left(u[t]\right).
$$

但 complementary path 仍包含 sigmoid derivative 和 $\rho$ 的 temporal product，也可能衰减。论文证明的是 extra terms 存在，并以 loss/accuracy experiments 提供一致证据；它没有证明 CLIF 在所有条件下消除 vanishing gradient，也没有完全证明 extra paths 而非 forward adaptive reset 是性能提升的唯一原因。
