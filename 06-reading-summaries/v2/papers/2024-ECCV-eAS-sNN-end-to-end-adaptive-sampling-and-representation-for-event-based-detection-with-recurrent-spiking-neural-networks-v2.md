---
tags:
  - SNN
  - event-camera
  - object-detection
  - adaptive-sampling
  - recurrent-SNN
  - event-representation
---

# Summary V2｜EAS-SNN: End-to-End Adaptive Sampling and Representation for Event-based Detection with Recurrent Spiking Neural Networks

## 1. Core Understanding

EAS-SNN 面向 event-based object detection，将 recurrent convolutional SNN 从传统的 feature extractor 扩展为可学习的 temporal sampler：神经元通过膜电位积累事件信息，并以 spike firing time 定义局部采样边界，再将采样区间内的 potential accumulation 作为下游检测器的表示。它明确属于 SNN 方法，核心路线是 **SNN-based adaptive event sampling and representation learning**，同时结合 spike-based 或 hybrid YOLOX detector。

该方法并非直接逐事件处理原始微秒级事件流，而是先进行固定时间粒度的 event-count early aggregation，再由 ARSNN 学习更高层的局部采样区间。因此，本文的“端到端”主要指 early aggregation 之后的 sampling、aggregation 与 detection 联合优化。

## 2. Problem and Motivation

现有 event-based detector 通常先使用 fixed-duration、fixed-event-count 或 rule-based strategy 对事件流切片，再将事件聚合为 Event Count、Voxel Grid、Time Surface 等规则张量。虽然部分 aggregation module 已能与 detector 联合训练，但 sampling boundary 往往仍由人工规则、事件速率或外部搜索决定，难以直接利用下游检测语义。

固定切片无法同时适应不同位置的运动速度、事件密度和纹理状况：活动强的区域可能在长窗口内产生模糊和噪声，稀疏区域又可能在短窗口内缺少足够信息。SNN 的膜电位积分—阈值发放机制与“信息积累足够后结束一次采样”的需求具有结构对应关系，因此作者尝试让每个空间—极性神经元根据局部事件内容学习自己的 firing time。

但将 spike 赋予 sampling-boundary 语义后，普通 surrogate-gradient training 会出现新的退化：potential aggregation 的梯度未显式感知 firing threshold，且最后一次 spike 之后的 residual potential 可能让神经元在不发放的情况下仍向 detector 传递信息。SAT 和 RPD 即为解决这两个问题而设计。

## 3. Method Overview

原始事件表示为：

$$
e_i=(x_i,y_i,p_i,t_i).
$$

首先，历史事件窗口被划分成 $T_m$ 个较细的固定时间片，并用 event-count histogram 形成输入序列：

$$
f_1,f_2,\ldots,f_{T_m}.
$$

随后，ARSNN 在每个时间步接收 $f_t$。对于每个空间位置 $(x,y)$ 和 polarity $p$，其状态更新依赖当前事件输入、上一时间步 spike 和上一时刻 reset 后膜电位：

$$
I_t=W_I^f*f_t+W_I^s*s_{t-1}+b_I,
$$

$$
\gamma_t=\sigma\left(W_\gamma^f*f_t+W_\gamma^s*s_{t-1}+b_\gamma\right),
$$

$$
u_t=\gamma_t v_{t-1}+I_t.
$$

当 $u_t\geq\theta$ 时产生 spike，并以 hard reset 清除前一采样区间的状态。某神经元相邻两次 spike time $t^{k-1}$ 与 $t^k$ 之间构成第 $k$ 个局部采样区间，区间内的膜电位被聚合为 $\hat f_k(x,y,p)$。不同位置的第 $k$ 个局部结果被组合成全局 adaptive representation $\hat{\mathbf F}_k$，论文取前三个 adaptive representations 依次作为下游 detector 的三个时间步输入。输出为目标类别与 bounding boxes。

## 4. Key Components and Mechanisms

### 4.1 Recurrent Adaptive Sampling

普通 convolutional SNN 使用固定衰减系数 $\gamma$，输入电流仅来自当前 event-count map。RSNN 进一步加入 recurrent synaptic connections，使上一时间步 spike 同时影响当前输入电流和动态衰减系数 $\gamma_t$。因此，不同位置可以根据当前事件和 spike history 采用不同的记忆长度。

ARSNN 在 RSNN 基础上将 spike 解释为 sampling boundary。最短区间可以只覆盖一个 early-aggregation step，最长区间可以覆盖完整输入窗口。采样结果按神经元的第 $k$ 次发放顺序组织，而不是按统一绝对时间对齐，因此同一个 $\hat{\mathbf F}_k$ 中不同位置可能对应不同时间跨度。

### 4.2 Potential-based Aggregation and Hard Reset

