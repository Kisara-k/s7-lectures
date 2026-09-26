## 8. Dictionaries and Indexed Search Trees

## Questions

#### 1. Which of the following statements about dictionaries are true?  
A) In a static dictionary, keys must be distinct.  
B) Dynamic dictionaries support insertions and deletions.  
C) Dictionaries with duplicates allow multiple entries with the same key.  
D) Hash tables are ideal for range queries and nearest match queries.  

#### 2. Regarding hash table dictionaries, which of the following are correct?  
A) Expected time complexity for get, put, and remove is O(1).  
B) Worst-case time complexity can degrade to O(n).  
C) Hash tables efficiently support indexed operations like "get element with 3rd smallest key."  
D) Balanced search trees can be used to handle hash table overflows, improving worst-case to O(log n).  

#### 3. In the Best Fit bin packing heuristic, which of the following describe the correct procedure?  
A) Pack each item into the bin with the largest available capacity that fits the item.  
B) If no bin can fit the item, start a new bin.  
C) Use a dynamic dictionary keyed by available capacity to find the best bin.  
D) The heuristic guarantees an optimal packing solution.  

#### 4. Consider an indexed binary search tree with a leftSize field at each node. Which of the following are true?  
A) leftSize represents the number of nodes in the left subtree of that node.  
B) The rank of an element corresponds to its position in the inorder traversal.  
C) To get the element at a given index, you compare the index with leftSize to decide which subtree to traverse.  
D) leftSize(x) equals the rank of x in the entire tree.  

#### 5. Which of the following statements about the complexity of dictionary operations are correct?  
A) Balanced binary search trees guarantee O(log n) worst-case time for get, put, and remove.  
B) Hash tables have O(log n) expected time for get, put, and remove.  
C) Indexed balanced search trees support get(index) and remove(index) in O(log n) time.  
D) Hash tables support ascend() operations efficiently in O(log n) time.  

#### 6. In the dynamic programming approach to constructing an optimal binary search tree, which of the following are true?  
A) The cost of a subtree includes the weighted path length of its nodes plus the sum of probabilities of keys and gaps.  
B) The root of the subtree Ti j is chosen to minimize the sum of costs of left and right subtrees plus the total weight.  
C) The total time complexity of the brute force approach is O(n^2).  
D) The dynamic programming solution can be optimized from O(n^3) to O(n^2) by restricting the range of root candidates.  

#### 7. When removing an element from a binary search tree, which of the following are valid cases and corresponding actions?  
A) If the node is a leaf, simply remove it.  
B) If the node has one child, replace the node with its child.  
C) If the node has two children, replace it with the smallest key in the right subtree or largest key in the left subtree.  
D) Removing a node with two children always requires rebalancing the entire tree.  

#### 8. Which of the following statements about meld operations on binary search trees are correct?  
A) Melding two balanced binary search trees of size n each can be done in O(log n) time.  
B) The worst-case number of comparisons to merge two sorted lists of size n each is 2n - 1.  
C) Logarithmic time melding of two binary search trees is impossible due to comparison lower bounds.  
D) Meld operations are trivial for hash tables.  

#### 9. Which of the following are true about balanced search trees?  
A) AVL trees maintain height balance to guarantee O(log n) operations.  
B) 2-3 trees and red-black trees are examples of degree balanced trees.  
C) Complete binary trees exist for all n and allow O(log n) insertions and deletions.  
D) B-trees are a type of balanced search tree optimized for disk storage.  

#### 10. Regarding the performance comparison of linear lists, arrays, and indexed AVL trees (IAVL) for get, put, and remove operations, which are correct?  
A) Arrays provide O(1) get but O(n) put and remove in the worst case.  
B) Chains (linked lists) have significantly worse performance than arrays and IAVL trees for get operations.  
C) Indexed AVL trees provide O(log n) time for get, put, and remove operations.  
D) For 40,000 operations, chains outperform arrays in average put and remove times.



<br>

## Answers

#### 1. Which of the following statements about dictionaries are true?  
A) ✓ Static dictionaries require distinct keys to avoid ambiguity.  
B) ✓ Dynamic dictionaries support insertions and deletions, unlike static ones.  
C) ✓ Dictionaries with duplicates allow multiple entries with the same key, e.g., word dictionaries.  
D) ✗ Hash tables do not support range or nearest match queries efficiently.  

