---
tags: [event-camera, event-based-synthetic-aperture-imaging, de-occlusion, image-reconstruction, hybrid-snn, ECCV-2024]
---

# Summary V2｜REDIR: Refocus-free Event-based De-occlusion Image Reconstruction

## 1. Core Understanding

REDIR 面向 event-based synthetic aperture imaging（E-SAI）中的去遮挡图像重建。其核心问题是：移动事件相机从多个视角观测被树枝、栅栏等前景遮挡的目标时，不同 timestamp 的目标事件会因相机运动而发生空间错位；若直接累积，目标边缘会形成模糊、重影和伪影。已有方法通常依赖 focal length、moving speed、depth of field、人工 refocusing 或预先生成的 focused event data，并且多假设相机执行理想的匀速直线运动。

REDIR 以 pure event stream 为输入，先用 UNet-like registration network 与 Spatial Transformer Network（STN）对每个 timestamp 的 event frame 及多尺度 feature map 进行仿射配准，再使用带 Temporal-Spatial Attention（TSA）的 SNN 过滤时间上不连续或空间上不稳定的遮挡干扰，最后通过 Perceptual Mask Connection Module（PMCM）和 CNN decoder 重建无遮挡强度图像。完整系统是 hybrid ANN–SNN，而不是 fully spiking network；SNN 只位于 registration 与 CNN reconstruction 之间的 filtering stage。

## 2. Problem and Motivation

E-SAI 通过移动相机形成多个观察位置，相当于合成更大的观测孔径。由于目标与前景遮挡物通常位于不同深度，二者在相机运动时产生不同视差。若按照目标所在的主要深度平面对齐，不同视角中的目标信息会趋于重合，而另一深度的遮挡物仍然保持错位和分散，因此可以通过跨时间融合削弱遮挡并恢复目标。

传统 E-SAI 方法的问题在于：真实相机可能存在抖动、非匀速运动、旋转、缩放或焦距变化，固定的线性偏移模型无法准确配准；人工 refocusing 和采集参数又增加数据制作与部署成本。REDIR 因而试图直接从 event data 中学习每个 timestamp 的二维变换，而不在推理时显式输入焦距、移动速度、景深或人工聚焦结果。

## 3. Method Overview

对第 $t$ 个 timestamp 的事件表示 $E_t$，STN 首先预测变换矩阵：

$$
\psi_{0,t}
=
\operatorname{STN}(E_t).
$$

Spatial Transformation Function（TF）利用 $\psi_{0,t}$ 生成 sampling grid，并从输入 event frame 中进行可微分重采样：

$$
E_t'
=
\operatorname{TF}(E_t,\psi_{0,t}).
$$

这是 event-frame-level coarse alignment。随后，在第 $l$ 个 UNet feature level 上继续预测：

$$
\psi_{l,t}
=
\operatorname{STN}(F_{l,t}),
$$

$$
F_{l,t}'
=
\operatorname{TF}(F_{l,t},\psi_{l,t}),
$$

形成 feature-level refinement。论文将其称为 global/local alignment，但每个 feature map 仍由一个 $2 \times 3$ 矩阵整体变换，并不是为每个像素预测独立 displacement field。

经过配准的多 timestamp features 输入三层 TSA-SNN。作者利用 LIF 的 temporal integration 与 leakage，试图增强连续存在的目标信号并抑制短暂、离散或位置不稳定的遮挡干扰；TSA 则对关键 timestamp 和空间区域赋予更高权重。之后，PMCM 将未掩膜的 registration feature 与 mask-enhanced feature 相加，并作为多尺度 shortcut 送入 CNN decoder。最终，多 timestamp feature maps 经累积和归一化形成重建表示：

$$
FM_{\mathrm{recon}}
=
\frac{1}{N}
\sum_{n=1}^{N}
FM(n).
$$

## 4. Key Components and Mechanisms

论文用相机几何说明配准动机：

$$
P_n^{\mathrm{ref}}
=
K R_n K^{-1}P_n
+
\frac{K T_n}{d}.
$$

该式不是不带条件的普适二维映射，而是针孔模型、相同或已知内参、近似固定目标深度等条件下的简化。更一般的投影需要使用相对位姿、齐次比例因子和最终坐标归一化。对于具有明显厚度和深度变化的三维目标，单个二维矩阵只能准确对齐一个主要深度附近的区域。

论文给出的二维变换为：

$$
\psi
=
\begin{bmatrix}
\frac{\cos\theta}{k} &
\frac{\sin\theta}{k} &
\Delta x \\
-\frac{\sin\theta}{k} &
\frac{\cos\theta}{k} &
\Delta y
\end{bmatrix}.
$$

