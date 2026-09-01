---
tags: [event-camera, event-graph, GNN, optical-flow, asynchronous-computing, low-latency, survey-core]
---

# Summary V2｜Graph Neural Network Combining Event Stream and Periodic Aggregation for Low-Latency Event-based Vision

## 1. Core Understanding

本文研究 event-based optical flow 的 accuracy-latency-computation trade-off。frame-based CNN 需要先在时间窗口内把 event stream 累积为 frame，能够使用 pooling、normalization 和较大时空上下文，但会产生毫秒级等待；完全 asynchronous event graph 可以逐 event 计算，却不能等待未来 events，也难以使用依赖全局统计或时间累积的操作，准确率因此受限。

作者提出 HUGNet2+PA：HUGNet2 是 accumulation-free、past-to-future directed 的 asynchronous event-graph branch，事件到达时触发 graph building、GNN 和 Event head，输出该事件位置的 optical flow；Periodic Aggregator（PA）在后台周期性聚合过去的 GNN features，补充 global spatio-temporal context，再由 Periodic head 输出 dense optical flow。两条 branch 并行，PA 不阻塞 Event branch，因此历史上下文可以提高 Event prediction，而不增加逐 event 的计算等待。

这是一种 non-spiking GNN architecture，不是 SNN。它只使用 event data，不使用 RGB image；GPU training 时 graph 可以预先构建并并行处理，异步硬件 deployment 才按 event arrival 在线构图和执行。作者报告在特定硬件估计下的 event latency 约 $50\,\mu\mathrm{s}$、相对 frame-based 方法约三个数量级降低，且 operations per second 最多降低 $48\times$；这些效率结论必须区分 operation estimate、hardware-informed latency estimate 和真实 energy measurement。

## 2. Problem and Motivation

光流是场景中物体或观察者运动造成的 apparent relative displacement。RGB camera 通过连续 frame 的像素位移估计光流，但 frame rate 和 CNN inference 共同造成 blind time；提高 frame rate 又会增加计算量和带宽。

Event camera 以异步方式在光强变化时产生 $e=(x,y,t,p)$，具有微秒级 temporal resolution。若把 events 转成 frames，CNN 可以使用强大的 spatial processing，但会丢失 event sparsity 和 event-level latency。Event graph 将 event 作为 node，并以时空邻近关系建立 edges；新 event 到达时可触发 graph convolution，并直接产生 node-level optical flow。

低延迟约束要求当前 event 的所有邻域信息已经存在，不能等待未来 event。本文因此采用 past-to-future directed graph，并以周期分支补足没有 pooling 和 global statistics 带来的 context 缺失。核心设计不是让 PA 参与当前 event 的同步计算，而是让 PA 只处理历史 data，Event branch 继续使用最新 event 输出。

## 3. Method Overview

每个 event 为：

$$
e=(x,y,t,p),
$$

其中 $(x,y)$ 是 pixel coordinate，$t$ 是 emission timestamp，$p$ 是 positive/negative polarity。event graph 为：

$$
G=(V,E),
$$

其中 event 是 vertices，spatio-temporal proximity 决定 edges，vertices 和 edges 可带 features。

### Event branch

HUGNet2 将 kNN search 限制在当前 event 周围的 past-only hemisphere：空间范围为 $(-r_{xy},+r_{xy})$，时间范围为 $(-r_t,0)$。因此新 event 只连接已经到达并保存在 memory 中的过去 events，图结构在当前时刻即可确定。Event branch 的计算流为：

$$
e_t
\rightarrow
\text{past-only graph update}
\rightarrow
\text{HUGNet2 GNN}
\rightarrow
\text{merge with PA}(T-2)
\rightarrow
\text{Event head}
\rightarrow
\hat{\mathbf v}_t.
$$

Event head 对每个 event 输出二维 optical-flow vector；它不等待当前周期 PA 完成。

### Periodic branch

