---
title: "Action Recognition and Benchmark Using Event Cameras"
authors: ["Yue Gao", "Jiaxuan Lu", "Siqi Li", "Nan Ma", "Shaoyi Du", "Yipeng Li", "Qionghai Dai"]
year: 2023
venue: "TPAMI"
level: "B"
priority: "SECNet reference-only"
advisor_track: "yes"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "SECNet references / 00-index/reading-plan-core.md"
official_page: "https://doi.org/10.1109/TPAMI.2023.3300741"
pdf_link: "https://doi.org/10.1109/TPAMI.2023.3300741"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["event camera", "action recognition", "EV-ACT", "THU E-ACT-50", "THU E-ACT-50-CHL", "LMFR", "SlowFast", "benchmark", "SECNet reference"]
---

# Summary V1｜Action Recognition and Benchmark Using Event Cameras

## 1. One-sentence Summary

本文提出 event-based action recognition framework EV-ACT，并发布 THU E-ACT-50 与 THU E-ACT-50-CHL benchmark，用 Learnable Multi-Fused Representation、Event Voxel Filtering、Event-based Slow-Fast Network 和 Event-based Spatial Temporal Attention 提升 event-camera action recognition。

## 2. Research Problem

本文解决 event-based action recognition 的两个核心问题：一是缺少大规模、真实、event-specific 的 action recognition benchmark；二是缺少适合 event streams 的有效 action recognition framework。

这个问题对 event cameras 很重要，因为 event cameras 只记录 brightness changes，具有低功耗、高时间分辨率、低运动模糊和一定隐私优势，但其输出是 sparse asynchronous event stream，不能直接套用 RGB video action recognition pipeline。对 SNN for event cameras survey 来说，本文是 action recognition benchmark 和 non-spiking CNN baseline 的重要背景。

前人工作的限制包括：PAF、DHP19、N-HAR、DailyAction 等 event-based action datasets 在样本数、类别数或真实应用动作覆盖上不足；已有 event representations 多是 hand-crafted features，尚无统一结论哪种表示最适合 action recognition；SNN-based event action recognition 方法可处理 spike trains，但训练困难且通常依赖特殊硬件。

## 3. Background and Motivation

event camera 在像素亮度变化超过阈值时触发事件，每个 event 记录为 `(x, y, t, p)`，其中 `p` 表示 positive/negative polarity。由于 event camera 不记录颜色和纹理，它在 bathroom fall detection、healthcare monitoring 等场景中可能比 RGB camera 更保护隐私。

action recognition 需要同时识别 appearance-like spatial semantics 和 fast motion dynamics。传统 RGB video 方法有 3D CNN、TSM、SlowFast 等，但 event stream 稀疏、不规则、噪声较多，必须先构建合适的 event representation。本文动机是把 event data 转成 CNN-friendly frame-like representation，同时保留多种 event information，并通过 slow-fast temporal granularity 捕获动作。

## 4. Method Overview

EV-ACT 由四个模块组成：Event Voxel Filtering (EVF)、Learnable Multi-Fused Representation (LMFR)、Event-based Slow-Fast Network (ESFN) 和 Event-based Spatial Temporal Attention (ESTA)。

输入是 raw event stream。EVF 将 events 视为 spatiotemporal point cloud，对 `X-Y-T` 空间做 voxel filtering 和 variance-based post-processing，以降采样和去噪。LMFR 将 Event Frame、Event Count、Surface of Active Events 等 basic event representations 统一到 `T x H x W` 形式，并用 learnable convolution kernels 转换后拼接为 CNN input。ESFN 采用 slow/fast dual pathways：slow pathway 使用较大时间窗积累 semantic boundary information，fast pathway 使用较小时间窗捕获快速动作细节。ESTA 对 slow/fast features 施加 spatial-temporal attention，最后输出 action class score。

本文不是 SNN，也不是 ANN/SNN hybrid；它是 CNN-based event-camera action recognition framework，使用 ResNet backbone。

## 5. Technical Details

### Event Representation

论文首先定义 event camera 的触发机制：当某像素当前 log brightness 与上次触发时的 log brightness 差异超过 polarity-adjusted threshold，就产生一个 event。event stream 表示为 `E = {(x_k, y_k, t_k, p_k)}_{k=1}^N`。

