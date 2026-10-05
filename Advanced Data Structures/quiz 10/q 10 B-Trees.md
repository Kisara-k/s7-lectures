## 10. B-Trees

## Questions

#### 1. Which of the following statements about B-trees are true?  
A) A B-tree of order 2 is equivalent to a full binary tree.  
B) All external (failure) nodes in a B-tree are at the same level.  
C) The root of a non-empty B-tree must have at least two children.  
D) A B-tree of order m is an m-way search tree where every internal node (except the root) has at least ceil(m/2) children.  

#### 2. Considering search performance on disk-based dictionaries, why are AVL and Red-Black trees generally not acceptable for very large datasets?  
A) Both AVL and Red-Black trees have a high number of cache misses due to their small node sizes.  
B) Red-Black trees have a height that can be up to twice that of AVL trees, leading to up to 60 disk accesses per search.  
C) AVL trees can require up to 43 disk accesses per search, causing delays of approximately 4 seconds.  
D) B-trees reduce disk accesses by having nodes with large degrees, minimizing tree height.  

#### 3. For an m-way search tree of height h, which of the following correctly describes the maximum number of pairs it can contain when all internal nodes are full m-nodes?  
A) The number of nodes is given by 1 + m + m² + ... + m^(h-1).  
B) The height h satisfies h ≤ log base ceil(m/2) of ((n+1)/2) + 1, where n is the number of pairs.  
C) Each node contains m pairs, so total pairs = m * number of nodes.  
D) The total number of pairs is m^h - 1.  

#### 4. When inserting a new pair into a full leaf node of a B-tree, which of the following steps occur?  
A) The middle key and a pointer to the new node are inserted into the parent node.  
B) The insertion always causes the tree height to increase by one.  
C) If the parent node is full, the splitting process propagates upward recursively.  
D) The node is split around the middle key.  

#### 5. Which of the following correctly describe the worst-case disk access cost for inserting a key into a B-tree of height h?  
A) The worst-case disk accesses are independent of the number of splits during insertion.  
B) The number of write accesses on the way up is 2s + 1, where s is the number of nodes that split.  
C) The total disk accesses can be as high as 3h + 1.  
D) The number of read accesses on the way down is h.  

#### 6. In a 2-3 tree, what happens when deleting a key from a 2-node leaf that has no adjacent 3-node siblings?  
A) The node combines with a sibling and the parent pair to form a new node.  
B) The node borrows a pair and subtree from an adjacent sibling via the parent.  
C) The height of the tree increases by one.  
D) The root is discarded if it becomes empty, and its single child becomes the new root.  

#### 7. Which of the following statements about B+-trees are correct?  
A) All dictionary pairs are stored only in the leaves.  
B) Internal nodes store keys that are the smallest keys in their respective subtrees.  
C) Leaves are linked together in a doubly-linked list.  
D) B+-trees do not require splitting nodes during insertion.  

#### 8. During deletion in a B+-tree, if an index node becomes deficient, which of the following actions may be taken?  
A) Borrow a key from a sibling and move the last key to the parent.  
B) Update parent keys to reflect changes in the subtree keys.  
C) Always discard the root node regardless of its content.  
D) Merge the deficient node with a sibling and delete the in-between key in the parent.  

#### 9. Regarding the choice of order m in a B-tree, which factors influence the worst-case search time?  
A) The number of children per node does not affect search time.  
B) The height of the tree, which decreases as m increases.  
C) The time to fetch a node from disk or memory.  
D) The time to search within a node, which depends on m.  

#### 10. Which of the following correctly describe the relationship between 2-3 trees, 2-3-4 trees, and B-trees?  
A) A 2-3-4 tree is a B-tree of order 4.  
B) A B-tree of order 2 is equivalent to a 2-3 tree.  
C) A 2-3 tree is a B-tree of order 3.  
D) A B-tree of order 5 is also called a 3-4-5 tree, but the root may be a 2-node.  



<br>

## Answers

#### 1. Which of the following statements about B-trees are true?  
A) ✓ B-tree of order 2 is a full binary tree by definition.  
B) ✓ All external (failure) nodes are at the same level in a B-tree.  
C) ✓ Root of a non-empty B-tree must have at least two children (except when it is a leaf).  
D) ✓ B-tree definition requires internal nodes (except root) to have at least ceil(m/2) children.  

