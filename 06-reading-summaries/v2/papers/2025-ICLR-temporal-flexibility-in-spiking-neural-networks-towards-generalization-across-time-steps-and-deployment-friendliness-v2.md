---
tags: [SNN, temporal-flexibility, mixed-time-step-training, event-driven, neuromorphic-hardware, DVS, deployment]
---

# Summary V2｜Temporal Flexibility in Spiking Neural Networks: Towards Generalization Across Time Steps and Deployment Friendliness

## 1. Core Understanding

本文研究 direct-trained SNN 的 **temporal inflexibility**：模型若只在固定 timestep $T$ 下训练，通常只适应该时间离散结构，换到其他 $T$、dynamic early-exit，或没有全局 timestep 的 fully event-driven hardware 时性能明显下降。这里的 $T$ 是 GPU/time-stepped simulation 将一个样本展开成多少轮同步 neuron update，不等同于连续物理时间或事件相机 timestamp。

作者先提出 Naive Mixture Training（NMT）：每次 iteration 采样多个全局 $T$，让同一组 weights 在不同时间展开长度下共同优化。进一步提出 Mixed Time-step Training（MTT）：把网络划分为 $G$ 个 stages，并为每个 stage 独立采样 timestep，形成 temporal configuration

$$
\mathbf t = (t_1, \ldots, t_G).
$$

相邻 stages 的时间长度不一致时，由 Temporal Transformation Module（TTM）通过 temporal grouping、sum 或 replication 传递 spike tensors。MTT 由此将全局 $T$ 的少量选择扩展为 stage-wise 组合空间，迫使共享 weights 降低对单一时间结构的依赖。

本文属于 **generic SNN training、temporal modeling、dynamic inference 与 neuromorphic deployment background**。DVS 输入在 time-stepped 路径中仍按 timestamp 分成 $T$ frames；事件数据集主要用于评估时间结构迁移，并未提出新的 event-camera representation 或下游视觉架构。网络使用 LIF/IF neurons 与 binary spike communication，但 BN、convolution 和 readout 等运算并非都被证明是纯 event-driven；芯片部署模型还必须移除 clocked bias addition，因此不能把所有实验统一描述为严格 fully spiking hardware systems。

## 2. Problem and Motivation

Standard Direct Training（SDT）将 SNN 视为 temporal RNN，用 surrogate gradient 与 BPTT 在固定 $T$ 上训练。这使 GPU 并行训练成为可能，却也可能让 weights、membrane trajectories、spike counts 和 BN statistics 共同过拟合该时间离散方式。部署时改变 $T$ 会改变 neuron update 次数、输入分箱和状态分布；fully event-driven chips 更没有同步迭代 $T$，只在 event arrival 时异步更新相关 neurons，因此 train–deployment temporal mismatch 更大。

这一问题影响两类部署。Clock-driven hardware 若根据样本置信度动态改变 inference steps，需要同一模型在多个 $T$ 下稳定工作。Fully event-driven hardware 则把训练时的 timestep 降为近似异步 dynamics 的辅助工具；若 weights 严重依赖训练 $T$，直接迁移会损失 accuracy。

ANN-SNN conversion 在较大 $T$ 下可表现出一定时间灵活性，但论文指出其低 timestep flexibility 较弱，而且主流 rate-based conversion 依赖 ANN activation–SNN firing-rate 对应，更自然地适用于 IF neurons 和静态输入。将其描述为“无法处理 DVS 或只能使用 IF”应理解为作者对主流 conversion pipeline 的范围判断，不是理论上的普遍不可能。

## 3. Method Overview

### 3.1 从 SDT、NMT 到 MTT

SDT 优化固定全局时间结构 $S(x,T)$。NMT 从 $\{T_{\min},\ldots,T_{\max}\}$ 中采样若干全局 $T$，对共享 weights 累积 gradients；它相当于在训练过程中联合优化多个共享参数、不同时间展开长度的 SNN variants，而不是保存多套网络。

MTT 将 partitioned SNN 写为 $S_P(x,\mathbf t)$。理想目标遍历 batch 与所有 stage-wise configurations：

$$
\mathcal L_{\mathrm{MTT(overall)}}
=
\sum_{k=1}^{N}
\sum_{\mathbf t \in \{T_{\min},\ldots,T_{\max}\}^{G}}
\mathcal L\left(S_P(x_k,\mathbf t),y_k\right).
$$

完整枚举代价过高，实际每次 iteration 采样 $s$ 个 vectors $\mathbf t^{(1)},\ldots,\mathbf t^{(s)}$，依次 forward/backward、累积 gradients，最后只更新一次共享 weights。论文实验通常设 $T_{\min}=1$、$s=3$。

