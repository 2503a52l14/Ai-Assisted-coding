# Data Structure Comparison Table (Short Output)

comparison_table = '''
| Data Structure      | Average Time Complexity |
|---------------------|--------------------------|
| Stack               | O(1)                    |
| Queue               | O(1)                    |
| Deque               | O(1)                    |
| Singly Linked List  | O(1) (head) / O(n) (tail) |
| Doubly Linked List  | O(1)                    |
| Hash Table          | O(1) avg                |
| Binary Search Tree  | O(log n)                |
| Heap/Priority Queue | O(log n)                |
| Graph (Adj. List)   | O(1) (add vertex/edge)  |
'''

if __name__ == "__main__":
    print(comparison_table)

