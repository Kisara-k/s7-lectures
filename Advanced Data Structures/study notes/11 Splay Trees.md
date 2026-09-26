## 11. Splay Trees

## Study Notes

### 1. 🌳 Introduction to Splay Trees

Splay trees are a special kind of **binary search tree (BST)** designed to improve the efficiency of common operations like search, insert, delete, split, and join. Unlike regular BSTs, splay trees use a technique called **splaying** to move frequently accessed elements closer to the root, which helps speed up future operations on those elements.

The key idea behind splay trees is that while individual operations might sometimes take longer (up to O(n) in the worst case), the **amortized complexity** — the average time per operation over a sequence of operations — is much better, specifically O(log n). This means that although some operations might be slow, most will be fast, making splay trees efficient in practice.

Splay trees also have efficient implementations of priority queues and double-ended priority queues, often outperforming other data structures like heaps or deaps when performing many operations in sequence.

There are two main varieties of splay trees:
- **Bottom-Up Splay Trees**
- **Top-Down Splay Trees**

Both achieve similar goals but differ in how they perform the splaying operation.


### 2. 🔄 Bottom-Up Splay Trees: How They Work

Bottom-up splay trees perform operations like search, insert, delete, and join similarly to an unbalanced binary search tree. However, after these operations, a **splay operation** is performed to move a specific node (called the **splay node**) up to the root of the tree.

#### What is the Splay Node?

The splay node depends on the operation:

- **Search(k):**  
  If the key `k` is found, the node containing `k` is the splay node.  
  If not found, the splay node is the parent of the external node where the search ended.

- **Insert(newPair):**  
  If the key already exists, the node with that key is the splay node.  
  Otherwise, the newly inserted node is the splay node.

- **Delete(k):**  
  If the key exists, the splay node is the parent of the node physically deleted.  
  If not found, the splay node is the parent of the external node where the search ended.

- **Split(k):**  
  Insert a new pair with key `k` using the unbalanced BST insert method.  
  The splay node is the same as in insert.  
  After splaying, the left subtree of the root is one part of the split, and the right subtree is the other.

#### The Splay Operation

The splay operation moves the splay node `q` up to the root through a series of **splay steps**. Each step moves `q` up either one or two levels in the tree.

- If `q` is already the root or null, the splay is done.
- If `q` is at level 2 (one level below the root), a one-level move is done, and the splay ends.
- If `q` is deeper than level 2, a two-level move is performed, and the splay continues.

These moves involve rotations that restructure the tree to bring `q` closer to the root efficiently.

#### Complexity of Bottom-Up Splay Trees

- The worst-case height of a splay tree can be as large as `n` (the number of nodes), meaning some operations can take O(n) time.
- However, the **amortized complexity** of search, insert, delete, and split is O(log n), meaning that over many operations, the average time per operation is logarithmic.


### 3. 🔝 Top-Down Splay Trees: A Different Approach

Top-down splay trees perform the splay operation **while descending the tree**, rather than after reaching the splay node as in bottom-up trees.

#### How Top-Down Splaying Works

As you move down the tree searching for the splay node, the tree is split into two smaller BSTs:

- **S:** Contains all elements smaller than the splay node.
- **B:** Contains all elements bigger than the splay node.

This splitting is similar to the split operation in an unbalanced BST but with an important difference: **rotations are performed whenever certain patterns (LL or RR moves) are encountered**. These rotations help maintain balance and speed up the splaying process.

The descent moves down two levels at a time, except possibly at the end where a one-level move might be made.

Once the splay node is reached, the two trees `S` and `B` and the subtree rooted at the splay node are combined back into a single BST.

#### Two-Level Moves in Top-Down Splaying

During the descent, the algorithm performs specific moves:

- **RL move:** Moving from one node to another in a right-left pattern.
- **RR move:** Moving in a right-right pattern.
- **L move:** Moving left towards the splay node.

These moves involve rotations that help restructure the tree efficiently as the splay node is approached.

#### Performance Comparison

Top-down splay trees are generally faster than bottom-up splay trees because they perform restructuring during the descent, avoiding some of the overhead of bottom-up splaying.


### 4. ⚙️ Key Operations in Splay Trees

Let's look at the main operations and how splay trees handle them:

#### Search

- Perform a standard BST search.
- Identify the splay node (found node or parent of the external node).
- Splay the splay node to the root.
- Result: The searched node is now at the root, making future accesses faster.

#### Insert

- Insert the new node as in a BST.
- Identify the splay node (newly inserted node or existing node with the same key).
- Splay the splay node to the root.
- Result: The inserted node is at the root.

#### Delete

- Search for the node to delete.
- If found, delete it as in a BST.
- Identify the splay node (parent of the deleted node or parent of the external node if not found).
- Splay the splay node to the root.
- Result: The tree remains balanced with the splay node at the root.

#### Split

- Insert a new node with key `k` (if not already present).
- Splay the splay node to the root.
- The left subtree of the root becomes one part of the split.
- The right subtree becomes the other part.
- Result: The tree is split into two BSTs based on key `k`.

#### Join

- Join two BSTs by making one the right subtree of the other.
- No splay is needed (or a null splay is done).
- Result: Efficient O(1) amortized join operation.


### 5. 📊 Complexity and Practical Considerations

- **Amortized Complexity:**  
  Most operations (search, insert, delete, split) have an amortized time complexity of O(log n). This means that while some individual operations might be slow, the average time over many operations is efficient.

- **Actual Complexity:**  
  In the worst case, the height of the tree can be as large as `n`, leading to O(n) time for some operations.

- **Join Operation:**  
  Join operations are very efficient, with an amortized complexity of O(1).

- **Performance in Practice:**  
  Splay trees often outperform other priority queue implementations like heaps or deaps when performing many operations in sequence because of their self-adjusting nature.


### 6. 🔄 Summary: Bottom-Up vs Top-Down Splay Trees

- **Bottom-Up Splay Trees:**  
  Perform splaying after the main operation by moving the splay node up to the root through rotations.  
  Simpler conceptually but can be slower in practice.

- **Top-Down Splay Trees:**  
  Perform splaying during the descent by splitting the tree into smaller parts and performing rotations on the way down.  
  Generally faster and more efficient in practice.

Both achieve the same goal: keeping frequently accessed nodes near the root to speed up future operations.


### Final Thoughts

Splay trees are a powerful and elegant data structure that adapt dynamically to usage patterns. By moving accessed nodes closer to the root, they optimize the tree structure for the sequence of operations performed, offering good average-case performance even if some individual operations are costly. Understanding both bottom-up and top-down splaying gives a solid foundation for implementing and using splay trees effectively.