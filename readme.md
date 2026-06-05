# DSA – Data Structures & Algorithms in Python

A collection of Python implementations covering core data structures and algorithms, built from the ground up with a focus on understanding how things work under the hood.

---

## Contents

| File                      | Topic                                                     |
|---------------------------|-----------------------------------------------------------|
| `01.Algorithms.py`        | Arrays & memory management (`ReservedMemory`, `IntArray`) |
| `02.SinglyLinkedList.py`  | Singly Linked Lists                                       |
| `03.DoublyLinkedLists.py` | Doubly Linked Lists                                       |
| `04.Stacks.py`            | Stacks                                                    |
| `05.Check_balance.py`     | Bracket/parenthesis balance checking                      |
| `06.Queues.py`            | Queues (array-based)                                      |
| `07.NodeBasedQueue.py`    | Queues (node/pointer-based)                               |
| `08.BST.py`               | Binary Search Trees                                       |
| `09.Detach.py`            | Node detachment utilities                                 |
| `10.Hashing.py`           | Hash tables & hashing                                     |
| `11.Graphs.py`            | Graph representations & traversal                         |
| `12.PriorityQueues.py`    | Priority Queues / Heaps                                   |
| `13.Search.py`            | Search algorithms                                         |
| `14.Sorting.py`           | Sorting algorithms                                        |
| `15.HeapSort.py`          | Sorting algorithms                                        |
| `16.MergeSort.py`         | Merge Sorting and optimized tabulation fibonacci          |
| `17.BFS_DFS.py`           | Incomplete BFS and DFS                                    |
| `17.Dijkstra.py`          | Representation of Dijkstra algorithm                      |

---

## Highlights

- **Low-level memory management** — `01.Algorithms.py` implements a raw `ReservedMemory` class using Python's `ctypes`, then builds an integer array on top of it with support for append, pop, insert, remove, and search.
- **Linked structures** — both singly and doubly linked list variants with full node manipulation.
- **Trees & graphs** — BST with insertion/search, and graph implementations covering common traversal patterns.
- **Classic ADTs** — stacks, queues (array and node-based), and priority queues implemented as proper classes.

---

## Getting Started

**Requirements:** Python 3.x (no external dependencies)

```bash
# Clone the repo
git clone https://github.com/mustah21/DSA.git
cd DSA

# Run any file directly
python 01.Algorithms.py
```

---
