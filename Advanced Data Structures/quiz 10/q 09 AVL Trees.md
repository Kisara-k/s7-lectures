## 9. AVL Trees

## Questions

#### 1. Which of the following statements about AVL trees are true?  
A) The balance factor of every node is always -1, 0, or 1.  
B) The height of an AVL tree with n nodes is at most 1.44 log₂(n+2).  
C) The balance factor is defined as the height of the right subtree minus the height of the left subtree.  
D) AVL trees guarantee O(log n) worst-case search time.

#### 2. Consider the insertion of a new node in an AVL tree that causes imbalance at node A with balance factor +2. Which of the following imbalance types could occur?  
A) RR (Right-Right)  
B) LL (Left-Left)  
C) RL (Right-Left)  
D) LR (Left-Right)

#### 3. After inserting a node in an AVL tree, retracing the path to the root stops when which of the following conditions is met?  
A) A node with balance factor 0 is reached.  
B) A node with balance factor 2 or -2 is reached.  
C) The root is reached.  
D) A node with balance factor 1 or -1 is reached.

#### 4. Which of the following statements about rotations in AVL trees are correct?  
A) LL and RR rotations are single rotations.  
B) LR rotation is a single rotation.  
C) RL rotation is a double rotation consisting of LL followed by RR.  
D) After rotations, the subtree height remains unchanged.

#### 5. Regarding deletion in AVL trees, which of the following are true?  
A) Deletion from the left subtree of a node q decreases q’s balance factor by 1.  
B) If the new balance factor of q after deletion is 0, the height of the subtree rooted at q decreases by 1.  
C) At most one rotation is needed to rebalance after deletion.  
D) The number of rebalancing rotations after deletion can be O(log n).

#### 6. Which of the following properties correctly describe red-black trees?  
A) Every path from the root to an external node contains the same number of black nodes.  
B) No root-to-external-node path contains two consecutive red nodes.  
C) The height of a red-black tree with n nodes is at most log₂(n+1).  
D) The root and all external nodes are black.

#### 7. In red-black trees, what happens when a newly inserted red node causes two consecutive red nodes?  
A) The tree is immediately balanced by a single rotation.  
B) Color flips and/or rotations are used to restore red-black properties.  
C) The new node is recolored black to fix the violation.  
D) The violation is ignored until the next insertion.

#### 8. Which of the following statements about rotations and color flips in red-black trees are true?  
A) At most one rotation and O(log n) color flips are needed per insertion or deletion.  
B) Color flips do not disturb the priority queue property in priority search trees.  
C) Rotations do not affect the priority queue property in priority search trees.  
D) The overall fix time for AVL trees is O(log² n) due to rotations.

#### 9. When deleting a black node in a red-black tree, which of the following situations can occur?  
A) The subtree rooted at the deleted node becomes deficient by one black pointer.  
B) If the deleted node is red, no rebalancing is needed.  
C) Deleting a black node with two children is impossible.  
D) The deficiency can be resolved by recoloring only, without rotations.

#### 10. In the context of red-black tree deletion rebalancing, which of the following statements about the Rb0 and Rb1 cases are correct?  
A) Rb0 case 1 involves a color change and continuing rebalancing.  
B) Rb0 case 2 eliminates deficiency immediately with a color change.  
C) Rb1 cases always require rotations to fix the deficiency.  
D) Rb1 cases correspond to LL and LR rotations similar to AVL trees.



<br>

## Answers

#### 1. Which of the following statements about AVL trees are true?  
A) ✓ The balance factor is defined as height(left subtree) - height(right subtree) and is always -1, 0, or 1.  
B) ✓ The height upper bound is proven to be at most 1.44 log₂(n+2).  
C) ✗ Incorrect definition; balance factor is left height minus right height, not the other way around.  
D) ✓ AVL trees guarantee O(log n) worst-case search time due to height balancing.

**Correct:** A, B, D


#### 2. Consider the insertion of a new node in an AVL tree that causes imbalance at node A with balance factor +2. Which of the following imbalance types could occur?  
A) ✗ RR imbalance corresponds to balance factor -2 (right-heavy), not +2.  
B) ✓ LL imbalance occurs when balance factor is +2 (left-heavy).  
C) ✗ RL imbalance corresponds to balance factor -2 with a left child imbalance.  
D) ✓ LR imbalance occurs with balance factor +2 and a right child imbalance.

**Correct:** B, D


#### 3. After inserting a node in an AVL tree, retracing the path to the root stops when which of the following conditions is met?  
A) ✓ If balance factor becomes 0, no further height changes occur, so retracing stops.  
B) ✗ Retracing does not stop at imbalance (2 or -2); instead, rotations are performed.  
C) ✓ Retracing stops if the root is reached.  
D) ✗ Balance factors ±1 mean height changed but no imbalance; retracing continues.

**Correct:** A, C


#### 4. Which of the following statements about rotations in AVL trees are correct?  
A) ✓ LL and RR are single rotations.  
B) ✗ LR is a double rotation (RR followed by LL), not single.  
C) ✗ RL is LL followed by RR, not the other way around.  
D) ✓ After rotations, subtree height remains unchanged, so no further adjustments needed.

**Correct:** A, D


#### 5. Regarding deletion in AVL trees, which of the following are true?  
A) ✓ Deletion from left subtree decreases balance factor by 1 (bf--).  
B) ✓ New bf=0 means subtree height decreased by 1.  
C) ✗ Deletion may require up to O(log n) rotations, not just one.  
D) ✓ Number of rotations after deletion can be O(log n).

**Correct:** A, B, D


#### 6. Which of the following properties correctly describe red-black trees?  
A) ✓ All root-to-external-node paths have the same number of black nodes.  
B) ✓ No path has two consecutive red nodes.  
C) ✗ Height is between log₂(n+1) and 2 log₂(n+1), not at most log₂(n+1).  
D) ✓ Root and all external nodes are black.

**Correct:** A, B, D


#### 7. In red-black trees, what happens when a newly inserted red node causes two consecutive red nodes?  
A) ✗ Immediate single rotation is not always sufficient; color flips may be needed.  
B) ✓ Color flips and/or rotations restore red-black properties.  
C) ✗ New node is inserted red, not recolored black immediately.  
D) ✗ Violation cannot be ignored; must be fixed immediately.

**Correct:** B


#### 8. Which of the following statements about rotations and color flips in red-black trees are true?  
A) ✓ At most one rotation and O(log n) color flips per insert/delete.  
B) ✓ Color flips do not disturb priority queue property in priority search trees.  
C) ✗ Rotations do disturb priority queue property, requiring O(log n) fix time.  
D) ✓ Overall fix time for AVL trees is O(log² n) due to rotations.

**Correct:** A, B, D


#### 9. When deleting a black node in a red-black tree, which of the following situations can occur?  
A) ✓ The subtree rooted at the deleted node becomes deficient by one black pointer.  
B) ✓ Deleting a red node requires no rebalancing.  
C) ✓ Degree 2 black nodes are never deleted directly (internal nodes with two children).  
D) ✗ Deficiency often requires rotations and recoloring, not just recoloring.

**Correct:** A, B, C


#### 10. In the context of red-black tree deletion rebalancing, which of the following statements about the Rb0 and Rb1 cases are correct?  
A) ✓ Rb0 case 1 involves a color change and continuing rebalancing.  
B) ✓ Rb0 case 2 eliminates deficiency immediately with a color change.  
C) ✗ Rb1 cases may require rotations but not always; some cases end after rotation.  
D) ✓ Rb1 cases correspond to LL and LR rotations similar to AVL trees.

**Correct:** A, B, D