---
title: "EventGait: Towards Robust Gait Recognition with Event Streams"
authors: ["Senyan Xu", "Shuai Chen", "Chuanfu Shen", "Kean Liu", "Zhijing Sun", "Chengzhi Cao", "Xueyang Fu"]
year: 2026
venue: "CVPR"
level: "A"
priority: "P0"
advisor_track: "yes"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/CVPR2026/A/2026-CVPR-A-eventgait-towards-robust-gait-recognition-with-event-streams.md"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Xu_EventGait_Towards_Robust_Gait_Recognition_with_Event_Streams_CVPR_2026_paper.html"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_EventGait_Towards_Robust_Gait_Recognition_with_Event_Streams_CVPR_2026_paper.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["SNN", "event camera", "EventGait", "gait recognition", "LIF", "Mixture of Spiking Experts", "CroSA", "SUSTech1K-E", "CCGR-Mini-E"]
---

# Summary V1｜EventGait: Towards Robust Gait Recognition with Event Streams

## 1. One-sentence Summary

EventGait 是一个 SNN + event-camera dual-stream gait recognition framework：Dynamic Motion Stream 用 LIF-based Mixture of Spiking Experts 建模短时事件运动，Static Shape Stream 以 DINOv2 teacher 的 Cross-modal Structure Alignment 学习长时事件形状，并在新建 event gait benchmarks 上评估。

## 2. Research Problem

本文解决 event-based gait recognition 在复杂 illumination、快速运动和空间稀疏条件下的表示问题。RGB gait methods 在 low-light、motion blur 与背景干扰下不稳定；早期 event gait methods 又往往把长时间 event streams 累积为 event images，牺牲了 event camera 的 fine-grained temporal dynamics。

作者认为 gait simultaneously depends on stable body shape and high-frequency motion pattern。只用长窗口的 grid/event image 会压缩运动时间信息，而只处理短时 sparse events 又可能缺少 dense structural cue。本文因此将 temporal scale 分开，并把 spiking dynamics 用作短时运动建模的主方法成分。

## 3. Background and Motivation

event camera 在每像素 log brightness change 超过 threshold 时异步输出 `(x, y, t, p)`，具有小于 3 microseconds 的 temporal resolution 和超过 120dB 的 dynamic range。对 gait recognition，这使其在低照度下可以记录 motion-relevant changes，同时弱化 static texture、color 与部分背景干扰。

已有 EVGait/GaitBasee 等 event-based baselines 将 events 转成长期 aggregated event images，再用 CNN 或 GNN。作者认为这种 voxelization 既削弱 high-frequency dynamics，也会得到 spatially sparse representation，普通 deep network 难从中恢复 dense human structure。因此 EventGait 同时建立 short-term dynamic stream 和 long-term static stream。

## 4. Method Overview

原始 event stream 先 voxelize 为 `E in R^(2 x K x H x W)`，positive/negative polarity 分开编码。一个 long exposure window `T` 被分成 `K` 个 short temporal slices `Delta T = T/K`。Dynamic Motion Stream 输入 short-term slices `E_d`，通过 Mixture of Spiking Experts (MoSE) 提取 high-frequency dynamic feature `F_d`；Static Shape Stream 将 long-term slice `E_s` 输入 CNN encoder，并在训练时由 frozen DINOv2 teacher 的 Cross-modal Structure Alignment (CroSA) 提供 dense shape prior，得到 `F_s`。

两个 feature concat 后由 fusion module 形成 gait descriptor，再通过 downstream recognition module 分类。模型是 hybrid design：dynamic stream 是 SNN-based，static stream 是 CNN-based，CroSA 使用 RGB-derived grayscale image 仅在训练时提供 teacher supervision。

## 5. Technical Details

### Event Representation

事件 `e_i = (x_i, y_i, t_i, p_i)` 以 bilinear temporal kernel 累积到 `K` bins；`p` 的两个 polarity 形成 separate channels。论文在一个 `T` 内同时使用 two scales：short slice `E_d` 保持高时间精度供 motion stream 使用，long slice `E_s` 聚合更多 events 供 shape stream 提取稳定空间结构。

