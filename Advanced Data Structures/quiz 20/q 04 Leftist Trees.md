## 4. Leftist Trees

## Questions

#### 1. What is the defining property of a height-biased leftist tree regarding the s() values of its children?  
A) s(leftChild(x)) ≤ s(rightChild(x)) for every internal node x  
B) s(leftChild(x)) ≥ s(rightChild(x)) for every internal node x  
C) s(leftChild(x)) = s(rightChild(x)) for every internal node x  
D) s(leftChild(x)) + s(rightChild(x)) = s(x) for every internal node x  

#### 2. In an extended binary tree, what is the relationship between the number of external nodes and internal nodes?  
A) Number of external nodes = number of internal nodes  
B) Number of external nodes = number of internal nodes + 1  
C) Number of external nodes = 2 × number of internal nodes  
D) Number of external nodes = number of internal nodes - 1  

#### 3. For any node x in an extended binary tree, how is s(x) defined?  
A) The length of the longest path from x to an external node in its subtree  
B) The length of the shortest path from x to an external node in its subtree  
C) The number of external nodes in the subtree rooted at x  
D) The height of the subtree rooted at x  

#### 4. Which of the following operations can be performed on a leftist tree with the same asymptotic complexity as a heap?  
A) Insert  
B) Remove minimum (or maximum)  
C) Initialize  
D) Search for an arbitrary element  

#### 5. What is the time complexity of melding two leftist trees with n total nodes?  
A) O(1)  
B) O(log n)  
C) O(n)  
D) O(n log n)  

#### 6. Which path in a leftist tree corresponds to the shortest root-to-external-node path?  
A) Leftmost path  
B) Rightmost path  
C) Path with maximum s() values  
D) Path with minimum s() values  

#### 7. Given a leftist tree with n internal nodes and root s-value s(root), which inequality correctly relates n and s(root)?  
A) n ≤ 2^(s(root)) - 1  
B) n ≥ 2^(s(root)) - 1  
C) n = s(root) + 1  
D) n ≤ s(root)²  

#### 8. What is the asymptotic upper bound on the length of the rightmost path in a leftist tree with n internal nodes?  
A) O(n)  
B) O(log n)  
C) O(√n)  
D) O(1)  

#### 9. Which of the following statements about min leftist trees is true?  
A) They are used as max priority queues  
B) The root always contains the minimum element  
C) They cannot be melded efficiently  
D) They maintain the leftist property based on s() values  

#### 10. During the meld operation of two min leftist trees, which subtree is recursively melded?  
A) Left subtree of the tree with the larger root  
B) Right subtree of the tree with the smaller root  
C) Left subtree of the tree with the smaller root  
D) Right subtree of the tree with the larger root  

#### 11. After melding two min leftist trees, what condition triggers swapping the left and right subtrees of the root?  
A) s(left) > s(right)  
B) s(left) < s(right)  
C) s(left) = s(right)  
D) The root value is larger than both children  

#### 12. What is the purpose of adding external nodes to a binary tree to form an extended binary tree?  
A) To increase the height of the tree  
B) To ensure every internal node has exactly two children  
C) To balance the tree  
D) To reduce the number of internal nodes  

#### 13. Which of the following best describes the initialization of a leftist tree priority queue in O(n) time?  
A) Insert all elements one by one using put()  
B) Create n single-node trees, then repeatedly meld pairs until one remains  
C) Build a balanced binary search tree first, then convert to leftist tree  
D) Use a heapify-like bottom-up approach  

#### 14. When removing an arbitrary element x (not the root) from a leftist tree, what is the correct sequence of steps?  
A) Remove x, then meld its left and right subtrees directly  
B) Replace x with the root, then remove the root  
C) Make the left subtree of x the right subtree of x’s parent, adjust s() and leftist property up to root, then meld with the right subtree of x  
D) Remove x and do nothing else  

#### 15. Which of the following is NOT a property of s(x) in an extended binary tree?  
A) s(x) = 0 if x is an external node  
B) s(x) = min{s(leftChild(x)), s(rightChild(x))} + 1 if x is internal  
C) s(x) is always equal to the height of the subtree rooted at x  
D) s(x) measures the shortest path length to an external node  

#### 16. Why does the rightmost path in a leftist tree have length O(log n)?  
A) Because the tree is balanced like an AVL tree  
B) Because the number of internal nodes is at least 2^(length of rightmost path) - 1  
C) Because s(root) is always constant  
D) Because the left subtree is always empty  

