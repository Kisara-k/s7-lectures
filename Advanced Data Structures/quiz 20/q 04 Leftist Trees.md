## 4. Leftist Trees

## Questions

#### 1. What is the defining property of a height-biased leftist tree regarding the s() values of its children?  
A) s(leftChild(x)) ≥ s(rightChild(x)) for every internal node x  
B) s(leftChild(x)) + s(rightChild(x)) = s(x) for every internal node x  
C) s(leftChild(x)) ≤ s(rightChild(x)) for every internal node x  
D) s(leftChild(x)) = s(rightChild(x)) for every internal node x  

#### 2. In an extended binary tree, what is the relationship between the number of external nodes and internal nodes?  
A) Number of external nodes = number of internal nodes - 1  
B) Number of external nodes = number of internal nodes + 1  
C) Number of external nodes = 2 × number of internal nodes  
D) Number of external nodes = number of internal nodes  

#### 3. For any node x in an extended binary tree, how is s(x) defined?  
A) The number of external nodes in the subtree rooted at x  
B) The length of the shortest path from x to an external node in its subtree  
C) The length of the longest path from x to an external node in its subtree  
D) The height of the subtree rooted at x  

#### 4. Which of the following operations can be performed on a leftist tree with the same asymptotic complexity as a heap?  
A) Initialize  
B) Insert  
C) Search for an arbitrary element  
D) Remove minimum (or maximum)  

#### 5. What is the time complexity of melding two leftist trees with n total nodes?  
A) O(log n)  
B) O(n log n)  
C) O(1)  
D) O(n)  

#### 6. Which path in a leftist tree corresponds to the shortest root-to-external-node path?  
A) Path with maximum s() values  
B) Rightmost path  
C) Path with minimum s() values  
D) Leftmost path  

#### 7. Given a leftist tree with n internal nodes and root s-value s(root), which inequality correctly relates n and s(root)?  
A) n = s(root) + 1  
B) n ≤ 2^(s(root)) - 1  
C) n ≤ s(root)²  
D) n ≥ 2^(s(root)) - 1  

#### 8. What is the asymptotic upper bound on the length of the rightmost path in a leftist tree with n internal nodes?  
A) O(log n)  
B) O(1)  
C) O(√n)  
D) O(n)  

#### 9. Which of the following statements about min leftist trees is true?  
A) They cannot be melded efficiently  
B) They maintain the leftist property based on s() values  
C) They are used as max priority queues  
D) The root always contains the minimum element  

#### 10. During the meld operation of two min leftist trees, which subtree is recursively melded?  
A) Left subtree of the tree with the larger root  
B) Right subtree of the tree with the smaller root  
C) Left subtree of the tree with the smaller root  
D) Right subtree of the tree with the larger root  

#### 11. After melding two min leftist trees, what condition triggers swapping the left and right subtrees of the root?  
A) The root value is larger than both children  
B) s(left) > s(right)  
C) s(left) = s(right)  
D) s(left) < s(right)  

#### 12. What is the purpose of adding external nodes to a binary tree to form an extended binary tree?  
A) To balance the tree  
B) To ensure every internal node has exactly two children  
C) To reduce the number of internal nodes  
D) To increase the height of the tree  

#### 13. Which of the following best describes the initialization of a leftist tree priority queue in O(n) time?  
A) Build a balanced binary search tree first, then convert to leftist tree  
B) Insert all elements one by one using put()  
C) Use a heapify-like bottom-up approach  
D) Create n single-node trees, then repeatedly meld pairs until one remains  

#### 14. When removing an arbitrary element x (not the root) from a leftist tree, what is the correct sequence of steps?  
A) Remove x, then meld its left and right subtrees directly  
B) Make the left subtree of x the right subtree of x’s parent, adjust s() and leftist property up to root, then meld with the right subtree of x  
C) Remove x and do nothing else  
D) Replace x with the root, then remove the root  

#### 15. Which of the following is NOT a property of s(x) in an extended binary tree?  
A) s(x) = min{s(leftChild(x)), s(rightChild(x))} + 1 if x is internal  
B) s(x) measures the shortest path length to an external node  
C) s(x) = 0 if x is an external node  
D) s(x) is always equal to the height of the subtree rooted at x  

#### 16. Why does the rightmost path in a leftist tree have length O(log n)?  
A) Because s(root) is always constant  
B) Because the left subtree is always empty  
C) Because the number of internal nodes is at least 2^(length of rightmost path) - 1  
D) Because the tree is balanced like an AVL tree  

