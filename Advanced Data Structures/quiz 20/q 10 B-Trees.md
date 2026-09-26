## 10. B-Trees

## Questions

#### 1. Which of the following statements about B-trees are true?  
A) B-trees of order m have internal nodes with at least ceil(m/2) children, except possibly the root.  
B) All external (failure) nodes in a B-tree are at the same level.  
C) The root of a non-empty B-tree must have at least m children.  
D) B-trees are always binary search trees.

#### 2. For a B-tree of order m, what is the maximum number of pairs (keys) in a full degree m tree of height h?  
A) $m^h - 1$  
B) $(m-1) \times (1 + m + m^2 + \cdots + m^{h-1})$  
C) $m^{h-1}$  
D) $(m-1)^h$

#### 3. Consider an m-way search tree with height h and n pairs. Which inequality correctly relates n, h, and m?  
A) $n + 1 \geq 2 \times \lceil m/2 \rceil^{h-1}$  
B) $n \leq 2 \times \lceil m/2 \rceil^{h}$  
C) $h \leq \log_{\lceil m/2 \rceil} \frac{n+1}{2} + 1$  
D) $h \geq \log_m (n)$

#### 4. Why are AVL and Red-Black trees considered inefficient for very large dictionaries stored on disk?  
A) Their height can be too large, causing many disk accesses per search.  
B) They require too much memory to store.  
C) They do not guarantee balanced height.  
D) Disk access times accumulate to several seconds per search.

#### 5. Which of the following correctly describe the insertion process in a B-tree when inserting into a full leaf node?  
A) The node is split around the middle key.  
B) The middle key is promoted to the parent node.  
C) The insertion always causes the tree height to increase.  
D) The new key is inserted into the parent node directly without splitting.

#### 6. In a 2-3 tree, what is the minimum number of children an internal node (other than the root) must have?  
A) 1  
B) 2  
C) 3  
D) ceil(3/2)

#### 7. Which of the following statements about 2-3-4 trees are true?  
A) They are B-trees of order 4.  
B) Internal nodes can have between 2 and 4 children.  
C) The root must always have at least 3 children.  
D) External nodes are all at the same level.

#### 8. When splitting an overfull node in a B-tree of order m, which key is promoted to the parent?  
A) The smallest key in the node.  
B) The largest key in the node.  
C) The middle key, specifically the $\lceil m/2 \rceil$-th key.  
D) The key with the highest value.

#### 9. What is the worst-case number of disk accesses during a B-tree insertion if s nodes split and the tree height is h?  
A) $h + 2s + 1$  
B) $3h + 1$  
C) $2h + s$  
D) $h + s$

#### 10. Which of the following are true about B+-trees compared to B-trees?  
A) Dictionary pairs are stored only in the leaves.  
B) Leaves form a doubly-linked list.  
C) Internal nodes store all dictionary pairs.  
D) B+-trees have the same structure as B-trees except for data storage.

#### 11. During deletion in a 2-3 tree, if a 2-node becomes deficient, what are the possible corrective actions?  
A) Borrow a pair and subtree from an adjacent 3-node sibling via the parent.  
B) Merge with an adjacent sibling and the parent pair.  
C) Immediately discard the deficient node without further action.  
D) Replace the deficient node with the largest key from its left subtree.

#### 12. In a B-tree of order 5, which of the following is true?  
A) The root may be a 2-node.  
B) All internal nodes must have exactly 5 children.  
C) The minimum number of children for internal nodes (except root) is 3.  
D) It is equivalent to a full binary tree.

#### 13. Which of the following correctly describe the height bounds for AVL and Red-Black trees with approximately $10^9$ nodes?  
A) AVL tree height is between 30 and 43.  
B) Red-Black tree height is between 30 and 60.  
C) AVL trees have worse height bounds than Red-Black trees.  
D) Both trees require fewer than 10 disk accesses per search.

#### 14. When inserting a key into a 3-node in a 2-3 tree, what happens if the node overflows?  
A) The node is split into two nodes around the middle key.  
B) The middle key is inserted into the parent node.  
C) The tree height always increases.  
D) The new key is discarded if it causes overflow.

#### 15. Which of the following statements about the minimum number of pairs in an m-way search tree are correct?  
A) The number of external nodes is $n + 1$ where n is the number of pairs.  
B) The height h satisfies $h \leq \log_{\lceil m/2 \rceil} \frac{n+1}{2} + 1$.  
C) The minimum number of pairs is independent of m.  
D) The minimum number of pairs grows exponentially with height h.

