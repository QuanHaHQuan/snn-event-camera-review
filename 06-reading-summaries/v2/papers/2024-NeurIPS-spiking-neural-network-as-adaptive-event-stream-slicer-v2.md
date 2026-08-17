---
tags:
  - event-camera
  - event-stream-slicing
  - spiking-neural-network
  - SNN-ANN-cooperation
  - adaptive-preprocessing
  - NeurIPS-2024
---

# Spiking Neural Network as Adaptive Event Stream Slicer｜Summary V2

## 1. Core Understanding

这篇论文研究的不是新的 event representation，也不是用 SNN 直接完成 tracking 或 recognition，而是研究位于 raw event stream 与 downstream ANN 之间的一个前置步骤：

$$
\text{raw event stream}
\rightarrow
\text{event slicing}
\rightarrow
\text{event representation}
\rightarrow
\text{downstream ANN}.
$$

传统方法通常采用 fixed-duration slicing 或 fixed-event-count slicing。它们分别固定真实时间长度或事件数量，但无法同时适应运动速度、目标尺度和事件密度变化。低速场景下，固定时间窗口可能积累的信息不足；高速场景下，同一窗口又可能包含大量冗余事件。固定事件数虽然保持每组事件数量一致，但对应的真实时间跨度会随运动状态显著变化。

SpikeSlicer 的核心思想是：先把连续事件流离散成很短的 voxel-grid event cells，再连续输入一个轻量 SNN；输出神经元何时产生 spike，何时就结束当前 event group。于是，SNN 的 spike time 被直接解释为 slicing boundary：

$$
S_{\mathrm{out}}[n]=1
\quad\Longrightarrow\quad
\text{在时间步 }n\text{ 切分事件流}.
$$

论文进一步提出两部分机制：

1. **SPA-Loss**：已知期望切点 $n^*$ 时，引导 SNN 在该时间步发放；
2. **Feedback-Update**：在当前切点附近生成多个候选切片，由 downstream ANN 的 task loss 选出局部最优切点 $n^*$，再用它监督 SNN。

因此，完整系统不是单次端到端反向传播，而是一个 alternating SNN–ANN optimization：

$$
\text{ANN evaluates candidate slices}
\rightarrow
n^*
\rightarrow
\text{SPA-Loss trains SNN}
\rightarrow
\text{SNN reslices data}
\rightarrow
\text{ANN fine-tuning}.
$$

这篇论文最有价值的地方，是将 SNN 的 spike timing 从普通中间神经活动转化为明确的数据处理动作：**切分原始事件流的时间边界**。

---

## 2. Problem and Motivation

### 2.1 Event slicing 与 event representation 的区别

设原始事件流为：

$$
\mathcal E=\{e_k\}_{k=1}^{N},
\qquad
e_k=(x_k,y_k,t_k,p_k).
$$

Event slicing 决定哪些事件属于同一组：

$$
\mathcal E
\rightarrow
\mathcal E_1,\mathcal E_2,\ldots,\mathcal E_K.
$$

Event representation 再决定如何将每组事件编码为神经网络可接收的 tensor：

$$
D_k=F(\mathcal E_k),
$$

其中 $F$ 可以是 event frame、voxel grid、time surface、event spike tensor、point 或 graph representation。

因此：

- slicing 决定时间边界；
- representation 决定编码形式；
- 两者是串联关系，不是同一问题。

### 2.2 Fixed-duration slicing 的问题

若始终每 $\Delta t$ 毫秒切一次：

- 低速或小目标：窗口内事件过少，目标边缘不完整；
- 高速或大目标：窗口内事件过多，出现拖尾、重复轮廓和冗余。

相同真实时间长度并不代表相同信息量。

### 2.3 Fixed-event-count slicing 的问题

若始终累计固定事件数 $M$：

- 高速场景很快达到 $M$，时间跨度可能过短；
- 低速场景需要很久才能达到 $M$，窗口内可能混入过长运动轨迹。

相同事件数量也不代表相同时间语义。

### 2.4 固定切片对下游任务确实敏感

Appendix C 在 N-Caltech101 上对两种固定切片规则、两个 ResNet backbone 和 15 个切片数量设置进行了 60 组实验。结果显示：

- 不同 slicing rule 和切片数量 $N$ 会带来显著性能波动；
- 不同 backbone 的最佳固定配置不同；
- ResNet-34 的最佳固定切片 accuracy 为 $78.48\%$；
- SpikeSlicer 达到 $82.54\%$，高出 $4.06$ 个百分点。

这说明最佳固定参数高度 task/model dependent，而动态切片具有明确研究动机。

---

## 3. Method Overview

### 3.1 从 raw events 到 event cells

完整事件流时间跨度为 $T$，先划分为短时间 event cells：

$$
C^\pm(x,y,t^*)
=
F_{\mathrm{voxel}}
\left(
G^\pm
\left(
x,y,t,
\{t\in[t^*,t^*+\delta t]\}
\right)
\right).
$$

若总时间为 $T$，则 event-cell 数为：

$$
N=\frac{T}{\delta t}.
$$

离散索引 $n$ 与真实时间区间之间的映射为：

$$
f_{\mathrm{time}}(n)
=
\left\{
t\mid
t\in[t_0+n\delta t,\,
t_0+(n+1)\delta t]
\right\}.
$$

