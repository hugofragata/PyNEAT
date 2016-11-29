import numpy

class NeuralNetwork():
    def __init__(self, max_node, inputs, outputs, node_evals):
        self.node_evals = node_evals
        self.input_nodes = inputs
        self.output_nodes = outputs
        self.values = [0.0] * (1 + max_node)
        self.num_nodes = 1 + max_node

    def activate(self, inputs):
        pass