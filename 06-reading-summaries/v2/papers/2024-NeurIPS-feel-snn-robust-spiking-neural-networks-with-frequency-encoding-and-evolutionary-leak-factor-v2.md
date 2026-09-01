---
tags: [SNN, frequency-encoding, Fourier, robustness, adversarial-attack, leak-factor, advisor-core]
---

# Summary V2｜FEEL-SNN: Robust Spiking Neural Networks with Frequency Encoding and Evolutionary Leak Factor

## 1. Core Understanding

本文研究 SNN 在对抗扰动和普通噪声下的鲁棒性。作者认为，已有 SNN 鲁棒性解释主要依赖实验，而且常用的 direct encoding（把同一图像重复输入 $T$ 个时间步）和固定 leak factor 过于简化，无法体现生物视觉注意和神经元非固定膜电位泄漏。论文从 loss 对输入扰动的敏感性出发，提出一个统一约束，并设计 FEEL-SNN：Frequency Encoding（FE）在输入侧按时间步选择不同频率，Evolutionary Leak factor（EL）让不同层、神经元和时间步学习不同的膜电位泄漏因子。

FEEL-SNN 是以规则网格静态图像为输入的 direct-trained、time-stepped SNN。FE 位于图像进入 SNN 之前，执行 DFT、频率 mask 和 inverse DFT；EL 位于 LIF membrane update 内。本文没有处理 raw event stream 或 Event Cloud，也没有给出 DVS 实验。因此，对 SECNet extension 的价值是提供 Fourier-to-SNN coupling 和可学习 temporal leak 的机制启发，而不是一个可直接替换 SECNet 输入接口的架构。

## 2. Problem and Motivation

局部线性分析给出扰动造成的 loss 增量上界：

$$
L(x+\epsilon)-L(x)
\leq
\left|\epsilon\odot\nabla_xL(x)\right|_1+g(\epsilon,x),
$$

其中 $g$ 是残差项。对 SNN，输入 $x+\epsilon$ 会被编码为 $T$ 个时间步，因此作者把鲁棒性目标写成减小：

$$
\sum_t\left|\epsilon^{(t)}\odot\frac{\partial L}{\partial x^t}\right|_1.
$$

通过 BPTT，作者将该项展开为输入扰动和时间泄漏、层间权重、脉冲 surrogate gradient 的乘积：

定理设 SNN 有 $L$ 层、推理 $T$ 个时间步，第 $l$ 层有 $N_l$ 个神经元，并且：

$$
\lambda_l\in\mathbb{R}^{N_l\times T},
\qquad
W_{l-1,l}\in\mathbb{R}^{N_l\times N_{l-1}}.
$$

$$
\min\sum_t\left|\epsilon^{(t)}\odot\frac{\partial L}{\partial x^t}\right|_1
=
\min\sum_t\left|\sum_{l=1}^{L}
\left[
\left(\prod_{k=t}^{T}\epsilon^{(t)}\odot\lambda_l^k\right)
\left(\prod_{q=2}^{l}W_{q-1,q}\right)
\left(\prod_{v=1}^{l}\frac{\partial O_v^t}{\partial u_v^t}\right)
\frac{\partial L}{\partial O_l^T}
\right]\right|_1.
$$

作者将三部分分别解释为：项 1 中的输入扰动与 leak factor，项 2 中的 weights，以及项 3 中的 surrogate gradient。FE 和 EL 都针对项 1：FE 使不同时间步的输入扰动不再被完全重复，EL 调整扰动沿 membrane state 的时间传播。该理论框架也解释了 weight regularization 和 surrogate-gradient design 为什么可能影响鲁棒性，但它并不单独证明 FE 或 EL 对所有数据集、噪声和攻击都有效。

## 3. Method Overview

### LIF dynamics

第 $l$ 层的突触输入为：

$$
m_l^t=
\begin{cases}
W_{l-1,l}O_{l-1}^t, & l>1,\\
x^t, & l=1.
\end{cases}
$$

膜电位和脉冲更新为：

$$
u_l^t=\lambda_l^t u_l^{t-1}\odot(1-O_l^{t-1})+m_l^t,
$$

$$
O_l^t=H(u_l^t-V_{\mathrm{th}}).
$$

