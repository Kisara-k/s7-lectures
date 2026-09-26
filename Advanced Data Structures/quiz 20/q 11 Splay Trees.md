## 11. Splay Trees

## Questions

#### 1. Which of the following operations in splay trees have an amortized complexity of O(log n) but an actual worst-case complexity of O(n)?  
A) Search  
B) Insert  
C) Delete  
D) Join  

#### 2. In a bottom-up splay tree, what happens immediately after a search, insert, or delete operation?  
A) The tree is split into two subtrees  
B) A splay operation is performed starting at the splay node  
C) The splay node becomes a leaf node  
D) The splay node becomes the root of the tree  

#### 3. For the split operation in bottom-up splay trees, where is the splay operation performed?  
A) At the root of the tree  
B) At the splay node after the operation completes  
C) In the middle of the split operation  
D) No splay operation is performed  

#### 4. When searching for a key k in a splay tree, if the key is not found, which node becomes the splay node?  
A) The node containing the closest smaller key  
B) The parent of the external node where the search terminates  
C) The root of the tree  
D) The newly inserted node  

#### 5. In the insert operation of a bottom-up splay tree, if the key already exists, which node is chosen as the splay node?  
A) The newly inserted node  
B) The node containing the existing key  
C) The root node  
D) The parent of the external node where the search terminates  

#### 6. During deletion in a bottom-up splay tree, if the key to delete exists, which node is the splay node?  
A) The node physically deleted  
B) The parent of the node physically deleted  
C) The root node  
D) The newly inserted node  

#### 7. What is the actual complexity of the join operation in splay trees?  
A) O(log n) amortized and O(n) actual  
B) O(1) amortized and O(1) actual  
C) O(n) amortized and O(log n) actual  
D) O(log n) amortized and O(1) actual  

#### 8. Which of the following statements about splay steps is true?  
A) Every splay step moves the splay node up exactly one level  
B) Every splay step, except possibly the last, moves the splay node up two levels  
C) Splay steps only occur if the splay node is at level 1  
D) Splay steps terminate when the splay node becomes a leaf  

#### 9. In a splay step, what happens if the splay node q is at level 2?  
A) A two-level move is performed and the splay continues  
B) A one-level move is performed and the splay operation terminates  
C) No move is performed and the splay operation terminates  
D) The splay node is rotated with its grandparent  

#### 10. Which of the following is true about the top-down splay tree approach?  
A) The tree is split into two trees S and B on the way down  
B) Rotations are performed only after reaching the splay node  
C) Moves down the tree are always one level at a time  
D) Rotations are done whenever an LL or RR move is made  

#### 11. How does the top-down splay tree differ from the bottom-up approach in terms of splay operation?  
A) Top-down performs splay steps on the way down the tree  
B) Bottom-up performs splay steps on the way up the tree  
C) Top-down does not perform any rotations  
D) Bottom-up splits the tree into S and B subtrees  

#### 12. In the top-down splay tree, what happens when the splay node is reached?  
A) The tree is split into S and B subtrees  
B) The subtrees S, B, and the subtree rooted at the splay node are combined into one tree  
C) The splay operation terminates without any further action  
D) The splay node is deleted  

#### 13. Which of the following moves are involved in the two-level move during splaying?  
A) RL move  
B) RR move  
C) LL move  
D) L move  

#### 14. What is the worst-case height of a splay tree after inserting keys in ascending order?  
A) O(log n)  
B) O(1)  
C) O(n)  
D) O(n log n)  

#### 15. Which of the following statements about the actual complexity of search, insert, delete, and split operations in splay trees is correct?  
A) They are always O(log n) in the worst case  
B) They can be O(n) in the worst case  
C) They are O(1) amortized  
D) They never exceed O(log n) actual complexity  

#### 16. Why are top-down splay trees generally faster than bottom-up splay trees?  
A) Because they avoid splaying altogether  
B) Because they perform rotations during the descent, reducing the number of splay steps  
C) Because they do not require splitting the tree  
D) Because they use a different data structure internally  

#### 17. In the split operation of a bottom-up splay tree, what happens to the left and right subtrees of the root after splaying?  
A) The left subtree becomes S and the right subtree becomes B  
B) Both subtrees are merged into one  
C) The left subtree is discarded  
D) The right subtree is discarded  

#### 18. Which of the following is NOT a characteristic of splay trees?  
A) They have amortized O(log n) complexity for search, insert, and delete  
B) They require explicit balance factors like AVL trees  
C) They perform rotations to move accessed nodes to the root  
D) They can have worst-case height O(n)  

#### 19. During a splay step, if the splay node q is the right child of the right child of its grandparent, which move is performed?  
A) LL move  
B) RR move  
C) RL move  
D) LR move  

#### 20. What is the role of the splay node in the splay tree operations?  
A) It is always the root of the tree before the operation  
B) It is the node that will be moved to the root by splaying  
C) It is the node that is deleted during the operation  
D) It is the node that remains unchanged during splaying



<br>

## Answers

#### 1. Which of the following operations in splay trees have an amortized complexity of O(log n) but an actual worst-case complexity of O(n)?  
A) ✓ Search has amortized O(log n) but worst-case O(n)  
B) ✓ Insert has amortized O(log n) but worst-case O(n)  
C) ✓ Delete has amortized O(log n) but worst-case O(n)  
D) ✗ Join has actual and amortized O(1) complexity  

**Correct:** A,B,C


#### 2. In a bottom-up splay tree, what happens immediately after a search, insert, or delete operation?  
A) ✗ The tree is not split immediately after these operations  
B) ✓ A splay operation is performed starting at the splay node  
C) ✗ The splay node does not become a leaf after these operations  
D) ✓ The splay node becomes the root after splaying  

**Correct:** B,D


