---
title: "SMV-EAR: Bring Spatiotemporal Multi-View Representation Learning into Efficient Event-Based Action Recognition"
authors: ["Rui Fan", "Weidong Hao", "Juntao Guan", "Lai Rui", "Tong Wu", "Fanhong Zeng", "Lin Gu"]
year: 2026
venue: "CVPR"
level: "B"
priority: "P0"
advisor_track: "yes"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/CVPR2026/B/2026-CVPR-B-smv-ear-bring-spatiotemporal-multi-view-representation-learning-into-efficient-event-based.md"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Fan_SMV-EAR_Bring_Spatiotemporal_Multi-View_Representation_Learning_into_Efficient_Event-Based_Action_CVPR_2026_paper.html"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Fan_SMV-EAR_Bring_Spatiotemporal_Multi-View_Representation_Learning_into_Efficient_Event-Based_Action_CVPR_2026_paper.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["event camera", "action recognition", "multi-view representation", "TISM", "DDCF", "DTW"]
---

# Summary V1｜SMV-EAR: Bring Spatiotemporal Multi-View Representation Learning into Efficient Event-Based Action Recognition

## 1. One-sentence Summary

SMV-EAR 是一个 non-spiking event-based action recognition method：它以 Translation-Invariant Spatiotemporal Maps (TISM) 将 sparse events转为 T-H/T-W views，以 Dynamic Dual-branch Cross-view Fusion (DDCF) 做sample-wise weighting，并用 Diverse Temporal Warping (DTW) 模拟real-action speed variation。

## 2. Research Problem

event-based action recognition (EAR) 需同时表示human motion的spatial change和temporal dynamics。已有 Spatiotemporal Multi-View Representation Learning (SMVRL) 把 H-W-T events投影到不同planes，但传统 spatial binning对translation敏感，early concatenation又忽略不同views的dimension mismatch与sample-specific discriminability。

本文不是 SNN paper，而是为 event-camera action recognition 提供representation/architecture/augmentation baseline。它试图用更经济的 multi-view ANN design替代增加transformer scale或直接采用Spiking Transformer的路线。

## 3. Background and Motivation

raw event `e=(x,y,t,p)` 可看作 H-W-T sparse point set。对动作，T-H或T-W projection可显示某spatial axis随time的motion trace，往往比H-W temporal accumulation更突出body movement；但若absolute spatial bins固定，摄像机或subject translation会改变map appearance。

同一action在不同sample/view上可能仅一个temporal map可辨，例如vertical/horizontal motion amplitude不同。因此作者将two views走separate ResNet branches，并以semantic features预测每class、每sample的fusion weights；training augmentation还应模拟speed change但不能像time reversal那样改变动作语义。

## 4. Method Overview

event stream先经TISM构建 `F_th` 和 `F_tw` two temporal maps。每个map由translation-invariant window、event measurement和temporal/spatial aggregation组成，作者最终选用event count `c`、polarity-aware `p`与sum aggregation。two maps分别进ResNet-18 branches，global pooled semantic features经multi-head attention/linear module生成dynamic weights，再加权two logits。

DTW在training中随机选多个non-overlap time intervals，以identity、linear、power、exponential或cosine monotonic warp改变timestamps，保持temporal order。output是action class；整个network是standard ANN-style ResNet/attention，不包含spiking neuron。

## 5. Technical Details

### Event Representation: TISM

TISM以translation-invariant interval/window而不是固定absolute binning组织events，并将H-W-T sparse events转换为T-H与T-W dense maps。论文测试count `c`、polarity `p`、latest timestamp `z`等measurement与sum/max/mean/variance aggregation；最终的two-view map用 `c,p,sum`，以兼顾accuracy与CPU conversion time。

TISM并不保留每个event的raw timestamp，仍是dense raster representation；但是相对传统H/W spatial binning，论文在controlled spatial translation test中显示更稳定。

### Dynamic Dual-branch Cross-view Fusion

`F_th`、`F_tw` 经independent ResNet-18得到logits `L_th`、`L_tw`。在classification heads之前global-pool的semantic vectors `S_th/S_tw` 被multi-head attention融合，linear layer产生two sets of `C` class-dependent weights `w_th(E), w_tw(E)`，最后`L = w_th L_th + w_tw L_tw`。这不是simple averaging或early concat：权重随sample及class变化。

作者称它为 DDCF；其“dynamic”具体指 sample-wise fusion weights，而不是event-by-event recurrent state。

### Diverse Temporal Warping

DTW的time-warp function `W` 只调整selected interval内timestamps。instantaneous scale `s(t)=dW/dt`：大于1使action locally slow/ events sparse，小于1使其accelerate/events dense。采用单调functions以避免FlipT式temporal reversal把“sit down”变成“stand up”。default随机interval count为`l=4`。

### Training and Inference

论文以PyTorch/AdamW训练80 epochs，learning rate `1e-4`、weight decay `1e-5`；time axis discretized为 `T=224`，maps resize至`224 x 224`。inference time含CPU sparse-to-dense conversion和RTX 3090 GPU forward，因此对单一GPU/CPU system有效，非neuromorphic energy/latency statement。

## 6. Experiments

### Datasets and Metrics

HARDVS含`107,646` sequences/`300` action types/5 subjects；DailyDVS-200含`22,046` sequences/`200` actions/47 subjects；THU-EACT-50-CHL含`2,330` samples/50 actions。报告five random seeds的Top-1/Top-5、parameters、MACs/FLOPs、CPU+GPU batch-1 inference time；baselines涵盖spike-input、frame、token和multi-view models。

### Main Results

