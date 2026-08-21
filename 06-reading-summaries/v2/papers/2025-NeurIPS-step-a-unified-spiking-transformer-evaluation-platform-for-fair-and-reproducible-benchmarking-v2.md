---
tags: [SNN, spiking-transformer, benchmarking, energy-efficiency, temporal-modeling, event-camera]
---

# Summary V2｜STEP: A Unified Spiking Transformer Evaluation Platform for Fair and Reproducible Benchmarking

## 1. Core Understanding

STEP 是一个用于 Spiking Transformer 的统一 benchmark framework，而不是一个新的单一网络。它把输入 encoding、spiking neuron、surrogate gradient、patch embedding、attention、MLP、task head 和 SNN backend 组织为可替换模块，并在统一或明确记录的训练协议下复现 Spikformer、SDT、QKFormer 等模型。

论文的核心结论不是“某一个 Spiking Transformer 达到最高 accuracy”，而是对现有模型的组成和效率重新审视：在当前代表性实现中，SPS convolutional frontend 承担了大部分视觉表征；可学习的 spike attention 对性能的边际贡献较小；模型在 serialized sequential data 上弱于 ANN counterparts，说明 temporal modeling 仍不充分；只用 AC/MAC 数量比较能效会高估 SNN 优势，量化 ANN 在纳入 bitwidth、稀疏性和 memory access 后可能更有竞争力。

STEP 覆盖 static、event-based 和 sequential inputs，支持 classification、segmentation、detection，并接入 SpikingJelly、BrainCog、BrainPy 以及 MMSegmentation/MMDetection 工具链。它是评估规范和诊断性分析平台，不能自动消除不同 backend、模型、数据预处理和资源预算之间的所有差异。

## 2. Problem and Motivation

现有 Spiking Transformer 论文通常同时改变模型实现、neuron、encoding、time steps、训练策略和 backend，导致 accuracy 与 energy 的横向比较缺少可解释性。STEP 试图固定评估接口和训练流程，再通过 module-wise ablation 分析每个组件的真实贡献。

论文特别关注三个问题。第一，Spiking Transformer 相对于 ANN 的独特优势是否主要出现在 temporal/event data，而不是静态图像。第二，模型的性能究竟来自 spike-native attention 和 temporal dynamics，还是来自普通 convolutional frontend。第三，SNN 的稀疏 binary computation 是否在完整系统 energy 上优于 quantized ANN。

## 3. Method Overview

STEP 的抽象数据流为：

$$
\mathrm{Input}
\rightarrow \mathrm{Encoding}
\rightarrow \mathrm{SPS/Patch\ Embedding}
\rightarrow \mathrm{Spiking\ Transformer\ Blocks}
\rightarrow \mathrm{Task\ Head}.
$$

静态图像、DVS event data 或 sequence 先被变成时间展开的输入，再进入 SPS。典型 block 使用 spiking attention 和 MLP，并通过 residual connection 传播 hidden states。分类使用 pooling 与 classification head；分割和检测分别接入 FCN/FPN 等 dense-prediction heads。

STEP 的四项设计原则是 modularity、dataset compatibility、multi-task adaptation 和 backend interoperability。最新版还声明支持 3D point cloud 与 PKU-DAVIS-SOD，但由于多数模型不兼容，这些数据没有纳入 unified evaluation；“支持接口”不能等同于“完成公平比较”。

## 4. Key Components and Mechanisms

### 4.1 Spiking encoding

论文比较 Direct、Phase、Rate 和 TTFS 四种 encoding。

Direct encoding 为 $S_t(p)=x(p)$，在每个 simulation step 重复完整 normalized intensity。它无损且与逐时间步独立计算的当前 Spiking Transformer 最匹配，但时间维不再承载新的输入信息，计算也会重复。

Phase encoding 将 $x(p)$ 量化为 8-bit integer，按时间循环访问 bit-plane，并用 $2^{-(b+1)}$ 加权。它把数值拆到不同 temporal phases，要求模型理解 phase 与 bit significance 的对应关系。