其中 $u_l^t$ 是 membrane potential，$O_l^t$ 是 binary spike，$W_{l-1,l}$ 是层间权重，$\lambda_l^t$ 控制历史膜电位保留程度，$V_{\mathrm{th}}$ 是阈值。上一时间步发放后，reset gate $1-O_l^{t-1}$ 阻止旧膜电位继续累积。过去工作通常令 $\lambda_l^t=\lambda$，本文将其变为按层、神经元和时间步可学习的量。

### Frequency Encoding

给定 $x\in\mathbb{R}^{M\times N}$，FE 先计算二维 DFT：

$$
x^F_{m,n}=F(x)_{m,n}
=\sum_{a=0}^{M-1}\sum_{b=0}^{N-1}x_{a,b}
e^{-j2\pi(\frac{ma}{M}+\frac{nb}{N})}.
$$

在作者采用的频谱布局中，低频位于中心附近。对第 $t$ 个时间步，频域 mask 通过逐元素乘法保留中心窗口：

$$
x_t^F\leftarrow M_t\odot x_t^F,
$$

$$
M_{m,n}=\begin{cases}
1, & 0\leq|m|,|n|\leq r,\\
0, & \text{otherwise}.
\end{cases}
$$

再通过 inverse DFT 得到 SNN 输入：

$$
\tilde{x}_{r_i}^{\,t}=F^{-1}\left(M_{r_i}^{\,t}\odot F(x)\right),
\qquad i,t\in\{1,\ldots,T\}.
$$

窗口半径满足 $r_i>r_j$（$i<j$）：早期时间步保留更宽的频率范围，后期时间步逐渐收缩到低频中心。因此 direct encoding 的 $x_1=\cdots=x_T=x$ 被替换为具有时间变化频率内容的序列。该机制假设自然图像的大尺度结构主要由低频表达，而噪声可能出现在不同频段；它不是保证所有高频都是噪声，也可能同时删除有用边缘。

### Evolutionary Leak factor

较小的 $\lambda$ 可以减弱扰动跨时间传播，但过小会损失正常的 temporal memory。作者不用单独的 leak regularization，而是直接把 $\lambda_l^t$ 作为可训练参数：

$$
\lambda_l^t\leftarrow\lambda_l^t-\eta\Delta\lambda_l^t,
$$

$$
\Delta\lambda_l^t=\frac{\partial L}{\partial\lambda_l^t}
=\frac{\partial L}{\partial O_l^t}
\frac{\partial O_l^t}{\partial u_l^t}
\frac{\partial u_l^t}{\partial\lambda_l^t}
=\frac{\partial L}{\partial O_l^t}
\frac{\partial O_l^t}{\partial u_l^t}u_l^{t-1}.
$$

损失为：

$$
L=L_{\mathrm{CE}}(x,y,W,\lambda).
$$

由于 Heaviside spike function 不可微，作者使用三角形 surrogate gradient：

$$
\frac{\partial O_l^t}{\partial u_l^t}
=\frac{1}{\gamma^2}\max\left(0,\gamma-|u_l^t-V_{\mathrm{th}}|\right).
$$

因此 FE 改变每个时间步的频率输入，EL 改变每个时间步和神经元对历史 membrane state 的保留程度；两者共同作用于理论约束中的项 1。

## 4. Key Components and Mechanisms

FE 的 mask 是中心低通窗口。较大 $r$ 保留低频、中频和部分高频；较小 $r$ 删除更多外围频率。本文的时间变化策略不是在每个时间步重复相同滤波图像，而是构造一个从宽频率范围逐渐收缩到低频核心的输入序列。IFE（从低频到高频裁剪）会快速删除低频结构，作者用它作为方向性对照。

EL 的“evolutionary”在当前方法中表现为训练时的梯度更新，而不是正文已明确给出的遗传算法。其优势来自鲁棒性与 temporal information preservation 的折中：$\lambda=0$ 能减弱历史扰动传播，却可能破坏有效时序信息；可学习的 $\lambda_l^t$ 试图让不同神经元在不同时间步找到更合适的配置。

本文的对抗攻击基于完整可微路径。FGSM 使用一次输入梯度：

