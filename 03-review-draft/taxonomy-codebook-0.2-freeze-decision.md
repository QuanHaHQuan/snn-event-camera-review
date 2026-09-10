# Codebook 0.2：Batch E2裁决与有限扩展冻结

日期：2026-09-10。裁决者：GPT-6 Astra High。输入提交：`ec707f94174808a3a387ae208e936227d9a898ed`，当前local main起始工作树干净。主要输入是E2报告、完整5行59字段校准表、G候选审计、E1定向重判和原checkpoint；复用现有30篇pilot证据，不重新抽取。

**Checkpoint通过，发布 codebook 0.2 / frozen_limited_expansion。** 这是第一个允许后续分批扩展的冻结版本；不是v1.0、最终taxonomy或最终usable corpus。冻结的是字段、操作性定义、证据合同和路由。没有新增role、extent、architecture、training标签或CSV字段，因此保留版本号0.2；JSON发布状态及本文件界定从校准到有限冻结的生效点。后续实质性定义/标签变更必须另发版本和迁移，不在冻结0.2中静默改写。

本轮没有启动572篇标注、重做30篇pilot、扩大G检索或修改Survey/Advisor membership。35篇校准集合仍与原candidate/active/selection语义源分离。

## 1. 为什么可以冻结，以及没有被证明的事

| 门 | 证据 | 裁决 |
| --- | --- | --- |
| 旧相邻类复现 | E1五个role判定5/5一致、两个mlp判定2/2一致；合同理由完整 | 通过定向稳定性检查；同一执行者且有上下文，不能称新盲测或模型间可靠性 |
| 经典/跨任务/硬件缺口 | C/F/D/P/H五篇独立canonical、PDF方法和模块边界 | 足以校准这些输入合同；不证明每个task或hardware家族穷尽 |
| G未找到正例 | AEGNN、HUGNet、GNN+PA有event graph而无真spiking；DRSGNN、MSG有真spiking graph而无camera input | 通过“明确适用域限制”这一冻结条件；不是通过G正例覆盖测试 |
| role表达力 | 五例不要求第五role；D增加不同年代的第三种明确engine机制 | 保留四个primary角色；不要仅用一致率决定冻结 |
| 字段与审计 | 59字段、既有词表可表达全部裁决；E2单独from/to事件 | 保持0.2，修正记录而不膨胀标签 |
| 事实缺口 | ABN、DailyDVS、generic conversion仍deferred；P训练过程另有局部缺口 | 限制对应表格使用，不影响已证实role/extent；不把deferred计为resolved |

G限制的准确表述是：**在已检查来源和五个最近候选中，没有可靠的同篇contrast-event graph × spiking message-passing正例；该组合尚未校准，不属于普通clear-case批处理的适用域。** 可以接收未来候选进入证据队列，不能排除整个家族、声称它不存在、或拼接不相交论文来证明覆盖。`graph_network`仍是架构轴，graph不是第五role。最早合格正例经High核查后必须回Astra；若现有合同足以表达，可个案准入，否则重开版本审查。

H校准的是实时sensor到spiking chip的系统集成和成本边界，**不是所有新sensor/ASIC共同设计**的代表。P校准3D人体SMPL姿态跟踪，未校准全部6-DoF相机位姿方法。稀有光流/深度/pose机制、sensor-neuron联合设计仍走High，不制造新的“已全覆盖”结论。

## 2. C/F/P/H与D逐项裁决

| 槽 / paper_id | Primary裁决 | Extent裁决 | 输入—输出与邻界；证据 |
| --- | --- | --- | --- |
| C / TPAMI2013-PEREZ-CARRASCO | 保留task_network | 保留fully_spiking_task_network | 转换后的ConvNet承担主要特征和类别发放；crop/downsample及扑克event tracker在外部，因此不是end_to_end_spiking_pipeline。训练路线与推理功能独立。C-E1–E4、C-A1/2 |
| F / ECCV2020-SPIKE-FLOWNET | 保留task_network | 保留hybrid_subnetwork | SNN供给四尺度主encoder层级、bottleneck与各decoder对应skip features；不是仅向另一完整编码器交付低层特征。最后积累层不发放，residual/decoder/flow head连续；因此也不能称fully_spiking_backbone。F-E1–E4、F-A1/2 |
| P / ARXIV2023-ZOU-POSE | 保留task_network | 保留hybrid_subnetwork | SEW-ResNet及spiking Q/K/FFN共同构成主要pose特征/时空推断；默认实值value路径使主干混合，三条SMPL线性head连续。event-only只描述模态，不保证纯度或causal streaming。P-E2–E5、P-A1/2 |
| H / CVPR2017-AMIR-TRUENORTH | 保留task_network | 保留fully_spiking_task_network | TrueNorth上的temporal cascade、15层CNN、WTA和smoother完整执行识别；输入实际经过USB/Zynq/FPGA，不能升级sensor-to-result全spiking。H-E1–E4、H-A1 |
| D / SCIREP2017-OSSWALD-STEREO | 保留algorithmic_engine | 保留fully_spiking_task_network，限数值模型 | coincidence候选(x,y,d)→视差支持/冲突积分→recurrent uniqueness竞争→disparity events；30 ms分桶仅非学习地图读出。FPGA coincidence + ROLLS disparity是局部硬件实现，不继承数值模型extent。D-E1–E5、D-A1/2 |

