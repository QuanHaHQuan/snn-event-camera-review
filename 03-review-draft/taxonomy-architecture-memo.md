# Taxonomy architecture memo

日期：2026-09-10。状态：**codebook 0.2 有限扩展冻结通过；最终taxonomy未冻结**。E1/E2已完成，G组合家族仍未校准；当前门禁以 [E2 freeze decision](taxonomy-codebook-0.2-freeze-decision.md) 为准，旧checkpoint保留历史。

本memo保留最初参考综述分析与文献扩展设计，并更新为30篇pilot加E1/E2后的高层判断。本次复用Sol High的36条pilot配置、5条E2配置、历史10-case盲重标及E1定向重判，裁决规则、迁移受影响字段，不重做pilot，不批量抽取，不修改Survey/Advisor membership、V2、outline或生成视图。

## 1. 当前 checkout、证据与研究边界

当前目录与 `git rev-parse --show-toplevel` 都是 `/Users/haoquanchen/Documents/Codex/2026-07-01/i-want-to-build-a-reusable/snn-event-camera-review`。最初design阶段曾有20个tracked modified和4个untracked文件，该历史状态已被后续提交收录。**原checkpoint开始时local main工作树干净，HEAD=5078db6；本次E2冻结审查起点仍为干净local main，HEAD=ec707f9**；近期Advisor文件和既有pilot成果均存在，保持不变。

最初设计的读取入口包括README/workflows/索引/历史图；下表保留那次基线说明。本次重新核对candidate=572、active=298、reference=259、Survey Core=26、Survey V2=16/26；主要裁决输入改为用户指定的九份taxonomy设计/pilot/盲重标/事件/schema文件。没有把旧role或旧PDF状态当作新的annotation答案。

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

用户本轮明确要求将来补充期刊、经典会议等，因此后续检索设计不沿用旧 proceedings allowlist 限制；这不授权本轮重写 intake 文件或给旧 audit 加行。新 annotation 是独立证据层，不能被旧 generator 当作语义源读取。

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

## 4. Pilot与E2支持的primary taxonomy：0.2执行结构

以**主要机制贡献中的SNN推理功能**作为核心章节第一层，保留四role；不是用单一物理拓扑覆盖每篇论文。裁决后的核心分布为event_interface 4、task_network 5、embedded_module 3、algorithmic_engine 2，另有3篇cross-cutting，共17篇core。30篇全pilot的task_network=7包含CLIF及RGB SpikeTrack两项foundation，不能混入核心分布。

| 第一层 | 第二层写作组织（非新增enum） | 纳入合同与代表 | 相邻排除 |
| --- | --- | --- | --- |
| event_interface | 边界控制；选择/聚合表示；新neuronal event train编码 | SpikeSlicer；EAS/SDA；FLAME。逐项核查I1输入位置、I2事件组织功能、I3交接内容/接收者、I4独立功能 | 层间binary activation、仅早期feature或task-specific命名不构成判据；不要求跨backbone复用实验 |
| task_network | Event输入主要特征/预测路径；多模态联合主推断 | SpikePoint、ABN、event SpikeTrack、HsVT；SpikeFET。SNN为主要抽取或多阶段混合主路径 | 局部head/支路不是backbone；连续head不自动使其成为embedded |
| embedded_module | 串行局部feature/时间过滤；支路与跨模态条件化 | CVPR2025-2047 PLIF/ASAB、REDIR；ClearSight | hybrid是boundary属性；明确event输入表示构造归interface，多阶段主路归task |
| algorithmic_engine（冻结版保留） | 概率竞争/在线参数推断；固定点/展开latent coding；约束对应求解 | Spike Bayesian的WTA/EM；STLR的SVT/ISTA；Osswald stereo的候选/竞争/视差事件 | 普通SGD、attack optimizer、一般STDP训练、仅算法灵感不合格 |

FLAME由embedded_module改为event_interface：LIF产生新的binary event trains，经timestamp pooling成为E_flat(t)，交给连续EA-HiPPO。代码/训练不可拆卸不否定功能handoff。其representation改为受限的neuronal_spike_train，以区别sensor occupancy binary_map；extent保持hybrid。PLIF-ASAB、REDIR、ClearSight仍是内部任务特征模块。E1定向重判已完成5/5 role与2/2 mlp一致；这是同一执行者的定向稳定性检查，不是新盲测，旧primary 9/10保持原样。

