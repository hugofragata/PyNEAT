import random
class ConnectionGene():
    def __init__(self, in_node, out_node, weight=1, enable=True, innovation=1):
        """Each connection gene
        specifies the in-node,
        the out-node,
        the weight of the connection,
        whether or not the connection gene is expressed,
        and an innovation number [...](Ken&Risto)"""
        self.in_node = in_node
        self.out_node = out_node
        self.weight = weight
        self.enable = enable
        self.innovation = innovation

    def mutate(self):
        if random.random() > 0.5:
            self.weight = self.weight * random.uniform(0,2)
        else:
            self.enable = not self.enable

def reproduce(conn_gene_A, conn_gene_B):
    id = conn_gene_A.innovation
    in_node = random.choice([conn_gene_A.in_node, conn_gene_B.in_node])
    out_node = random.choice([conn_gene_A.out_node, conn_gene_B.outnode])
    weight = (conn_gene_B.weight + conn_gene_A.weight) / 2
    en = random.choice([conn_gene_A.enable, conn_gene_B.enable])
    child = ConnectionGene(in_node, out_node, weight, en, id)
    return child

class ConnectionGeneError:
    def __init__(self, a):
        print("CONNECTION_GENE ERROR: " + str(a))
        pass