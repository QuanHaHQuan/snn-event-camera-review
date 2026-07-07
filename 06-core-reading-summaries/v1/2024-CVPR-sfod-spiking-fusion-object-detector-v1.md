---
title: "SFOD: Spiking Fusion Object Detector"
authors: ["Yimeng Fan", "Wei Zhang", "Changsong Liu", "Mingyang Li", "Wenrui Lu"]
year: 2024
venue: "CVPR"
level: "A"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/CVPR2024/A/2024-CVPR-A-sfod-spiking-fusion-object-detector.md"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Fan_SFOD_Spiking_Fusion_Object_Detector_CVPR_2024_paper.html"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Fan_SFOD_Spiking_Fusion_Object_Detector_CVPR_2024_paper.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["SNN", "event camera", "object detection", "feature fusion", "spiking decoding", "GEN1", "NCAR"]
---

# Summary V1｜SFOD: Spiking Fusion Object Detector

## 1. One-sentence Summary

SFOD 提出一种面向 event camera object detection 的 SNN detector，通过 Spiking Fusion Module 融合多尺度 spiking feature maps，并结合 Spiking Rate Decoding 与 MSE loss 提升 NCAR 分类预训练和 GEN1 检测性能。

## 2. Research Problem

这篇论文解决的是 event camera 数据上的 object detection 问题，尤其关注如何让 Spiking Neural Networks 在保持事件数据稀疏性和低功耗潜力的同时获得更好的检测精度。

event cameras 输出异步、稀疏的 brightness-change events，适合高速运动、高动态范围和低功耗场景，但这种数据格式对传统 dense frame-based detection pipeline 并不友好。SNN 以 spike 为计算单元，天然接近 event stream 的离散和时序特征，因此是 event-camera perception 的重要候选方法。

论文认为已有 SNN-based event-camera object detection 工作仍然性能有限，一个关键缺口是缺少适合 SNN 的 multi-scale feature map fusion。传统 object detector 常用多尺度融合，但直接照搬 element-wise sum、bilinear interpolation 等非脉冲网络操作可能破坏 SNN 的二值 spike 特性并增加计算复杂度。

## 3. Background and Motivation

event camera 与普通 frame camera 不同，它在像素亮度变化超过阈值时异步产生事件，因此具有 high temporal resolution、high dynamic range、low power consumption 和 high pixel bandwidth 等优势。object detection 任务中，这些优势对快速运动、复杂光照和车载场景尤其有价值。

SNN 被论文称为第三代神经网络，使用 spiking neurons 进行信息编码与处理。论文采用 PLIF neurons，并选择 direct training / surrogate-gradient 方向，而不是 ANN-to-SNN conversion，因为 conversion 往往需要大量 time steps，且更适合静态数据，不适合 event-driven datasets。

在 event-based object detection 背景中，非 SNN 方法通常会把事件积分成帧，或使用 RNN / Transformer 保留时间信息。论文认为这些方法虽然性能强，但未充分利用 event data 的稀疏性；而早期 SNN detection 方法如 MobileNet-64+SSD、VGG-11+SSD、DenseNet121-24+SSD 和 EMS-YOLO 在 GEN1 上的检测性能仍有提升空间。

## 4. Method Overview

SFOD 的整体 pipeline 是：先把原始 event stream 编码为 voxel cube，再输入 Spiking DenseNet backbone 提取特征；随后用 Extra Block 产生更深层 feature maps；核心的 Spiking Fusion Module 对选定的多尺度 feature maps 进行上采样、拼接和 pyramid feature regeneration；最后将处理后的特征送入 SSD detection head 输出 object detection results。

输入数据类型是 event camera 事件流。事件表示采用 voxel cube，把给定时间窗口内的事件按 time bins、polarity 和空间坐标组织成张量。论文设置 T = 5，并把每个 time bin 进一步分成 n = 2 个 micro time bins；结合正负 polarity，输入 channel 数为 C = 2n。

模型架构由 Spiking DenseNet backbone、Extra Blocks、Spiking Fusion Module 和 SSD detection head 组成。SNN/spiking component 体现在 backbone、feature fusion pipeline 中使用 PLIF neurons，以及输出到 SSD head 前对 spiking feature maps 进行 spiking decoding。SSD head 本身由 convolution 组成，不含 activation functions，因此进入 head 之前需要解码。

