# Taxonomy annotation codebook

版本：**0.1-design / 2026-09-10，待用户确认用于 pilot**。本 codebook 是可被 pilot 推翻的规则草案；只有 Astra checkpoint 可以修订取值，Sol 不得自建标签。它不继承旧 A/B/C、role、Core membership 或旧 needs_pdf_check 作为答案，也不替代现有 audit。

## A. 执行契约与数据类型

最小单位是 `paper_id + annotation_unit`。scope 是研究对象，primary_functional_role 是主要机制贡献中的 SNN 功能，spiking_extent 是计算范围，training_route 是学习路径，selection_status 是阅读/纳排决定，evidence_basis/confidence 是证据状态。这六层不得互换。相同 paper 的训练和推理、ANN/SNN变体若关键结构不同须分行；总文献数按 canonical work family 去重，不能按行数或多选标签相加。

下文每个 `### Fxx` 恰好对应 CSV 一列，顺序与 schema header 完全一致。只有 metadata、理由、引用、原始名称、数值等采用有格式约束的开放文本；不能对无限的标题/数据集名称编造“有限全集”。其约束是保留来源原文，不是允许创造 taxonomy labels。

- `single enum`：一个且仅一个已列标签。`multi enum`：以分号分隔，不重复，按本文词表顺序；不能加入同义变体。全无证据时用单独 `unknown`；`none`/`not_applicable`/`pending` 等哨兵不得与实质标签并列。
- `single text`：一个 UTF-8 文本值，依字段格式填写。`single JSON object` 与 `multi JSON array`：CSV单元格内存标准JSON；固定keys，不用Python repr，CSV writer处理引号和换行。JSON嵌套中的原文名称不是新标签。
- 除明确不允许的管理字段外，`unknown` 表示“适用但证据不足”；`not_applicable` 表示“不适用且有明确理由”，只用于该字段声明允许处；`none/absent/non_spiking` 必须基于检查后的否定证据，不能因摘要没提就填。
- 部分多选字段已确认一个值、其它关键值未定时只填已确认值，在 evidence_basis、confidence、pdf_check_question 中对未定 field_path 记录 unresolved；不要把 `unknown` 混进已知标签集合。
- 所有正反例是**规则示例或从存储摘要得到的检索线索**，不是本轮完成的论文 annotation。涉及实际论文的 neuron、接口、pure、measurement 都须执行者回原始材料核对；旧 V2/graph 只导航。引用优先用忠实转述，短原文要逐字且带位置。
- 受控的 `other_documented` 仅允许“原文明确但现有字典没有”的已知对象；必须同时 open missing_label issue。不能当默认垃圾桶，不能自动进入最终taxonomy；Astra决定增标、合并或保留文本例外。

### 条件填写与最小阅读负担

所有记录必须填写身份/完整摘要、scope/directness、event_input_source、spiking_computation的已知状态、contribution_focus、selection/use/reasons和证据/问题/QC。其余技术字段按适用性填写，不能因有59列就强迫无关论文全文精读。

- **清楚的范围外且无独立综述用途**：在下列技术字段中使用not_applicable，理由指向已确认的scope/use边界；这表示“本综述不提取该机制”，不是断言论文没有这些机制。仍可保留摘要明确说有SNN的claimed事实。三篇abstract-only负例均遵守此门。
- **真实event-camera单轴或SNN一般基础**：填写与具体比较用途有关的技术字段；event-only论文的neuron/neuronal-spike字段不适用，generic SNN的event表示字段不适用。若拟用其方法/效率作为代表证据，相关字段必须PDF，不准以not_applicable绕过。
- **core_intersection方法代表**：全部适用的接口、role、boundary、时间、训练与评测字段均须取证；不知道就unknown+具体问题。training-only交叉可以primary not_applicable，但被训练/攻击对象的输入和边界仍需按用途核查。

允许该条件门的字段白名单：modalities, temporal_organization, representation_form, representation_properties, representation_learning, event_to_spike_interface, primary_functional_role, secondary_functional_roles, snn_module_functions, spiking_boundary_map, spiking_extent, spiking_signal, architecture_family, neuron_family, internal_state, temporal_mechanism, time_axis_mapping, training_route, learning_signal, credit_assignment, task, output, dataset_evaluation, efficiency_evidence, efficiency_claim_details, robustness_evidence。白名单外不能据此填not_applicable。枚举字段直接用not_applicable；JSON字段整体不适用时用JSON字符串 `"not_applicable"`，不是 `{}` 或 `[]` 来掩盖缺失；已有适用记录时保持固定JSON结构与逐键unknown。primary_role_reason需解释不适用的原因。

此白名单也是以下各字段controlled vocabulary的显式补充；not_applicable的正例是已证实无本综述提取用途的范围外论文，反例是有待解决机制问题的交叉代表作。相邻unknown表示应该提取却没证据，二者不能互换。最终批量validator需执行此条件门。

## B. 顺序决策树

1. **身份与完整摘要门。** 精确匹配paper ID、完整标题、版本和完整官方摘要；核验hash。先不显示旧role/旧reason，以免锚定。已有card/V2在初判封存后只用于发现冲突。摘要缺失/截断先解决来源，不能从标题筛完。
2. **输入门。** 它是否真的处理contrast-change event-camera信号/表示？记录physical/simulated/sensor-resampled/noncamera/spike-camera。camera event是传感器亮度变化记录；neuronal spike是计算神经元的发放输出。二值数据、事件数、稀疏点、脉冲相机都不能自动跨过此门。
3. **真实计算门。** 寻找输入如何驱动state、发放函数和发放后状态/重置，以及发放是否参与下游计算。仅threshold、attention gate、stateful、asynchronous、膜电位比喻不足。已明确SNN但无实现只填claimed；冲突用unknown。无SNN也要判是否event_camera_foundation，不等于排除。
4. **耦合门。** 找到原文明确的event-to-SNN接口/特定系统设计或event-specific训练/分析联系。只有DVS benchmark的一般neuron/训练研究为snn_foundation+benchmark_only；没有独立机制的generic benchmark-only工作可boundary_or_exclude。事件特定augmentation/攻击可为core_intersection+event_specific_training_analysis，但不自动获得推理role。
5. **接口门。** 从最早camera event沿pipeline走到第一处neuronal spike。写source→slicing→representation→encoding/current→spiking module→continuous/spike readout。input在论文中叫raw不构成direct neuronal injection证据。先记录representation构造位置，再判断role。
6. **功能门。** 确认作者主要机制贡献和SNN模块输入/输出，按下文规则选primary。独立额外职责标secondary；多任务/multiple modules不是多篇论文。不确定主次用unknown+role_conflict。
7. **边界门。** 核查preprocess/backbone/fusion/head/readout；将continuous算子和保留状态显式列出。由map导出spiking_extent。不能从fully spiking backbone外推task network，也不能从task network外推sensor-to-result pipeline。端到端可训练不等于端到端fully spiking。
8. **时间、神经元和学习门。** 区分physical event time、event-group order、SNN simulation timestep；检查state reset、causal/lookahead、neuron、架构、训练路线、监督和credit assignment。conversion/hybrid/integer train分开；不能凭常见实现补PLIF/SG/BPTT。
9. **证据与用途门。** task/dataset/configuration/metric作为比较轴；能耗按证据类型和system boundary拆开，robustness需威胁/预算/数据设置。写具体use和纳排理由；只有Astra在后续阶段决定最终usable与outline。
10. **关闭门。** 按字段定位证据和confidence。所有触发问题逐题关闭或正式保持unresolved；不要为了填满表格猜测。执行validator和自检，初判与PDF修正保留差异记录，交issue queue。

## C. Primary role 的操作性裁决

先确认论文是否提出/改变推理SNN功能。纯training、分析、攻击、数据、理论背景没有新的inference role时用not_applicable；现成backbone仍可写snn_module_functions与边界，taxonomy_placement=cross_cutting/foundation_comparison。不能将“使用现成classifier评测augmentation”变成新的task_network代表。

对于推理方法，按**主要机制贡献的输出合同**判断，而不是按标题词、参数多少、FLOPs占比或最后一个输出层决定：

- 输出是事件保留/切片触发，或论文明确分离的event-derived表示，交给后续principal feature extractor：候选event_interface。必须能指出交接tensor/control及其事件构造作用。
- 输出是主要任务特征及推理路径：候选task_network。主要路径指从表示进入后承担核心层级特征抽取/任务推断的模块，而非仅有最大参数量；SNN主干之后的连续task head不自动降成embedded_module。若ANN/SNN交替均承担核心抽取且没有明确主要路径，则unknown+issue。
- 局部SNN从属另一主要系统，生成latent features、过滤/记忆/注意力/融合/路由/head：候选embedded_module。hybrid是边界属性，不能当本role的同义词。
- 明确存在算法变量/步骤与spike/state更新对应，且论文以此作为主要解释或消融对象：候选algorithmic_engine。WTA对应E-step、STDP对应M-step是检查线索；ISTA-inspired名称还需验证展开变量和spiking更新；一般SGD训练不算。

