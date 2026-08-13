---
tags: ["SNN", "event camera", "object detection", "SFOD", "Spiking DenseNet", "feature fusion", "spiking decoding", "GEN1", "NCAR"]
---

# Summary V2｜SFOD: Spiking Fusion Object Detector

## 1. Core Understanding

SFOD 是一种面向 event-camera object detection 的 SNN-based detector。它沿用 voxel cube、Spiking DenseNet 和 SSD 检测框架，核心改进是在 backbone 与检测头之间加入 Spiking Fusion Module，对多层 spiking feature maps 进行对齐、拼接并重新生成 feature pyramid，同时研究 spiking decoding 与 loss function 的匹配关系。

该方法的 backbone 和 feature fusion 部分使用 PLIF neurons，但多尺度特征在进入 SSD head 前会被解码为连续值，因此它不是 fully spike-only detector，而是“spiking feature extractor/fusion + decoded conventional detection head”路线。

## 2. Problem and Motivation

已有 SNN event detectors 通常直接将 Spiking DenseNet 和 Extra Blocks 产生的多个尺度特征分别送入 SSD head，浅层高分辨率信息和深层语义信息之间缺少充分交互。目标检测又依赖多尺度表示：浅层有利于定位小目标和局部边缘，深层具有更大 receptive field 和更强语义，因此作者将 multi-scale spiking feature fusion 视为提高 SNN detection accuracy 的关键。

另一个问题是 SNN 输出为跨时间步的 spike trains，而分类或检测最终需要连续预测值。不同 decoding strategies 会改变输出范围，并进一步影响 MSE、CE 和后续检测头的优化。SFOD 因此同时研究网络结构和输出接口，而不是只替换 neuron model。

## 3. Method Overview

原始 event stream 被编码为 voxel cube。整个事件窗口被划分为 `T=5` 个主要时间步，每个时间步再划分为 `n=2` 个 micro time bins，并按两种 polarity 分开，因此每个主时间步包含 4 个输入通道。

模型流程为：

```text
Event stream
→ Voxel cube
→ Spiking DenseNet backbone
→ Multi-level spiking feature maps
→ Deconv Blocks
→ Concatenation
→ Spiking Pyramid Extraction Submodule
→ Spiking Rate Decoding
→ SSD detection head
→ Classes and bounding boxes
```

Spiking DenseNet 使用 dense connectivity 复用同一时间步中不同网络层的特征，并通过 PLIF membrane states 在时间步之间积累信息。SFOD 选择分辨率为 `30×38`、`15×19` 和 `7×9` 的前三层特征进行融合。低分辨率特征经过 1×1 convolution 和 transposed convolution 对齐到统一尺寸，随后沿 channel dimension 拼接。SPES 再从融合后的高分辨率特征中逐级生成六个检测尺度。

各尺度输出仍是 spike sequences，随后通过 Rate Decoding 转换为连续 feature maps，再输入不含 spiking activation 的 SSD head，预测 anchor classes 与 bounding-box offsets。

## 4. Key Components and Mechanisms

### 4.1 Spiking DenseNet Backbone

Spiking DenseNet 继承普通 DenseNet 的 dense connection：每个 Dense Layer 接收当前 Dense Block 内所有前序层的输出，而不是只接收上一层。普通 activation 被 PLIF neuron 替代，因此 convolution 负责当前时间步的空间与通道变换，PLIF 负责膜电位积累、阈值发放和时间状态传递。

SFOD 没有重新设计 Dense Block 本身，而是比较不同 depth 和 growth rate 的 Spiking DenseNet，并最终根据 GEN1 detection performance 选择 DenseNet121-24，而不是直接采用 NCAR classification accuracy 最高的 DenseNet121-16。

### 4.2 Spiking Fusion Module

原始 Spiking DenseNet+SSD 将多个尺度直接送入检测头；SFOD 则先融合三个较高分辨率特征。作者选择 concat 而不是 element-wise sum，以避免多个 binary spike maps 相加后出现大于 1 的多值输出。Concat 能保留各分支的 spike values，但会增加 channel width 和 memory cost，因此不能简单等同于更低计算量。

Transposed convolution 用于对齐空间尺寸。它可以嵌入 Conv–PLIF 结构，但本身仍是带权卷积，并不天然保持二值输出或保证低能耗。

### 4.3 SPES and SEW Residual Enhancement

