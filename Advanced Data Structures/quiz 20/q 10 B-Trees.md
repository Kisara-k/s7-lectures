## 10. B-Trees

## Questions

#### 1. Which of the following statements about B-trees are true?  
A) The root of a non-empty B-tree must have at least m children.  
B) B-trees are always binary search trees.  
C) All external (failure) nodes in a B-tree are at the same level.  
D) B-trees of order m have internal nodes with at least ceil(m/2) children, except possibly the root.  

#### 2. For a B-tree of order m, what is the maximum number of pairs (keys) in a full degree m tree of height h?  
A) $m^{h-1}$  
B) $(m-1) \times (1 + m + m^2 + \cdots + m^{h-1})$  
C) $m^h - 1$  
D) $(m-1)^h$  

#### 3. Consider an m-way search tree with height h and n pairs. Which inequality correctly relates n, h, and m?  
A) $n + 1 \geq 2 \times \lceil m/2 \rceil^{h-1}$  
B) $h \geq \log_m (n)$  
C) $h \leq \log_{\lceil m/2 \rceil} \frac{n+1}{2} + 1$  
D) $n \leq 2 \times \lceil m/2 \rceil^{h}$  

#### 4. Why are AVL and Red-Black trees considered inefficient for very large dictionaries stored on disk?  
A) They do not guarantee balanced height.  
B) They require too much memory to store.  
C) Their height can be too large, causing many disk accesses per search.  
D) Disk access times accumulate to several seconds per search.  

#### 5. Which of the following correctly describe the insertion process in a B-tree when inserting into a full leaf node?  
A) The node is split around the middle key.  
B) The insertion always causes the tree height to increase.  
C) The middle key is promoted to the parent node.  
D) The new key is inserted into the parent node directly without splitting.  

#### 6. In a 2-3 tree, what is the minimum number of children an internal node (other than the root) must have?  
A) ceil(3/2)  
B) 3  
C) 2  
D) 1  

#### 7. Which of the following statements about 2-3-4 trees are true?  
A) Internal nodes can have between 2 and 4 children.  
B) The root must always have at least 3 children.  
C) They are B-trees of order 4.  
D) External nodes are all at the same level.  

#### 8. When splitting an overfull node in a B-tree of order m, which key is promoted to the parent?  
A) The largest key in the node.  
B) The smallest key in the node.  
C) The middle key, specifically the $\lceil m/2 \rceil$-th key.  
D) The key with the highest value.  

#### 9. What is the worst-case number of disk accesses during a B-tree insertion if s nodes split and the tree height is h?  
A) $2h + s$  
B) $h + 2s + 1$  
C) $h + s$  
D) $3h + 1$  

#### 10. Which of the following are true about B+-trees compared to B-trees?  
A) Internal nodes store all dictionary pairs.  
B) Dictionary pairs are stored only in the leaves.  
C) Leaves form a doubly-linked list.  
D) B+-trees have the same structure as B-trees except for data storage.  

#### 11. During deletion in a 2-3 tree, if a 2-node becomes deficient, what are the possible corrective actions?  
A) Borrow a pair and subtree from an adjacent 3-node sibling via the parent.  
B) Replace the deficient node with the largest key from its left subtree.  
C) Merge with an adjacent sibling and the parent pair.  
D) Immediately discard the deficient node without further action.  

#### 12. In a B-tree of order 5, which of the following is true?  
A) The root may be a 2-node.  
B) It is equivalent to a full binary tree.  
C) The minimum number of children for internal nodes (except root) is 3.  
D) All internal nodes must have exactly 5 children.  

#### 13. Which of the following correctly describe the height bounds for AVL and Red-Black trees with approximately $10^9$ nodes?  
A) AVL tree height is between 30 and 43.  
B) Both trees require fewer than 10 disk accesses per search.  
C) AVL trees have worse height bounds than Red-Black trees.  
D) Red-Black tree height is between 30 and 60.  

#### 14. When inserting a key into a 3-node in a 2-3 tree, what happens if the node overflows?  
A) The tree height always increases.  
B) The node is split into two nodes around the middle key.  
C) The middle key is inserted into the parent node.  
D) The new key is discarded if it causes overflow.  

#### 15. Which of the following statements about the minimum number of pairs in an m-way search tree are correct?  
A) The minimum number of pairs is independent of m.  
B) The number of external nodes is $n + 1$ where n is the number of pairs.  
C) The height h satisfies $h \leq \log_{\lceil m/2 \rceil} \frac{n+1}{2} + 1$.  
D) The minimum number of pairs grows exponentially with height h.  