**interface vs embedded front-end：** 位置早不是充分条件。明确控制event子集/边界一定是interface候选；表示构造需有pre-backbone event-to-representation交接和构造目标。仅输出任务专用latent feature的前端优先embedded_module，不因叫representation改标。如果论文既有显式表示又有latent feature，依据主要被提出/验证的模块；替换不同下游backbone的实验证据可增强interface判断但不是强制准入条件。仍无法区分则交Astra，不能自称已互斥。

**backbone vs head：** 从representation至多层任务特征是backbone；从这些features到特定输出预测是head。SNN只在head就是embedded_module；head输出为连续值不否定其内部spiking。encoder-decoder都是SNN且共同完成任务可以task_network，decoder不因名字就降为head。

**多role的选择：** 先列独立模块，利用贡献句、方法组织和针对性消融找论文真正提出的主机制。SDA/EAS同时可能有SNN sampler和SNN detector；STLR可能有algorithmic encoder和task decoder。能定位主贡献则择一，另记secondary；无法证实主次必须unknown，禁止固定“engine永远胜过backbone”等机械优先级。Astra在pilot后比较“按贡献选primary”与“按系统主路径选primary”的一致性，必要时推翻此规则。

## D. 字段定义与受控词表

每节的“取值/定义”均包含操作条件及正反例；“判别例/邻界”说明最容易混淆的邻值。所有字段共用A节的unknown规则；以下逐字段规定例外、摘要可用程度和PDF触发。嵌套JSON词表另见E节，不可任意扩keys。

### F01. `paper_id`

- 目的：稳定连接 audit 或批准后的外部登记。
- 选择类型：single text。
- 取值及操作性定义：现有候选必须逐字匹配 audit paper_id；外部候选采用 future registry 批准的稳定 ID，禁止自行给已知论文改 ID。
- 判别例与邻界：正：ICLR2024-1097；反：SpikePoint（别名不能作 ID）。
- unknown 条件：不允许；身份未解析则暂不生成论文行。
- 摘要权限 / PDF 触发：官方 metadata 冲突时查首页/正式来源；摘要不决定 ID。
- 最终用途：去重与回溯。

### F02. `canonical_title`

- 目的：保留完整正式标题。
- 选择类型：single text。
- 取值及操作性定义：原始候选逐字复制 audit title；正式版本冲突先保留原文并建 issue，不用模型名代替标题。
- 判别例与邻界：正：SpikePoint: An Efficient Point-based Spiking Neural Network for Event Cameras Action Recognition；反：SpikePoint。
- unknown 条件：不允许；缺完整标题阻塞该记录。
- 摘要权限 / PDF 触发：可由官方 metadata 判断；PDF 首页与 metadata 不同必须记录。
- 最终用途：引用身份。

### F03. `year`

- 目的：论文版本年份。
- 选择类型：single text。
- 取值及操作性定义：四位公历年份；取被标注版本，online-first 与卷期差异放 official_source。
- 判别例与邻界：正：2024；反：用预印本 2023 年静默覆盖 ICLR 2024。
- unknown 条件：unknown 仅外部记录尚未规范化，不能最终 usable。
- 摘要权限 / PDF 触发：官方 metadata 可；冲突查正式版本。
- 最终用途：历史与检索覆盖。

### F04. `venue`

- 目的：正式发表出处及 track。
- 选择类型：single text。
- 取值及操作性定义：保留 venue/year 对应身份；NeurIPS track 写 official_source，venue 不偷换成 Main Track；不是 closed venue allowlist。
- 判别例与邻界：正：ICLR；反：把 arXiv 当作已发表期刊。
- unknown 条件：外部 metadata 未确认可 unknown。
- 摘要权限 / PDF 触发：metadata 足够；有冲突查首页/出版页。
- 最终用途：来源偏差。

### F05. `official_source`

- 目的：版本、官方页面、PDF 与来源定位。
- 选择类型：single JSON object。
- 取值及操作性定义：固定键 page_url,pdf_url,pdf_sha256,version,official_track,access_date,repository_locator；值为原文 URL/路径/日期/哈希或 unknown/not_applicable。
- 判别例与邻界：正：官方页 URL + 实际核查 PDF hash；反：将 V2 路径冒充 official PDF。
- unknown 条件：未下载 PDF 的 hash=unknown；不因此伪造已查证状态。
- 摘要权限 / PDF 触发：可用 metadata；要写 PDF 证据时必须绑定实际 PDF 版本。
- 最终用途：所有证据审计。

### F06. `abstract_text`

- 目的：执行者必须读完整官方摘要。
- 选择类型：single text。
- 取值及操作性定义：当前候选完整复制 audit.abstract（不得摘要化）；新增文献获取官方完整摘要；没有摘要时保留 unknown 并解释来源限制，必须 PDF。
- 判别例与邻界：正：完整段落，保留限定语；反：只留命中 spike 的句子。
- unknown 条件：仅确实无可取得官方摘要；不能据此自动排除。
- 摘要权限 / PDF 触发：允许 official abstract；截断、冲突或无摘要触发 PDF/来源复查。
- 最终用途：最低筛选证据。

### F07. `abstract_sha256`

- 目的：检查文本未发生静默变化。
- 选择类型：single text。
- 取值及操作性定义：对 abstract_text 的 UTF-8 原始字符串算 SHA256，不先去空格或规范化换行。
- 判别例与邻界：正：64 位 hex；反：沿用别的版本哈希。
- unknown 条件：abstract_text=unknown 才允许 unknown。
- 摘要权限 / PDF 触发：无需 PDF；存储值不符先修复抽取，不能改变 audit。
- 最终用途：抽取质量。

### F08. `record_origin`

- 目的：追踪召回入口。
- 选择类型：multi enum。
- 取值及操作性定义：candidate_audit=当前572条（+现有ID；−只在bibliography）；reference_bibliography=用户参考综述引用（+其[72]；−模型记忆）；core_backward=Core正文或引用追溯（+有source/marker；−只共享词）；forward_search=引用关键种子的后续论文（+记录检索来源；−无出处猜测）；classic_pool=现有历史候选/graph入口（+稳定node key；−新候选假称已入库）；targeted_search=针对明确缺口的正式检索（+query/date；−任意扩库）。
- 判别例与邻界：可多入口同存；入口不是 scope 或 admission。
- unknown 条件：不可 unknown；每行至少一个可追溯入口。
- 摘要权限 / PDF 触发：metadata 足够；引文机制关系要另查 source PDF。
- 最终用途：coverage report。

### F09. `codebook_version`

- 目的：绑定字典和迁移规则。
- 选择类型：single enum。
- 取值及操作性定义：0.1-design=当前未冻结试运行规则（+pilot初版；−称final）；后续版本仅由Astra正式发布后加入，不预填1.0。
- 判别例与邻界：正：0.1-design；反：Sol自行写0.2并增加标签。
- unknown 条件：不允许。
- 摘要权限 / PDF 触发：不需 PDF，来自交接文件。
- 最终用途：版本审计。

### F10. `annotation_unit`

- 目的：避免把不同变体证据拼成不存在的系统。
- 选择类型：single text。
- 取值及操作性定义：paper::variant::phase 的稳定标识；默认 paper::main::inference；training-only用paper::main::training_analysis。若变体在输入/role/boundary/训练路径不同，独立行并共享paper_id；不能平均或选最优数值拼接。
- 判别例与邻界：正：paper::SNN_detector::inference 与 paper::ANN_detector::inference 分行；反：把不同配置的accuracy和energy合到main。
- unknown 条件：变体不明可 paper::unresolved::inference 并建 issue。
- 摘要权限 / PDF 触发：摘要只支持paper-level初筛；变体拆分一般需 PDF。
- 最终用途：论文计数按去重ID，表格可多配置。

### F11. `scope`

- 目的：区分研究对象；不是最终纳排。
- 选择类型：single enum。
- 取值及操作性定义：event_camera_foundation=真实事件相机方法/数据/传感且无方法性SNN交叉（+PEPNet的非spiking点方法；−SNN检测器）；snn_foundation=一般SNN机制/评估贡献而无event-specific桥接（+CLIF一般神经元；−event sampler专用SNN）；core_intersection=事件信号与真实spiking computation有明确方法联系，包括专门训练/攻击（+event-to-spike接口设计；−只报DVS准确率）；boundary_or_exclude=错误信号域或无独立目标轴贡献（+spike camera/EHR；−冗余但真实的交叉方法）。
- 判别例与邻界：同为DVS测试：一般neuron研究可snn_foundation，无新机制的baseline-only可boundary；差别看贡献，不看重要程度。
- unknown 条件：关键信号或SNN证据不足用unknown；不增加unresolved scope。
- 摘要权限 / PDF 触发：摘要可初判明确正负例；intersection代表作、输入/真实spike/贡献桥接不明时PDF。
- 最终用途：筛选和主图边界。

### F12. `intersection_directness`