### 3.2 Temporal Transformation Module

若前一 stage 输出 $t_{\mathrm{in}}$ 帧、后一 stage 需要 $t_{\mathrm{out}}$ 帧，TTM 进行无参数 temporal remapping：相等时为 identity；downsampling 时将相邻输入帧尽量均匀分组并逐组求和；upsampling 时按同一分组边界复制输入帧。Downsampling 后的值可能是 integer spike counts，而不再是 binary spikes。Eq. (13) 的混合取整符号及 $\epsilon$ 定义不清，精确边界实现为 `Needs further check`。

### 3.3 BN calibration 与部署

混合 temporal configurations 会显著改变 batch statistics，使训练期间累计的 BN running mean/variance 不可靠。作者在 fine-tuning 时锁定 BN，或在 weights 固定后用少量 training batches 重新校准 statistics；正文报告 10 batches 已足够，并声称 $T_{\max}$ statistics 可用于其他 $T$，后者的普适性为 `Needs further check`。

Time-stepped 实验使用 LIF，$V_{\mathrm{th}}=1$、decay factor $\tau=0.5$；event-based experiments 因 Speck 等异步芯片的支持范围采用 IF，$V_{\mathrm{th}}=1$。PDF Eq. (7)–(8) 将 LIF decay 写成正指数 $\exp((t_i-t_{i-1})/\tau_0)$，但由前述微分方程应为负指数；这是疑似论文公式错误。

## 4. Key Components and Mechanisms

MTT 的关键不是让输出完全与 timestep 无关，而是共同约束

$$
S_P(x,\mathbf t^{(1)}) \approx S_P(x,\mathbf t^{(2)})
$$

在任务预测层面保持一致。这样 weights 不能依赖“恰好运行了几轮”才能分类，而需学习对 temporal discretization 更稳定的表示。作者将其解释为对单一 temporal structure 的 regularization，并类比为同时训练多个共享 weights 的结构 variants；新采样配置还可能帮助 optimization 离开 sharp local minima。Noise injection、gradient norms 与 loss landscape 与该解释一致，但没有证明 flatter minimum 是性能提升的唯一原因。

MTT 的 configuration count 一般为

$$
(T_{\max}-T_{\min}+1)^G.
$$

论文写 $T_{\max}^{G}$ 是因为实验设 $T_{\min}=1$。这种组合扩张不要求全部枚举，但带来额外 training cost。Appendix 在 RTX 3090 上报告 MTT first-epoch time 为 SDT 的 $1.60\times$–$1.77\times$，与理论近似一致；逐 configuration 立即 backward 后释放计算图，使 peak GPU memory 与 SDT 相近。这里是 GPU training runtime/memory evidence，不是 inference energy measurement。

## 5. Experiments and Main Evidence

**Across-$T$ flexibility。** 单个 MTT model 在 CIFAR10/100 与 ImageNet 的 $T=2\ldots6$ 保持稳定 accuracy。CIFAR10-DVS 的 VGGSNN 均在 $T=10$ 或 $T_{\max}=10$ 训练；测试延伸到约 $T=200$ 时，MTT 仍接近 $70\%$，而 SDT/TET 降至约 $57\%$–$59\%$。这支持 MTT 降低 out-of-training-range timestep sensitivity，但不是完全 invariant。CIFAR100/ResNet-18 上，MTT 在 $T=1,2$ 分别为 $72.09\%$、$76.54\%$，高于表中 conversion baselines；到 $T=64$ 仍为 $79.42\%$。跨论文 training protocols 不完全相同，不能据此宣称全面优于 conversion。

**Dynamic inference。** 与 SEENN-I 结合后，平均 $T=1.20$ 时 accuracy 从 $96.38\%$ 提至 $96.58\%$，平均 $T=1.09$ 时仅从 $96.07\%$ 提至 $96.08\%$。这证明兼容性，但增益分别只有 $0.20$ 和 $0.01$ 个百分点。

**Real Speck2e deployment。** N-MNIST 的 6,160-parameter 3C1FC 模型中，MTT 从 Torch $99.16\%$ 到 Speck $98.57\%$，下降 $0.59$ 个百分点；SDT 从 $98.09\%$ 降至 $92.77\%$。这是“nearly lossless”的直接硬件证据，但仅覆盖小模型和 N-MNIST。模拟器–芯片 Spike Difference 为 $3.92\%$，接近同一模型两次芯片运行的 $2.81\%$，并明显低于 time-stepped output–chip 的 $28.77\%$。

