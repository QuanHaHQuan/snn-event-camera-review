# Taxonomy pilot results

日期：2026-09-10。首轮/盲重标使用`0.1-design`；当前canonical annotations使用**0.2（有限扩展冻结）**。**E1/E2后的有限扩展checkpoint通过，最终taxonomy未冻结**。当前门禁见§12及 [freeze decision](taxonomy-codebook-0.2-freeze-decision.md)；下文§1–11保留各阶段当时结论与原分歧，§9原checkpoint由§12的扩展冻结门禁补充；不是最终taxonomy或usable终审。

## 1. Batch A 完成范围

本批覆盖 pilot 的接口/表示边界样本 01–06。六篇均先封存完整官方标题与摘要的初判，再读取可回答具体问题的官方 PDF 页面；PDF SHA-256、证据位置、摘要→全文修订和配置拆分均已记录。

- Canonical papers：6
- Annotation rows：12
- Abstract-initial events：6
- PDF-resolution events：6
- PDF-required / resolved：6 / 6
- 结构校验：59 列、全部 JSON、受控枚举顺序、audit 精确连接、evidence ID 三表连接、boundary/extent 约束均通过
- 盲重标：30 篇首轮完成后已按计划复核 10 个高风险 case；结果见第 8 节

EAS-SNN 和 SDA 各有四种会改变推理边界的配置，因此分成配置级行；论文计数始终按 `paper_id` 去重，不能把 12 行误报成 12 篇。

## 2. 六篇的初步定位

| Paper | Primary role | Verified extent | 关键裁决 |
| --- | --- | --- | --- |
| ICLR2024-1097 SpikePoint | `task_network` | `fully_spiking_task_network` | 点集先经过固定采样/分组与 Poisson rate recoding；16 steps 不是 16 ms，也不是 raw address-event injection。 |
| ECCV2024-1778 STLR | `algorithmic_engine`；secondary `task_network` | `fully_spiking_task_network` | SVT 的 state/spike-rate 与非负 LASSO/ISTA 迭代有实质映射；终端图像来自 MP-LIF membrane readout。 |
| ECCV2024-1168 EAS-SNN | `event_interface` | 随配置为 `fully_spiking_task_network`、`fully_spiking_backbone` 或 `hybrid_subnetwork` | SNN firing 决定 pixel-local sampling interval，potential embedding 再交给 SNN/ANN detector；不能给整篇一个 purity 标签。 |
| CVPR2026-1873 SDA | `event_interface` | 随配置为 `fully_spiking_task_network` 或 `hybrid_subnetwork` | gated recurrent spiking neuron 是真实神经元；但 early Event Count 与 MTF sigmoid mask 含连续计算。 |
| NeurIPS2024-2388 SpikeSlicer | `event_interface` | `hybrid_subnetwork` | SNN spike 是全局 slicing control，实际实现输入是小 `δt` voxel event cells；ANN feedback 用于训练，ANN 仍承担推理任务。 |
| NeurIPS2025-0641 FLAME | 暂定 `embedded_module` | `hybrid_subnetwork` | raw events 确实驱动 LIF threshold/reset；EA-HiPPO/NPLR/FFT 与最终 readout 是连续路径，不能称全 SNN。interface vs embedded 已送 Astra。 |

按 canonical paper 计数，当前 primary role 分布是：`event_interface` 3、`task_network` 1、`algorithmic_engine` 1、`embedded_module` 1。按配置行计数会因 EAS-SNN/SDA 的拆分而人为放大 interface，不应用于 taxonomy 频率结论。

## 3. 对 taxonomy architecture 的首批压力测试

### 3.1 四个 primary roles 暂时可覆盖本批，但 role 不是唯一写作维度

六篇没有迫使我们新增第五种 primary role。真正产生解释力的是 role 与以下正交字段组合：

