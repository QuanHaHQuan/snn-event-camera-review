# SECNet-SNN Advisor Reselection

Date: 2026-09-10
Status: user-confirmed; semantic source and generated views synchronized

## Decision

The Advisor direction now asks how to implement SECNet as an accurate, trainable, and deployable SNN while preserving its ordered Event Cloud hierarchy. SECNet remains the focus paper. Frequency/Fourier modules remain part of the baseline architecture but no longer determine Core admission.

The confirmed eight-paper set is:

- required: SpikePoint; Spiking Discrepancy Transformer; Spike-driven Discrete Aggregation; STEP; CLIF; Temporal Interaction in Spiking Transformers with Multi-Delay Mixer;
- helpful: Rethinking SNN Online Training and Deployment (HD-LIF); SMixer.

The previous frequency-centered required/helpful assignments were returned to retained-reference status. Their audit evidence and existing V2 files remain preserved.

## Semantic policy change

Advisor retrieval and reading now classify evidence by event-to-spike interface, point/Event Cloud hierarchy, neuron dynamics, SNN architecture, temporal modeling, training, efficiency, and deployment. Frequency and Fourier remain controlled topics for historical and baseline analysis rather than enrollment criteria.

## Regeneration

After the audit update, regenerate the selection views and V2 indexes with the maintained scripts, then run the literature-graph validator and `git diff --check`. No commit or push is part of this reselection.