F是本次唯一需要补强主角色原文合同的位置：定向回看PDF pp.7–10，查看p.8 Fig.3及对应段落，确认各尺度encoder输出直接参与decoder。**“有四层”“位于前端”“叫encoder”都不构成task_network判据。** PLIF-ASAB（CVPR2025-2047）的现有AH-E2与E1合同显示低层PLIF features经ASAB交给后续ANN blocks承担主要编码；保留embedded_module。F的全编码层级和PLIF的局部早期feature区分可复现；遇到无法定位主层级的新串行encoder，交High，不机械套用这个类比。F的ANN decoder不等于另一个以事件表示为输入的principal model，故也不是event_interface。

D满足engine的三个必要条件：命名的求解目标/变量；spike/state与候选、证据和解的具体对应；这种对应就是提出的推理机制。它与WTA/EM、ISTA/fixed point形成三个独立机制锚点，因此在冻结版正式保留primary algorithmic_engine。一般STDP训练、SGD、attack optimizer、普通网络推理及只有灵感名称的算子不满足。若算法对应只是局部机制，则按真正主要功能归类；不存在固定engine优先级。

**D的secondary task_network改为none。** 同一solver完成depth不是独立第二职责；否则所有engine都能重复获得task_network，破坏F23。STLR的独立SNN decoder确有另一职责，可保留secondary。extent的fully_spiking_task_network名称不要求primary等于task_network。

## 3. 字段修正、迁移和deferred

| 记录 | 旧值 → 当前值 | 理由 / issue |
| --- | --- | --- |
| C training_route | conversion_then_finetune → ann_to_snn | 原文保留学得kernel，只优化timing/threshold，包括simulated annealing。这是F34已涵盖的转换校准，不据此断言另有SNN再训练。PDF p.9 §V、p.16 Appendix 5定向核查；E2-C-I2 resolved / astra |
| F training_route | direct_snn → joint_ann_snn | 同一loss通过ANN与SNN块共同反传，Algorithm 1/§3.5/Fig.4直接支持。选择已有更具体hybrid训练标签；E2-F-I2 resolved / astra |
| D secondary_functional_roles | task_network → none | 没有独立第二个SNN任务模型；E2-D-I2 resolved / astra |
| P snn_module_functions | feature_extraction;attention_routing;fusion;task_head → feature_extraction;attention_routing;fusion | SMPL head是连续linear，不能记为SNN承担的模块；E2-P-I2 resolved / astra |
| P training_route | direct_snn → unknown | 现有证据定位主要支持推理架构，不能仅从混合图推断连续部分与SNN共同优化，也不能无依据保留direct_snn。E2-P-I3 deferred / sol_high：需要时定向查v5训练section的参数/phase范围，区分direct_snn与joint_ann_snn |

没有更改五篇scope、primary、extent、selection、身份、完整摘要或来源版本。五行增加Astra问题处置与证据，review_status=astra_adjudicated仅覆盖本文件的role/extent与上述字段，**不是59字段事实终审**。P原先已回答的PDF问题保持resolved；新训练用途限制由deferred issue管理，pdf_check_status不代表“所有未知已解决”。若启动该具体核查，再开启相应PDF question。P的learning_signal/credit_assignment等未在本轮重新终审，不能拿角色审查当作训练表引用认证。

`taxonomy-codebook-0.2-gap-events.csv`保留5条Astra事件，每个变化单元格保存完整from/to；原C-E1的Sol解释保留，当前C-A2说明为何修正。`calibration_baseline`绑定Sol提交ec707f9和5行原快照hash。反向迁移必须恢复该独立快照，不将这5篇塞入原30篇/36配置/107事件，不改旧blind 9/10。G审计五候选原样保留。本次不是定义变更迁移；是按既有F22/F23/F25/F34纠正记录和发布状态。

继续保留原三项deferred，且冻结不解除其引用限制：

