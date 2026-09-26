## 11. Splay Trees

## Key Points

#### 1. 🌳 Splay Trees Overview  
- Search, insert, delete, and split operations have **amortized complexity O(log n)** and worst-case actual complexity O(n).  
- Join operation has **amortized and actual complexity O(1)**.  
- Splay trees outperform heaps and deaps in priority queue operations over sequences of operations.  
- Two main varieties: **Bottom-Up** and **Top-Down** splay trees.

#### 2. 🔄 Bottom-Up Splay Trees  
- Operations (search, insert, delete, join) are done like in an unbalanced BST, followed by a splay operation.  
- The splay operation moves the **splay node** to the root after the main operation.  
- Join requires no splay or a null splay.  
- Split operation involves splaying in the middle of the operation.  
- Splay node depends on the operation:  
  - Search: node with key k or parent of external node where search ends.  
  - Insert: newly inserted node or existing node with the same key.  
  - Delete: parent of physically deleted node or parent of external node if not found.  
  - Split: same as insert splay node.  
- Splay steps move the splay node up one or two levels until it becomes root.  
- Worst-case height can be n, leading to O(n) actual complexity per operation.

#### 3. 🔝 Top-Down Splay Trees  
- Splaying is done **during the descent** down the tree, splitting it into two BSTs: S (smaller elements) and B (bigger elements).  
- Rotations are performed whenever LL or RR moves occur during descent.  
- Moves down two levels at a time, except possibly one level at the end.  
- After reaching the splay node, S, B, and the splay node’s subtree are combined into one BST.  
- Top-down splay trees are generally faster than bottom-up splay trees.

#### 4. ⚙️ Key Operations and Splay Nodes  
- Search, insert, delete, and split all identify a splay node which is then splayed to the root.  
- Join operation does not require splaying.  
- Split operation involves inserting a new key and then splaying it to root, splitting the tree into left and right subtrees.

#### 5. 📊 Complexity and Performance  
- Amortized complexity of search, insert, delete, and split is **O(log n)**.  
- Actual worst-case complexity of these operations is **O(n)** due to possible tree height.  
- Join operation has **O(1)** amortized and actual complexity.  
- Splay trees adapt to usage patterns, improving access times for frequently accessed nodes.



<br>

