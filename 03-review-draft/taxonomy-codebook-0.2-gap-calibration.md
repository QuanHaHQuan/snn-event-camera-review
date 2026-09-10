# Codebook 0.2 冻结前缺口校准（Batch E2）

日期：2026-09-10。执行者：GPT-5.6 Sol High。依据：[Astra checkpoint §6](taxonomy-checkpoint-adjudication.md#6-冻结前最小补充校准)。状态：**E2已获Astra裁决，0.2有限扩展冻结通过**。当前结论见 [freeze decision](taxonomy-codebook-0.2-freeze-decision.md)。下文§1–§6为Sol提交时的证据和建议；C训练、D secondary、F训练、P模块/训练字段以§7及迁移事件为准，保留原建议用于追溯。

本轮严格限制在 G/C/F/D/P/H 六个证据槽位，没有重做 30 篇 pilot，没有启动 572 篇扩展，也没有修改 Survey/Advisor membership、codebook、canonical pilot annotations 或历史 events。新增 5 篇 canonical 校准论文；G 槽按规则保留“所查范围内未找到合格正例”，没有把两个不相交的方法拼成伪正例。

完整 59 字段记录见 [calibration CSV](taxonomy-codebook-0.2-gap-calibration.csv)，G 槽逐候选失败记录见 [candidate audit](taxonomy-codebook-0.2-gap-candidate-audit.csv)。这些论文目前均为 `proposed_usable` 校准样本，不是最终 usable 裁决。

## 1. 六槽结论

| 槽 | 结果 | 校准样本或限制 | 事实答案 | 对 taxonomy 的压力测试 |
| --- | --- | --- | --- | --- |
| G graph × SNN | **未发现合格正例** | 检查 AEGNN、HUGNet、CVPR 2025 GNN+PA、DRSGNN、MSG | 前三者是真实 contrast-event graph 但无 spiking message passing；后两者是真 spiking GNN 但无 event camera | `graph_network` 只能保留为架构轴的可用标签；冻结时必须明示当前适用域未校准 event-graph SNN，不可据此设新 role 或宣称该家族不存在 |
| C event-specific conversion | **满足** | Pérez-Carrasco et al., TPAMI 2013 | 固定时长 DVS 事件帧训练 ANN；权重解析映射到 event-driven ConvNet；再优化层级 timing 参数；推理保持物理事件时间，未增加独立 simulation T；扑克变体仍有外部 event tracker/crop | `ann_to_snn` / `conversion_then_finetune` 是 training route；推理职责仍为 `task_network`，无需 conversion role |
| F optical flow | **满足** | Spike-FlowNet, ECCV 2020 | IF-SNN 只承担四层 encoder；最后 SNN 层仅累积膜电位；残差、decoder、dense-flow head 与训练期 grayscale warping 均连续；`dt=1/4` 是灰度帧间隔，`N=5/20` 是 SNN 输入步 | `task_network + hybrid_subnetwork` 能表达早期 hybrid flow；不能把训练 warping 说成推理算子，也不能把约 17% 代理节能说成硬件实测 |
| D depth | **满足** | Osswald et al., Scientific Reports 2017 | ON/OFF retina spikes → coincidence neurons → disparity-evidence neurons → recurrent uniqueness competition；输出为 `(x,y,d)` disparity events，30 ms bin 仅用于数值地图/评估 | 明确支持 `algorithmic_engine`：spike/state 与命名的 stereo-correspondence 变量和更新实质对应；同时是 `task_network` secondary |
| P pose | **满足** | Zou et al., arXiv:2303.09681v5 | event-only 输入被阈值化为 T 个 binary voxel grids；SEW-ResNet 与 query/key/FFN 为 spiking，但最佳 value branch 为实值；三条 linear heads 回归逐时刻 SMPL shape、pose、translation | 主职责为 `task_network`，extent 应为 `hybrid_subnetwork`；作者的“SNN framework / events only”不能覆盖实值 attention branch 和连续 pose head |
| H sensor–chip | **满足** | Amir et al., CVPR 2017 | live DVS128 经 USB → NS1e Zynq/FPGA → TrueNorth；temporal cascade、15 层 CNN、WTA、80 ms smoother 全在芯片；Ethernet/laptop只显示 | 无传统 backbone 时仍用 `task_network` 表达功能，`hardware_system` 保持正交；178.8 mW 只测 TrueNorth network，不含 DVS、2–3 W NS1e board、host/I/O/显示 |

## 2. 逐槽决定性边界

### C：转换改变训练路线，不改变推理角色

TPAMI 2013 先把 DVS 事件按固定时长累积为训练图像，以监督方式训练 frame-driven 六层 ConvNet，再按公式缩放/映射权重到连续 event-driven 神经元，并以启发式和 simulated annealing 调整 refractory、leak、characteristic-time 等参数。推理端逐地址事件执行卷积、subsampling 和输出发放；它没有把真实事件时间复制为另一条固定 T-step rate code。

因此本例不支持新增“conversion”功能角色：转换发生在训练/部署路线，最终 event-driven ConvNet 仍完成完整识别。边界例外是固定 crop/downsample；扑克实验另使用 event-driven clustering/tracking 产生 32×32 crop，不能称传感器到任务输出全部都是神经元计算。

### F：经典 hybrid flow 的职责只覆盖 encoder

Spike-FlowNet 将物理窗口分成前/后两组，并在每组内累积为 N 个 ON/OFF event frames；四通道张量按时间顺序进入 IF encoder。前三个 SNN 层发放，最后 SNN 层不发放而把膜电位作为连续交接；两层 residual block、四层 decoder、skip concatenation 与 multi-scale flow prediction 均为 ANN。

灰度图像只用于训练：预测 flow warp 第二幅灰度图以形成 photometric loss；推理输入仍是事件。`dt=1/4` 指一或四个灰度帧间隔，分别映射到 `N=5/20` event/SNN steps，不能把 N 直接解释为毫秒。能效是 firing-rate 加 AC/MAC 成本的解析代理；SNN encoder 只占整网 17.6% 的操作量，因此整网估计降幅约 17%，并非 neuromorphic deployment measurement。

### D：depth 样本反而强化 algorithmic_engine

2017 spiking stereo model 不是普通回归 backbone。每个 coincidence neuron 对应候选 `(x,y,d)` 匹配，disparity neurons 对 constant-disparity plane 的支持证据做兴奋积分、对冲突证据做抑制，并以 recurrent inhibition 实现 uniqueness constraint；最终 disparity events 明确编码求解变量。外部把这些 spikes 聚合为 30 ms disparity map 只是显示/评估 readout。

这满足 engine 的三项严格条件：有命名的 stereo-correspondence 目标和 disparity 变量；spike/state 与候选、证据、竞争和解有实质对应；该对应就是论文提出的推理机制。硬件演示只将 disparity integration/inhibition 放到 256-neuron ROLLS，coincidence units 位于 FPGA，因此它不能替代 H 槽的完整 sensor–spiking-chip 样本；论文的功耗也是 projection。

### P：事件-only 不等于 end-to-end spike-only

最新 v5 版本将物理事件片段转换为 T 个 256×256×4 binary voxel grids；SEW-ResNet 提取 spike features，Spiking Spatiotemporal Transformer 在完整空间—时间张量上做双向融合。query/key 与 FFN 路径发放，但论文明确说明实值 value aggregation 更准确，默认比较采用该实值分支。随后 2D average pooling 和三条普通 linear heads 输出每个 timestep 的 SMPL `β`、72-D `θ` 和 global translation `d`。

测试时 `T=8/64` 对应 1 s/8 s；训练又随机改变同一 T 覆盖的物理时长。因 transformer 需要完整 T tensor 且有双向 attention，本例是 windowed lookahead，而不是逐事件 causal stream。主 feature path 足以构成 `task_network`，但实值 value branch 与连续 SMPL head 使 `hybrid_subnetwork` 比“fully spiking”更忠实。

### H：把 functional role 与 hardware boundary 分开

Amir et al. 的真实运行路径是 DVS128 经 USB 进入 NS1e；Zynq 上的 ARM/Linux 与 FPGA 完成标准接口、数据转换和地址翻译。NS1e 具备绕过 Zynq 的 pin-to-pin connector，但论文明确说该能力在本工作中未使用。进入 TrueNorth 后，temporal filter cascade、15-layer CNN、WTA decoder 和 80 ms sliding-window filter 全部以 spikes 实现，输出事件再经 Ethernet 到 laptop 显示。

所以系统在主图中仍是 `task_network`，不需要 hardware role；硬件、host 和成本范围用正交字段表达。E1 的 178.8 mW 来自 NS1t characterization board 对 TrueNorth 芯片的采样，并由活动功率与按使用 core 比例缩放的 leakage 构成。论文同时说明 TrueNorth 只约占 NS1e board 功耗的 6%，整板通常为 2–3 W；相机、USB/Ethernet、Zynq/FPGA、laptop/display 均不在 178.8 mW 内。104.6 ms onset latency 是运行测量，但对齐前删除了手势间无标签事件，引用时需保留该条件。

## 3. G 槽的明确适用域限制

本轮按 checkpoint 的停止规则，从现有 classic pool、Core bibliography、用户给出的 event-representation survey 引用和定向官方检索中检查五个最接近候选：

- AEGNN、HUGNet、CVPR 2025 GNN+PA 都从真实 contrast events 构图，也有逐事件或异步 message passing，但计算节点不是 spiking neurons。
- DRSGNN 与 MSG 都有真正的 spiking graph neurons/message propagation，但输入是普通静态/领域图，而非 event-camera contrast events。

因此当前不能回答图构造成本、edge message 和 neuron location 在**同一篇真实 event-camera spiking GNN**中的组合关系。可冻结的最小表述是：“0.2 的 primary-role 结构允许未来 graph SNN 按其 functional role 进入，`graph_network` 记录架构；当前证据覆盖尚未校准这一组合家族。”不能写成“事件相机中没有 graph SNN”。

## 4. 对冻结门的建议

E2 的证据支持如下判断，最终裁决仍属于 Astra：

1. C/F/D/P/H 已有直接事实答案；G 已有可审计的失败候选与清楚适用域限制。
2. 五篇正例均可由现有四 role 表达：C/F/P/H 为 `task_network`，D 为 `algorithmic_engine` + secondary `task_network`。
3. `hardware_system`、conversion、graph、continuous head、energy measurement boundary 都可由现有正交字段承载，没有出现必须新增 primary role 的方法。
4. D 提供了 pilot 外的第三种 engine 机制证据，降低了 engine 只靠两篇近期论文命名维持的风险。
5. G 仍是 coverage gap；若 Astra 冻结，应把允许扩展的适用域写成“除真实 contrast-event spiking GNN 组合外”，并令该家族进入 Sol High 路由，而非 ordinary clear-case 批处理。

## 5. 数据、来源与验证

- 新增 canonical：5；annotation rows：5；字段：59；所有行保持在独立 calibration CSV，不写入 30 篇 pilot baseline。
- 本地绑定 PDF：TPAMI 2013、Scientific Reports 2017、CVPR 2017、ECCV 2020，均记录 SHA256。
- Pose 使用不可变的 `arXiv:2303.09681v5` URL 完成网页 PDF 核验；shell 端连接被重置，故 `pdf_sha256=unknown`，未伪造 byte hash。决定性事实均绑定 v5 页码；正式写作前若需要本地归档，可补 hash，不影响当前 role/boundary 结论。
- G 的五个 rejected candidates 只写入 gap audit，不伪装成 canonical calibration rows。

只读验证入口：

```sh
python3 scripts/validate_taxonomy_pilot.py \
  --annotations 03-review-draft/taxonomy-codebook-0.2-gap-calibration.csv \
  --standalone-calibration
python3 scripts/validate_taxonomy_pilot.py
git diff --check
```

预期结果：5 rows / 5 papers / 59 columns 的 calibration contract 通过；30 papers / 36 rows / 107 events 的原 pilot 与可逆历史保护仍独立通过。

## 6. 下一步

停止 E2，不继续找第六篇、不扩大 graph 搜索，也不把 5 篇合并进 canonical pilot。把本报告、59 字段 calibration CSV、G candidate audit 和验证结果交给 Astra High；由 Astra 决定：

- 是否发布第一个允许分批扩展的冻结版本；
- G 的适用域限制是否足够，或是否只为该家族保留 Sol High 特殊路由；
- D 的新增证据是否足以正式保留 `algorithmic_engine`；
- C/F/P/H 是否需要任何 role/extent migration。

## 7. Astra冻结裁决与受影响字段

C/F/P/H primary及全部五篇extent均保留，D primary正式保留engine。现有词表下更正：C conversion_then_finetune→ann_to_snn（仅timing/threshold校准）；F direct_snn→joint_ann_snn（Algorithm 1共同反传）；D secondary task_network→none（同一solver不重复计role）；P移除SNN functions中的连续task_head，training_route由direct_snn→unknown并以E2-P-I3 deferred / sol_high保留联合训练证据问题。后三种训练路线更正不改变scope/role。

5行review_status设astra_adjudicated，仅覆盖主role、extent及上述字段，非59字段重审。原抽取证据保留，新增Astra证据/issue与 [5条可逆事件](taxonomy-codebook-0.2-gap-events.csv)。源快照ec707f9、独立baseline hash、原30篇历史均保护；不向canonical pilot追加这5篇。G记录保留原5候选，不补伪正例。

允许下一任务按30篇首批执行；G进入特殊路由。现有ABN、DailyDVS、generic conversion三项deferred及新增P训练路线用途限制不被冻结解除。
