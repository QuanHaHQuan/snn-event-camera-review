# Taxonomy architecture memo

日期：2026-09-10。状态：**design v0.1，等待用户确认；不是最终 taxonomy**。

本轮角色为 Taxonomy Architect，按用户要求采用 Astra High 的高层设计职责。只设计新 annotation 工作流；不执行 pilot，不批量重标，不修改任何既有 Survey/Advisor membership、V2、outline、生成视图或语义源。后续模型由用户在交接时选择，不把文档中的模型名称当成已经执行过的调用记录。

## 1. 当前 checkout、证据与研究边界

当前目录与 `git rev-parse --show-toplevel` 都是 `/Users/haoquanchen/Documents/Codex/2026-07-01/i-want-to-build-a-reusable/snn-event-camera-review`。开始时为 20 个 tracked modified 和 4 个 untracked 文件；用户列出的四个近期文件均存在。旧修改主要涉及状态同步、SECNet-SNN Advisor 重选及相应生成器/视图，必须原样保留。

读取入口是用户指定的 README、索引说明、两个 workflow、scripts README、两个近期日志、Survey reading plan、V2 索引、旧 outline/closure/roadmap，以及五个 CSV。CSV 全文件解析、关联与计数不同于逐篇完成新语义标注；本轮只对 pilot 选择所需的候选读取完整标题和完整存储官方摘要，并以旧 V2/graph 边界记录作回查入口。未把旧 role 或旧 PDF 状态复制成新 annotation。

| 数据源 | 本轮只读核验 | 对新工作的含义 |
| --- | --- | --- |
| candidate audit | 572 个唯一 paper ID；2024/2025/2026 分别 199/226/147；全部 abstract_reviewed=yes；572 个存储摘要 SHA256 均匹配 | 全量遍历基线，不缩到 active；本轮未重新联网认证 572 个摘要 |
| active selection | 298；与 audit 的 active 集合一致；另 274 inactive | active 是双轨并集，不是新 usable corpus |
| 旧 Survey roles | 15 anchor、4 included、266 background、287 exclude | 仅是旧分布，不支持断言只有 19 篇真实交叉论文 |
| Survey Core | 26 = 15 anchor + 2 included + 9 background | 深读种子，不能当作最终分类训练答案 |
| Survey reference pool | 259 = 257 background + 2 included；与 audit reference 集合一致 | 与 Core 合计旧 Survey 保留 285；active 中另有 13 篇 Survey exclude |
| V2 | canonical 文件 29；Survey complete 16/26、missing 10 | 阅读进度不是新 codebook 完成率 |
| 当前 Advisor | proceedings 6 required + 2 helpful；另 SECNet focus；与 Survey 重叠 4 篇 | 独立实施工作流，本轮不改变 |
| literature graph | 84 nodes、72 edges；65 nodes 标为不在当前 corpus；25 条 classic candidates | 有回溯入口，但节点不自动等于 usable paper；旧 edge 的 track 是历史 provenance |
| 旧 PDF 状态 | 572 个 needs_pdf_check=no；12 checked_conference_pdf、2 official_abstract_resolved、558 not_needed | 旧筛选足够，不代表 neuron/边界/能耗等细节已核查 |

572 篇仅覆盖六个会议且集中于 2024–2026：CVPR 184、ICLR 114、ICCV 46、ICML 64、NeurIPS 117、ECCV 47。期刊、较早方法、机器人/神经形态会议的缺口是结构性的。298 篇也明显包含大量单轴背景。当前距离约 150–180 篇有论证用途的集合，缺少新 scope 复审、逐字段证据、跨版本去重、经典交叉方法回溯和跨任务公平比较。

用户本轮明确要求将来补充期刊、经典会议等，因此后续检索设计不沿用旧 proceedings allowlist 限制；这不授权本轮重写 intake 文件或给旧 audit 加行。新 annotation 是待确认的独立证据层，不能被旧 generator 当作语义源读取。

## 2. 参考综述：正文、图表与篇幅

参考文件：`/Users/haoquanchen/Downloads/A Comprehensive Survey on Event Camera Representation Learning.pdf`。已抽取全部 20 页正文及 bibliography，并渲染检查 pp.1–15 的版面。首页可见标题为 *A Comprehensive Survey on Event Camera Representation Learning*，arXiv 标记为 2606.23078v2 / 20 Aug 2026。PDF metadata title 却为 *A Systematic Survey on Event Camera Representation Learning*；记录这一差异，不据 metadata 改写用户给出的标题。页眉的 JOURNAL OF LATEX CLASS FILES 是模板文字，不是发表刊名。SHA256：`f59d5c39110a65c7e7eaa469a90dcdec33c7ba8c36f39339f75bb86ab6158de7`。

