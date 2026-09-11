# Taxonomy 中期综合报告

## 范围与证据等级

本报告只分析 `00-index/taxonomy-census.csv`、批次 manifest、census protocol、validator 及既有 checkpoint/adjudication 文件；不扩展纳入范围，不修改 CSV、schema、protocol、codebook 或 membership，也不进行逐篇深读。当前 census 有 228 条、11 列，覆盖 B001–B004。文中“数据直接支持”指可由现有记录计数或字段内容直接复核的结论；“基于数据的推断”指对 taxonomy 设计的解释；“仍需验证”指不能由摘要级 census 决定的事项。

## 1. 11 个字段的中期判断

| 字段 | 判断 | 理由与建议 |
|---|---|---|
| `scope` | 保留 | 是语料边界主字段，直接区分双轴、单轴、范围外和不确定。不能与任务字段合并。 |
| `intersection_directness` | 保留 | 补充交叉深度，尤其区分方法耦合、事件特定训练/分析和 benchmark-only；与 scope 互补。后续应检查 `benchmark_only` 是否把“同一实验使用 DVS”与真正方法耦合清楚分开。 |
| `contribution_type` | 保留，作为贡献轴 | 覆盖 architecture/inference、representation、neuron/dynamics、training/conversion、robustness、hardware、dataset/theory。枚举仍偏粗，`inference_method` 过宽；本轮不改 schema，后续只观察是否需要在正式 taxonomy 中拆出 architecture 与 inference。 |
| `pipeline_position` | 保留，但定位为证据/中间表示 | 它描述输入—处理—SNN—输出链路，比四个 role 更少预设。当前是开放短文本，重复率低；不适合直接作统计主轴，需后续从文本归纳稳定簇。 |
| `provisional_snn_role` | 保留为候选角色字段 | 适合表达 event interface、task network、embedded module、algorithmic engine，但当前 209/228 为 `not_applicable`（含大量单轴/范围外记录），不能据此判断 role 轴失败。应在 core 子集内评估；`not_applicable` 与 `unknown` 必须继续区分。 |
| `snn_service_function` | 保留，作为能力/服务轴 | 与 role 不同：role 是“在哪里”，service 是“提供什么”。但 `no_specific_service` 达 206/228，说明摘要常未明确服务，或该枚举在非 core 记录中被机械填充。后续须优先检查 core 记录和“训练/硬件贡献但无新增推理服务”的边界。 |
| `task_application` | 保留为索引/分层变量 | 便于检查跨任务泛化和避免漏读，但不应成为综述主 taxonomy，防止退化为普通任务综述。 |
| `cross_cutting_topics` | 保留，作为横向比较轴 | 训练、转换、效率、硬件、鲁棒性、数据集、时序等跨越角色和服务。与 contribution_type 有语义相邻项（如 training、hardware），但前者回答“贡献是什么”，后者回答“贯穿哪些分析主题”，不宜合并。需防止同一论文在两列被重复计数。 |
| `abstract_basis` | 保留 | 是摘要级结论的证据链，支持审计和后续抽样，不是 taxonomy 类别。 |
| `pdf_trigger_question` | 保留 | 将不确定性转成定向深读队列；`none` 不是缺失。后续只对边界/anchor 论文使用。 |
| `paper_id` | 保留 | 唯一连接键，非科学维度，但不可删除。 |

关键缺失维度是“事件交互机制/耦合方式”：SNN 是否直接接收事件、事件如何编码/聚合、SNN 与非脉冲模块如何协同、是否真正利用异步性。这些内容目前分散在 `pipeline_position`、`provisional_snn_role` 和 `snn_service_function`，尚未形成稳定的独立轴。当前约束下不新增字段；可在正式章节中由三轴组合推导，并在后续 B005–B007 观察是否反复出现。

## 2. 三个重点轴的关系

三轴应作为并列但有层级的维度，而不是合并：

1. **Pipeline position（位置）**：SNN 在事件视觉系统的哪一段——event interface、task network、embedded module、algorithmic engine，或尚未归入候选角色。
2. **SNN service function（服务）**：SNN 为系统提供何种能力——temporal modeling、asynchronous processing、feature representation、sparsity/efficiency、memory/state、low latency、robustness、hardware compatibility 等。
3. **Contribution type（贡献）**：论文主要改变了什么——architecture/inference、neuron/dynamics、training/conversion、representation、robustness、hardware、dataset/theory 等。

