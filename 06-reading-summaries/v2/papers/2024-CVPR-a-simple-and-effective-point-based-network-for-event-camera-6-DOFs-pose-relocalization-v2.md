---
tags:
  - event-camera
  - event-cloud
  - point-based-network
  - camera-pose-relocalization
  - temporal-attention
  - Bi-LSTM
  - non-spiking
---

# Summary V2｜A Simple and Effective Point-based Network for Event Camera 6-DOFs Pose Relocalization

## 1. Core Understanding

PEPNet 是一个用于 event-camera 6-DOFs Camera Pose Relocalization（CPR）的 **non-spiking point-based network**。给定与某个 pose label 对应的一段 event stream，它不先生成 event image 或 time surface，而是把每个事件的 $(x,y,t)$ 当作 pseudo-3D point：$x,y$ 是像素位置，$t$ 是归一化时间坐标。网络先用三层 hierarchical point abstraction 提取 spatial feature 和 timestamp-conditioned implicit temporal feature，再把最后保留下来的 point features 按时间排列，交给 Attentive Bi-directional LSTM（A-Bi-LSTM）显式建模前后依赖，最终回归三维 translation 与三维 Euler-angle rotation。

PEPNet 的完整数据流是：

$$
\text{event stream}
\rightarrow
\text{time window}
\rightarrow
\text{fixed-size }(x,y,t)\text{ point set}
\rightarrow
3\text{-stage hierarchy}
\rightarrow
\text{chronological feature sequence}
\rightarrow
\text{A-Bi-LSTM}
\rightarrow
(\hat{\mathbf p},\hat{\mathbf q}).
$$

它没有 spiking neuron、membrane potential、surrogate gradient 或 spike-driven arithmetic。事件输入的稀疏性不等于网络计算是 spiking。因此，PEPNet 在本综述中的价值是作为 **Event Cloud representation、point hierarchy、non-spiking temporal modeling 和 lightweight pose regression** 的对照案例。

## 2. Problem and Motivation

传统 frame camera 每个时刻输出整幅图像；event camera 只在像素 log-intensity change 越过阈值时输出事件：

$$
e_k=(x_k,y_k,t_k,p_k).
$$

其中 $p_k$ 是 polarity。事件的微秒级 timestamp 和稀疏分布携带运动线索，而 camera relocalization 需要从近期观测判断相机的 global 位置和姿态。现有 event-based CPR 通常把一段事件累积为 event image、event surface 或 RWEI，再送入 CNN、LSTM 或 DSAC-style pipeline。这样容易复用 frame-based architecture，但会把不同 timestamp 的事件压进有限 channels，降低单事件级时间分辨率，并可能引入 denoising、representation conversion 和 geometric solver 等额外成本。

Event Cloud 路线把事件写成 $(x,y,t)$ points，可以保留 timestamp 并利用 point network 处理稀疏输入。但它不能机械照搬普通 $(x,y,z)$ Point Cloud：$z$ 是空间深度，$t$ 是有方向的时间；普通 point network 常用 symmetric pooling，强调 permutation invariance，却不显式建模事件之间的 temporal dependency。PEPNet 因而解决两个问题：

1. 如何在不转成 frame 的情况下，从稀疏 $(x,y,t)$ points 提取多尺度特征；
2. 如何在 point hierarchy 之后恢复显式的 chronological dependency，用于 6-DOF pose regression。

## 3. Method Overview

### 3.1 Event window、sampling 与 normalization

完整事件序列为：

$$
\mathcal E=\{e_k=(x_k,y_k,t_k,p_k)\mid k=1,\ldots,n\}.
$$

对 sequence 中的 pose labels，作者截取持续时间为 $R$ 的事件段：

$$
P_i=\{e_j,\ldots,e_l\mid t_l-t_j=R\},
\qquad i=1,\ldots,M.
$$