ARSNN 不直接将二值 spike map 作为 detector 输入，而是对 spike-defined interval 内的 membrane potentials 进行聚合：

$$
\hat f_k(x,y,p)
=
\sum_{\tau=t^{k-1}+1}^{t^k}u_\tau(x,y,p).
$$

Spike 决定区间边界，potential accumulation 负责形成连续值 embedding。Sampler 使用 hard reset，使每次 spike 后的状态回到 $u_{\mathrm{reset}}$，避免前一采样区间的 residual potential 泄漏到下一采样区间；下游 spike-based detector 则使用 soft reset，以保留超过阈值的特征信息。

### 4.3 Spike-Aware Training

未使用 SAT 时，firing-time update 的近似只依赖 detection gradient 和发放时刻附近的膜电位变化：

$$
\Delta t^k
\propto
-
\frac{\partial\mathcal L}{\partial\hat f_k}
\left(u_{t^k}-u_{t^k-1}\right),
$$

其中没有显式的 threshold term。SAT 将发放时刻的 spike 乘入 aggregation：

$$
\hat f_k
=
s_{t^k}
\sum_{t'=t^{k-1}+1}^{t^k}u_{t'}.
$$

由于 $s_{t^k}=1$，forward value 不变；但 backward pass 多出经过 spike surrogate gradient 的路径，使梯度受到 $u_{t^k}-\theta$ 的调制。SAT 不是额外 loss，也不是直接更新连续 firing time，而是通过改变参数梯度，调整膜电位轨迹和离散 threshold-crossing timestep。

### 4.4 Residual Potential Dropout

最后一次 spike 之后的事件尚未形成完整 spike-defined interval。若仍将其 residual potential 送入 detector，神经元即使不发放也能传递信息，从而绕过 spike-timing learning。RPD 确定性删除最后一个未被 spike 闭合的 residual interval，迫使有效表示通过“积累—越阈值—发放—闭合区间”的路径产生。

SAT 强化 threshold-aware gradient，RPD 删除 non-firing shortcut。实验表明两者单独使用并不稳定，联合使用才使 adaptive sampling 超过 RSNN。

## 5. Experiments and Main Evidence

实验覆盖 N-Caltech 101、Gen1 和 1Mpx。Table 1 显示，recurrent connection 本身带来稳定收益：SNN 到 RSNN 的 mAP50 在 N-Caltech 101 和 Gen1 上分别提高 6.7 和 4.9 个百分点。Plain ARSNN 反而低于 RSNN，说明把 spike 用作 sampling boundary 会引入明显训练退化；SAT 或 RPD 单独使用也未稳定超过 RSNN。只有 ARSNN + SAT + RPD 达到最佳结果：N-Caltech 101 为 0.664 mAP50 / 0.437 mAP50:95，Gen1 为 0.731 / 0.409。

与固定表示比较时，完整 ARSNN 在两个数据集上均优于 Event Count、Voxel Grid、Time Surface 和 Voxel Cube。Gen1 上，小型 fully spiking EAS-SNN 在 3 个 detector timesteps 下取得 0.354 mAP50:95，高于 EMS-ResNet34 的 0.310，同时参数量为 8.92M，对方为 14.40M。最佳 Gen1 结果 0.409 则来自 spiking backbone + non-spiking FPN + non-spiking head 的 hybrid configuration，而不是 fully spiking detector。

在 1Mpx 上，EAS-SNN 报告 0.362 mAP50:95，并作为论文所称的首个 spike-based result，但仍低于强 ANN/RNN/Transformer detectors。Early-aggregation analysis 表明，$T_m$ 控制 sampler 内部时间粒度，而下游始终只接收前三个 adaptive representations；训练和测试粒度一致时通常最好，$T_m=8$ 的模型具有一定跨粒度鲁棒性。

能耗结果根据 MAC/AC operation count 和 32-bit 单操作能耗估算：Spiking YOLOX-M 和 YOLOX-S 分别获得约 $5.85\times$ 和 $3.73\times$ 的理论 arithmetic-energy advantage。该结果不是 neuromorphic hardware 上的端到端实测。模型报告 54.35 FPS，属于有竞争力但并非最快的检测速度。

## 6. Strengths and Limitations

**Strengths**

- 将 SNN 的 spike timing 明确用于 task-driven adaptive sampling，而不是仅作为后端 feature activation。
- 将局部采样、potential aggregation 与检测损失连接到统一训练图中。
- 通过 SAT 与 RPD 揭示并处理 spike 被赋予离散采样语义后出现的特殊优化退化。
- 在 representation-level ablation 和多个 detection benchmark 上提供较完整证据，并覆盖 fully spiking 与 hybrid configurations。

**Limitations / Questions**

