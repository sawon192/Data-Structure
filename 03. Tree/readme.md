
# Tree 🌳

A Tree is a hierarchical, non-linear data structure made up of nodes connected by edges, with one root node and no cycles.

## Types Covered
- **Binary Tree** — each node has at most 2 children
- **Binary Search Tree (BST)** — binary tree where left < root < right

## Key Terms
- **Root** — topmost node
- **Leaf** — node with no children
- **Height** — longest path from root to a leaf
- **Balance Factor** (AVL) — height(left) - height(right)

## Traversals
- **Inorder** (Left, Root, Right) — gives sorted order in BST
- **Preorder** (Root, Left, Right)
- **Postorder** (Left, Right, Root)
- **Level Order** (BFS style, level by level)

## Time Complexity
| Operation | BST (avg) | BST (worst) | AVL Tree |
|-----------|-----------|-------------|----------|
| Insert | O(log n) | O(n) | O(log n) |
| Search | O(log n) | O(n) | O(log n) |
| Delete | O(log n) | O(n) | O(log n) |

## Run
```bash
python BinaryTree.py
python BinarySearchTree.py
```