Algorithm 1 设置 $N_p=1024$、$R=10^3$、$S_{\mathrm{num}}=3$、$K=24$。若 timestamp 单位确为论文图中所示的 $1\ \mu\mathrm{s}$，则 $R=10^3$ 对应约 $1\ \mathrm{ms}$；但正文同时说 pose ground truth resolution 为 $5\ \mathrm{ms}$，没有解释二者如何对齐。算法在取完 $e_{j:l}$ 后令 $j=l$，更接近连续分段，而不是通常意义上带 overlap 的 sliding window。

每个 $P_i$ 被采样为固定 $N_p$ 个 points，然后归一化：

$$
P_i^N=\left(
\frac{X_i}{w},
\frac{Y_i}{h},
\frac{T_i-t_j}{t_l-t_j}
\right),
$$

$$
X_i=\{x_j,\ldots,x_l\},\quad
Y_i=\{y_j,\ldots,y_l\},\quad
T_i=\{t_j,\ldots,t_l\}.
$$

因此 $x,y,t$ 都被缩放到近似 $[0,1]$，使 pseudo-3D distance 不会直接由像素分辨率或绝对 timestamp 数值主导。原始事件定义包含 $p_k$，但 Eq. (3)、Figure 3 的 $N\times3$ 输入和后续 shape 都只有 $(x,y,t)$；论文没有显示 polarity 进入 backbone。预处理中的 `Sampling` 如何在事件不足或过多时选择、重复或丢弃 points，也未说明。

### 3.2 三层 hierarchy 的逐层数据流

每个 hierarchy stage 都执行：

$$
\text{FPS/KNN}
\rightarrow
\text{standardization}
\rightarrow
\text{local residual extractor}
\rightarrow
\text{temporal attention aggregation}
\rightarrow
\text{global residual extractor}.
$$

标准 PEPNet 的三个输出 feature dimensions 为 $D_1,D_2,D_3=[64,128,256]$；PEPNettiny 为 $[16,32,64]$。初始 point count 为 1024，Figure 6 显示最后的 temporal sequence 有 128 points；正文没有列出每个 stage 的完整 centroid-count schedule。

论文给出的主要 tensor flow 如下。$N_s$ 是 stage $s$ 的 centroid 数量，$D_{s-1}$ 是输入 feature dimension：

| Step | Tensor | PDF 给出的或可直接对应的 shape | 含义 |
| --- | --- | --- | --- |
| Stage input | $P^N$ | $[B,N,3+D_{s-1}]$ | 每个 point 的 $(x,y,t)$ 与上一层 feature |
| FPS centroids | $P^S$ | $[B,N_s,3+D_{s-1}]$ | 从输入 points 选出的 representative points |
| KNN groups | $P^G$ | $[B,N_s,K,3+2D_{s-1}]$ | 每个 centroid 的 $K$ 个 neighbors；包含坐标、neighbor feature 和 centroid feature |
| Local extractor | $F_{\mathrm{local}}$ | $[B,N_s,K,D_s]$ | 每个 neighbor 的局部 feature |
| Attention aggregation | $F_{\mathrm{aggre}}$ | $[B,N_s,D_s]$ | 每个 group 汇聚成一个 centroid feature |
| Global extractor | $F_{\mathrm{global}}$ | $[B,N_s,D_s]$ | 当前 stage 输出，进入下一 stage |
| Final hierarchy sequence | $X$ | $[B,N_3,D_3]$，Figure 3 也画成 $3+D_3$ | 按 timestamp 排列的高层 point features |
| Forward/backward recurrent outputs | $y_t,y'_t$ | 各 $[B,N_3,D_3/2]$ | 两个时间方向的 features |
| Concatenated sequence | $Y_t$ | $[B,N_3,D_3]$ | $y_t\oplus y'_t$ |
| Sequence attention | $Y_a$ | $[B,D_3]$ | 对 $N_3$ 个 recurrent outputs 加权求和 |
| Regressor output | $(\hat{\mathbf p},\hat{\mathbf q})$ | $[B,3]+[B,3]$ | translation 与 Euler rotation |

