---
title: "FlexEvent: Towards Flexible Event-Frame Object Detection at Varying Operational Frequencies"
authors: ["Dongyue Lu", "Lingdong Kong", "Gim Hee Lee", "Camille Simon Chane", "Wei Ooi"]
year: 2025
venue: "NeurIPS"
level: "B"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/NeurIPS2025/B/2025-NEURIPS-B-flexevent-towards-flexible-event-frame-object-detection-at-varying-operational-frequencies.md"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/8064e4ebbcbe594628887b420956d8c3-Abstract-Conference.html"
pdf_link: "https://papers.nips.cc/paper_files/paper/2025/file/8064e4ebbcbe594628887b420956d8c3-Paper-Conference.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["event camera", "event-frame fusion", "object detection", "frequency adaptation", "DSEC"]
---

# Summary V1｜FlexEvent: Towards Flexible Event-Frame Object Detection at Varying Operational Frequencies

## 1. One-sentence Summary

FlexEvent 针对 event-frame object detection 的 varying operational frequencies 问题，提出 FlexFuse 和 FlexTune，使 detector 在 20 Hz 到 180 Hz 的事件频率变化下保持更稳定的检测性能。

## 2. Research Problem

论文解决的问题是：现有 event-based object detectors 常以固定频率或固定时间窗口处理事件，难以充分利用 event camera 的高时间分辨率，也难以在不同 operational frequencies 下泛化。这个问题在自动驾驶和高速动态场景中很重要，因为事件流本身可提供比人工标注帧更高频的时间信息。

对 SNN/Event Camera 综述而言，FlexEvent 是事件相机检测侧的重要背景：它不是 SNN 方法，但讨论了 event-only、event-frame fusion、GNN/SNN sparse detectors 与 dense feed-forward detectors 的局限。

## 3. Background and Motivation

Event cameras 可以异步记录亮度变化，适合高速和低延迟检测。但现有数据集的人工标注通常随较低帧率图像同步，导致 detector 多在固定频率上训练和评估。高频事件中包含的运动细节无法被充分利用。

论文认为 event-only detectors 缺少 RGB semantic cues，event-frame fusion 方法虽然可融合两种模态，但通常没有显式处理频率变化。FlexEvent 的动机是同时补充 RGB semantics 和 frequency-aware training。

## 4. Method Overview

整体方法包括两个核心模块：FlexFuse 和 FlexTune。输入是 event stream 与 RGB frames，任务输出为 object detection bounding boxes/classes。FlexFuse 是 adaptive event-frame fusion module，用 RGB frame 的语义信息补足高频 event data 的语义不足，同时保持事件的时间优势。FlexTune 是 frequency-adaptive fine-tuning mechanism，通过 frequency-adjusted labels 改善模型在不同 inference frequencies 下的泛化。

该方法不是 SNN，也没有 spiking neuron module。它属于 event-frame hybrid detection framework。

## 5. Technical Details

### Event Representation

论文围绕 DSEC 系列 detection datasets，使用 event streams 与 frame annotations。检测频率通过不同 temporal offsets / operational frequencies 构造，覆盖 20 Hz、36 Hz、45 Hz、60 Hz、90 Hz 和 180 Hz 等设置。

### Spiking Neuron / SNN Module

无。论文在 Related Work 中讨论 SNN detectors 作为 event detector 一类，但 FlexEvent 自身不是 SNN。

### Network Architecture

FlexFuse 负责 event-frame fusion，动态平衡 event modality 和 frame modality 的贡献。FlexTune 通过频率自适应微调，把高频下插值得到或调整后的 labels 纳入训练，使 detector 不只适配低频 frame annotations。

### Training Strategy

训练遵循 YOLO-X 风格，使用 standard detection loss，包括 IoU loss、classification loss 和 regression loss，并加入轻量 regularizer 平衡模态贡献。论文报告训练 100,000 iterations，batch size 8，sequence length 11，learning rate 1e-4，在两张 NVIDIA RTX A5000 GPU 上约一天完成。

### Loss Function

核心 loss 是 detection loss：IoU、classification、regression，再加 modality balancing regularizer。FlexTune 通过 frequency-adjusted labels 影响训练信号。

### Inference Process

推理时模型可在不同 operational frequencies 下运行，对 event-frame 输入进行融合后输出 detection results。论文重点测试从 20 Hz 到 180 Hz 的频率变化。

## 6. Experiments

Datasets 包括 DSEC-Det、DSEC-Detection 和 DSEC-MOD。指标采用 COCO-style mAP、AP50、AP75、APS、APM、APL，以及不同频率下的 inference time。

