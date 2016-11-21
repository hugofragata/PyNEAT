from genome import Genome
from species import Species
from neural_network import NeuralNetwork
class Organism():
    def __init__(self):
        self.fitness = 0.0
        self.winner = False
        self.eliminate = False
        self.champion = False
        self.population_champ = False
        self.child_of_population_champ = False
        self.net = NeuralNetwork
        self.genome = Genome
        self.species = Species
        self.generation = 1
