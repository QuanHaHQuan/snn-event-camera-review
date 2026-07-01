---
title: 'Scaling Dense Event-Stream Pretraining from Visual Foundation Models'
authors: ['Zhiwen Chen', 'Junhui Hou', 'Zhiyu Zhu', 'Jinjian Wu', 'Guangming Shi']
conference: 'CVPR'
year: 2026
level: 'B'
category: 'Event Camera'
pdf_link: 'https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_Scaling_Dense_Event-Stream_Pretraining_from_Visual_Foundation_Models_CVPR_2026_paper.pdf'
official_page: 'https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Scaling_Dense_Event-Stream_Pretraining_from_Visual_Foundation_Models_CVPR_2026_paper.html'
tags: []
abstract: 'Learning versatile, fine-grained representations from irregular event streams is pivotal yet nontrivial, primarily due to the heavy annotation that hinders scalability in dataset size, semantic richness, and application scope. To mitigate this dilemma, we launch a novel self-supervised pretraining method that distills visual foundation models (VFMs) to push the boundaries of event representation at scale. Specifically, we curate an extensive synchronized image-event collection to amplify cross-modal alignment. Nevertheless, due to inherent mismatches in sparsity and granularity between image-event domains, existing distillation paradigms are prone to semantic collapse in event representations, particularly at high resolutions. To bridge this gap, we propose to extend the alignment objective to semantic structures provided off-the-shelf by VFMs, indicating a broader receptive field and stronger supervision. The key ingredient of our method is a structure-aware distillation loss that grounds higher-quality image-event correspondences for alignment, optimizing dense event representations. Extensive experiments demonstrate that our approach takes a great leap in downstream benchmarks, significantly surpassing traditional methods and existing pretraining techniques. This breakthrough manifests in enhanced generalization, superior data efficiency and elevated transferability. The source code will be available.'
status: 'auto-generated; brief scan note'
---

## Core Problem

事件流表示学习受限于标注成本和图像-事件域间稀疏性、粒度差异，直接蒸馏视觉基础模型容易导致高分辨率事件表示语义坍塌。

## Core Method

论文构建同步 image-event collection，并用 VFM 提供的 semantic structures 做 structure-aware distillation，以获得 dense event representations。

## Key Metrics and Findings

摘要称在下游 benchmark 上显著超过传统方法和已有预训练方法，并提升泛化、数据效率和迁移能力；具体任务和数值需核表。

## Personal Notes

B 类事件流预训练论文，可用于事件表示学习、foundation model 迁移到事件数据的背景讨论。