因此，SNN 实际接收的是：

$$
C[0],C[1],\ldots,C[N-1],
$$

而不是原始异步事件逐个输入。

### 3.2 SNN 作为 slicing trigger

最后隐藏层特征 $h^{L-1}$ 被映射到一个输出 spiking neuron：

$$
S_{\mathrm{out}}
=
\operatorname{IF}
\left(
\operatorname{SNN}_{\mathrm{FC}}(h^{L-1})
\right).
$$

虽然正文以一般 LIF 形式推导，但 Appendix L 明确说明实际网络使用 IF neuron。因此实验实现中主要依赖：

- 跨时间累积；
- threshold crossing；
- reset；
- spike timing；

而不是 leakage-based temporal forgetting。

设上一次 spike index 为 $n_p$，当前 spike index 为 $n_c$，则当前 event group 的时间范围为：

$$
T_{\mathrm{group}}
=
\bigcup_{n=n_p+1}^{n_c}
f_{\mathrm{time}}(n).
$$

再从原始事件流提取该区间，并转换为 downstream representation：

$$
D_{n_c}
=
F
\left(
G^\pm(x,y,t,T_{\mathrm{group}})
\right).
$$

SNN 输入始终是短时间 voxel-grid event cells，但 downstream ANN 的输入 representation 可以是 frame、EST、voxel、point、graph 或 time surface。

### 3.3 SPA-Loss

SPA-Loss 由两部分组成：

$$
\mathcal L_{\mathrm{SPA}}
=
\mathcal L_{\mathrm{Mem}}
+
\mathcal L_{\mathrm{LA}}.
$$

#### Mem-Loss

作者不直接监督 binary spike，而是监督 no-reset membrane potential $U[n]$。

最终目标电位定义为：

$$
U_{\mathrm{target}}[n^*]
=
(1-\alpha)U_{\mathrm{lower}}
+
\alpha U_{\mathrm{upper}},
$$

其中：

$$
U_{\mathrm{lower}}=V_{\mathrm{th}},
$$

$$
U_{\mathrm{upper}}
=
\max
\left(
\beta V_{\mathrm{th}}
+
\gamma I[n^*],
V_{\mathrm{th}}
\right),
$$

于是：

$$
\mathcal L_{\mathrm{Mem}}
=
\left\|
U[n^*]
-
U_{\mathrm{target}}[n^*]
\right\|_2^2.
$$

其目标是让 $n^*$ 时刻达到阈值，同时避免将目标电位抬得过高。

#### LA-Loss

若当前实际 spike $n_c$ 早于目标 $n^*$，并且早期膜电位形成 hill：

$$
U[n_c]\ge U[n^*],
\qquad
n_c<n^*,
$$

则作者把 $U[n_c]$ 压向一条人为设定的线性参考轨迹：

$$
U_{\mathrm{ref}}[n_c]
=
\frac{n_c}{n^*}V_{\mathrm{th}}.
$$

对应：

$$
\mathcal L_{\mathrm{LA}}
=
\left\|
U[n_c]
-
\frac{n_c}{n^*}V_{\mathrm{th}}
\right\|_2^2.
$$

该损失主要针对 early-spike hill effect，并不严格约束整条膜电位轨迹线性或单调。

### 3.4 Feedback-Update

当 SNN 当前在 $n_c$ 发放时，在其邻域内生成 $2d+1$ 个候选切片：

$$
\{D_{n_c-d},\ldots,D_{n_c+d}\}.
$$

分别输入 downstream model $M$，得到 task loss：

$$
y_i=L_M(D_i).
$$

局部最优切点为：

$$
n^*
=
\arg\min_i y_i.
$$

这个 $n^*$ 是 ANN 生成的 pseudo-label，而不是人工标注。

训练流程分两阶段循环：

1. ANN 评价候选切片，生成 $n^*$，SPA-Loss 更新 SNN；
2. 更新后的 SNN 重新切片，ANN 在新数据上 fine-tune。

由于包含 neighborhood search、$\arg\min$ 和分阶段更新，该方法不是严格可微的 end-to-end optimization。

---

## 4. Key Components and Mechanisms

### 4.1 Event cell 不是最终 event group

Event cell 是最小离散输入单元，event group 是多个连续 cells 聚合后的最终切片。

例如：

$$
\delta t=5\ \mathrm{ms},
$$

SNN 在累计 13 个 cells 后发放，则当前 event group 的持续时间约为：

$$
13\times5=65\ \mathrm{ms}.
$$

因此 SpikeSlicer 的自适应性体现在“选择多少个 cells 后切”，而不是取消所有固定时间离散。

### 4.2 Reset / No-reset 双状态机制

SpikeSlicer 在输出神经元上概念性维护两条膜电位轨迹，它们共享同一个 SNN 参数和 synaptic current $I_\theta[n]$：

$$
I_\theta[n]
\rightarrow
\begin{cases}
V[n]: \text{执行 reset，产生真实 spike 与切点 }n_c,\\
U[n]: \text{不 reset，用于计算 SPA-Loss}.
\end{cases}
$$

Reset trajectory：

$$
V[n]
=
\beta V[n-1]
+
\gamma I_\theta[n].
$$

