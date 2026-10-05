## 8. Dictionaries and Indexed Search Trees

## Questions

#### 1. Which of the following statements about dictionaries are true?  
A) Dynamic dictionaries support insertions and deletions.  
B) Hash tables are ideal for range queries and nearest match queries.  
C) Dictionaries with duplicates allow multiple entries with the same key.  
D) In a static dictionary, keys must be distinct.  

#### 2. Regarding hash table dictionaries, which of the following are correct?  
A) Worst-case time complexity can degrade to O(n).  
B) Balanced search trees can be used to handle hash table overflows, improving worst-case to O(log n).  
C) Hash tables efficiently support indexed operations like "get element with 3rd smallest key."  
D) Expected time complexity for get, put, and remove is O(1).  

#### 3. In the Best Fit bin packing heuristic, which of the following describe the correct procedure?  
A) If no bin can fit the item, start a new bin.  
B) Pack each item into the bin with the largest available capacity that fits the item.  
C) The heuristic guarantees an optimal packing solution.  
D) Use a dynamic dictionary keyed by available capacity to find the best bin.  

#### 4. Consider an indexed binary search tree with a leftSize field at each node. Which of the following are true?  
A) The rank of an element corresponds to its position in the inorder traversal.  
B) To get the element at a given index, you compare the index with leftSize to decide which subtree to traverse.  
C) leftSize represents the number of nodes in the left subtree of that node.  
D) leftSize(x) equals the rank of x in the entire tree.  

#### 5. Which of the following statements about the complexity of dictionary operations are correct?  
A) Indexed balanced search trees support get(index) and remove(index) in O(log n) time.  
B) Balanced binary search trees guarantee O(log n) worst-case time for get, put, and remove.  
C) Hash tables have O(log n) expected time for get, put, and remove.  
D) Hash tables support ascend() operations efficiently in O(log n) time.  

#### 6. In the dynamic programming approach to constructing an optimal binary search tree, which of the following are true?  
A) The cost of a subtree includes the weighted path length of its nodes plus the sum of probabilities of keys and gaps.  
B) The total time complexity of the brute force approach is O(n^2).  
C) The root of the subtree Ti j is chosen to minimize the sum of costs of left and right subtrees plus the total weight.  
D) The dynamic programming solution can be optimized from O(n^3) to O(n^2) by restricting the range of root candidates.  

#### 7. When removing an element from a binary search tree, which of the following are valid cases and corresponding actions?  
A) If the node is a leaf, simply remove it.  
B) If the node has two children, replace it with the smallest key in the right subtree or largest key in the left subtree.  
C) If the node has one child, replace the node with its child.  
D) Removing a node with two children always requires rebalancing the entire tree.  

#### 8. Which of the following statements about meld operations on binary search trees are correct?  
A) Melding two balanced binary search trees of size n each can be done in O(log n) time.  
B) Meld operations are trivial for hash tables.  
C) Logarithmic time melding of two binary search trees is impossible due to comparison lower bounds.  
D) The worst-case number of comparisons to merge two sorted lists of size n each is 2n - 1.  

#### 9. Which of the following are true about balanced search trees?  
A) B-trees are a type of balanced search tree optimized for disk storage.  
B) AVL trees maintain height balance to guarantee O(log n) operations.  
C) 2-3 trees and red-black trees are examples of degree balanced trees.  
D) Complete binary trees exist for all n and allow O(log n) insertions and deletions.  

#### 10. Regarding the performance comparison of linear lists, arrays, and indexed AVL trees (IAVL) for get, put, and remove operations, which are correct?  
A) Chains (linked lists) have significantly worse performance than arrays and IAVL trees for get operations.  
B) For 40,000 operations, chains outperform arrays in average put and remove times.  
C) Indexed AVL trees provide O(log n) time for get, put, and remove operations.  
D) Arrays provide O(1) get but O(n) put and remove in the worst case.  



<br>

## Answers

#### 1. Which of the following statements about dictionaries are true?  
A) ✓ Dynamic dictionaries support insertions and deletions, unlike static ones.  
B) ✗ Hash tables do not support range or nearest match queries efficiently.  
C) ✓ Dictionaries with duplicates allow multiple entries with the same key, e.g., word dictionaries.  
D) ✓ Static dictionaries require distinct keys to avoid ambiguity.  

