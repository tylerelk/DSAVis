'''
This file contains a merge sort algorithm. In merge sort, an unsorted array is divided recursively until each division triggers the base case where the
length of the array is 1 or 0. The divided sections are then merged back together in order, resulting in multiple sorted divisions that merge into one
sorted array. This implementation utilizes two separate functions - one for merging in sorted order and another for splitting and processing the initial list;
In practice, the Merge function would be used only by the MergeSort function.

- Time complexity: O(n log n)
- Space complexity: O(n^2)
'''
def Merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    while left:
        result.append(left[0])
        left.pop(0)
    while right:
        result.append(right[0])
        right.pop(0)
    return result

def MergeSort(array):
    if len(array) <= 1:
        return array
    midpoint = len(array) // 2
    left = array[:midpoint]
    right = array[midpoint:]
    sortLeft = MergeSort(left)
    sortRight = MergeSort(right)
    return Merge(sortLeft, sortRight)

print(MergeSort([3, 1, 6, 2, 9, 4, 11, 15]))
print(MergeSort([900, -14, -222, 5, 22, 9, 7, -4, -4]))
print(MergeSort([]))
print(MergeSort([9]))
print(MergeSort([2, -99]))