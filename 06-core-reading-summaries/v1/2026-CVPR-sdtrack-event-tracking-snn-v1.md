---
title: "SDTrack: A Baseline for Event-based Tracking via Spiking Neural Networks"
authors: ["Yimeng Shan", "Zhenbang Ren", "Haodi Wu", "Wenjie Wei", "Rui-Jie Zhu", "Shuai Wang", "Dehao Zhang", "Yichen Xiao", "Jieyuan Zhang", "Kexin Shi", "Jingzhinan Wang", "Jason K. Eshraghian", "Haicheng Qu", "Malu Zhang"]
year: 2026
venue: "CVPR"
level: "A"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/CVPR2026/A/2026-CVPR-A-sdtrack-a-baseline-for-event-based-tracking-via-spiking-neural-networks.md"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Shan_SDTrack_A_Baseline_for_Event-based_Tracking_via_Spiking_Neural_Networks_CVPR_2026_paper.html"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Shan_SDTrack_A_Baseline_for_Event-based_Tracking_via_Spiking_Neural_Networks_CVPR_2026_paper.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["SNN", "event camera", "event-based tracking", "SDTrack", "GTP", "I-LIF"]
---

# Summary V1｜SDTrack: A Baseline for Event-based Tracking via Spiking Neural Networks

## 1. One-sentence Summary

SDTrack 将 event stream 转为带 Global Trajectory Prompt (GTP) 的 three-channel frames，并用 Intrinsic Position Learning (IPL)、SNN Conv/Transformer backbone 和 center tracking head 构建无 data augmentation/post-processing 的 fully SNN event-based single-object tracker。

## 2. Research Problem

event cameras 适合 high dynamic range、microsecond response 的 tracking，但 sparse event frames 缺 texture，常用 ANN tracker 不能利用 spike sparsity；早期 SNN tracking 亦常为 ANN-SNN hybrid，或没有 template-search self-attention/cross-correlation。

作者认为两个缺口必须共同解决：已有 event aggregation 只保留 recent polarity 或弱 temporal surface，无法保留 global trajectory；SNN tracker 还需获得 template-search 的 position relation，而不应以额外 positional encoding 破坏 spike-driven architecture。

## 3. Background and Motivation

event `e={x,y,t,p}` 常被固定窗口聚合成 frames，使 vision backbone 可用，但 aggregation 决定运动信息损失。对于像素在一个 window 内多次反向运动，latest-polarity Event Frame 丢掉前面的轨迹；Time-Surface/Event Count 也难表达长期 path。

SNN 的 membrane states 可以保留 temporal context，发放 binary spikes 时可将部分 MAC 替换为 AC。作者的设计目标是以 GTP 保留 event motion，再以 SNN Transformer 让 template/search tokens 交互；论文用 I-LIF/LIF variants 表示不同 virtual-time/spike precision tradeoff。

## 4. Method Overview

template 与 search event streams 各经 GTP 转为 `3 x H x W` frame。GTP channels 1/2 分别累积 negative/positive event counts；channel 3 是从上一个 frame decay 并按新激活更新的 global trajectory cache。template/search frames 经 IPL 斜向拼成一张 unified matrix 后输入 SNN Conv Module。

卷积 features 在 IPL layout 中被 split/restore 并 tokenized，之后经 SNN Transformer Module 的 spike self-attention。template/search features cross-correlate 后进入 SNN center head，预测 target center、size 和 offset。output 为每 time interval 的 SOT bounding box。

## 5. Technical Details

### Event Representation: Global Trajectory Prompt

在 window `L` 内，`h1`、`h2` 分别将 negative 和 positive events 累积，scale `alpha` 既放大有效 signal 亦试图抑制 partial noise。第三 channel `h3_i` 以 `beta h3_(i-1)` 衰减 prior trajectory，只有某 pixel 在 current channels 新出现 event 时才增加 prompt。这样既保存当前 multi-direction polarity counts，也保留跨 windows 的 motion trace。