#### 17. Which of the following statements about the put() operation in a min leftist tree is correct?  
A) It inserts the new element at the root directly  
B) It creates a single-node min leftist tree and melds it with the existing tree  
C) It always traverses the leftmost path to insert  
D) It removes the minimum element before inserting  

#### 18. What happens if during melding, the right subtree of the tree with the smaller root is empty?  
A) The meld operation fails  
B) The result is just the other tree  
C) The trees are swapped before melding  
D) The left subtree is melded instead  

#### 19. Which of the following is true about the number of external nodes in a leftist tree with n internal nodes?  
A) It is exactly n  
B) It is exactly n + 1  
C) It is at least 2n  
D) It depends on the shape of the tree  

#### 20. In the context of leftist trees, what is the main advantage of maintaining the leftist property (s(left) ≥ s(right))?  
A) It ensures the tree is perfectly balanced  
B) It guarantees logarithmic time complexity for meld, insert, and remove operations  
C) It minimizes the height of the tree  
D) It maximizes the number of external nodes



<br>

## Answers

#### 1. What is the defining property of a height-biased leftist tree regarding the s() values of its children?  
A) ✗ s(leftChild(x)) ≤ s(rightChild(x)) is the opposite of the leftist property.  
B) ✓ s(leftChild(x)) ≥ s(rightChild(x)) is the defining property of height-biased leftist trees.  
C) ✗ s(leftChild(x)) = s(rightChild(x)) is not required, only inequality matters.  
D) ✗ s(leftChild(x)) + s(rightChild(x)) ≠ s(x); s(x) depends on min of children plus one.  

**Correct:** B


#### 2. In an extended binary tree, what is the relationship between the number of external nodes and internal nodes?  
A) ✗ They are not equal; external nodes exceed internal nodes.  
B) ✓ Number of external nodes = number of internal nodes + 1 is a known property.  
C) ✗ External nodes are not double internal nodes.  
D) ✗ External nodes are not fewer than internal nodes.  

**Correct:** B


#### 3. For any node x in an extended binary tree, how is s(x) defined?  
A) ✗ s(x) is the shortest path length, not the longest.  
B) ✓ s(x) is the length of the shortest path from x to an external node in its subtree.  
C) ✗ s(x) is a path length, not a count of external nodes.  
D) ✗ s(x) is not the height but shortest path length to external node.  

**Correct:** B


#### 4. Which of the following operations can be performed on a leftist tree with the same asymptotic complexity as a heap?  
A) ✓ Insert is supported with heap-like complexity.  
B) ✓ Remove minimum (or maximum) is supported similarly.  
C) ✓ Initialize can be done efficiently like a heap.  
D) ✗ Search for arbitrary element is not guaranteed efficient in leftist trees.  

**Correct:** A,B,C


#### 5. What is the time complexity of melding two leftist trees with n total nodes?  
A) ✗ O(1) is too optimistic; melding requires path traversal.  
B) ✓ O(log n) is the known complexity due to rightmost path length.  
C) ✗ O(n) is too large for melding.  
D) ✗ O(n log n) is incorrect for melding.  

**Correct:** B


#### 6. Which path in a leftist tree corresponds to the shortest root-to-external-node path?  
A) ✗ Leftmost path is not guaranteed shortest.  
B) ✓ Rightmost path is the shortest root-to-external-node path by property.  
C) ✗ Path with max s() values is not shortest.  
D) ✗ Path with min s() values is the rightmost path, but s() is node property, not path.  

**Correct:** B


#### 7. Given a leftist tree with n internal nodes and root s-value s(root), which inequality correctly relates n and s(root)?  
A) ✗ n ≤ 2^(s(root)) - 1 is reversed.  
B) ✓ n ≥ 2^(s(root)) - 1 is correct from property 2.  
C) ✗ n = s(root) + 1 is incorrect.  
D) ✗ n ≤ s(root)² is not supported.  

**Correct:** B


#### 8. What is the asymptotic upper bound on the length of the rightmost path in a leftist tree with n internal nodes?  
A) ✗ O(n) is too large.  
B) ✓ O(log n) is correct due to the leftist property and s(root) bound.  
C) ✗ O(√n) is not supported.  
D) ✗ O(1) is too small.  

**Correct:** B


