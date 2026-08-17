---
tags:
  - SNN
  - event-camera
  - adversarial-attack
  - raw-events
  - Gumbel-Softmax
  - robustness
---

# Summary V2｜Exploring Vulnerabilities in Spiking Neural Networks: Direct Adversarial Attacks on Raw Event Data

## 1. Core Understanding

本文研究 event-camera SNN 在 raw event interface 上的 adversarial vulnerability，而不是提出新的 SNN architecture。其核心问题是：许多系统只开放原始 COO event input，内部 grid representation 被封装在 pipeline 中，传统 grid-based attack 即使能生成 adversarial tensor，也未必能直接注入真实接口。

作者将可变长度 raw event set 重参数化为固定候选位置上的三状态变量：

$$
p_i\in\{-1,0,+1\},
$$

其中 $-1$ 和 $+1$ 表示两种 polarity，$0$ 表示该候选位置不存在事件。随后使用 Gumbel-Softmax 和 straight-through estimator（STE）优化这些离散状态，并通过 target-guided position selection 缩小搜索空间。实验表明，该方法在 strong white-box digital threat model 下能够有效生成 targeted adversarial raw events。

## 2. Problem and Motivation

Continuous grid attack 可以直接使用 FGSM 或 PGD 等连续优化方法；binary grid attack 则在固定 $0/1$ spike tensor 上执行 spike insertion 或 deletion。二者都绕开了 raw events 的微秒级时空结构、可变长度和稀疏集合约束。

Raw event attack 更困难，因为输入由 indices 与 values 共同构成：

$$
\mathcal{E}
=
\{(x_k,y_k,t_k,p_k)\}_{k=1}^{N},
$$

其中 polarity 为离散值，事件数量可变，完整候选时空空间极大。攻击既要提高 target-class probability，又要控制 event insertion、deletion、polarity flip 和最终 event count。作者因此定义 dense-event distance penalty，并将 adversarial event count 限制在合理范围内。

## 3. Method Overview

作者首先把原始样本与目标类别样本的时空位置合并：

$$
I_{\mathrm{cand}}
=
I_{\mathrm{original}}
\cup
I_{\mathrm{target}}.
$$

原始位置按真实 polarity 初始化，target-only positions 初始化为 $0$。每个候选位置再被编码为三分类 categorical parameter：

$$
\alpha_i
\in
\mathbb{R}^{3}.
$$

攻击过程中，Gumbel-Softmax 生成连续 soft sample，argmax 生成用于 forward 的 hard state。Hard states 被整理为合法 COO events，送入完整 raw-event-to-SNN pipeline。若预测已变为 target label，则提前返回；否则通过 SNN surrogate gradient、STE 和 Gumbel-Softmax derivative 更新 $\alpha$。

最终目标可概括为：

$$
\mathcal{L}
=
l\!\left(
\mathcal{F}_S(\mathcal{E}_{\mathrm{adv}}),
y
\right)
+
\lambda
\left\|
\mathcal{E}_{\mathrm{adv}}^{*}
-
\mathcal{E}_{0}^{*}
\right\|_1.
$$

第一项推动 targeted misclassification，第二项限制 event modifications。

## 4. Key Components and Mechanisms

### 4.1 Three-State Reparameterization

真实事件 polarity 只有 $-1$ 与 $+1$。本文引入的第三个状态 $0$ 不是第三种 polarity，而是 no-event state。该设计允许统一表示：

- event insertion：$0 \rightarrow \pm 1$；
- event deletion：$\pm 1 \rightarrow 0$；
- polarity flip：$+1 \leftrightarrow -1$。

因此，本文实际优化的是固定候选 indices 上的 event existence 与 polarity。

### 4.2 Gumbel-Softmax and STE

对第 $i$ 个候选位置，soft sample 为：

$$
\hat{p}_j^i
=
\frac{
\exp((\alpha_j^i+g_j)/\kappa)
}{
\sum_{l=0}^{2}
\exp((\alpha_l^i+g_l)/\kappa)
}.
$$

Forward 使用 hard argmax state，保证输入是合法离散事件；backward 则借助 STE 将梯度近似传回 soft probabilities 和 logits。攻击中因此存在两层梯度近似：输入端使用 Gumbel-Softmax 与 STE，SNN 内部使用 surrogate gradient。

### 4.3 Efficient Position Selection

完整微秒级时空空间难以直接优化。作者只保留原始事件位置和目标类别样本位置。原始位置提供可删除或翻转的事件，目标位置提供可添加的 target-class structure。该策略显著缩小搜索空间，但也引入较强 threat assumption：攻击者需要目标类别 raw-event sample。