LMFR 将多个基础 event representations 融合起来。Event Frame 记录 polarity accumulation，Event Count 记录各 polarity 的 event count，Surface of Active Events 记录 timestamp，Event Voxel 和 Event Spike Tensor 则进一步保留时间分辨率。论文将这些表示抽象为一个统一公式：representation 由 pure representation term 和 kernel transformation term 组成。LMFR 对每个 basic representation 使用 learnable convolution kernel，再经过 normalization 后沿 channel dimension concat，得到 `C x T x H x W` representation。

### Spiking Neuron / SNN Module

本文没有 spiking neuron 或 SNN module。HMAX SNN 和 Motion SNN 作为 baselines 出现。论文在 related work 中指出 SNN 适合处理 spike trains，但需要特殊硬件且比 CNN 更难训练。

### Network Architecture

EVF 将 events 按 polarity 分开处理，把事件看作 `(x, y, t)` point with polarity attribute。`X-Y-T` 空间被划分为 voxels，每个 voxel 内 events 用平均坐标代表；timestamp 会先 normalization 并 rescale。之后，variance-based post-processing 会删除 event count 低于阈值的 noisy voxels。

ESFN 借鉴 SlowFast video architecture。slow pathway 输入较少 time bins，用于积累更稳定的 appearance / boundary semantics；fast pathway 输入更多 time bins，用于捕获快速运动。论文默认设置 `T_slow = 4`、`T_fast = 16`，并使用 ResNet 34 as backbone。

ESTA 使用 learnable attention weight matrices 分别作用于 slow/fast pathway features，再 concat 后通过 fully connected layer 输出 action score。attention 的动机是 event data 中 motion regions 和 active time bins 更稀疏，空间/时间注意力更容易聚焦到动作区域。

### Training Strategy

实验使用 ResNet 34 pre-trained on ImageNet 作为 backbone。网络训练 80 epochs，optimizer 为 Adam，learning rate 为 `1e-4`，weight decay 为 `1e-4`，使用 exponential learning rate decay，gamma 为 0.5。实验基于 PyTorch，在 Tesla V100 GPU 上训练。

### Loss Function

最终 action prediction 使用 cross-entropy loss。论文创新集中在 event filtering、learnable multi-representation fusion、slow-fast temporal modeling 和 spatial-temporal attention，而不是新 loss。

### Inference Process

推理时 raw event stream 先经 EVF 降采样/去噪，再转成 LMFR representation，同时构造 slow/fast temporal granularities。ESFN 提取 dual-pathway features，ESTA 对动作相关的 spatial-temporal regions 加权，最后输出类别预测。

## 6. Experiments

### Datasets

论文评估 PAF、DHP19、DailyAction、THU E-ACT-50 和 THU E-ACT-50-CHL。THU E-ACT-50 是本文新建标准 benchmark，使用 CeleX-V event cameras，分辨率 `1280 x 800`，包含 105 subjects、50 action categories、10,500 recordings、两个 frontal views。THU E-ACT-50-CHL 是 challenging dataset，使用 DAVIS346，分辨率 `346 x 260`，包含 18 students、2,330 recordings，在 corridor/open hall 等复杂光照和视角条件下采集。

### Evaluation Protocols

PAF 和 DailyAction 使用 8:2 train/test split；DHP19 使用原论文 split，并按 camera view 分别训练测试；THU E-ACT-50 和 THU E-ACT-50-CHL 按 subject 8:2 划分，保证 train/test identity disjoint。DHP19、THU E-ACT-50、THU E-ACT-50-CHL 报告 Top-1/Top-3/Top-5；PAF 报告 Top-1/Top-2/Top-3；DailyAction 主要报告 Top-1。

### Main Results

Table IV 显示 EV-ACT 在四个 benchmarks 上超过 HMAX SNN 和 Motion SNN。Top-1 accuracy 分别为：PAF 92.6、DailyAction 97.9、THU E-ACT-50-CHL 58.5、THU E-ACT-50 92.7。相对前人方法，论文正文报告在 PAF、DailyAction、THU E-ACT-50-CHL、THU E-ACT-50 上分别提升 14.5%、7.6%、11.2%、7.4%。

### Ablation Studies

