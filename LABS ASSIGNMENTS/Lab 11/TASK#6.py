class Graph:
    """
    A class representing a graph using an adjacency list.
    """

    def __init__(self):
        """
        Initializes an empty graph.
        """
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph.

        Args:
            vertex: The vertex to add.
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """
        Adds an edge between two vertices in the graph.

        Args:
            vertex1: The first vertex.
            vertex2: The second vertex.
        """
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)  # For undirected graph

    def display(self):
        """
        Displays the graph as an adjacency list.
        """
        for vertex, edges in self.adjacency_list.items():
            print(f"{vertex}: {edges}")


if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "C")
    graph.display()