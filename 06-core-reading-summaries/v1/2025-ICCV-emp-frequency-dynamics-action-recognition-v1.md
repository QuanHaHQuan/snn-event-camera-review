---
title: "Exploiting Frequency Dynamics for Enhanced Multimodal Event-based Action Recognition"
authors: ["Meiqi Cao", "Xiangbo Shu", "Xin Jiang", "Rui Yan", "Yazhou Yao", "Jinhui Tang"]
year: 2025
venue: "ICCV"
level: "B"
priority: "P0"
advisor_track: "yes"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/ICCV2025/B/2025-ICCV-B-exploiting-frequency-dynamics-for-enhanced-multimodal-event-based-action-recognition.md"
official_page: "https://openaccess.thecvf.com/content/ICCV2025/html/Cao_Exploiting_Frequency_Dynamics_for_Enhanced_Multimodal_Event-based_Action_Recognition_ICCV_2025_paper.html"
pdf_link: "https://openaccess.thecvf.com/content/ICCV2025/papers/Cao_Exploiting_Frequency_Dynamics_for_Enhanced_Multimodal_Event-based_Action_Recognition_ICCV_2025_paper.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["event camera", "action recognition", "EMP", "CFE", "HGS", "frequency dynamics", "advisor-track"]
---

# Summary V1｜Exploiting Frequency Dynamics for Enhanced Multimodal Event-based Action Recognition

## 1. One-sentence Summary

本文提出 EMP framework，用 CFE 和 HGS 从 raw event streams 生成并选择高频/纹理线索，以减少对 paired RGB 的依赖并提升 event-based action recognition。

## 2. Research Problem

event cameras 具有强时间动态但空间纹理稀疏；RGB-Event multimodal methods 需要额外 RGB acquisition，削弱 privacy advantage 并增加成本。

## 3. Background and Motivation

event-to-image reconstruction 可从 events 中恢复 texture-enriched visual representation。频域信息可以区分 reconstructed frames 与 stacked event frames 的互补线索。

## 4. Method Overview

EMP 从 raw events 构造 reconstructed frames 与 stacked frames。Cross-Modal Frequency Enhancer (CFE) 利用两类表示的频率互补性优化 representation；High-Frequency Guided Selector (HGS) 以 dynamic edge features 选择 semantic-consistent tokens，抑制冗余 multimodal interference。输出为 action class。

## 5. Technical Details

### 1. Event Representation

使用 reconstructed frames 和 stacked frames 两种 event-derived modalities。
### 2. CFE

在 representation level 融合/增强互补 frequency characteristics。
### 3. HGS

在 feature level 用 high-frequency/edge guidance 选择 tokens。
### 4. Training / Loss

PDF 提到 balance parameter lambda；具体 loss 需人工核验。
### 5. SNN Module

无 SNN，是 event action recognition background。

## 6. Experiments

PDF Section 4 报告 PAF、SeAct、HARDVS 和 DVS128 Gesture。Table 1 比较 PAF、SeAct、DVS128 Gesture 上的 performance；PDF key lines 提到在 PAF 和 DVS128 Gesture 上有 3.31% 和 2.59% Top-1 accuracy gains。具体 HARDVS 和 ablation 需核验。

## 7. Main Contributions

1. 提出 privacy-preserving event-only multimodal perception 思路。
2. 提出 EMP 框架，包含 CFE 和 HGS。
3. 从 raw events 中构建 texture-enriched representation，减少 paired RGB 依赖。
4. 在多个 event action recognition datasets 上展示提升。

## 8. Limitations and Risks

- 不是 SNN 方法，主要是 event representation/background。
- reconstructed frames 是否引入额外计算和隐私泄露需讨论。
- Top-1 gains 需确认对应 baseline 和 dataset split。

## 9. Relation to SNN for Event Cameras

分类：B: Event Camera side background; advisor-track support。它可支撑 action recognition 和 event representation 章节。

## 10. Relation to Survey Taxonomy

- Event representations for SNNs
- Datasets and benchmarks
- Event reconstruction
- Open challenges

## 11. Key Terms and Concepts

- EMP：Enhanced Multimodal Perceptual framework。
- CFE：Cross-Modal Frequency Enhancer。
- HGS：High-Frequency Guided Selector。
- DVS128 Gesture/PAF/SeAct/HARDVS：event action recognition datasets。

## 12. Questions for Human Deep Reading

1. reconstructed frames 由哪个模型生成？
2. CFE 的频域操作具体在哪个 transform domain？
3. HGS token selection 是否可微？
4. HARDVS 上的提升是否同样显著？
5. event-only multimodal 是否仍保留低延迟优势？

## 13. Evidence Notes

- PDF Section 3: EMP, CFE, HGS。
- PDF Section 4: datasets PAF, SeAct, HARDVS, DVS128 Gesture。
- PDF Table 1: action recognition comparisons。
- PDF Conclusion: privacy-preserving event-only paradigm。

## 14. Draft Survey-Usable Sentences

Draft material: EMP is useful background for event-only multimodal representations, especially when discussing privacy-preserving alternatives to RGB-event fusion.

Draft material: Its frequency-guided design is non-spiking but may inspire event representations fed into SNNs.
