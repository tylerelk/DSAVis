'''
This file contains logic for a heap. A heap is a tree data structure that is arranged into either a min-heap or a max-heap. This implementation shows a
min-heap. In a heap, each node can have a left and a right child. To say that a node and/or it's associated children are "heapified" means that the tree is
complete, but not necessarily full. Elements are inserted into the bottom of the tree in the last position (reading left to right), then bubbled upwards
towards the root until they are smaller than any children they may have and larger than their parent. Similarly, when extracting the root node the very last
element in the tree is placed at the root, then bubbled downward to the leaves until it meets the rules of a min heap.

Mathematically, the following are always true in a heap:
For any given node, i:
- It's parent is (i - 1) / 2
- It's left child is 2i + 1
- It's right child is 2i + 2

Note: Almost all methods in this class are meant to be private. In production this type of class would only have insert, extract, and peek available.
'''

class Heap:
    def __init__(self, items = []):
        self.size = len(items)
        self.items = items

    #Helper functions that retain basic logic for a heap

    #Left child of a parent node is at index 2i + 1
    def getLeftChildIndex(self, parent_index):
        return parent_index * 2 + 1
    #Right child of a parent node is at index 2i + 2
    def getRightChildIndex(self, parent_index):
        return parent_index * 2 + 2
    #Parent node index is at the floor of (i - 1) / 2
    def getParentIndex(self, child_index):
        return (child_index - 1) // 2
    #These check if nodes exist
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
    #These return the associated values in self.items
    def leftChild(self, index):
        return self.items[self.getLeftChildIndex(index)]    
    def rightChild(self, index):
        return self.items[self.getRightChildIndex(index)]
    def parent(self, index):
        return self.items[self.getParentIndex(index)]
    #Swaps values within the heap, based on index
    def swap(self, index1, index2):
        self.items[index1], self.items[index2] = self.items[index2], self.items[index1]
    
    #Shows the root node
    def peek(self):
        return self.items[0]
    
    #Extracts the root and returns it
    def extractRoot(self):
        item = self.items[0]
        self.items[0] = self.items[-1]
        self.size -= 1
        self.heapifyDown()
        return item
    
    #Inserts a new item as the last leaf node
    def insert(self, item):
        self.items.append(item)
        self.size += 1
        self.heapifyUp()

    #Ensures heap rules are adhered to by swapping elements starting at the leaves and working to the root as needed.
    #To be used only when inserting an element, as elements are inserted at the bottom of the heap
    def heapifyUp(self):
        index = self.size - 1
        while self.hasParent(index) and self.parent(index) > self.items[index]:
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)

    #Ensure heap rules are adhered to by swapping elelents start at the root and working to the leaves as needed.
    #To be used only when extracting the root, as extracting swaps in a new root which may or may not be in order.
    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            smallerChildIndex = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.leftChild(index) > self.rightChild(index):
                smallerChildIndex = self.getRightChildIndex(index)
            if self.items[index] > self.items[smallerChildIndex]:
                self.swap(index, smallerChildIndex)
            index = smallerChildIndex