该方法不是典型 ANN-SNN hybrid；论文把 SFOD 归为 SNN-based object detector，但 head 的卷积检测部分在解码后处理特征，能量估计与真正全链路 neuromorphic 部署之间仍需人工阅读 supplement 后核验。

## 5. Technical Details

### Event Representation

论文采用 voxel cube 表示事件。对时间区间 [ta, tb) 内的事件 e_k，事件被映射到离散时间 bin、polarity channel 和像素坐标上。公式 (1) 表示 voxel cube 中某个时间、极性和空间位置的事件累积；公式 (2) 把连续 timestamp t_k 映射为离散 time bin τ_k。

需要注意的是，论文中公式 (2) 的排版抽取结果显示为 `(t_k - t_a) / (t_a - t_b) * T`，人工阅读时应核对 PDF 原式是否为常见的 `(t_k - t_a) / (t_b - t_a) * T`，因为分母符号在文本抽取中可能存在 OCR/排版误读。

### Spiking Neuron / SNN Module

论文用 PLIF neurons 替换传统 activation functions。PLIF 的作用是以可学习膜时间常数建模 spike firing dynamics，从而让网络在直接训练中更好适应时序事件数据。论文没有在正文中完整展开 PLIF 方程，相关细节主要来自引用文献。

### Network Architecture

Spiking DenseNet 被选为 backbone，原因是前作在 event-camera SNN detection 上表现较好。Extra Block 由 1x1 和 3x3 convolution 组成，用于提取更深层特征。SSD detection head 接收解码后的多尺度特征，输出 detection boxes 和分类结果。

Spiking Fusion Module 包含三个部分：Deconv Block、concat fusion 和 Spiking Pyramid Extraction Submodule (SPES)。论文公式 (3) 用 `X_p = Phi_p(Phi_f(union {Phi_i(X_i)}))` 描述融合过程，其中 `X_i` 是原始多尺度 feature maps，`Phi_i` 对应 Deconv Block，`Phi_f` 对应 concat，`Phi_p` 对应 SPES，`X_p` 是融合后重新生成的 pyramid feature maps。

### Feature Fusion Design

论文从 backbone 和 Extra Block 中候选的六个 feature maps 里选择前三层用于融合，分辨率为 30x38、15x19 和 7x9。更深的 4x5、2x3、1x2 feature maps 虽然 receptive field 更大，但空间分辨率较低；实验显示加入第四层会降低 mAP，因此最终采用三层融合。

融合方式选择 concat，而不是 element-wise sum。作者的理由是 element-wise summation 会破坏 SNN 的二值性并增加计算复杂度。为对齐空间尺寸，论文使用 transposed convolution 上采样，而不是 bilinear interpolation，因为后者包含较多 multiplication 和 division，不符合 SNN 友好设计。每个 Deconv Block 前还用 1x1 convolution 调整 channel 和非线性表达。

SPES 用于把拼接后的高分辨率 fused feature maps 重新生成多尺度 pyramid features。论文比较了 basic SPES、Spiking Dense Block-enhanced SPES 和 SEW Res Block-enhanced SPES，最终选择 SEW Res Block-enhanced version，即 SFOD-R。

### Training Strategy

论文采用 direct training，而不是 ANN-to-SNN conversion。优化器为 AdamW，学习率调度为 cosine learning rate scheduler。NCAR 分类预训练训练 30 epochs，batch size 64，initial learning rate 5e-3，weight decay 1e-2。GEN1 检测训练 50 epochs，batch size 16，initial learning rate 1e-3，weight decay 1e-4，并使用 horizontal flipping 做数据增强。

### Loss Function

论文重点比较 Spiking Rate Decoding / Spiking Count Decoding 与 MSE / CE 的组合。公式 (4) 是 MSE，它直接度量 label 与 decoded value 的平方误差；公式 (5) 是 CE，它基于 post-softmax probability value 计算分类损失。