推荐关系是“**位置作主轴，服务作解释层，贡献作方法学横轴**”。原因是位置最接近“如何把 SNN 放进 event-camera pipeline”这一核心问题；服务描述其作用机制；贡献说明创新落点。把位置与服务合并会把“task network 用于 temporal modeling”和“event interface 用于 asynchronous processing”混成同一层，丢失可解释性。把贡献与服务合并则会把 training/conversion 等实现手段误当成能力本身。

## 3. 三种可行 taxonomy architecture

### A. Pipeline 角色主轴（推荐候选）

- 一级：Event interface；Task network；Embedded module；Algorithmic engine；Cross-role systems。
- 二级：按 service function 分（时序/异步、表示、聚合/选择、状态记忆、稀疏效率、低延迟、鲁棒性、硬件协同）。
- 覆盖：24 条 core 中已有 `event_interface`、`task_network`，以及未来可能识别的嵌入式 SNN、脉冲求解器；也能容纳 benchmark-only 作为外围证据。
- 优点：直接回答 SNN 在 pipeline 中的位置，能跨任务组织论文；与 `pipeline_position` 有天然证据链。
- 缺点：当前 role 对 209 条非 core 记录必然为 N/A；`embedded_module`、`algorithmic_engine` 证据量尚未显现。
- 重复归类：中等；一篇论文可能既是 event interface 又是 task network，需要主 role + secondary role 规则。
- 综述适配：高，适合主体章节。

### B. 服务功能/能力主轴

- 一级：Temporal/asynchronous modeling；Event representation and selection；State/memory；Efficiency/latency；Feature learning；Robustness/hardware。
- 二级：按 contribution_type 和 pipeline role 细分。
- 覆盖：适合描述明确声称利用时序、异步、状态、稀疏或硬件优势的 core 论文；也可吸收跨任务方法。
- 优点：更接近“为什么使用 SNN”，便于比较能力与代价。
- 缺点：现有 206 条 `no_specific_service`，摘要证据不足；不同位置的同一服务容易混在一起。
- 重复归类：高，一篇论文常同时声称 temporal、representation、efficiency。
- 综述适配：中高，适合作为 A 的二级或横向章节，不宜单独作唯一主轴。

### C. 交叉耦合机制主轴

- 一级：Direct event-to-spike coupling；Event-conditioned SNN task processing；Hybrid event/SNN modules；SNN with event-specific training or conversion；Benchmark co-occurrence。
- 二级：按耦合环节（encoding/aggregation/backbone/decoder/solver）及 contribution_type 细分。
- 覆盖：最适合 24 条 core，尤其 method-coupled 9 条、event-specific training/analysis 1 条和 benchmark-only 14 条的边界比较。
- 优点：最能体现“交叉耦合”而非单纯任务；可明确区分真正 event-camera × SNN 机制与仅共同 benchmark。
- 缺点：对单轴背景论文覆盖弱；耦合级别与 pipeline position 容易重复；需要更强全文证据。
- 重复归类：高，混合系统通常跨多个耦合环节。
- 综述适配：适合做核心专题/边界章节，单独承担全综述主体会丢失大量方法学背景。

## 4. 推荐最终方案

推荐 **A 为主 taxonomy，B 为能力横向层，C 为交叉耦合专题与边界分析**。A 比 B 更稳定，因为“位置”在摘要中通常可从输入—模块—输出链路识别，而服务标签在当前数据中过度缺失；A 比 C 更可扩展，因为 C 对仅 benchmark 共现和单轴背景的组织能力有限。

具体写法：主体章节按 event interface、task network、embedded module、algorithmic engine（若后续证据足够）组织；每章内部用 service function 比较 temporal/asynchronous、representation、state/memory、efficiency/latency、robustness、hardware；贡献类型放入统一比较表，标出 architecture、neuron/dynamics、training/conversion、representation、robustness、hardware 等。C 用一张耦合矩阵或专题章节呈现“事件如何进入 SNN、SNN 如何回馈事件处理、哪些只是 benchmark-only”。

多类别规则建议：每篇论文指定一个**主 pipeline role**（决定主体章节），允许 0–2 个 secondary role；service function 与 contribution_type 均可多选；benchmark-only 不强行赋予推理 role；任务只作为分层/索引。这样既承认真实多重归属，又避免章节复制全文。最终角色规则仍是 provisional，须待全库和 High 核查后冻结。

为避免退化成按任务分类，任务名称不做一级标题；所有任务只作为章节内的应用标签，比较同一 role/service 在分类、检测、跟踪、重建、控制等任务上的迁移。

## 5. 数据质量检查

### 直接支持的结论

