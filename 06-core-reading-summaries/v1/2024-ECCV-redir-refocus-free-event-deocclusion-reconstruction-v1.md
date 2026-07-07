---
title: "REDIR: Refocus-free Event-based De-occlusion Image Reconstruction"
authors: ["Qi Guo", "Hailong Shi", "Huan Li", "Jinsheng Xiao", "Xingyu Gao"]
year: 2024
venue: "ECCV"
level: "A"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/ECCV2024/A/2024-ECCV-A-redir-refocus-free-event-based-de-occlusion-image-reconstruction.md"
official_page: "https://eccv.ecva.net/virtual/2024/poster/2118"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/10433.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["event camera", "SNN block", "E-SAI", "de-occlusion", "image reconstruction", "V-ESAI", "spatial-temporal attention"]
---

# Summary V1｜REDIR: Refocus-free Event-based De-occlusion Image Reconstruction

## 1. One-sentence Summary

REDIR 提出一种 refocus-free variable E-SAI de-occlusion reconstruction framework，通过 event registration、PMCM 和带 spatial-temporal attention 的 SNN block，从纯事件流中重建遮挡后的目标图像。

## 2. Research Problem

论文研究 event-based synthetic aperture imaging (E-SAI) 下的 de-occlusion image reconstruction：在相机移动并穿过遮挡缝隙采集事件时，如何无需 prior information / manual refocus 就重建被遮挡目标。

现有 E-SAI 方法通常依赖 prior information 或对相机运动有严格假设，例如 uniform linear motion、fixed focal length 或 manual focusing。实际采集可能出现 lens rotation、focus change、non-uniform motion，导致 event points misalignment，降低 reconstruction quality。

## 3. Background and Motivation

event cameras 能捕获高频亮度变化，适合在遮挡环境下通过移动采集多个视角中的目标事件。E-SAI 利用类似 synthetic aperture 的思想，从不同时间和视角聚合事件以去除前景遮挡。

但 E-SAI 的关键困难是 registration：不同 timestamp 下的 events 会因相机运动、焦距变化或旋转而错位。传统 refocus 方法需要手动或先验信息，限制应用场景。REDIR 的动机是做 end-to-end refocus-free registration and reconstruction。

## 4. Method Overview

REDIR 输入 pure event streams，先进行 variable event data feature registration，对 global / local features 进行 alignment；随后用 reconstruction module 生成 de-occluded image。方法包含 STN-style registration、UNet-Hybrid reconstruction、perceptual mask-gated connection module (PMCM)，以及带 temporal-spatial attention 的 SNN block。

输出是高分辨率 de-occluded reconstructed image。该论文中的 SNN 不是完整事件视觉 backbone，而是用于增强目标提取的模块，特别在 spatial-temporal attention context 中处理 event features。

## 5. Technical Details

### Event Representation

论文基于 E-SAI / V-ESAI event streams，每组数据按 30 timestamps 组织。V-ESAI 通过 rotation、scaling、translation 等 affine transformations 扩展 E-SAI，以模拟 lens rotation、focal length change 和 perspective change。

### Spiking Neuron / SNN Module

论文在 SNN block 中加入 spatial-temporal attention mechanism，用于提升 target extraction ability。正文抽取中没有完整展开 spiking neuron 公式，SNN 在本文中更像 reconstruction network 的增强模块而非完整 end-to-end SNN system。

### Network Architecture

REDIR 包含 registration model、filter reconstruction model、PMCM 和 TSA/SNN block。PMCM 用于模块间信息连接，帮助重建被遮挡目标。UNet + STN 负责预测 transformation parameters 并对每个 timestamp 的 global/local features 做 affine alignment。

### Training Strategy

训练分三阶段：第一阶段对 filter reconstruction model 预训练 200 epochs，initial learning rate 5e-4；第二阶段固定 reconstruction 部分，训练 registration model 500 epochs，initial learning rate 3e-4；第三阶段引入 PMCM 后整体 fine-tune 300 epochs。batch size 为 12，优化器为 Adam，使用 SGDR schedule，在 NVIDIA RTX3090 GPUs 上训练。

### Loss Function

loss 包含 perceptual loss、pixel loss 和 total variation loss。perceptual loss 用深层特征约束 semantic similarity；pixel loss 使用 L1 保证像素级精度；TV loss 约束平滑性。总 loss 是三者的加权和。

### Inference Process

推理时输入多 timestamp event stream，REDIR 逐时间对齐 variable event features，通过 PMCM 和 reconstruction module 生成最终无遮挡图像，不需要 manual refocus 或 prior focusing information。

## 6. Experiments

数据集包括 E-SAI 与新提出的 V-ESAI。E-SAI 含 488 indoor groups 和 100 outdoor groups，每组被分为 30 timestamps；V-ESAI 在 E-SAI 基础上加入三类 random affine transformations，总计扩展到 1,952 indoor groups 和 400 outdoor groups，共 2,352 groups。

