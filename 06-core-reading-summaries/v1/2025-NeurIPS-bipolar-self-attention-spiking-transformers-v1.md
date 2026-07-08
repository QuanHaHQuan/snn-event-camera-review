---
title: "Bipolar Self-attention for Spiking Transformers"
authors: ["Shuai Wang", "Malu Zhang", "Jingya Wang", "Dehao Zhang", "Yimeng Shan", "Jieyuan Zhang", "Yichen Xiao", "Honglin Cao", "Haonan Zhang", "Zeyu Ma", "Yang Yang", "Haizhou Li"]
year: 2025
venue: "NeurIPS"
level: "C"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/NeurIPS2025/C/2025-NEURIPS-C-bipolar-self-attention-for-spiking-transformers.md"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/9316cfcb0a81e53a1f35b4353f115571-Abstract-Conference.html"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/file/9316cfcb0a81e53a1f35b4353f115571-Paper-Conference.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["SNN", "spiking transformer", "self-attention", "BSA", "Shiftmax", "event-based tracking"]
---

# Summary V1｜Bipolar Self-attention for Spiking Transformers

## 1. One-sentence Summary

这篇论文提出 Bipolar Self-attention (BSA)，用 ternary matrix product 和 Shiftmax 修正 Spiking Self-attention 中 polarity information loss 与 row-stochasticity 缺失问题，从而提升 Spiking Transformer 在分类、分割和 event-based tracking 上的表现。

## 2. Research Problem

论文处理 Spiking Transformer 的核心瓶颈：现有 Spiking Self-attention (SSA) 使用 binary spike trains，通常只能表达 positive-positive interactions，丢失 negative-negative 和 positive-negative membrane potential interactions；同时为了避免 expensive Softmax，SSA 往往缺少 row-stochasticity，导致 attention allocation 不稳定。

这对 SNN/Event Camera 综述很重要，因为 Spiking Transformer 正成为 SNN architecture 的重要路线，而 event-based tracking 也出现在实验中。虽然论文不是 event-camera-specific method，但 BSA 可作为 SNN architecture background。

## 3. Background and Motivation

Transformer self-attention 通过 Q/K correlation 和 Softmax 建模全局依赖，但计算复杂度高。SNN 通过 sparse binary spikes 和 accumulate operations 提高能效。现有 SSA 为了保持 spike-driven 特性，通常去掉 Softmax，并使用 binary matrix product，这造成表达能力下降。

论文动机是保留 SNN 的 spike-driven/energy-efficient 特性，同时恢复 self-attention 所需的 polarity relation 和近似 row-stochastic constraints。

## 4. Method Overview

BSA 将原来的 binary matrix product (BMP) 扩展为 ternary matrix product (TMP)，让 attention 能区分同极性和异极性 membrane potential interactions。随后提出 Shiftmax，用 bit-shift operations 近似 Softmax 的 low-entropy activation 和部分 row-stochasticity，而不是使用昂贵 nonlinear Softmax。

输入/输出层面，BSA 是一个可插入 Spiking Transformer architectures 的 attention module，可用于 image classification、semantic segmentation 和 event-based tracking。

## 5. Technical Details

### Event Representation

论文不是 event-camera representation paper。event-based tracking 只作为实验任务之一；具体 event representation 需要在 tracking experimental protocol 中人工复核。

### Spiking Neuron / SNN Module

BSA 面向 spike-driven Transformer。它关心 Q/K 中 membrane potential 的正负 polarity，而不是仅用 binary spike 的 0/1 相关。

### Network Architecture

BSA 可替换 Spikingformer、Spike-driven Transformer V3、QKformer 等中的 SSA module。它包括两个核心机制：TMP 和 Shiftmax。

### Training Strategy

论文在不同任务上按照各 backbone/protocol 训练。classification 使用 ImageNet/CIFAR 等常见分类设置；semantic segmentation 使用 ADE20K；event-based tracking 使用对应 tracking benchmark。具体 optimizer 和 schedule 需要人工复核。

### Loss Function

无新 task loss。核心贡献是 attention module；loss 依任务采用分类、分割或 tracking 任务原有损失。

### Inference Process

推理时，BSA 用 ternary products 计算 richer attention correlations，再用 Shiftmax 进行低成本归一化近似。Shiftmax 通过 bit-shift 近似 `2^x / sum 2^x` 的归一效果，意图避免 Softmax 的高能耗。

## 6. Experiments

论文覆盖 image classification、semantic segmentation 和 event-based tracking。Table 1 显示在多个 Spiking Transformer architectures 上加入 BSA 后 accuracy 提升。例如 Spikingformer D=512 提升 1.35%，D=768 提升 0.97%；Spike-driven V3 在不同参数规模上提升约 0.36%-0.74%；QKformer 提升约 0.35%-0.41%。

