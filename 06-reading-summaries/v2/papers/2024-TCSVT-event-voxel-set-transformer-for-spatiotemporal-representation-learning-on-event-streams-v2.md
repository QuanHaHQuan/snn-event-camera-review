---
tags: [event-camera, event-voxel-set, transformer, point-based, action-recognition, non-spiking, NeuroHAR]
---

# Summary V2｜Event Voxel Set Transformer for Spatiotemporal Representation Learning on Event Streams

## 1. Core Understanding

EVSTr 是一个面向 event-based object classification 与 action recognition 的稀疏 voxel-set Transformer。它先把 raw event stream 转换为 non-empty event voxel set，再通过 **Multi-Scale Neighbor Embedding Layer（MNEL）** 聚合局部多尺度邻居，通过 **Voxel Self-Attention Layer（VSAL）** 建立单个 voxel set 内的全局交互；对长时动作流，则使用 **Stream-Segment Temporal Modeling Module（S2TM）** 建模 segment 之间的长期依赖。

本文不是 SNN。EVSTr 使用 MLP、BN、ReLU、k-NN、pooling、self-attention 和 FC layers，没有 spiking neuron、membrane potential、firing threshold、reset、surrogate gradient 或 ANN-to-SNN conversion。它应归为 **non-spiking sparse event representation learning**，可作为 SNN event recognition 的重要非脉冲对照。

## 2. Problem and Motivation

Dense frame-based methods 能复用 ImageNet/Kinetics pretrained models，但 sparse-to-dense conversion 会牺牲 event data 的稀疏性并引入冗余计算。Point-based methods 更符合 event stream 的结构，但作者认为已有方法存在两项不足：

1. 局部聚合器通常没有同时充分利用邻居之间的 positional relation、semantic relation 和 multi-scale neighborhood；
2. 仅依赖局部 graph/neighborhood aggregation，缺少远距离 voxel feature interaction。

此外，object classification 可由单个短时 voxel set 处理，而 action recognition 需要跨多个时间阶段理解完整运动模式。作者因此分别用 MNEL、VSAL 和 S2TM 对应局部、全局和跨 segment 时间建模，并提出在 camera motion 与 low-light 条件下采集的 NeuroHAR，补充现有真实动作数据集场景较简单的问题。

## 3. Method Overview

整体数据流为：

$$
\text{event stream}
\rightarrow
\text{event voxel set}
\rightarrow
\text{MNEL hierarchy}
\rightarrow
\text{VSAL}
\rightarrow
\text{recognition}.
$$

对于 object classification，整个事件流形成一个 voxel set，encoder 输出经 max/average pooling 和三层 FC head 分类。对于 action recognition，事件流等时长切分为 $K$ 个 segments；共享权重的 encoder 分别提取 segment features，S2TM 将每个 segment 压缩为 token，再用 Transformer 聚合长期上下文并以 class token 分类。

时间层级必须区分：

- $t_k$：sensor 的真实 event timestamp；
- $t_k^*$：归一化时间坐标；
- $T_v$：voxel 的 temporal size；
- $k\in\{1,\ldots,K\}$：stream segment index；
- Transformer token position：segment 顺序；
- 这些都不是 SNN timestep。

## 4. Key Components and Mechanisms

### 4.1 Event Voxel Set Representation

单个事件为 $e_k=(x_k,y_k,t_k,p_k)$，其中 $p_k\in\{+1,-1\}$。作者将不同持续时间的样本线性归一化到 $[0,T]$：

$$
t_k^*
=
\frac{T(t_k-t_1)}{t_M-t_1}.
$$

随后以 $H_v\times W_v\times T_v$ 划分三维 grid，并通过引用自 [12] 的 motion-sensitive sampling 选取 $N_v$ 个 non-empty voxels。每个 voxel 表示为 feature-coordinate pair：

$$
\mathcal V
=
\{(\mathbf f_i,\mathbf c_i)\}_{i=1}^{N_v},
\qquad
\mathbf c_i\in\mathbb R^3.
$$