- **AB-I2 / astra**：ABN实验STBP与结论STDP冲突；training_route和credit_assignment仍unknown，不推定phase，不做已确认训练机制计数。
- **DD-I1 / astra**：DailyDVS参与者名单/人数冲突；不刊自行修复的ID，不把结果当已验证跨人泛化。不影响dataset authority；是否重开manifest核验取决于具体复现/定量用途。
- **CV-I1 / astra**：generic conversion的distillation证据仍不足，learning_signal=unknown。C是独立的event-specific conversion例证，不能替另篇补教师损失事实。

## 4. 可执行章节结构

第一层按主要机制贡献中SNN的推理职责组织，以下二级标题用于写作组织，**不是新增enum或互斥子类**。按一次主要叙述加交叉引用避免重复计算论文。

| 第一层 | 二级组织及纳入合同 | 邻界排除 | 校准代表 |
| --- | --- | --- | --- |
| event_interface | 边界控制；事件选择/聚合；有时间/地址或通道语义的新neuronal event train。都须I1–I4显式交接 | 普通隐藏feature、仅binary激活、固定非SNN slicing | SpikeSlicer；EAS/SDA；FLAME |
| task_network | 主要event特征/预测路径（含完整spiking编码层级或分布式hybrid主路径）；联合多模态主要推断 | 局部特征/head、纯training-only、独立sampler、明确solver主贡献 | SpikePoint、ABN、HsVT、event SpikeTrack；SpikeFET；C/F/P/H |
| embedded_module | 串行局部feature/时序过滤；支路/跨模态条件化、局部head或memory | 满足事件表示合同的interface；主要层级编码/混合主路径 | PLIF-ASAB、REDIR；ClearSight |
| algorithmic_engine | 概率竞争/在线参数推断；固定点/展开latent coding；约束对应求解 | 通用学习优化、只有算法灵感、同一solver再次计task角色 | Spike Bayesian；STLR；D stereo |

另设核心cross-cutting章节：event-specific训练、增广、攻击/鲁棒性、转换与部署条件中没有新inference topology的工作，primary=not_applicable；含新系统的转换论文C按task主叙述，再交叉引用training axis。foundation是压缩解释层；dataset/benchmark是评估权威层；non-SNN comparator进同协议比较表；hardware/efficiency跨四role，不设第五角色。

正交表字段保留：scope/directness、输入来源/模态、时间组织/representation/interface、secondary roles、boundary/extent/signal、architecture/neuron/state、物理时间/事件分组/SNN步与reset/lookahead、training/credit/监督、task/output、dataset/version/split、效率证据类型及system boundary、robustness、source/confidence和具体survey use。H的178.8 mW为TrueNorth network功耗；D为投影；F/P为代理，不能并作全系统能效排行。

## 5. 特殊路由与自动检查边界

**Mid不能终审：** 所有core-intersection方法、所有具体PDF触发、engine、conversion/phase、fully-spiking及芯片/功耗主张、interface/module/task难例、冲突/弱证据、真event-graph SNN候选。Mid可以完整抽取标题摘要、规范metadata、按规则作初判，但必须保存unknown、具体问题与证据定位，不能靠旧role或模型知识填空。

**High处理：** 按已有规则查PDF的具体问题，定位event→neuron→输出、学习phase、成本范围；解决可由现有字典直接判定的事实问题。无法表达/相邻合同仍冲突时创建issue：owner=astra、status=evidence_ready，不创标签。G首例必须同时证明同篇event graph和spiking message passing，写图构造、edge message、neuron位置、三个时间轴及成本；issue ID以`G-`开头供门禁核验，High提议后Astra resolved才能主图准入。未准入用taxonomy_placement=pending，scope可保留证据已确证的core，不以pending冒充排除。

**Astra处理：** 首例G适用域、无法套合同的核心机制、role/extent冲突、定义和版本、批次分布、最终taxonomy/outline与usable裁剪。AB/DD/CV只有来源更正或相应实验证据才重开；P训练问题由High在训练比较需要前准备，不阻止首批角色抽取。

validator检查可复现结构而不是代替科学判断：默认模式保护pilot；standalone校准模式对E2追加反向迁移校验；新增`--expansion-batch`只验证独立candidate批次、完整标题摘要join与hash、40篇上限、不允许最终usable，以及G主图准入必须有Astra `G-`resolved记录。它不能从自由文本发现被误标的graph，也不能证明High确实读了PDF；因此批末人工合同审查不可省。

## 6. 冻结后首批：只规划，不在本轮启动

