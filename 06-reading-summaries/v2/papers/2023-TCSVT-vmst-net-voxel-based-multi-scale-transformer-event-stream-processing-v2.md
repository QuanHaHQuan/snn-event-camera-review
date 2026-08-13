---
tags: ["event camera", "VMST-Net", "voxel token", "STFE", "multi-scale transformer", "MSMHSA", "MSF", "voxel merging", "downsampling", "non-SNN"]
---

# Summary V2｜Voxel-Based Multi-Scale Transformer Network for Event Stream Processing

## 1. Core Understanding

VMST-Net 将 event stream 转换为稀疏的 voxel tokens：每个 token 既包含 voxel 在 `x-y-t` 网格中的坐标，也包含由 STFE 编码的 voxel 内局部时空特征。随后，模型通过 multi-scale transformer 和 hierarchical voxel merging，在控制计算量的同时逐步建立 local-to-global dependencies。

本文不是 SNN 方法，没有 spiking neuron、membrane dynamics 或 surrogate-gradient training。它属于 **sparse voxel representation + non-spiking hierarchical transformer** 路线，可作为 SNN event models 的强非脉冲对照。

## 2. Problem and Motivation

已有 event representations 各有明显局限。Dense frame/map methods 可以直接使用 CNN，但会把稀疏 events 转成规则稠密张量，引入空区域计算，并压缩细粒度时间信息。Point/graph methods 能保留稀疏性和 `x-y-t` 几何，但单个 event 信息量低，激进 downsampling 又容易丢失局部轮廓和运动线索。

Voxel-wise methods 在二者之间折中：一个 voxel 聚合多个相邻 events，比单点包含更多局部信息，同时只保留 nonempty voxels。不过，EV-VGCNN 主要将 voxel 内二维 patch flatten 后输入 MLP，时间关系不足；VMV-GCN 使用 multi-view projection 改善运动表示，但简单 flattening 仍难充分建模 voxel 内局部时空依赖。网络层面，GCN 通常偏重固定局部邻域，global modeling 较弱；早期 event transformers 虽擅长长距离关系，却容易忽视局部多尺度细节。

VMST-Net 因而解决两个问题：先提高单个 voxel token 的信息密度，再以较低计算量建模 voxel tokens 之间从局部到全局的关系。

## 3. Method Overview

输入事件集合为：

$$
\varepsilon
=

\left\{
(x_i,y_i,t_i,p_i)
\right\}_{i=1}^{N_e}
$$

时间戳首先归一化到：

$$
[0,B-1]
$$

然后按空间—时间尺寸：

$$
(v_w,v_h,v_t)
$$

划分 coarse voxel grid。模型删除 empty voxels，再根据内部 event count 选出固定数量的 representative voxels。

每个 selected voxel 内部进一步构造：

$$
E_v
\in
\mathbb{R}^{v_h\times v_w\times d}
$$

其中 `d` 是局部 temporal bins。STFE 通过 temporal bilinear interpolation、2D convolutions 和 pooling，将其编码为一个 `D` 维特征，最终形成：

$$
U\in\mathbb{R}^{N_v\times3},
\qquad
F\in\mathbb{R}^{N_v\times D}
$$

其中 `U` 是 voxel coordinates，`F` 是 voxel features。

Backbone 包含四个 stages：

```text
Stage 1:
Voxel Token Generation
→ Multi-Scale Transformer Block

Stage 2–4:
Voxel Merging
→ Multi-Scale Transformer Block
```

随着网络加深，token 数量逐步减少，feature channels 由 `32` 增至 `128、256、512`。分类与动作识别任务通过 pooling 和 FC classifier 输出类别；姿态估计任务输出每个关节在横纵坐标轴上的概率分布。

## 4. Key Components and Mechanisms

### 4.1 Voxel Token Generation and STFE

全局时间首先归一化为：

$$
t_i^*
=

\frac{t_i-t_{\min}}
{t_{\max}-t_{\min}}
(B-1)
$$

每个 voxel 的离散位置为：