它实际是 rotation、uniform scaling 和 translation 组成的 similarity transform，只有四个独立参数；后文却称其为 six-degree-of-freedom affine transformation。实际 STN 输出四个受约束参数，还是六个独立矩阵元素：`Needs further check`。

TSA-SNN 在 Fig. 2 中位于 registration 与 CNN decoder 之间，在 Fig. 4 中表示为三个 S-Conv layers 和 TSA skip connection。论文未给出 LIF state update、threshold、reset、surrogate gradient、S-Conv 内部结构、attention 公式和 tensor order：`Needs further check`。因此只能确认 SNN 用于 temporal filtering，不能确认其具体 neuronal dynamics。

PMCM 可概念化为：

$$
Y
=
\operatorname{Conv}(F)
+
\operatorname{Conv}(M \odot F),
$$

其中 $F$ 是已配准 feature，$M$ 是 mask。第一条路径保留完整信息，第二条路径强调目标轮廓并抑制遮挡；两者相加可降低 mask 错误导致目标信息被彻底删除的风险。Mask 如何生成、是否为 soft mask、是否有独立监督：`Needs further check`。

训练目标包含三项。Pixel loss 约束逐像素准确性：

$$
\mathcal L_{\mathrm{pix}}
=
\frac{
\left\|
\Phi-\hat{\Phi}
\right\|_1
}{
CHW
}.
$$

Perceptual loss 比较卷积 feature space 中的结构和感知相似性：

$$
\mathcal L_{\mathrm{per}}
=
\sum_k
\frac{\lambda_k}{C_kH_kW_k}
\left\|
\Phi_k-\hat{\Phi}_k
\right\|_2^2.
$$

Total variation loss 抑制局部噪点和不自然振荡：

$$
\mathcal L_{\mathrm{tv}}
=
\sum_{i,j}
\sqrt{
(\phi_{i,j+1}-\phi_{i,j})^2
+
(\phi_{i+1,j}-\phi_{i,j})^2
}.
$$

Perceptual backbone、选取层和三个 loss weights 均未说明：`Needs further check`。

## 5. Experiments and Main Evidence

原始 E-SAI dataset 包含 488 组 indoor 和 100 组 outdoor scenes，每组划分为 30 timestamps。V-ESAI 在每组原始数据上分别加入 rotation、scaling 和 translation，连同原样本扩展为 2352 组。它直接验证的是人工二维仿射增强下的适应能力，而不是在真实变焦、真实复杂轨迹或真实六自由度相机运动下重新采集的 event data。

Table 1 中，REDIR 的总体结果为 PSNR 25.74、SSIM 0.7395、LPIPS 0.1139。Refocus+Hybrid 需要 prior information，但三个指标均优于 REDIR，因此 REDIR 不是 overall SOTA。在不需要 prior information 的方法中，REDIR 的总体 PSNR 和 LPIPS 最好，但 SSIM 低于 FSAI+CNN。论文的 SOTA 结论必须限定到具体 prior-free metrics。

作者报告相对 Hybrid 的 PSNR 增加 $3.42$ dB；SSIM 从 0.6649 增至 0.7395，实际是增加 0.0746，即 7.46 个百分点，而非相对提高 7.46%；LPIPS 从 0.1678 降至 0.1139，绝对下降 0.0539，相对下降约 32.12%。

Table 2 的完整配置 STN + PMCM + TSA 达到 PSNR 32.61、SSIM 0.8842、LPIPS 0.0279，在该消融设置中最佳。移除 STN 的退化最大，说明 learned registration 是主要贡献；移除 TSA 后 SSIM 和 LPIPS 明显下降；PMCM 提供较小但一致的增益。表中没有仅 STN、仅 PMCM 或仅 TSA 的单模块配置，也没有 mean/std。

Table 1 与 Table 2 对 Hybrid 和完整模型报告的数值明显不一致，而 Table 2 仅标注 E-SAI dataset “part”，未说明具体 subset 或评估协议：`Needs further check`。V-ESAI 只给出少量定性图，无 baseline 定量对比，因此只能支持仿射增强条件下的定性可行性。

## 6. Strengths and Limitations

Strengths：将 event registration、SNN temporal filtering 和 multi-scale reconstruction 统一为端到端框架；STN 避免推理时显式输入焦距、速度或人工 refocusing 结果；消融结果表明 registration 对去遮挡重建确有明显作用；论文展示了 E-SAI 去遮挡这一 hybrid SNN 应用场景。