### 2.1 实际组织而非只看目录

- pp.1–4 的 Introduction 已展开传感器事件方程、表示空间和 taxonomy 定义；“背景”并不是整个 Introduction。Fig.1 解释 sensing，Fig.2 用同一 STOP 场景对照不同表示，Fig.3 在 p.3 给分类总图并标注 IV-A 到 VI-B 的正文入口。
- 主分类先 single/multi representation，再对 single 按 principal feature extractor 实际接收的结构分 dense/sparse；叶子是 event frame、time surface、binary map、voxel、learned dense，以及 token、graph、point；multi 分 dense–dense/dense–sparse。除根节点外最深三层，图中叶子直接对应小节，不再把任务或网络嵌成下级。
- 正文 IV（p.5 至 p.8 上部）逐项解释 dense；V（p.8 中部至 p.11 上部）解释 sparse；VI（p.11）解释 multi。典型小节遵循“对象及数学定义 → 关键设计变量 → 代表方法的演变与差异 → 能力与代价”的逻辑。
- 必须注意其定义的实际约束：III/IV-E 在 pp.3、7–8 把 learned dense 限为 principal feature extractor 之前可学习的 event-to-grid mapping，普通隐藏特征不算；V-A 在 pp.8–9 把 token 限为 raw-event/group token，dense patch token 不自动算独立表示；V-B 在 pp.9–10 允许 voxel-derived nodes 仍属于 graph，因为后续计算对象是节点/边。这些是值得借鉴的操作性边界。
- Fig.4（p.5）合并展示三种 map，Fig.5–9（pp.7–10）分别展开 voxel、learned dense、token、graph、point：图强调输入、构造、backbone、head 的共同接口。Fig.10（p.11）连接 VII 的 adaptive optimization 与 fidelity/efficiency 讨论，而非增加另一套互斥类别。
- VIII（p.12）引出 Table I（pp.13–15）：按 task → dataset 分组，组内按 representation，列为 method/representation/metric/performance。不是按 taxonomy 章节复制论文列表，也不是新的 task taxonomy。正文明确指出 backbone、modality、window、training、supervision 等混杂因素，不能视为严格 leaderboard。
- 架构是表示兼容性与方法差异；learning method 是 trainable mapping 或横向优化讨论；task/dataset 在结果轴。特别地，learned dense 同时带有构造是否可学习的属性，仍可能与 voxel 交叠。因此不能直接复制它为本项目的单选 representation 标签。

### 2.2 篇幅口径

20 个物理 PDF 页中，pp.1–12 是正文及图，pp.13–15 是三页汇总表，pp.16–20 是 references（最后一页仅一条，[167]）。参考条目数 167 不等于 167 篇核心方法；作者在 II 称保留超过 150 篇，不能把这一声明当作我们的规模依据。

以下是按双栏版面/图表面积估计的页当量，非精确字数统计。以 **15 页非 bibliography 内容**为分母；跨页浮动图按其功能分配，避免重复计数。

| 功能 | 约页当量 | 比例解释 |
| --- | ---: | --- |
| 标题摘要、动机与范围 | 0.65 | 约 4% |
| 独立 sensor background | 0.45 | 约 3%；不是 Introduction 的全部 |
| Introduction 中 taxonomy 预览、表示定义和总图 | 2.60 | 约 17% |
| II 方法与 III 对既有综述的区分 | 0.75 | 约 5% |
| IV–VI 核心表示 taxonomy 与机制图 | 6.35 | 约 42% |
| VII 优化方向 | 0.80 | 约 5% |
| VIII 与三页结果表 | 3.25 | 约 22% |
| IX 结论 | 0.15 | 约 1% |

总计约 15 页。把前置 taxonomy 也计入核心，核心解释约 9 页、约 60%（合理估计区间 58–62%）；若只数 IV–VI 会低估。若用全部 20 页作分母，核心约 45%，bibliography 物理页占 25%；这不是正文比例。传感器独立背景非常压缩，但与 taxonomy 密切相关的表示定义篇幅不小。

### 2.3 借鉴与不照搬

借鉴固定分类观察位置、同一信号的多表示对照、图和章节一一对应、每类统一问题、机制叙事与任务证据表分离、独立检索方法说明。

