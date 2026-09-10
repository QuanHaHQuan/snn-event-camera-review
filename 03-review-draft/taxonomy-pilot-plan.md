# Taxonomy pilot plan

日期：2026-09-10。版本：**pilot design v0.1 / 30 papers，未执行**。

用户确认codebook后由Sol High执行；完成后回Astra修订规则。本文件只给选择理由、现有摘要线索、边界和具体检查问题，不填论文的scope/role/neuron/训练/纯度等最终annotation，也不决定usable membership。canonical title、paper ID、venue/year从当前audit精确取得。

## 1. 抽样策略与证据约束

这是刻意的最大差异/困难边界样本，不用于估计572篇的真实类别比例。先从完整audit及全局资料发现潜在失败点，再选能相互反证的论文；包含当前Core以外、inactive负例、同名不同对象和旧证据冲突，不能用“都属于四类”作成功标准。

30篇中：19篇旧Survey Core、11篇非Core；27篇active、3篇inactive。这些只是抽样来源属性，执行者的首遍隐藏旧role/Core标签。所有30篇已检查完整存储官方标题和摘要来制定检查点；机制细节不由标题或旧标签补齐。

27篇预计PDF-required，3篇可仅用完整摘要完成受限的scope/use负例筛选；后者一旦拟保留机制/数字/中央比较用途仍触发PDF。高PDF比例来自pilot故意富集困难例，不应用到全部572篇。PDF-required只读能回答本行问题的页面，不要求生成V2或逐段精读全文。

按A→B→C→D批次执行且保留初判：A接口/表示（01–06）、B系统/角色重叠（07–15）、C基础与非SNN对照（16–25）、D召回负例与补充挑战（26–30）。原始title/abstract-only判定封存后再读PDF和旧locator；每次修正记录字段、旧值、新证据和适用规则。

## 2. 30篇真实论文与检查点

### 01. ICLR2024-1097

**Canonical title:** SpikePoint: An Efficient Point-based Spiking Neural Network for Event Cameras Action Recognition
**Venue/year:** ICLR 2024
**阅读要求:** PDF-required

- 选择理由：point/Event Cloud、recognition、主干与能耗宣称同时出现；打破raw输入等于原生spike的推断。
- 测试边界：point_set与raw_event_sequence；rate recoding与address injection；group order与simulation step。
- 完整摘要中的选择线索（转述，非最终判定）：摘要明确point-based SNN、sparse event cloud、surrogate training和16 timesteps，没有完整定义输入spike接口。
- PDF具体问题：点的x/y/t/p哪些保留？grouping/normalization之后怎样进入首个neuron？16步对应什么轴，state在哪重置？能耗包括sampling/grouping吗？

### 02. ECCV2024-1778

**Canonical title:** Spike-Temporal Latent Representation for Energy-Efficient Event-to-Video Reconstruction
**Venue/year:** ECCV 2024
**阅读要求:** PDF-required

- 选择理由：voxel输入和重建任务；同时有算法型encoder与U形decoder，挑战单primary。
- 测试边界：algorithmic_engine vs task_network；learned latent不是新representation结构；continuous output与fullyspiking。
- 完整摘要中的选择线索（转述，非最终判定）：摘要明确event voxels、SVT、U-shape SNN Decoder及近似ISTA fixed point。
- PDF具体问题：SVT每个spike/state与ISTA何变量/步骤对应？主要贡献证据偏encoder还是整体？decoder/readout是否spiking，能耗何配置何范围？

### 03. ECCV2024-1168

**Canonical title:** EAS-SNN: End-to-End Adaptive Sampling and Representation for Event-based Detection with Recurrent Spiking Neural Networks
**Venue/year:** ECCV 2024
**阅读要求:** PDF-required

