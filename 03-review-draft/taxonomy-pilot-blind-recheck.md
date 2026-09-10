# Taxonomy pilot blind recheck

日期：2026-09-10。Codebook：`0.1-design`。范围：pilot 03、04、06、07、12、13、14、22、24、29。

## 1. 方法

10 个高风险 case 在第二轮中打乱顺序。重标阶段只使用 codebook、官方论文标题和决定性 PDF 页面，先固定 `scope`、`intersection_directness`、`primary_functional_role`、`spiking_extent` 与补充的 `selection_status`，之后才读取首轮字段进行比较。

比较单位是 canonical paper。EAS-SNN 和 SDA 含多个配置，因此 `spiking_extent` 比较的是该论文全部配置的去重标签集合，而不是把配置行当成多篇论文。该复核由同一模型执行，只能解释为 intra-annotator stability，不能称为独立人类 inter-rater agreement。完整逐项记录见 `taxonomy-pilot-blind-recheck.csv`。

## 2. Exact agreement

| Field | Agreement | Pilot criterion | Result |
| --- | ---: | ---: | --- |
| `scope` | 10/10（100%） | ≥9/10 | pass |
| `intersection_directness` | 10/10（100%） | reported | pass |
| `primary_functional_role` | 9/10（90%） | ≥9/10 | pass at threshold |
| `spiking_extent` | 10/10（100%） | ≥9/10 | pass |
| `selection_status` | 10/10（100%） | supplementary | pass |

本样本是刻意富集的困难边界集，且 rare labels 很多，因此不使用一个总体 kappa 掩盖具体错误。需要关注的是 confusion pair 是否重复出现。

## 3. Case-level comparison

| Case | Scope | Directness | Primary | Extent signature | 结论 |
| --- | --- | --- | --- | --- | --- |
| 24 PPLN | match | match | match | match | `membrane` 术语负例稳定。 |
| 13 Spike Bayesian | match | match | match | match | `algorithmic_engine` 与普通 task backbone 可复现地区分。 |
| 04 SDA | match | match | match | match | interface role 与 SNN/ANN 配置级 extent 均稳定。 |
| 29 retiming attack | match | match | match | match | event-specific analysis 保持 core，但无新 inference role。 |
| 06 FLAME | match | match | **mismatch** | match | 首轮 `embedded_module`；重标 `event_interface`。 |
| 22 ABN | match | match | match | match | direct event-to-spike task network 判定稳定。 |
| 12 event SpikeTrack | match | match | match | match | spiking backbone 与连续终端预测层边界稳定。 |
| 03 EAS-SNN | match | match | match | match | 四配置的 role 和 extent 集合均稳定。 |
| 14 EventRPG | match | match | match | match | training/analysis 不被误标成 inference role。 |
| 07 HsVT | match | match | match | match | 混合主任务路径稳定归 `task_network`。 |

## 4. Confusion and disposition

唯一 confusion pair：

| First pass | Blind recheck | Count | Case |
| --- | --- | ---: | --- |
| `embedded_module` | `event_interface` | 1 | FLAME（06） |

FLAME 的直接证据是：raw events 驱动多分支 LIF，达到 threshold 后 reset，并输出新的 binary event trains；这些事件经逐 timestamp pooling 后作为 `E_flat(t)` 交给连续 EA-HiPPO SSM。首轮强调它是不可分离的 task-specific latent front-end，因而选择 `embedded_module`；第二轮按 codebook 的“交付显式表示至主特征提取器”合同，选择 `event_interface`。

这不是需要 Sol 猜测的事实缺口，而是规则边界：学习得到的 event train 在立即 pooling 后交给连续 principal backbone，是否已经构成“显式表示 handoff”。因此不覆盖首轮 canonical label，继续由现有 `FL-I1` 交 Astra 裁决。

没有第二个相同 confusion pair，也没有 scope、directness 或 extent 的系统性混淆。

## 5. 结论

Pilot 达到预设稳定性门槛。四角色假设目前可以继续使用：interface、task network、embedded module 和 algorithmic engine 在其余九个困难 case 中均可复现；配置级 purity、training/attack 的 `not_applicable` role、PPLN 假阳性及三层时间轴也保持稳定。

当前不应直接把 codebook 宣布为 v1.0。下一步是把本报告、完整 30 篇结果和四项 evidence-ready issue 一并交给 Astra：优先裁决 FLAME 的 interface/module handoff 规则，然后处理 ABN architecture/credit conflict 与 DailyDVS split conflict，决定是否需要小范围规则修订或补充校准样本。
