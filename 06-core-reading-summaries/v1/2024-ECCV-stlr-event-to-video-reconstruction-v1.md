---
title: "Spike-Temporal Latent Representation for Energy-Efficient Event-to-Video Reconstruction"
authors: ["Jianxiong Tang", "Jian-Huang Lai", "Lingxiao Yang", "Xiaohua Xie"]
year: 2024
venue: "ECCV"
level: "A"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/ECCV2024/A/2024-ECCV-A-spike-temporal-latent-representation-for-energy-efficient-event-to-video-reconstruction.md"
official_page: "https://eccv.ecva.net/virtual/2024/poster/1446"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05843.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["SNN", "event camera", "event-to-video", "STLR", "SVT", "energy efficiency", "IJRR", "HQF", "MVSEC"]
---

# Summary V1｜Spike-Temporal Latent Representation for Energy-Efficient Event-to-Video Reconstruction

## 1. One-sentence Summary

STLR 用 Spike-based Voxel Temporal Encoder 和 U-shape SNN Decoder 学习 event voxel 的 spike-temporal latent representation，在保持接近现有 SNN/ANN-SNN reconstruction quality 的同时显著降低参数量和理论能耗。

## 2. Research Problem

本文解决 event-to-video (E2V) reconstruction：从 event camera stream 重建 grayscale video frames。问题在于 ANN-based E2V 方法效果好但计算量大；现有 SNN-based E2V 更节能，但很少显式建模 event voxel 的 temporal latent representation，导致 reconstruction quality 和 efficiency 的平衡仍不理想。

## 3. Background and Motivation

event camera 输出 `(x, y, t, p)` 事件，能低延迟记录运动信息。E2V reconstruction 把稀疏事件恢复为连续灰度帧，对下游视觉任务很有价值。SNN 以 spike-based computation 和 IF/LIF dynamics 运行，有潜力降低 event reconstruction 成本。

作者认为 event voxel 与对应 frame 共享一种 temporal latent coding，可以用 sparse coding / ISTA 的视角解释。STLR 的动机是用 SNN 近似这种 latent coding，再用 SNN decoder 恢复 frame。

## 4. Method Overview

STLR 由两个 cascaded SNN 组成：Spike-based Voxel Temporal Encoder (SVT) 和 U-shape SNN Decoder。SVT 是 spike-driven spatial unfolding network，用专门设计的 coding dynamic 把 event voxel 编码成 layer-wise spiking features，并近似 Iterative Shrinkage-Thresholding Algorithm (ISTA) 的 fixed point。随后 U-shape SNN Decoder 基于这些 encoded spikes 重建视频帧。

输入是 event voxel，输出是 reconstructed grayscale frame/video。event voxel temporal bins 设置为 5，SVT coding steps K 默认为 5，sensing matrix column C 为 10。

## 5. Technical Details

### Event Representation

event stream 先被压缩为 event voxels。论文认为 event voxel 的 temporal vector y 可通过 latent coding z 表示，并与对应 frame 共享 latent representation。

### Spiking Neuron / SNN Module

SVT 使用 LIF neurons 进行 spike generation。U-shape SNN Decoder 使用带 spatial learning through time (SLTT) mechanism 的 LIF neuron；upsampling 后加入 interpolation spiking layer，把 interpolation 结果转换为 binary spikes，避免后续 convolution 处理 real-valued features。

### Network Architecture

SVT 是 spike-driven spatial-unfolding network，用多个 MCS modules 产生 layer-wise spikes `{o_k}`。U-shape decoder 包含 header block、residual block 和 decoder block，并通过 MP skip connection / MP-LIF 结构恢复 frame。

### Training Strategy

训练数据由 ESIM 在 MS-COCO images 上通过 random 6-DOF camera motions 合成，含 950 training sequences。训练使用 SpikingJelly、Adam optimizer，initial learning rate 0.001，batch size 4，100 epochs，在 NVIDIA RTX Q8000 GPU 上训练。评估使用 EVREAL platform。

### Loss Function

总 loss 包含 event reconstruction loss `L_R1`、frame reconstruction LPIPS loss `L_R2`、Fixed Point Approximation loss `L_FP` 和 Temporal Consistency loss `L_TC`。FPA loss 用于让 SVT output 的 spike rate 近似 ISTA fixed point。训练 SNN 时使用 arctan-style surrogate gradient。

### Inference Process

推理时，event voxel 经 SVT 生成 spiking sequence；spike rate / layer-wise spiking features 被送入 U-shape SNN Decoder；decoder 以 spike-based operations 重建 frames。与 EVSNN / PA-EVSNN 的 bin-by-bin ergodic mechanism 相比，STLR 直接分解整个 event voxel，因此 inference steps 为 0.2x。

## 6. Experiments

评估数据集为 IJRR、HQF 和 MVSEC。指标包括 MSE、SSIM 和 LPIPS。对比方法包括 ANN models E2VID、FireNet、SPADE-E2VID、SSL-E2VID，ANN-SNN hybrid PA-EVSNN，以及 SNN EVSNN。