$$
u=(u^x,u^y,u^t)
$$

Voxel selection 优先保留内部 events 较多的 voxels，以固定 transformer token 数。随后，voxel 内 event 被映射到局部坐标，并通过 temporal bilinear interpolation 分配到相邻的 local time bins：

$$
E_v(x,y,n)
=

\sum_j
p_j
\max
\left(
0,1-\left|n-t_j^v\right|
\right)
I(x_j^v=x,y_j^v=y)
$$

STFE 将 `d` 个 temporal bins 视为 2D convolution 的 input channels。卷积核在空间平面滑动，同时对不同时间通道加权，因此能够联合提取局部 spatial pattern 和 temporal change。该表示仍然会聚合 events，并不保留原始 event list，但比单纯 event count 或 flattened patch 更有信息量。

### 4.2 MSMHSA and MSF

Multi-Scale Multi-Head Self-Attention 接收：

$$
F\in\mathbb{R}^{N\times C},
\qquad
U\in\mathbb{R}^{N\times3}
$$

并生成：

$$
Q=FW_Q,\qquad
K=FW_K,\qquad
V=FW_V
$$

不同 attention branches 根据 `U` 使用不同邻居数量的 kNN neighborhoods。小邻域侧重局部细节和细微运动，大邻域侧重粗粒度结构和远距离关系。Relative position encoding 不仅进入 attention score，也被加入 value features，因此几何关系会直接影响聚合结果。

MSF 先拼接不同尺度的输出，再经过 FC、GELU 和 global pooling 生成 channel-wise、scale-wise weights，对原始多尺度 features 动态重加权。其意义在于：multi-scale information 本身可能包含 sub-optimal scales，简单 addition 或 concatenation 不一定能够自动选择有效尺度。

### 4.3 Local-to-Global Strategy and Voxel Merging

前两个 stages 采用两种 local neighborhoods，后两个 stages 则同时保留 local branch 和 global branch：

```text
Stage 1–2: local + local
Stage 3–4: global + local
```

因此 local-to-global 并不是每层连续增加同一个邻居数，而是浅层优先保存局部细节，深层才引入全局上下文。

Voxel Merging 使用 FPS 选择覆盖较均匀的 representative tokens。对于 sampled token `u`，模型寻找 `K` 个邻居，并组合邻居 feature 与相对位置：

$$
\Delta C_k
=

\operatorname{concat}
\left(
f_k,u_k-u
\right)
$$

随后通过共享 FC、LN 和邻居维 max pooling 得到新的 token feature：

$$
\hat{f}
=

\max_{k\in K}
\left[
\operatorname{LN}
\left(
\operatorname{FC}(\Delta C_k)
\right)
\right]
$$

因此 Voxel Merging 不是简单删除未采样 tokens，而是先选择中心，再将邻域信息聚合回保留的 tokens。

## 5. Experiments and Main Evidence

实验覆盖 object classification、action recognition 和 human pose estimation。VMST-Net 在 N-Caltech101、CIFAR10-DVS 和 N-ImageNet 等较复杂分类数据集上表现突出；在 DVS128 Gesture 上不是最高，但在 UCF101-DVS 和 HMDB51-DVS 上明显领先论文列出的 baselines。DHP19 上，它以约 `3.59M` parameters 和 `0.38G` MACs 获得比 point-transformer baselines 更低的 pose error，但精度仍不及较重的 frame-based Pose-Res50。

消融表明，完整 STFE 相比只保留空间编码的 `d=1` 版本提升约 `2.5` 个百分点。单独引入 multi-scale mechanism 可能使 CIFAR10-DVS accuracy 从 `74.9%` 降至 `74.4%`，说明额外尺度也可能产生干扰；加入 MSF 后提高至 `75.3%`。在 DHP19 上，阶段式 L-G 优于始终 local 的 L-L，也优于从浅层开始就使用 local-global 的 G-G，支持“浅层保留局部运动、深层加入全局人体结构”的设计。

