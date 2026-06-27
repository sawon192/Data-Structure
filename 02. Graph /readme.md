
# Graph 

A Graph is a non-linear data structure made of **vertices (nodes)** connected by **edges**.
Unlike trees, graphs can have cycles and multiple connections between nodes.

## Concepts Covered
- **Graph Representation** — using adjacency list
- **BFS** (Breadth-First Search) — explores neighbors level by level, uses a queue
- **DFS** (Depth-First Search) — explores as deep as possible before backtracking, uses recursion/stack
- **Dijkstra's Algorithm** — finds shortest path from a source node in a weighted graph

## When to use what?
| Use case | Algorithm |
|----------|-----------|
| Shortest path (unweighted) | BFS |
| Detect cycles / connected components | DFS |
| Shortest path (weighted, no negative edges) | Dijkstra |

## Time Complexity
| Algorithm | Time Complexity |
|-----------|------------------|
| BFS | O(V + E) |
| DFS | O(V + E) |
| Dijkstra | O((V + E) log V) using min-heap |

(V = vertices, E = edges)

## Real-world uses
- BFS → Social network friend suggestions, shortest path in maze
- DFS → Solving puzzles, topological sorting, cycle detection
- Dijkstra → Google Maps shortest route, network routing protocols

## Run
```bash
python Graph.py
python BFS.py
python DFS.py
python Dijkstra.py
```
