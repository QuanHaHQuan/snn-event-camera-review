---
tags: [event-camera, state-space-model, continuous-time-model, object-detection, transformer, non-SNN-baseline]
---

# Summary V2｜State Space Models for Event Cameras

## 1. Core Understanding

本文研究 event-camera object detection 中的两个问题：其一，传统 recurrent detector 在时间维度上需要顺序计算，训练效率较低；其二，模型通常在固定长度的 event window 上训练，当测试时缩短窗口、提高 inference frequency，检测性能会显著下降。作者将 continuous-time State Space Model（SSM）嵌入四阶段 Vision Transformer backbone，以 S4、S4D 或 S5 替代传统 RNN/LSTM temporal aggregation，并提出 frequency-selective output masking 与 H2 regularization 抑制训练时间网格中的高频混叠。

整体流程为：

```
Raw asynchronous events
→ 固定时间窗口内构造 dense tensor representation
→ 4-stage SSM-ViT backbone
→ Block-SA / Grid-SA 建模空间关系
→ S4D 或 S5 保存跨窗口 temporal state
→ YOLOX detection head
```

本文不是 SNN，也没有逐 event 异步更新神经元。它仍将 events 聚合成 dense tensors，其主要价值是提供一种 non-spiking、stateful、continuous-time temporal baseline。

## 2. Problem and Motivation

现有 dense event detectors 通常把一个固定时间窗口内的 events 转换成多通道图像式表示。训练时若每个输入覆盖 50 ms，则模型每秒处理 20 个 representations，即 20 Hz。测试时若将窗口缩短到 25、12.5、10 或 5 ms，则 inference frequency 分别提高到 40、80、100 和 200 Hz。更短窗口带来的不仅是时间步变化，还包括 event 数减少、目标轮廓不完整和输入统计分布变化。

慢速或暂时静止的物体可能在当前窗口中几乎不产生 events，因此模型需要 recurrent memory 利用此前窗口的信息。RNN/LSTM 能提供这种记忆，但其状态依赖造成时间维度上的顺序训练。作者希望同时获得：
$$
\text{parallel sequence training}
+
\text{stateful streaming inference}.
$$
Continuous-time SSM 的优势在于，它先定义连续时间动态，再根据实际 step size 离散化；时间窗口改变后，可以相应调整离散时间尺度，而不必为每一种 inference frequency 重新训练整套网络。

## 3. Method Overview

连续时间线性 SSM 定义为：
$$
\frac{d\mathbf{x}(t)}{dt}
=
A\mathbf{x}(t)+B\mathbf{u}(t),
$$
其中 $\mathbf{u}(t)$ 是当前输入，$\mathbf{x}(t)$ 是保存历史信息的 latent state，$\mathbf{y}(t)$ 是输出。给定离散步长 $\Delta$，系统可转换为：
$$
\mathbf{x}_k
=
\bar A\mathbf{x}_{k-1}
+
\bar B\mathbf{u}_k,
$$
离散参数由连续参数、$\Delta$ 和 Euler、bilinear 或 ZOH 等离散化方法共同决定。

SSM-ViT 采用四阶段 hierarchical backbone。每个 stage 的结构为：

```
Convolution
→ Block-SA
→ MLP
→ Grid-SA
→ MLP
→ SSM
```

Block-SA 在连续局部窗口内执行 self-attention；Grid-SA 将分散在不同局部窗口中的位置组成稀疏网格，以扩大空间 receptive field。最后，SSM 在相同 stage 的相邻 event windows 之间传递 temporal state。当前时间步的特征沿 Stage 1 至 Stage 4 向深层传播，而每个 stage 又分别沿时间方向保存自己的状态。论文未明确给出每个 stage 的 SSM state tensor 精确形状。

## 4. Key Components and Mechanisms

### S4、S4D 与 S5

三者需要从“状态矩阵结构”和“多通道组织方式”两个维度区分：
$$
\boxed{
\text{S4}
=
\text{多个独立 SISO SSMs}
+
\text{DPLR state dynamics}
}
$$
S4 通常让每个 feature channel 对应一套独立的 single-input single-output SSM。单个 SSM 内部的 $A$ 采用 diagonal-plus-low-rank structure，使多个 state dimensions 之间保留结构化耦合，并能高效构造长 temporal convolution kernel。
$$
\boxed{
\text{S4D}
=
\text{多个独立 SISO SSMs}
+
\text{diagonal }A
}
$$
S4D 保留 S4 的多 SISO 组织，但删除 low-rank correction。每个 diagonal state 独立演化，计算和频率分析更简单，但对初始化更敏感。
$$
\boxed{
\text{S5}
=
\text{一个共享 MIMO SSM}
+
\text{diagonalized dynamics}
+
\text{parallel scan}
}
$$
S5 将多个输入 channels 通过 $B$ 写入一组共享 states，再通过 $C$ 生成多个输出 channels；训练时以 associative parallel scan 并行求解 recurrence。

