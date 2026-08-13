---
tags: [event-camera, spiking-neural-network, bayesian-computation, motion-segmentation, NeurIPS-2024]
---

# Summary V2｜Continuous Spatiotemporal Events Decoupling through Spike-based Bayesian Computation

## 1. Core Understanding

本文研究无监督、在线的 event-based motion segmentation：从混合了 camera self-motion 与 object motions 的连续 event stream 中，同时估计各 motion models 的参数 $\theta$，以及每个 event 属于各 motion cluster 的 soft responsibility $P$。核心思想不是用 BPTT 训练一个分类 SNN，而是将传统 EM motion segmentation 重写为 spike-based Bayesian computation：WTA circuit 的 stochastic firing 近似 E-step，STDP-like local update 近似最大化 IWE contrast 的 M-step。

SNN/WTA/STDP 是论文的核心计算机制，但完整 pipeline 还包含 conventional event warping、IWE/variance computation、TPE parameter search、SVD/K-means initialization 以及预定义 motion-model structure。因此更准确的分类是 **hybrid spike-based event-motion framework**，不能无条件称为 fully spiking 或端到端 neuromorphic implementation。

## 2. Problem and Motivation

Event camera 输出 $e_k = (\mathbf{x}_k,t_k,q_k)$。本文不使用 polarity $q_k$，实际依赖 position 与 timestamp。多个运动源产生的 events 在同一 stream 中混合，形成相互依赖的问题：不知道 event 属于哪个 object，就难以估计其 motion；motion parameters 不准确，又无法正确分配 events。

传统 EM-like 方法交替求解两个未知量：motion parameters $\theta = \{\theta_j\}_{j = 1}^{N_\ell}$，以及 responsibilities $P = \{p_{kj}\}$。作者希望用 WTA competition 与 STDP local plasticity 实现相同的迭代逻辑，从而为 asynchronous、online、neuromorphic processing 建立理论基础。论文强调 Loihi、SpiNNaker 和 Tianjic 等硬件的潜力，但没有实际 hardware deployment 或 energy measurement。

## 3. Method Overview

对 motion model $j$，event $e_k$ 通过 $\theta_j$ warp 到 reference time：

$$
\mathbf{x}'_{kj}
=
\mathcal{W}(\mathbf{x}_k,t_k;\theta_j).
$$

全部 warped events 按 responsibility 加权累积成 Image of Warped Events（IWE）：

