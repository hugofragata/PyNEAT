from genome import Genome
import math
###
#THIS IS A FEED FORWARD NEURAL NET
###
class NeuralNetwork():
    def __init__(self, max_node, inputs, outputs, node_evals):
        self.node_evals = node_evals
        self.input_nodes = inputs
        self.output_nodes = outputs
        self.values = [0.0] * (1 + max_node)
        self.num_nodes = 1 + max_node

    def activate(self, inputs):
        pass

def create_phenotype(genome):
    if not type(genome) == Genome:
        raise NeuralNetworkError("To create a phenotype you need to pass an instance of Genome")

    input_nodes = [node_gene.ID for node_gene in genome.node_genes.values() if node_gene.type == 'input']
    output_nodes = [node_gene.ID for node_gene in genome.node_genes.values() if node_gene.type == 'output']
    connections = [(conn_gene.in_node_id, conn_gene.out_node_id) for conn_gene in genome.conn_genes.values() if conn_gene.enabled]

    layers = []

    checked_nodes_set = set(input_nodes)
    while True:
        next_layer_candidates_set = set(b for (a, b) in connections if a in checked_nodes_set and b not in checked_nodes_set)
        layer_set = set()
        for node in next_layer_candidates_set:
            if all(a in checked_nodes_set for (a, b) in connections if b == node):
                layer_set.add(node)

        if not layer_set:
            break

        layers.append(layer_set)
        checked_nodes_set = checked_nodes_set.union(layer_set)

    node_evals = []
    used_nodes = set(input_nodes + output_nodes)

    for layer in layers:
        for node_id in layer:
            inputs = []
            for conn_gene in genome.conn_genes.values():
                if conn_gene.out_node_id == node_id and conn_gene.enabled:
                    inputs.append( (conn_gene.in_node_id, conn_gene.connection_weight) )
                    used_nodes.add( conn_gene.in_node_id )

            used_nodes.add(node_id)
            node_gene = genome.node_genes[node_id]
            node_evals.append(NodeEval(node_id, math.sin, node_gene.bias, node_gene.response, inputs))

    return NeuralNetwork(max(used_nodes), input_nodes, output_nodes, node_evals)

class NodeEval():
    def __init__(self, node_id, trigger, bias, response, in_node_ids):
        self.node_id = node_id
        self.trigger = trigger
        self.bias = bias
        self.response = response
        self.in_node_ids = in_node_ids

class NeuralNetworkError():
    def __init__(self, a):
        print("NEURAL_NETWORK ERROR: "+str(a))
        pass