---
title: "SpikeTrack: High-performance and Energy-efficient Event-Based Object Tracking with Spiking Neural Network"
authors: ["Yang Wang", "Jiqing Zhang", "Chuanyu Sun", "Qianhui Liu", "Huilin Ge", "Ziqi Wei", "Xin Yang"]
year: 2026
venue: "CVPR"
level: "A"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/CVPR2026/A/2026-CVPR-A-spiketrack-high-performance-and-energy-efficient-event-based-object-tracking-with-spiking-.md"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Wang_SpikeTrack_High-performance_and_Energy-efficient_Event-Based_Object_Tracking_with_Spiking_Neural_CVPR_2026_paper.html"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_SpikeTrack_High-performance_and_Energy-efficient_Event-Based_Object_Tracking_with_Spiking_Neural_CVPR_2026_paper.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["SNN", "event camera", "event-based tracking", "SpikeTrack", "DI-LIF", "MSST"]
---

# Summary V1｜SpikeTrack: High-performance and Energy-efficient Event-Based Object Tracking with Spiking Neural Network

## 1. One-sentence Summary

SpikeTrack 是一个 pure spike-driven event-based single-object tracker：以 Multi-Search-sequence-and-Single-Template (MSST) 将多个 event search frames 作为 temporally ordered spike trains，并以 Dynamic Integer LIF (DI-LIF) 在训练时自适应 integer activation、推理时进行 spike-driven firing。

## 2. Research Problem

event-camera SOT 在 fast motion、occlusion 和 target appearance change 下需要连续的 temporal cue，但许多 RGB tracker 单帧 template-search formulation 缺少 event temporal structure。既有 SNN tracking 要么使用 fixed-threshold binary/LIF representation，造成 quantization error/under-capacity，要么将 temporal modeling 交给额外 ANN/temporal modules。

本文将 tracking 的 multi-frame relation 与 SNN membrane accumulation 对齐：同一 template 配多个 search frames 应被视为 spike sequence；而 event density 随运动变化，fixed maximum firing level 可能在 dense input saturation 或 sparse input redundancy之间失衡。

## 3. Background and Motivation

event camera 以 threshold-crossing events 记录 brightness change，拥有 microsecond temporal resolution与wide dynamic range。将 events voxelize 后，positive/negative polarity 的 frames 可送入 regular vision layers，但时序分箱会产生不同 event density；tracker需要从连续 target state change中抽取 temporal coherence。

LIF 将 membrane potential quantize为 binary spike，I-LIF以固定 integer maximum `D` 增大表示能力。作者认为固定 `D` 不适合 dense/sparse event conditions，因此提出对每个 input sample动适应 firing capacity的 DI-LIF。

## 4. Method Overview

给定一段 event stream，SpikeTrack 在 `n` bins 建 voxel grid；每一 bin 内的 events 累积为一个有 positive/negative channels 的 event frame。MSST 在 training 时输入 one template 和 multiple temporally ordered search frames，模板/搜索 frames 经 I-LIF SNN Conv Module，membrane potential跨 time intervals 更新。

features 送进由多个 DI-LIF SNN Transformer blocks 组成的 interaction module。template/search cross-correlation features 经 I-LIF SNN center tracking head，输出 classification score、bounding-box size和offset。inference是 end-to-end、无 data augmentation/post-processing的模型（作者声明）。

## 5. Technical Details

### Event Representation and MSST

event frame是每个 voxel bin的 polarity accumulation。MSST 不把多个 search frames 在 channel维早期堆叠，而是在 SNN temporal dimension sequentially feed；single template与多个 search sequence共享。论文实验令 search sequence length最多为 10，意图让 membrane potential及spike trains编码trajectory/appearance evolution。

### I-LIF and DI-LIF

I-LIF 在训练中以 integer-valued firing level近似 membrane potential，`D` 控制 maximum emitted integer；推理转换到 spikes。DI-LIF先对 input feature的 global statistic `mu(X)` 做 learnable linear transform和sigmoid，取得 adjustment factor `alpha`，进而adaptive设置每 sample 的 integer firing capacity。dense input会提高 capacity以保留 cues；sparse input降低capacity以抑制冗余。

作者将 DI-LIF 主要放入 Transformer，因为 template-search interaction具有较高 entropy/global information；SNN Conv module与tracking head使用 I-LIF。这个“adaptive quantization”是sample-dependent firing range，不是权重量化。

### Network Architecture

SNN Conv Block 包含 pointwise/depthwise separable convolution、BatchNorm、I-LIF和residual refinement。DI-LIF SNN Transformer Block为 spike self-attention加SNN MLP，论文使用 eight blocks。tracking head由classification、size and offset prediction组成，以center-based localization输出 box。

### Training and Loss

训练用 weighted focal loss做classification、GIoU与L1做box regression：`L = L_cls + 2 L_iou + 5 L_L1`。模型训练60 epochs，每epoch 20K samples；search/template size为 `256 x 256`/`128 x 128`，default `D_init=6`。MSST 10 search frames提高training memory/time（论文报告 `5.8 -> 18.8 GB`, `2.5 -> 8 h`），是性能换取训练成本。

### Energy

paper将SNN energy归于sparse firing并报告theoretical power；具体processor、memory access和event voxelization cost不在model-level power中完整体现，不能直接等价为device energy。

## 6. Experiments

### Datasets and Metrics

在 FE108、FELT、VisEvent 三个 event-based tracking benchmarks评估。table使用 success rate (SR)、precision rate (PR)、parameters和theoretical power；和ANN、SNNTrack、HDETrack等作比较。作者还测DI-LIF、Transformer depth、MSST length和`D_init`。