这张表忠实保留了论文内部的不一致：Eq. (5) 把 group 写成 $3+2D$，Algorithm 1 line 10 却写成 $2D_{s-1}$；Figure 3 在 hierarchy output 保留 $3+D_s$，Algorithm 1 line 16 又只写 $D_s$。因此 coordinates 是否在每个 extractor 后始终与 features 拼接、stage 1 的 $D_0$ 如何定义，需要代码确认。

### 3.3 A-Bi-LSTM 与 pose output

三层 hierarchy 并行处理 points，虽然 feature 受 timestamp 和 spatiotemporal neighborhood 影响，却没有 recurrent state。作者将这种信息称为 implicit temporal feature。最后保留下来的 features 按 timestamp 形成 $x_1,\ldots,x_{N_3}$，再送入正向和反向 recurrent paths：

$$
h_t=f(W_hx_t+U_hh_{t-1}+b_h),
$$

$$
h'_t=f(W'_hx_t+U'_hh'_{t+1}+b'_h),
$$

$$
y_t=Vh_t+b_y,\qquad y'_t=V'h'_t+b'_y.
$$

随后拼接两个方向：

$$
Y_t=y_t\oplus y'_t,
$$

并对完整 sequence 做第二次 attention：

$$
A=\operatorname{SoftMax}(\operatorname{MLP}(Y_t)),
\qquad
Y_a=A\cdot Y_t.
$$

Algorithm 1 明确给出两个方向各输出 $D_3/2$ channels，拼接后恢复为 $D_3$，最后 attention 得到单个 $[B,D_3]$ descriptor。Figure 6 的 attention visualization 覆盖 128 个 chronological points，并显示首尾位置权重较高。作者据此推测 pose estimation 依赖窗口起点与终点的 feature difference，但这只是 visualization-based interpretation。

论文称模块为 Bi-LSTM，Eq. (14)-(16) 却只是 generic bidirectional RNN 的简写，没有 input/forget/output gates、cell state 或 hidden-size 细节。由于使用 backward recurrence，模型必须看到完整 window，不能作为严格 causal event-by-event estimator。

### 3.4 Regressor、loss 与训练目标

一个含 hidden layer 的 fully connected regressor 从 $Y_a$ 输出：

$$
\hat{\mathbf p}\in\mathbb R^3,
\qquad
\hat{\mathbf q}\in\mathbb R^3,
$$

分别表示 displacement/translation vector 和三维 Euler angles。训练目标写为：

$$
\mathcal L
=
\alpha\lVert\hat{\mathbf p}-\mathbf p\rVert_2
+
\beta\lVert\hat{\mathbf q}-\mathbf q\rVert_2
+
\lambda\sum_iw_i^2.
$$

$\alpha,\beta$ 平衡不同单位和尺度的 translation/rotation，$\lambda$ 是 weight decay。Eq. (20) 是未平方的 L2 norm，但 Section 4 又称训练和评价使用 translation/rotation MSE，二者并不完全一致。Table 4 的综合指标也不是训练 loss，而是：

$$
T+R
=
\text{translation error}
+
\text{rotation error}\times\frac{\pi}{180},
$$

即把 degree 转成 rad 后与 meter 数值相加，仅用于表内比较，不是物理上统一的误差单位。Table 4 的 `T+R` 数值看起来又将该结果乘了 100，例如 $0.015+0.884\pi/180\approx0.0304$，表中写为 $3.04$；caption 没有注明这个 scale factor。

## 4. Key Components and Mechanisms

### 4.1 FPS、KNN 与 pseudo-spatiotemporal neighborhood

每个 stage 先用 Farthest Point Sampling 选择 centroids，再用 KNN 查找每个 centroid 的 $K=24$ 个 neighbors：

$$
P_i^S=\operatorname{FPS}(P_i^N),
\qquad
P_i^G=\operatorname{KNN}(P_i^N,P_i^S).
$$