$$
\hat{x}=x+\epsilon\operatorname{sign}(\nabla_xL(x,y)).
$$

PGD 使用多步梯度更新并投影回 $L_\infty$ 球：

$$
x^{k+1}=\Pi_{B_\infty(x,\epsilon)}\left(x^k+\alpha\operatorname{sign}(\nabla_xL(x^k,y))\right).
$$

BIM 是从 $x$ 开始、通常不使用 random start 的 iterative FGSM；CW 则把扰动大小和分类失败目标写成优化问题。White-box attack 可访问 FE、SNN、surrogate gradient 和权重；black-box 实验使用不同随机种子的源模型生成扰动，测试其向目标模型的迁移。由于 DFT、mask 和 inverse DFT 可微，FE 不是通过阻断梯度实现防御，而是通过改变时间-频率输入和后续 membrane dynamics 改变攻击敏感性。

## 5. Experiments and Main Evidence

实验使用 CIFAR-10、CIFAR-100 和 Tiny-ImageNet，网络为 VGG11、WideResNet16 和 ResNet19；$\gamma=1.0$、$V_{\mathrm{th}}=1.0$。比较 vanilla BPTT、adversarial training（AT）、带 Lipschitz penalty 的 RAT 和随机门控 StoG，并测试加入 FE 或 FEEL 后的表现。AT 使用 white-box PGD 样本训练，$\epsilon=2/255$、迭代步数 $k=2$。攻击包括 white-box/black-box FGSM、PGD、BIM、CW，以及 Gaussian Noise。

FE 的频率窗口按时间步设置：CIFAR-10/CIFAR-100 在 $T=4$ 时使用 $r=[16,14,12,10]$，在 $T=8$ 时使用 $r=[16,14,12,10,8,6,4,2]$；Tiny-ImageNet 在 $T=4$ 时使用 $r=[32,30,28,26]$。对抗扰动在图像域、FE 之前生成，因为 DFT、mask 和 inverse DFT 都是可微的。

在 CIFAR-10 的 VGG11 上、$T=4$ 时，作者报告 FEEL 相对 vanilla 在 PGD 和 CW 下最多提升 15% 和 6%。CIFAR-100 的 WideResNet16 在 $T=8$、CW black-box 下最多提升 4.27%。在 PGD 上，vanilla、RAT、RAT+FE、RAT+FEEL 的报告鲁棒准确率示例为 0.16%、8.87%、9.70% 和 12.36%，说明 FE/FEEL 可以叠加在既有鲁棒训练方法上。

IFE 将 clean accuracy 从 vanilla 的 92.64% 降到 64.81%，而 FE 的 clean accuracy 为 92.26%；PGD 下 vanilla 为 15.59%，FE 为 21.56%。该对照支持在这些静态图像实验中保留低频中心更有利于准确率和鲁棒性。作者还报告：不同时间步使用不同 $r$ 优于固定 $r$ 或先滤波再重复 $T$ 次的策略。

EL 消融显示，完全令 $\lambda=0$ 虽然可将 PGD accuracy 提高到 63.80%，但 clean accuracy 降至 81.76%；REL 的 clean accuracy 为 88.52%，而 EL 同时达到 92.73% clean accuracy 和 30.27% PGD accuracy，vanilla 对应为 92.64% 和 15.59%。这些结果支持“过强 leak 抑制扰动但损失时间信息，学习到的 leak 可以取得折中”。

效率证据主要是模型在指定攻击下的 accuracy、时间步配置和训练/推理设置，不是 neuromorphic hardware 的真实能耗测量。结论应限定在这些静态数据集、网络、攻击算法和扰动预算内；论文第 6 节也明确承认尚未解决 DVS 数据集的可靠频率编码。

## 6. Strengths and Limitations

本文的优势是把鲁棒性分析连接到 SNN 的具体时间传播项，并同时修改 input encoding 与 membrane dynamics；FE 具有明确的 DFT-mask-iDFT 数据流，EL 具有明确的梯度更新公式；FE、EL 与 IFE、固定半径、$\lambda=0$ 和已有鲁棒方法的对照能支持其主要机制解释。

