# B005–B007 及全文证据边界核查

## 范围与访问说明

本轮只核查摘要 census 中触发 `pdf_trigger_question` 的 5 篇论文，以及 B005–B007 标为 High 的 16 篇论文，共 **21 篇唯一论文**。未重新遍历全库，未修改 taxonomy schema、protocol、validator、membership、codebook 或 `00-index/taxonomy-census.csv`。

仓库中没有这些目标论文的本地 PDF；因此以出版社/会议的官方 PDF 或官方 HTML 的全文索引为证据，并按 PDF 印刷页码（能确定时）记录章节。`NeurIPS2024-1436` 的官方 PDF 直接打开超过工具单文件大小限制，但官方索引文本已覆盖摘要、模型构造、算法和实验章节，足以完成边界判断；这不是科学证据不足。命令行下载因当前沙箱 DNS/超时失败，未把失败下载文件写入仓库。

## 逐篇核查结论

| paper_id | PDF 证据（页码/章节） | event-camera/DVS 轴 | 真实 SNN computation | 结论与字段建议 |
|---|---|---|---|---|
| **ICML2024-1996** | ALERT PDF p.3–4 Sec.2.2–2.3、Sec.3.1.1；p.4 明列 DVS128Gesture、N-Cars；p.5–6 Tables 1–3；Transformer 为标准 ViT，ALERT 的“leakage”是 token 更新而非神经元。 | **确认**（DVS128Gesture、N-Cars） | **否**；未见 LIF/膜电位/脉冲神经元计算 | **建议修改**：`scope=event_camera_only`，`intersection_directness=single_axis`，`provisional_snn_role=not_applicable`，`snn_service_function=no_specific_service`；pipeline 改为 “event-camera recordings → ALERT token embedding → ViT/Transformer recognition”。 |
| **NeurIPS2024-0783** | PDF p.2 contributions；p.4–5 Sec.4.2/Algorithm 1；p.6 Sec.5.1 数据设置；p.8 Table 4 的 CIFAR10-DVS 结果。方法是通用 shortcut-backprop + evolutionary SNN training。 | **确认**（CIFAR10-DVS，仅 benchmark） | **确认**（训练和推理均为通用 SNN） | **建议修改**：`scope=core_intersection`，`intersection_directness=benchmark_only`，`provisional_snn_role=not_applicable`，`snn_service_function=no_specific_service`；pipeline/task 补为 “CIFAR10-DVS/static images → generic trained SNN → classification”。 |
| **CVPR2026-3426** | arXiv/PDF Abstract；Sec.3.2–3.5（single LIF、delayed autapses、surrogate gradients）；Sec.4.1 数据设置（DVS Gesture、MNIST/fMNIST、CIFAR10）；Sec.4.4 DVS Gesture 与静态 CIFAR10 实验。 | **确认**（DVS Gesture，benchmark） | **确认**（单 LIF 神经元、延迟自连接和脉冲状态） | **建议修改**：`scope=core_intersection`，`intersection_directness=benchmark_only`，`provisional_snn_role=not_applicable`，`snn_service_function=no_specific_service`；task/pipeline 改为 reservoir/MLP/convolution-like classification on DVS Gesture and image/sequential benchmarks。 |
| **ICML2025-2800** | arXiv/PDF Abstract 与实验章节；N-Omniglot 数据集说明确认其为 DVS/neuromorphic few-shot 数据，另有 CUB、miniImageNet 静态集。 | **确认**（N-Omniglot，benchmark） | **确认**（FSL-SNN 脉冲特征模块） | **建议修改**：`scope=core_intersection`，`intersection_directness=benchmark_only`，`provisional_snn_role=not_applicable`，`snn_service_function=no_specific_service`；pipeline/task 改为 “N-Omniglot (DVS)/static CUB, miniImageNet → self/cross-feature FSL-SNN → few-shot classification”。 |
| **CVPR2026-0405** | CVPR PDF/HTML Sec. Dataset/Experiment；静态 CIFAR-100/ImageNet 与 DVS-CIFAR10；TRE 是 ResNet-LIF 上的 temporal representation/learning-to-forget gate。 | **确认**（DVS-CIFAR10，benchmark） | **确认**（ResNet-LIF SNN） | **建议修改**：`scope=core_intersection`，`intersection_directness=benchmark_only`，`provisional_snn_role=not_applicable`，`snn_service_function=no_specific_service`；task/pipeline 改为 generic SNN classification on static/DVS-CIFAR10。 |
| **NeurIPS2024-1436** | 官方 PDF 索引 Abstract；Sec.4.1 Model Construction/Learning；Algorithm 1（WTA E-step responsibilities、STDP M-step motion-parameter update）。 | **确认**（连续事件流） | **确认**（SNN Bayesian/WTA + STDP） | **确认无需修改**：`core_intersection / method_coupled / algorithmic_engine / event_selection_or_aggregation;algorithmic_inference` 均有显式事件到脉冲状态、E/M 更新的对应关系；不是泛化的“普通 SNN”。 |
| **NeurIPS2024-2388** | PDF p.1 摘要；p.2 Fig.2/Sec.2；p.2–4 Sec.3.1–3.2（event-cell voxelization、LIF spike-triggered adaptive slicing）；p.7–9 Sec.4/结论；Appendix R p.22。 | **确认**（事件流） | **确认**（LIF 触发切片） | **确认无需修改**：SNN 的推理角色确为 `event_interface`，直接度 `method_coupled`，服务 `asynchronous_event_processing;event_selection_or_aggregation;low_latency`。注意其是 SNN 触发切片、与后端 tracker 协作，不应误写成完整 SNN tracker。 |
| **CVPR2026-3630** | CVPR/arXiv Abstract 与 Sec.3；GTP 将事件聚合为 global trajectory prompt/event images，随后 Spiking MetaFormer + tracking head；不是 SpikeSlicer 式 SNN-adaptive slicing。 | **确认** | **确认**（fully spike-driven tracker） | **建议修改 pipeline**：`event stream → GTP global-trajectory/event-image aggregation → Spiking MetaFormer + spike tracking head → trajectories`；保留 `core_intersection / method_coupled / task_network`。建议移除 `asynchronous_event_processing`（可保留 temporal、sparsity、low_latency，取决于表中报告）。 |
| **CVPR2024-0028** | CVF PDF Sec.4 “DTSNN for Event Denoising”、Fig.7；Sec.5 Experiments。LED/DED 数据集和 DED 去噪是主贡献，DTSNN 是动态阈值 LIF 的 SNN baseline。 | **确认**（LED 事件流） | **确认**（DTSNN LIF baseline） | **建议修改**：将 `intersection_directness` 改为 `benchmark_only`，`provisional_snn_role=not_applicable`，`snn_service_function=no_specific_service`；pipeline 注明 “LED paired events → DED denoising (main) / DTSNN LIF baseline → clean events”。不要把 baseline 的 LIF 误归因成 event-interface 服务。 |
| **ECCV2024-1740** | ECCV PDF Abstract；Sec.4.2、Tables 2/4（CIFAR10-DVS、DVS Gesture、N-MNIST raw-event attacks）。贡献是 raw-event adversarial perturbation 与 SNN vulnerability evaluation。 | **确认** | **确认**（被攻击的 SNN） | **建议修改**：`intersection_directness=event_specific_training_analysis`（攻击/鲁棒性分析最接近的合法标签）；`scope=core_intersection`、role `not_applicable`、service `robustness` 保持。 |
| **ICLR2026-3011** | arXiv/PDF Abstract 与实验表；CIFAR100、Mini-ImageNet、CIFAR-10-DVS、DVS128Gesture、N-Caltech101；SAFA 是通用 few-shot class-incremental SNN。 | **确认**（DVS benchmarks） | **确认** | **建议修改**：保持 `core_intersection / benchmark_only`，但改 `provisional_snn_role=not_applicable`、`snn_service_function=no_specific_service`；稀疏/记忆是模型效率与持续学习属性，不是 event-specific inference service。 |
| **ECCV2024-0537** | ECCV PDF Abstract/Sec.1；Sec.5 COCO 与 neuromorphic Gen1 实验；integer-valued training neuron、spike-driven inference、能耗比较。 | **确认**（Gen1 neuromorphic camera） | **确认**（SpikeYOLO） | **确认无需修改**：`core_intersection / method_coupled / task_network` 及 `sparsity_and_efficiency;low_latency;feature_representation` 与 detector 的实际推理角色一致。 |
| **ECCV2024-1778** | ECCV PDF Abstract/Sec.1（事件 `(x,y,t,p)`）；方法章节 SVT + U-shape SNN decoder；Sec.4–5 IJRR/HQF/MVSEC、Table 2 能耗/脉冲率。 | **确认** | **确认**（spike-temporal encoder/decoder） | **确认无需修改**：event-to-video reconstruction 是 SNN 任务网络，当前 `method_coupled / task_network / temporal_modeling;sparsity_and_efficiency;feature_representation` 合适。 |
| **ICLR2026-1286** | ICLR PDF/arXiv Abstract；方法/实验章节（timing-only spike retiming、timing-aware adversarial training）；CIFAR10-DVS、DVS-Gesture、N-MNIST。 | **确认** | **确认**（event-driven SNN 被攻击） | **建议修改**：`intersection_directness=event_specific_training_analysis`；`scope=core_intersection`、role `not_applicable`、service `robustness` 保持。pipeline 改为 “event timing grids → retiming attack → attacked SNN analysis”。 |
| **ICLR2024-0249** | ICLR PDF Sec.5.2/Table 3；N-Caltech101、CIFAR10-DVS、N-Cars、SL-Animals；SLRP/SLTRP relevance-guided event augmentation。 | **确认** | **确认**（SNN relevance propagation） | **确认无需修改**：`core_intersection / event_specific_training_analysis / not_applicable / no_specific_service` 正确；这是训练/增强分析，不是推理服务。 |
| **ICLR2024-1097** | ICLR PDF Abstract/Sec.1；方法和实验章节，5 个 event-based action datasets，point-based SNN 直接接收稀疏 event cloud，16 timesteps。 | **确认** | **确认**（end-to-end point SNN） | **确认无需修改**：`method_coupled / task_network` 与 `asynchronous_event_processing;sparsity_and_efficiency;low_latency;feature_representation` 均由直接 event-cloud action inference 支持。 |
| **ICML2024-0876** | PMLR PDF 实验章节 CIFAR10-DVS 与静态数据；NDOT 是 neuronal-dynamics online training。 | **确认**（CIFAR10-DVS，benchmark） | **确认** | **确认无需修改**：`core_intersection / benchmark_only / not_applicable / no_specific_service`；贡献是训练而非新 event-vision inference function。 |
| **ICLR2024-0272** | ICLR PDF Sec.4–5；DVS-CIFAR10 对比表（TAB/TEBN 等）；方法是 temporal accumulated batch normalization。 | **确认**（DVS-CIFAR10，benchmark） | **确认** | **确认无需修改**：当前 benchmark-only 与 N/A service 已准确表达通用 SNN training contribution。 |
| **ICCV2025-1894** | ICCV 官方页面/补充 A.2；CIFAR10-DVS（DVS 捕获）与 N-Caltech101 等数据；SpiLiFormer 是 lateral-inhibition Spiking Transformer。 | **确认**（DVS benchmark） | **确认** | **建议修改**：保持 `core_intersection / benchmark_only`，改 `provisional_snn_role=not_applicable`、`snn_service_function=no_specific_service`；不要把通用 lateral inhibition 的 sparsity/feature 属性写成 event-specific service。 |
| **NeurIPS2025-5334** | NeurIPS PDF Abstract/Introduction；Datasets/Experiments；STEP 明确支持 static、event-based、sequential 数据、DVS-CIFAR10/N-Caltech101 loaders，并评测神经元、编码和 temporal modeling。 | **确认**（平台 benchmark 支持） | **确认**（评测对象为 Spiking Transformers） | **确认无需修改**：平台是 benchmark/evaluation infrastructure，不承担单一任务网络推理；`core_intersection / benchmark_only / not_applicable / no_specific_service` 合理。 |
| **ECCV2024-0903** | ECCV PDF Abstract/Introduction；事件数据转换为 image-like representation，攻击通过 immutable/mutable simulated event-spike triggers；全文未建立 SNN 模型或脉冲神经元计算。 | **确认**（event-camera axis） | **否**；“event-spike”是攻击触发数据，不是 SNN computation | **确认无需修改**：`event_camera_only / single_axis / not_applicable / no_specific_service` 正确；这是 spike-camera/attack 边界，不能因 “spike trigger” 改成 core intersection。 |