### 训练形式与推理形式

S4/S4D 的 recurrence 可以展开成 causal convolution。定义：
$$
K_i=C\bar A^{i}\bar B,
$$
则：
$$
\mathbf{y}_k
=
\sum_{i=0}^{k}
K_i\mathbf{u}_{k-i}
+
D\mathbf{u}_k.
$$
训练时完整 sequence 已知，可以利用 convolution 并行计算所有时间位置；在线推理时未来输入未知，只需保存上一 state 并递归更新。S5 不主要依赖 FFT convolution，而是利用满足结合律的 parallel scan 处理完整序列；推理阶段同样转为逐步 state update。

### Anti-aliasing

低频训练时，某些超过训练 Nyquist frequency 的 continuous temporal modes，可能在训练采样点上伪装成低频 modes。提高 inference frequency 后采样点变密，二者表现不再相同，导致模型行为发生变化。作者因此提出：

1. **Output masking**：根据 diagonal mode 的 normalized frequency，将过高频率 mode 对应的 $C_n$ 置零。
2. **H2 regularization**：在 loss 中惩罚指定 cutoff 以上的整体 frequency-response energy。

Output masking 是 hard removal；H2 norm 是 soft suppression。

## 5. Experiments and Main Evidence

模型使用 Gen1 和 1 Mpx datasets。训练输入由 50 ms event windows 构成，对应 20 Hz，每个 representation 划分为 $T=10$ temporal bins。Gen1 使用 batch size 8、sequence length 21；1 Mpx 使用 batch size 12、sequence length 10。训练共 400k iterations，使用 Adam、OneCycle schedule，并采用一半 BPTT、一半 TBPTT 的 mixed batching。

在标准 20 Hz 下：

- S4D-ViT-B：Gen1 46.2 mAP，1 Mpx 46.8 mAP；
- S5-ViT-B：Gen1 47.4 mAP，1 Mpx 47.2 mAP；
- RVT-B：47.2 / 47.4；
- GET-T：47.9 / 48.4。

因此，SSM-ViT 在标准频率下具有竞争力，但不是全面 SOTA。S5-ViT-B 的表格参数量为 18.2M，正文出现的 17.5M 与表格不一致。

跨频率测试中，模型仅在 20 Hz 训练，再于 40、80、100、200 Hz 测试。S5 在 Gen1 上的平均下降为 3.94 mAP，在 1 Mpx 上为 2.68 mAP，二者平均得到 3.31 mAP；RVT 和 GET 分别下降 21.25 和 24.53 mAP。3.31 并非 20 Hz 到 200 Hz 的终点差值：S5 在 200 Hz 时实际仍下降约 7.5 mAP。

初始化消融显示，legS 整体优于 inv 和 lin；S5-legS 在 $\alpha=0.5$ 时达到 48.48 mAP，为 Table 3 最佳结果。Stage 消融显示，仅保留 Stage 4 的 temporal state 已带来明显提升；加入 Stage 3 和 Stage 2 后继续改善，而为 S5 加入 Stage 1 仅再提高约 0.07 mAP，说明主要收益来自高层 temporal memory。

## 6. Strengths and Limitations

**优势：**

- 将 S4/S4D/S5 系统性用于高维 event-camera detection；
- 同时处理 temporal-state training efficiency 与 inference-frequency generalization；
- 提供 20–200 Hz 的明确跨频率评估协议；
- 比较 hard output masking 与 soft H2 regularization；
- S5 在标准精度、reported runtime 和频率鲁棒性之间取得较好平衡。

**局限：**

