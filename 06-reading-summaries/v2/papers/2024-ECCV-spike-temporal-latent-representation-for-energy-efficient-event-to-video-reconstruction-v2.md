---
tags:
  - event-camera
  - event-to-video-reconstruction
  - spiking-neural-network
  - sparse-coding
  - ISTA
  - algorithm-unfolding
  - spike-rate-coding
  - energy-efficiency
  - ECCV-2024
---

# Spike-Temporal Latent Representation for Energy-Efficient Event-to-Video Reconstruction｜Summary V2

## 1. Core Understanding

这篇论文研究 Event-to-Video（E2V）reconstruction：从 event camera 输出的事件流中恢复连续灰度视频。其核心不是让普通 SNN 直接黑箱学习 event-to-frame mapping，而是先为 event voxel 建立一个具有 LASSO 稀疏先验的 temporal latent code，再由 SNN decoder 从该 code 恢复灰度帧。

STLR 由两个级联的 SNN 组成：

$$
\text{event voxel}
\rightarrow
\text{Spike-based Voxel Temporal Encoder}
\rightarrow
\text{layer-wise spikes}
\rightarrow
\text{U-shape SNN decoder}
\rightarrow
\text{grayscale frame}.
$$

设一个 event voxel 为 $Y \in \mathbb R^{H \times W \times B}$。固定一个空间位置后，可取出长度为 $B$ 的 temporal vector $y \in \mathbb R^B$。作者用非负 LASSO 为其定义 $C$ 维稀疏 latent code $z \in \mathbb R_+^C$：

$$
\min_{z \geq 0}
\frac{1}{2}
\left\|
y - \Phi z
\right\|_2^2
+
\lambda
\left\|
z
\right\|_1,
\qquad
C > B.
$$

SVT 不直接输出任意连续系数，而是在 $K$ 个 unfolding layers 中产生 binary vectors $o^1,\ldots,o^K$，并将逐维平均发放率定义为：

$$
z^K
=
\frac{1}{K}
\sum_{k=1}^{K}
o^k.
$$

作者专门设计 membrane dynamics，使该 spike rate 在特定条件下近似 ISTA 的 fixed point；随后通过 Fixed Point Approximation（FPA）loss 在有限 $K$ 下进一步约束 fixed-point residual。

同一组 layer-wise spikes 被用于两个方向：

$$
\{o^k\}_{k=1}^{K}
\rightarrow
\begin{cases}
z^K \rightarrow \Phi z^K \approx y,
&
\text{重建 event temporal vector},
\\
[o^1;\ldots;o^K]
\rightarrow
\text{SNN decoder}
\rightarrow
\hat X,
&
\text{重建灰度帧}.
\end{cases}
$$

因此，LASSO 不直接完成 video reconstruction。它负责给 encoder 的 latent representation 加入非负、稀疏和可重建 event observation 的结构先验；真正把 latent spikes 映射为 frame 的是 U-shape SNN decoder。

---

## 2. Problem and Motivation

Event camera 只记录亮度变化事件 $e_i=(x_i,y_i,t_i,p_i)$，而不直接给出绝对灰度。不同初始亮度或不同真实视频可能产生相似的变化事件；低运动、低纹理区域又可能几乎没有事件。因此，event-to-video mapping 存在解不唯一、观测不足和对噪声敏感等问题，属于 ill-posed inverse problem。

已有 ANN-based E2V 方法重建质量较高，但依赖大量 dense floating-point computation。已有 SNN 方法降低了部分计算，却仍可能包含 ANN modules、浮点 upsampling 或 continuous synaptic filtering，同时缺少明确的 inverse-problem prior。

传统 spiking sparse-coding 方法常通过 synaptic filtering 将 binary spike train 转为 continuous rate estimate，例如：

$$
s^{t+1}
=
\beta s^t + o^t.
$$

该机制需要维护连续滤波状态和浮点衰减运算，也不容易直接组织为现代 multilayer convolutional SNN。STLR 的思路是把 optimization iterations 展开为 network depth，并用有限层之间的 spike frequency 表示 latent coefficient，从而将 LASSO/ISTA 结构与可训练 SNN 结合。

---

## 3. Method Overview

### 3.1 Event voxel 与 temporal vector

一段事件流被量化为 $B$ 个 temporal bins：

$$
Y \in \mathbb R^{H \times W \times B}.
$$

第 $B_i$ 个 bin 在空间位置 $(h_l,w_l)$ 的值为该时间区间内 polarity 的累加：

$$
Y_{h_l,w_l,B_i}
=
\sum_{r \in \mathcal T_{B_i}}
p_{h_l,w_l,r}.
$$

固定空间位置后：

$$
y
=
Y_{h_l,w_l,:}
\in
\mathbb R^B.
$$

实验中 $B=5$，即每个像素位置由 5 个时间分箱值构成。

### 3.2 Non-negative ISTA

非负 LASSO 的 ISTA update 写为：

