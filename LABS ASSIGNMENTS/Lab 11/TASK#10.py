from collections import deque

class CafeteriaQueue:
    """
    A class representing a cafeteria order queue using a FIFO queue.
    """

    def __init__(self):
        """
        Initializes an empty queue.
        """
        self.queue = deque()

    def add_order(self, order):
        """
        Adds an order to the queue.

        Args:
            order (str): The order to be added.
        """
        self.queue.append(order)

    def serve_order(self):
        """
        Serves the next order in the queue.

        Returns:
            str: The order that was served.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("No orders to serve.")
        return self.queue.popleft()

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.queue) == 0

    def display_queue(self):
        """
        Displays the current orders in the queue.
        """
        print("Current Queue:", list(self.queue))


if __name__ == "__main__":
    # Example usage
    cafeteria = CafeteriaQueue()
    cafeteria.add_order("Burger")
    cafeteria.add_order("Pizza")
    cafeteria.add_order("Pasta")
    cafeteria.display_queue()  # Current Queue: ['Burger', 'Pizza', 'Pasta']
    print("Served:", cafeteria.serve_order())  # Served: Burger
    cafeteria.display_queue()  # Current Queue: ['Pizza', 'Pasta']