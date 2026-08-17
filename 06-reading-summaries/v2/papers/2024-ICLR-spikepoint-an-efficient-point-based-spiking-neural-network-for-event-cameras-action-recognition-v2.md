---
tags: [event-camera, spiking-neural-network, point-cloud, action-recognition, ICLR-2024]
---

# Summary V2｜SpikePoint: An Efficient Point-Based Spiking Neural Network for Event Cameras Action Recognition

## 1. Core Understanding

SpikePoint 面向 event-based action recognition，目标是在不生成 event frames/voxels 的情况下，将 event stream 表示为稀疏 $(x,y,t)$ pseudo-Point Cloud，再用直接训练的 point-based SNN 分类。它的核心不是单纯“把 PointNet 换成 SNN”，而是同时改造输入编码、point architecture 和 residual training：

1. 在固定时间窗口中随机采样 events，将 $x,y$ 与 relative timestamp $z$ 归一化为 point coordinates；
2. 用 FPS 和 KNN 构造一次局部 grouping，而不是重复多层 set abstraction；
3. 将带符号 relative coordinates 改造成适合 Bernoulli/Poisson rate coding 的非负 features，并用 centroid branch 补偿方向信息损失；
4. 以 local extractor 建模 group 内结构，以 global extractor 建模 groups 之间的动作结构；
5. 将 residual connection 移到 LIF 之后，为 BPTT 提供不经过 surrogate derivative 的 identity gradient path。

完整路径是：

$$
\text{raw events}
\rightarrow
\text{windowed }(x,y,z)\text{ points}
\rightarrow
\text{FPS/KNN groups}
\rightarrow
\text{rate-coded coordinate spikes}
\rightarrow
\text{local/global spiking extractor}
\rightarrow
\text{spiking classifier and voting}.
$$

网络使用 SpikingJelly ParametricLIF、$T=16$、ATan surrogate gradient 和 BPTT，从头直接训练，不是 ANN-to-SNN conversion。但 preprocessing 中的 windowing、random sampling、FPS、KNN、normalization 和 random rate encoding 都是同步的非神经计算；post-LIF residual addition 还可能产生值 2。因此本文的“full spike/end-to-end”应限定为 feature extractor 与 classifier 的 SNN 主体，不能等同于逐 raw event、完全异步、全程 binary 的 neuromorphic implementation。

## 2. Problem and Motivation

Event camera 输出稀疏、异步且具有高时间分辨率的事件，但已有 event-camera SNN 往往先生成 frames，增加映射开销并削弱稀疏性与细粒度时间信息。Point Cloud 可以把事件的空间坐标与时间组织为稀疏点集，却通常依赖 ANN 中反复 sampling/grouping 的 hierarchical architecture；作者认为深层 stage 会使 spike features 更稀疏、难以区分，并加重 BPTT 的梯度问题。

SpikePoint 因此试图解决两个耦合问题：一是直接在 point representation 上利用事件的稀疏时空结构；二是设计适合 rate-coded spikes 和 surrogate training 的轻量 Point Cloud SNN。

## 3. Method Overview

### 3.1 Event clip 与 pseudo-Point Cloud

单个 raw event 为：

$$
e_m=(x_m,y_m,t_m,p_m).
$$

每段 recording 被切成长度为 $L$ 的 clips：

$$
AR_{\mathrm{clip}}
=
\operatorname{clip}_i\{e_k,\ldots,e_l\},
\qquad
t_l-t_k=L.
$$

窗口长度并不统一：DVS128 Gesture 与 DVS Action 为 $0.5\ \mathrm{s}$，Daily DVS 为 $1.5\ \mathrm{s}$，HMDB51-DVS 为 $0.5\ \mathrm{s}$，UCF101-DVS 为 $1\ \mathrm{s}$；相邻窗口 overlap 分别为 $0.25/0.25/0.5/0.5/0.5\ \mathrm{s}$。Daily DVS 用 $0.5\ \mathrm{s}$ 时只有约 $80\%$，调至接近平均动作长度的 $1.5\ \mathrm{s}$ 后才取得最终结果，说明性能明显依赖人工 window selection。

窗口内 timestamp 被变成 relative coordinate：

$$
z_m
=
\frac{t_m-t_k}{t_l-t_k},
$$

同时 $x_m,y_m$ 按 sensor resolution 归一化到 $[0,1]$。模型丢弃 polarity $p_m$，得到：

$$
AR_{\mathrm{point}}
=
\{(x_m,y_m,z_m)\mid m=k,\ldots,l\}.
$$

Random sampling 将 variable event count 变成固定 point set。Appendix 给出 `Number of Points = 1024`，但正文没有说明 event 数少于 1024 时如何补齐，也没有说明采样是否在 recording-level train/test split 之后执行。由于 windows 高度重叠且 test clips 是总 samples 中随机抽取的 20%，若先生成 clips 再随机划分，相邻重叠内容可能跨 split；实际顺序需要代码确认。

### 3.2 FPS/KNN grouping 与符号冲突

对 sampled point set $P^N$，FPS 选择 centroids，KNN 构造 neighborhoods：

$$
\mathrm{Centroid}=\operatorname{FPS}(P^N),
$$