$$
z^{k+1}
=
\left(
\Phi^\top y
-
\left(
\Phi^\top \Phi - I
\right)
z^k
-
\lambda
\right)^+.
$$

其中 $(a)^+=\max(a,0)$ 为逐元素非负投影。$\Phi^\top y$ 是 observation drive，$(\Phi^\top \Phi-I)z^k$ 描述 basis 之间的竞争，$\lambda$ 控制 sparsity。

### 3.3 Spike-temporal coding dynamics

作者设计：

$$
u^{k+1}
=
u^k
-
\Phi^\top \Phi o^k
+
\Phi^\top y
-
\lambda,
$$

$$
o^k
=
f
\left(
u^k - V_{\mathrm{th}}
\right).
$$

这里的 $k$ 不是 event timestamp，也不是 video-frame index，而是 latent coding 的 unfolding step，同时对应 SDFN 的 network depth。每一层产生 $C$ 维 binary spike vector $o^k$。

若在适当 $K$ 下满足：

$$
\frac{u^K}{K}
\rightarrow
0,
$$

则平均 spike rate $z^K$ 近似满足 ISTA fixed-point equation：

$$
z^K
\approx
\left(
\Phi^\top y
-
\left(
\Phi^\top \Phi-I
\right)
z^K
-
\lambda
\right)^+.
$$

该结论依赖前置条件，并不是对任意有限 $K$ 的无条件收敛保证。

### 3.4 Spike-Driven Spatial Unfolding Network

每个 unfolding layer 使用一个 Multi-Compartment Spiking（MCS）module，将理论 state $u^k$ 与可学习的空间特征变换结合。MCS 由 Heaviside function、两个 LIF neurons、两个 $3 \times 3$ convolution kernels $W^{k,1}$、$W^{k,2}$ 和可学习 decay factors $\alpha_1,\alpha_2$ 组成。

其作用不是逐层严格复制一次标准 ISTA，而是：

- 用公式化 state update 保留 ISTA-inspired competition；
- 用可学习 convolution 和 LIF dynamics 增加参数空间；
- 在第 $k$ 层输出 layer-wise spike $o^k$；
- 通过网络深度实现一条人工 coding sequence。

公式（13）右侧使用与左侧相同的 $m^{k,1}$、$m^{k,2}$，而非明确的 previous-state index。它可能是 assignment notation、内部时间索引省略或排版问题：`Needs further check`。

### 3.5 FPA Loss

定义：

$$
q
=
\Phi^\top y
-
\left(
\Phi^\top \Phi-I
\right)
z^K
-
\lambda.
$$

FPA loss 为：

$$
\mathcal L^{FP}
=
\frac{1}{C}
\left\|
z^K-q^+
\right\|_2^2
+
\frac{1}{C}
\left\|
q^-
\right\|_2^2.
$$

第一项让 spike rate 接近 ISTA fixed point；第二项压制 $q$ 的 negative components，使未投影关系 $z^K \approx q$ 与非负关系 $z^K \approx q^+$ 更接近。它约束的是 fixed-point algebraic residual，不等于证明 ISTA dynamics 已严格收敛或 $z^K$ 已是唯一最优解。

### 3.6 U-shape SNN Decoder

对第 $j$ 个样本、第 $t$ 个 event voxel，将全部层的 spikes 沿 channel 维拼接：

$$
o_S^{j,t}
=
\left[
o^{j,t,1};
o^{j,t,2};
\ldots;
o^{j,t,K}
\right],
\qquad
S=C \times K.
$$

在所有空间位置上组合后：

$$
O^{j,t}
\in
\{0,1\}^{H \times W \times S}.
$$

实验设置 $C=10$、$K=5$，所以 decoder input 有 $50$ 个 spike channels。Decoder 包含 header、residual 和 decoding blocks，并使用 MP skip connections、stride-2 spiking convolution 和 interpolation spiking layer：

$$
\hat O^{j,t}
=
\operatorname{SN}
\left(
\operatorname{Inter}
\left(
O^{j,t}
\right)
\right).
$$

Bilinear interpolation 本身产生 continuous values，之后再由 spiking neuron 量化为 spikes。因此“full spike-driven features”不等于整个 pipeline 只包含 binary addition。

### 3.7 Training objective

总损失为：

$$
\mathcal L
=
\sum_{t=1}^{T}
\left(
\mathcal L_t^{R1}
+
\mathcal L_t^{R2}
+
\mathcal L_t^{FP}
\right)
+
\sum_{t=L_0}^{T}
\mathcal L_t^{TC}.
$$

- $\mathcal L^{R1}$：使 $\Phi z^K$ 重建 event temporal vector；
- $\mathcal L^{R2}$：使用 LPIPS 监督 reconstructed frame；
- $\mathcal L^{FP}$：约束 ISTA fixed-point residual；
- $\mathcal L^{TC}$：约束连续 frames 的 temporal consistency。