1. `event_to_spike_interface`：raw address injection、continuous current、rate recoding；
2. `spiking_extent`：task network、backbone、hybrid subnetwork；
3. `time_axis_mapping`：physical event time、event-group order、SNN simulation/iteration steps；
4. `training_route`：direct SNN 与 joint ANN–SNN；
5. `efficiency_evidence`：operation proxy 与实测 runtime 分开。

因此后续主 taxonomy 可以继续以 **SNN 的功能角色**作为第一层，但每个 role 的比较表/子层必须显式呈现接口、边界和时间轴，不能用 task 或 dataset 取代这些机制维度。

### 3.2 `event_interface` 内部至少出现三种不同合同

- 全局边界控制：SpikeSlicer 的单一 spike 决定整个事件流的下一处 slice boundary；
- 空间局部自适应采样：EAS-SNN 的每像素/极性 firing time 决定局部 interval；
- 事件选择并聚合：SDA 的 spike 决定哪些事件进入 dense representation，并可叠加连续 MTF。

目前不新增 primary role 或正式 subtype。等 Batch B–D 完成后，Astra 应判断这三类是作为 interface 的稳定二级 taxonomy，还是仅作为 `snn_module_functions × temporal_organization × representation_learning` 的组合视图。

### 3.3 `interface` 与 `embedded_module` 的边界仍是最需要裁决的邻类

本批操作性证据支持：若 SNN 输出事件子集、切片边界或独立表示并交给 principal feature extractor，归 `event_interface`；若其输出是系统内部的任务专用 latent feature，且直接进入不可分离的连续主干，优先 `embedded_module`。FLAME 正落在边界上，当前 evidence-ready 但保留 Astra 裁决，不能通过增加新标签绕开。

### 3.4 “fully spiking” 必须是配置级结论

EAS-SNN 与 SDA 证明 paper-level purity 不可靠。相同论文可以同时包含 fully spiking detector、spiking backbone + ANN head、以及仅保留 SNN interface 的 ANN detector。输入构造、continuous mask、terminal readout 和 NMS 也必须和学习网络分开陈述。

### 3.5 event time 与 SNN time 不是同一对象

- SpikePoint：固定物理 clip → point set → 16-step Poisson/SNN simulation；
- STLR：物理 event voxel sequence → 每 voxel 的 5 次 solver-like coding steps；
- EAS-SNN/SDA：早期固定细粒度 event cells → 自适应 sample/aggregation → 3-step detector；
- SpikeSlicer：每个 `δt` event cell 对应一次 SNN update，spike 再映射回物理切片边界；
- FLAME：直接使用 event timestamp 和 inter-event interval，不要求固定 simulation clock。

这一字段应保留为强制字段；它已经阻止了“timesteps 等于毫秒”和“raw events 等于 neuronal spikes”两类高风险误判。

### 3.6 当前能效证据不支持笼统的低功耗结论

SpikePoint、STLR、EAS-SNN、SDA、SpikeSlicer 的能量数字主要来自 AC/MAC/SOP 成本模型，不是芯片实测；FLAME 提供 conventional CPU/GPU runtime 与 operation count，但明确不是纯 spiking neuromorphic pipeline。后续综述应把算法稀疏度、理论能量代理、常规设备 runtime、神经形态芯片实测分栏，不可相互替代。

## 4. 当前未关闭的规则问题

只有一项需要 Astra 的 taxonomy judgment，而不是继续搜索事实：

- `FL-I1`：FLAME 的 LIF Event Attention Layer 应归 `event_interface` 还是 `embedded_module`。PDF 已确认其输入、发放、下游交接与连续 SSM 边界；当前按“task-specific latent front-end”暂标 `embedded_module`，issue 状态为 `evidence_ready`。

FLAME 未明确说明离散 threshold 的梯度处理方式，因此 `credit_assignment=unknown`；这不是 primary role、scope 或 purity 的阻塞项，PDF 问题已按“not reported”关闭。

## 5. Batch B 结果（pilot 07–15）