Table 1 在 DSEC-Det validation set 上比较 event-only 与 event-frame fusion methods。FlexEvent mAP 57.4、AP50 78.2、AP75 66.6，明显高于 RVT、SAST、SSM、LEOD、DAGr 等。Table 2 在 DSEC-Detection test set 上报告 Car/Pedestrian/Large-Vehicle，FlexEvent average mAP 47.4，高于 CAFR 38.0 和 RENet 29.4 等。Table 3 在 DSEC-MOD test set 上报告 F.mAP、V.mAP 和 Average，FlexEvent Average 36.9，高于 RENet 29.0。

Frequency generalization 是核心实验。Figure 6 和 Table 5 显示，在 20/36/45/60/90/180 Hz 下，完整 FlexEvent 的平均 mAP 为 57.2；无 Tune/无 Fuse 平均 43.7；只 Tune 为 48.0；只 Fuse 为 56.4。180 Hz 下完整模型 mAP 为 50.9，明显高于无 Fuse/无 Tune 的 22.9。

Table 4 报告 efficiency：FlexEvent 45.4M 参数，在 20 Hz/36 Hz/90 Hz/180 Hz 下 inference time 分别约 14.27/13.00/12.47/12.37 ms，慢于 RVT/SSM，但远快于 DAGr-50。

## 7. Main Contributions

- 明确提出 varying operational frequencies 下的 event camera object detection 问题。
- 提出 FlexFuse，将高频 event data 与 RGB semantic information 自适应融合。
- 提出 FlexTune，用 frequency-adjusted labels 提升跨频率泛化。
- 在 DSEC-Det、DSEC-Detection、DSEC-MOD 上展示检测精度和高频稳定性。

## 8. Limitations and Risks

论文没有把所有限制集中展开。V1 推断：FlexEvent 依赖 event-frame paired data 和 RGB frames，因此不适用于纯 event-only 或严格低功耗 event-only 场景；frequency-adjusted labels 涉及插值和标注假设，高速物体或遮挡下可能产生 label noise；模型参数 45.4M，效率并不一定优于轻量 event-only methods。

对综述风险：不能把 FlexEvent 作为 SNN 证据。它适合作为 event-based object detection、event-frame fusion 和频率泛化背景。

## 9. Relation to SNN for Event Cameras

分类：B: Event Camera side background。

理由是 FlexEvent 研究 event camera detection 的高频适应问题，但方法本身不是 spiking model。它可作为 SNN detector 的任务背景和非 SNN baseline。

## 10. Relation to Survey Taxonomy

可支持的章节包括：

- Event-based object detection
- Hybrid ANN-SNN models
- Event representations for SNNs
- Datasets and benchmarks
- Efficiency, latency, and energy
- Open challenges

## 11. Key Terms and Concepts

- Operational frequency：detector 运行/输出检测结果的频率。
- FlexFuse：adaptive event-frame fusion module。
- FlexTune：frequency-adaptive fine-tuning mechanism。
- DSEC-Det / DSEC-Detection / DSEC-MOD：event camera detection/fusion benchmarks。
- Frequency-adjusted labels：用于高频检测训练的调整或插值标注。
- Event-frame fusion：结合 event stream temporal detail 与 RGB semantic cues。

## 12. Questions for Human Deep Reading

1. FlexTune 的 frequency-adjusted labels 如何生成，插值假设是否可靠？
2. FlexFuse 的具体结构和 modality balancing regularizer 是什么？
3. FlexEvent 与 DAGr、SAST、RVT 的输入模态和标注使用是否完全公平？
4. 180 Hz 实验是否有真实高频标注，还是主要依赖插值？
5. Table 4 的 inference time 是否包含 event preprocessing 和 frame branch？
6. 在没有 RGB frame 的 event-only setting 下是否可退化运行？
7. 对夜间、motion blur、低光场景的收益来自 event 还是 RGB？
8. 是否有小目标或远距离目标的 AP 分析？

## 13. Evidence Notes

- Abstract：提出 varying frequencies、FlexFuse、FlexTune、20 Hz 到 180 Hz claim。
- Contributions 段：列出四条贡献。
- Table 1：DSEC-Det validation set 检测对比。
- Table 2：DSEC-Detection test set 类别 mAP。
- Table 3：DSEC-MOD event-frame fusion 对比。
- Table 4：不同 operational frequencies 下 inference time。
- Table 5 / Figure 6：FlexFuse/FlexTune ablation 和高频泛化结果。

## 14. Draft Survey-Usable Sentences

草稿句 1：FlexEvent highlights that event-camera object detection is not only a representation problem but also a frequency-generalization problem, because detectors trained at fixed annotation rates may fail to exploit high-frequency event streams.

草稿句 2：For SNN-event-camera surveys, FlexEvent can serve as a non-spiking detection baseline that emphasizes event-frame fusion and operational-frequency robustness.

草稿句 3：Its reliance on RGB frames and frequency-adjusted labels should be noted when comparing it with event-only SNN detectors.
