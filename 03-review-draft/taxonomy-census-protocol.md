# Taxonomy census protocol

版本：0.3，2026-09-11。状态：以 taxonomy discovery 为唯一目的的标题—摘要普查层。

## 1. 目的与边界

本层回答两个问题：当前 572 篇候选分别属于哪一个大范围，以及这些论文自然呈现出哪些 SNN × event-camera 机制簇。它服务于 taxonomy discovery，不负责最终 taxonomy、最终纳排或逐篇深度证据表。

这里的 `core_intersection` 指综述的核心交叉**语料库**，不是“深度耦合方法”的同义词。只要论文同时具有明确的 SNN 轴和 contrast-change event-camera / DVS 轴，就进入 `core_intersection`；DVS 只作为训练集、测试集或 benchmark 也算交叉。交叉有多深由 `intersection_directness` 单独表达。因此，`snn_only` 只用于当前可见证据中没有 event-camera / DVS 关系的 SNN 论文，`event_camera_only` 反之亦然。

数据源固定为 `00-index/candidate-screening-audit.csv`。其中 572 篇均已有完整官方标题、摘要、摘要哈希和来源页。census 通过 `paper_id` 连接这些信息，不复制 metadata、标题、摘要、来源或哈希，也不修改原 audit。

本层与 codebook 0.2 分开：

- `taxonomy-annotation-codebook.md` 的 59 字段继续作为后续关键论文的深度证据规范；
- census 不执行 codebook 0.2 的 expansion batch，也不把摘要判断冒充全文终审；
- `event_interface`、`task_network`、`embedded_module`、`algorithmic_engine` 只是待检验候选；
- 全库普查与 High 核查完成后，才由 Astra 根据分布和反例提出 provisional taxonomy。

## 2. 文件与所有权

| 文件 | 作用 | 是否编辑 |
| --- | --- | --- |
| `00-index/candidate-screening-audit.csv` | 572 篇身份、完整摘要和既有双轨决策 | 本流程只读 |
| `00-index/taxonomy-census-batches.csv` | 每个 `paper_id` 的确定性批次与批内顺序 | 固定 manifest，不手改 |
| `00-index/taxonomy-census.csv` | 轻量 census 结果 | Mid 初填，High 定向修订 |
| `scripts/validate_taxonomy_census.py` | validator，并提供不显示旧决策的 batch view | 维护脚本 |

`taxonomy-census.csv` 保留 11 列：1 个连接字段、9 个 taxonomy 科学字段和 1 个 PDF 问题字段。已删除 annotator、review_status、review_note、confidence、emergent_code、taxonomy_use，因为它们不直接参与 taxonomy 构建。

## 3. Taxonomy 字段

| 字段 | 类型 | 填写规则 |
| --- | --- | --- |
| `scope` | 单选 | `core_intersection` = 两轴均存在（包括仅用 DVS benchmark）；`event_camera_only` / `snn_only` = 只有一轴；`out_of_scope` = 两轴均无；证据不足才用 `uncertain` |
| `intersection_directness` | 单选 | 在 scope 之外记录交叉深度：`method_coupled`、`event_specific_training_analysis`、`benchmark_only`、`single_axis`、`neither_axis`、`uncertain` |
| `contribution_type` | 有序多选 | 记录摘要明确主张的贡献类型，不因论文有实验就标 dataset |
| `pipeline_position` | 开放短文本 | 用一条短链描述输入 → 关键处理 → SNN/连续组件 → 输出；不适用时填 `not_applicable` |
| `provisional_snn_role` | 有序多选 | 四个既有 role 只是候选；允许 `other_candidate`、`unknown` 或 `not_applicable` |
| `snn_service_function` | 有序多选 | 记录 SNN 为事件视觉提供的功能：时序、异步处理、事件选择/聚合、稀疏效率、低延迟、状态记忆、表示、鲁棒性、硬件或算法推断 |
| `task_application` | 开放短文本 | 使用摘要中的实际任务；不适用或不明时用 `not_applicable` / `unknown` |
| `cross_cutting_topics` | 有序多选 | 训练、转换、增广、鲁棒性、效率、硬件、数据集等正交主题 |
| `abstract_basis` | 开放短文本 | 一至两句忠实转述摘要中支持 scope、贡献与候选作用的内容，不引用旧 survey/advisor 决策 |
| `pdf_trigger_question` | 开放文本 | 没有必要则 `none`；否则只写一个摘要无法回答且会影响 scope、机制簇或 taxonomy 边界的具体问题 |

多选字段以分号连接，去重并按下列顺序填写：

- `contribution_type`：`inference_method;event_representation;neuron_or_dynamics;training_or_conversion;analysis_or_robustness;dataset_or_benchmark;hardware_or_deployment;survey_or_theory;other;uncertain`
- `provisional_snn_role`：`event_interface;task_network;embedded_module;algorithmic_engine;other_candidate;not_applicable;unknown`
- `cross_cutting_topics`：`training;conversion;augmentation;robustness_or_attack;efficiency;hardware_or_deployment;dataset_or_evaluation;temporal_modeling;representation_learning;generalization;none;other`
`uncertain`、`unknown`、`none` 和 `not_applicable` 是各字段的独占哨兵值，不能与同字段的实质标签并列。

## 4. 字段关系

