---
tags: [SNN, event-camera, data-augmentation, relevance-propagation, SLRP, SLTRP, EventRPG]
---

# Summary V2｜EventRPG: Event Data Augmentation with Relevance Propagation Guidance

## 1. Core Understanding

EventRPG 是一个面向 **event-based SNN classification** 的 model-aware data augmentation framework。其核心链条不是直接设计新的随机增强，而是先提出适用于 SNN 的 relevance propagation：**Spiking Layer-Time-wise Relevance Propagation（SLTRP）** 和 **Spiking Layer-wise Relevance Propagation（SLRP）**，从而生成与预测相关的 CAM 和 saliency map；随后利用这些 relevance maps 指导 **RPGDrop** 和 **RPGMix**，优先扰动模型依赖的区域，并减少两个 label-related regions 在混合时的重叠。

本文属于 **Core SNN**：SLTRP 的推导直接依赖 membrane voltage、current input 和跨 time-step dynamics。实验主要采用 directly trained SNN，如 Spike-VGG11、SEW ResNet-18、LIF/PLIF neuron，并非 ANN-to-SNN conversion。EventRPG 的主要贡献位于训练阶段的 augmentation 与 SNN interpretability，而不是提出新 backbone，也不是 neuromorphic hardware 方法。

## 2. Problem and Motivation

Event-based classification 容易出现 overfitting。作者将其部分归因于 SNN 相对有限的 spatial representation capability，但该因果解释主要作为 motivation，论文没有通过专门实验直接证明。

已有 event augmentation 包括 geometric transformation、random EventDrop 和 EventMix。其共同问题是缺乏对模型当前决策区域的感知：随机删除背景 events 可能几乎不影响模型；随机混合两个 event streams 则可能让两个目标严重重叠，破坏 event texture，并使基于整幅 mask 面积计算的 mixed label 与实际保留的目标信息不匹配。

图像领域已有 saliency-guided augmentation，但普通 CAM、Grad-CAM 或 activation-based SAM 没有显式处理 SNN 的 temporal state。SAM 能显示 intermediate activation，却不直接解释某一预测类别的贡献。本文因此先解决“如何在 SNN 中传播 prediction relevance”，再用该解释结果指导增强。

## 3. Method Overview

整体流程为：

$$
\text{event sequence}
\rightarrow
\text{SNN prediction}
\rightarrow
\text{SLRP / SLTRP}
\rightarrow
\text{CAM / saliency map}
\rightarrow
\text{RPGDrop / RPGMix}
\rightarrow
\text{augmented sample}.
$$

作者首先使用 Contrastive Layer-wise Relevance Propagation（CLRP）初始化各 time step 的 output relevance，再根据数据类型选择 SLRP 或 SLTRP 向前传播：

- relevance 传播到某个 intermediate layer，并沿 channel dimension 聚合，可形成 CAM；
- relevance 一直传播到 input level，可形成更细粒度的 saliency map；
- RelCAM 则进一步结合 relevance 和 feature maps。

EventRPG 将 RPGDrop、RPGMix 与 NDA 中的 geometric policies 组合。每个 event stream 先随机采样一种 policy 和 magnitude，随后以 $0.5$ 的概率执行 RPGMix。论文未引入新的推理期分类模块，因此其功能定位是 training-time augmentation。

## 4. Key Components and Mechanisms

### 4.1 LRP 与 Conservation Property

LRP 为每个 neuron 分配 relevance score，表示其对目标预测的贡献，并要求逐层传播时 relevance 总量保持：

$$
\sum_i R_i^{(l-1)}
=
\sum_j R_j^{(l)}.
$$

在线性层中，输出 neuron 的 relevance 按各输入连接的正、负贡献比例重新分配。该性质保证 relevance 不会在解释过程中凭空产生或消失，但 conservation 本身并不等于 attribution 必然语义正确，仍需 faithfulness experiment 验证。

### 4.2 SLTRP：同时沿 layer 和 time 传播

SNN neuron 在时刻 $t$ 的状态被统一写为：

$$
f(V,I)
=
cV[t-1]+dI[t],
$$