本批按精简工作流完成：九篇均先封存官方标题/完整摘要初判，再只读取能回答 role、边界、时间轴、训练和效率问题的 PDF 段落；每篇保留一行，没有为了穷尽细节拆分配置。

- Canonical papers：累计 15；annotation rows：累计 21
- Abstract-initial / PDF-resolution events：15 / 15
- 当前 scope：14 篇 `core_intersection`，1 篇 `snn_foundation`
- 当前 primary：`event_interface` 3、`task_network` 5、`embedded_module` 3、`algorithmic_engine` 2、`not_applicable` 2
- PDF-required / resolved：累计 15 / 15
- 批次校验：通过；未新增 taxonomy label，也未修改 codebook

| Paper | Scope / primary | Verified extent | Taxonomy 用途 |
| --- | --- | --- | --- |
| ICML2025-2762 HsVT | core / `task_network` | `hybrid_subnetwork` | MaxViT、LSTM 与 LIF 模块交错的 hybrid task network；作者的 45 nm 能量表也显示连续模块代价占主导。 |
| CVPR2025-2047 Attention Hybrid | core / `embedded_module` | `hybrid_subnetwork` | SNN fast front-end 经 ASAB 转 dense ANN feature；Loihi-2 实测只覆盖四层 SNN block。 |
| ICCV2025-1790 ClearSight | core / `embedded_module` | `hybrid_subnetwork` | event-SNN 支路以图像/事件特征动态设置 membrane 与空间 threshold，最终融合和重建仍为连续网络。 |
| NeurIPS2025-4041 SpikeFET | core / `task_network` | `fully_spiking_backbone` | multimodal spiking feature/fusion 主干；integer training、binary spike inference，末端预测卷积阻止更强 purity 结论。 |
| CVPR2026-1935 SpikeTrack | SNN foundation / `task_network` | `fully_spiking_backbone` | RGB-only 对照；保留用于非对称 timestep、spike memory 设计和同名论文消歧，不计入核心交叉语料。 |
| CVPR2026-1798 SpikeTrack | core / `task_network` | `fully_spiking_backbone` | event-only SNN tracker；MSST 把连续 search frames 放入神经状态轴，DI-LIF 依据输入调整 integer firing depth。 |
| NeurIPS2024-1436 Spike Bayesian | core / `algorithmic_engine` | `hybrid_subnetwork` | WTA firing 对应 EM E-step，STDP 对应 M-step，验证 algorithmic_engine 不是 task backbone 的别名。 |
| ICLR2024-0249 EventRPG | core / `not_applicable` | `not_applicable` | SNN-specific relevance propagation 与 event augmentation 属于 cross-cutting training/analysis，不创造新 inference role。 |
| ECCV2024-1740 Raw-event attack | core / `not_applicable` | `not_applicable` | raw COO event 攻击与 hidden grid 攻击的 threat boundary；属于 cross-cutting robustness。 |

Batch B 支持四个结构性结论：`task_network` 与 `embedded_module` 的区别必须看 SNN 是否承担主任务路径；“fully spiking”标题仍需核查输入构造和末端 head；硬件证据必须写清只覆盖局部 SNN block 还是完整系统；training/attack 类论文应保留在核心交叉语料，但 primary inference role 应为 `not_applicable`。这些结论暂不触发 codebook 修改，待 30 篇完成后统一交 Astra 判断。

## 6. Batch C 结果（pilot 16–23）

本批专门测试 SNN foundation、event-camera-only 方法与真实交叉方法的边界。八篇均完成摘要初判和决定性 PDF 核查，没有拆分配置。

- Canonical papers：累计 23；annotation rows：累计 29
- Abstract-initial / PDF-resolution events：23 / 23
- 当前 scope：16 篇 `core_intersection`、4 篇 `snn_foundation`、3 篇 `event_camera_foundation`
- 当前 primary：`event_interface` 3、`task_network` 7、`embedded_module` 4、`algorithmic_engine` 2、`not_applicable` 7
- Selection：19 篇 `proposed_usable`、4 篇 `reference_only`
- 批次校验：通过；59 列及 JSON、枚举顺序、证据连接、boundary/extent 与 PDF closure 均通过

