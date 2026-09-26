## 6. Binomial Heaps

## Questions

#### 1. What is the time complexity of the insert operation in a binomial heap?  
A) O(1) amortized  
B) O(log n) worst case  
C) O(n) worst case  
D) O(log n) amortized  

#### 2. Which of the following correctly describe the structure of a node in a binomial heap?  
A) Degree represents the number of children  
B) Child pointer points to the parent node  
C) Sibling pointer is used for a circular linked list of siblings  
D) Data field stores the key value  

#### 3. How is a binomial heap represented at the top level?  
A) A binary search tree  
B) A circular linked list of min trees  
C) A doubly linked list of max trees  
D) A heap-ordered array  

#### 4. When inserting a new element into a binomial heap, what happens?  
A) A new single-node min tree is added to the collection  
B) The min-element pointer is updated if necessary  
C) All trees are pairwise combined immediately  
D) The heap is rebuilt from scratch  

#### 5. What is the main operation performed during the meld of two binomial heaps?  
A) Merge two sorted arrays  
B) Combine the two top-level circular lists  
C) Rebuild the heap from all nodes  
D) Update the min-element pointer  

#### 6. What is the first step in the remove-min operation on a nonempty binomial heap?  
A) Remove the min tree from the top-level list  
B) Pairwise combine all trees in the heap  
C) Reinsert the subtrees of the removed min tree  
D) Update the min-element pointer  

#### 7. How is a min tree removed from the circular linked list of min trees?  
A) By deleting the node and all its children recursively  
B) By copying the next node’s data into the current node and removing the next node  
C) By breaking the circular list into two halves  
D) By merging it with its sibling trees  

#### 8. After removing the min tree, what is done with its subtrees?  
A) They are discarded  
B) They are reinserted by combining with the existing top-level list  
C) They are converted into a binary search tree  
D) They are merged pairwise by degree immediately  

#### 9. What is the complexity of the remove-min operation without enhancement?  
A) O(log n)  
B) O(n)  
C) O(s), where s is the number of min trees in the top-level list  
D) O(1) amortized  

#### 10. What is the purpose of the enhanced remove-min operation?  
A) To reduce the number of min trees by pairwise combining trees of equal degree  
B) To avoid updating the min-element pointer  
C) To convert the heap into a balanced binary tree  
D) To improve the complexity from O(n) to O(log n) amortized  

#### 11. During pairwise combine, what determines which tree becomes the subtree of the other?  
A) The tree with the smaller root becomes the subtree  
B) The tree with the larger root becomes the subtree  
C) The tree with the smaller degree becomes the subtree  
D) The tree with the larger degree becomes the subtree  

#### 12. What data structure is used to keep track of trees by degree during pairwise combine?  
A) A stack  
B) A queue  
C) A table indexed by degree  
D) A priority queue  

#### 13. What is the maximum degree of any binomial tree in a binomial heap with n nodes?  
A) O(n)  
B) O(log n)  
C) O(√n)  
D) O(1)  

#### 14. Which of the following statements about binomial trees Bk is true?  
A) Bk is formed by linking two Bk-1 trees  
B) Bk has 2^k nodes  
C) Bk is a complete binary tree of height k  
D) Bk has k children  

#### 15. What is the overall complexity of the enhanced remove-min operation?  
A) O(MaxDegree + s), where s is the number of min trees after reinsertion  
B) O(n log n)  
C) O(log n) amortized  
D) O(MaxDegree * s)  

#### 16. Why is the min-element pointer updated after meld or remove-min operations?  
A) Because the minimum element may have changed  
B) To maintain the heap property in each binomial tree  
C) To keep track of the largest element in the heap  
D) To optimize future insert operations  

#### 17. Which of the following is NOT true about the sibling pointer in a binomial heap node?  
A) It is used to form a circular linked list of siblings  
B) It can be null if the node has no siblings  
C) It points to the node’s parent  
D) It helps in traversing the children of a node  

