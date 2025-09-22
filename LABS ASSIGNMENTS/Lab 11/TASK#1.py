class Stack:
    """
    A simple stack implementation using a Python list.
    Supports push, pop, peek, and is_empty operations.
    """

    def __init__(self):
        """Initialize an empty stack."""
        self._items = []

    def push(self, item):
        """
        Add an item to the top of the stack.
        :param item: Item to be added.
        """
        self._items.append(item)

    def pop(self):
        """
        Remove and return the top item from the stack.
        :return: The top item.
        :raises IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """
        Return the top item without removing it.
        :return: The top item.
        :raises IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        """
        Check if the stack is empty.
        :return: True if empty, False otherwise.
        """
        return len(self._items) == 0


if __name__ == "__main__":
    stack = Stack()
    print("Is empty?", stack.is_empty())  # True
    stack.push(10)
    stack.push(20)
    print("Peek:", stack.peek())          # 20
    print("Pop:", stack.pop())            # 20
    print("Peek after pop:", stack.peek())# 10
    print("Is empty?", stack.is_empty())  # False
    stack.pop()
    print("Is empty after popping all:", stack.is_empty())  # True