#### 16. In the context of B-trees, what does the term "external (or failure) nodes" refer to?  
A) Nodes that contain no keys and no children.  
B) Leaf nodes that store dictionary pairs.  
C) Null pointers or placeholders for missing children.  
D) Nodes at the lowest level of the tree.

#### 17. Which of the following factors influence the worst-case search time in a B-tree?  
A) Time to fetch a node from disk.  
B) Time to search within a node (linear or binary search).  
C) The height of the tree.  
D) The number of siblings of the node.

#### 18. During deletion in a B+-tree, if an index node becomes deficient, what are the possible steps to fix it?  
A) Borrow a key from a sibling and update the parent key.  
B) Merge with a sibling and delete the in-between key in the parent.  
C) Immediately discard the deficient node without further action.  
D) Replace the deficient node with a leaf node.

#### 19. Which of the following statements about the height change during insertion and deletion in B-trees are true?  
A) Insertion can increase the height by 1 if the root splits.  
B) Deletion can reduce the height by 1 if the root is discarded.  
C) Height always remains constant during insertion.  
D) Height always remains constant during deletion.

#### 20. Consider a B-tree of order 2. Which of the following are true?  
A) It is a full binary tree.  
B) Each internal node has at least 1 child.  
C) The minimum number of children for internal nodes (except root) is 1.  
D) It behaves identically to a 2-3 tree.



<br>

## Answers

#### 1. Which of the following statements about B-trees are true?  
A) ✓ B-trees require internal nodes (except root) to have at least ceil(m/2) children.  
B) ✓ All external (failure) nodes are at the same level by definition.  
C) ✗ Root must have at least 2 children if not empty, not necessarily m children.  
D) ✗ B-trees are m-way search trees, not necessarily binary.

**Correct:** A,B


#### 2. For a B-tree of order m, what is the maximum number of pairs (keys) in a full degree m tree of height h?  
A) ✗ $m^h - 1$ counts nodes, not pairs.  
B) ✓ Total pairs = (m-1) times total nodes = $(m-1)(1 + m + \cdots + m^{h-1})$.  
C) ✗ $m^{h-1}$ is number of nodes at level h-1, not total pairs.  
D) ✗ $(m-1)^h$ is incorrect growth formula.

**Correct:** B


#### 3. Consider an m-way search tree with height h and n pairs. Which inequality correctly relates n, h, and m?  
A) ✓ $n + 1 \geq 2 \times \lceil m/2 \rceil^{h-1}$ is the minimum number of external nodes.  
B) ✗ Inequality direction and exponent incorrect.  
C) ✓ Rearranged form for height bound: $h \leq \log_{\lceil m/2 \rceil} \frac{n+1}{2} + 1$.  
D) ✗ Height bound depends on ceil(m/2), not m directly.

**Correct:** A,C


#### 4. Why are AVL and Red-Black trees considered inefficient for very large dictionaries stored on disk?  
A) ✓ Their height causes many disk accesses per search.  
B) ✗ Memory size is not the main issue here.  
C) ✗ Both guarantee balanced height.  
D) ✓ Disk access times accumulate to seconds, which is unacceptable.

**Correct:** A,D


#### 5. Which of the following correctly describe the insertion process in a B-tree when inserting into a full leaf node?  
A) ✓ Node is split around the middle key.  
B) ✓ Middle key is promoted to the parent.  
C) ✗ Height increases only if root splits, not always.  
D) ✗ New key is not inserted directly into parent without splitting.

**Correct:** A,B


#### 6. In a 2-3 tree, what is the minimum number of children an internal node (other than the root) must have?  
A) ✗ Minimum is not 1.  
B) ✓ Minimum is 2 children (since order 3, ceil(3/2) = 2).  
C) ✗ 3 is maximum, not minimum.  
D) ✓ ceil(3/2) = 2, so same as B.

**Correct:** B,D


#### 7. Which of the following statements about 2-3-4 trees are true?  
A) ✓ 2-3-4 trees are B-trees of order 4.  
B) ✓ Internal nodes can have 2 to 4 children.  
C) ✗ Root must have at least 2 children, not necessarily 3.  
D) ✓ External nodes are all at the same level.

**Correct:** A,B,D


#### 8. When splitting an overfull node in a B-tree of order m, which key is promoted to the parent?  
A) ✗ Smallest key is not promoted.  
B) ✗ Largest key is not promoted.  
C) ✓ The middle key, specifically the $\lceil m/2 \rceil$-th key, is promoted.  
D) ✗ Highest value key is not necessarily the middle.