Rate encoding 使用 $S_t(p)\sim\mathrm{Bernoulli}(x(p))$，使平均 firing rate 表示强度。它具有随机稀疏性，但短时间窗口中的 rate estimation 不稳定。

TTFS 使用首次发放时间表示强度：强度越高，spike 越早；每个位置最多发放一次。论文用 $1/t^\star$ 缩放 spike amplitude 以保持不同 latency 的能量一致，也说明可改用 binary amplitude 1。TTFS 极其稀疏，但依赖模型解释 spike timing。

### 4.2 Spiking neurons

基本 LIF 执行 leak、integrate、fire、reset。PLIF 学习 membrane time constant，使不同 neuron 能适应不同 decay；CLIF 增加 complementary trace 以改善 threshold 附近的 surrogate gradient；GLIF 使用多个 gated internal states 表达 adaptation 和 refractory dynamics；KLIF 使用 learnable kernel constant 调整 leak behavior。正文的 neuron ablation 显示 PLIF 在三个 backbone 上提升最大，但“只增加一个 scalar parameter”的共享粒度需结合实现进一步核查。

### 4.3 Basic architecture

附录给出的典型结构为：

$$
X=\mathrm{SPS}(\mathrm{Input}),\quad
PE=\mathrm{SN}(\mathrm{BN}(\mathrm{Conv2d}(X))),\quad
X_0=X+PE.
$$