若实现直接在 normalized $(x,y,t)$ 上计算距离，则 neighborhood 同时受空间和时间距离影响：相近像素但相隔较久的 events、同一时刻但相距较远的 events 都可能被排除。Normalization 使三轴数值量级接近，但这也隐式假定单位归一化后的 spatial distance 和 temporal distance 可直接比较。论文没有消融不同 temporal scaling，也没有明确 KNN metric，因此这一几何假设的敏感性仍未知。

作者强调 FPS/KNN 后仍严格保持 timestamp order。不过 FPS 选出的 centroid indices 和 KNN 按距离返回的 neighbor order 通常都不天然等于时间顺序，所以实现需要额外 sort 或 order-preserving gather。正文未给出具体重排操作，属于 `Needs further check`。

### 4.2 Group standardization 到底做什么

每个 group 相对 centroid 做中心化并除以局部 standard deviation：

$$
P_i^{GS}
=
\frac{P_i^G-P_i^S}{\operatorname{Std}(P_i^G)},
$$

$$
\operatorname{Std}(P_i^G)
=
\sqrt{
\frac{
\sum_{j=0}^{3n-1}(g_j-\bar g)^2
}{3n-1}
},
$$

$$
g=[x_0,y_0,t_0,\ldots,x_n,y_n,t_n].
$$

从 Eq. (7) 看，standard deviation 是把一个 group 的所有 $x,y,t$ 坐标展平后计算的 scalar，而不是分别对三个轴计算；中心化则表达 neighbor 相对 centroid 的 offset。这样可减少局部运动尺度或 point density 对 MLP 的影响。可是 Eq. (6) 对 $P^G$ 和 $P^S$ 的 feature channels 如何广播、是否只标准化 coordinates，没有完整定义。

### 4.3 Local/global residual extractor

Local extractor 和 global extractor 使用相同形式的 bottleneck residual MLP：

$$
I(x)=f(\operatorname{BN}(\operatorname{MLP}_1(x))),
$$

$$
O(x)=\operatorname{BN}(\operatorname{MLP}_2(I(x))),
$$

$$
\operatorname{Ext}(x)=f(x+O(x)).
$$

Local extractor 独立处理 $K$ 个 neighbors，shape 保持 $[B,N_s,K,D_s]$；attention 把 $K$ 维压缩后，global extractor 在 centroid level 处理 $[B,N_s,D_s]$。Residual path 使输入输出维度一致，feature dimension 的增加主要在 stage 间 projection/group concatenation 发生，而不是在 bottleneck 内发生。论文没有给出 $f$ 的具体选择和两层 MLP 的 bottleneck ratio。

### 4.4 两级 attention 的对象不同

第一层 temporal aggregation 在每个 local KNN group 内工作：

$$
F_{\mathrm{local}}
=(F_{t_1},\ldots,F_{t_K}),
$$

$$
a_{t_k}
=
\frac{
\exp(\operatorname{MLP}(F_{t_k}))
}{
\sum_{r=1}^{K}\exp(\operatorname{MLP}(F_{t_r}))
},
$$

$$
F_{\mathrm{aggre}}
=
\sum_{k=1}^{K}a_{t_k}F_{t_k}.
$$

MLP 将每个 $D_s$-dim feature 映射为一个 scalar，softmax 在 $K$ 个 neighbors 上归一化。它比 channel-wise MaxPooling 允许多个 points 同时贡献，但该 weighted sum 本身仍是 symmetric aggregation；时间信息主要来自 $F_{t_k}$ 已编码的 $t_k$、neighborhood 和作者声称保留的 chronological ordering。

第二层 attention 位于 Bi-LSTM 之后，在整个 $N_3$-length sequence 上汇聚 recurrent outputs。第一层回答“一个局部 group 中哪些 events 重要”，第二层回答“完整窗口的哪些高层时间位置对 pose 最重要”。

## 5. Experiments and Main Evidence

