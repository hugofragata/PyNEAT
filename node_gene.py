
NODE_GENE_TYPES = ["input", "output", "hidden", "bias"]

class NodeGene():

    def __init__(self, gene_id):
        """Node genes provide a
        list of inputs, hidden nodes,
        and outputs that can be connected.(Ken&Risto)"""
        self.type = None
        self.gene_id = gene_id

        #TODO: make this not hardcoded
        self.bias = 0.001
        self.response = 0.5

    def something(self, arg):
        pass

class NodeGeneError:
    def __init__(self, a):
        print("NODE_GENE ERROR: " + str(a))
        pass