Limitations：核心方法主要是现有 STN、UNet、attention SNN、mask connection 和 CNN decoder 的组合，机制新颖性有限；公式（5）与 six-DoF 表述不一致；Algorithm 1 中 $l=L$ 的分支很可能存在索引错误；TSA-SNN 和 PMCM 缺乏关键实现细节；V-ESAI 只是二维仿射 augmentation；Table 1 与 Table 2 协议不清且数值冲突；百分比表述存在错误；没有 runtime、latency、operation count、energy 或 neuromorphic hardware evaluation。

## 7. Relation to Other Papers and Survey Taxonomy

本论文主要属于 event-based image reconstruction、event-based de-occlusion、event registration/alignment、hybrid ANN–SNN architecture、temporal filtering、attention mechanism 和 dense prediction。它不属于 fully spiking reconstruction，也不是新的 SNN training method 或 neuromorphic hardware work。

在综述中，其价值主要是补充一个应用分支：SNN 不仅可用于 classification、detection 或 optical flow，也可作为 E-SAI 去遮挡系统中的 temporal filter。相较专门研究 event representation、neuronal dynamics 或 SNN learning 的论文，REDIR 更适合作为 application-oriented example，而不是深入展开的核心方法论文。

### PDF-verified relation backfill

主要路线是 STN timestamp registration、SNN/TSA occlusion filtering 与 ANN reconstruction decoder 的 hybrid pipeline。

- **Learning to See Through with Events (Lei Yu et al., TPAMI 2023)** — `foundation`。该工作提供 event synthetic aperture de-occlusion 的基础机制；当前论文将其用于自身的 event/SNN pipeline，而不是把该前驱本身作为新贡献。 对应 Section 5: reconstruction and restoration。证据：Introduction and Related Work, PDF pp.2-4, citation and bibliography [30]。 当前 active corpus 未覆盖。
- **Event-based Synthetic Aperture Imaging with a Hybrid Network (Xinyu Zhang et al., CVPR 2021)** — `baseline`。该工作是 event de-occlusion reconstruction 的实验 comparator；当前论文与其主要区别在于本文第 3–4 节所述的核心机制。 对应 Section 5: reconstruction and restoration。证据：Experiments 5.2, PDF pp.11-12, citation and bibliography [31]。 当前 active corpus 未覆盖。
- **Spatial Transformer Networks (Max Jaderberg et al., NeurIPS 2015)** — `foundation`。该工作提供 learned affine event registration 的基础机制；当前论文将其用于自身的 event/SNN pipeline，而不是把该前驱本身作为新贡献。 对应 Section 5: reconstruction and restoration。证据：Method 4.2, PDF pp.7-8, citation and bibliography [9]。 当前 active corpus 未覆盖。

## 8. Survey-Usable Takeaways

REDIR 表明，移动事件相机的多视角去遮挡任务可以分解为：先学习每个 timestamp 的二维 registration，再利用 SNN 的时间状态过滤不稳定遮挡事件，最后通过 ANN decoder 恢复强度图像。其最值得综述引用的结论是：在 E-SAI 场景中，SNN 可作为 hybrid pipeline 的 temporal filtering component；但论文的主要性能来源更可能是 STN-based registration，而不是新的 SNN 机制。

实验只能支持 REDIR 在既定 E-SAI 数据和人工 affine-augmented V-ESAI 上具有可行性。对真实 variable-motion acquisition、复杂三维深度、SNN 过滤机制以及系统效率的结论仍缺乏充分证据。因此，综述中宜简要介绍其任务设定和 hybrid architecture，不宜将其作为 SNN 方法论或效率研究的重点案例。

## Supplement Points

### Questions and Clarifications

#### 1. E-SAI 是什么？为什么移动相机可以用于去遮挡？

E-SAI 是 Event-based Synthetic Aperture Imaging，即事件式合成孔径成像。它不是一种神经网络，而是一种数据采集与成像方式：事件相机沿多个空间位置移动，从不同视角观察同一场景，并将这些位置的事件信息对齐和融合。

假设目标位于树枝后方。相机在位置 $C_1$ 时，树枝可能遮住目标左侧；移动到 $C_2$ 后，由于目标和树枝深度不同，二者在图像中的相对位置发生变化，之前被遮挡的区域可能重新可见。若按目标所在深度对齐：

$$
P_1^{\mathrm{target}}
\approx
P_2^{\mathrm{target}}
\approx
\cdots
\approx
P_N^{\mathrm{target}},
$$

目标事件会在统一坐标中重合；前景遮挡物因为深度不同，通常不会同时重合。后续 temporal filtering 和 multi-view accumulation 因而可以增强目标并削弱遮挡。

E-SAI 的核心不是从一个视角“看穿”遮挡，而是利用多个视角补全目标信息：