- 输入仍是 dense event representation，不保留 raw-event-level asynchronous sparsity；
- 不是 SNN，也没有 neuromorphic hardware energy evidence；
- 提高 inference frequency 意味着每秒执行更多次完整网络，并非无计算代价；
- Runtime 来自不同但“可比”的 GPU，不是所有模型在同一环境下重新测量；
- 论文声称训练最高快 33%，但主文缺少完整 training-time table 和 profiling；
- DSEC 仅提供 qualitative visualization；
- Event-trigger Equation 1 只显式写出 positive threshold，未完整表达 negative polarity；
- $\alpha$ 的文字描述与公式相反：根据公式，较小 $\alpha$ 才会屏蔽更多高频 modes；
- Table 3 中 $\alpha=0$ 应视为关闭 masking 的特殊 baseline，而非字面零 cutoff；
- 论文对 timescale rate 符号的定义不够清楚。

## 7. Relation to Other Papers and Survey Taxonomy

本文应归入：

- continuous-time temporal modeling；
- non-spiking stateful architecture；
- recurrent alternatives；
- inference-frequency generalization；
- dense event representation；
- event-based object detection。

与 SFOD 相比，二者都保存 temporal state，但 SFOD 使用 membrane potential、threshold 和 spikes，本文使用连续 latent state，没有 spike firing。与 EV-ACT、TTPOINT 和 VMST-Net 相比，后者主要关注 representation、spatial modeling 或轻量化，本文重点解决跨窗口 temporal memory 与 frequency shift。与 RVT/GET 的关系最直接：空间 backbone 均依赖 dense representation 和 attention，但本文用 continuous-time SSM 替代 conventional recurrent module。

对 SNN survey 的核心启示是：

> Temporal state、streaming inference 和连续时间适应性并非 SNN 独有属性。评估 SNN 时，应与 SSM 这类可并行训练、可递归部署的 non-spiking stateful models 比较，而不应只与无状态 CNN 比较。

## 8. Survey-Usable Takeaways

1. 固定 event-window training 会造成明显的 inference-frequency distribution shift。
2. Continuous-time SSM 可通过重新离散化或缩放有效 step size，增强跨频率适应性。
3. SSM 能同时提供 parallel sequence training 与 recurrent streaming inference。
4. Cross-frequency robustness 应成为 event-camera model 的独立评价维度。
5. S5 的共享 MIMO state 与 parallel scan 在本文中优于 S4D 的多 SISO diagonal organization。
6. Bandlimiting 的作用不是处理“高频推理新产生的混叠”，而是排除低频训练时不可辨识的隐藏高频 kernels。
7. Dense SSM 在 GPU 上效率较好，但不等价于 spike-driven sparsity 或 neuromorphic energy advantage。
8. 对 SNN 与 SSM 的公平比较应同时考虑 accuracy、频率鲁棒性、stateful streaming、训练效率、输入稀疏性和真实硬件能耗。

## Supplement Points

### A. SSM 的状态、通道与真实张量维度

连续时间 SSM 写为：

$$
\frac{d\mathbf{x}(t)}{dt}
=
A\mathbf{x}(t)+B\mathbf{u}(t),
$$

$$
\mathbf{y}(t)
=
C_{\mathrm{read}}\mathbf{x}(t)+D\mathbf{u}(t).
$$

为避免符号混淆，本文统一使用：

- $\mathbb{R}$：实数集合；
- $\mathbb{C}$：复数集合；
- $F$：输入 feature channels；
- $P$：内部 state dimension；
- $M$：输出 feature channels；
- $C_{\mathrm{read}}$：从 state 读取输出的矩阵。

在一个确定的时间、样本和空间位置上：

$$
\mathbf{u}_t\in\mathbb{R}^{F},
\qquad
\mathbf{x}_t\in\mathbb{C}^{P},
\qquad
\mathbf{y}_t\in\mathbb{R}^{M}.
$$

参数维度为：

$$
A\in\mathbb{C}^{P\times P},
\qquad
B\in\mathbb{C}^{P\times F},
$$

$$
C_{\mathrm{read}}\in\mathbb{C}^{M\times P},
\qquad
D\in\mathbb{R}^{M\times F}.
$$

它们分别表示：

- $A$：旧 state 如何随时间演化；
- $B$：当前 $F$ 个 feature channels 如何写入 $P$ 维 state；
- $C_{\mathrm{read}}$：如何将 $P$ 维 state 读成 $M$ 维输出；
- $D$：当前输入绕过 state 直接影响输出的 skip path。

需要区分 **feature channel** 与 **state dimension**：

- feature channel 是当前时间步可见的输入特征；
- state dimension 是 SSM 内部用于压缩历史的潜在记忆变量。