**Correct:** A,B,C


#### 2. Regarding hash table dictionaries, which of the following are correct?  
A) ✓ Expected time for get, put, remove is O(1) due to hashing.  
B) ✓ Worst-case time can degrade to O(n) if many collisions occur.  
C) ✗ Hash tables do not support indexed operations like "get 3rd smallest key" efficiently.  
D) ✓ Using balanced search trees for overflow buckets improves worst-case to O(log n).  

**Correct:** A,B,D


#### 3. In the Best Fit bin packing heuristic, which of the following describe the correct procedure?  
A) ✗ Best Fit packs into the bin with the least available capacity that fits the item, not the largest.  
B) ✓ If no bin fits the item, a new bin is started.  
C) ✓ A dynamic dictionary keyed by available capacity is used to find the best bin efficiently.  
D) ✗ Best Fit is a heuristic and does not guarantee an optimal packing.  

**Correct:** B,C


#### 4. Consider an indexed binary search tree with a leftSize field at each node. Which of the following are true?  
A) ✓ leftSize counts nodes in the left subtree, used for indexing.  
B) ✓ Rank corresponds to the element’s position in inorder traversal (ascending order).  
C) ✓ To get element at index, compare index with leftSize to decide subtree traversal.  
D) ✗ leftSize(x) is rank of x only within its subtree, not the entire tree.  

**Correct:** A,B,C


#### 5. Which of the following statements about the complexity of dictionary operations are correct?  
A) ✓ Balanced BSTs guarantee O(log n) worst-case for get, put, remove.  
B) ✗ Hash tables have O(1) expected time, not O(log n).  
C) ✓ Indexed balanced BSTs support get(index) and remove(index) in O(log n).  
D) ✗ Hash tables do not efficiently support ascend() operations; these require sorting or tree traversal.  

**Correct:** A,C


#### 6. In the dynamic programming approach to constructing an optimal binary search tree, which of the following are true?  
A) ✓ Cost includes weighted path length plus sum of probabilities of keys and gaps.  
B) ✓ Root is chosen to minimize sum of left and right subtree costs plus total weight.  
C) ✗ Brute force approach is O(4^n / n^1.5), not O(n^2).  
D) ✓ Restricting root candidates reduces complexity from O(n^3) to O(n^2).  

**Correct:** A,B,D


#### 7. When removing an element from a binary search tree, which of the following are valid cases and corresponding actions?  
A) ✓ Leaf nodes can be removed directly.  
B) ✓ Nodes with one child are replaced by their child.  
C) ✓ Nodes with two children are replaced by largest key in left subtree or smallest in right subtree.  
D) ✗ Removing a two-child node does not always require rebalancing; depends on tree type.  

**Correct:** A,B,C


#### 8. Which of the following statements about meld operations on binary search trees are correct?  
A) ✗ Logarithmic time melding of two BSTs is not possible due to comparison lower bounds.  
B) ✓ Merging two sorted lists of size n requires at most 2n - 1 comparisons.  
C) ✓ Logarithmic time melding is impossible because of the comparison lower bound.  
D) ✗ Meld operations are not trivial for hash tables since they do not maintain order.  

**Correct:** B,C


#### 9. Which of the following are true about balanced search trees?  
A) ✓ AVL trees maintain height balance for O(log n) operations.  
B) ✓ 2-3 trees and red-black trees are degree balanced trees.  
C) ✗ Complete binary trees exist for all n but do not support O(log n) insert/delete.  
D) ✓ B-trees are balanced trees optimized for disk storage and large blocks.  

**Correct:** A,B,D


#### 10. Regarding the performance comparison of linear lists, arrays, and indexed AVL trees (IAVL) for get, put, and remove operations, which are correct?  
A) ✓ Arrays provide O(1) get but put and remove can be O(n) due to shifting.  
B) ✓ Chains (linked lists) have much worse get performance than arrays and IAVL trees.  
C) ✓ Indexed AVL trees provide O(log n) get, put, and remove.  
D) ✗ Chains perform worse than arrays in average put and remove times, not better.  

**Correct:** A,B,C