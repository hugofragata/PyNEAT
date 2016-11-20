"""Whenever a new gene appears (through structural mutation),
a global innovation number is incremented and assigned to that gene.
The innovation numbers thus represent a chronology of the appearance of every gene in the system.
As an example, let us say the two mutations in Figure 3 occurred one after another in the system.
The new connection gene created in the first mutation is assigned the number 7,
and the two new connection genes added during the new node mutation are assigned the numbers 8 and 9.
In the future, whenever these genomes mate,
the offspring will inherit the same innovation numbers on each gene; innovation numbers are never changed.
Thus, the historical origin of every gene in the system is known throughout evolution."""

class InnovationTracker():
    def __init__(self):
        self.id = 1

    def next_id(self):
        id = self.id
        self.id+=1
        return id