其中 $cV[t-1]$ 表示历史 membrane state 的贡献，$dI[t]$ 表示当前输入贡献。作者定义 $\gamma[t]$，用于决定当前 relevance 中有多少应沿 membrane connection 传回前一时刻；其余 $1-\gamma[t]$ 归因于当前输入。

原文式（10）和式（11）复用了 $R^{(l-1)}[t]$ 表示“尚未拆分的 relevance pool”和“拆分后的 input relevance”，容易混淆。等价地，可定义：

- $A_t=R^{(l)}[t]$：后续网络直接分配给时刻 $t$ 的 relevance；
- $Q_t$：时刻 $t$ 尚未拆分的 relevance pool。

则递推可清楚写成：

$$
Q_{t-1}
=
A_{t-1}+\gamma[t]Q_t,
$$

$$
R^{(l-1)}[t]
=
\left(1-\gamma[t]\right)Q_t.
$$

第一式说明，时刻 $t-1$ 的 relevance 同时来自其自身的直接路径 $R^{(l)}[t-1]$，以及未来时刻经 membrane state 返回的 relevance；第二式把当前 pool 中不属于历史状态的部分分给当前 input current。最终满足：

$$
\sum_{t=1}^{T}R^{(l-1)}[t]
=
\sum_{t=1}^{T}R^{(l)}[t].
$$

因此 SLTRP 可得到 time-resolved attribution，回答模型在不同时刻关注哪些区域。

### 4.3 SLRP：聚合时间以降低成本

对于由静态图像转换、目标空间位置随时间变化较小的数据，作者只保留 time-aggregated relevance：

$$
R^{(l)}
\equiv
\frac{1}{T}
\sum_{t=1}^{T}R^{(l)}[t].
$$

根据 SLTRP 的时间守恒关系，spiking layer 聚合前后有 $R^{(l-1)}=R^{(l)}$。对于 linear layer，则先沿时间聚合每条连接的正、负贡献，再使用普通 $\alpha\beta$-rule。SLRP 省略的是 relevance backward 中的逐时间递推，而不是 SNN forward 的时间维度；代价是无法给出 $S[t,x,y]$ 形式的 temporal saliency。

### 4.4 CAM、saliency map 与 relevance propagation

Relevance propagation 是“如何从输出向输入追溯贡献”的计算规则；CAM 和 saliency map 是由该规则产生的不同层级结果。CAM 来自 intermediate features，通常分辨率较粗，适合定位 label-related region；saliency map 将 relevance 传播到输入层，表示每个输入位置对目标预测的贡献，更适合控制 pixel-level dropping。

需要注意，高 relevance 严格表示 **model-prediction-related region**，不必然等于 ground-truth object。若模型依赖背景 shortcut，relevance map 也可能忠实揭示这种错误依赖。

### 4.5 RPGDrop

RPGDrop 对 saliency map 进行 normalization，并用 magnitude $\theta$ 控制强度。位置的 saliency 越高，该处 events 被删除的概率越大。其目的不是保护最显著区域，而是主动遮蔽模型当前最依赖的证据，迫使网络学习更分散的特征。过强 dropping 可能移除过多类别信息并引入 label noise。论文未完整给出 normalization、概率截断和采样公式：`Needs further check`。

### 4.6 RPGMix

RPGMix 对两个 samples 分别生成 CAM 或 saliency map，经 threshold 得到 bounding boxes，并通过 spatial translation 尽量减少两个 label-related regions 的重叠。随后采用 CutMix-style mask，使同一像素只保留一个 event stream 的信息。

mixed label 根据两个 bounding boxes 的有效面积计算：

$$
L_{\mathrm{mix}}
=
\frac{
L_1\left(w_1h_1-S_{\mathrm{overlap}}\right)
+
L_2w_2h_2
}{
w_1h_1+w_2h_2-S_{\mathrm{overlap}}
}.
$$

