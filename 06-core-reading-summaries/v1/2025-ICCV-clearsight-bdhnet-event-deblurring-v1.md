---
title: "ClearSight: Human Vision-Inspired Solutions for Event-Based Motion Deblurring"
authors: ["Xiaopeng Lin", "Yulong Huang", "Hongwei Ren", "Zunchang Liu", "Hongxiang Huang", "Yue Zhou", "Haotian Fu", "Bojun Cheng"]
year: 2025
venue: "ICCV"
level: "A"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/ICCV2025/A/2025-ICCV-A-clearsight-human-vision-inspired-solutions-for-event-based-motion-deblurring.md"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Lin_ClearSight_Human_Vision-Inspired_Solutions_for_Event-Based_Motion_Deblurring_ICCV_2025_paper.html"
pdf_link: "https://openaccess.thecvf.com/content/ICCV2025/papers/Lin_ClearSight_Human_Vision-Inspired_Solutions_for_Event-Based_Motion_Deblurring_ICCV_2025_paper.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["SNN", "ANN-SNN hybrid", "event camera", "motion deblurring", "BDHNet", "NCM", "RBAM"]
---

# Summary V1｜ClearSight: Human Vision-Inspired Solutions for Event-Based Motion Deblurring

## 1. One-sentence Summary

本文提出 BDHNet，用 SNN 提取 event-stream motion features、用 ANN 处理 blurry RGB image，并通过 NCM 与 RBAM 做动态跨模态融合以改善 event-based motion deblurring。

## 2. Research Problem

论文处理 camera/scene motion 导致的 image blur。event cameras 能记录异步运动线索，但 event data 分布不均且冗余较强，直接把 event features 与 image features 融合容易把无关 event noise 带入重建。对 SNN + event camera survey 来说，它展示了 SNN 作为 motion feature extractor 参与 image restoration 的 hybrid 路线。

## 3. Background and Motivation

传统 motion deblurring 主要依赖 frame intensity，遇到 fast motion 和 exposure integration 时信息不足。event cameras 以 microsecond latency 输出 brightness-change events，适合补充运动边缘。SNN 的 spike dynamics 与 event stream 在形式上接近，但单独依赖 spikes 难以恢复颜色/纹理，因此本文采用 ANN/SNN dual-drive。

## 4. Method Overview

整体 pipeline 输入 blurry image 和 event stream。event branch 使用 SNN 编码 motion clues，image branch 使用 ANN 编码 color/texture clues；BDHNet 通过 Neuron Configurator Module 动态调整 spiking neuron configuration，并通过 Region of Blurry Attention Module 生成 unsupervised blurry mask，引导跨模态 fusion 和 decoder reconstruction。输出为 deblurred image。

## 5. Technical Details

### 1. Event Representation

PDF 抽取显示方法围绕 asynchronous event streams 与 blurry image 配对输入展开；具体 binning 参数需要人工核验。
### 2. Spiking Neuron / SNN Module

NCM 根据 cross-modal features 动态调节 neuron configuration，使 spikes 更集中于 blurry regions。
### 3. Network Architecture

BDHNet 包含 event SNN branch、image ANN branch、NCM、RBAM、fusion module 和 image reconstruction decoder。
### 4. Training / Loss

论文报告使用 GoPro、REBlur、MS-RBD 等数据进行训练/评估；具体 loss 组合和权重需要 V2 深读核验。
### 5. Inference

推理阶段用 event motion features 辅助恢复 frame texture，RBAM 负责把注意力限制到更可能模糊的区域。

## 6. Experiments

PDF Table 1 报告 GoPro 与 REBlur 上的 PSNR/SSIM 对比；Table 2 是 GoPro ablation，涉及 Image、Event、NCM、Mask/Fusion module 对 PSNR/SSIM 的贡献。PDF conclusion 声称 BDHNet 在 synthetic 和 real-world scenarios 上优于现有方法。精确数值需要人工复核表格。

## 7. Main Contributions

1. 提出 Bio-inspired Dual-Drive Hybrid Network (BDHNet) 处理 event-based motion deblurring。
2. 设计 NCM 动态配置 spiking neuron，使 event spikes 关注 blurry regions。
3. 设计 RBAM 以 unsupervised blurry mask 引导 cross-modal feature fusion。
4. 在 GoPro、REBlur、MS-RBD 等场景展示 image/event fusion 对 deblurring 的作用。

## 8. Limitations and Risks

- [Inferred] SNN 主要作为 event branch feature extractor，完整系统不是 fully spiking。
- PSNR/SSIM 改善是否来自 event branch、mask 或训练数据，需要仔细看 ablation 细节。
- real-world deblurring 的 ground truth 构造和 domain gap 需要人工核验。

## 9. Relation to SNN for Event Cameras

分类：A: SNN + Event Camera core paper。它把 SNN 直接放入 event camera restoration pipeline，是 survey 中 “Hybrid ANN-SNN models” 与 “Event reconstruction/restoration” 的交叉案例。

## 10. Relation to Survey Taxonomy

- Hybrid ANN-SNN models
- Event reconstruction
- SNN architectures for event cameras
- Event representations for SNNs
- Open challenges

## 11. Key Terms and Concepts

- BDHNet：Bio-inspired Dual-Drive Hybrid Network。
- NCM：Neuron Configurator Module，用 cross-modal features 调整 spiking neuron。
- RBAM：Region of Blurry Attention Module，生成 blurry mask。
- PSNR/SSIM：image restoration 常用质量指标。

## 12. Questions for Human Deep Reading

1. NCM 具体调节哪些 neuron parameters？
2. event representation 的 time bin 和 polarity handling 如何设置？
3. RBAM 的 unsupervised mask 是否有额外正则？
4. GoPro/REBlur/MS-RBD 的训练和测试划分是否公平？
5. SNN branch 的能耗或 spike sparsity 是否被量化？
6. 与纯 ANN event deblurring 方法相比，主要收益来自哪里？

## 13. Evidence Notes

- PDF Abstract 与 Section 3: BDHNet、NCM、RBAM。
- PDF Table 1: GoPro/REBlur PSNR/SSIM comparison。
- PDF Table 2: ablation study。
- PDF Conclusion: dual-drive and attention modules 的总体结论。

## 14. Draft Survey-Usable Sentences

Draft material: ClearSight is a hybrid event deblurring system in which an SNN branch extracts motion cues from events while an ANN branch preserves image appearance.

Draft material: Its NCM/RBAM design is useful evidence that spiking modules can be used as adaptive event feature extractors inside restoration pipelines.