| Paper | Scope / primary | Verified extent | Taxonomy 用途 |
| --- | --- | --- | --- |
| ICML2024-0803 CLIF | SNN foundation / `task_network` | `fully_spiking_task_network` | 通用多状态神经元基础；额外 complementary state 改善梯度与 firing rate，但 memory-aware 模型揭示状态开销可能抵消算术节省。 |
| CVPR2025-0053 ANN–SNN conversion | SNN foundation / `not_applicable` | `not_applicable` | conversion 属于 training route，不是 inference role；低 timestep 的 threshold、pooling 与 delayed-evaluation 设计可供实现参考。 |
| NeurIPS2025-5334 STEP | SNN foundation / `not_applicable` | `not_applicable` | 作为 evaluation authority，要求把 bitwidth、membrane memory 与量化 ANN 对照纳入能效比较。 |
| CVPR2025-1552 GNN+PA | event foundation / `not_applicable` | `non_spiking` | event-by-event GNN 与周期 CNN/RNN 都是连续计算；异步、稀疏和硬件投影不能替代 SNN 证据。 |
| CVPR2024-1880 PEPNet | event foundation / `not_applicable` | `non_spiking` | x-y-t point set 保留 timestamp，但 A-Bi-LSTM 使用窗内未来信息；是 point-SNN 的输入/因果性对照。 |
| ECCV2024-1737 REDIR | core / `embedded_module` | `hybrid_subnetwork` | 三层 TSA-LIF 负责持续目标/瞬态遮挡过滤，注册、mask、fusion 与 decoder 仍为连续网络。 |
| ECCV2024-0096 ABN | core / `task_network` | `fully_spiking_task_network` | PDF 将摘要初判从 generic benchmark 修正为直接 event-to-spike 系统；动态 threshold 由 membrane gradient、threshold history 与 spike efficiency 共同控制。 |
| ECCV2024-0945 FARSE-CNN | event foundation / `not_applicable` | `non_spiking` | fully asynchronous、sparse、causal、stateful 仍不等于 SNN；核心单元是 sigmoid/tanh LSTM，且单事件 PyTorch runtime 并不低。 |

Batch C 没有产生新的 primary role。它强化了两条边界：第一，只有 event dataset 不足以把通用 SNN 升级为核心交叉，但 ABN 的 direct address-event injection 与 event-rate-adaptive threshold 足以升级；第二，`event-driven`、`asynchronous`、`sparse`、`membrane` 等词都不能单独证明 spiking computation。CLIF、STEP 和 conversion 可保留在主图外的 foundation/evaluation 层，非 SNN event 方法只在具有明确反例价值时保留为 comparator。

新增两项 evidence-ready 问题交 Astra：spiking MLP 是否需要独立 architecture-family 标签；ABN 实验部分的 spatio-temporal backpropagation 与结论中的 STDP 表述冲突应如何裁决。原有 FLAME interface vs embedded 问题仍保留。

## 7. Batch D 结果（pilot 24–30）

本批完成四篇决定性 PDF 核查和三个明确负例的官方完整摘要闭环。没有为了形式一致而下载无关 PDF，也没有新增 taxonomy label。

- Canonical papers：30；annotation rows：36
- Abstract-initial events：30；PDF-resolution events：27；abstract-resolution events：3
- Scope：17 篇 `core_intersection`、5 篇 `snn_foundation`、6 篇 `event_camera_foundation`、2 篇 `boundary_or_exclude`
- Primary：`event_interface` 3、`task_network` 7、`embedded_module` 4、`algorithmic_engine` 2、`not_applicable` 14
- Extent：`fully_spiking_task_network` 6、`fully_spiking_backbone` 3、`hybrid_subnetwork` 7、`non_spiking` 5、`not_applicable` 9
- Selection：22 篇 `proposed_usable`、5 篇 `reference_only`、3 篇 `excluded`
- 批次校验：通过；59 列、audit 精确连接、JSON/枚举、evidence ID、boundary/extent 和 PDF closure 均有效

