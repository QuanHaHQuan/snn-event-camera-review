---
title: "Fully Spiking Neural Networks for Unified Frame-Event Object Tracking"
authors: ["Jingjun Yang", "Liangwei Fan", "Jinpu Zhang", "Xiangkai Lian", "Hui Shen", "Dewen Hu"]
year: 2025
venue: "NeurIPS"
level: "A"
priority: "P0"
advisor_track: "no"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/NeurIPS2025/A/2025-NEURIPS-A-fully-spiking-neural-networks-for-unified-frame-event-object-tracking.md"
official_page: "https://papers.nips.cc/paper_files/paper/2025/hash/af752cfbdcc6fd3e4cd0eea9f1ad0fab-Abstract-Conference.html"
pdf_link: "https://arxiv.org/pdf/2505.20834"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["SNN", "event camera", "frame-event tracking", "SpikeFET", "Transformer"]
---

# Summary V1｜Fully Spiking Neural Networks for Unified Frame-Event Object Tracking

## 1. One-sentence Summary

SpikeFET 是一个 fully spiking frame-event single-object tracker，以 dual-single-dual ConvFormer/Transformer backbone 融合 image frames 和 time-integrated event frames，并用 Randomized Patchwork Module (RPM) 与 Spatial-Temporal Regularization (STR) 改善位置鲁棒性和跨模板匹配。

## 2. Research Problem

frame-event fusion 可把 image texture 与 event 的 low-light/high-speed motion 互补，但现有 tracker 多为 ANN 或 ANN-SNN hybrid，计算高且未充分利用 event sparsity。纯 event SNN tracker 又缺少 frame appearance cue，或在 feature alignment、translation invariance 与 template similarity 上不稳定。

作者的目标是以一个 end-to-end fully spiking network 做 unified frame-event tracking，同时结合 convolution local feature extraction 和 Transformer global correlation。关键技术问题是：padding 会让 convolution tracker 学得 position bias，RPM 随机重排 template/search patches 后会产生 asymmetric temporal boundary features。

## 3. Background and Motivation

event camera 输出 `(x,y,t,p)`，适合低照度、过曝和高速运动，但输入稀疏、难像 RGB 那样提供稳定 texture。SNN 的 spike-driven operation 与 event data 在表示上相容，理论上可降低 AC/MAC cost；但“fully spiking”不必然等于实际 device energy low。

传统 SOT 常用 template 与 search 的 relation modeling；本文采用 two templates（initial 与 online temporal template）和 search。作者认为 binary spike feature 要在 modality-specific representation 和 cross-modal global fusion 中都保持 spiking，才可避免 hybrid fusion 的 energy compromise。

## 4. Method Overview

frame input与 continuous event stream 分别生成 template/search patches。event stream 不采用 voxel/GTP，而是在 temporal window 内用 B bins 的 Time-Integrated Image of Events，生成 `B x H x W` event time image。RPM 将 initial template、online template、search 的 patches 进行 randomized patchwork，并附加 type encoding。

network 为 dual-single-dual：image/event branches 各自经 ConvFormer Spike Blocks 提取 modality-specific features；加入 position/modality/type encodings 后拼接，经过 12 个 TransFormer Spike Blocks 做 joint fusion；最后以两条 SNN tracking heads 预测，并融合 response maps。STR 对两个 template 的 latent features 和 spatial boundaries 加约束。

## 5. Technical Details

### Event Representation

event `E(x,y,t,p)` 在 accumulated time interval 内先分成 `B` bins，分别累积 polarity 并经 sigmoid-like activation/normalization 转为 `[0,255]` 的 image-like tensor。该表示保留 bin 内 polarity/time ordering，但已把原生 asynchronous event 流离散化；与 frame 的 temporal synchronization 细节需人工核对。

### Spiking Network Architecture

ConvFormer Spike Block 用 separable spike convolution 作为 token mixer：pointwise convolution、spiking neuron、depthwise convolution，再配 channel convolution mixer。TransFormer Spike Block 包含 separable spike convolution、Cross-Shaped Window Spiking Self-Attention (CSWin-SSA) 和 Channel MLP；`Q/K/V` 都经 spiking neuron，attention output 有 scale factor。