#### 18. What happens if the binomial heap is empty and a remove-min operation is attempted?  
A) The operation fails  
B) The heap is rebuilt  
C) The min-element pointer is set to null  
D) The heap inserts a dummy node  

#### 19. How does the pairwise combine process affect the number of trees in the top-level list?  
A) It increases the number of trees  
B) It decreases the number of trees by merging trees of equal degree  
C) It keeps the number of trees the same  
D) It removes all trees except one  

#### 20. Which of the following best describes the relationship between the number of nodes n and the maximum degree MaxDegree in a binomial heap?  
A) MaxDegree is proportional to n  
B) MaxDegree is proportional to log n  
C) MaxDegree is constant regardless of n  
D) MaxDegree grows faster than n



<br>

## Answers

#### 1. What is the time complexity of the insert operation in a binomial heap?  
A) ✗ Insert is not O(1) amortized; it requires merging trees, which can take O(log n).  
B) ✓ Insert worst case is O(log n) due to merging trees of equal degree.  
C) ✗ Insert is not O(n) worst case; that would be inefficient.  
D) ✓ Insert amortized complexity is O(log n) because merges happen rarely.  

**Correct:** B,D


#### 2. Which of the following correctly describe the structure of a node in a binomial heap?  
A) ✓ Degree is the number of children of the node.  
B) ✗ Child pointer points to one of the node’s children, not the parent.  
C) ✓ Sibling pointer is used for circular linked list of siblings.  
D) ✓ Data field stores the key or value of the node.  

**Correct:** A,C,D


#### 3. How is a binomial heap represented at the top level?  
A) ✗ It is not a binary search tree.  
B) ✓ It is a circular linked list of min trees.  
C) ✗ It is not a doubly linked list of max trees.  
D) ✗ It is not represented as a heap-ordered array.  

**Correct:** B


#### 4. When inserting a new element into a binomial heap, what happens?  
A) ✓ A new single-node min tree is added.  
B) ✓ The min-element pointer is updated if the new element is smaller.  
C) ✗ Trees are not pairwise combined immediately on insert; that happens during remove-min or meld.  
D) ✗ The heap is not rebuilt from scratch.  

**Correct:** A,B


#### 5. What is the main operation performed during the meld of two binomial heaps?  
A) ✗ Meld does not merge sorted arrays.  
B) ✓ Meld combines the two top-level circular lists of min trees.  
C) ✗ Meld does not rebuild the heap from all nodes.  
D) ✓ Meld updates the min-element pointer after combining.  

**Correct:** B,D


#### 6. What is the first step in the remove-min operation on a nonempty binomial heap?  
A) ✓ Remove the min tree from the top-level list.  
B) ✗ Pairwise combine happens later, not first.  
C) ✗ Reinsertion of subtrees happens after removal.  
D) ✗ Updating min-element pointer happens after reinsertion.  

**Correct:** A


#### 7. How is a min tree removed from the circular linked list of min trees?  
A) ✗ The entire subtree is not deleted recursively at this step.  
B) ✓ The next node’s data is copied into the current node, and the next node is removed (if not empty).  
C) ✗ The circular list is not broken into halves.  
D) ✗ It is not merged with siblings at removal.  

**Correct:** B


#### 8. After removing the min tree, what is done with its subtrees?  
A) ✗ Subtrees are not discarded; they must be reinserted.  
B) ✓ Subtrees are reinserted by combining with the existing top-level list.  
C) ✗ Subtrees are not converted into binary search trees.  
D) ✗ Pairwise combine happens during enhanced remove-min, not immediately here.  

**Correct:** B


#### 9. What is the complexity of the remove-min operation without enhancement?  
A) ✗ It is not O(log n) without enhancement.  
B) ✓ It is O(n) because it may need to scan all trees.  
C) ✓ O(s), where s is the number of min trees, can be O(n) in worst case.  
D) ✗ It is not O(1) amortized.  

**Correct:** B,C