#### 17. Which of the following statements about the put() operation in a min leftist tree is correct?  
A) It inserts the new element at the root directly  
B) It removes the minimum element before inserting  
C) It always traverses the leftmost path to insert  
D) It creates a single-node min leftist tree and melds it with the existing tree  

#### 18. What happens if during melding, the right subtree of the tree with the smaller root is empty?  
A) The meld operation fails  
B) The left subtree is melded instead  
C) The result is just the other tree  
D) The trees are swapped before melding  

#### 19. Which of the following is true about the number of external nodes in a leftist tree with n internal nodes?  
A) It depends on the shape of the tree  
B) It is at least 2n  
C) It is exactly n + 1  
D) It is exactly n  

#### 20. In the context of leftist trees, what is the main advantage of maintaining the leftist property (s(left) ≥ s(right))?  
A) It guarantees logarithmic time complexity for meld, insert, and remove operations  
B) It ensures the tree is perfectly balanced  
C) It minimizes the height of the tree  
D) It maximizes the number of external nodes  



<br>

## Answers

#### 1. What is the defining property of a height-biased leftist tree regarding the s() values of its children?  
A) ✓ s(leftChild(x)) ≥ s(rightChild(x)) is the defining property of height-biased leftist trees.  
B) ✗ s(leftChild(x)) + s(rightChild(x)) ≠ s(x); s(x) depends on min of children plus one.  
C) ✗ s(leftChild(x)) ≤ s(rightChild(x)) is the opposite of the leftist property.  
D) ✗ s(leftChild(x)) = s(rightChild(x)) is not required, only inequality matters.  

**Correct:** A


#### 2. In an extended binary tree, what is the relationship between the number of external nodes and internal nodes?  
A) ✗ External nodes are not fewer than internal nodes.  
B) ✓ Number of external nodes = number of internal nodes + 1 is a known property.  
C) ✗ External nodes are not double internal nodes.  
D) ✗ They are not equal; external nodes exceed internal nodes.  

**Correct:** B


#### 3. For any node x in an extended binary tree, how is s(x) defined?  
A) ✗ s(x) is a path length, not a count of external nodes.  
B) ✓ s(x) is the length of the shortest path from x to an external node in its subtree.  
C) ✗ s(x) is the shortest path length, not the longest.  
D) ✗ s(x) is not the height but shortest path length to external node.  

**Correct:** B


#### 4. Which of the following operations can be performed on a leftist tree with the same asymptotic complexity as a heap?  
A) ✓ Initialize can be done efficiently like a heap.  
B) ✓ Insert is supported with heap-like complexity.  
C) ✗ Search for arbitrary element is not guaranteed efficient in leftist trees.  
D) ✓ Remove minimum (or maximum) is supported similarly.  

**Correct:** A, B, D


#### 5. What is the time complexity of melding two leftist trees with n total nodes?  
A) ✓ O(log n) is the known complexity due to rightmost path length.  
B) ✗ O(n log n) is incorrect for melding.  
C) ✗ O(1) is too optimistic; melding requires path traversal.  
D) ✗ O(n) is too large for melding.  

**Correct:** A


#### 6. Which path in a leftist tree corresponds to the shortest root-to-external-node path?  
A) ✗ Path with max s() values is not shortest.  
B) ✓ Rightmost path is the shortest root-to-external-node path by property.  
C) ✗ Path with min s() values is the rightmost path, but s() is node property, not path.  
D) ✗ Leftmost path is not guaranteed shortest.  

**Correct:** B


#### 7. Given a leftist tree with n internal nodes and root s-value s(root), which inequality correctly relates n and s(root)?  
A) ✗ n = s(root) + 1 is incorrect.  
B) ✗ n ≤ 2^(s(root)) - 1 is reversed.  
C) ✗ n ≤ s(root)² is not supported.  
D) ✓ n ≥ 2^(s(root)) - 1 is correct from property 2.  

**Correct:** D


#### 8. What is the asymptotic upper bound on the length of the rightmost path in a leftist tree with n internal nodes?  
A) ✓ O(log n) is correct due to the leftist property and s(root) bound.  
B) ✗ O(1) is too small.  
C) ✗ O(√n) is not supported.  
D) ✗ O(n) is too large.  

**Correct:** A


