## 10. B-Trees

## Study Notes

### 1. 🌳 Introduction to B-Trees and Their Importance

When working with very large datasets, especially those stored on disk rather than in fast internal memory, the choice of data structure for searching and updating dictionaries (collections of key-value pairs) becomes critical. Traditional binary search trees like AVL trees or Red-Black trees, while efficient in memory, perform poorly on disk because each node access may require a slow disk read.

**B-Trees** are advanced data structures designed to minimize disk accesses by having nodes with many children (high degree), allowing the tree to be shorter and wider. This reduces the number of disk reads needed to find or update a key, making B-Trees ideal for databases and file systems.


### 2. 📊 Why Not AVL or Red-Black Trees for Disk Storage?

To understand why B-Trees are necessary, let's compare them with AVL and Red-Black trees for large datasets:

- Suppose we have about $n = 2^{30} \approx 10^9$ keys.
- **AVL Trees** have heights between 30 and 43 for this size.
- **Red-Black Trees** have heights between 30 and 60.

When these trees are stored on disk, each node access corresponds to a disk read, which is slow (about 100 milliseconds per access). So:

- Searching in an AVL tree might require up to 43 disk accesses → roughly 4 seconds.
- Searching in a Red-Black tree might require up to 60 disk accesses → roughly 6 seconds.

These times are too slow for practical use, motivating the need for trees with fewer levels and more children per node.


### 3. 🌲 Understanding m-Way Search Trees

An **m-way search tree** generalizes binary search trees by allowing each node to have up to $m$ children and $m-1$ key-value pairs (called dictionary pairs). For example:

- When $m = 2$, this is just a binary search tree.
- When $m = 4$, each node can have up to 3 keys and 4 children.

The key idea is that increasing $m$ reduces the height of the tree because each node covers a larger range of keys.

#### Maximum Number of Pairs in an m-Way Tree

- If the tree is full (all internal nodes have $m$ children), the number of nodes at height $h$ is:

$$
  1 + m + m^2 + \cdots + m^{h-1}
$$

- Each node has $m-1$ pairs, so the total number of pairs is roughly:

$$
  m^h - 1
$$


This shows how the number of keys grows exponentially with the height and degree $m$.


### 4. 📚 What is a B-Tree?

A **B-Tree** is a special kind of m-way search tree with additional balance and capacity rules designed to optimize disk access:

- It is an **m-way search tree**.
- The root node has at least 2 children if the tree is not empty.
- Every other internal node has at least $\lceil m/2 \rceil$ children (this is the minimum degree condition).
- All external nodes (leaves or failure nodes) are at the same level, ensuring the tree is balanced.

This structure guarantees that the tree remains balanced and shallow, which is crucial for minimizing disk reads.

#### Examples of B-Trees

- A **2-3 tree** is a B-tree of order 3.
- A **2-3-4 tree** is a B-tree of order 4.
- A B-tree of order 5 is sometimes called a 3-4-5 tree, where the root may have fewer children.

When $m = 2$, the B-tree is just a full binary tree.


### 5. 📏 Height and Capacity of B-Trees

The height $h$ of a B-tree is important because it determines the worst-case number of disk accesses during search or update.

- The minimum number of pairs $n$ in a B-tree of height $h$ satisfies:

$$
  n + 1 \geq 2 \times \lceil m/2 \rceil^{h-1}
$$

- Rearranging, the height is bounded by:

$$
  h \leq \log_{\lceil m/2 \rceil} \left(\frac{n+1}{2}\right) + 1
$$


This means the height grows logarithmically with the number of keys, but the base of the logarithm is $\lceil m/2 \rceil$, which is larger than 2 for $m > 2$. Hence, B-trees are much shorter than binary trees for large $m$.


### 6. ✍️ Insertion in B-Trees: How It Works

Insertion in a B-tree is more complex than in a binary tree because nodes can hold multiple keys and must maintain balance.

- When inserting a new key, you first find the correct leaf node.
- If the leaf node has fewer than $m-1$ keys, simply insert the new key in sorted order.
- If the leaf node is full (has $m-1$ keys), it **splits**:
  - The middle key moves up to the parent node.
  - The node splits into two nodes, each holding about half the keys.
- This splitting can propagate upward if the parent is also full, possibly increasing the tree height by creating a new root.

#### Example: Inserting into a 3-node (a node with 2 keys)

- Insert the new key so the keys are in ascending order.
- Split the node around the middle key.
- Insert the middle key into the parent node along with a pointer to the new node.

If the parent is full, repeat the split process up the tree.


### 7. 🗑️ Deletion in B-Trees: Handling Underflow

Deletion is trickier because removing a key can cause nodes to have too few keys, violating the minimum degree condition.

- If deleting a key from a leaf node leaves it with enough keys, just remove it.
- If the node becomes deficient (too few keys), fix it by:
  - **Borrowing** a key from an adjacent sibling node that has extra keys, adjusting the parent key accordingly.
  - If siblings cannot lend keys, **merge** the deficient node with a sibling and pull down a key from the parent to maintain balance.
- This process may propagate upward, possibly reducing the tree height if the root ends up with only one child.


### 8. 💾 Disk Accesses and Performance Considerations

The main advantage of B-trees is reducing disk accesses:

- Searching requires reading nodes from root to leaf, so $h$ disk reads.
- Insertion may cause splits, requiring additional writes.
- Worst-case disk accesses for insertion are about $3h + 1$.

Choosing the order $m$ of the B-tree balances:

- The cost of searching within a node (which grows with $m$).
- The height of the tree (which decreases as $m$ increases).

The goal is to minimize the total time:

$$
(\text{time to fetch a node} + \text{time to search node}) \times \text{height}
$$



### 9. 🔗 B+-Trees: A Variant of B-Trees

**B+-Trees** are a popular variant used in databases:

- All dictionary pairs (keys and values) are stored only in the leaf nodes.
- Internal nodes only store keys to guide the search.
- Leaves are linked together in a doubly-linked list, allowing efficient range queries and sequential access.
- This structure improves performance for range queries and bulk operations.

Insertion and deletion in B+-trees follow similar principles to B-trees but maintain the linked list of leaves.


### Summary

- **B-Trees** are balanced m-way search trees optimized for disk storage.
- They reduce tree height by allowing many children per node, minimizing slow disk accesses.
- Insertion and deletion involve splitting and merging nodes to maintain balance.
- B+-Trees store all data in leaves and link leaves for efficient sequential access.
- Choosing the right order $m$ is crucial for performance.

Understanding B-trees is essential for working with large-scale databases and file systems where disk access speed is a bottleneck.