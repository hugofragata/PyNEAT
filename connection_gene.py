from node_gene import NodeGene

class ConnectionGene():
    def __init__(self):
        """Each connection gene
        specifies the in-node,
        the out-node,
        the weight of the connection,
        whether or not the connection gene is expressed,
        and an innovation number [...](Ken&Risto)"""
        self.in_node = NodeGene()
        self.out_node = NodeGene()
        self.connection_weight = 0.0
        self.enable = False
        self.innovation_id = 1