按主要贡献选primary仍优于只按系统主路径：后者会把EAS/SDA按detector变体拆散，也会淹没STLR的求解贡献。独立额外职责记secondary；不能用参数数量、最后一层、名称或固定engine优先级决定。证据无法判断主次时unknown+issue。

algorithmic_engine经E2 stereo的第三种独立机制校准，在0.2正式保留为primary；其变量/更新/解的合同比“optimization-inspired”更严格。不把训练算法改名为推理角色。未来若明确PDF仍反复无法稳定区分，必须重开Astra版本审查并迁移受影响记录，不能由Sol随意降级。D无独立第二个SNN任务网络，secondary由task_network改none；STLR的独立decoder保留secondary。

**独立cross-cutting章节成立：** EventRPG、raw-event attack和input-grid retiming均为core，primary=not_applicable；以训练/增广、时间信用分配、安全/泛化组织，不能把victim classifier当新role。conversion始终是training_route；event-specific但无新推理功能的conversion放cross-cutting，generic conversion放foundation。

主图的外围是定向event/SNN foundations、dataset/benchmark authority、non-SNN comparators，以及横跨roles的hardware/evaluation evidence。它们用支持/比较边连接主图，不作为第五至第八个角色。真正sensor-chip共同设计如构成event-SNN方法，按推理功能归role、以hardware_system与测量边界补注。