- 选择理由：SNN自适应sampling与SNN/ANN下游变体，并有专门训练设计。
- 测试边界：event_interface vs embedded_module/task_network；role与joint training分开。
- 完整摘要中的选择线索（转述，非最终判定）：摘要明确recurrent convolutional SNN采样、RPD/SAT、SNN和non-spiking detector验证。
- PDF具体问题：采样输出是spike、event subset还是dense tensor？与backbone的交接在哪？ANN/SNN版本是否要拆annotation_unit？三步是什么时间轴？

### 04. CVPR2026-1873

**Canonical title:** Spike-driven Discrete Aggregation for Event-based Object Detection
**Venue/year:** CVPR 2026
**阅读要求:** PDF-required

- 选择理由：最新事件选择/aggregation方法，摘要既说spike-inspired又说gated recurrent spiking neurons。
- 测试边界：阈值门控与真实neuron；interface与主干；fullyspiking宣称范围。
- 完整摘要中的选择线索（转述，非最终判定）：摘要明确discrete selection、SDA、MTF和非SNN模型兼容。
- PDF具体问题：gated neuron的state/firing/reset是什么？输出选择如何构造表示？MTF及detector是否连续；fullyspiking究竟指哪个变体？

### 05. NeurIPS2024-2388

**Canonical title:** Spiking Neural Network as Adaptive Event Stream Slicer
**Venue/year:** NeurIPS 2024
**阅读要求:** PDF-required

- 选择理由：最清楚的spike控制event slicing候选，作为interface规则校准对照。
- 测试边界：控制输出与latent feature；ANN反馈训练与hybrid inference。
- 完整摘要中的选择线索（转述，非最终判定）：摘要明确SNN触发切片、SPA-Loss和下游ANN反馈。
- PDF具体问题：发放时刻如何转切片边界？SNN输入先聚合吗？ANN反馈仅训练还是推理也使用？如何计等待窗口延迟？

### 06. NeurIPS2025-0641

**Canonical title:** FLAME: Fast Long-context Adaptive Memory for Event-based Vision
**Venue/year:** NeurIPS 2025
**阅读要求:** PDF-required

- 选择理由：event-by-event/raw候选；LIF特征器与SSM记忆共存，刻意挑战hybrid front-end。
- 测试边界：event_interface vs embedded_module；network memory与neuron state；native physical time。
- 完整摘要中的选择线索（转述，非最终判定）：摘要明确LIF Event Attention Layer、EA-HiPPO按inter-event intervals调整记忆。
- PDF具体问题：LIF是否真的输出离散spikes参与下游？event attention交接的是显式表示还是latent feature？HiPPO更新与LIF更新使用哪种时间，是否依赖同步packet？

### 07. ICML2025-2762

**Canonical title:** Hybrid Spiking Vision Transformer for Object Detection with Event Cameras
**Venue/year:** ICML 2025
**阅读要求:** PDF-required

- 选择理由：混合Spiking Vision Transformer；摘要未充分展开spiking boundary。
- 测试边界：task_network vs embedded_module；architecture名字不能证明purity。
- 完整摘要中的选择线索（转述，非最终判定）：摘要说明空间/时间feature modules和hybrid spike Vision Transformer，但缺模块级算子。
- PDF具体问题：哪些spatial/temporal模块真spiking？attention、normalization、recurrent部分、head各是什么？Fall DVS来源是否模拟，数据与能耗配置是否匹配？

### 08. CVPR2025-2047

**Canonical title:** Efficient Event-Based Object Detection: A Hybrid Neural Network with Spatial and Temporal Attention
**Venue/year:** CVPR 2025
**阅读要求:** PDF-required

- 选择理由：同时包含SNN-ANN bridge、快慢状态和数字neuromorphic hardware声称。
- 测试边界：hybrid_subnetwork vs fully_spiking_backbone；局部硬件与端到端系统能耗。
- 完整摘要中的选择线索（转述，非最终判定）：摘要明确稀疏SNN层经bridge转dense ANN特征，含DWConvLSTM变体和芯片实现。
- PDF具体问题：芯片运行哪些block，host运行哪些？bridge算子和I/O成本计入了吗？SNN短步与ANN慢动态如何映射？报告的延迟是实测还是推算？

