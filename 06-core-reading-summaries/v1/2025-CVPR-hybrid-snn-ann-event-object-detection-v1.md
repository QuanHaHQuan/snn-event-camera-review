---
title: "Efficient Event-Based Object Detection: A Hybrid Neural Network with Spatial and Temporal Attention"
authors: ["Soikat Hasan Ahmed", "Jan Finkbeiner", "Emre Neftci"]
year: 2025
venue: "CVPR"
level: "A"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/CVPR2025/A/2025-CVPR-A-efficient-event-based-object-detection-a-hybrid-neural-network-with-spatial-and-temporal-a.md"
official_page: "https://openaccess.thecvf.com/content/CVPR2025/html/Ahmed_Efficient_Event-Based_Object_Detection_A_Hybrid_Neural_Network_with_Spatial_CVPR_2025_paper.html"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2025/papers/Ahmed_Efficient_Event-Based_Object_Detection_A_Hybrid_Neural_Network_with_Spatial_CVPR_2025_paper.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["SNN", "ANN-SNN hybrid", "event camera", "object detection", "ASAB", "Loihi 2", "Gen1", "Gen4"]
---

# Summary V1｜Efficient Event-Based Object Detection: A Hybrid Neural Network with Spatial and Temporal Attention

## 1. One-sentence Summary

本文提出 Attention-based Hybrid SNN-ANN backbone，用 SNN block 提取低层快速事件特征，再通过 ASAB bridge 转为 dense feature maps 给 ANN detector，从而在 Gen1/Gen4 event-based object detection 上取得较高精度和较低参数/能耗。

## 2. Research Problem

event-based object detection 需要同时处理高时间分辨率、稀疏性和低功耗部署。纯 ANN 往往精度较高但参数和 MACs 大；纯 SNN 适合 neuromorphic hardware 但精度和灵活性不足。本文试图结合二者：用 SNN 处理 early event features，用 ANN/RNN 处理 dense high-level features。

## 3. Background and Motivation

DVS / event cameras 具有低延迟、高动态范围和 minimal motion blur，适合 fast-motion 和 low-light detection。SNN 在 neuromorphic hardware 上能利用 sparsity，但目前 SNN-based detectors 往往落后于 ANN/RNN/Transformer detectors。本文动机是构建 hybrid SNN-ANN，让 SNN 的低功耗和 ANN 的高表达能力互补。

## 4. Method Overview

pipeline 包含 event tensor construction、SNN low-level spatio-temporal extractor、Attention-based SNN-ANN Bridge (ASAB)、ANN high-level spatial extractor、可选 DWConvLSTM variant，以及 YOLOX-style detection head。

输入是 event tensor `T x 2 x H x W`，其中 T 是 time discretization steps，2 是 polarity channels。输出是 object bounding boxes。SNN part 处理短时间尺度 fast dynamics；ASAB 把 sparse spiking features 转成 dense features；ANN/DWConvLSTM 捕获更高层空间特征和慢时间动态。

## 5. Technical Details

### Event Representation

事件 `e_n=(x_n,y_n,t_n,p_n)` 被离散成 4D tensor。训练时用 5 ms bins 构建 event representation；检测每 50 ms 生成一次，使用最后 10 time bins。

### Spiking Neuron / SNN Module

SNN blocks 由 convolution、batch normalization 和 PLIF spiking neuron 组成。PLIF 有 trainable time constant，用于 event-level spatio-temporal feature extraction。

### Network Architecture

ASAB 包含 Spatial-aware Temporal (SAT) attention 和 Event-Rate Spatial (ERS) attention。SAT 使用 channel-wise temporal grouping、Time-wise Separable Deformable Convolution (TSDC) 和 temporal self-attention；ERS 根据 summed event rate 生成 spatial attention weight。可选 hybrid+RNN variant 加入 DWConvLSTM 捕获 slow dynamics。

### Training Strategy

模型用 PyTorch 和 SpikingJelly 端到端训练。Gen1 训练 50 epochs，batch size 24，learning rate 2e-4，约 8 小时，4 张 3090 GPUs；Gen4 训练 10 epochs，batch size 8，learning rate 3.5e-4，约 1.5 天。RNN variant 训练 400k steps，batch size 2，约 6 天。

### Loss Function

detection head 使用 YOLOX framework，包含 IOU loss、class loss 和 regression loss。论文的核心贡献在 ASAB / hybrid backbone，而不是 detection loss。

### Inference Process

推理时 SNN block 可在 neuromorphic hardware 上运行，输出中间 spiking features；ASAB 和 ANN/detection head 完成 dense detection。SNN block 在 Loihi 2 上实现并测试了 power/time。

## 6. Experiments

数据集为 Gen1 Automotive Detection 和 Gen4 Automotive Detection。Gen1 含 39 小时 event recordings，分辨率 304x240；Gen4 含 15 小时，分辨率 720x1280。类别包括 car、pedestrian，Gen4 还包括 two-wheeler。