- 方法仍依赖 fixed early aggregation，尚未实现 raw-event、microsecond-level、fully asynchronous sampling。
- Plain ARSNN 低于 RSNN，说明方法有效性高度依赖 SAT 与 RPD，而非自适应采样结构本身自然成立。
- 最佳总体精度来自 hybrid detector；fully spiking head 在 3 个 timestep 下明显损失性能。
- Gen1 和 1Mpx 上仍落后于强 dense recurrent 或 Transformer detectors，不能视为 event-based detection overall SOTA。
- 能耗优势是 operation-level estimation，未完整计入 memory access、data movement、state storage 和实际硬件利用率。
- 不同位置缺失第 $k$ 次 spike 时如何构造规则 tensor，以及超过三次 spike 后如何截断，正文未充分说明，`Needs further check`。

## 7. Relation to Other Papers and Survey Taxonomy

EAS-SNN 与传统 SNN detector 的区别在于：后者通常接收预先固定的 event representation，再用 SNN 提取特征；本文则让 SNN 直接参与 representation formation。它相对于 event-rate rule、Gromov–Wasserstein-based window search 和 pseudo-label-guided global triggering，进一步尝试让 detection loss 通过 surrogate gradient 直接影响 sampler。

在综述 taxonomy 中，它应主要归入：

- **Learnable event sampling**
- **SNN-based event representation**
- **Recurrent SNN temporal modeling**
- **Event-based object detection**
- **Hybrid ANN–SNN detection**
- **Low-timestep and energy-efficient SNNs**

它是讨论“从 fixed event slicing 转向 task-driven adaptive representation”的核心 SNN 案例，也适合用于说明：当 spike 承担 sampling、routing 或 boundary decision 等功能时，标准 surrogate-gradient training 可能需要专门的梯度和状态约束。

## 8. Survey-Usable Takeaways

- Takeaway 1: EAS-SNN 将 recurrent SNN 用作局部自适应事件采样器，以 spike firing time 定义采样边界，并用膜电位积累构造检测表示。
- Takeaway 2: Adaptive spike sampling 并非自动带来性能提升；plain ARSNN 低于 RSNN，只有 SAT 与 RPD 联合使用后才稳定改善检测结果。
- Takeaway 3: SAT 通过前向值不变的 gradient rewiring，使 detection loss 对 threshold crossing 更敏感；RPD 则删除不发 spike 仍可输出 residual potential 的旁路。
- Takeaway 4: 论文报告的最佳 Gen1 精度来自 hybrid spiking–non-spiking detector，fully spiking configuration 在有限 timestep 下仍存在明显精度损失。
- Takeaway 5: 该方法仍在固定 early-aggregation bins 上运行，因此它证明的是 coarse-to-adaptive sampling 的有效性，而非原始微秒事件上的完全异步端到端采样。

## Supplement Points：

### Questions and Clarifications

#### 1. 一阶 Euler 离散化如何得到 LIF 更新式？Soft reset 和 hard reset 如何计算？

连续 LIF 方程可写为：

$$
\tau_m\frac{dV(t)}{dt}=-V(t)+I(t).
$$

使用时间间隔 $\Delta t_s$ 的 forward Euler approximation：

$$
\frac{dV(t)}{dt}
\approx
\frac{u[t]-v[t-1]}{\Delta t_s},
$$

代入并整理可得：

$$
u[t]
=
\left(1-\frac{\Delta t_s}{\tau_m}\right)v[t-1]
+
\frac{\Delta t_s}{\tau_m}I[t].
$$

其中，$u[t]$ 是当前 threshold 判断前的膜电位，$v[t-1]$ 是上一时间步 reset 后的状态。完整计算顺序为：

$$
v[t-1]\rightarrow u[t]\rightarrow s[t]\rightarrow v[t].
$$

Spike 由：

$$
s[t]=\Theta(u[t]-\theta)
$$

决定。

Soft reset 为：

$$
v[t]=u[t]-\theta s[t].
$$

若 $s[t]=1$，只减去一个阈值，因此保留超阈值 residual potential；若 $s[t]=0$，则 $v[t]=u[t]$。

Hard reset 为：

$$
v[t]
=
u[t](1-s[t])
+
u_{\mathrm{reset}}s[t].
$$

若 $s[t]=1$，膜电位直接被设为 $u_{\mathrm{reset}}$，通常为 0。ARSNN sampler 使用 hard reset，因为每次 spike 表示一个采样区间结束，需要阻止前一区间状态泄漏；下游 SNN 使用 soft reset，以保留连续特征信息。

#### 2. 式（5）、式（6）和式（7）为什么形式不同？它们是什么关系？

式（5）是通用 LIF neuron dynamics，只说明输入电流如何积累、何时发放以及如何 reset，并未规定输入电流来自哪里。

式（6）将通用 LIF 用到 event sampling module 中：

$$
I_t=W_{\mathrm{conv}}*f_t+b,
$$