- 目的：记录两种技术实际如何关联。
- 选择类型：single enum。
- 取值及操作性定义：method_coupled=事件输入/表示和SNN接口或系统共同被设计（+SpikePoint摘要；−泛用SNN基准）；event_specific_training_analysis=事件信号与SNN特性共同定义训练/攻击/分析（+raw-event攻击问题；−任意图像增广）；benchmark_only=event数据只检验一般方法（+静态/DVS通用neuron测试；−event slicing loss）；single_axis=只存在一个目标技术轴（+非SNN event graph；−两轴专门耦合）；neither_axis=两轴均不真实（+EHR event；−SNN时间序列方法）。
- 判别例与邻界：benchmark_only不等于exclude；method_coupled不要求发明新neuron，但需接口/系统证据。
- unknown 条件：摘要不能区分专门耦合与普通基准则unknown。
- 摘要权限 / PDF 触发：摘要可初判；benchmark_only与training_analysis冲突必须查方法及消融。
- 最终用途：防止DVS-only污染。

### F13. `contribution_focus`

- 目的：把论文贡献与SNN推理职责分开。
- 选择类型：multi enum。
- 取值及操作性定义：inference_system=推理系统或结构（+detector pipeline；−仅训练loss）；event_interface_design=输入编码/选择/表示机制（+slicer；−普通隐藏层）；neuron_dynamics=神经元状态/发放新机制（+CLIF；−仅使用LIF）；training_method=训练目标/梯度/转换（+SAT/ANN conversion；−只常规训练）；analysis_robustness=分析/攻击/受控检验（+raw-event attack；−无测试的robust宣传）；dataset_benchmark=数据或评测协议为贡献（+DailyDVS；−只是使用数据集）；hardware_system=硬件实现/共同设计为贡献（+实物系统；−SOP估计）；survey_theory=综述或基础理论（+概念依据；−实验网络）。
- 判别例与邻界：多选必须对应作者具体贡献句；不因论文必然有实验就dataset_benchmark。
- unknown 条件：无充分证据unknown。
- 摘要权限 / PDF 触发：摘要能明确贡献；决定primary主次、纯度、硬件机制时PDF。
- 最终用途：章节功能与selection。

### F14. `event_input_source`

- 目的：辨认事件信号的来源。
- 选择类型：multi enum。
- 取值及操作性定义：physical_event_camera=真实contrast-change事件采集（同一数据若属于下述静态图案重采样则优先用sensor_resampled_static，不重复计数）（+DVS实际记录；−光强积分spike camera）；simulated_event_camera=仿真contrast-event信号（+明确event simulator；−Poisson图像编码）；sensor_resampled_static=事件相机扫描静态图案（+明确saccade采集；−纯软件rate coding）；spike_camera=按光强积分发放的spike成像传感器（+Nope-SGS摘要spike camera；−DVS ON/OFF）；noncamera_signal=图像/语音/EHR/图等非event-camera信号（+EHR；−实际event stream）；not_applicable=无实证输入对象的理论/综述（+纯理论；−作者未说明）。
- 判别例与邻界：仿真event允许交叉候选，但必须与真实验证分开。
- unknown 条件：仅neuromorphic dataset或raw spikes未指明来源用unknown；不能凭熟悉的数据集名字补写生成过程。
- 摘要权限 / PDF 触发：明确摘要可；raw/direct、真实/模拟/静态重采样不明须PDF或数据原始权威来源。
- 最终用途：source×generalization。

### F15. `modalities`

- 目的：区分多模态与多表示。
- 选择类型：multi enum。
- 取值及操作性定义：event=目标事件相机信号（+DVS；−EHR事件）；rgb_frame=普通彩色图像（+RGB-event；−event count map）；intensity_frame=灰度/曝光图像（+DAVIS intensity；−time surface）；depth_lidar=深度或LiDAR（+点深度；−xyt event点）；imu=惯性传感（+gyro；−推算速度）；other_signal=其他明确传感输入（+音频需写原文；−未知）；not_applicable=无输入实验。
- 判别例与邻界：同一event流的frame+voxel仅event；训练teacher RGB但测试event-only需不同phase行。
- unknown 条件：input modality缺失用unknown。
- 摘要权限 / PDF 触发：摘要可明确模态；train/test或teacher输入混淆时PDF。
- 最终用途：融合与公平比较。

### F16. `spiking_computation`

- 目的：先证实计算再贴SNN标签。
- 选择类型：single enum。
- 取值及操作性定义：confirmed=状态/发放/重置或等价明确neuron机制得到直接证据（+LIF update+spike传递；−单纯阈值）；claimed=摘要明确称SNN/neuron但机制尚未核对（+fullyspiking标题加摘要声称；−只event-driven）；absent=方法明确为非spiking且已足以回答检查问题（+纯连续state模块；−摘要未提SNN）；unknown=术语或证据冲突不能判断。
- 判别例与邻界：claimed不能支持已验证fullyspiking；连续膜状态本身不否定SNN，关键是是否发放及参与计算。
- unknown 条件：unknown用于无法确认存在或否定，不能以缺词当absent。
- 摘要权限 / PDF 触发：通常摘要只可claimed；明确解释状态/发放也可confirmed但代表作仍PDF；所有模糊spike名称须PDF。
- 最终用途：核心证据门。

### F17. `temporal_organization`

- 目的：事件集合如何形成，不等于tensor格式。
- 选择类型：multi enum。
- 取值及操作性定义：event_by_event=每事件触发逻辑更新，无先等待成组（+单event更新；−packet内顺序扫描）；fixed_duration=固定物理时长分组（+20ms；−5000 events）；fixed_count=固定事件数分组（+N=5000；−固定ms）；adaptive_window=数据/规则/学习改变边界（+spike触发切片；−固定count虽时长变动仍fixed_count）；spatial_local_window=各空间局部有独立分组边界（+patch时间窗；−统一窗后卷积）；whole_sequence=预定义整段clip一次进入，无更细group（+整段点集；−先切片再汇总）；not_applicable=非event输入。
- 判别例与邻界：event_by_event的算法语义不自动证明硬件异步；滑窗重叠、阈值和组长写time_axis_mapping。
- unknown 条件：slicing未给出用unknown。
- 摘要权限 / PDF 触发：除明确摘要的adaptive/event_by_event初判外，窗口、局部/全局、组长通常需PDF。
- 最终用途：延迟/信息损失。

### F18. `representation_form`

- 目的：记录交接给principal feature extractor的结构。
- 选择类型：multi enum。
- 取值及操作性定义：raw_event_sequence=仍是按到达顺序的事件tuple（+地址时间极性流；−采样后无序点集）；event_frame=位置聚合计数/极性图（+2D histogram；−RGB）；time_surface=位置记录最近时间或衰减值（+recency map；−事件计数）；binary_map=窗内事件占据/bit-packed图（+TBR；−neuronal spike输出）；voxel_grid=显式时空bin张量（+B×H×W；−图节点来自voxel但交接为graph）；point_set=事件几何点集合和组（+Event Cloud；−普通LiDAR点）；graph=交接实体有nodes/edges（+event邻接图；−仅kNN grouping）；event_tokens=由raw event/subset直接形成tokens（+group event tokens；−voxel patch embedding）；not_applicable=无event representation。
- 判别例与邻界：多选用于确有并用表示或不同明确交接点；先后变换需time_axis_mapping说明，不能把所有网络层都当输入表示。learned不另作结构类别。
- unknown 条件：dense input未说明frame/voxel时unknown。
- 摘要权限 / PDF 触发：摘要明确结构可初标；token来源、voxel-derived graph、多输入或raw/dense边界需PDF。
- 最终用途：role×representation。

### F19. `representation_properties`

- 目的：防止dense/sparse吞并全部表示信息。
- 选择类型：multi enum。
- 取值及操作性定义：dense_storage=规则全域分配（+dense voxel；−只非空位置）；sparse_storage=仅活跃实体存储（+event节点；−dense里数值为零）；polarity_preserved=极性仍可辨识（+双通道；−丢弃p）；polarity_discarded=明确删除/不可恢复（+仅xyt；−未知）；timestamp_preserved=精确timestamp作为属性保留（+每点t；−仅bin索引）；timestamp_quantized=只有bin/时间段精度（+voxel分桶；−仍另存t）；timestamp_discarded=无时间编码（+纯count无时序；−时间作为坐标）。
- 判别例与邻界：互斥属性仅在同一交接点互斥；多点或多branch需证据指明，不能用timestamp_preserved宣称物理时钟更新。
- unknown 条件：允许部分known；缺的关键属性在evidence_basis记unresolved，整个未知用unknown。
- 摘要权限 / PDF 触发：通常PDF，摘要明确丢弃或保留才可初判。
- 最终用途：信息忠实度与构造成本。

### F20. `representation_learning`

- 目的：构造映射是否被学习。
- 选择类型：multi enum。
- 取值及操作性定义：fixed_rule=计数/分桶等固定映射（+手工voxel；−可学习时间kernel）；learned_mapping=event-to-representation参数被任务优化（+learned aggregation；−普通backbone feature）；learned_selection=事件或group边界/保留由学习控制（+SNN sampler；−固定N）；not_applicable=无event表示。
- 判别例与邻界：同一模型可learned_selection+fixed_rule；neuron在隐藏层可学习不自动learned_mapping。
- unknown 条件：无证据unknown。
- 摘要权限 / PDF 触发：摘要可初判，学习到哪一模块及梯度路径不明须PDF。
- 最终用途：避免复制参考综述learned/dense交叠。

### F21. `event_to_spike_interface`