## 需要修改的 CSV 行（建议清单）

以下只列本轮有证据支持的字段变更；未列字段保持原值：

| paper_id | 建议修改 |
|---|---|
| ICML2024-1996 | `scope uncertain → event_camera_only`; `intersection_directness uncertain → single_axis`; `provisional_snn_role unknown → not_applicable`; `snn_service_function unknown → no_specific_service`; 更新 pipeline/task。 |
| NeurIPS2024-0783 | `scope uncertain → core_intersection`; `intersection_directness uncertain → benchmark_only`; `provisional_snn_role unknown → not_applicable`; `snn_service_function unknown → no_specific_service`; 更新 pipeline/task。 |
| CVPR2026-3426 | 同上（DVS Gesture benchmark）；更新 pipeline/task。 |
| ICML2025-2800 | 同上（N-Omniglot/DVS benchmark）；更新 pipeline/task。 |
| CVPR2026-0405 | 同上（DVS-CIFAR10 benchmark）；更新 pipeline/task。 |
| CVPR2026-3630 | pipeline 删除 “adaptive slicing”，改为 GTP event-image/prompt aggregation；建议从 service 移除 `asynchronous_event_processing`。 |
| CVPR2024-0028 | `intersection_directness method_coupled → benchmark_only`; `provisional_snn_role task_network → not_applicable`; `snn_service_function async;event_selection → no_specific_service`; pipeline 标注 DTSNN 为 baseline。 |
| ECCV2024-1740 | `intersection_directness method_coupled → event_specific_training_analysis`。 |
| ICLR2026-3011 | `provisional_snn_role task_network → not_applicable`; `snn_service_function sparsity_and_efficiency;memory_or_state_modeling → no_specific_service`。 |
| ICLR2026-1286 | `intersection_directness method_coupled → event_specific_training_analysis`; pipeline 明确为 retiming attack/analysis。 |
| ICCV2025-1894 | `provisional_snn_role task_network → not_applicable`; `snn_service_function sparsity_and_efficiency;feature_representation → no_specific_service`。 |

