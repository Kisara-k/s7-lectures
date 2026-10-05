## 6. Binomial Heaps

## Questions

#### 1. What is the time complexity of the insert operation in a binomial heap?  
A) O(log n) worst case  
B) O(n) worst case  
C) O(log n) amortized  
D) O(1) amortized  

#### 2. Which of the following correctly describe the structure of a node in a binomial heap?  
A) Sibling pointer is used for a circular linked list of siblings  
B) Child pointer points to the parent node  
C) Data field stores the key value  
D) Degree represents the number of children  

#### 3. How is a binomial heap represented at the top level?  
A) A doubly linked list of max trees  
B) A heap-ordered array  
C) A circular linked list of min trees  
D) A binary search tree  

#### 4. When inserting a new element into a binomial heap, what happens?  
A) All trees are pairwise combined immediately  
B) The min-element pointer is updated if necessary  
C) The heap is rebuilt from scratch  
D) A new single-node min tree is added to the collection  

#### 5. What is the main operation performed during the meld of two binomial heaps?  
A) Merge two sorted arrays  
B) Update the min-element pointer  
C) Rebuild the heap from all nodes  
D) Combine the two top-level circular lists  

#### 6. What is the first step in the remove-min operation on a nonempty binomial heap?  
A) Update the min-element pointer  
B) Remove the min tree from the top-level list  
C) Reinsert the subtrees of the removed min tree  
D) Pairwise combine all trees in the heap  

#### 7. How is a min tree removed from the circular linked list of min trees?  
A) By copying the next node’s data into the current node and removing the next node  
B) By breaking the circular list into two halves  
C) By merging it with its sibling trees  
D) By deleting the node and all its children recursively  

#### 8. After removing the min tree, what is done with its subtrees?  
A) They are discarded  
B) They are reinserted by combining with the existing top-level list  
C) They are converted into a binary search tree  
D) They are merged pairwise by degree immediately  

#### 9. What is the complexity of the remove-min operation without enhancement?  
A) O(log n)  
B) O(1) amortized  
C) O(s), where s is the number of min trees in the top-level list  
D) O(n)  

#### 10. What is the purpose of the enhanced remove-min operation?  
A) To reduce the number of min trees by pairwise combining trees of equal degree  
B) To convert the heap into a balanced binary tree  
C) To improve the complexity from O(n) to O(log n) amortized  
D) To avoid updating the min-element pointer  

#### 11. During pairwise combine, what determines which tree becomes the subtree of the other?  
A) The tree with the larger degree becomes the subtree  
B) The tree with the larger root becomes the subtree  
C) The tree with the smaller root becomes the subtree  
D) The tree with the smaller degree becomes the subtree  

#### 12. What data structure is used to keep track of trees by degree during pairwise combine?  
A) A table indexed by degree  
B) A stack  
C) A queue  
D) A priority queue  

#### 13. What is the maximum degree of any binomial tree in a binomial heap with n nodes?  
A) O(log n)  
B) O(1)  
C) O(√n)  
D) O(n)  

#### 14. Which of the following statements about binomial trees Bk is true?  
A) Bk has 2^k nodes  
B) Bk has k children  
C) Bk is formed by linking two Bk-1 trees  
D) Bk is a complete binary tree of height k  

#### 15. What is the overall complexity of the enhanced remove-min operation?  
A) O(MaxDegree * s)  
B) O(n log n)  
C) O(log n) amortized  
D) O(MaxDegree + s), where s is the number of min trees after reinsertion  

#### 16. Why is the min-element pointer updated after meld or remove-min operations?  
A) To optimize future insert operations  
B) To maintain the heap property in each binomial tree  
C) To keep track of the largest element in the heap  
D) Because the minimum element may have changed  

#### 17. Which of the following is NOT true about the sibling pointer in a binomial heap node?  
A) It can be null if the node has no siblings  
B) It points to the node’s parent  
C) It is used to form a circular linked list of siblings  
D) It helps in traversing the children of a node  

