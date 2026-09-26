## 9. AVL Trees

## Questions

#### 1. What is the balance factor of a node in an AVL tree?  
A) Height of left subtree minus height of right subtree  
B) Height of right subtree minus height of left subtree  
C) Number of nodes in left subtree minus number of nodes in right subtree  
D) Difference between depths of left and right children  

#### 2. Which of the following are true about the height of an AVL tree with n nodes?  
A) It is at least log2(n+1)  
B) It is at most 1.44 log2(n+2)  
C) It is always exactly log2(n)  
D) It can be greater than 2 log2(n)  

#### 3. When inserting a new node into an AVL tree, at which point do you stop retracing and adjusting balance factors?  
A) When a node’s balance factor becomes 0  
B) When a node’s balance factor becomes 2 or -2  
C) When the root is reached  
D) When the newly inserted node is found again  

#### 4. Which imbalance type corresponds to the newly inserted node being in the right subtree of the right subtree of node A?  
A) LL  
B) RR  
C) LR  
D) RL  

#### 5. Which rotations are considered single rotations in AVL trees?  
A) LL and RR  
B) LR and RL  
C) LL and LR  
D) RR and RL  

#### 6. What is the effect of an LL rotation on the height of the subtree?  
A) Increases subtree height by 1  
B) Decreases subtree height by 1  
C) Subtree height remains unchanged  
D) Subtree height doubles  

#### 7. After deleting a node from an AVL tree, if the balance factor of a node q becomes 0, what does this imply?  
A) Height of subtree rooted at q has increased by 1  
B) Height of subtree rooted at q has decreased by 1  
C) Height of subtree rooted at q remains the same  
D) Tree is unbalanced at q  

#### 8. In AVL deletion, what does it mean if the balance factor of an ancestor A becomes 2 after deletion from its left subtree?  
A) Type L imbalance  
B) Type R imbalance  
C) Tree is balanced  
D) No rotations needed  

#### 9. Which of the following statements about rotations during AVL deletion are true?  
A) R0 rotation does not change subtree height  
B) R1 rotation reduces subtree height by 1 and requires continuing up the tree  
C) R-1 rotation always stops rebalancing  
D) R1 rotation is similar to LL rotation  

#### 10. Regarding the number of rotations needed for AVL tree operations, which is correct?  
A) At most one rotation per insertion  
B) At most O(log n) rotations per insertion  
C) At most O(log n) rotations per deletion  
D) No rotations are needed for deletion  

#### 11. Which of the following are properties of red-black trees?  
A) Root and all external nodes are black  
B) No root-to-external-node path has two consecutive red nodes  
C) All root-to-external-node paths have the same number of red nodes  
D) Height is between log2(n+1) and 2 log2(n+1)  

#### 12. Collapsing red nodes into their black parents in a red-black tree results in a tree with:  
A) Node degrees between 2 and 4  
B) Height at least half the original height  
C) All external nodes at the same level  
D) Node degrees between 1 and 3  

#### 13. Which of the following statements about insertions in red-black trees are true?  
A) Inserting a black node can cause an extra black node on one root-to-external path  
B) Inserting a red node may cause two consecutive red nodes  
C) Color flips and rotations can fix violations caused by red node insertions  
D) Inserting a black node never requires rebalancing  

#### 14. In red-black trees, what does the pattern XYr represent in the context of rebalancing?  
A) A color flip operation  
B) A rotation operation  
C) A violation that cannot be fixed  
D) A deletion case  

#### 15. Which rotations in red-black trees correspond directly to AVL tree rotations?  
A) LLb and LRb  
B) RRb and RLb  
C) XYr and Rb0  
D) Rr(1) and Rb1  

#### 16. When deleting a black leaf node in a red-black tree, what is the root of the deficient subtree called?  
A) y  
B) py  
C) v  
D) w  

#### 17. What happens if the deficient subtree root y is a red node during red-black tree deletion rebalancing?  
A) It is recolored black and deficiency is resolved  
B) It is deleted immediately  
C) The entire tree becomes deficient  
D) A rotation is always required  

#### 18. In red-black tree deletion, if y is black but not the root, and py is black, which case applies?  
A) Rb0 case 1  
B) Rb0 case 2  
C) Rb1 case 1  
D) Rb1 case 2  

