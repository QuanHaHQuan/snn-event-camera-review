# Proceedings Semantic Integration Prompt

Use this prompt in the command window after a proceedings intake agent has completed `docs/proceedings-intake-agent-prompt.md`.

Replace `<VENUE>` and `<YEAR>` before use.

---

请对刚接入的 `<VENUE> <YEAR>` proceedings 执行全量语义审计，并把它无缝整合到当前 Survey/Advisor 双轨语料库。

开始前完整读取：

```text
docs/workflow-instructions.md
00-index/README.md
03-review-draft/outline.md
03-review-draft/advisor-frequency-reading-map.md
00-index/reading-plan-survey-core.md
00-index/reading-plan-advisor-core.md
00-index/survey-reference-pool.csv
00-index/candidate-screening-audit.csv
01-papers-by-conference/<VENUE><YEAR>/mother-list.csv
01-papers-by-conference/<VENUE><YEAR>/candidates.csv
01-papers-by-conference/<VENUE><YEAR>/abc-reviewed.csv
```

## 审计目标

对该会议 `candidates.csv` 中的每一篇论文，至少完整阅读 official title + complete official abstract；不能只看 title、关键词、A/B/C/X、旧 reason 或检索 agent 的结论。检索 agent 的产物是召回 provenance，不是最终语义判断。

逐篇写入唯一可编辑语义源：

```text
00-index/candidate-screening-audit.csv
```

不得手工编辑以下生成视图：

```text
00-index/retained-papers.csv
00-index/conferences.md
00-index/paper-selection.csv
00-index/reading-plan-survey-core.md
00-index/survey-reference-pool.csv
00-index/reading-plan-advisor-core.md
01-papers-by-conference/*/search-report.md
06-reading-summaries/v2/index.md
06-reading-summaries/v2/survey/index.md
06-reading-summaries/v2/advisor/index.md
```

## Survey 判断

Survey 主题严格限定为 `Spiking Neural Networks for Event Cameras`，结构是并行基础加交叉接口：

1. event-camera data organization and representation；
2. SNN computation、temporal learning、training and efficiency；
3. event camera 与 SNN 的 interface/integration topology；
4. task/evidence comparison and open problems。

角色只用：

- `anchor`: event-camera input/representation 与真实 SNN mechanism 构成论文核心贡献；
- `included`: 确实属于交叉方向，但贡献较窄、任务特定或主要用于安全/数据/应用；
- `background`: 对 event representation、SNN dynamics/training/efficiency、强非 SNN comparator、dataset/benchmark 或 open challenge 有不可替代的支撑，但不是交叉核心；
- `exclude`: 对严格综述没有可用论证角色。

注意：

- 仅在 DVS 数据集上测试的 generic SNN 不等于 SNN-for-event-camera integration；
- threshold、memory update、event-driven 或 stateful 不自动等于 SNN；
- spike camera 与 event camera/DVS 不同；
- generic event vision 不能因“可能可作背景”全部保留，必须给出具体 survey section 和非冗余作用。

## Advisor 判断

Advisor 主线严格为：SECNet/Event Cloud + frequency/Fourier/FFT + SNN。Mamba/SSM 本身不属于主线；只有可拆出的 Event Cloud、FFT/frequency 或 SNN coupling mechanism 才有价值。

角色只用：

- `method_chain`: SECNet、Event Cloud hierarchy、FFT/frequency module 或 SNN coupling 的直接前驱/最近机制链；
- `discussion`: 有明确可讨论、可迁移的模块、数据组织、频率接口或实验 comparator；
- `watch`: 关联较弱但保留检索价值；
- `exclude`: 对确认的扩刊方向无实际用途。

不要把所有 frequency、wavelet、event 或 point-cloud 论文都加入 Advisor。必须说明 signal、sampling、transform、axis、insertion point、spike interaction 中至少哪一项可用于 SECNet；摘要无法确认关键边界时再标记 PDF check。

## Core 与 Reading Assignment

Core enrollment 必须比角色判断更严格，而且不能机械按新论文优先：

