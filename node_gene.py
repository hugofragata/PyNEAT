
NODE_GENE_TYPES = ["input", "output", "hidden", "bias"]

class NodeGene():

    def __init__(self):
        """Node genes provide a
        list of inputs, hidden nodes,
        and outputs that can be connected.(Ken&Risto)"""
        self.inputs = []
        self.hidden_nodes = []
        self.output_nodes = []
        self.type = None

    def something(self, arg):
        pass