---
title: "A Simple and Effective Point-based Network for Event Camera 6-DOFs Pose Relocalization"
authors: ["Hongwei Ren", "Jiadong Zhu", "Yue Zhou", "Haotian Fu", "Yulong Huang", "Bojun Cheng"]
year: 2024
venue: "CVPR"
level: "B"
priority: "P0"
advisor_track: "yes"
summary_version: "v1"
summary_type: "Codex automated PDF-based summary"
source_card: "01-papers-by-conference/CVPR2024/B/2024-CVPR-B-a-simple-and-effective-point-based-network-for-event-camera-6-dofs-pose-relocalization.md"
official_page: "https://openaccess.thecvf.com/content/CVPR2024/html/Ren_A_Simple_and_Effective_Point-based_Network_for_Event_Camera_6-DOFs_CVPR_2024_paper.html"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2024/papers/Ren_A_Simple_and_Effective_Point-based_Network_for_Event_Camera_6-DOFs_CVPR_2024_paper.pdf"
local_pdf_status: "downloaded"
status: "auto-generated; needs human review"
tags: ["event camera", "PEPNet", "event cloud", "point-based network", "pose relocalization", "A-Bi-LSTM", "advisor-track support"]
---

# Summary V1｜A Simple and Effective Point-based Network for Event Camera 6-DOFs Pose Relocalization

## 1. One-sentence Summary

PEPNet 直接将 `(x, y, t)` event cloud 作为 pseudo-point cloud 输入，用保留时间顺序的 hierarchical point network、temporal attention 和 Attentive Bi-directional LSTM 回归 event camera 的 6-DOFs pose。

## 2. Research Problem

本文解决 event-camera Camera Pose Relocalization (CPR) 中表示与计算效率之间的矛盾。已有 event-based CPR 通常先把异步 events 聚合为 event images、time surfaces 或其他 dense/grid representations，再交给 CNN/LSTM；这会压缩 fine-grained timestamp information，也常带来较重的 network 或额外的 preprocessing。

CPR 需要从场景中的结构、运动与深度线索回归 camera translation 和 rotation，常见于 AR、VR 与 robotics 等 edge-device 场景。作者认为 event 的高时间分辨率和稀疏性与 CPR 密切相关，因此提出直接处理 raw event cloud，同时避免把 point-cloud method 中与事件时间顺序冲突的 permutation invariance 假设直接照搬过来。

## 3. Background and Motivation

event camera 在 log brightness change 超过阈值时异步触发 event，每个 event 为 `(x, y, t, p)`。对 pose relocalization 而言，`x-y` 提供空间位置，`t` 反映细粒度运动变化；将 `t` 作为 pseudo-3D point cloud 的第三坐标可以保留时空稀疏结构。

传统 PointNet/PointNet++ 及其 hierarchical variants 常追求 point permutation invariance，并用 MaxPooling 聚合邻域。但 event sequence 的生成顺序本身具有时间语义：若随意打乱或只保留每个 channel 的 maximum，可能损失事件动态。PEPNet 因而保留 timestamp order，并以 attention aggregation 和 A-Bi-LSTM 分别建模局部与跨阶段的 temporal feature。

## 4. Method Overview

输入 raw event stream 后，PEPNet 先按 sliding window 取 events，对坐标和时间归一化并采样固定数量的 points。随后，三个 hierarchical stages 通过 Farthest Point Sampling (FPS) 和 K-Nearest Neighbors (KNN) 形成局部 groups，以 residual MLP 抽取 point features；在 group 内使用 temporal attention aggregation，而不是 MaxPooling。最后，Attentive Bi-directional LSTM (A-Bi-LSTM) 对保留下来的 ordered features 做显式时间建模，fully connected regressor 输出 translation `p` 与 rotation Euler angles `q`。