**Correct:** C


#### 9. What is the worst-case number of disk accesses during a B-tree insertion if s nodes split and the tree height is h?  
A) ✓ Total disk accesses = $h + 2s + 1$.  
B) ✓ Max is $3h + 1$ (worst case when s = h).  
C) ✗ Formula incorrect.  
D) ✗ Formula incomplete.

**Correct:** A,B


#### 10. Which of the following are true about B+-trees compared to B-trees?  
A) ✓ Dictionary pairs stored only in leaves.  
B) ✓ Leaves form a doubly-linked list.  
C) ✗ Internal nodes do not store all dictionary pairs, only keys for routing.  
D) ✓ Structure is similar except for data storage location.

**Correct:** A,B,D


#### 11. During deletion in a 2-3 tree, if a 2-node becomes deficient, what are the possible corrective actions?  
A) ✓ Borrow from adjacent 3-node sibling via parent.  
B) ✓ Merge with sibling and parent pair if borrowing not possible.  
C) ✗ Deficient node cannot be discarded immediately.  
D) ✗ Replacement by largest in left subtree applies to internal node deletion, not deficiency fix.

**Correct:** A,B


#### 12. In a B-tree of order 5, which of the following is true?  
A) ✓ Root may be a 2-node (less than ceil(5/2) children).  
B) ✗ Internal nodes must have at least ceil(5/2) = 3 children, not exactly 5.  
C) ✓ Minimum children for internal nodes (except root) is 3.  
D) ✗ Not a binary tree.

**Correct:** A,C


#### 13. Which of the following correctly describe the height bounds for AVL and Red-Black trees with approximately $10^9$ nodes?  
A) ✓ AVL height between 30 and 43.  
B) ✓ Red-Black height between 30 and 60.  
C) ✗ AVL trees have better (lower) height bounds than Red-Black trees.  
D) ✗ Both require many disk accesses (30+), not fewer than 10.

**Correct:** A,B


#### 14. When inserting a key into a 3-node in a 2-3 tree, what happens if the node overflows?  
A) ✓ Node splits into two nodes around the middle key.  
B) ✓ Middle key is inserted into the parent.  
C) ✗ Height increases only if root splits.  
D) ✗ New key is never discarded.

**Correct:** A,B


#### 15. Which of the following statements about the minimum number of pairs in an m-way search tree are correct?  
A) ✓ Number of external nodes = n + 1.  
B) ✓ Height bound: $h \leq \log_{\lceil m/2 \rceil} \frac{n+1}{2} + 1$.  
C) ✗ Minimum pairs depend on m.  
D) ✓ Minimum pairs grow exponentially with height h.

**Correct:** A,B,D


#### 16. In the context of B-trees, what does the term "external (or failure) nodes" refer to?  
A) ✓ Null pointers or placeholders for missing children.  
B) ✗ Leaves store dictionary pairs, not external nodes.  
C) ✓ External nodes are null or failure nodes.  
D) ✗ External nodes are not necessarily the lowest level nodes with data.

**Correct:** A,C


#### 17. Which of the following factors influence the worst-case search time in a B-tree?  
A) ✓ Time to fetch a node from disk.  
B) ✓ Time to search within a node (linear or binary search).  
C) ✓ Height of the tree.  
D) ✗ Number of siblings does not affect search time.

**Correct:** A,B,C


#### 18. During deletion in a B+-tree, if an index node becomes deficient, what are the possible steps to fix it?  
A) ✓ Borrow a key from sibling and update parent key.  
B) ✓ Merge with sibling and delete in-between key in parent.  
C) ✗ Cannot discard deficient node immediately without fix.  
D) ✗ Deficient index node is not replaced by leaf node.

**Correct:** A,B


#### 19. Which of the following statements about the height change during insertion and deletion in B-trees are true?  
A) ✓ Insertion can increase height by 1 if root splits.  
B) ✓ Deletion can reduce height by 1 if root is discarded.  
C) ✗ Height can change during insertion.  
D) ✗ Height can change during deletion.

**Correct:** A,B


#### 20. Consider a B-tree of order 2. Which of the following are true?  
A) ✓ It is a full binary tree.  
B) ✗ Internal nodes must have at least ceil(2/2) = 1 child, but root must have at least 2 if not empty.  
C) ✗ Minimum children for internal nodes (except root) is 1, but root must have at least 2 children if not empty.  
D) ✗ It is not equivalent to a 2-3 tree (order 3).

**Correct:** A