$$
\text{multi-view acquisition}
\rightarrow
\text{target registration}
\rightarrow
\text{occlusion filtering}
\rightarrow
\text{reconstruction}.
$$

#### 2. APS frame、event stream 和 event frame 有什么区别？

APS 是 Active Pixel Sensor。DAVIS 类事件相机通常可同时输出异步事件流和 APS intensity frames。

APS frame 类似普通灰度图，它在一个曝光周期内记录整张图像的光强。Event stream 则由异步事件组成：

$$
e_i
=
(x_i,y_i,t_i,p_i),
$$

其中 $x_i,y_i$ 是像素位置，$t_i$ 是触发时间，$p_i \in \{-1,+1\}$ 是亮度变化极性。静态场景即使没有明显变化，APS 仍可输出图像；事件相机像素只有在亮度变化超过阈值时才触发 event。

Event frame 不是 APS frame。它通常是算法把一个时间窗口内的离散 events 累积、投影或编码为规则 tensor，以便 CNN、UNet 或 STN 处理。REDIR 没有说明具体采用 event count map、polarity-separated map、voxel grid 还是其他表示：`Needs further check`。

#### 3. 公式 $P_n^{\mathrm{ref}}=K R_n K^{-1}P_n+K T_n/d$ 为什么成立？它是普适结论吗？

它不是任意三维场景中的普适二维映射，而是针孔相机几何在若干假设下的简化。

设同一三维点在当前相机坐标系中的坐标为：

$$
X_n
=
\begin{bmatrix}
X_n\\
Y_n\\
Z_n
\end{bmatrix}.
$$

若从当前相机坐标系到参考相机坐标系的相对位姿为 $R_{\mathrm{rel}},T_{\mathrm{rel}}$，则刚体坐标变换为：

$$
X_{\mathrm{ref}}
=
R_{\mathrm{rel}}X_n
+
T_{\mathrm{rel}}.
$$

其中 $R_{\mathrm{rel}}$ 改变坐标轴方向，$T_{\mathrm{rel}}$ 改变坐标系原点。参考相机将该三维点投影到图像平面：

$$
\lambda_{\mathrm{ref}}
\widetilde P_n^{\mathrm{ref}}
=
K_{\mathrm{ref}}X_{\mathrm{ref}}
=
K_{\mathrm{ref}}
\left(
R_{\mathrm{rel}}X_n
+
T_{\mathrm{rel}}
\right).
$$

当前图像中的齐次像素坐标满足：

$$
X_n
=
Z_n K_n^{-1}\widetilde P_n.
$$

代入可得：

$$
\widetilde P_n^{\mathrm{ref}}
\sim
K_{\mathrm{ref}}
R_{\mathrm{rel}}
K_n^{-1}
\widetilde P_n
+
\frac{
K_{\mathrm{ref}}T_{\mathrm{rel}}
}{
Z_n
}.
$$

若进一步假设当前相机和参考相机内参相同：

$$
K_n
=
K_{\mathrm{ref}}
=
K,
$$

并把目标深度近似为统一常数：

$$
Z_n
\approx
d,
$$

便得到论文公式（4）的形式。论文还省略了齐次比例关系、最终归一化以及 $R_n,T_n$ 是否是相对位姿等说明。

对一般三维场景，单个二维矩阵通常不能严格对齐所有深度。只有在场景近似平面、相机纯旋转、目标很远或视角变化较小时，统一 homography 或 affine approximation 才较合理。

#### 4. 什么是齐次坐标？为什么最终要除以第三个坐标？

三维点经过内参投影后，可能得到齐次像素坐标：

$$
\widetilde P
=
\begin{bmatrix}
\widetilde u\\
\widetilde v\\
\widetilde w
\end{bmatrix}.
$$

它不是最终的普通二维像素坐标。需要做 dehomogenization：

$$
u
=
\frac{\widetilde u}{\widetilde w},
\qquad
v
=
\frac{\widetilde v}{\widetilde w}.
$$

例如：

$$
\widetilde P
=
\begin{bmatrix}
640\\
360\\
2
\end{bmatrix}
$$

对应的实际像素位置是：

$$
u
=
\frac{640}{2}
=
320,
\qquad
v
=
\frac{360}{2}
=
180.
$$

在齐次坐标中：

$$
\begin{bmatrix}
320\\
180\\
1
\end{bmatrix},
\qquad
\begin{bmatrix}
640\\
360\\
2
\end{bmatrix},
\qquad
\begin{bmatrix}
960\\
540\\
3
\end{bmatrix}
$$

表示同一个二维点，因为三个向量只相差一个非零比例因子。除以第三个分量，就是将其恢复为第三维等于 1 的普通欧氏坐标。