输入是 `(x, y, t)` pseudo-point cloud，polarity 不出现在论文给出的核心 point coordinate 公式中。模型不是 SNN，也不是 ANN/SNN hybrid；其核心是 point-based network + attention + Bi-LSTM。输出为 6-DOFs pose。

## 5. Technical Details

### Event Representation

给定 event sequence `E = {e_k = (x_k, y_k, t_k, p_k)}`，论文在 pose 对应的 sliding window 内收集 events，形成 `P_i`。每个 window 被采样为固定 `N = 1024` 个 points，并将 `x`、`y` 除以 camera width/height，将 timestamp 归一化到窗口内的相对范围。这样每个输入 point 保留 normalized `(x, y, t)`。

论文强调 event cloud 的 `t` 维与 LiDAR point cloud 的 physical depth 不同，因此网络不能只沿用普通 point-cloud invariance。Algorithm 1 给出 `R = 1e+3` 的窗口参数，但其在全文中的时间单位与数据预处理细节需要在 V2 阶段再核对。

### Spiking Neuron / SNN Module

本文没有 spiking neuron、membrane dynamics、surrogate gradient 或 ANN-to-SNN conversion。尽管输入来自 event camera，PEPNet 是 non-spiking point-based baseline。

### Network Architecture

每个 hierarchy stage 包含 grouping/sampling、standardization、local feature extraction、temporal aggregation 和 global feature extraction。FPS 选择 centroids，KNN 构造邻域；point order 严格按 timestamp 维持。grouped coordinates 相对 centroid 标准化后，经带 BatchNorm、activation 和 residual connection 的 bottleneck MLP 提取 features。

对于 group 内 feature `F_local = (F_t1, ..., F_tk)`，模型以 MLP 加 Softmax 生成 attention weights `A = (a_t1, ..., a_tk)`，并计算 weighted sum `F_aggre = sum_k a_tk F_tk`。它替代 MaxPooling，以便在聚合中保留多个时刻的细粒度信息。

三个 hierarchy stages 后，A-Bi-LSTM 同时从前向与后向处理 feature sequence，并再次通过 attention 汇聚不同时刻的双向输出。作者将前一部分称为 implicit temporal feature，而把 Bi-LSTM 建模的跨时间依赖称为 explicit temporal feature。

### Training Strategy

论文明确报告实验在 AMD Ryzen 7950X、RTX 4090 与 32GB memory 的 server 上完成。正文未完整给出 optimizer、batch size、initial learning rate 或 standard training epoch；这些参数应在 appendix/code 或 V2 人工阅读中核验。loss ablation 使用 PEPNet tiny 训练 100 epochs。

### Loss Function

pose loss 由 translation error、rotation error 与 L2 regularization 组成：`Loss = alpha ||p_hat - p||^2 + beta ||q_hat - q||^2 + lambda sum_i w_i^2`。其中 `alpha` 与 `beta` 平衡平移和旋转，`lambda` 是 weight regularization coefficient。Table 5 表明不同 alpha/beta 比例会随 translation、rotation、6-DOFs scene 而改变误差。

### Inference Process

推理时 event window 经 sampling/normalization、three-stage hierarchy、A-Bi-LSTM 和 regressor 输出 pose。论文在 IJRR novel split 上报告 PEPNet server inference time 为 6.7ms/sample；FPS/KNN grouping and sampling 是主要耗时来源，因此该时间不应直接理解为 event-sensor end-to-end latency。

## 6. Experiments

### Datasets and Protocols

论文在 indoor IJRR 和 outdoor M3ED event-based CPR datasets 上实验。IJRR 使用 random split 与 novel split：random split 随机取 70% sequences 训练、30% 测试；novel split 按时间顺序以前 70% 训练、后 30% 测试。M3ED 选取 Car、Falcon、Spot 三类 robot 的五个 outdoor-night sequences，并将 point count 从 1024 提高到 2048。

