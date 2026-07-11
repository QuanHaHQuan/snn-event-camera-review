---
title: "QP-SNN: Quantized and Pruned Spiking Neural Networks"
authors: ["Wenjie Wei", "Malu Zhang", "Zijian Zhou", "Ammar Belatreche", "Yimeng Shan", "Yu Liang", "Honglin Cao", "Jieyuan Zhang", "Yang Yang"]
year: 2025
venue: "ICLR"
level: "C"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/ICLR2025/C/2025-ICLR-C-qp-snn-quantized-and-pruned-spiking-neural-networks.md"
official_page: "https://proceedings.iclr.cc/paper_files/paper/2025/hash/f04aef8513b788a69229cede8c8cb5a8-Abstract-Conference.html"
pdf_link: "https://proceedings.iclr.cc/paper_files/paper/2025/file/f04aef8513b788a69229cede8c8cb5a8-Paper-Conference.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["SNN", "quantization", "structured pruning", "edge deployment"]
---

# Summary V1｜QP-SNN: Quantized and Pruned Spiking Neural Networks

## 1. One-sentence Summary

QP-SNN 将 hardware-friendly uniform weight quantization 与 structured kernel pruning 结合，并以 ReScaW 改善低 bit-width 表达、以 SVS 根据 spatiotemporal spike activity 的 singular value 选择待剪 kernel。

## 2. Research Problem

SNN 的 binary spike 与 AC operation 有潜在低功耗优势，但高性能 SNN 往往仍有大量 weights、storage 和 memory traffic。已有联合压缩方法会出现 accuracy loss，或依赖 unstructured pruning 而难以在一般 accelerator 上加速。

本文聚焦资源受限 edge deployment：如何将 quantization 和 pruning 同时用于 directly trained SNN，又维持可部署性与精度。它不是为 event-camera input 专门设计，但在 DVS-CIFAR10 上测试了 neuromorphic data。

## 3. Background and Motivation

uniform quantization 将 continuous weights 映射到等间距 integer grid，易部署却可能只使用少数 levels，因为 trained weights 多集中在 zero 附近。structured pruning 删除 whole convolution kernels，保留 dense regular layout；但已有 SCA score 基于 spike/membrane activity，对 input batch 敏感，可能错误删除重要 kernel。

作者以 LIF SNN 为 backbone，认为应从两个失败来源分别修正：用 rescaling 让 assigned bit width 得到有效利用，并用更稳定的 spike-activity singular-value score 排序结构化冗余。

## 4. Method Overview

QP-SNN baseline 先对 LIF SNN 做 uniform quantization 和 structured pruning。ReScaW 在 quantization 前按 layer-wise scale 对 weights 重标定，再映射到 `8/4/2-bit` integer grid；SVS 则收集 convolutional channels 的 spatiotemporal spike activities，以 singular value 导出 kernel importance 并按该 score pruning。

训练仍是 directly trained SNN：spike non-differentiability 用 surrogate gradient，quantizer 用 Straight-Through Estimator (STE)。论文在 VGG/ResNet、Spikingformer 和 YOLO-v3-style detector 上验证，输入包括 static image、DVS-CIFAR10 event data 与 remote-sensing image；不是 event-camera tracking pipeline。

## 5. Technical Details

### Spiking Neuron and Training

baseline 使用 hard-reset LIF：`U_tilde[l,t] = tau U[l,t-1] + W[l] S[l-1,t]`，过 threshold 后输出 spike 并将 membrane reset 为 zero。训练采用 Spatio-Temporal Backpropagation (STBP) 与 triangular surrogate；classification 使用 time-averaged output membrane potentials 的 cross-entropy。

### Uniform Quantization and ReScaW

vanilla quantizer 将 clipped `[-1, 1]` weights 映射到 `2^b` 个 uniform integer levels，再 dequantize 供 forward use。ReScaW 不改变 uniform grid 的 hardware-friendly nature，而是依据 weight distribution 的 scale `gamma` 重新放大/缩小 layer weights，使 1st-99th percentile 的主要 weights 更充分分布于可用 levels。作者的默认 `gamma` 取 layer weight 的 mean L1 magnitude；这是一种范围校正，不是 non-uniform quantization。

