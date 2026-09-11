# Taxonomy census Batch 003 — Sol High lightweight review

日期：2026-09-11。对象：B003 的 57 篇 title—abstract census。

Batch 003 通过轻量 High 核查，可以继续 Batch 004。核查覆盖 5 篇 core、3 篇 uncertain 和 5 篇分层样本；三个 PDF trigger 均已关闭。

关键修正：

- `ICML2025-0323` 的 CCNN 是连续耦合动力学编码器，事件相机关系成立但没有离散 SNN computation，改为 `event_camera_only / single_axis`。
- `NeurIPS2025-3401` 的官方补充材料明确使用 FE108、FELT、VisEvent 事件相机数据，BSA 是 tracking task network，改为 `core_intersection / method_coupled / task_network`。
- `CVPR2024-2342` 的官方论文实验包含 CIFAR10-DVS 和 DVS-Gesture，Bit Budget 属于通用 SNN 效率/量化分析，改为 `core_intersection / benchmark_only / not_applicable`。
- `CVPR2026-1873` 的 SDA 满足 event-interface 交接判据；`NeurIPS2025-0641` 的 LIF Event Attention 也满足事件流到后续记忆模块的接口判据；`CVPR2025-1714` 保持 event-specific training/analysis 且没有新的推理 role。

修正后 B003 分布：scope 为 core 7、event-only 18、SNN-only 14、out-of-scope 18；directness 为 method-coupled 3、event-specific training/analysis 1、benchmark-only 3、single-axis 32、neither-axis 18；provisional role 为 event-interface 2、task-network 2、not-applicable 50、unknown 0。PDF trigger 为 0。

本轮未发现需要 Astra 裁决的新 role，也未合并开放编码。`frequency_generalized_event_ssm` 与 `path_selective_event_ssm`，以及 B003 的 `dense_to_sparse_event_depth_distillation` 与 B002 的 image-to-event depth distillation，继续作为待全库聚类的机制家族保留。
