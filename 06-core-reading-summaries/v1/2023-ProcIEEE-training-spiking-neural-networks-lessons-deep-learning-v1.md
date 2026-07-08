---
title: "Training Spiking Neural Networks Using Lessons From Deep Learning"
authors: ["Jason K. Eshraghian", "Max Ward", "Emre O. Neftci", "Xinxin Wang", "Gregor Lenz", "Girish Dwivedi", "Mohammed Bennamoun", "Doo Seok Jeong", "Wei D. Lu"]
year: 2023
venue: "Proceedings of the IEEE"
level: "C"
priority: "manual extra"
advisor_track: "not in current core reading plan"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "Manual user-provided PDF; not listed in 00-index/reading-plan-core.md at generation time"
official_page: "https://doi.org/10.1109/JPROC.2023.3308088"
pdf_link: "https://doi.org/10.1109/JPROC.2023.3308088"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["SNN", "training", "surrogate gradient", "BPTT", "online learning", "STDP", "snnTorch", "manual extra"]
---

# Summary V1｜Training Spiking Neural Networks Using Lessons From Deep Learning

## 1. One-sentence Summary

这篇 tutorial/perspective 系统总结了如何借鉴 deep learning 的 gradient descent、backpropagation、loss design 和 software tooling 来训练 Spiking Neural Networks，并讨论 surrogate gradients、BPTT、online learning 与 STDP 之间的关系。

## 2. Research Problem

本文关注 SNN training 的核心困难：spikes 是离散事件，spike generation function 不可微；神经元状态具有时间递归性，导致 temporal credit assignment 困难；同时，面向 neuromorphic hardware 的 online/local learning 又不容易与 deep learning 中高性能的 global error optimization 兼容。

这个问题对 SNN for event cameras 很重要，因为 event cameras 自然输出 asynchronous events，常被视为适合 SNN 的输入模态。但是，如果没有可靠训练方法，event-based SNN 很难在 detection、tracking、recognition 等任务上与 ANN 或 hybrid ANN-SNN 方法竞争。

## 3. Background and Motivation

论文把 neuromorphic systems 分为 sensors、SNN algorithms 和 neuromorphic hardware。event cameras / Dynamic Vision Sensors (DVS) 被作为 neuromorphic sensor 的代表之一，它们输出 sparse events，而不是固定帧率图像。

作者的动机不是提出一个新的 event-camera model，而是为 SNN training 建立从 deep learning 到 spiking computation 的桥梁。文章讨论 spike encoding、output decoding、loss functions、surrogate gradient learning、ANN-to-SNN conversion、spike-timing-based learning、online learning 和 biologically inspired plasticity。

## 4. Method Overview

本文是 tutorial/review-style paper，不是单一模型。它的“方法”是组织一套 SNN training framework：先说明 input encoding 如何把 continuous values 或 event streams 转成 spikes；再说明 spiking neuron dynamics 如何在时间上积分输入并触发 spikes；然后讨论如何定义 output decoding 和 loss；最后比较 conversion、surrogate gradient、BPTT、online learning 等训练范式。

输入数据类型可以是 conventional data encoded as spike trains，也可以是 neuromorphic sensor events。event representation 方面，文章介绍 rate coding、latency/temporal coding 和 delta modulation 等。SNN component 主要围绕 spiking neuron model、membrane potential、threshold firing 和 reset mechanism。输出可以通过 spike count、firing rate、first spike time、population coding 或 membrane potential 来解码。

## 5. Technical Details

### Event Representation

文章介绍多种 spike encoding。rate coding 用 firing rate 表示强度，易于与 ANN activation 类比，但可能需要较长时间窗。latency/temporal coding 用 spike timing 表示信息，潜在 latency 更低。delta modulation 只在信号变化超过阈值时发放 spikes，与 event-camera 的 brightness-change events 有概念上的相似性。

### Spiking Neuron / SNN Module

论文以 spiking neuron dynamics 为中心解释 SNN。神经元接收 spike input 后更新 membrane potential；当 membrane potential 超过 threshold 时产生 output spike，并发生 reset 或 refractory behavior。由于 spike function 在 threshold 处不连续，直接 backpropagation 会遇到 zero/undefined gradient。

