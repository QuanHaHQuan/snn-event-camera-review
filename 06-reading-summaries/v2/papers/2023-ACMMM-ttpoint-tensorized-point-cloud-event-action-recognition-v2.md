---
tags: ["event camera", "point cloud", "TTPOINT", "tensor-train decomposition", "subwindow sampling", "action recognition", "lightweight model", "non-SNN baseline"]
---

# Summary V2｜TTPOINT: A Tensorized Point Cloud Network for Lightweight Action Recognition with Event Cameras

## 1. Core Understanding

TTPOINT 是一种面向 event-camera action recognition 的轻量化 point cloud network。它将 event stream 直接表示为空间—时间点集，通过 subwindow sampling 保证时间覆盖，再利用 hierarchical LocalTTRes / GlobalTTRes 提取局部与全局几何特征，并用 Tensor-Train Decomposition 压缩 residual MLP。

本文不是 SNN 方法：没有 spiking neuron、membrane dynamics、surrogate gradient 或 spike-driven computation。在综述中，它属于 event-camera point-cloud representation 与 lightweight non-spiking baseline 路线。

## 2. Problem and Motivation

Frame-based 方法通常将一段 events 累积成 event frame、density map 或 temporal surface，再输入 CNN。这样便于利用成熟视觉网络，但会提高数据密度、压缩细粒度时间信息，并可能引入事件聚合延迟。

Point-based 方法则可将每个 event 直接视为空间—时间点，保留输入的稀疏性。然而，实际网络通常只从大量 events 中采样约 0.1%–1% 的点。由于快速运动产生高密度 events、慢速运动产生低密度 events，直接 random sampling 容易被高密度时段主导，遗漏低密度但具有动作判别力的片段。与此同时，普通 PointNet++ 类网络中的 MLP 仍可能带来较多参数。

TTPOINT 因此同时解决两个问题：通过 subwindow sampling 改善时间覆盖，通过 tensorized MLP 降低 hierarchical point network 的模型规模。

## 3. Method Overview

原始 event 为：

$$
e_m=(x_m,y_m,t_m,p_m)
$$

TTPOINT 将其转换为空间—时间点：

$$
e_m=(x_m,y_m,z_m)
$$

其中：

$$
z_m=
\frac{t_m-t_1}{t_n-t_1}
$$

坐标均被归一化至 `[0,1]`。这里的第三维不是物理深度，而是 sliding window 内的相对时间；原始 polarity 没有被显式保留。

每个动作序列先被切为 fixed-length sliding windows；每个 window 再被分成多个 subwindows，并从每个 subwindow 中采样相同数量的点，最终拼成：

$$
\mathrm{clip}_{sample}
\in
\mathbb{R}^{1\times1024\times3}
$$

加入 batch 后，输入为：

$$
S_0\in\mathbb{R}^{B\times1024\times3}
$$

随后经过四个 hierarchical stages：

$$
P_i=
\operatorname{Max}
\left(
\operatorname{LocalTTRes}(S_{i-1})
\right)
$$

$$
S_i=
\operatorname{GlobalTTRes}(P_i)
$$

最终特征送入 MLP classifier 输出动作类别。

## 4. Key Components and Mechanisms

### 4.1 Event Point Cloud and Subwindow Sampling

点云本质上是无序点集，不要求第三个坐标必须是真实深度。TTPOINT 把时间映射为第三个几何轴，因此一个动作片段形成 `x-y-t` point cloud。

Subwindow sampling 与 FPS 作用不同。前者发生在输入预处理阶段：将一个 sliding window 分成多个时间子段，再为各子段分配相同采样配额，以防随机采样只集中在快速运动区。Figure 4 的 air-drums 示例显示，该策略能使慢运动时段获得更多代表点。

但 subwindow 并非越细越好；过多子窗口会限制高密度、信息丰富片段的采样数量。其最优长度依赖动作速度和数据分布，属于 dataset-sensitive preprocessing。

### 4.2 Hierarchical Local and Global Extraction

LocalTTRes 首先通过 Farthest Point Sampling 选择分布较均匀的 centroids，再用 KNN 为每个 centroid 构造局部邻域。论文设置每组邻居数为 `N=24`。若输入为：