Table V 通过逐步加入 LMF、EVF、ESFN、ESTA 证明各模块有效。完整模型在 PAF 上达到 Top-1/Top-2/Top-3 = 92.6/98.2/100；在 DHP19-C4 上达到 91.5/98.8/99.4；在 THU E-ACT-50-CHL 上达到 58.5/78.6/86.0；在 THU E-ACT-50 上达到 92.7/98.4/99.2。

移除 EVF 会导致 PAF、DHP19、THU E-ACT-50-CHL、THU E-ACT-50 的 Top-1 分别下降 1.1%、1.7%、1.0%、0.4%。移除 ESTA 会导致 Top-1 分别下降 3.7%、1.8%、2.6%、1.5%。LMF 相比 baseline 在四个数据集上分别提升 2.2%、1.9%、2.5%、3.5% Top-1。

Table VIII 在 THU E-ACT-50-CHL 比较 input sources：pure RGB sequence 为 30.8%，frame differentiation 为 44.4%，optical flow 为 46.8%，LMFR event representation 为 58.5%。这支持作者关于 event data 在 challenging illumination 中更有优势的论点。

### Efficiency / Embedded Results

论文在 Nvidia Jetson AGX Xavier 上部署 EV-ACT。Table XIII 报告 ResNet 18 版本为 11.2M parameters、14.5 GFlops、5.4W、72.8ms/sample；ResNet 34 版本为 21.3M parameters、29.0 GFlops、7.2W、76.9ms/sample。系统平均达到 326,140 EPS 和 1.3GB memory usage。论文还比较 event cameras 与 frame-based cameras 的 sensor latency/power，指出 event cameras 通常为 microsecond-level latency 和 milliwatt-level power。

## 7. Main Contributions

1. 提出 EV-ACT，一个 CNN-based event-camera action recognition framework，包含 EVF、LMFR、ESFN 和 ESTA。
2. 提出 LMFR，用 learnable convolutional transformations 融合多种 event representations，而不是依赖单一 hand-crafted representation。
3. 构建并发布 THU E-ACT-50 和 THU E-ACT-50-CHL，大幅扩展 event-based action recognition 的类别数、样本数和场景难度。
4. 在 PAF、DailyAction、THU E-ACT-50-CHL 和 THU E-ACT-50 上与 HMAX SNN、Motion SNN 对比，展示 event-CNN framework 的性能优势。
5. 在 Jetson AGX Xavier 上实现 embedded event-based action recognition system，并报告功耗、推理时间和 EPS。

## 8. Limitations and Risks

本文不是 SNN 方法。虽然将 HMAX SNN 和 Motion SNN 作为 baselines，但 survey 中不能把 EV-ACT 归类为 SNN architecture。

模型使用 ImageNet pre-trained ResNet 34 backbone，这意味着性能提升不完全来自 event representation，也部分来自成熟 CNN backbone 和 pretraining；与纯 SNN 或从零训练模型比较时需要谨慎。

THU E-ACT-50/CHL 的数据集价值很高，但 V2 阶段需要人工核验 dataset link、license、下载可用性和后续论文采用情况。

跨视角实验显示仍存在明显 performance degradation；论文虽然比 SNN baselines 下降更小，但 cross-view generalization 仍是挑战。

效率结论同时包含 sensor capture 和 computation 两部分，且计算部分基于 Jetson AGX Xavier 与 ResNet backbone；不能直接外推到 neuromorphic hardware 或 SNN energy。

## 9. Relation to SNN for Event Cameras

分类：B: Event Camera side background；advisor-track support。

本文是 event-camera action recognition benchmark 和 CNN-based baseline，不是 SNN paper。它对 SNN for Event Cameras survey 的价值在于：提供 THU E-ACT-50/CHL benchmark context；提供与 HMAX SNN、Motion SNN 的对比；展示 non-spiking CNN 方法如何通过 event representation 和 temporal modeling 达到较强性能。对于 SECNet/SpikePoint/TTPOINT 等 action-recognition 方向论文，它是重要数据集和实验背景。

## 10. Relation to Survey Taxonomy

- Event representations for SNNs：LMFR、Event Frame、Event Count、SAE、Event Voxel、EST。
- Event-based action recognition：核心 benchmark 和 baseline。
- Hybrid ANN-SNN models：作为 non-spiking CNN baseline 对照。
- Datasets and benchmarks：THU E-ACT-50、THU E-ACT-50-CHL。
- Efficiency, latency, and energy：event camera power、Jetson deployment、EPS。
- Open challenges：cross-view generalization、challenging illumination、fair comparison between CNN and SNN。