### SVS Structured Pruning

SVS 以 kernel 产生的 spatiotemporal spike activity 构造 activity matrix，并用 singular value 作为 importance criterion。作者的论点是 singular-value statistic 比直接依赖某一 batch membrane/spike magnitude 的 SCA 更 input-insensitive，从而能更稳健地去掉 redundant convolutional kernels。pruning 保持 channel/kernel structure，面向 standard hardware。

### Inference and Loss

forward 中 low-bit weight 与 sparse spike activation 共同降低 model size/SOPs。论文以 theoretical power model 计算，不能等同于 on-device measurement；其中 ANN 的 FLOPs 按 MAC energy，SNN 按 firing-rate-weighted AC energy估算。

## 6. Experiments

### Datasets and Settings

分类实验使用 CIFAR-10、CIFAR-100、TinyImageNet、ImageNet-1k 和 DVS-CIFAR10；architectures 包括 VGG-SNN、ResNet20/18 和 SEW-ResNet。额外在 CIFAR-100 上压缩 Spikingformer-4-384，并以 YOLO-v3 + ResNet10 在 SSDD、NWPU VHR-10 测试 detection。指标包括 top-1 accuracy、model size、SOPs 和 theoretical power。

### Main Quantitative Results

Table 1 中，ResNet20 QP-SNN 在 CIFAR-10 的 `8/4/2-bit` accuracy 为 `95.12/95.41/95.06%`，对应 `6.27/3.16/1.61 MB`、`T=2`；CIFAR-100 为 `75.29/75.77/75.13%`，对应 `6.45/3.35/1.79 MB`。DVS-CIFAR10 的 VGGSNN `8/4/2-bit` 结果为 `82.10/81.80/81.30%`，model size `1.61/0.90/0.55 MB`，`T=10`。这些是论文给定 architecture/pruning setting 下的结果。

Table 2 的 Spikingformer experiment 将 connection ratio 降至 `44.74%`、4-bit，model size 从 `18.64` 到 `2.25 MB`，SOPs 从 `292.14` 到 `130.05 M`、theoretical power `0.266` 到 `0.118 mJ`，accuracy 从 `79.09%` 到 `76.94%`。Table 3 中，4-bit detector 在 SSDD 以 `2.15 MB` 得到 `97.10 mAP@0.5`，在 NWPU VHR-10 为 `86.68`，后者低于 full-precision `89.89`。

### Ablations and Efficiency

在 CIFAR-100 ResNet20、约 `1.20 MB` 的 ablation setting，only vanilla quantization 为 `78.53%`，only ReScaW 为 `79.16%`；联合压缩 baseline 为 `69.16%`，仅换 ReScaW 为 `73.40%`、仅换 SVS 为 `73.32%`、两者为 `73.89%`。Table 5 显示 quantize-then-prune 的 QP order 在该实验优于 prune-then-quantize。

Appendix Table 6 对 full-precision VGG-16/CIFAR-10 与极端压缩版比较：connection ratio `9.61%`、4-bit 的 QP-SNN 将 size 从 `58.88` 降至 `0.74 MB`、SOPs `54.60` 降至 `11.63 M`、estimated power `0.204` 降至 `0.046 mJ`，accuracy `93.63%` 降至 `91.19%`。

## 7. Main Contributions

1. 建立 uniform quantization + structured pruning 的 hardware-friendly QP-SNN baseline。
2. 提出 ReScaW，以更充分使用 assigned bit width 的 uniform levels。
3. 提出 SVS pruning criterion，以 spatiotemporal spike activity 的 singular value 排序 kernel importance。
4. 在 static、neuromorphic、Spikingformer 与 detection settings 展示 compression-performance trade-off。

## 8. Limitations and Risks