完整各分支的输入/输出、邻界、pilot ID和证据位置见 [checkpoint §4](taxonomy-checkpoint-adjudication.md#4-可执行的核心章节树)。二级标题仍是写作结构，不能作为Sol擅自添加的schema标签。

## 5. Secondary comparison axes 与图表用途

以 codebook 为唯一取值来源。保留 scope/directness；把 temporal organization、representation structure、representation learning 分开；把 input provenance 与 modality 分开；将真实 spike existence、模块边界、signal coding 和 training 分开。neuron 与 architecture 分开；physical event time、event-group order、SNN timestep 必须以映射说明连接。

建议待验证的输出：一张 signal-to-computation 总图；四个 role 的等格式局部 pipeline 图；role × representation 证据矩阵；一张以模块为列的 spiking boundary 表；task/dataset/configuration 结果表；efficiency claim/measurement/system boundary 表。一个 paper 可支撑多个表，但只按 canonical work 计一次。没有独立方法证据的空格标 missing evidence，不能宣称研究机会已被证明。

## 6. Selection policy 与篇幅

usable paper 必须有可填写的“支持什么具体论点、与哪个邻近证据不同、删掉它会失去什么”三联理由。inclusion_tier 允许多选：core_taxonomy_evidence、indispensable_background、representative_comparator、evaluation_authority、historical_foundation；另设 redundant_reference、excluded_paper、pending 三个与上述实质 tier 互斥的取值。selection_status 与 tier 分开，纳入建议在 Astra 最终裁剪前为 proposed_usable 或 pending。

先在全部 572 及补充候选上按证据分类，再做 claim-level coverage ledger，最后选择代表集。背景与比较论文需要绑定至少一个交叉论点；同类论文以机制差异、独立验证、首次历史贡献、权威评估协议或关键反例保留，不能只写“重要”。preprint/会议/期刊先建 duplicate_family，同方法无新增证据优先正式完整版本；实质扩展可另保留但说明增量，避免两次计算同一实验。未纳入的记录保留，不删除旧库。

150–180 是预期结果带，不是各 scope 配额。若低于 150，检查遗漏搜索和论证缺口；若高于 180，检查重复与背景膨胀。若检查后仍超范围，提交基于证据的理由，保留不可替代工作。不能为了体面数量给 generic SNN 或 event task 留名额。

建议正文（含机制图和比较表、不含 bibliography）讨论起点为：Introduction/scope/search 6%，两轴基础合计 14%，核心交叉 58%（暂按推理role约46% + cross-cutting约12%），任务与实证 12%，open problems/conclusion 10%，合计 100%。基础内部暂按 event 6% + SNN 8%，只解释后文必要概念。训练、鲁棒性与部署的交叉证据可进入核心章节，不用泛化背景取代。参考综述约 60% 核心和低背景比值得借鉴，但其约三页结果表的占比不照搬；本主题需要额外解释 spike/time/纯度/训练差异。最终篇幅随论证复杂度调整，不能按论文数线性分配。

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

**当前不冻结v1.0。** 历史盲重标scope/directness/extent/selection均10/10，primary9/10；FLAME唯一分歧保留。0.2修复interface合同、mlp架构和neuronal_spike_train表示，规范八行未经批准的trigger写法，并建立可逆migration。ABN训练原文冲突、DailyDVS协议冲突以及generic conversion的监督来源限制均保持deferred；它们不改变主要role，但相关比较用途受限。

E1/E2满足有限扩展门：五例旧role与两例mlp复判完成；C/F/D/P/H五篇获得直接role/extent证据。G在五个已检查候选中没有可靠正例，明确排除出ordinary clear-case校准适用域，进入Sol High→Astra首例准入；不宣称不存在或已覆盖。H验证live sensor到芯片系统集成与成本边界，不足以宣称所有sensor/ASIC联合设计都已覆盖。P仅代表3D人体姿态，不代表全部6-DoF相机位姿家族。

可扩展冻结要求：上述缺口已回答或正式限制范围；新合同无未解释分歧；没有必须发明primary才能表达的方法；关键scope/role/extent有直接证据或对应记录暂不作主图代表；unknown/来源冲突均有责任人和用途限制。达到agreement阈值只是必要条件，不能替代这些判断。

最终 taxonomy 收敛需要：572 条逐项完成或有阻塞原因，补充检索来源均记录、去重；所有 central representatives 的核心证据已验证；critical issue=0；最近两个审查批次无未解释的新 role/需重画主图的冲突；最后两轮定向引用追踪没有出现可改变主结构的新机制（有新增但重复的 bibliography 不算失败）；每个大类有至少两个独立 work family，单篇独特机制保留例外框而不强升顶层；按来源/年份/active 状态/任务检查偏差；Astra 能用固定定义解释跨类差异与类内共同点。达到阈值后仍需用户确认最终 taxonomy/outline。

## 8. Astra / Sol 工作流与当前停止点

| 阶段 | 执行者 | 输入/交付 | 当前门禁 |
| --- | --- | --- | --- |
| 设计及30篇pilot | Astra High → Sol High | 原0.1、30篇/36配置、27 PDF检查、10-case盲重标 | 已完成，保留历史 |
| 原checkpoint | Astra High | 四项原issue裁决、0.2校准版及可逆迁移 | 已完成；AB/DD/CV用途限制继续有效 |
| E1/E2 | Sol High | 五例旧role、两例mlp；五篇新校准及G失败审计 | 已完成，35篇/41配置的校准证据层与旧membership独立 |
| E2冻结审查 | Astra High | 保留四role与五例extent；修正少数字段，保留deferred | 0.2有限扩展冻结，G特殊路由；不是v1.0 |
| 冻结后首批及后续 | Sol Mid / High | 首批30篇=3×10：clear-case候选、core inference候选、cross-cutting/边界候选；High解决所有核心方法及PDF触发 | 全572是待遍历母域，本轮不启动；首批后Astra，后续每批最多40篇 |
| 中期 | Astra High | 约150/300/450条审查来源/年代/role/表示/未知/排除与family | 规则修改带版本迁移；不为了数量改变scope |
| 最终合成 | Astra High，必要时单次xhigh | 全文献扩展与claim ledger后，final taxonomy、outline、150–180预期usable裁剪 | 属后续任务，不由本checkpoint提前决定 |

Sol High负责证据与按规则解歧，Sol Mid负责冻结后的明确案例和确定性操作；不得自创标签，不同时修改同一工作树。Astra负责规则、全库分布、冲突、最终结构和裁剪。既有Survey/Advisor成员及V2仍独立。

本轮完成规则裁决、文档与可逆迁移、只读验证、本地commit后停止；不push、不继续全量工作。下一步按freeze decision启动单独30篇首批并停在Astra checkpoint；本次不创建批次或执行标注。

## 9. E2冻结后的增量结论

原pilot仍30篇/36配置；E2单独5篇/5配置，合计35篇/41配置。核心22篇=interface 4、task 9、embedded 3、engine 3及cross-cutting 3；这个刻意校准样本不能作为全库方法频率。C/F/P/H的task_network及extent保留；D保留engine及数值模型fully_spiking_task_network。首批规则、G限制、P训练路线新deferred与逐字段迁移见freeze decision。篇幅与150–180预期规模仍按独立论证价值，不设类别配额。