该 `3-channel` design 与 RGB-pretrained vision input format 相容，但不是 raw-event processing；`alpha=30`、`beta=0.8` 是 Tiny/FE108 ablation 得到的 chosen configuration，不可当作 general sensor constants。

### Spiking Neuron / SNN Module

论文给出 general membrane equation，IF/LIF/I-LIF 都可由参数取得。I-LIF 以 virtual time step `D` 对 membrane 作 clipped/rounded integer firing，并可在 inference 通过 spike-ahead principle 转成 `T x D` binary spike process。SDTrack 的 Tiny/Base results 比较了 LIF 和 I-LIF variants。

SNN Conv Block 是 pointwise-depthwise-pointwise separable spike convolution 加 convolution group residual；SNN Transformer Block 为 `U' = U + SSA(U)`、`U'' = U' + SNNMLP(U')`。SSA 由 spike-form `Q_s/K_s/V_s` 做 correlation；它不含 standard softmax 的细节需从 code核验。

### Intrinsic Position Learning and Head

IPL 将 template `Z` 与 search `X` 在 diagonal blocks 拼接，另外两个 blocks 是 zero matrices。这样 SNN Conv Module 在不增加 learnable positional vectors 的条件下学 joint position/semantic information。再 split/tokenize 后，cross-correlation features 输入 SNN center head；作者发现 center head 优于 SNN corner head。

### Training and Energy

loss 为 weighted focal classification loss + `2 * GIoU` + `5 * L1` box loss。inference 使用 first frame as template，没有 dynamic template、Hanning penalty 或 postprocessing。power 用 45nm `4.6 pJ/MAC`、`0.9 pJ/AC` 和 layer firing rate估算，attention FLOPs 单列；不是 physical energy measurement。

## 6. Experiments

### Datasets and Settings

benchmarks 为 FE108、FELT、VisEvent。template/search input sizes 是 `128 x 128` / `256 x 256`；Tiny channel base `C=32`、Base `C=64`。报告 AUC、PR、parameters、theoretical energy。作者也把 GTP 放入多个 mainstream trackers，测试 aggregation 的 generality。

### Main Results

Table 1：SDTrack-Tiny with I-LIF `T=1 x 4` 在 FE108 为 `59.0 AUC / 91.3 PR`，FELT 为 `39.3 / 51.2`，VisEvent 为 `35.6 / 49.2`，`19.61M` parameters、`8.16 mJ` estimated power。SDTrack-Base with I-LIF `1 x 4` 为 FE108 `59.9/91.5`、FELT `40.0/51.4`、VisEvent `37.4/51.5`，`107.26M`、`30.52 mJ`。

论文称 Tiny 的 low parameter/power 在 comparison table 中较突出，Base 在三个 data sets 的 AUC/PR 达到强结果。因为表中部分 competitors 的 scores 表明采用 GTP（作者为显示 tracker quality而注入 GTP），应避免把它当作纯 backbone-only fair comparison。

### Ablations

FE108 Tiny/I-LIF ablation：去 IPL 从 `59.00/91.30` 到 `58.10/89.66`；加入 learnable/sinusoidal positional encoding 反而为 `58.79/89.52`、`58.57/90.77`。center head 改 corner head 为 `58.81/90.17`；no pretrain 为 `47.80/74.50`。candidate backbone comparison 的 Tiny SDTrack 为 `59.0/91.3`，higher than cited Spike-driven Transformer V1/V2/V3 `52.4/85.3`、`55.9/85.8`、`58.9/90.3`。

## 7. Main Contributions

1. 提出 GTP：positive/negative accumulation + decayed global trajectory cache 的 3-channel event representation。
2. 提出 IPL，以 diagonal template-search concatenation 提取 intrinsic positional relation，而非显式 positional embedding。
3. 提出 SNN Conv + SNN Transformer + center head 的 transformer-based spike-driven event tracker。
4. 在 FE108、FELT、VisEvent 评估 fully SNN tracker，并报告 GTP 的跨-tracker generality和 operation-level power。

