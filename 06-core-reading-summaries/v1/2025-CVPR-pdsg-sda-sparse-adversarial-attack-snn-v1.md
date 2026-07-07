---
title: "Towards Effective and Sparse Adversarial Attack on Spiking Neural Networks via Breaking Invisible Surrogate Gradients"
authors: ["Li Lun", "Kunyu Feng", "Qinglong Ni", "Ling Liang", "Yuan Wang", "Ying Li", "Dunshan Yu", "Xiaoxin Cui"]
year: 2025
venue: "CVPR"
level: "A"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/CVPR2025/A/2025-CVPR-A-towards-effective-and-sparse-adversarial-attack-on-spiking-neural-networks-via-breaking-in.md"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Lun_Towards_Effective_and_Sparse_Adversarial_Attack_on_Spiking_Neural_Networks_CVPR_2025_paper.html"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Lun_Towards_Effective_and_Sparse_Adversarial_Attack_on_Spiking_Neural_Networks_CVPR_2025_paper.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["SNN", "adversarial attack", "surrogate gradient", "PDSG", "SDA", "CIFAR10-DVS", "DVS-Gesture", "N-MNIST"]
---

# Summary V1｜Towards Effective and Sparse Adversarial Attack on Spiking Neural Networks via Breaking Invisible Surrogate Gradients

## 1. One-sentence Summary

本文提出 PDSG 和 SDA，分别解决 inference-only SNN 中 invisible surrogate gradients 与 binary dynamic images 稀疏攻击困难的问题，在 static/dynamic SNN attacks 上取得更高 ASR 和更少扰动。

## 2. Research Problem

SNN 的 gradient-based adversarial attack 依赖 STBP 和 surrogate gradients，但训练阶段 SG 对 inference-only model 不可见，攻击者难以选择合适 SG。对于 DVS 产生的 binary dynamic images，floating-point gradients 还难以直接转换为稀疏 binary perturbations。

本文解决两个问题：如何为不可见 SG 的 victim SNN 构造更适配模型的 attack-phase SG；如何对 binary dynamic images 做有效且稀疏的 adversarial attack。

## 3. Background and Motivation

SNN 使用 binary spike sequences，有低能耗和异步处理优势，也被用于 event-based data。已有攻击如 RGA、HART、SCG、SpikeFool、GSAttack 分别处理 surrogate gradient 或 binary attacks，但 universal SG 与 victim model 相关性不足，binary dynamic attacks 的 sparsity 也不够好。

作者认为 SG 形状应与 membrane potential distribution 相关，而不是固定选择；binary perturbation 也应通过 generation-reduction 机制减少冗余。

## 4. Method Overview

PDSG (Potential-Dependent Surrogate Gradient) 根据 membrane potential variance 自适应构造 SG，并通过 right-shift calibration 平衡 threshold 两侧梯度。SDA (Sparse Dynamic Attack) 针对 binary dynamic images，先用 PDSG 计算 contributing gradients，再用 top-k gradients 和 finite differences 选择 perturbation pixels，最后通过 binary-search reduction 删除冗余扰动。

输入包括 static images、integer dynamic frames 或 binary dynamic frames；输出是 adversarial examples。动态数据来自 event streams 聚合后的 frames。

## 5. Technical Details

### Event Representation

对于 dynamic data，DVS event stream 被聚合为 integer frames，每个 polarity 对应一个 channel；若 neuromorphic hardware 只接受 binary spike inputs，则进一步 binarize 为 binary frames。论文主要在 CIFAR10-DVS、DVS-Gesture、N-MNIST 上测试 binary dynamic images。

### Spiking Neuron / SNN Module

论文采用 LIF neuron model，membrane potential 根据上一时间步、spike reset、weights 和 inputs 更新。STBP gradient 包含 spatial 和 temporal terms，surrogate gradient 用来近似 non-differentiable firing function。

### Network Architecture

攻击对象包括 spiking ResNet-18、spiking VGG-11、VGGSNN、PLIFNet、HST 等。论文不提出新 victim model，而是攻击多种 SNN architectures。

### Training Strategy

PDSG 不依赖训练阶段 SG，而是在攻击阶段根据 membrane potential distribution 构造。SDA 是 iterative attack，不是训练方法。

### Loss Function

PDSG/SDA 使用 C&W-style loss 解决 gradient vanishing。SDA generation 阶段选择与 input change 方向相反的 contributing gradients 和 finite differences；reduction 阶段按 FD 重要性排序并移除冗余 perturbations。

### Inference Process

攻击时对 victim SNN forward/backward，使用 PDSG 近似 spike derivative。binary dynamic input 的扰动通过 mask 翻转 selected pixels，直到 misclassification，再做 sparsity reduction。

## 6. Experiments

数据集包括 static CIFAR10、CIFAR100、ImageNet，以及 dynamic N-MNIST、DVS-Gesture、CIFAR10-DVS。动态数据被聚合为 10 frames 并 binarized。攻击指标为 ASR 和 L0 perturbation。