#### 18. What happens if the binomial heap is empty and a remove-min operation is attempted?  
A) The operation fails  
B) The min-element pointer is set to null  
C) The heap inserts a dummy node  
D) The heap is rebuilt  

#### 19. How does the pairwise combine process affect the number of trees in the top-level list?  
A) It removes all trees except one  
B) It keeps the number of trees the same  
C) It decreases the number of trees by merging trees of equal degree  
D) It increases the number of trees  

#### 20. Which of the following best describes the relationship between the number of nodes n and the maximum degree MaxDegree in a binomial heap?  
A) MaxDegree grows faster than n  
B) MaxDegree is proportional to n  
C) MaxDegree is constant regardless of n  
D) MaxDegree is proportional to log n  



<br>

## Answers

#### 1. What is the time complexity of the insert operation in a binomial heap?  
A) ✓ Insert worst case is O(log n) due to merging trees of equal degree.  
B) ✗ Insert is not O(n) worst case; that would be inefficient.  
C) ✓ Insert amortized complexity is O(log n) because merges happen rarely.  
D) ✗ Insert is not O(1) amortized; it requires merging trees, which can take O(log n).  

**Correct:** A, C


#### 2. Which of the following correctly describe the structure of a node in a binomial heap?  
A) ✓ Sibling pointer is used for circular linked list of siblings.  
B) ✗ Child pointer points to one of the node’s children, not the parent.  
C) ✓ Data field stores the key or value of the node.  
D) ✓ Degree is the number of children of the node.  

**Correct:** A, C, D


#### 3. How is a binomial heap represented at the top level?  
A) ✗ It is not a doubly linked list of max trees.  
B) ✗ It is not represented as a heap-ordered array.  
C) ✓ It is a circular linked list of min trees.  
D) ✗ It is not a binary search tree.  

**Correct:** C


#### 4. When inserting a new element into a binomial heap, what happens?  
A) ✗ Trees are not pairwise combined immediately on insert; that happens during remove-min or meld.  
B) ✓ The min-element pointer is updated if the new element is smaller.  
C) ✗ The heap is not rebuilt from scratch.  
D) ✓ A new single-node min tree is added.  

**Correct:** B, D


#### 5. What is the main operation performed during the meld of two binomial heaps?  
A) ✗ Meld does not merge sorted arrays.  
B) ✓ Meld updates the min-element pointer after combining.  
C) ✗ Meld does not rebuild the heap from all nodes.  
D) ✓ Meld combines the two top-level circular lists of min trees.  

**Correct:** B, D


#### 6. What is the first step in the remove-min operation on a nonempty binomial heap?  
A) ✗ Updating min-element pointer happens after reinsertion.  
B) ✓ Remove the min tree from the top-level list.  
C) ✗ Reinsertion of subtrees happens after removal.  
D) ✗ Pairwise combine happens later, not first.  

**Correct:** B


#### 7. How is a min tree removed from the circular linked list of min trees?  
A) ✓ The next node’s data is copied into the current node, and the next node is removed (if not empty).  
B) ✗ The circular list is not broken into halves.  
C) ✗ It is not merged with siblings at removal.  
D) ✗ The entire subtree is not deleted recursively at this step.  

**Correct:** A


#### 8. After removing the min tree, what is done with its subtrees?  
A) ✗ Subtrees are not discarded; they must be reinserted.  
B) ✓ Subtrees are reinserted by combining with the existing top-level list.  
C) ✗ Subtrees are not converted into binary search trees.  
D) ✗ Pairwise combine happens during enhanced remove-min, not immediately here.  

**Correct:** B


#### 9. What is the complexity of the remove-min operation without enhancement?  
A) ✗ It is not O(log n) without enhancement.  
B) ✗ It is not O(1) amortized.  
C) ✓ O(s), where s is the number of min trees, can be O(n) in worst case.  
D) ✓ It is O(n) because it may need to scan all trees.  