当 $V[n]\ge V_{\mathrm{th}}$ 时，真实输出 neuron 发放并 reset。该分支决定实际 slicing action。

No-reset trajectory：

$$
U[n]
=
\beta U[n-1]
+
\gamma I_\theta[n],
$$

即使超过阈值也不重置。它保留未经错误早期 spike 截断的累积轨迹。

论文公开的最终损失都基于 $U[n]$：

$$
\mathcal L_{\mathrm{SPA}}
=
\mathcal L_{\mathrm{Mem}}(U)
+
\mathcal L_{\mathrm{LA}}(U).
$$

因此，主要直接梯度路径是：

$$
\mathcal L_{\mathrm{SPA}}
\rightarrow
U[n]
\rightarrow
I_\theta[n]
\rightarrow
\theta.
$$

参数更新后，因为 $V[n]$ 与 $U[n]$ 共享 $\theta$ 和 $I_\theta[n]$，真实 reset trajectory 也随之改变：

$$
\theta\text{ changes}
\Rightarrow
I_\theta[n]\text{ changes}
\Rightarrow
V[n]\text{ changes}
\Rightarrow
n_c\text{ changes}.
$$

所以：

- $U[n]$ 主要负责直接 loss supervision；
- $V[n]$ 负责真实预测和切片决策；
- $V[n]$ 还通过 $n_c$、候选搜索中心、LA-Loss condition 和动态 $\alpha$ 间接影响训练；
- 它们不是两个独立网络，也不是两份输入数据。

### 4.3 Dynamic $\alpha$

$\alpha$ 决定目标电位在上下界之间的位置：

$$
U_{\mathrm{target}}
=
(1-\alpha)U_{\mathrm{lower}}
+
\alpha U_{\mathrm{upper}}.
$$

论文观察：

$$
\alpha\uparrow
\Rightarrow
\text{目标膜电位更高}
\Rightarrow
\text{spike 倾向更早},
$$

$$
\alpha\downarrow
\Rightarrow
\text{目标膜电位更低}
\Rightarrow
\text{spike 倾向更晚}.
$$

其更新规则为：

$$
\alpha
\leftarrow
\alpha
-
2\eta
\frac{1}{N_s}
\sum_{i=1}^{N_s}
(n_i^*-n_c^i).
$$

这更接近 signed-error feedback controller，而不是严格由 spike-index loss 链式求导得到的 gradient，因为推导中没有包含：

$$
\frac{\partial n_c}{\partial\alpha}.
$$

论文也没有说明如何强制保持：

$$
\alpha\in[0,1].
$$

### 4.4 SNN architecture

实际 SpikeSlicer 使用三层 convolution 和两层 linear 的 IF network：

$$
\{
16C3-GN-IF-AvgP2-
32C3-GN-IF-AvgP2-
64C3-GN-IF-AdaP2-
LN-IF-LN-IF
\}.
$$

没有 residual block 或 attention。训练使用 SGD、初始学习率 $10^{-4}$、cosine scheduler、batch size 32，并在 RTX 4090 GPU 上完成。

---

## 5. Experiments and Main Evidence

### 5.1 Toy spike-position control

在随机 event-cell toy task 中，SPA-Loss 能在少于 400 次迭代内将 spike 推向目标时间步。相较之下：

- MSE 只在部分时间步成功；
- CE 无法完成精确 spike-position control；
- Mem-Loss + LA-Loss 比单独 Mem-Loss 更平滑。

这些实验验证的是“已知 $n^*$ 时能否控制 spike time”，不是 ANN feedback 找到的 $n^*$ 是否全局最优。

### 5.2 Event-based tracking

在 FE108 上，SpikeSlicer 被接入多种 tracker。对 TransT 的公平 fixed-event baseline：

$$
\mathrm{RSR}: 51.0\rightarrow63.6,
$$

绝对提升为 $12.6$ 个百分点，相对提升约为：

$$
\frac{12.6}{51.0}\times100\%
\approx24.7\%.
$$

但不同 tracker 上并非全部提升，TaMOs 等配置中存在下降，因此不能描述为 universally beneficial。

### 5.3 Event-based recognition

在 DVS-Gesture、N-Caltech101、DVS-CIFAR10、SL-Animals 上，SpikeSlicer 在所列 ResNet 和 Swin 配置中均优于 fixed/random slicing。

ResNet-34：

$$
\text{DVS-Gesture}: 93.40\rightarrow96.18,
$$

即增加 $2.78$ 个百分点。

$$
\text{N-Caltech101}: 76.08\rightarrow82.54,
$$

即增加 $6.46$ 个百分点。

论文宣称 recognition 最大提升 $19.2\%$，实际对应 Swin-S 在 SL-Animals 上：

$$
56.25\rightarrow75.45,
$$

是单个 backbone–dataset 配置的 $19.20$ 个百分点，而不是平均提升。

N-ImageNet 扩展实验中：

$$
39.43\rightarrow45.48,
$$

即高出 fixed slicing $6.05$ 个百分点。

### 5.4 Representation compatibility

在 Time Surface、Event Spike Tensor、Voxel Grid 和 Event Frame 上，动态切片均取得正向增益，支持 slicing 与 representation 在一定程度上可以解耦。