- 目的：说明camera event怎样影响第一处neuronal spikes。
- 选择类型：multi enum。
- 取值及操作性定义：address_event_injection=事件地址/极性直接驱动神经元输入更新（+每event电流脉冲；−已重采样rate code）；continuous_current=event tensor/feature作为连续电流输入neuron（+voxel→membrane；−它本身已经是spike）；rate_recoding=数值通过概率/次数重编码为spikes（+rate编码点特征；−直接地址输入）；latency_phase_recoding=数值转首次发放时间/phase（+TTFS；−保留事件timestamp坐标）；learned_spike_mapping=可学习映射明确输出传给后续的spikes（+trainable event encoder；−仅continuous embedding）；no_spike_interface=已确认无SNN接口（+非spiking graph；−SNN接口未知）；not_applicable=不处理event-camera输入。
- 判别例与邻界：多选须画清串行/并行；普通LIF第一层不自动另加learned_spike_mapping，需明确encoder模块目标。
- unknown 条件：claimed SNN但未见输入映射一律unknown。
- 摘要权限 / PDF 触发：原文明确接口可abstract初判；raw/直接输入、rate vs physical timing、代表作须PDF。
- 最终用途：核心signal图。

### F22. `primary_functional_role`

- 目的：一个主要机制贡献的SNN功能。
- 选择类型：single enum。
- 取值及操作性定义：event_interface=SNN交付事件选择/切片/显式表示至主特征提取器（+独立sampler；−普通hidden feature）；task_network=SNN承担主要任务特征提取与推理路径（+point SNN backbone；−仅局部head）；embedded_module=主要系统中局部SNN特征/记忆/融合/head（+ANN中SNN支路；−主干SNN仅终端读出连续）；algorithmic_engine=spike dynamics明确对应算法变量与推断/优化步骤且为核心贡献（+WTA/EM；−SGD训练网络）；not_applicable=该论文没有新推理SNN role需要归类（+training-only/背景；−角色不明确）。
- 判别例与邻界：同一个hybrid系统也可能task_network；选择准则见决策树，不按参数量/标题/最后输出层裁决。
- unknown 条件：两个角色都有充分理由但主次无法证实时unknown；taxonomy_issue保留备选。
- 摘要权限 / PDF 触发：摘要可给暂定角色；所有pilot真实交叉primary与双role争议需PDF。
- 最终用途：主taxonomy候选叶子。

### F23. `secondary_functional_roles`

- 目的：保留实际独立SNN职责而不多算论文。
- 选择类型：multi enum。
- 取值及操作性定义：使用primary_functional_role中四个实质role；none=没有额外独立role（+只有任务主干；−未看方法）；unknown=是否额外角色不明。不得含not_applicable。
- 判别例与邻界：正：sampler+backbone明确两模块时primary interface、secondary task_network；反：把任何第一层都增标interface。
- unknown 条件：未查各模块可unknown；不要与none同选。
- 摘要权限 / PDF 触发：摘要可暂记；角色交接和模块独立性需PDF。
- 最终用途：叠加role图与冲突报告。

### F24. `primary_role_reason`

- 目的：提供primary可复现的裁决链。
- 选择类型：single text。
- 取值及操作性定义：必须写SNN输入→输出、位置、主要贡献证据、一个最接近备选及其被排除的机制理由；not_applicable必须解释贡献为什么不在新推理拓扑。
- 判别例与邻界：正：输出是切片触发信号交给独立ANN，主要消融针对切片，故interface而非task_network；反：这篇主要是SNN。
- unknown 条件：可写尚缺哪个交接/主次证据，不能只写unknown。
- 摘要权限 / PDF 触发：依据相关abstract/PDF；缺主次依据时PDF并保留unknown role。
- 最终用途：审稿可解释性。

### F25. `snn_module_functions`

- 目的：局部SNN模块在做什么，与主要role解耦。
- 选择类型：multi enum。
- 取值及操作性定义：encoding_selection=编码/过滤/选择（+spike gate；−ANN门控）；feature_extraction=任务特征（+SNNconv；−输入计数）；temporal_filter_memory=随时间保留/过滤（+spiking memory；−SSM连续状态）；attention_routing=注意力或路由（+spiking attention；−softmax模块未spiking）；fusion=合并尺度/模态（+SNN fusion；−只是两个输入）；task_head=从features预测（+SNNregressor；−主feature extractor）；algorithm_update=算法状态或局部可塑性更新（+EM对应；−普通优化训练）；none=确认无SNN模块。
- 判别例与邻界：multi标签必须附模块名；activation不是独立role，定位在此和neuron字段。
- unknown 条件：模块位置或是否spiking不明用unknown。
- 摘要权限 / PDF 触发：明确摘要可初判；完整module map需PDF。
- 最终用途：局部模块比较。

### F26. `spiking_boundary_map`

- 目的：显式描述哪部分真正spiking。
- 选择类型：single JSON object。
- 取值及操作性定义：固定键 input_preprocess,backbone,fusion,head,readout；每键对象含status和detail。status仅 all_spiking=该范围所有学习计算通过spiking信号完成（+已查算子；−只名称fully）；mixed=同范围含SNN及连续学习算子（+混合注意力；−neuron连续膜态本身）；non_spiking=只有连续或非SNN计算（+ANNhead；−膜电位）；absent=该范围在系统中不存在（+单模态无fusion；−未说明）；unknown=未核查。detail必须列模块、信号及例外，连续BN/softmax/FFT/residual、膜态readout等不能省略。
- 判别例与邻界：正：backbone all_spiking / head non_spiking / readout non_spiking；反：一句fullyspiking覆盖全部。
- unknown 条件：每部分可unknown，不能从backbone外推；只写absent需证据。
- 摘要权限 / PDF 触发：必须PDF才能关闭central boundary；摘要只记录作者claim。
- 最终用途：purity comparison table。

### F27. `spiking_extent`

- 目的：按核查范围导出最强可支持的表述。
- 选择类型：single enum。
- 取值及操作性定义：end_to_end_spiking_pipeline=输入预处理到最终输出的计算均经核查符合spiking且无连续外部计算例外（+全管线检查；−external FPGA/ANN decode）；fully_spiking_task_network=所有学习task layers含head/fusion均spiking，但输入构造/终端非学习数值读出另列（+spikinghead+countreadout；−ANNhead）；fully_spiking_backbone=主干全spiking，head/fusion或外部pipeline未达到task条件（+SNNbackbone+ANNhead；−只有前端SNN）；hybrid_subnetwork=真实SNN与ANN/连续模块混合且主干也未全spiking（+混合backbone；−纯SNNbackbone只外部读出）；non_spiking=全方法无SNN；not_applicable=无具体inference模型。
- 判别例与邻界：取已验证的最高范围，不把三个fully标签全选；最终连续输出是否来自非学习readout必须披露。
- unknown 条件：边界缺失或作者纯度声称未核查用unknown；不能降级为“肯定hybrid”。
- 摘要权限 / PDF 触发：需PDF；abstract-only不能给verified fully值。
- 最终用途：边界而非training分类。

### F28. `spiking_signal`

- 目的：避免binary、integer、多次发放混淆。
- 选择类型：multi enum。
- 取值及操作性定义：binary=单更新0/1发放（+标准LIF；−多级activation）；signed_binary=有符号单脉冲（+−1/0/+1；−polarity仅输入属性）；burst_count=一次窗口多次二值发放以计数表征（+burst序列；−单个连续幅度）；integer_multilevel=离散多级发放值（+integer spike inference；−仅训练时整数）；continuous_only=已确认无离散神经发放（+PPLN实值输出；−SNN膜态）；not_applicable=无模型信号。
- 判别例与邻界：training与inference不同必须分phase/variant或详细标明；DI-LIF整数训练不能推断inference也整数。
- unknown 条件：“spike”未定义时unknown。
- 摘要权限 / PDF 触发：通常PDF/neuron equation；摘要直接描述也只是待核对。
- 最终用途：signal coding与硬件。

### F29. `architecture_family`

- 目的：描述算子/结构家族，不取代role。
- 选择类型：multi enum。
- 取值及操作性定义：conv_residual=卷积及残差（+convSNN；−点集MLP仅名字Res）；recurrent=显式recurrent连接/循环模块（+RNN层；−LIF自身膜记忆）；transformer_attention=attention/token interaction（+spikingattention；−任意gating）；mixer=明确token/channel混合器（+MLPmixer；−泛称fusion）；point_network=点邻域抽样/聚合（+点层级；−densevoxel）；graph_network=图邻接messagepassing（+GNN；−kNNgroup后pool）；state_space=显式SSM算子（+HiPPOstate；−LIF被泛称state）；algorithmic_circuit=为算法组成的竞争/反馈网络（+WTAcircuit；−任意CNN）；other_documented=证据明确但不属以上（+给结构原名并建issue；−为绕过unknown随填）；not_applicable=无模型。
- 判别例与邻界：other_documented是固定逃逸标签，不授权自造family；要交Astra处理。
- unknown 条件：只“network”不明时unknown。
- 摘要权限 / PDF 触发：明确abstract可；spiking子模块与whole-system family分别在证据路径中标明，复杂组合需PDF。
- 最终用途：architecture横向表。

