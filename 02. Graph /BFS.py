# Breadth-First Search (BFS) 

from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)
        self.graph.setdefault(v, []).append(u)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order


# ---- Driver Code ----
if __name__ == "__main__":
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")
    g.add_edge("D", "E")

    print("BFS starting from A:", g.bfs("A"))