主要限制是：理论框架给出的是约束和设计动机，不是对 FEEL 在所有数据和噪声下有效的普适证明；自然图像低频假设不等于高频都是噪声；所有主要实验都是静态规则网格图像，不能直接证明 raw event 或 DVS 适用；white-box robustness 依赖 surrogate-gradient attack protocol；当前给出的章节没有完整展开 CW 的范数和优化参数，需以附录 A.1 为准。论文中的 efficiency 也应理解为模型/实验指标，而不是硬件实测能耗。

## 7. Relation to SECNet Extension Direction

FEEL-SNN 对 SECNet extension 最直接的启发是把频率机制和 SNN state dynamics 联合考虑。FE 提供一个明确的 frequency-to-spike 输入接口：先对规则图像做 DFT，再用随时间变化的 mask，最后 inverse DFT 后进入 SNN。SECNet 可以借鉴这种“频率选择随时间或事件上下文变化”的思想，但 Event Cloud 是稀疏、异步、带 $(x,y,t,p)$ 坐标的事件集合，不能直接套用规则二维图像 DFT。需要重新定义对 event coordinate、局部 voxel、Event Cloud hierarchy 或 temporal bins 的频率对象。

EL 则提供 SNN coupling 方向：不同空间位置/通道或事件层级的神经元，可以根据局部事件密度、时间间隔或频率响应学习不同 leak。真正迁移前需要验证不规则事件时间、事件极性、稀疏邻域和 asynchronous state update 是否仍能形成可解释的 leak gradient。FEEL-SNN 只证明了静态图像 adversarial noise 下的结果，没有证明对 event noise、background activity、sensor noise 或 event burst 有效。

因此，FEEL-SNN 更适合作为 SECNet 的机制参考：frequency representation 可以放在 Event Cloud 分层之后或局部时频聚合处，adaptive leak 可以放在 SNN coupling 的 temporal state 中；但 event-side transform、异步更新、稀疏计算和鲁棒性评估都需要重新设计，不能把 image DFT 与静态数据上的 accuracy 直接视为 SECNet extension 的证据。

## 8. Survey-Usable Takeaways

本文可作为 Advisor direction 中的 Fourier-to-SNN coupling 参考：它的核心不是在网络内部进行 spatial attention，而是用输入级 DFT mask 改变不同时间步接收的频率内容，再用可学习 leak factor 调节这些频率内容在 SNN membrane state 中的传播。对 SECNet 的可迁移部分是“频率选择与脉冲状态联合建模”；不可直接迁移部分是规则图像网格、静态频谱假设以及仅针对图像 adversarial attacks 的证据。

## Supplement Points

### Questions and Clarifications

#### 1. 为什么 DFT 频谱中心通常表示低频，外围通常表示高频，以及 FE 的频率窗口为什么随时间变化

用户询问：根据 DFT，为什么图像的低频部分位于 $x^F$ 的中心区域？为什么论文说原始图像信息主要集中在低频区域，而噪声从低频延伸到高频？frequency spectrum 应该如何理解？为什么 FE 让频率抑制范围随时间步从高频逐渐扩展到低频？

低频位于频谱中心首先不是 DFT 数学定义必然产生的布局，而是通常使用 `fftshift` 后的显示约定。严格的 DFT 中，零频率 DC component 位于数组的 $X[0,0]$，通常在角落；`fftshift` 将零频率移到中心，因此频谱图显示为中心低频、外围高频。也就是说，“中心低频、外围高频”同时包含数学频率坐标和可视化排列两个层面；如果不做 shift，低频通常仍然在频谱数组的角落附近。

二维 DFT 为：

$$
X[m,n]=\sum_{a=0}^{M-1}\sum_{b=0}^{N-1}x[a,b]
e^{-j2\pi\left(\frac{ma}{M}+\frac{nb}{N}\right)}.
$$

频谱坐标 $(m,n)$ 代表一种二维空间变化模式。若频率坐标接近零，图像亮度在空间上变化缓慢；若坐标距离零频率较远，图像亮度变化更快。一个一维例子是 $\sin(2\pi ka/N)$：$k$ 较小时，信号在整个空间中缓慢起伏，是低频；$k$ 较大时，信号在相邻位置之间快速变化，是高频。二维图像只是把这种变化扩展到水平和垂直方向。