baselines 包括 PoseNet、Bayesian PoseNet、Pairwise-CNN、LSTM-Pose、SP-LSTM、CNN-LSTM、DSAC* 和 AECRN。指标主要是 translation / rotation median error、combined translation-plus-rotation error、parameters、FLOPs 和 inference time。

### Main Results

Table 1 的 IJRR random split 显示，PEPNet average error 为 `0.013m, 0.904 degrees`，对应 `0.774M` parameters 和 `0.459G` FLOPs；PEPNet tiny 为 `0.019m, 1.306 degrees`、`0.064M` parameters、`0.033G` FLOPs。CNN-LSTM 的 average 为 `0.019m, 1.591 degrees`、`12.63M` parameters、`1.998G` FLOPs。论文据此报告 PEPNet 相对 CNN-LSTM 的 average combined error improvement 为 38%。

Table 2 的 IJRR novel split 中，PEPNet average 为 `0.029m, 2.13 degrees`，略优于 AECRN 的 `0.035m, 2.23 degrees`；PEPNet inference time 为 6.7ms/sample，DSAC* 与 AECRN 均为 30ms/sample。作者同时指出 novel split 下 distribution shift 会使 PEPNet 出现更明显 overfitting。

Table 3 的 M3ED random split 中，PEPNet 在五个 outdoor-night sequences 的 average 为 `0.372m, 1.04 degrees`，而 CNN-LSTM 为 `0.43m, 2.197 degrees`。

### Ablations and Efficiency

Table 4 在 IJRR shape-translation sequence 上比较 hierarchy structure、LSTM、Bi-LSTM 和 temporal aggregation。完整设置的 translation / rotation / combined error 为 `0.011m / 0.582 degrees / 2.12`，优于只使用 hierarchy structure 的 `0.015m / 0.884 degrees / 3.04`。这支持 temporal aggregation 与 bidirectional sequence modeling 的作用。

论文的 lightweight claim 主要基于 parameter/FLOP reduction 与 server inference time，并非 neuromorphic hardware energy measurement。PEPNet tiny 虽只有 CNN-LSTM 参数量约 0.5%，但其 FPS/KNN preprocessing 仍需要在真实 edge hardware 上单独评估。

## 7. Main Contributions

1. 提出 PEPNet，直接从 raw event cloud 回归 6-DOFs pose，而非先转成 event images。
2. 针对 event cloud 的时间顺序改造 hierarchical point processing，避免将普通 point cloud 的 permutation invariance 直接施加到 events。
3. 以 temporal attention aggregation 替代 MaxPooling，并以 A-Bi-LSTM 显式建模时间依赖。
4. 在 IJRR random/novel split 与 M3ED outdoor-night settings 上报告竞争性 pose accuracy，同时给出 parameters、FLOPs 和 inference-time comparisons。
5. 提供 PEPNet tiny，说明较小 point-based model 仍可保持相对强的 CPR 性能。

## 8. Limitations and Risks

本文不是 SNN；survey 中不应把 point-cloud input 等同于 spike-driven computation。

`t` 被作为 pseudo-point cloud coordinate，但时间维与物理 depth 不同。其 coordinate normalization、FPS/KNN metric 和 local neighborhood design 可能对 sensor resolution、motion scale 与 window size 敏感。

PEPNet 的 novelty split 结果已显示 distribution shift / overfitting 风险。其 scene-specific CPR setting 也限制了对新场景的直接泛化。

论文在 server 上报告 6.7ms，但 main bottleneck 是 grouping/sampling。parameters 和 FLOPs 不能完整代表 device-side end-to-end latency、memory traffic 或 energy。

## 9. Relation to SNN for Event Cameras

分类：B: Event Camera side background；advisor-track support。

PEPNet 不含 SNN，但它是同一 advisor method chain 中的 point-based event-camera predecessor。它直接处理 event cloud、保存 time ordering，并将 point hierarchy 与 temporal model 结合，对理解 TTPOINT、EventMamba、SECNet 等表示路线很有参考价值。它也适合作为 event-camera point method 与 point-SNN / voxel-SNN 的非脉冲对照。