### F30. `neuron_family`

- 目的：记录神经元类型而非架构。
- 选择类型：multi enum。
- 取值及操作性定义：if=无leak的积分发放（+IF式；−LIF）；lif=固定leak积分发放（+固定tau；−learnabletau）；adaptive_lif=leak/threshold/adaptation可学习或随状态改变（+PLIF/gatedLIF，保留原名；−固定tau）；multi_state_neuron=多个明确耦合神经内部状态（+CLIF额外state；−普通LIF膜态）；other_documented=有真实发放的其他方程（+明确随机neuron；−仅类脑称呼）；not_applicable=确认无spiking neuron。
- 判别例与邻界：允许adaptive_lif+multi_state_neuron；CLIF原名写证据而不是不断扩字典；模型别名不构成判据。
- unknown 条件：SNN存在但type未给用unknown。
- 摘要权限 / PDF 触发：明确neuron名称abstract可暂标，方程、额外state、clock需PDF。
- 最终用途：neuron比较。

### F31. `internal_state`

- 目的：神经或系统保留的具体状态。
- 选择类型：multi enum。
- 取值及操作性定义：membrane=积分电位（+v_t；−普通feature称membrane）；synaptic_current=独立突触current状态（+i_t动态；−当前输入张量）；threshold_adaptation=阈值历史/适应状态（+动态theta；−固定threshold参数）；auxiliary_neural_state=神经额外记忆/互补状态（+CLIFcomp；−普通attentioncache）；network_memory=跨输入的网络级记忆（+SSMhidden需注明continuous；−只中间张量）；plastic_weight=在线学习权重作为推断状态（+EM/STDP更新；−离线权重）；none=已确认无跨更新状态。
- 判别例与邻界：连续state与spike communication可共存；不要把network_memory一律当neuron。
- unknown 条件：缺方程或reset信息用unknown。
- 摘要权限 / PDF 触发：通常PDF；不凭LIF惯例补公式。
- 最终用途：state位置与memorycost。

### F32. `temporal_mechanism`

- 目的：描述时间处理机制。
- 选择类型：multi enum。
- 取值及操作性定义：integration_decay=状态累积泄漏（+积分方程；−静态聚合）；recurrence_feedback=跨更新反馈（+recurrentconnection；−前馈深度）；delay=显式延迟（+learned synapticdelay；−普通网络耗时）；multi_timescale=多个明确时间尺度（+不同tau/快慢分支；−层数多）；temporal_attention=跨时间交互（+time-axisattention；−仅空间attention）；adaptive_update=依据事件/状态改变更新时机（+selectiveupdate；−固定count）；iterative_dynamics=算法迭代（+spikecodedISTA；−simulation步自然存在）；none=明确无时间机制。
- 判别例与邻界：多选需每项证据；时间机制不是训练credit assignment。
- unknown 条件：摘要泛说temporal建unknown；关键维度待PDF。
- 摘要权限 / PDF 触发：明确abstract可暂标；物理时间/仿真步/深度关系须PDF。
- 最终用途：role内机制差异。

### F33. `time_axis_mapping`

- 目的：强制拆开三个时间轴及状态重置。
- 选择类型：single JSON object。
- 取值及操作性定义：固定键 physical_event_time,event_group_order,snn_simulation_timestep,mapping,state_reset,lookahead；值为带单位/顺序/关系的文本或unknown/not_applicable。mapping必须写 t_event→group_j→step_k，不能默认一一映射；lookahead记录因果/未来窗口/双向访问。
- 判别例与邻界：正：timestamps用于坐标，group按时间排序，每group另运行T步，T无物理ms等价；反：T=16所以16ms。
- unknown 条件：每键可unknown；没有sim step时not_applicable需说明真正连续事件更新。
- 摘要权限 / PDF 触发：完整映射原则上PDF；摘要明确event-by-event只是初始线索。
- 最终用途：时间与延迟比较。

### F34. `training_route`

- 目的：区分训练过程与推理纯度。
- 选择类型：single enum。
- 取值及操作性定义：direct_snn=以spiking模型为训练目标并直接优化（+SG训练；−ANN权重转换）；ann_to_snn=先训练/取得ANN，再转换校准为SNN（+thresholdbalance；−训练用ANNteacher）；conversion_then_finetune=转换后再训练SNN（+转换+SGfine-tune；−只校准）；joint_ann_snn=ANN和SNN部件作为混合系统联合训练（+端到端hybrid；−独立ANN转全SNN）；integer_train_spike_infer=以integer/multi-level训练图映射到spike推理且未构成传统ANN预训练转换（+明确integertrain；−只因为多阈值便推断conversion）；local_adaptive=无上述全局预训练路径，局部可塑性/在线适应构成学习（+STDP推断；−SGD在线）；no_training=固定权重或解析构造无需学习；not_applicable=无训练方法对象。
- 判别例与邻界：若联合hybrid中含转换子模块而无法单一归类，先拆variant/描述phase；仍不合则unknown+issue，不能多选含混训练路径。
- unknown 条件：摘要“trained SNN”不足区分时unknown。
- 摘要权限 / PDF 触发：明确abstract可暂判；转换/混合/整数训练边界须PDF训练section。
- 最终用途：training横向轴，永不作primaryrole。

### F35. `learning_signal`

- 目的：监督来源，不等于gradient算法。
- 选择类型：multi enum。
- 取值及操作性定义：supervised=外部标签（+分类label；−自监督重建）；self_supervised=由输入/物理一致性自生成目标（+contrastloss；−人工标注）；unsupervised_local=无目标标签的局部统计学习（+无监督STDP；−supervisedSTDP）；distillation=teacher输出/feature指导（+ANNteacher；−ANNconversion本身）；reinforcement=reward驱动（+rewardmodulatedlearning；−普通lossfeedback）；not_applicable=无学习。
- 判别例与邻界：supervised与distillation可同时存在；learning_signal不表示是否spiking。
- unknown 条件：目标来源不明unknown。
- 摘要权限 / PDF 触发：abstract明确可；多loss来源或teacherphase需PDF。
- 最终用途：learning comparison。

### F36. `credit_assignment`

- 目的：优化梯度/局部更新如何传递。
- 选择类型：multi enum。
- 取值及操作性定义：surrogate_bptt=替代spike梯度加跨步反传（+STBP；−仅SG未明时间反传）；surrogate_other=明确SG但非完整BPTT或尚只确认SG（+onlineSG需注明；−用backprop就猜SG）；local_plasticity=局部活动决定更新（+STDP；−全局SG）；analytic_conversion=解析/校准参数映射（+阈值平衡；−teacherloss）；ordinary_gradient=对连续计算普通求导（+ANNpart；−真实spike不连续处未经说明）；gradient_free=无梯度搜索/演化（+evolution；−analyticmapping）；not_applicable=无学习。
- 判别例与邻界：surrogate_other若仅因BPTT细节待查，evidence里注明未定，不可被表述为已确认online。
- unknown 条件：未说明优化用unknown。
- 摘要权限 / PDF 触发：摘要明确SG可surrogate_other；BPTT/local/online和stability需PDF。
- 最终用途：时间信用分配。

### F37. `task`

- 目的：组织任务证据，非primary role。
- 选择类型：multi enum。
- 取值及操作性定义：recognition=类别/身份/动作判断（+action/gait；−目标框）；detection=位置及类别目标集合（+boxes；−模板跟踪）；tracking=跨时刻持续目标状态（+template-search；−单帧检测）；reconstruction_restoration=图像/视频恢复（+deblur；−光流预测）；pose=相机/人体位姿（+6DoF；−depth）；depth=距离/视差（+depthmap；−flow）；flow_motion=像素/事件运动向量或场（+opticalflow；−motionmask）；segmentation=像素/事件标签（+motionsegmentation；−单label）；other_documented=其他明确任务须issue；not_applicable=无具体task。
- 判别例与邻界：动作分类不叫tracking；motionsegmentation可主segmentation，只有独立flow指标才加flow_motion。
- unknown 条件：摘要不够unknown。
- 摘要权限 / PDF 触发：abstract通常可，joint任务与实际评测输出不一致须PDF。
- 最终用途：task×role证据表。

### F38. `output`

- 目的：记录预测对象而非任务名。
- 选择类型：multi enum。
- 取值及操作性定义：class_identity=类/身份分数（+classlogits；−features）；boxes_trajectories=框或轨迹（+trackerboxes；−eventgroups）；image_video=恢复像素（+grayscale；−voxel）；pose_coordinates=姿态坐标/矩阵（+6DoF；−深度）；depth_disparity=深度视差值（+densemap；−z不是深度的time坐标）；motion_vectors=flow向量（+u/v；−运动mask）；labels_masks=逐像素/事件标签（+motionsegmask；−globalclass）；representation_control=供下游使用的表示/切片决定（+slicingtrigger；−最终class）；analysis_metric=分析/攻击/benchmark产物（+扰动评估；−常规task输出）；other_documented=明确未涵盖输出须issue；not_applicable=无输出对象。
- 判别例与邻界：annotationunit对应主贡献模块可同时输出representation_control与系统task，但需说明层级。
- unknown 条件：输出对象未明确unknown。
- 摘要权限 / PDF 触发：abstract可；latent输出与系统readout不清需PDF。
- 最终用途：pipeline终点。

