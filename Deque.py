import time

#   An implementation of a deque
#       A deque (pronounced "cheque") is a double-ended queue
#       A data structure where data can be added and removed from both sides
#           A queue and a stack put together
#       HOWEVER, this deque can only have items added to the right
class Deque:
    def __init__(self, max_size):
        self.max_size = max_size
        self.arr = []


    #   Appends the item to the end of the queue
    #       Trims the list if there are too many items
    def push(self, item):
        self.arr.append(item)
        self.trim()

    #   If the current size of the list is greater than max_size, delete the oldest (leftmost) item
    def trim(self):
        if len(self.arr) > self.max_size:
            del self.arr[0]

    def pop(self):
        if not self.is_empty():
            return self.arr.pop(-1)

    def dequeue(self):
        if not self.is_empty():
            return self.arr.pop(0)

    def peek_left(self):
        if not self.is_empty():
            return self.arr[0]

    def peek_right(self):
        if not self.is_empty():
            return self.arr[-1]

    def size(self):
        return len(self.arr)

    def is_empty(self):
        return self.size() == 0


#   A stopwatch is used to keep track of time
#   It is a Stack-like data structure whose items are timestamps
#      The timestamps are measure in seconds
class Stopwatch(Deque):
    def __init__(self, max_size):
        Deque.__init__(self, max_size)

        #   A special time to keep note of
        #       Mostly for simplifying time since startup of program
        self.note = time.time_ns() / 1e9

    #   Pushes the current time in seconds (measured through nanos since the epoch) to the list
    #   Units are seconds (s)
    def push_time(self):
        self.push(time.time_ns() / 1e9)

    #   Returns the difference between the two most recent items
    def peek_delta(self):
        if self.size() >= 2:
            return self.arr[-1] - self.arr[-2]
        return -1

    #   Returns the difference in time since the last time was pushed
    def since(self):
        return (time.time_ns() / 1e9) - self.peek_right()

    def since_start(self):
        return (time.time_ns() / 1e9) - self.note


#   A Debugger holds prints statements that are print out
#       As a developer view sort of thing
#   Holds plenty of tags
#       These tags determine what is and isn't accepted into the debugger
class Debugger(Deque):
    def __init__(self):
        Deque.__init__(self, float("infinity"))
        self.tags = []

    #   Adds a tag to the tag list
    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def add_tags(self, tags):
        for tag in tags:
            self.add_tag(tag)

    #   Pushes an item to the Debugger
    #   Overrides Deque's push function
    #   Will only push if the tag matches and the Debugger is open
    def push(self, item, tag, open):
        if open and tag in self.tags:
            self.arr.append(item)