Voxel 内部 events 沿时间轴积分成 $\mathbf F_i\in\mathbb R^{H_v\times W_v}$，再 flatten 并经 MLP 得到 $\mathbf f_i\in\mathbb R^{D_f}$。该表示保留稀疏 voxel structure 和局部统计，但单个 voxel 内不再保留独立 temporal-bin axis；更细粒度 event ordering 会被压缩。Motion-sensitive sampling 的具体规则以及 $t_j^v$ 是 global normalized timestamp 还是 voxel-local timestamp：`Needs further check`。

### 4.2 MNEL：局部多尺度关系聚合

对中心 voxel $i$，MNEL 在三维坐标上使用 k-NN 搜索 $N_n$ 个邻居，并包含 self-loop。位置关系同时包含中心绝对坐标与相对偏移：

$$
\mathbf r_{ij}
=
\mathcal C(\mathbf c_i,\mathbf c_i-\mathbf c_{ij})
\in\mathbb R^6.
$$

邻居 feature 与 position relation 分别编码后再融合，生成 channel-wise relational weights。作者按距离构造 $S=3$ 个逐渐扩大的 neighborhood subspaces，并在每个尺度内将关系权重 softmax 后执行逐通道加权：

$$
\hat{\mathbf f}_i
=
\operatorname{MLP}
\left(
\sum_{k=1}^{S}
\sum_{j=1}^{kN_n/S}
\tilde{\mathbf f}_{ij}
\odot
\hat{\mathbf r}_{ijk}
\right).
$$

最后加入 residual projection：

$$
\mathbf l_i
=
\hat{\mathbf f}_i+\theta(\mathbf f_i).
$$

每个 MNEL 后使用 random sampling，voxel 数量按 $N_v\rightarrow UN_v\rightarrow U^2N_v\rightarrow U^3N_v$ 减少。被保留的 feature 已聚合上一层局部信息；下一层在更稀疏的 set 上仍搜索固定数量的 k-NN，通常需要覆盖更大的原始时空范围，因此有效 receptive field 逐层扩大。随机采样也可能丢弃关键稀疏模式；论文未报告其随机方差或与 importance/FPS sampling 的比较。

### 4.3 VSAL：全局 voxel interaction

三层 MNEL 后，VSAL 对剩余 voxels 执行 global self-attention。Absolute positional embedding 由坐标产生并加入 feature：

$$
\mathbf P
=
\operatorname{MLP}(\mathbf C),
\qquad
\{\mathbf Q,\mathbf K,\mathbf V\}
=
(\mathbf L+\mathbf P)
\{\mathbf W_q,\mathbf W_k,\mathbf W_v\}.
$$

同时，每个 ordered voxel pair 通过坐标关系生成 scalar relative position bias：

$$
B(i,j)
=
\phi\left(
\mathcal C(\mathbf c_i,\mathbf c_i-\mathbf c_j)
\right).
$$

最终：

$$
\mathbf A
=
\operatorname{softmax}
\left(
\frac{\mathbf Q\mathbf K^\top}{\sqrt D}
+
\mathbf B
\right)
\mathbf V,
\qquad
\tilde{\mathbf A}
=
\operatorname{MLP}(\mathbf A)+\mathbf L.
$$

Absolute position 同时影响 $Q/K/V$，relative bias 直接修正 pairwise attention logits。论文给出 $\mathbf Q,\mathbf K\in\mathbb R^{N\times(D/4)}$，但缩放项写为 $\sqrt D$，而标准 attention 通常使用 $\sqrt{D/4}$；这是有意设计还是记号问题：`Needs further check`。

### 4.4 S2TM：跨 segment 长程时间建模

长事件流被等时长切为 $\{\mathcal E_1,\ldots,\mathcal E_K\}$。共享 encoder 为每段输出：

$$
\hat{\mathbf A}_k
\in
\mathbb R^{U^3N_v\times D_a}.
$$

Mapping function 对 voxel dimension 分别执行 max pooling 和 average pooling，拼接后经 MLP 映射为 512-dimensional segment token。加入 learnable class token 与 trainable temporal positional embeddings 后，由一层 8-head Transformer encoder 建模：