## 11. Key Terms and Concepts

- EV-ACT：本文提出的 event-based action recognition framework。
- THU E-ACT-50：50 类、10,500 recordings、1280 x 800 resolution 的 event action dataset。
- THU E-ACT-50-CHL：challenging version，包含复杂光照、不同视角和较小动作幅度。
- EVF：Event Voxel Filtering，用 voxel filtering 和 post-processing 降采样/去噪。
- LMFR：Learnable Multi-Fused Representation，用 learnable kernels 融合多种 event representations。
- ESFN：Event-based Slow-Fast Network，用 dual temporal granularity 捕获 slow semantics 和 fast motion。
- ESTA：Event-based Spatial Temporal Attention，给 motion-relevant spatial/temporal features 更高权重。
- EPS：Event Per Second，论文用于衡量 embedded system 每秒处理 event points 的指标。

## 12. Questions for Human Deep Reading

1. THU E-ACT-50 和 THU E-ACT-50-CHL 的数据下载链接现在是否仍可访问？
2. EV-ACT 的 ImageNet pretraining 是否让它与 SNN baselines 的比较不完全公平？
3. Table IV 中 HMAX SNN 和 Motion SNN 在 THU E-ACT-50/CHL 上的 replication details 是否充分？
4. LMFR 中 basic representations 的选择是否固定为 Event Count、Event Frame、Time Surface，还是可扩展到 EST/Event Voxel？
5. EVF 的 variance-based post-processing 阈值是否对不同 event cameras 和 scenes 敏感？
6. ESFN 的 `T_slow` 和 `T_fast` 在其他 datasets 上是否需要重新调参？
7. THU E-ACT-50 的 cross-view split 是否适合作为未来 SNN methods 的标准评估协议？
8. Jetson energy results 是否包含 event camera sensor power、preprocessing 和 data transfer？
9. 对 SECNet/TTPOINT/SpikePoint 来说，引用本文时应优先强调 dataset、representation，还是 CNN/SNN baseline gap？

## 13. Evidence Notes

- Abstract，第 1 页：提出 EV-ACT、LMFR、THU E-ACT-50/CHL，并报告四个 benchmark 上相对前人提升。
- Section I，第 2 页：列出三项主要 contributions。
- Section II-B，第 3 页：讨论 SNN、Event Frame、Event Count、SAE、Event Voxel、EST 等 event representation background。
- Section III / Fig. 2，第 4 页：展示 EV-ACT pipeline：EVF、LMFR、ESFN、ESTA。
- Section IV，第 6-8 页：介绍 THU E-ACT-50 和 THU E-ACT-50-CHL 的类别、样本、分辨率和采集条件。
- Section V-A/B，第 8 页：说明 evaluation protocols 和 implementation details。
- Table IV，第 9 页：报告 EV-ACT 与 HMAX SNN、Motion SNN 的 Top-1 comparison。
- Table V，第 9 页：报告 incremental modules ablation。
- Table VIII，第 11 页：比较 RGB、frame differentiation、optical flow 和 LMFR input sources。
- Section V-E / Table XI，第 13-14 页：cross-view evaluation。
- Section V-F / Table XIII，第 14-15 页：embedded system 和 energy/inference results。

## 14. Draft Survey-Usable Sentences

Draft material: EV-ACT is a non-spiking CNN-based event-camera action recognition baseline that combines learnable multi-representation fusion with slow-fast temporal modeling and spatial-temporal attention.

Draft material: The THU E-ACT-50 and THU E-ACT-50-CHL datasets substantially expanded event-based action recognition benchmarks and are useful references when evaluating SNN methods on realistic action categories.

Draft material: Although EV-ACT reports stronger accuracy than HMAX SNN and Motion SNN on several action benchmarks, the comparison should be interpreted cautiously because EV-ACT uses a CNN backbone and ImageNet pretraining rather than spiking computation.

Draft material: The paper's embedded evaluation is useful for discussing practical event-camera systems, but its energy conclusions should not be directly generalized to neuromorphic SNN hardware.