Semantic segmentation：Table 2 在 ADE20K 上评估，SDT-V3 + BSA 在 10M+1.4M 配置达到 41.90 mIoU，比 SDT-V3 40.1 提升 1.80；在 19.4M+1.4M 配置达到 43.41，比 41.3 提升 2.11。

Ablation：Table 4 在 CIFAR100 上比较 BMP/TMP 与 Softmax/Shiftmax。SSA/BMP/None 为 79.13%；TMP/None 为 79.27%；TMP/Softmax 为 80.76%；TMP/Shiftmax 为 80.48，说明 polarity modeling 和 row-stochasticity 近似都重要。

Event-based tracking：摘要声称 BSA 在 event-based tracking 上也有提升，但 V1 抽取中未得到完整 tracking 表格数值，需要人工重点核对。

## 7. Main Contributions

- 指出 SSA 的两个具体限制：polarity information loss 和缺少 row-stochasticity。
- 提出 BSA，用 TMP 捕捉 multi-polar membrane potential interactions。
- 提出 Shiftmax，用 bit-shift operations 近似 Softmax 效果，保持更高能效。
- 在 classification、segmentation、event-based tracking 上展示模块可迁移性。

## 8. Limitations and Risks

论文主要是 SNN attention module，不是 event-camera-specific architecture。Event-based tracking 的实验细节需要人工核实，不能仅凭摘要判断其对 event camera 任务的充分性。Shiftmax 是近似 Softmax，理论上可能在不同数据分布下不稳定。TMP 引入 ternary representation，硬件能效是否在真实 neuromorphic hardware 上成立需要进一步验证。

对综述风险：可作为 Spiking Transformer 背景，但除非 tracking 实验确认为 event-camera benchmark，否则不应强行归入 event-camera core。

## 9. Relation to SNN for Event Cameras

分类：C: SNN side background。

理由是论文核心为 Spiking Transformer attention mechanism，event-camera 相关性主要来自 event-based tracking 实验和 SNN architecture 可迁移性。它不是为 event camera 专门设计。

## 10. Relation to Survey Taxonomy

可支持的章节包括：

- SNN architectures for event cameras
- SNN training methods
- Surrogate gradient and temporal credit assignment
- Event-based tracking
- Efficiency, latency, and energy
- Open challenges

## 11. Key Terms and Concepts

- Spiking Self-attention (SSA)：Spiking Transformer 中基于 spike trains 的 attention。
- Bipolar Self-attention (BSA)：考虑正/负 polarity interactions 的 spiking attention。
- Binary Matrix Product (BMP)：基于 binary spikes 的矩阵乘，可能丢失负极性关系。
- Ternary Matrix Product (TMP)：用 ternary states 近似 real-valued correlation。
- Shiftmax：用 bit-shift operations 近似 Softmax 的低成本机制。
- Row-stochasticity：attention rows 归一化为可比较分布的性质。

## 12. Questions for Human Deep Reading

1. TMP 的 ternary states 如何从 membrane potential 或 spike signals 得到？
2. BSA 是否仍保持 fully spike-driven，还是引入非 spike-valued intermediates？
3. Shiftmax 的能耗估计是否包含指数近似、归一化和 memory access？
4. Table 1 中不同 backbone 的训练协议是否一致？
5. Event-based tracking 用的是哪个 dataset 和 event representation？
6. BSA 在 tracking 上的实际指标提升是多少？
7. TMP/Shiftmax 对 timestep T 的敏感性如何？
8. 是否有 neuromorphic hardware 或 edge hardware 实测？

## 13. Evidence Notes

- Abstract：定义 BSA、TMP、Shiftmax，并声称覆盖 classification、segmentation、event-based tracking。
- Figure 1：比较 VSA 与 SSA，说明 polarity 和 row-stochasticity 缺失。
- Table 1：BSA 在多个 Spiking Transformer classification architectures 上的提升。
- Table 2：ADE20K semantic segmentation mIoU。
- Table 4：BMP/TMP 与 None/Softmax/Shiftmax ablation。

## 14. Draft Survey-Usable Sentences

草稿句 1：Bipolar Self-attention addresses a core limitation of Spiking Transformers by recovering polarity interactions that are lost in binary Spiking Self-attention.

草稿句 2：For event-camera SNN surveys, BSA is best treated as SNN architecture background, with event-based tracking evidence requiring careful manual verification.

草稿句 3：Its Shiftmax mechanism is relevant to energy-aware attention design because it approximates Softmax-like normalization through bit-shift operations rather than standard dense nonlinear computation.