$$
\left\{
\hat{\mathbf s}_{\mathrm{cls}},
\hat{\mathbf s}_1,
\ldots,
\hat{\mathbf s}_K
\right\}
=
h
\left(
\left\{
\mathbf s_{\mathrm{cls}},
\phi(\hat{\mathbf A}_1),
\ldots,
\phi(\hat{\mathbf A}_K)
\right\}
+
\mathbf P_t
\right).
$$

$\mathbf s_{\mathrm{cls}}$ 是 auxiliary learnable token；传播后的 $\hat{\mathbf s}_{\mathrm{cls}}$ 才是直接输入 FC classifier 的预测表示。S2TM 建模的是 segment-level dependency，不是 raw event-level continuous dynamics。

### 4.5 Architecture and Training

Object classification 的 encoder 使用三层 MNEL，输出维度为 64、64、128；$N_n=24$，$U=0.75$，两层 VSAL 的 feature dimension 为 128。训练 250 epochs，SGD momentum 为 0.9，batch size 为 32，cross-entropy loss，learning rate 由 $3\times10^{-2}$ cosine annealing 至 $10^{-6}$。

Action recognition 使用相同 encoder，S2TM token dimension 为 512，1-layer、8-head attention，每个 head 64 dimensions，FFN hidden dimension 为 1024。训练 300 epochs，batch size 为 16，learning rate 从 $10^{-2}$ 调整至 $10^{-7}$。Action setting 的 SGD momentum 未明确说明：`Needs further check`。

## 5. Experiments and Main Evidence

### 5.1 Object Classification

EVSTr 在 N-Caltech101、CIFAR10-DVS、N-Cars 和 ASL-DVS 上分别达到 $79.7\%$、$73.1\%$、$94.1\%$ 和 $99.7\%$。

- N-Caltech101：比 point-based VMV-GCN 高 $1.9$ 个百分点；
- CIFAR10-DVS：表中 point-based methods 最好；
- N-Cars：低于 EV-VGCNN 的 $95.3\%$，不是 point-based SOTA；
- ASL-DVS：与 ECSNet 的 $99.7\%$ 并列。

因此论文不支持“四个 object datasets 上全面 point-based SOTA”或 overall SOTA。与 ImageNet-pretrained dense models 相比，EVSTr 多数情况下是 competitive，而非整体最好；相较从头训练的 frame-based models，其结果更有优势。

N-Caltech101 上，EVSTr 为 0.93 M parameters、0.34 G MACs；MACs 为表中最低，但 parameters 不是最低。N-Cars 上 inference time 为 6.62 ms，低于多数方法但不是最快。这里的 efficiency evidence 是 model-level MACs、参数量和 RTX 3090 workstation runtime，不是 hardware-measured energy 或 neuromorphic deployment result。

### 5.2 Action Recognition

EVSTr 在 UCF101-DVS、HMDB51-DVS、DvsGesture、DailyAction 和 NeuroHAR 上分别达到 $73.5\%$、$60.7\%$、$98.6\%$、$99.6\%$ 和 $89.4\%$。

- 两个 converted datasets 上，EVSTr 是 point-based methods 最好，但不总能超过 pretrained frame models；
- DvsGesture 与 ECSNet 并列最好；
- DailyAction 和 NeuroHAR 为表中独立最好；
- NeuroHAR 上比第二名 TANet 高 $2.8$ 个百分点。

DailyAction 上 EVSTr 为 2.88 M parameters、1.38 G MACs、41 samples/s。VMV-GCN 更小、更快，但准确率明显较低；EVSTr 的结论应写为更好的 accuracy-complexity trade-off，而非全部效率指标最优。

### 5.3 Ablation and NeuroHAR Evidence

MNEL ablation 中，single-scale max pooling、multi-scale max pooling 和完整 MNEL 在 N-Caltech101 上分别为 $76.5\%$、$77.4\%$、$79.7\%$，支持 multi-scale 与 feature-position attentive aggregation 的增量价值。Point representation 降至 $62.8\%$；bilinear voxel integration 为 $79.8\%$，与 direct integration 基本相当，因此 direct integration 的主要理由是简化计算而非更高准确率。

