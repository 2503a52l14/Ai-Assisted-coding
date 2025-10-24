"""
Task 1: Merge Sort Implementation
---------------------------------
Prompt : Generate a Python function merge_sort(arr) that sorts a list in ascending order using Merge Sort.
Include time and space complexity in the docstring, and ensure the code is clean and optimized.

Objective:
Implement Merge Sort using AI assistance and test its correctness
with assert statements. Also, display the sorted output.
"""

def merge_sort(arr):
    """
    Merge Sort Algorithm
    --------------------
    Recursively splits the list into halves and merges them in sorted order.

    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if len(arr) <= 1:
        return arr  # Base case

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # Sort left half
    right = merge_sort(arr[mid:])  # Sort right half

    return merge(left, right)

def merge(left, right):
    """Helper function to merge two sorted lists."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# --- Test Cases ---
arr1 = [5, 3, 8, 4, 2]
arr2 = []
arr3 = [1, 1, 1, 1]

assert merge_sort(arr1) == [2, 3, 4, 5, 8]
assert merge_sort(arr2) == []
assert merge_sort(arr3) == [1, 1, 1, 1]

# --- Output Section ---
print("Original List 1:", arr1)
print("Sorted List 1:", merge_sort([5, 3, 8, 4, 2]))
print("Original List 2:", arr2)
print("Sorted List 2:", merge_sort(arr2))
print("Original List 3:", arr3)
print("Sorted List 3:", merge_sort(arr3))
print("✅ Task 1 (Merge Sort) executed successfully!")
# --- Merge Sort Implementation ---