#### 19. Which of the following statements about rotations and color flips in red-black trees are true?  
A) At most one rotation and O(log n) color flips per insert/delete  
B) Color flips do not disturb the priority queue property in priority search trees  
C) Rotations do not affect the priority queue property in priority search trees  
D) Red-black trees require O(log² n) time per insertion due to rotations  

#### 20. Which of the following are true about the complexity and implementation of red-black trees?  
A) C++ STL uses red-black trees for balanced maps  
B) java.util.TreeMap is implemented using AVL trees  
C) Restructuring after insert/delete has O(1) amortized complexity in red-black trees  
D) Red-black trees guarantee height at most 1.44 log2(n+2)



<br>

## Answers

#### 1. What is the balance factor of a node in an AVL tree?  
A) ✓ Height of left subtree minus height of right subtree (Definition of balance factor)  
B) ✗ Reverse order; balance factor is left minus right, not right minus left  
C) ✗ Balance factor is based on height, not number of nodes  
D) ✗ Depth difference is not used for balance factor  

**Correct:** A


#### 2. Which of the following are true about the height of an AVL tree with n nodes?  
A) ✓ Height is at least log2(n+1) (Lower bound for any binary tree)  
B) ✓ Height is at most 1.44 log2(n+2) (Known upper bound for AVL trees)  
C) ✗ Height is not always exactly log2(n)  
D) ✗ Height cannot exceed 2 log2(n) for AVL trees  

**Correct:** A,B


#### 3. When inserting a new node into an AVL tree, at which point do you stop retracing and adjusting balance factors?  
A) ✓ Stop if balance factor becomes 0 (Height unchanged, no further rebalancing needed)  
B) ✗ Stop if balance factor is 2 or -2 (This indicates imbalance, so rebalancing is required)  
C) ✓ Stop if root is reached (No further ancestors to check)  
D) ✗ Retracing does not stop when reaching the inserted node again  

**Correct:** A,C


#### 4. Which imbalance type corresponds to the newly inserted node being in the right subtree of the right subtree of node A?  
A) ✗ LL is left-left imbalance  
B) ✓ RR is right-right imbalance (Right subtree of right subtree)  
C) ✗ LR is left-right imbalance  
D) ✗ RL is right-left imbalance  

**Correct:** B


#### 5. Which rotations are considered single rotations in AVL trees?  
A) ✓ LL and RR (Single rotations)  
B) ✗ LR and RL (Double rotations)  
C) ✗ LL and LR (LR is double rotation)  
D) ✗ RR and RL (RL is double rotation)  

**Correct:** A


#### 6. What is the effect of an LL rotation on the height of the subtree?  
A) ✗ Height does not increase after LL rotation  
B) ✗ Height does not decrease after LL rotation  
C) ✓ Subtree height remains unchanged (LL rotation restores balance without height change)  
D) ✗ Height does not double  

**Correct:** C


#### 7. After deleting a node from an AVL tree, if the balance factor of a node q becomes 0, what does this imply?  
A) ✗ Height does not increase after deletion  
B) ✓ Height of subtree rooted at q has decreased by 1 (Balance factor 0 means height decreased)  
C) ✗ Height does not remain the same if bf=0 after deletion  
D) ✗ Tree is not necessarily unbalanced at q if bf=0  

**Correct:** B


#### 8. In AVL deletion, what does it mean if the balance factor of an ancestor A becomes 2 after deletion from its left subtree?  
A) ✓ Type L imbalance (Deletion from left subtree causing bf=2)  
B) ✗ Type R imbalance corresponds to bf = -2 after deletion from right subtree  
C) ✗ bf=2 means unbalanced, not balanced  
D) ✗ Rotations are needed when bf=2  

**Correct:** A


#### 9. Which of the following statements about rotations during AVL deletion are true?  
A) ✓ R0 rotation does not change subtree height (No further adjustments needed)  
B) ✓ R1 rotation reduces subtree height by 1 and requires continuing up the tree (Height decreases, rebalancing continues)  
C) ✗ R-1 rotation does not always stop rebalancing; it may continue  
D) ✓ R1 rotation is similar to LL rotation (Both fix left-heavy imbalance)  

**Correct:** A,B,D


