## 9. AVL Trees

## Study Notes

### 1. 🌳 Introduction to Dynamic Dictionaries and Balanced Search Trees

When working with data, one common need is to store key-element pairs so that we can quickly find, add, or remove elements based on their keys. This is what dynamic dictionaries do. The primary operations are:

- **get(key):** Search for an element by its key.
- **put(key, element):** Insert a new key-element pair.
- **remove(key):** Delete the element with the given key.

Additional operations might include:

- **ascend():** Traverse elements in ascending order.
- **get(index):** Access element by position.
- **remove(index):** Remove element by position.

To efficiently support these operations, especially when the data changes dynamically, we use **balanced search trees**. These trees maintain a structure that keeps their height small relative to the number of nodes, ensuring operations like search, insert, and delete remain fast (typically O(log n)).

There are different types of balanced trees:

- **Height Balanced:** AVL trees
- **Weight Balanced**
- **Degree Balanced:** 2-3 trees, 2-3-4 trees, red-black trees, B-trees

This note focuses primarily on **AVL trees** and **red-black trees**, two popular height-balanced binary search trees.


### 2. 🌲 AVL Trees: Definition and Properties

#### What is an AVL Tree?

An **AVL tree** is a type of binary search tree where the heights of the two child subtrees of any node differ by at most 1. This difference is called the **balance factor**.

- For every node $x$, the **balance factor** is defined as:


$$
\text{balance factor}(x) = \text{height(left subtree)} - \text{height(right subtree)}
$$


- The balance factor can only be -1, 0, or 1 for the tree to be considered balanced.

#### Why is this important?

Maintaining this balance ensures the tree remains approximately balanced, preventing it from degenerating into a linked list (which would have O(n) operations). This balance guarantees that the height of the AVL tree is always logarithmic in the number of nodes, specifically:


$$
\log_2 (n+1) \leq \text{height} \leq 1.44 \log_2 (n+2)
$$


This means the height grows slowly as the number of nodes increases, keeping operations efficient.


### 3. 📏 Height Bound and Fibonacci Connection

#### Understanding the Height Bound

To understand why the height is bounded by approximately $1.44 \log_2 n$, consider:

- Let $N_h$ be the minimum number of nodes in an AVL tree of height $h$.
- For an AVL tree of height $h$, its two subtrees have heights $h-1$ and $h-2$ (because the balance factor is at most 1).
- Therefore:


$$
N_h = 1 + N_{h-1} + N_{h-2}
$$


This recurrence relation is similar to the Fibonacci sequence, where each term is the sum of the two preceding terms plus one for the root node.

#### Fibonacci Numbers and AVL Trees

- The Fibonacci sequence grows exponentially, approximately as:


$$
F_i \approx \frac{\phi^i}{\sqrt{5}}
$$


where $\phi = \frac{1 + \sqrt{5}}{2} \approx 1.618$ is the golden ratio.

- Because $N_h$ grows like Fibonacci numbers, the height $h$ grows logarithmically with the number of nodes $n$.

This mathematical relationship explains why AVL trees maintain a good balance and efficient height.


### 4. 🔄 Insertion in AVL Trees and Rebalancing

#### How Insertion Works

When inserting a new node:

1. Insert the node as in a normal binary search tree.
2. Retrace the path from the inserted node back to the root, updating balance factors.
3. If any node's balance factor becomes 2 or -2, the tree is unbalanced and needs rebalancing.

#### Identifying the Unbalanced Node (A-Node)

- The **A-node** is the nearest ancestor of the inserted node whose balance factor becomes +2 or -2 after insertion.
- Before insertion, all nodes between the new node and A had balance factors of 0.

#### Types of Imbalance

There are four cases depending on where the new node was inserted relative to the A-node:

- **RR (Right-Right):** New node inserted into the right subtree of the right child of A.
- **LL (Left-Left):** New node inserted into the left subtree of the left child of A.
- **RL (Right-Left):** New node inserted into the left subtree of the right child of A.
- **LR (Left-Right):** New node inserted into the right subtree of the left child of A.

#### Rotations to Fix Imbalance

- **Single Rotations:** Fix RR and LL imbalances.
- **Double Rotations:** Fix RL and LR imbalances.

##### Single Rotation Example: LL Rotation