单个 state coordinate：

$$
x_{t,p}
$$

确实是一个标量，但每个空间位置拥有一个完整的 $P$ 维 state vector。

在本文的视觉网络中，某一 stage 的输入原本为：

$$
U\in\mathbb{R}^{T\times B\times F\times H\times W}.
$$

它被重排为：

$$
U_{\mathrm{SSM}}
\in
\mathbb{R}^{(BHW)\times T\times F},
$$

即每个空间位置被视为一条独立的时间序列。当前时刻的全部状态可写为：

$$
X_t^{\mathrm{state}}
\in
\mathbb{C}^{B\times P\times H\times W}.
$$

因此，不是整张图只有一个 $P$ 维 state，而是每个空间位置都有自己的 $P$ 维 temporal memory，所有位置共享同一组 SSM 参数。

---

### B. S4、S4D 与 S5：结构和计算方式

设输入为：

$$
U\in\mathbb{R}^{Q\times T\times F},
$$

其中 $Q$ 表示独立序列数；在本文中通常有：

$$
Q=BHW.
$$

#### S4 与 S4D：多个 SISO SSM

S4 和 S4D 都为每个 feature channel 建立一个独立的 SISO SSM。第 $f$ 个 channel 在每个时刻只有一个标量输入：

$$
u_t^{(f)}\in\mathbb{R},
$$

但其内部拥有一个 $N$ 维状态：

$$
\mathbf{x}_t^{(f)}\in\mathbb{C}^{N}.
$$

因此当前全部状态为：

$$
X_t\in\mathbb{C}^{Q\times F\times N}.
$$

一个标量 channel 之所以需要 $N$ 个 states，是因为同一输入特征可能同时需要：

- 快速衰减的短期记忆；
- 缓慢衰减的长期记忆；
- 对不同时间频率敏感的动态模式。

S4 与 S4D 的主要区别在状态矩阵 $A$：

$$
\text{S4:}\qquad
A=\Lambda-PQ^{*},
$$

即 diagonal plus low-rank，允许同一 SISO 内部的 state modes 受控耦合。

$$
\text{S4D:}\qquad
A=\Lambda,
$$

即完全 diagonal，不同 state modes 在 $A$ 中独立演化。S4D 实现更简单，但性能较依赖 eigenvalue initialization。

#### S5：一个共享 MIMO SSM

S5 不再逐 channel 建立独立 SSM，而是在每个时间步一次接收完整 feature vector：

$$
\mathbf{u}_t\in\mathbb{R}^{F},
$$

维护一个共享状态：

$$
\mathbf{x}_t\in\mathbb{C}^{P}.
$$

其计算为：

$$
\mathbf{x}_t
=
\overline{\Lambda}\odot\mathbf{x}_{t-1}
+
\overline{B}\mathbf{u}_t,
$$

$$
\mathbf{y}_t
=
\operatorname{Re}
\left(
C_{\mathrm{read}}\mathbf{x}_t
\right)
+
\mathbf{d}\odot\mathbf{u}_t.
$$

其中：

$$
\overline B\in\mathbb{C}^{P\times F},
\qquad
C_{\mathrm{read}}\in\mathbb{C}^{F\times P}.
$$

因此多个 input channels 在写入 state 时已经发生融合，多个 output channels 也共同读取同一组 state modes。

| 项目                      | S4                     | S4D                    | S5                             |
| ------------------------- | ---------------------- | ---------------------- | ------------------------------ |
| 基本结构                  | $F$ 个 SISO            | $F$ 个 SISO            | 1 个 MIMO                      |
| 单步输入                  | 每个 SSM 接收 1 个标量 | 每个 SSM 接收 1 个标量 | 一次接收 $F$ 维向量            |
| 当前状态                  | $Q\times F\times N$    | $Q\times F\times N$    | $Q\times P$                    |
| $A$ 的结构                | DPLR                   | Diagonal               | Diagonalized                   |
| channel 是否在 SSM 内混合 | 否                     | 否                     | 是，通过 $B,C_{\mathrm{read}}$ |
| 离线训练                  | Kernel + convolution   | Kernel + convolution   | Parallel scan                  |
| 在线推理                  | Recurrence             | Recurrence             | Recurrence                     |

S4/S4D 训练时可将 recurrence 展开为 temporal convolution：

