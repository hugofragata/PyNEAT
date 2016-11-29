from genome import Genome

class Species():
    """The number of excess and disjoint genes between a pair of genomes is a natural
    measure of their compatibility distance. The more disjoint two genomes are, the less
    evolutionary history they share, and thus the less compatible they are. Therefore, we
    can measure the compatibility distance δ of different structures in NEAT as a simple linear
    combination of the number of excess E and disjoint D genes, as well as the average
    weight differences of matching genes W, including disabled genes:
    δ = c1E/N + c2D/N + c3·W (1)
    The coefficients c1, c2, and c3 allow us to adjust the importance of the three factors, and
    the factor N, the number of genes in the larger genome, normalizes for genome size (N
    can be set to 1 if both genomes are small, i.e., consist of fewer than 20 genes).
    The distance measure δ allows us to speciate using a compatibility threshold δt.
    An ordered list of species is maintained. In each generation, genomes are sequentially
    placed into species. Each existing species is represented by a random genome inside
    the species from the previous generation. A given genome g in the current generation is
    placed in the first species in which g is compatible with the representative genome of
    that species. This way, species do not overlap.1
    If g is not compatible with any existing
    species, a new species is created with g as its representative.(stanley)"""

    def __init__(self, species_id, representative):
        self.id = species_id
        if not type(representative) == Genome:
            raise SpeciesError("Representative provided is not a Genome but it should be.")
        self.representative = representative
        self.average_fitness = 0.0
        self.max_fitness = 0.0
        self.max_fitness_ever = 0.0
        self.members = [representative]

class SpeciesError:
    def __init__(self, a):
        print("SPECIES ERROR: " + str(a))
        pass