### F39. `dataset_evaluation`

- 目的：把数据、配置、协议绑在同一证据单元。
- 选择类型：multi JSON array。
- 取值及操作性定义：每个对象固定键 dataset_name,version,split,setting,modality,window,timesteps,metric,configuration,evidence_id。setting仅 in_domain=同分布测试；cross_domain=跨域；cross_subject=跨人；cross_sensor=跨sensor；sim_to_real=仿真到真实；online_stream=流式在线；other_documented=需描述；unknown；not_applicable。其他值为原文/数字带单位或unknown。dataset_name为官方原名，不允许Sol自造缩写。
- 判别例与邻界：正：dataset+split+配置+metric定义关联；反：把不同split的最佳结果并排当公平比较。
- unknown 条件：每项可以unknown；不可据常识补标准split；没有评测则not_applicable。
- 摘要权限 / PDF 触发：摘要可列明确dataset；关键结论、protocol、数值必须PDF/authority。
- 最终用途：task结果表与authority筛选。

### F40. `efficiency_evidence`

- 目的：区别宣称、代理与实测。
- 选择类型：multi enum。
- 取值及操作性定义：claim_only=只有低能耗/实时宣称（+abstract宣称；−有测量）；operation_count=操作数量无能耗模型（+MAC/SOP总数；−实测J）；sop_mac_energy_proxy=按SOP/MAC成本换算能量（+pJ×ops；−power测量）；analytical_memory_energy=计入bitwidth/memory模型（+STEP分析模型；−测GPUmemory）；runtime_measurement=实测时延/吞吐（+GPUms；−1/frequency估算）；memory_measurement=实测运行/训练内存（+peakVRAM；−参数量）；conventional_device_energy=非neuromorphic设备实测功率/能量（+GPUpower；−SOP能量）；neuromorphic_measurement=neuromorphic芯片实测（+片上功耗/延迟；−仅chip映射推算）；hardware_projection=硬件模型/模拟/借用测量推算（+FPGA估算；−本系统实测）；activity_proxy=spike率/稀疏度/参数量（+firingrate；−自动称省能）；none=明确未提供效率证据。
- 判别例与邻界：可多选，claim_only只有未定位支持时使用；查到实证后按证据替换/保留其他未证实claim到details。芯片上的SNNblock不等于全系统。
- unknown 条件：未查实验用unknown，不等于none。
- 摘要权限 / PDF 触发：只要声称event-driven/asynchronous/low-power/hardware-efficient须PDF，摘要的数字不是已验证测量。
- 最终用途：claim-evidence效率表。

### F41. `efficiency_claim_details`

- 目的：限定每项效率证据的分母和系统范围。
- 选择类型：multi JSON array。
- 取值及操作性定义：固定键 claim,kind,metric,value,unit,device,boundary,baseline,accuracy_setting,window_and_timestep,preprocessing,memory_io,measurement_setup,evidence_id；kind使用efficiency_evidence实质标签。其它字段原文/数字或unknown。
- 判别例与邻界：正：SNN block能耗，不含host ANN和I/O；反：把它称sensor-to-result energy。
- unknown 条件：不报告数字可value=not_applicable；未说明成本项=unknown而非0。
- 摘要权限 / PDF 触发：一切拟写综述的定量结论必须查PDF表/设置/附录。
- 最终用途：可审计efficiency结论。

### F42. `robustness_evidence`

- 目的：区分鲁棒证据的威胁和分布。
- 选择类型：multi enum。
- 取值及操作性定义：noise_test=传感/输入噪声测试（+eventdropnoise；−口头robust）；lighting_motion_shift=光照/速度/运动条件变化测试（+低光分组；−训练aug）；domain_transfer=跨域/sensor/generalization（+simtoreal；−随机同域split）；temporal_perturbation=时间窗/retiming/顺序扰动（+jitter；−普通neuron时间步实验无输入扰动）；adversarial=明确攻击及预算（+rawevent attack；−随机噪声）；timestep_transfer=训练/推理T变化测试（+mixedT；−只一个T）；claim_only=只有宣称无检查证据；none=检查后无相关证据。
- 判别例与邻界：augmentation本身不证明generalization；传感noise和adversarial预算不可互换。
- unknown 条件：未查实验unknown。
- 摘要权限 / PDF 触发：摘要可识别测试意图；实际robustness结论/威胁空间/数值须PDF。
- 最终用途：风险与泛化比较。

### F43. `taxonomy_placement`

- 目的：把事实role映射到待验证的写作视图。
- 选择类型：single enum。
- 取值及操作性定义：role_hypothesis=真实intersection且新inference role有足够证据（+pipeline方法；−training-only）；cross_cutting=intersection训练/分析或角色尚不宜组织章节（+EventRPG；−强塞新role）；foundation_comparison=单轴解释/比较（+genericneuron；−仅DVS即入主图）；outside=已明确无本综述论证位置（+EHR；−信息不足）；pending=等待机制或Astra裁决。
- 判别例与邻界：这只是placement层，不是另一个primary taxonomy，不能填旧outline章节号。
- unknown 条件：用pending而非unknown；不清楚保持pending。
- 摘要权限 / PDF 触发：随scope/role证据；代表作必须PDF。
- 最终用途：生成主图/表入口。

### F44. `taxonomy_issue`

- 目的：受控问题队列，不允许发明标签。
- 选择类型：multi JSON array。
- 取值及操作性定义：每项固定键 issue_id,type,field,alternatives,question,evidence_ids,owner,status。type仅 scope_conflict,role_conflict,boundary_conflict,time_conflict,missing_label,metadata_conflict,evidence_conflict,selection_conflict；均以字面对象命名。owner=astra/sol_high；status=open/evidence_ready/resolved/deferred。alternatives只能已定义标签；未覆盖机制用原文描述。无issue写[]。
- 判别例与邻界：正：role_conflict比较interface/module并附具体交接问题；反：自由新增role叫spikingactivation。
- unknown 条件：无须unknown；真实未解决就是open，不能用空列表隐藏。
- 摘要权限 / PDF 触发：Sol High查事实，Astra改规则；PDF无法解决规则冲突仍需Astra。
- 最终用途：checkpoint输入。

### F45. `selection_status`

- 目的：表达reading/纳排状态，不改scope事实。
- 选择类型：single enum。
- 取值及操作性定义：pending=用途/证据未决；proposed_usable=执行者建议可用尚待Astra裁剪；usable=用户批准流程中Astra最终认可；reference_only=保留检索但当前不计usable；excluded=范围错误/无用途已证实。
- 判别例与邻界：正：重复交叉论文core_intersection+reference_only；反：为了凑180改变scope。
- unknown 条件：用pending不用unknown。
- 摘要权限 / PDF 触发：摘要可清楚负例；usable中央机制/关键数值必须PDF。本轮不写任何真实行。
- 最终用途：150–180裁剪。

### F46. `inclusion_tier`

- 目的：记录具体论证职责并保留非纳入原因。
- 选择类型：multi enum。
- 取值及操作性定义：core_taxonomy_evidence=直接支撑方法结构差异（+role代表；−只有DVS结果）；indispensable_background=解释特定交叉机制无法省的基础（+所用spike训练原理；−泛SNN综述大全）；representative_comparator=受控比较/关键反例（+同任务非SNN异步基线；−任意SOTA）；evaluation_authority=数据/协议/效率评测定义（+正式dataset；−只是用dataset）；historical_foundation=可定位的关键前驱（+原始机制论文；−旧但无后续关系）；redundant_reference=论证被已有同等证据覆盖（+重复版本；−不可替代反例）；excluded_paper=确定无scope/use（+EHR）；pending=未定。
- 判别例与邻界：前五可多选；后三与其它值互斥。tier无数量配额，不同于旧Core。
- unknown 条件：用pending不用unknown。
- 摘要权限 / PDF 触发：背景/comparator初筛可abstract，indispensable机制关系或数字需PDF。
- 最终用途：selectionledger。

### F47. `concrete_survey_use`

- 目的：明确这篇在综述支撑什么。
- 选择类型：single text。
- 取值及操作性定义：必须给出可证伪claim、拟放视图/段落功能、最近替代论文ID及不可替代差异；没有合格用途时说明缺什么，不写假用途。
- 判别例与邻界：正：用于区分SNNblock硬件测量与host剩余计算，和仅SOP估计形成反例；反：重要背景。
- unknown 条件：可写待解决的用途问题；不能空白。
- 摘要权限 / PDF 触发：abstract可以初步定位用途，关键claim须PDF。
- 最终用途：claim-evidence-citation。

### F48. `inclusion_reason`

- 目的：给纳入建议的具体机制理由。
- 选择类型：single text。
- 取值及操作性定义：proposed_usable/usable必须包含目标轴联系、方法/证据差异、删除后缺失的论证；其它状态可not_applicable。
- 判别例与邻界：正：提供独立spike触发切片机制，补足现有backbone论文未回答的边界选择；反：相关。
- unknown 条件：pending需说明待查项；不可只unknown。
- 摘要权限 / PDF 触发：跟随用途证据，Astra最终确认。
- 最终用途：裁剪可追溯。