$$
K_i
=
C_{\mathrm{read}}
\overline A^i
\overline B,
$$

$$
\mathbf{y}=K*\mathbf{u}.
$$

在线推理时则只保存当前 state。S5 不显式构造卷积核，而利用 recurrence 组合满足结合律这一性质，通过 parallel scan 并行计算所有时间前缀状态。

Parallel scan 只决定 forward sequence 如何并行计算；BPTT/TBPTT 决定 backward gradient 能传播多远，二者不是同一个概念。

---

### C. 连续时间 SSM、离散化与 learned step size $\Delta$

连续时间参数 $A,B$ 描述系统每单位内部时间如何演化，但神经网络实际接收的是离散时间序列，因此必须根据 step size $\Delta$ 进行离散化。

本文最重要的是 Zero-Order Hold：

$$
\overline A(\Delta)
=
e^{\Delta A},
$$

$$
\overline B(\Delta)
=
\int_0^\Delta
e^{(\Delta-\tau)A}B\,d\tau.
$$

当 $A$ 可逆时：

$$
\overline B(\Delta)
=
A^{-1}
\left(
e^{\Delta A}-I
\right)B.
$$

离散 recurrence 为：

$$
\mathbf{x}_{k+1}
=
\overline A(\Delta)\mathbf{x}_k
+
\overline B(\Delta)\mathbf{u}_k.
$$

$\Delta$ 不会增加新的张量维度，它决定一次网络更新相当于连续系统向前演化多长时间。真正决定离散动态的是：

$$
\Delta A.
$$

现代 SSM 通常学习一个正的内部 timescale：

$$
\Delta_{\mathrm{learned}}
=
e^{\theta_\Delta}
$$

或：

$$
\Delta_{\mathrm{learned}}
=
\operatorname{softplus}(\theta_\Delta).
$$

Detection loss 通过：

$$
\overline A=e^{\Delta A},
\qquad
\overline B=\overline B(\Delta)
$$

反向传播到 $\theta_\Delta$，从而学习适合任务的 memory timescale。

需要区分：

- $\delta_{\mathrm{physical}}$：真实 event aggregation window，例如 50 ms；
- $\Delta_{\mathrm{learned}}$：模型内部 timescale，不应简单等同于 50 ms；
- $\Delta_{\mathrm{eff}}$：当前推理频率下实际用于离散化的 step。

本文在 20 Hz 训练，对应 50 ms event windows。测试频率提高时，应按物理窗口比例缩小有效 $\Delta$：

$$
\Delta_{\mathrm{test}}
=
\frac{f_{\mathrm{train}}}
{f_{\mathrm{test}}}
\Delta_{\mathrm{train}}.
$$

例如：

| Inference frequency | Event window | 有效 step scaling |
| ------------------: | -----------: | ----------------: |
|               20 Hz |        50 ms |       $1.0\Delta$ |
|               40 Hz |        25 ms |       $0.5\Delta$ |
|               80 Hz |      12.5 ms |      $0.25\Delta$ |
|              100 Hz |        10 ms |       $0.2\Delta$ |
|              200 Hz |         5 ms |       $0.1\Delta$ |

这能校正 state dynamics 的时间尺度，但不能完全消除短窗口带来的输入分布变化：窗口越短，每个 representation 中的 events 越少，目标轮廓也可能越不完整。

论文明确说明训练时每个 50 ms representation 包含 10 个内部 bins；高频测试时是否仍固定 10 bins、仅缩短每个 bin 的物理跨度，正文未明确说明，仍为 `Needs further check`。

---

### D. Complex modes：衰减、旋转与 `.real`

SSM 不必须使用复数。复数只是将一个二维实数衰减—旋转系统紧凑表示为一个 complex scalar。

令一个连续 mode 为：

$$
\lambda=a+ib.
$$

其响应为：

$$
z(t)=e^{\lambda t}z(0)
=
e^{at}
\left[
\cos(bt)+i\sin(bt)
\right]
z(0).
$$

因此：

- $a=\operatorname{Re}(\lambda)$：控制衰减或增长；
- $b=\operatorname{Im}(\lambda)$：控制旋转速度，即 angular frequency。

离散化后：

$$
\overline\lambda
=
e^{\Delta\lambda}
=
e^{a\Delta}
\left[
\cos(b\Delta)+i\sin(b\Delta)
\right].
$$

每个时间步：

- 幅度乘以 $e^{a\Delta}$；
- 相位旋转 $b\Delta$。