| Paper | Scope / primary | 终态 | Taxonomy 用途 |
| --- | --- | --- | --- |
| NeurIPS2024-2307 PPLN | event foundation / `not_applicable` | `non_spiking`、`reference_only` | 关键术语反例：真实值 piecewise temporal function 不含 threshold、firing、reset；`membrane` 和 neuromorphic motivation 不能证明 SNN。 |
| ECCV2024-1631 DailyDVS-200 | event foundation / `not_applicable` | benchmark authority | 22,046 段、200 类、47 人、14 种属性；SNN 只是十二类 baseline 中的一部分。原文 cross-subject participant list 有重叠/计数冲突，已入 issue。 |
| CVPR2026-1021 Nope-SGS | boundary / `not_applicable` | `excluded` | intensity-integrating spike camera，不是 contrast event camera；摘要未声称 SNN。 |
| ICLR2024-1543 SpikeGCL | SNN foundation / `not_applicable` | `excluded` | 普通 graph contrastive SNN，没有 event-camera signal，也没有不可替代的机制桥梁。 |
| ICLR2024-1607 MOTOR | boundary / `not_applicable` | `excluded` | `event` 指临床 time-to-event；输入是 EHR/insurance records，两个目标轴都缺失。 |
| ICLR2026-1286 retiming attack | core / `not_applicable` | cross-cutting robustness | 攻击对象是量化后的 event-input temporal bins，不是 raw microsecond timestamps，也不是内部 neuron spike times。 |
| CVPR2025-1775 on-device depth | event foundation / `not_applicable` | `non_spiking` comparator | Conv/ConvGRU + contrast maximization 在 Jetson 上完成约 30 Hz、约 9 W 的在线学习；为 SNN 能效论述提供实测常规设备对照。 |

Batch D 进一步确认：四个 primary inference roles 无需扩张；dataset、training/attack analysis 和 comparison layer 必须与 primary-role 主图并列存在，但不能伪装成第五种 role。它也补齐了搜索与术语边界：`spike camera`、clinical `event`、graph SNN、`membrane`、asynchronous/stateful/event-driven 都不能单独把论文送入核心交叉。

当前尚待 Astra 裁决或上游更正的 evidence-ready issue 共四项：`FL-I1`（FLAME interface vs embedded）、`AB-I1`（spiking MLP architecture label）、`AB-I2`（ABN backpropagation vs STDP 表述冲突）、`DD-I1`（DailyDVS cross-subject participant split 冲突）。它们均不阻塞 30 篇 pilot 首轮完成。

## 8. 10-case 盲重标结果

03、04、06、07、12、13、14、22、24、29 已按打乱次序完成 evidence-first 第二轮，并在固定重标结果后解盲。paper-level exact agreement 为：`scope` 10/10、`intersection_directness` 10/10、`primary_functional_role` 9/10、`spiking_extent` 10/10；补充检查的 `selection_status` 为 10/10。EAS-SNN 与 SDA 的 extent 使用配置标签集合比较，没有把多行配置重复计为多篇论文。

唯一 confusion pair 是 FLAME 的 `embedded_module → event_interface`。第二轮认为 LIF Event Attention Layer 输出新的 binary event trains，并经 pooling 交给连续 EA-HiPPO principal backbone，符合当前“显式表示 handoff”的 interface 字面合同；首轮则强调这是 task-specific latent front-end。该分歧已由 `FL-I1` 完整覆盖，保留首轮 canonical label 等待 Astra，未为提高一致率而覆盖数据。