### 4.4 Sparsity-Aware Constraint

Dense-event L1 penalty 对不同修改具有不同代价：

- insertion 或 deletion：代价为 1；
- polarity flip：代价为 2。

此外，event-count interval 控制最终非零事件数量。两者分别约束“改了多少”与“最终还有多少事件”，不能互相替代。

## 5. Experiments and Main Evidence

实验在 CIFAR10-DVS、DVS Gesture 和 N-MNIST 上进行，攻击对象为 SEW ResNet-34 与 Spiking ResNet-18。每个数据集随机选择 100 个 correctly classified samples，并进行 targeted attack。

在 raw-event attack 上，本文方法相较 modified FGSM 的 ASR 绝对提升约为 42–71 个百分点，六组结果平均提升约 55 个百分点，同时 MSE 和事件修改比例 $\Delta$ 更低。例如，DVS Gesture 上 SEW ResNet-34 的 ASR 从 15.56% 提升到 86.67%，$\Delta$ 从 64% 降到 19%。

在 binary-grid attack 上，本文明显优于 SpikeFool，并与 Spike-Compatible 接近，但六组比较中有五组略低于 Spike-Compatible。因此，它并非 binary-grid attack 的整体最优方法；其主要价值是能够输出 raw-event-compatible adversarial samples。

Table 5 显示 soft continuous attack 的 ASR 显著高于 hard discrete attack，多组达到 100%。这说明连续松弛空间中容易找到 adversarial solution，但量化为合法 $-1/0/+1$ 状态后会产生明显 performance gap。有效 raw-event attack 结论应以 hard result 为准。

## 6. Strengths and Limitations

**Strengths**

- 首次系统展示直接针对 SNN raw-event interface 的 gradient-based targeted attack。
- 将可变长度事件集合转化为固定候选位置上的 categorical optimization。
- 同时处理 event insertion、deletion 与 polarity flip。
- Target-guided position selection 显著压缩搜索空间。
- 在三个 DVS datasets 和两个 SNN architectures 上均显著优于 raw-event FGSM baseline。

**Limitations**

- 攻击依赖 white-box gradients、目标类别 event sample 和 raw-event modification capability。
- 仅验证 digital attack，未证明物理 event-camera perturbation 的可实现性。
- 每个数据集只评估 100 个样本，缺少更大规模、方差和多随机种子结果。
- $\Delta$ 的精确定义、polarity flip 计数方式与 FGSM 离散化过程说明不足。
- Soft ASR 不是合法 raw-event attack result。
- 搜索空间缩小具有结构依据，但正文没有系统报告 attack runtime 或 GPU memory benchmark。

## 7. Relation to Other Papers and Survey Taxonomy

本文属于 SNN for Event Cameras 综述中的 robustness and security 分支，可归入：

- **Raw-event adversarial attack**
- **Discrete spatiotemporal perturbation**
- **SNN white-box vulnerability**
- **Event-interface security**
- **Gumbel-Softmax-based discrete optimization**

与 SpikeFool 和 Spike-Compatible 相比，本文不是只在固定 binary spike tensor 上做 spike flips，而是直接生成可变长度 COO event list。它适合支撑一个重要结论：event discreteness 和 SNN spike dynamics 并不会天然带来 adversarial robustness，因为连续松弛、STE 和 surrogate gradient 仍可建立有效攻击路径。

### PDF-verified relation backfill

主要路线是把 raw-event insertion/deletion/polarity change 表为三状态离散变量，并用 Gumbel-Softmax、STE 和 SNN surrogate gradient 联合优化。

- **Adversarial Attacks on Spiking Convolutional Neural Networks for Event-based Vision (Jonas Büchel et al., arXiv 2021)** — `baseline`。该工作是 discrete spike/event adversarial perturbation 的实验 comparator；当前论文与其主要区别在于本文第 3–4 节所述的核心机制。 对应 Section 6: robustness and security。证据：Related Work 2 and Experiments, PDF pp.3 and 11, citation and bibliography [6]。 当前 active corpus 未覆盖。 值得 backward search。
- **Exploring Adversarial Attack in Spiking Neural Networks with Spike-Compatible Gradient (Ling Liang et al., TNNLS 2021)** — `baseline`。该工作是 binary spike tensor attack 的实验 comparator；当前论文与其主要区别在于本文第 3–4 节所述的核心机制。 对应 Section 6: robustness and security。证据：Related Work 2, PDF p.3, citation and bibliography [26]。 当前 active corpus 未覆盖。
- **Categorical Reparameterization with Gumbel-Softmax (Eric Jang et al., arXiv 2016)** — `foundation`。该工作提供 categorical relaxation for event edits 的基础机制；当前论文将其用于自身的 event/SNN pipeline，而不是把该前驱本身作为新贡献。 对应 Section 6: robustness and security。证据：Method 3.2, PDF pp.5-6, citation and bibliography [21]。 当前 active corpus 未覆盖。

