# Taxonomy 边界裁决：B005–B007

## 裁决范围与原则

本裁决基于现有 census、`taxonomy-midterm-synthesis-report.md`、High 全文边界审查、protocol 与 validator；不重新检索、不修改 CSV/schema/protocol/codebook/membership。`scope` 判断两条轴是否存在；`intersection_directness` 判断交叉深度；role 只有在 SNN 改变推理路径时赋值；service 描述实际系统服务，不等同于贡献类型。

## 逐篇裁决

### ICML2024-1996

- **裁决**：修改 `scope=event_camera_only`；`intersection_directness=single_axis`；`provisional_snn_role=not_applicable`；`snn_service_function=no_specific_service`；`pipeline_position=event-camera recordings → ALERT token embedding → ViT/Transformer recognition`。其余字段保持。
- **证据**：全文 Sec.2.2–2.3、3.1.1 明列 DVS128Gesture/N-Cars，但模型为标准 ViT/Transformer，ALERT leakage 是 token 更新而非 LIF/脉冲神经元。
- **理由**：有 event-camera 轴、无真实 SNN 轴，故不能保留 core 或任何 SNN role/service。

### NeurIPS2024-0783

- **裁决**：`scope=core_intersection`；`intersection_directness=benchmark_only`；`provisional_snn_role=not_applicable`；`snn_service_function=no_specific_service`；`pipeline_position=static images/CIFAR10-DVS → generic shortcut/evolutionary SNN → classification`。其余字段保持。
- **证据**：全文贡献是通用 shortcut-backprop/evolutionary SNN training；CIFAR10-DVS 仅出现在实验设置与 Table 4。
- **理由**：两条轴均存在，但事件数据没有改变 SNN 推理路径，属于 benchmark-only。

### CVPR2026-3426

- **裁决**：`scope=core_intersection`；`intersection_directness=benchmark_only`；`provisional_snn_role=not_applicable`；`snn_service_function=no_specific_service`；`pipeline_position=DVS Gesture and static/sequential inputs → LIF reservoir/MLP-like TDA-SNN → classification`。其余字段保持。
- **证据**：Sec.3 的 single LIF、delayed autapses、surrogate gradients；Sec.4 的 DVS Gesture 与静态 CIFAR/MNIST 实验。
- **理由**：DVS 是 benchmark，方法没有 event-specific interface 或 event-conditioned inference。

### ICML2025-2800

- **裁决**：`scope=core_intersection`；`intersection_directness=benchmark_only`；`provisional_snn_role=not_applicable`；`snn_service_function=no_specific_service`；`pipeline_position=N-Omniglot (DVS)/CUB/miniImageNet → FSL-SNN feature module → few-shot classification`。其余字段保持。
- **证据**：全文数据集说明确认 N-Omniglot 为 DVS/neuromorphic few-shot 数据；SNN 是通用 few-shot 模块。
- **理由**：存在两轴，但 N-Omniglot 只作为评测来源，未形成事件接口服务。

### CVPR2026-0405

- **裁决**：`scope=core_intersection`；`intersection_directness=benchmark_only`；`provisional_snn_role=not_applicable`；`snn_service_function=no_specific_service`；`pipeline_position=static CIFAR-100/ImageNet and DVS-CIFAR10 → ResNet-LIF with TRE temporal gate → classification`。其余字段保持。
- **证据**：实验同时使用静态集与 DVS-CIFAR10；TRE 是 ResNet-LIF 的通用 temporal representation/forgetting gate。
- **理由**：DVS 轴明确，但没有事件专用推理路径。

### CVPR2026-3630

- **裁决**：保持 `scope=core_intersection`、`intersection_directness=method_coupled`、`provisional_snn_role=task_network`；修改 `pipeline_position=event stream → GTP global-trajectory/event-image aggregation → Spiking MetaFormer + spike tracking head → trajectories`；从 service 移除 `asynchronous_event_processing`，保留其余已有服务标签（若表中为 temporal/sparsity/low-latency）。
- **证据**：全文 GTP 先聚合 global trajectory/event images，随后 fully spike-driven tracker；没有 SpikeSlicer 式 SNN-adaptive slicing。
- **理由**：方法耦合和 task-network 判断成立，错误只在把 GTP 误写成 adaptive slicer 并过度宣称异步处理。

### CVPR2024-0028（LED/DTSNN）

- **裁决**：保持 `scope=core_intersection`；改 `intersection_directness=benchmark_only`、`provisional_snn_role=not_applicable`、`snn_service_function=no_specific_service`；`pipeline_position=LED paired events → DED denoising main model / DTSNN dynamic-threshold LIF baseline → clean events`。其余字段保持。
- **证据**：Sec.4 “DTSNN for Event Denoising”、Fig.7、Sec.5 显示 LED/DED 去噪是主贡献，DTSNN 是 baseline。
- **理由**：baseline 的 LIF 不等于论文主方法改变 event-camera 推理接口；benchmark-only 能保留交叉语料而避免虚构 SNN 服务。

### ECCV2024-1740

- **裁决**：保持 `scope=core_intersection`、role `not_applicable`、service `robustness`；改 `intersection_directness=event_specific_training_analysis`。其余字段保持。
- **证据**：全文在 CIFAR10-DVS、DVS Gesture、N-MNIST 上对 raw-event adversarial perturbation 与 SNN vulnerability 做专门分析。
- **理由**：攻击改变的是事件输入/训练分析对象，不是新增 SNN 推理模块；在现有枚举中 event-specific training/analysis 最准确。

