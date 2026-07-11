---
title: "Spiking Neural Networks Need High-Frequency Information"
authors: ["Yuetong Fang", "Deming Zhou", "Ziqing Wang", "Hongwei Ren", "zeng zecui", "Lusong Li", "shibo zhou", "Renjing Xu"]
year: 2025
venue: "NeurIPS"
level: "C"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/NeurIPS2025/C/2025-NEURIPS-C-spiking-neural-networks-need-high-frequency-information.md"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/956834836f36dd07df7064ff42ca69f2-Abstract-Conference.html"
pdf_link: "https://arxiv.org/pdf/2505.18608"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["SNN", "frequency analysis", "Spiking Transformer", "Max-Former", "CIFAR10-DVS"]
---

# Summary V1｜Spiking Neural Networks Need High-Frequency Information

## 1. One-sentence Summary

本文从 frequency-domain 分析指出 spiking neuron 在 network level 是 low-pass filter，并以 Max-Pool patch embedding 和 early-stage Depth-Wise Convolution (DWC) 的 Max-Former 恢复 SNN 中易丢失的 high-frequency visual information。

## 2. Research Problem

SNN 与 ANN 的 performance gap 通常被归咎于 binary/sparse activation 的 information loss。作者反驳这一单一解释，认为更根本的问题是 LIF-like integration 在跨层传递时 preferentially suppresses high-frequency components，导致 local edges/textures 等 feature detail 被衰减。

这与 event cameras 有关联：event stream 保留细粒度 temporal change，event-camera SNN 若在 tokenization 或 early layers 过度 low-pass，可能无法利用其高时间分辨率。论文并未在真实 event tracking/detection task 直接验证这个推断。

## 3. Background and Motivation

单个 spike waveform 的 Fourier spectrum 表面上似乎包含很多 high-frequency components，但作者区分“waveform-induced spectra”和可跨层传递的 information。对 input -> activation -> linear transform 的完整链条，spiking neuron 的 membrane integration 被推导为 first-order IIR low-pass response；多层串联会加强此偏好。

ANN/Transformer 中 Avg-Pool 常有利于 global low-frequency pattern，但论文认为 SNN 的天然 low-pass bias 意味着 early vision stage 反而需要额外频率增强。Max-Pool 偏保留 local high-frequency extrema，small-kernel DWC 比 early global self-attention 更能保持局部 detail，构成其设计动机。

## 4. Method Overview

Max-Former 是 3-stage hierarchical Spiking Transformer。patch embedding 提供 `Embed-Orig`、`Embed-Max`、`Embed-Max+` 三种选择；后两者在 `LIF-Conv-BN` 后加入 MaxPool。early stage 用 spiking DWC 做 token mixing，final stage 使用 Spiking Self-Attention (SSA) 获取 global interaction；residual 使用 membrane shortcut。

模型支持 static images 和 binned event frames。event `(x,y,t,p)` 先按 temporal resolution 合并到 two-polarity frames，再作为 spike sequence 输入；输出为 class label。另构造 Max-ResNet，检查 high-frequency restoration 是否跨 Transformer/CNN architecture 有效。

## 5. Technical Details

### Frequency Analysis

对 LIF charging `V[n] = beta V[n-1] + (1-beta) I[n]` 做 Z-transform，得到 `H(z) = (1-beta)/(1-beta z^-1)`。这是 first-order low-pass filter；`beta` 越接近 1，越偏向 low frequency。论文进一步认为 spike firing 的 local linear approximation 及多 layer cascade 会使 network-level transmission 加剧 high-frequency attenuation。

这个公式表达的是 membrane current-to-potential transfer，不应被误读为对所有 nonlinear SNN、所有 neuron configuration 都作严格 universal proof。

### Architecture and Input

3 stages 分别有 `H/4 x W/4`、`H/8 x W/8`、`H/16 x W/16` tokens。patch embed 的 `Max-Embed = LIF-Conv-BN-MaxPool`；static input repeat `T` times 后 spike encode。event input 通过 temporal binning：相邻 `alpha` raw event bins 聚合为目标-resolution frame，保留 positive/negative channels。

### Token Mixing and Shortcut

early DWC 的 local neighbourhood aggregation 后接 LIF，避免以 quadratic self-attention 过早平滑细节；final stage 的 SSA 以 spike-form `Q/K/V` 运算。Membrane Shortcut 直接连接 membrane potentials，以保持 identity mapping 及 binary spike output；作者批评 pre-spike shortcut 可能出现 `{0,1,2}` non-binary signal。

### Training / Energy

论文采用 LIF throughout，设置按 dataset 见 Appendix。energy 是 operation-level calculation，使用 MAC/AC 与 firing activity；不是 physical device measurement。Max-Former 的改动也降低 early attention complexity，但 MaxPool/DWC 的“high-pass”效果是该文 empirically supported architectural interpretation，不是通用 signal-processing equivalence。

## 6. Experiments

### Datasets and Metrics

实验覆盖 CIFAR-10、CIFAR-100、ImageNet、DVS128 Gesture 和 CIFAR10-DVS；比较 Spikformer、S-Transformer、SWformer、QKFormer/MS-QKFormer 等。指标包括 top-1 accuracy、parameters、simulation timesteps、estimated power，appendix 还比较 GPU training/inference time 和 memory。

### Main Results

Table 2：Max-Former 在 `T=4` 时 CIFAR-10 `97.04%` (`6.57M`)、CIFAR-100 `82.65%` (`6.60M`)；DVS128 `98.6%` (`1.45M`, `T=16`)；CIFAR10-DVS `84.2%` (`1.45M`, `T=16`)。在对应表内，CIFAR10-DVS 高于 MS-QKFormer `82.3%`。