**Correct:** A, B, C, D


#### 2. Considering search performance on disk-based dictionaries, why are AVL and Red-Black trees generally not acceptable for very large datasets?  
A) ✗ Cache misses are not the main reason given; the issue is disk access count.  
B) ✓ Red-Black trees can have height up to 60, causing up to 60 disk accesses (~6 seconds).  
C) ✓ AVL trees can require up to 43 disk accesses, causing slow searches (~4 seconds).  
D) ✓ B-trees reduce disk accesses by having large node degrees, lowering height and disk reads.  

**Correct:** B, C, D


#### 3. For an m-way search tree of height h, which of the following correctly describes the maximum number of pairs it can contain when all internal nodes are full m-nodes?  
A) ✓ Number of nodes is geometric series: 1 + m + m² + ... + m^(h-1).  
B) ✓ Height bound h ≤ log base ceil(m/2) of ((n+1)/2) + 1 is correct for minimum pairs.  
C) ✗ Each node has m-1 pairs, not m pairs.  
D) ✓ Total pairs = m^h - 1 (since each node has m-1 pairs and total nodes sum to m^h).  

**Correct:** A, B, D


#### 4. When inserting a new pair into a full leaf node of a B-tree, which of the following steps occur?  
A) ✓ Middle key and pointer to new node are inserted into the parent node.  
B) ✗ Height increases only if splitting propagates to the root, not always.  
C) ✓ If parent is full, splitting propagates upward recursively.  
D) ✓ Node is split around the middle key to maintain balance.  

**Correct:** A, C, D


#### 5. Which of the following correctly describe the worst-case disk access cost for inserting a key into a B-tree of height h?  
A) ✗ Disk accesses depend on number of splits; more splits mean more writes.  
B) ✓ 2s + 1 write accesses on the way up, where s = number of splits.  
C) ✓ Total disk accesses can be as high as 3h + 1 in worst case.  
D) ✓ h read accesses on the way down to find insertion point.  

**Correct:** B, C, D


#### 6. In a 2-3 tree, what happens when deleting a key from a 2-node leaf that has no adjacent 3-node siblings?  
A) ✓ Node combines with sibling and parent pair to fix deficiency.  
B) ✗ Borrowing requires an adjacent 3-node sibling, which is absent here.  
C) ✗ Height reduces by one in this case, not increases.  
D) ✓ If root becomes empty, it is discarded and its single child becomes new root.  

**Correct:** A, D


#### 7. Which of the following statements about B+-trees are correct?  
A) ✓ All dictionary pairs are stored only in leaves in B+-trees.  
B) ✓ Internal nodes store keys that are smallest keys in their subtrees (index entries).  
C) ✓ Leaves form a doubly-linked list for efficient range queries.  
D) ✗ B+-trees require node splitting during insertion like B-trees.  

**Correct:** A, B, C


#### 8. During deletion in a B+-tree, if an index node becomes deficient, which of the following actions may be taken?  
A) ✓ Borrow a key from sibling and move last key to parent to fix deficiency.  
B) ✓ Parent keys are updated to reflect changes in subtree keys after deletion or borrowing.  
C) ✗ Root is discarded only if it becomes empty and has a single child; not always.  
D) ✓ Merge deficient node with sibling and delete in-between key in parent if borrowing not possible.  

**Correct:** A, B, D


#### 9. Regarding the choice of order m in a B-tree, which factors influence the worst-case search time?  
A) ✗ Number of children per node directly affects search time, so it does affect it.  
B) ✓ Height decreases as m increases, reducing number of node accesses.  
C) ✓ Time to fetch a node (disk or memory access) affects search time.  
D) ✓ Time to search within a node depends on m (number of keys per node).  

**Correct:** B, C, D


#### 10. Which of the following correctly describe the relationship between 2-3 trees, 2-3-4 trees, and B-trees?  
A) ✓ 2-3-4 tree is a B-tree of order 4.  
B) ✗ B-tree of order 2 is a full binary tree, not a 2-3 tree.  
C) ✓ 2-3 tree is a B-tree of order 3.  
D) ✓ B-tree of order 5 is called a 3-4-5 tree; root may be a 2-node.  

**Correct:** A, C, D