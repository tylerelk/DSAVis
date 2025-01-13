'''
This algorithm sorts an array by comparing each element to the following element until it reaches a point at which
there is no following element. For each pair, the values are compared and if they are out of order they are swapped.
This process repeats itself until no swaps are made, indicating that the list is sorted.

Analysis
    - Time complexity: O(n^2)
    - Space complexity: O(n)
'''
def bubbleSort(arr):
    if len(arr) < 2:
        return arr
    swapped = True
    while swapped:
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                pass
            swapped = False
    return arr

print(bubbleSort([5, 2, 6, 1, 3]))