重叠区域由 sample 2 的 mask 覆盖，因此 overlap 只从 sample 1 的有效面积中扣除。该设计比按整幅 mask 面积分配标签更关注目标区域，但 bounding-box area 仍不等同于真实 object pixels 或 saliency mass。threshold、connected components、边界外 events 的处理方式未充分说明：`Needs further check`。

## 5. Experiments and Main Evidence

### 5.1 Relevance map 的 faithfulness

作者使用 Average Increase（A.I.，越高越好）和 Average Drop（A.D.，越低越好）评估 attention map 作为 mask 后对目标输出的保持程度。

- N-Caltech101 上，SLRP/SLTRP-CAM 的 A.I. 为 $34.24$，SLRP-Saliency 的 A.D. 为 $4.18$，明显优于主要 baselines。
- CIFAR10-DVS 上，SLTRP-Saliency 达到 A.I. $9.51$、A.D. $19.98$，但与 SLRP-Saliency 的差距极小。
- N-Cars 上，Grad-CAM++ 的 A.I. $26.04$、A.D. $5.41$ 优于作者方法。
- DVS-Gesture 上，saliency map 获得更高 A.I.，而 RelCAM 获得更低 A.D.；SL-Animals 上最高 A.I. 来自 relevance-based RelCAM，但最低 A.D. 来自 SAM。

因此实验支持 relevance-based maps 在多数设置中具有较强或有竞争力的 faithfulness，但不支持“所有数据集和指标全面最优”。Figure 4 提供了 SLTRP attention 随时间从手部转向手臂的定性示例，但缺少 IoU、pointing game 或 temporal tracking metric，不能视为全面的 localization proof。

### 5.2 Classification performance

在相同 TET + Spike-VGG11 配置的内部比较中：

- N-Caltech101：Identity $75.70\%$，EventRPG-Saliency $85.62\%$，提升 $9.92$ 个百分点；
- CIFAR10-DVS：Identity $78.85\%$，EventRPG-CAM $85.55\%$，提升 $6.70$ 个百分点；
- N-Cars：EventRPG-Saliency $96.00\%$，低于不同配置下 EventMix 的 $96.29\%$。

在 SEW ResNet-18 action recognition 中：

- DVS-Gesture 的 EventRPG 最高为 $96.53\%$，优于作者同配置复现的 Identity、NDA 和 EventDrop，但低于 EventMix 的 $96.75\%$，也不是 overall SOTA；
- SL-Animals 4 sets 最高为 $91.59\%$，比第二好的 augmentation 高 $3.82$ 个百分点；
- SL-Animals 3 sets 最高为 $93.75\%$，高 $4.20$ 个百分点。

SLRP 与 SLTRP 没有形成稳定优劣规律：动态任务中 SLTRP 在部分设置最好，但 SL-Animals 4 sets 的最佳结果来自 SLRP。因而 temporal attribution 是 SLTRP 的明确能力，而稳定的 accuracy superiority 尚未得到证明。

附录中，EventRPG 在 mini N-ImageNet 达到 Top-1 $40.90\%$、Top-5 $67.74\%$，分别比 NDA 高 $5.06$ 和 $4.10$ 个百分点。单独比较 mix strategy 时，RPGMix 在 N-Caltech101、SL-Animals 4 sets 和 3 sets 上分别达到 $81.75\%$、$88.67\%$ 和 $90.45\%$，均优于 SaliencyMix、PuzzleMix 及其 mask-only variant，为 RPGMix 的独立有效性提供了补充证据。

### 5.3 Efficiency evidence

Table 2 测量的是 GPU 上生成 CAM/saliency map 的平均时间。CAM 只传播到 intermediate layer，SLRP-CAM 和 SLTRP-CAM 较快；SLTRP-Saliency 必须逐层、逐时间传播，明显慢于 SLRP-Saliency。

Figure 5 报告 augmentation time per event stream。relevance propagation 可通过 batch parallelization 摊薄，当 batch size per GPU 大于 4 时，EventRPG 的单样本 augmentation runtime 接近 NDA 和 EventDrop。该证据属于 **GPU software runtime / amortized latency**，不是 hardware-measured energy、neuromorphic hardware result、完整训练 wall-clock time 或 memory benchmark。