正文未给出 TC loss 的完整公式，也未说明四项是否另有 weighting coefficients：`Needs further check`。

---

## 4. Key Components and Mechanisms

### 4.1 三种不同的“时间”

必须区分：

1. Event timestamp $t_i$：传感器真实时间；
2. Temporal-bin index $B_i$：event voxel 内的时间分箱；
3. Coding step $k=1,\ldots,K$：optimization unfolding depth。

STLR 名称中的 spike-temporal coding 主要指第 3 种人工 coding sequence，不应直接等同于原始事件流时间。

### 4.2 Spike rate 与 layer-wise spikes 的不同用途

平均后的：

$$
z^K
=
\frac{1}{K}
\sum_{k=1}^{K}
o^k
$$

用于 LASSO/FPA 和 event-vector reconstruction。

Decoder 则使用：

$$
[o^1;\ldots;o^K],
$$

即保留每一层的 binary pattern，而不是只使用平均 rate。由此，frame branch 获得的信息比单独 $z^K$ 更丰富。

### 4.3 Joint supervision

同一个 SVT encoder 同时受到两类目标约束：

$$
\text{event-structure supervision}
:
\mathcal L^{R1}
+
\mathcal L^{FP},
$$

$$
\text{video-reconstruction supervision}
:
\mathcal L^{R2}
+
\mathcal L^{TC}.
$$

所谓“event voxel 与 frame 共享 latent coding”并非先验已被证明，而是通过 joint training 强制同一组 spikes 同时服务于 event reconstruction 和 frame reconstruction。

### 4.4 Surrogate gradient

论文公式（18）写为：

$$
\frac{\partial o^t}{\partial u^t}
=
\frac{1}{\pi}
\arctan
\left(
\pi
\left(
u^t-V_{\mathrm{th}}
\right)
\right)
+
\frac{1}{2}.
$$

该表达式更像 Heaviside 的平滑近似，而其导数通常应为 rational function。论文可能混写了 surrogate activation 与 surrogate derivative；实际代码采用哪一形式：`Needs further check`。

---

## 5. Experiments and Main Evidence

### 5.1 Setting

训练数据由 MS-COCO images 经过 3D mapping、随机 6-DOF motion 和 ESIM 生成，共 950 synthetic sequences。测试使用 IJRR、HQF 和 MVSEC，形成 synthetic-to-real evaluation。

主要设置：

- temporal bins：$B=5$；
- coding steps：$K=5$；
- latent dimension：$C=10$；
- crop：$128 \times 128$；
- optimizer：Adam；
- learning rate：$0.001$；
- batch size：4；
- epochs：100。

### 5.2 Reconstruction quality

STLR 在三个数据集的九个指标上均优于纯 SNN baseline EVSNN。

IJRR：

$$
\text{EVSNN}
:
0.097/0.383/0.352
\rightarrow
\text{STLR}
:
0.075/0.469/0.264
$$

分别对应 MSE、SSIM、LPIPS。

与 ANN–SNN hybrid PA-EVSNN 相比：

- IJRR：STLR 的 SSIM、LPIPS 更好，MSE 略差；
- HQF：互有优劣；
- MVSEC：STLR 三项均明显更好。

MVSEC 上 STLR 为表中 overall best：

$$
\mathrm{MSE}=0.128,
\qquad
\mathrm{SSIM}=0.251,
\qquad
\mathrm{LPIPS}=0.552.
$$

因此“comparable to PA-EVSNN”基本成立，但应限定为不同数据集互有优劣；在 MVSEC 上 STLR 明显领先。Table 1 的星号未标出 MVSEC，尽管其三项也优于 EVSNN，属于表格标注遗漏。

### 5.3 Parameters、spike rate 与 theoretical energy

参数量：

$$
\text{EVSNN}=4.41\ \mathrm M,
\qquad
\text{PA-EVSNN}=4.62\ \mathrm M,
\qquad
\text{STLR}=0.61\ \mathrm M.
$$

STLR 分别约为前两者的 $13.8\%$ 和 $13.2\%$。

STLR 在 IJRR、HQF、MVSEC 的 spike rate 分别为：

$$
21.98\%,
\qquad
21.07\%,
\qquad
20.07\%.
$$

作者基于 7 nm CMOS 上：

$$
E_{\mathrm{MUL}}
=
1.31\ \mathrm{pJ},
\qquad
E_{\mathrm{ADD}}
=
0.38\ \mathrm{pJ}
$$

进行 operation-count energy estimate。STLR 的估计能耗约为 EVSNN 的 $5.26\%$–$5.53\%$、PA-EVSNN 的 $4.75\%$–$5.00\%$。

这是 theoretical MUL/ADD proxy，不是 GPU、neuromorphic chip 或完整系统的 hardware-measured energy。它未明确包含 memory access、state storage、BatchNorm、interpolation、voxelization 和 control overhead。

### 5.4 Unfolding steps