### 09. ICCV2025-1790

**Canonical title:** ClearSight: Human Vision-Inspired Solutions for Event-Based Motion Deblurring
**Venue/year:** ICCV 2025
**阅读要求:** PDF-required

- 选择理由：RGB-event restoration，跨模态控制neuron配置，测试融合的位置和神经元适应。
- 测试边界：embedded SNN支路与主任务网络；multimodality不是multi-representation。
- 完整摘要中的选择线索（转述，非最终判定）：摘要明确SNN运动features、ANN颜色处理、NCM及RBAM。
- PDF具体问题：NCM改变哪些neuron参数/状态？跨模态反馈方向和时刻是什么？RBAM是否spiking？SNN输出是否仅局部motion feature，最终decoder/readout何类型？

### 10. NeurIPS2025-4041

**Canonical title:** Fully Spiking Neural Networks for Unified Frame-Event Object Tracking
**Venue/year:** NeurIPS 2025
**阅读要求:** PDF-required

- 选择理由：fullyspiking frame-event tracking强宣称，同时涉及局部conv和全局Transformer。
- 测试边界：fully_spiking_task_network vs pipeline；RGB输入编码与event输入编码区分。
- 完整摘要中的选择线索（转述，非最终判定）：摘要明确SpikeFET、conv与Transformer融合、RPM和STR。
- PDF具体问题：两模态在哪里变成neuronalspike？RPM/type encoding、fusion、head、readout有哪些continuous例外？power是估计还是测量、涵盖哪些部分？

### 11. CVPR2026-1935

**Canonical title:** SpikeTrack: A Spike-driven Framework for Efficient Visual Tracking
**Venue/year:** CVPR 2026
**阅读要求:** PDF-required

- 选择理由：与下一篇同名SpikeTrack做完整标题/输入对照；两篇同年同会但一篇是RGB追踪。
- 测试边界：canonical identity；RGB SNN与event-camera SNN；memory module不是算法engine的充分条件。
- 完整摘要中的选择线索（转述，非最终判定）：完整摘要明确energy-efficient RGB object tracking、asymmetric timestep expansion和memory-retrieval module。
- PDF具体问题：输入是否仅RGB，是否存在event-camera设计？asymmetric timestep如何编码图像，memory retrieval是普通模块还是显式算法对应？1/26能耗来源与系统边界是什么？

### 12. CVPR2026-1798

**Canonical title:** SpikeTrack: High-performance and Energy-efficient Event-Based Object Tracking with Spiking Neural Network
**Venue/year:** CVPR 2026
**阅读要求:** PDF-required

- 选择理由：与另一篇同名SpikeTrack做身份对照，并测试整数训练/脉冲推理。
- 测试边界：canonical title去重；integer_train_spike_infer vs ANN conversion；training与inference信号差异。
- 完整摘要中的选择线索（转述，非最终判定）：摘要明确event-camera tracking、DI-LIF训练时integer activations推理转spikes。
- PDF具体问题：DI-LIF完整状态式及训练→推理映射是什么？属于离散训练映射还是ANN预训练conversion？head/memory边界如何，所谓purely spike-driven覆盖到哪？

### 13. NeurIPS2024-1436

**Canonical title:** Continuous Spatiotemporal Events Decoupling through Spike-based Bayesian Computation
**Venue/year:** NeurIPS 2024
**阅读要求:** PDF-required

- 选择理由：无传统深度backbone的Bayesian motion segmentation和STDP案例。
- 测试边界：algorithmic_engine覆盖性；local_plasticity与普通training；task/output分离。
- 完整摘要中的选择线索（转述，非最终判定）：摘要明确WTA对应EM的E-step，STDP对应M-step及事件motion segmentation。
- PDF具体问题：事件warping/contrast计算哪些仍连续？STDP在线更新属于推断还是训练阶段？WTA竞争输出和运动参数怎样读出，真实event time怎样驱动？

### 14. ICLR2024-0249