## 6. Strengths and Limitations

**Strengths**

- 将 LRP 扩展到包含 membrane memory 的 SNN，并区分 time-resolved SLTRP 与低成本 SLRP。
- 将 interpretability 与 augmentation 连接成闭环，而不是仅把 saliency map 用于事后可视化。
- RPGDrop 针对无效背景扰动，RPGMix 针对目标重叠和 mixed-label mismatch，设计动机明确。
- 在多个 object/action datasets、两类 SNN backbones 及附录的大规模 mini N-ImageNet 上取得明显增益。

**Limitations**

- 作者明确限制当前方法只能用于 classification；detection、segmentation、tracking 中的 box/mask/label transformation 尚未定义。
- augmentation quality 依赖 relevance quality，而 model attention 不一定对应真实目标。
- 主要结果报告固定 seed 下的 best accuracy，缺少多次独立运行的 mean $\pm$ std；小幅差异的稳定性无法判断。
- 跨论文 SOTA 对比混合了不同 backbone、neuron、resolution、timesteps 和 training methods，不能完全隔离 augmentation 的独立贡献。
- 完整 pipeline 缺少更细的 ablation，例如 translation、non-overlap placement、CutMix mask 和 bounding-box label weighting 各自的贡献。
- threshold/reset 对 relevance 的影响、数值 stabilizer、CLRP target initialization、训练早期 relevance 的可靠性、warm-up、显存与完整训练成本均未充分说明：`Needs further check`。

## 7. Relation to Other Papers and Survey Taxonomy

本文主要属于：

- **SNN training and data augmentation**：通过 model-aware augmentation 缓解 overfitting；
- **SNN interpretability**：提出面向 spiking temporal dynamics 的 relevance propagation；
- **temporal attribution**：SLTRP 提供逐 time-step saliency；
- **event-based classification**：覆盖静态图像转换的 object datasets 与真实动态 action datasets；
- **generalization and robustness**：通过遮蔽与混合高 relevance regions 提高训练样本难度。

与 EventDrop、EventMix 相比，EventRPG 的区别是增强位置由模型 relevance 决定；与 SAM 相比，它强调 prediction-conditioned contribution，而不是仅根据 activation 强度；与 Grad-CAM 类方法相比，它专门处理 spiking layer 的 temporal state。它不属于新型 event representation、dense prediction architecture 或 neuromorphic hardware efficiency 工作。

### PDF-verified relation backfill

主要路线是将 LRP 扩展为 SNN layer-time relevance propagation，再以 saliency 引导 event dropping/mixing。

- **On Pixel-Wise Explanations for Non-Linear Classifier Decisions by Layer-Wise Relevance Propagation (Sebastian Bach et al., PLOS ONE 2015)** — `foundation`。该工作提供 relevance conservation and saliency 的基础机制；当前论文将其用于自身的 event/SNN pipeline，而不是把该前驱本身作为新贡献。 对应 Sections 3 and 4: SNN interpretability and training。证据：Introduction and Preliminary, PDF pp.1-2, Bach et al. 2015 bibliography entry。 当前 active corpus 未覆盖。 值得 backward search。
- **Visual Explanations from Spiking Neural Networks Using Inter-Spike Intervals (Youngeun Kim et al., Scientific Reports 2021)** — `extends`。当前论文沿用该工作的 SNN saliency maps，并针对当前任务增加新的结构或训练约束。对应 Section 3: SNN interpretability。证据：Introduction and Experiments 5.1, PDF pp.2 and 9-10, Kim and Panda 2021b bibliography entry。当前 active corpus 未覆盖。
- **EventMix: An Efficient Data Augmentation Strategy for Event-Based Learning (Guobin Shen et al., Information Sciences 2023)** — `baseline`。该工作是 event-stream mixing augmentation 的实验 comparator；当前论文与其主要区别在于本文第 3–4 节所述的核心机制。 对应 Section 4: event-SNN training。证据：Introduction and Experiments Table 3, PDF pp.2 and 11, Shen et al. 2023 bibliography entry。 当前 active corpus 未覆盖。