SMV-EAR在HARDVS为 `59.63 Top-1 / 67.56 Top-5`，DailyDVS-200为 `54.65 / 78.28`，`1.8G MACs`、`23.5M` parameters。THU-EACT-50-CHL为 `66.7 Top-1`、`3.6G FLOPs`、`23.5M` parameters。相比Table中的MVF-Net baseline，top-1 gains为`+7.0`、`+10.7`、`+10.2` points；这三个数字对应specific comparable tables，不宜泛化为all EAR settings。

与SNN inputs的SDT、Spikeformer在HARDVS/DailyDVS-200表内显著较低，而token transformer虽强但cost更高；这提供event action-recognition background，但不表示SNN天生不适用EAR，因为architectures、training budget和input representations不同。

### Ablations and Robustness

THU-EACT-50-CHL Table 3：MVF-Net baseline为`56.5%`、`5.6G`、`33.6M`、`14.0 ms`；加TISM为`59.4%`，加TISM+DDCF为`62.9%`、`3.6G`、`23.5M`、`10.6 ms`，再加DTW为`66.7%`。Table 6显示`F_th/F_tw` dual-branch sample-wise fusion为`66.7%`，triple-view仅`67.0%`却增至`5.35G`/`34.7M`。

controlled z-axis shift下，SMV-EAR从`66.7` (0px)到`64.9` (40px)，MVF-Net从`56.5`到`46.1`。这支持TISM的translation robustness，但仍是synthetic test-time shifts，不能完全代替camera-motion distribution evaluation。

## 7. Main Contributions

1. 提出TISM，以translation-invariant event conversion构建temporal multi-view maps。
2. 提出DDCF：two ResNet branches和sample/class-aware dynamic fusion。
3. 提出DTW，以monotonic local temporal warping模拟action speed variation。
4. 在HARDVS、DailyDVS-200、THU-EACT-50-CHL上报告accuracy-efficiency与translation robustness结果。

## 8. Limitations and Risks

SMV-EAR不含SNN，不能证明spiking computation或event-driven hardware efficiency。TISM依赖CPU sparse-to-dense conversion，所报`T(all)`是specific CPU/GPU environment的batched-1 measurement，且没有energy measurement。

T-H/T-W projection舍弃H-W view与部分3D spatial-temporal structure；paper在camera-motion attribute上承认仍较SlowFast低`2.9` points，background events可淹没temporal maps。DTW只模拟monotonic speed variation，不能代表sensor noise、viewpoint变化或more complex temporal distortion。

## 9. Relation to SNN for Event Cameras

分类：B: Event Camera side background；advisor-track support。

它提供event action-recognition中dense multi-view representation、input conversion cost、translation/camera-motion问题的强对照。对SNN survey，它可用来说明SNN需要与何种non-spiking event representation/ANN baseline比较；它本身不是SNN architecture evidence。

## 10. Relation to Survey Taxonomy

- Event representations for SNNs：T-H/T-W multi-view maps可作non-spiking comparator。
- Event-based action recognition：EAR datasets、metrics、multi-view fusion与speed augmentation。
- Datasets and benchmarks：HARDVS、DailyDVS-200、THU-EACT-50-CHL。
- Efficiency, latency, and energy：CPU conversion + GPU forward的end-to-end time分解。
- Open challenges：translation、camera motion、projection information loss、fair SNN/ANN comparison。

## 11. Key Terms and Concepts

- SMV-EAR：Spatiotemporal Multi-View Event-based Action Recognition。
- TISM：Translation-Invariant Spatiotemporal Maps。
- `F_th` / `F_tw`：time-height / time-width event maps。
- DDCF：Dynamic Dual-branch Cross-view Fusion。
- DTW：Diverse Temporal Warping，event timestamp augmentation。
- EAR：Event-based Action Recognition。
- MACs/FLOPs：ANN compute metrics，不是SNN AC operation count。

## 12. Questions for Human Deep Reading

1. TISM translation-invariant window的exact coordinate definition、boundary behavior和normalization是什么？
2. `c,p,sum` maps的channel ranges如何standardize，是否保留polarity sign或two channels？
3. DDCF weights是否softmax-normalized，为什么dimension是`2C`而不是per-view scalar？
4. twoResNet branches是否shareweights，pretraining和input channels是否一致？
5. DTW interval/warp magnitude range以及monotonicity implementation是什么？
6. data splits、subject overlap和five-seed protocol与all baselines是否可比？
7. `T(cpu)`是否含disk I/O、event decoding与data transfer，10.6ms的variance如何？
8. camera motion attribute上的failure是否可借助foreground/background event separation修复？

## 13. Evidence Notes

- Abstract与Section 1，第1-2页：SMVRL limitations、TISM/DDCF/DTW和overall claims。
- Section 3.2-3.3，第3-5页：TISM representation和dynamic dual-branch fusion。
- Section 3.4 / Algorithm 1，第5页：DTW time-warp procedure和monotonic functions。
- Section 4.1，第5页：datasets、metrics、training/inference environment。
- Tables 1-3，第6页：SOTA comparison、THU-EACT result和contribution ablation。
- Tables 4-6与Section 4.3-4.4，第6-7页：TISM/DDCF/shift ablations、camera-motion limitation。

## 14. Draft Survey-Usable Sentences

Draft material: SMV-EAR is a non-spiking multi-view event-action baseline that converts event streams into translation-invariant T-H and T-W maps before dual-branch recognition.

Draft material: Its dynamic cross-view fusion shows that the relative usefulness of temporal projections can vary by action instance, rather than being well served by fixed early concatenation.

Draft material: The reported 10.6ms inference includes sparse-to-dense CPU conversion and GPU forward processing, making it a useful end-to-end ANN reference but not a neuromorphic energy result.
