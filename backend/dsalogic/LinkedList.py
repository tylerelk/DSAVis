'''
This is a simple linked list. The class Node is made up of an integer value and a pointer to the next Node.
If Node.next is null, we've reached the end of the linked list.

The file allows users to do the following:
    - Create a linked list from a single value
    - Add to the linked list from either the start or end
    - Insert into the linked list after a specified value
    - Delete from the linked list based on value
    - Display the linked list

Analysis:
    - Inserting at the tail is O(n), since you have to traverse the list to find the tail
    - Inserting at the head is O(1)
    - Inserting in the middle is O(n), since you need to traverse the list to find the search term
    - Deleting is O(n) for the same reason as middle-insertion
    - Reading is O(n) for the same reason as deleting and middle-insertion
    - Space complexity for the structure is O(n), where n is the number of nodes in the list
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode

    def prepend(self, value):
        newNode = Node(value)
        tmp = self.head
        self.head = newNode
        newNode.next = tmp

    def insert(self, value, term):
        current = self.head
        while current.value is not term:
            current = current.next
        if current is None:
            return "Insertion point not found"
        else:
            newNode = Node(value)
            tmp = current.next
            current.next = newNode
            newNode.next = tmp

    def delete(self, term):
        current = self.head
        if current.value == term:
            self.head = current.next
            return
        else:
            prev = None
            while current is not None and current.value != term:
                prev = current
                current = current.next
            if current is None:
                return "Cannot delete: term not found"
            prev.next = current.next
    
    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    
    #This method used for jsonify only; increases space complexity to return Flask-friendly json
    def export(self):
        current = self.head
        vals = []
        while current:
            vals.append({'value': current.value, 'next': current.next is not None})
            current = current.next
        return vals