PA 在一个 aggregation period 内累积 GNN output features，对 accumulated event features 做 spatial-temporal pooling，再用 convolutional 和 recurrent layers 聚合 global context。PA 输出经 bilinear upsampling 回到原始 pixel resolution，送入 Periodic head，得到每个 pixel 的 dense optical flow：

$$
\text{GNN features over a period}
\rightarrow
\text{feature pooling}
\rightarrow
\text{PA convolution/recurrent aggregation}
\rightarrow
\text{bilinear upsampling}
\rightarrow
\text{Periodic head}.
$$

PA 只能处理过去数据，且在周期结束后才启动，计算还可能持续另一个周期。因此在当前 period $T$ 中可用的历史输出是 PA$(T-2)$。Event branch 融合当前 event 的 GNN feature 与该 event pixel location 的 PA$(T-2)$ feature。这样 PA 提供 delayed global context，GNN 提供 recent event-level evidence。

## 4. Key Components and Mechanisms

### HUGNet2：因果 event graph

原始 HUGNet 使用 instance normalization 的 on-the-fly statistics 和 3D neighborhood normal vectors。前者需要先处理完整 graph/sequence 才能计算，后者可能依赖 future events，都会破坏 event-level low latency。HUGNet2 删除 normalization 和 normal vectors，并将第一层 SplineConv 替换为 PointTransformerConv，以略微提升 accuracy、减少 parameters；之后使用四个 GCNConv layers。GCNConv 只对邻居的 projected features 做 mean aggregation，成本低于 PointTransformerConv，因此较昂贵的 PointTransformerConv 仅放在第一层。

HUGNet2 不是简单地“没有状态”：它仍然保存过去 events 和对应 graph features；“accumulation-free”指 Event branch 不等待 future data，也不使用必须依赖整段序列统计的 pooling/normalization。Periodic branch 可以对已经结束的过去 period 做累积，但这条计算不阻塞当前 Event branch。

### Periodic Aggregator 与融合

PA 在降低空间分辨率的 pixel grid 上对 GNN 的 64-dimensional features 做 feature-wise max pooling，再通过：

$$
\text{Conv}_{3\times3,\,\mathrm{stride}=2,\,64}
\rightarrow
\text{SepConvGRU}_{64}
\rightarrow
\text{Conv}_{3\times3,\,128}
$$

进行时空聚合。SepConvGRU 使用 $1\times5$ recurrent convolutions，先 horizontal、再 vertical。输出 bilinear upsample 到原始 resolution，并由 Periodic head 映射为 2-channel flow。

Event branch 的 merge 是：

$$
F_{\mathrm{merge}}(e_t)=
\operatorname{Concat}\left(
F_{\mathrm{GNN}}(e_t),
F_{\mathrm{PA}(T-2)}(x_t,y_t)
\right),
$$

即 $64+128=192$ 个 features。Event head 为 $192\rightarrow128\rightarrow64\rightarrow2$ fully connected layers；Periodic head 为 $128\rightarrow2$ fully connected layers。两者都是 ANN/GNN feature computation，不包含 spike、membrane potential 或 SNN neuron dynamics。

### PA rate

若 PA rate 为 $f_{\mathrm{PA}}$，PA 每秒运行 $f_{\mathrm{PA}}$ 次，周期为：

$$
\Delta t_{\mathrm{PA}}=\frac{1}{f_{\mathrm{PA}}}.
$$

PA20 的周期约为 $50\,\mathrm{ms}$，PA100 的周期约为 $10\,\mathrm{ms}$。由于融合使用 PA$(T-2)$，历史 context 的时间滞后近似为：

$$
D_{\mathrm{PA}}\approx\frac{2}{f_{\mathrm{PA}}}.
$$

提高 PA rate 会更频繁地更新 global context、减少 PA stale features 的影响，但也增加 Periodic branch 的计算。若一次 PA 运行需 $C_{\mathrm{PA}}$ operations，则：

