'''
This algorithm sorts an array by comparing each element to the following element until it reaches a point at which
there is no following element. For each pair, the values are compared and if they are out of order they are swapped.
This process repeats itself until no swaps are made, indicating that the list is sorted.

Analysis
    - Time complexity: O(n^2)
    - Space complexity: O(n)
'''
def bubbleSort(arr):
    n = len(arr)
    if n < 2:
        return arr
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr