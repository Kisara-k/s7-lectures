## 8. Dictionaries and Indexed Search Trees

## Questions

#### 1. Which of the following statements about dictionaries are true?  
A) Each item in a dictionary is a pair consisting of a key and an element.  
B) Keys in a dictionary must always be distinct.  
C) Dictionaries with duplicates allow multiple entries with the same key.  
D) A dictionary can be static or dynamic depending on whether insertions and deletions are allowed.  

#### 2. Which operations are typically supported by a dynamic dictionary?  
A) get(key)  
B) put(key, element)  
C) remove(key)  
D) sort()  

#### 3. Why are hash table dictionaries not suitable for nearest match or range queries?  
A) Hash tables have O(n) worst-case time complexity for get operations.  
B) Hash tables cannot efficiently support indexed operations like "get element with 3rd smallest key."  
C) Hash tables do not maintain any order among keys.  
D) Hash tables require keys to be integers.  

#### 4. In the Best Fit bin packing heuristic, how is the bin chosen for a new item of size s?  
A) A new bin is always started for each item.  
B) The bin with the largest available capacity that fits s.  
C) The first bin that can fit s.  
D) The bin with the smallest available capacity that is at least s.  

#### 5. What data structure is recommended to implement Best Fit bin packing efficiently?  
A) Dynamic dictionary with pairs (available capacity, bin index).  
B) Balanced binary search tree with duplicates allowed.  
C) Hash table with keys as bin indices.  
D) Simple array of bin capacities.  

#### 6. In an indexed binary search tree, what does the field leftSize represent?  
A) The rank of the node in the entire tree.  
B) The number of nodes in the left subtree.  
C) The number of nodes in the right subtree.  
D) The height of the left subtree.  

#### 7. How can the get(index) operation be performed efficiently in an indexed binary search tree?  
A) By comparing index with leftSize at each node and moving left or right accordingly.  
B) By traversing the tree in preorder and counting nodes.  
C) By converting the tree to an array first.  
D) By performing a hash lookup on the index.  

#### 8. Which of the following correctly describe the performance of get, put, and remove operations in an Indexed AVL Tree (IAVL) compared to arrays and chains?  
A) IAVL has O(log n) worst-case time for all three operations.  
B) IAVL outperforms chains significantly in put and remove operations.  
C) Chains have better performance than IAVL for all operations.  
D) Arrays have constant time for get but linear time for put and remove.  

#### 9. What is the main advantage of perfect hashing over general hashing?  
A) It guarantees no collisions.  
B) It requires no preprocessing time.  
C) It uses minimal space equal to the number of keys.  
D) It supports range queries efficiently.  

#### 10. In the context of static dictionaries and binary search trees, what is the significance of the probabilities pi and qi?  
A) They are used to compute the weighted path length (cost) of the tree.  
B) pi is the probability of searching for key si successfully.  
C) pi and qi sum to more than 1.  
D) qi is the probability of an unsuccessful search between keys si and si+1.  

#### 11. Why is the brute force algorithm for constructing an optimal binary search tree impractical for large n?  
A) It only works for balanced trees.  
B) It generates O(4^n / n^{1.5}) trees to examine.  
C) It requires O(n^3) time.  
D) It cannot handle duplicate keys.  

#### 12. In the dynamic programming approach to optimal BST construction, what does the term cij represent?  
A) The root of the subtree spanning keys ai+1 to aj.  
B) The weight of the subtree spanning keys ai+1 to aj.  
C) The number of nodes in the subtree spanning keys ai+1 to aj.  
D) The cost of the least cost tree containing keys ai+1 to aj.  

#### 13. How is the cost cij computed from its left and right subtrees in the dynamic programming solution?  
A) cij = cost(L) + cost(R) + weight(L) + weight(R) + pk  
B) cij = min over k of (cik-1 + ckj) + wij  
C) cij = cost(L) + cost(R) + wij  
D) cij = max over k of (cik-1 + ckj) + wij  

#### 14. What is the time complexity of computing the entire cost matrix cij for the optimal BST using dynamic programming?  
A) O(n^2)  
B) O(2^n)  
C) O(n^3)  
D) O(n)  

#### 15. Which of the following are true about the remove operation in a binary search tree?  
A) Removing a leaf node is the simplest case.  
B) Removing a node with one child involves replacing the node with its child.  
C) Removing a node always requires rebalancing the tree.  
D) Removing a node with two children requires replacing it with the largest key in its left subtree or smallest in its right subtree.  

#### 16. What is the worst-case time complexity of the remove operation in a binary search tree?  
A) O(n^2)  
B) O(log n)  
C) O(1)  
D) O(height of the tree)  