### 5.1 Protocol 与模型规模

实验覆盖室内 IJRR 和 outdoor-night M3ED。IJRR random split 随机取 70% sequences 训练、30% 测试；novel split 按时间取前 70% 训练、后 30% 测试，更能暴露 temporal distribution shift。M3ED 选择 Car、Falcon、Spot 三类 robots 的五段夜间 sequences；由于 sensor resolution 更高，作者先 downsample，并将输入 points 从 1024 增至 2048，其余设置沿用 IJRR random split。

标准 PEPNet 为 0.774 M parameters、0.459 G FLOPs；PEPNettiny 为 0.064 M、0.033 G。训练和测试平台是 AMD Ryzen 7950X、RTX 4090、32 GB memory。论文没有完整报告 optimizer、learning rate、batch size、training epochs、data augmentation 或 stage-wise point counts，不能只靠正文完全复现。

### 5.2 IJRR random/novel split

Table 1 先报告每个 sequence 的 median translation/rotation error，再对六个 sequence 求平均。PEPNet random split 平均为 $0.013\ \mathrm m$ 和 $0.904^\circ$；CNN-LSTM 为 $0.019\ \mathrm m$ 和 $1.591^\circ$。PEPNettiny 仅约为 CNN-LSTM 参数量的 $0.5\%$，仍达到 $0.019\ \mathrm m$ 和 $1.306^\circ$。Abstract 的 `38% improvement` 大致来自 translation 与 rotation 两项相对改善的平均，不是单独定义的统一 metric。

Novel split 上，PEPNet 上升至 $0.029\ \mathrm m$ 和 $2.13^\circ$，接近 AECRN 的 $0.035\ \mathrm m$ 和 $2.23^\circ$，说明 scene/time distribution shift 明显削弱了优势。作者报告 RTX 4090 server 上每个 sample 为 $6.7\ \mathrm{ms}$，主要耗时在 grouping and sampling；这不包含 sensor-to-window waiting time，也不是 edge device 或 FPGA/ASIC 上的实测 latency。

### 5.3 M3ED 与逐场景结果

M3ED 五段 outdoor-night sequences 上，PEPNet 平均为 $0.372\ \mathrm m$ 和 $1.04^\circ$，CNN-LSTM 为 $0.430\ \mathrm m$ 和 $2.197^\circ$。PEPNet 并非逐项都最优：例如 `SpotNightPenLoop` 和 `SpotPlazaLight` 的 translation error 高于 CNN-LSTM，但 rotation 更低。Abstract 的 `33% improvement` 同样是 translation/rotation 相对改善的汇总表达，不是统一定义的 pose metric。

### 5.4 Key-module ablation

Table 4 在 IJRR `shape translation` random split 上分离 hierarchy、recurrent module 和 aggregation：

| Configuration | Translation | Rotation | $T+R$ |
| --- | ---: | ---: | ---: |
| HS + Max | 0.015 m | $0.884^\circ$ | 3.04 |
| HS + Temporal | 0.014 m | $0.786^\circ$ | 2.77 |
| HS + LSTM + Max | 0.014 m | $0.833^\circ$ | 2.85 |
| HS + LSTM + Temporal | 0.012 m | $0.603^\circ$ | 2.25 |
| HS + Bi-LSTM + Max | 0.014 m | $0.813^\circ$ | 2.82 |
| HS + Bi-LSTM + Temporal | **0.011 m** | **$0.582^\circ$** | **2.12** |

可见 temporal aggregation 在无 recurrent、LSTM、Bi-LSTM 三组配对中均优于 MaxPooling；加入单向 LSTM 有明确收益；Bi-LSTM 相对 LSTM 的独立增益较小。最好的结果来自 hierarchy、bidirectional recurrence 和 temporal aggregation 的组合，而不是某个单一模块。

