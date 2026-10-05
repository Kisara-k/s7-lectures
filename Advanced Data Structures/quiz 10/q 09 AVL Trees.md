## 9. AVL Trees

## Questions

#### 1. Which of the following statements about AVL trees are true?  
A) AVL trees guarantee O(log n) worst-case search time.  
B) The balance factor is defined as the height of the right subtree minus the height of the left subtree.  
C) The balance factor of every node is always -1, 0, or 1.  
D) The height of an AVL tree with n nodes is at most 1.44 log₂(n+2).  

#### 2. Consider the insertion of a new node in an AVL tree that causes imbalance at node A with balance factor +2. Which of the following imbalance types could occur?  
A) LL (Left-Left)  
B) RR (Right-Right)  
C) LR (Left-Right)  
D) RL (Right-Left)  

#### 3. After inserting a node in an AVL tree, retracing the path to the root stops when which of the following conditions is met?  
A) The root is reached.  
B) A node with balance factor 2 or -2 is reached.  
C) A node with balance factor 1 or -1 is reached.  
D) A node with balance factor 0 is reached.  

#### 4. Which of the following statements about rotations in AVL trees are correct?  
A) RL rotation is a double rotation consisting of LL followed by RR.  
B) LL and RR rotations are single rotations.  
C) After rotations, the subtree height remains unchanged.  
D) LR rotation is a single rotation.  

#### 5. Regarding deletion in AVL trees, which of the following are true?  
A) Deletion from the left subtree of a node q decreases q’s balance factor by 1.  
B) If the new balance factor of q after deletion is 0, the height of the subtree rooted at q decreases by 1.  
C) At most one rotation is needed to rebalance after deletion.  
D) The number of rebalancing rotations after deletion can be O(log n).  

#### 6. Which of the following properties correctly describe red-black trees?  
A) The root and all external nodes are black.  
B) No root-to-external-node path contains two consecutive red nodes.  
C) Every path from the root to an external node contains the same number of black nodes.  
D) The height of a red-black tree with n nodes is at most log₂(n+1).  

#### 7. In red-black trees, what happens when a newly inserted red node causes two consecutive red nodes?  
A) The new node is recolored black to fix the violation.  
B) The violation is ignored until the next insertion.  
C) Color flips and/or rotations are used to restore red-black properties.  
D) The tree is immediately balanced by a single rotation.  

#### 8. Which of the following statements about rotations and color flips in red-black trees are true?  
A) Rotations do not affect the priority queue property in priority search trees.  
B) At most one rotation and O(log n) color flips are needed per insertion or deletion.  
C) The overall fix time for AVL trees is O(log² n) due to rotations.  
D) Color flips do not disturb the priority queue property in priority search trees.  

#### 9. When deleting a black node in a red-black tree, which of the following situations can occur?  
A) The deficiency can be resolved by recoloring only, without rotations.  
B) Deleting a black node with two children is impossible.  
C) If the deleted node is red, no rebalancing is needed.  
D) The subtree rooted at the deleted node becomes deficient by one black pointer.  

#### 10. In the context of red-black tree deletion rebalancing, which of the following statements about the Rb0 and Rb1 cases are correct?  
A) Rb0 case 1 involves a color change and continuing rebalancing.  
B) Rb1 cases correspond to LL and LR rotations similar to AVL trees.  
C) Rb0 case 2 eliminates deficiency immediately with a color change.  
D) Rb1 cases always require rotations to fix the deficiency.  



<br>

## Answers

#### 1. Which of the following statements about AVL trees are true?  
A) ✓ AVL trees guarantee O(log n) worst-case search time due to height balancing.  
B) ✗ Incorrect definition; balance factor is left height minus right height, not the other way around.  
C) ✓ The balance factor is defined as height(left subtree) - height(right subtree) and is always -1, 0, or 1.  
D) ✓ The height upper bound is proven to be at most 1.44 log₂(n+2).  