paper 的 power numbers 是 analytical estimates，未报告真实 neuromorphic chip、memory traffic、quant/dequant overhead 或 device latency。model-size/SOP gains 也不自动意味着 every accelerator 的 wall-clock gain。

event-camera evidence 只包括 DVS-CIFAR10 classification，不覆盖 raw asynchronous inference、event detection/tracking 或真实 sensor deployment。ReScaW/SVS 的 robustness 也主要来自所给 model/dataset，pruning schedule 与 target sparsity 对结果敏感。

## 9. Relation to SNN for Event Cameras

分类：C: SNN side background。

QP-SNN 可为 event-camera SNN 的 model compression、low-bit implementation 和 structured sparsity 提供方法背景，尤其 DVS-CIFAR10 证明其可用于一个 neuromorphic benchmark；但它不是针对 event representation 或 event-camera task 提出的核心方法。

## 10. Relation to Survey Taxonomy

- SNN training methods：STBP、triangular surrogate 和 STE。
- Efficiency, latency, and energy：quantization、structured pruning、SOP/power estimation。
- SNN architectures for event cameras：compressed LIF-SNN backbone 的实现背景。
- Datasets and benchmarks：DVS-CIFAR10 作为小规模 neuromorphic classification benchmark。
- Open challenges：compression accuracy、hardware-realistic energy、event-stream deployment。

## 11. Key Terms and Concepts

- QP-SNN：Quantized and Pruned SNN，本文的 jointly compressed SNN。
- ReScaW：weight rescaling strategy，用于改善 uniform quantizer 的 effective level use。
- SVS：singular value of spatiotemporal spike activity，本文的 structured pruning score。
- STBP：Spatio-Temporal Backpropagation，沿 space/time 展开 SNN gradient。
- STE：Straight-Through Estimator，以 surrogate derivative 训练 quantizer。
- structured pruning：删除完整 convolution kernels/channels，保持 dense structure。
- SOPs：synaptic operations，用于估算 SNN inference compute。

## 12. Questions for Human Deep Reading

1. SVS activity matrix 的 exact shape、sample/batch aggregation 与 singular-value reduction 如何定义？
2. pruning 是一次性、iterative 还是 joint training，target connection ratios 由何确定？
3. ReScaW 的 `gamma` 是否 per-channel、per-layer，outlier clipping 的敏感性如何？
4. DVS-CIFAR10 的 event bins、input encoding、T=10 和 data augmentation 与 prior work 是否一致？
5. Table 1 的同一 architecture 两行分别对应何种 pruning ratio，需从 table header/code 核验。
6. theoretical power 是否计入 first/last layer、residual addition、batch norm 和 quantization operations？
7. 在 real event-camera detector/tracker 上，structured pruning 是否保持 event sparsity和 latency advantage？
8. 远程感知 detection 的 SNN timestep/input representation 与 standard RGB YOLO 的比较是否公平？

## 13. Evidence Notes

- Abstract 与 Section 1，第 1-2 页：联合压缩问题、ReScaW、SVS 和 hardware-friendly objective。
- Section 3，第 3-4 页：LIF update、uniform quantization 和 baseline structured pruning。
- Section 4.1-4.2，第 5-7 页：ReScaW 的 bit-width utilization 与 SVS criterion。
- Section 5 / Table 1-4，第 7-10 页：benchmarks、Spikingformer/detection scaling 与 ablation。
- Appendix C-D，第 17-18 页：power/efficiency comparison、STBP+STE、surrogate 和 cross-entropy。

## 14. Draft Survey-Usable Sentences

Draft material: QP-SNN combines uniform low-bit weights with structured pruning, targeting SNN compression that remains compatible with conventional dense accelerators.

Draft material: Its ReScaW and singular-value spike-activity criterion address two distinct sources of compression loss: underused quantization levels and input-sensitive kernel ranking.

Draft material: The reported energy figures are theoretical estimates, so they should be separated from measured end-to-end efficiency claims for event-camera systems.