在 $K=5,8,10$ 中，$K=10$ 的跨数据集平均 MSE、SSIM 和 LPIPS 最好，但性能并不随 $K$ 单调提升；IJRR 的部分感知指标在 $K=5$ 更好，$K=8$ 的平均结果甚至差于 $K=5$。

主实验仍采用 $K=5$，作者未解释为何不采用平均结果更好的 $K=10$。较可能的原因是 efficiency–quality trade-off，但属于推断：`Needs further check`。

### 5.5 FPA ablation

加入 FPA 后，平均结果从：

$$
0.148/0.296/0.464
$$

改善为：

$$
0.104/0.316/0.458.
$$

但它并非逐数据集、逐指标全面提升：

- IJRR 的 MSE 变差；
- HQF 的 SSIM 和 LPIPS 略差；
- 主要增益来自 MVSEC 的显著改善。

因此，实验支持“FPA 平均有效”，不能写成“FPA 在所有设置中都改善性能”。

### 5.6 Decoder neurons 与 robustness

LIF、PLIF、SPSN 和 SLTT 在不同数据集、指标上互有优劣；不存在统一最优 neuron。主模型采用 SLTT，其在 MVSEC 上最好，但选择理由未被完整解释。

在 Poisson noise $\lambda=0.1$ 的 IJRR 实验中，STLR 的 MSE、SSIM、LPIPS 均优于 E2VID、EVSNN 和 PA-EVSNN。但实验只包含一种噪声和一个强度，且噪声注入方式未完整说明：`Needs further check`。

---

## 6. Strengths and Limitations

### 6.1 Strengths

1. 将 event voxel 的 temporal vector 明确建模为 non-negative sparse coding。
2. 将 ISTA fixed-point structure 与 SNN spike rate 建立可解释联系。
3. 用 algorithm unfolding 将 optimization steps 转换为可学习 network depth。
4. 同时利用 rate code 做 event reconstruction、layer-wise spikes 做 frame decoding。
5. 参数量显著低于已有 SNN E2V models。
6. 在 synthetic training、real evaluation 下表现出较好的 sim-to-real generalization。
7. 在 operation-count model 下取得显著理论能耗优势。
8. 在 sparse-event 和 Poisson-noise 示例中表现出较好的纹理保持和鲁棒性。

### 6.2 Limitations

1. “Event voxel 与 frame 共享 latent coding”是核心假设，主要由 joint reconstruction loss 支撑，缺少独立理论证明。
2. Theorem 1 依赖 $u^K/K \rightarrow 0$，但该条件未被证明自然成立。
3. 证明用 $\sum_{k=1}^{K-1}o^k/K$ 近似定义中的 $\sum_{k=1}^{K}o^k/K$；主设置 $K=5$ 时差异未必可忽略。
4. 由 $z^K \geq 0$ 推出未投影式与正投影式等价并不严格，FPA 的 negative-part penalty 也间接说明存在差距。
5. FPA 只最小化 fixed-point residual，不等于证明 ISTA convergence、唯一解或 LASSO optimum。
6. 公式（13）的 state index 不清晰，公式（18）可能混写 surrogate activation 与 derivative。
7. TC loss 和各 loss weights 未完整说明。
8. “Full spike-driven features”仍包含 voxelization、continuous membrane states、matrix projection、BatchNorm、bilinear interpolation 和 final continuous MP output。
9. Energy 是 theoretical operation estimate，不是硬件实测；没有报告 wall-clock latency。
10. $K=10$ 平均更好，但主实验采用 $K=5$，缺少 trade-off 解释。
11. Robustness 只验证一个 Poisson-noise setting，不能泛化到全部 event noise。
12. 论文将稀疏先验描述为处理 ill-posedness，但它只能缩小可行解空间，不能彻底消除 E2V 的不适定性。

---

## 7. Relation to Other Papers and Survey Taxonomy

### 7.1 Primary taxonomy

- Event-to-Video Reconstruction
- SNN-based Dense Reconstruction
- Temporal Latent Representation
- Non-negative Sparse Coding
- LASSO / ISTA
- Algorithm Unfolding
- Spike-Rate Coding
- Optimization-Inspired SNN
- Energy-Efficient Event Vision

### 7.2 SNN role

STLR 中的 SNN 承担两种不同角色：

- SVT：spike rate 表示 optimization-inspired latent coefficient；
- Decoder：layer-wise binary spikes 传播空间特征，final membrane potential 输出连续灰度。

它在 network architecture 层面是两个串联 SNN，不是 ANN–SNN hybrid；但由于仍包含多种 continuous operations，不能称为 binary-only end-to-end neuromorphic implementation。

### 7.3 Relation to SpikeSlicer

SpikeSlicer 将：

$$
\text{spike time}
\rightarrow
\text{event slicing boundary}.
$$

STLR 将：

$$
\text{spike rate across unfolding depth}
\rightarrow
\text{sparse latent code}.
$$

