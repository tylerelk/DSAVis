'''
This file contains logic for Insertion Sort. Visually, this algorithm looks like Bubble Sort in reverse, where the list is iterated and each value is moved
to the left until it is larger than the value before it and greater than or equal to the number after it. Consider the first value in the array (index 0) as
sorted, since a single value is, by default, sorted. For each following value, move it to the appropriate part of the sorted array. The slgorithm runs with 
nested loops, inherently making this a quadratic algorithm, which work through all values after the first one, and comparing them to the sorted values. In 
short, for each newly-inspected value, the value is compared to each of the sorted values in descending order until a sorted value is found which is less than
the current value.

- Time complexity: O(n^2)
- Space complexity: O(1)
'''

def InsertionSort(arr):
    for i in range(1, len(arr)):
        insert_at = i
        current = arr.pop(i)
        for j in range(i - 1, -1, -1):
            if arr[j] > current:
                insert_at = j
        arr.insert(insert_at, current)
    return arr