但“plug-and-play”应限定为 architecture-level compatibility。接入新任务仍需要：

- downstream task loss；
- candidate labels；
- Feedback-Update；
- SNN training；
- ANN fine-tuning。

### 5.5 SPA-Loss ablation

SL-Animals 上：

| 设置 | ResNet-18 | ResNet-34 |
|---|---:|---:|
| Fixed Slice | 83.93 | 87.50 |
| Mem-Loss | 87.50 | 88.52 |
| Mem-Loss + LA-Loss | 88.39 | 89.73 |

结果说明 Mem-Loss 是主要机制，LA-Loss 在此基础上进一步改善 early-hill suppression。

### 5.6 Event-cell granularity

当 $N=15,20,25$ 时，平均 spike index 分别为：

$$
2.42,\quad3.15,\quad4.77,
$$

对应相对持续时间：

$$
16.13\%,\quad15.75\%,\quad19.08\%.
$$

说明改变离散粒度后，SNN 会调整实际 spike index，而不是固定在某个输入步。但三组比例并非严格一致，只能说处于相近范围。

### 5.7 Base 与 Small

PrDiMP 规模消融中：

| Model | Params | Energy | RSR | OP50 | OP75 | RPR |
|---|---:|---:|---:|---:|---:|---:|
| Base | 45.11 M | 0.85 mJ | 59.24 | 75.25 | 29.12 | 86.82 |
| Small | 0.42 M | 0.69 mJ | 60.88 | 78.19 | 32.34 | 87.19 |

Small 仅保留约 $0.93\%$ 参数量，并在该 PrDiMP 配置中所有指标更好。

但论文没有把后续实验统一明确为 Small：

- 主 tracking 表同时报告 B/S；
- Small 在多数 tracker 上更好，但 TaMOs 上 Base 的部分指标更优；
- recognition、representation、loss 和扩展实验多数只写 SpikeSlicer，没有标明版本；
- efficiency 表的额外能耗为 $0.85$ mJ，与 Base 完全一致，暗示该分析至少按 Base 估算。

因此，不能说后续实验全部采用 Small。

### 5.8 Energy 与 runtime

Table 3：

$$
259.26\rightarrow260.11\ \mathrm{mJ},
$$

理论能耗增加：

$$
0.85\ \mathrm{mJ}
\approx0.328\%.
$$

但该 energy 来自 45 nm MAC/AC operation model，不是 GPU 或 neuromorphic chip 实测。

Latency：

$$
0.045\rightarrow0.060\ \mathrm{s/image},
$$

相对增加约：

$$
33.3\%.
$$

因此，速度损失在比例上并不小，而且 caption 说明未包含 image processing time。

---

## 6. Strengths and Limitations

### 6.1 Strengths

1. 将 SNN spike time 赋予明确的 slicing-boundary 语义。
2. 关注 event representation 之前长期被忽视的 slicing stage。
3. 用 downstream task loss 定义 task-aware slicing quality。
4. 将 SNN 低层时序决策与 ANN 高层语义任务结合。
5. slicing mechanism 与多种 representation 兼容。
6. Small 模型表明该机制不依赖超大网络。
7. 在 tracking、recognition、多种 backbone 和 N-ImageNet 上提供了较广泛实验。

### 6.2 Limitations

1. Event stream 仍需先转换为固定 $\delta t$ 的 voxel-grid cells，不是真正 raw-event asynchronous processing。
2. Feedback-Update 是多阶段、task-specific training，不是严格端到端，也不是完全免训练的 plug-and-play。
3. Recognition 主要基于 single-frame representation，尚未验证 mainstream multi-frame setting。
4. Proposition 1 的理论证明存在 $U/V$ 混用、上下界措辞错误、$\max$ 修补失效和对 $n^*+1$ 论证不足等问题。
5. LA-Loss 的线性轨迹是人为 regularizer，不是由 IF/LIF dynamics 推导。
6. Dynamic $\alpha$ 是 heuristic signed-error update，缺少严格链式梯度和范围约束说明。
7. Algorithm 1 可能存在 off-by-one、tail-event handling 和 hidden-state reset 未说明问题。
8. Tracking 的细粒度标签来自线性插值，可能对急转、加速、形变和遮挡场景产生 pseudo-label error。
9. 正文重点介绍 LIF，但实际网络采用 IF，理论与实现说明不够统一。
10. Neuromorphic low-energy claim 仍停留在理论 operation estimate 和未来部署愿景。
11. “适用于任何 event-based vision task”的表述超出当前 tracking/recognition 实验证据。

---

## 7. Relation to Other Papers and Survey Taxonomy

### 7.1 Primary taxonomy

- Event stream slicing
- Adaptive temporal segmentation
- Task-aware event preprocessing
- SNN temporal decision
- SNN–ANN cooperation
- Hybrid neuromorphic pipeline
- Spike-timing-based control
- Efficient event processing

### 7.2 What it is not

- 不是新的 event representation；
- 不是 fully spiking tracker；
- 不是 fully spiking recognizer；
- 不是新的 neuron model；
- 不是 neuromorphic hardware deployment paper；
- 不是 raw-event end-to-end asynchronous implementation。

### 7.3 Relation to SNN research