SPES 将 fused feature map 重新生成多尺度 pyramid。作者比较 basic SPES、Spiking Dense Block-enhanced SPES 和 SEW Res Block-enhanced SPES。

Spiking Dense Block 通过 dense concatenation 强化 feature reuse，但在 SPES 中导致 feature connections、channel interaction 和 firing activity增加。SEW Res Block 则提供更直接的 identity path，改善超过 100 层网络中的信息和梯度传播。最终 SFOD-R 使用 SEW-enhanced SPES。

### 4.4 Spiking Decoding and Loss Matching

Count Decoding 直接统计 `T` 个时间步内的 spikes，输出范围为 `[0,T]`；Rate Decoding 将其除以 `T`，输出范围归一化为 `[0,1]`。固定 `T` 时两者信息相同，差异主要是数值尺度。

NCAR 使用 one-hot targets，因此 Rate outputs 与 MSE targets 的范围更匹配。作者最终在分类预训练中采用 Rate + MSE，并在检测网络中使用 Rate Decoding 将 spiking features连接到 SSD head。

## 5. Experiments and Main Evidence

实验使用 NCAR 进行 car/background classification 和 backbone pretraining，使用 GEN1 进行 car/pedestrian object detection。

NCAR 上，DenseNet121-16 配合 Rate + MSE 达到 93.7% accuracy 和 14.70% firing rate，优于其他 decoding/loss combinations，并取得论文比较范围内的 SNN-based最好结果。更深或更宽的 Spiking DenseNet 通常伴随更高 firing rate，但 classification accuracy 并未提升，说明扩大 SNN 容量并不自动改善简单二分类任务。

GEN1 上，Rate Decoding 将无 fusion 的 DenseNet121-24-SSD 从 0.235 提升到 0.288 mAP@0.5:0.95，而 firing rate 基本不变，说明改进主要来自 decoded feature scale 与检测头接口的匹配。三层融合达到 0.299，加入第四个 `4×5` 低分辨率特征后参数增加且 mAP 降至 0.294，表明融合更多尺度不一定有益。

SFOD-D 使用 Spiking Dense Block 后降至 0.286，并具有更高 firing rate；SFOD-R 使用 SEW Res Block 后达到 0.321 mAP@0.5:0.95、0.593 mAP@0.5 和 24.04% firing rate。它超过 EMS-YOLO 的 0.310，是表中最强 SNN detector，但仍低于 RED 的 0.400 和 RVT 的 0.472。

论文报告 11.9M parameters、6.7 ms runtime 和 7.26 mJ energy。Energy 的计算方法位于 supplementary material，主文没有真实 neuromorphic hardware measurement，因此只能视为估算性效率证据。相较前作最佳 0.189，SFOD 提升约 70%，并非严格意义上的“接近翻倍”。

## 6. Strengths and Limitations

**Strengths**

* 将成熟 object detector 中的 multi-scale feature fusion 明确引入 event-camera SNN。
* 将 fusion architecture、decoding strategy 和 loss matching 放在同一框架中分析。
* 消融覆盖 backbone、decoding、fusion range 和 SPES variants，能够定位主要增益来源。
* 在 GEN1 上显著推进 SNN-based detection performance。

**Limitations / Questions**

* 进入 SSD head 前进行 decoding，因此不是 fully spiking detector。
* 所谓 temporal fusion 主要来自 spiking feature maps 和 PLIF states，没有独立 temporal attention 或 recurrent fusion operator。
* Concat、transposed convolution、SEW operations 和普通 SSD head 都削弱了“纯 spike-driven computation”的表述。
* 论文没有报告 no-NCAR-pretraining baseline，无法分离预训练与 fusion 的独立贡献。
* Voxel time-index 公式在 PDF 中将分母写成 `t_a-t_b`，按定义会产生负索引，几乎可以确定是 typographical error，但仍需代码核对。
* Firing rate 和 estimated energy 不能直接证明真实硬件功耗优势。

## 7. Relation to Other Papers and Survey Taxonomy

SFOD 继承前作 Spiking DenseNet+SSD 的 voxel cube、PLIF backbone、Extra Blocks 和 SSD head，但将“多尺度特征独立预测”改成“先融合、再重建 pyramid”。其核心创新主要位于 detection neck 和 spiking-to-analog interface，而不是 neuron model 或 backbone 基础结构。

在综述 taxonomy 中，它属于：