$$
\mathrm{OPS}_{\mathrm{PA}}=C_{\mathrm{PA}}f_{\mathrm{PA}}.
$$

PA rate 太低时，历史 context 更旧，快速运动时 Event head 需要更多依赖当前 GNN features；PA rate 太高时，准确率可能饱和而 operations 持续增加。最佳 rate 依赖 motion-change speed、ground-truth rate、event density 和 application budget。

## 5. Experiments and Main Evidence

### Setup

MVSEC 包含 indoor flying 和 outdoor driving scenes，resolution 为 $346\times260$，ground truth optical flow 为 20 Hz。训练使用 outdoor day2，测试使用 outdoor day1 和 indoor flying sequences 1--3；这些场景运动较慢且平滑。

Rock Scenes 是评估快速运动变化的 synthetic dataset：moving cover-art images 与 textured background 进行不相关运动，方向和速度会突然变化；ground truth 为 500 Hz、$100\times100$ resolution，变化发生在一个 $2\,\mathrm{ms}$ timestep 内。训练集 100 sequences，测试集 4 sequences，测试组合包含 unseen objects/scenes。

图先在完整 sequence 上构建，再切分为 Rock Scenes 的 $400\,\mathrm{ms}$、overlap $200\,\mathrm{ms}$ segments，以及 MVSEC 的 $800\,\mathrm{ms}$、overlap $200\,\mathrm{ms}$ segments。数据先经过 spatio-temporal contrast filter；MVSEC outdoor 还下采样 $3\times$ 以接近 indoor event density。

Graph parameters 为 MVSEC 的 $r_{xy}=8$ pixels、$r_t=80\,\mathrm{ms}$，Rock Scenes 的 $r_{xy}=9$ pixels、$r_t=90\,\mathrm{ms}$，$k=32$ neighbors。Node features 使用 pixel coordinates 和 polarity，不使用 absolute timestamp，以避免时间绝对值影响 flow 或造成 overfitting。

训练使用 AdamW、batch size 1、初始 learning rate $5\times10^{-4}$；若 10 epochs 内 loss 没有 $0.05$ relative change，learning rate 减半。Event 和 Periodic predictions 都使用 supervised smooth-L1 loss。增强包括 horizontal/vertical flips、$0.5$--$1.5$ temporal stretching、$0$--$360^\circ$ rotations 和 probability $0.25$ 的 edge dropout；MVSEC 额外使用 $256\times256$ random crop。Instance normalization 只 warm up 100 epochs，随后移除并 fine-tune 100 epochs。GPU 训练使用 NVIDIA A100 40 GB。

### Metrics and efficiency evidence

Endpoint Error（EPE）为 predicted flow 与 ground truth flow 的 $L_2$ distance：

$$
\mathrm{EPE}=\left\|\hat{\mathbf v}-\mathbf v_{\mathrm{gt}}\right\|_2.
$$

论文使用 Sparse EPE，即只在至少发生一个 event 的 pixel 上计算。Event prediction 选择每个 ground-truth voxel 中的 last event；Periodic prediction 则通过 temporal upsampling/downsampling 与 ground-truth rate 对齐。表 1/2 报告的是 low-latency Event prediction 的 EPE，不是 Periodic prediction 的 EPE。

Frame-based 方法的每秒操作数为 operations per frame 乘 frame rate：

$$
\mathrm{OPS}_{\mathrm{frame}}=C_{\mathrm{frame}}f_{\mathrm{frame}}.
$$

Event graph 方法的 operations per event 固定，但 event rate 会变，因此用 average event density 估计：

$$
\mathrm{OPS}_{\mathrm{event}}=C_{\mathrm{event}}\rho_e.
$$

本文总操作量由两项组成：

$$
\mathrm{OPS}_{\mathrm{total}}=C_E\rho_e+C_Pf_P,
$$