$$
X_l'=\mathrm{SpikingAttn}(X_{l-1})+X_{l-1},\quad
X_l=\mathrm{MLP}(X_l')+X_l',\quad
Y=\mathrm{Heads}(\mathrm{AP}(X_L)).
$$

SPS 通常由多个 Conv-BN-Pool-Spiking-Neuron stages 组成，完成局部特征提取、空间下采样、通道扩展和 token 化。位置编码也经过 Conv2d-BN-SN，而不是简单的连续可学习位置向量。该结构说明当前模型仍保留 ANN Transformer 的骨架，脉冲机制主要位于输入、activation 和 attention 路径。

### 4.4 Spiking attention

SDSA 的输入为 $Q,K,V\in\mathbb{R}^{B\times N\times C}$，先对 $Q$ 和 $K$ 做 element-wise outer-product 类型组合，再沿 channel 求和，经 spiking neuron 生成 binary spike map，最后与 $V$ 逐元素相乘：

$$
\mathrm{SDSA}(Q,K,V)=
\mathrm{SN}\left(\mathrm{SUM}_c(Q\otimes K)\right)\otimes V.
$$

它不是标准的 $N\times N$ softmax attention，而更像由 Q/K 产生 spike gate、由 V 提供内容。附录未完全说明 $\otimes$ 的广播规则和中间 tensor shape，属于 `Needs further check`。

Spikformer+SEMM 使用 mixture of experts。第 $i$ 个 expert 计算 $A_i=\mathrm{SSA}_i(Q_i,K,V)$，router 通过 $\mathrm{SN}(\mathrm{BN}(W_R^\top X))$ 生成 $r_i$，最终输出为：

$$
\mathrm{SSA+SEMM}=\sum_{i=1}^{m}r_iA_i.
$$

原文没有明确说明是否 top-k routing、inactive expert 是否真正跳过计算，不能仅据此断言 SEMM 已实现硬件级稀疏执行。

### 4.5 AC 与 MAC 的能耗抽象

ANN 的 dense linear layer 通常统计 MAC，因为每个权重和 activation 都要执行乘法再累加。SNN 的输入 spike 常为 $0/1$，当 $s_i=0$ 时可跳过 $w_i s_i$，当 $s_i=1$ 时只需把 $w_i$ 加入 accumulator，因此非零突触事件常被近似为 AC。SNN 并非没有乘法：attention、convolution、normalization、continuous membrane update 和量化/位级运算仍可能包含其他操作。

STEP 进一步指出，quantized ANN 也可通过 bit-serial execution 和 bit-level sparsity 跳过无效计算；而 SNN 需要跨多个 steps 读写高精度 membrane potential。更完整的总能耗应同时考虑 compute、memory access、state maintenance 和 routing。因此 AC/MAC 是 operation-count proxy，不是 hardware power measurement。

## 5. Experiments and Main Evidence

### 5.1 Reproduction and task scaling

在 CIFAR-10/100 上，STEP 使用统一 optimizer、learning rate、batch size、epochs 和 random seed，复现结果总体接近原论文。SGLFormer 因显存使用更小 batch；SpikingResformer 原本使用 transfer learning，而 STEP 使用 end-to-end training，因此“统一”仍受模型约束影响。

在 ImageNet-1K 上只评估 Spikformer 与 QKFormer 两个 architectural endpoints。由于显存和计算预算不同，保留各自 published regime：QKFormer 为 200 epochs、32 samples/GPU，Spikformer 为 300 epochs、24 samples/GPU。QKFormer 采用 compact variant 且未使用 architecture-specific optimization，结果低于原论文，说明该比较是 resource-aware reproduction 而非完全相同训练预算的严格因果比较。

ADE20K 上无预训练重训 Spikformer、Spikformer+SEMM 和 SDT；前两者超过 SDT。COCO 只评估具有真实 multi-scale outputs 的 SDTv2：从 scratch 的 box mAP@0.5 为 1.7，使用 ImageNet pre-training 后为 10.5；segmentation mAP@0.5 从 1.6 提升到 10.4。作者据此认为 detection 比 segmentation 更依赖 multi-scale backbone、object-level cues 和 pre-training。

### 5.2 分析实验的关键结论

1. **Neuron dynamics 很重要。** PLIF、CLIF、GLIF、KLIF 替换 LIF 后，三个 backbone 都出现提升，说明性能显著依赖 membrane decay、gating、internal state 和 surrogate-gradient dynamics，而不只是依赖显式 temporal module。

2. **当前模型更擅长 spatial modeling，而不是 long-range temporal modeling。** 在 sMNIST、psMNIST、sCIFAR 上，Spiking Transformer 落后于 ViT+SPS、SMPConv 等 ANN。作者推测 restricted training steps 和 sparse activation 削弱了 temporal expressiveness。

3. **Direct encoding 的优势暴露了当前模型的时间弱点。** Direct 在 CIFAR-10 上明显高于 Phase、Rate、TTFS，因为它每个 step 都提供完整空间输入；稀疏 temporal encoding 需要更强的 temporal-aware attention 或 recurrent mechanism 才能被有效解释。

4. **可学习的 Q/K 贡献有限，但不能据此说 attention 完全无用。** 随机冻结 Q/K 后，Spikformer、SDT 和 Spikformer+SEMM 的 accuracy drop 小于 0.35%，而 ViT 明显下降。该证据支持“当前可学习 Q/K 的边际贡献很小”，不等于所有 attention computation 没有作用。

5. **SPS convolutional frontend 是主要视觉表征来源。** 将 SPS 从四层 convolution 减至两层或一层后，性能大幅下降；一层时模型接近纯 attention-based SNN。用 SDSA-v3 加强 attention 只能缩小差距，不能消除对 convolution depth 的依赖。

6. **当前模型更像 convolution-dominant、attention-assisted 的 hybrid。** 三组实验共同表明，许多现有 Spiking Transformer 的主要视觉能力仍来自 ANN-style convolutional preprocessing，spike attention 尚未承担足够强的独立空间建模功能。

7. **传统 AC/MAC 比较会高估 SNN 能效优势。** 量化 ANN 同样可以利用 bit-level sparsity，SNN 还需要多步维护 membrane state；只看 AC 与 MAC 时的计算小优势，在纳入 memory access 后可能被抵消。

8. **量化 ANN 可能具有相当甚至更好的总能效。** 这是 analytical energy model 的结论，不是 neuromorphic hardware power measurement。它要求在相同硬件、位宽、稀疏性、模型规模和 memory hierarchy 假设下比较。

9. **需要 spike-native architecture。** 作者认为直接移植 ANN convolution/attention 没有充分利用 dendritic computation、STDP、temporal coding、多区室状态等神经科学机制，未来应从“脉冲化 ANN 模块”转向以 spike timing 和 neuron dynamics 为核心的架构。

## 6. Strengths and Limitations

**Strengths**

- 统一了多个模型、数据类型和任务的评估入口，并把 implementation differences 显式记录出来。
- 不只报告 accuracy，还用 encoding、neuron、attention、SPS depth 和 sequential tasks 诊断模型到底依赖什么。
- 将量化 ANN、bitwidth 和 memory access 纳入 SNN energy discussion，纠正单纯 AC/MAC proxy 的过强结论。
- 对 static、event-based 和 sequential data 的区分有助于识别“空间能力”与“时间能力”。

**Limitations**

- 统一协议受显存、原论文训练 regime 和模型兼容性限制；ImageNet 比较并非完全相同的 batch/epoch budget。
- 真实 event-driven hardware 结果并非本文核心证据；大多数 event-based 或复杂任务结论仍依赖 time-stepped simulation 或软件评估。
- 随机 Q/K 实验只能证明可学习 Q/K 的边际贡献小，不能单独证明 attention 没有功能。
- energy 结论是 analytical/operation-and-memory estimate，不是完整芯片功耗、延迟和吞吐测量。
- 当前附录没有完全给出 SDSA 的广播规则、SEMM 的实际 expert skipping，以及各 backend 的 state/reset 一致性；这些实现边界需要代码核查。

## 7. Relation to Other Papers and Survey Taxonomy

### PDF-verified literature relations

- **Spikformer: When Spiking Neural Network Meets Transformer (Zhou et al., arXiv 2022)** — `foundation`; STEP 将其作为早期代表性 Spiking Transformer 和 attention baseline，复现并通过 randomized attention、SPS depth 与 encoding ablations 分析其真正贡献。证据：Sections 4–5、Appendix A.3–A.4，PDF pp. 4–8、21–23，citation [9]，并映射至 source PDF bibliography [9]。
- **Spike-Driven Transformer (Yao et al., NeurIPS 2023)** — `baseline`; STEP 将 SDT 作为降低 attention complexity 的代表 baseline，并在 CIFAR、ADE20K、sequence modeling 和 attention ablations 中比较；SDTv2 进一步用于 COCO detection。证据：Sections 4–5，PDF pp. 4–8，citation [12]，并映射至 source PDF bibliography [12]。
- **QKFormer: Hierarchical Spiking Transformer Using QK Attention (Zhou et al., arXiv 2024)** — `baseline`; STEP 将 QKFormer 作为引入 hierarchical pyramid、并在 ImageNet reproduction 中作为高准确率 architectural endpoint 的代表模型。证据：Sections 4.1–4.2.1，PDF pp. 4–5，citation [10]，并映射至 source PDF bibliography [10]。

Survey taxonomy：benchmarking/evaluation；Spiking Transformer architecture analysis；temporal modeling diagnosis；SNN-versus-quantized-ANN efficiency；static/event/sequential cross-domain evaluation。

## 8. Survey-Usable Takeaways

- 评估 Spiking Transformer 时，必须把 static image accuracy、event-stream processing 和 genuine sequential modeling 分开；静态输入重复 $T$ 次不能证明时间建模能力。
- “spike attention”不等于 attention 已经承担主要表征；STEP 的 randomized Q/K、SPS-depth 和 SDSA-v3 实验共同提示当前模型仍是 convolution-dominant hybrid。
- Direct encoding 的高 accuracy 不能直接转化为高 efficiency；它重复完整输入，可能增加 temporal computation。
- SNN efficiency 应报告证据类型：AC/MAC proxy、spike sparsity、GPU runtime、memory-aware estimate 或真实 hardware measurement，不能将其中一种替代另一种。
- 对 event-camera review 而言，STEP 的价值主要是提供评估警示：统一 task protocol、encoding、time steps、state handling、memory assumptions 后，才有意义比较 SNN 与 quantized ANN。

## Supplement Points

### Questions and Clarifications

- **为什么传统 SNN 能耗通常统计 AC，而 ANN 统计 MAC？SNN 里面没有乘法吗？**

  ANN 的线性层计算 $y=\sum_i w_i x_i$。每一项通常需要 multiplication 后再 accumulation，因此用 MAC 表示。SNN 的突触输入常写为 $I[t]=\sum_i w_i s_i[t]$，其中 $s_i[t]\in\{0,1\}$。当 $s_i[t]=0$ 时可以跳过该连接；当 $s_i[t]=1$ 时，只需把已经存储的 $w_i$ 加入 accumulator。因此在假设硬件能够跳过 zero spikes 时，非零 spike 常被近似为一次 AC。

  SNN 并不是没有 multiplication。连续权重仍需要读取；attention 中的 $QK^\top$、convolution、normalization、continuous membrane update、量化和位级运算也可能包含乘法或其他操作。AC/MAC 只是把主要突触计算抽象成两种 operation，不代表整个网络只有 AC 或 MAC。

  例如 $w=[2.3,-1.1,0.7,4.0]$、$s=[1,0,1,0]$ 时，输出只需要累加 $2.3+0.7$；但如果 spike 为非二值、权重也需要乘法，或者硬件不能利用 sparsity，就不能直接使用理想 AC 计数。STEP 的贡献在于进一步加入 quantized ANN 的 bit-level sparsity，以及 SNN 的 membrane-state 和 memory-access cost。

- **附录 A 的四个部分分别是什么？**

  A.1 Spiking Encoding 说明 static RGB intensity 如何被映射到时间上的 spike train；A.2 Spiking Neuron 说明 LIF 及其变体如何更新 membrane state；A.3 Model Basic Architecture 说明 SPS、position embedding、spiking attention、MLP 和 task head 如何连接；A.4 Spiking Attention 说明 SDSA 与 Spikformer+SEMM 的具体计算。它们分别回答“输入如何变成 spike”“neuron 如何产生 spike”“网络如何组装”和“attention 如何在 spike domain 中工作”。

### Additional Technical Details

#### 1. 四种 Spiking Encoding 的技术细节

**Direct encoding**：

$$
S_t(p)=x(p),\qquad t=1,\ldots,T.
$$

归一化 intensity 在每个 step 重复注入。若 $x(p)=0.8$，则四个 step 都收到 $0.8$。这保留完整强度信息，但不是由时间编码新信息；它更像把同一输入重复送入 recurrent/spiking computation。

**Phase encoding**：先量化为 $v(p)=\lfloor256x(p)\rfloor$，再循环访问 8 个 bit-plane：

$$
S_t(p)=
\begin{cases}
2^{-(b+1)}, & v_{7-b}(p)=1,\
0, & \text{otherwise},
\end{cases}
\qquad b\equiv(t-1)\pmod 8.
$$

时间位置决定当前查看哪一位，high bit 权重大，low bit 权重小。因此模型必须同时理解 spike 是否出现和当前 phase 的 bit significance。

**Rate encoding**：

$$
S_t(p)\sim\operatorname{Bernoulli}(x(p)),\qquad
\mathbb E[S_t(p)]=x(p).
$$

强度通过 firing frequency 表示。若 $x(p)=0.75$、$T=16$，期望 spike 数是 $12$，但一次实际采样可能得到 $11$；解码 rate 是 $11/16=0.6875$。只有在更长窗口上，平均 rate 才更稳定。

**TTFS encoding**：

$$
t^\star(p)=1+\left\lfloor(1-x(p))T\right\rfloor,
$$

$$
S_t(p)=
\begin{cases}
1/t^\star(p), & t=t^\star(p),\\
0, & \text{otherwise}.
\end{cases}
$$

每个位置最多发放一次，强度越大，首次 spike 越早。$1/t^\star$ 是作者为不同 latency 设置的 amplitude scaling；作者也允许使用 amplitude 1。TTFS 极其稀疏，但要求网络保留并解释时间顺序。

#### 2. 五类 Spiking Neuron 的机制

- **LIF**：固定 time constant 的 leak-integrate-fire-reset 循环，累积输入、衰减 membrane potential、超过 threshold 发放，再 reset。
- **PLIF**：将 membrane time constant 设为可学习参数，使不同 neuron 或实现粒度下的 decay dynamics 可以通过训练适应数据。
- **CLIF**：增加 complementary trace，使 threshold crossing 附近的 surrogate-gradient 更平滑，重点是改善 gradient flow，而不是单纯增加 feature width。
- **GLIF**：使用多个 gated internal states，表达 adaptation、refractory process 和多种时间动态。
- **KLIF**：用 learnable kernel constant 调整 leak kernel，在生物合理性与计算效率之间寻找更合适的 decay。

正文表 3 的直接证据是增强型 neuron 在三个 backbone 上带来 accuracy gains，PLIF 提升最大。作者将其解释为 intrinsic neuron dynamics 比显式 temporal module 更重要；但若要严格证明两者的相对贡献，还需要相同参数和训练预算下的显式 temporal-module 对照。PLIF 的“一个 scalar parameter”具体是每 neuron、channel、layer 还是全局共享，当前文本未说明：`Needs further check`。

#### 3. Model Basic Architecture 的 forward data flow

附录公式为：

$$
X=\operatorname{SPS}(\operatorname{Input}),\quad
PE=\operatorname{SN}(\operatorname{BN}(\operatorname{Conv2d}(X))),\quad
X_0=X+PE.
$$

$$
X_l'=\operatorname{SpikingAttn}(X_{l-1})+X_{l-1},\quad
X_l=\operatorname{MLP}(X_l')+X_l',\quad
Y=\operatorname{Heads}(\operatorname{AP}(X_L)).
$$

SPS 的每个 stage 是 Conv-BN-Pool-Spiking-Neuron：Conv 提取局部特征，BN 稳定数值，Pool 降低空间分辨率，SN 将连续 activation 转为脉冲/状态表示。多个 stage 逐步把 image feature map 转成 token feature map，同时通常增加 channel width。

Position embedding 不是简单查表向量，而是由 Conv2d-BN-SN 生成，再和 $X$ 相加。随后每个 residual block 先做 spiking attention，再做 MLP；两者都通过 residual path 保留前一层表示。最后 average pooling 将最终 feature map/token representation 聚合，再由 classification、segmentation 或 detection head 输出任务结果。

因此，当前模型的数据流更接近“卷积完成主要视觉预处理，脉冲 attention/MLP 在其上做交互和变换”，而不是从 raw pixels 开始完全由 spike attention 建立视觉表征。

#### 4. SDSA 的技术细节与未决维度

附录给出 $Q,K,V\in\mathbb R^{B\times N\times C}$。SDSA 不是标准的 $QK^\top$ 加 softmax，而是：

$$
Q,K
\rightarrow Q\otimes K
\rightarrow \operatorname{SUM}_c(Q\otimes K)
\rightarrow \operatorname{SN}(\cdot)
\rightarrow \text{binary spike map}
\rightarrow \otimes V.
$$

公式为：

$$
\operatorname{SDSA}(Q,K,V)=
\operatorname{SN}\left(\operatorname{SUM}_c(Q\otimes K)\right)\otimes V.
$$

直观上，Q/K 生成决定哪些位置或通道被激活的 spike gate，V 提供被保留或调制的 feature content。它可能避免显式构造 $N\times N$ attention matrix，但附录没有说明 element-wise outer product 的确切广播规则、intermediate tensor shape 和是否跨 token 交互：`Needs further check`。

#### 5. Spikformer+SEMM 的技术细节

SEMM 是 mixture-of-experts attention。每个 expert 有 private query $Q_i$，共享 $K,V$：

$$
A_i=\operatorname{SSA}_i(Q_i,K,V).
$$

Router 对输入 $X$ 做 linear projection、BN 和 spiking activation：

$$
\operatorname{Router}=\operatorname{SN}\left(\operatorname{BN}(W_R^\top X)\right)
=\{r_1,\ldots,r_m\}.
$$

最终融合为：

$$
\operatorname{SSA+SEMM}=\sum_{i=1}^{m}r_iA_i.
$$

这表示 router 的 spike coefficients 控制各 expert 输出的贡献。但原文没有明确 $r_i$ 是否严格 binary、是否 top-k、inactive expert 是否跳过 forward、以及硬件是否真正只计算 active experts。因此 SEMM 的“稀疏”不能直接等价于实际 energy saving。

#### 6. 分析实验的关键结论（不是实验配置）

1. **Neuron dynamics 很重要。** PLIF、CLIF、GLIF、KLIF 替换 LIF 后，三个 backbone 都提升，说明 membrane decay、gating、internal state 和 surrogate-gradient dynamics 对性能有实际影响。

2. **当前模型偏 spatial modeling。** 在 sMNIST、psMNIST、sCIFAR 上落后 ANN counterparts，说明当前 spike attention 尚不足以处理长距离 temporal dependency。作者推测 restricted training steps 和 sparse activation 削弱 temporal expressiveness。

3. **Direct encoding 暴露 temporal weakness。** Direct 每个 step 都提供完整 image，所以和当前 attention independently/comparatively processed 的结构最匹配；Phase、Rate、TTFS 的性能下降说明模型尚未充分利用 spike timing 和跨时间稀疏信息。

4. **可学习 Q/K 的边际贡献很小。** 随机冻结 Q/K 后，三个 Spiking Transformer 的 accuracy drop 小于 $0.35\%$，而 ViT 明显下降。严格结论是 learned Q/K contribution limited，不是 attention 完全无用。

5. **SPS convolutional frontend 主导视觉表征。** SPS 从四层减少到两层或一层时性能显著下降，一层时近似纯 attention-based SNN，说明主要 representation power 仍在 convolutional preprocessing。

6. **加强 attention 不能替代 convolution。** SDSA-v3 可以缩小差距，却不能消除 accuracy 与 SPS convolution depth 的正相关，说明当前 spike attention 的独立 spatial modeling capacity 仍有限。

7. **整体上是 convolution-dominant、attention-assisted hybrid。** randomized Q/K、reduced SPS depth 和 stronger SDSA 三组实验共同支持这一判断，但不能外推到所有未来 spike-native Transformer。

8. **AC/MAC proxy 会高估 SNN 的 efficiency advantage。** quantized ANN 也可利用 bit-level sparsity；SNN 还要在多个 step 中维护 membrane state。计算操作的小优势可能被 memory access 和 state maintenance 抵消。

9. **需要 spike-native architecture。** 作者因此提出探索 dendritic computation、STDP、temporal coding、多区室 neuron 和 hybrid recurrent-spiking mechanism，而不是继续直接移植 ANN attention/convolution。

#### 7. 效率结论的证据边界

本文的 energy 结果属于 analytical/operation-and-memory estimate。它不是 neuromorphic hardware power measurement，也不是 wall-clock latency 或 throughput benchmark。参数量、spike sparsity、AC/MAC 数量和估算 energy 必须分开报告。

如果要把 SNN 与 quantized ANN 公平比较，至少需要明确：模型规模、bitwidth、spike sparsity、AC/MAC 定义、SRAM/DRAM/register access cost、membrane potential precision、权重是否重复读取、routing 是否计入，以及使用的 hardware energy constants。当前附录 B 的表格和正文没有把这些假设全部展开：`Needs further check`。