不照搬 dense/sparse 作首层：同一个 voxel SNN 可以是 sampler、task network 或 optimization engine；相同 raw-event 外观也不保证 neuronal spikes 或真实异步执行。multi-representation 与 RGB-event multimodality 更不是 ANN-SNN hybrid。避免让 Introduction 重复展开一遍全部定义；新综述只用总览图与范围判定，细节进入核心章节。Table I 的每组最佳高亮不能转为因果“最佳方法”；本项目要增加 timestep、时间窗、输入模态、测量边界与协议一致性。稀疏 point 保留 timestamp 坐标，也不证明物理时间以原分辨率参与神经元更新。

## 3. Scope、证据与选择必须分层

保留用户的四个 scope 值，但重新限定 `boundary_or_exclude` 为“无目标方法交叉、且不是所研究的单轴机制”的范围位置，**不承载冗余或最终删除决定**。关键修订如下：

1. `event_camera_foundation`：真实 event-camera 方法/传感/数据/表示，未构成真实 SNN 交叉。是否 indispensable 由 selection 决定。
2. `snn_foundation`：真实 SNN 的一般 neuron/training/architecture 等方法；event dataset 仅验证一般机制时仍是此类，directness 记 `benchmark_only`。不是因为测试 DVS 就自动归 boundary；否则 CLIF 等机制基础会被错误丢弃。
3. `core_intersection`：事件相机信号与真实 spiking computation 存在明确的方法性联系。包括 event-specific training、攻击/评估研究，但 contribution_focus 必须区分是否提出新的 inference topology。明确 event-to-SNN 系统本身可以是交叉贡献，不强求每篇都发明新 neuron；需要原文给出接口或系统设计而非只列数据集。
4. `boundary_or_exclude`：spike camera、EHR/log、生物 spike、仅有类脑/threshold 修辞、一般异步计算等；generic SNN 仅作为无独立机制的 dataset baseline 也在此。

`unresolved` 是 evidence state；scope 字段用 `unknown` 表示尚不能落入四类，不发明第五研究领域。`reference_only` 是 reading/selection disposition，表示暂不进 usable、但保留检索记录；不是 scope。完全重复的真实交叉论文仍为 core_intersection，selection 可以是 reference_only/redundant_reference；不能改写方法事实以迁就数量。

## 4. Proposed primary taxonomy hypotheses

四种 topology 尚未被证明互斥，更不是 final taxonomy。把候选名称改为功能语义，避免把网络纯度揉入 role：

| 候选 primary role | 判定对象 | 最强反证测试 |
| --- | --- | --- |
| `event_interface` | SNN 的交付物是 event selection/slice/encoding/aggregation，位于主要特征提取器之前 | SpikeSlicer/SDA/EAS 与 FLAME/REDIR：可定位的表示交接点是否真实存在，还是普通 latent feature |
| `task_network` | SNN 构成主要任务特征提取和推理路径 | SDTrack/SpikePoint；连续 head 不会自动把 spiking backbone 降为 module；混合多尺度 backbone 的“主要”能否证据化 |
| `embedded_module` | SNN 承担局部 feature、memory、attention、fusion、routing 或 head，主要系统由其他计算完成 | ClearSight/HsVT/FLAME；hybrid 是 boundary，不是这个 role 的必要充分条件 |
| `algorithmic_engine` | spike/state 演化与一个明确推断/优化算法的变量或步骤相对应 | Bayesian EM 与 STLR；仅名字叫 optimization 或训练用 SGD 不能进入 |

原来的 Hybrid Functional Module 改名 embedded_module；主任务 SNN 也可能属于 hybrid pipeline。`SNN as activation` 不另立顶层，以 neuron/state、模块功能及边界标注。

用两种 primary 选择规则做反证：默认以论文**主要机制贡献**所作用的 SNN 功能作 primary；同时记录全部真实 secondary roles 与系统位置。若核心论证在 spike sampler，则 downstream SNN backbone 不是自动 primary；若主要贡献是任务网络，普通首层编码不是独立 role。algorithmic_engine 只有显式算法对应且是主要贡献才优先于一般 task network。没有证据能判贡献主次时 primary=unknown，保留两个备选到 issue，不按顺序强行取胜。

training-only 论文不建立第五 inference role。可标 scope=core_intersection，contribution_focus=training_method 和/或 analysis_robustness，primary_functional_role=not_applicable，其被训练/攻击的 SNN backbone 记录在模块/边界字段，taxonomy_placement 指向 cross_cutting。EventRPG、raw-event attack、retiming 会测试这项设计是否足够。conversion 为 training_route；directly trained hybrid 与 converted fully spiking 可以交叉出现。