二者都赋予 spike 明确算法语义，但一个使用发放时刻控制数据边界，另一个使用跨层发放频率近似优化变量。

---

### PDF-verified relation backfill

主要路线是把 convolutional LASSO/ISTA unfolding 映射为 spike-rate latent code，再用串联 spiking decoder 输出 video intensity。

- **An Iterative Thresholding Algorithm for Linear Inverse Problems with a Sparsity Constraint (Ingrid Daubechies et al., Communications on Pure and Applied Mathematics 2004)** — `foundation`。该工作提供 unfolded sparse coding 的基础机制；当前论文将其用于自身的 event/SNN pipeline，而不是把该前驱本身作为新贡献。 对应 Sections 4 and 5: optimization-inspired SNN and reconstruction。证据：Method 3.1, PDF pp.4-5, citation and bibliography [5]。 当前 active corpus 未覆盖。
- **Learning Efficient Sparse and Low Rank Models (Pablo Sprechmann et al., TPAMI 2015)** — `foundation`。该工作提供 unfolded sparse coding 的基础机制；当前论文将其用于自身的 event/SNN pipeline，而不是把该前驱本身作为新贡献。 对应 Sections 4 and 5: optimization-inspired SNN and reconstruction。证据：Method 3.1, PDF pp.4-5, citation and bibliography [32]。 当前 active corpus 未覆盖。
- **Events-to-Video: Bringing Modern Computer Vision to Event Cameras (Henri Rebecq et al., CVPR 2019)** — `baseline`。该工作是 event-to-video reconstruction 的实验 comparator；当前论文与其主要区别在于本文第 3–4 节所述的核心机制。 对应 Section 5: reconstruction。证据：Related Work and Experiments, PDF pp.3 and 10, citation and bibliography [28]。 当前 active corpus 未覆盖。 值得 backward search。
- **Fast Image Reconstruction with an Event Camera (Cedric Scheerlinck et al., WACV 2020)** — `baseline`。该工作是 lightweight recurrent reconstruction 的实验 comparator；当前论文与其主要区别在于本文第 3–4 节所述的核心机制。 对应 Sections 5 and 6: reconstruction and efficiency。证据：Related Work and Experiments Table 1, PDF pp.3 and 10, citation and bibliography [30]。 当前 active corpus 未覆盖。

## 8. Survey-Usable Takeaways

1. E2V 是从亮度变化恢复绝对灰度的 ill-posed inverse problem。
2. STLR 不直接用普通 SNN 黑箱重建，而是引入 non-negative LASSO sparse prior。
3. 每个像素位置的 $B$ 维 event temporal vector 被编码为 $C$ 维 spike-rate latent code。
4. Coding step $k$ 是 unfolding depth，不是原始事件时间。
5. Average spike rate 用于近似 ISTA fixed point；layer-wise spikes 则被拼接后输入 decoder。
6. FPA loss 约束 fixed-point residual，但不构成完整 convergence proof。
7. Event reconstruction loss 与 frame reconstruction loss 共同迫使同一 latent spikes 服务于两个目标。
8. STLR 全面优于 EVSNN，并在 MVSEC 上取得表中 overall best。
9. 参数量仅 $0.61$ M，operation-level theoretical energy 约为已有 SNN baselines 的 $5\%$。
10. 能效结论不是硬件实测，且 full spike-driven 不等于全流程只有 binary operations。
11. $K=10$ 平均质量最好而主配置使用 $K=5$，说明方法存在未充分说明的 quality–efficiency trade-off。
12. 论文的主要方法学价值是把 sparse optimization fixed point 转换为可训练 SNN 的 spike-rate representation。

---

# Supplement Points

## Questions and Clarifications

### Q1. Event voxel 中的 $B$ 是什么？

$B$ 表示一个 event voxel 沿时间轴划分出的 temporal-bin 数量。

完整 voxel 为：

$$
Y
\in
\mathbb R^{H \times W \times B}.
$$

其中：

- $H,W$：空间尺寸；
- $B$：时间分箱数。

固定空间位置 $(h,w)$ 后：

$$
y
=
Y_{h,w,:}
\in
\mathbb R^B.
$$

实验中 $B=5$。因此，每个像素位置由 5 个连续时间段中的 polarity accumulation 构成，而不是一个单独 event value。

### Q2. “近似 ISTA fixed point”是什么意思？

把 ISTA update 记为：

$$
\mathcal T(z)
=
\left(
\Phi^\top y
-
\left(
\Phi^\top \Phi-I
\right)
z
-
\lambda
\right)^+.
$$

Fixed point $z^*$ 满足：

$$
z^*
=
\mathcal T(z^*).
$$

含义是：将 $z^*$ 再执行一次 ISTA update，结果基本不再改变。

STLR 并不声称每个 SNN layer 严格等于一次标准 ISTA。它声称经过 $K$ 个 coding layers 后得到的 average spike rate $z^K$，在特定条件下满足：

$$
z^K
\approx
\mathcal T(z^K).
$$

