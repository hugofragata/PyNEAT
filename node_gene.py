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