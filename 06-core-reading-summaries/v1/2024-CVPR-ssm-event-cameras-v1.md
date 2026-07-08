---
title: "State Space Models for Event Cameras"
authors: ["Nikola Zubic", "Mathias Gehrig", "Davide Scaramuzza"]
year: 2024
venue: "CVPR"
level: "B"
priority: "P0"
advisor_track: "yes"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/CVPR2024/B/2024-CVPR-B-state-space-models-for-event-cameras.md"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Zubic_State_Space_Models_for_Event_Cameras_CVPR_2024_paper.html"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Zubic_State_Space_Models_for_Event_Cameras_CVPR_2024_paper.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["event camera", "SSM", "Transformer"]
---

# Summary V1｜State Space Models for Event Cameras

## 1. One-sentence Summary

本文围绕 State Space Models for Event Cameras，基于论文 PDF 中的方法与实验描述，总结其在 event-camera 背景方向 的主要问题、方法和证据。

## 2. Research Problem

Today state-of-the-art deep neural networks that process event-camera data first convert a temporal window of events into dense grid-like input representations. As such they exhibit poor generalizability when deployed at higher inference frequencies (i.e.

这对本项目的意义在于：它提供了 event-camera 任务、表示或 benchmark 背景，可用于后续 survey 中建立问题边界和比较基线。

## 3. Background and Motivation

As such they exhibit poor generalizability when deployed at higher inference frequencies (i.e. smaller temporal windows) than the ones they were trained on.

从 survey 角度看，需要关注它是否真正利用 event data 的 asynchronous / sparse / high-temporal-resolution 特性，或是否主要是把已有视觉/SNN 模型迁移到相关任务上。

## 4. Method Overview

smaller temporal windows) than the ones they were trained on. We address this challenge by introducing state-space models (SSMs) with learnable timescale parameters to event-based vision.

整体 pipeline、输入输出和模块边界已经在 PDF 中出现；本 V1 先记录高层结构，V2 阶段应逐图核对 architecture figure 和 method equations。

## 5. Technical Details

### Event Representation / Input

论文涉及 event streams / event camera data；具体表示形式请在 V2 阶段核对 PDF method section。

### Spiking Neuron / SNN Module

未发现明确 SNN/spiking module；该论文主要是 event-camera 或视觉模型背景。

### Network Architecture

smaller temporal windows) than the ones they were trained on. We address this challenge by introducing state-space models (SSMs) with learnable timescale parameters to event-based vision.

### Training Strategy

训练设置、pretraining/fine-tuning、augmentation 和 optimization 细节已在 PDF 中出现，但本轮只做自动抽取，精确超参数需要人工核验。

### Loss Function

若论文包含专门 loss 或 objective，本 V1 只记录其作用；公式符号和权重请在 V2 阶段结合 PDF 原文核对。

### Inference Process

推理过程需要结合模型 pipeline、event aggregation window 和硬件/软件环境进一步核验。

## 6. Experiments

PDF 自动抽取到以下实验相关证据线索：

- Evaluation of SSM, RVT, and GET-Transformer on Gen1 and 1 Mpx Test Datasets
- Our SSM-based models achieve an average performance drop between training and testing frequencies of 3.31 mAP averaged on both
- Gen1 [7] and 1 Mpx [29] datasets, while RVT [12] and GET [28] have a drop of 21.25 and 24.53 mAP, respectively.
- timescale parameters to event-based vision. This design
- exhibit performance drops of more than 20 mAP , with SSMs
- having a drop of 3.31 mAP , highlighting the effectiveness of
- compromised accuracy. In this work, we utilize dense repre-
- timescale parameters, thus inhibiting the model’s capacity

本 V1 只引用这些可从 PDF 抽取到的实验线索；完整数值、baseline 顺序和显著性比较需要人工在 V2 中逐表核对。

## 7. Main Contributions

1. 提出或系统化研究了与 `State Space Models for Event Cameras` 对应的核心方法/任务设定。
2. PDF 摘要和方法部分给出了主要模块设计，涉及 event camera, SSM, Transformer。
3. PDF 实验部分报告了数据集、指标或 ablation 线索，可作为后续人工深读的入口。
4. 对 survey 的价值在于补充 B: Event Camera side background 这一类证据，而不是直接作为未经核验的最终结论。

## 8. Limitations and Risks

- 本 V1 是自动 PDF-based 摘要，尚未逐式核验全部公式和表格数值。
- 若论文报告 efficiency / energy / latency，需要确认其是理论 operation count、GPU 测量还是 neuromorphic hardware 实测。
- 若论文属于 B/C 类，应避免在 survey 中把它误写成 SNN + Event Camera core method。
- 部分实验结论可能依赖特定 dataset split、pretraining 设置或 implementation details，需要人工复核。

## 9. Relation to SNN for Event Cameras

分类：B: Event Camera side background。

理由：reading plan 将该论文标为 level B；PDF 内容显示其关键词和任务与 `event camera, SSM, Transformer` 相关。最终归类仍应在 V2 阶段结合全文细读修正。

## 10. Relation to Survey Taxonomy

- Surrogate gradient and temporal credit assignment
- Open challenges

## 11. Key Terms and Concepts

- event camera: 论文中相关的关键概念，V2 阶段需要结合原文定义进一步精读。
- State Space Model: 论文中相关的关键概念，V2 阶段需要结合原文定义进一步精读。
- Transformer: 论文中相关的关键概念，V2 阶段需要结合原文定义进一步精读。
- mAP: 论文中相关的关键概念，V2 阶段需要结合原文定义进一步精读。
- Gen1: 论文中相关的关键概念，V2 阶段需要结合原文定义进一步精读。
- 1Mpx: 论文中相关的关键概念，V2 阶段需要结合原文定义进一步精读。

## 12. Questions for Human Deep Reading

1. PDF 中 method section 对核心模块的数学定义是什么？
2. 实验使用的数据集、划分和评价指标是否与 baseline 完全一致？
3. 主要提升来自 representation、architecture、training strategy 还是 post-processing？
4. 效率、能耗或 latency 结论是理论估算还是硬件实测？
5. 该论文对 SNN for Event Cameras survey 的贡献应归入方法、数据集、训练还是挑战部分？

## 13. Evidence Notes

- Local PDF parsed successfully: 2024-CVPR-state-space-models-for-event-cameras.pdf, 10 pages.
- PDF headings observed: State Space Models for Event Cameras; Previous work; Our work; Event; Abstract; 1. Introduction; 2. Related Work; 3. Method.
- PDF key experiment/evidence lines include datasets/metrics/table mentions listed in Section 6.

## 14. Draft Survey-Usable Sentences

Draft material: `State Space Models for Event Cameras` can be cited cautiously as B: Event Camera side background evidence after its quantitative tables and method details are manually verified.

Draft material: The paper is useful for mapping how event camera, SSM, Transformer relates to event-camera/SNN survey taxonomy, but V2 should refine the exact claim boundaries.