* SNN-based event-camera object detection；
* voxelized event representation；
* surrogate-gradient direct training；
* PLIF-based spiking CNN；
* multi-scale spiking feature fusion；
* decoded non-spiking detection head；
* firing-rate and estimated-energy evaluation。

它适合作为讨论 SNN 如何继承现代检测器 multi-scale hierarchy，以及 SNN 与 conventional head 之间接口设计的核心案例。

## 8. Survey-Usable Takeaways

* Takeaway 1: SNN event detector 的性能瓶颈不只来自 neuron model，缺乏深浅层 feature fusion 同样会限制检测性能。
* Takeaway 2: Count 和 Rate Decoding 在固定时间步下包含相同信息，但输出尺度会显著影响 loss 和后续 detection head 的优化。
* Takeaway 3: 多尺度融合并非层数越多越好；过低分辨率特征可能增加参数和冗余，却无法改善定位性能。
* Takeaway 4: SEW residual identity mapping 在本文 SPES 中优于 dense connectivity，说明适合 backbone 的连接方式不一定适合 detection neck。
* Takeaway 5: Firing rate、runtime、estimated energy 和真实硬件功耗是不同层面的指标，不能相互替代。

## Supplement Points

### 1. ANN-to-SNN Conversion 与 Direct Training

ANN-to-SNN conversion 先训练普通 ANN，再将 ReLU activation 用 SNN firing rate 近似，并通过 weight normalization、threshold calibration 等方式将网络转换为 spiking neurons。其问题是 firing rate 的离散精度依赖较多时间步。SFOD 不采用 conversion，而是通过 surrogate gradients 直接训练 PLIF-based SNN，只运行较少时间步。

### 2. LIF、PLIF 与 Convolution–PLIF 计算

Convolution 在当前时间步对空间邻域和 channels 加权，产生输入电流：

$$
I_t^{(l)}
=

\operatorname{Conv}_l
\left(
S_t^{(l-1)}
\right)
$$

PLIF 将当前输入与上一时间步膜电位结合：

$$
\widetilde{V}_t^{(l)}
=

\lambda_l V_{t-1}^{(l)}
+
I_t^{(l)}
$$

达到阈值时输出 spike：

$$
S_t^{(l)}
=

H
\left(
\widetilde{V}_t^{(l)}
-

V_{\mathrm{th}}
\right)
$$

普通 LIF 通常固定泄漏率或时间常数，PLIF 则使相关时间参数可学习。Convolution 负责空间和通道特征，PLIF 负责跨时间状态积累。

### 3. 多层 SNN 如何工作

每一层同时接收两类信息：

* 前一网络层在当前时间步输出的 spike map；
* 当前层自己在上一时间步保留的 membrane potential。

网络深度方向是：

```text
Layer 1 spikes → Layer 2 spikes → Layer 3 spikes
```

时间方向是：

```text
Layer l membrane state at time t
→ Layer l membrane state at time t+1
```

因此，多层 SNN 可以理解为“空间上的卷积前馈网络”和“时间上的膜电位递推网络”叠加。Spiking DenseNet 的 dense concatenation发生在同一时间步的不同网络层之间，不是跨时间连接。

### 4. 三种 Spiking Decoding、Count/Rate 差异与 Rate + CE 问题

三种主要 decoding strategies 为：

1. **Spiking Count Decoding**

$$
a_{\mathrm{count}}
=

\sum_{t=1}^{T}s_t
$$

输出范围为 `[0,T]`。

2. **Spiking Rate Decoding**

$$
a_{\mathrm{rate}}
=

\frac{1}{T}
\sum_{t=1}^{T}s_t
$$

输出范围为 `[0,1]`。

3. **Membrane Potential Accumulation Decoding**

最后一层不发 spike，而是读取最终或累计 membrane potential。其输出更连续，但输出层不再是 spike-only。SFOD认为这会削弱 SNN 的发放机制和非线性，因此没有进一步采用；具体读取最终膜电位还是累计全部时间步，正文未明确，`Needs further check`。

本文设置 `T=5`。若 spike sequence 中有 3 个 spikes，则：

$$
a_{\mathrm{count}}=3
$$

$$
a_{\mathrm{rate}}=\frac{3}{5}=0.6
$$

二者信息相同，但 Rate 与 one-hot label 的 `[0,1]` 范围更匹配，因此 Rate + MSE 较稳定。Count + MSE 则直接用 `[0,5]` 输出拟合 `[0,1]` target，absolute error 较大。