#### 9. Which of the following statements about min leftist trees is true?  
A) ✗ Min leftist trees are used as min priority queues, not max.  
B) ✓ The root always contains the minimum element in a min leftist tree.  
C) ✗ They can be melded efficiently in O(log n).  
D) ✓ They maintain the leftist property based on s() values.  

**Correct:** B,D


#### 10. During the meld operation of two min leftist trees, which subtree is recursively melded?  
A) ✗ Left subtree of larger root is not melded recursively.  
B) ✓ Right subtree of the tree with the smaller root is melded recursively.  
C) ✗ Left subtree of smaller root is not melded recursively.  
D) ✗ Right subtree of larger root is not melded recursively.  

**Correct:** B


#### 11. After melding two min leftist trees, what condition triggers swapping the left and right subtrees of the root?  
A) ✗ Swap occurs if s(left) < s(right), not greater.  
B) ✓ Swap occurs if s(left) < s(right) to maintain leftist property.  
C) ✗ Equal s() values do not trigger swap.  
D) ✗ Root value comparison does not determine swap.  

**Correct:** B


#### 12. What is the purpose of adding external nodes to a binary tree to form an extended binary tree?  
A) ✗ It does not increase height necessarily.  
B) ✓ To ensure every internal node has exactly two children (full binary tree).  
C) ✗ It does not necessarily balance the tree.  
D) ✗ It does not reduce internal nodes.  

**Correct:** B


#### 13. Which of the following best describes the initialization of a leftist tree priority queue in O(n) time?  
A) ✗ Inserting one by one is O(n log n), not O(n).  
B) ✓ Creating n single-node trees and repeatedly melding pairs until one remains is correct.  
C) ✗ Building a BST first is unrelated.  
D) ✗ Heapify-like bottom-up approach is not used here.  

**Correct:** B


#### 14. When removing an arbitrary element x (not the root) from a leftist tree, what is the correct sequence of steps?  
A) ✗ Meld left and right subtrees directly is incomplete.  
B) ✗ Replacing x with root is incorrect.  
C) ✓ Make left subtree of x the right subtree of x’s parent, adjust s() and leftist property up to root, then meld with right subtree of x.  
D) ✗ Removing x and doing nothing else breaks the tree.  

**Correct:** C


#### 15. Which of the following is NOT a property of s(x) in an extended binary tree?  
A) ✓ s(x) = 0 if x is external node is true.  
B) ✓ s(x) = min{s(leftChild(x)), s(rightChild(x))} + 1 if internal is true.  
C) ✗ s(x) equals height is false; s(x) is shortest path length, not height.  
D) ✓ s(x) measures shortest path length to external node is true.  

**Correct:** C


#### 16. Why does the rightmost path in a leftist tree have length O(log n)?  
A) ✗ Leftist trees are not balanced like AVL trees.  
B) ✓ Because n ≥ 2^(length of rightmost path) - 1, bounding path length logarithmically.  
C) ✗ s(root) is not constant.  
D) ✗ Left subtree is not always empty.  

**Correct:** B


#### 17. Which of the following statements about the put() operation in a min leftist tree is correct?  
A) ✗ New element is not inserted directly at root.  
B) ✓ put() creates a single-node min leftist tree and melds it with existing tree.  
C) ✗ put() does not traverse leftmost path specifically.  
D) ✗ put() does not remove minimum before inserting.  

**Correct:** B


#### 18. What happens if during melding, the right subtree of the tree with the smaller root is empty?  
A) ✗ Meld does not fail.  
B) ✓ Result is just the other tree, since melding empty subtree with other tree returns the other tree.  
C) ✗ Trees are not swapped before melding in this case.  
D) ✗ Left subtree is not melded instead.  

**Correct:** B


#### 19. Which of the following is true about the number of external nodes in a leftist tree with n internal nodes?  
A) ✗ External nodes are not exactly n.  
B) ✓ External nodes are exactly n + 1, as in any extended binary tree.  
C) ✗ External nodes are not at least 2n.  
D) ✗ Number of external nodes does not depend on shape; it is fixed by n.  

**Correct:** B


#### 20. In the context of leftist trees, what is the main advantage of maintaining the leftist property (s(left) ≥ s(right))?  
A) ✗ It does not ensure perfect balance.  
B) ✓ It guarantees logarithmic time complexity for meld, insert, and remove operations by bounding right path length.  
C) ✗ It does not minimize height overall.  
D) ✗ It does not maximize external nodes; external nodes count is fixed by n.  

**Correct:** B