分别对应 Event branch 和 Periodic branch。约 $50\,\mu\mathrm{s}$ 的 latency 是基于已有 FPGA event-graph implementation 的 $16\,\mu\mathrm{s}$ per-event result，以及本文约 $3\times$ per-event GNN operations 的比例估计，不是完整本文硬件端到端 wall-clock measurement。约 $48\times$ 是 operations-per-second evidence，不等于 $48\times$ measured energy reduction。

### Results

HUGNet2 的 accuracy 低于 HUGNet，但 parameters 和 operations 更少，latency 降低四个数量级；HUGNet2+PA 在适度增加 operations 的情况下超过 HUGNet2 和 HUGNet。MVSEC 上 PA20、Rock Scenes 上 PA100 得到最高 accuracy；提高 PA rate 超过数据集相关饱和点后不再改善 accuracy。

MVSEC 上本文 accuracy 低于 frame-based state of the art，但相对 ADMFlow 报告 $48\times$ fewer operations per second、$17\times$ fewer parameters，并把 latency 从 tens of milliseconds 的量级推进到 tens of microseconds 的 hardware-informed estimate。Rock Scenes 没有现成 SOTA CNN baseline，作者用 open-source ADMFlow 在该数据集重新训练；本文方法在该比较中 accuracy 更高且更 efficient。

在 Event 与 Periodic$(T-2)$ 的对比中，Event prediction error 最多降低 $59\%$。Rock Scenes 上 PA20 Event prediction 达到 PA100 Periodic$(T-2)$ 的 accuracy，同时 operations 减少 $56\%$；MVSEC 上 PA5 Event prediction 达到 PA20 Periodic$(T-2)$ 的 accuracy，同时 operations 减少 $29\%$。PA rate 越低，两个周期造成的历史滞后越大，Event head 利用 current GNN features 的优势越明显。

Rock Scenes 的突变实验显示 Periodic$(T-2)$ 至少滞后 1--2 frames；PA20 时约为 $50$--$100\,\mathrm{ms}$，有时更久。Event error 也会在突变时上升，但下降更快；它仍需要积累足够新 events 才能精确估计新的 flow。Event prediction 平均优于 ADMFlow$(T)$ 和 ADMFlow$(T-2)$，但这涉及不同可用信息时间与 recurrent history，不能只解读为模型结构绝对优越。

## 6. Strengths and Limitations

**Strengths。** 本文把 past-only event graph、event-level prediction 和 periodic global aggregation 放在同一架构中，清楚分离 low-latency local response 与 delayed global context；HUGNet2 删除会引入未来依赖的 normalization/normal vectors，PA rate、Event/Periodic output 和突变响应实验直接检验 accuracy-latency trade-off；MVSEC 与 Rock Scenes 同时覆盖平滑和突变运动。

**Limitations。** HUGNet2 不使用 event pooling，所有 GNN layers 的操作仍受原始 event density 影响，power-constrained scalability 有边界；$50\,\mu\mathrm{s}$ 是基于既有 FPGA 结果的估计，不是本文完整硬件的实测端到端 latency；operations count 不等于真实 energy；Event branch 与 Periodic branch 的信息可用时间不同，ADMFlow 对比存在时间对齐和输入历史长度差异；模型只使用 event data，不能直接说明 frame-event multimodal fusion；它是 non-spiking GNN，不提供 SNN membrane/spike coupling 证据。

## 7. Relation to Other Papers and Survey Taxonomy

本文在 Survey 中属于 **event representation and aggregation、asynchronous event graph、event-level dense prediction、non-spiking event-camera comparator、low-latency/efficiency evaluation**。它不是 fully spiking、hybrid SNN-ANN 或 ANN-SNN conversion 方法。其主要贡献是 event graph interface 和两级时间聚合：past-only graph 保证即时预测，Periodic Aggregator 补充更大上下文。

### PDF-verified literature relations