## 8. Survey-Usable Takeaways

1. EventRPG 展示了一种两阶段的 model-aware event augmentation：先解释 SNN 的预测依据，再据此构造更有针对性的 event dropping 和 mixing。
2. SLTRP 的核心价值是 time-resolved attribution；SLRP 通过聚合时间降低解释成本，且在多项分类实验中不弱于 SLTRP。
3. 实验较有力地支持 EventRPG 对 event-based SNN classification 的有效性，但不支持其在所有 faithfulness metrics、所有动态任务或所有配置中全面最优。
4. SOTA 结论应限定在 N-Caltech101、CIFAR10-DVS 和 SL-Animals 的相应表格设置；DVS-Gesture 与 N-Cars 不属于 overall best。
5. 论文中的 efficiency 证据是 GPU runtime 和 batch-amortized augmentation latency，不能等同于真实 energy efficiency 或 neuromorphic deployment advantage。
6. 当前结论应限制在 classification；向 detection、tracking、segmentation 或 self-supervised learning 的扩展仍属于未来方向。

## Supplement Points

### Questions and Clarifications

#### 1. Saliency map、CAM 与 relevance propagation 分别是什么？三者是什么关系？

这三个概念并不是同一层级：**relevance propagation 是计算贡献的方法，CAM 和 saliency map 是把贡献映射到空间位置后得到的结果。**

假设一个 SNN 将输入 event sample 预测为“dog”。模型内部可能同时响应狗头、身体轮廓和背景事件。relevance propagation 从目标类别输出开始，把该输出的 relevance 逐层分配给前面的 neuron、feature 和 input location，试图回答：

> 当前“dog”预测具体由哪些内部特征和输入位置贡献而来？

它与普通 gradient 的含义不同。gradient 主要衡量输入发生微小变化时输出有多敏感，即 sensitivity；relevance propagation 更关注当前这个实际输入中，各部分已经为目标预测贡献了多少，即 contribution attribution。

若某个 intermediate layer 的 feature/relevance tensor 为：

$$
R^{(l)} \in \mathbb{R}^{C \times H' \times W'},
$$

沿 channel dimension 聚合后可以形成较粗粒度的 CAM：

$$
M_{\mathrm{CAM}}(h,w)
=
\sum_{c=1}^{C}R^{(l)}(c,h,w).
$$

CAM 通常具有较低空间分辨率，适合回答“模型主要关注哪个目标区域”，因此本文主要用它帮助 RPGMix 定位 label-related bounding box。

如果 relevance 继续穿过全部网络层，一直传播到输入侧，则可形成 saliency map。对时间聚合后的 SLRP，其结果可理解为：

$$
S \in \mathbb{R}^{H \times W},
$$

表示整个 event sequence 中每个空间位置对目标预测的综合贡献；对保留时间维度的 SLTRP，则原则上可以得到：

$$
S \in \mathbb{R}^{T \times H \times W},
$$

从而观察模型在不同时刻关注的位置如何变化。saliency map 更接近输入分辨率，因此本文用它为 RPGDrop 提供位置相关的 drop probability。

三者的关系可以概括为：

$$
\text{target-class output}
\xrightarrow{\text{relevance propagation}}
\begin{cases}
\text{intermediate-layer CAM},\\
\text{input-level saliency map}.
\end{cases}
$$

需要注意，高 relevance 只说明该区域与**当前模型的预测**密切相关，不保证它一定是 ground-truth object。如果模型错误依赖背景 shortcut，一个 faithful saliency map 也可能准确显示这种背景依赖。

---

#### 2. 式（10）和式（11）到底如何工作？为什么式（10）中会出现 $R^{(l)}[t-1]$？

原文的困难主要来自记号复用：$R^{(l-1)}[t]$ 既被用作“尚未拆分的 relevance pool”，又被用作“最终归因于当前输入的 relevance”。为了区分这两个阶段，可以重新定义：

