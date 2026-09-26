## 7. Fibonacci Heaps and Pairing Heaps

## Study Notes

### 1. 📚 Introduction to Fibonacci and Pairing Heaps

In advanced data structures, **heaps** are specialized tree-based structures that allow efficient access to the minimum or maximum element. Two important types of heaps used in graph algorithms and priority queue implementations are **Fibonacci heaps** and **pairing heaps**. Both are designed to optimize operations like insertion, deletion, and key updates, which are crucial in algorithms such as Dijkstra’s shortest path.

This note will explain these heaps in detail, focusing on their structure, operations, and performance characteristics, along with how they improve the efficiency of graph algorithms.


### 2. 🔢 Fibonacci Heaps: Structure and Operations

#### What is a Fibonacci Heap?

A **Fibonacci heap** is a collection of heap-ordered trees (min-trees or max-trees) that are linked together in a circular, doubly linked list. It is designed to support a set of operations with very efficient *amortized* time complexities, especially for decrease-key operations, which are common in graph algorithms.

#### Key Operations and Their Amortized Complexities

| Operation          | Amortized Time Complexity |
|--------------------|---------------------------|
| Insert             | O(1)                      |
| Remove Min (or Max)| O(log n)                  |
| Meld (Union)       | O(1)                      |
| Decrease Key       | O(1)                      |
| Remove (arbitrary) | O(log n)                  |

- **Insert** is very fast because it just adds a new single-node tree to the root list.
- **Remove Min** is more complex because it involves consolidating trees to maintain heap order.
- **Decrease Key** is very efficient, which is why Fibonacci heaps are preferred in algorithms like Dijkstra’s.

#### Why Fibonacci Heaps Matter in Shortest Path Algorithms

In **Dijkstra’s algorithm**, we repeatedly select the vertex with the smallest tentative distance (`d(i)`) and update the distances of its neighbors. This involves:

- Removing the minimum element (`Remove Min`) from the priority queue (done O(n) times).
- Decreasing keys (`Decrease Key`) when shorter paths are found (done O(e) times, where e is the number of edges).

Using a simple array leads to O(n²) complexity, a binary heap leads to O((n + e) log n), but a Fibonacci heap reduces this to **O(n log n + e)**, which is a significant improvement for dense graphs.


### 3. 🌳 Fibonacci Heap Node Structure and Representation

Each node in a Fibonacci heap contains:

- **Degree**: Number of children.
- **Child**: Pointer to one of its children.
- **Data**: The key or value stored.
- **Left and Right Sibling**: Pointers for a circular doubly linked list of siblings.
- **Parent**: Pointer to the parent node.
- **ChildCut**: A boolean flag indicating if the node has lost a child since it became a child of its current parent.

The **ChildCut** flag is crucial for the *cascading cut* operation, which helps maintain the heap’s amortized efficiency.


### 4. ✂️ Key Operations in Fibonacci Heaps: Remove, Decrease Key, and Cascading Cut

#### Remove(theNode)

- If `theNode` is the minimum element, perform a **remove min** operation.
- Otherwise:
  - Remove `theNode` from its sibling list.
  - Add its children to the root list (top-level list), updating their parent pointers to null.
  - Consolidate the heap if necessary.

#### DecreaseKey(theNode, amount)

- Decrease the key of `theNode` by `amount`.
- If `theNode` is not a root and its new key is less than its parent’s key:
  - Cut the subtree rooted at `theNode` from its sibling list.
  - Insert it into the root list.
  - Perform a **cascading cut** on the parent.

#### Cascading Cut

- When a node loses a child, its `ChildCut` flag is set to true.
- If a node with `ChildCut = true` loses another child, it is cut from its parent and added to the root list.
- This process continues up the tree until a node with `ChildCut = false` is found, which then has its `ChildCut` set to true.
- This operation ensures that trees remain shallow, preserving the amortized time bounds.

The actual complexity of cascading cuts can be O(h) where h is the height of the tree, but amortized analysis shows it remains efficient.


### 5. 🔄 Pairing Heaps: Simpler Alternative to Fibonacci Heaps

#### What is a Pairing Heap?

A **pairing heap** is a simpler heap structure that also supports efficient priority queue operations. It is a single heap-ordered tree where each node has a pointer to its first child and doubly linked siblings (not circular). Unlike Fibonacci heaps, pairing heaps do **not** maintain parent pointers, degrees, or child-cut flags.

#### Operations and Their Complexities

| Operation          | Pairing Heap Amortized Complexity |
|--------------------|-----------------------------------|
| Insert             | O(log n) (often close to O(1) in practice) |
| Remove Min (or Max)| O(log n)                         |
| Meld (Union)       | O(log n)                         |
| Decrease Key       | O(log n)                         |

While theoretically slower than Fibonacci heaps for decrease key, **pairing heaps are often faster in practice** due to simpler implementation and lower overhead.


### 6. ⚙️ Pairing Heap Node Structure and Meld Operation

#### Node Structure

- **Child**: Pointer to the first child.
- **Left and Right Sibling**: Pointers for a doubly linked list of siblings.
- **Data**: The key or value stored.

No parent pointers or extra flags are maintained, which simplifies the structure.

#### Meld Operation (Compare-Link)

- To meld two pairing heaps, compare their roots.
- The heap with the smaller root becomes the parent, and the other becomes its leftmost child.
- This operation takes O(1) time.


### 7. 🔧 Pairing Heap Operations: Insert, Remove Max, and Increase Key

#### Insert

- Create a new single-node heap.
- Meld it with the existing heap.
- Actual cost is O(1).

#### Remove Max (or Min)

- Remove the root.
- Meld all its subtrees into a single heap.
- Two main ways to meld subtrees:
  - **Bad way**: Meld subtrees one by one from left to right, which can be O(n²) in worst case.
  - **Good ways**: Use **two-pass** or **multipass** schemes to meld subtrees efficiently in O(n) time.

#### Two-Pass Scheme

- **Pass 1**: Meld pairs of subtrees from left to right, halving the number of trees.
- **Pass 2**: Meld the resulting trees from right to left into one heap.

#### Multipass Scheme

- Place all subtrees in a queue.
- Repeatedly remove two trees, meld them, and enqueue the result until one tree remains.

#### Increase Key

- Since no parent pointers exist, we cannot easily check if the heap property is violated.
- Detach the node from its sibling list.
- Meld the detached subtree back into the main heap.
- Actual cost is O(1).


### 8. 🏁 Summary and Practical Considerations

- **Fibonacci heaps** offer excellent theoretical amortized bounds, especially for decrease key operations, making them ideal for algorithms like Dijkstra’s shortest path.
- **Pairing heaps** are simpler to implement and often faster in practice, despite slightly worse theoretical bounds.
- Both heaps rely on clever tree linking and restructuring to maintain heap order and efficiency.
- Understanding the internal node structures and operations like cascading cuts (Fibonacci) and two-pass melding (pairing) is key to grasping their performance.