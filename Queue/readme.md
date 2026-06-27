
# Queue 

A Queue follows **FIFO** (First In, First Out) order — the first element added is the first one removed.
Think of a queue at a ticket counter: first person in line gets served first.

## Types Covered
- **Simple Queue** — basic FIFO queue
- **Priority Queue** — elements are dequeued based on priority, not insertion order

## Operations
- `enqueue(item)` — add item to the rear
- `dequeue()` — remove item from the front
- `peek()` — view front item

## Time Complexity
| Operation | Simple Queue | Circular Queue | Priority Queue |
|-----------|--------------|----------------|----------------|
| Enqueue | O(1) | O(1) | O(log n) |
| Dequeue | O(n)* | O(1) | O(log n) |

*O(n) with list.pop(0); O(1) if using deque

## Real-world uses
- CPU task scheduling
- Printer queue
- Handling requests in web servers
- Priority Queue → Dijkstra's Algorithm, Huffman coding

## Run
```bash
python SimpleQueue.py
python PriorityQueue.py
```
