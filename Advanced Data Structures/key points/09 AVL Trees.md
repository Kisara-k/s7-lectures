## 9. AVL Trees

## Key Points

#### 1. 🌳 AVL Tree Definition and Balance Factor
- AVL trees are binary search trees where the balance factor of every node is -1, 0, or 1.
- Balance factor = height(left subtree) - height(right subtree).

#### 2. 📏 AVL Tree Height Bound
- Height of an AVL tree with $n$ nodes is at most $1.44 \log_2 (n+2)$.
- Height of any binary tree with $n$ nodes is at least $\log_2 (n+1)$.
- Minimum number of nodes in AVL tree of height $h$ follows $N_h = 1 + N_{h-1} + N_{h-2}$ (Fibonacci relation).

#### 3. 🔄 AVL Tree Insertion and Imbalance Types
- After insertion, retrace path to root adjusting balance factors.
- Tree becomes unbalanced if a node’s balance factor becomes +2 or -2.
- Four imbalance types: RR, LL, RL, LR.
- Single rotations fix RR and LL imbalances.
- Double rotations fix RL and LR imbalances.

#### 4. ❌ AVL Tree Deletion and Rebalancing
- After deletion, retrace path to root updating balance factors.
- New balance factor changes by ±1 depending on which subtree deletion occurred.
- Imbalance after deletion classified as type L or R.
- Rotations used: R0 (like LL), R1 (like LL with height reduction), R-1 (like LR).
- At most 1 rotation needed for insertion; up to O(log n) rotations for deletion.

#### 5. 🟥 Red-Black Tree Properties
- Each node is red or black.
- Root and all external (null) nodes are black.
- No path from root to leaf has two consecutive red nodes.
- All root-to-leaf paths have the same number of black nodes.
- Height of red-black tree with $n$ nodes is between $\log_2 (n+1)$ and $2 \log_2 (n+1)$.

#### 6. 🔧 Red-Black Tree Insertion Fixes
- New nodes inserted as red.
- Violations (two consecutive red nodes) fixed by color flips and/or rotations.
- Cases classified by relationships $XYz$ (grandparent-parent-child and sibling colors).
- Rotations used are analogous to AVL rotations (LL, LR, RR, RL).

#### 7. 🔧 Red-Black Tree Deletion Fixes
- Deleting a red node requires no rebalancing.
- Deleting a black node causes black deficiency in subtree.
- Deficiency fixed by color changes and rotations (cases Rb0, Rb1, Rr1).
- Fixing may propagate up to the root.

#### 8. ⚙️ Performance and Implementation
- AVL insertions require at most 1 rotation; deletions up to O(log n) rotations.
- Red-black trees require at most 1 rotation and O(log n) color flips per insert/delete.
- Red-black trees are widely used in standard libraries (e.g., C++ STL, Java TreeMap).



<br>

