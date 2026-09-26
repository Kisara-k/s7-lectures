## 8. Dictionaries and Indexed Search Trees

## Questions

#### 1. Which of the following statements about dictionaries are true?  
A) Each item in a dictionary is a pair consisting of a key and an element.  
B) Keys in a dictionary must always be distinct.  
C) A dictionary can be static or dynamic depending on whether insertions and deletions are allowed.  
D) Dictionaries with duplicates allow multiple entries with the same key.

#### 2. Which operations are typically supported by a dynamic dictionary?  
A) get(key)  
B) put(key, element)  
C) remove(key)  
D) sort()

#### 3. Why are hash table dictionaries not suitable for nearest match or range queries?  
A) Hash tables do not maintain any order among keys.  
B) Hash tables have O(n) worst-case time complexity for get operations.  
C) Hash tables cannot efficiently support indexed operations like "get element with 3rd smallest key."  
D) Hash tables require keys to be integers.

#### 4. In the Best Fit bin packing heuristic, how is the bin chosen for a new item of size s?  
A) The bin with the largest available capacity that fits s.  
B) The bin with the smallest available capacity that is at least s.  
C) The first bin that can fit s.  
D) A new bin is always started for each item.

#### 5. What data structure is recommended to implement Best Fit bin packing efficiently?  
A) Hash table with keys as bin indices.  
B) Dynamic dictionary with pairs (available capacity, bin index).  
C) Balanced binary search tree with duplicates allowed.  
D) Simple array of bin capacities.

#### 6. In an indexed binary search tree, what does the field leftSize represent?  
A) The number of nodes in the right subtree.  
B) The number of nodes in the left subtree.  
C) The rank of the node in the entire tree.  
D) The height of the left subtree.

#### 7. How can the get(index) operation be performed efficiently in an indexed binary search tree?  
A) By traversing the tree in preorder and counting nodes.  
B) By comparing index with leftSize at each node and moving left or right accordingly.  
C) By performing a hash lookup on the index.  
D) By converting the tree to an array first.

#### 8. Which of the following correctly describe the performance of get, put, and remove operations in an Indexed AVL Tree (IAVL) compared to arrays and chains?  
A) IAVL has O(log n) worst-case time for all three operations.  
B) Arrays have constant time for get but linear time for put and remove.  
C) Chains have better performance than IAVL for all operations.  
D) IAVL outperforms chains significantly in put and remove operations.

#### 9. What is the main advantage of perfect hashing over general hashing?  
A) It guarantees no collisions.  
B) It requires no preprocessing time.  
C) It uses minimal space equal to the number of keys.  
D) It supports range queries efficiently.

#### 10. In the context of static dictionaries and binary search trees, what is the significance of the probabilities pi and qi?  
A) pi is the probability of searching for key si successfully.  
B) qi is the probability of an unsuccessful search between keys si and si+1.  
C) pi and qi sum to more than 1.  
D) They are used to compute the weighted path length (cost) of the tree.

#### 11. Why is the brute force algorithm for constructing an optimal binary search tree impractical for large n?  
A) It requires O(n^3) time.  
B) It generates O(4^n / n^{1.5}) trees to examine.  
C) It cannot handle duplicate keys.  
D) It only works for balanced trees.

#### 12. In the dynamic programming approach to optimal BST construction, what does the term cij represent?  
A) The cost of the least cost tree containing keys ai+1 to aj.  
B) The root of the subtree spanning keys ai+1 to aj.  
C) The weight of the subtree spanning keys ai+1 to aj.  
D) The number of nodes in the subtree spanning keys ai+1 to aj.

#### 13. How is the cost cij computed from its left and right subtrees in the dynamic programming solution?  
A) cij = cost(L) + cost(R) + weight(L) + weight(R) + pk  
B) cij = cost(L) + cost(R) + wij  
C) cij = min over k of (cik-1 + ckj) + wij  
D) cij = max over k of (cik-1 + ckj) + wij

#### 14. What is the time complexity of computing the entire cost matrix cij for the optimal BST using dynamic programming?  
A) O(n)  
B) O(n^2)  
C) O(n^3)  
D) O(2^n)

#### 15. Which of the following are true about the remove operation in a binary search tree?  
A) Removing a leaf node is the simplest case.  
B) Removing a node with two children requires replacing it with the largest key in its left subtree or smallest in its right subtree.  
C) Removing a node with one child involves replacing the node with its child.  
D) Removing a node always requires rebalancing the tree.

#### 16. What is the worst-case time complexity of the remove operation in a binary search tree?  
A) O(1)  
B) O(log n)  
C) O(height of the tree)  
D) O(n^2)