#### 9. Which of the following statements about min leftist trees is true?  
A) ✗ They can be melded efficiently in O(log n).  
B) ✓ They maintain the leftist property based on s() values.  
C) ✗ Min leftist trees are used as min priority queues, not max.  
D) ✓ The root always contains the minimum element in a min leftist tree.  

**Correct:** B, D


#### 10. During the meld operation of two min leftist trees, which subtree is recursively melded?  
A) ✗ Left subtree of larger root is not melded recursively.  
B) ✓ Right subtree of the tree with the smaller root is melded recursively.  
C) ✗ Left subtree of smaller root is not melded recursively.  
D) ✗ Right subtree of larger root is not melded recursively.  

**Correct:** B


#### 11. After melding two min leftist trees, what condition triggers swapping the left and right subtrees of the root?  
A) ✗ Root value comparison does not determine swap.  
B) ✗ Swap occurs if s(left) < s(right), not greater.  
C) ✗ Equal s() values do not trigger swap.  
D) ✓ Swap occurs if s(left) < s(right) to maintain leftist property.  

**Correct:** D


#### 12. What is the purpose of adding external nodes to a binary tree to form an extended binary tree?  
A) ✗ It does not necessarily balance the tree.  
B) ✓ To ensure every internal node has exactly two children (full binary tree).  
C) ✗ It does not reduce internal nodes.  
D) ✗ It does not increase height necessarily.  

**Correct:** B


#### 13. Which of the following best describes the initialization of a leftist tree priority queue in O(n) time?  
A) ✗ Building a BST first is unrelated.  
B) ✗ Inserting one by one is O(n log n), not O(n).  
C) ✗ Heapify-like bottom-up approach is not used here.  
D) ✓ Creating n single-node trees and repeatedly melding pairs until one remains is correct.  

**Correct:** D


#### 14. When removing an arbitrary element x (not the root) from a leftist tree, what is the correct sequence of steps?  
A) ✗ Meld left and right subtrees directly is incomplete.  
B) ✓ Make left subtree of x the right subtree of x’s parent, adjust s() and leftist property up to root, then meld with right subtree of x.  
C) ✗ Removing x and doing nothing else breaks the tree.  
D) ✗ Replacing x with root is incorrect.  

**Correct:** B


#### 15. Which of the following is NOT a property of s(x) in an extended binary tree?  
A) ✓ s(x) = min{s(leftChild(x)), s(rightChild(x))} + 1 if internal is true.  
B) ✓ s(x) measures shortest path length to external node is true.  
C) ✓ s(x) = 0 if x is external node is true.  
D) ✗ s(x) equals height is false; s(x) is shortest path length, not height.  

**Correct:** D


#### 16. Why does the rightmost path in a leftist tree have length O(log n)?  
A) ✗ s(root) is not constant.  
B) ✗ Left subtree is not always empty.  
C) ✓ Because n ≥ 2^(length of rightmost path) - 1, bounding path length logarithmically.  
D) ✗ Leftist trees are not balanced like AVL trees.  

**Correct:** C


#### 17. Which of the following statements about the put() operation in a min leftist tree is correct?  
A) ✗ New element is not inserted directly at root.  
B) ✗ put() does not remove minimum before inserting.  
C) ✗ put() does not traverse leftmost path specifically.  
D) ✓ put() creates a single-node min leftist tree and melds it with existing tree.  

**Correct:** D


#### 18. What happens if during melding, the right subtree of the tree with the smaller root is empty?  
A) ✗ Meld does not fail.  
B) ✗ Left subtree is not melded instead.  
C) ✓ Result is just the other tree, since melding empty subtree with other tree returns the other tree.  
D) ✗ Trees are not swapped before melding in this case.  

**Correct:** C


#### 19. Which of the following is true about the number of external nodes in a leftist tree with n internal nodes?  
A) ✗ Number of external nodes does not depend on shape; it is fixed by n.  
B) ✗ External nodes are not at least 2n.  
C) ✓ External nodes are exactly n + 1, as in any extended binary tree.  
D) ✗ External nodes are not exactly n.  

**Correct:** C


#### 20. In the context of leftist trees, what is the main advantage of maintaining the leftist property (s(left) ≥ s(right))?  
A) ✓ It guarantees logarithmic time complexity for meld, insert, and remove operations by bounding right path length.  
B) ✗ It does not ensure perfect balance.  
C) ✗ It does not minimize height overall.  
D) ✗ It does not maximize external nodes; external nodes count is fixed by n.  

**Correct:** A