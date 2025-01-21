'''
This file contains logic for Selection Sort. Selection Sort creates a new array from the input array, building it piece by piece by finding the lowest element
in the input, removing it, and placing it in the new, sorted array. Once te input array is empty, the algorithm returns the sorted array. While intuitive, it 
is not efficient with large data sets.

Time complexiy: O(n^2)
Space complexity: O(n), where n is the size of the input array
'''
def SelectionSort(arr):
    sorted = []
    while arr:
        lowest = arr[0]
        index = 0
        for i in range(len(arr)):
            if arr[i] < lowest:
                lowest = arr[i]
                index = i
        sorted.append(lowest)
        arr.pop(index)
    return sorted