VMST-Net 在 object classification 设置中仅约 `0.44G` MACs，但 runtime 约为 `42.5 ms/sample`。论文明确将较慢推理归因于 kNN neighbor search 和 FPS voxel downsampling。其优势是神经网络主体算术量低，而不是 model size 最小或 wall-clock runtime 最快。

## 6. Strengths and Limitations

**Strengths**

* 在 raw event points 和 dense event tensors 之间形成信息量较高的 sparse voxel-token representation。
* STFE、MSMHSA、MSF 和 Voxel Merging 共同构成完整的 hierarchical architecture。
* Multi-scale mechanism 配有动态 fusion，而不是默认所有尺度都有效。
* 同时覆盖分类、动作识别和姿态估计，验证了静态语义、动态运动和细粒度空间预测。
* Reported MACs 较低，尤其体现出 token reduction 对深层 global modeling 成本的控制。

**Limitations / Questions**

* 不同数据集使用不同的 `B`、voxel size、`N_v` 和 downsampling schedule，前端具有明显 dataset-specific tuning。
* Top-event-count selection 可能删除低密度但有判别力的 voxels，也可能保留高频噪声区域。
* 当 nonempty voxel 数不足 `0.95N_v` 时，论文描述的 selection rule 逻辑不完整，`Needs further check`。
* Neighborhood scales、`B`、`d` 和 polarity accumulation 缺少系统消融。
* Model size 并非最小，FPS、kNN 和不规则 memory access 导致实际 runtime 较慢。
* 未报告真实 edge-device latency、energy 或功耗。
* 多个分类和动作数据集由 RGB images/videos 转换得到，不能完全代表原生 event scenes。

## 7. Relation to Other Papers and Survey Taxonomy

与 TTPOINT 相比，VMST-Net 不把 sampled events 直接作为 points，而是先将局部 events 聚合成 informative voxel tokens。它减少了单点过度稀疏的问题，但引入 voxelization、STFE、kNN 和 FPS 开销。

与 EV-ACT 相比，VMST-Net 不生成覆盖全图的 dense event tensors，而是仅处理 selected voxel tokens；EV-ACT 强调 multi-representation fusion 和 SlowFast CNN，VMST-Net 则强调 sparse hierarchical transformer。

在综述 taxonomy 中，本文属于：

* sparse voxel-based event representation；
* non-spiking event transformer；
* intra-voxel spatio-temporal encoding；
* local-to-global attention；
* hierarchical token downsampling；
* MACs–runtime efficiency trade-off。

它不是 SNN 文献，但适合作为判断 SNN 方法收益究竟来自 spiking computation，还是来自 sparse voxel representation 与 hierarchical architecture 的重要对照。

## 8. Survey-Usable Takeaways

* Takeaway 1: Voxel representation 的性能不只取决于如何划分 voxel，更取决于如何编码 voxel 内部的 events。
* Takeaway 2: Multi-scale attention 不一定自动带来收益；sub-optimal scales 可能产生干扰，因此需要动态 fusion 或 scale selection。
* Takeaway 3: Local-to-global modeling 应与网络层级匹配：浅层过早引入 global context 可能损害局部细节。
* Takeaway 4: Downsampling 是 sparse event network 的核心结构决策，它同时决定 token coverage、信息损失、感受野和 global-attention cost。
* Takeaway 5: MACs、parameter count、runtime 和 energy 是不同指标；低 MACs 不意味着实现中的 FPS、kNN 和 memory operations 同样高效。

## Supplement Points：

### 1. Related Work 中各路线的优缺点

#### Dense Frame / Map

代表方法包括 Time Surface、Event Frame、4D Grid、Voxel Grid、TBR、EST 和 Matrix-LSTM。

**优点**

* 表示规则，容易 batch；
* 可直接使用成熟 CNN；
* 部分 learnable representations 可以根据任务调整编码。

**缺点**

* 将 sparse events 转成 dense tensor；
* 空白区域仍参与卷积；
* 时间离散或累计会损失 fine timing；
* Time Surface 可能对高频 events 和噪声敏感；
* 模型复杂度和 memory cost 通常较高。