**Large-model event-driven simulator。** CIFAR10-DVS/VGGSNN 上，MTT simulator accuracy 为 $58.5\%$，SDT 为 $48.4\%$，提高 **10.1 个百分点**；这不是 10.1% relative gain，也不是真实 Speck measurement。DVS-Gesture simulator 提升仅 $1.14$ 个百分点。Simulator 的硬件对齐只在较小 N-MNIST 设置和 output spike-count metric 上验证，不能证明大模型的 spike timing、内部 states、latency 或 energy 与芯片一致。

**Ablation and robustness。** ResNet-18 中每 stage blocks 数 $g$ 从 8 降到 1 时，模型由 NMT 逐步变为细粒度 MTT，整体 accuracy 提升，支持 network partitioning。没有 BN calibration 会造成显著 accuracy degradation，10-batch calibration 可恢复。Weight/input Gaussian-noise tests、较小 gradient norms 与 flatter loss landscape 支持 perturbation robustness；它们不足以单独证明跨数据分布 generalization。

**SOTA comparison。** MTT 在 CIFAR10/100、ImageNet 和 N-Caltech101 上具有竞争力；CIFAR10-DVS 平均 $82.8\%$ 接近但低于表中 TET 的 $83.17\%$。论文的主要贡献是 one-training–multiple-$T$ 与 deployment stability，而不是无条件 overall SOTA。

## 6. Strengths and Limitations

**Strengths**

- 将 fixed-$T$ training 与 clock-driven dynamic inference、fully event-driven deployment 之间的结构错配明确化。
- MTT 只共享一套 weights，并以 stage-wise sampling 扩大 temporal-structure coverage；方法可接入既有 backbone。
- 同时提供 across-$T$、dynamic early exit、真实 Speck2e、小/大规模 simulator、partition 与 BN ablation。
- 清楚暴露 BN statistics、bias-free chip mapping 和 event-driven simulator validation 等实际部署问题。

**Limitations**

- 真实 Speck2e accuracy 仅覆盖 N-MNIST 小网络；CIFAR10-DVS 的 10.1-point 增益来自软件模拟器。
- Spike Difference 只比较 output spike counts，不验证精确 timing、隐藏层 trajectories、功耗或延迟；hardware zero-spike denominator 的处理未说明。
- 论文把 event-driven dynamics 近似为 $T\rightarrow\infty$ 有助于直觉说明，但真实 asynchronous ordering、timestamp precision 和 hardware scheduling 不能由单一全局 $T$ 完全刻画。
- TTM downsampling 可能把 binary spikes 变成 counts；对 event semantics、scale 和 hardware mapping 的影响说明不足。
- BN calibration 使用 training batches，增加部署准备步骤；跨 $T$ 共用 $T_{\max}$ statistics 的边界仍需核查。
- MTT 的 GPU training time 约为 SDT 的 $1.6\times$–$1.77\times$；更强部署灵活性并非无成本获得。
- “conversion 无法处理 DVS”“MTT 提升 generalization”“首次 large-scale fully event-driven evaluation”均应保留为作者范围内的 claim。

## 7. Relation to Other Papers and Survey Taxonomy

本文连接 Survey 的 temporal dynamics、SNN training、latency/energy/hardware evidence 和 deployment limitations。它不提供新的 event representation；其核心价值是提醒综述区分 sensor time、training discretization、clock-driven inference steps 与 asynchronous hardware execution，并要求部署结论说明测试平台。

### PDF-verified literature relations

