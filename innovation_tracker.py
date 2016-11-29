class InnovationTracker():
    def __init__(self):
        self.id = 1

    def next_id(self):
        id = self.id
        self.id+=1
        return id
