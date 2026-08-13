---
tags: [event-camera, spiking-neural-network, point-cloud, action-recognition, ICLR-2024]
---

# Summary V2｜SpikePoint: An Efficient Point-Based Spiking Neural Network for Event Cameras Action Recognition

## 1. Core Understanding

SpikePoint 面向 event-based action recognition，核心目标是不把异步事件堆叠为 conventional frames，而是将其表示为稀疏的三维时空 pseudo-point cloud，再用直接训练的 point-based SNN 分类。其主要贡献是：以 $(x,y,t)$ points 保留稀疏结构和窗口内相对时间；设计适配非负 rate coding 的坐标表示；用 singular-stage local/global feature extractor 避免传统 Point Cloud ANN 的多阶段层次结构；将 residual connection 放到 LIF 之后以改善 surrogate-gradient propagation。

网络主体是使用 Parametric LIF、binary spikes、BPTT 和 ATan surrogate gradient 的直接训练 SNN，不是 ANN-to-SNN conversion。但完整 pipeline 还包含 sliding window、random sampling、FPS、KNN、normalization 和 Poisson encoding 等常规预处理，因此只能将神经网络主体称为 spiking，不能把整个系统无条件归类为 fully event-driven neuromorphic pipeline。

## 2. Problem and Motivation

Event camera 输出稀疏、异步且具有高时间分辨率的事件，但已有 event-camera SNN 往往先生成 frames，增加映射开销并削弱稀疏性与细粒度时间信息。Point Cloud 可以把事件的空间坐标与时间组织为稀疏点集，却通常依赖 ANN 中反复 sampling/grouping 的 hierarchical architecture；作者认为深层 stage 会使 spike features 更稀疏、难以区分，并加重 BPTT 的梯度问题。

SpikePoint 因此试图解决两个耦合问题：一是直接在 point representation 上利用事件的稀疏时空结构；二是设计适合 rate-coded spikes 和 surrogate training 的轻量 Point Cloud SNN。

## 3. Method Overview

原始事件为 $e_m=(x_m,y_m,t_m,p_m)$。模型用长度为 $L$ 的 sliding window 截取 event clip，将 $x_m,y_m$ 归一化到 $[0,1]$，并将窗口内时间转换为：

$$
z_m
=
\frac{t_m-t_k}{t_l-t_k}
$$

随后丢弃 polarity $p_m$，得到 $(x_m,y_m,z_m)$ pseudo-point cloud。Random sampling 统一 point 数量；FPS 选择中心，KNN 为每个中心构建局部邻域。Figure 8 给出的实际 local input 为 $[1024,24,6]$：1024 个保留中心/邻域、每个邻域 24 个 points、每个 point 6 个特征。论文对 $N$、$N'$、$M$ 的文字定义与图中轴含义不一致，正式符号对应为 `Needs further check`。

连续 coordinates 通过 stateless Poisson rate encoder 转为 $T=16$ 的 binary spike sequence。对 $v\in[0,1]$，每个 timestep 独立采样 $s[t]\sim\operatorname{Bernoulli}(v)$，以 firing rate 表示数值。标准化 relative coordinates 包含负值，不能直接作为该 encoder 的发放概率，因此作者取 $[\Delta|x|,\Delta|y|,\Delta|z|]$，并用 group minimum coordinates 与独立 centroid branch 补偿方向和分布信息。标准化值可能超过 1 时如何进入 Poisson encoder，论文未说明：`Needs further check`。

这一转换需要持续区分三类对象：raw event 是传感器输出的 $(x,y,t,p)$；pseudo-point 是预处理后的 $(x,y,z)$；input spike 则是 coordinates 经 Poisson sampling 重新生成的 binary sequence。SpikePoint 的“直接处理 event data”是指避免 frame/voxel conversion，不是逐个 raw event 直接驱动网络。

## 4. Key Components and Mechanisms

Local main branch 的输入为 $X_1=[\Delta|x|,\Delta|y|,\Delta|z|,x_{\min},y_{\min},z_{\min}]$，centroid branch 为 $X_2=[x_c,y_c,z_c]$。小模型将 $[1024,24,6]$ 映射为 $[1024,24,32]$，在 24-point neighborhood 上 max pooling 得到 $[1024,32]$，再与 centroid feature 相加。Global extractor 依次升维 $32 \rightarrow 64 \rightarrow 128 \rightarrow 256$，对 1024 个 features 做 global max pooling，得到 $[1,256]$；大模型对应 $64 \rightarrow 128 \rightarrow 256 \rightarrow 512$。

带 bottleneck 的 $\operatorname{ResF}_B$ 用于 point-level local extraction，其中间 channel 为输入的一半；不带 bottleneck 的 $\operatorname{ResF}$ 用于 global extraction，以保留较宽表示。每个 Conv1D 后接 BatchNorm。

短 rate coding 会严重量化小坐标。Daily DVS 中原始平均距离约为 $|d|=0.039$，16 steps 的 expected spike count 仅为 $0.624$；除以 group standard deviation $0.052$ 后得到 $\Delta|d|\approx0.75$，expected count 变为 12。论文报告 MRE 从 1.07 降至 0.26，即 relative encoding error 约下降 76%。A.3 用 CV 说明编码概率增大后相对随机波动下降，但其公式混合了单个 Bernoulli spike 与 firing-rate estimator，并遗漏或消去了 $nT$ 因子，严格推导为 `Needs further check`。