## 10. Relation to Survey Taxonomy

- Event representations for SNNs：raw event cloud / pseudo-point cloud representation。
- SNN architectures for event cameras：作为 non-spiking point-based comparator。
- Event-based pose relocalization：6-DOFs CPR。
- Hybrid ANN-SNN models：不属于 hybrid，但可作为 ANN point-network baseline。
- Efficiency, latency, and energy：parameters、FLOPs、server inference time 与 sampling overhead。
- Open challenges：temporal ordering、cross-scene generalization、point sampling cost。

## 11. Key Terms and Concepts

- PEPNet：Point-based Event Pose Network，用于 event-camera 6-DOFs pose relocalization。
- Event Cloud：把 event 的 `(x, y, t)` 看作 pseudo-3D point set。
- CPR：Camera Pose Relocalization，回归 camera position 和 orientation。
- FPS：Farthest Point Sampling，用于选择 point centroids。
- KNN：K-Nearest Neighbors，用于构造 local groups。
- temporal aggregation：根据 learned attention weights 聚合按时间排序的 neighbor features。
- A-Bi-LSTM：Attentive Bi-directional LSTM，对双向 temporal feature 加权汇聚。
- novel split：按时间顺序切分 train/test 的更难 protocol。

## 12. Questions for Human Deep Reading

1. `R = 1e+3` 在 Algorithm 1 中的具体时间单位是什么，window 与 pose label 的 5ms resolution 如何对应？
2. sampling 1024 points 时是否按 timestamp、polarity 或 density 做了额外约束？
3. `t` 与 `x-y` 在 FPS/KNN distance 中是否采用同尺度度量，normalization 是否足够？
4. A-Bi-LSTM 的输入 sequence 是 centroids 的 timestamp order 还是 stage-level features 的另一种序列？
5. Table 1 的 38% improvement 使用的 combined metric 如何精确计算？
6. novel split 下 PEPNet 的 overfitting 主要来自 scene-specific training、数据量，还是 point-cloud representation？
7. 6.7ms 是否包含 event loading、sliding-window construction、FPS、KNN 与 output postprocessing？
8. PEPNet tiny 在 IJRR 和 M3ED 上的 accuracy-efficiency tradeoff 是否足够稳定？
9. 与 TTPOINT、EventMamba、SECNet 相比，PEPNet 对 temporal order 的保留机制有何关键差异？

## 13. Evidence Notes

- Abstract，第 1 页：提出 PEPNet、raw Point Cloud input、A-Bi-LSTM、IJRR/M3ED result claims 和 PEPNet tiny。
- Section 3.1，第 3 页：定义 event cloud、sliding window、`N = 1024` sampling 与 coordinate normalization。
- Section 3.2-3.3，第 4-5 页：说明 timestamp-order-preserving hierarchy、temporal aggregation 与 A-Bi-LSTM。
- Eq. (20)，第 5 页：translation、rotation 和 L2 regularization 的 pose loss。
- Section 4.1-4.2，第 6 页：datasets、splits、baselines 与 hardware environment。
- Table 1，第 7 页：IJRR random split accuracy、parameters、FLOPs。
- Table 2-3，第 8 页：IJRR novel split inference time 与 M3ED results。
- Table 4-5，第 8 页：module 与 loss-coefficient ablations。

## 14. Draft Survey-Usable Sentences

Draft material: PEPNet is a representative non-spiking point-based event-camera method that preserves the temporal ordering of raw event clouds for 6-DOFs pose relocalization.

Draft material: Its temporal attention aggregation and A-Bi-LSTM illustrate one route for exploiting event timing without converting events into dense frames or using spiking neurons.

Draft material: Although PEPNet reports low parameter counts and a 6.7ms server inference time, FPS/KNN preprocessing should be included before making end-to-end edge-efficiency claims.