这种 two-scale design 不是逐 event asynchronous inference，而是将 events 组织为两种 voxelized tensors。其价值在于针对不同任务分工保留快运动和完整 body shape。

### Spiking Neuron / SNN Module

Dynamic Motion Stream 以 Leaky Integrate-and-Fire (LIF) neuron 为基本单元。LIF membrane potential 的 decay/integration 由 membrane time constant `tau` 控制：较小 `tau` 更适合 high-frequency spike trains，较大 `tau` 更有利于整合 sparse, low-frequency events。

MoSE 包含 `N` 个 time constants 不同的 spiking experts `E_i`。lightweight spiking gating network `G(.)` 根据 event dynamic pattern 生成 adaptive mixture weights `alpha_i`，输出 `E_hat_t = sum_i alpha_i E_i(E_t)`。默认选择 3 experts，以平衡 normal-light、low-light 与不同 motion regimes 的 performance/complexity。

论文没有在主文明确给出 surrogate gradient 的具体函数、time steps、neuron reset 或 full backpropagation implementation；这些是 V2 应核对 code/appendix 的关键点。

### Network Architecture

Static Shape Stream 使用 CNN-based student encoder 处理 long-term event slice。训练时，synchronized RGB frame 先转 grayscale，再输入 frozen DINOv2 teacher；student event feature 经 alignment convolution 投影到 teacher feature space。CroSA 以 feature alignment 迫使 sparse event input 学到更 dense 的 human structural prior。

最终 descriptor 为 `F_gait = Phi([F_s; F_d])`。Static Shape Stream 负责 dense structure，Dynamic Motion Stream 负责 multi-timescale motion，两者均不可完全替代。

### Training Strategy

论文在 8 RTX 3090 GPUs 上训练，使用 SGD，initial learning rate `0.1`，weight decay `0.0005`。输入经过 Pad-and-Resize 以保持 body proportion，并 resize 到 `64 x 64`。更多 schedule、batch size、augmentation 与 temporal-bin details 被放在 appendix，需 V2 核验。

### Loss Function

总目标为 `L_total = L_ce + L_tri + lambda_d L_align`。`L_ce` 是 identification cross-entropy，`L_tri` 拉近同一 identity / 拉远不同 identity，`L_align` 是 CroSA 中 student/teacher feature 的 L2 distance。Table 7 显示 `lambda_d = 0.2` 的 L2 alignment 在所报告设置下最佳；过大权重可能把 identity-irrelevant teacher cues 引入 event representation。

### Inference Process

推理时不需要 RGB teacher 或 CroSA teacher path；event stream 经 short/long slice 后由 two streams、fusion 和 classifier 产生 identity prediction。论文未在主文报告完整 event-sensor-to-output latency、energy 或 neuromorphic hardware measurement，因此不能将 SNN component 直接等同于实测低功耗。

## 6. Experiments

### Datasets and Tasks

作者用 synthesis pipeline 将 RGB gait videos 转成 events：先 frame interpolation，再用 v2e 模拟不同 illumination/noise settings，之后按 temporal windows 累积 events，并用 RGB human detector boxes 裁剪 event slices。由此构建两个 synthetic datasets：CCGR-Mini-E 含 970 subjects、47,884 sequences、53 covariates、33 views；SUSTech1K-E 含 1,050 identities、25,239 sequences，并提供 RGB/silhouette/skeleton/point-cloud/event modalities。

real-world evaluation 包括 DVS128-Gait（DVS128 采集、20 subjects、4,000 event streams）和 playback-based EV-CASIA-B（124 subjects、11 views）。任务指标包括 Rank-1、mAP 与 mINP。

### Main Results

Table 1 在 SUSTech1K-E 报告 EventGait overall Rank-1 为 92.8，参数量为 4.6M；在 night condition 为 84.8。作为 event baseline，EVGait overall 为 65.4，GaitBasee 为 63.1。论文还将其与 silhouette 和 LiDAR methods 比较，结论是 EventGait 在 many conditions 下接近或超过强 camera/LiDAR baselines，尤其在 low-light。