#### 5. “目标近似位于固定深度平面”合理吗？真实物体不是有厚度吗？

真实目标通常有厚度，不可能所有点严格处于同一深度。因此，单一深度 $d$ 只是 focus-plane approximation，而不是物理真值。

若目标距离相机约为 $20$ m，目标前后厚度约为 $0.5$ m，则相对深度变化为：

$$
\frac{0.5}{20}
=
2.5\%.
$$

在相机基线较小、目标较远或只处理局部区域时，可以把主要目标近似为一个平面。但若目标前表面深度为 $d_1$、后表面深度为 $d_2$，相机平移导致的像素位移分别近似与：

$$
\frac{T}{d_1},
\qquad
\frac{T}{d_2}
$$

有关。只要 $d_1 \neq d_2$，同一个矩阵就不能同时精确对齐两者，结果可能出现局部重影、边缘模糊或残余失焦。

E-SAI 仍采用目标主深度，是因为它只希望主要目标平面重合，而让另一深度的前景遮挡物保持分散。例如：

$$
d_{\mathrm{target}}
=
10\ \mathrm m,
\qquad
d_{\mathrm{occluder}}
=
2\ \mathrm m.
$$

按 $10$ m 对齐时，目标趋于重合，遮挡物仍错位。这正是 synthetic aperture de-occlusion 的基础。若要严格处理目标自身的三维厚度，需要 depth map、multi-plane model、dense optical flow、piecewise homography 或 deformable registration。REDIR 的多尺度 STN 可能缓解部分残余误差，但不能等同于显式三维几何对齐。

#### 6. 仿射矩阵 $\psi$ 是做什么的？它和公式（4）是什么关系？

公式（4）从物理相机几何出发，说明相机内参、相对旋转、相对平移和目标深度如何共同决定像素位置变化：

$$
(K,R,T,d)
\rightarrow
P_n^{\mathrm{ref}}.
$$

REDIR 并不显式求解这些物理量，而是让 STN 直接预测一个二维变换矩阵 $\psi_t$，再作用于 event frame 或 feature map：

$$
E_t
\xrightarrow{\operatorname{STN}}
\psi_t
\xrightarrow{\operatorname{TF}}
E_t'.
$$

因此，公式（4）给出物理几何动机，公式（5）的 $\psi$ 给出网络中可以直接执行的二维近似。预测出的 $\psi_t$ 只需有利于降低最终 reconstruction loss，不一定对应真实相机的 $R,T,d$。

论文写出的 $\psi$ 为：

$$
\psi
=
\begin{bmatrix}
\frac{\cos\theta}{k} &
\frac{\sin\theta}{k} &
\Delta x \\
-\frac{\sin\theta}{k} &
\frac{\cos\theta}{k} &
\Delta y
\end{bmatrix}.
$$

它包含 rotation、uniform scaling 和 translation，只有 $\theta,k,\Delta x,\Delta y$ 四个独立参数。一般二维 affine matrix 应为：

$$
\psi_{\mathrm{aff}}
=
\begin{bmatrix}
a_{11} &
a_{12} &
t_x \\
a_{21} &
a_{22} &
t_y
\end{bmatrix},
$$

六个元素可独立变化，还能表示 non-uniform scaling 和 shear。论文把公式（5）称为 affine matrix，并在后文声称 six-degree-of-freedom transformation，二者不完全一致：`Needs further check`。

#### 7. STN 是什么？$\psi_{0,t}=\operatorname{STN}(E_t)$ 如何预测？

STN 是 Spatial Transformer Network。它不是一个固定公式，而是一个可学习的 spatial-parameter predictor。标准 STN 通常包括：

1. localization network：从输入 $E_t$ 中提取描述位置、旋转、缩放和形变的 feature；
2. parameter regression head：通过 MLP 或 fully connected layers 输出变换参数；
3. grid generator 和 sampler：根据参数执行实际变换。

概念上：

$$
z_t
=
f_{\mathrm{loc}}(E_t),
$$

$$
\theta_t
=
f_{\mathrm{reg}}(z_t),
$$

然后将 $\theta_t$ reshape 或构造成：

$$
\psi_t
=
\begin{bmatrix}
a_{11} &
a_{12} &
t_x \\
a_{21} &
a_{22} &
t_y
\end{bmatrix}.
$$

如果严格按照论文公式（5），regression head 也可能输出：

$$
\theta_t,
\qquad
k_t,
\qquad
\Delta x_t,
\qquad
\Delta y_t,
$$

再构造受约束矩阵。但本文到底采用四参数 similarity transform，还是六参数 general affine transform：`Needs further check`。

