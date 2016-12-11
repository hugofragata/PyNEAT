import math, random
NODE_GENE_TYPES = ["input", "output", "hidden"]

class NodeGene():

    def __init__(self, gene_id, type="hidden", bias=0.01, response=1, trigger=None):
        """Node genes provide a
        list of inputs, hidden nodes,
        and outputs that can be connected.(Ken&Risto)"""
        self.type = type
        self.gene_id = gene_id
        self.bias = bias
        self.response = response
        if not trigger:
            triggers = Triggers()
            self.trigger = triggers.get_random_trigger()
        else:
            self.trigger = trigger

#TODO: mutation params must be configurable, as in a max value and a min value for changes in the gene's attributes
    def mutate(self):
        action = random.choice({'bias', 'response', 'trigger'})
        if action == 'bias':
            self.mutate_bias()
        elif action == 'response':
            self.mutate_response()
        else:
            self.mutate_trigger()

    def mutate_bias(self):
        self.bias = random.uniform(0.01, 0.1)

    def mutate_response(self):
        self.response = random.gauss(0.5 , 0.15)

    def mutate_trigger(self):
        trigs = Triggers()
        current_trigger = self.trigger
        self.trigger = trigs.get_random_trigger()
        while self.trigger == current_trigger:
            self.trigger = trigs.get_random_trigger()

def reproduce(node_gene_A, node_gene_B):
    '''
    Use this method to get children between two node genes.
    :param node_gene_A: A node gene
    :param node_gene_B: Another node gene
    :return: A child of them
    '''
    #Children get the node_id of their parents, which should be the same
    id = node_gene_A.node_id
    #The type should be the same for parents, which will be the children's type
    type = node_gene_A.type
    #The other node_gene attributes could be different for A and B
    #therefore, to produce children we must randomly choose between A and B for each attribute
    bias = random.choice([node_gene_A.bias, node_gene_B.bias])
    response = random.choice([node_gene_A.response, node_gene_B.response])
    trigger = random.choice([node_gene_A.trigger, node_gene_B.trigger])
    #init the child and return it
    child = NodeGene(id, type, bias, response, trigger)
    return child

class Triggers():
    def __init__(self):
        self.triggers = [self.cube_trigger, self.square_trigger, self.sin_trigger]

    def cube_trigger(self, a):
        return a**3

    def square_trigger(self, a):
        return a**2

    def sin_trigger(self, a):
        return math.sin(a)

    def get_random_trigger(self):
        return random.choice(self.triggers)

class NodeGeneError:
    def __init__(self, a):
        print("NODE_GENE ERROR: " + str(a))
        pass