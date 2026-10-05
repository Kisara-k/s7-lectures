## 11. Splay Trees

## Questions

#### 1. Which of the following operations in splay trees have an amortized complexity of O(log n) but an actual worst-case complexity of O(n)?  
A) Delete  
B) Join  
C) Insert  
D) Search  

#### 2. In a bottom-up splay tree, what happens immediately after a search, insert, or delete operation?  
A) The splay node becomes the root of the tree  
B) The tree is split into two subtrees  
C) A splay operation is performed starting at the splay node  
D) The splay node becomes a leaf node  

#### 3. For the split operation in bottom-up splay trees, where is the splay operation performed?  
A) At the splay node after the operation completes  
B) At the root of the tree  
C) In the middle of the split operation  
D) No splay operation is performed  

#### 4. When searching for a key k in a splay tree, if the key is not found, which node becomes the splay node?  
A) The root of the tree  
B) The newly inserted node  
C) The parent of the external node where the search terminates  
D) The node containing the closest smaller key  

#### 5. In the insert operation of a bottom-up splay tree, if the key already exists, which node is chosen as the splay node?  
A) The root node  
B) The newly inserted node  
C) The parent of the external node where the search terminates  
D) The node containing the existing key  

#### 6. During deletion in a bottom-up splay tree, if the key to delete exists, which node is the splay node?  
A) The root node  
B) The newly inserted node  
C) The parent of the node physically deleted  
D) The node physically deleted  

#### 7. What is the actual complexity of the join operation in splay trees?  
A) O(1) amortized and O(1) actual  
B) O(log n) amortized and O(1) actual  
C) O(n) amortized and O(log n) actual  
D) O(log n) amortized and O(n) actual  

#### 8. Which of the following statements about splay steps is true?  
A) Every splay step, except possibly the last, moves the splay node up two levels  
B) Splay steps only occur if the splay node is at level 1  
C) Every splay step moves the splay node up exactly one level  
D) Splay steps terminate when the splay node becomes a leaf  

#### 9. In a splay step, what happens if the splay node q is at level 2?  
A) A one-level move is performed and the splay operation terminates  
B) No move is performed and the splay operation terminates  
C) The splay node is rotated with its grandparent  
D) A two-level move is performed and the splay continues  

#### 10. Which of the following is true about the top-down splay tree approach?  
A) Moves down the tree are always one level at a time  
B) Rotations are performed only after reaching the splay node  
C) The tree is split into two trees S and B on the way down  
D) Rotations are done whenever an LL or RR move is made  

#### 11. How does the top-down splay tree differ from the bottom-up approach in terms of splay operation?  
A) Top-down does not perform any rotations  
B) Bottom-up splits the tree into S and B subtrees  
C) Bottom-up performs splay steps on the way up the tree  
D) Top-down performs splay steps on the way down the tree  

#### 12. In the top-down splay tree, what happens when the splay node is reached?  
A) The tree is split into S and B subtrees  
B) The subtrees S, B, and the subtree rooted at the splay node are combined into one tree  
C) The splay operation terminates without any further action  
D) The splay node is deleted  

#### 13. Which of the following moves are involved in the two-level move during splaying?  
A) RL move  
B) L move  
C) RR move  
D) LL move  

#### 14. What is the worst-case height of a splay tree after inserting keys in ascending order?  
A) O(log n)  
B) O(n log n)  
C) O(1)  
D) O(n)  

#### 15. Which of the following statements about the actual complexity of search, insert, delete, and split operations in splay trees is correct?  
A) They can be O(n) in the worst case  
B) They are always O(log n) in the worst case  
C) They never exceed O(log n) actual complexity  
D) They are O(1) amortized  

#### 16. Why are top-down splay trees generally faster than bottom-up splay trees?  
A) Because they perform rotations during the descent, reducing the number of splay steps  
B) Because they avoid splaying altogether  
C) Because they use a different data structure internally  
D) Because they do not require splitting the tree  

#### 17. In the split operation of a bottom-up splay tree, what happens to the left and right subtrees of the root after splaying?  
A) The right subtree is discarded  
B) Both subtrees are merged into one  
C) The left subtree is discarded  
D) The left subtree becomes S and the right subtree becomes B  

#### 18. Which of the following is NOT a characteristic of splay trees?  
A) They require explicit balance factors like AVL trees  
B) They can have worst-case height O(n)  
C) They perform rotations to move accessed nodes to the root  
D) They have amortized O(log n) complexity for search, insert, and delete  

#### 19. During a splay step, if the splay node q is the right child of the right child of its grandparent, which move is performed?  
A) RL move  
B) RR move  
C) LL move  
D) LR move  

#### 20. What is the role of the splay node in the splay tree operations?  
A) It is the node that will be moved to the root by splaying  
B) It is always the root of the tree before the operation  
C) It is the node that is deleted during the operation  
D) It is the node that remains unchanged during splaying  



<br>

## Answers

#### 1. Which of the following operations in splay trees have an amortized complexity of O(log n) but an actual worst-case complexity of O(n)?  
A) ✓ Delete has amortized O(log n) but worst-case O(n)  
B) ✗ Join has actual and amortized O(1) complexity  
C) ✓ Insert has amortized O(log n) but worst-case O(n)  
D) ✓ Search has amortized O(log n) but worst-case O(n)  

**Correct:** A, C, D


#### 2. In a bottom-up splay tree, what happens immediately after a search, insert, or delete operation?  
A) ✓ The splay node becomes the root after splaying  
B) ✗ The tree is not split immediately after these operations  
C) ✓ A splay operation is performed starting at the splay node  
D) ✗ The splay node does not become a leaf after these operations  

**Correct:** A, C