#### 16. In the context of B-trees, what does the term "external (or failure) nodes" refer to?  
A) Null pointers or placeholders for missing children.  
B) Nodes that contain no keys and no children.  
C) Leaf nodes that store dictionary pairs.  
D) Nodes at the lowest level of the tree.  

#### 17. Which of the following factors influence the worst-case search time in a B-tree?  
A) The number of siblings of the node.  
B) Time to search within a node (linear or binary search).  
C) The height of the tree.  
D) Time to fetch a node from disk.  

#### 18. During deletion in a B+-tree, if an index node becomes deficient, what are the possible steps to fix it?  
A) Immediately discard the deficient node without further action.  
B) Replace the deficient node with a leaf node.  
C) Borrow a key from a sibling and update the parent key.  
D) Merge with a sibling and delete the in-between key in the parent.  

#### 19. Which of the following statements about the height change during insertion and deletion in B-trees are true?  
A) Height always remains constant during deletion.  
B) Deletion can reduce the height by 1 if the root is discarded.  
C) Insertion can increase the height by 1 if the root splits.  
D) Height always remains constant during insertion.  

#### 20. Consider a B-tree of order 2. Which of the following are true?  
A) The minimum number of children for internal nodes (except root) is 1.  
B) Each internal node has at least 1 child.  
C) It behaves identically to a 2-3 tree.  
D) It is a full binary tree.  



<br>

## Answers

#### 1. Which of the following statements about B-trees are true?  
A) ✗ Root must have at least 2 children if not empty, not necessarily m children.  
B) ✗ B-trees are m-way search trees, not necessarily binary.  
C) ✓ All external (failure) nodes are at the same level by definition.  
D) ✓ B-trees require internal nodes (except root) to have at least ceil(m/2) children.  

**Correct:** C, D


#### 2. For a B-tree of order m, what is the maximum number of pairs (keys) in a full degree m tree of height h?  
A) ✗ $m^{h-1}$ is number of nodes at level h-1, not total pairs.  
B) ✓ Total pairs = (m-1) times total nodes = $(m-1)(1 + m + \cdots + m^{h-1})$.  
C) ✗ $m^h - 1$ counts nodes, not pairs.  
D) ✗ $(m-1)^h$ is incorrect growth formula.  

**Correct:** B


#### 3. Consider an m-way search tree with height h and n pairs. Which inequality correctly relates n, h, and m?  
A) ✓ $n + 1 \geq 2 \times \lceil m/2 \rceil^{h-1}$ is the minimum number of external nodes.  
B) ✗ Height bound depends on ceil(m/2), not m directly.  
C) ✓ Rearranged form for height bound: $h \leq \log_{\lceil m/2 \rceil} \frac{n+1}{2} + 1$.  
D) ✗ Inequality direction and exponent incorrect.  

**Correct:** A, C


#### 4. Why are AVL and Red-Black trees considered inefficient for very large dictionaries stored on disk?  
A) ✗ Both guarantee balanced height.  
B) ✗ Memory size is not the main issue here.  
C) ✓ Their height causes many disk accesses per search.  
D) ✓ Disk access times accumulate to seconds, which is unacceptable.  

**Correct:** C, D


#### 5. Which of the following correctly describe the insertion process in a B-tree when inserting into a full leaf node?  
A) ✓ Node is split around the middle key.  
B) ✗ Height increases only if root splits, not always.  
C) ✓ Middle key is promoted to the parent.  
D) ✗ New key is not inserted directly into parent without splitting.  

**Correct:** A, C


#### 6. In a 2-3 tree, what is the minimum number of children an internal node (other than the root) must have?  
A) ✓ ceil(3/2) = 2, so same as B.  
B) ✗ 3 is maximum, not minimum.  
C) ✓ Minimum is 2 children (since order 3, ceil(3/2) = 2).  
D) ✗ Minimum is not 1.  

**Correct:** A, C


#### 7. Which of the following statements about 2-3-4 trees are true?  
A) ✓ Internal nodes can have 2 to 4 children.  
B) ✗ Root must have at least 2 children, not necessarily 3.  
C) ✓ 2-3-4 trees are B-trees of order 4.  
D) ✓ External nodes are all at the same level.  

**Correct:** A, C, D


#### 8. When splitting an overfull node in a B-tree of order m, which key is promoted to the parent?  
A) ✗ Largest key is not promoted.  
B) ✗ Smallest key is not promoted.  
C) ✓ The middle key, specifically the $\lceil m/2 \rceil$-th key, is promoted.  
D) ✗ Highest value key is not necessarily the middle.  

