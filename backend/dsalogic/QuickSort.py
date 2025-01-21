'''
This file contains logic for Quick Sort. This is a recursive algorithm that continuously divides an array until the subarrays contain 0 or 1 elements, meaning
they are inherently sorted. The concept of Quick Sort works off of one guiding principle: Given a value, num, if all elements to the left are less and all the 
elements to the right are more, num must be in it's sorted position within the array. The work of the Quick Sort algorithm (and the Partition helper function) is
 to place each element of the array in it's sorted position.

Pseudocode:
1. By default, no high or low values are provided and are set to the length of the array and 0, respectively
2. If low is greater than high, return the array as we have sorted it
3. determine a partition point (p), using a separate Partition function
4. Partition takes the entire array as well as a low index and a high index - this effectively feeds Partition a sub-array
5. Set a pivot point, in this case it is the element at the high position (defaults to length of array)
6. Set a separate counter, i, to low - 1
    - This is so we can iterate with i without losing the value of low
    - i is responsible for tracking the most recent element in the following loop that is less than or equal to the pivot
    - i represents the barrier between the lesser and greater than sides of the array
7. Iterate through the array starting at low and ending at the element before high
8. If a value is found that is less than or equal to the pivot, increment i and swap i with the iterator
    - By doing this, we are determining if the value at j should be on the left side of the sorted array
    - Incrementing i at this point creates room on the left side of the array for this found lesser value
9. When the loop completes, we swap the pivot value with the value just after i
    - Since i represents the barrier between larger and smaller, placing the pivot value at i + 1 ensures that all values before it are lower
10. From Partition, return the position of the pivot (i + 1)
11. Recursively call QuickSort over the left half of the array - that is, all elements less than the partition
12. Repeat on the right for elements greater than the partition
13. During recursive calls, new low and high values are entered as arguments in QuickSort, ensuring that subarrays are inspected and sorted
14. After sorting in-place, return the sorted array

Analysis:
- Time complexity:
    - If Partition always returns the element at the center of the array or sub-array, time complexity results in O(nlogn)
    - However, if Partition returns elements at the beggining or end of the list every time, time complexity is O(n^2)
        - This happens if the list is already sorted
- Space complexity:
    - Similar to time complexity, the space complexity is determined by the position of the partition:
        - Worst case: O(n)
            - Occurs if the list is already sorted or nearly sorted, as the call stack increases
        - Best case: O(logn)
            - Occurs if the partition is centered in the array, since the call stack will reduce on the left before calling the right
'''

def QuickSort(arr, low = 0, high = None):
    if not high:
        high = len(arr) - 1
    if low < high:
        p = Partition(arr, low, high)
        QuickSort(arr, low, p - 1)
        QuickSort(arr, p + 1, high)
    return arr

def Partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
    tmp = arr[high]
    arr[high] = arr[i + 1]
    arr[i + 1] = tmp
    return i + 1

test = [1, 6, 3, 8, 5, 0, 10]
print(QuickSort(test))