#### Point / Graph

代表方法包括 RG-CNN、EV-Gait、AEGNN 和 rasterized point representation。

**优点**

* 保留 `x-y-t` 稀疏结构；
* 不需要处理大面积空白区域；
* 部分方法可以异步处理 events；
* 通常具有较低的理论计算量。

**缺点**

* 单个 event 信息量有限；
* aggressive sampling 会造成过度稀疏；
* 对噪声和采样分布敏感；
* local semantic 和 motion cues 不足；
* 增加 point 数又会提高计算量。

#### Existing Voxel Methods

EV-VGCNN 将 voxel 内 events 投影为二维 patch，flatten 后输入 MLP；它比单点保存更多空间信息，但弱化时间关系。VMV-GCN 通过 multi-view projections 增加运动信息，但 flattening 仍不足以表达完整局部时空结构。

Voxel route 的优势是兼顾 sparsity 和 local information；不足是 voxel 内编码方式、voxel selection 和 neighborhood aggregation 会成为新的信息瓶颈。

#### CNN、SNN、GCN 与 Transformer Frameworks

CNN 精度较强，但经常忽略 event sparsity。SNN 理论上适合异步稀疏计算，但训练较困难。GCN 擅长局部几何聚合，但 global modeling 受限。Transformer 擅长全局关系，却可能缺少局部多尺度细节，并承担较高 attention cost。

VMST-Net 实际上是把 voxel representation、point-style neighborhoods 和 transformer attention 组合起来。

### 2. 普通 Voxel Grid 和 VMST-Net 的 Voxel Token

普通 dense Voxel Grid 通常表示为：

$$
V\in\mathbb{R}^{T\times H\times W}
$$

如果分离 polarity：

$$
V\in\mathbb{R}^{2\times T\times H\times W}
$$

多个 events 会被累积到相同 spatial-temporal bin，因此一个 bin 最终保存 aggregate value，而不是独立 event list。可以把每个 temporal bin 理解为一张局部 Event Frame。

VMST-Net 使用相同的时间离散思想，但不是直接保留完整 dense grid，而是：

```text
全局 x-y-t 空间
→ 划分 coarse voxels
→ 仅选择 nonempty representative voxels
→ 每个 coarse voxel 内构造局部 event tensor
→ 编码为一个 voxel token
```

因此它最终处理的是：

$$
N_v
$$

个 token，而不是全部：

$$
T\times H\times W
$$

位置。

---

### 3. `B`、Voxel Coordinate `u` 和局部时间 `d`

`B` 控制整个输入样本归一化后的全局时间范围：

$$
t_i^*
=

\frac{t_i-t_{\min}}
{t_{\max}-t_{\min}}
(B-1)
$$

例如：

$$
B=9
$$

则最早 event 映射到 `0`，最晚 event 映射到 `8`。它使不同绝对时长的样本具有统一的相对时间坐标，并避免原始微秒 timestamp 与像素坐标尺度差距过大。

三组时间参数需要区分：

* `B`：整个样本的全局时间网格范围；
* `v_t`：一个 coarse voxel 覆盖多少个全局时间单位；
* `d`：一个 selected voxel 内部再次划分多少个 local time bins。

Voxel coordinate：

$$
u=(u^x,u^y,u^t)
$$

是该 voxel 在离散 grid 中的索引，不是 events 的平均坐标：

$$
u^x
=

\left\lfloor
\frac{x}{v_w}
\right\rfloor
$$

$$
u^y
=

\left\lfloor
\frac{y}{v_h}
\right\rfloor
$$

$$
u^t
=

\left\lfloor
\frac{t^*}{v_t}
\right\rfloor
$$

---

### 4. Voxel Token Generation 数值例子

假设一段样本时间范围为：

$$
t_{\min}=0\ \mathrm{ms},
\qquad
t_{\max}=100\ \mathrm{ms}
$$

设置：

$$
B=9
$$

