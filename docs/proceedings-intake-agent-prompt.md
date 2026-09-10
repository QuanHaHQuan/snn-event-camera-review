# Proceedings Intake Agent Prompt

Replace every value in angle brackets before starting:

- `<VENUE>`: one of `CVPR`, `ICCV`, `ECCV`, `NeurIPS`, `ICML`, or `ICLR`;
- `<YEAR>`: four-digit year;
- `<OFFICIAL_PROCEEDINGS_URL>`: complete official proceedings or accepted-paper-list URL.

Then give the following instruction to the proceedings intake agent.

---

你现在只负责把 `<VENUE> <YEAR>` 官方 proceedings 接入现有仓库，并准备供后续指挥窗口进行双轨语义筛选的完整候选证据。不要自行决定 Survey Core、Advisor Core 或 reading assignment。

仓库：`snn-event-camera-review`

官方入口：`<OFFICIAL_PROCEEDINGS_URL>`

开始前必须完整读取：

```text
docs/workflow-instructions.md
00-index/README.md
04-templates/conference-report.md
04-templates/paper-card.md
scripts/README.md
```

## 任务边界

本阶段只完成：

1. 官方 scope 核验；
2. 完整 mother list；
3. 高召回候选检索；
4. 每位候选的完整官方 title、abstract 和下载信息；
5. A/B/C/X 检索 provenance；
6. paper cards；
7. 可恢复、可审计的交接报告。

本阶段禁止：

- 修改 `00-index/candidate-screening-audit.csv`；
- 修改 `paper-selection.csv`、两个 reading plan、Survey reference pool 或 outline；
- 决定 `survey_role`、`advisor_role`、Core membership 或 reading status；
- 根据旧 A/B/C、旧优先级或关键词数量推断阅读优先级；
- commit 或 push；
- 把 PDF、网页缓存、raw parser output 或临时脚本加入 Git。

## 官方范围

- 只处理 `<VENUE> <YEAR>` 官方正式长论文。
- 排除 workshop、demo、challenge、tutorial、invited talk 和非正式项目页。
- NeurIPS 必须包含官方 proceedings 中全部正式 long-paper tracks，并逐篇保存 `official_track`；其他会议若官方有明确 track，也保留原始 track。
- 先确认官方列表已经完整 online；不完整时停止并报告缺失，不得用第三方列表拼成“完整 proceedings”。

## 输出目录

创建或更新：

```text
01-papers-by-conference/<VENUE><YEAR>/
```

必须产出：

```text
mother-list.csv
candidates.csv
abc-reviewed.csv
A/*.md
B/*.md
C/*.md
X/*.md
```

`search-report.md` 是生成视图，本阶段不要手写最终版本；后续语义筛选运行生成器后统一产生。

## Mother List

`mother-list.csv` 必须覆盖官方 scope 内全部论文，一篇一行，至少包含：

```text
id,title,authors,conference,year,official_track,official_page,pdf_link,status_or_award,source_url
```

若现有会议目录的 schema 有兼容差异，应保留当前生成器所需字段，但不得丢失上述语义信息。要求：

- ID 在全仓库唯一，格式稳定，建议 `<VENUE><YEAR>-NNNN`；
- title、authors、track、官方页面和 PDF URL 来自官方来源；
- 不得只保存搜索命中的论文；
- 去重后数量必须与官方 proceedings 数量一致，或在报告中逐项解释差异。

## 高召回检索

只把检索当作召回，不把关键词命中当语义结论。

在官方提供摘要时，对 mother list 的完整 title + complete official abstract 做召回；官方列表不含摘要时，逐篇访问 official paper page 获取摘要后再召回。不要只查 title。

至少覆盖以下召回轴，并处理缩写、复数、连字符和大小写变体：

1. Event camera / DVS：`event camera`, `event-based vision`, `event stream`, `event representation`, `DVS`, `DVXplorer`, `neuromorphic vision`, `asynchronous vision`, `event voxel`, `event cloud`, `event point`；
2. SNN：`spiking neural network`, `spiking`, `spike-driven`, `LIF`, `IF neuron`, `membrane potential`, `surrogate gradient`, `ANN-SNN conversion`, `neuromorphic computing`；
3. Advisor SECNet-SNN implementation direction：`spiking neuron`, `LIF`, `PLIF`, `adaptive neuron`, `surrogate gradient`, `STBP`, `online training`, `spiking transformer`, `spike-driven`, `point SNN`, `temporal delay`, `spike sparsity`, `event-driven deployment`；
4. 高风险歧义词：`event`, `spike`, `asynchronous`, `frequency`。这些命中必须通过完整摘要排除 event log、temporal point process、spike camera、biological spike sorting、普通 asynchronous optimization 和无关 signal processing。

