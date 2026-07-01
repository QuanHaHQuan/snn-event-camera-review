---
title: "Towards Reliable Evaluation of Adversarial Robustness for Spiking Neural Networks"
authors: ["Jihang Wang", "Dongcheng Zhao", "Ruolin Chen", "Qian Zhang", "Yi Zeng"]
conference: "CVPR"
year: 2026
level: "C"
category: "SNN"
pdf_link: "https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Towards_Reliable_Evaluation_of_Adversarial_Robustness_for_Spiking_Neural_Networks_CVPR_2026_paper.pdf"
official_page: "https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Towards_Reliable_Evaluation_of_Adversarial_Robustness_for_Spiking_Neural_Networks_CVPR_2026_paper.html"
tags: []
abstract: "Spiking Neural Networks (SNNs) utilize spike-based activations to mimic the brain's energy-efficient information processing. However, the binary and discontinuous nature of spike activations causes vanishing gradients, making adversarial robustness evaluation via gradient descent unreliable. While improved surrogate gradient methods have been proposed, their effectiveness under strong adversarial attacks remains unclear. We propose a more reliable framework for evaluating SNN adversarial robustness. We theoretically analyze the degree of gradient vanishing in surrogate gradients and introduce the Adaptive Sharpness Surrogate Gradient (ASSG), which adaptively evolves the shape of the surrogate function according to the input distribution during attack iterations, thereby enhancing gradient accuracy while mitigating gradient vanishing. In addition, we design an adversarial attack with adaptive step size under the L_infinity constraint--Stable Adaptive Projected Gradient Descent (SA-PGD), achieving faster and more stable convergence under imprecise gradients. Extensive experiments show that our approach substantially increases attack success rates across diverse adversarial training schemes, SNN architectures and neuron models, providing a more generalized and reliable evaluation of SNN adversarial robustness. The experimental results further reveal that the robustness of current SNNs has been significantly overestimated and highlighting the need for more dependable adversarial training methods. The code is released at https://github.com/craree/ASSG-SNNs-Robustness-Evaluation"
status: "auto-generated; brief scan note"
---

## Core Problem

SNN 的二值与不连续激活使梯度消失严重，导致对抗鲁棒性评估不稳定。

## Core Method

提出更可靠的评估框架，并设计 Adaptive Sharpness Surrogate Gradient 来缓解梯度消失。

## Key Metrics and Findings

摘要强调传统梯度下降式评估在强攻击下不够可靠。

## Personal Notes

适合放在 SNN 训练与评估方法部分。