$$
u_t=\gamma v_{t-1}+I_t.
$$

其中 $f_t$ 是 early-aggregated event-count map。式（6）没有再次写出 spike generation 和 reset，但仍默认使用式（5）的：

$$
s_t=\Theta(u_t-\theta),
$$

以及 hard reset。PDF 中式（6）印为 $v_t$，但根据式（5）、式（7）和因果递推关系，合理形式应为 $v_{t-1}$，很可能是下标 typo。

式（7）不是从式（6）做普通代数推导，而是加入两项结构扩展。第一，上一时间步 spike 通过 recurrent convolution 参与当前输入电流：

$$
I_t=W_I^f*f_t+W_I^s*s_{t-1}+b_I.
$$

第二，固定衰减 $\gamma$ 被改成输入和 spike history 决定的动态 gate：

$$
\gamma_t
=
\sigma\left(
W_\gamma^f*f_t
+
W_\gamma^s*s_{t-1}
+
b_\gamma
\right).
$$

因此统一计算链为：

$$
f_t,s_{t-1}
\rightarrow
I_t,\gamma_t
\rightarrow
u_t
\rightarrow
s_t
\rightarrow
v_t.
$$

普通 LIF 已有 membrane-state recurrence，式（7）则额外加入显式 recurrent spike synapses。

#### 3. SAT 为什么被设计出来？它优化什么，目的是什么，又如何做到？

ARSNN 用 spike time 决定采样边界，但原始 representation 仅写成 membrane-potential sum：

$$
\hat f_k
=
\sum_{t'=t^{k-1}+1}^{t^k}u_{t'}.
$$

在这种形式下，detection loss 主要告诉 sampler 应如何改变 potential embedding，却没有显式感知：

$$
u_{t^k}-\theta.
$$

因此，它不能充分区分“刚刚越过阈值、容易提前或推迟的临界 spike”与“远高于阈值、较稳定的 spike”。SAT 的目标是让 detection gradient 对 threshold crossing 更敏感，从而通过改变网络参数和膜电位轨迹，间接改变 spike 出现在哪个离散 timestep。

SAT 将：

$$
\hat f_k=A_k
$$

改为：

$$
\hat f_k=s_{t^k}A_k,
\qquad
A_k=\sum_{t'}u_{t'}.
$$

因为 $t^k$ 是 firing time，所以 forward pass 中 $s_{t^k}=1$，输出数值完全不变。但反向传播时：

$$
\frac{\partial\hat f_k}{\partial u_{t^k}}
=
1+
A_k\frac{\partial s_{t^k}}{\partial u_{t^k}}.
$$

利用 surrogate gradient：

$$
\frac{\partial s_{t^k}}{\partial u_{t^k}}
\approx
h_\alpha(u_{t^k}-\theta),
$$

即可获得 threshold-aware gradient modulation。SAT 不是新的 loss，也不是直接把 $t^k$ 当成连续参数更新；它通过 gradient rewiring 更新卷积权重、recurrent weights 和 dynamic decay parameters，使 threshold-crossing timestep 发生变化。

SAT 单独仍不够，因为 residual potential 允许神经元在不发 spike 时输出信息。RPD 删除这一 non-firing shortcut，所以两者需要联合使用。

#### 4. Early aggregation 中“只使用前三个 slice”是什么意思？

这里存在两类不同的 slice。

第一类是固定 early-aggregation inputs：

$$
f_1,f_2,\ldots,f_{T_m}.
$$

它们由原始事件窗口按固定时间粒度划分，ARSNN 会完整处理全部 $T_m$ 个输入时间步。

第二类是 ARSNN 根据 spike order 产生的 adaptive representations：

$$
\hat{\mathbf F}_1,
\hat{\mathbf F}_2,
\hat{\mathbf F}_3,\ldots
$$

对于某个位置，第一次 spike 前的积累形成该位置的第一个 adaptive slice，第一次与第二次 spike 之间形成第二个，依此类推。所有位置的第 $k$ 个局部结果被组合成全局 $\hat{\mathbf F}_k$。由于不同位置 spike time 不同，同一个 $\hat{\mathbf F}_k$ 中不同像素可能覆盖不同的绝对时间范围和不同长度的 early bins。

论文所说的“前三个 slices”是：

$$
\hat{\mathbf F}_1,\hat{\mathbf F}_2,\hat{\mathbf F}_3,
$$

而不是：

$$
f_1,f_2,f_3.
$$

ARSNN 先在全部 $T_m$ 个细粒度输入上演化，再将前三个 spike-defined adaptive representations 依次送入下游 backbone，构成 Table 3 中报告的 3 detector timesteps。$T_m$ 控制 sampler 内部时间分辨率，3 控制 downstream detector 的展开长度，两者不能混为一谈。
