class Queue:
    """
    A class representing a FIFO (First-In-First-Out) queue.
    """

    def __init__(self):
        """
        Initializes an empty queue.
        """
        self.items = []

    def enqueue(self, item):
        """
        Adds an item to the end of the queue.

        Args:
            item: The item to be added to the queue.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Removes and returns the item at the front of the queue.

        Returns:
            The item at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue: Queue is empty.")
        return self.items.pop(0)

    def peek(self):
        """
        Returns the item at the front of the queue without removing it.

        Returns:
            The item at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot peek: Queue is empty.")
        return self.items[0]

    def size(self):
        """
        Returns the number of items in the queue.

        Returns:
            The size of the queue.
        """
        return len(self.items)

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        return len(self.items) == 0


if __name__ == "__main__":
    queue = Queue()
    print("Is empty?", queue.is_empty())  # True
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Peek:", queue.peek())          # 10
    print("Dequeue:", queue.dequeue())    # 10
    print("Size:", queue.size())          # 2
    print("Is empty?", queue.is_empty())  # False