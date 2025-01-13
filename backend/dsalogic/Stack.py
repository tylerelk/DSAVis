'''
This file lets users create a stack. A stack is a list in which data is both added and removed only from one end,
in this case we will use the last element of the list.

This file lets users:
    - Create a stack
    - Add to the top (tail) of the stack
    - Remove from the top (tail) of the stack and return the value found there
    - Print the stack to the console
    - Export the stack to Flask

Analysis:
    - Adding and removing from the stack are both O(1)
    - Printing the stack is O(n), as we have to traverse the stack
'''
class Stack:
    def __init__(self):
        self.list = []
        self.top = None

    def add(self, value):
        self.list.append(value)

    def remove(self):
        return self.list.pop()
    
    def print(self):
        for val in self.list:
            print(val)

    def export(self):
        vals = []
        for val in self.list:
            vals.append(val)
        return vals