**Correct:** C


#### 9. What is the worst-case number of disk accesses during a B-tree insertion if s nodes split and the tree height is h?  
A) ✗ Formula incorrect.  
B) ✓ Total disk accesses = $h + 2s + 1$.  
C) ✗ Formula incomplete.  
D) ✓ Max is $3h + 1$ (worst case when s = h).  

**Correct:** B, D


#### 10. Which of the following are true about B+-trees compared to B-trees?  
A) ✗ Internal nodes do not store all dictionary pairs, only keys for routing.  
B) ✓ Dictionary pairs stored only in leaves.  
C) ✓ Leaves form a doubly-linked list.  
D) ✓ Structure is similar except for data storage location.  

**Correct:** B, C, D


#### 11. During deletion in a 2-3 tree, if a 2-node becomes deficient, what are the possible corrective actions?  
A) ✓ Borrow from adjacent 3-node sibling via parent.  
B) ✗ Replacement by largest in left subtree applies to internal node deletion, not deficiency fix.  
C) ✓ Merge with sibling and parent pair if borrowing not possible.  
D) ✗ Deficient node cannot be discarded immediately.  

**Correct:** A, C


#### 12. In a B-tree of order 5, which of the following is true?  
A) ✓ Root may be a 2-node (less than ceil(5/2) children).  
B) ✗ Not a binary tree.  
C) ✓ Minimum children for internal nodes (except root) is 3.  
D) ✗ Internal nodes must have at least ceil(5/2) = 3 children, not exactly 5.  

**Correct:** A, C


#### 13. Which of the following correctly describe the height bounds for AVL and Red-Black trees with approximately $10^9$ nodes?  
A) ✓ AVL height between 30 and 43.  
B) ✗ Both require many disk accesses (30+), not fewer than 10.  
C) ✗ AVL trees have better (lower) height bounds than Red-Black trees.  
D) ✓ Red-Black height between 30 and 60.  

**Correct:** A, D


#### 14. When inserting a key into a 3-node in a 2-3 tree, what happens if the node overflows?  
A) ✗ Height increases only if root splits.  
B) ✓ Node splits into two nodes around the middle key.  
C) ✓ Middle key is inserted into the parent.  
D) ✗ New key is never discarded.  

**Correct:** B, C


#### 15. Which of the following statements about the minimum number of pairs in an m-way search tree are correct?  
A) ✗ Minimum pairs depend on m.  
B) ✓ Number of external nodes = n + 1.  
C) ✓ Height bound: $h \leq \log_{\lceil m/2 \rceil} \frac{n+1}{2} + 1$.  
D) ✓ Minimum pairs grow exponentially with height h.  

**Correct:** B, C, D


#### 16. In the context of B-trees, what does the term "external (or failure) nodes" refer to?  
A) ✓ External nodes are null or failure nodes.  
B) ✓ Null pointers or placeholders for missing children.  
C) ✗ Leaves store dictionary pairs, not external nodes.  
D) ✗ External nodes are not necessarily the lowest level nodes with data.  

**Correct:** A, B


#### 17. Which of the following factors influence the worst-case search time in a B-tree?  
A) ✗ Number of siblings does not affect search time.  
B) ✓ Time to search within a node (linear or binary search).  
C) ✓ Height of the tree.  
D) ✓ Time to fetch a node from disk.  

**Correct:** B, C, D


#### 18. During deletion in a B+-tree, if an index node becomes deficient, what are the possible steps to fix it?  
A) ✗ Cannot discard deficient node immediately without fix.  
B) ✗ Deficient index node is not replaced by leaf node.  
C) ✓ Borrow a key from sibling and update parent key.  
D) ✓ Merge with sibling and delete in-between key in parent.  

**Correct:** C, D


#### 19. Which of the following statements about the height change during insertion and deletion in B-trees are true?  
A) ✗ Height can change during deletion.  
B) ✓ Deletion can reduce height by 1 if root is discarded.  
C) ✓ Insertion can increase height by 1 if root splits.  
D) ✗ Height can change during insertion.  

**Correct:** B, C


#### 20. Consider a B-tree of order 2. Which of the following are true?  
A) ✗ Minimum children for internal nodes (except root) is 1, but root must have at least 2 children if not empty.  
B) ✗ Internal nodes must have at least ceil(2/2) = 1 child, but root must have at least 2 if not empty.  
C) ✗ It is not equivalent to a 2-3 tree (order 3).  
D) ✓ It is a full binary tree.  

**Correct:** D