Table 1 在 F-SAI/E-SAI dataset 上比较 de-occlusion reconstruction。REDIR 不需要 prior information，Total PSNR / SSIM / LPIPS 为 25.74 / 0.7395 / 0.1139，高于同样不需 prior 的 Hybrid 22.32 / 0.6649 / 0.1678 和 FSAI+CNN 23.67 / 0.7527 / 0.1263 的 PSNR/LPIPS。Refocus+Hybrid 27.94 / 0.7889 / 0.0628 更高，但需要 prior information / manual-refocused pretraining。

Section 5.3 在 V-ESAI 上验证 translation、scaling、rotation transformations，展示 REDIR 能处理 variable acquisition motion。论文主要提供 qualitative analysis，具体 V-ESAI 数值表在抽取页中未出现，需人工核验。

Table 2 的 ablation 显示，Hybrid baseline 为 23.32 PSNR / 0.7091 SSIM / 0.1481 LPIPS；加入完整 UNet+Hybrid+STN+PMCM+TSA 后达到 32.61 / 0.8842 / 0.0279。论文称相比 reconstruction-only baseline，PSNR 提升 9.3 dB，SSIM 提升 17.51%，LPIPS 降低 12.02%。

## 7. Main Contributions

1. 提出 refocus-free E-SAI de-occlusion reconstruction 方法 REDIR。
2. 构建 V-ESAI dataset，用于测试 focus change、lens rotation 和 non-uniform motion 下的重建。
3. 设计 event feature registration，使 REDIR 不依赖 prior information 或 manual refocus。
4. 提出 PMCM 和包含 spatial-temporal attention 的 SNN block，提高遮挡目标提取和重建质量。
5. 在 E-SAI 上优于无需 prior information 的现有方法，并在 V-ESAI 上展示 variable transformation robustness。

## 8. Limitations and Risks

本文与 survey 主题的 SNN 关系比 object detection SNN papers 弱：SNN block 是 reconstruction model 内部模块，论文主要贡献是 event-based de-occlusion reconstruction 和 registration。

Table 1 中 REDIR 低于需要 prior information 的 Refocus+Hybrid，因此不能简单称为所有方法 SOTA；应强调“without prior information”设定。

V-ESAI 是基于 E-SAI 的 data enhancement / transformations 构造，真实复杂运动采集中的泛化仍需核验。

SNN block 的具体能耗、spike rate 和 neuromorphic deployment 没有在正文主要实验中报告。

## 9. Relation to SNN for Event Cameras

分类：A: SNN + Event Camera core paper，但偏 event reconstruction / SNN-assisted module。

它直接处理 event camera streams，并在 reconstruction network 中使用 SNN block 和 spatial-temporal attention。不过它不是典型的 full SNN perception architecture，更适合作为 event reconstruction 与 SNN module 融合的案例。

## 10. Relation to Survey Taxonomy

- Event reconstruction：E-SAI de-occlusion image reconstruction。
- Event representations for SNNs：multi-timestamp E-SAI / V-ESAI event streams。
- Hybrid ANN-SNN models：registration/reconstruction network 中嵌入 SNN block。
- Open challenges：prior-free registration、variable camera motion、occlusion removal。

## 11. Key Terms and Concepts

- E-SAI：Event-based Synthetic Aperture Imaging，用于遮挡场景重建。
- REDIR：Refocus-free Event-based De-occlusion Image Reconstruction。
- V-ESAI：包含 translation、scaling、rotation 等 variable transformations 的扩展数据集。
- PMCM：Perceptual Mask-gated Connection Module。
- TSA：Temporal-Spatial Attention。
- PSNR / SSIM / LPIPS：重建质量指标。

## 12. Questions for Human Deep Reading

1. SNN block 的具体 neuron model 和 spike computation 是否完整描述在 supplement？
2. V-ESAI 是否只是 synthetic augmentation，还是包含真实 variable acquisition？
3. Table 2 中 PSNR 32.61 与 Table 1 中 REDIR Total PSNR 25.74 的实验设置有何差异？
4. PMCM 如何计算 perceptual mask，是否依赖 ground truth？
5. REDIR 是否能在 outdoor dense occlusion 上稳定优于 baselines？
6. 无 prior information 的定义是否完全排除 camera motion metadata？
7. 是否有推理时间、参数量或能耗报告？
8. 代码是否提供 V-ESAI 构造脚本？

## 13. Evidence Notes

- Abstract：说明 REDIR、PMCM、SNN block 和 V-ESAI。
- Section 4.5，第 10 页：loss functions。
- Section 5.1，第 11 页：V-ESAI dataset 与三阶段训练。
- Figure 5 / Table 1，第 12 页：qualitative and quantitative E-SAI comparison。
- Section 5.3，第 13 页：variable motion acquisition reconstruction。
- Table 2，第 14 页：module ablation。
- Conclusion，第 14 页：总结 refocus-free 与 V-ESAI。

## 14. Draft Survey-Usable Sentences

Draft material: REDIR is best treated as an event reconstruction paper with an SNN-enhanced module, rather than as a fully spiking event-camera architecture.

Draft material: Its prior-free E-SAI formulation is useful for discussing event-camera reconstruction under occlusion and variable motion.

Draft material: The SNN-related claim should be described cautiously unless the spike computation and energy behavior are verified in the supplementary material.

