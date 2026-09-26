## 10. B-Trees

## Key Points

#### 1. 🌳 B-Trees Basics  
- B-trees are m-way search trees optimized for disk storage with large node degrees.  
- Root has at least 2 children if the tree is not empty.  
- All other internal nodes have at least $\lceil m/2 \rceil$ children.  
- All external (leaf) nodes are at the same level, ensuring balance.

#### 2. 📏 Height and Capacity of B-Trees  
- Maximum number of pairs in a full m-way tree of height $h$ is $m^h - 1$.  
- Minimum number of pairs $n$ satisfies: $n + 1 \geq 2 \times \lceil m/2 \rceil^{h-1}$.  
- Height $h$ is bounded by: $h \leq \log_{\lceil m/2 \rceil} \left(\frac{n+1}{2}\right) + 1$.

#### 3. ⚙️ Insertion in B-Trees  
- Inserting into a full leaf node triggers a bottom-up node splitting process.  
- The middle key of the full node moves up to the parent during a split.  
- Splitting can propagate up to the root, possibly increasing tree height by 1.

#### 4. 🗑️ Deletion in B-Trees  
- Deletion from a leaf node may cause underflow (too few keys).  
- Underflow is fixed by borrowing a key from a sibling or merging with a sibling and parent key.  
- If the root becomes empty after deletion, it is discarded and the height decreases by 1.

#### 5. 💾 Disk Access Performance  
- AVL trees with $n \approx 10^9$ keys have height 30–43, causing up to 43 disk accesses per search (~4 seconds).  
- Red-Black trees with $n \approx 10^9$ keys have height 30–60, causing up to 60 disk accesses per search (~6 seconds).  
- B-trees reduce height by increasing node degree, minimizing disk accesses.

#### 6. 🔢 B-Tree Orders and Examples  
- 2-3 tree is a B-tree of order 3.  
- 2-3-4 tree is a B-tree of order 4.  
- B-tree of order 5 is called a 3-4-5 tree (root may be a 2-node).  
- B-tree of order 2 is a full binary tree.

#### 7. 🔗 B+-Trees  
- B+-trees store all dictionary pairs in leaf nodes only.  
- Internal nodes contain only keys to guide searches.  
- Leaves are linked in a doubly-linked list for efficient range queries.

#### 8. ⚖️ Choice of Order $m$  
- Worst-case search time is approximately $(a + b \times m + c \times \log_2 m) \times h$, where $a, b, c$ are constants.  
- Increasing $m$ reduces height $h$ but increases node search time.

#### 9. 🔄 Disk Accesses During Insertions  
- On insertion, $h$ nodes are read on the way down.  
- On the way up, $2s + 1$ nodes are written, where $s$ is the number of splits.  
- Maximum disk accesses per insertion is $3h + 1$.



<br>