#### 17. Which of the following statements about meld (merge) operations on binary search trees are correct?  
A) Melding is efficient only if the trees are balanced.  
B) Melding two BSTs of size n each requires at least 2n - 1 comparisons.  
C) Logarithmic time melding of two BSTs is possible.  
D) Melding two BSTs is equivalent to merging two sorted lists.  

#### 18. Which of the following are true about balanced search trees?  
A) Red-black trees are a type of weight balanced tree.  
B) B-trees are used primarily for in-memory data structures.  
C) 2-3 trees are degree balanced.  
D) AVL trees maintain height balance.  

#### 19. Regarding the complexity of dictionary operations, which statements are true?  
A) Indexed balanced BSTs can perform get(index) and remove(index) in O(log n) time.  
B) Hash tables can perform ascend() operations in O(log n) time.  
C) Balanced binary search trees guarantee O(log n) worst-case time for get, put, and remove.  
D) Hash tables have expected O(1) time for get, put, and remove.  

#### 20. Which of the following statements about internal and external nodes in a binary search tree are correct?  
A) Internal nodes correspond to keys stored in the dictionary.  
B) External nodes store keys that are smaller than all internal nodes.  
C) A binary tree with n internal nodes has n + 1 external nodes.  
D) External nodes correspond to unsuccessful search terminations.  



<br>

## Answers

#### 1. Which of the following statements about dictionaries are true?  
A) ✓ Each item in a dictionary is a pair consisting of a key and an element.  
B) ✗ Keys in a dictionary must always be distinct. (Duplicates allowed in some dictionaries.)  
C) ✓ Dictionaries with duplicates allow multiple entries with the same key.  
D) ✓ A dictionary can be static or dynamic depending on whether insertions and deletions are allowed.  

**Correct:** A, C, D


#### 2. Which operations are typically supported by a dynamic dictionary?  
A) ✓ get(key) is the search operation.  
B) ✓ put(key, element) is the insert operation.  
C) ✓ remove(key) is the delete operation.  
D) ✗ sort() is not a standard dictionary operation.  

**Correct:** A, B, C


#### 3. Why are hash table dictionaries not suitable for nearest match or range queries?  
A) ✗ O(n) worst-case time is true but not the main reason for unsuitability of range queries.  
B) ✓ Indexed operations like "get element with 3rd smallest key" require order, which hash tables lack.  
C) ✓ Hash tables do not maintain any order among keys, so nearest or range queries are inefficient.  
D) ✗ Hash tables do not require keys to be integers.  

**Correct:** B, C


#### 4. In the Best Fit bin packing heuristic, how is the bin chosen for a new item of size s?  
A) ✗ New bin is only started if no existing bin fits.  
B) ✗ Largest available capacity is not chosen; that would be Worst Fit.  
C) ✗ First bin that fits is First Fit, not Best Fit.  
D) ✓ Bin with smallest available capacity ≥ s is chosen to minimize wasted space.  

**Correct:** D


#### 5. What data structure is recommended to implement Best Fit bin packing efficiently?  
A) ✓ Dynamic dictionary with pairs (available capacity, bin index) supports efficient search.  
B) ✓ Balanced binary search tree with duplicates allowed supports ordered queries and duplicates.  
C) ✗ Hash table with bin indices does not support ordered queries needed.  
D) ✗ Simple array does not efficiently support searching for smallest capacity ≥ s.  

**Correct:** A, B


#### 6. In an indexed binary search tree, what does the field leftSize represent?  
A) ✗ leftSize is local to the node, not the global rank in the entire tree.  
B) ✓ It is the number of nodes in the left subtree, used for indexing.  
C) ✗ It is not the number of nodes in the right subtree.  
D) ✗ It is not the height of the left subtree.  

**Correct:** B


#### 7. How can the get(index) operation be performed efficiently in an indexed binary search tree?  
A) ✓ Compare index with leftSize at each node to decide traversal direction.  
B) ✗ Preorder traversal is inefficient and does not use leftSize.  
C) ✗ Converting to array first is inefficient and not required.  
D) ✗ Hash lookup on index is not applicable here.  

**Correct:** A


#### 8. Which of the following correctly describe the performance of get, put, and remove operations in an Indexed AVL Tree (IAVL) compared to arrays and chains?  
A) ✓ IAVL has O(log n) worst-case time for all three operations.  
B) ✓ IAVL significantly outperforms chains in put and remove operations.  
C) ✗ Chains have worse performance than IAVL for put and remove.  
D) ✓ Arrays have O(1) get but O(n) put and remove due to shifting.  

**Correct:** A, B, D