## 确认无需修改

NeurIPS2024-1436、NeurIPS2024-2388、ECCV2024-0537、ECCV2024-1778、ICLR2024-0249、ICML2024-0876、ICLR2024-0272、ICLR2024-1097、NeurIPS2025-5334、ECCV2024-0903，共 **10 篇**。它们的当前 scope/directness/role/service 能由全文直接支持。

## uncertain/unknown 与 Astra 裁决项

- 本轮 21 篇在科学证据层面均已解析，**没有论文因摘要或 PDF 证据不足而必须继续保留 `uncertain/unknown`**。
- 建议交由 Astra 统一裁决的标签边界有三项：
  1. raw-event attack（ECCV2024-1740）和 spike-retiming attack（ICLR2026-1286）是否统一采用 `event_specific_training_analysis`，还是新增/映射到更一般的 robustness-analysis 规则；本报告采用现有 codebook 中最接近的合法值。
  2. LED（CVPR2024-0028）的 DTSNN 是 baseline 而非主方法，是否按 `benchmark_only` 处理；本报告建议如此，避免把硬件/数据集/主 ANN 方法贡献误计为 SNN inference role。
  3. 对 SAFA-SNN、SpiLiFormer、TRE、TDA-SNN、Shortcut、FSL-SNN 等“通用 SNN + DVS benchmark”论文，是否统一把 role/service 设为 N/A/no-specific-service；本报告按 protocol 的“cross-system inference role”定义统一建议。

