# Taxonomy codebook migration：0.1-design → 0.2

日期：2026-09-10。发布性质：checkpoint calibration release，**未冻结**。源快照：`5078db6`；完整commit及快照hash写入 `04-templates/taxonomy-paper-annotation-schema.json` 的 `pilot_baseline`。

## 1. 版本与结构兼容性

- 当前36条配置行的codebook_version统一为0.2。数量仍为30篇，原paper_id、canonical title、official abstract/hash及annotation_unit不变。
- CSV仍为59列，header-only的 `taxonomy-paper-annotation-schema.csv` **字节不变**，不添加伪论文示例。新伴随JSON契约记录同一59列、受控词表、nested enum、版本和历史快照；validator同时校验codebook的F01–F59及词表镜像。
- primary role词表、scope、selection/inclusion词表均未增加。新实质标签只有 `architecture_family: mlp` 和 `representation_form: neuronal_spike_train`；后者用于修复FLAME被误记为sensor binary occupancy的矛盾。
- 0.1-design仍是历史事件/盲重标版本；不是当前新标注可选版本。旧盲重标两份CSV、报告及前70条事件原样保留。

## 2. 语义迁移清单

| paper_id | 字段/旧值 | 0.2值与原因 | 裁决/未决事项 |
| --- | --- | --- | --- |
| NeurIPS2025-0641 FLAME | primary: embedded_module | event_interface；EAL新event trains→逐timestamp pooling→E_flat(t)→连续EA-HiPPO满足I1–I4 | FL-I1 resolved；旧FL-E3与blind分歧保留；当前依据FL-A1 |
| NeurIPS2025-0641 | representation: binary_map | neuronal_spike_train；这是neuron生成的交接流，非sensor occupancy | FL-I2 resolved；FL-A2；hybrid extent不变 |
| ECCV2024-0096 ABN | architecture: other_documented | mlp；原文明确的多层全连接spiking承载架构 | AB-I1 resolved；AB-A1 |
| ECCV2024-0096 | credit: surrogate_bptt；route: direct_snn | 两项unknown；实验STBP与结论STDP没有phase/config对应，不能断言实际训练路线 | AB-I2 deferred；分别保留p.10/p.14证据AB-A2/3和限制AB-A4 |
| ICML2025-2762 HsVT | architecture: conv_residual;recurrent;transformer_attention | conv_residual;mlp;recurrent;transformer_attention；明确命名的SpikingMLP是功能组件，不是给所有Transformer FFN加标签 | HV-I1 resolved；HV-A1；role和extent不变 |
| ECCV2024-1631 DailyDVS | dataset setting: cross_subject；split无保留说明 | setting=unknown；split保留作者cross-subject声明及冲突，不刊更正ID/人数 | DD-I1 deferred / owner由sol_high转astra；DD-A1/2记录官方README仍冲突，authority不变 |
| CVPR2025-0053 conversion | learning_signal: distillation | unknown；已有CV-E1仅支持ANN转换/阈值校准，不能证明teacher objective，不推断另一种监督 | CV-I1 deferred / astra；CV-A1；ann_to_snn和foundation均不变 |

受上述裁决的五篇使用astra_adjudicated，范围仅包括表中字段及关联理由、证据、置信度、issue、用途限制；**不表示Astra重读了该行全部59字段的原文**。原annotator保留Sol，事件annotator记录Astra。其他行仅做版本或trigger规范化，保留Sol原review_status。

原四项evidence-ready问题中两个resolved、两个deferred；新增FL-I2/HV-I1两个联动resolved事项及CV-I1非决定性证据缺口。全pilot去重issue共11项，8 resolved、3 deferred。AB/DD/CV三项事实缺口不计“已解决”，也不用于相应确定性比较统计。

## 3. Trigger规范化：不扩大词表

旧validator只校验JSON keys，没有检查trigger取值，因此六种未经批准的拼写进入八行。依原问题含义确定性映射，不改问句的事实答案。