某个正极性 event 为：

$$
e=(27,14,82.5\ \mathrm{ms},+1)
$$

归一化时间为：

$$
t^*
=

\frac{82.5-0}{100-0}
\times 8
=

6.6
$$

假设 coarse voxel size 为：

$$
(v_w,v_h,v_t)=(10,10,3)
$$

那么其 voxel coordinate 是：

$$
u^x=\left\lfloor\frac{27}{10}\right\rfloor=2
$$

$$
u^y=\left\lfloor\frac{14}{10}\right\rfloor=1
$$

$$
u^t=\left\lfloor\frac{6.6}{3}\right\rfloor=2
$$

所以：

$$
u=(2,1,2)
$$

Event 在 voxel 内的局部空间坐标为：

$$
x^v=27-2\times10=7
$$

$$
y^v=14-1\times10=4
$$

若局部 temporal bins：

$$
d=3
$$

则局部时间位置为：

$$
t^v
=

\frac{6.6-2\times3}{3}
\times(3-1)
=

0.4
$$

该 event 会向 local bin `0` 贡献：

$$
1-\left|0-0.4\right|=0.6
$$

向 local bin `1` 贡献：

$$
1-\left|1-0.4\right|=0.4
$$

因此：

$$
E_v(7,4,0)\mathrel{+}=0.6
$$

$$
E_v(7,4,1)\mathrel{+}=0.4
$$

如果同一位置存在 negative event，则 signed polarity accumulation 可能发生部分抵消。

所有 events 写入后，得到：

$$
E_v\in\mathbb{R}^{v_h\times v_w\times d}
$$

再经过共享 STFE，压缩为：

$$
f_v\in\mathbb{R}^{D}
$$

最终该 voxel token 表示为：

$$
(u,f_v)
$$

---

### 5. 2D Convolution 如何同时混合 Spatial 和 Channel Information

STFE 的输入是：

$$
E_v\in\mathbb{R}^{v_h\times v_w\times d}
$$

将 `d` 个 time bins 当作 input channels 后，一个二维卷积核为：

$$
W
\in
\mathbb{R}^{
C_{\mathrm{out}}
\times d
\times k_h
\times k_w
}
$$

在每个输出位置，卷积同时执行：

1. 对 `k_h×k_w` 邻域内的空间位置加权；
2. 对所有 `d` 个 temporal channels 加权求和。

因此它可以学习：

```text
早期时间通道的左侧响应
+
后期时间通道的右侧响应
→ 局部向右运动模式
```

但它不是 3D convolution，因为卷积核不会沿独立的时间轴滑动；时间已经被固定编码进 channel dimension。

---

### 6. MSMHSA 与 MSF 的简化例子

以下数字仅用于说明机制，不是论文实验中的真实 attention weights。

假设当前有：

$$
N=8
$$

个 voxel tokens，feature dimension 为：

$$
C=4
$$

将特征分成两个二维 branches。

对 reference token `A`：

* local branch 使用 `k_1=2`，只查看最近的 `B、C`；
* larger-scale branch 使用 `k_2=4`，查看 `B、C、D、E`。

Local branch 可能得到：

$$
o_1
=

0.7v_B+0.3v_C
$$

Large-scale branch 可能得到：

$$
o_2
=

0.4v_B+0.3v_C+0.2v_D+0.1v_E
$$

其中 attention weights 由 query-key similarity 和 relative position共同决定。

随后，MSF 根据全局 pooled features 生成不同尺度的权重。例如某个 channel 更依赖局部边缘：

$$
w_{\mathrm{local}}=0.75,
\qquad
w_{\mathrm{large}}=0.25
$$

另一个 channel 更依赖全局轮廓：

$$
w_{\mathrm{local}}=0.30,
\qquad
w_{\mathrm{large}}=0.70
$$

因此 MSF 不是给整个 head 一个固定 scalar，而是动态、按 channel 调整各尺度贡献。