作者认为 MSE 更适合 Spiking Rate Decoding，因为 SNN 输出的是离散 spike count 或 frequency，MSE 可以直接基于 decoded values 提供梯度；CE 需要 softmax，把离散输出转成概率分布，可能改变梯度含义并增加计算复杂度。Table 1 支持这一点：DenseNet121-16 使用 Rate + MSE 时 accuracy 为 0.937，firing rate 为 14.70%，优于 Rate + CE 的 0.930 / 20.42%。

### Inference Process

推理时，event stream 先被编码为 voxel cube，经过 spiking backbone 与 fusion module 后得到 spiking feature maps。由于 SSD detection head 不含 activation functions，论文在送入 head 之前采用 Spiking Rate Decoding，把 spike count 除以 time steps 得到归一化后的 decoded features，再由 SSD head 产生 detection output。

## 6. Experiments

论文使用两个数据集。NCAR 用于 car/background 二分类，包含 12,336 car samples 和 11,693 background samples，每个样本持续 100 ms。GEN1 用于 object detection，是 large-scale event-based automotive detection dataset，包含超过 39 小时的 GEN1 camera 视频，并在 1-4 Hz 频率提供 car 和 pedestrian bounding boxes，总计超过 255,000 labels。

分类任务指标是 accuracy；检测任务指标是 mAP@0.5:0.95 和 mAP@0.5；SNN efficiency 相关指标是 firing rate，即所有 time steps 上 neuron spikes 数量与总 neuron 数量的平均比例。论文还在 GEN1 benchmark comparison 中报告了 inference time 和 energy，但 energy 计算方法位于 supplementary material，正文未给完整细节。

NCAR 上，Table 1 显示 DenseNet121-16 + Spiking Rate Decoding + MSE 取得 0.937 accuracy 和 14.70% firing rate；Count + MSE 为 0.869 / 12.95%，Rate + CE 为 0.930 / 20.42%，Count + CE 为 0.920 / 17.09%。Table 2 比较不同 Spiking DenseNet architectures，DenseNet121-16 在 accuracy / firing rate trade-off 上最好。Table 3 显示该 SNN 模型在 NCAR 上超过列出的 SNN baselines，并接近 Asynet 的 0.944。

GEN1 消融见 Table 4。DenseNet121-24-SSD 在 rate decoding 和无 fusion 时达到 0.288 mAP@0.5:0.95、0.553 mAP@0.5、22.29% firing rate。SFOD-B 三层融合达到 0.299 / 0.575 / 24.41%。SFOD-D 降为 0.286 / 0.558 / 26.37%。最终 SFOD-R 达到 0.321 mAP@0.5:0.95、0.593 mAP@0.5、24.04% firing rate，参数量 11.9M。

GEN1 benchmark comparison 见 Table 5。与 SNN baselines 相比，SFOD 的 0.321 mAP@0.5:0.95 高于 MobileNet-64+SSD 的 0.147、VGG-11+SSD 的 0.174、DenseNet121-24+SSD 的 0.189 和 EMS-YOLO 的 0.310。与非 SNN 方法相比，SFOD 高于 Asynet、AEGNN、Inception+SSD、MatrixLSTM，但低于 RED 的 0.400 和 RVT 的 0.472。论文报告 SFOD 参数量 11.9M、firing rate 24.04%、time 6.7 ms、energy 7.26 mJ。

## 7. Main Contributions

1. 提出 Spiking Fusion Module，用 Deconv Block、concat 和 SPES 在 SNN 中实现 event-camera object detection 的多尺度 spiking feature fusion。
2. 构建 SFOD，把 Spiking DenseNet、Spiking Fusion Module 和 SSD detection head 组合为一个 SNN-based event-camera object detector。
3. 系统比较 Spiking Rate Decoding、Spiking Count Decoding 与 MSE、CE 的组合，并在 NCAR 预训练实验中显示 Rate + MSE 对该设置最有效。
4. 在 GEN1 上通过 SFOD-R 达到 0.321 mAP@0.5:0.95，超过论文列出的 SNN-based detection baselines。
5. 通过消融分析说明三层 fusion、SEW Res Block-enhanced SPES 和 rate decoding 对最终性能的影响。

## 8. Limitations and Risks

