#   A state stores the state of the universe at that time
#   Takes in all actors at that time and the time, and returns the state
#   Uses a Dictionary
#       index:  timestamp
#       column: list of actors

#   Yeah, this is pretty basic and can be greatly improved
#       Add a method to return the closest timestamp if no matches found
#       Clears all items listed before the current index
#           Would be far more efficient with list representations

import copy # Making deep copies _drastically_ slows things down

class State:
    def __init__(self):
        self.states = {}

    #   Adds the state, indexed by a timestamp
    def add(self, timestamp, actors):
        self.states[timestamp] = copy.deepcopy(actors)

    #   Retrieves a state by a timestamp
    def get(self, timestamp):
        try:
            return self.states[timestamp]
        except:
            return self.closest(timestamp)


    #   The current idea is to extract the keys and sort them
    #   Then do a binary search (?) to find the closest match
    #       If I want to make it even better, then I'll get the closest smaller match
    #       Then, I would simulate one step up to 'now'
    #           I might make it try to "snap" if the delta is small enough
    #           That way, if I simulate a 0.45 in between steps of 1, I don't have to resimulate even when its 1.05: just snap
    #    For now, just rounds to the nearest integer
    def closest(self, timestamp):
        closest_timestamp = int(round(timestamp))
        return self.states[closest_timestamp]