**Canonical title:** EventRPG: Event Data Augmentation with Relevance Propagation Guidance
**Venue/year:** ICLR 2024
**阅读要求:** PDF-required

- 选择理由：event-specific augmentation/relevance工作，不能因现成SNN分类器而新设backbone类别。
- 测试边界：training/analysis contribution与primary not_applicable；benchmark_only边界。
- 完整摘要中的选择线索（转述，非最终判定）：摘要明确SNN的SLTRP/SLRP和event augmentation，跨SNN结构验证。
- PDF具体问题：augmentation具体操作raw events还是grid？哪些规则依赖SNN时间/发放而非一般ANN？推理网络有没有新功能结构？是否应进入cross_cutting证据而不是role主图？

### 15. ECCV2024-1740

**Canonical title:** Exploring Vulnerabilities in Spiking Neural Networks: Direct Adversarial Attacks on Raw Event Data
**Venue/year:** ECCV 2024
**阅读要求:** PDF-required

- 选择理由：攻击输入raw events但victim可能是grid SNN；测试攻击对象与输入语义。
- 测试边界：raw signal vs network input；event_specific_training_analysis vs generic robustness；证据不能由标题补全。
- 完整摘要中的选择线索（转述，非最终判定）：摘要强调raw-event攻击、grid conversion不透明和sparsity约束。
- PDF具体问题：victim实际输入如何grid化，攻击改timestamp/polarity/位置哪个量？算法中的离散事件与neuronalspike是否不同？威胁预算及成功率对应哪配置？

### 16. ICML2024-0803

**Canonical title:** CLIF: Complementary Leaky Integrate-and-Fire Neuron for Spiking Neural Networks
**Venue/year:** ICML 2024
**阅读要求:** PDF-required

- 选择理由：强SNN基础neuron论文，用来测试一般方法与event integration准入。
- 测试边界：snn_foundation vs core_intersection；multi-state neuron与architecture/role分离。
- 完整摘要中的选择线索（转述，非最终判定）：摘要专门分析LIF时间梯度，CLIF添加路径并保持binary output，未建立event-specific接口。
- PDF具体问题：DVS是否只是评测？互补state如何更新及增加什么内存/算子？支持哪项交叉方法解释，而不是因旧Survey/Advisor Core直接纳入？

### 17. CVPR2025-0053

**Canonical title:** Inference-Scale Complexity in ANN-SNN Conversion for High-Performance and Low-Power Applications
**Venue/year:** CVPR 2025
**阅读要求:** PDF-required

- 选择理由：明确ANN-SNN conversion候选，但摘要没有event-camera integration。
- 测试边界：conversion是training_route，不是primary；converted不自动hybrid。
- 完整摘要中的选择线索（转述，非最终判定）：摘要明确pretrained ANN、local threshold balancing和delayed evaluation，含多任务验证。
- PDF具体问题：转换前后网络哪些层保留连续计算？calibration/训练成本边界是什么？是否有真实event-camera设计，还是只能作为conversion foundation？

### 18. NeurIPS2025-5334

**Canonical title:** STEP: A Unified Spiking Transformer Evaluation Platform for Fair and Reproducible Benchmarking
**Venue/year:** NeurIPS 2025
**阅读要求:** PDF-required

- 选择理由：benchmark/公平能耗强基础；混合静态、event、sequential数据，防止按dataset自动入交叉。
- 测试边界：evaluation_authority vs core_taxonomy_evidence；analytical memory energy vs芯片测量。
- 完整摘要中的选择线索（转述，非最终判定）：摘要明确统一Spiking Transformer评估、controlled ablation、bitwidth/memory analytical energy。
- PDF具体问题：event数据的作用是特定接口研究还是一般基准？能耗模型假设、memory项、对照quantized ANN和T设置怎么定义？哪些结论可作为跨论文公平比较约束？

### 19. CVPR2025-1552

**Canonical title:** Graph Neural Network Combining Event Stream and Periodic Aggregation for Low-Latency Event-based Vision
**Venue/year:** CVPR 2025
**阅读要求:** PDF-required

