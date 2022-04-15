#   A state stores the state of the universe at that time
#   Takes in all actors at that time and the time, and returns the state
#   Uses a Dictionary
#       index:  timestamp
#       column: list of actors

class State:
    def __init__(self):
        self.states = {}

    #   Adds the state, indexed by a timestamp
    def add(self, timestamp, actors):
        self.states[timestamp] = actors

    #   Retrieves a state by a timestamp
    def get(self, timestamp):
        return self.states[timestamp]