- **Spatio-Temporal Backpropagation for Training High-Performance Spiking Neural Networks (Yujie Wu et al., Frontiers in Neuroscience 2018)** — `foundation`。STBP 将 time-stepped SNN 作为 recurrent computation 以 surrogate gradient/BPTT 直接训练；本文识别该 fixed-$T$ paradigm 的 temporal inflexibility，并在其训练框架上混合 temporal structures。对应 Section 4: SNN training。证据：Introduction and Preliminaries 3.4, PDF pp.1–4, citation Wu et al. (2018) and mapped bibliography。当前 active corpus 未覆盖。
- **Temporal Efficient Training of Spiking Neural Network via Gradient Re-Weighting (Shikuang Deng et al., arXiv 2022)** — `baseline`。TET 是 fixed-time-step direct-training comparator；Fig. 4 显示其与 SDT 一样在远离训练 $T$ 时明显退化，而 MTT 针对 across-$T$ flexibility 优化。对应 Section 4: training and temporal generalization。证据：Related Work and Experiments 5.1, PDF pp.2 and 8, citation Deng et al. (2022) and mapped bibliography。当前 active corpus 未覆盖。
- **Optimal ANN-SNN Conversion for High-Accuracy and Ultra-Low-Latency Spiking Neural Networks (Tong Bu et al., arXiv 2023)** — `baseline`。QCFS 是 Table 3 的 ANN-SNN conversion comparator；本文用无需 target-$T$ fine-tuning 的单个 MTT model 比较低 timestep 与跨 timestep 表现。对应 Section 4: direct training versus conversion。证据：Related Work and Table 3, PDF pp.2 and 8, citation Bu et al. (2023) and mapped bibliography。当前 active corpus 未覆盖。
- **SEENN: Towards Temporal Spiking Early-Exit Neural Networks (Yuhang Li et al., arXiv 2023)** — `extends`。SEENN 根据 confidence 动态决定 per-sample inference steps；本文以 MTT weights 替代原 TET weights，验证 temporal flexibility 可支持 clock-driven dynamic early exit。对应 Section 6: latency and dynamic inference。证据：Related Work and Table 4, PDF pp.2 and 8, citation Li et al. (2023c) and mapped bibliography。当前 active corpus 未覆盖。
- **Speck: A Smart Event-Based Vision Sensor with a Low Latency 327K Neuron Convolutional Neuronal Network Processing Pipeline (Ole Richter et al., Nature Communications 2024)** — `foundation`。Speck2e 提供 fully event-driven vision-sensor/neuromorphic deployment platform；本文在其 Devkit 上测量 N-MNIST accuracy 与 simulator–hardware Spike Difference。对应 Section 6: neuromorphic hardware evidence。证据：Method 4.4 and Experiments 5.1, PDF pp.7–9, citation Richter et al. (2023) and mapped bibliography；registry 将该 preprint 规范化为 2024 journal version。当前 active corpus 未覆盖。

## 8. Survey-Usable Takeaways

1. SNN 的 timestep 必须注明是 sensor framing、GPU simulation iteration、clock-driven inference step，还是 physical/event timestamp；这些时间概念不可混用。
2. Fixed-$T$ direct training 可能让 weights 和 BN statistics 过拟合离散时间结构，导致 dynamic-$T$ 或 asynchronous deployment degradation。
3. MTT 通过 stage-wise timestep sampling 和 TTM 训练一套跨时间结构 weights；其价值是 deployment flexibility，不是消除 temporal dynamics。
4. “Fully event-driven”表示没有统一全局 clock step，相关 neuron 在 event arrival 时局部异步更新；它可避免 empty-step state updates，但实际能效仍需硬件测量。
5. 真实硬件与 simulator 结果必须分开报告：本文只有 N-MNIST 小模型在 Speck2e 上直接测量，大规模 DVS 结果来自经过有限对齐的软件模拟器。
6. 本文的 10.1% 表述应写成 CIFAR10-DVS simulator 上相对 SDT 提高 10.1 个百分点；“nearly lossless”应限定为 N-MNIST/3C1FC/Speck2e。
7. 灵活部署的代价包括 TTM、多个 sampled forwards/backwards、BN calibration 和约 $1.6\times$–$1.77\times$ GPU training runtime。

## Supplement Points

### Questions and Clarifications

#### 1. Timestep 到底是什么？Clock-driven 与 fully event-driven 有何区别？

本文的 timestep 是 time-stepped simulation 的离散更新轮次。静态图像通常重复输入 $T$ 次；DVS events 则按 timestamp 分成 $T$ 个 temporal bins。Clock-driven execution 每个全局 step 都更新所有 neuron states，即使某个 bin 没有 event；fully event-driven execution 不设统一迭代轮次，只在带 timestamp 的 event 到达时更新受影响 neurons。前者便于 GPU batch parallelism 和 BPTT，后者更接近传感器连续产生事件时的异步、always-on execution。

“time-step-free”不是没有时间，而是没有人为统一的 global time grid。系统仍保留 event timestamps、事件先后顺序、膜电位随间隔的 decay，以及真实 wall-clock latency。其潜在低功耗来自避免 empty-step updates；实时友好来自 event 到达即可处理，无需等待整帧；生物相似性来自局部 asynchronous state transition。上述优势依赖具体芯片实现，不能仅凭算法标签推断真实 energy。

#### 2. 为什么先用 time-stepped simulation 训练，再部署到 event-driven hardware？

异步事件具有不规则、依赖顺序的计算图，难以像固定 $T$ tensor 一样在 GPU 上批量并行和执行 BPTT。Time-stepped simulation 将事件分箱并展开成规则 tensors，从而复用 PyTorch training。Synaptic weights 和 neuron equations 的语义可以迁移到芯片，但离散近似与真实异步 event ordering 会产生不同 membrane trajectories 和 spike outputs；因此“weights 可直接部署”不等于行为完全一致。MTT 正是通过多种训练时间结构降低这种依赖。