#### 10. What is the purpose of the enhanced remove-min operation?  
A) ✓ To reduce the number of min trees by pairwise combining trees of equal degree.  
B) ✗ It does update the min-element pointer.  
C) ✗ It does not convert the heap into a balanced binary tree.  
D) ✓ It improves complexity from O(n) to O(log n) amortized by limiting max degree.  

**Correct:** A,D


#### 11. During pairwise combine, what determines which tree becomes the subtree of the other?  
A) ✗ The tree with the smaller root does not become the subtree.  
B) ✓ The tree with the larger root becomes the subtree of the smaller root tree.  
C) ✗ Degree is always equal when combining; degree does not determine subtree.  
D) ✗ Degree is equal, so it does not determine which becomes subtree.  

**Correct:** B


#### 12. What data structure is used to keep track of trees by degree during pairwise combine?  
A) ✗ A stack is not used.  
B) ✗ A queue is not used.  
C) ✓ A table indexed by degree is used to track trees.  
D) ✗ A priority queue is not used here.  

**Correct:** C


#### 13. What is the maximum degree of any binomial tree in a binomial heap with n nodes?  
A) ✗ Max degree is not proportional to n.  
B) ✓ Max degree is O(log n) because binomial trees grow exponentially in size.  
C) ✗ It is not O(√n).  
D) ✗ It is not constant.  

**Correct:** B


#### 14. Which of the following statements about binomial trees Bk is true?  
A) ✓ Bk is formed by linking two Bk-1 trees.  
B) ✓ Bk has 2^k nodes.  
C) ✗ Bk is not necessarily a complete binary tree; it has a specific recursive structure.  
D) ✗ Bk has degree k, but not necessarily k children (degree = number of children). Actually, Bk has k children, so this is true.  
(Review: Bk has degree k, so it has k children.)  
So D) ✓ Bk has k children.  

**Correct:** A,B,D


#### 15. What is the overall complexity of the enhanced remove-min operation?  
A) ✓ O(MaxDegree + s), where s is the number of min trees after reinsertion.  
B) ✗ It is not O(n log n).  
C) ✗ It is not O(log n) amortized for remove-min (insert is amortized O(log n)).  
D) ✗ It is not O(MaxDegree * s).  

**Correct:** A


#### 16. Why is the min-element pointer updated after meld or remove-min operations?  
A) ✓ Because the minimum element may have changed after these operations.  
B) ✗ Updating min-element pointer does not maintain heap property inside trees.  
C) ✗ It does not track the largest element.  
D) ✗ It does not optimize insert operations directly.  

**Correct:** A


#### 17. Which of the following is NOT true about the sibling pointer in a binomial heap node?  
A) ✗ It is true that sibling pointer forms circular linked list of siblings.  
B) ✗ It can be null if the node has no siblings.  
C) ✓ It does NOT point to the node’s parent; it points to siblings.  
D) ✗ It helps traverse children by linking siblings.  

**Correct:** C


#### 18. What happens if the binomial heap is empty and a remove-min operation is attempted?  
A) ✓ The operation fails because there is no min element.  
B) ✗ The heap is not rebuilt.  
C) ✗ Min-element pointer is already null; no update needed.  
D) ✗ No dummy node is inserted.  

**Correct:** A


#### 19. How does the pairwise combine process affect the number of trees in the top-level list?  
A) ✗ It does not increase the number of trees.  
B) ✓ It decreases the number of trees by merging trees of equal degree.  
C) ✗ It does not keep the number the same; it reduces it.  
D) ✗ It does not remove all trees except one.  

**Correct:** B


#### 20. Which of the following best describes the relationship between the number of nodes n and the maximum degree MaxDegree in a binomial heap?  
A) ✗ MaxDegree is not proportional to n.  
B) ✓ MaxDegree is proportional to log n due to exponential growth of binomial trees.  
C) ✗ MaxDegree is not constant.  
D) ✗ MaxDegree does not grow faster than n.  

**Correct:** B