- 选择理由：图结构与event-by-event强对照；摘要声称低延迟硬件能力，但不等于SNN。
- 测试边界：graph vs spike graph；asynchronous不等于spiking；hardware projection vsmeasurement。
- 完整摘要中的选择线索（转述，非最终判定）：摘要明确异步无累积event branch+periodic graph aggregation，可逐事件预测optical flow。
- PDF具体问题：有无发放/重置的真实neurons？周期分支是否等待未来？tens of microseconds来自实际实现还是硬件投影？图构造/更新成本如何计？

### 20. CVPR2024-1880

**Canonical title:** A Simple and Effective Point-based Network for Event Camera 6-DOFs Pose Relocalization
**Venue/year:** CVPR 2024
**阅读要求:** PDF-required

- 选择理由：point/Event Cloud强foundation，pose回归和Bi-LSTM时间序列，配对SpikePoint。
- 测试边界：raw point不是SNN；timestamp坐标/chronology/causality；任务与role分开。
- 完整摘要中的选择线索（转述，非最终判定）：摘要明确raw Point Cloud、hierarchical features、A-Bi-LSTM和6-DOFs。
- PDF具体问题：xyt/p如何组织，Bi-LSTM使用未来组吗？主干是否非spiking？比较point SNN时哪些输入/协议必须控制，不能把参数少写成energy实测？

### 21. ECCV2024-1737

**Canonical title:** REDIR: Refocus-free Event-based De-occlusion Image Reconstruction
**Venue/year:** ECCV 2024
**阅读要求:** PDF-required

- 选择理由：非Core的真实交叉检索候选，避免pilot只看旧Core；hybrid de-occlusion。
- 测试边界：hidden SNN模块位置；interface与embedded模块；pure-event input不等于pure-SNN。
- 完整摘要中的选择线索（转述，非最终判定）：摘要明确pure event reconstruction、feature registration、mask gate及SNN block内spatiotemporal attention。
- PDF具体问题：注册、mask、attention和decoder中哪些是连续？SNN block何输入输出，主贡献在registration还是spiking功能？如何表示在primary与contribution_focus？

### 22. ECCV2024-0096

**Canonical title:** Asynchronous Bioplausible Neuron for Spiking Neural Networks for Event-Based Vision
**Venue/year:** ECCV 2024
**阅读要求:** PDF-required

- 选择理由：标题同时含SNN和event vision，摘要主要谈generic homeostasis，制造证据张力。
- 测试边界：标题不能弥补event-specific摘要证据；neuron贡献与integration directness。
- 完整摘要中的选择线索（转述，非最终判定）：摘要明确ABN及MG/TRG/SE，但只说多数据集分类/分割，没明确event接口。
- PDF具体问题：是否存在真实event-camera preprocessing或仅DVS评测？ABN的state/firing/reset是什么？asynchronous依据是算法或硬件，能耗证据哪一层？

### 23. ECCV2024-0945

**Canonical title:** FARSE-CNN: Fully Asynchronous, Recurrent and Sparse Event-Based CNN
**Venue/year:** ECCV 2024
**阅读要求:** PDF-required

- 选择理由：完整异步/稀疏/递归却未明确spiking的event方法，防止关键词误判。
- 测试边界：recurrence vs neuron；event_by_event vs真实SNN；foundation的具体比较用途。
- 完整摘要中的选择线索（转述，非最终判定）：摘要明确recurrent+convolution、压缩模块和事件识别/检测，不宣称spiking neuron。
- PDF具体问题：递归单元是否发放/重置还是连续RNN？事件压缩怎样改变时间语义？如果非SNN，它对spiking方法“异步效率独占”主张提供什么反例？

### 24. NeurIPS2024-2307

**Canonical title:** PPLNs: Parametric Piecewise Linear Networks for Event-Based Temporal Modeling and Beyond
**Venue/year:** NeurIPS 2024
**阅读要求:** PDF-required

