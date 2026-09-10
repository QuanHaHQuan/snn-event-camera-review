# Taxonomy pilot results

日期：2026-09-10。Codebook：`0.1-design`。当前状态：**Batch A complete（6/30 papers）**，不是最终 taxonomy，也不是 usable 文献终审。

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

## 5. 下一步

继续执行 Batch B（09 篇，pilot 07–15），重点测试：

- `task_network` 与局部 `embedded_module` 的主次；
- multimodal fusion、spiking backbone、ANN head 和 bridge 的边界；
- “fully spiking”标题与实际 attention/normalization/readout；
- neuromorphic hardware 数字究竟覆盖 SNN block 还是完整系统；
- 同一方法训练与推理是否需要拆 annotation unit。

Batch B 完成后再做一次本地提交；30 篇首轮全部完成后才开始 10-case 盲重标和 agreement/confusion 统计，随后交 Astra 修订并冻结 codebook。