Loss-weight ablation 使用 PEPNettiny 训练 100 epochs，说明 $\alpha/\beta$ 会随 motion type 改变 translation-rotation trade-off。例如 rotation scene 增加 rotation weight 可改善 rotation error，但论文没有提出跨场景自动平衡方案。

## 6. Strengths and Limitations

**Strengths.** PEPNet 避免 event-to-frame conversion，给出了从 normalized Event Cloud 到 pose 的端到端 point pipeline；三层 hierarchy、local temporal aggregation 和 A-Bi-LSTM 的职责较清晰；相较 frame-based baselines 参数和 FLOPs 显著降低；同时报告 random split、novel split、M3ED、module ablation 和 server latency。

**Limitations.** 论文缺少完整训练超参数和 stage sampling schedule；polarity 在 backbone 中去向不明；`sliding window`、$R=10^3$ 和 5 ms pose labels 的对齐未解释；Eq. (5)、Figure 3 与 Algorithm 1 的 tensor shapes 不完全一致；FPS/KNN 后如何保持严格 timestamp order 未说明；Bi-LSTM 非因果；Euler-angle regression 受 rotation representation 影响；novel split 显示过拟合；参数/FLOPs 和 RTX 4090 latency 不能证明 ultra-low-power deployment，论文也没有 energy 或 edge-hardware measurement。

## 7. Relation to Other Papers and Survey Taxonomy

相较 event-image + CNN/LSTM，PEPNet 保留单事件 timestamp；相较 RWEI + DSAC*，它避免 representation conversion 和 geometric hybrid solver；相较普通 PointNet/PointNet++，它增加 temporal aggregation 与 A-Bi-LSTM。它在综述 taxonomy 中属于：

- **Event Cloud / point-based event representation**
- **Non-spiking temporal modeling**
- **Event-based camera pose relocalization**
- **Lightweight ANN comparator for SNN methods**

它说明 event timing 可以由 normalized temporal coordinate、point neighborhood、attention 和 recurrent state 利用，不一定必须依赖 SNN；同时也提醒我们区分 sparse event input 与 spike-driven computation。

### PDF-verified relation backfill

主要路线是以 normalized $(x,y,t)$ Event Cloud 为输入的 hierarchical point network，并用 temporal aggregation 与 A-Bi-LSTM 完成 6-DOF pose regression。

- **PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space (Charles Ruizhongtai Qi et al., NeurIPS 2017)** - `foundation`。该工作提供 hierarchical sparse point abstraction 的基础机制；PEPNet 将其改造为带 timestamp preservation 和 temporal aggregation 的 Event Cloud hierarchy。对应 Section 2: event representation。证据：Related Work 2.3，PDF p.3，citation and bibliography [29]。当前 active corpus 未覆盖。
- **Space-Time Event Clouds for Gesture Recognition: From RGB Cameras to Event Cameras (Qinyi Wang et al., WACV 2019)** - `extends`。PEPNet 沿用 Event Cloud point processing 思路，并为 pose relocalization 增加 hierarchy、temporal aggregation 和 A-Bi-LSTM。对应 Sections 2 and 5: representation and pose。证据：Related Work 2.3，PDF p.3，citation and bibliography [40]。当前 active corpus 未覆盖。值得 backward search。
- **Real-time 6DOF Pose Relocalization for Event Cameras with Stacked Spatial LSTM Networks (Anh Nguyen et al., CVPRW 2019)** - `baseline`。该工作是 event-image + spatial LSTM pose relocalization comparator；PEPNet 的主要区别是直接处理 Event Cloud。对应 Section 5: pose relocalization。证据：Related Work 2.2 and Experiments 4.2，PDF pp.2 and 6，citation and bibliography [26]。当前 active corpus 未覆盖。值得 backward search。

## 8. Survey-Usable Takeaways