Complex mode 并不意味着 event data 必须周期性。它只是为 temporal kernel 提供一组带衰减的正弦、余弦动态基础，可以表达：

- 快慢不同的变化；
- 正负交替；
- 相位关系；
- 延迟峰值；
- 局部振荡。

代码中的：

```python
y = (C_read @ x + D * u).real
```

表示最终取：

$$
\operatorname{Re}
\left(
C_{\mathrm{read}}\mathbf{x}
+
D\mathbf{u}
\right).
$$

这不是说虚部没有作用。虚部已经参与内部状态的旋转和相位演化；取实部只是将 complex parameterization 映射回后续 CNN、Transformer 和 detection head 所需的实值 feature。

---

### E. Nyquist、aliasing 与 $\alpha$

若 sampling frequency 为：

$$
f_s,
$$

则采样间隔为：

$$
\Delta=\frac{1}{f_s}.
$$

一个连续 cosine：

$$
x(t)=\cos(2\pi ft)
$$

在采样时刻：

$$
t_k=\frac{k}{f_s}
$$

上变成：

$$
x[k]
=
\cos
\left(
2\pi\frac{f}{f_s}k
\right).
$$

Normalized frequency 为：

$$
\nu=\frac{f}{f_s}
=
\frac{\Delta|\operatorname{Im}(\lambda)|}{2\pi}.
$$

Nyquist limit 为：

$$
f_{\mathrm{Nyquist}}
=
\frac{f_s}{2},
\qquad
\nu_{\mathrm{Nyquist}}=0.5.
$$

Aliasing 的本质是：不同 continuous frequencies 在当前采样网格上产生完全相同的离散 samples。

例如：

$$
f_s=20\text{ Hz}.
$$

比较 6 Hz 和 14 Hz：

$$
x_6[k]
=
\cos
\left(
2\pi\frac{6}{20}k
\right),
$$

$$
x_{14}[k]
=
\cos
\left(
2\pi\frac{14}{20}k
\right).
$$

因为：

$$
\frac{14}{20}
=
1-\frac{6}{20},
$$

所以：

$$
\cos
\left(
2\pi\frac{14}{20}k
\right)
=
\cos
\left(
2\pi k-
2\pi\frac{6}{20}k
\right)
=
x_6[k].
$$

因此，在 20 Hz 训练网格上：

$$
x_6[k]=x_{14}[k].
$$

若训练 loss 只比较这些离散点，则模型内部使用 6 Hz 或 14 Hz mode 时，可能得到相同 loss：

$$
\mathcal L(6)=\mathcal L(14).
$$

这不是损失函数“能力不足”，而是训练数据没有提供区分两种连续动态的证据，即 continuous frequency 不可辨识。

提高到 40 Hz 后，新增中间采样点。例如在：

$$
t=0.025\text{ s},
$$

有：

$$
\cos(2\pi\cdot6\cdot0.025)\approx0.588,
$$

$$
\cos(2\pi\cdot14\cdot0.025)\approx-0.588.
$$

二者开始不同。因而：

> 提高 inference frequency 不会制造 aliasing，而是会暴露低频训练阶段被 aliasing 掩盖的高频 internal modes。

论文使用 $\alpha$ 控制允许保留的 normalized-frequency 范围：

$$
\nu_n
\leq
\frac{\alpha}{2}.
$$

| $\alpha$ | 最大 normalized frequency | 20 Hz 下对应 physical cutoff |
| -------: | ------------------------: | ---------------------------: |
|      1.0 |                       0.5 |                        10 Hz |
|      0.5 |                      0.25 |                         5 Hz |
|     0.25 |                     0.125 |                       2.5 Hz |

因此：

$$
\boxed{
\alpha\text{ 越小，频率限制越严格}
}
$$

论文中若称“更大 $\alpha$ 会丢弃更多高频 modes”，则与其公式方向相反。实验表中的 $\alpha=0$ 应理解为关闭 masking，而不是字面上的零频率 cutoff。

---

### F. Output Masking 与 $H_2$ Regularization

两种方法都用于抑制训练采样网格无法可靠辨认的高频动态，但策略不同。

#### Output Masking：硬截断

对于 diagonal SSM，其 impulse-response kernel 可写为：

$$
K(t)
=
C_{\mathrm{read}}e^{tA}B
=
\sum_{n=1}^{P}
C_{\mathrm{read},:,n}
e^{\lambda_nt}
B_{n,:}.
$$