#### 17. Which of the following statements about meld (merge) operations on binary search trees are correct?  
A) Melding two BSTs of size n each requires at least 2n - 1 comparisons.  
B) Logarithmic time melding of two BSTs is possible.  
C) Melding two BSTs is equivalent to merging two sorted lists.  
D) Melding is efficient only if the trees are balanced.

#### 18. Which of the following are true about balanced search trees?  
A) AVL trees maintain height balance.  
B) 2-3 trees are degree balanced.  
C) Red-black trees are a type of weight balanced tree.  
D) B-trees are used primarily for in-memory data structures.

#### 19. Regarding the complexity of dictionary operations, which statements are true?  
A) Hash tables have expected O(1) time for get, put, and remove.  
B) Balanced binary search trees guarantee O(log n) worst-case time for get, put, and remove.  
C) Indexed balanced BSTs can perform get(index) and remove(index) in O(log n) time.  
D) Hash tables can perform ascend() operations in O(log n) time.

#### 20. Which of the following statements about internal and external nodes in a binary search tree are correct?  
A) A binary tree with n internal nodes has n + 1 external nodes.  
B) External nodes correspond to unsuccessful search terminations.  
C) Internal nodes correspond to keys stored in the dictionary.  
D) External nodes store keys that are smaller than all internal nodes.



<br>

## Answers

#### 1. Which of the following statements about dictionaries are true?  
A) ✓ Each item in a dictionary is a pair consisting of a key and an element.  
B) ✗ Keys in a dictionary must always be distinct. (Duplicates allowed in some dictionaries.)  
C) ✓ A dictionary can be static or dynamic depending on whether insertions and deletions are allowed.  
D) ✓ Dictionaries with duplicates allow multiple entries with the same key.

**Correct:** A,C,D


#### 2. Which operations are typically supported by a dynamic dictionary?  
A) ✓ get(key) is the search operation.  
B) ✓ put(key, element) is the insert operation.  
C) ✓ remove(key) is the delete operation.  
D) ✗ sort() is not a standard dictionary operation.

**Correct:** A,B,C


#### 3. Why are hash table dictionaries not suitable for nearest match or range queries?  
A) ✓ Hash tables do not maintain any order among keys, so nearest or range queries are inefficient.  
B) ✗ O(n) worst-case time is true but not the main reason for unsuitability of range queries.  
C) ✓ Indexed operations like "get element with 3rd smallest key" require order, which hash tables lack.  
D) ✗ Hash tables do not require keys to be integers.

**Correct:** A,C


#### 4. In the Best Fit bin packing heuristic, how is the bin chosen for a new item of size s?  
A) ✗ Largest available capacity is not chosen; that would be Worst Fit.  
B) ✓ Bin with smallest available capacity ≥ s is chosen to minimize wasted space.  
C) ✗ First bin that fits is First Fit, not Best Fit.  
D) ✗ New bin is only started if no existing bin fits.

**Correct:** B


#### 5. What data structure is recommended to implement Best Fit bin packing efficiently?  
A) ✗ Hash table with bin indices does not support ordered queries needed.  
B) ✓ Dynamic dictionary with pairs (available capacity, bin index) supports efficient search.  
C) ✓ Balanced binary search tree with duplicates allowed supports ordered queries and duplicates.  
D) ✗ Simple array does not efficiently support searching for smallest capacity ≥ s.

**Correct:** B,C


#### 6. In an indexed binary search tree, what does the field leftSize represent?  
A) ✗ It is not the number of nodes in the right subtree.  
B) ✓ It is the number of nodes in the left subtree, used for indexing.  
C) ✗ leftSize is local to the node, not the global rank in the entire tree.  
D) ✗ It is not the height of the left subtree.

**Correct:** B


#### 7. How can the get(index) operation be performed efficiently in an indexed binary search tree?  
A) ✗ Preorder traversal is inefficient and does not use leftSize.  
B) ✓ Compare index with leftSize at each node to decide traversal direction.  
C) ✗ Hash lookup on index is not applicable here.  
D) ✗ Converting to array first is inefficient and not required.

**Correct:** B


#### 8. Which of the following correctly describe the performance of get, put, and remove operations in an Indexed AVL Tree (IAVL) compared to arrays and chains?  
A) ✓ IAVL has O(log n) worst-case time for all three operations.  
B) ✓ Arrays have O(1) get but O(n) put and remove due to shifting.  
C) ✗ Chains have worse performance than IAVL for put and remove.  
D) ✓ IAVL significantly outperforms chains in put and remove operations.

**Correct:** A,B,D