### Main Results

Table 1：SpikeTrack有 `25.26M` parameters、estimated `7.92 mJ`，在 FE108为 `60.3 SR / 92.7 PR`，FELT为 `41.0 / 52.3`，VisEvent为 `38.9 / 54.3`。论文称其在三个dataset达到table内strong results；例如VisEvent相对runner-up提升 `1.6 SR` 和 `1.8 PR`，但应以论文的comparison set和energy model为限。

### Ablations

VisEvent Table 2：Ours为 `38.9/54.3`；DI-LIF换I-LIF为 `38.1/53.0`、换learnable fixed-D的 LI-LIF为 `38.4/52.8`。8 Transformer blocks改为4/12时为 `37.4/52.0`、`38.0/52.2`；center head换corner/linear head为 `37.0/51.9`、`35.3/49.1`。

Table 3显示MSST search length从1到10时VisEvent SR/PR由 `34.6/48.1` 上升到 `38.9/54.3`，length 12又降至 `37.1/51.8`。Table 4中不同 `D_init` 下SR变化约0.9、PR约1.5 points，作者以此说明DI-LIF对初始range不敏感。Table 5的long sequence comparison称在2000 frames时相对HDETrack高 `1.5 SR`、`1.9 PR`。

## 7. Main Contributions

1. 提出 pure spike-SNN event tracker，将多search temporal context显式组织为MSST spike sequence。
2. 提出DI-LIF，以input-adaptive integer firing range减少fixed-I-LIF quantization的限制。
3. 以I-LIF conv/head与DI-LIF Transformer构造template-search interaction和center tracking。
4. 在三个event tracking benchmarks上报告accuracy、sequence-length、neuron/depth和power trade-offs。

## 8. Limitations and Risks

尽管推理是spike-driven，输入仍先以voxel grid/event frames离散化；它不是逐event asynchronous tracker。MSST主要在training使用multiple search frames，实际online inference如何维护membrane state、template refresh和frame scheduling需要从code核验。

DI-LIF增加per-sample statistic/threshold control，其floating-point/control overhead和hardwaremapping未完全报告。theoretical power也没有包括event voxelization、memory traffic或latency；10-frame训练成本显著，且long-sequence分析只有有限benchmarks。

## 9. Relation to SNN for Event Cameras

分类：A: SNN + Event Camera core paper。

SpikeTrack直接以event representation、I-LIF/DI-LIF、spike attention和event SOT组成核心方法。它特别支持survey中“temporal credit/memory design”与“adaptive spiking neuron for event density variation”两条讨论线。

## 10. Relation to Survey Taxonomy

- Event representations for SNNs：n-bin voxel grid和two-polarity event frames。
- SNN architectures for event cameras：I-LIF conv/head、DI-LIF Transformer。
- Event-based tracking：MSST、template-search cross-correlation和center head。
- SNN training methods：integer firing training、spike inference、multi-frame temporal supervision。
- Efficiency, latency, and energy：adaptive firing capacity、theoretical power与MSST cost。
- Open challenges：voxelization、online state/sequence management、hardware adaptive thresholds。

## 11. Key Terms and Concepts

- SpikeTrack：本文的pure spike-driven event SOT framework。
- MSST：Multi-Search-sequence-and-Single-Template training paradigm。
- I-LIF：Integer Leaky Integrate-and-Fire neuron，固定max integer firing level。
- DI-LIF：Dynamic Integer LIF，按input feature调整firing capacity。
- `D_init`：DI-LIF的initial maximum integer parameter。
- SR/PR：tracking success rate和precision rate。
- GIoU：Generalized Intersection over Union regression loss。

## 12. Questions for Human Deep Reading

1. `n` bins、event window和MSST sequence time axis在不同datasets的exact setting是什么？
2. DI-LIF 的`alpha`如何map到integer `D`，rounding/clipping与surrogate gradient是什么？
3. DI-LIF inference是否完全由integer/spike operations实现，threshold adaptation有无floating point control？
4. template在10 search frames之间是否reusedwith membrane state，online inference和training是否一致？
5. “no data augmentation”是否也包括event-specific spatial/temporal augmentation？
6. 7.92mJ power的operation constants、firing-rate和first/last layer accounting为何？
7. MSST performance gain是否可由更多training samples/compute而不是temporal model本身解释？
8. Table 5 的long sequenceprotocol、target update策略和HDETrack comparison是否完全对齐？

## 13. Evidence Notes

- Abstract与Section 1，第1-2页：MSST、DI-LIF、pure spike-SNN和任务动机。
- Section 3.1 / Eq. (1)-(4)，第3页：event voxel/event-frame representation与MSST。
- Section 3.2-3.3 / Eq. (5)-(12)，第4-5页：I-LIF conv、DI-LIF mechanism和Transformer。
- Section 3.4 / Eq. (16)，第5-6页：center head和focal/GIoU/L1 loss。
- Section 4 / Tables 1-5，第6-8页：benchmarks、main results、ablation和long-term tracking。

## 14. Draft Survey-Usable Sentences

Draft material: SpikeTrack aligns an event-tracking training protocol with SNN temporal dynamics by feeding a sequence of search frames against one template rather than treating each search frame independently.

Draft material: Its DI-LIF neuron adaptively selects an integer firing range from the input features, aiming to preserve dense-event cues while limiting sparse-event redundancy.

Draft material: The tracker reports strong benchmark results with low estimated power, but its voxelized input and unmeasured hardware costs should remain explicit in survey comparisons.