第 $n$ 个 mode 是否影响输出，由：

$$
C_{\mathrm{read},:,n}
$$

决定。若该 mode 超出频率 cutoff，则令：

$$
\widetilde C_{\mathrm{read},:,n}
=
0.
$$

即：

$$
\widetilde C_{\mathrm{read},:,n}
=
\begin{cases}
C_{\mathrm{read},:,n},
&
\nu_n\leq\frac{\alpha}{2},
\\[4pt]
0,
&
\nu_n>\frac{\alpha}{2}.
\end{cases}
$$

该 state mode 仍可在内部演化，但不再影响模型输出。因此 Output Masking 是 hard cutoff：

> 判断一个 mode 是否有资格进入输出。

#### $H_2$ Regularization：软性高频抑制

连续 SSM 的动态 transfer function 为：

$$
G(j\omega)
=
C_{\mathrm{read}}
(j\omega I-A)^{-1}B.
$$

它描述输入中 angular frequency 为 $\omega$ 的成分，经过 SSM 后会被放大或衰减到什么程度。

论文惩罚 cutoff 以上的高频响应能量：

$$
\left\|
G
\right\|_{
H_2(\omega_{\min},\infty)
}^2
=
\frac{1}{\pi}
\int_{\omega_{\min}}^\infty
\left\|
G(j\omega)
\right\|_F^2
\,d\omega.
$$

训练 loss 为：

$$
\mathcal L_{\mathrm{total}}
=
\mathcal L_{\mathrm{det}}
+
\lambda_{H_2}
\mathcal L_{H_2}.
$$

实际通过有限频率区间和离散采样点进行 numerical integration。

这一正则项可以推动模型：

- 减小高频 mode 的 $C_{\mathrm{read}}$；
- 减小其输入写入权重 $B$；
- 增大 damping，使 $\operatorname{Re}(\lambda)$ 更负；
- 移动 mode 的中心频率。

它不会立即删除整个 mode，而是使系统在高频区的整体响应逐渐变弱。

| 对比项    | Output Masking                                  | $H_2$ Regularization               |
| --------- | ----------------------------------------------- | ---------------------------------- |
| 类型      | Hard constraint                                 | Soft constraint                    |
| 作用对象  | 单个 mode                                       | 整体 frequency response            |
| 主要操作  | 超过 cutoff 时令对应 $C_{\mathrm{read}}$ 列为 0 | 在 loss 中惩罚高频响应能量         |
| 高频 mode | 内部可存在，但不能输出                          | 可以保留，但代价更高               |
| 推理阶段  | 继续应用 mask                                   | 不再计算正则项                     |
| 优点      | 简单、明确、频率边界清晰                        | 平滑、灵活，可保留部分有用高频信息 |
| 风险      | 可能硬性删除有用 mode                           | 正则过弱时高频响应仍可能过强       |

最简洁的理解是：

> Output Masking 决定“这个 mode 能不能说话”；  
> $H_2$ regularization 决定“整个系统在高频区域说得有多响”。

---

### G. 本文其他实现细节

**Block-SA 与 Grid-SA。**  
Block Self-Attention 在连续局部窗口内建模相邻空间关系；Grid Self-Attention 将不同局部窗口中相同相对位置的 tokens 分组，从而建立稀疏的长距离空间联系。两者组合负责单个时间窗口内的 spatial modeling，S5 则负责同一空间位置跨 event windows 的 temporal memory。

**BPTT 与 TBPTT。**  
Full BPTT 允许后期 loss 沿 state dependency 反向传播到完整序列早期，但显存开销大。TBPTT 在 chunk 边界继续传递 state 数值，同时执行：

$$
\operatorname{stopgrad}(\mathbf{x}),
$$

使后续 loss 不再更新更早 chunk。本文在同一 batch 中混合使用 BPTT 和 TBPTT，以平衡长期 temporal credit assignment 与训练成本；正文未给出具体 truncation length。

**跨频率实验的正确解释。**  
模型在 20 Hz 训练，在 40–200 Hz 下不重新训练，通过缩放有效 $\Delta$ 重新离散化。该机制解决 state dynamics 的时间尺度失配；bandlimiting 与 $H_2$ regularization 则解决低频训练网格对高频 continuous modes 的不可辨识问题。二者针对的是不同问题，缺一不可。