### Network Architecture

本文不提出固定 architecture，而是讨论 feedforward SNN、recurrent SNN、convolutional SNN，以及从 ANN 转换到 SNN 的网络。作者强调 SNN 的时间维既可以作为 computation unfolding 的维度，也可以承载 temporal information。

### Training Strategy

文章比较三类主要训练策略。ANN-to-SNN conversion 先训练 ANN，再将 activations 映射为 firing rates 或 thresholds，优点是可利用成熟 ANN training，缺点是通常需要较长 inference time 或 calibration。spike-time gradients 直接针对 spike timing 优化，但适用条件较严格。surrogate gradient learning 在 forward pass 使用真实 spike，在 backward pass 用平滑函数近似 spike derivative，是当前 deep SNN training 的常用路线。

### Loss Function

论文讨论 cross-entropy spike rate loss、mean-square spike rate loss、membrane-potential-based loss 和 spike-time-based loss。核心观点是，loss 的选择隐含了输出解码假设：如果用 spike count / rate 做分类，则 loss 通常鼓励正确类别 firing rate 更高；如果用 first-spike 或 spike-time objective，则 loss 更直接约束时间延迟。

### Inference Process

SNN 推理通常沿时间展开。输入 spike train 逐步进入网络，神经元状态随时间更新，输出层通过 firing rate、spike count、first spike time 或 membrane potential 产生最终预测。文章提醒，energy/latency claims 需要结合 time steps、spike sparsity、hardware 和 data movement 共同判断。

## 6. Experiments

本文主要是 tutorial and perspective，不以单一 benchmark 实验为主。它引用多个 datasets 和 prior works 来说明 SNN training 的应用场景，包括 neuromorphic vision datasets、event-camera datasets 和非视觉数据。

论文中 Table 1 汇总了 neuromorphic datasets 的例子，其中包含由 event cameras 或 cochlear-style sensors 记录的数据。正文还通过 snnTorch tutorials 和 prior SNN papers 说明 surrogate gradients、BPTT 和 online learning 的实际训练方式。

由于本文不是新的 empirical benchmark paper，不能把它当作某个模型在某个 event-camera task 上的 SOTA 证据。它更适合作为 survey 中解释 SNN training taxonomy、surrogate gradients 和 temporal credit assignment 的背景材料。

## 7. Main Contributions

1. 系统梳理 deep learning 训练思想如何迁移到 SNN，包括 gradient descent、backpropagation、loss design 和 software abstractions。
2. 清晰解释 SNN training 的关键困难：non-differentiable spike function、spatial credit assignment、temporal credit assignment 和 dead neuron problem。
3. 总结 ANN-to-SNN conversion、spike-time learning、surrogate gradient learning 和 BPTT 的关系。
4. 讨论 online learning、RTRL、e-prop、DECOLLE、OSTL、ETLP、OSTTP 和 FPTT 等更具 temporal locality 的训练路线。
5. 将 surrogate-gradient/BPTT updates 与 STDP-style plasticity 建立概念联系，并讨论 future directions。

## 8. Limitations and Risks

本文不是 event-camera-specific paper，也不是 empirical SOTA paper；survey 中不能用它支持某个 event-camera benchmark 上的性能结论。

作为 tutorial/perspective，它覆盖范围很广，但许多方法的细节需要回到原论文核对。例如 e-prop、DECOLLE、ANN-to-SNN conversion 和 surrogate gradient 的具体假设差异，不能只依赖本文摘要式描述。

文章讨论 energy efficiency 时主要是概念性和条件性的；实际能耗依赖 neuromorphic hardware、time steps、data movement 和 implementation，因此 survey 中应避免泛化为“SNN 必然更省电”。

本文与 snnTorch 生态联系紧密，可能更偏向 gradient-based deep SNN training 的教学表达；V2 阶段可补充其他框架或 hardware-oriented 视角。

## 9. Relation to SNN for Event Cameras