尚可能遗漏：neuromorphic sensor-compute co-design、closed-loop event control、在线自适应、训练阶段 spike teacher/非 SNN inference、无传统 backbone 的局部可塑性系统。先作为 issue 问题和检索方向，不为猜测增设新 role。

## 5. Secondary comparison axes 与图表用途

以 codebook 为唯一取值来源。保留 scope/directness；把 temporal organization、representation structure、representation learning 分开；把 input provenance 与 modality 分开；将真实 spike existence、模块边界、signal coding 和 training 分开。neuron 与 architecture 分开；physical event time、event-group order、SNN timestep 必须以映射说明连接。

建议待验证的输出：一张 signal-to-computation 总图；四个 role 的等格式局部 pipeline 图；role × representation 证据矩阵；一张以模块为列的 spiking boundary 表；task/dataset/configuration 结果表；efficiency claim/measurement/system boundary 表。一个 paper 可支撑多个表，但只按 canonical work 计一次。没有独立方法证据的空格标 missing evidence，不能宣称研究机会已被证明。

## 6. Selection policy 与篇幅

usable paper 必须有可填写的“支持什么具体论点、与哪个邻近证据不同、删掉它会失去什么”三联理由。inclusion_tier 允许多选：core_taxonomy_evidence、indispensable_background、representative_comparator、evaluation_authority、historical_foundation；另设 redundant_reference、excluded_paper、pending 三个与上述实质 tier 互斥的取值。selection_status 与 tier 分开，纳入建议在 Astra 最终裁剪前为 proposed_usable 或 pending。

先在全部 572 及补充候选上按证据分类，再做 claim-level coverage ledger，最后选择代表集。背景与比较论文需要绑定至少一个交叉论点；同类论文以机制差异、独立验证、首次历史贡献、权威评估协议或关键反例保留，不能只写“重要”。preprint/会议/期刊先建 duplicate_family，同方法无新增证据优先正式完整版本；实质扩展可另保留但说明增量，避免两次计算同一实验。未纳入的记录保留，不删除旧库。

150–180 是预期结果带，不是各 scope 配额。若低于 150，检查遗漏搜索和论证缺口；若高于 180，检查重复与背景膨胀。若检查后仍超范围，提交基于证据的理由，保留不可替代工作。不能为了体面数量给 generic SNN 或 event task 留名额。

建议正文（含机制图和比较表、不含 bibliography）讨论起点为：Introduction/scope/search 6%，两轴基础合计 14%，核心交叉 taxonomy 58%，任务与实证 12%，open problems/conclusion 10%，合计 100%。基础内部暂按 event 6% + SNN 8%，只解释后文必要概念。训练、鲁棒性与部署的交叉证据可进入核心章节，不用泛化背景取代。参考综述约 60% 核心和低背景比值得借鉴，但其约三页结果表的占比不照搬；本主题需要额外解释 spike/time/纯度/训练差异。最终篇幅随论证复杂度调整，不能按论文数线性分配。

## 7. 后续扩展与可证伪验证

检索设计：以全部 572 个 ID 为基线，reference bibliography 的 167 条为一条独立入口；从 26 Core 的 Related Work/正文引用及 bibliography 抽取关键前驱、不同机制 comparator 和任务历史；与 84-node registry、25 classic candidates 合并去重。对关键种子作 backward search；对薄弱 family、期刊版本和较新跟进作必要 forward search。补入 IJCNN、WACV、ICRA/IROS、AAAI/IJCAI 等经典会议与 TNNLS/TIP/TPAMI/RA-L 等期刊时先记录出处与检索日期，不因 venue 放宽证据门槛。此处只规划，不执行扩展。

参考 bibliography 的 [5] 早期 frame-to-event mapping、[24] HALSIE、[72] Spike-FlowNet、[102] hybrid spiking-point pose、[106] Spike-EVPR、[137] motion-SNN 是后续核查入口，不是本轮已确认的新纳入。尤其转换式 event SNN、graph-SNN 真交叉与 depth/flow/pose 历史仍需外部证据。bibliography 对 SpikePoint 使用 2023 preprint，仓库为 ICLR 2024，说明版本规范化必须独立完成。

