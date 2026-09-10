# Taxonomy pilot results

日期：2026-09-10。Codebook：`0.1-design`。当前状态：**Batch A–C complete（23/30 papers）**，不是最终 taxonomy，也不是 usable 文献终审。

## 1. Batch A 完成范围

本批覆盖 pilot 的接口/表示边界样本 01–06。六篇均先封存完整官方标题与摘要的初判，再读取可回答具体问题的官方 PDF 页面；PDF SHA-256、证据位置、摘要→全文修订和配置拆分均已记录。

- Canonical papers：6
- Annotation rows：12
- Abstract-initial events：6
- PDF-resolution events：6
- PDF-required / resolved：6 / 6
- 结构校验：59 列、全部 JSON、受控枚举顺序、audit 精确连接、evidence ID 三表连接、boundary/extent 约束均通过
- 盲重标：尚未开始；将在 30 篇首轮完成后按计划抽取 10 个高风险 case

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

## 7. 下一步

继续执行 Batch D（pilot 24–30）：PPLN 与 `membrane` 术语负例、DailyDVS dataset authority、spike-camera / graph-SNN / EHR 三个摘要级负例、spike-retiming attack，以及 on-device 非 SNN depth comparator。

Batch D 后完成 30 篇首轮；随后按既定清单做 10-case 盲重标和 agreement/confusion 统计，再交 Astra 修订并冻结 codebook。