论文公式按两个尺度分支展开，但 Figure 5 又说明 two-head design 仅为便于表示；实际 head number 与 scale-to-head mapping 仍需结合代码确认：

`Needs further check`

---

### 7. Voxel Merging 数值例子

假设一个 stage 原有 8 个 tokens：

$$
{A,B,C,D,E,F,G,H}
$$

FPS 选择 4 个覆盖较均匀的 sampled tokens：

$$
{A,D,F,H}
$$

对于 sampled token `A`，假设找到三个邻居：

$$
B,C,D
$$

若输入 feature dimension 为 2，则：

$$
f_B=[1.0,0.2]
$$

相对位置为：

$$
u_B-u_A=[1,0,0]
$$

拼接后：

$$
\Delta C_B
=

[1.0,0.2,1,0,0]
$$

同理构造：

$$
\Delta C_C,\qquad
\Delta C_D
$$

经过共享 FC 和 LN 后，假设得到：

$$
g_B=[0.5,1.2]
$$

$$
g_C=[0.8,0.4]
$$

$$
g_D=[0.3,1.0]
$$

沿邻居维 max pooling：

$$
\hat{f}_A
=

\max
\left(
g_B,g_C,g_D
\right)
=

[0.8,1.2]
$$

因此，新 token `A` 不仅保留自身位置，还吸收了邻域中的 feature 和 relative geometry。

---

### 8. 为什么 MACs 低但 Runtime 较慢

MACs 主要统计 convolution、FC、attention projection 和矩阵乘法等算术操作。VMST-Net 之所以 MACs 较低，是因为：

* 只处理 selected sparse voxels；
* attention 主要在 kNN neighborhoods 内执行；
* 每个 transformer block 只有一层；
* token 数通过 Voxel Merging 持续减少；
* MSF 只增加少量 FC 计算。

但 runtime 还包含 MACs 不充分反映的操作。

#### kNN Search

需要根据三维坐标搜索邻居，并生成不规则 index lists。这类计算通常不是大型连续矩阵乘法。

#### FPS

FPS 是迭代采样。每选一个 token，都要更新其他 token 到已选集合的最小距离，难以充分并行。

#### Gather / Scatter

邻居 features 在 memory 中通常不连续，需要根据 indices 收集，容易成为 memory-bound operation。

#### Small Kernel Overhead

多个 sampling、indexing、pooling 和 neighborhood kernels 会产生额外 kernel-launch 和 synchronization cost。

#### Model Size 与 MACs 不同步

最后 stage 使用 `512` 维 features，因此参数量不一定最小；但此时 token 数已经很少，所以大 channel layers 的总 MACs 仍然可控。

因此，VMST-Net 的强项应表述为：

> 神经网络主体的理论算术量较低，但 sparse geometric operations 的不规则性使其实际推理速度不占优势。

---

### 9. Local-to-Global 消融的准确理解

三种结构应区分为：

* **L-L**：所有 stages 都使用 local multi-scale neighborhoods；
* **G-G**：所有 stages 都使用 local-global combination；
* **L-G**：浅层 local-local，深层 local-global。

所以，DHP19 结果支持的是：

> 阶段式 L-G 优于始终局部的 L-L，也优于从浅层就加入 global branch 的 G-G。

这说明 global context 并非越早加入越好。姿态估计需要浅层保留关节、边缘和细微运动，深层再整合整体人体结构。

---

### 10. Personal Reflection：Downsampling 的地位

这篇论文中，downsampling 不是普通的减算模块，而是整个 hierarchy 的核心。

它同时决定：

* 哪些 token 可以进入深层；
* 低密度信息是否被保留；
* 深层 token 对 `x-y-t` 空间的覆盖；
* feature channels 如何扩展；
* global attention 的计算规模；
* 实际 kNN/FPS runtime。

VMST-Net 的矛盾也集中在这里：FPS 提供比 random sampling 更均匀的时空覆盖，却引入更高实际延迟。因此，event-network downsampling 的评价不能只看保留精度，也必须同时考虑硬件并行性和 memory-access pattern。