## 边界类别汇总

- **benchmark-only**：NeurIPS2024-0783、CVPR2026-3426、ICML2025-2800、CVPR2026-0405、ICLR2026-3011、ICML2024-0876、ICLR2024-0272、ICCV2025-1894；以及 LED 的 DTSNN baseline（CVPR2024-0028）。
- **event_specific_training_analysis**：ICLR2024-0249（增强/训练）、ECCV2024-1740（raw-event attack）、ICLR2026-1286（retiming attack）。
- **event_interface**：NeurIPS2024-2388（SNN 直接触发 adaptive slicing）。
- **algorithmic_engine**：NeurIPS2024-1436（WTA E-step + STDP M-step 显式映射）。
- **spike-camera**：ECCV2024-0903 的 simulated event-spike trigger 只是攻击数据，不构成 SNN computation。
- **训练/攻击/硬件贡献误归推理 role**：CVPR2024-0028、ECCV2024-1740、ICLR2026-1286、ICLR2024-0249，以及泛 benchmark 论文中的 task_network 赋值，已在建议中单列。

## PDF 访问失败

- **科学证据不可用：0 篇。**
- `NeurIPS2024-1436`：官方 PDF 直接读取触发单文件大小限制（约 12 MB）；官方索引文本覆盖所需章节，因此结论仍为 confirmed。
- 其余 20 篇均通过官方 PDF/HTML 全文或官方索引文本完成边界证据核查。命令行下载失败是环境 DNS/超时问题，不改变论文可核查性。

## 完成状态

- 实际核查：**21 篇**（pdf-trigger 5 + B005–B007 High 16，去重后仍为 21）。
- 建议修改：**11 篇**；确认无需修改：**10 篇**。
- 仍 uncertain：**0 篇**（争议项见上）。
- 仅新增本报告文件；未修改 census、protocol、validator、membership 或 codebook。