`scope` 与 `intersection_directness` 先确定语料库边界。`contribution_type` 说明贡献维度，`pipeline_position` 说明系统位置，`provisional_snn_role` 说明 SNN 功能角色，`task_application` 说明任务，`cross_cutting_topics` 记录跨角色主题；`abstract_basis` 保存证据，`pdf_trigger_question` 负责后续定向核查。这些字段互补，不互相替代。

## 5. 摘要级判断顺序

1. 只从 batch view 阅读完整标题和摘要，不先查看旧 survey/advisor role、reason 或 membership。
2. 确认是否为 contrast-change event camera；普通“event”、事件日志、物理 rare event、spike camera 不能自动进入 event 轴。
3. 确认摘要是否声称真实 SNN / spiking-neuron computation；稀疏、异步、二值或 threshold 不能自动进入 SNN 轴。
4. 先按两轴是否存在判断 scope，再判断两轴是方法耦合、事件特定训练/分析、仅 benchmark 共现、单轴还是都不是。只要两轴均存在，scope 就是 `core_intersection`；不能用“耦合不够深”把 benchmark-only 论文降为 `snn_only`。
5. 用开放的 pipeline 和 emergent code 先描述论文，再给 provisional role。不要从旧四 role 倒推描述。
6. 摘要不能回答 taxonomy 关键边界时保留 `uncertain`/`unknown` 并提出一个具体 PDF 问题，不猜测补全。

scope 与 directness 的合法组合为：

- `core_intersection` → `method_coupled`、`event_specific_training_analysis`、`benchmark_only`，少数深度暂不能判断时可用 `uncertain`；
- `event_camera_only` / `snn_only` → `single_axis`；
- `out_of_scope` → `neither_axis`；
- `uncertain` → `uncertain`。

`provisional_snn_role` 描述 SNN 在交叉系统推理路径中的功能，因此只对 `core_intersection` 使用四个 role。单轴和范围外论文填 `not_applicable`；核心论文若只贡献训练、评测或硬件而没有新增推理功能，也可填 `not_applicable`。`algorithmic_engine` 保留给把优化变量、迭代状态或求解步骤显式映射到 spikes / neuronal states 的算法求解器，不能泛指新的神经元、训练方法或一般 SNN 架构。

`scripts/validate_taxonomy_census.py --show-batch B001` 输出的只读 JSONL view 只含身份、完整摘要和官方页面，不暴露旧双轨决策。它是 Mid 的推荐入口。

## 6. 批次与模型职责

manifest 将 572 篇分成 7 批：已完成的 B001–B004 保持历史批次，剩余 344 篇分为 B005=115、B006=115、B007=114。批次大小是执行安排，不是科学限制。

### Sol Mid

- 逐篇完整阅读当前 batch 的 title/abstract；
- 只填本表，不读 PDF，不填 59 字段，不改 source audit；
- 一个 batch 全部完成并通过 validator 后停止；
- 缺身份、摘要或哈希时不修 source，报告阻塞；
- 不合并 open codes，不发布 taxonomy，不做最终纳排。

Batch 001 通过 High 核查后，Mid 可依次完成其余批次。每批独立校验；不需要每批交 Astra。

### Sol High

Batch 001 核查全部 `core_intersection` / `uncertain`，并从其他 scope 分层抽查约 10%。全库完成后核查全部 `core_intersection` / `uncertain`，再对其余 scope 分层抽查。默认仍只使用 title/abstract；只有 scope 无法解决或可能出现 taxonomy-breaking mechanism 时才定向读取 PDF。

High 可以修正记录并说明重复错误模式，不能为了个案扩充 schema 或静默创建正式 taxonomy label。需要 Astra 判断的新机制标为 `high_escalated`。

### Astra

Astra 不参与逐 batch 摘要标注，也不在 Batch 001 后重审 codebook。572 篇 census 和 High 核查完成后，Astra读取分布、共现、open-code clusters、反例和 PDF 队列，形成 provisional taxonomy。现有四 role 可以保留、重组、降级或在证据支持下修订。

## 7. 停止条件与后续升级

Mid 当前 batch 的停止条件：manifest 中每个 ID 恰有一条记录，11 个字段均非空，枚举与哨兵规则通过。不要为了消除 `uncertain` 而读 PDF。

Batch 001 High 核查通过的条件：没有反复出现的轴误判或强迫 role；若只是措辞和少量个案修正，记录模式后允许继续全库。若 schema 本身无法表达多篇论文，暂停剩余批次，交当前 Sol High 做一次最小修订，不直接交 Astra。

全库 census 的停止条件：572 个 source IDs 各有一条记录，全部批次通过，High 已核查 core/uncertain 并完成分层抽查。此时输出聚类和 PDF 队列，交 Astra synthesis。

论文只有在 Astra provisional taxonomy 后被提升为 anchor、边界证据或关键代表时，才进入模块化全文抽取。codebook 0.2 的相关字段按论文用途启用，不要求无关背景论文填满 59 列。

## 8. 命令

```bash
# 检查 manifest、空表/当前结果和已完成行
python3 scripts/validate_taxonomy_census.py

# 查看不带旧决策的 Batch 001 title/abstract JSONL
python3 scripts/validate_taxonomy_census.py --show-batch B001

# 要求 Batch 001 的全部记录完成
python3 scripts/validate_taxonomy_census.py --require-batch B001

# 全库结束时要求 572 篇全部完成
python3 scripts/validate_taxonomy_census.py --require-all
```