分类：C: SNN side background；manual extra。

本文本身不提出 event-camera model，但它解释了 event-camera SNN papers 常用的训练概念：surrogate gradient、BPTT、spike encoding、output decoding、temporal credit assignment 和 online learning。它适合放在 survey 的 SNN training background 部分，用来支撑为什么 event-based SNN 需要特殊训练策略。

## 10. Relation to Survey Taxonomy

- SNN training methods：核心背景材料。
- Surrogate gradient and temporal credit assignment：重点相关。
- Event representations for SNNs：通过 spike encoding / delta modulation 提供背景。
- Hybrid ANN-SNN models：涉及 ANN-to-SNN conversion 和 deep learning lessons。
- Efficiency, latency, and energy：提供概念框架，但需要结合硬件证据。
- Open challenges：dead neurons、vanishing gradients、online/local learning、hardware-aware training。

## 11. Key Terms and Concepts

- surrogate gradient：forward pass 使用 hard spike，backward pass 用平滑近似替代 spike derivative。
- BPTT：Backpropagation Through Time，将 recurrent temporal dynamics 展开后反传梯度。
- temporal credit assignment：判断不同时刻的 state/spike 对最终 loss 的贡献。
- dead neuron problem：神经元长期不发放 spikes，导致梯度信号不足或学习停滞。
- ANN-to-SNN conversion：先训练 ANN，再映射成 SNN 的方法。
- STDP：Spike-Timing-Dependent Plasticity，根据 pre/post spike timing 调整 synaptic weights。
- e-prop / DECOLLE / OSTL：面向 online/local SNN learning 的方法家族。
- snnTorch：论文相关的 PyTorch-based SNN teaching and research toolkit。

## 12. Questions for Human Deep Reading

1. 本文对 surrogate gradient 的定义与 event-camera SNN papers 中实际使用的 surrogate functions 是否一致？
2. 文章讨论的 dead neuron problem 在 sparse event-camera inputs 中是否更严重？
3. rate coding、latency coding 和 delta modulation 哪一种最适合解释 event-camera SNN 输入？
4. ANN-to-SNN conversion 对 event-camera tasks 的限制是否比 frame-based tasks 更明显？
5. BPTT 的 memory cost 与 event-stream 长序列处理之间有什么冲突？
6. online learning methods 是否已有成功的 event-camera detection/tracking 应用？
7. STDP 与 surrogate-gradient updates 的联系在 survey 中应作为直觉类比还是理论结论？
8. 文章关于 energy efficiency 的表述是否有硬件实验支撑，还是主要来自 neuromorphic computing 的一般预期？
9. snnTorch tutorials 中的 examples 是否可作为 survey reproducibility resource 引用？

## 13. Evidence Notes

- Abstract：说明文章目标是从 deep learning、gradient descent、backpropagation 和 neuroscience 中总结 SNN training lessons。
- Section I：介绍 neuromorphic computing、SNN algorithms、neuromorphic sensors 和 hardware 的背景。
- Table 1：列出 neuromorphic datasets，其中包含 event-camera / DVS 类数据。
- Encoding sections：讨论 rate coding、latency/temporal coding 和 delta modulation。
- Training sections：讨论 ANN-to-SNN conversion、spike-time gradients、surrogate gradients 和 BPTT。
- Online learning sections：讨论 RTRL、e-prop、DECOLLE、OSTL、ETLP、OSTTP 和 FPTT。
- Outlook sections：讨论 spikes 的潜在优势和未来训练挑战。

## 14. Draft Survey-Usable Sentences

Draft material: Eshraghian et al. provide a useful training-oriented bridge between deep learning and SNNs, especially for explaining surrogate gradients, BPTT, and temporal credit assignment.

Draft material: For event-camera SNN surveys, this paper is best used as SNN-side background rather than event-camera evidence, because it does not introduce a new event-vision model or benchmark result.

Draft material: The paper also cautions that SNN efficiency depends on time steps, spike sparsity, hardware, and implementation details, which is important when interpreting energy claims in event-based SNN papers.
