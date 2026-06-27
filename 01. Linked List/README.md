# Linked List 🔗

A Linked List is a linear data structure where each element (node) points to the next one.
Unlike arrays, elements aren't stored in contiguous memory — each node has data + a pointer to the next node.

## Types Covered
- **Singly Linked List** — each node points only to the next node
- **Doubly Linked List** — each node points to both next and previous node
## Why use it?
- Dynamic size (no need to define size beforehand like arrays)
- Efficient insertions/deletions (especially at the beginning)

## Time Complexity
| Operation | Singly LL | Doubly LL |
|-----------|-----------|-----------|
| Insert at head | O(1) | O(1) |
| Insert at tail | O(n) | O(1)* |
| Search | O(n) | O(n) |
| Delete | O(n) | O(n) |

*O(1) if tail pointer is maintained

## Run
```bash
python SinglyLinkedList.py
python DoublyLinkedList.py
```

See `Output.png` for sample run.
