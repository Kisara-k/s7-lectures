## 6. Binomial Heaps

## Questions

#### 1. Which of the following statements correctly describe the structure of a node in a binomial heap?  
A) Each node stores its degree, which is the number of its children.  
B) The child pointer points to the node's parent.  
C) Sibling pointers are used to form a circular linked list of siblings.  
D) The data field stores the key value of the node.  

#### 2. What is the time complexity of the basic insert operation in a binomial heap, and why?  
A) O(1), because a single-node tree is simply added to the root list.  
B) O(log n), due to the need to update the min-element pointer.  
C) O(log n), because the insert involves merging trees of equal degree.  
D) O(n), since all trees must be examined to find the min element.  

#### 3. During the remove-min operation in a binomial heap, what steps are involved?  
A) Removing the min tree from the root list.  
B) Reinserting the subtrees of the removed min tree back into the heap.  
C) Updating the min-element pointer by scanning all root nodes.  
D) Pairwise combining all trees in the heap regardless of degree.  

#### 4. Why is the initial remove-min operation in a binomial heap considered O(n) in complexity?  
A) Because it requires scanning all nodes in the heap.  
B) Because reinserting subtrees involves merging multiple trees without consolidation.  
C) Because updating the min pointer requires examining all root nodes.  
D) Because pairwise combining trees is done for all nodes, not just roots.  

#### 5. How does the enhanced remove-min operation improve the complexity of remove-min?  
A) By using a tree table to track trees by degree during reinsertion.  
B) By pairwise combining min trees whose roots have equal degree.  
C) By avoiding the need to update the min-element pointer.  
D) By reducing the number of trees in the root list after reinsertion.  

#### 6. In the pairwise combine process, what determines which tree becomes the subtree of the other?  
A) The tree with the smaller root key becomes the subtree.  
B) The tree with the larger root key becomes the subtree.  
C) The tree with the higher degree becomes the subtree.  
D) The tree that appears later in the circular list becomes the subtree.  

#### 7. Which of the following correctly describe the properties of binomial trees Bk?  
A) Bk has 2^k nodes.  
B) Bk is formed by linking two Bk-1 trees.  
C) The maximum degree of any node in Bk is k.  
D) Bk trees are always balanced binary trees.  

#### 8. What is the relationship between the maximum degree of trees in a binomial heap and the number of elements n?  
A) MaxDegree = O(n) because each element can increase degree.  
B) MaxDegree = O(log n) because binomial trees grow exponentially in size.  
C) MaxDegree is constant regardless of n.  
D) MaxDegree depends on the number of insert operations only.  

#### 9. When melding two binomial heaps, which of the following are true?  
A) The two root lists are combined into one circular linked list.  
B) The min-element pointer is updated after melding.  
C) All trees of equal degree are immediately pairwise combined during meld.  
D) Meld operation always takes O(log n) time.  

#### 10. Regarding the circular linked list representation of binomial heaps, which statements are correct?  
A) The root list is maintained as a circular linked list of min trees.  
B) Removing a min tree from the root list is equivalent to removing a node from a circular list.  
C) If the root list has only one tree, removing it leaves the heap empty.  
D) The sibling pointer of a node points to its parent in the circular list.



<br>

## Answers

#### 1. Which of the following statements correctly describe the structure of a node in a binomial heap?  
A) ✓ Node degree is the number of children, correctly describing the degree field.  
B) ✗ Child pointer points to a child, not the parent.  
C) ✓ Sibling pointers form a circular linked list of siblings, as described.  
D) ✓ Data field stores the key value of the node.  

**Correct:** A, C, D


#### 2. What is the time complexity of the basic insert operation in a binomial heap, and why?  
A) ✗ Insert is not O(1) because min pointer update or merging may be needed.  
B) ✓ O(log n) due to potential updates and merging of trees.  
C) ✗ Insert does not always involve merging trees of equal degree immediately.  
D) ✗ O(n) is too large for insert; scanning all trees is not required.  

**Correct:** B


#### 3. During the remove-min operation in a binomial heap, what steps are involved?  
A) ✓ Removing the min tree from the root list is the first step.  
B) ✓ Reinserting subtrees of the removed min tree is necessary.  
C) ✓ Updating the min-element pointer by scanning all roots is required.  
D) ✗ Pairwise combining all trees regardless of degree happens only in enhanced remove-min, not basic remove-min.  

**Correct:** A, B, C


#### 4. Why is the initial remove-min operation in a binomial heap considered O(n) in complexity?  
A) ✗ It does not scan all nodes, only root nodes.  
B) ✓ Reinserting subtrees without consolidation can be costly.  
C) ✓ Updating the min pointer requires scanning all root nodes.  
D) ✗ Pairwise combining all nodes does not happen in basic remove-min.  

**Correct:** B, C


#### 5. How does the enhanced remove-min operation improve the complexity of remove-min?  
A) ✓ Using a tree table to track trees by degree speeds up consolidation.  
B) ✓ Pairwise combining min trees of equal degree reduces the number of trees.  
C) ✗ Min-element pointer still needs updating after consolidation.  
D) ✓ Reducing the number of trees in the root list improves efficiency.  

**Correct:** A, B, D


#### 6. In the pairwise combine process, what determines which tree becomes the subtree of the other?  
A) ✗ The tree with smaller root key does not become the subtree.  
B) ✓ The tree with larger root key becomes the subtree to maintain min-heap property.  
C) ✗ Degree is always equal when combining; degree does not determine subtree.  
D) ✗ Position in the list does not determine which becomes subtree.  

**Correct:** B


#### 7. Which of the following correctly describe the properties of binomial trees Bk?  
A) ✓ Bk has 2^k nodes by definition.  
B) ✓ Bk is formed by linking two Bk-1 trees.  
C) ✗ Maximum degree of any node in Bk is not necessarily k; degree refers to root's children count.  
D) ✗ Binomial trees are not necessarily balanced binary trees; they have a specific recursive structure.  

**Correct:** A, B


#### 8. What is the relationship between the maximum degree of trees in a binomial heap and the number of elements n?  
A) ✗ MaxDegree is not O(n), that would be too large.  
B) ✓ MaxDegree = O(log n) because binomial trees grow exponentially in size.  
C) ✗ MaxDegree grows with n, so not constant.  
D) ✗ MaxDegree depends on total elements, not just insert operations.  

**Correct:** B


#### 9. When melding two binomial heaps, which of the following are true?  
A) ✓ The two root lists are combined into one circular linked list.  
B) ✓ The min-element pointer is updated after melding.  
C) ✗ Pairwise combining trees is not done immediately during meld; it happens during remove-min or explicitly.  
D) ✓ Meld operation takes O(log n) time due to merging root lists and updating min.  

**Correct:** A, B, D


#### 10. Regarding the circular linked list representation of binomial heaps, which statements are correct?  
A) ✓ The root list is maintained as a circular linked list of min trees.  
B) ✓ Removing a min tree from the root list is equivalent to removing a node from a circular list.  
C) ✓ If only one tree remains, removing it leaves the heap empty.  
D) ✗ Sibling pointer points to siblings, not parents.  

**Correct:** A, B, C