- **HUGNet: Hemi-spherical Update Graph Neural Network Applied to Low-latency Event-based Optical Flow (Thomas Dalgaty et al., CVPR Workshops 2023)** — `extends`。本文明确将 HUGNet2 定义为 HUGNet 的改进版本：继承 past-to-future hemi-spherical event graph，删除依赖整段 graph 或 future events 的 normalization 与 normal vectors，并用 PointTransformerConv 替换首层 SplineConv；Tables 1--2 还直接比较 HUGNet、HUGNet2 和 HUGNet2+PA。证据：Introduction、Related Work 2、Method 3.1.1 和 Tables 1--2，PDF pp.2--3、6，citation [6]；bibliography，PDF p.9。
- **Learning Optical Flow from Event Camera with Rendered Dataset (Xinglong Luo et al., ICCV 2023)** — `baseline`。ADMFlow 是本文 frame-based optical-flow comparator：Related Work 将其描述为用 learnable adaptive density module 补偿 event frames 的异质 event density；Table 1 在 MVSEC 比较 accuracy、parameters、OPS/s 和 latency，Table 2 使用 open-source code 在 Rock Scenes 重新训练 ADMFlow。证据：Related Work 2、Experiments 4.1--4.2 和 Tables 1--2，PDF pp.2、6--7，citation [20]；bibliography，PDF p.9。
- **EVGNN: An Event-driven Graph Neural Network Accelerator for Edge Vision (Yufeng Yang et al., arXiv 2024)** — `foundation`。本文的 asynchronous-hardware latency estimate 直接建立在 EVGNN 的 FPGA event-graph building/processing result 上：EVGNN 报告 $16\,\mu\mathrm{s}$ per event，本文根据约 $3\times$ per-event GNN operations 比例估计约 $50\,\mu\mathrm{s}$。该关系支持硬件估算方法，不代表本文完成了自身端到端硬件实测。证据：Introduction、Method 3.3，PDF pp.2、5，citation [34]；bibliography，PDF p.10。

## 8. Survey-Usable Takeaways

本文提供一个非 SNN 的 event-side comparator：event-by-event graph computation 可以保留事件稀疏性和微秒级响应，Periodic Aggregator 则以不阻塞 Event branch 的方式补充 global context。它说明 event accumulation 不是只有“全部等待成 frame”或“完全禁止累积”两种选择，也可以把异步即时路径和后台历史聚合并行组织。

对 Survey 的关键区分是：Event graph 的 past-to-future causality、GNN feature state 和 PA period，不等同于 SNN 的 spike、membrane potential 和 timestep recurrence。本文的 $48\times$ operations、$50\,\mu\mathrm{s}$ latency 和三个数量级改善，应分别标记为 operation-count、hardware-informed estimate 和 paper-reported comparison，不能直接写成实测 energy 或普遍硬件优势。

## Supplement Points

### Questions and Clarifications

#### 1. 本文为什么有多种 based 方法？Event、Periodic、frame-based 和 event-graph-based 分别如何评估？

用户询问：本文不是只有一种方法吗，为什么评估指标部分出现很多种不同的 based，它们分别如何计算？

本文确实只提出一套完整架构 HUGNet2+PA，但这套架构内部同时产生 Event prediction 和 Periodic prediction；实验还要与 frame-based、纯 event-graph-based 等计算范式比较。因此，多种 “based” 不是多套相互矛盾的模型或指标，而是在区分输出接口、计算触发方式和 baseline category。

本文的完整输出结构为：

$$
\text{Event stream}
\rightarrow
\text{HUGNet2 GNN features}
\rightarrow
\begin{cases}
\text{Event head: per-event output},\\
\text{PA + Periodic head: periodic dense output}.
\end{cases}
$$

Event head 在每个新 event 到达时，预测该 event location 的二维 optical flow；Periodic head 每隔一个 PA period 输出覆盖整个 pixel grid 的 dense optical flow。两者共享 GNN event features，但 aggregation 和 output rate 不同。

对一个位置，predicted optical flow 和 ground truth 分别为：

