'''
This file creates a doubly-linked list. This is similar to a linked list, except extra space
is allocated to preserve a pointer on each node to it's previous node in the list. If Node.next
is null, we are at the tail of the list; if Node.prev is null we are at the head. In a list
with only one element, the element is considered the head and the tail. In short, this structure sacrifices
space for speed.

The file will allow users to do the following:
    - Create a doubly-linked list
    - Insert at the head or tail of the list
    - Insert before or after a specific value
    - Delete from the list
    - Display the list in the console
    - Export the list in a Flask-friendly json format (increases space complexity)

Analysis:
    - Inserting at the head or tail is O(1)
    - Inserting in the middle is O(n), since we need to traverse the list to find the search term
    - Deleting is O(n), for the same reason as middle-insertion
    - Reading is O(n), for the same reason as middle-insertion and deletion
    - Space complexity for the structure is O(n), n being the number of nodes in the list
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class DblLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
        if not self.tail:
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
    
    def prepend(self, value):
        newNode = Node(value)
        if not self.tail:
            self.tail = newNode
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
    
    def insertBefore(self, value, term):
        current = self.head
        newNode = Node(value)
        while current:
            if current is self.head and self.head.value == term:
                self.head.prev = newNode
                newNode.next = self.head
                self.head = newNode
                return
            elif current.value == term:
                newNode.next = current
                newNode.prev = current.prev
                current.prev.next = newNode
                current.prev = newNode
                return
            else:
                current = current.next
        return "Cannot insert: term not found"
    
    def insertAfter(self, value, term):
        current = self.head
        newNode = Node(value)
        while current:
            if current is self.tail and self.tail.value == term:
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
                return
            elif current.value == term:
                newNode.prev = current
                newNode.next = current.next
                current.next.prev = newNode
                current.next = newNode
                return
            else:
                current = current.next
        return "Cannot insert: term not found"
    
    def delete(self, term):
        current = self.head
        while current:
            if current is self.head:
                self.head = current.next
                self.head.prev = None
                return
            elif current is self.tail:
                self.tail = current.prev
                self.tail.next = None
                return
            elif current.value == term:
                current.prev.next = current.next
                current.next.prev = current.prev
                return
            else:
                current = current.next
        return "Cannot delete: term not found"
    
    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def export(self):
        current = self.head
        vals = []
        while current:
            vals.append({
                'value': current.value,
                'next': current.next.value if current.next else None,
                'prev': current.prev.value if current.prev else None
                })
            current = current.next
        return vals