Table 1 显示 PDSG 在 static images 和 integer dynamic frames 上整体比 STBP/RGA/HART 更稳定。例如 ImageNet HST-10-768 direct input 上，PGD ϵ=8/255 时 PDSG 达到 100.00% ASR；CIFAR10 ResNet18 direct input 上 PGD ϵ=8/255 也达到 100.00%。

Table 2 显示 SDA 在 binary dynamic images 上优于 SCG、SpikeFool、GSAttack。CIFAR10-DVS ResNet18 上，L0 < 800 时 SDA + PDSG 达到 82.0% ASR；dynamic evaluation 中 ASR 100.0%，mean L0 458.02，median L0 303。论文指出 303 pixels 约为 CIFAR10DVS input pixels 的 0.24%。

Table 3 分析不同 training SG 和 attack SG，PDSG 在各种训练 SG 下通常达到约 80% ASR，显示比固定 SG 更稳。

Table 4 ablation 显示 SDA 各组件都有效：top-k gradients baseline 为 69.0% ASR / mean L0 655.70；加入 C&W loss、FDs、reduction 和 PDSG 后达到 82.0% ASR / mean L0 458.02 / median L0 303.0。

## 7. Main Contributions

1. 提出 Potential-Dependent Surrogate Gradient，根据 membrane potential distribution 自适应构造 attack SG。
2. 用 calibration shift 平衡 threshold 两侧梯度，提高 attack stability。
3. 提出 Sparse Dynamic Attack，用 generation-reduction paradigm 攻击 binary dynamic images。
4. 在 static/integer/binary dynamic SNN attack settings 上超过多个 SOTA attacks。
5. 展示 SNN robustness 在 event-based data 上仍存在明显风险。

## 8. Limitations and Risks

论文是 adversarial attack paper，不是 event-camera perception architecture；survey 中应放在 robustness/security 部分。

动态数据是 event streams 聚合/二值化后的 frames，而不是直接 raw event attack；这与 ECCV 2024 raw event attack paper 不同。

攻击假设包括 white-box / gradient access；实际 inference-only threat model 下哪些参数可获得需要细读。

Table 2 的 dynamic evaluation 在 100 correctly classified inputs 上进行，规模和统计稳定性需核验。

## 9. Relation to SNN for Event Cameras

分类：A: SNN + Event Camera core paper。

它研究 SNN 对 DVS binary dynamic images 的 adversarial vulnerability，是 survey 中 robustness / security / surrogate gradient risks 的核心文献。它也可与 raw event attack paper 对照：一个攻击 binary dynamic frames，一个攻击 raw events。

## 10. Relation to Survey Taxonomy

- SNN training methods：surrogate gradients and STBP。
- Surrogate gradient and temporal credit assignment：SG choice affects attacks。
- Open challenges：robustness and adversarial security。
- Datasets and benchmarks：N-MNIST、DVS-Gesture、CIFAR10-DVS。
- Event representations for SNNs：integer/binary dynamic frames。

## 11. Key Terms and Concepts

- PDSG：Potential-Dependent Surrogate Gradient。
- SDA：Sparse Dynamic Attack。
- Invisible SG：inference-only model 中训练 SG 不可见。
- STBP：Spatial-Temporal Backpropagation。
- Binary dynamic image：DVS event stream 聚合并二值化后的 frame sequence。
- ASR：Attack Success Rate。
- L0：modified pixels 数量。

## 12. Questions for Human Deep Reading

1. PDSG 的 membrane potential distribution 是否需要访问所有 layers？
2. inference-only model 下如何获得 backward path？
3. SDA 是否能作用于 raw event data，还是只能 binary frames？
4. 0.24% pixels 的分母具体是 T x C x H x W 吗？
5. Table 2 中 dynamic evaluation 与 bounded L0 evaluation 的区别是什么？
6. PDSG 对 defended/adversarially trained SNN 的效果是否稳定？
7. right-shift b=0.5 sigma 是否可自动选择？
8. 与 ECCV raw event attack 的 threat model 如何区分？

## 13. Evidence Notes

- Section 3，第 3-4 页：LIF、STBP、input preprocessing、attack formulation。
- Section 4.1，第 4-5 页：PDSG derivation and calibration。
- Section 4.2，第 5-6 页：SDA generation and reduction。
- Table 1-2，第 7 页：static/integer and binary dynamic attack results。
- Table 3-4，第 8 页：PDSG effects and SDA ablation。
- Conclusion，第 8 页：100% ImageNet ASR and 82% CIFAR10DVS sparse attack claim。

## 14. Draft Survey-Usable Sentences

Draft material: This work shows that surrogate-gradient design is not only a training issue but also a security surface for attacking SNNs.

Draft material: For event-based SNNs, SDA demonstrates that binary dynamic inputs can be attacked with sparse perturbations when gradients are adapted to membrane potential statistics.

Draft material: The paper should be discussed alongside raw-event attacks to separate vulnerabilities of binned binary frames from vulnerabilities of raw asynchronous event streams.