为降低漏检，还要做组合与反向检查：

- 所有 SNN 候选检查摘要中是否实际使用 event-camera/DVS 输入，而不是只在 neuromorphic dataset 上做通用 benchmark；
- 所有 event-camera 候选检查摘要中是否实际包含 SNN/spiking mechanism；
- 所有 Advisor SNN 候选检查是否提供可迁移到 SECNet 的 input encoding、point hierarchy、neuron、aggregation、temporal operator、training、efficiency 或 deployment mechanism；
- 所有标题不明显但摘要命中的论文必须保留为 candidate；
- 对边界词分别列出 false positives，不得静默删除。

## Candidate Evidence

`candidates.csv` 必须包含每篇候选的：

```text
id,title,authors,conference,year,official_track,official_page,pdf_link,
abstract,abstract_sha256,matched_terms,matched_axis,retrieval_reason
```

如果兼容现有 schema 需要额外列，可以增加；不得删掉完整 abstract 和 SHA256。摘要必须是未经总结改写的完整官方文本。SHA256 对去除首尾空白后的实际保存字符串计算。

每个 candidate 必须创建 paper card，至少包含：

- official metadata；
- complete official abstract；
- retrieval axis 和命中理由；
- `semantic screening pending`；
- PDF 才能确认的机制、公式、表格和数值不得从摘要猜测。

## A/B/C/X 仅作检索 provenance

- `A`: official title/abstract 明确同时包含 event-camera processing 与真实 SNN/spiking mechanism；
- `B`: event-camera/event-stream 侧候选，但摘要未建立真实 SNN mechanism；
- `C`: SNN/spiking 侧候选，但摘要未建立 event-camera integration；
- `X`: 歧义召回或双轨均明显无关的 false positive。

不要因为一篇论文被标为 `X` 就删除它；X paper card 和 candidate row 必须保留，供指挥窗口审计。A/B/C/X 不决定是否进入 active corpus、reference pool 或 Core。

`abc-reviewed.csv` 在 intake 暂存阶段只包含 A/B/C provenance rows；X 保留在 `candidates.csv` 和 `X/` cards 中。后续指挥窗口完成双轨语义审计后，会让 active candidates 保持 A/B/C provenance、让 dual-excluded candidates 保持 X provenance，以满足当前 active metadata 校验；这是语义结果反向同步 provenance，不是让 A/B/C 决定语义角色。它至少包含兼容 `scripts/update_index.py` 的字段：

```text
id,title,authors,conference,year,official_track,level,category,
pdf_link,official_page,abstract,matched_keywords,classification_reason,card_path,notes
```

## 恢复和异常处理

- 单篇下载或 official page 失败时，至少尝试三个官方或作者提供来源；仍失败则记录错误并继续其他论文，不得暂停整个会议。
- 只有 mother list 官方 scope 不完整、官方来源整体不可用或 ID 冲突无法安全解决时才停止。
- PDF 不是本阶段必需输入。只有摘要无法确认检索 provenance 时才做 boundary PDF check，并在报告中单列。
- 不要把第三方搜索摘要当 official abstract。

## 验证

交付前必须验证：

1. mother-list ID、title 唯一；
2. mother-list 数量与官方 scope 一致；
3. candidates 是 mother list 的严格子集；
4. 每个 candidate 都有完整官方 abstract、official page 和有效 SHA256；
5. A/B/C/X cards 与 candidates 一一对应；
6. `abc-reviewed.csv` 恰好等于 A/B/C candidate 子集；
7. NeurIPS 的 `official_track` 无缺失；
8. 无 PDF、cache、临时提取文件进入 Git；
9. `git diff --check` 通过。

不要运行 `scripts/update_selection.py`，因为本阶段没有权限写全局语义 audit。可以运行只读或本阶段局部验证；不要生成或覆盖全局 reading plans。

## 最终报告

完成后暂停，不 commit、不 push。报告：

- 官方 scope 与 URL；
- mother-list 数量及 track 分布；
- candidates 总数；
- A/B/C/X 数量；
- 每个 retrieval axis 数量；
- title-only 命中与 abstract-only 命中数量；
- 边界 PDF check 和 unresolved 数量；
- 新增/修改文件；
- 验证结果；
- 当前 `git status --short`；
- 明确写出：`semantic screening and Core decisions pending in the command window`。

---

After this agent finishes, return to the command window and use `docs/proceedings-semantic-integration-prompt.md`.