该工作对 SNN 的使用具有明确方法学意义：

- SNN 不负责最终类别或 bounding box；
- SNN 负责判断“数据何时足够形成一个下游样本”；
- ANN 负责语义任务，并反向提供 task-dependent slicing supervision。

这构成一种“低层事件处理由 SNN 承担，高层任务由 ANN 承担”的 hybrid cooperation paradigm。

---

### PDF-verified relation backfill

主要路线是以 SNN output spike time 决定 event-cell boundary，并由下游 ANN task loss 交替产生 pseudo-label。

- **Better and Faster: Adaptive Event Conversion for Event-based Object Detection (Yansong Peng et al., AAAI 2023)** — `same_task_different_mechanism`。两者都尝试根据任务需求形成自适应 event windows；该工作学习 adaptive event conversion，SpikeSlicer 则用 SNN output spike time 决定 event-cell boundary。对应 Sections 2 and 4: slicing and hybrid interface。证据：Related Work 2, PDF p.3, citation and bibliography [13]。当前 active corpus 未覆盖。值得 backward search。
- **Asynchronous Spatio-Temporal Memory Network for Continuous Event-Based Object Detection (Jia Li et al., TIP 2022)** — `same_task_different_mechanism`。两者都面向连续 event stream 的 temporal grouping/processing；ASTMNet 使用 asynchronous spatio-temporal memory，SpikeSlicer 学习 task-dependent slicing boundary。对应 Sections 2 and 4: slicing and hybrid interface。证据：Related Work 2, PDF p.3, citation and bibliography [14]。当前 active corpus 未覆盖。值得 backward search。

## 8. Survey-Usable Takeaways

1. Event-based vision pipeline 不仅需要研究 representation，也需要研究 representation 之前的 temporal slicing。
2. 固定 duration 和固定 event count 都无法适应变化的运动速度与事件密度。
3. SpikeSlicer 将 SNN output spike time 直接解释为 event-group boundary。
4. SNN 输入是固定细粒度 voxel cells，最终 adaptive slice 由若干 cells 动态组合而成。
5. SPA-Loss 通过 no-reset membrane potential 控制目标 spike position。
6. Mem-Loss 负责目标时刻电位，LA-Loss 负责压低提前出现的 membrane hill。
7. ANN task loss 在当前切点邻域内选择局部最优 $n^*$，再作为 SNN 的 pseudo-label。
8. Feedback-Update 属于 alternating optimization，不是严格 end-to-end differentiable training。
9. 实际网络使用 IF，正文 LIF 推导主要是一般化表述。
10. 实验支持 adaptive slicing 在多个任务和 representation 上有效，但增益不是所有 tracker 上普遍成立。
11. Small 版本显示方法可以非常轻量，但论文没有明确将其作为所有实验的统一默认版本。
12. $0.32\%$ energy increase 是 operation-level theoretical estimate，不是实际硬件系统实测。
13. SPA-Loss 有实验效果，但其 Proposition、线性假设和 dynamic $\alpha$ 更接近 heuristic design，而不是严格的 spike-time control theory。

---

# Supplement Points

## Questions and Clarifications

### Q1. 原始 Mem-Loss 的意义是什么？为什么这样设计？

原始形式为：

$$
\mathcal L_{\mathrm{Mem}}
=
\left\|
U[n^*]
-
(1+\alpha)V_{\mathrm{th}}
\right\|_2^2.
$$

它把“希望在 $n^*$ 发放”转化为连续回归目标：

$$
U[n^*]
\rightarrow
(1+\alpha)V_{\mathrm{th}}.
$$

因为 spike condition 是：

$$
S[n^*]
=
\Theta
\left(
U[n^*]-V_{\mathrm{th}}
\right),
$$

只要 $U[n^*]\ge V_{\mathrm{th}}$ 就可以发放。作者引入 $\alpha\ge0$，让目标略高于阈值，形成 firing margin。

它不是执行：

$$
U[n]\leftarrow(1+\alpha)U[n],
$$

因此不是显式把所有时间步电压统一放大。但 $U[n^*]$ 由过去全部输入累积形成：

$$
U[n^*]
=
\beta^{n^*}U[0]
+
\gamma
\sum_{k=1}^{n^*}
\beta^{n^*-k}I[k].
$$

对 $U[n^*]$ 施加 loss 后，梯度会传播到此前所有输入和共享网络参数，因此整条膜电位轨迹都可能被改变。

### Q2. 为什么公式（6）会导致 premature spike？既然有问题，为什么还要提出？

设：

$$
V_{\mathrm{th}}=1,\qquad
\alpha=0.5,
$$

则目标为：

$$
U[n^*]=1.5.
$$

又设：

$$
\beta=0.8,\qquad
\gamma I[n^*]=0.4.
$$

由：

$$
U[n^*]
=
\beta U[n^*-1]+\gamma I[n^*],
$$

反推：

$$
U[n^*-1]
=
\frac{1.5-0.4}{0.8}
=
1.375.
$$

因为：

$$
1.375>V_{\mathrm{th}},
$$

神经元在 $n^*-1$ 就会提前发放。

所以问题不是 $n^*$ 没达到阈值，而是目标设得过高，迫使前一时刻也越过阈值。