- Takeaway 1: PEPNet 不是“完全无预处理”：它避免 frame conversion，但仍执行 fixed-duration segmentation、fixed-count sampling、normalization、FPS 和 KNN。
- Takeaway 2: $(x,y,t)$ hierarchy 提取的是 timestamp-conditioned implicit temporal feature；Bi-LSTM 才通过 recurrent state 显式建立前后时间依赖。
- Takeaway 3: Local temporal aggregation 和 sequence attention 是两级不同的加权机制，分别汇聚 KNN neighbors 与完整 recurrent sequence。
- Takeaway 4: Tensor shape、timestamp reordering、polarity 和 window-label alignment 是正文未闭合的关键复现问题。
- Takeaway 5: PEPNet 在论文协议下兼顾 accuracy 与 model size，但 novel split 的退化和非因果 Bi-LSTM 限制了实时泛化结论。
- Takeaway 6: 作为 non-spiking baseline，PEPNet 证明 point-based sparse event processing 本身就能获得较强效果，SNN 方法必须进一步证明 spike dynamics 或 hardware execution 的独立价值。

## Supplement Points

### Additional Technical Details

#### 1. 用一个 symbolic example 走完 hierarchy stage

假设 stage $s$ 接收 $N$ 个 points，每个 point 携带三维坐标和 $D_{s-1}$ 维 feature：

$$
P^N\in\mathbb R^{B\times N\times(3+D_{s-1})}.
$$

FPS 先保留 $N_s$ 个 centroids；KNN 再为每个 centroid 查找 24 个 neighbors。若按 Eq. (5) 组织 group，则每个 neighbor record 包含：

$$
(x,y,t)
\oplus
f_{\mathrm{neighbor}}
\oplus
f_{\mathrm{centroid}},
$$

因此：

$$
P^G\in\mathbb R^{B\times N_s\times24\times(3+2D_{s-1})}.
$$

Coordinates 相对 centroid 标准化后，local residual MLP 为每个 neighbor 产生 $D_s$ 维 feature：

$$
F_{\mathrm{local}}
\in
\mathbb R^{B\times N_s\times24\times D_s}.
$$

Attention MLP 在最后一维执行 $D_s\rightarrow1$，softmax 在 24 个 neighbors 上执行，随后 weighted sum 消去 $K$ 轴：

$$
F_{\mathrm{aggre}}
\in
\mathbb R^{B\times N_s\times D_s}.
$$

Global residual MLP 不改变 shape，输出进入下一 stage。重复三次后，points 从 1024 逐层减少，features 从 3 coordinates 扩展到 256 channels，最后保留约 128 个 chronological descriptors。中间具体 $N_1,N_2$ 和 coordinate concatenation 仍需代码确认。

#### 2. Permutation invariance 与 Event Cloud 的真正矛盾

对包含 timestamp 的 tuples 来说，重排内存顺序并不会改变集合本身：

$$
\{(x_i,y_i,t_i)\}_{i=1}^{N}
=
\{(x_{\pi(i)},y_{\pi(i)},t_{\pi(i)})\}_{i=1}^{N}.
$$

所以论文“Event Cloud contradicts permutation invariance”的说法过强。真正的问题是 symmetric set aggregation 通常不会显式表达：

$$
t_1<t_2<\cdots<t_N
$$

对应的 state transition。PEPNet 一方面让 $t$ 参与 point feature 和 neighborhood construction，另一方面把 final features 重新组织成 chronological sequence 交给 Bi-LSTM。前者编码“事件发生在什么时候”，后者建模“前后事件如何关联”。

#### 3. 隐式 temporal feature 与显式 temporal feature

隐式 temporal feature 来自 $t$ 作为 coordinate 参与 normalization、FPS/KNN、standardization、MLP 和 local attention。所有 points 仍可并行处理，没有隐藏状态从较早时间递推到较晚时间。

显式 temporal feature 来自 Bi-LSTM：$h_t$ 依赖 $h_{t-1}$，$h'_t$ 依赖 $h'_{t+1}$。因此某个位置的 output 不只描述自身 point feature，还整合窗口前后上下文。这也是 PEPNet 更强但非因果的原因。