$$
\hat{\mathbf v}=(\hat v_x,\hat v_y),
\qquad
\mathbf v=(v_x,v_y).
$$

Endpoint Error（EPE）是两个二维向量端点之间的 Euclidean distance：

$$
\mathrm{EPE}
=
\left\|\hat{\mathbf v}-\mathbf v\right\|_2
=
\sqrt{(\hat v_x-v_x)^2+(\hat v_y-v_y)^2}.
$$

例如 ground truth 为 $(3,4)$、prediction 为 $(2,6)$，则 EPE 为 $\sqrt{5}$。EPE 越小，说明预测越接近 ground truth；数据集结果通常对所有 evaluation locations 和 times 取平均。

本文使用 Sparse Endpoint Error。“Sparse”不是说 Periodic prediction 必须是 sparse，而是只在至少发生一个 event 的 pixel locations 上计算。若该时段有 event 的 pixels 构成集合 $\Omega_e$，则：

$$
\mathrm{SparseEPE}
=
\frac{1}{|\Omega_e|}
\sum_{(x,y)\in\Omega_e}
\left\|
\hat{\mathbf v}(x,y)-\mathbf v_{\mathrm{gt}}(x,y)
\right\|_2.
$$

没有 event 的 pixels 不参与计算，因为 Event head 只在 event arrival locations 产生 output；要求它在完全没有 event 的位置输出 flow 对 per-event method 不公平。

Event prediction 和 Periodic prediction 的 output form 不同，因此计算 Sparse EPE 前需要分别与 ground truth 对齐。一个 ground-truth temporal voxel 内，同一 pixel 可能产生多个 events，Event head 也会产生多个 predictions。论文选择该 voxel 内的 last event prediction：

$$
\hat{\mathbf v}^{E}(x,y,\tau)
=
\hat{\mathbf v}\left(e_{\mathrm{last}}(x,y,\tau)\right),
$$

其中 $\tau$ 是 ground-truth interval。last event 最接近该 interval 的时间边界，也包含该 interval 内最新的信息；如果选择较早 event，会混入额外 temporal misalignment。

Periodic prediction 每隔一个 period 输出完整 flow map：

$$
\hat{\mathbf V}^{P}_{q}\in\mathbb{R}^{H\times W\times2},
$$

其中 $q$ 是 period index。PA output rate 可能不同于 ground-truth rate，因此需要在 temporal dimension 上 upsample 或 downsample，把 prediction timestamps 与 ground truth 对齐。对齐后，虽然 Periodic output 是 dense 的，论文仍然只在 $\Omega_e$ 上计算 Sparse EPE，保证 Event 和 Periodic outputs 使用同一 spatial evaluation support。

因此，同一 HUGNet2+PA 可以得到 $\mathrm{EPE}_{\mathrm{event}}$ 和 $\mathrm{EPE}_{\mathrm{periodic}}$。前者衡量最新 event 带来的低延迟响应，后者衡量周期聚合和 global context 带来的稳定预测。论文 Tables 1--2 报告的是 low-latency Event prediction 的 EPE，而不是 Periodic prediction 的 EPE。

frame-based、event-graph-based 和 proposed hybrid architecture 主要出现在 computation 与 latency comparison。Frame-based 方法先在时间窗口内将 events 累积成 frame，再每 frame 运行一次 CNN。若每 frame 需要 $C_{\mathrm{frame}}$ operations，frame rate 为 $f_{\mathrm{frame}}$，则：

$$
\mathrm{OPS}_{\mathrm{frame}}=C_{\mathrm{frame}}f_{\mathrm{frame}}.
$$

它的 computation period 固定；即使某个时段 events 很少，只要仍形成 frame，dense CNN 通常仍执行完整 forward pass。

纯 event-graph-based 方法在每个 event 到达时运行固定 graph update 和 node computation。若平均每 event 需要 $C_{\mathrm{event}}$ operations，average event rate 为 $\rho_e$，则：

