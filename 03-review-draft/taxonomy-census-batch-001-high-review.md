# Taxonomy census Batch 001 — Sol High lightweight review

日期：2026-09-10。对象：B001 的 57 篇 title/abstract census，以及两个摘要无法消歧的 PDF 边界项。

## 结论

Batch 001 通过轻量 High 核查，可以继续全库普查。核查同时确认了一个需要立即澄清的 scope 语义：`core_intersection` 是 SNN × event-camera 交叉语料库，而不是“方法深度耦合”标签。任何同时具有 SNN 与 contrast-change event-camera / DVS 关系的论文都进入该语料库，包括仅在 DVS benchmark 上训练或评测的通用 SNN 方法；交叉深度由 `intersection_directness` 表达。

这项修改不会预先冻结 taxonomy，也不扩大 16 列 census schema。它只是把“是否属于两轴交叉语料库”和“交叉有多深”分开。

## 核查范围与修正

- 全查原有 2 篇 `core_intersection` 和 2 篇 `uncertain`；从 event-camera-only、SNN-only、out-of-scope 各抽查 2 篇。
- `ICLR2025-2158` 与 `NeurIPS2025-2213` 保留为 `core_intersection / benchmark_only`。前者改为无适用推理 role；后者从误用的 `algorithmic_engine` 改为 `task_network`。
- `NeurIPS2024-0322` 的摘要只写 “neuromorphic datasets”，全文实验明确包含 CIFAR10-DVS，因此从 `snn_only / single_axis` 改为 `core_intersection / benchmark_only`，role 为 `task_network`。
- `CVPR2026-3868` 的单时间步 IF 单元只二值化 Gaussian 标签，不构成 SNN，且没有事件相机输入；改为 `out_of_scope / neither_axis`。
- `ICLR2026-0741` 使用的是高频 spike camera，而非 contrast-change event camera；校准器为连续 MLP/Transformer，不是 SNN；改为 `out_of_scope / neither_axis`。
- 分层抽查的两篇 event-camera-only 记录通过。
- 规则级规范化：单轴论文不再套用交叉系统 role；范围外误命中机制不进入 open-code 聚类。该规范化不表示其余论文都经过全文复核。

修正后 B001 分布为：`core_intersection` 3、`event_camera_only` 24、`snn_only` 12、`out_of_scope` 18、`uncertain` 0。directness 为 `benchmark_only` 3、`single_axis` 36、`neither_axis` 18。

## 对 codebook 0.2 与旧 pilot 的影响

冻结的 codebook 0.2 把“通用 SNN + DVS benchmark”放在 `snn_foundation`，这与本次明确的综述范围不一致。旧 pilot 中目前只发现两条直接受影响的记录：

- `ICML2024-0803`（CLIF）；
- `NeurIPS2025-5334`（STEP）。

它们的 `intersection_directness=benchmark_only`、模型机制、证据和功能 role 不需要重做；未来只需把 scope membership 版本化迁移到 `core_intersection`，并更新由 scope 推导的计数/图纳入规则。

本轮不改写 pilot、E1/E2 校准、Astra 裁决或 0.2 freeze decision，因为这些文件是当时规则下的历史快照。全库 census 不应为此暂停。建议在 572 篇普查完成后的 Astra synthesis 中发布 codebook 0.3 scope migration；如果中途需要生成当前 core 清单，则可提前做一次小型版本化迁移，但不重跑 pilot。

## 后续执行规则

接下来的 Mid 批次按 census protocol 0.2 执行：先判断两轴是否存在，再标 directness。High 仍只全查 `core_intersection` / `uncertain` 并对其他 scope 分层抽查；只有摘要可能漏掉会改变 scope 的 DVS 数据集或边界机制时才读 PDF。开放代码保持细粒度，等全库完成后再聚类，不要求每批合并成 taxonomy。
