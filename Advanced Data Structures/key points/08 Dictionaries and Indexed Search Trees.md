## 8. Dictionaries and Indexed Search Trees

## Key Points

#### 1. 📚 Dictionaries
- A dictionary stores items as (key, element) pairs.
- Keys in a dictionary are usually distinct; duplicates allowed in some cases (e.g., word dictionary with multiple meanings).
- Static dictionaries support initialize/create and get (search) operations.
- Dynamic dictionaries support get (search), put (insert), and remove (delete) operations.

#### 2. 🗃️ Hash Table Dictionaries
- Hash tables provide expected O(1) time for get, put, and remove.
- Worst-case time for hash table operations is O(n), or O(log n) if collisions are handled by balanced search trees.
- Hash tables are not suitable for nearest match, range queries, or indexed operations.

#### 3. 📦 Bin Packing and Best Fit Heuristic
- Bin packing aims to minimize the number of bins used to pack items with sizes into bins of capacity c.
- Best Fit heuristic packs each item into the bin with the least available capacity that fits the item.
- If no bin fits, a new bin is started.
- Best Fit can be implemented using a dynamic dictionary keyed by available capacity.
- Complexity of Best Fit packing n items is O(n log n) using balanced binary search trees.

#### 4. 🌳 Indexed Binary Search Trees (BST)
- Each node stores `leftSize`, the number of nodes in its left subtree.
- `leftSize` enables efficient rank-based operations like get(index) in O(log n) time.
- get(index) compares index with leftSize to decide traversal direction.

#### 5. ⚙️ Performance of Indexed Structures
- Arrays provide O(1) get but slow insert/remove.
- Linked chains have slow get (O(n)).
- Indexed AVL Trees (IAVL) provide O(log n) time for get, put, and remove.
- Experimental results show IAVL is significantly faster than chains and competitive with arrays.

#### 6. 🔎 Static Dictionaries and Optimal Binary Search Trees
- Perfect hashing achieves O(1) search time with no collisions.
- Minimal perfect hashing uses space exactly equal to the number of keys.
- Optimal BSTs minimize expected search cost based on key access probabilities.
- Construction of optimal BSTs uses dynamic programming with O(n^3) time complexity, reducible to O(n^2).

#### 7. 🧮 Cost and Construction of Optimal BSTs
- Cost includes weighted path length of internal (successful search) and external (unsuccessful search) nodes.
- Dynamic programming formula:  
  $c_{i,j} = \min_{i < k \leq j} \{ c_{i,k-1} + c_{k,j} \} + w_{i,j}$, where $w_{i,j}$ is sum of probabilities.
- Root $r_{i,j}$ is chosen to minimize cost.

#### 8. 🔄 Dynamic Dictionaries Operations and Complexity
- get, put, remove operations in balanced BSTs have worst-case O(log n) time.
- Hash tables have worst-case O(n) but expected O(1) for these operations.
- Additional operations like ascend(), get(index), remove(index) take O(log n) in indexed balanced BSTs.
- Hash tables require O(D + n log n) for these additional operations, where D is number of buckets.

#### 9. 🪓 Removing Elements from BSTs
- Removing a leaf node: simply delete it.
- Removing a degree 1 node: replace node with its child.
- Removing a degree 2 node: replace node with largest key in left subtree or smallest key in right subtree.
- Replacement node is always a leaf or degree 1 node.
- Removal complexity is O(height of tree).

#### 10. 🌲 Balanced Search Trees
- Balanced trees maintain height O(log n) for efficient operations.
- Types include:
  - Height balanced: AVL trees.
  - Weight balanced.
  - Degree balanced: 2-3 trees, 2-3-4 trees, red-black trees, B-trees.
- Balanced trees support insert, delete, and search in O(log n) time.



<br>