- Survey `anchor` 通常是 Core 候选，但仍要检查是否与现有 Core 重复、是否填补 outline 的真实证据缺口；
- `included`/`background` 只有在填补非冗余章节缺口或提供必要 comparator/benchmark 时进入 Survey Core；
- Advisor 只选择开学前确实必须掌握的 `advisor_required` 和少量可拆机制的 `advisor_helpful`；
- `method_chain`、`discussion`、`watch` 不自动进入 Advisor Core；
- 两轨均 `exclude` 时设为 `excluded_from_active_corpus`，但保留 audit row 和 conference provenance；
- 不进行自动升降。每个新增、移出或保持 Core 的决定必须有 title + abstract 证据和与现有 Core/outline 的比较理由。

若新会议带来 Core 变更，必须逐项报告：

- 新增哪些论文；
- 是否替换或移出旧 Core；
- 填补哪个 outline/Advisor knowledge gap；
- 为什么 reference pool 不足以承载它；
- 预计采用 full V2 还是 focused V2。

## Audit Row

严格使用现有 header：

```text
paper_id,title,year,venue,official_track,in_active_corpus,
abstract_reviewed,abstract_sha256,abstract,official_page,
survey_role,survey_topics,survey_core_decision,survey_reason,
advisor_role,advisor_topics,advisor_core_decision,advisor_reason,
reading_status,needs_pdf_check,evidence_basis,
pdf_boundary_check,pdf_boundary_finding
```

要求：

- abstract 原样保存完整官方文本；
- `abstract_reviewed=yes`；
- SHA256 必须根据实际保存 abstract 重算；
- topics 只用 `scripts/update_selection.py` 中当前受控词表；
- reason 必须具体到论文机制、综述章节或 Advisor 接口；
- `needs_pdf_check=yes` 只用于摘要无法解决且会实质影响角色/Core 的边界；
- unresolved paper 不得进入 Survey Core；
- PDF check 只核查具体边界，不进行无目的全文扩展。

同时核查 intake agent 的 provenance：

- 如果 A/B/C/X 与完整摘要明显不符，修正 conference provenance 和 card；
- 当前生成器要求 `abc-reviewed.csv` 与 active metadata 对齐：双轨至少一侧保留的 candidate 使用 A/B/C provenance 并进入 `abc-reviewed.csv`，双轨均 `exclude` 的 candidate 使用 X provenance、保留在 `candidates.csv`、`X/` card 和 audit 中但不进入 `abc-reviewed.csv`；这是语义审计结果同步 provenance 视图，不允许反过来根据 A/B/C 决定角色；
- 如果发现漏召回，只能在能够说明母表中哪篇 title/abstract 满足召回轴时补入 candidates、card、provenance 和 audit；
- 不删除 mother list；
- 不因语义双轨 exclude 删除 candidate/X card 或 audit evidence。

## 生成和验证

审计完成后运行：

```bash
python3 scripts/update_index.py
python3 scripts/update_selection.py
python3 scripts/update_v2_indexes.py
python3 scripts/validate_literature_graph.py
git diff --check
```

然后额外验证：

1. 新会议 candidate IDs 与该会议 audit IDs 完全一致；
2. complete official abstracts 与 SHA256 全部匹配；
3. active + dual-excluded 正好覆盖所有新 candidate；
4. A/B/C retained rows 与 active metadata 一致；
5. Core、reference pool、Advisor plan 的新增数量可解释；
6. `work/`、PDF、cache 和 raw extraction 未进入版本控制。

## 输出边界

- 不生成 V1/V2；
- 不修改 `03-review-draft/outline.md`，除非用户明确要求本次同时执行 outline checkpoint；
- 新会议加入并不自动触发 outline 重写；只有新增 Core 形成明确章节缺口或达到约 10 篇新 Survey V2 的 checkpoint 时再调整 outline；
- 不 commit、不 push，等待用户检查最终报告。

## 最终报告

报告：

- mother list、candidate、A/B/C/X 数量；
- 对每篇 candidate 完整 title + abstract 审阅覆盖率；
- Survey 和 Advisor role 分布；
- active 与 dual-excluded 数量；
- 新增 Survey Core、Advisor required/helpful、reference pool 数量和标题；
- `needs_pdf_check=yes` 及其具体边界；
- 全局更新后 Survey Core、reference pool、Advisor Core 和 V2 进度；
- 所有验证命令结果；
- 修改文件和 `git status --short`；
- 明确写出未 commit、未 push。

---

The command window should review this report before providing commit/push instructions.