- $A_t = R^{(l)}[t]$：后续网络已经直接分配给第 $l$ 个 spiking layer 在时刻 $t$ 的 relevance；
- $Q_t$：时刻 $t$ 尚未在历史 membrane state 与当前 input current 之间拆分的 relevance pool；
- $B_t = R^{(l-1)}[t]$：穿过该 spiking layer 后，最终分配给当前输入 $I[t]$ 的 relevance。

第 $l$ 个 spiking layer 的前向状态为：

$$
f(V,I)
=
cV[t-1]+dI[t].
$$

因此，时刻 $t$ 的 relevance pool $Q_t$ 也需要拆成两部分：

$$
\underbrace{\gamma[t]Q_t}_{\text{归因于历史 membrane state }V[t-1]}
+
\underbrace{\left(1-\gamma[t]\right)Q_t}_{\text{归因于当前 input current }I[t]}.
$$

用新记号重写原文式（10）和式（11）：

$$
Q_{t-1}
=
A_{t-1}+\gamma[t]Q_t,
$$

$$
B_t
=
\left(1-\gamma[t]\right)Q_t.
$$

这里的 $A_{t-1}=R^{(l)}[t-1]$ 不是由时刻 $t$ 临时产生的，而是**在 relevance 到达这个 spiking layer 之前，后续网络就已经直接分配给时刻 $t-1$ 的 relevance**。时刻 $t-1$ 对最终预测有两条贡献路径：

1. 它在时刻 $t-1$ 直接产生 spike/output，并通过后续网络影响预测，对应 $R^{(l)}[t-1]$；
2. 它的 membrane state 被保留到时刻 $t$，继续影响未来输出，对应从未来传回的 $\gamma[t]Q_t$。

因此，时刻 $t-1$ 的完整 relevance pool 必须把这两条路径相加，而不能只保留其中一条。

##### 三个 time steps 的完整例子

设后续网络已经向第 $l$ 个 spiking layer 的三个时刻分配：

$$
R^{(l)}[1]=1,
\qquad
R^{(l)}[2]=2,
\qquad
R^{(l)}[3]=3.
$$

取：

$$
\gamma[3]=0.6,
\qquad
\gamma[2]=0.5,
\qquad
\gamma[1]=0.
$$

首先初始化最后时刻：

$$
Q_3=R^{(l)}[3]=3.
$$

在时刻 3，归因于当前输入 $I[3]$ 的 relevance 为：

$$
R^{(l-1)}[3]
=
\left(1-\gamma[3]\right)Q_3
=
0.4 \times 3
=
1.2.
$$

其余部分沿 membrane path 返回时刻 2：

$$
\gamma[3]Q_3
=
0.6 \times 3
=
1.8.
$$

时刻 2 本身已经有直接 relevance $R^{(l)}[2]=2$，所以其完整 pool 为：

$$
Q_2
=
R^{(l)}[2]+\gamma[3]Q_3
=
2+1.8
=
3.8.
$$

再将 $Q_2$ 拆分：

$$
R^{(l-1)}[2]
=
\left(1-\gamma[2]\right)Q_2
=
0.5 \times 3.8
=
1.9,
$$

并向时刻 1 传回：

$$
\gamma[2]Q_2
=
0.5 \times 3.8
=
1.9.
$$

时刻 1 自身的直接 relevance 是 $R^{(l)}[1]=1$，因此：

$$
Q_1
=
R^{(l)}[1]+\gamma[2]Q_2
=
1+1.9
=
2.9.
$$

由于初始 membrane state 不再向更早时刻追溯，取 $\gamma[1]=0$：

$$
R^{(l-1)}[1]
=
2.9.
$$

最终得到：

$$
R^{(l-1)}[1]=2.9,
\qquad
R^{(l-1)}[2]=1.9,
\qquad
R^{(l-1)}[3]=1.2.
$$

总 relevance 保持不变：

$$
1+2+3
=
2.9+1.9+1.2
=
6.
$$

这个例子说明，较早时刻的输入可能通过 membrane memory 持续影响后续预测，因此会接收一部分来自未来 time steps 的 relevance。SLTRP 的核心并不是简单地把每个时刻独立解释，而是追踪这种跨时间贡献。