## 8. Survey-Usable Takeaways

- Raw-event interface 本身是独立攻击面，不能只评估内部 grid representation 的鲁棒性。
- 本文把可变长度 event set 转换为 target-guided candidate positions 上的三状态 categorical variables。
- Gumbel-Softmax 与 STE 解决输入离散性，SNN surrogate gradient 解决神经元 firing 的不可导性。
- 主要实验结论是 raw-event ASR 显著高于 modified FGSM，而不是 binary-grid attack 全面优于 Spike-Compatible。
- 该工作证明的是 strong white-box digital vulnerability，不等同于可物理实现的 event-camera attack。

## Supplement Points

### Questions and Clarifications

#### Continuous grid representation attack 与 binary grid representation attack 分别如何构造？

Continuous grid 将事件聚合为实值 tensor，例如 event count、normalized timestamp 或 kernel response。由于输入值连续，可直接使用 FGSM、PGD 等方法：

$$
X_{\mathrm{adv}}
=
\Pi_{\mathcal{B}_{\epsilon}(X)}
\left[
X-\eta\operatorname{sign}
\left(
\nabla_X\mathcal{L}
\right)
\right].
$$

Binary grid 将输入表示为：

$$
X\in\{0,1\}^{T\times2\times H\times W},
$$

每个位置只表示该 temporal bin 是否出现对应 polarity spike。攻击操作为 $0 \rightarrow 1$ 或 $1 \rightarrow 0$，因此需要 rounding、spike-compatible gradient 或 heuristic spike flipping。

二者与 raw-event attack 的本质差异是：grid attack 操作固定尺寸 tensor；raw-event attack 还要处理微秒级 indices、可变 event count、polarity 和 COO sparsity。

#### Soft version 为什么能达到 100% ASR，而 hard version 明显较低？

Soft version 允许连续值，例如：

$$
p_i^{\mathrm{soft}}=0.43,
$$

而真实事件只能取 $-1,0,+1$。连续空间可以通过细微数值变化穿过 decision boundary；hard version 必须量化为离散状态，部分攻击方向会在 argmax 后消失。因此，Table 5 主要反映 continuous relaxation 与 executable discrete events 之间的 gap。Soft result 可视为优化上限或 vulnerability indicator，但不能作为合法 raw-event attack result。

#### Binary Grid Attack 是什么，本文方法如何用于 Binary Grid？

Binary grid attack 在固定 $0/1$ spatiotemporal tensor 上执行 spike insertion 或 deletion。本文方法可将每个位置的三分类 logits 简化为二分类 logits：

$$
\alpha_i
=
[\alpha_{i,0},\alpha_{i,1}].
$$

Gumbel-Softmax 产生 soft $0/1$ probabilities，argmax 产生 hard binary grid，STE 用于 backward。该版本不需要 candidate-index union、zero-state removal 或 COO reconstruction，因此比 raw-event attack 简单。论文报告了 binary-grid results，但主文没有完整展开实现细节，具体特化方式仍为 `Needs further check`。

#### SpikeFool 与 Spike-Compatible 有何区别？

SpikeFool 基于 DeepFool 与 SparseFool：先局部近似 decision boundary，再寻找稀疏连续扰动，最后通过 rounding 和 binary bounds 转成 spike flips。其主要问题是小连续更新在取整后可能消失，从而产生 gradient vanishing。

Spike-Compatible 直接将连续 spatiotemporal gradient 转换为合法 spike update。其 Gradient-to-Spike Converter 根据 gradient magnitude 概率筛选位置、保留 gradient sign，并限制更新后仍处于 binary domain；当梯度全部为零时，Restricted Spike Flipper 会随机翻转少量 spikes，帮助攻击跳出 zero-gradient region。它因此通常比 SpikeFool 更稳定，也在本文 binary-grid experiments 中整体表现更强。

### Additional Technical Details

#### Algorithm 1：采样攻击流程与维度变化

原始事件 indices 与 values 为：

$$
I_{\mathrm{original}}
\in
\mathbb{Z}^{N_0\times3},
\qquad
V_{\mathrm{original}}
\in
\{-1,+1\}^{N_0}.
$$

目标类别样本提供：