**Correct:** A, C, D


#### 2. Regarding hash table dictionaries, which of the following are correct?  
A) ✓ Worst-case time can degrade to O(n) if many collisions occur.  
B) ✓ Using balanced search trees for overflow buckets improves worst-case to O(log n).  
C) ✗ Hash tables do not support indexed operations like "get 3rd smallest key" efficiently.  
D) ✓ Expected time for get, put, remove is O(1) due to hashing.  

**Correct:** A, B, D


#### 3. In the Best Fit bin packing heuristic, which of the following describe the correct procedure?  
A) ✓ If no bin fits the item, a new bin is started.  
B) ✗ Best Fit packs into the bin with the least available capacity that fits the item, not the largest.  
C) ✗ Best Fit is a heuristic and does not guarantee an optimal packing.  
D) ✓ A dynamic dictionary keyed by available capacity is used to find the best bin efficiently.  

**Correct:** A, D


#### 4. Consider an indexed binary search tree with a leftSize field at each node. Which of the following are true?  
A) ✓ Rank corresponds to the element’s position in inorder traversal (ascending order).  
B) ✓ To get element at index, compare index with leftSize to decide subtree traversal.  
C) ✓ leftSize counts nodes in the left subtree, used for indexing.  
D) ✗ leftSize(x) is rank of x only within its subtree, not the entire tree.  

**Correct:** A, B, C


#### 5. Which of the following statements about the complexity of dictionary operations are correct?  
A) ✓ Indexed balanced BSTs support get(index) and remove(index) in O(log n).  
B) ✓ Balanced BSTs guarantee O(log n) worst-case for get, put, remove.  
C) ✗ Hash tables have O(1) expected time, not O(log n).  
D) ✗ Hash tables do not efficiently support ascend() operations; these require sorting or tree traversal.  

**Correct:** A, B


#### 6. In the dynamic programming approach to constructing an optimal binary search tree, which of the following are true?  
A) ✓ Cost includes weighted path length plus sum of probabilities of keys and gaps.  
B) ✗ Brute force approach is O(4^n / n^1.5), not O(n^2).  
C) ✓ Root is chosen to minimize sum of left and right subtree costs plus total weight.  
D) ✓ Restricting root candidates reduces complexity from O(n^3) to O(n^2).  

**Correct:** A, C, D


#### 7. When removing an element from a binary search tree, which of the following are valid cases and corresponding actions?  
A) ✓ Leaf nodes can be removed directly.  
B) ✓ Nodes with two children are replaced by largest key in left subtree or smallest in right subtree.  
C) ✓ Nodes with one child are replaced by their child.  
D) ✗ Removing a two-child node does not always require rebalancing; depends on tree type.  

**Correct:** A, B, C


#### 8. Which of the following statements about meld operations on binary search trees are correct?  
A) ✗ Logarithmic time melding of two BSTs is not possible due to comparison lower bounds.  
B) ✗ Meld operations are not trivial for hash tables since they do not maintain order.  
C) ✓ Logarithmic time melding is impossible because of the comparison lower bound.  
D) ✓ Merging two sorted lists of size n requires at most 2n - 1 comparisons.  

**Correct:** C, D


#### 9. Which of the following are true about balanced search trees?  
A) ✓ B-trees are balanced trees optimized for disk storage and large blocks.  
B) ✓ AVL trees maintain height balance for O(log n) operations.  
C) ✓ 2-3 trees and red-black trees are degree balanced trees.  
D) ✗ Complete binary trees exist for all n but do not support O(log n) insert/delete.  

**Correct:** A, B, C


#### 10. Regarding the performance comparison of linear lists, arrays, and indexed AVL trees (IAVL) for get, put, and remove operations, which are correct?  
A) ✓ Chains (linked lists) have much worse get performance than arrays and IAVL trees.  
B) ✗ Chains perform worse than arrays in average put and remove times, not better.  
C) ✓ Indexed AVL trees provide O(log n) get, put, and remove.  
D) ✓ Arrays provide O(1) get but put and remove can be O(n) due to shifting.  

**Correct:** A, C, D