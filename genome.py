import abc
from node_gene import NodeGene
from connection_gene import ConnectionGene

MUTATION_TYPES = ["add_node", "remove_node", "add_connection", "remove_connection"]

class Genome():
    def __init__(self):
        """Each genome includes a
        list of connection genes,
        each of which refers to
        two node genes being connected.(Ken&Risto)"""
        self.connection_genes = []

        self.mutation_threshold = None


    def mutation(self, threshold, mutation_type):
        if mutation_type not in MUTATION_TYPES:
            raise GenomeError("mutation type not supported")
        if threshold < self.mutation_threshold:
            return
        if mutation_type == "add_node":
            self.mutate_add_node()
        elif mutation_type == "remove_node":
            self.mutate_remove_node()
        elif mutation_type == "add_connection":
            self.mutate_add_connection()
        elif mutation_type == "remove_connection":
            self.mutate_remove_connection()
        else:
            raise GenomeError("something wrong happened in mutation.")

    def mutate_add_node(self):
        """In the add node mutation, an existing connection is
        split and the new node placed where the old connection used to be.
        The old connection is disabled and two new connections are added to the genome.
        The new connection leading into the new node receives a weight of 1,
        and the new connection leading out receives the same weight as the old connection. """
        pass

    def mutate_remove_node(self):
        pass

    def mutate_add_connection(self):
        """In the add connection mutation,
        a single new connection gene with a random weight is added
        connecting two previously unconnected nodes."""
        pass

    def mutate_remove_connection(self):
        pass


class GenomeError():
    def __init__(self, a):
        print("GENOME ERROR: "+str(a))
        pass