公式（6）是作者最直接的初始设计：

$$
\text{希望 }n^*\text{ 发放}
\Rightarrow
\text{让 }U[n^*]\text{ 高于阈值}.
$$

随后作者发现这一目标不能无界抬高，才引出 Proposition 1 和公式（8）。因此公式（6）主要是用于暴露问题并引出最终 bounded target，而不是最终完整方案。

### Q3. Proposition 1 的上下界为什么这样设计？

为了在 $n^*$ 发放，需要：

$$
U[n^*]\ge V_{\mathrm{th}}.
$$

因此下界为：

$$
U_{\mathrm{lower}}=V_{\mathrm{th}}.
$$

为了避免 $n^*-1$ 提前发放，要求：

$$
U[n^*-1]\le V_{\mathrm{th}}.
$$

由递推式：

$$
U[n^*]
=
\beta U[n^*-1]
+
\gamma I[n^*],
$$

得到：

$$
U[n^*]
\le
\beta V_{\mathrm{th}}
+
\gamma I[n^*].
$$

所以理论 upper bound 为：

$$
\beta V_{\mathrm{th}}
+
\gamma I[n^*].
$$

直观含义是：假设前一时刻最多刚好位于阈值，再加上当前输入，就得到目标时刻允许的最高电位。

### Q4. Proposition 1 的结论严格成立吗？

不严格。

第一，论文为了避免 upper bound 低于 lower bound，写成：

$$
U_{\mathrm{upper}}
=
\max
\left(
\beta V_{\mathrm{th}}+\gamma I[n^*],
V_{\mathrm{th}}
\right).
$$

但若：

$$
\beta V_{\mathrm{th}}+\gamma I[n^*]
<
V_{\mathrm{th}},
$$

强行取 $V_{\mathrm{th}}$ 并不能保证前一时刻不发放。

例如：

$$
V_{\mathrm{th}}=1,\quad
\beta=0.5,\quad
\gamma I[n^*]=0.2.
$$

则：

$$
U[n^*]=1,
$$

反推：

$$
U[n^*-1]
=
\frac{1-0.2}{0.5}
=
1.6>1.
$$

第二，推导只约束 $n^*-1$，不能保证 $n^*-2$ 或更早时刻不存在 hill。

第三，论文使用 no-reset $U[n]$ 推导，却在证明中讨论 reset 后下降，混用了 $U[n]$ 与真实 reset state $V[n]$。

第四，是否在 $n^*+1$ 再次发放仍取决于 reset state 和 $I[n^*+1]$，不能由当前约束直接排除。

因此 Proposition 1 更适合理解为局部 target-range heuristic，而不是普遍成立的 spike-time theorem。

### Q5. 修改后的公式（8）是什么意思？

最终目标为：

$$
U_{\mathrm{target}}
=
(1-\alpha)U_{\mathrm{lower}}
+
\alpha U_{\mathrm{upper}},
\qquad
\alpha\in[0,1].
$$

这是上下界之间的线性插值。

若：

$$
\alpha=0,
$$

则：

$$
U_{\mathrm{target}}
=
U_{\mathrm{lower}}
=
V_{\mathrm{th}}.
$$

若：

$$
\alpha=1,
$$

则：

$$
U_{\mathrm{target}}
=
U_{\mathrm{upper}}.
$$

若：

$$
\alpha=0.5,
$$

则取上下界中点。

例如：

$$
U_{\mathrm{lower}}=1,\qquad
U_{\mathrm{upper}}=1.2,\qquad
\alpha=0.25,
$$

则：

$$
U_{\mathrm{target}}
=
0.75\times1
+
0.25\times1.2
=
1.05.
$$

相比公式（6）可能要求 $1.5$，公式（8）只在作者设定的局部区间内调整目标，是一种 bounded correction。

### Q6. LA-Loss 的线性假设从哪里来？凭什么使用？

作者假设目标 spike 之前的理想膜电位近似线性上升：

$$
U_{\mathrm{ref}}[n]
=
\frac{n}{n^*}V_{\mathrm{th}}.
$$

这不是从 IF/LIF dynamics 推导出来的。

真实递推是：

$$
U[n]
=
\beta U[n-1]+\gamma I[n],
$$

即使 $I[n]$ 恒定，轨迹也未必是直线；输入随事件内容变化时，膜电位更可能非单调。

作者采用线性形式，主要因为它简单满足：

$$
U_{\mathrm{ref}}[0]=0,
$$

$$
U_{\mathrm{ref}}[n^*]=V_{\mathrm{th}},
$$

并且对：

$$
0<n<n^*
$$

有：

$$
U_{\mathrm{ref}}[n]<V_{\mathrm{th}}.
$$

所以它是人为 regularizer，而不是神经动力学结论。

此外，LA-Loss 实际只监督当前错误 spike 位置 $n_c$：

$$
U[n_c]
\rightarrow
\frac{n_c}{n^*}V_{\mathrm{th}},
$$

没有显式约束：

$$
U[0]\le U[1]\le\cdots\le U[n^*].
$$

因此它只是压低当前 early hill，不能保证整条曲线真正线性或单调。

### Q7. $\alpha$ 只出现在 $n^*$ 的目标中，为什么会影响其他时间步？