所有预设门槛均通过，且没有重复出现的同类 confusion。详细方法、逐 case 对比和处置见 `taxonomy-pilot-blind-recheck.md` 与 `taxonomy-pilot-blind-recheck.csv`。当前 audit 共 70 events：30 次 abstract initial、27 次 PDF resolution、3 次 abstract-only resolution、10 次 blind recheck。

## 9. Astra checkpoint（0.2）

30篇、36配置保持不变；27篇PDF resolution和3篇摘要负例不重做。scope仍为17 core / 5 SNN foundation / 6 event-camera foundation / 2 boundary，selection仍为22 proposed_usable / 5 reference_only / 3 excluded。

| 原issue | 当前裁决 | 状态 |
| --- | --- | --- |
| FL-I1 | event_interface；新的neuronal event trains经timestamp pooling成为E_flat(t)，明确交给连续EA-HiPPO；不要求独立训练或跨backbone复用 | resolved / astra |
| AB-I1 | 新增architecture_family=mlp；ABN与HsVT显式SpikingMLP适用，普通FFN不自动适用 | resolved / astra |
| AB-I2 | 实验STBP与结论STDP原文冲突；credit_assignment及training_route=unknown，不虚构phase/config | deferred / astra |
| DD-I1 | 官方README也未提供可靠更正；dataset setting=unknown，保留有冲突说明的author-declared cross-subject，不刊具体ID | deferred / astra |

联动修复：FL-I2把FLAME的sensor binary_map纠正为新受限标签neuronal_spike_train；HV-I1按mlp规则同步HsVT；CV-I1将generic conversion中仅凭校准证据得到的distillation监督标签降为unknown并限制比较用途，deferred / astra。这些都是既有证据的裁决/充分性处置，不是新一轮论文抽取。

裁决后核心role：interface 4、task_network 5、embedded_module 3、algorithmic_engine 2；另3篇core cross-cutting。全pilot role为interface 4、task_network 7、embedded_module 3、algorithmic_engine 2、not_applicable 14；不能把两个foundation task网络混入核心图。历史盲测仍为primary 9/10，其余四字段10/10；没有新的0.2盲测成绩。

可执行核心结构：四role作第一层；interface按控制/选择聚合/新事件列，task按event主要路径/联合多模态主推断，embedded按串行局部功能/支路条件化，engine按概率竞争/固定点编码组织二级叙述。二级是暂定写作合同，非新增enum。训练、增广、安全与泛化设独立cross-cutting；foundation/authority/comparator/hardware evidence处于解释和比较层。

发布0.2校准版，不冻结v1.0。下一步只补checkpoint §6的六个缺口证据槽位（最多六篇，允许合并）并对五个旧case定向重判；不重做pilot，不启动572篇。之后回Astra检查适用域、边界稳定性、engine与遗漏机制，再决定扩展冻结。

验证入口改为`python3 scripts/validate_taxonomy_pilot.py`：59列与codebook/JSON契约一致，107条事件包含原70条及32次确定性迁移、5次Astra裁决。历史blind文件不改分数；迁移可逐字段反向恢复原0.1快照。验证结果与更改清单见 [migration](taxonomy-codebook-migration-0.2.md)。

## 10. Codebook 0.2 定向重判（Batch E1）

按 checkpoint §6，仅复核 FLAME、CVPR2025-2047、REDIR、HsVT、STLR 五个受影响 role 边界，并检查 ABN/HsVT 的 `mlp` 映射。决定性 PDF 页面重读后，5/5 role 判断与当前 canonical 一致，2/2 `mlp` 判断一致；没有新事实、未解释分歧、第五种 primary role 或 annotation migration。

- interface / embedded：FLAME 满足 I1–I4；PLIF-ASAB 的二值输出仍是低层任务特征；REDIR 的 SNN 已位于连续注册后的内部 feature path。
- distributed task / embedded：HsVT 的 SpikingMLP 和 STFE 分布于四级主要 backbone，因此稳定为 `task_network`。
- engine / task：STLR 的 spike/state 与非负 LASSO/ISTA 变量、更新及 fixed point 有显式核心映射，故 primary 仍为 `algorithmic_engine`，U-shaped SNN decoder 提供 secondary `task_network`。
- `mlp`：ABN 的 Spiking MLP 是主任务承载架构；HsVT 的 SpikingMLP 是每个空间块中明确命名、重复出现的多层功能模块。普通 FFN/单 projection 不因此获得该标签。

