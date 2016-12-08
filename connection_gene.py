class ConnectionGene():
    def __init__(self):
        """Each connection gene
        specifies the in-node,
        the out-node,
        the weight of the connection,
        whether or not the connection gene is expressed,
        and an innovation number [...](Ken&Risto)"""
        self.in_node = None
        self.out_node = None
        self.connection_weight = 0.0
        self.enable = False
        self.innovation_id = None

class ConnectionGeneError:
    def __init__(self, a):
        print("CONNECTION_GENE ERROR: " + str(a))
        pass