#### 3. For the split operation in bottom-up splay trees, where is the splay operation performed?  
A) ✗ Not after the operation completes, but during it  
B) ✗ Not at the root initially  
C) ✓ The splay is done in the middle of the split operation  
D) ✗ A splay is always performed for split  

**Correct:** C


#### 4. When searching for a key k in a splay tree, if the key is not found, which node becomes the splay node?  
A) ✗ The root is not automatically the splay node if key not found  
B) ✗ No new node is inserted during search  
C) ✓ The parent of the external node where the search terminates is the splay node  
D) ✗ Not necessarily the closest smaller key node  

**Correct:** C


#### 5. In the insert operation of a bottom-up splay tree, if the key already exists, which node is chosen as the splay node?  
A) ✗ The root is not automatically the splay node  
B) ✗ The newly inserted node does not exist if key exists  
C) ✗ The parent of external node is not relevant here  
D) ✓ The node containing the existing key is the splay node  

**Correct:** D


#### 6. During deletion in a bottom-up splay tree, if the key to delete exists, which node is the splay node?  
A) ✗ The root is not automatically the splay node  
B) ✗ No new node is inserted during delete  
C) ✓ The parent of the node physically deleted is the splay node  
D) ✗ The deleted node is removed, not splayed  

**Correct:** C


#### 7. What is the actual complexity of the join operation in splay trees?  
A) ✓ Join has O(1) amortized and actual complexity  
B) ✗ Join is not O(log n) amortized with O(1) actual  
C) ✗ Join is not O(n) amortized  
D) ✗ Join is not O(log n) amortized  

**Correct:** A


#### 8. Which of the following statements about splay steps is true?  
A) ✓ Every splay step except possibly the last moves the splay node up two levels  
B) ✗ Splay steps occur at any level, not only level 1  
C) ✗ Splay steps usually move the node two levels up, not one  
D) ✗ Splay steps terminate when node becomes root, not leaf  

**Correct:** A


#### 9. In a splay step, what happens if the splay node q is at level 2?  
A) ✓ One-level move is performed and splay terminates  
B) ✗ A move is always performed if q is not root  
C) ✗ Rotation with grandparent only happens if level > 2  
D) ✗ Two-level move is for levels > 2  

**Correct:** A


#### 10. Which of the following is true about the top-down splay tree approach?  
A) ✗ Moves are mostly two levels at a time, not always one  
B) ✗ Rotations are done during descent, not only after splay node reached  
C) ✓ The tree is split into S (small) and B (big) on the way down  
D) ✓ Rotations are done whenever an LL or RR move is made  

**Correct:** C, D


#### 11. How does the top-down splay tree differ from the bottom-up approach in terms of splay operation?  
A) ✗ Top-down does perform rotations  
B) ✗ Bottom-up does not split into S and B subtrees on descent  
C) ✓ Bottom-up performs splay steps on the way up  
D) ✓ Top-down performs splay steps on the way down  

**Correct:** C, D


#### 12. In the top-down splay tree, what happens when the splay node is reached?  
A) ✗ The split into S and B happens on the way down, not at splay node  
B) ✓ S, B, and the subtree rooted at splay node are combined into one tree  
C) ✗ The splay operation does not terminate without combining  
D) ✗ The splay node is not deleted  

**Correct:** B


#### 13. Which of the following moves are involved in the two-level move during splaying?  
A) ✓ RL move is part of two-level moves  
B) ✓ L move is part of the final one-level move after two-level moves  
C) ✓ RR move is part of two-level moves  
D) ✗ LL move is symmetric but not explicitly listed here  

**Correct:** A, B, C


#### 14. What is the worst-case height of a splay tree after inserting keys in ascending order?  
A) ✗ Not O(log n) in worst case  
B) ✗ Not O(n log n)  
C) ✗ Not O(1)  
D) ✓ Worst-case height can be O(n)  

**Correct:** D


#### 15. Which of the following statements about the actual complexity of search, insert, delete, and split operations in splay trees is correct?  
A) ✓ They can be O(n) in worst case  
B) ✗ They can be O(n) in worst case, not always O(log n)  
C) ✗ They can exceed O(log n) actual complexity  
D) ✗ They are not O(1) amortized  

**Correct:** A


#### 16. Why are top-down splay trees generally faster than bottom-up splay trees?  
A) ✓ They perform rotations during descent, reducing splay steps  
B) ✗ They do not avoid splaying  
C) ✗ They use the same data structure internally  
D) ✗ They still split the tree into S and B  

**Correct:** A


#### 17. In the split operation of a bottom-up splay tree, what happens to the left and right subtrees of the root after splaying?  
A) ✗ Right subtree is not discarded  
B) ✗ They are not merged immediately after splay in split  
C) ✗ Left subtree is not discarded  
D) ✓ Left subtree becomes S and right subtree becomes B  

**Correct:** D


#### 18. Which of the following is NOT a characteristic of splay trees?  
A) ✓ They do NOT require explicit balance factors like AVL trees  
B) ✗ They can have worst-case height O(n)  
C) ✗ They do perform rotations to move accessed nodes to root  
D) ✗ They do have amortized O(log n) complexity  

**Correct:** A


#### 19. During a splay step, if the splay node q is the right child of the right child of its grandparent, which move is performed?  
A) ✗ RL move is different case  
B) ✓ RR move is performed in this scenario  
C) ✗ LL move is symmetric but not this case  
D) ✗ LR move is different case  

**Correct:** B


#### 20. What is the role of the splay node in the splay tree operations?  
A) ✓ It is the node moved to the root by splaying  
B) ✗ It is not always the root before operation  
C) ✗ It is not necessarily deleted  
D) ✗ It is not unchanged during splaying  

**Correct:** A