"""
Task 2: Binary Search Implementation
------------------------------------
Prompt :Create a function binary_search(arr, target) in Python to find a target element in a sorted list.
Add docstrings describing best, average, and worst-case complexities.

Objective:
Implement Binary Search using AI assistance, test it with assert statements,
and display the search results in the output.
"""

def binary_search(arr, target):
    """
    Binary Search Algorithm
    -----------------------
    Efficiently finds 'target' in a sorted array.

    Best Case: O(1)
    Average Case: O(log n)
    Worst Case: O(log n)
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Found target
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Not found

# --- Test Cases ---
arr1 = [1, 2, 3, 4, 5]
arr2 = [10, 20, 30, 40]
arr3 = []

assert binary_search(arr1, 3) == 2
assert binary_search(arr2, 25) == -1
assert binary_search(arr3, 1) == -1

# --- Output Section ---
print("Array 1:", arr1)
print("Searching for 3 → Index:", binary_search(arr1, 3))
print("Array 2:", arr2)
print("Searching for 25 → Index:", binary_search(arr2, 25))
print("Array 3:", arr3)
print("Searching for 1 → Index:", binary_search(arr3, 1))
print("✅ Task 2 (Binary Search) executed successfully!")
# --- Binary Search Implementation ---