#### 9. What is the main advantage of perfect hashing over general hashing?  
A) ✓ Perfect hashing guarantees no collisions.  
B) ✗ It requires O(n) preprocessing time, not zero.  
C) ✓ Minimal perfect hashing uses space exactly equal to number of keys.  
D) ✗ Perfect hashing does not support range queries efficiently.

**Correct:** A,C


#### 10. In the context of static dictionaries and binary search trees, what is the significance of the probabilities pi and qi?  
A) ✓ pi is the probability of searching for key si successfully.  
B) ✓ qi is the probability of an unsuccessful search between keys si and si+1.  
C) ✗ pi and qi sum to exactly 1, not more.  
D) ✓ They are used to compute the weighted path length (cost) of the tree.

**Correct:** A,B,D


#### 11. Why is the brute force algorithm for constructing an optimal binary search tree impractical for large n?  
A) ✗ Brute force is worse than O(n^3); it is exponential.  
B) ✓ It generates O(4^n / n^{1.5}) trees to examine, which is huge.  
C) ✗ It can handle duplicates if designed, but impractical anyway.  
D) ✗ It is not limited to balanced trees only.

**Correct:** B


#### 12. In the dynamic programming approach to optimal BST construction, what does the term cij represent?  
A) ✓ The cost of the least cost tree containing keys ai+1 to aj.  
B) ✗ rij is the root of the subtree, not cij.  
C) ✗ wi j is the weight, not cij.  
D) ✗ cij is cost, not number of nodes.

**Correct:** A


#### 13. How is the cost cij computed from its left and right subtrees in the dynamic programming solution?  
A) ✗ Weight terms are included in wij, not separately added.  
B) ✓ cij = cost(L) + cost(R) + wij is the correct formula.  
C) ✓ cij = min over k of (cik-1 + ckj) + wij is the recurrence to find minimal cost.  
D) ✗ cij is minimized, not maximized.

**Correct:** B,C


#### 14. What is the time complexity of computing the entire cost matrix cij for the optimal BST using dynamic programming?  
A) ✗ O(n) is too low.  
B) ✗ O(n^2) is possible with optimizations but not the basic method.  
C) ✓ O(n^3) is the standard complexity for the naive DP approach.  
D) ✗ O(2^n) is exponential, not DP.

**Correct:** C


#### 15. Which of the following are true about the remove operation in a binary search tree?  
A) ✓ Removing a leaf node is the simplest case.  
B) ✓ Removing a node with two children requires replacing it with largest key in left subtree or smallest in right subtree.  
C) ✓ Removing a node with one child involves replacing the node with its child.  
D) ✗ Removing a node does not always require rebalancing unless the tree is balanced.

**Correct:** A,B,C


#### 16. What is the worst-case time complexity of the remove operation in a binary search tree?  
A) ✗ O(1) is unrealistic for tree operations.  
B) ✗ O(log n) only if tree is balanced.  
C) ✓ O(height of the tree) is correct for general BSTs.  
D) ✗ O(n^2) is not applicable.

**Correct:** C


#### 17. Which of the following statements about meld (merge) operations on binary search trees are correct?  
A) ✓ Melding two BSTs of size n each requires at least 2n - 1 comparisons (like merging sorted lists).  
B) ✗ Logarithmic time melding is not possible for BSTs.  
C) ✓ Melding two BSTs is equivalent to merging two sorted lists.  
D) ✗ Melding is not efficient even if trees are balanced; complexity remains linear.

**Correct:** A,C


#### 18. Which of the following are true about balanced search trees?  
A) ✓ AVL trees maintain height balance.  
B) ✓ 2-3 trees are degree balanced.  
C) ✗ Red-black trees are height balanced with color properties, not weight balanced.  
D) ✗ B-trees are primarily used for external storage, not just in-memory.

**Correct:** A,B


#### 19. Regarding the complexity of dictionary operations, which statements are true?  
A) ✓ Hash tables have expected O(1) time for get, put, and remove.  
B) ✓ Balanced binary search trees guarantee O(log n) worst-case time for get, put, and remove.  
C) ✓ Indexed balanced BSTs can perform get(index) and remove(index) in O(log n) time.  
D) ✗ Hash tables cannot perform ascend() efficiently; it takes O(D + n log n).

**Correct:** A,B,C


#### 20. Which of the following statements about internal and external nodes in a binary search tree are correct?  
A) ✓ A binary tree with n internal nodes has n + 1 external nodes.  
B) ✓ External nodes correspond to unsuccessful search terminations.  
C) ✓ Internal nodes correspond to keys stored in the dictionary.  
D) ✗ External nodes do not store keys; they represent failure points, not smaller keys.

**Correct:** A,B,C