因此它近似一个自洽的 ISTA solution state，而不是逐层完全复制 ISTA trajectory。

### Q3. Synaptic filtering 是什么？为什么传统方法需要它？

单个 spike 只能取：

$$
o^t
\in
\{0,1\},
$$

但 sparse coefficient 通常是 continuous value。传统方法会对 spike train 做低通滤波：

$$
s^{t+1}
=
\beta s^t + o^t
$$

或：

$$
s(t)
=
\sum_{\tau \leq t}
\kappa(t-\tau)o(\tau).
$$

发放越频繁，continuous state $s$ 越大，可将其作为 latent coefficient 或 synaptic current。

使用它的原因是：

1. 将 binary spike sequence 解码为 continuous rate；
2. 让单个 spike 对后续时刻持续产生作用。

问题是滤波需要维护 floating state，并执行 $\beta s^t$ 等连续乘法；传统稳态 firing-rate dynamics 也不容易直接组织成现代 multilayer convolutional SNN。

STLR 用有限 unfolding layers 的平均 spike frequency 替代长期 synaptic filtering，但整个模型仍不是无浮点运算。

### Q4. LASSO 恢复的是 event voxel，和 Video Reconstruction 有什么关系？

LASSO 分支首先约束：

$$
y
\approx
\Phi z^K.
$$

它保证 latent code 保留 event voxel 的 temporal information。

Frame 分支则使用同一 encoder 的 layer-wise spikes：

$$
[o^1;\ldots;o^K]
\rightarrow
\text{SNN decoder}
\rightarrow
\hat X.
$$

因此：

- LASSO 不直接输出 video frame；
- $\Phi z^K$ 重建 event temporal vector；
- U-shape SNN decoder 重建 grayscale frame；
- 两个目标通过共享 SVT latent spikes 联合训练。

所谓“event voxel 与 frame 共享 latent coding”是训练中被强制建立的关系，不是 LASSO 自动给出的结论。

### Q5. 什么叫经过 $K$ 个 coding steps 后，将 binary spikes 求平均？

对同一个 event voxel、同一个空间位置，第 $k$ 个 unfolding layer 输出：

$$
o^k
\in
\{0,1\}^C.
$$

假设 $K=5$、$C=4$：

$$
o^1=[1,0,0,1],
$$

$$
o^2=[1,0,1,1],
$$

$$
o^3=[0,0,0,1],
$$

$$
o^4=[1,1,0,1],
$$

$$
o^5=[0,0,0,1].
$$

逐维相加并除以 5：

$$
z^5
=
\frac{1}{5}
\sum_{k=1}^{5}
o^k
=
[0.6,0.2,0.2,1.0].
$$

每个分量表示对应 latent channel 在 5 个 unfolded layers 中的发放比例。

该平均不是对：

- raw-event timestamps；
- $B$ 个 temporal bins；
- 不同 frames；
- 不同 samples；

求平均，而是对同一输入在 network depth 上产生的 $K$ 个 binary latent vectors 求平均。

### Q6. “标准 SNN dynamics 与 ISTA 无关”是什么意思？Neuron dynamics 是什么？

Neuron dynamics 是 membrane state 如何积累输入、越过阈值、发放和 reset 的规则。普通 IF neuron 例如：

$$
u^{t+1}
=
u^t
+
w o_{\mathrm{inp}}^t
-
o^t V_{\mathrm{reset}}
+
b.
$$

ISTA update 则要求特定结构：

$$
z^{k+1}
=
\left(
\Phi^\top y
-
\left(
\Phi^\top \Phi-I
\right)
z^k
-
\lambda
\right)^+.
$$

它包含：

- observation drive $\Phi^\top y$；
- basis competition；
- sparsity penalty $\lambda$；
- non-negative shrinkage。

普通 IF equation 不会自动包含这些 LASSO-specific terms。因此，“无法由标准 SNN 实现”更准确的含义是：仅使用默认 IF dynamics，并不能保证输出 rate 满足 ISTA fixed-point equation；并非标准 SNN 在函数逼近意义上绝对无法学习该 mapping。

### Q7. “通过 spike rate 建立公式（5），同时受益于 spike computation 和 nonlinear dynamics”是什么意思？

作者将 state update改写为：

$$
u^{k+1}
=
u^k
-
\Phi^\top\Phi o^k
+
\Phi^\top y
-
\lambda.
$$

这样，公式中显式加入了：

- 与 observation 的匹配；
- latent bases 之间的 competition；
- sparsity penalty。

再使用 threshold：

$$
o^k
=
H
\left(
u^k-V_{\mathrm{th}}
\right)
$$

产生 binary spikes，并以 average rate 作为 continuous latent code。

“受益于 spike-based computation”是指 sparse binary feature 在理想硬件上可用 conditional ADD 替代 dense MUL–ADD。

“受益于 nonlinear spiking dynamics”是指 threshold、reset、LIF accumulation 和 learnable MCS modules 提供非线性、稀疏选择与可学习映射。