因为 $U[n^*]$ 是递推累积量：

$$
U[n^*]
=
\beta^{n^*}U[0]
+
\gamma
\sum_{k=1}^{n^*}
\beta^{n^*-k}I[k].
$$

所以：

$$
\frac{\partial U[n^*]}{\partial I[k]}
=
\gamma\beta^{n^*-k}.
$$

对 $U[n^*]$ 计算 loss 时，梯度会传播到所有过去时间步的输入特征和共享参数。

而同一组 SNN 参数被每个时间步共享，因此更新后：

$$
U[1],U[2],\ldots,U[n^*]
$$

都可能改变。

从递推关系也可以直接看出：

$$
U[n^*-1]
=
\frac{
U[n^*]-\gamma I[n^*]
}{\beta}.
$$

在其他条件近似不变时，提高 $U[n^*]$ 也会使前一时刻电位上升。因此 $\alpha$ 虽然只显式控制目标时间的 target，却能间接改变整条 trajectory。

### Q8. Dynamic $\alpha$ 的更新到底是什么？

论文使用：

$$
\alpha
\leftarrow
\alpha
-
2\eta
\frac{1}{N_s}
\sum_i
(n_i^*-n_c^i).
$$

如果当前 spike 太早：

$$
n_c<n^*,
$$

则：

$$
n^*-n_c>0,
$$

因此：

$$
\alpha\downarrow.
$$

目标电位降低，spike 倾向后移。

如果当前 spike 太晚：

$$
n_c>n^*,
$$

则：

$$
n^*-n_c<0,
$$

因此：

$$
\alpha\uparrow.
$$

目标电位提高，spike 倾向提前。

但这不是严格 gradient descent。若定义：

$$
\mathcal L_\alpha
=
(n^*-n_c(\alpha))^2,
$$

严格求导应包含：

$$
\frac{\partial n_c}{\partial\alpha}.
$$

论文更新式没有这一项，而 $n_c$ 又是离散 threshold-crossing index。因此它更接近 heuristic signed-error controller。

论文也没有说明如何确保更新后的：

$$
\alpha\in[0,1].
$$

### Q9. 公式（6）是否就是在把整体电压放大？

不是显式统一乘法，但训练效果可能表现为整体抬高。

公式（6）不是：

$$
U[n]\leftarrow(1+\alpha)U[n],
$$

而是要求：

$$
U[n^*]\rightarrow(1+\alpha)V_{\mathrm{th}}.
$$

由于 $U[n^*]$ 依赖此前所有输入，且网络参数跨时间共享，优化这一目标常会同时抬高前面多个时间步的膜电位。因此“整体电压被抬高”的直觉基本正确，只是它是通过 shared-parameter learning 间接发生，而不是显式乘法。

公式（8）则不再使用无界的 $(1+\alpha)V_{\mathrm{th}}$，而是在上下界之间插值，因此缓解了这一问题，但不能完全消除前期 hill。

### Q10. Small 模型全面更好后，后续实验是否都使用 Small？

不能确认，而且答案不是“全部使用 Small”。

主 tracking 表同时报告 Base 与 Small。Small 在 DiMP、PrDiMP 和 TransT 的多数指标上更好，但在 TaMOs 上 Base 的部分指标更优。

PrDiMP 消融中 Small 确实：

- 参数量从 $45.11$ M 降至 $0.42$ M；
- 理论能耗从 $0.85$ mJ 降至 $0.69$ mJ；
- 所列 tracking metrics 全部更好。

但：

- recognition 表只写 `Ours`；
- representation、loss、event-cell-number 和部分扩展实验也未标明版本；
- efficiency 表额外能耗为 $0.85$ mJ，与 Base 完全一致。

因此最准确的结论是：Small 在部分主 tracking 和 PrDiMP 规模消融中更优，但论文没有将其明确设为所有后续实验的统一默认版本。

### Q11. Reset 与 no-reset 是否是两条数据流？有 reset 的电压只负责预测吗？

更准确地说，是两条共享输入与参数的膜电位状态轨迹，而不是两套独立数据流。

同一个输出 current：

$$
I_\theta[n]
$$

同时用于：

$$
V[n]
=
\beta V[n-1]+\gamma I_\theta[n],
$$

和：

$$
U[n]
=
\beta U[n-1]+\gamma I_\theta[n].
$$

区别是：

- $V[n]$ 达到阈值后 reset，负责真实输出 spike 与 slicing；
- $U[n]$ 不 reset，用于 Mem-Loss 和 LA-Loss。

论文没有给 $V[n]$ 单独定义一个最终可微 loss，因此主要直接梯度来自 $U[n]$ 分支：

$$
\mathcal L_{\mathrm{SPA}}
\rightarrow
U[n]
\rightarrow
I_\theta[n]
\rightarrow
\theta.
$$

但 $V[n]$ 不是完全不参与训练。它产生当前实际 spike index $n_c$，而 $n_c$ 会：

- 决定 neighborhood search 中心；
- 决定 LA-Loss 是否启用；
- 进入 dynamic $\alpha$ 更新；
- 决定实际重新切片的数据。

所以：

- $U[n]$ 是主要直接 loss-supervision state；
- $V[n]$ 是实际决策 state，并通过 $n_c$ 间接控制训练；
- 两者通过共享参数耦合。