VSAL 无位置编码时 N-Caltech101/DailyAction 为 $75.5\%/95.8\%$，absolute-relative combination 提升至 $79.7\%/99.6\%$。该实验支持二者互补，但“relative position 更适合非固定运动模式”仍是作者根据增益作出的解释。

无 S2TM 时，NeuroHAR 为 $80.9\%$；average pooling、LSTM、self-attention 分别为 $84.0\%$、$88.4\%$、$89.4\%$，说明复杂动作流更受益于 adaptive temporal modeling。NeuroHAR 包含 1584 samples、22 subjects、18 actions，以及 event/RGB/depth 三种 modalities；每类各有 $50\%$ camera-motion 和 $50\%$ low-light samples，采用 16-subject training、6-subject testing。

在同一 pretrained I3D 设置下，NeuroHAR 的 event modality 比 RGB 高 $6.2$ 个百分点、比 depth 高 $1.9$ 个百分点。该结论仅适用于当前数据集、模型和预处理，不能推广为 event modality 在所有任务中必然优于 frame modalities。

## 6. Strengths and Limitations

**Strengths**

- 从 event voxel representation、局部关系聚合、全局 interaction 到 segment temporal modeling，problem–module correspondence 清晰。
- MNEL 联合 absolute center position、relative offset 和 semantic feature，并通过多尺度 channel-wise attention 聚合邻居。
- VSAL 将 absolute embedding 与 directed relative bias 同时引入 sparse voxel attention。
- S2TM 通过共享 encoder 和轻量 Transformer 扩展到长时 action recognition，消融在 NeuroHAR 上显示明显增益。
- 在多个 object/action datasets 上取得较强 accuracy-complexity trade-off，并提供具有 camera motion、low light 和多模态数据的 NeuroHAR。

**Limitations**

- Voxel 内时间轴被积分为 2D patch，segment 再被 pooling 为单一 token，细粒度 temporal ordering 在两个阶段被压缩。
- 时间归一化到固定 $[0,T]$ 会弱化绝对 duration/speed information，论文未验证其影响。
- Random voxel sampling 不依赖内容重要性，可能丢失关键稀疏 events，且缺少稳定性分析。
- 公式（10）的 attention scaling、motion-sensitive sampling、timestamp reference、test-time random clipping 与 sampling reproducibility 均未充分说明。
- 多个结果仅为单次 accuracy，缺少 mean $\pm$ std；部分 train/test split 和 evaluation clips 为随机选择。
- t-SNE 仅是定性辅助证据；modality comparison 和跨架构 SOTA 对比同时混合了 representation、architecture 与 pretraining 差异。
- Efficiency 仅由 Params、MACs 和 GPU runtime 支持，不能直接等同于真实 energy efficiency 或 neuromorphic hardware advantage。

## 7. Relation to Other Papers and Survey Taxonomy

本文主要属于：

- **event representation**：sparse event voxel set；
- **point/set-based event processing**；
- **local spatiotemporal aggregation**：MNEL；
- **Transformer-based global modeling**：VSAL；
- **segment-level temporal modeling**：S2TM；
- **object classification and action recognition**；
- **efficiency and model complexity**；
- **event-based dataset construction**：NeuroHAR。

与 point-wise graph methods 相比，EVSTr 先在 voxel 内整合局部 events，以提高统计稳定性；与 dense frame Transformers 相比，它只处理 selected non-empty voxels；与 SNN 方法相比，它不使用 neuron dynamics，而依靠显式 timestamp/coordinate、set aggregation 和 Transformer attention 建模时间。它不属于 spike coding、SNN training、ANN-to-SNN conversion 或 neuromorphic hardware deployment。

## 8. Survey-Usable Takeaways

