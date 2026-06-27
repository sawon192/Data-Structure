# DFS (Depth First Search) - Recursive and Iterative

class Graph:
    def __init__(self):
        # Dictionary to store the graph
        self.graph = {}

    # Add an edge between two nodes
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    # Recursive DFS
    def dfs_recursive(self, node, visited=None):
        if visited is None:
            visited = []

        visited.append(node)
        print(node, end=" ")

        for neighbour in self.graph[node]:
            if neighbour not in visited:
                self.dfs_recursive(neighbour, visited)

    # Iterative DFS using stack
    def dfs_iterative(self, start):
        visited = []
        stack = [start]

        while stack:
            node = stack.pop()

            if node not in visited:
                visited.append(node)
                print(node, end=" ")

                # Add neighbours in reverse order
                for neighbour in reversed(self.graph[node]):
                    if neighbour not in visited:
                        stack.append(neighbour)


# Main Program
g = Graph()

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")
g.add_edge("D", "E")

print("Recursive DFS:")
g.dfs_recursive("A")

print("\n")

print("Iterative DFS:")
g.dfs_iterative("A")