#### 3. 为什么主流 ANN-SNN conversion 被说成不能处理 DVS，并且只能得到 IF SNN？

主流 rate-based conversion 先训练处理静态 activations 的 ANN，再令 SNN 在多个 steps 的 firing rate 逼近这些 activations。IF neuron 的无 leak accumulation 更容易建立 ReLU activation 与 spike count/rate 的对应；LIF leak 会使相同输入在不同 timing 下得到不同累计响应。DVS 的信息则包含 event timing 和 ordering，不天然对应单个静态 ANN activation target。论文中的说法应理解为这类主流 conversion assumptions 的限制，而不是任何 conversion 方法在理论上都不可能处理 DVS 或 LIF。

#### 4. “Outputs 与 time-step-based temporal structure 解耦”以及“NMT 同时训练 6 个 SNN”是什么意思？

解耦指同一输入在不同 $T$ 或 $\mathbf t$ 下仍尽量给出一致任务预测，而不是输出在数值上绝对相同或模型不再利用时间。若 sampling space 为 $T\in\{1,\ldots,6\}$，同一组 parameters 可展开成 6 个 computation graphs；它们共享 topology 和 weights，但 update 次数、membrane trajectories 与 spike sequences 不同。NMT 每次只抽取其中若干个，例如 3 个，分别 forward/backward 后统一更新；“同时训练 6 个”指整个训练过程联合覆盖六种共享权重 variants，不是每次 iteration 保存或运行六套独立模型。

#### 5. Spike Difference 在做什么？

Hardware output $\mathbf s_0$ 是 Speck2e 输出层各 neurons 在一个样本期间的累计 spike counts；simulator output $\mathbf s$ 是软件事件驱动模拟器在相同 input/weights 下的对应 counts。论文定义：

$$
\operatorname{SD}(\mathbf s_0,\mathbf s)
=
\frac{\sum_{i=0}^{N_f-1}|s_0[i]-s[i]|}
{\sum_{i=0}^{N_f-1}s_0[i]}.
$$

差异可能来自有限数值精度、weight/state quantization、timestamp rounding、事件调度顺序、芯片非理想性和 simulator 建模简化。衡量 SD 是为了判断软件 simulator 能否替代容量有限的 Speck2e 承担较大模型实验。低 SD 只说明 output spike-count vector 接近；它不验证 spike timing、hidden states、latency 或 energy。若 hardware 总输出 spike 为零，分母为零，论文未说明处理方式：`Needs further check`。

### Additional Technical Details

#### 1. Downsampling 与 Upsampling TTM

对于 $t_{\mathrm{in}}=5 \rightarrow t_{\mathrm{out}}=3$，可将输入帧均匀分成 $\{1,2\}$、$\{3\}$、$\{4,5\}$，并计算

$$
y_1=x_1+x_2,\qquad y_2=x_3,\qquad y_3=x_4+x_5.
$$

对于 $3\rightarrow5$，使用相同的对应分组反向复制：

$$
y_1=x_1,\quad y_2=x_1,\quad y_3=x_2,\quad y_4=x_3,\quad y_5=x_3.
$$

TTM 本身没有论文声明的 learnable parameters。Downsampling 的 sum 保留 grouped activity quantity，但会改变数值范围；upsampling replication 会重复同一 activity，因此它们都不是严格保持原始 event timestamps 的可逆变换。

#### 2. Algorithm 1 的一次 iteration

一次 iteration 读取 mini-batch $(x_i,y_i)$，随后循环 $j=1,\ldots,s$：采样含 $G$ 个 stage timesteps 的 $\mathbf t^{(j)}$；执行 $S_P(x_i,\mathbf t^{(j)})$，其中 stage boundaries 通过 TTM 转换；计算 task loss 并立即 backward，将 gradient 累积到共享 parameters。完成 $s$ 次后，optimizer 只执行一次 update：

$$
\nabla_\theta \mathcal L_{\mathrm{MTT}}
=
\sum_{j=1}^{s}
\nabla_\theta
\mathcal L\left(S_P(x_i,\mathbf t^{(j)}),y_i\right),
$$

$$
\theta
\leftarrow
\theta-\eta\nabla_\theta\mathcal L_{\mathrm{MTT}}.
$$

Algorithm 1 只写 collect gradients，没有明确说明实现对 $s$ 项求和还是取平均；精确 normalization 为 `Needs further check`。逐个 configuration backward 后释放 graph，使 memory 不必随 $s$ 线性增加。
