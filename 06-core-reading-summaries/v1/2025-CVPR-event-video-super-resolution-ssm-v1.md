---
title: "Event-based Video Super-Resolution via State Space Models"
authors: ["Zeyu Xiao", "Xinchao Wang"]
year: 2025
venue: "CVPR"
level: "B"
priority: "P0"
advisor_track: "yes"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/CVPR2025/B/2025-CVPR-B-event-based-video-super-resolution-via-state-space-models.md"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Xiao_Event-based_Video_Super-Resolution_via_State_Space_Models_CVPR_2025_paper.html"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Xiao_Event-based_Video_Super-Resolution_via_State_Space_Models_CVPR_2025_paper.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["event camera", "video super-resolution", "Mamba", "SSM", "MamEVSR", "iMamba", "cMamba"]
---

# Summary V1｜Event-based Video Super-Resolution via State Space Models

## 1. One-sentence Summary

本文提出 MamEVSR，用 interleaved Mamba 和 crossmodality Mamba 在 linear complexity 下融合 video frames 与 event information，实现 event-based video super-resolution。

## 2. Research Problem

VSR 需要利用相邻帧时序相关性；event cameras 可提供细粒度 motion details，但 CNN 的 receptive field 有限、Transformer 计算复杂度高。

## 3. Background and Motivation

Mamba/selective SSM 以线性复杂度建模长程依赖，适合高分辨率 video/event fusion。event streams 为 VSR 提供高时间分辨率运动线索，可弥补 frame blur 和 motion ambiguity。

## 4. Method Overview

MamEVSR 包含 iMamba block 和 cMamba block。iMamba interleaves tokens from adjacent frames，并进行 multidirectional selective state-space modeling，实现双向 frame feature fusion/propagation；cMamba 在 event information 与 iMamba output 之间做跨模态交互和聚合。输出为 super-resolved video frames。

## 5. Technical Details

### 1. Event Representation

事件作为辅助 modality 输入 cMamba；具体 voxel/binning 需 PDF 核验。
### 2. SSM Architecture

iMamba 处理相邻 frame tokens，cMamba 融合 event/frame modality。
### 3. SNN Module

无 SNN，是 event-camera + SSM background。
### 4. Training / Loss

VSR 常用 reconstruction/perceptual losses；本文具体 loss 需要人工核验。
### 5. Inference

Mamba 提供 global receptive field coverage 和 linear complexity。

## 6. Experiments

PDF Section/abstract 表示 MamEVSR 在 various datasets 上取得 quantitative 和 qualitative superior performance。具体 datasets、PSNR/SSIM、runtime 和 ablations 需要人工核验 PDF 表格。

## 7. Main Contributions

1. 提出 Mamba-based event VSR network MamEVSR。
2. 设计 iMamba 进行 inter-frame bidirectional fusion。
3. 设计 cMamba 融合 event 与 frame features。
4. 把 selective SSM 引入 event-based video super-resolution。

## 8. Limitations and Risks

- 不是 SNN 方法，survey 中应作为 event-camera restoration/SSM background。
- 需要核验 event modality 的实际贡献和 cMamba ablation。
- linear complexity 不等同于低能耗，实际 runtime/VRAM 需查看表格。

## 9. Relation to SNN for Event Cameras

分类：B: Event Camera side background; advisor-track support。它支持 event reconstruction/restoration 和 SSM temporal modeling 讨论。

## 10. Relation to Survey Taxonomy

- Event reconstruction
- Event representations for SNNs
- Efficiency, latency, and energy
- Open challenges

## 11. Key Terms and Concepts

- MamEVSR：Mamba-based event video super-resolution network。
- iMamba：interleaved Mamba block。
- cMamba：crossmodality Mamba block。
- VSR：Video Super-Resolution。

## 12. Questions for Human Deep Reading

1. 使用了哪些 event VSR datasets？
2. event input representation 是 voxel、stacked frame 还是 raw events？
3. cMamba 相比 concat/attention fusion 的提升是多少？
4. runtime 和 parameter count 如何？
5. 能否为 SNN-event fusion 提供结构启发？

## 13. Evidence Notes

- Source card / official abstract: iMamba、cMamba、linear complexity。
- Local PDF available; precise tables need human verification.

## 14. Draft Survey-Usable Sentences

Draft material: MamEVSR is not an SNN method, but it is useful background for event-frame temporal fusion with state-space models.

Draft material: Its iMamba/cMamba split provides a reference design for separating frame propagation and event-conditioned fusion.