DC component 对应整个图像的平均亮度，因为零频率基函数在空间中是常数。频谱通常显示复数系数的幅度，而不是直接显示复数：

$$
A[m,n]=|X[m,n]|,
$$

或其对数幅度：

$$
A_{\log}[m,n]=\log(1+|X[m,n]|).
$$

频谱中的每个位置表示一种二维空间变化模式。接近中心的频率表示亮度缓慢变化，例如大面积平滑区域；远离中心的频率表示相邻像素快速变化，例如边缘、纹理和像素级突变。自然图像通常具有空间连续性，所以整体轮廓、亮度和大尺度结构往往贡献较多低频能量。但“自然图像低频能量较多”是自然图像统计规律，不是 DFT 定理；高频也可能包含重要的物体边缘和纹理。

因此，frequency spectrum 不是一张“低频图片”和一张“高频图片”的拼接，而是图像中各种空间变化速度的系数表。频谱图中的亮区域表示该频率模式的幅度较大。水平或垂直方向远离中心，分别表示某个方向上的变化更快；沿对角线远离中心，则表示两个方向都存在较快变化。若对频谱乘 mask，再执行 inverse DFT，才会得到只保留某些变化速度的空间图像。

噪声也不能简单等同于高频。像素独立随机噪声通常覆盖较宽频率范围，快速变化噪声通常包含较多高频；大面积亮度偏移、缓慢变化的传感器偏差和某些条纹噪声则可能位于低频或中频。因而论文中“噪声从低频到高频分布”应理解为其数据和攻击设置中的观察，而不是适用于所有噪声的普遍定律。

FE 执行：

$$
\tilde{x}_t=F^{-1}\left(M_t\odot F(x)\right).
$$

中心方形 mask 保留低频中心。半径较大时，保留低频、中频和部分高频；半径较小时，删除更多外围频率和中频，只保留更小的低频核心。由于作者设定 $r_i>r_j$（$i<j$），早期时间步使用较大窗口，后期时间步使用较小窗口，输入频率内容因此从较宽范围逐步收缩到低频核心。被抑制的区域是从外围高频逐渐向中心扩展，但低频中心并没有被全部删除。

这使不同时间步不再重复同一个带噪图像。direct encoding 是 $x_1=\cdots=x_T=x$，噪声也会被重复 $T$ 次；FE 则让每个时间步接收不同频率范围的图像，因此特定频段的噪声不会以完全相同的形式在所有时间步传播。不过，如果真实目标边缘和噪声位于同一频段，FE 也可能同时删除二者；所以其鲁棒性依赖噪声频谱、任务内容和实验数据，不能推出所有高频都是噪声或所有任务都适合低通过滤。

#### 2. 对抗攻击是什么以及如何工作

用户要求详细理解本文提到的 FGSM、PGD、BIM、CW，以及 white-box/black-box 攻击。对抗攻击的共同目标是在原始图像 $x$ 上寻找扰动 $\delta$，得到 $\hat{x}=x+\delta$，使模型预测错误，同时限制扰动幅度：

$$
f(\hat{x})\neq f(x),
\qquad
\|\hat{x}-x\|_p\leq\epsilon.
$$

本文使用 $L_\infty$ 约束：

$$
\|\delta\|_\infty=\max_i|\delta_i|.
$$

它限制的是所有像素中最大的单像素改变量，而不是所有像素改变量的总和。因此，当 $\epsilon=2/255$ 时，每个像素最多变化 $2/255$，但很多像素可能同时发生变化。对 untargeted attack，攻击者只需要让原来的预测出错；targeted attack 则会进一步要求输出指定的错误类别。本文当前章节主要讨论前一种情况。

FGSM 只计算一次输入梯度：

$$
\hat{x}=x+\epsilon\operatorname{sign}(\nabla_xL(x,y)).
$$

它沿着最能增大 loss 的方向同时修改像素，速度快但只有一步。

这里的 $\nabla_xL(x,y)$ 是 loss 对每个输入像素的梯度。对 $L_\infty$ 约束，沿梯度的 sign 方向让每个像素尽量移动到允许边界，因而得到一次更新：梯度为正的像素增加 $\epsilon$，梯度为负的像素减少 $\epsilon$。FGSM 的完整流程是前向计算 loss、对输入反向传播、取梯度符号并更新图像。