| 旧值 | 受控值 | 受影响paper_id |
| --- | --- | --- |
| benchmark_contamination | input_identity | ICML2024-0803 |
| spike_term | misleading_terms | CVPR2025-1552、ECCV2024-0945、NeurIPS2024-2307 |
| lookahead | neuron_state_time | CVPR2024-1880 |
| training_conflict | source_conflict | ECCV2024-0096 |
| metadata_conflict | source_conflict | ECCV2024-1631 |
| time_conflict | neuron_state_time | ICLR2026-1286 |

这些旧值仅保存在迁移事件的from字段，不作为兼容alias继续被validator接受。issue.type中的metadata_conflict/time_conflict本来合法，不受此trigger规范化影响。不同层级的词表不能混用。

## 4. 追溯与执行方式

`taxonomy-pilot-events.csv`由70增至107条：原70条byte prefix保留；新增 `ASTRA-02-001` 至 `ASTRA-02-037`。其中32条codebook_migration、5条astra_adjudication。每个更改字段以完整from/to保存，包括嵌套JSON单元格；第二次对conversion行的保守修正也有独立事件，不覆盖前次迁移。

validator从当前CSV逆序应用新事件，检查每个to是否匹配，再比对还原后0.1全部行的canonical SHA256。它还验证原70条事件的canonical hash及三份blind文件的byte hash，避免通过修正历史分歧抬高agreement。最终运行时额外确认原事件byte prefix与源快照一致。

当前只读命令：

```sh
python3 scripts/validate_taxonomy_pilot.py
git diff --check
```

`scripts/validate_taxonomy_pilot.py`从旧ignored work运行器移植并扩展，正式读取伴随JSON契约。旧 `work/validate_taxonomy_pilot.py` 不修改，也不应再用于验证0.2；它仍只接受0.1，是历史工具，不是新入口。本次未运行任何generator。

validator验证：audit身份/完整摘要hash精确join、CSV列与codebook/schema完全一致、枚举顺序与nested enums、重复/悬空evidence ID、main taxonomy的scope门、engine必须有algorithm_update、neuronal_spike_train必须有confirmed interface、Astra review的issue disposition、配置级purity及PDF-check调度状态。原先end-to-end边界检查把不存在的fusion也拒绝，现允许absent组件；未知、混合和continuous组件仍不合格。此次没有记录被升级成end-to-end。

它是当前pilot的结构/追溯验证器，不是通用572篇工作流生成器，不从合法标签反推出论文事实，也不检验I1–I4的科学语义。补充校准的新样本另表共用0.2契约，增加相应的schema检查入口；不得改写原pilot_baseline或删掉历史保护以容纳新行。旧case定向重判另记审计结果，再决定是否迁移canonical行。

## 5. 验证结果与限制

- 正向：30个canonical paper、36配置、59列、107事件通过；源audit join及完整摘要hash一致。
- 历史：两份blind CSV和blind报告不改，原始primary agreement仍9/10；原70条事件不改；当前各更改字段可逆恢复0.1。
- 七项临时负例均被特定检查拒绝：未知architecture标签、未批准nested trigger、非法issue status、悬空evidence引用、foundation进入主role图、历史事件覆盖、无迁移事件的annotation改动。测试在临时目录运行，未更改实际pilot数据；不是新论文标注。
- Python AST解析通过；`git diff --check`通过。初次检查发现CSV writer默认CRLF被Git视为trailing whitespace，已将新增记录规范为仓库LF并重新验证，既有70条事件字节保持不变。
- 仍有三项deferred来源事实和未覆盖的方法家族；0.2没有完成新的盲重标或最小补充校准，不能宣称规则已冻结、全部非关键字段已具备最终写作证据，或150–180篇已选完。

下一步严格限于 [checkpoint §6](taxonomy-checkpoint-adjudication.md#6-冻结前最小补充校准) 的新样本证据槽位与旧边界定向重判；本次本地commit后停止，不push。