### F49. `exclusion_reason`

- 目的：区分范围错误与冗余。
- 选择类型：single text。
- 取值及操作性定义：excluded/reference_only必填明确signal/mechanism/use/duplicate原因与最近替代ID（适用时）；proposed/usable用not_applicable。
- 判别例与邻界：正：输入为光强积分spike camera，未涉及contrast-event信号；反：不是Core所以exclude。
- unknown 条件：pending写尚缺证据不能排除；不允许用lowconfidence自动exclude。
- 摘要权限 / PDF 触发：明确abstract负例可；未知spiking或metadata冲突需PDF。
- 最终用途：排除审计。

### F50. `duplicate_family`

- 目的：在版本与方法层去重。
- 选择类型：single text。
- 取值及操作性定义：稳定canonical work family ID；无已知重复用same_as_paper_id；有关联则用批准的代表paper_id或registered family key。
- 判别例与邻界：正：conference/journal同方法共享family并记录增量；反：同名SpikeTrack强并。
- unknown 条件：是否重复未知用unknown并issue，不能最终计数。
- 摘要权限 / PDF 触发：metadata可初筛，同名/扩刊增量要查PDF。
- 最终用途：唯一usable计数。

### F51. `evidence_quote_or_paraphrase`

- 目的：保存可核查支持内容。
- 选择类型：multi JSON array。
- 取值及操作性定义：每项固定键 evidence_id,field_path,value,mode,text；mode仅quote=逐字原文/paraphrase=忠实转述。field_path可指CSV字段或nested路径，value对应被支持值。每个决定性标签各有证据，允许一条支持多字段但需显式列出。
- 判别例与邻界：正：引述spike trigger后忠实说明控制窗口；反：作者未说的neuron公式。
- unknown 条件：不能确定的text写具体缺口并配unresolved basis，不能虚构引文。
- 摘要权限 / PDF 触发：摘要是最低证据；PDF-check通过后添加PDF证据，保留初判历史。
- 最终用途：所有事实来源。

### F52. `evidence_location`

- 目的：将每条证据绑定准确位置。
- 选择类型：multi JSON array。
- 取值及操作性定义：每项固定键 evidence_id,source_ref,location；source_ref链接official_source或具体原始文件；location用abstract完整句号序号/段、PDF物理页+section+figure/equation/table；作者印刷页与PDF页不同须说明。
- 判别例与邻界：正：PDF p.5 §3.2 Eq.(4)；反：Method（无页无定位）。
- unknown 条件：引用尚未拿到写unknown并pdf_check_status待处理；不能算验证完成。
- 摘要权限 / PDF 触发：不可凭模型记忆造页码；图/公式抽取损坏须看页面。
- 最终用途：复现审计。

### F53. `evidence_basis`

- 目的：区分来源与论断性质。
- 选择类型：multi JSON array。
- 取值及操作性定义：每项固定键 evidence_id,source_type,nature。source_type仅 official_abstract,pdf_main,pdf_appendix,official_metadata,repository_locator,inference,unresolved；nature仅 author_claim,method_description,empirical_observation,metadata_fact,reasoned_inference,unresolved。repository_locator只能导航；inference必须写前提，不能充当真实neuron或关键数值直接证据。
- 判别例与邻界：正：摘要power数字=official_abstract+author_claim；PDF测量表=pdf_main+empirical_observation；反：PDF里作者宣称就一律实验证明。
- unknown 条件：无来源/冲突未解用unresolved；不抹去相反证据。
- 摘要权限 / PDF 触发：任何来源都可记录；正式core标签需相应直接证据。
- 最终用途：证据权重与风险。

### F54. `confidence`

- 目的：逐字段置信度，不能平均掩盖关键未知。
- 选择类型：single JSON object。
- 取值及操作性定义：键为field_path另加overall；值仅 high=直接且定位充分、无未解冲突；medium=明确摘要/局部证据足够暂定但范围待核；low=有理由的暂定推断/冲突；unknown=关键证据缺失。overall取scope、spiking_computation、primary_functional_role、spiking_extent、selection_status中适用字段的最低置信度；不适用项不计。
- 判别例与邻界：正：task high但boundary unknown则overall unknown；反：多数元数据确定所以整篇high。
- unknown 条件：允许unknown；unknown不等于excluded。
- 摘要权限 / PDF 触发：不能仅因阅读了PDF整体升high；必须按字段。
- 最终用途：QC抽样和High路由。

### F55. `needs_pdf_check`

- 目的：表示是否有尚需PDF回答的具体问题。
- 选择类型：single enum。
- 取值及操作性定义：yes=至少一个必要问题未关闭（+neuron不明）；no=问题已关闭或摘要足以明确负例且无主张要核（+EHRscope）；不能unknown。
- 判别例与邻界：旧audit no不传递；检查后仍未解决就是yes。
- unknown 条件：执行时必须确定yes/no；信息缺失默认yes并写问题。
- 摘要权限 / PDF 触发：yes由触发器导出；abstract-only清楚negative可以no。
- 最终用途：调度。

### F56. `pdf_check_question`

- 目的：把check变成具体问句。
- 选择类型：multi JSON array。
- 取值及操作性定义：每项固定键 question_id,field,question,target_section,trigger,answer,evidence_ids；trigger仅 input_identity,real_neuron,purity,role_location,neuron_state_time,representative,efficiency_claim,quantitative_claim,source_conflict,multiple_roles,misleading_terms,version_conflict。answer在未查时pending；无问题写[]。
- 判别例与邻界：正：GTP输出之后第一层输入是连续frame还是neuronalspikes？查Fig/Method；反：全文看看。
- unknown 条件：未看PDF也必须能提出可回答问题；不允许孤立unknown。
- 摘要权限 / PDF 触发：与yes和status逐题一致，读图→Method→方程→训练/实验/附录。
- 最终用途：定向阅读预算。

### F57. `pdf_check_status`

- 目的：保留已查但未解决的状态。
- 选择类型：single enum。
- 取值及操作性定义：not_required=无触发问题且摘要足以当前决定；pending=尚未开始必要PDF；partial=检查了一部分仍有未答；resolved=必要问题均有直接证据或明确not_reported并经裁决；unavailable=无法取得指定PDF版本。
- 判别例与邻界：resolved可保留非关键unknown，但criticalunknown不能宣告role已确定；unavailable不可自动exclude。
- unknown 条件：不允许unknown；可选择pending/unavailable。
- 摘要权限 / PDF 触发：状态来自执行记录。
- 最终用途：completion coverage。

### F58. `annotator`

- 目的：记录真实执行模型/人和时间。
- 选择类型：single text。
- 取值及操作性定义：实际model名称、reasoning设置、run/date；未调用不得声称另一模型完成。
- 判别例与邻界：正：Sol High / 实际run/date；反：设计阶段预写Sol完成。
- unknown 条件：执行后不允许unknown，未执行不创建行。
- 摘要权限 / PDF 触发：不需PDF。
- 最终用途：handoff审计。

### F59. `review_status`

- 目的：区分机器初判、复读与Astra裁决。
- 选择类型：single enum。
- 取值及操作性定义：draft=未过完整校验；self_checked=执行者已检；blind_rechecked=第二次独立复判并保留初判；astra_adjudicated=Astra已裁决且有issue记录；blocked=因来源/规则不能完成。
- 判别例与邻界：blind重读不宣称多个人类间一致性；Astra裁决不自动冻结finaltaxonomy。
- unknown 条件：不允许unknown，尚未检查用draft。
- 摘要权限 / PDF 触发：不需额外PDF除发现新问题。
- 最终用途：QC门禁。

## E. 嵌套记录与辅助词表

JSON允许的key已在字段逐一列出。不能在CSV外维护一套未记录的隐式证据。每条evidence_id必须在quote/paraphrase、location、basis三处连接；pdf questions引用同一ID；confidence使用稳定field_path。metadata原文名称、page URL、日期、metric及单位是来源转录，不是新taxonomy标签。