- 选择理由：摘要把parametric piecewise function称membrane，旧PDF finding称非SNN，测试冲突处理。
- 测试边界：membrane词汇不等于spiking；旧finding只导航；scope fact与use分离。
- 完整摘要中的选择线索（转述，非最终判定）：摘要称parametric piecewise linear membrane，含event/image pose、deblur；旧audit另有非SNN finding。
- PDF具体问题：原PDF是否明确没有离散发放而传递real-valued output？旧finding所在页/式是什么？时间连续函数与neuron state更新有何区别？不能直接照抄旧判断。

### 25. ECCV2024-1631

**Canonical title:** DailyDVS-200: A Comprehensive Benchmark Dataset for Event-Based Action Recognition
**Venue/year:** ECCV 2024
**阅读要求:** PDF-required

- 选择理由：dataset-only event foundation，确保“数据集论文”可有authority用途但没有SNN role。
- 测试边界：dataset_benchmark vs SNN functional role；physical event provenance与split。
- 完整摘要中的选择线索（转述，非最终判定）：摘要明确DailyDVS-200真实采集、多参与者和属性标注，没有SNN方法贡献。
- PDF具体问题：数据实际采集设备/协议、cross-subject split、类别及属性定义在哪里？若仅作为dataset authority需引用哪些原始定义，避免全篇深读？

### 26. CVPR2026-1021

**Canonical title:** 3D Gaussian Splatting from Unposed Spike Stream
**Venue/year:** CVPR 2026
**阅读要求:** abstract-only (conditional)

- 选择理由：inactive高置信术语负例：spike camera加3DGS，标题易误召回。
- 测试边界：spike_camera与contrast-event camera。
- 完整摘要中的选择线索（转述，非最终判定）：完整摘要明确采用spike cameras和unposed spike-camera captures。
- PDF具体问题：默认无需PDF；只有原始来源另称contrast-event输入或拟保留比较用途时，核查sensor生成方程与SNN是否实际存在。

### 27. ICLR2024-1543

**Canonical title:** A Graph is Worth 1-bit Spikes: When Graph Contrastive Learning Meets Spiking Neural Networks
**Venue/year:** ICLR 2024
**阅读要求:** abstract-only (conditional)

- 选择理由：inactive graph+SNN负例，防止把“graph SNN”直接填成event-camera graph交叉。
- 测试边界：非camera graph vs event graph；有SNN不等于有交叉；scope与排除用途分开。
- 完整摘要中的选择线索（转述，非最终判定）：完整摘要研究graph contrastive learning和graph benchmarks，没有event-camera输入设计。
- PDF具体问题：默认只做摘要级scope/use筛选；若Astra拟将其保留为graph-SNN基础，须核查输入图来源与真实发放机制，再说明不可替代用途。

### 28. ICLR2024-1607

**Canonical title:** MOTOR: A Time-to-Event Foundation Model For Structured Medical Records
**Venue/year:** ICLR 2024
**阅读要求:** abstract-only (conditional)

- 选择理由：inactive明显event语义负例，校准快速排除，不浪费全库PDF预算。
- 测试边界：EHR time-to-event与event-camera。
- 完整摘要中的选择线索（转述，非最终判定）：完整摘要明确electronic health records、insurance claims和医学time-to-event预测。
- PDF具体问题：默认无需PDF；若出现metadata错配才查首页/输入定义，不因event词自动展开方法。

### 29. ICLR2026-1286

**Canonical title:** Time Is All It Takes: Spike-Retiming Attacks on Event-Driven Spiking Neural Networks
**Venue/year:** ICLR 2026
**阅读要求:** PDF-required

- 选择理由：不在旧Core的timing攻击，摘要涉及binary/integer event grids；挑战新边界。
- 测试边界：input-grid retiming vs physical-event timestamps vs neuronal spikes；event-specific vsbenchmark_only。
- 完整摘要中的选择线索（转述，非最终判定）：摘要明确保持counts/amplitudes的retiming、capacity-1约束，DVS等基准和binary/integer grids。
- PDF具体问题：时间偏移发生在物理event流、grid bin还是network spike time？哪些约束来自camera接口、哪些是generic SNN？能否与raw-event attack放同一cross-cutting类？