- Rotate the subtree right around A.
- This restores balance and the subtree height remains unchanged.
- No further adjustments are needed.

##### Double Rotation Example: LR Rotation

- First, rotate left around the left child of A.
- Then, rotate right around A.
- This restores balance and subtree height remains unchanged.


### 5. ❌ Deletion in AVL Trees and Rebalancing

#### How Deletion Works

When deleting a node:

1. Delete the node as in a normal binary search tree.
2. Let $q$ be the parent of the deleted node.
3. Retrace the path from $q$ back to the root, updating balance factors.

#### Updating Balance Factors After Deletion

- If deletion was from the left subtree of $q$, then:


$$
\text{balance factor}(q) = \text{old bf}(q) - 1
$$


- If deletion was from the right subtree of $q$, then:


$$
\text{balance factor}(q) = \text{old bf}(q) + 1
$$


#### Possible Outcomes

- New balance factor = ±1: Height of subtree rooted at $q$ unchanged.
- New balance factor = 0: Height of subtree rooted at $q$ decreased by 1.
- New balance factor = ±2: Tree is unbalanced at $q$, needs rebalancing.

#### Imbalance Types After Deletion

- Let $A$ be the ancestor where imbalance occurs.
- If deletion was from left subtree of $A$, imbalance type is **L**.
- If deletion was from right subtree of $A$, imbalance type is **R**.

#### Rotations for Deletion Imbalance

- **R0 Rotation:** Similar to LL rotation, subtree height unchanged, no further adjustments.
- **R1 Rotation:** Subtree height reduced by 1, continue rebalancing up the tree.
- **R-1 Rotation:** Similar to LR rotation, subtree height reduced by 1, continue rebalancing.

#### Number of Rotations

- At most 1 rotation needed for insertion.
- Up to O(log n) rotations may be needed for deletion.


### 6. 🟥 Red-Black Trees: Overview and Properties

#### What is a Red-Black Tree?

A **red-black tree** is a binary search tree with an extra bit of storage per node: its color, which can be either red or black. This coloring enforces balance with the following rules:

- The root and all external (null) nodes are black.
- No path from root to leaf has two consecutive red nodes.
- Every path from root to leaf has the same number of black nodes.

#### Why Use Red-Black Trees?

They provide a balanced tree structure with guaranteed logarithmic height:


$$
\log_2 (n+1) \leq \text{height} \leq 2 \log_2 (n+1)
$$


This ensures efficient search, insert, and delete operations.


### 7. 🔧 Insertions and Deletions in Red-Black Trees

#### Insertion

- Insert the new node as in a binary search tree.
- Color the new node red.
- If this causes two consecutive red nodes, fix by:
  - **Color flips:** Change colors of nodes to maintain properties.
  - **Rotations:** Similar to AVL rotations (LL, LR, RR, RL) to restore balance.

#### Classification of Red-Red Violations

- Use notation $XYz$ to describe relationships:
  - $X$: Relationship between grandparent (gp) and parent (pp) (L or R).
  - $Y$: Relationship between parent (pp) and node (p) (L or R).
  - $z$: Color of sibling node (black or red).

- Depending on the case, apply color flips or rotations.

#### Deletion

- Delete as in a normal binary search tree.
- If a red node is deleted, no rebalancing needed.
- If a black node is deleted, the subtree becomes "black deficient" and needs fixing.

#### Fixing Black Deficiency

- Several cases depending on the colors and positions of sibling nodes.
- Use rotations and color changes to restore red-black properties.
- The process may continue up the tree until balance is restored.


### 8. ⚙️ Practical Considerations and Performance

- **AVL trees** require at most one rotation per insertion but can require up to O(log n) rotations per deletion.
- **Red-black trees** require at most one rotation and O(log n) color flips per insertion or deletion.
- Red-black trees are often preferred in practice because they are easier to implement and maintain.
- Many standard libraries use red-black trees internally, e.g., C++ STL `std::map` and Java's `java.util.TreeMap`.


### Summary

- **AVL trees** maintain strict height balance using balance factors and rotations, ensuring very tight height bounds.
- **Red-black trees** use node colors and relaxed balancing rules to maintain balance with fewer rotations.
- Both support efficient dynamic dictionary operations with guaranteed logarithmic time complexity.
- Understanding rotations and balance factor updates is key to mastering these data structures.