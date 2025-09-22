from collections import deque

class DequeDS:
    """
    A class representing a double-ended queue (deque) using collections.deque.
    """

    def __init__(self):
        """
        Initializes an empty deque.
        """
        self.deque = deque()

    def insert_front(self, item):
        """
        Inserts an item at the front of the deque.

        Args:
            item: The item to be added.
        """
        self.deque.appendleft(item)

    def insert_rear(self, item):
        """
        Inserts an item at the rear of the deque.

        Args:
            item: The item to be added.
        """
        self.deque.append(item)

    def remove_front(self):
        """
        Removes and returns the item from the front of the deque.

        Returns:
            The item removed from the front.

        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot remove from front: Deque is empty.")
        return self.deque.popleft()

    def remove_rear(self):
        """
        Removes and returns the item from the rear of the deque.

        Returns:
            The item removed from the rear.

        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot remove from rear: Deque is empty.")
        return self.deque.pop()

    def is_empty(self):
        """
        Checks if the deque is empty.

        Returns:
            True if the deque is empty, False otherwise.
        """
        return len(self.deque) == 0

    def display(self):
        """
        Displays the contents of the deque.
        """
        print("Deque contents:", list(self.deque))


if __name__ == "__main__":
    dq = DequeDS()
    dq.insert_rear(10)
    dq.insert_rear(20)
    dq.insert_front(5)
    dq.display()  # Deque contents: [5, 10, 20]
    print("Removed from front:", dq.remove_front())  # 5
    print("Removed from rear:", dq.remove_rear())    # 20
    dq.display()  # Deque contents: [10]