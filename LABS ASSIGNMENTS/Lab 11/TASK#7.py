import heapq

class PriorityQueue:
    """
    A class representing a priority queue using Python's heapq module.
    """

    def __init__(self):
        """
        Initializes an empty priority queue.
        """
        self.queue = []

    def enqueue(self, item, priority):
        """
        Adds an item to the priority queue with the given priority.

        Args:
            item: The item to be added.
            priority: The priority of the item (lower value means higher priority).
        """
        heapq.heappush(self.queue, (priority, item))

    def dequeue(self):
        """
        Removes and returns the item with the highest priority (lowest priority value).

        Returns:
            The item with the highest priority.

        Raises:
            IndexError: If the priority queue is empty.
        """
        if not self.is_empty():
            return heapq.heappop(self.queue)[1]
        raise IndexError("Cannot dequeue from an empty priority queue.")

    def display(self):
        """
        Displays the contents of the priority queue.
        """
        print("Priority Queue:", [(priority, item) for priority, item in self.queue])

    def is_empty(self):
        """
        Checks if the priority queue is empty.

        Returns:
            True if the priority queue is empty, False otherwise.
        """
        return len(self.queue) == 0


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.enqueue("Task A", 3)
    pq.enqueue("Task B", 1)
    pq.enqueue("Task C", 2)
    pq.display()  # Priority Queue: [(1, 'Task B'), (3, 'Task A'), (2, 'Task C')]
    print("Dequeued:", pq.dequeue())  # Task B
    pq.display()  # Priority Queue: [(2, 'Task C'), (3, 'Task A')]
    print("Dequeued:", pq.dequeue())  # Task C
    pq.display()  # Priority Queue: [(3, 'Task A')]