$$
[B,S,D]
$$

FPS 选取：

$$
S'=\frac{S}{2}
$$

个中心点，grouping 后的局部张量可理解为：

$$
[B,S',N,D]
$$

LocalTTRes 对每个邻域内的点特征进行 residual MLP/TTLayer 变换，再沿邻居维进行 max pooling，得到每个中心点的局部几何表示。

GlobalTTRes 进一步综合这些 group features，扩大 feature dimension 并提取更高级的整体动作特征。Figure 3 给出的整体 stage 变化为点或 group 数减少、feature dimension 增加，概念上对应：

$$
S'=\frac{S}{2},
\qquad
D'=2D
$$

论文未完整列出四个 stage 的全部精确张量尺寸，因此维度扩展具体发生在 LocalTTRes 还是 GlobalTTRes 内部，`Needs further check`。消融表明 local extractor 是主体：only-local、only-global 和二者结合的 sliding-window accuracy 分别为 96.19%、90.2% 和 97.78%。

### 4.3 Tensor-Train Compressed Residual Extractor

普通 residual extractor 使用：

$$
M(x)=BN(MLP(x))
$$

$$
Res=
F\left(
x+M(F(M(x)))
\right)
$$

TTPOINT 将其中的大型 MLP 替换为 TTLayer：

$$
T(x)=BN(TTLayer(x))
$$

$$
TTRes=
F\left(
x+T(F(T(x)))
\right)
$$

TTD 将原权重矩阵重排为高阶 tensor，并用一串小 tensor cores 的乘积近似。其参数量由完整矩阵的输入—输出维度乘积，变为各 tensor core 参数量之和。TT-rank 控制相邻 cores 之间的信息通道：rank 较小意味着压缩更强但表达能力更弱。

本文报告 TTD 将参数减少约 55%，使模型约为 0.334M parameters，并将计算量降低至 0.587 GFLOPs；但 FLOPs 的下降幅度小于参数下降幅度，说明 tensorized contraction 本身仍包含额外运算。

## 5. Experiments and Main Evidence

实验覆盖 Daily DVS、DVS128 Gesture、DVS Action、HMDB51-DVS 和 UCF101-DVS。TTPOINT 分别达到 99.1%、98.8%、92.7%、56.9% 和 72.5% accuracy，模型约为 0.334M–0.357M parameters、0.587 GFLOPs。它在五个数据集上均属于较强 point-based method，但并非所有数据集的 overall SOTA，例如 DVS128 Gesture 和 UCF101-DVS 上仍有更高的 frame/recurrent baselines。

Subwindow sampling 在 DVS128 Gesture 上将 accuracy 从 97.0% 提高至 97.8%，在 DVS Action 上从 87.5% 提高至 92.7%；但继续缩短 subwindow 后性能回落。Compression ablation 表明，TTPOINT 在 Daily DVS、DVS Action 和 DVS128 Gesture 上接近或略优于 uncompressed model，可能具有 regularization 效果；在 HMDB51-DVS 上则从 59.0% 降至 56.9%，更强压缩的 TTPOINT-tiny 进一步降至 54.5%，说明复杂任务可能出现 underfitting。

论文只报告 parameters 与 GFLOPs，没有真实 edge-device latency、功耗或能量测量；0.587 GFLOPs 是否包括 FPS、KNN、grouping 和 preprocessing 也未明确。

## 6. Strengths and Limitations

**Strengths**

* 直接处理 sparse event point cloud，避免完整 dense-frame conversion。
* Subwindow sampling 针对 event density 随运动速度变化这一实际问题。
* Local/global hierarchy 同时保留局部时空几何和高层动作表示。
* TTD 被用于明确的 MLP compression，而非仅作为附加模块。
* 在极小参数规模下覆盖五个 action-recognition benchmarks。

**Limitations / Questions**

* 不是 SNN，不能用于证明 spiking computation 的能效优势。
* `(x,y,t,p)` 被简化为 `(x,y,z)`，polarity 未显式利用。
* Sliding-window 和 subwindow length 对结果影响明显。
* DVS Action 使用 denoising 和从序列后半段开始采样等 dataset-specific heuristic。
* 过强 TTD compression 会在复杂数据集上削弱表示能力。
* 论文对 TT-rank vector 与 width-dependent rank configuration 的符号说明不够清晰。
* 轻量化证据限于 params/GFLOPs，未验证实际硬件部署。

## 7. Relation to Other Papers and Survey Taxonomy

TTPOINT 继承 PointNet、PointNet++ 和 PointMLP 的 hierarchical point-cloud processing 思路。与 ST-EVNet 和 PAT 相比，它更强调时间均衡采样与 tensorized model compression，而不是 self-attention 或复杂 subset selection。

在 “Spiking Neural Networks for Event Cameras” 综述中，它应归入：

* event stream as point cloud；
* non-spiking sparse event processing；
* event-based action recognition；
* sampling strategy；
* tensor decomposition and model compression；
* lightweight ANN baseline。

它的重要性在于说明：即使不使用 SNN，point-based ANN 也可达到极小参数规模，因此评估 SNN efficiency 时不能只与大型 frame-based CNN 对比。

### PDF-verified relation backfill

主要路线是 time-balanced sampled Event Cloud + hierarchical point MLP，并以 tensor-train decomposition 压缩 action-recognition network。

- **PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space (Charles Ruizhongtai Qi et al., NeurIPS 2017)** — `foundation`。该工作提供 hierarchical point processing 的基础机制；当前论文将其用于自身的 event/SNN pipeline，而不是把该前驱本身作为新贡献。 对应 Sections 2 and 6: representation and efficiency。证据：Related Work 2, PDF pp.2-3, citation and bibliography [24]。 当前 active corpus 未覆盖。
- **Modeling Point Clouds with Self-Attention and Gumbel Subset Sampling (Jiancheng Yang et al., CVPR 2019)** — `alternative`。两者都处理 point sampling and attention，但采用不同 representation、state 或 computation route。 对应 Sections 2 and 5: representation and action recognition。证据：Related Work 2, PDF p.3, citation and bibliography [33]。 当前 active corpus 未覆盖。
- **Space-Time Event Clouds for Gesture Recognition: From RGB Cameras to Event Cameras (Qinyi Wang et al., WACV 2019)** — `baseline`。该工作是 Event Cloud recognition 的实验 comparator；当前论文与其主要区别在于本文第 3–4 节所述的核心机制。 对应 Sections 2 and 5: representation and action recognition。证据：Related Work, PDF p.2, citation and bibliography [29]。 当前 active corpus 未覆盖。 值得 backward search。

## 8. Survey-Usable Takeaways

* Takeaway 1: Event stream 可以将时间视为第三个坐标，直接构成 sparse `x-y-t` point cloud，而无需先生成 dense event frames。
* Takeaway 2: Event-point sampling 不只是降低点数；它决定哪些运动阶段能够进入网络，random sampling 可能忽略低事件密度的慢动作。
* Takeaway 3: Local geometry extraction 是 point-based action recognition 的关键，global extractor主要提供补充性提升。
* Takeaway 4: Tensor-train compression 能显著降低 MLP 参数，但 rank 过小会在复杂数据集上造成 underfitting。
* Takeaway 5: TTPOINT 是 non-SNN lightweight baseline，其 params/GFLOPs 结果不能等价为真实 latency 或 energy efficiency。

## Supplement Points

### 1. Frame-based 方法中的 Frequency、SAE 和 LIF

Figure 2 将 Frequency、SAE 和 LIF 作为 event-to-frame coding examples，但正文未给出其完整公式。

**Frequency representation** 通常在一个时间窗口内统计每个像素的 event 次数：

$$
F(x,y)
=

\sum_k
\mathbf{1}
\left[
(x_k,y_k)=(x,y)
\right]
$$

它主要保存 event density；若正负 polarity 分通道，则可生成两个 count maps。其缺点是窗口内事件先后顺序基本丢失。

**SAE，Surface of Active Events** 为每个像素保存最近一次 event 的 timestamp：

$$
SAE(x,y)=t_{\mathrm{last}}(x,y)
$$

实际使用时常将 timestamp 转成时间衰减 surface，例如越新的 event 值越大。它比简单 frequency map 更能表达最近运动轮廓，但通常只保留每个像素的最后事件或衰减状态。

**LIF coding** 在该图中应理解为受 Leaky Integrate-and-Fire 动态启发的 event accumulation：新 event 提高像素状态，状态随时间泄漏或衰减，达到条件后形成 frame-like response。这里的 LIF 是一种 event coding / temporal accumulation 思路，不表示 TTPOINT 本身使用 SNN。论文没有给出对应实现公式，具体编码方式需核查其引用文献：

`Needs further check`

### 2. Point Cloud：不带属性与带属性

一个不带显式属性的点云通常写成：

$$
P\in\mathbb{R}^{N\times3}
$$

每个点只有坐标：

$$
(x,y,z)
$$

带属性点云则可写为：

$$
P\in\mathbb{R}^{N\times(3+C)}
$$

其中额外的 `C` 维可以是颜色、法向量、强度、polarity、event count 或 learned feature。

TTPOINT 的输入是：

$$
\mathrm{clip}_{sample}
\in
\mathbb{R}^{1\times1024\times3}
$$

因此它将归一化后的 `(x,y,z)` 作为点坐标，没有把 polarity 作为第四维属性输入。这里的 `z` 是相对时间，而不是真实深度。

### 3. 从固定点云输入到 Hierarchical Feature 的维度变化

初始输入：

$$
S_0\in\mathbb{R}^{B\times S\times D}
$$

本文起点为：

$$
S=1024,
\qquad
D=3
$$

即：

$$
S_0\in\mathbb{R}^{B\times1024\times3}
$$

一个 stage 可按下列步骤理解。

#### 第一步：FPS 选择中心点

从 `S` 个点中选出：

$$
S'=\frac{S}{2}
$$

个 centroids。FPS 每次选择离当前已选集合最远的点：

$$
q^*
===

\arg\max_q
\min_{c\in\mathcal C}
\lVert q-c\rVert_2
$$

它使中心点在 `x-y-t` 空间中分布较均匀，但只考虑几何覆盖，不考虑语义重要性。

#### 第二步：KNN Grouping

为每个 centroid 搜索 `N=24` 个邻居，形成：

$$
G_i
\in
\mathbb{R}^{B\times S'\times N\times D}
$$

论文 Figure 3 将轴顺序画作 `[B,N,S',D]`，二者只是张量排列方式不同。

#### 第三步：LocalTTRes

TTLayer 对每个邻居的特征进行变换，得到：

$$
\widetilde{G}_i
\in
\mathbb{R}^{B\times S'\times N\times D'}
$$

再沿 `N` 个邻居执行 max pooling：

$$
P_i
===

\max_{n=1,\ldots,N}
\widetilde{G}_i
\in
\mathbb{R}^{B\times S'\times D'}
$$

这样一个邻域被压缩成一个 centroid feature。

#### 第四步：GlobalTTRes

GlobalTTRes 在所有 centroid features 上继续执行 residual feature transformation，输出：

$$
S_i
\in
\mathbb{R}^{B\times S'\times D'}
$$

Figure 3 给出的整体 stage 设计为：

$$
S'=\frac{S}{2},
\qquad
D'=2D
$$

例如概念上可写为：

```text
[B,1024,3]
→ [B,512,6]
→ [B,256,12]
→ ...
```

但论文没有完整列出真实各 stage 的 feature widths，因此该数值链只能用于理解“点数下降、维度上升”的原则，不能视为实现中的确切尺寸。Figure 3 最终画出一个 `256×1` representation，说明 stage 输出还会经过全局聚合形成固定长度分类向量。

### 4. LocalRes 与 GlobalRes 的计算区别

普通 residual MLP 为：

$$
M(x)=BN(MLP(x))
$$

$$
Res=
F
\left(
x+M(F(M(x)))
\right)
$$

LocalRes 将该 residual transformation 应用于每个 centroid 的局部邻域，随后通过邻域 max pooling 提取 local geometry。

GlobalRes 接收已经池化的 centroid features，不再针对单个邻域内部做 max pooling，而是进一步组合、升维和抽象各局部区域之间的关系。

因此：

* LocalRes 回答“这个局部时空邻域是什么形状”；
* GlobalRes 回答“多个局部动作片段组合起来是什么动作”。

实验中 only-global 明显弱于 only-local，说明直接处理单点或全局信息而缺少 local geometry 会损失关键结构。

### 5. Tensor-Train Decomposition 的具体例子

普通 MLP 中最昂贵的部分是：

$$
Y=WX+B
$$

假设：

$$
W\in\mathbb{R}^{256\times64}
$$

原矩阵共有：

$$
256\times64=16384
$$

个权重。

作者将输出维度拆为：

$$
256=4\times4\times4\times4
$$

输入维度拆为：

$$
64=4\times4\times2\times2
$$

因此一个权重位置不再由单一二维索引表示，而是由四组输入—输出索引表示：

$$
(o_1,p_1),
(o_2,p_2),
(o_3,p_3),
(o_4,p_4)
$$

对应权重由四个 tensor cores 的矩阵乘积近似：

$$
W
\big(
(o_1,p_1),\ldots,(o_4,p_4)
\big)
\approx
G_1(o_1,p_1)
G_2(o_2,p_2)
G_3(o_3,p_3)
G_4(o_4,p_4)
$$

每个 core 的形状为：

$$
G_m
\in
\mathbb{R}^{
r_{m-1}\times o_m\times p_m\times r_m
}
$$

原来的 16384 个独立参数被替换为：

$$
\sum_{m=1}^{4}
r_{m-1}o_mp_mr_m
$$

个参数。Rank 越小，中间矩阵越窄，参数越少；但它限制了不同 tensor dimensions 之间可传递的信息量。

### 6. Rank 8、Rank 4 是否手动设置？

是结构超参数，由作者人工设定，而不是普通反向传播自动决定。论文明确表示这些 rank configurations 是根据经验设置的。标准 TTPOINT 使用较大的 rank，TTPOINT-tiny 将 rank 降为 4，以获得更强压缩和最高约 53 的 compression ratio。

训练过程会学习 tensor cores 内的参数，但不会自动改变预先设定的 core shapes 或 TT-ranks。其作用类似于选择 CNN 的 channel width：

* rank 大：容量更强，参数更多；
* rank 小：压缩更强，可能 underfit。

### 7. `r_m`、`l_m`、`o_m` 和 `p_m` 的区别

严格定义如下。

原高阶 tensor 的第 `m` 个物理维度是：

$$
l_m
$$

作者将其拆为：

$$
l_m=o_mp_m
$$

其中：

* `o_m` 是输出维度的分解因子；
* `p_m` 是输入维度的分解因子。

相邻 tensor cores 的连接维度是：

$$
r_m
$$

这才是严格意义上的 TT-rank。

因此：

$$
G_m
\in
\mathbb{R}^{
r_{m-1}\times o_m\times p_m\times r_m
}
$$

论文的例子中：

$$
[o_m]=[4,4,4,4]
$$

$$
[p_m]=[4,4,2,2]
$$

它们是 input/output tensorization factors，不是 rank。

论文实验设置又写到不同 MLP widths 对应 `[8,8,4,4]`、`[8,4,4,4]` 等 “rank” 配置。根据上下文，这些更可能是不同 TTLayer 的 internal rank vectors，而不是 `l_m`；但正文没有给出边界 rank、core 数量和程序参数的完整映射，而且部分列表长度不同，因此无法仅凭论文完全确认：

`Needs further check against code`

### 8. Efficiency Evidence Boundary

TTPOINT 证明的是：

* parameter count 较低；
* theoretical GFLOPs 较低；
* point-based sparse representation 有较强 accuracy–complexity trade-off。

它没有证明：

* ARM/MCU 上的真实 latency；
* 实际 energy per inference；
* FPS、KNN、grouping 在硬件上的完整开销；
* tensorized kernels 在目标设备上的利用效率。

因此，在 SNN 综述中应将 TTPOINT 视为重要的 non-spiking lightweight comparator：SNN 方法若声称高效，除了与大型 CNN 比较，也应与这类约 0.33M 参数的 sparse ANN 对照。
