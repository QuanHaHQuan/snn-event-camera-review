# Survey Outline

## Working Title

Spiking Neural Networks for Event Cameras

## Draft Structure

The survey should use **parallel foundations plus an explicit intersection chapter**. Event representation is not a subcategory of SNN, and SNN is not a subcategory of event representation. They are two independent axes that meet in the SNN-for-event-camera literature.

The chapter order is therefore not a nested taxonomy. Chapters 2 and 3 define the two axes independently; Chapter 4 studies their combinations; Chapter 5 compares those combinations across tasks; Chapter 6 synthesizes the evidence. A paper can appear in more than one cross-cutting table, but it should not be treated as a new category every time it crosses an axis.

1. Introduction and scope
   - Define event cameras, SNNs, and the strict intersection.
   - State the survey question: how do event representations and SNN computation interact?
   - Explain the two-axis taxonomy and prevent broad event-based-vision drift.

2. Event-camera representations: the sensor-side axis
   - Raw asynchronous event stream and event tuple semantics.
   - Dense representations: event frames, accumulation, voxel grids, stacked histograms.
   - Sparse representations: point/Event Cloud, time surfaces, graphs, event-by-event processing.
   - Learned/adaptive representations: slicing, sampling, polarity-aware and, where the transformation is applied to the event signal itself, frequency-aware representations.
   - Comparison dimensions: sparsity, temporal precision, spatial completeness, memory, latency, and information loss.

3. Spiking neural networks: the computation-side axis
   - Spike coding, neuron state, membrane dynamics, reset, and temporal simulation.
   - Efficiency axis: sparse activation, addition-only computation, conversion, hybrid ANN-SNN, latency, energy, and hardware evidence.
   - Temporal axis: short-term dynamics, long-range state/memory, delay, temporal credit assignment, and timestep flexibility.
   - Training axis: surrogate gradient, BPTT/online learning, distillation, and stability.

4. SNN for Event Cameras: the intersection axis
   - Event-to-spike interfaces: raw events, event tuples, time surfaces, and discretized event tensors.
   - Dense representation x SNN mechanism: voxel/frame inputs with fully spiking, hybrid, or converted networks.
   - Sparse representation x SNN mechanism: point/Event Cloud, event-by-event, and graph inputs with spiking processing.
   - SNN-controlled event sampling, slicing, aggregation, or memory updates.
   - For each family, ask the same questions: what is represented, what is spiking, where is temporal state kept, and what evidence supports the efficiency claim.
   - Keep frequency, wavelet, and SSM/Mamba methods as mechanisms that may cross both axes; do not create a separate representation chapter for every mechanism.

5. Tasks and empirical evidence across the intersection
   - Recognition and action classification.
   - Object detection.
   - Tracking.
   - Reconstruction/restoration.
   - Pose, depth, flow, and segmentation.
   - Cross-task comparison of accuracy, timestep, latency, energy, and hardware measurement.
   - Treat tasks as an evidence-organizing axis, not as a replacement for the representation/SNN taxonomy.

6. Two-axis synthesis and open problems
   - A matrix with event representation on one axis and SNN mechanism on the other.
   - Empty, weak, and well-supported cells in the matrix.
   - Representation–dynamics mismatch, event sparsity versus spatial completeness, long-term memory, frequency modeling, and reproducible efficiency claims.
   - Open problems for event representation, SNN computation, and their intersection separately.