Table 2 报告 EventGait 在 CCGR-Mini-E 上取得 Rank-1 40.3、mAP 38.7、mINP 25.5；在 EV-CASIA-B 的 NM metric 为 96.7。Table 5 在 realistic DVS128-Gait 上报告 Rank-1 87.4，优于 EV-Gait 的 81.8 与 GaitBasee 的 74.4。

Table 3 的 cross-domain setting 中，CCGR-Mini to SUSTech1K 的 event-based EventGait 在 night condition 达到 51.4；CCGR-Mini to low-light SUSTech1K 的 overall 为 20.7。论文强调其在 night 的优势，但也承认部分 normal cross-domain settings 仍不如 strongest silhouette method。

Table 4 的 cross-illumination experiment 中，EventGait 在 normal-light overall 为 92.8、low-light overall 为 83.2，drop 为 9.6。该结果是本文关于 event modality illumination robustness 的主要实验证据。

### Ablations and Efficiency

Table 6 显示只用 Static Shape Stream 时 SUSTech1K-E overall 为 82.0，只用 Dynamic Motion Stream 为 72.4，同时使用两者为 92.8。Table 7 显示 L2 CroSA、`lambda_d = 0.2` 时达到 92.8 overall，而 no alignment 为 87.4。

Table 8 比较 MoSE experts 数目：1/2/3/4 experts 在 normal-light overall 分别为 88.4/89.8/92.8/92.7，在 low-light overall 为 72.5/78.6/83.2/83.4。作者因 3 与 4 的增益很小而采用 3 experts。

论文报告 4.6M parameters，但没有给出 FLOPs、spike rate、energy、latency 或 neuromorphic hardware measurement。它的 efficiency claim 应仅限于模型较小及 spiking dynamics 的设计动机。

## 7. Main Contributions

1. 提出 EventGait，将 event gait recognition 分解为 SNN-based dynamic motion stream 和 CNN-based static shape stream。
2. 提出 MoSE，以不同 LIF membrane time constants 的 spiking experts 和 adaptive spiking gating 应对 varied motion/illumination dynamics。
3. 提出 CroSA，以 frozen DINOv2 teacher 向 event static encoder transfer dense structure prior。
4. 构建 event synthesis pipeline，并发布 SUSTech1K-E 和 CCGR-Mini-E 两个 large-scale synthetic event gait benchmarks。
5. 在 synthetic、cross-domain、cross-illumination 与 real DVS128-Gait settings 上报告 event gait results。

## 8. Limitations and Risks

两项 largest benchmarks 是 synthetic events，而不是直接由 physical event camera 大规模采集；sim-to-real gap 是论文自己在 future work 中指出的限制。DVS128-Gait 的 real-world evaluation 只有 20 subjects，规模仍有限。

CroSA 在训练时依赖 synchronized RGB frame 和 frozen DINOv2 teacher。它并非只用 event data 训练，因此与纯 event-only/SNN method 的公平比较需要注明这个 extra supervision。

EventGait 是 hybrid SNN-CNN model，而非 fully spiking system；static stream、fusion 和 classifier 的 spiking implementation 未被声明。论文也没有完整 energy/latency/hardware evidence。

MoSE 的 gains 在 3 到 4 experts 间很小，且具体 surrogate-gradient training、spike sparsity 与 gating cost 在主文未充分展开。survey 中不应仅凭 LIF/MoSE 推断系统层面的能效。

## 9. Relation to SNN for Event Cameras

分类：A: SNN + Event Camera core paper；advisor-track support。

EventGait 的 dynamic stream 直接将 voxelized event slices 输入 LIF-based MoSE，并用 spiking gating 选择 time-constant experts，SNN 是主要方法模块而非仅作为 baseline。它同时展示一种 practical hybrid route：用 SNN 建模 event-native fast motion，用 CNN/VFM distillation 恢复 sparse event 的 static structure。

## 10. Relation to Survey Taxonomy