Rate + CE 在本文中并非完全失效，accuracy 仍有 93.0%，但 firing rate 高于 Rate + MSE。普通分类任务中 CE 通常作用于**不受限的 logits**，网络可以不断扩大正确类别与错误类别的 logit margin。本文却将受限于 `[0,1]` 的 firing rates 直接作为 logits。即使理想输出为 `[0,1]`，softmax 后正确类别概率也只有约 0.731，CE 仍要求继续增大 margin，但 Rate output 已到达上限。

因此，区别不是“正常分类能用 CE，而 SNN 不能用 CE”，而是：

> 普通 ANN 的 logits 通常无固定上界；SFOD 的 Rate outputs 被限制在 `[0,1]`，却未经 scale 或 temperature 调整就输入 softmax。

论文没有比较 scaled rates、temperature 或其他 logit transformation，因此其结果只能说明当前 output-range setting 下 Rate + MSE 更匹配，不能证明 CE 普遍不适合 SNN。

### 5. Voxel Cube 公式与时间索引

Voxel cube 中：

$$
E(\tau,c,x,y)
$$

表示落入主时间格、micro-time/polarity channel 和像素位置的 event 数量。多个 delta functions相当于匹配开关：只有事件的时间、通道和坐标都与当前位置一致时，该事件才被计入。

PDF 中时间索引写为：

$$
\tau_k
=

\left\lfloor
\frac{t_k-t_a}{t_a-t_b}T
\right\rfloor
$$

合理形式应更可能为：

$$
\tau_k
=

\left\lfloor
\frac{t_k-t_a}{t_b-t_a}T
\right\rfloor
$$

否则会产生负时间索引。`Needs further check against code`。

### 6. SEW Res Block 与 Spiking Dense Block

SEW Res Block 通过 identity shortcut 和 spike-compatible element-wise fusion改善深层网络的信息与梯度传播。SFOD 正文没有明确说明采用哪种具体 SEW operation，`Needs further check`。

Spiking Dense Block 将所有前层 feature maps 沿 channel dimension concatenation，强化 feature reuse，但会增加 channels、memory traffic 和可能的 spike activity。本文中 SFOD-D 的 mAP 下降且 firing rate 上升，而 SFOD-R 同时提高 mAP并略降 firing rate，说明 SPES 更适合 residual identity path，而不是进一步增加 dense connectivity。

### 7. Spiking DenseNet、Growth Rate 与 Firing Rate

DenseNet 中每个 Dense Layer 新增的 channel 数称为 growth rate。若初始 channels 为 `C_0`，每层增加 `k` 个 channels，则：

$$
C_l
=

C_0+l,k
$$

DenseNet121-24 中 `121` 表示网络深度，`24` 表示每个 Dense Layer 新增 24 个 channels。

Firing rate 可近似写为：

$$
\mathrm{FR}
=

\frac{
\text{所有时间步产生的 spike 总数}
}{
\text{神经元总数}\times T
}
$$

Growth rate 增大会增加网络宽度、feature interactions 和神经元数量，但 firing rate 是比例，神经元数量增加本身不必然使该比例升高。本文只能观察到：更大的 growth rate 通常伴随更高 firing rate，这是模型特征分布和激活模式变化的实验结果，而不是普遍数学规律。

Firing rate 在本文中用于评估 accuracy–activity trade-off：Rate + MSE、DenseNet121-16 和 SFOD-R 都表现出更好的精度与神经元活动平衡。但较低 firing rate 只有在支持 sparse event-driven execution 的硬件上才可能转化为低能耗，不能单独代表 runtime 或真实 power consumption。

### 8. SFOD 相对原始 Spiking DenseNet+SSD 的改动

SFOD 没有重写 Spiking DenseNet 内部 Dense Blocks，主要改动包括：

1. 比较不同 depth 和 growth rate，并为检测选择 DenseNet121-24；
2. 在 NCAR pretraining 中研究 decoding/loss combinations；
3. 使用 Rate Decoding 连接 spiking features 与 SSD head；
4. 新增 Spiking Fusion Module；
5. 将三个 backbone feature levels 对齐并 concat；
6. 使用 SPES 重新生成六级 feature pyramid；
7. 使用 SEW Res Block增强 SPES；
8. 保留非脉冲 SSD prediction head。

其创新重点是 backbone 输出后的 feature organization、fusion 和 decoding，而不是新的 neuron model或新的 DenseNet backbone。
