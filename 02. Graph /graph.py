# Basic Graph representation using Adjacency List

class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def display(self):
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")


# ---- Driver Code ----
if __name__ == "__main__":
    g = Graph(directed=False)

    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")
    g.add_edge("D", "E")

    print("Graph (Adjacency List):")
    g.display()