#### 9. What is the main advantage of perfect hashing over general hashing?  
A) ✓ Perfect hashing guarantees no collisions.  
B) ✗ It requires O(n) preprocessing time, not zero.  
C) ✓ Minimal perfect hashing uses space exactly equal to number of keys.  
D) ✗ Perfect hashing does not support range queries efficiently.  

**Correct:** A, C


#### 10. In the context of static dictionaries and binary search trees, what is the significance of the probabilities pi and qi?  
A) ✓ They are used to compute the weighted path length (cost) of the tree.  
B) ✓ pi is the probability of searching for key si successfully.  
C) ✗ pi and qi sum to exactly 1, not more.  
D) ✓ qi is the probability of an unsuccessful search between keys si and si+1.  

**Correct:** A, B, D


#### 11. Why is the brute force algorithm for constructing an optimal binary search tree impractical for large n?  
A) ✗ It is not limited to balanced trees only.  
B) ✓ It generates O(4^n / n^{1.5}) trees to examine, which is huge.  
C) ✗ Brute force is worse than O(n^3); it is exponential.  
D) ✗ It can handle duplicates if designed, but impractical anyway.  

**Correct:** B


#### 12. In the dynamic programming approach to optimal BST construction, what does the term cij represent?  
A) ✗ rij is the root of the subtree, not cij.  
B) ✗ wi j is the weight, not cij.  
C) ✗ cij is cost, not number of nodes.  
D) ✓ The cost of the least cost tree containing keys ai+1 to aj.  

**Correct:** D


#### 13. How is the cost cij computed from its left and right subtrees in the dynamic programming solution?  
A) ✗ Weight terms are included in wij, not separately added.  
B) ✓ cij = min over k of (cik-1 + ckj) + wij is the recurrence to find minimal cost.  
C) ✓ cij = cost(L) + cost(R) + wij is the correct formula.  
D) ✗ cij is minimized, not maximized.  

**Correct:** B, C


#### 14. What is the time complexity of computing the entire cost matrix cij for the optimal BST using dynamic programming?  
A) ✗ O(n^2) is possible with optimizations but not the basic method.  
B) ✗ O(2^n) is exponential, not DP.  
C) ✓ O(n^3) is the standard complexity for the naive DP approach.  
D) ✗ O(n) is too low.  

**Correct:** C


#### 15. Which of the following are true about the remove operation in a binary search tree?  
A) ✓ Removing a leaf node is the simplest case.  
B) ✓ Removing a node with one child involves replacing the node with its child.  
C) ✗ Removing a node does not always require rebalancing unless the tree is balanced.  
D) ✓ Removing a node with two children requires replacing it with largest key in left subtree or smallest in right subtree.  

**Correct:** A, B, D


#### 16. What is the worst-case time complexity of the remove operation in a binary search tree?  
A) ✗ O(n^2) is not applicable.  
B) ✗ O(log n) only if tree is balanced.  
C) ✗ O(1) is unrealistic for tree operations.  
D) ✓ O(height of the tree) is correct for general BSTs.  

**Correct:** D


#### 17. Which of the following statements about meld (merge) operations on binary search trees are correct?  
A) ✗ Melding is not efficient even if trees are balanced; complexity remains linear.  
B) ✓ Melding two BSTs of size n each requires at least 2n - 1 comparisons (like merging sorted lists).  
C) ✗ Logarithmic time melding is not possible for BSTs.  
D) ✓ Melding two BSTs is equivalent to merging two sorted lists.  

**Correct:** B, D


#### 18. Which of the following are true about balanced search trees?  
A) ✗ Red-black trees are height balanced with color properties, not weight balanced.  
B) ✗ B-trees are primarily used for external storage, not just in-memory.  
C) ✓ 2-3 trees are degree balanced.  
D) ✓ AVL trees maintain height balance.  

**Correct:** C, D


#### 19. Regarding the complexity of dictionary operations, which statements are true?  
A) ✓ Indexed balanced BSTs can perform get(index) and remove(index) in O(log n) time.  
B) ✗ Hash tables cannot perform ascend() efficiently; it takes O(D + n log n).  
C) ✓ Balanced binary search trees guarantee O(log n) worst-case time for get, put, and remove.  
D) ✓ Hash tables have expected O(1) time for get, put, and remove.  

**Correct:** A, C, D


#### 20. Which of the following statements about internal and external nodes in a binary search tree are correct?  
A) ✓ Internal nodes correspond to keys stored in the dictionary.  
B) ✗ External nodes do not store keys; they represent failure points, not smaller keys.  
C) ✓ A binary tree with n internal nodes has n + 1 external nodes.  
D) ✓ External nodes correspond to unsuccessful search terminations.  

**Correct:** A, C, D