### 30. CVPR2025-1775

**Canonical title:** On-Device Self-Supervised Learning of Low-Latency Monocular Depth from Only Events
**Venue/year:** CVPR 2025
**阅读要求:** PDF-required

- 选择理由：depth/on-device online learning候选，摘要未说SNN，避免把低功耗sensor与算法混同。
- 测试边界：hardware claim与真实SNN存在；generic online learning与local plasticity；depth任务覆盖。
- 完整摘要中的选择线索（转述，非最终判定）：摘要明确contrast maximization、on-device drone depth learning和self-supervision，未定义spiking计算。
- PDF具体问题：模型是否含spiking neuron？on-board是何设备，训练/推理时延和memory实测范围是什么？能否作为on-device非SNN comparator，还是无独立用途？

## 3. Coverage matrix：覆盖检查对象，不预判结果

| 要覆盖的边界 | Pilot编号 | 验证目的/限制 |
| --- | --- | --- |
| raw-event / direct-input SNN 候选 | 01、05、06、13 | raw点/逐事件不能当address-event injection已确认；让Sol找到真实接口 |
| dense frame / voxel SNN | 02、03、10 | representation与SNN输入发放分开 |
| point/Event Cloud | 01、20 | SNN与非SNN配对，保留timestamp不等于物理时钟 |
| graph event processing | 19；负对照27 | 19是event graph待核非SNN，27是非camera graph SNN；不宣称覆盖真event-graph SNN家族 |
| SNN preprocessing/interface controller | 03、04、05 | 输出事件选择/切片与latent feature区别 |
| main task backbone | 01、10、12 | head、preprocess不自动随backbone变spiking |
| hybrid ANN-SNN | 06、07、08、09、21 | hybrid boundary与embedded role独立 |
| converted SNN | 17；映射对照12 | 17提供一般conversion规则测试；未证明event-specific converted pipeline覆盖充分 |
| optimization/inference engine | 02、13 | 算法对应、主要贡献与secondary task role |
| neuron/training contribution | 03、14、16、22 | 不能给每种neuron/训练法建顶层role |
| event-camera-only foundation | 19、20、23、24、25、30 | 是否有具体cross-axis比较用途；不能全部自动保留 |
| SNN-only strong foundation / DVS generic | 16、17、18、22 | 一般neuron/benchmark与真正integration分开；摘要不够就unknown |
| misleading spike/event language | 23、24、11、26、27、28 | 异步、膜电位、spike camera、图SNN与EHR |
| fully spiking claim / ambiguous boundary | 04、07、10、11、12、21、22 | map逐模块核查，允许作者claim与证据不一致 |
| RGB/frame-event multimodal | 09、10 | RGBteacher/train、test输入和多表示不能混同 |
| recognition / detection / tracking | 01、14、25 / 03、04、07、08 / 05、10、11、12 | task是证据组织轴，不是role |
| reconstruction/restoration | 02、09、21、24 | latent representation、hybrid decoder、continuous output |
| pose / depth / flow / segmentation | 20、24 / 30 / 19 / 13 | 这些任务有foundation对照；不把它们冒充所有任务的真实SNN交叉覆盖 |
| efficiency / hardware | 01、08、11、17、18、19、30 | proxy、runtime、memory、chip局部/全系统及projection分开 |
| weak / conflicting abstract evidence | 06、07、22、24、29 | 冲突进入问题队列；尤其24旧PDF结论须重新定位 |
| training-only / security without new topology | 14、15、29 | primary not_applicable是否可复现，是否必须独立cross-cutting章节 |