STN 也需要知道“对齐到哪里”。从架构看，它可能通过训练将所有 timestamp 映射到一个学习到的统一参考坐标系，但论文没有说明 reference timestamp、reference frame 或 canonical coordinate 的具体定义：`Needs further check`。

#### 8. TF 是什么？为什么先得到 source coordinates？

TF 是 Spatial Transformation Function，即真正执行空间变换的 differentiable sampler。它的目标是从未对齐输入 $E_t$ 生成对齐输出 $E_t'$：

$$
E_t'
=
\operatorname{TF}(E_t,\psi_t).
$$

对于输出图中的每个位置：

$$
(x^{\mathrm{out}},y^{\mathrm{out}}),
$$

TF 不直接把输入像素向前“扔”到输出，而是先计算：

$$
\begin{bmatrix}
x^{\mathrm{src}}\\
y^{\mathrm{src}}
\end{bmatrix}
=
\psi_t
\begin{bmatrix}
x^{\mathrm{out}}\\
y^{\mathrm{out}}\\
1
\end{bmatrix}.
$$

该 source coordinate 表示：

> 为了生成输出位置 $(x^{\mathrm{out}},y^{\mathrm{out}})$ 的值，应该去输入 $E_t$ 的哪个位置取值。

随后执行：

$$
E_t'
(x^{\mathrm{out}},y^{\mathrm{out}})
=
E_t
(x^{\mathrm{src}},y^{\mathrm{src}}).
$$

之所以采用 output-to-input inverse sampling，是因为 forward mapping 容易出现两个问题：某些输出位置没有输入像素落入而形成空洞；多个输入像素可能同时落到一个输出位置而发生冲突。Inverse sampling 为每个输出位置指定明确来源。

#### 9. Source coordinate 不是整数时怎么办？Bilinear interpolation 如何工作？

若：

$$
x^{\mathrm{src}}
=
10.3,
\qquad
y^{\mathrm{src}}
=
5.7,
$$

输入 feature map 中不存在该整数像素。TF 通常利用周围四个位置：

$$
(10,5),
\qquad
(11,5),
\qquad
(10,6),
\qquad
(11,6)
$$

做 bilinear interpolation。

水平方向上，$10.3$ 距离 10 为 0.3、距离 11 为 0.7，因此对 $x=10$ 和 $x=11$ 的权重分别为 0.7 与 0.3。竖直方向上，$5.7$ 对 $y=5$ 和 $y=6$ 的权重分别为 0.3 与 0.7。最终：

$$
\begin{aligned}
E_t'
(x^{\mathrm{out}},y^{\mathrm{out}})
={}&
0.7 \times 0.3\,E_t(10,5)\\
&+
0.3 \times 0.3\,E_t(11,5)\\
&+
0.7 \times 0.7\,E_t(10,6)\\
&+
0.3 \times 0.7\,E_t(11,6).
\end{aligned}
$$

所以 TF 的完整流程是：

$$
\text{output coordinate}
\rightarrow
\text{source coordinate}
\rightarrow
\text{neighboring input values}
\rightarrow
\text{bilinear interpolation}
\rightarrow
\text{aligned output}.
$$

#### 10. TF 为什么可优化？重建损失如何更新 STN？

关键是 bilinear interpolation 对 source coordinate 是分段连续可微的，而 source coordinate 又是 $\psi_t$ 的函数。

一维情况下，若 $x^{\mathrm{src}} \in [i,i+1]$，插值结果为：

$$
y
=
(1-\alpha)x_i
+
\alpha x_{i+1},
$$

其中：

$$
\alpha
=
x^{\mathrm{src}}-i.
$$

则：

$$
\frac{\partial y}
{\partial x^{\mathrm{src}}}
=
-x_i+x_{i+1}.
$$

只要相邻输入值不完全相同，该导数通常不为零。另一方面：

$$
x^{\mathrm{src}}
=
a_{11}x^{\mathrm{out}}
+
a_{12}y^{\mathrm{out}}
+
t_x,
$$

因此：

$$
\frac{\partial x^{\mathrm{src}}}{\partial t_x}
=
1,
\qquad
\frac{\partial x^{\mathrm{src}}}{\partial a_{11}}
=
x^{\mathrm{out}},
\qquad
\frac{\partial x^{\mathrm{src}}}{\partial a_{12}}
=
y^{\mathrm{out}}.
$$

最终 reconstruction loss 可以通过链式法则传回变换矩阵：

