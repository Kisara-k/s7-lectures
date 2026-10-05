## 11. Splay Trees

## Questions

#### 1. Which of the following statements about the amortized and actual complexities of splay tree operations are correct?  
A) Search, insert, delete, and split have amortized complexity O(log n) but actual complexity O(n) in the worst case.  
B) The actual complexity of search, insert, delete, and split is always O(log n).  
C) Join operation has both actual and amortized complexity O(log n).  
D) Join operation has actual and amortized complexity O(1).  

#### 2. In a bottom-up splay tree, which nodes can be the splay node after a search(k) operation?  
A) The node containing the key k if it exists.  
B) The root of the tree regardless of the search result.  
C) The newly inserted node if k was inserted during the search.  
D) The parent of the external node where the search terminates if k is not found.  

#### 3. During a splay step, what happens if the splay node q is at level 2 in the tree?  
A) No move is performed and the splay operation terminates immediately.  
B) A two-level move is performed and the splay continues.  
C) A one-level move is performed and the splay operation terminates.  
D) The splay node is moved directly to the root in one step.  

#### 4. Which of the following correctly describe the difference between bottom-up and top-down splay trees?  
A) Bottom-up splay trees perform rotations during the descent down the tree.  
B) Top-down splay trees move down two levels at a time, except possibly at the end.  
C) Top-down splay trees split the tree into smaller and bigger subtrees on the way down before combining them.  
D) Bottom-up splay trees perform the splay operation after the standard BST operation is complete.  

#### 5. In the split(k) operation of a bottom-up splay tree, what is true about the splay node and the resulting subtrees?  
A) The splay node is the newly inserted node with key k.  
B) The right subtree of the root contains all keys greater than k.  
C) After splaying, the left subtree of the root contains all keys less than k.  
D) The splay operation is not performed during split.  

#### 6. Which of the following statements about the actual complexity of splay tree operations when inserting keys in ascending order (1, 2, 3, ...) is true?  
A) The actual complexity of search, insert, delete, and split can degrade to O(n) per operation.  
B) The worst-case height of the splay tree can be O(n).  
C) The worst-case height of the splay tree remains O(log n).  
D) The amortized complexity of these operations becomes O(n).  

#### 7. Regarding the splay step’s two-level move, which of the following are correct?  
A) It is symmetric for q being the left child of the left child of its grandparent.  
B) It is performed only if q is the right child of the right child of its grandparent.  
C) It is performed when q is at level 2 in the tree.  
D) It moves the splay node q two levels up the tree.  

#### 8. In top-down splay trees, what is the role of rotations during the descent?  
A) Rotations are performed whenever an LL or RR move is made.  
B) Rotations help maintain the binary search tree property while splitting into S and B.  
C) Rotations are never performed in top-down splay trees.  
D) Rotations are only performed after reaching the splay node.  

#### 9. Which of the following statements about the join operation in bottom-up splay trees is true?  
A) Join requires no splay or only a null splay operation.  
B) Join has actual complexity O(n).  
C) Join has amortized complexity O(1).  
D) Join requires a splay operation on one of the trees before joining.  

#### 10. Why are top-down splay trees generally considered faster than bottom-up splay trees?  
A) Because top-down splay trees combine subtrees immediately after reaching the splay node.  
B) Because top-down splay trees perform splaying during the descent, avoiding extra passes.  
C) Because top-down splay trees do not require rotations.  
D) Because bottom-up splay trees require multiple splay steps after each operation.  



<br>

## Answers

#### 1. Which of the following statements about the amortized and actual complexities of splay tree operations are correct?  
A) ✓ Amortized complexity of search, insert, delete, and split is O(log n), but actual worst-case complexity is O(n).  
B) ✗ Actual complexity of search, insert, delete, and split can be O(n) in worst case, not always O(log n).  
C) ✗ Join operation does not have O(log n) complexity; it is faster.  
D) ✓ Join operation has actual and amortized complexity O(1).  

**Correct:** A, D


#### 2. In a bottom-up splay tree, which nodes can be the splay node after a search(k) operation?  
A) ✓ If key k is found, the node containing k is the splay node.  
B) ✗ The root is not necessarily the splay node before splaying.  
C) ✗ The newly inserted node is relevant only for insert, not search.  
D) ✓ If k is not found, the parent of the external node where search ends is the splay node.  

**Correct:** A, D


#### 3. During a splay step, what happens if the splay node q is at level 2 in the tree?  
A) ✗ Some move is performed; splay does not terminate without a move.  
B) ✗ Two-level move is for levels greater than 2, not level 2.  
C) ✓ One-level move is done and splay terminates at level 2.  
D) ✗ The splay node is not moved directly to root in one step at level 2.  

**Correct:** C


#### 4. Which of the following correctly describe the difference between bottom-up and top-down splay trees?  
A) ✗ Bottom-up does not perform rotations during descent; rotations happen during splay after operation.  
B) ✓ Top-down moves down two levels at a time, except possibly at the end.  
C) ✓ Top-down splits the tree into smaller (S) and bigger (B) subtrees on the way down.  
D) ✓ Bottom-up performs splay after the BST operation is complete.  

**Correct:** B, C, D


#### 5. In the split(k) operation of a bottom-up splay tree, what is true about the splay node and the resulting subtrees?  
A) ✗ The splay node is not necessarily the newly inserted node; it depends on insert rules.  
B) ✓ The right subtree of the root contains all keys greater than k (B).  
C) ✓ After splaying, the left subtree of the root contains all keys less than k (S).  
D) ✗ The splay operation is performed during split, not skipped.  

**Correct:** B, C


#### 6. Which of the following statements about the actual complexity of splay tree operations when inserting keys in ascending order (1, 2, 3, ...) is true?  
A) ✓ Actual complexity of search, insert, delete, and split can degrade to O(n) per operation.  
B) ✓ Worst-case height can be O(n) due to unbalanced insertions.  
C) ✗ Worst-case height can be linear, not logarithmic.  
D) ✗ Amortized complexity remains O(log n), not O(n).  

**Correct:** A, B


#### 7. Regarding the splay step’s two-level move, which of the following are correct?  
A) ✓ Two-level move is symmetric for q being left child of left child of grandparent.  
B) ✗ Two-level move is not limited to q being right child of right child; symmetric cases exist.  
C) ✗ Two-level move is for levels greater than 2, not level 2.  
D) ✓ Two-level move moves q two levels up the tree.  

**Correct:** A, D


#### 8. In top-down splay trees, what is the role of rotations during the descent?  
A) ✓ Rotations are performed whenever an LL or RR move is made.  
B) ✓ Rotations help maintain BST property while splitting into S and B.  
C) ✗ Rotations are definitely performed, not never.  
D) ✗ Rotations happen during descent, not only after reaching splay node.  

**Correct:** A, B


#### 9. Which of the following statements about the join operation in bottom-up splay trees is true?  
A) ✓ Join requires no splay or only a null splay operation.  
B) ✗ Join does not have actual complexity O(n).  
C) ✓ Join has amortized complexity O(1).  
D) ✗ Join does not require splaying one of the trees before joining.  

**Correct:** A, C


#### 10. Why are top-down splay trees generally considered faster than bottom-up splay trees?  
A) ✓ Top-down trees combine subtrees immediately after reaching the splay node, improving efficiency.  
B) ✓ Because top-down splaying is done during descent, avoiding extra passes.  
C) ✗ Top-down splay trees do require rotations, so this is false.  
D) ✓ Bottom-up requires splaying after each operation, which can be more costly.  

**Correct:** A, B, D