| 辅助词表 | 定义与正/反例 |
| --- | --- |
| source_type | official_abstract=官方完整摘要（正：audit原文；反：card概述）；pdf_main=原始论文正文（正：Method页；反：旧V2）；pdf_appendix=该版本附录/补充（正：实现附录；反：其它版本）；official_metadata=出版来源身份数据（正：正式题名；反：算法推断）；repository_locator=仓库笔记导航（正：V2指出Eq位置；反：当直接PDF证据）；inference=明确前提下的研究者推断（正：比较可能的边界；反：补写LIF）；unresolved=证据缺失/矛盾（正：未见head；反：已确认无head）。 |
| nature | author_claim=作者声称但未核查支持（正：摘要“低功耗”；反：本地实测）；method_description=原文定义（正：state方程；反：是否最好）；empirical_observation=具体设置下实验结果（正：表中指定配置结果；反：普遍更高效）；metadata_fact=身份事实（正：venue；反：scope）；reasoned_inference=推断（正：可能来自窗口差异；反：当直接因果）；unresolved=尚无可支持内容（正：缺公式；反：已明确未报告）。 |
| evaluation setting | in_domain=训练测试目标域相同（正：指定同域split；反：跨sensor）；cross_domain=测试域不同（正：不同环境域；反：随机split）；cross_subject=身份分离（正：train/test人员不同；反：同人随机clip）；cross_sensor=sensor跨设备类型（正：相机迁移；反：同设备不同序列）；sim_to_real=模拟训练真实测试（正：显式迁移；反：模拟内测试）；online_stream=连续流式评估（正：因果逐事件；反：offline clip）；other_documented=明确额外设置并提出issue；unknown=原文不足；not_applicable=无实验。一个配置可需多个setting时拆相同dataset的设置记录，不拼成新标签。 |
| issue type | scope_conflict=目标轴归属（正：DVS-only；反：训练路线）；role_conflict=功能主次（正：interface/module）；boundary_conflict=计算范围（正：head连续）；time_conflict=时间轴或reset（正：T含义）；missing_label=已证实机制无标签（反：没读懂）；metadata_conflict=版本/身份（正：同名论文）；evidence_conflict=原始材料相反（正：摘要和Method冲突）；selection_conflict=独立用途/冗余（正：版本重复）。类型只负责路由，不是新scope。 |
| issue owner/status | sol_high=可按规则通过查证解决事实；astra=规则/类别/纳排架构裁决。open=问题未解决；evidence_ready=证据齐待裁决；resolved=有明确答案和依据；deferred=正式延期且有理由，仍计未解决，不算成功清零。 |
| question trigger | input_identity=传感输入；real_neuron=真实spike；purity=纯度边界；role_location=SNN位置；neuron_state_time=方程/状态/时间；representative=taxonomy代表作；efficiency_claim=异步/效率主张；quantitative_claim=拟引用数字；source_conflict=摘要与仓库或原文冲突；multiple_roles=多个primary候选；misleading_terms=spike/event语义；version_conflict=版本。每项的正例是对应字段有具体未答问题；反例是无目的“全文精读”。 |

以下是**合成的字段格式示例，非任何真实论文 annotation**；不写入本轮header-only CSV：

```json
{
  "evidence_quote_or_paraphrase": [{"evidence_id":"E1","field_path":"primary_functional_role","value":"event_interface","mode":"paraphrase","text":"示例：神经元发放只触发事件窗口结束，窗口交给独立分类器。"}],
  "evidence_location": [{"evidence_id":"E1","source_ref":"synthetic_example","location":"synthetic example; not a paper citation"}],
  "evidence_basis": [{"evidence_id":"E1","source_type":"inference","nature":"reasoned_inference"}],
  "confidence": {"primary_functional_role":"low","overall":"unknown"}
}
```

此例仅演示JSON连接方式，不可因示例有标签便当gold label。对于真实数据，不得使用synthetic_example作为来源。

## F. PDF-check protocol

触发规则是or关系，**不要求全部572篇全文精读**。所有论文最低读取完整官方title/abstract；以下任一条件存在就建立有字段和目标位置的具体问题：

1. 真实输入源/形式不明；camera event与spike-camera/neuromorphic benchmark易混；raw/direct只是宣传。
2. 存在真实spiking neuron不明；threshold/stateful/sparse/bio-inspired不足；方法名含spike/spiking却无定义。
3. fully-spiking、spiking backbone、hybrid、conversion、integer训练/二值推理边界不清。
4. SNN在pipeline的位置或主要role不明，或一篇有两个primary候选。
5. neuron/state update/temporal mechanism/reset或三个时间轴映射不明。
6. 将作为taxonomy代表论文。即使摘要非常完整，primary、interface和boundary仍需检查Method/图/关键方程。
7. 声称event-driven、asynchronous、low-power、hardware-efficient；必须区分算法、软件、芯片和全系统边界。
8. 任何关键定量结论计划写入综述；需核对metric定义、baseline、dataset、配置、measurement与分母。
9. 摘要与card/旧判断/V2或不同PDF版本冲突。

检查顺序：system/method figure → Method输入输出 → neuron/state方程 → training section → 支持当前问题的实验/消融/efficiency setup → 必要appendix。图表/双栏抽取有歧义时看原PDF页面，不靠OCR猜公式。不需要逐段翻译或生成V2；先明确问题才能安排阅读。一个paper的局部问题解决不代表全篇已精读。

例：SDTrack核查GTP、backbone、head是否都spiking；SpikePoint核查点值是否重编码、T与t的关系、grouping计入能耗否；PPLNs核查是否发放/重置或仅实值分段函数；hybrid detector核查chip数字是否仅SNNblock；STLR核查ISTA对应是否实质推断步骤而非修辞。

无法拿到PDF：status=unavailable，needs_pdf_check=yes；保留当前直接证据与unknown，不以不足替代exclude。PDF未报告细节：记录checked section与not reported，在适用字段保留unknown；非关键未知可resolved，影响scope/role/purity/关键数字的未知需Astra判定限制用途或继续查证。

## G. Ambiguity、QC 与交接

初判先只看原始title/abstract，封存初判之后才看旧标注。Sol High可据PDF修正自己的标签，但不能替Astra发明规则。每个争议记录原标签、证据新增、修订和规则依据；保持同一paper不同版本的差异可追踪。规则争议不得由低confidence投票强制收敛。

必须满足的交叉约束：

- core_intersection的最终方法证据需要真实event signal + confirmed spiking + method_coupled或event_specific_training_analysis；仅claimed可保留初判，但selection不得直接usable、confidence不得high。
- scope=boundary_or_exclude不能被赋予core_taxonomy_evidence；冗余论文不要用此scope，保留真实方法scope再reference_only。
- benchmark_only不得因dataset自动进core；具有一般SNN机制时优先snn_foundation；训练/分析交叉以具体机制桥接判定。
- no_spike_interface/continuous_only与confirmed真实SNN若同一annotation_unit相冲突则issue；输入非camera时event接口字段not_applicable而非no_spike_interface。
- fully_spiking_*必须与模块map相容；head有连续学习ANN时最多fully_spiking_backbone；preprocessing/readout未知禁止end_to_end_spiking_pipeline。连续膜态不自动推翻spiking，但连续路径绕过spikes参与下游需说明。
- primary=not_applicable不能成为role_hypothesis主图代表；算法/训练不明不能靠not_applicable隐藏；secondary不能重复primary或含none同时带实质role。
- training_route与purity独立；converted可以fullyspiking，direct可以hybrid，teacher仅训练时存在不使推理hybrid。
- dataset_evaluation的配置要能连接效率和accuracy；不能跨配置比较同名metric，不把latency estimate写实测。
- selection_status=usable/proposed_usable要求前五种tier之一、有具体use及inclusion_reason；reference_only用redundant_reference或有明确保留用途的前五tier并解释当前不计数原因；excluded要求excluded_paper和exclusion_reason；pending对应pending tier。
- needs_pdf_check=yes必须至少一个未关闭问题且status为pending/partial/unavailable；resolved/not_required应no。resolved仍有非关键unknown需记录范围限制；open规则issue可存在，但不能假装final taxonomy无争议。
- evidence_id三表连接完整，每个关键标签有field_path和location；overall confidence不得高于关键适用字段。禁止未经来源支持的数字、neuron和时钟补全。

Pilot QC：30个ID精确join；100%完整title/abstract/hash检查；100%非法标签和必填规则检查；100%决定性scope/role/boundary由Sol High人工式自检（不能把代码合法性当语义正确）。挑10个高风险case盲重标，隐藏旧结果且打乱次序，再报告scope、primary、extent的各自exact agreement与confusion pairs。由于通常是同一模型复读，不将它包装为独立人类inter-rater reliability。允许并如实报告初始低一致性，它是规则失败信号。

目标是10篇关键字段至少9/10一致，且反复混淆的相邻标签在Astra修订后必须消除或合并；决策性unknown不可为达标猜填。若某scope/role只有一个paper，保留类别假设而不宣称覆盖验证。正式批次每40–50篇：Sol Mid检查所有字段合法性和coverage；Sol High处理全部core机制、所有PDF触发和模糊纳排，并复核清楚正例至少10%、负例至少10%（按固定paper_id排序等距抽样，可复现）。出现一个实质性scope误排就回查同批同类，而非只修该一行。

Astra review输入：字段缺失率、unknown/PDF状态、scope×directness、primary×secondary重叠、role×representation、task×evidence、来源/年代/active偏差、重复family、排除理由、所有critical issues。Astra发布新版本需明确旧值→新值迁移与需重读ID；Sol Mid只能执行确定性迁移，不能据新标签名自动重新判断机制。

分工固定：Astra负责字典、相邻标签、pilot后冻结、全库分布、最终taxonomy/outline与usable裁剪；Sol High负责pilot、PDF与困难证据准备，事实歧义按既有规则解决；Sol Mid负责冻结后的完整title/abstract抽取、clear case结构化、metadata、CSV验证、coverage和确定性生成。任何阶段不得自行修改Survey/Advisor membership或旧生成视图。后续结果/issue文件路径由用户确认后的执行任务另定。

**暂停点：本轮交付只有设计和header；用户确认codebook后交Sol High执行pilot，pilot完成再回Astra。禁止本轮自动进入572篇批量标注、全量检索或最终taxonomy。**