### ICLR2026-3011

- **裁决**：保持 `scope=core_intersection`、`intersection_directness=benchmark_only`；改 `provisional_snn_role=not_applicable`、`snn_service_function=no_specific_service`。其余字段保持。
- **证据**：SAFA-SNN 的 adaptive dynamics、synaptic traces、sparsity/continual-learning 机制在 CIFAR10-DVS、DVS128Gesture 等 neuromorphic benchmarks 上评测，但未形成 event-specific path。
- **理由**：记忆与稀疏是通用 SNN 属性/贡献，不能自动升级为 event-camera 服务或 task-network role。

### ICLR2026-1286

- **裁决**：保持 `scope=core_intersection`、role `not_applicable`、service `robustness`；改 `intersection_directness=event_specific_training_analysis`；`pipeline_position=event timing grids → spike-retiming adversarial optimization → attacked event-driven SNN analysis`。其余字段保持。
- **证据**：全文对 CIFAR10-DVS、DVS-Gesture、N-MNIST 进行 timing-only retiming attack 与 timing-aware adversarial training。
- **理由**：这是事件特定攻击/鲁棒性分析，不是新的推理路径，故不使用 method_coupled。

### ICCV2025-1894

- **裁决**：保持 `scope=core_intersection`、`intersection_directness=benchmark_only`；改 `provisional_snn_role=not_applicable`、`snn_service_function=no_specific_service`。其余字段保持。
- **证据**：SpiLiFormer 的 lateral-inhibition Spiking Transformer 在 CIFAR10-DVS、N-Caltech101 等数据上评测；lateral inhibition 是通用 SNN 架构机制。
- **理由**：DVS 仅为 benchmark，不能把通用 sparsity/feature 属性解释成 event-specific service。

## 三项统一规则

### 1. 攻击论文的 directness

- **benchmark_only**：论文提出通用 SNN attack/robustness 方法，DVS 只作为与静态数据并列的评测集；攻击生成或分析不依赖事件的时间/极性/异步结构。
- **event_specific_training_analysis**：攻击、训练或鲁棒性分析明确操作 event-camera 的事件时间、极性、raw-event 流或 DVS 特有编码，但不改变被评测 SNN 的推理路径。ECCV2024-1740 与 ICLR2026-1286 属此类。
- **method_coupled**：论文新增或改造事件到 SNN 的推理链路（编码、聚合、接口、SNN 模块或输出回路），攻击不是唯一的交叉机制。攻击论文不能仅因使用 raw events 就升为 method_coupled。

### 2. LED 中 DTSNN baseline

CVPR2024-0028 保留 `core_intersection`，因为 LED 是 contrast-change event-camera 数据且 DTSNN 确为 SNN；但 directness 为 `benchmark_only`，role 为 `not_applicable`，service 为 `no_specific_service`。DTSNN 只有在论文主方法把动态阈值 LIF 接入事件去噪推理链并由此产生方法性贡献时，才可赋 `task_network` 或 event-interface service；baseline 身份本身不足以赋 role。

### 3. 通用 SNN + DVS benchmark

- **task_network**：SNN 是论文主方法并实际接收事件流/DVS 表示，且其模块改变从输入到任务输出的推理路径；不要求提出 event-specific encoding，但必须是交叉系统中的主推理网络。
- **not_applicable**：SNN 仅用于训练、攻击、转换、硬件、评测或 baseline，未改变事件视觉推理路径；也适用于 benchmark-only 的通用 SNN 论文。
- **no_specific_service**：论文没有证据表明 SNN 为 event-camera vision 提供独特系统服务；通用 temporal dynamics、sparsity、memory、lateral inhibition 不能仅凭 DVS benchmark 自动算作服务。
- **benchmark_only**：两条轴均明确存在，但 DVS/event-camera 只作为评测、数据集或平台共现，方法没有 event-specific inference coupling。它仍属于 `core_intersection`，不能降为单轴。

## 建议回填清单

- ICML2024-1996：scope、directness、role、service、pipeline。
- NeurIPS2024-0783：scope、directness、role、service、pipeline。
- CVPR2026-3426：scope、directness、role、service、pipeline。
- ICML2025-2800：scope、directness、role、service、pipeline。
- CVPR2026-0405：scope、directness、role、service、pipeline。
- CVPR2026-3630：pipeline；删除 service 中 `asynchronous_event_processing`。
- CVPR2024-0028：directness、role、service、pipeline。
- ECCV2024-1740：directness。
- ICLR2026-3011：role、service。
- ICLR2026-1286：directness、pipeline。
- ICCV2025-1894：role、service。

## 仍存在的争议

1. `benchmark_only` 与 `event_specific_training_analysis` 的边界依赖论文是否把事件时间/极性作为攻击或训练变量；未来遇到混合攻击需保持“是否改变推理路径”的优先判据。
2. `embedded_module` 在全库是否会出现，当前 11 篇没有新增证据支持该 role。
3. `no_specific_service` 是“未声称服务”而非“没有任何 SNN 能力”；正式写作时不得把它作为能力缺失的强结论。
4. LED DTSNN baseline 的处理是当前 protocol 下的保守规则；若后续全文显示 baseline 实际参与主方法的事件去噪路径，应另行 High/Astra 裁决。

## 验证与提交状态

按用户要求执行：

- `git diff --check`：通过。
- `python3 scripts/validate_taxonomy_census.py --require-batch B007`：通过（source=572，census=228，B007=114）。
- commit：待提交后填入实际 hash。
- 未 push。