1. EVSTr 展示了稀疏 event recognition 的三级建模结构：voxel-level local aggregation、voxel-set global interaction 和 segment-level long-range temporal modeling。
2. Voxelization 能在 point-level noise robustness 与 dense-frame redundancy 之间提供折中，但会压缩 voxel 内细粒度 event ordering。
3. MNEL 的贡献不只是 multi-scale k-NN，而是将 semantic feature 与 absolute-relative position 联合映射为 channel-wise neighbor attention。
4. S2TM 的时间语义是 inter-segment dependency，不应描述为 event-by-event 或 SNN-style temporal dynamics。
5. 实验支持 EVSTr 在 N-Caltech101、CIFAR10-DVS、DailyAction 和 NeuroHAR 的相应比较范围内表现突出；N-Cars 不是 point-based SOTA，DvsGesture 和 ASL-DVS 属于并列最好。
6. 论文的效率结论应限定为低 MACs、较小模型和 GPU inference throughput，不能转写为真实 energy 或 neuromorphic hardware efficiency。
7. 对 SNN survey 而言，EVSTr 最适合作为 non-spiking sparse Transformer baseline，用于比较显式时空坐标建模与 neuronal temporal dynamics 的差别。

## Supplement Points

### Questions and Clarifications

#### 1. 为什么每个 MNEL 后进行 random sampling，会降低 voxel density 并扩大 receptive field？

MNEL 首先将每个 voxel 与其局部 k-NN neighbors 聚合，因此采样前的 voxel feature 已经包含周围区域的信息。Random sampling 随后只保留一部分 voxel nodes：

$$
N_v
\rightarrow
UN_v
\rightarrow
U^2N_v
\rightarrow
U^3N_v.
$$

它不会重新定义更大的 voxel，也不是对相邻 voxels 做平均，而是减少后续 set 中的节点数量和对应计算。在更稀疏的 set 上，下一层仍搜索固定数量 $N_n$ 的最近邻；为了找到足够多的 neighbors，典型搜索距离会增大。与此同时，每个被搜索到的 feature 已代表上一层的局部区域，因此更深层聚合的是“邻域的邻域”。

其有效 receptive field 扩大来自两方面：

1. 节点密度下降后，固定数量 k-NN 通常覆盖更大的原始 $x$-$y$-$t$ 范围；
2. 层次化 feature 已递归包含前一层邻居信息。

Random sampling 同时降低后续 MNEL 和 $N\times N$ self-attention 的计算量，但可能丢失关键稀疏模式。论文没有报告 sampling variance、test-time 固定策略或与 FPS/importance sampling 的对比：`Needs further check`。

### Additional Technical Details

#### 1. 公式（2）：voxel 内 direct timestamp-polarity integration

第 $i$ 个 voxel 覆盖 $H_v\times W_v\times T_v$，内部 events 为：

$$
\left\{
(x_j^v,y_j^v,t_j^v,p_j^v)
\right\}_{j=1}^{M_v}.
$$

作者沿时间轴把它压缩为 2D patch $\mathbf F_i\in\mathbb R^{H_v\times W_v}$：

$$
F_i(x,y)
=
\sum_{j=1}^{M_v}
\delta(x-x_j^v,y-y_j^v)
p_j^v t_j^v,
$$

$$
\delta(a,b)
=
\begin{cases}
1, & a=0\ \text{且}\ b=0,\\
0, & \text{其他情况}.
\end{cases}
$$

Kronecker delta 只选择 voxel 内位于同一空间位置 $(x,y)$ 的 events，因此等价于：

$$
F_i(x,y)
=
\sum_{\substack{j:\\x_j^v=x,\,y_j^v=y}}
p_j^v t_j^v.
$$

每个 event 的贡献是 polarity 与 timestamp 的乘积。较晚 event 的绝对权重通常更大，正负 polarity 可相互抵消；因此 $F_i(x,y)=0$ 不一定表示该位置没有 event，也可能表示加权和恰好为零。

例如，同一位置发生 $(t,p)=(0.2,+1)$、$(0.6,+1)$ 和 $(0.8,-1)$，则：

$$
F_i(x,y)
=
0.2+0.6-0.8
=
0.
$$

该操作将 $H_v\times W_v\times T_v$ 的局部 event structure 压缩成 $H_v\times W_v$ continuous-valued patch，随后 flatten 并经 MLP 产生 voxel feature。论文未明确 $t_j^v$ 是整个 normalized stream 的 global timestamp，还是减去 voxel 起始时间后的 local timestamp：`Needs further check`。