$$
\mathrm{OPS}_{\mathrm{event}}=C_{\mathrm{event}}\rho_e.
$$

event rate 随场景变化，运动越剧烈、纹理越复杂通常 events 越多，所以不能只报告 operations per event，还要乘 average event density。

HUGNet2+PA 同时包含 event-triggered 和 periodic computation：

$$
\mathrm{OPS}_{\mathrm{total}}
=
C_E\rho_e+C_Pf_P.
$$

第一项是 Event branch，随 event density 变化；第二项是 Periodic branch，随 PA rate 变化。论文的 “up to $48\times$ fewer operations per second” 比较的是这种 OPS/s，而不是单个 Event head forward 固定少 $48\times$，也不是直接测得 energy 少 $48\times$。

latency 与 operation count 也不同。Frame-based latency 包含 event/frame accumulation 和 inference：

$$
D_{\mathrm{frame}}
=
D_{\mathrm{accumulation}}+D_{\mathrm{inference}}.
$$

即使 CNN 很快，也必须等待 frame formed。Event branch 不等待完整窗口，理想 latency 为 graph building、GNN 和 Event head 的总和：

$$
D_{\mathrm{event}}
=
D_{\mathrm{graph}}+D_{\mathrm{GNN}}+D_{\mathrm{head}}.
$$

作者没有在本文完整 asynchronous hardware 上直接测得该值，而是参考已有 FPGA implementation 的约 $16\,\mu\mathrm{s}$ per event，并按本文约 $3\times$ per-event GNN operations 比例估计：

$$
D_{\mathrm{event}}\approx50\,\mu\mathrm{s}.
$$

所以 $50\,\mu\mathrm{s}$ 是 hardware-informed estimate，不是本文完整 pipeline 的直接 wall-clock measurement。

Periodic prediction 必须等待 period 结束并等待 PA computation，因此约落后两个 periods。它通常更稳定、context 更广，但突然改变 direction 或 speed 时会 stale。本文的 evaluation 因而同时衡量三件事：Sparse EPE 衡量 flow accuracy，OPS/s 衡量给定 event/output rate 下的 computation，latency 衡量新信息出现后多久可产生 prediction。多种 “based” 描述的是 input organization 与 compute trigger，不是多种不同的 EPE 定义。

#### 2. PA rate 是什么？如何影响计算流程和结果？

用户询问本文中的 PA rate 是什么，以及它如何影响计算流程和实验结果。

PA rate 是 Periodic Aggregator 的运行频率，即 Periodic branch 每秒启动多少次聚合和预测。若 PA rate 为 $f_{\mathrm{PA}}$，两个周期之间的时间间隔为：

$$
\Delta t_{\mathrm{PA}}=\frac{1}{f_{\mathrm{PA}}}.
$$

PA20 表示每秒运行 20 次，周期约为 $50\,\mathrm{ms}$；PA100 表示每秒运行 100 次，周期约为 $10\,\mathrm{ms}$；PA5 表示每秒运行 5 次，周期约为 $200\,\mathrm{ms}$。

PA rate 不是 Event branch 的事件处理速率。Event branch 仍由 event arrival 触发，每来一个 event，就通过 HUGNet2 计算该 event 的 GNN feature，并由 Event head 产生逐事件预测。PA rate 只控制另一条 Periodic branch 多久对过去的 event features 进行一次聚合。

本文完整数据流可抽象为：

$$
\text{Event stream}
\rightarrow
\text{HUGNet2 GNN features}
\rightarrow
\begin{cases}
\text{Event branch: event arrival 时计算},\\
\text{Periodic branch: 每隔 }\Delta t_{\mathrm{PA}}\text{ 聚合一次}.
\end{cases}
$$

在一个 PA period 内，PA 收集这段时间中 GNN 产生的 event features，执行 feature pooling、convolution 和 SepConvGRU 时空聚合，再输出 dense optical-flow map。因此 PA rate 越高，每次聚合覆盖的时间窗口越短；PA rate 越低，每次聚合覆盖的时间窗口越长。

