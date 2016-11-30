from genome import Genome
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


class NeuralNetworkError():
    def __init__(self, a):
        print("NEURAL_NETWORK ERROR: "+str(a))
        pass