这属于方法动机，并不自动证明它比标准 ISTA 更准确。

### Q8. 什么叫把一个 coding step “展开成 network layer”？

普通 iterative algorithm 可以写成：

$$
z^1=\mathcal T(z^0),
\qquad
z^2=\mathcal T(z^1),
\qquad
\ldots,
\qquad
z^K=\mathcal T(z^{K-1}).
$$

在程序中它是一个循环。Algorithm unfolding 将第 $k$ 次更新变成第 $k$ 个 network layer：

$$
\text{Layer 1}
\rightarrow
\text{Layer 2}
\rightarrow
\cdots
\rightarrow
\text{Layer }K.
$$

STLR 的数据流为：

$$
u^1
\rightarrow
\operatorname{MCS}_1
\rightarrow
o^1
\rightarrow
u^2
\rightarrow
\operatorname{MCS}_2
\rightarrow
o^2
\rightarrow
\cdots.
$$

每层拥有自己的 $W^{k,1}$、$W^{k,2}$，所以它不是简单重复完全相同的固定函数，而是将 optimization-inspired recurrence 变成可学习 deep network。

### Q9. 四个 Loss 分别是什么？

总损失为：

$$
\mathcal L
=
\mathcal L^{R1}
+
\mathcal L^{R2}
+
\mathcal L^{FP}
+
\mathcal L^{TC}
$$

在各 voxel/frame 上求和。

#### Event reconstruction loss

$$
\mathcal L^{R1}
=
\left\|
y-\Phi z^K
\right\|_2^2.
$$

检查 latent code 是否保留 event temporal vector。

#### Frame reconstruction loss

$$
\mathcal L^{R2}
=
\operatorname{LPIPS}
\left(
\hat X,X
\right).
$$

检查 reconstructed frame 与 ground truth 的感知特征是否一致。

#### Fixed-point approximation loss

$$
\mathcal L^{FP}
=
\frac{1}{C}
\left\|
z^K-q^+
\right\|_2^2
+
\frac{1}{C}
\left\|
q^-
\right\|_2^2.
$$

检查 spike rate 是否接近 ISTA fixed point，并压制未投影 expression 的负值。

#### Temporal consistency loss

$$
\mathcal L^{TC}
$$

约束连续 frames 在运动对齐后保持时间一致，减少闪烁。正文未给出其完整实现：`Needs further check`。

### Q10. 一个从 events 到 losses 的完整简化计算流

以下是解释性例子，不是论文真实参数。

设一个像素使用 $B=2$ 个 bins，原始事件累积得到：

$$
y
=
\begin{bmatrix}
1\\
0
\end{bmatrix}.
$$

取：

$$
\Phi
=
\begin{bmatrix}
1 & 0 & 1/\sqrt{2}\\
0 & 1 & 1/\sqrt{2}
\end{bmatrix},
\qquad
C=3,
\qquad
K=3,
$$

$$
\lambda=0.2,
\qquad
V_{\mathrm{th}}=0.5.
$$

计算：

$$
\Phi^\top y-\lambda
\approx
\begin{bmatrix}
0.8\\
-0.2\\
0.507
\end{bmatrix}.
$$

从 $u^0=0$ 开始，简化 dynamics 产生：

$$
o^1
=
\begin{bmatrix}
1\\0\\1
\end{bmatrix},
\qquad
o^2
=
\begin{bmatrix}
0\\0\\0
\end{bmatrix},
\qquad
o^3
=
\begin{bmatrix}
1\\0\\0
\end{bmatrix}.
$$

平均得到：

$$
z^3
=
\frac{o^1+o^2+o^3}{3}
=
\begin{bmatrix}
0.667\\
0\\
0.333
\end{bmatrix}.
$$

Event reconstruction：

$$
\hat y
=
\Phi z^3
\approx
\begin{bmatrix}
0.902\\
0.236
\end{bmatrix}.
$$

因此：

$$
\mathcal L^{R1}
=
\left\|
y-\hat y
\right\|_2^2
\approx
0.065.
$$

再计算 ISTA mapping：

$$
q
=
\Phi^\top y
-
\left(
\Phi^\top\Phi-I
\right)
z^3
-
\lambda
\approx
\begin{bmatrix}
0.564\\
-0.436\\
0.036
\end{bmatrix}.
$$

于是：

$$
q^+
=
\begin{bmatrix}
0.564\\
0\\
0.036
\end{bmatrix},
\qquad
q^-
=
\begin{bmatrix}
0\\
0.436\\
0
\end{bmatrix}.
$$

得到：

$$
\mathcal L^{FP}
\approx
0.096.
$$

Frame decoder 使用的不是单独 $z^3$，而是：

$$
o_S
=
[o^1;o^2;o^3]
=
[1,0,1,0,0,0,1,0,0].
$$