- Event representations for SNNs：two-scale voxelized event slices。
- SNN architectures for event cameras：LIF-based MoSE 和 spiking gating。
- Hybrid ANN-SNN models：SNN dynamic stream + CNN static stream + VFM distillation。
- Event-based action recognition：event-based gait identification。
- Datasets and benchmarks：SUSTech1K-E、CCGR-Mini-E、DVS128-Gait、EV-CASIA-B。
- SNN training methods：surrogate-gradient details需要进一步核验。
- Efficiency, latency, and energy：parameter count 有报告，但无 end-to-end hardware evidence。
- Open challenges：sim-to-real transfer、illumination robustness、teacher dependence。

## 11. Key Terms and Concepts

- EventGait：本文的 dual-stream event gait recognition framework。
- MoSE：Mixture of Spiking Experts，用多种 LIF time constants 的 experts 建模不同 temporal regimes。
- LIF neuron：Leaky Integrate-and-Fire neuron，以 membrane integration/decay 处理 temporal spike signal。
- spiking gating network：根据 event dynamic pattern 生成 expert mixture weights。
- CroSA：Cross-modal Structure Alignment，从 RGB-based VFM teacher 向 event encoder transfer structure prior。
- SUSTech1K-E：25,239 sequences、1,050 identities 的 synthetic event gait dataset。
- CCGR-Mini-E：47,884 sequences、970 subjects、53 covariates、33 views 的 synthetic event gait dataset。
- EV-CASIA-B：由 CASIA-B playback/re-recording 构建的 event gait dataset。

## 12. Questions for Human Deep Reading

1. MoSE 中 LIF neuron 的 exact update/reset equation、surrogate gradient 和 number of time steps 是什么？
2. spiking gating network 自身是否也由 LIF neurons 构成，参数和 computational overhead 如何？
3. short/long exposure windows 的 `T`、`K` 与 dataset-specific settings 分别是多少？
4. CroSA 训练是否要求每段 event 都有严格同步 RGB frame，real DVS128-Gait 如何处理？
5. DINOv2 teacher 的 model size、frozen layers 与 alignment convolution 的细节是什么？
6. synthetic SUSTech1K-E/CCGR-Mini-E 使用 v2e 的参数范围是否覆盖真实 sensor noise、threshold 与 HDR behavior？
7. Table 1 中各 modality 的 input、pretraining、detector/cropping protocol 是否真正可比？
8. 4.6M parameter count 是否包括 DINOv2 teacher，推理是否完全排除 teacher？
9. EventGait 在 DVS128-Gait 的 20-subject scale 上如何处理 cross-subject split？
10. 论文没有能耗测量，未来 survey 能否补充 spike rate、FLOPs 或 device-side runtime 证据？

## 13. Evidence Notes

- Abstract，第 1 页：说明 EventGait、MoSE、CroSA、SUSTech1K-E、CCGR-Mini-E 与 low-light claim。
- Section 1，第 2 页：列出 dual-stream、MoSE、CroSA、synthetic datasets 四项 contributions。
- Section 3.1，第 3 页 / Eq. (2)：event voxel representation 与 two-scale temporal design。
- Section 3.2，第 3-4 页 / Eq. (3)-(5)：LIF motivation、MoSE experts 与 spiking gating mixture。
- Section 3.3-3.4，第 5 页 / Eq. (6)-(9)：DINOv2-based CroSA、fusion 和 total loss。
- Section 4，第 5-6 页：event synthesis pipeline、CCGR-Mini-E、SUSTech1K-E 与 real datasets。
- Table 1-2，第 6 页：within-domain SUSTech1K-E、CCGR-Mini-E、EV-CASIA-B results。
- Table 3-5，第 7 页：cross-domain、cross-illumination 与 DVS128-Gait results。
- Table 6-8，第 8 页：two streams、CroSA weight、MoSE expert-number ablations。

## 14. Draft Survey-Usable Sentences

Draft material: EventGait is a hybrid event-camera architecture in which a LIF-based Mixture of Spiking Experts models high-frequency motion while a CNN static stream receives cross-modal structural supervision during training.

Draft material: Its two-scale event representation separates short-term dynamic evidence from long-term shape evidence, providing a concrete design pattern for SNN-event models that must balance temporal fidelity and spatial density.

Draft material: EventGait reports strong low-light gait-recognition results and introduces large synthetic event benchmarks, but its teacher dependence and synthetic-to-real gap should be made explicit in any survey comparison.
