## 9. AVL Trees

## Questions

#### 1. What is the balance factor of a node in an AVL tree?  
A) Height of right subtree minus height of left subtree  
B) Difference between depths of left and right children  
C) Height of left subtree minus height of right subtree  
D) Number of nodes in left subtree minus number of nodes in right subtree  

#### 2. Which of the following are true about the height of an AVL tree with n nodes?  
A) It is always exactly log2(n)  
B) It is at most 1.44 log2(n+2)  
C) It is at least log2(n+1)  
D) It can be greater than 2 log2(n)  

#### 3. When inserting a new node into an AVL tree, at which point do you stop retracing and adjusting balance factors?  
A) When a node’s balance factor becomes 0  
B) When a node’s balance factor becomes 2 or -2  
C) When the root is reached  
D) When the newly inserted node is found again  

#### 4. Which imbalance type corresponds to the newly inserted node being in the right subtree of the right subtree of node A?  
A) RL  
B) LR  
C) LL  
D) RR  

#### 5. Which rotations are considered single rotations in AVL trees?  
A) RR and RL  
B) LL and RR  
C) LR and RL  
D) LL and LR  

#### 6. What is the effect of an LL rotation on the height of the subtree?  
A) Increases subtree height by 1  
B) Subtree height doubles  
C) Subtree height remains unchanged  
D) Decreases subtree height by 1  

#### 7. After deleting a node from an AVL tree, if the balance factor of a node q becomes 0, what does this imply?  
A) Tree is unbalanced at q  
B) Height of subtree rooted at q remains the same  
C) Height of subtree rooted at q has increased by 1  
D) Height of subtree rooted at q has decreased by 1  

#### 8. In AVL deletion, what does it mean if the balance factor of an ancestor A becomes 2 after deletion from its left subtree?  
A) Tree is balanced  
B) Type L imbalance  
C) No rotations needed  
D) Type R imbalance  

#### 9. Which of the following statements about rotations during AVL deletion are true?  
A) R1 rotation reduces subtree height by 1 and requires continuing up the tree  
B) R-1 rotation always stops rebalancing  
C) R1 rotation is similar to LL rotation  
D) R0 rotation does not change subtree height  

#### 10. Regarding the number of rotations needed for AVL tree operations, which is correct?  
A) At most O(log n) rotations per deletion  
B) No rotations are needed for deletion  
C) At most O(log n) rotations per insertion  
D) At most one rotation per insertion  

#### 11. Which of the following are properties of red-black trees?  
A) All root-to-external-node paths have the same number of red nodes  
B) No root-to-external-node path has two consecutive red nodes  
C) Root and all external nodes are black  
D) Height is between log2(n+1) and 2 log2(n+1)  

#### 12. Collapsing red nodes into their black parents in a red-black tree results in a tree with:  
A) Node degrees between 1 and 3  
B) All external nodes at the same level  
C) Node degrees between 2 and 4  
D) Height at least half the original height  

#### 13. Which of the following statements about insertions in red-black trees are true?  
A) Inserting a black node never requires rebalancing  
B) Inserting a red node may cause two consecutive red nodes  
C) Inserting a black node can cause an extra black node on one root-to-external path  
D) Color flips and rotations can fix violations caused by red node insertions  

#### 14. In red-black trees, what does the pattern XYr represent in the context of rebalancing?  
A) A deletion case  
B) A violation that cannot be fixed  
C) A color flip operation  
D) A rotation operation  

#### 15. Which rotations in red-black trees correspond directly to AVL tree rotations?  
A) RRb and RLb  
B) LLb and LRb  
C) Rr(1) and Rb1  
D) XYr and Rb0  

#### 16. When deleting a black leaf node in a red-black tree, what is the root of the deficient subtree called?  
A) py  
B) y  
C) w  
D) v  

#### 17. What happens if the deficient subtree root y is a red node during red-black tree deletion rebalancing?  
A) It is recolored black and deficiency is resolved  
B) A rotation is always required  
C) It is deleted immediately  
D) The entire tree becomes deficient  

#### 18. In red-black tree deletion, if y is black but not the root, and py is black, which case applies?  
A) Rb0 case 2  
B) Rb1 case 1  
C) Rb0 case 1  
D) Rb1 case 2  