Table 1 显示 STLR 在 IJRR 上达到 MSE 0.075、SSIM 0.469、LPIPS 0.264；HQF 上为 0.089、0.349、0.408；MVSEC 上为 0.128、0.251、0.552。相较 EVSNN，STLR 在全部三项数据集上有明显提升；相较 PA-EVSNN，质量大致 comparable，并在 MVSEC 上 MSE/SSIM/LPIPS 表现更好。

Table 2 报告 efficiency：STLR 参数量 0.61M，低于 EVSNN 4.41M 和 PA-EVSNN 4.62M；spike rate 在 IJRR/HQF/MVSEC 上为 21.98% / 21.07% / 20.07%，均低于 baselines。理论 energy cost 分别为 1.26e-3 J、1.21e-3 J、2.49e-3 J，约为 EVSNN 的 5.26%-5.53%、PA-EVSNN 的 4.75%-5.00%。

Table 3 ablation 分析 SVT unfolding steps、FPA loss 和 decoder spiking neuron。K=10 在平均指标上最佳，但默认 K=5 在效率上更轻；FPA loss 平均提升 MSE/SSIM/LPIPS；decoder neuron 对不同数据集存在 trade-off。

## 7. Main Contributions

1. 提出 event voxel 的 spike-temporal latent representation 建模。
2. 设计 SVT，把 event voxel 编码为 layer-wise spiking latent features。
3. 设计 U-shape SNN Decoder，以 spike-based computation 重建 video frames。
4. 提出 FPA loss，让 spike rate 近似 ISTA fixed point。
5. 在 IJRR、HQF、MVSEC 上以显著更低参数和理论能耗达到 comparable reconstruction quality。

## 8. Limitations and Risks

STLR 的 reconstruction quality 仍总体低于强 ANN E2VID / FireNet 等方法，尤其 SSIM 指标上 ANN 通常更高。

energy cost 是基于 7 nm CMOS 上 MUL/ADD cost 的理论估计，不是实际 neuromorphic hardware measurement。

训练数据为 ESIM synthetic data，真实数据泛化依赖 EVREAL 评估，但训练/测试域差异需人工进一步核验。

K=10 平均性能更好但成本更高；论文默认设置和最佳性能之间需要在 survey 中说清。

## 9. Relation to SNN for Event Cameras

分类：A: SNN + Event Camera core paper。

STLR 是 event camera reconstruction 中较明确的 SNN-based model，输入是 event voxel，主体 encoder/decoder 都是 SNN，且重点讨论 spike rate、ADD/MUL energy 和 spike-driven reconstruction。

## 10. Relation to Survey Taxonomy

- Event reconstruction：event-to-video reconstruction。
- Event representations for SNNs：event voxel temporal latent coding。
- SNN architectures for event cameras：SVT + U-shape SNN Decoder。
- Efficiency, latency, and energy：参数量、spike rate、theoretical energy。
- SNN training methods：surrogate gradient、FPA loss、TC loss。

## 11. Key Terms and Concepts

- STLR：Spike-Temporal Latent Representation。
- SVT：Spike-based Voxel Temporal Encoder。
- ISTA：Iterative Shrinkage-Thresholding Algorithm，用于解释 latent coding fixed point。
- FPA loss：Fixed Point Approximation loss。
- U-shape SNN Decoder：基于 spiking features 的 frame reconstruction decoder。
- EVREAL：event reconstruction evaluation platform。

## 12. Questions for Human Deep Reading

1. STLR 默认 K=5 与 K=10 的性能/能耗 trade-off 如何取舍？
2. FPA loss 的 sensing matrix Phi 是否可解释或可视化？
3. synthetic ESIM training 对真实 IJRR/HQF/MVSEC 的泛化是否充分？
4. interpolation spiking layer 是否仍包含 non-spiking interpolation cost？
5. Table 2 energy 是否包含 memory access cost？
6. 与 PA-EVSNN 的公平性是否基于同一 normalization / EVREAL pipeline？
7. 是否有 inference latency 实测？
8. STLR 是否能用于彩色或 high-resolution reconstruction？

## 13. Evidence Notes

- Abstract / Introduction：提出 STLR、SVT、U-shape SNN Decoder。
- Section 3.2-3.4，第 7-9 页：SVT、decoder、training pipeline、loss。
- Section 4.1，第 10 页：training data、model details、evaluation setup。
- Table 1，第 11 页：IJRR/HQF/MVSEC quality comparison。
- Figure 5-6，第 11-12 页：qualitative comparison。
- Table 2，第 13 页：operations、spike rate、energy cost。
- Table 3，第 13 页：ablation。

## 14. Draft Survey-Usable Sentences

Draft material: STLR is a representative SNN-based event reconstruction method that explicitly models event voxels through spike-temporal latent coding.

Draft material: Its main survey value lies in the quality-efficiency trade-off: STLR approaches prior SNN/hybrid reconstruction quality with much fewer parameters and lower theoretical energy.

Draft material: Energy claims should be framed as analytical estimates based on operation costs, not as direct chip measurements.