本轮是同一执行者的 evidence-first 定向稳定性检查，不报告为新的 blind 或 inter-rater agreement。完整逐合同记录见 [targeted recheck](taxonomy-codebook-0.2-targeted-recheck.md) 与 [CSV](taxonomy-codebook-0.2-targeted-recheck.csv)。现有事件合同没有 `targeted_recheck` 类型，因此没有把它伪装成 blind/PDF-resolution 事件，也没有修改 codebook 0.2。

E1 已完成，但冻结门仍等待 G/C/F/D/P/H 六个补充证据槽位。下一步为最小补充校准 Batch E2，而不是全量 572 篇标注。

## 11. 冻结前缺口校准（Batch E2）

按 checkpoint §6 完成 G/C/F/D/P/H 的最小校准：新增 5 篇独立 canonical 样本、5 条 59 字段记录；没有修改 30 篇 pilot baseline。C/F/D/P/H 均获得 PDF 事实答案；G 检查 5 个最接近候选后没有找到同时具备真实 contrast-event graph 与 spiking message passing/neuron 的可靠正例，因此按停止规则保留明确适用域限制，没有拼接 event GNN 与 generic spiking GNN。

- C：TPAMI 2013 的 event-specific ANN-to-SNN 映射仍归 `task_network`；conversion 是 training route。
- F：Spike-FlowNet 的 SNN 只承担 encoder，ANN residual/decoder 与 flow head 使其为 `hybrid_subnetwork`。
- D：2017 spiking stereo 的 coincidence/disparity/WTA dynamics 直接实现 stereo-correspondence solver，形成 pilot 外的 `algorithmic_engine` 正例。
- P：event-only spiking pose 系统仍含 real-valued attention value branch 和连续 SMPL heads，归 `task_network + hybrid_subnetwork`。
- H：live DVS–TrueNorth 系统仍由 `task_network` 表达；178.8 mW 只覆盖 TrueNorth network，不是 sensor/board/host/I/O 全系统。

完整裁定建议与限制见 [E2 report](taxonomy-codebook-0.2-gap-calibration.md)、[59 字段 calibration CSV](taxonomy-codebook-0.2-gap-calibration.csv) 和 [G candidate audit](taxonomy-codebook-0.2-gap-candidate-audit.csv)。E2 至此停止，下一步交 Astra 决定冻结版本和允许扩展的适用域；不得直接启动 572 篇。

## 12. Astra E2冻结决策（当前有效）

发布0.2 frozen_limited_expansion，维持59字段与全部受控标签。E1为5/5 role、2/2 mlp定向一致；旧10-case blind仍primary9/10，其余四项10/10，未伪造新盲测。E2五篇主role及extent全部保留；G未获真实组合正例，形成明确适用域限制与Sol High→Astra首例路由。D的stereo-correspondence机制使engine在冻结版正式保留；其secondary task_network移除，避免同一solver重复计数。

独立E2表的C训练改ann_to_snn，F改joint_ann_snn，P移除连续task_head并把训练路线暂置unknown（E2-P-I3 deferred）。AB-I2、DD-I1、CV-I1继续deferred。5条新可逆E2事件不进入原107条pilot事件。全部5行review_status=astra_adjudicated只表示上述字段审查；proposed_usable未提升为usable。

冻结只允许后续分批扩展：首批30篇、3×10小批、先Mid后High，批末回Astra；通过后每批最多40篇。没有启动批次、重做pilot、改变membership或冻结final taxonomy。详细适用域、章节结构、停止条件、验证和迁移见freeze decision。
