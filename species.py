from genome import Genome

class Species():

    def __init__(self):
        self.species_set = []
        self.tracker = InnovationTracker

    def separate_between_species(self, genomes):
        pass

class InnovationTracker():
    def __init__(self):
        self.id = 1

    def next_id(self):
        id = self.id
        self.id+=1
        return id

