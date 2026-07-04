---
title: "Towards Effective and Sparse Adversarial Attack on Spiking Neural Networks via Breaking Invisible Surrogate Gradients"
authors: ["Li Lun", "Kunyu Feng", "Qinglong Ni", "Ling Liang", "Yuan Wang", "Ying Li", "Dunshan Yu", "Xiaoxin Cui"]
conference: "CVPR"
year: 2025
level: "A"
category: "SNN + Event Camera"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Lun_Towards_Effective_and_Sparse_Adversarial_Attack_on_Spiking_Neural_Networks_CVPR_2025_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Lun_Towards_Effective_and_Sparse_Adversarial_Attack_on_Spiking_Neural_Networks_CVPR_2025_paper.html"
tags: []
abstract: "Spiking neural networks (SNNs) have shown their competence in handling spatial-temporal event-based data with low energy consumption. Similar to conventional artificial neural networks (ANNs), SNNs are also vulnerable to gradient-based adversarial attacks, wherein gradients are calculated by spatial-temporal back-propagation (STBP) and surrogate gradients (SGs). However, the SGs may be invisible for an inference-only model as they do not influence the inference results, and current gradient-based attacks are ineffective for binary dynamic images captured by the dynamic vision sensor (DVS). While some approaches addressed the issue of invisible SGs through universal SGs, their SGs lack a correlation with the victim model, resulting in sub-optimal performance. Moreover, the imperceptibility of existing SNN-based binary attacks is still insufficient. In this paper, we introduce an innovative potential-dependent surrogate gradient (PDSG) method to establish a robust connection between the SG and the model, thereby enhancing the adaptability of adversarial attacks across various models with invisible SGs. Additionally, we propose the sparse dynamic attack (SDA) to effectively attack binary dynamic images. Utilizing a generation-reduction paradigm, SDA can fully optimize the sparsity of adversarial perturbations. Experimental results demonstrate that our PDSG and SDA outperform state-of-the-art SNN-based attacks across various models and datasets. Specifically, our PDSG achieves 100% attack success rate on ImageNet, and our SDA obtains 82% attack success rate by modifying only 0.24% of the pixels on CIFAR10DVS. The code is available at https://github.com/ryime/PDSG-SDA ."
status: "auto-generated; needs human review"
---
## Core Problem

Spiking neural networks (SNNs) have shown their competence in handling spatial-temporal
event-based data with low energy consumption.

## Core Method

Similar to conventional artificial neural networks (ANNs), SNNs are also vulnerable to
gradient-based adversarial attacks, wherein gradients are calculated by spatial-temporal
back-propagation (STBP) and surrogate gradients (SGs).

## Key Metrics and Findings

自动流程尚未深读 PDF，不能可靠提取完整指标、数据集、对比方法和数值结论；需要人工核验后补充。

## Personal Notes

检索命中关键词：spiking neural networks; surrogate gradients; spiking。自动分类理由：Official abstract/page
strictly confirms both event-camera/DVS/visual-event-stream evidence and SNN/spiking neural
computation.。 备注：CVPR 2025 official CVF page inspected under broad high-recall title
workflow.。 该卡片用于优先阅读队列，引用前必须核对官方论文。

## Method Details

However, the SGs may be invisible for an inference-only model as they do not influence the
inference results, and current gradient-based attacks are ineffective for binary dynamic
images captured by the dynamic vision sensor (DVS). While some approaches addressed the
issue of invisible SGs through universal SGs, their SGs lack a correlation with the victim
model, resulting in sub-optimal performance. Moreover, the imperceptibility of existing SNN-
based binary attacks is still insufficient. In this paper, we introduce an innovative
potential-dependent surrogate gradient (PDSG) method to establish a robust connection
between the SG and the model, thereby enhancing the adaptability of adversarial attacks
across various models with invisible SGs. Additionally, we propose the sparse dynamic attack
(SDA) to effectively attack binary dynamic images. Utilizing a generation-reduction
paradigm, SDA can fully optimize the sparsity of adversarial perturbations. Experimental
results demonstrate that our PDSG and SDA outperform state-of-the-art SNN-based attacks
across various models and datasets. Specifically, our PDSG achieves 100% attack success rate
on ImageNet, and our SDA obtains 82% attack success rate by modifying only 0.24% of the
pixels on CIFAR10DVS. The code is available at https://github.com/ryime/PDSG-SDA .

## Experimental Analysis

需要人工检查实验数据集、任务设置、baselines、消融、延迟、能耗与硬件条件，避免把摘要级表述当成最终结论。

## Related Work Connections

该论文应与 Level B 的事件相机背景论文和 Level C 的 SNN 背景论文交叉阅读，确认它真正处在 SNN 与事件相机交叉点。

## Survey-Usable Points

可作为交叉方向候选核心论文；最终可用观点需要在人工阅读全文后再写入综述草稿。