#### 10. Regarding the number of rotations needed for AVL tree operations, which is correct?  
A) ✓ At most one rotation per insertion (AVL insertions require ≤1 rotation)  
B) ✗ Insertions do not require O(log n) rotations  
C) ✓ At most O(log n) rotations per deletion (Deletion can cause cascading rebalances)  
D) ✗ Rotations are often needed for deletion  

**Correct:** A,C


#### 11. Which of the following are properties of red-black trees?  
A) ✓ Root and all external nodes are black (Fundamental property)  
B) ✓ No root-to-external-node path has two consecutive red nodes (Red nodes cannot be adjacent)  
C) ✗ Paths have same number of black nodes, not red nodes  
D) ✓ Height between log2(n+1) and 2 log2(n+1) (Known height bounds)  

**Correct:** A,B,D


#### 12. Collapsing red nodes into their black parents in a red-black tree results in a tree with:  
A) ✓ Node degrees between 2 and 4 (Collapsed nodes form 2-4 tree nodes)  
B) ✓ Height at least half the original height (Collapsed height h' ≥ h/2)  
C) ✓ All external nodes at the same level (Property of 2-3-4 trees)  
D) ✗ Node degrees are not between 1 and 3 after collapsing  

**Correct:** A,B,C


#### 13. Which of the following statements about insertions in red-black trees are true?  
A) ✓ Inserting a black node can cause an extra black node on one root-to-external path (Black height imbalance)  
B) ✓ Inserting a red node may cause two consecutive red nodes (Red violation)  
C) ✓ Color flips and rotations can fix violations caused by red node insertions  
D) ✗ Inserting a black node often requires rebalancing due to black height changes  

**Correct:** A,B,C


#### 14. In red-black trees, what does the pattern XYr represent in the context of rebalancing?  
A) ✓ A color flip operation (XYr indicates color flip case)  
B) ✗ Not a rotation case  
C) ✗ It can be fixed by color flip, so not unfixable  
D) ✗ Not related to deletion specifically  

**Correct:** A


#### 15. Which rotations in red-black trees correspond directly to AVL tree rotations?  
A) ✓ LLb and LRb (Same as AVL LL and LR rotations)  
B) ✓ RRb and RLb (Symmetric to AVL RR and RL rotations)  
C) ✗ XYr is color flip, not rotation  
D) ✗ Rr(1) and Rb1 are deletion cases, not direct AVL rotations  

**Correct:** A,B


#### 16. When deleting a black leaf node in a red-black tree, what is the root of the deficient subtree called?  
A) ✓ y (Root of deficient subtree)  
B) ✗ py is parent of y, not root of deficient subtree  
C) ✗ v is sibling or child in rebalancing  
D) ✗ w is child of v, not root of deficient subtree  

**Correct:** A


#### 17. What happens if the deficient subtree root y is a red node during red-black tree deletion rebalancing?  
A) ✓ It is recolored black and deficiency is resolved (Simple fix)  
B) ✗ It is not deleted immediately; deletion already done  
C) ✗ Entire tree does not become deficient  
D) ✗ Rotation is not always required in this case  

**Correct:** A


#### 18. In red-black tree deletion, if y is black but not the root, and py is black, which case applies?  
A) ✓ Rb0 case 1 (py black, color change, continue rebalancing)  
B) ✗ Rb0 case 2 applies if py is red  
C) ✗ Rb1 cases involve rotations, not just color changes  
D) ✗ Rb1 case 2 applies when py is red and rotations needed  

**Correct:** A


#### 19. Which of the following statements about rotations and color flips in red-black trees are true?  
A) ✓ At most one rotation and O(log n) color flips per insert/delete (Known complexity)  
B) ✓ Color flips do not disturb priority queue property in priority search trees  
C) ✗ Rotations do disturb priority queue property  
D) ✗ Red-black trees do not require O(log² n) time per insertion  

**Correct:** A,B


#### 20. Which of the following are true about the complexity and implementation of red-black trees?  
A) ✓ C++ STL uses red-black trees for balanced maps (True for std::map)  
B) ✗ java.util.TreeMap uses red-black trees, not AVL trees  
C) ✗ O(1) amortized restructuring applies to AVL trees, not red-black trees  
D) ✗ Height bound 1.44 log2(n+2) applies to AVL trees, not red-black trees  

**Correct:** A