#### 3. For the split operation in bottom-up splay trees, where is the splay operation performed?  
A) ✗ Not at the root initially  
B) ✗ Not after the operation completes, but during it  
C) ✓ The splay is done in the middle of the split operation  
D) ✗ A splay is always performed for split  

**Correct:** C


#### 4. When searching for a key k in a splay tree, if the key is not found, which node becomes the splay node?  
A) ✗ Not necessarily the closest smaller key node  
B) ✓ The parent of the external node where the search terminates is the splay node  
C) ✗ The root is not automatically the splay node if key not found  
D) ✗ No new node is inserted during search  

**Correct:** B


#### 5. In the insert operation of a bottom-up splay tree, if the key already exists, which node is chosen as the splay node?  
A) ✗ The newly inserted node does not exist if key exists  
B) ✓ The node containing the existing key is the splay node  
C) ✗ The root is not automatically the splay node  
D) ✗ The parent of external node is not relevant here  

**Correct:** B


#### 6. During deletion in a bottom-up splay tree, if the key to delete exists, which node is the splay node?  
A) ✗ The deleted node is removed, not splayed  
B) ✓ The parent of the node physically deleted is the splay node  
C) ✗ The root is not automatically the splay node  
D) ✗ No new node is inserted during delete  

**Correct:** B


#### 7. What is the actual complexity of the join operation in splay trees?  
A) ✗ Join is not O(log n) amortized  
B) ✓ Join has O(1) amortized and actual complexity  
C) ✗ Join is not O(n) amortized  
D) ✗ Join is not O(log n) amortized with O(1) actual  

**Correct:** B


#### 8. Which of the following statements about splay steps is true?  
A) ✗ Splay steps usually move the node two levels up, not one  
B) ✓ Every splay step except possibly the last moves the splay node up two levels  
C) ✗ Splay steps occur at any level, not only level 1  
D) ✗ Splay steps terminate when node becomes root, not leaf  

**Correct:** B


#### 9. In a splay step, what happens if the splay node q is at level 2?  
A) ✗ Two-level move is for levels > 2  
B) ✓ One-level move is performed and splay terminates  
C) ✗ A move is always performed if q is not root  
D) ✗ Rotation with grandparent only happens if level > 2  

**Correct:** B


#### 10. Which of the following is true about the top-down splay tree approach?  
A) ✓ The tree is split into S (small) and B (big) on the way down  
B) ✗ Rotations are done during descent, not only after splay node reached  
C) ✗ Moves are mostly two levels at a time, not always one  
D) ✓ Rotations are done whenever an LL or RR move is made  

**Correct:** A,D


#### 11. How does the top-down splay tree differ from the bottom-up approach in terms of splay operation?  
A) ✓ Top-down performs splay steps on the way down  
B) ✓ Bottom-up performs splay steps on the way up  
C) ✗ Top-down does perform rotations  
D) ✗ Bottom-up does not split into S and B subtrees on descent  

**Correct:** A,B


#### 12. In the top-down splay tree, what happens when the splay node is reached?  
A) ✗ The split into S and B happens on the way down, not at splay node  
B) ✓ S, B, and the subtree rooted at splay node are combined into one tree  
C) ✗ The splay operation does not terminate without combining  
D) ✗ The splay node is not deleted  

**Correct:** B


#### 13. Which of the following moves are involved in the two-level move during splaying?  
A) ✓ RL move is part of two-level moves  
B) ✓ RR move is part of two-level moves  
C) ✗ LL move is symmetric but not explicitly listed here  
D) ✓ L move is part of the final one-level move after two-level moves  

**Correct:** A,B,D


#### 14. What is the worst-case height of a splay tree after inserting keys in ascending order?  
A) ✗ Not O(log n) in worst case  
B) ✗ Not O(1)  
C) ✓ Worst-case height can be O(n)  
D) ✗ Not O(n log n)  

**Correct:** C


#### 15. Which of the following statements about the actual complexity of search, insert, delete, and split operations in splay trees is correct?  
A) ✗ They can be O(n) in worst case, not always O(log n)  
B) ✓ They can be O(n) in worst case  
C) ✗ They are not O(1) amortized  
D) ✗ They can exceed O(log n) actual complexity  

**Correct:** B


#### 16. Why are top-down splay trees generally faster than bottom-up splay trees?  
A) ✗ They do not avoid splaying  
B) ✓ They perform rotations during descent, reducing splay steps  
C) ✗ They still split the tree into S and B  
D) ✗ They use the same data structure internally  

**Correct:** B


#### 17. In the split operation of a bottom-up splay tree, what happens to the left and right subtrees of the root after splaying?  
A) ✓ Left subtree becomes S and right subtree becomes B  
B) ✗ They are not merged immediately after splay in split  
C) ✗ Left subtree is not discarded  
D) ✗ Right subtree is not discarded  

**Correct:** A


#### 18. Which of the following is NOT a characteristic of splay trees?  
A) ✗ They do have amortized O(log n) complexity  
B) ✓ They do NOT require explicit balance factors like AVL trees  
C) ✗ They do perform rotations to move accessed nodes to root  
D) ✗ They can have worst-case height O(n)  

**Correct:** B


#### 19. During a splay step, if the splay node q is the right child of the right child of its grandparent, which move is performed?  
A) ✗ LL move is symmetric but not this case  
B) ✓ RR move is performed in this scenario  
C) ✗ RL move is different case  
D) ✗ LR move is different case  

**Correct:** B


#### 20. What is the role of the splay node in the splay tree operations?  
A) ✗ It is not always the root before operation  
B) ✓ It is the node moved to the root by splaying  
C) ✗ It is not necessarily deleted  
D) ✗ It is not unchanged during splaying  

**Correct:** B