**B1总量30个新的canonical papers，3个10篇小批。** 在全部572 candidate audit中选取，排除已处理pilot身份/重复family；不局限298 active，不重抽已完成35篇。后续执行任务先列ID清单、选择依据及与旧family的join，再开始抽取；旧A/B/C、role只能导航，完整官方标题/摘要及新证据才决定标签。

| 小批 | 10篇的选择对象（预期，不是强制最终类别） | 执行/交接 |
| --- | --- | --- |
| B1a | 预计清晰的event/SNN单轴基础、dataset authority、non-SNN comparator、明确术语负例 | Mid完整摘要初判并保存引用用途；High复核其中3例，涵盖foundation/boundary/evaluation，每个已出现组至少1例；所有意外core/触发项全部转High |
| B1b | 预计core inference，覆盖interface、主要网络、局部module及engine候选；有疑似G自然进入但不为凑槽追加检索 | Mid建10条来源记录→High逐篇关键PDF合同；按实际内容分类，不设四role数量配额 |
| B1c | event-specific training/augmentation/attack、generic DVS-only边界、conversion/混合或fully-spiking claim | Mid作scope/contribution初判→High复核全部10篇，定位cross-cutting或角色与phase；无可得abstract/PDF者记录阻塞，不悄悄换篇 |

B1a–c不是新标签，也不保证每篇最终归入预期。各组在可得候选内覆盖active与非active、不同年份/venue；不足某预期时注明，不靠标题虚构例子。这个安排先检验Mid是否把DVS-only误收、把冗余当scope排除，再测试核心和cross-cutting分界。

每个小批按 **Mid写完并停止 → High接手原批次并保存修正 → validator与coverage → 下个小批** 顺序执行，同工作树不并发写。记录单位可因配置拆分增加，但canonical上限不变。交接包必须有ID清单/完整摘要hash、59字段表、逐字段变更历史、具体PDF问题/答案/页码、issue及owner/status、按canonical去重的coverage报告；绝不覆盖candidate audit或membership。范围外新增文献留单独来源审计，下一检索批次再纳入。

**B1完成即回Astra，不自动开始B2。** 检查：30个预定ID逐一完成或明列阻塞、核心role/extent证据合同、Mid→High翻转原因、unknown和deferred用途、scope×role×representation与active/非active/年代分布、重复family及G路由。出现新的无法表达机制、关键合同仍有未解释冲突，相关记录保持pending，暂停同类终审；不为赶批次清零。

Astra接受B1后，B2起每批**最多40篇，仍按10篇小批顺序交接**；PDF不可得或High积压不得通过扩大批量掩盖。前两批都回Astra；稳定后每批有coverage和issue交接，约150/300/450候选覆盖点做全库分布审查，任何定义级冲突即时回Astra。150–180只在最后依据独立论证价值裁剪，没有scope/role配额。

## 7. 验证、文件与停止边界

主要当前文件：本裁决、codebook、architecture memo、E2校准表及新增gap-events、schema JSON、validator。历史checkpoint/E1/migration只加当前状态导航；pilot results与E2报告追加当前结论。CSV header、candidate audit、membership、V2、旧pilot/blind/events、G候选失败记录不改。

只读验证入口：

```sh
python3 scripts/validate_taxonomy_pilot.py
python3 scripts/validate_taxonomy_pilot.py --annotations 03-review-draft/taxonomy-codebook-0.2-gap-calibration.csv --standalone-calibration
git diff --check
```

未来独立candidate批次入口为`python3 scripts/validate_taxonomy_pilot.py --annotations <batch.csv> --expansion-batch`；本轮只用临时结构fixture测试入口，不产生真实新论文标注。最终验证结果记录于本节追加项。

当前范围内完成后创建本地commit，**不push**。不启动B1，更不启动572全量；用户下一次交给Sol执行时以本文件和冻结0.2为合同。

验证结果（提交前）：

- 原pilot：30篇 / 36行 / 59字段 / 107事件通过；历史blind与70条原事件不变，可逆恢复0.1快照。
- E2：5篇 / 5行 / 59字段通过；5条新事件可逆恢复ec707f9的独立Sol快照。全部scope、primary、extent、selection及身份/摘要保持原值。
- 8个临时结构测试通过：合法独立批次、未准入G拒绝、带裁决结构的G门禁、G可保持pending、过早usable拒绝、非法标签拒绝、41篇超限拒绝、无事件修改拒绝。G测试只更改临时fixture，不是新增科学正例。
- 19个受保护文件逐字节核对通过；00-index、V2和既有logs无改动；59字段和所有受控/嵌套词表及pilot_baseline不变；当前文档相对链接可解析。
- Python AST及`git diff --check`通过；新增文件纳入暂存后再检查cached diff。上述测试证明结构和追溯，不能替代论文方法证据审查。