$$
G=\operatorname{KNN}(P^N,\mathrm{Centroid},N').
$$

正文称输入从 $[N,3]$ 变为 $[N',M,3]$，并定义 $M$ 为 group 数、$N'$ 为每组 points；Appendix A.3 又把实际 input 写成 $[N',M,6]=[1024,24,6]$；Figure 8 则清楚显示 1024 个 group-level branches、每组 24 points。可确认的实际运算是 **1024 个 neighborhoods，每个 neighborhood 含 24 个 points**，但 $N,N',M$ 的正式符号在正文、附录和 figure legend 中互换，不能可靠沿用。

每个 neighbor 相对 centroid 标准化：

$$
[\Delta x,\Delta y,\Delta z]
=
\frac{G-\mathrm{Centroid}}{\operatorname{SD}(G)},
$$

$$
\operatorname{SD}(G)
=
\sqrt{
\frac{\sum_{i=1}^{n}(g_i-\bar g)^2}{n-1}
}.
$$

作者将标准化后分布近似为 $\mathcal N(0,1)$，但 Appendix A.1 也承认 FPS/KNN 产生的几何 points 不一定服从 Gaussian，standardization 只保证中心和尺度，不保证正态性。

### 3.3 从 signed coordinates 到可 rate-code 的双分支输入

Bernoulli rate encoder 要求输入可解释为 $[0,1]$ probability，而 $\Delta x,\Delta y,\Delta z$ 有正有负。直接 min-max normalization 会让距 centroid 相同但方向相反的 points 获得不对称编码，因此作者改用 absolute values：

$$
[\Delta|x|,\Delta|y|,\Delta|z|].
$$

若标准化 coordinate 近似 $\mathcal N(0,1)$，取绝对值后成为 folded normal，其均值从 0 移到：

$$
\mathbb E[|\Delta|]
=
\sqrt{\frac{2}{\pi}}
\approx0.798.
$$

Absolute value 解决负 probability，却丢失方向，并使 relative part 整体变大。作者不采用精确的 expectation correction $c-\sqrt{2/\pi}\operatorname{SD}$，而是构造两个 branches：

$$
X_1
=
[\Delta|x|,\Delta|y|,\Delta|z|,x_{\min},y_{\min},z_{\min}],
$$

$$
X_2
=
[x_c,y_c,z_c].
$$

$X_1$ 用 group minimum coordinates 在数值上补偿 absolute relative coordinates 的正向偏移；$X_2$ 独立保留真实 centroid，弥补 $x_{\min},y_{\min},z_{\min}$ 不能代表中心的问题。两条 branch 的 features 在 local extractor 中相加。这里的补偿只恢复 group-level boundary/center 信息，无法恢复每个 neighbor 原来的正负方向。

所有连续 coordinate channels 随后由 stateless Poisson encoder 转成 $T=16$ 的 spike sequence：

$$
s_v[t]\sim\operatorname{Bernoulli}(v),
\qquad
t=1,\ldots,T.
$$

因此 network input 的时间轴不是 raw event timestamp 轴，而是对同一 point coordinates 重复 16 次随机采样得到的 simulation axis。标准化后的 $\Delta|d|$ 可能大于 1，论文未说明 clipping 或 renormalization；这对合法 Bernoulli probability 至关重要。

### 3.4 Singular-stage local/global extractor 的完整 shape flow

SpikePoint 只做一次 FPS/KNN grouping，随后保持 1024 个 group-level features，用 shared Conv1D 和 spiking residual blocks 升维。省略代码中未知的 axis order 后，加入 batch 和 SNN timestep 的概念 shapes 如下：

| Step | Small model | Large model | 作用 |
| --- | --- | --- | --- |
| Main rate-coded input $X_1$ | $[B,T,1024,24,6]$ | 相同 | 24 个 neighbors 的 absolute-relative + minimum coordinates |
| Centroid input $X_2$ | $[B,T,1024,3]$ | 相同 | 每个 neighborhood 的真实 centroid |
| Main Conv1D + $\operatorname{ResF}_B$ | $[B,T,1024,24,32]$ | $[B,T,1024,24,64]$ | point-level local features |
| Neighbor MaxPool | $[B,T,1024,32]$ | $[B,T,1024,64]$ | 消去 24-point axis |
| Centroid Conv1D + $\operatorname{ResF}_B$ | $[B,T,1024,32]$ | $[B,T,1024,64]$ | centroid feature |
| Add fusion | $[B,T,1024,32]$ | $[B,T,1024,64]$ | local group descriptors |
| Global block 1 | $32\rightarrow64$ | $64\rightarrow128$ | group-to-group feature abstraction |
| Global block 2 | $64\rightarrow128$ | $128\rightarrow256$ | further abstraction |
| Final Conv1D | $128\rightarrow256$ | $256\rightarrow512$ | classifier width |
| Global MaxPool over 1024 groups | $[B,T,256]$ | $[B,T,512]$ | one descriptor per SNN timestep |
| Spike MLP | $256\rightarrow256\rightarrow10C$ | $512\rightarrow512\rightarrow10C$ | class voting neurons |

Small model 用于 Daily DVS、DVS Action；large model 用于 DVS128 Gesture、HMDB51-DVS、UCF101-DVS。每个 Conv1D 后接 BatchNorm。$\operatorname{ResF}_B$ 的 bottleneck width 是输入的一半，并保持 block 外部 channels 不变；global $\operatorname{ResF}$ 不使用 bottleneck。Figure 8 画出 dropout 0.5，而 Appendix A.7.1 又称 extractor 与 classifier 之间的 dropout 被省略，具体 placement 存在文字/图示不一致。

### 3.5 PLIF dynamics、post-LIF residual 与训练

正文先用带 synaptic-current state 的 generic LIF 描述：

$$
I[n]
=
e^{-\Delta t/\tau_{\mathrm{syn}}}I[n-1]
+
\sum_jW_jS_j[n],
$$

$$
U[n+1]
=
e^{-\Delta t/\tau_{\mathrm{mem}}}U[n]
+I[n]-S[n].
$$

实际实现使用 SpikingJelly ParametricLIF，learnable $\tau$ 初始为 2.0，`no decay input`，binary threshold 的 backward derivative 使用 ATan surrogate：

$$
\sigma(x)
=
\frac{1}{\pi}\arctan(\pi x)+\frac12,
\qquad
\sigma'(x)
=
\frac{1}{1+(\pi x)^2}.
$$

Residual 从 pre-LIF：

$$
S^l=\operatorname{LIF}(I+S^{l-1})
$$

改成 post-LIF：

$$
S^l=\operatorname{LIF}(I)+S^{l-1}.
$$

原 residual path 必须乘 $\sigma'(\cdot)$；新 identity branch 对 $S^{l-1}$ 的 derivative 为 1，因而缓解 surrogate-gradient vanishing。主分支依然需要 surrogate gradient，网络整体也没有由此获得“不消失梯度”的保证。更重要的是，若两项都是 binary，则相加结果属于 $\{0,1,2\}$；论文没有说明后续 Conv1D 将它视为 multi-bit spike count、integer activation 还是其他 state。因此“binary spike throughout”并不成立。

训练使用 Adam、initial learning rate $10^{-3}$、cosine scheduler、最多 300 epochs，batch size 为 6 或 12，$T=16$。论文未列明各数据集具体 batch size、weight decay、augmentation 和 early stopping。

### 3.6 Voting classifier 与 loss

每个类别不是对应一个 neuron，而是对应 10 个 output neurons，所以最后一层宽度为 $10C$。Voting layer 将每组 10 个 outputs 汇成一个 class score；论文没有给出该汇聚是 sum、mean 还是 spike count normalization。

Appendix 给出的 loss 为：

$$
\mathcal L
=
\frac1T
\sum_{t=0}^{T-1}
\frac1C
\sum_{c=0}^{C-1}
\left(Y_{t,c}-y_c\right)^2.
$$

它在 class 和 simulation timestep 上平均 MSE。Algorithm 1 的 classifier 顺序是 `fc1 -> bn1 -> lif1 -> fc2 -> bn2 -> lif2 -> voting`。最终 inference 如何再跨 $T$ 聚合 class scores，正文没有单独给出公式。

## 4. Key Components and Mechanisms

### 4.1 三种“event/spike”不能混为一谈

SpikePoint pipeline 中有三种不同对象：

- raw event：sensor 输出的 $(x,y,t,p)$；
- pseudo-point：窗口化、丢弃 polarity、归一化后的 $(x,y,z)$；
- neuronal spike：point coordinates 经 Bernoulli sampling 重新生成的 $s_v[t]\in\{0,1\}$。

因此 SpikePoint 避免的是 frame/voxel conversion，但没有保持“一条 sensor event 对应一条 neuronal spike”。Raw timestamp 被压成 $z\in[0,1]$ 后，再以 firing rate 表达；精确 event timing 被转换为有限 $T=16$ 下的随机 spike-count estimate。

### 4.2 为什么 singular-stage 更适合本文的 SNN

PointNet++-style hierarchy 会重复 FPS/KNN、减少 point count、增加 feature depth。作者认为对 SNN 来说，多 stage 会使 binary features 随深度变得更 sparse/indistinguishable，并使 BPTT 梯度更难传播。SpikePoint 因而只 grouping 一次：local extractor 负责 neighborhood 内关系，global extractor 在不再次采样的情况下处理 1024 个 group descriptors。

Local branches 为：

$$
F_{l1}
=
\operatorname{ResF}_B(\operatorname{Conv1D}(X_1)),
$$

$$
F_{l2}
=
\operatorname{ResF}_B(\operatorname{Conv1D}(X_2)),
$$

$$
F_{\mathrm{local}}
=
\operatorname{MaxPool}_{24}(F_{l1})+F_{l2}.
$$

Global extractor 为：

$$
\mathcal L(x)
=
\operatorname{ResF}(\operatorname{Conv1D}(x)),
$$

$$
F_m=\mathcal L_2(\mathcal L_1(F_{\mathrm{local}})),
$$

$$
F_{\mathrm{global}}
=
\operatorname{MaxPool}_{1024}(\operatorname{Conv1D}(F_m)).
$$

这里两个 MaxPool 对象不同：第一个消去每组 24 neighbors，第二个消去 1024 groups。所谓 singular-stage 指只进行一次 geometric grouping，并不表示网络只有一层 Conv1D 或一个 spiking block。

### 4.3 Coordinate rescaling 为什么能改善短 rate coding

对 probability $p$ 做 $T$ 次 Bernoulli coding，firing-rate estimate 为：

$$
\hat p=\frac1T\sum_{t=1}^{T}s_p[t],
$$

$$
\mathbb E[\hat p]=p,
\qquad
\operatorname{Var}(\hat p)=\frac{p(1-p)}{T}.
$$

当 $p$ 很小时，expected spike count $Tp$ 小，全零 sequence 的概率 $(1-p)^T$ 很高。Daily DVS 中原始平均 relative distance 为 $|d|\approx0.039$，$T=16$ 时 expected count 仅 $0.624$，全零概率约为 $0.961^{16}\approx0.529$。除以 group standard deviation $0.052$ 后：

$$
\Delta|d|
=
\frac{0.039}{0.052}
\approx0.75,
$$

expected count 变为 12。论文测得 MRE 从 1.07 降至 0.26，约下降 76%。这支持“放大小 relative coordinates 可降低短 rate-code 的相对误差”。Appendix 的 CV 公式却缺少标准 firing-rate estimator 应有的 $1/\sqrt T$ 项，并混合 trial count $n$，其定量推导不能直接采用。

### 4.4 ResF 的 gradient path 与 activation 类型

Post-LIF identity branch 的关键价值是：

$$
\frac{\partial S^l}{\partial S^{l-1}}=1,
$$

而 pre-LIF branch 近似为：

$$
\frac{\partial S^l}{\partial S^{l-1}}
\approx
\sigma'(I+S^{l-1}).
$$

当 argument 接近 1 时，ATan surrogate derivative 约为 $1/(1+\pi^2)\approx0.092$，跨多个 blocks 连乘会迅速缩小。新结构提供 gradient highway，但不改变 main branch 的 threshold nonlinearity。Appendix Eq. (29) 声称系数被取消，印刷公式却仍保留该项，因此应以 graph structure 而非该式作为解释依据。

Post-LIF addition 也改变 forward representation：identity sum 可能是多值 integer，而非 binary spike。这对 AC operation accounting、后续 firing rate 和“full spike”定义都有影响，论文没有专门计数或消融。

## 5. Experiments and Main Evidence

### 5.1 Dataset provenance 与主要结果

SpikePoint 在五个 datasets 上评估。DVS128 Gesture、Daily DVS、DVS Action 是直接 sensor recordings；HMDB51-DVS 和 UCF101-DVS 由 conventional videos 转换为 events，不能用于证明真实 event-camera noise/timing 下的性能。DVS Action 还使用 event-density denoising，并从 recording 后半段开始生成 samples，因为作者观察到动作主要发生在那里；其 $90.6\%$ 必须限定到该 preprocessing configuration。

| Dataset | Model | SpikePoint | 结论边界 |
| --- | --- | ---: | --- |
| DVS128 Gesture | large, 0.58 M | 98.74% | SNN SOTA，低于 TBR+I3D 的 99.6% overall best |
| Daily DVS | small, 0.16 M | 97.92% | 表内 overall best，高于 TANet 96.5% |
| DVS Action | small, 0.16 M | 90.6% | 特定 denoise + half-stream preprocessing 下 overall best |
| HMDB51-DVS | large, 0.79 M | 55.6% | converted dataset 上表内 overall best |
| UCF101-DVS | large, 1.05 M | 68.46% | SNN SOTA，低于 ECSNet-SES 70.2% |

因此论文支持“五个数据集上的 SNN SOTA、其中三个表格内 overall best”，不支持五个数据集均为 overall SOTA。不同 class count 使 large model 的 classifier 参数量不同，不代表 backbone 不同。

### 5.2 Timestep、grouping 与 structure ablations

Timestep ablation 仅在 Daily DVS/DVS Action 上进行：

| $T$ | 2 | 4 | 8 | 12 | 16 | 24 | 32 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Daily DVS | 92.75 | 95.17 | 96.53 | 97.22 | **97.92** | 96.70 | 96.01 |
| DVS Action | 60.93 | 71.88 | 80.09 | 85.65 | **90.60** | 88.39 | 81.03 |

$T=16$ 最佳，说明更多 timesteps 没有单调改善 accuracy。论文没有判断下降来自 optimization、overfitting、firing saturation 还是 stochastic encoding behavior。

Grouping Table 8 的可配对证据包括：absolute + centroid single branch 为 97.78%，$[0,1]$ + centroid 为 96.53%，差 1.25 points；absolute + minimum + double/add 为 97.92%，double/concat 为 97.50%，Add 高 0.42 points；minimum coordinate 在部分配对中有改善，但 centroid 在 single branch 下略强。由于多行同时改变 absolute/minimum/centroid/branch/fusion，不能把所有差异归因于单一变量。

ResF ablation 比较 pre-LIF residual、no residual 和 post-LIF ResF。Figure 3 定性显示 post-LIF ResF 收敛更快且稳定 accuracy 更高，但没有 final numeric table、mean/std 或重复 runs。Structural ablation 中，仅 local 或仅 global extractor 在 DVS Action 上约 40%；PointNet-like configuration 还把 width 扩到 1024，因此不能单独证明 grouping stage 数量是唯一原因。

LIF/IF 只在 DVS128 Gesture 上比较：98.74% vs. 97.78%。作者推测 leak 缓解 overfitting，但没有 train-test gap、多个 datasets 或重复实验支持，属于 author speculation。

### 5.3 Energy evidence 与可复算性

作者使用 45 nm、$V_{DD}=0.9\ \mathrm V$ proxy：

$$
E_{\mathrm{MAC}}=4.6\ \mathrm{pJ},
\qquad
E_{\mathrm{AC}}=0.9\ \mathrm{pJ},
$$

$$
\mathrm{SOP}
=
f_{\mathrm{rate}}\times T\times\mathrm{FLOPs}.
$$

SpikePoint 的 0.9 G OPs 乘 $0.9\ \mathrm{pJ}$ 可得到约 $0.81\ \mathrm{mJ}$，与 Table 7 的 0.82 mJ dynamic energy 基本一致。但这一估计没有完整计入 sliding-window storage、random sampling、FPS、KNN、standardization、Poisson random generation、state memory 和 data movement，也没有针对 post-LIF multi-valued residual 调整 AC cost。

Static energy 定义为：

$$
E_{\mathrm{static}}
=
N_{\mathrm{param}}
\times12.991\ \mathrm{pW}
\times L_{\mathrm{sample}}.
$$

对 SpikePoint 的 0.58 M parameters 和 DVS128 $0.5\ \mathrm{s}$ window，该式给出约 $0.00377\ \mathrm{mJ}$；即使代入 6.52 s average recording length 也只有约 $0.049\ \mathrm{mJ}$，无法复现表中的 $0.756\ \mathrm{mJ}$。因此 static-energy table 的 $L_{\mathrm{sample}}$ 或单位存在未报告 scale，不能作为可复算硬件证据。整体 energy comparison 是 operation/SRAM theoretical proxy，不是 measured chip、GPU 或 wall-clock energy。

## 6. Strengths and Limitations

**Strengths.** 方法将 event stream 组织为稀疏时空 points，避免 frame/voxel representation；point-based SNN 从头直接训练；singular-stage local/global architecture 参数较少；coordinate rescaling 明确针对 16-step rate coding 的高相对误差；post-LIF residual 给出具体的 surrogate-gradient bypass；五个 datasets 上结果具有竞争力。

**Limitations.** Polarity 被丢弃；raw timestamps 被重新编码成随机 rate spikes；absolute coordinates 丢失 per-point direction，且超出 $[0,1]$ 时的 encoder 处理不明；$N,N',M$ 符号冲突；random sampling 易选中 noise；window length 与 DVS Action preprocessing 依赖 dataset-specific tuning；overlapping random split 可能泄漏；post-LIF sum 不保证 binary；CV 与 residual-gradient 推导有错误或印刷不一致；energy 没有覆盖完整 pipeline，static estimate 也无法按公式复现。

## 7. Relation to Other Papers and Survey Taxonomy

本论文主要属于 event representation、SNN architecture、temporal modeling、training method、action recognition、efficiency and hardware proxy 以及 open challenges。它连接 PointNet/PointNet++ 式 point processing 与 direct-trained SNN：相较 frame-based SNN，它保留 point sparsity 和归一化时间坐标；相较 Point Cloud ANN，它避免多阶段 set abstraction，并用 spike-compatible coordinate encoding 与 post-LIF residual mapping。它不是 dense prediction、tracking、optical flow、detection 或 adversarial robustness 方法。

### PDF-verified relation backfill

主要路线是 sparse Event Cloud grouping/aggregation 与 point-wise spiking computation 的端到端结合。

- **PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space (Charles Ruizhongtai Qi et al., NeurIPS 2017)** — `foundation`。该工作提供 hierarchical Event Cloud grouping 的基础机制；当前论文将其用于自身的 event/SNN pipeline，而不是把该前驱本身作为新贡献。 对应 Sections 2 and 4: representation and SNN integration。证据：Related Work and Method, PDF pp.2-4, citation and bibliography [24]。 当前 active corpus 未覆盖。
- **TTPOINT: A Tensorized Point Cloud Network for Lightweight Action Recognition with Event Cameras (Hongwei Ren et al., ACMMM 2023)** — `baseline`。该工作是 point-based event action recognition 的实验 comparator；当前论文与其主要区别在于本文第 3–4 节所述的核心机制。 对应 Sections 4 and 5: ANN-SNN comparison and action recognition。证据：Related Work and Experiments, PDF pp.3 and 8, citation and bibliography [33]。 当前 active corpus 未覆盖。
- **Modeling Point Clouds with Self-Attention and Gumbel Subset Sampling (Jiancheng Yang et al., CVPR 2019)** — `alternative`。两者都处理 point subset selection and feature modeling，但采用不同 representation、state 或 computation route。 对应 Sections 2 and 4: sparse representation and SNN integration。证据：Related Work, PDF p.3, citation and bibliography [37]。 当前 active corpus 未覆盖。

## 8. Survey-Usable Takeaways

SpikePoint 表明，event stream 可以不经 frame accumulation，而以 $(x,y,t)$ pseudo-point cloud 输入直接训练的 SNN；但这种“直接”仍包含窗口化、sampling/grouping 和重新 rate encoding。其最有综述价值的机制不是笼统的低功耗声明，而是三个具体设计：用 point neighborhoods 提取 local/global geometry；通过 relative-coordinate rescaling 降低短 timestep Poisson encoding 的相对误差；通过 $\operatorname{LIF}(I)+S^{l-1}$ 为 surrogate training 提供 identity gradient path。实验支持其为当时强竞争力的 point-based SNN，但真实系统能效、异步部署能力和带符号/超范围 coordinates 的编码仍未得到验证。

## Supplement Points

### Questions and Clarifications

#### 1. 对 Point Cloud coordinates 进行 rate encoding 是什么意思？

完成 grouping 后，主分支中每个 point 有六个连续特征：

$$
X_1
=
[\Delta|x|,\Delta|y|,\Delta|z|,x_{\min},y_{\min},z_{\min}].
$$

这些值不是 spikes。SpikePoint 使用 stateless Poisson encoder，把每个 $v\in[0,1]$ 转换成长度 $T=16$ 的 binary sequence。每个 timestep 独立采样：

$$
s[t]
\sim
\operatorname{Bernoulli}(v),
\qquad
P(s[t]=1)=v.
$$

例如 $v=0.75$ 时，16 steps 的 expected spike count 是 $16 \times 0.75=12$。某次实际序列可能产生 11 个 spikes，其解码 firing rate 为：

$$
\widehat v
=
\frac{1}{16}
\sum_{t=1}^{16}s[t]
=
\frac{11}{16}
=
0.6875.
$$

单次结果不一定等于 0.75，但 $\mathbb{E}[\widehat v]=0.75$。数值越大，expected firing rate 越高。

这里需要区分三种“事件/脉冲”：

- raw event 是传感器产生的 $(x,y,t,p)$；
- pseudo-point 是窗口化、归一化并丢弃 polarity 后的 $(x,y,z)$；
- neuronal input spike 是 point coordinates 经 Poisson sampling 重新生成的 0/1 sequence。

因此，SpikePoint 没有把 raw events 一一当作神经元 spikes。它避免了 frame conversion，但仍执行 point preprocessing 和重新编码。

作者说“SNN 不能处理负数”也过于宽泛。准确说，是本文把数值直接作为 Bernoulli probability 的 Poisson encoder 不能接受负 probability。SNN 可以使用正负双通道、signed weights 或其他 encoder 表达 signed input。另一个未解决问题是 $|d|/\operatorname{SD}$ 可能大于 1，论文没有说明 clipping 或再次 normalization：`Needs further check`。

---

#### 2. 为什么论文的 LIF 公式与常见公式不同？

常见离散公式为：

$$
u[t]
=
\left(
1-\frac{\Delta t_s}{\tau_m}
\right)u[t-1]
+
\frac{\Delta t_s}{\tau_m}I[t].
$$

它来自连续模型 $\tau_m\,du/dt=-u+I$ 的 forward-Euler discretization。历史膜电位的保留系数为 $1-\Delta t_s/\tau_m$，当前输入则乘以 $\Delta t_s/\tau_m$。

论文先更新 synaptic-current state：

$$
I[n]
=
\exp\left(
-\frac{\Delta t}{\tau_{\mathrm{syn}}}
\right)I[n-1]
+
\sum_jW_jS_j[n],
$$

再更新 membrane state：

$$
U[n+1]
=
\exp\left(
-\frac{\Delta t}{\tau_{\mathrm{mem}}}
\right)U[n]
+
I[n]
-
S[n].
$$

两种写法都描述 leaky integration，但有三点差别：

1. 常见公式使用 Euler coefficient；论文使用 exponential decay。小步长下二者近似，因为 $e^{-\Delta t/\tau}\approx1-\Delta t/\tau$。
2. 常见公式直接注入 $I[t]$；论文额外让 synaptic current 自身具有衰减记忆。
3. 论文用 $-S[n]$ 表示 spike 后 reset，可能隐含 $V_{\mathrm{th}}=1$ 的 soft reset，但没有明确说明。

严格 exponential discretization 常见输入项为 $(1-\alpha)I[n]$，而论文直接加 $I[n]$，可能把比例吸收到 current 或 weights 中。Appendix A.8 又说明实际使用 SpikingJelly ParametricLIF、initial $\tau=2$ 和 `no decay input`。正文 generic equations 与实际 implementation 是否逐项一致：`Needs further check`。

---

#### 3. Bottleneck、$\operatorname{ResF}_B$ 和 $\operatorname{ResF}$ 是什么？

Bottleneck 是 residual block 内“先压缩 channels，再恢复”的窄层。若输入宽度为 $D=64$，可以概念性写成：

$$
64
\rightarrow
32
\rightarrow
64.
$$

Figure 8 明确说明 $\operatorname{ResF}_B$ 的 bottleneck width 是输入的一半。最后恢复到 64，是因为 identity branch 不改变 shape，主分支必须恢复相同宽度才能相加。

$\operatorname{ResF}_B$ 用于 local extractor。它需要对每个 neighborhood 的每个 point 执行计算，因此 bottleneck 可显著减少 point-level Conv1D 参数和 operations。$\operatorname{ResF}$ 不使用 bottleneck，主要用于 global extractor，使 channel width 可以持续增大并保留较宽的 global representation。论文没有逐层列出两个 block 的全部 kernel、stride 和 neuron placement：`Needs further check`。

---

#### 4. 从 $\operatorname{LIF}(I+S^{l-1})$ 改成 $\operatorname{LIF}(I)+S^{l-1}$ 到底是什么意思？

原结构先把 main branch 与 residual branch 相加，再送入 LIF：

$$
I+S^{l-1}
\rightarrow
\operatorname{LIF}
\rightarrow
S^l.
$$

因此 residual information 也必须通过 threshold/spike nonlinearity。BPTT 时不可导 spike function 由 surrogate derivative 近似，所以 residual path 的梯度包含：

$$
\sigma'
\left(
I+S^{l-1}
\right).
$$

修改后，只有 main branch 经过 LIF，residual branch 在 LIF 后相加：

$$
I
\rightarrow
\operatorname{LIF}(I),
\qquad
S^l
=
\operatorname{LIF}(I)+S^{l-1}.
$$

此时对 residual input 求导：

$$
\frac{\partial S^l}{\partial S^{l-1}}
=
1.
$$

所谓 surrogate-gradient coefficient “被消除”，不是把它设置为 0，而是 identity branch 不再经过 spike function，所以该路径的导数中不再出现它。主分支仍使用 surrogate gradient。完整梯度与数值例子见 `Additional Technical Details`。

---

#### 5. $F_m=\mathcal{L}_2(\mathcal{L}_1(F_{\mathrm{local}}))$ 中的 $\mathcal{L}_1$ 和 $\mathcal{L}_2$ 是什么？

论文先定义一个 global feature block：

$$
\mathcal{L}(x)
=
\operatorname{ResF}
\left(
\operatorname{Conv1D}(x)
\right).
$$

$\mathcal{L}_1$ 和 $\mathcal{L}_2$ 是两个连续但参数独立的 block，不是 timestep，也不是同一组 weights 重复两次。执行顺序是：

$$
F_{\mathrm{local}}
\rightarrow
\mathcal{L}_1
\rightarrow
\mathcal{L}_2
\rightarrow
F_m.
$$

在小模型中可对应：

$$
[1024,32]
\rightarrow
[1024,64]
\rightarrow
[1024,128].
$$

随后最后一个 Conv1D 再升维到 $[1024,256]$，global max pooling 得到 $[1,256]$。

---

#### 6. Local feature extractor 和 Global feature extractor 的维度如何变化？

省略 batch 与 timestep axes，小模型的实际流程如下。

主 local branch 输入：

$$
[1024,24,6].
$$

Conv1D 对每个 point 共享一个 $6 \rightarrow 32$ feature mapping：

$$
[1024,24,6]
\rightarrow
[1024,24,32].
$$

$\operatorname{ResF}_B$ 保持外部 shape 不变，再在每个 neighborhood 的 24 个 points 上 max pooling：

$$
[1024,24,32]
\rightarrow
[1024,32].
$$

Centroid branch 同时执行：

$$
[1024,3]
\rightarrow
[1024,32].
$$

两条分支相加，得到 1024 个 center-level local features：

$$
[1024,32]
+
[1024,32]
\rightarrow
[1024,32].
$$

Global extractor 再逐步升维：

$$
[1024,32]
\rightarrow
[1024,64]
\rightarrow
[1024,128]
\rightarrow
[1024,256].
$$

最后在 1024 个 center-level features 上 global max pooling：

$$
[1024,256]
\rightarrow
[1,256].
$$

所以 local extractor 回答“每个局部时空 neighborhood 中出现了什么结构”，global extractor 回答“1024 个局部结构合起来描述了什么动作”。加入时间和 batch 后，概念 shape 为 $[B,T,1024,24,C]$，但实际 code 的 axis order 未给出。

---

#### 7. 为什么 centroid 的均值修正是 $c-\sqrt{2/\pi}\operatorname{SD}$？

原始 point 与标准化 relative coordinate 的关系为：

$$
g
=
c+\Delta\operatorname{SD}.
$$

作者假设 $\Delta\sim\mathcal{N}(0,1)$，因此 $\mathbb{E}[\Delta]=0$，原表示的期望中心为 $c$。取绝对值后：

$$
\mathbb{E}[|\Delta|]
=
\sqrt{\frac{2}{\pi}}.
$$

如果仍使用原 centroid，则：

$$
\mathbb{E}
\left[
c+|\Delta|\operatorname{SD}
\right]
=
c
+
\sqrt{\frac{2}{\pi}}
\operatorname{SD}.
$$

relative part 在期望上增加了 $\sqrt{2/\pi}\operatorname{SD}$，所以将 centroid 减去同量：

$$
c_{\mathrm{corr}}
=
c
-
\sqrt{\frac{2}{\pi}}
\operatorname{SD}.
$$

此时 $\mathbb{E}[c_{\mathrm{corr}}+|\Delta|\operatorname{SD}]=c$。例如 $c=0.5$、$\operatorname{SD}=0.1$ 时，偏移量约为 $0.0798$，修正 centroid 为 $0.4202$，加回 absolute relative part 的期望后重新得到 0.5。

这只能补偿 distribution mean，无法恢复单个 point 的正负方向；$-1$ 和 $+1$ 取绝对值后都变成 1。论文实际采用 $[x_{\min},y_{\min},z_{\min}]$ 这一 empirical geometric boundary，测试准确率 97.92%，高于理论均值修正的 97.50%。因此“precise correction”只是作者措辞，更准确的说法是 expectation-level compensation。

---

#### 8. Relative encoding error 和 CV 分别衡量什么？

若原值为 $p$，一次 rate coding 解码结果为 $\widehat p$，relative encoding error 是：

$$
\varepsilon_{\mathrm{rel}}
=
\frac{|\widehat p-p|}{|p|}.
$$

例如 $p=0.039$，16 steps 中产生 1 个 spike，则 $\widehat p=1/16=0.0625$，relative error 约为：

$$
\frac{|0.0625-0.039|}{0.039}
\approx
0.603.
$$

若没有 spike，$\widehat p=0$，relative error 为 1，即 100%。MRE 是许多 coordinates 的 relative errors 的平均，回答“实际编码结果平均偏离原值多少”。

CV 定义为：

$$
cv
=
\frac{
\operatorname{SD}(\widehat p)
}{
\mathbb{E}[\widehat p]
}.
$$

它不针对某一次误差，而衡量同一个数值反复随机编码时，相对于均值有多不稳定。对 $T$ 次独立 Bernoulli sampling 的 firing-rate estimator：

$$
\mathbb{E}[\widehat p]
=
p,
\qquad
\operatorname{Var}(\widehat p)
=
\frac{p(1-p)}{T},
$$

因此标准 CV 为：

$$
cv
=
\sqrt{
\frac{1-p}{Tp}
}.
$$

Daily DVS 中，原 $p=0.039$ 时 expected count 只有 0.624，全零序列概率约为 $0.961^{16}\approx0.529$；大量小 coordinates 因而不可区分。Rescaling 后 $p'=0.039/0.052\approx0.75$，expected count 变为 12，relative fluctuation 显著降低。论文报告 MRE 从 1.07 降至 0.26，下降约 75.7%。

论文公式（25）得到 $cv=\sqrt{1/p-1}$，更接近单个 Bernoulli spike 的 CV，缺少 firing-rate mean 应有的 $1/\sqrt{T}$，并且对重复次数 $n$ 的处理不清楚。因此其定量推导为 `Needs further check`，但 $p$ 增大时相对波动下降的趋势成立。

---

#### 9. $[1024,24,6] \rightarrow [1024,24,32]$ 的每个维度来自哪里？

Figure 8 和 Appendix A.3 给出的 actual shape 是：

$$
[1024,24,6].
$$

- 1024 来自 Appendix A.8 的 `Number of Points: 1024`，并对应 Figure 8 中保留到 global extractor 的 1024 个 center/neighborhood features；
- 24 是 KNN 为每个中心组织的 neighborhood-point axis，后续 local max pooling 正是在该轴上执行；
- 6 来自 $[\Delta|x|,\Delta|y|,\Delta|z|,x_{\min},y_{\min},z_{\min}]$；
- 32 是小模型 channel list $[32,64,128,256]$ 的第一个宽度。

Conv1D 只把每个 point 的 feature vector 从 $\mathbb{R}^6$ 映射到 $\mathbb{R}^{32}$，不改变 1024 和 24 两个结构轴：

$$
[1024,24,6]
\rightarrow
[1024,24,32].
$$

论文 Figure 8 的图例以及正文对 $N$、$N'$、$M$ 的命名与实际 pooling axis 不一致。因此 shape 和运算可确认，但三个符号与“group 数/每组 point 数”的正式对应是 `Needs further check`。

### Additional Technical Details

#### 为什么将 residual 放在 LIF 之后

原结构为：

$$
S^l
=
\operatorname{LIF}(I+S^{l-1})
$$

其 forward path 是：

$$
I+S^{l-1}
\rightarrow
\operatorname{LIF}
\rightarrow
S^l.
$$

主分支与 residual signal 都必须经过 LIF threshold。Heaviside spike function 不可导，训练时使用 ATan surrogate：

$$
\sigma(x)
=
\frac{1}{\pi}\arctan(\pi x)
+
\frac{1}{2},
$$

$$
\sigma'(x)
=
\frac{1}{1+(\pi x)^2}.
$$

所以原结构对 residual input 的近似导数为：

$$
\frac{\partial S^l}{\partial S^{l-1}}
\approx
\sigma'
\left(
I+S^{l-1}
\right).
$$

当输入约为 1 时：

$$
\sigma'(1)
=
\frac{1}{1+\pi^2}
\approx
0.092.
$$

若多个 residual blocks 上的系数都约为 0.1，经过 5 个 blocks 后，identity-path gradient 量级会变成：

$$
0.1^5
=
0.00001.
$$

这就是作者担心的 accumulative multiplication 与 gradient vanishing。严格来说 $\sigma'(0)=1$，因此“surrogate derivative 始终小于 1”并不完全正确；Appendix A.4 的论点是 BatchNorm output 加 spike 后期望约为 1，所以该系数通常明显小于 1。

修改后：

$$
S^l
=
\operatorname{LIF}(I)+S^{l-1}
$$

其 forward path 分成两条：

$$
I
\rightarrow
\operatorname{LIF}(I),
$$

$$
S^{l-1}
\rightarrow
\text{identity branch},
$$

最后相加。于是：

$$
\frac{\partial S^l}{\partial S^{l-1}}
=
1.
$$

两个 blocks 的例子更直观。若原结构每个 block 的 surrogate derivative 都为 0.2，则：

$$
\frac{\partial S^{l+2}}{
\partial S^l
}
\approx
0.2 \times 0.2
=
0.04.
$$

修改后的 identity path 为：

$$
\frac{\partial S^{l+2}}{
\partial S^l
}
=
1 \times 1
=
1.
$$

因此，“公式（29）中的系数被消除”表示 residual path 不再穿过 $\sigma'(\cdot)$，而不是主分支不再需要 surrogate gradient。该修改提供的是一条 gradient highway，只能说明 residual path 的 vanishing 得到缓解，不能证明整个网络不存在 gradient explosion/vanishing。

附录推导本身存在两个问题：一是作者声称该系数被消除，但打印出的公式（29）仍包含它；二是 ANN identity mapping 的写法 $Y^l=\sigma(A^l+Y^{l-1})$ 在 $A^l=0$ 时只能得到 $Y^l=\sigma(Y^{l-1})$，除非 $\sigma$ 为 identity，否则不严格等于 $Y^{l-1}$。因此应保留 residual-bypass 的结构性解释，而不把附录公式视为完整严谨证明。

最后，若 $\operatorname{LIF}(I)\in\{0,1\}$ 且 $S^{l-1}\in\{0,1\}$，加法输出可能属于 $\{0,1,2\}$。所以 post-LIF residual output 不一定仍是严格 binary spike。论文没有完整说明下一层如何解释这一 multi-valued feature：`Needs further check`。