**Correct:** C, D


#### 10. What is the purpose of the enhanced remove-min operation?  
A) ✓ To reduce the number of min trees by pairwise combining trees of equal degree.  
B) ✗ It does not convert the heap into a balanced binary tree.  
C) ✓ It improves complexity from O(n) to O(log n) amortized by limiting max degree.  
D) ✗ It does update the min-element pointer.  

**Correct:** A, C


#### 11. During pairwise combine, what determines which tree becomes the subtree of the other?  
A) ✗ Degree is equal, so it does not determine which becomes subtree.  
B) ✓ The tree with the larger root becomes the subtree of the smaller root tree.  
C) ✗ The tree with the smaller root does not become the subtree.  
D) ✗ Degree is always equal when combining; degree does not determine subtree.  

**Correct:** B


#### 12. What data structure is used to keep track of trees by degree during pairwise combine?  
A) ✓ A table indexed by degree is used to track trees.  
B) ✗ A stack is not used.  
C) ✗ A queue is not used.  
D) ✗ A priority queue is not used here.  

**Correct:** A


#### 13. What is the maximum degree of any binomial tree in a binomial heap with n nodes?  
A) ✓ Max degree is O(log n) because binomial trees grow exponentially in size.  
B) ✗ It is not constant.  
C) ✗ It is not O(√n).  
D) ✗ Max degree is not proportional to n.  

**Correct:** A


#### 14. Which of the following statements about binomial trees Bk is true?  
A) ✓ Bk has 2^k nodes.  
B) ✓ Bk has degree k, so it has k children.  
C) ✓ Bk is formed by linking two Bk-1 trees.  
D) ✗ Bk is not necessarily a complete binary tree; it has a specific recursive structure.  

**Correct:** A, B, C


#### 15. What is the overall complexity of the enhanced remove-min operation?  
A) ✗ It is not O(MaxDegree * s).  
B) ✗ It is not O(n log n).  
C) ✗ It is not O(log n) amortized for remove-min (insert is amortized O(log n)).  
D) ✓ O(MaxDegree + s), where s is the number of min trees after reinsertion.  

**Correct:** D


#### 16. Why is the min-element pointer updated after meld or remove-min operations?  
A) ✗ It does not optimize insert operations directly.  
B) ✗ Updating min-element pointer does not maintain heap property inside trees.  
C) ✗ It does not track the largest element.  
D) ✓ Because the minimum element may have changed after these operations.  

**Correct:** D


#### 17. Which of the following is NOT true about the sibling pointer in a binomial heap node?  
A) ✗ It can be null if the node has no siblings.  
B) ✓ It does NOT point to the node’s parent; it points to siblings.  
C) ✗ It is true that sibling pointer forms circular linked list of siblings.  
D) ✗ It helps traverse children by linking siblings.  

**Correct:** B


#### 18. What happens if the binomial heap is empty and a remove-min operation is attempted?  
A) ✓ The operation fails because there is no min element.  
B) ✗ Min-element pointer is already null; no update needed.  
C) ✗ No dummy node is inserted.  
D) ✗ The heap is not rebuilt.  

**Correct:** A


#### 19. How does the pairwise combine process affect the number of trees in the top-level list?  
A) ✗ It does not remove all trees except one.  
B) ✗ It does not keep the number the same; it reduces it.  
C) ✓ It decreases the number of trees by merging trees of equal degree.  
D) ✗ It does not increase the number of trees.  

**Correct:** C


#### 20. Which of the following best describes the relationship between the number of nodes n and the maximum degree MaxDegree in a binomial heap?  
A) ✗ MaxDegree does not grow faster than n.  
B) ✗ MaxDegree is not proportional to n.  
C) ✗ MaxDegree is not constant.  
D) ✓ MaxDegree is proportional to log n due to exponential growth of binomial trees.  

**Correct:** D