- 228 条中：`core_intersection` 24、`event_camera_only` 79、`snn_only` 47、`out_of_scope` 76、`uncertain` 2。
- `intersection_directness`：method-coupled 9、event-specific training/analysis 1、benchmark-only 14；这三者合计 24 条 core，组合一致。
- `provisional_snn_role`：task_network 14、event_interface 3、not_applicable 209、unknown 2；当前未出现 embedded_module 或 algorithmic_engine。
- `snn_service_function`：no_specific_service 206；出现较多的是 feature_representation（单独或组合）以及 temporal/asynchronous/memory 等组合；这表明服务标签主要集中在少数 core 论文。
- `contribution_type` 组合很多，最常见含 `inference_method`（单独或组合），其次是 event_representation、training_or_conversion、dataset_or_benchmark；贡献轴比 role/service 更有分辨率。

### 基于数据的推断

`core_intersection` 的 24 条记录已覆盖多种候选边界：纯 task network（如 NeurIPS2024-0322）、event interface（如 NeurIPS2025-0641、ECCV2024-1168）、跨模态 fully-spiking fusion（NeurIPS2025-4041）、仅训练/转换或鲁棒性而无新增交互服务（ICML2025-2813、CVPR2025-1714、ICLR2026-0897）、以及 benchmark-only（ICLR2025-2158 等）。这些反例说明 role、service、contribution 不能压成一列。

`not_applicable` 的高比例主要由 79+47+76 条非 core 记录构成，不能直接解释为 SNN role 轴无用；但在 core 内仍有若干 `not_applicable`，提示“论文属于交叉语料但 SNN 只承担训练、转换、攻击或硬件功能”的情况需要明确保留。

`no_specific_service` 的高比例一部分来自非 core 记录的合法哨兵值，另一部分可能表示摘要没有声称 SNN-specific service。若 core 内持续出现该值，则服务轴需要采用“未知/未声称”解释，而不能把它当成真实能力类别。

最适合展示候选 taxonomy 边界的论文包括：

- **位置边界**：NeurIPS2025-0641、ECCV2024-1168（event interface）；NeurIPS2024-0322、CVPR2025-0065（task network）；NeurIPS2025-4041（混合/跨模块）。
- **服务边界**：CVPR2026-1873（异步聚合、状态与事件选择同时出现）；NeurIPS2025-0641（时序、异步、状态、表示共现）；CVPR2024-2179（事件选择/聚合与表示）。
- **贡献与服务脱钩**：ICML2025-2813、ICML2025-0181、CVPR2024-2342（训练/转换/硬件贡献，但不一定提供新的 event-specific service）。
- **交叉边界**：ICLR2025-2158（benchmark-only 与硬件兼容）；ICML2025-2762（DVS 与 spiking Transformer 的方法耦合）；CVPR2026-2918（事件流与 fully spiking/branch coupling）。

### 仍需后续验证的问题

- B005–B007 是否会出现 `embedded_module` 或 `algorithmic_engine`，以及这两个候选 role 是否需要保留为正式章节。
- `benchmark_only` 中是否存在摘要未说清、但全文实际有事件特定训练或接口设计的论文。
- `snn_service_function` 的 `no_specific_service` 在 core 子集内究竟是“未声称”还是当前枚举覆盖不足。
- `pipeline_position` 开放文本能否稳定归并为少数机制簇，还是需要全文才能判断。
- contribution_type 中 `inference_method` 是否应在正式 synthesis 中拆成 architecture/backbone、system inference、fusion/decoder 等子类。

## 6. 后续流程建议

1. **B005–B007**：继续使用当前 11 列，保持 schema 和枚举不变；先观察剩余批次是否产生系统性不可表达案例。
2. **是否改 schema**：在剩余批次前不改。只有出现重复、跨多篇且无法由现有字段表达的机制，才进行最小修订并记录影响。
3. **B001–B004 回填**：暂不做大范围回填。可在全库完成后对 core/uncertain 做有限一致性复核，重点是 role/service 与 `pdf_trigger_question`，不改变纳入范围。
4. **PDF 深读**：不做大范围下载。仅对影响 scope、耦合等级、候选 role 或 taxonomy-breaking mechanism 的少量边界论文定向深读。
5. **下一 checkpoint**：建议在 B005–B007 完成并通过 validator、High 完成 core/uncertain 核查和分层抽查后进行；若出现同一不可表达模式反复出现，则提前触发最小 schema 评估 checkpoint。

本报告是中期 synthesis，不宣称 taxonomy 已最终冻结；最终章节结构应等待全库 census、High 核查、边界 PDF 证据和分布聚类完成后再确定。
