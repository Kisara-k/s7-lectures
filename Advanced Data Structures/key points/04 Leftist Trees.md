## 4. Leftist Trees

## Key Points

#### 1. 🌳 Leftist Trees Basics  
- Leftist trees are linked binary trees that support heap operations (insert, remove min/max, initialize) with the same asymptotic complexity as heaps.  
- They allow melding (merging) two priority queues in **O(log n)** time.

#### 2. 🌲 Extended Binary Trees and s() Function  
- An extended binary tree is formed by adding external nodes wherever a subtree is empty, resulting in $n + 1$ external nodes for $n$ internal nodes.  
- For any node $x$, $s(x)$ is the length of the shortest path from $x$ to an external node in its subtree.  
- If $x$ is external, $s(x) = 0$; otherwise, $s(x) = \min(s(\text{leftChild}(x)), s(\text{rightChild}(x))) + 1$.

#### 3. 🌿 Leftist Tree Definition and Properties  
- A binary tree is a height-biased leftist tree if for every internal node $x$, $s(\text{leftChild}(x)) \geq s(\text{rightChild}(x))$.  
- In a leftist tree, the rightmost path is the shortest root-to-external-node path, and its length equals $s(\text{root})$.  
- The number of internal nodes $n$ satisfies $n \geq 2^{s(\text{root})} - 1$.  
- The length of the rightmost path is $O(\log n)$, where $n$ is the number of internal nodes.

#### 4. 🎯 Leftist Trees as Priority Queues  
- Min leftist trees maintain the minimum element at the root; max leftist trees maintain the maximum.  
- Operations supported include put (insert), removeMin, meld, and initialize.

#### 5. 🔄 Meld Operation  
- Meld compares roots of two trees, makes the smaller root the new root, and recursively melds the right subtree of the smaller root with the other tree.  
- After melding, if $s(\text{leftChild}) < s(\text{rightChild})$, the left and right children are swapped to maintain the leftist property.  
- Meld only traverses the rightmost paths, ensuring $O(\log n)$ time complexity.

#### 6. ➕ Insertion and Removal  
- Insertion (put) creates a single-node leftist tree and melds it with the existing tree in $O(\log n)$ time.  
- removeMin removes the root and melds its left and right subtrees, also in $O(\log n)$ time.

#### 7. ⚙️ Initialization in O(n) Time  
- Initialize by creating $n$ single-node trees, placing them in a FIFO queue, and repeatedly melding pairs until one tree remains.  
- This process runs in $O(n)$ time.

#### 8. ❌ Arbitrary Removal  
- Removing an arbitrary node $x$ (not root) involves replacing $x$ with its left subtree in its parent, adjusting $s()$ values and leftist property up to the root, then melding the right subtree of $x$ back.



<br>