**明确的pilot覆盖限制：** 真event-graph SNN、event-specific ANN-to-SNN conversion、经典event-SNN optical flow/depth/pose、sensor-chip co-design尚不能由这个当前仓库样本完全验证。不得拿“graph事件ANN + generic graph SNN”的组合宣称已覆盖两者交叉。Astra若认为这些是冻结的必要条件，应在pilot后指定小型补充校准；后续检索优先从参考综述及Core引用回溯，不在本轮新增论文或补标签。

## 4. 交付与成功标准

Sol High执行阶段的产物（路径由用户确认后的任务明确指定）应包含：30篇paper/variant结构化记录；每字段直接证据/置信度；PDF问题与答案；abstract→PDF修订记录；issue queue；coverage和validator报告；每篇阅读时间和触发原因。不可把paper/variant多行算成超过30篇；不可生成或改V2、旧audit、旧Core、旧Advisor任何文件。

建议盲重标的10个边界case：03、04、06、07、12、13、14、22、24、29。先隐藏第一次标签/旧role并打乱顺序；第二次从同一原始证据重新判定scope、directness、primary、extent，再比较。不能只复制第一遍label后声称一致。

成功标准：

1. 30/30身份、完整title/abstract、hash可追溯；零非法标签、零空的必要理由；所有evidence ID和字段引用一致。
2. PDF-required的决定性问题全部取得直接答案或清楚标为unavailable/not reported，不能默认为解决。影响scope/primary/边界的unknown需Astra裁决或限制使用；不要求消灭诚实的unknown。
3. 10篇盲重标，scope、primary、extent分别至少9/10一致；同时报告directness的一致性。少数rare label样本不适合用单一kappa掩盖；先看具体confusion pairs。重复出现同一interface/module或engine/backbone混淆即需要修规则，即使总率达标。
4. 每个实质新role都有明确输入/输出合同；所有multi-role样本能解释为何primary而不是相邻值，或被正式保留为role_conflict。若无法操作性区分，允许合并/替换四role假设。
5. 不出现dataset→role、genericDVS→core、event→neuronalspike、stateful→SNN、conversion→hybrid、SOP→measurement、T→ms的无证据跳步。
6. 3个abstract-only负例只用于已被摘要解决的scope/use边界；不得偷偷填其neuron/训练/硬件细节。若最终作为背景保留，重新触发PDF。
7. Pilot结果不作为150–180篇的数量预测；不把未覆盖家族当不存在。任何需要增删label的case由Astra统一裁决，Sol只准备证据。

如果未达标：保留失败case、问题和证据，交Astra发布v0.2规则与针对性复查清单，先重跑受影响pilot；不要转入572篇全量。

## 5. Pilot后Astra必须回答的问题

- 以论文主要机制贡献选primary能否复现，还是应换成系统主路径，并把贡献放secondary？两种规则对03/04/02结果有什么影响？
- event_interface与early embedded feature extractor是否仍有本质不可区分的交界？若有，应合并还是增加交接证据要求？
- task_network在混合多阶段backbone的定义是否稳定；head/decoder与主特征提取的边界是否可描述？
- algorithmic_engine有真正共同的计算机制，还是仅为不同方法的算法解释标签，适合降为secondary吗？
- EventRPG和两种攻击：作为core_intersection但不在inference role主图是否足以组织综述？需独立training/evaluation证据小节吗？
- CLIF/STEP/ABN怎样稳定区分一般SNN机制、benchmark-only和event-specific integration？何种直接证据足够升级？
- integer训练/spike推理、局部chip实测、continuous readout的定义是否能避免误用fullyspiking？
- raw-event/point/graph/token/voxel的交接位置与三个时间轴能否逐篇复现？哪个字段重复、应合并、或仍遗漏？
- 59字段的阅读成本是否适合clear-case批量，哪些应按scope条件not_applicable，哪些必须升级High？
- 现有样本对graph-SNN、event-specific conversion及经典稠密任务是否不足以冻结字典；是否必须先补校准？

**本计划不授权执行。下一步应由用户确认codebook，再交Sol High执行pilot；pilot之后由Astra修订并决定是否冻结v1.0。**
