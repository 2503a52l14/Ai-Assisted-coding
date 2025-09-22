class Node:
    """
    A class representing a node in a binary search tree.
    """

    def __init__(self, data):
        """
        Initializes a node with data and pointers to left and right children.

        Args:
            data: The data to store in the node.
        """
        self.data = data
        self.left = None
        self.right = None


class BST:
    """
    A class representing a binary search tree.
    """

    def __init__(self):
        """
        Initializes an empty binary search tree.
        """
        self.root = None

    def insert(self, data):
        """
        Inserts a new node with the given data into the BST.

        Args:
            data: The data to insert into the tree.
        """
        self.root = self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        """
        Helper method to insert a node recursively.

        Args:
            node: The current node in the tree.
            data: The data to insert.

        Returns:
            The updated node after insertion.
        """
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        else:
            node.right = self._insert_recursive(node.right, data)
        return node

    def in_order_traversal(self):
        """
        Performs an in-order traversal of the BST and prints the elements.
        """
        print("In-order traversal:", end=" ")
        self._in_order_recursive(self.root)
        print()

    def _in_order_recursive(self, node):
        """
        Helper method to perform in-order traversal recursively.

        Args:
            node: The current node in the tree.
        """
        if node is not None:
            self._in_order_recursive(node.left)
            print(node.data, end=" ")
            self._in_order_recursive(node.right)


if __name__ == "__main__":
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)
    bst.in_order_traversal()  # Output: 20 30 40 50 60 70 80