ImageNet Table 3：Max-Former-10-768 (`63.99M`, `T=4`) 为 `82.39%`、estimated `14.87 mJ`；Spikformer-8-768 为 `74.81%`、`21.48 mJ`。论文据此报告同量级 parameters 下比该 Spikformer higher `7.58` points、lower `30%` estimated energy。Max-Former-10-384 (`16.23M`, `T=4`) 为 `77.82%`、`4.89 mJ`。

### Ablations and Generality

Table 4：CIFAR100 将 proposed Embed-Orig/Max/Max 改为 all Orig，accuracy 从 `82.65` 到 `81.63`；CIFAR10-DVS 以 Orig 替代 first-stage Max+，从 `84.2` 到 `81.5`。early DWC-3 + SSA 也优于 all SSA 的 `84.2` versus `83.9` on CIFAR10-DVS。Max-ResNet-18 在 CIFAR-10/CIFAR-100 的 `[3,3,2]` configuration 分别为 `97.17%`、`83.06%`，相对 MS-ResNet report gains `+2.25`、`+6.65` points。

## 7. Main Contributions

1. 提出 SNN 在 network-level propagation 中表现为 low-pass filter 的理论/empirical analysis。
2. 提出以 Max-Pool 和 early DWC 恢复 high-frequency detail 的 Max-Former。
3. 使用 membrane shortcut 保持 binary spike-driven residual path。
4. 以 Max-ResNet 说明 high-frequency restoration 的 effect 不限于 Transformer，并在 DVS benchmarks 验证。

## 8. Limitations and Risks

low-pass conclusion建立在特定 neuron dynamics、linearization 和视觉模型实验上；它尚未直接验证 raw asynchronous event processing 或非 LIF neuron family。event data 经过 temporal binning，可能已先损失部分 fine-grained timing。

“energy saving”来自 theoretical mJ estimation，不含 sensor I/O、event binning、memory/data movement 或 chip measurements。对更高分辨率/高 event rate 场景，MaxPool/DWC 与 tokenization 的实际 latency 需重新评估。

## 9. Relation to SNN for Event Cameras

分类：C: SNN side background。

论文的 CIFAR10-DVS/DVS128 evidence 与 event-camera SNN 有直接 benchmark 联系，且其 high-frequency argument 很适合讨论 event temporal detail 的 preservation；但它没有针对 event-camera task 的 architecture/representation，不能作为 event-based tracking/detection core paper。

## 10. Relation to Survey Taxonomy

- SNN architectures for event cameras：frequency-aware Spiking Transformer 和 membrane shortcut。
- Event representations for SNNs：temporal-binned two-polarity event frames的影响。
- Efficiency, latency, and energy：DWC vs SSA、AC/MAC energy estimate。
- Datasets and benchmarks：DVS128 Gesture、CIFAR10-DVS。
- Open challenges：frequency bias、early tokenization、true asynchronous efficiency。

## 11. Key Terms and Concepts

- network-level low-pass filter：跨 layer information transmission 中 high frequency 被衰减的论文结论。
- Max-Former：以 MaxPool+DWC 频率增强的 Spiking Transformer。
- Max-Embed：`LIF-Conv-BN-MaxPool` patch embedding。
- DWC：Depth-Wise Convolution，early local token mixer。
- SSA：Spiking Self-Attention，final-stage global token mixer。
- membrane shortcut：直接连接 membrane potential 的 residual design。
- CIFAR10-DVS：event-camera object classification benchmark。

## 12. Questions for Human Deep Reading

1. theoretical derivation 中 spike nonlinearity 的 local linearization region 如何选择，是否随 firing rate 改变？
2. Event frame binning 的 `alpha`、T、sensor resolution 和 denoising settings 在 DVS datasets 是什么？
3. MaxPool 是否在 event data 上引入 spatial aliasing 或 polarity mixing，作者是否分析？
4. DWC kernel size 选择和 high-frequency preservation 的 relation 是否有 Fourier-level measurement？
5. Table 3 mJ 的 layer-wise firing rates 和 energy constants 是否完整公开？
6. Max-Former against QKFormer/MS-QKFormer 是否训练 budget、augmentation 与 shortcut完全对齐？
7. Max-ResNet 是否隔离了 MaxPool 本身引起的 receptive-field/inductive-bias变化？
8. 在 event-based detection/tracking 任务，high-frequency temporal component 应如何定义和量化？

## 13. Evidence Notes

- Abstract、Section 1，第 1-2 页：frequency-bias claim、Max-Former、ImageNet result。
- Section 3.1 / Eq. (6)-(13)，第 4-5 页：LIF Z-transform、low-pass derivation与 network cascade argument。
- Section 3.2，第 5-7 页：event/static input、Max-Embed、DWC、SSA、shortcut。
- Tables 2-5 与 Section 4，第 8-10 页：CIFAR/DVS/ImageNet、ablation、Max-ResNet。
- Appendix C-D，约第 18 页：runtime/memory 和 layer-wise estimated energy analysis。

## 14. Draft Survey-Usable Sentences

Draft material: This work argues that SNN performance loss is not only a binary-coding issue: LIF dynamics can attenuate high-frequency information as it propagates through layers.

Draft material: Max-Former restores early-stage high-frequency features through Max-Pool embedding and depth-wise convolution, and reports improvements on both static and DVS classification benchmarks.

Draft material: Its energy results are analytical estimates and its event inputs are temporally binned, so the method should not be read as a direct measurement of asynchronous sensor-to-output efficiency.