PA rate 首先影响 PA context 的新鲜程度。本文中 PA output 有两个 period 的 delay，当前 period $T$ 的 Event branch 不能等待当前 PA 完成，而使用已经可用的 PA$(T-2)$：

$$
D_{\mathrm{PA}}\approx\frac{2}{f_{\mathrm{PA}}}.
$$

PA20 的两个 period 约为 $100\,\mathrm{ms}$，PA100 的两个 period 约为 $20\,\mathrm{ms}$。PA rate 越低，PA$(T-2)$ 越 stale；如果 scene optical flow 快速变化，历史 PA feature 可能仍描述运动变化之前的状态。PA rate 越高，PA context 更新更频繁，Periodic prediction 通常更准确。

但 PA rate 越高并不意味着 accuracy 无限增加。提高 PA rate 同时带来两种影响：global context 更新更快，但 Periodic branch 每秒运行次数增加。若一次 PA 运行需要 $C_{\mathrm{PA}}$ operations，则：

$$
\mathrm{OPS}_{\mathrm{PA}}=C_{\mathrm{PA}}f_{\mathrm{PA}}.
$$

因此 PA20 到 PA100 在单次计算量相同的假设下，会使 Periodic branch 的 operations per second 大约增加 5 倍。准确率可能先提升，达到数据集相关饱和点后不再明显提升，而计算成本仍然增加。

PA rate 还影响每次聚合能看到的历史信息。低 PA rate 的单次 period 更长，能够积累更长时间的 context，但更新慢、滞后大；高 PA rate 的单次 period 更短，更新及时，但单次聚合包含的历史 events 更少，并且需要更频繁运行 PA。因此 PA rate 是 context freshness、temporal receptive field 和 periodic computation cost 之间的折中。

Event branch 可以部分缓解低 PA rate 的问题。Event head 融合当前 event 的 GNN feature 和历史 PA feature：

$$
F_{\mathrm{merge}}(e)
=
\operatorname{Concat}
\left(
F_{\mathrm{GNN}}(e),
F_{\mathrm{PA}(T-2)}(x_e,y_e)
\right).
$$

其中 $F_{\mathrm{GNN}}(e)$ 来自当前 event，$F_{\mathrm{PA}(T-2)}(x_e,y_e)$ 来自较早 period，并取该 event pixel location 的 PA feature。Event head 可以用 GNN 的最新 local information 修正过时的 PA context。

这解释了论文中的结果：Rock Scenes 上 PA20 的 Event prediction 可以接近 PA100 的 Periodic$(T-2)$ accuracy，同时 Periodic branch 的运行频率降低，operations 减少 56%；MVSEC 上 PA5 的 Event prediction 可以接近 PA20 的 Periodic$(T-2)$ accuracy，operations 减少 29%。PA rate 越低，历史 PA 与当前运动越可能不一致，Event head 利用 recent GNN features 的优势越明显。

但 Event prediction 也不是完全不受 PA rate 影响。PA rate 越低，PA$(T-2)$ 越旧，Event head 需要更多依赖当前 GNN；如果新 event 数量不足，GNN 也可能没有足够证据识别新的速度和方向。因此降低 PA rate 后，Event branch 仍需要积累一定的新 events 才能完成 motion correction。

还必须区分 PA rate、单事件计算 latency 和运动变化可靠识别时间：

$$
\text{PA rate}
\neq
\text{Event branch latency}
\neq
\text{motion-change recognition time}.
$$

PA rate 控制 Periodic context 的更新频率和计算成本；Event branch 的单事件 latency 是论文基于硬件实现估计的约 $50\,\mu\mathrm{s}$；而识别一个新的 optical-flow direction 通常需要足够多的新 events。本文方法的价值是无需把 PA rate 提高到极高，也可以依靠 Event branch 对快速 motion change 做及时响应。