## 8. Limitations and Risks

GTP 是 fixed-window event-to-frame aggregation，会损失 within-bin exact timestamps 与 fully asynchronous execution。第三 channel 也依赖 hand-set `alpha/beta`，对 very long gaps、rapid reversals、sensor noise和不同 scene 的稳健性尚需系统检验。

论文的 “end-to-end” 指 tracker learning pipeline without postprocessing，而非从 sensor event 到 chip output 的全部 asynchronous system。power 是 theoretical estimate；pretraining 与 imported GTP comparisons 可能使 baseline fairness 和 energy accounting 复杂化。

## 9. Relation to SNN for Event Cameras

分类：A: SNN + Event Camera core paper。

SDTrack 把 event representation、spiking backbone、spike attention 与 real event-based SOT task 结合，适合作为 pure-event fully SNN tracking baseline。它也是分析“event rasterization后SNN是否仍保留event-native advantage”的重要对照。

## 10. Relation to Survey Taxonomy

- Event representations for SNNs：GTP three-channel event frame。
- SNN architectures for event cameras：I-LIF/LIF SNN Conv、SNN Transformer、IPL。
- Event-based tracking：template-search SOT、center head、cross-correlation。
- SNN training methods：spike-ahead I-LIF/time-step tradeoff。
- Efficiency, latency, and energy：firing-rate power analysis与 tiny/base scaling。
- Open challenges：rasterization、position priors、trajectory persistence、pretraining fairness。

## 11. Key Terms and Concepts

- SDTrack：Spike-Driven Tracking pipeline。
- GTP：Global Trajectory Prompt，three-channel event aggregation。
- IPL：Intrinsic Position Learning，diagonal template/search concatenation。
- I-LIF：Integer LIF，可用 `D` 表示 integer firing level/virtual time。
- spike-ahead principle：将 I-LIF integer firing 转为 binary spike inference 的方式。
- AUC/PR：success curve area 与 20-pixel center precision。
- center head：预测 target center、size、offset 的 tracking head。

## 12. Questions for Human Deep Reading

1. GTP 的 `alpha` 对 noise clipping的 exact behavior 和 event normalization是什么？
2. `h3` cache 是否跨整条 sequence 保留，template/search stream 是否共享/独立 cache？
3. I-LIF `D`、actual `T` 和 spike-ahead implementation 在 GPU/neuromorphic inference分别如何执行？
4. IPL zero blocks/intersection sizes如何影响 receptive field和 target-relative coordinates？
5. pretrained weights来自哪个 model/data，GTP RGB-style channels如何适配它们？
6. GTP generality Figure 4 的每个 tracker是否重新训练、使用相同 budget？
7. no dynamic template对 long sequences有何影响，FELT results反映了什么限制？
8. energy calculation是否包括 GTP、tokenization、float decision layer与memory traffic？

## 13. Evidence Notes

- Abstract 与 Section 1，第 1-2 页：SDTrack/GTP/IPL的目标、fully SNN claim和 Tiny/Base summary。
- Section 3.1-3.2 / Eq. (1)-(7)，第 3-4 页：general neuron、GTP channel construction。
- Section 3.3 / Eq. (8)-(19)，第 4-5 页：IPL、backbone, SSA、head和loss。
- Table 1 与 Section 4.3，第 6-7 页：FE108/FELT/VisEvent comparison与 energy model。
- Table 2-4 与 Section 4.4-5，第 7-9 页：GTP/IPL/head/backbone ablations、discussion。

## 14. Draft Survey-Usable Sentences

Draft material: SDTrack represents events with a three-channel Global Trajectory Prompt that combines polarity counts with a decayed trajectory cache before SNN processing.

Draft material: Its IPL design uses a joint template-search layout to induce positional learning without explicit positional embeddings in a spike-driven tracker.

Draft material: SDTrack provides a useful pure-event SNN tracking baseline, but its event windows and reported energy estimates should be distinguished from fully asynchronous hardware evidence.