论文的主要限制之一是与强 non-SNN event-based detectors 仍有明显差距，尤其 Table 5 中 RVT 达到 0.472 mAP@0.5:0.95，RED 达到 0.400，而 SFOD 为 0.321。因此在 survey 中不能把它表述为 event-based object detection 的总体 SOTA，只能说是论文报告的 SNN-based setting 下强结果。

能耗结论需要谨慎。正文 Table 5 给出 energy numbers，但 energy 计算方法放在 supplementary material；V1 只确认正文报告值，不应在未核 supplement 的情况下扩展为硬件部署结论。

SFOD 使用 SSD head，并且在进入 head 前进行 spiking decoding，因此它不是严格意义上从输入到输出全程 spike-only 的 detector。它仍然是 SNN-based event-camera detector，但 survey 中应区分 fully spiking、hybrid decoded-head 和 ANN-SNN hybrid 等类别。

论文对 voxel cube 的事件表示依赖固定时间窗口和 time bins，可能牺牲部分原始异步性；这是一种常见但值得在 taxonomy 中标注的 event representation choice。

数据增强较简单，作者在 conclusion 中也认为更有效的数据增强可能进一步提升性能。这说明方法性能可能受训练 recipe 限制。

## 9. Relation to SNN for Event Cameras

分类：A: SNN + Event Camera core paper。

原因是该论文同时满足 survey 的两个核心轴：输入和任务来自 event camera / event stream，模型主体采用 SNN / spiking computation，并直接研究 event-camera object detection。它不仅把 SNN 用作背景或通用模型，也提出了面向 event-camera detection 的 spiking feature fusion 和 decoding 设计。

在 survey 中，它适合作为“SNN architectures for event cameras”和“Event-based object detection”交叉处的核心案例，也可用于讨论 SNN 在事件视觉中如何处理 multi-scale feature fusion。

## 10. Relation to Survey Taxonomy

可支持的 future survey sections：

- Event representations for SNNs：voxel cube、time bins、micro time bins、polarity channels。
- SNN architectures for event cameras：Spiking DenseNet backbone、PLIF neurons、Spiking Fusion Module。
- Hybrid ANN-SNN models：需要谨慎放入，因 SSD head 前有 spiking decoding，但主体仍是 SNN-based。
- Event-based object detection：GEN1 car/pedestrian detection。
- SNN training methods：direct training、surrogate-gradient context、AdamW + cosine schedule。
- Efficiency, latency, and energy：firing rate、time、energy comparison，但 energy 需 supplement 核验。
- Datasets and benchmarks：NCAR classification pretraining 与 GEN1 detection benchmark。
- Open challenges：与 non-SNN high-performing methods 的差距、事件表示离散化、SNN-friendly fusion 设计。

## 11. Key Terms and Concepts

- Event camera：异步记录像素亮度变化的视觉传感器，适合高速、高动态范围和低功耗场景。
- Voxel cube：把事件按时间、极性和空间坐标离散成张量的 event representation。
- Spiking Neural Network (SNN)：使用 spike trains 和 spiking neurons 处理信息的神经网络。
- PLIF neuron：Parametric Leaky Integrate-and-Fire neuron，带可学习参数的脉冲神经元模型。
- Spiking DenseNet：用于特征提取的 SNN backbone，来自前作并在本文中用于 NCAR 预训练和 GEN1 detection。
- Spiking Fusion Module：本文核心模块，用于 SNN 中的多尺度 feature fusion。
- Deconv Block：由 1x1 convolution 和 transposed convolution 组成，用于 channel 对齐和上采样。
- SPES：Spiking Pyramid Extraction Submodule，用于从 fused feature map 重新生成 pyramid features。
- SEW Res Block：Spike-Element-Wise Residual Block，用于增强 SPES，构成最终 SFOD-R。
- Spiking Rate Decoding：把 spike count 除以 time steps 的输出解码方式，使输出范围归一化。
- Spiking Count Decoding：直接统计 spike count 的输出解码方式。
- Firing rate：SNN 神经元活动水平指标，表示 spike 数占总神经元数和时间步的平均比例。
- GEN1：event-based automotive object detection dataset，含 car 和 pedestrian boxes。
- NCAR：event-based car/background binary classification dataset。

## 12. Questions for Human Deep Reading