$$
\frac{\partial\mathcal L}{\partial\psi_t}
=
\frac{\partial\mathcal L}{\partial E_t'}
\frac{\partial E_t'}
{\partial(x^{\mathrm{src}},y^{\mathrm{src}})}
\frac{\partial(x^{\mathrm{src}},y^{\mathrm{src}})}
{\partial\psi_t},
$$

再传回 STN parameters：

$$
\frac{\partial\mathcal L}
{\partial\theta_{\mathrm{STN}}}
=
\frac{\partial\mathcal L}{\partial\psi_t}
\frac{\partial\psi_t}
{\partial\theta_{\mathrm{STN}}}.
$$

因此，模型不必为每个样本提供真实 rotation、translation 或 affine matrix 标签。若当前 $\psi_t$ 使目标仍然错位，最终重建图像会更模糊，loss 较大；gradient descent 会推动 STN 输出更有利于目标重合的矩阵。

本文未报告独立 registration loss 或 affine-label supervision，因此该监督路径是根据网络和 loss 结构作出的合理推断：`Needs further check`。

Nearest-neighbor sampling 不适合这种优化，因为坐标在小范围内变化时，采样结果常保持不变，梯度大部分为零；bilinear interpolation 则使坐标微调能够连续改变输出。

#### 11. TSA-SNN 在哪里？为什么网络图中不明显？

REDIR 的整体结构为：

$$
\text{ANN registration}
+
\text{SNN filtering}
+
\text{CNN reconstruction}.
$$

SNN 位于 registration module 和 CNN decoder 之间。Fig. 2 中间的多个蓝色模块标为 `TSA SNN`，并沿 timestamp 方向显示 `State Update`；Fig. 4 中三个 `S-Conv` 对应论文所说的三层 spiking neural layers。

因此，SNN 不是最终图像输出模块，而是中间 filtering module。最终 reconstruction image 仍由 CNN decoder 生成，所以 REDIR 是 hybrid ANN–SNN，而不是 fully spiking network。

论文没有定义 S-Conv 内部究竟是：

$$
\operatorname{Conv}
\rightarrow
\operatorname{LIF},
$$

还是还包含 normalization、threshold 和其他操作：`Needs further check`。

#### 12. PMCM 到底如何工作？

根据正文和 Fig. 2，PMCM 是 registration encoder 与 reconstruction decoder 之间的多尺度双分支 connection。

设 registration module 输出已对齐 feature：

$$
F
\in
\mathbb R^{C \times H \times W}.
$$

第一条分支不使用 mask，保留完整配准信息：

$$
Y_{\mathrm{base}}
=
\operatorname{Conv}_{3 \times 3}(F).
$$

第二条分支利用 mask $M$ 强调目标并抑制遮挡：

$$
Y_{\mathrm{mask}}
=
\operatorname{Conv}_{3 \times 3}
\left(
M \odot F
\right).
$$

两条路径相加：

$$
Y
=
Y_{\mathrm{base}}
+
Y_{\mathrm{mask}}.
$$

若目标位置的 mask 接近 1，该位置特征会在第二条分支中被增强；若遮挡位置的 mask 接近 0，该位置会被削弱。保留未掩膜分支的原因是：若 mask 错误地将目标区域判为遮挡，完整分支仍可保留原始信息，避免目标特征被不可逆删除。

Fig. 2 中多个 PMCM 分别连接不同尺度的 registration features 与对应 CNN decoder，类似经过门控的 UNet skip connections。因此，它同时承担：

- multi-scale feature transmission；
- target-feature enhancement；
- registration 与 reconstruction 之间的信息融合。

论文没有说明 mask 由哪个模块产生、是 binary 还是 soft、是否使用 sigmoid、是否有 mask supervision、是否按 timestamp 或 scale 分别生成，以及 “perceptual” 与 perceptual loss 是否直接相关：`Needs further check`。

#### 13. 三个 loss 分别是干什么的？

Pixel loss：

$$
\mathcal L_{\mathrm{pix}}
=
\frac{
\left\|
\Phi-\hat{\Phi}
\right\|_1
}{
CHW
}
$$

逐像素比较重建图像 $\Phi$ 与 ground truth $\hat{\Phi}$，保证位置、亮度和局部细节在数值上接近。它防止输出只在视觉上“像目标”，但对应像素值偏差很大。单独使用 pixel loss 时，模型可能倾向于生成较平滑、偏模糊的平均结果。

Perceptual loss：

$$
\mathcal L_{\mathrm{per}}
=
\sum_k
\frac{\lambda_k}{C_kH_kW_k}
\left\|
\Phi_k-\hat{\Phi}_k
\right\|_2^2
$$

先通过卷积 feature extractor 得到第 $k$ 层特征，再比较输出和 GT 的 feature maps。浅层通常更关注边缘、纹理和局部轮廓，深层通常更关注形状和高层结构。它用于保证重建目标的轮廓和视觉结构相似，而不只追求逐像素平均。

Total variation loss：

$$
\mathcal L_{\mathrm{tv}}
=
\sum_{i,j}
\sqrt{
(\phi_{i,j+1}-\phi_{i,j})^2
+
(\phi_{i+1,j}-\phi_{i,j})^2
}
$$

惩罚相邻像素之间不必要的剧烈跳变，用于抑制孤立噪点、条纹、棋盘格和局部振荡，使平坦区域更加平滑。其权重过大时也可能抹掉真实边缘。

三者的分工可概括为：

$$
\mathcal L_{\mathrm{pix}}
:
\text{pixel fidelity},
$$

$$
\mathcal L_{\mathrm{per}}
:
\text{perceptual structure},
$$

$$
\mathcal L_{\mathrm{tv}}
:
\text{spatial smoothness}.
$$

论文没有说明 perceptual feature extractor、使用层和三个 $\beta$ 的数值：`Needs further check`。

#### 14. “不需要 prior information”到底是什么意思？其他方法是否需要？

这里的 prior information 特指 registration/refocusing 所需的外部采集信息或人工处理结果，例如：

- focal length；
- moving speed；
- depth of field；
- camera motion path 或 motion-compensation parameters；
- 人工 refocusing；
- 使用 manual-refocused/focused E-SAI dataset 进行预训练。

REDIR 通过：

$$
\psi_t
=
\operatorname{STN}(E_t)
$$

直接从输入数据预测二维 warp，因此在推理时不显式输入 $K,R,T,d$，也不要求先人工生成 focused event data。

“不需要 prior information”不等于：

- 不需要 training data；
- 不需要无遮挡 ground truth；
- 不需要 supervised loss；
- 不进行 registration；
- 完全不使用任务结构先验。

Table 1 中，FSAI+ACC 和 Refocus+Hybrid 被标为需要 prior information；FSAI+CNN、Hybrid 和 REDIR 被标为不需要。因此 REDIR 不是唯一 prior-free method。其主要特点是：在 prior-free 条件下仍显式学习 timestamp-wise registration，而 Hybrid 缺少有效 alignment，直接累积时容易产生严重错位。

### Additional Technical Details

#### 目标—遮挡光强差与事件响应

论文给出：

$$
\left|E_{OA}(n)\right|
\propto
\left|
\Gamma_A(n)
-
\Gamma_O(n)
\right|.
$$

其中：

- $\Gamma_A(n)$：目标区域的光强；
- $\Gamma_O(n)$：遮挡物区域的光强；
- $\left|E_{OA}(n)\right|$：与目标—遮挡关系有关的事件数量、事件幅度或响应强度。

其核心直觉是：目标和遮挡物之间的光强差越大，在相机运动导致目标边界与遮挡边界相互穿越、显露或再次遮挡时，像素经历的亮度变化越大，因此更容易超过事件触发阈值并产生明显 event response。

低对比度例子：

$$
\Gamma_A
=
0.50,
\qquad
\Gamma_O
=
0.45,
$$

则：

$$
\left|
\Gamma_A-\Gamma_O
\right|
=
0.05.
$$

目标与遮挡物外观接近，边界穿越引起的亮度变化较弱，可能只产生较少或较弱的事件。

高对比度例子：

$$
\Gamma_A
=
0.90,
\qquad
\Gamma_O
=
0.20,
$$

则：

$$
\left|
\Gamma_A-\Gamma_O
\right|
=
0.70.
$$

目标和遮挡物差异较大，边界变化更容易触发大量事件。

但该式只是定性或简化正比关系，不是完整事件生成方程。实际事件响应还会受以下因素影响：

- contrast threshold；
- 相机速度和运动方向；
- 目标边缘方向；
- event accumulation window；
- pixel refractory behavior；
- sensor noise；
- 是否使用 log intensity。

此外，论文没有严格定义 $E_{OA}(n)$ 是一个 event set、event count、event-frame intensity，还是某种连续 feature magnitude。因此不能将该公式理解成可直接用于精确计算事件数量的确定性方程：`Needs further check`。

### Personal Reflections

这篇论文整体较为一般。其主要价值是为综述补充一种 SNN 的具体使用场景：在 E-SAI 去遮挡重建系统中，将 SNN 用作 registration 后的 temporal filtering module。方法本身主要由 STN、UNet、attention SNN、mask connection 和 CNN decoder 组合而成，SNN 机制与实验分析都不够深入。

因此，在综述中可以简要介绍其任务设定、hybrid architecture 和 prior-free registration 思路，用来说明 event-based de-occlusion 这一应用方向；没有必要作为核心论文展开过多技术细节。