**Correct:** A, C, D


#### 2. Consider the insertion of a new node in an AVL tree that causes imbalance at node A with balance factor +2. Which of the following imbalance types could occur?  
A) ✓ LL imbalance occurs when balance factor is +2 (left-heavy).  
B) ✗ RR imbalance corresponds to balance factor -2 (right-heavy), not +2.  
C) ✓ LR imbalance occurs with balance factor +2 and a right child imbalance.  
D) ✗ RL imbalance corresponds to balance factor -2 with a left child imbalance.  

**Correct:** A, C


#### 3. After inserting a node in an AVL tree, retracing the path to the root stops when which of the following conditions is met?  
A) ✓ Retracing stops if the root is reached.  
B) ✗ Retracing does not stop at imbalance (2 or -2); instead, rotations are performed.  
C) ✗ Balance factors ±1 mean height changed but no imbalance; retracing continues.  
D) ✓ If balance factor becomes 0, no further height changes occur, so retracing stops.  

**Correct:** A, D


#### 4. Which of the following statements about rotations in AVL trees are correct?  
A) ✗ RL is LL followed by RR, not the other way around.  
B) ✓ LL and RR are single rotations.  
C) ✓ After rotations, subtree height remains unchanged, so no further adjustments needed.  
D) ✗ LR is a double rotation (RR followed by LL), not single.  

**Correct:** B, C


#### 5. Regarding deletion in AVL trees, which of the following are true?  
A) ✓ Deletion from left subtree decreases balance factor by 1 (bf--).  
B) ✓ New bf=0 means subtree height decreased by 1.  
C) ✗ Deletion may require up to O(log n) rotations, not just one.  
D) ✓ Number of rotations after deletion can be O(log n).  

**Correct:** A, B, D


#### 6. Which of the following properties correctly describe red-black trees?  
A) ✓ Root and all external nodes are black.  
B) ✓ No path has two consecutive red nodes.  
C) ✓ All root-to-external-node paths have the same number of black nodes.  
D) ✗ Height is between log₂(n+1) and 2 log₂(n+1), not at most log₂(n+1).  

**Correct:** A, B, C


#### 7. In red-black trees, what happens when a newly inserted red node causes two consecutive red nodes?  
A) ✗ New node is inserted red, not recolored black immediately.  
B) ✗ Violation cannot be ignored; must be fixed immediately.  
C) ✓ Color flips and/or rotations restore red-black properties.  
D) ✗ Immediate single rotation is not always sufficient; color flips may be needed.  

**Correct:** C


#### 8. Which of the following statements about rotations and color flips in red-black trees are true?  
A) ✗ Rotations do disturb priority queue property, requiring O(log n) fix time.  
B) ✓ At most one rotation and O(log n) color flips per insert/delete.  
C) ✓ Overall fix time for AVL trees is O(log² n) due to rotations.  
D) ✓ Color flips do not disturb priority queue property in priority search trees.  

**Correct:** B, C, D


#### 9. When deleting a black node in a red-black tree, which of the following situations can occur?  
A) ✗ Deficiency often requires rotations and recoloring, not just recoloring.  
B) ✓ Degree 2 black nodes are never deleted directly (internal nodes with two children).  
C) ✓ Deleting a red node requires no rebalancing.  
D) ✓ The subtree rooted at the deleted node becomes deficient by one black pointer.  

**Correct:** B, C, D


#### 10. In the context of red-black tree deletion rebalancing, which of the following statements about the Rb0 and Rb1 cases are correct?  
A) ✓ Rb0 case 1 involves a color change and continuing rebalancing.  
B) ✓ Rb1 cases correspond to LL and LR rotations similar to AVL trees.  
C) ✓ Rb0 case 2 eliminates deficiency immediately with a color change.  
D) ✗ Rb1 cases may require rotations but not always; some cases end after rotation.  

**Correct:** A, B, C