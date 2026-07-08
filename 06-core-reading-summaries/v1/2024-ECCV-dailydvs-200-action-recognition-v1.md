---
title: "DailyDVS-200: A Comprehensive Benchmark Dataset for Event-Based Action Recognition"
authors: ["Qi Wang", "Zhou Xu", "Yuming Lin", "Jingtao Ye", "Hongsheng Li", "Guangming Zhu", "Syed Afaq Ali Shah", "Mohammed Bennamoun", "Liang Zhang"]
year: 2024
venue: "ECCV"
level: "B"
priority: "P0"
advisor_track: "yes"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/ECCV2024/B/2024-ECCV-B-dailydvs-200-a-comprehensive-benchmark-dataset-for-event-based-action-recognition.md"
official_page: "https://eccv.ecva.net/virtual/2024/poster/330"
pdf_link: "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/11182.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["event camera", "dataset", "action recognition", "DailyDVS-200", "benchmark", "advisor-track"]
---

# Summary V1｜DailyDVS-200: A Comprehensive Benchmark Dataset for Event-Based Action Recognition

## 1. One-sentence Summary

本文提出 DailyDVS-200，一个包含 200 类日常动作、47 名参与者和超过 22,000 个 event sequences 的大规模 event-based action recognition benchmark。

## 2. Research Problem

event-based action recognition 缺少足够大、真实、多样且细粒度标注的数据集，限制了方法评估和泛化研究。

## 3. Background and Motivation

event cameras 在低延迟、高动态范围和能效方面有优势，但现有动作数据集常为模拟数据、类别少或场景简单。大规模真实数据对 SNN 和 event model 都是重要基础。

## 4. Method Overview

论文主要贡献是数据集而非模型。DailyDVS-200 覆盖 200 action categories、real-world scenarios、47 participants 和 14 attributes per sample；配套评估多个 event-based action recognition methods。

## 5. Technical Details

### 1. Event Representation

数据来自 DVS/event camera，记录 pixel intensity changes。
### 2. Dataset Design

强调 action category diversity、scene complexity、subject diversity 和 attributes。
### 3. Annotation

每个样本有 14 个属性，便于分析场景、姿态、持续时间等因素。
### 4. Baselines

PDF conclusion 称评估超过 10 different methods。
### 5. SNN Module

本文不是 SNN 方法，但可作为 SNN action recognition benchmark。

## 6. Experiments

PDF 与 abstract 报告 DailyDVS-200 含 200 categories、47 individuals、over 22,000 event sequences。论文进行 over 10 methods 的 evaluation 和 intragroup testing，并与其他 large-scale event datasets 对比，指出现有数据集可能过于容易而不利于推动方法创新。具体 baseline accuracies 需要人工核验表格。

## 7. Main Contributions

1. 提出大规模真实 event-based action recognition dataset DailyDVS-200。
2. 提供 200 类日常动作和超过 22,000 个 event sequences。
3. 为每个样本提供 14 attributes。
4. 系统评估十余种方法，揭示真实复杂场景中的挑战。

## 8. Limitations and Risks

- 不是 SNN 方法，survey 中应归入 dataset/background。
- 需要核验数据集 license、下载可用性和 train/test split。
- 动作类别和属性是否覆盖 SNN 研究常用场景需人工判断。

## 9. Relation to SNN for Event Cameras

分类：B: Event Camera side background; advisor-track support。它可支撑 event-based action recognition 和 dataset benchmark 章节，也可作为 SNN action recognition 评估资源。

## 10. Relation to Survey Taxonomy

- Datasets and benchmarks
- Event representations for SNNs
- SNN architectures for event cameras
- Open challenges

## 11. Key Terms and Concepts

- DailyDVS-200：大规模 event-based action recognition dataset。
- Attribute annotation：对样本场景/动作属性的细粒度标注。
- Intragroup testing：按属性或子组分析模型表现。

## 12. Questions for Human Deep Reading

1. 数据集具体 train/val/test split 是什么？
2. 14 attributes 分别是什么？
3. SNN baselines 是否包含 SpikePoint 等方法？
4. 是否有原始 event stream 和预处理 representation？
5. dataset license 是否允许 survey 复现实验？

## 13. Evidence Notes

- PDF Abstract/Introduction: dataset scale and motivation。
- PDF Figure 2: 与已有数据集比较。
- PDF Conclusion: 200 categories、47 individuals、over 22,000 sequences、14 attributes、over 10 methods。

## 14. Draft Survey-Usable Sentences

Draft material: DailyDVS-200 is a dataset resource for evaluating event-based action recognition under broader real-world diversity.

Draft material: For an SNN-event-camera survey, it is best cited as benchmark context rather than an SNN method contribution.
