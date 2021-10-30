# MicroModelNetwork

This experimental network is composed of highly modular, single-node "micro-models". Each micromodel node volunteers a prediction and an estimation of certainty when given input. These predictions can be put through a weighted average to derive a final answer. Right now, output is constrained to simple probabilities.

Hypotheses:

1. A MicroModelNetwork can learn everything a convolutional neural-network can.
2. Knowledge learned by two MicroModelNetworks can be combined simply by concatenating their nodes into a new network.
3. The nodes responsible for undesirable behaviors in a model can be easily identified. The undesirable behaviors can be removed without appreciably affecting the rest of the model's behavior simply by removing these nodes from the model.
5. A MicroModelNetwork requires much more computation to train than other deep-learning models as many more nodes are required to train it.
