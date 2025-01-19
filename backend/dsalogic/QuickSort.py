'''
This file contains logic for Quick Sort. This is a recursive algorithm that continuously divides an array until the subarrays contain 0 or 1 elements, meaning
they are inherently sorted. The concept of Quick Sort works off of one guiding principle: Given a value, num, if all elements to the left are less and all the 
elements to the right are more, num must be in it's sorted position within the array. The work of the Quick Sort algorithm (and the Partition helper function) is
 to place each element of the array in it's sorted position.

Pseudocode:
1. 
'''
def QuickSort(arr):
    end = len(arr) - 1
    if end >= 1:
        p = Partition(arr)
        QuickSort(arr[:p])
        QuickSort(arr[p:])
    return arr

def Partition(arr):
    pivot = arr[0]
    i = 1
    j = len(arr) - 1
    while i < j:
        while arr[i] <= pivot and i < j:
            i += 1
        while arr[j] > pivot and i < j:
            j -= 1
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
    tmp = arr[0]
    arr[0] = arr[j]
    arr[j] = tmp
    return j

test = [3, 1, 6, 3, 8, 5, 0, 10]
print(QuickSort(test))