PGD 是多步 FGSM，并在每一步后投影回原图附近的 $L_\infty$ 邻域：

$$
x^{(k+1)}=\Pi_{B_\infty(x,\epsilon)}\left(x^{(k)}+\alpha\operatorname{sign}(\nabla_xL(x^{(k)},y))\right).
$$

带 random start 的 PGD 从允许扰动区域内随机点开始，因此通常比单步 FGSM 更强。

PGD 的 projection 会把每个像素限制在原始像素的区间 $[x_i-\epsilon,x_i+\epsilon]$ 内，同时通常还要把像素限制在合法图像范围 $[0,1]$。random start 可以写成：

$$
x^{(0)}=x+\delta^{(0)},
\qquad
\delta^{(0)}\sim\mathcal{U}(-\epsilon,\epsilon).
$$

因此 PGD 不只在同一个初始点上重复走梯度，而是在允许扰动区域中的随机位置开始搜索。攻击强度由 $\epsilon$、步长 $\alpha$、迭代次数、random start 和梯度是否来自完整 white-box 模型共同决定。

BIM 是从干净图像开始的 iterative FGSM，反复执行小步梯度符号更新并裁剪到 $L_\infty$ 约束范围内。它与 PGD 的更新形式相近，经典区别主要是 BIM 通常不使用 random start。

CW 将攻击写成优化问题，在改变分类结果的同时尽量减小扰动，例如：

$$
\min_\delta \|\delta\|_p+c f(x+\delta,y),
\qquad x+\delta\in[0,1]^d.
$$

CW 常见实现使用 $L_2$ 目标，也有其他范数版本；其具体范数和参数应以本文附录 A.1 为准。

若模型输出 logits 为 $Z(x)$，一个典型的 untargeted CW 目标可以写为：

$$
f(x+\delta,y)=\max\left(
Z_y(x+\delta)-\max_{i\neq y}Z_i(x+\delta)+\kappa,
0\right).
$$

当真实类别的 logit 仍然最大时，优化会继续推动错误类别超过真实类别；$\kappa$ 控制要求的错误分类置信间隔。CW 与 FGSM、PGD、BIM 的主要差异是：后者通常先固定扰动预算，再在预算内增大 loss；CW 把扰动代价和改变分类的目标一起写进优化问题，直接寻找更小的成功扰动。

White-box attack 访问目标模型结构、参数、FE、SNN 和 surrogate gradient，直接计算 $\nabla_xL$。Black-box attack 不直接使用目标模型梯度；本文用不同随机种子的源模型生成扰动，再测试扰动能否迁移到目标模型。SNN 的攻击梯度通过 BPTT 和 surrogate gradient 计算，因为真实 Heaviside spike function 不可微。FE 的 DFT、mask 和 inverse DFT 是可微的，所以 white-box 攻击可以穿过完整的 FE-to-SNN 路径；FE 的防御作用来自改变时间-频率输入和 membrane dynamics，而不是阻断梯度。

FEEL-SNN 的攻击路径可以抽象为：

$$
x
\rightarrow F(x)
\rightarrow M_t\odot F(x)
\rightarrow F^{-1}(\cdot)
\rightarrow \operatorname{SNN}
\rightarrow L.
$$

因此，攻击扰动是在图像域、FE 之前生成的，但 white-box 梯度会穿过 DFT、频率 mask、inverse DFT、多个时间步和多个脉冲神经元。SNN 的真实 Heaviside 发放函数不可微，实际攻击使用 BPTT 加 surrogate gradient：

$$
\frac{\partial O_l^t}{\partial u_l^t}
\approx
\frac{1}{\gamma^2}
\max\left(0,\gamma-|u_l^t-V_{\mathrm{th}}|\right).
$$

所以 FE 不是通过阻断梯度实现防御，而是改变不同时间步的频率内容以及扰动在 membrane dynamics 中的传播方式。本文报告的 robust accuracy 只能限定在对应 dataset、攻击算法、$\epsilon$、步长和迭代设置下，不能直接推广为对所有攻击或真实噪声都有效。