关键 residual modification 是：

$$
S^l
=
\operatorname{LIF}(I+S^{l-1})
\quad \longrightarrow \quad
\operatorname{LIF}(I)+S^{l-1}
$$

修改后，identity branch 绕过不可微 spike function，其反向导数为 1，不再连续乘以通常小于 1 的 surrogate derivative，从而缓解 residual path 的 gradient vanishing。论文公式（29）仍保留声称已消除的系数，推导书写不完整，但 Figure 3 的消融支持该 ResF 在当前配置下具有更快收敛和更高稳定准确率。

Classifier 是 spike-based MLP。每个类别对应 10 个 output neurons，通过 voting 形成类别输出，并在类别和 16 个 timesteps 上计算 MSE。论文没有明确给出 10-neuron voting 与跨 timestep aggregation 的完整公式：`Needs further check`。

小模型 classifier 为 $256 \rightarrow 256 \rightarrow 10C$，大模型为 $512 \rightarrow 512 \rightarrow 10C$，其中 $C$ 是类别数。LIF 在 DVS128 Gesture 上为 98.74%，IF 为 97.78%；作者将 0.96 个百分点差异解释为 leakage 缓解 overfitting，但没有报告多次运行方差、train-test gap 或其他数据集对比，因此该机制仍是 author speculation。

## 5. Experiments and Main Evidence

SpikePoint 在 DVS128 Gesture、Daily DVS、DVS Action、HMDB51-DVS 和 UCF101-DVS 上评估。Daily DVS、DVS Action 使用 0.16 M 的小模型；其余使用大模型。DVS Action 额外使用 denoising，并从 event stream 后半段开始采样，因此其 90.6% 结果应限定在该 preprocessing configuration 下。HMDB51-DVS 和 UCF101-DVS 是由 frame videos 转换的 events，不是直接 event-camera recordings。

关键结果如下：DVS128 Gesture 为 98.74%，是表中 SNN SOTA，但低于 TBR+I3D 的 overall 99.6%；Daily DVS 为 97.92%，高于表中最佳 ANN 96.5%；DVS Action 为 90.6%，高于 ST-EVNet 的 88.7%；HMDB51-DVS 为 55.6%，高于 RG-CNN 的 51.5%；UCF101-DVS 为 68.46%，是 SNN SOTA，但低于 ECSNet-SES 的 overall 70.2%。因此论文支持“五个数据集上的 SNN SOTA、其中三个表格内 overall best”，不支持五个数据集均为 overall SOTA。

Timestep ablation 只在 Daily DVS 和 DVS Action 上验证：16 timesteps 分别达到 97.92% 和 90.6%，24/32 timesteps 反而下降，原因未解释。Grouping ablation 中，absolute-value encoding 比 $[0,1]$ normalization 高 1.25 个百分点，Add fusion 比 Concat 高 0.42 个百分点。部分 grouping comparisons 同时改变多个变量，不能作为严格单变量因果证据。论文也未说明 overlapping clips 是在 recording-level split 之后生成，还是生成后随机划分；潜在 train-test leakage 为 `Needs further check`。

Energy 不是硬件实测。作者假设 45 nm、$V_{DD}=0.9$ V，使用 $E_{MAC}=4.6$ pJ、$E_{AC}=0.9$ pJ，并以 firing rate、timesteps 和 FLOPs 估算 SOP。SpikePoint 的 0.82 mJ dynamic energy 与 0.756 mJ static energy 属于 theoretical operation/SRAM model-level proxy，不是 GPU runtime、wall-clock latency 或 neuromorphic hardware result；FPS、KNN、encoding、memory movement 与神经元状态更新等成本未被完整计入。

ResF ablation 比较 conventional pre-LIF residual、no residual 和 post-LIF ResF。训练曲线定性支持 ResF 收敛更快、稳定准确率更高，但没有最终数值表、mean/std 或重复实验。Structural ablation 显示仅 local 或仅 global extractor 在 DVS Action 上约 40%，显著低于完整模型；PointNet-style comparison 同时改变 feature width，不能单独证明 singular-stage 是唯一原因。

## 6. Strengths and Limitations

Strengths：方法将 event stream 组织为稀疏时空 points，避免 frame/voxel representation；point-based SNN 为直接训练而非 conversion；singular-stage local/global design 参数量小；坐标 rescaling 明确针对 16-step rate coding 的高相对误差；五个数据集上的 SNN 结果具有竞争力。

Limitations：polarity 被直接丢弃；Poisson encoding 重新随机化传感器事件，且只用 16 timesteps；random sampling 易选中 illumination/background noise；window length 需要按数据集调优；DVS Action 使用特定去噪与时间裁剪；论文的 tensor symbols、CV 推导和 residual-gradient 公式存在内部不一致；“full spike”不覆盖完整预处理 pipeline；energy 仅为理论 proxy。

## 7. Relation to Other Papers and Survey Taxonomy

本论文主要属于 event representation、SNN architecture、temporal modeling、training method、action recognition、efficiency and hardware proxy 以及 open challenges。它连接 PointNet/PointNet++ 式 point processing 与 direct-trained SNN：相较 frame-based SNN，它保留 point sparsity 和归一化时间坐标；相较 Point Cloud ANN，它避免多阶段 set abstraction，并用 spike-compatible coordinate encoding 与 post-LIF residual mapping。它不是 dense prediction、tracking、optical flow、detection 或 adversarial robustness 方法。

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