#### 19. Which of the following statements about rotations and color flips in red-black trees are true?  
A) Color flips do not disturb the priority queue property in priority search trees  
B) At most one rotation and O(log n) color flips per insert/delete  
C) Rotations do not affect the priority queue property in priority search trees  
D) Red-black trees require O(log² n) time per insertion due to rotations  

#### 20. Which of the following are true about the complexity and implementation of red-black trees?  
A) C++ STL uses red-black trees for balanced maps  
B) java.util.TreeMap is implemented using AVL trees  
C) Red-black trees guarantee height at most 1.44 log2(n+2)  
D) Restructuring after insert/delete has O(1) amortized complexity in red-black trees  



<br>

## Answers

#### 1. What is the balance factor of a node in an AVL tree?  
A) ✗ Reverse order; balance factor is left minus right, not right minus left  
B) ✗ Depth difference is not used for balance factor  
C) ✓ Height of left subtree minus height of right subtree (Definition of balance factor)  
D) ✗ Balance factor is based on height, not number of nodes  

**Correct:** C


#### 2. Which of the following are true about the height of an AVL tree with n nodes?  
A) ✗ Height is not always exactly log2(n)  
B) ✓ Height is at most 1.44 log2(n+2) (Known upper bound for AVL trees)  
C) ✓ Height is at least log2(n+1) (Lower bound for any binary tree)  
D) ✗ Height cannot exceed 2 log2(n) for AVL trees  

**Correct:** B, C


#### 3. When inserting a new node into an AVL tree, at which point do you stop retracing and adjusting balance factors?  
A) ✓ Stop if balance factor becomes 0 (Height unchanged, no further rebalancing needed)  
B) ✗ Stop if balance factor is 2 or -2 (This indicates imbalance, so rebalancing is required)  
C) ✓ Stop if root is reached (No further ancestors to check)  
D) ✗ Retracing does not stop when reaching the inserted node again  

**Correct:** A, C


#### 4. Which imbalance type corresponds to the newly inserted node being in the right subtree of the right subtree of node A?  
A) ✗ RL is right-left imbalance  
B) ✗ LR is left-right imbalance  
C) ✗ LL is left-left imbalance  
D) ✓ RR is right-right imbalance (Right subtree of right subtree)  

**Correct:** D


#### 5. Which rotations are considered single rotations in AVL trees?  
A) ✗ RR and RL (RL is double rotation)  
B) ✓ LL and RR (Single rotations)  
C) ✗ LR and RL (Double rotations)  
D) ✗ LL and LR (LR is double rotation)  

**Correct:** B


#### 6. What is the effect of an LL rotation on the height of the subtree?  
A) ✗ Height does not increase after LL rotation  
B) ✗ Height does not double  
C) ✓ Subtree height remains unchanged (LL rotation restores balance without height change)  
D) ✗ Height does not decrease after LL rotation  

**Correct:** C


#### 7. After deleting a node from an AVL tree, if the balance factor of a node q becomes 0, what does this imply?  
A) ✗ Tree is not necessarily unbalanced at q if bf=0  
B) ✗ Height does not remain the same if bf=0 after deletion  
C) ✗ Height does not increase after deletion  
D) ✓ Height of subtree rooted at q has decreased by 1 (Balance factor 0 means height decreased)  

**Correct:** D


#### 8. In AVL deletion, what does it mean if the balance factor of an ancestor A becomes 2 after deletion from its left subtree?  
A) ✗ bf=2 means unbalanced, not balanced  
B) ✓ Type L imbalance (Deletion from left subtree causing bf=2)  
C) ✗ Rotations are needed when bf=2  
D) ✗ Type R imbalance corresponds to bf = -2 after deletion from right subtree  

**Correct:** B


#### 9. Which of the following statements about rotations during AVL deletion are true?  
A) ✓ R1 rotation reduces subtree height by 1 and requires continuing up the tree (Height decreases, rebalancing continues)  
B) ✗ R-1 rotation does not always stop rebalancing; it may continue  
C) ✓ R1 rotation is similar to LL rotation (Both fix left-heavy imbalance)  
D) ✓ R0 rotation does not change subtree height (No further adjustments needed)  

**Correct:** A, C, D


