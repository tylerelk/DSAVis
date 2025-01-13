'''
This file represents a queue. A queue is a list that allows only insertion at the head and deletion at the tail.
Methods to add data insert as the first element in the list, and methods to delete data remove from the tail
of the list and return the removed data.

This file will allow users to:
    - Create a queue
    - Print values in the queue to the console
    - Export the queue to Flask
    - Insert values at the end of the list
    - Remove and return values from the beginning of the list

Analysis:
    - Inserting is O(1)
    - Removing is O(1)
    - Retrieving is O(n), since we traverse the list
'''
class Queue:
    def __init__(self):
        self.list = []
        self.head = None
        self.tail = None

    def enqueue(self, value):
        self.list.append(value)

    def dequeue(self):
        if len(self.list) > 1:
            result = self.list[0]
            del self.list[0]
            return result
        print("List is empty")
        return -1
    
    def print(self):
        for val in self.list:
            print(val)
    
    def export(self):
        vals = []
        for val in self.list:
            vals.append(val)
        return vals