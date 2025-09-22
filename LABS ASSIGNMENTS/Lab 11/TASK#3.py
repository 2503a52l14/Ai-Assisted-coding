class Node:
    """
    A class representing a node in a singly linked list.
    """

    def __init__(self, data):
        """
        Initializes a node with data and a pointer to the next node.

        Args:
            data: The data to store in the node.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A class representing a singly linked list.
    """

    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.head = None

    def insert(self, data):
        """
        Inserts a new node with the given data at the end of the list.

        Args:
            data: The data to insert into the list.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        """
        Displays the elements of the linked list.
        """
        if self.head is None:
            print("The linked list is empty.")
        else:
            current = self.head
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.display()  # The linked list is empty.
    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.insert(30)
    linked_list.display()  # 10 -> 20 -> 30 -> None