论文没有公开足够代码级细节来确认是否所有层都同时维护 $V/U$，还是只在输出 neuron 维护 no-reset state。最合理理解是：至少输出神经元维护真实 reset trajectory 与辅助 no-reset trajectory。

---

## Additional Technical Details

### Theoretical Preconditions and Application Boundaries

#### 1. 固定细粒度 event-cell 离散假设

连续事件流先被离散为：

$$
C[0],C[1],\ldots,C[N-1].
$$

因此切点只能位于：

$$
t_0+n\delta t
$$

这些离散边界，而不能落在任意 raw-event timestamp。

理论边界：

- $\delta t$ 太大：切分精度不足；
- $\delta t$ 太小：SNN 时间步和计算开销增加。

所以它是细粒度 grid 上的 adaptive boundary selection，不是完全连续时间切分。

#### 2. 膜电位递推与跨时间参数共享假设

Mem-Loss 虽只直接监督 $U[n^*]$，但依赖：

$$
U[n^*]
=
\beta^{n^*}U[0]
+
\gamma
\sum_{k=1}^{n^*}
\beta^{n^*-k}I[k].
$$

作者隐含假设：通过共享参数更新，可以把整条 trajectory 朝目标 spike time 推动。

实际边界是：更新 $U[n^*]$ 可能同时改变所有前期时刻，甚至产生新的 hill，因此仅靠 endpoint regression 无法保证首次 threshold crossing。

#### 3. No-reset potential 可代理真实 reset neuron 的假设

训练监督使用 $U[n]$，真实 slicing 使用 $V[n]$。

作者假设连续的 no-reset trajectory 可以有效指导真实 reset neuron 的首次 spike time。

但一旦前面发生错误 spike：

$$
V[n]\neq U[n].
$$

二者偏离越大，基于 $U[n]$ 的局部理论保证越弱。因此 $U[n]$ 更适合作为 supervision proxy，而不是实际 spike trajectory 的严格等价物。

#### 4. Proposition 1 的局部相邻时刻假设

Upper bound 只由：

$$
U[n^*-1]\le V_{\mathrm{th}}
$$

推导。

它没有充分处理：

- $n^*-2$ 或更早的 hill；
- $n^*+1$ 的强输入；
- reset 后的真实状态；
- upper bound 低于 lower bound 的情况。

所以 Proposition 1 只能理解为降低局部提前发放风险的 heuristic range。

#### 5. 线性单调上升假设

LA-Loss 使用：

$$
U_{\mathrm{ref}}[n]
=
\frac{n}{n^*}V_{\mathrm{th}}.
$$

它不是 IF/LIF dynamics，也不是 event physical law，而是人为 regularization。

适用边界：

- 当错误主要表现为一个 early hill 时，它有明确作用；
- 当真实输入是间歇、强非单调或存在多个峰值时，只压低当前 $n_c$ 未必足够；
- 它没有显式约束整条轨迹单调。

#### 6. $\alpha$ 能控制整体发放早晚的假设

作者假设：

$$
\alpha\uparrow
\Rightarrow
\text{spike earlier},
$$

$$
\alpha\downarrow
\Rightarrow
\text{spike later}.
$$

这一关系依赖于参数更新使前期膜电位整体随 target height 同方向变化。

但 $\alpha$ 是共享控制量，不保证每条 event stream 都具有相同时间响应；更新式也是 signed-error heuristic，而非严格 gradient。

#### 7. Neighborhood search 包含合适切点的假设

作者只搜索：

$$
n_c-d,\ldots,n_c+d.
$$

得到的：

$$
n^*
=
\arg\min_i L_M(D_i)
$$

只是局部候选中的最优值。

若真实更优切点远离当前 $n_c$，局部搜索无法发现。训练早期 SNN 较差时，这一问题尤其明显。

#### 8. Tracking label 线性插值假设

为了给任意 candidate boundary 分配 bounding-box label，作者在两个原始标注时刻之间进行线性插值：

$$
l(t)
=
(1-\lambda)l_{t_1}
+
\lambda l_{t_2}.
$$

该假设对缓慢、近似匀速变化较合理，但对：

- acceleration；
- abrupt turning；
- deformation；
- rapid scale change；
- occlusion；

可能产生 pseudo-label error。

因此，tracking feedback 找到的是相对于 interpolation labels 的局部最优切点，不一定是真实连续轨迹下的最优边界。

#### 9. Reset / No-reset 双状态的应用边界

论文的训练逻辑依赖：

$$
U[n]\text{ 的 loss gradient}
\Rightarrow
\text{共享参数更新}
\Rightarrow
V[n]\text{ 的 spike time 改变}.
$$

这一机制成立的前提是：

- $V/U$ 使用相同的 $I_\theta[n]$；
- 两者共享同一网络参数；
- no-reset trajectory 对真实首次 spike time具有足够代理性。

论文没有完整公开计算图，因此无法确认：

- no-reset state 是否只存在于输出 neuron；
- 所有 hidden spiking layers 是否也维护双状态；
- 实际实现是否还有未在论文中写出的 surrogate spike loss。

这一部分属于实现级 `Needs further check`，也是方法复现时需要优先核对的内容。