$$
I_j(\mathbf{x})
=
\sum_{k=1}^{N_e}
p_{kj}
\delta(\mathbf{x} - \mathbf{x}'_{kj}).
$$

正确 motion compensation 会使同一物体边缘在 reference time 对齐，得到集中、sharp、high-variance IWE；错误参数会把 events 拖散。整体目标是最大化各 motion-specific IWEs 的 variance 之和。PDF 公式（4）至（6）将 motion-model sum 的 upper bound 印为 $N_e$，但 summation index $j$ 表示 motion model，语义上应为 $N_\ell$；原文符号存在内部不一致。

传统 E-step 在当前 $\theta$ 下查询每个 motion model 对 event $e_k$ 的响应并归一化：

$$
p_{kj}
=
\frac{
I_j(\mathbf{x}'_{kj})
}{
\sum_{i=1}^{N_\ell}I_i(\mathbf{x}'_{ki})
}.
$$

PDF 公式（5）的 denominator 混用了 $\mathbf{x}'_{kj}$ 与 $\theta_i$，上式是语义一致的写法，原公式的准确索引为 `Needs further check`。M-step 固定 $P$，更新 $\theta$ 以提高 IWE contrast，然后重新执行 E-step。

## 4. Key Components and Mechanisms

### WTA 对应 E-step

每个 motion neuron $y_j$ 表示带参数的 warping function，并将 warped events 累积到与 event-space 对应的 output tensor $u_j$；作者将 $u_j$ 视为 IWE $I_j$。Global inhibition 汇总竞争响应：

$$
H(t)
=
\sum_j u_j(t),
$$

并令 output neuron $z_j$ 的 stochastic firing probability 为：

$$
P(z_j\text{ fires at }t)
=
\frac{u_j(t)}{H(t)}.
$$

这更接近 soft/stochastic WTA，而不是 hard winner selection。作者将 normalized firing probability 解释为 responsibility $p_{kj}$。但论文没有完整说明如何从 tensor-valued firing process 逐 event 读出 $p_{kj}$，也没有说明 circuit 是否强制同一位置只有一个 winner；严格等价性为 `Needs further check`。

### STDP 对应 M-step

作者给出的 motion-parameter update 为：

$$
\Delta\theta_j
=
\eta
\operatorname{Var}(u_j)
p_{kj}
\frac{\partial\mathcal{W}_j}{\partial\theta_j}.
$$

$p_{kj}$ 使主要属于 model $j$ 的 events 强烈更新 $\theta_j$，其他 events 影响较小。若 update direction 与 $\nabla_{\theta_j}\operatorname{Var}(u_j)$ 的夹角小于 $90^\circ$，则足够小的一阶更新会提高 variance。论文没有从其 timing-based STDP 定义完整推出该方向一致性，因此这是 M-step-like、conditional first-order argument，不是每次 STDP update 必然增大 objective 的完整证明，也不是 global convergence proof。

### Initialization 与 online processing

$N_\ell$ 和 motion-model type 必须预设；实验主要使用 linear motion $\theta = (v_x,v_y)$。作者先将 event subset 分成 patches，对每个 patch 用 random sampling + TPE 搜索最大化 IWE contrast 的 candidate motion，得到多于 $N_\ell$ 个 candidates，再用 SVD 选取差异显著的 $N_\ell$ 个 initial parameters；Appendix 表明 K-means 也可替代 SVD。SVD 如何从 components 精确选回具体 candidates 未充分说明：`Needs further check`。

连续 stream 按固定 event count 切为 chronological packets $\{\mathbf e^n\}_{n = 1}^{N_g}$。每个 packet 再分 patches，反复执行 WTA E-step 和 STDP M-step，得到 $(\theta_n^*,P_n)$；上一 packet 的 motion estimate 用于预测下一 packet 的 cluster initialization。具体 packet count、patch construction、convergence criterion、epochs 和 propagation formula 均未给出。

## 5. Experiments and Main Evidence

实验使用 Extreme Event Dataset（EED），场景同时包含 camera self-motion 与 moving objects。Figure 5 显示学习后两个 motion-specific IWEs 比学习前更清晰，并用不同 output-neuron spike colors 分离 background 与 ball motion。Figure 6 对 “What is background?”、“Occlusions” 和 “Fast drone” 三个 continuous sequences 给出 qualitative temporal visualization。Appendix Figure S7 中，正确与错误 warp 的 IWE variance 分别为 582.87 和 55.18，直接支持正确 compensation 可产生更集中、高-variance IWE 的局部例子。

这些结果证明的是 qualitative proof of concept，而不是 SOTA performance：论文没有 event-wise accuracy、IoU、F1、baseline table、mean/std、repeated runs、convergence rate 或 initialization-sensitivity study。作者声称 patches 可并行、CPU 与 GPU speed comparable、network compact 且 memory consumption 低，但没有给出 runtime、wall-clock latency 或 memory 数字。这些不是 hardware-measured energy、neuromorphic hardware result 或已验证的 efficiency evidence。

## 6. Strengths and Limitations

Strengths：将 WTA-STDP Bayesian computation 落到真实 spatiotemporal event decoupling；建立 motion compensation、IWE contrast、soft assignment 与 local plasticity 的统一数据流；输出是 per-event soft responsibilities，而非仅粗糙 region mask；支持 chronological packets 的 online-learning 形式；作者主动承认 local convergence 与验证范围。

Limitations：算法高度依赖 TPE + SVD/K-means initialization；cluster count 和 motion-model type 必须先验指定；polarity 被丢弃；WTA/E-step 与 STDP/M-step 主要是形式及方向上的近似对应；output 被称为 IF neuron，却未给出 conventional threshold/reset dynamics；tensor-valued neuron、exclusive competition 与 neuromorphic mapping 不完整；packet/patch 和 temporal propagation 实现不足；实验只有少量 qualitative EED cases，不能支撑 robustness、competitive accuracy 或真实能效结论。

## 7. Relation to Other Papers and Survey Taxonomy

本文主要属于 event-based motion segmentation、motion compensation / contrast maximization、spike-based Bayesian computation、WTA circuit、STDP/local learning、online unsupervised learning、temporal modeling 与 neuromorphic vision。它区别于 ANN/SNN optical-flow regression：不是先预测 dense flow 再 segmentation，而是直接以 motion hypotheses warp events、以 IWE contrast 驱动 clustering。它也区别于常规 supervised SNN，不使用 labels、BPTT 或 surrogate-gradient classification loss。

在 efficiency and hardware taxonomy 中只能作为 neuromorphic motivation / open challenge：论文未报告真实 hardware、energy、latency 或 operation count。重要开放问题包括 robust initialization、自动确定 motion count/type、cluster birth/death、复杂非线性 motion、完整 tensor-neuron implementation 与 quantitative benchmarking。

## 8. Survey-Usable Takeaways

本文最有综述价值的贡献，是展示一种不同于“event representation + deep SNN”的路线：将 event motion segmentation 看成 Bayesian latent-variable inference，并以 WTA competition 近似 posterior responsibility、以 STDP-like plasticity 近似 contrast-maximizing parameter update。其结论应限制为 spike-based EM prototype 在少量 EED cases 上的可行性验证。TPE/SVD initialization 与 conventional warping/IWE computation 是方法不可忽略的组成，因此不能将结果概括为纯 local-STDP SNN 从 raw events 自动发现 motions，也不能从 event-driven 形式推导真实 hardware efficiency。

## Supplement Points

### Questions and Clarifications

#### 1. Dirac delta 是什么，为什么 IWE 写成加权 delta 之和？

Dirac delta $\delta(\mathbf{x} - \mathbf{x}_0)$ 不是普通有限高度函数，而是表示“全部质量集中在位置 $\mathbf{x}_0$”的理想 impulse：除 $\mathbf{x}_0$ 外取 0，对包含该位置的区域积分为 1。Event $e_k$ 经 model $j$ warp 到 $\mathbf{x}'_{kj}$ 后，

$$
p_{kj}\delta(\mathbf{x} - \mathbf{x}'_{kj})
$$

表示在该位置放入质量 $p_{kj}$。对所有 events 求和：

$$
I_j(\mathbf{x})
=
\sum_k p_{kj}\delta(\mathbf{x} - \mathbf{x}'_{kj}),
$$

就得到 motion model $j$ 的 IWE。实际 discrete image 中可理解为向相应 pixel bin 累加 $p_{kj}$；若位置非整数，可用 Gaussian 等 smooth kernel 分配到邻近 pixels。

例如三个 events 在 model $j$ 下都 warp 到 pixel $(5,4)$，responsibilities 为 $0.8$、$0.6$、$0.9$，则该 pixel 累积：

$$
I_j(5,4)
=
0.8 + 0.6 + 0.9
=
2.3.
$$

若 motion parameter 正确，来自同一 physical edge 的 events 会在 reference time 落到相同或相邻位置，形成清晰高峰；错误参数会把 impulses 摊到长条区域。

---

#### 2. 为什么 peaked IWE 的 variance 更大？两种 variance 公式为什么完全相同？

对包含 $M$ 个 pixels 的 IWE，均值为：

$$
\mu
=
\frac{1}{M}\sum_{r=1}^{M}I_r.
$$

Variance 的定义式为：

$$
\operatorname{Var}(I)
=
\frac{1}{M}
\sum_{r=1}^{M}
(I_r - \mu)^2.
$$

展开平方：

$$
\begin{aligned}
\operatorname{Var}(I)
&=
\frac{1}{M}\sum_r
(I_r^2 - 2I_r\mu + \mu^2)\\
&=
\frac{1}{M}\sum_r I_r^2
-2\mu\left(\frac{1}{M}\sum_rI_r\right)
+\mu^2\\
&=
\frac{1}{M}\sum_rI_r^2
-\mu^2.
\end{aligned}
$$

因此“与均值差的平方的平均”和“平方的平均减去均值的平方”是同一公式。

以 $I = [0,0,0,4]$ 为例，$\mu = 1$。定义式给出：

$$
\frac{(0 - 1)^2 + (0 - 1)^2 + (0 - 1)^2 + (4 - 1)^2}{4}
=
3.
$$

展开式给出：

$$
\frac{0^2 + 0^2 + 0^2 + 4^2}{4} - 1^2
=
4 - 1
=
3.
$$

对相同 total event mass，集中分布 $[0,0,0,4]$ 的 variance 为 3，而均匀分布 $[1,1,1,1]$ 的 variance 为 0。正确 warp 将许多 events 对齐到少数 edge pixels，使高值更高、其余位置接近 0，因此 pixel values 偏离均值更远。这个结论依赖比较时 image domain 和 event mass 可比；variance 大本身不保证一定是正确 object edge，噪声或不受控的质量变化也可能增大 variance。

---

#### 3. 一个 event 如何被所有 motion models warp、查询 IWE response 并得到 $p_{kj}$？

假设 event $e_k$ 位于 $\mathbf{x}_k = (7,5)$，有两个 motion hypotheses。分别 warp 后得到：

$$
\mathbf{x}'_{k1} = (4,5),
\qquad
\mathbf{x}'_{k2} = (7,2).
$$

Model 1 的 IWE 在 $(4,5)$ 处已有较多对齐 events：

$$
I_1(4,5) = 8.
$$

Model 2 的 IWE 在 $(7,2)$ 处响应较弱：

$$
I_2(7,2) = 2.
$$

“读取 IWE response”就是查询对应 warped pixel 的 intensity；若使用 smooth kernel，则可能是插值后的局部值。归一化得到：

$$
p_{k1}
=
\frac{8}{8 + 2}
=
0.8,
\qquad
p_{k2}
=
\frac{2}{8 + 2}
=
0.2.
$$

这表示在当前 parameters 和当前 IWE 下，event $e_k$ 更符合 motion model 1。它不是 ground-truth probability；若初始 parameters 错误，IWE response 与 responsibility 也可能错误，所以算法需要 EM-like iteration 并高度依赖初始化。

---

#### 4. WTA circuit、global inhibition、stochastic firing 和 tensor-valued neuron 是什么？

Winner-Take-All（WTA）是一组 hypotheses 之间的竞争机制。Hard WTA 只保留最大响应；soft/stochastic WTA 则令强响应更可能获胜，但不把其他 hypotheses 直接置零。

若三个 motion models 在同一位置的响应为：

$$
u_1 = 6,
\qquad
u_2 = 3,
\qquad
u_3 = 1,
$$

global inhibition 汇总：

$$
H = 6 + 3 + 1 = 10.
$$

本文的 stochastic firing probabilities 为：

$$
P(z_1 = 1) = 0.6,
\qquad
P(z_2 = 1) = 0.3,
\qquad
P(z_3 = 1) = 0.1.
$$

因此 strong model 获胜概率更高，同时所有 probabilities 归一化为 1，形式上对应 EM soft responsibilities。论文未说明是 categorical draw 还是分别进行 Bernoulli draws；若独立采样，可能出现多个 neurons 同时发放，因此严格的 mutual exclusion 为 `Needs further check`。

这里 $u_j$ 不是普通 IF neuron 的单个 scalar membrane potential，而是与 image/event space 对应的 tensor，即一张 motion-specific response map。Motion neuron $y_j$ 也不只是普通 scalar synaptic weight，而代表 receptive-field/warping function $\mathcal{W}_j(\cdot;\theta_j)$。STDP 更新的是该 function 的 coefficients，例如 linear motion 的 $(v_x,v_y)$。论文没有给出 conventional IF threshold/reset equation，也未说明这种 tensor neuron 如何映射到具体 neuromorphic cores：`Needs further check`。

---

#### 5. Section 3 的传统 EM 与 Section 4 的 WTA-STDP 到底如何对应？

Section 3 先给出传统 event-motion EM 作为参照：

$$
\theta
\rightarrow
\text{warp events}
\rightarrow
I_j
\rightarrow
P
\rightarrow
\theta'.
$$

固定当前 $\theta$ 时，E-step 构造 motion-specific IWEs，并根据各 IWE 在 event warped locations 的 response 更新 $p_{kj}$。固定 $P$ 时，M-step 更新 $\theta_j$，使 $\sum_j\operatorname{Var}(I_j)$ 增大。

Section 4 将相同流程改写为：

$$
\begin{aligned}
\text{motion neuron }y_j
&\longleftrightarrow
\text{warping model }\theta_j,\\
u_j
&\longleftrightarrow
I_j,\\
\text{WTA firing probability}
&\longleftrightarrow
p_{kj},\\
\text{STDP update}
&\longleftrightarrow
\text{M-step update of }\theta_j.
\end{aligned}
$$

一次具体迭代中，若某 event 对两个 models 的 responses 为 9 和 1，WTA 给出 $p_{k1} = 0.9$、$p_{k2} = 0.1$；该 event 主要更新 $\theta_1$，几乎不影响 $\theta_2$。更新后的 $\theta_1$ 若使 events 更集中，下一轮 $I_1$ contrast 与 $p_{k1}$ 会继续提高。

这里的“equivalent”应谨慎理解为 computation-role correspondence。论文没有证明 spike circuit 与标准 EM 具有相同 likelihood、逐步更新值或收敛点。

---

#### 6. 为什么作者说 STDP update 会提高 variance？证明到什么程度？

更新前后：

$$
\theta'_j
=
\theta_j+\Delta\theta_j,
\qquad
u'_j(k)
=
u_j(k)+\Delta u_j(k).
$$

当 $\Delta\theta_j$ 足够小时，一阶 Taylor approximation 为：

$$
\Delta u_j(k)
\approx
\frac{\partial u_j(k)}{\partial\theta_j}
\Delta\theta_j.
$$

忽略 $\Delta u_j(k)^2$ 等二阶项，variance change 为：

$$
\Delta\operatorname{Var}
\approx
\frac{2}{N}
\sum_k
\left(u_j(k)-\bar u_j\right)
\Delta u_j(k).
$$

代入一阶近似可写成：

$$
\Delta\operatorname{Var}
\approx
\nabla_{\theta_j}
\operatorname{Var}(u_j)^{\mathsf T}
\Delta\theta_j.
$$

所以 variance 增加的实际条件是：

$$
\nabla_{\theta_j}
\operatorname{Var}(u_j)^{\mathsf T}
\Delta\theta_j
>
0.
$$

即 gradient 与 update direction 的夹角小于 $90^\circ$，并且 step 足够小。论文直接假设其 STDP update 满足这一方向关系，却没有从公式（12）的 pre/post spike timing conditional probability 完整推导到公式（13）的 contrast-gradient-like update。因此这是一阶、条件性解释；Figure 3(b) 的 selected trajectory 提供案例支持，但不是 arbitrary initialization 下的 global convergence proof。

---

#### 7. TPE 是什么，本文如何用它搜索 motion parameters？

Tree-structured Parzen Estimator（TPE）是一种 Bayesian optimization 方法。本文搜索的主要不是 learning rate，而是每个 patch 的 candidate motion parameter。在线性模型下：

$$
\theta = (v_x,v_y),
\qquad
\theta^*
=
\arg\max_\theta
\operatorname{Var}(I(\theta)).
$$

对每次 trial，系统用候选 $(v_x,v_y)$ warp patch events、构造 IWE 并计算 variance。TPE 将已有 trials 按 objective quantile 分成 high-contrast good group 与 low-contrast bad group，并分别估计：

$$
\ell(\theta)
=
p(\theta\mid\text{good}),
\qquad
g(\theta)
=
p(\theta\mid\text{bad}).
$$

下一批候选倾向选择在 $\ell(\theta)$ 中常见、在 $g(\theta)$ 中少见的区域，直观上偏好较大的 $\ell(\theta)/g(\theta)$。例如 trials 显示 $(4,1)$、$(5,1)$、$(5,2)$ 产生高 variance，下一次可能在 $(4.8,1.3)$ 附近评估，而不是穷举整个 $(v_x,v_y)$ grid。

每个 patch 搜索出一个 candidate 后，若 patches 数 $N_{np} > N_\ell$，再用 SVD 或 K-means 从 candidates 中选出 $N_\ell$ 个 representative initial motions。TPE/SVD 解决“从哪里开始”，WTA/STDP 才解决“如何继续优化”。这也意味着方法不是仅靠 local STDP 从随机状态自动发现全部 motions。

---

#### 8. Event stream、packet 和 patch 是什么层级？“把 patches 输入网络”是什么意思？

数据层级为：

$$
\text{complete event stream}
\supset
\text{chronological packet}
\supset
\text{patch}.
$$

完整 stream 按固定 event count 切为：

$$
\mathcal{E}
=
\{\mathbf e^1,\mathbf e^2,\ldots,\mathbf e^{N_g}\}.
$$

例如仅为说明，若有 30,000 events、每 packet 10,000 个，则 $\mathbf e^1 = \{e_1,\ldots,e_{10000}\}$，$\mathbf e^2 = \{e_{10001},\ldots,e_{20000}\}$。论文没有给出实际 count。

第 $n$ 个 packet 又被拆成 local subsets：

$$
\mathbf e^n
=
\mathcal{P}_1^n
\cup
\cdots
\cup
\mathcal{P}_{N_{np}}^n.
$$

每个 patch 可能主要覆盖 background 或 moving object，使局部 contrast search 更容易发现不同 motions，也允许 patches 并行处理。“输入网络”指对 patch 内 asynchronous events 用每个 $\theta_j$ 执行 warping、IWE accumulation、WTA competition 与 STDP update，不是转换成 RGB frames 后送入 CNN。

论文没有说明 patch 是 image-grid、temporal slice、fixed-count subset 还是其他 space-time sampling，也未给出 overlap、event count 或 tensor dimensions：`Needs further check`。

---

#### 9. 上一 packet 的 motion 如何用于下一 packet initialization？

处理 packet $\mathbf e^n$ 后得到：

$$
\theta_n^*
=
\{\theta_{n,1}^*,\ldots,\theta_{n,N_\ell}^*\},
$$

以及 responsibilities $P_n$。因为相邻 packets 时间连续，作者用当前 motion estimate 预测下一 packet 的 cluster initialization，最直接的语义是：

$$
\theta_{n+1,j}^{\mathrm{init}}
\approx
\theta_{n,j}^*.
$$

例如 ball 在 packet $n$ 中的 estimate 为 $(5.0,1.0)$，packet $n+1$ 不从 $(0,0)$ 或随机值开始，而从 $(5.0,1.0)$ 附近继续 WTA-STDP optimization，可能更新到 $(5.2,0.9)$。这使 online tracking 不必对每个 packet 完全重新搜索。

论文只明确说 motions can be propagated in time，没有给出直接复制、constant-velocity extrapolation、smoothing 或其他 prediction formula，也没有说明 object birth/death、occlusion、cluster identity swap 和重新初始化机制。因此可以确认“上一 packet 为下一 packet提供起点”，但精确 propagation implementation 为 `Needs further check`。
