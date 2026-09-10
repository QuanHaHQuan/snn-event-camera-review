# Taxonomy census Batch 002 — Sol High lightweight review

日期：2026-09-10。对象：B002 的 57 篇 title/abstract census。

## 结论

Batch 002 通过轻量 High 核查，可以继续 Batch 003。没有发现系统性 scope 误判、强迫 role 或 census schema 无法表达的新机制，也不需要在本批次交 Astra 裁决。

本轮核查全部 8 篇原有 `core_intersection`、全部 3 篇 `uncertain`，并分层抽查 5 篇非核心记录。只对会改变 scope 的三个边界项读取全文；其余核查保持在标题—摘要层。

## 修正

- `ECCV2024-1484`：全文实验包含 CIFAR10-DVS、N-Caltech101、N-Cars、ASL-DVS 等事件相机衍生数据，改为 `core_intersection / benchmark_only / task_network`。
- `ICML2024-1239`：全文第 5.2 节在 CIFAR10-DVS 上评测 10-timestep SNN 的梯度稀疏鲁棒训练，改为 `core_intersection / benchmark_only / not_applicable`。这是 cross-cutting 训练与鲁棒性证据，不产生新的推理 role。
- `CVPR2024-1560`：论文明确区分积分式 spike camera 与 event camera；IF 层用于建立可微传感器生成模型和 rendering loss，不是任务 SNN。改为 `out_of_scope / neither_axis / not_applicable`。
- `NeurIPS2024-2942`：scope 与 directness 保留；learnable initial membrane potential 和 last-timestep decoding 会改变任务 SNN 的推理行为，role 从 `not_applicable` 改为 `task_network`。
- `ICML2025-0181`：scope 与 directness 保留；two-phase probabilistic spiking neurons 在转换后的推理网络中运行，role 从 `not_applicable` 改为 `task_network`。

其余 6 篇原有 core 记录通过。五篇分层样本也通过：`ICLR2024-2253` 的主体仍是 BANN、`CVPR2025-1668` 的 SNN 仅出现在背景比较中；一篇 event-only、一篇 SNN-only 和一篇 spike-camera 范围外记录均与 protocol 0.2 一致。

## 修正后分布

- scope：`core_intersection` 10、`event_camera_only` 18、`snn_only` 10、`out_of_scope` 19、`uncertain` 0；
- directness：`method_coupled` 3、`benchmark_only` 7、`single_axis` 28、`neither_axis` 19；
- provisional role：`task_network` 8、`not_applicable` 49；
- PDF trigger：0。

本轮进一步验证了 protocol 0.2 的关键分离：DVS benchmark 足以决定交叉语料库 membership，但不自动产生 event-specific role 或 method-coupled 标签。一般 SNN 的训练/鲁棒性论文可进入 `core_intersection / benchmark_only`，同时保持 `provisional_snn_role=not_applicable`；真正改变推理网络的 neuron/architecture 方法则可标 `task_network`。

## 后续

Batch 003 继续按 protocol 0.2 进行 Mid title/abstract census。开放编码仍保持原始粒度，等全库完成后统一聚类；本轮不修改 codebook 0.2、旧 pilot、Survey/Advisor membership 或正式 taxonomy。