| 假设 | 验证方法 | 推翻/修订信号 |
| --- | --- | --- |
| 四 role 足够覆盖主要方法 | pilot 记录无法表达的真实 SNN output contract；批次 issue 累积 | 一个新机制无法表达且会改变比较，或多个独立工作反复落 unknown |
| primary 可复现 | Sol High 盲重标最难 10 篇，保留初始判定后由 Astra 裁决 | interface/module 或 engine/task_network 在明确 PDF 后仍重复混淆 |
| role 比 task/architecture 更有解释力 | 控制相同 task/input 比较 SNN 输出、状态位置、训练、代价；再跨 task 比较同 role | 同 role 仅同名无共同机制，或 task 才解释大部分结构差异 |
| event-specific contribution 可区分 DVS-only | 比较 CLIF/STEP、EventRPG/攻击、ABN；要求明确机制桥接句 | 执行者只用 dataset 名或标题来决定 scope |
| 三种 fully spiking 边界可审计 | 逐模块定位 continuous operations 与最终 readout | 缺预处理/融合/head 却推断全管线 fully spiking |
| 时间语义可追溯 | 写 raw event→group→network step 的映射与 reset 策略 | 用 T 同时指物理时长和仿真步而无法拆开 |

冻结 codebook v1.0 只表示规则可执行，不冻结 final taxonomy。pilot 无非法标签/错 ID/空理由；10 篇关键字段盲重标至少 9/10 一致，且同一相邻标签对不得有未解决的系统性混淆；所有剩余 unknown 必须有问题与责任人。主分类、真实 spike 和边界的关键歧义必须由 PDF 解决或正式保留 unresolved，不能为通过率猜测。

最终 taxonomy 收敛需要：572 条逐项完成或有阻塞原因，补充检索来源均记录、去重；所有 central representatives 的核心证据已验证；critical issue=0；最近两个审查批次无未解释的新 role/需重画主图的冲突；最后两轮定向引用追踪没有出现可改变主结构的新机制（有新增但重复的 bibliography 不算失败）；每个大类有至少两个独立 work family，单篇独特机制保留例外框而不强升顶层；按来源/年份/active 状态/任务检查偏差；Astra 能用固定定义解释跨类差异与类内共同点。达到阈值后仍需用户确认最终 taxonomy/outline。

## 8. Astra / Sol 工作流与暂停点

| 阶段 | 执行者 | 具体输入和交付 | 门禁 |
| --- | --- | --- | --- |
| 1 设计（本轮） | Astra High | 本 memo、codebook v0.1、30-paper pilot、header schema、日志 | 用户确认后才进入 2 |
| 2 pilot | Sol High | 逐篇完整 title/abstract；问题导向 PDF；原始标签、证据、冲突和工时 | 只执行 pilot；不改标签字典、不修改旧 membership |
| 3 修订 | Astra High | 冲突矩阵、10 篇盲重标、覆盖失败；发布迁移表并冻结 codebook v1.0 | 必要时补充对照样本；不强宣 pilot 全覆盖 |
| 4 全候选首遍 | Sol Mid | 以 40–50 篇为批次做抽取、明确 case 标注、metadata/CSV 验证与 coverage | 模糊、core mechanism、PDF/数字交 Sol High；第 50 篇先校准 |
| 5 中期 checkpoint | Astra High | 约 150、300、450 条和末批审查；查看 scope/role/unknown/来源分布和退出理由 | 调整规则须 version/migration/recheck；不静默改标签 |
| 6 补充与难例 | Sol High + Sol Mid | High 定向 PDF、难纳排证据与扩展检索判断；Mid 去重、已批准来源抽取、只读验证和确定性产物 | 不同时修改同一工作树；按用户批准路径顺序交接 |
| 7 合成 | Astra High，必要时单次 xhigh | 最终 taxonomy、outline、约 150–180 usable 裁剪、关键反例和篇幅 | 属后续任务，用户确认后另行授权 |

Sol High 的 ambiguity resolution 是查证并应用既有规则；规则本身冲突、未有标签或可改变顶层的问题必须交 Astra。Sol Mid 不依据标题/旧 role 推断、不能为低 confidence 自造标签；所有新机制进入 issue queue。后续新增 annotation/result/issue 文件路径须由用户确认的执行任务明确指定，本轮不创建它们。

主要未解决问题：主要贡献与系统计算主干作为 primary 标准何者更可复现；表征构造与隐藏特征的交接边界；training/攻击论文是否需要独立 evidence chapter；integer training/binary inference 和一体 sensor-chip 的 purity 描述；graph 和转换式真实交叉的覆盖缺口；150–180 是否适合实际可用证据密度。**完成设计后暂停，等待用户确认 codebook，再交 Sol High 执行 pilot。**