论文将 neuron 记为 Spike Firing Approximation (SFA) [11]，没有在主文重新完整定义其 surrogate/update；需在 code 或 cited model 中确认每个 block 的 exact neuron dynamics、timesteps、firing rate。

### RPM and Encodings

RPM 随机拼接 temporal templates 与 search frames，避免 padding boundary 让网络把 absolute location 当作 tracking cue；learnable type encoding 标注各 patch 的 logical role，使 residual padding 得以保留。position and modality encodings 在 fusion 前加入。本文的 RPM 与标准 random crop 不同：它是 tracking inputs 的 spatial reorganization，以保持/扰动 layout 来降低 positional bias。

### STR and Loss

STR 在两个 template features 之间要求 spatial-temporal consistency，缓解 RPM 边界导致的 matching asymmetry。tracking head 以 response-map similarity fusion 联合两个 modality；response loss 用 Gaussian-Weighted Focal loss，对 image/event response maps 以 temperature `tau=2` 对齐。Appendix 指出 total training 还包括 box-prediction losses，精确 full loss weight应由人工读 code/appendix核验。

### Efficiency Estimate

论文用 45nm constants `E_MAC=4.6 pJ`、`E_AC=0.9 pJ`，按 layer firing rate 估算 SNN power。该数值是 theoretical power，不是 neuromorphic hardware measurement；GPU FPS/AC-MAC table只可作为 implementation reference。

## 6. Experiments

### Datasets, Metrics and Baselines

frame-event tracking 在 FE108、VisEvent、COESOT 上测试；event-only variant SpikeET 也在 FE108/VisEvent 比较。指标为 success AUC、precision rate (PR)、parameters、estimated power，比较 ANN trackers、ANN-SNN trackers、SDTrack/SNNTrack 等。

### Main Results

Table 9：SpikeFET-Tiny 在 FE108/VisEvent/COESOT 分别为 `68.5/96.5`、`56.8/73.5`、`64.0/77.9`（AUC/PR），estimated compute `30.34` MAC/AC；SpikeFET-Base 分别为 `68.7/97.0`、`59.0/75.3`、`68.5/81.7`，`121.24` MAC/AC。需注意表中 MAC/AC 与 Table 1 的 power presentation 不同，不能混为 mJ。

event-only SpikeET 在 FE108 为 `64.4 AUC / 94.7 PR`、VisEvent 为 `39.4 / 54.0`，parameters `22.36M`、estimated power `8.80 mJ`。论文称其比 SDTrack 在 FE108 高 `4.5` AUC、`3.2` PR；而 SpikeFET-Tiny 在 summary claim 中比 SDSTrack 高 `2.7` AUC、约 `39x` lower theoretical power，这些都应保留其选择的 baseline/estimation context。

### Ablations

Table 3 的 Tiny variant：无 RPM baseline 在 FE108/VisEvent 为 `32.1/45.0`、`45.1/60.5`；加 RPM 后为 `66.8/94.9`、`55.5/72.4`；加 RPM、type encoding、STR 后为 `68.5/96.5`、`56.8/73.5`。Table 4 显示 full fusion 优于 SpikeFT (frame only) `51.8/76.2, 54.6/71.1` 和 SpikeET (event only) `64.4/94.7, 41.0/57.1`。

## 7. Main Contributions

1. 提出被作者称为 first fully spiking unified frame-event tracker 的 SpikeFET。
2. 采用 dual-single-dual structure，在 spiking convolution/Transformer 中融合 frame/event features。
3. 提出 RPM，通过 randomized spatial reorganization 加 type encoding 抑制 padding-induced position bias。
4. 提出 STR 与 dual-head response similarity fusion，增强 temporal template matching。
5. 在 FE108、VisEvent、COESOT 及 event-only settings 报告 accuracy/efficiency trade-offs。

## 8. Limitations and Risks

“fully spiking”应以网络 activation path 理解，input event 已 rasterize 成 time-integrated tensor，frame sensor、event binning 和 possible preprocessing 不是 event-by-event neuromorphic pipeline。它还依赖 image frame，因此不等同于纯 event-camera tracker。