1. 公式 (2) 中 time-bin mapping 的分母在 PDF 原文是否存在排版符号问题？应与代码实现对齐核验。
2. SFOD 中 SSD detection head 的非 spiking 部分占整体计算和能耗多少？supplement 是否给出清晰计算边界？
3. Table 5 的 energy 计算是否基于理论 operation counting、特定硬件假设，还是实际测量？
4. Spiking Fusion Module 的 concat 是否会显著增加 channel 数和 memory footprint？论文是否讨论存储开销？
5. 为什么加入第四层 feature map 降低 mAP？是分辨率过低、上采样困难，还是训练不稳定？
6. SFOD-R 引入 SEW Res Block 后包含哪些 non-spiking computations？这些操作对 neuromorphic 部署是否有影响？
7. voxel cube 的 T = 5、micro time bin = 2 是否经过调参？不同 time resolution 对 mAP 和 firing rate 的影响如何？
8. GEN1 上与 EMS-YOLO 的公平性如何？二者训练设置、输入表示、time steps 和数据增强是否一致？
9. NCAR 预训练 backbone 对 GEN1 detection 的迁移贡献有多大？是否有 no-pretrain ablation？
10. 论文代码是否复现 Table 4/5 的关键结果，尤其是 SFOD-R 的 0.321 mAP 和 7.26 mJ？

## 13. Evidence Notes

- 论文基本信息来自 CVF official page：CVPR 2024，pp. 17191-17200，authors 为 Yimeng Fan、Wei Zhang、Changsong Liu、Mingyang Li、Wenrui Lu。
- Abstract 和 Introduction，第 17191-17192 页：说明 event cameras 的优势、SNN 的适配性、已有 SNN detection 性能有限，以及本文提出 SFOD。
- Figure 2，第 17193 页：展示 SFOD architecture，包括 Spiking Fusion Module、Spiking DenseNet、Extra Blocks、Deconv Blocks 和 SSD head。
- Section 3.1，第 17193 页：描述 voxel cube event coding、Spiking DenseNet backbone、Extra Block、Spiking Fusion Module、SSD head，以及使用 PLIF neurons。
- Section 3.2，第 17193-17194 页：描述 Spiking Fusion Module、三层 feature maps、concat fusion、transposed convolution 和 SPES。
- Figure 3，第 17194 页：展示 SPES 的三种结构变体。
- Section 3.3，第 17194-17195 页：比较 Spiking Count Decoding、Spiking Rate Decoding、MSE 和 CE。
- Table 1，第 17195 页：给出 decoding / loss function 在 NCAR 上的消融结果。
- Section 4.1，第 17195-17196 页：给出 NCAR、GEN1 数据集、训练超参数、metrics 和 firing rate 定义。
- Table 2 和 Table 3，第 17196-17197 页：给出 NCAR backbone architecture comparison 和 NCAR SOTA comparison。
- Table 4，第 17197 页：给出 GEN1 ablation，包括 backbone、fusion layers、SPES variants。
- Table 5，第 17197 页：给出 GEN1 benchmark comparison，包括 mAP、firing rate、time 和 energy。
- Figure 4，第 17198 页：展示 GEN1 detection visualization。
- Conclusion，第 17198 页：作者总结 SFOD 和 Rate + MSE 的作用，并指出未来可通过更有效的数据增强进一步提升。

## 14. Draft Survey-Usable Sentences

Draft material: SFOD is a representative SNN-based event-camera object detector that adapts multi-scale feature fusion to spiking feature maps through deconvolution, concatenation, and a spiking pyramid extraction module.

Draft material: On GEN1, the paper reports that SFOD-R improves over prior SNN-based detectors, reaching 0.321 mAP@0.5:0.95, while remaining below stronger non-SNN event-based detectors such as RED and RVT in the same comparison table.

Draft material: The paper highlights that decoding choices matter for event-camera SNNs: in its NCAR pretraining experiments, Spiking Rate Decoding with MSE outperforms alternatives involving Spiking Count Decoding or CE loss.

Draft material: For survey taxonomy, SFOD is useful as an example of SNN-friendly architectural adaptation, but its decoded SSD head and energy assumptions should be described carefully rather than treated as evidence of fully spike-only deployment.