Table 1 与 ANN-based methods 对比：Proposed Hybrid 参数 6.6M，在 Gen1 mAP 0.35，Gen4 mAP 0.27。Gen1 上略高于 Events-RetinaNet 0.34，低于强 RNN/Transformer methods；Gen4 上高于 Events-RetinaNet 0.18 和 E2Vid-RetinaNet 0.25，但低于 Inception+SSD / RRC-Events 的 0.34。

Table 2 与 SNN-based methods 对比：Proposed Hybrid 0.35 mAP，高于 VGG-11+SSD 0.17、DenseNet121-24+SSD 0.19、EMS-RES34 0.31、SpikeFPN 0.22。

Table 3 与 RNN/SSM methods 对比：Proposed+RNN 为 7.7M params，0.43 mAP，低于 RVT/S5/ASTMNet 的 0.46-0.48，但参数较少。

Table 4 ablation 显示完整 ASAB 达到 0.61 mAP(.5) / 0.35 mAP；去掉 ASAB 仅 0.53 / 0.30，说明 bridge module 关键。

Table 5 报告 Loihi 2 SNN block：int8/int6 约 1.71-1.73 W，2.06 ms/step；int4 约 1.95 W，1.16 ms/step。Table 6 显示 Proposed w/ ASAB 为 1.63e9 MACs、0.97e9 ACs，mAP(.5) 0.61；Baseline ANN 为 15.34e9 MACs。

## 7. Main Contributions

1. 提出 hybrid SNN-ANN event-based object detector。
2. 设计 ASAB bridge，把 sparse spiking features 转为 dense ANN features，同时保留 spatial/temporal relations。
3. 引入 SAT attention 和 ERS attention 处理 temporal coherence 与 event-rate spatial focus。
4. 在 Gen1/Gen4 上超过 SNN-based baselines，并接近部分 ANN methods。
5. 在 Intel Loihi 2 上实现 SNN block，提供硬件 power/time evidence。

## 8. Limitations and Risks

这不是 fully spiking detector，而是 hybrid SNN-ANN；survey 中应明确 SNN 主要在 early backbone 部分。

与强 RNN/SSM/Transformer methods 相比仍有精度差距，特别是 Gen1 上 RVT/S5/ASTMNet 约 0.46-0.48。

Loihi 2 只实现 SNN block，不是完整 end-to-end detector 部署；整体系统能耗还包含 ASAB/ANN/detection head。

RNN variant 训练成本高，约 6 天，和“efficient”叙述需分开看训练与推理。

## 9. Relation to SNN for Event Cameras

分类：A: SNN + Event Camera core paper。

它是典型 Hybrid ANN-SNN event camera detector，尤其适合 survey 中“Hybrid ANN-SNN models”和“neuromorphic hardware partial deployment”章节。

## 10. Relation to Survey Taxonomy

- Hybrid ANN-SNN models：SNN early extractor + ANN detector。
- Event-based object detection：Gen1/Gen4。
- SNN architectures for event cameras：PLIF SNN block + ASAB。
- Efficiency, latency, and energy：Loihi 2 measurements、MAC/AC analysis。
- Open challenges：full-system deployment、accuracy gap to RNN/SSM。

## 11. Key Terms and Concepts

- ASAB：Attention-based SNN-ANN Bridge。
- SAT attention：Spatial-aware Temporal attention。
- ERS attention：Event-Rate Spatial attention。
- TSDC：Time-wise Separable Deformable Convolution。
- DWConvLSTM：depth-wise separable ConvLSTM for slower dynamics。
- Loihi 2：Intel neuromorphic hardware used for SNN block benchmark。

## 12. Questions for Human Deep Reading

1. Loihi 2 测量是否包含 input/output transfer overhead？
2. ASAB 本身是否能部署到 neuromorphic hardware？
3. full detector end-to-end energy 是多少？
4. Gen4 上为什么低于 older ANN baselines？
5. mAP(.5) 和 COCO-style mAP 在文中如何对应？
6. Proposed SNN+ variant 的结构差异是什么？
7. RNN variant 与 RVT 的 high-frequency detection claim 是否公平？
8. 代码是否开源并可复现 Loihi 2 measurements？

## 13. Evidence Notes

- Section 3.1-3.3，第 3-5 页：event tensor、hybrid backbone、ASAB。
- Section 4.1，第 5 页：datasets and training setup。
- Table 1-3，第 6 页：ANN/SNN/RNN benchmark comparisons。
- Table 4，第 7 页：ASAB ablation。
- Table 5-6，第 7-8 页：Loihi 2 and computational analysis。
- Conclusion，第 8 页：summary and hardware implications。

## 14. Draft Survey-Usable Sentences

Draft material: This CVPR 2025 work is a clear hybrid SNN-ANN detector: the SNN processes early sparse event dynamics, while attention bridging converts spiking outputs into dense features for ANN detection.

Draft material: Its Loihi 2 experiment is valuable hardware evidence, but only for the SNN block rather than the full detector.

Draft material: The method improves over SNN-based detectors on Gen1, while still trailing stronger recurrent or state-space event detectors.