大幅 RPM gain 表明该 module 与 baseline training/design 强耦合，需检查是否存在 patchwork distribution、input order 或 initialization 的 confound。所有 energy claims 为 estimated 45nm operation cost，不含 frame/event acquisition、temporal binning、memory traffic 与 on-chip implementation。

## 9. Relation to SNN for Event Cameras

分类：A: SNN + Event Camera core paper。

SpikeFET 的 event branch、spiking backbone/fusion/head 与 event-camera tracking task 均为方法核心。它也代表 hybrid-input but fully-spiking-network 这一 survey 子路线，可与 pure event trackers SDTrack、SpikeTrack 和 ANN-SNN fusion methods 比较。

## 10. Relation to Survey Taxonomy

- Event representations for SNNs：time-integrated multi-bin event time image。
- SNN architectures for event cameras：ConvFormer Spike Block、CSWin-SSA、dual-single-dual fusion。
- Hybrid ANN-SNN models：它避免 ANN-SNN network hybrid，但输入为 frame + event。
- Event-based tracking：frame-event SOT、RPM、STR、response-map fusion。
- Efficiency, latency, and energy：firing-rate-based theoretical power、GPU FPS reference。
- Open challenges：multimodal synchronization、rasterization、position invariance、hardware evidence。

## 11. Key Terms and Concepts

- SpikeFET：Fully Spiking Frame-Event Tracking framework。
- SpikeET：SpikeFET 的 event-only tracking variant。
- RPM：Randomized Patchwork Module，随机重排 tracking patches。
- STR：Spatial-Temporal Regularization，约束 two-template latent consistency。
- CSWin-SSA：Cross-Shaped Window Spiking Self-Attention。
- SFA：Spike Firing Approximation，论文引用的 spiking-neuron implementation。
- response loss：约束两模态 response maps 的 Gaussian-Weighted Focal loss。

## 12. Questions for Human Deep Reading

1. image frame 与 event time image 如何 timestamp-align；online template 的 update rule 是什么？
2. RPM 随机化在 training/inference 都使用吗，patch geometry、sampling distribution 和 seed 是否固定？
3. SFA 的 membrane update、surrogate gradient、T 和 reset setting 分别是什么？
4. STR 的 exact formula、latent layers、weights 以及与 response loss 的总 loss 关系是什么？
5. event B bins 和 accumulation window 如何随 FE108/VisEvent/COESOT 改变？
6. Table 1、9 的 power/MAC/AC metrics是否统一；39x 的 comparison是否只针对 specific Tiny/SDSTrack setting？
7. ablation 中无 RPM 的极低分数是否与 training instability 或 input ordering 相关？
8. 是否存在真实 hardware latency、energy 或 memory measurement来验证 theoretical power？

## 13. Evidence Notes

- Abstract 与 Section 1，第 1-2 页：fully spiking claim、dual-single-dual design、RPM/STR、high-level results。
- Figure 3 与 Section 3.1，第 3-5 页：ConvFormer/TransFormer spike blocks、encodings、dual tracking heads。
- Section 3.2-3.3，第 5-7 页：RPM 和 STR 的位置/temporal matching motivation。
- Section 4 / Tables 1-4，第 8-10 页：FE108、VisEvent、COESOT comparison 和 module ablation。
- Appendix B.2/C.1/C.2，第 17-18 页：event time-image formula、response loss、45nm energy estimation。
- Appendix G / Tables 9-10，第 21 页：runtime、MAC/AC、full tracking scores。

## 14. Draft Survey-Usable Sentences

Draft material: SpikeFET uses a fully spiking network to fuse conventional frames with temporally integrated event images for single-object tracking.

Draft material: Its RPM and STR target a tracking-specific issue often obscured in backbone comparisons: position bias from padding and template-boundary asymmetry after multimodal reorganization.

Draft material: The reported power advantage is derived from firing-rate-based operation estimates; it should be distinguished from end-to-end energy measured on a frame-event sensing system.