$$
I_{\mathrm{target}}
\in
\mathbb{Z}^{N_t\times3}.
$$

两者合并并去重后得到候选位置：

$$
I_{\mathrm{cand}}
=
I_{\mathrm{original}}
\cup
I_{\mathrm{target}}
\in
\mathbb{Z}^{K\times3},
$$

其中 $K\leq N_0+N_t$。

原始位置用真实 polarity 初始化，target-only positions 初始化为 0：

$$
v_i^{(0)}
=
\begin{cases}
p_i^{\mathrm{original}},
&
i\in I_{\mathrm{original}},
\\
0,
&
i\in I_{\mathrm{target}}
\setminus
I_{\mathrm{original}}.
\end{cases}
$$

因此初始状态为：

$$
V_{\mathrm{init}}
\in
\{-1,0,+1\}^{K}.
$$

三种状态被编码为 one-hot：

$$
-1\rightarrow[1,0,0],
\qquad
0\rightarrow[0,1,0],
\qquad
+1\rightarrow[0,0,1].
$$

由此初始化 categorical logits：

$$
\alpha
\in
\mathbb{R}^{K\times3}.
$$

每一轮外层优化中，在同一组 $\alpha$ 下进行 $M$ 次 Gumbel-Softmax sampling。第 $m$ 次采样得到：

$$
\hat{P}^{(m)}
\in
\mathbb{R}^{K\times3},
$$

以及 hard states：

$$
p^{(m)}
\in
\{-1,0,+1\}^{K}.
$$

Soft sample 用于 backward，hard state 用于 forward。去掉所有 $p_i^{(m)}=0$ 的候选位置后：

$$
N_{\mathrm{adv}}^{(m)}
=
\sum_{i=1}^{K}
\mathbf{1}
\left[
p_i^{(m)}\neq0
\right].
$$

最终构造：

$$
I_{\mathrm{adv}}^{(m)}
\in
\mathbb{Z}^{N_{\mathrm{adv}}^{(m)}\times3},
$$

$$
V_{\mathrm{adv}}^{(m)}
\in
\{-1,+1\}^{N_{\mathrm{adv}}^{(m)}}.
$$

每个 hard sample 都被送入完整 pipeline 并计算 targeted loss。若：

$$
\mathcal{F}_S
\left(
\mathcal{E}_{\mathrm{adv}}^{(m)}
\right)
=
y_{\mathrm{target}},
$$

则立即返回当前 adversarial sample，避免继续增加扰动。

若 $M$ 次采样均未成功，则通过 SNN surrogate gradient 和 STE 得到每次采样对 $\alpha$ 的近似梯度，并求平均：

$$
\delta_{\alpha}
=
\frac{1}{M}
\sum_{m=1}^{M}
\nabla_{\hat{P}^{(m)}}
\mathcal{L}^{(m)}
\frac{\partial\hat{P}^{(m)}}{\partial\alpha}.
$$

随后更新：

$$
\alpha
\leftarrow
\alpha
-
\gamma\delta_{\alpha}.
$$

完整维度流为：

```text
Original indices: N0 × 3
Target indices: Nt × 3
        ↓ merge / deduplicate
Candidate indices: K × 3
        ↓
Categorical logits α: K × 3
        ↓ Gumbel-Softmax
Soft samples: K × 3
        ↓ argmax
Hard states: K
        ↓ remove zero states
Adversarial COO events:
Nadv × 3 indices + Nadv polarity values
```

Algorithm 1 第 6 行似乎把每条样本的 event-value 数量写成 $M$，但 $M$ 是 sampling number；合理上限应为候选位置数量 $K$。此外，伪代码列出 $V_{\mathrm{target}}$，却没有清楚说明其实际用途。两处均为 `Needs further check`。

#### Modified FGSM 中将输出裁剪到 $[-1,+1]$ 的含义

Raw-event FGSM baseline 先执行连续梯度更新，再限制数值范围：

$$
V_{\mathrm{adv}}^{\mathrm{cont}}
=
\operatorname{clip}
\left(
V_0
-
\epsilon
\operatorname{sign}
\left(
\nabla_{V_0}\mathcal{L}
\right),
-1,
+1
\right).
$$

Clipping 只能防止数值越界，例如 $1.4 \rightarrow 1$，却不能保证结果属于合法离散集合。若更新后为 $0.72$，裁剪后仍是 $0.72$，但 raw-event polarity 必须为 $-1$ 或 $+1$，若允许 no-event state则还可为 0。论文没有充分说明 FGSM 结果如何进一步 sign、round 或 threshold，因此该 baseline 的离散合法化过程为 `Needs further check`。