#### 10. Regarding the number of rotations needed for AVL tree operations, which is correct?  
A) ✓ At most O(log n) rotations per deletion (Deletion can cause cascading rebalances)  
B) ✗ Rotations are often needed for deletion  
C) ✗ Insertions do not require O(log n) rotations  
D) ✓ At most one rotation per insertion (AVL insertions require ≤1 rotation)  

**Correct:** A, D


#### 11. Which of the following are properties of red-black trees?  
A) ✗ Paths have same number of black nodes, not red nodes  
B) ✓ No root-to-external-node path has two consecutive red nodes (Red nodes cannot be adjacent)  
C) ✓ Root and all external nodes are black (Fundamental property)  
D) ✓ Height between log2(n+1) and 2 log2(n+1) (Known height bounds)  

**Correct:** B, C, D


#### 12. Collapsing red nodes into their black parents in a red-black tree results in a tree with:  
A) ✗ Node degrees are not between 1 and 3 after collapsing  
B) ✓ All external nodes at the same level (Property of 2-3-4 trees)  
C) ✓ Node degrees between 2 and 4 (Collapsed nodes form 2-4 tree nodes)  
D) ✓ Height at least half the original height (Collapsed height h' ≥ h/2)  

**Correct:** B, C, D


#### 13. Which of the following statements about insertions in red-black trees are true?  
A) ✗ Inserting a black node often requires rebalancing due to black height changes  
B) ✓ Inserting a red node may cause two consecutive red nodes (Red violation)  
C) ✓ Inserting a black node can cause an extra black node on one root-to-external path (Black height imbalance)  
D) ✓ Color flips and rotations can fix violations caused by red node insertions  

**Correct:** B, C, D


#### 14. In red-black trees, what does the pattern XYr represent in the context of rebalancing?  
A) ✗ Not related to deletion specifically  
B) ✗ It can be fixed by color flip, so not unfixable  
C) ✓ A color flip operation (XYr indicates color flip case)  
D) ✗ Not a rotation case  

**Correct:** C


#### 15. Which rotations in red-black trees correspond directly to AVL tree rotations?  
A) ✓ RRb and RLb (Symmetric to AVL RR and RL rotations)  
B) ✓ LLb and LRb (Same as AVL LL and LR rotations)  
C) ✗ Rr(1) and Rb1 are deletion cases, not direct AVL rotations  
D) ✗ XYr is color flip, not rotation  

**Correct:** A, B


#### 16. When deleting a black leaf node in a red-black tree, what is the root of the deficient subtree called?  
A) ✗ py is parent of y, not root of deficient subtree  
B) ✓ y (Root of deficient subtree)  
C) ✗ w is child of v, not root of deficient subtree  
D) ✗ v is sibling or child in rebalancing  

**Correct:** B


#### 17. What happens if the deficient subtree root y is a red node during red-black tree deletion rebalancing?  
A) ✓ It is recolored black and deficiency is resolved (Simple fix)  
B) ✗ Rotation is not always required in this case  
C) ✗ It is not deleted immediately; deletion already done  
D) ✗ Entire tree does not become deficient  

**Correct:** A


#### 18. In red-black tree deletion, if y is black but not the root, and py is black, which case applies?  
A) ✗ Rb0 case 2 applies if py is red  
B) ✗ Rb1 cases involve rotations, not just color changes  
C) ✓ Rb0 case 1 (py black, color change, continue rebalancing)  
D) ✗ Rb1 case 2 applies when py is red and rotations needed  

**Correct:** C


#### 19. Which of the following statements about rotations and color flips in red-black trees are true?  
A) ✓ Color flips do not disturb priority queue property in priority search trees  
B) ✓ At most one rotation and O(log n) color flips per insert/delete (Known complexity)  
C) ✗ Rotations do disturb priority queue property  
D) ✗ Red-black trees do not require O(log² n) time per insertion  

**Correct:** A, B


#### 20. Which of the following are true about the complexity and implementation of red-black trees?  
A) ✓ C++ STL uses red-black trees for balanced maps (True for std::map)  
B) ✗ java.util.TreeMap uses red-black trees, not AVL trees  
C) ✗ Height bound 1.44 log2(n+2) applies to AVL trees, not red-black trees  
D) ✗ O(1) amortized restructuring applies to AVL trees, not red-black trees  

**Correct:** A