假设简化 decoder 输出 $\hat X=0.6$，ground truth 为 $X=0.8$，用平方误差仅示意 LPIPS 方向：

$$
\mathcal L^{R2}
\approx
(0.6-0.8)^2
=
0.04.
$$

假设上一帧为 $0.55$，忽略 motion warping，仅示意 temporal loss：

$$
\mathcal L^{TC}
\approx
(0.6-0.55)^2
=
0.0025.
$$

则示意总损失为：

$$
\mathcal L
\approx
0.065+0.096+0.04+0.0025
=
0.2035.
$$

反向传播时：

- $\mathcal L^{R1}$、$\mathcal L^{FP}$ 直接约束 SVT 和 $\Phi$；
- $\mathcal L^{R2}$、$\mathcal L^{TC}$ 通过 decoder 回传到 SVT；
- surrogate gradient 近似处理 binary threshold 的不可导问题。

### Q11. Ill-posed problem 是什么？

一个 well-posed problem 通常要求：

1. 解存在；
2. 解唯一；
3. 输入小变化只引起输出小变化。

E2V 可能违反后两点。

Event camera 记录的是 brightness change，而不是 absolute intensity。两个灰度序列：

$$
[50,60,70]
$$

和：

$$
[100,110,120]
$$

具有相同变化量，可能产生相似 events，但绝对亮度不同。

此外，未达到 threshold 的亮度变化不会产生事件；稀疏区域存在大量未观测信息。少量噪声或漏事件也可能导致明显纹理和亮度误差。

LASSO 通过 sparsity prior 缩小 latent solution space：

$$
\min_{z \geq 0}
\frac{1}{2}
\left\|
y-\Phi z
\right\|_2^2
+
\lambda
\left\|
z
\right\|_1.
$$

它是在众多可能解释中偏好稀疏解，从而缓解欠约束问题，但不能从数学上彻底消除 E2V 的 ill-posedness。

---

## Additional Technical Details

### Theorem 1：Spike Rate 近似 ISTA Fixed Point 的推导与边界

作者从带 reset-by-subtraction 的 charging process 出发：

$$
u^{k+1}
=
u^k
+
\Phi^\top y
-
\left(
\Phi^\top\Phi-I
\right)o^k
-
o^kV_{\mathrm{reset}}
-
\lambda.
$$

当：

$$
V_{\mathrm{reset}}=1
$$

时：

$$
-
\left(
\Phi^\top\Phi-I
\right)o^k
-
o^k
=
-
\Phi^\top\Phi o^k,
$$

所以该式化为：

$$
u^{k+1}
=
u^k
-
\Phi^\top\Phi o^k
+
\Phi^\top y
-
\lambda,
$$

即论文公式（6）。

将 $K$ 步更新累积，得到：

$$
u^K
=
K\Phi^\top y
-
\left(
\Phi^\top\Phi-I
\right)
\sum_{k=1}^{K-1}o^k
-
K\lambda
-
V_{\mathrm{reset}}
\sum_{k=1}^{K-1}o^k.
$$

整理并除以 $K$：

$$
\frac{1}{K}
\sum_{k=1}^{K-1}o^k
=
\frac{1}{V_{\mathrm{reset}}}
\left(
\Phi^\top y
-
\left(
\Phi^\top\Phi-I
\right)
\frac{1}{K}
\sum_{k=1}^{K-1}o^k
-
\lambda
\right)
-
\frac{u^K}{KV_{\mathrm{reset}}}.
$$

取 $V_{\mathrm{reset}}=1$，若满足：

$$
\frac{u^K}{K}
\rightarrow
0,
$$

则 residual membrane term 消失，average spikes 近似满足：

$$
\bar o
\approx
\Phi^\top y
-
\left(
\Phi^\top\Phi-I
\right)
\bar o
-
\lambda.
$$

再利用 non-negative spike rate，作者写为：

$$
z^K
\approx
\left(
\Phi^\top y
-
\left(
\Phi^\top\Phi-I
\right)
z^K
-
\lambda
\right)^+,
$$

即 ISTA fixed-point equation。

该推导需要保留以下边界：

1. $u^K/K \rightarrow 0$ 是前置条件，论文没有证明其必然成立。
2. 定义使用 $\sum_{k=1}^{K}o^k/K$，证明主要使用 $\sum_{k=1}^{K-1}o^k/K$，二者相差 $o^K/K$。
3. 主实验 $K=5$，所以最大单维差异可能达到 $0.2$，不能只用“大 $K$”直觉忽略。
4. $z^K \geq 0$ 并不足以严格保证未投影右侧也非负，因此公式（11）与（12）并非天然完全等价。
5. FPA 的 negative-part term 正是在训练中缩小这一差异。
6. Fixed-point residual 小，不自动证明 fixed point 唯一、ISTA trajectory 收敛或 $z^K$ 已达到 LASSO global optimum。
7. 因此 Theorem 1 提供的是有条件的 optimization interpretation，而不是完整的 finite-depth convergence theorem。
