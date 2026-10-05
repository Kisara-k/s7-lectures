## 6. Binomial Heaps

## Questions

#### 1. Which of the following statements correctly describe the structure of a node in a binomial heap?  
A) The data field stores the key value of the node.  
B) Each node stores its degree, which is the number of its children.  
C) Sibling pointers are used to form a circular linked list of siblings.  
D) The child pointer points to the node's parent.  

#### 2. What is the time complexity of the basic insert operation in a binomial heap, and why?  
A) O(log n), because the insert involves merging trees of equal degree.  
B) O(log n), due to the need to update the min-element pointer.  
C) O(1), because a single-node tree is simply added to the root list.  
D) O(n), since all trees must be examined to find the min element.  

#### 3. During the remove-min operation in a binomial heap, what steps are involved?  
A) Removing the min tree from the root list.  
B) Updating the min-element pointer by scanning all root nodes.  
C) Pairwise combining all trees in the heap regardless of degree.  
D) Reinserting the subtrees of the removed min tree back into the heap.  

#### 4. Why is the initial remove-min operation in a binomial heap considered O(n) in complexity?  
A) Because updating the min pointer requires examining all root nodes.  
B) Because it requires scanning all nodes in the heap.  
C) Because reinserting subtrees involves merging multiple trees without consolidation.  
D) Because pairwise combining trees is done for all nodes, not just roots.  

#### 5. How does the enhanced remove-min operation improve the complexity of remove-min?  
A) By avoiding the need to update the min-element pointer.  
B) By using a tree table to track trees by degree during reinsertion.  
C) By reducing the number of trees in the root list after reinsertion.  
D) By pairwise combining min trees whose roots have equal degree.  

#### 6. In the pairwise combine process, what determines which tree becomes the subtree of the other?  
A) The tree with the larger root key becomes the subtree.  
B) The tree with the higher degree becomes the subtree.  
C) The tree with the smaller root key becomes the subtree.  
D) The tree that appears later in the circular list becomes the subtree.  

#### 7. Which of the following correctly describe the properties of binomial trees Bk?  
A) The maximum degree of any node in Bk is k.  
B) Bk has 2^k nodes.  
C) Bk trees are always balanced binary trees.  
D) Bk is formed by linking two Bk-1 trees.  

#### 8. What is the relationship between the maximum degree of trees in a binomial heap and the number of elements n?  
A) MaxDegree depends on the number of insert operations only.  
B) MaxDegree = O(n) because each element can increase degree.  
C) MaxDegree is constant regardless of n.  
D) MaxDegree = O(log n) because binomial trees grow exponentially in size.  

#### 9. When melding two binomial heaps, which of the following are true?  
A) The two root lists are combined into one circular linked list.  
B) The min-element pointer is updated after melding.  
C) All trees of equal degree are immediately pairwise combined during meld.  
D) Meld operation always takes O(log n) time.  

#### 10. Regarding the circular linked list representation of binomial heaps, which statements are correct?  
A) The sibling pointer of a node points to its parent in the circular list.  
B) Removing a min tree from the root list is equivalent to removing a node from a circular list.  
C) If the root list has only one tree, removing it leaves the heap empty.  
D) The root list is maintained as a circular linked list of min trees.  



<br>

## Answers

#### 1. Which of the following statements correctly describe the structure of a node in a binomial heap?  
A) ✓ Data field stores the key value of the node.  
B) ✓ Node degree is the number of children, correctly describing the degree field.  
C) ✓ Sibling pointers form a circular linked list of siblings, as described.  
D) ✗ Child pointer points to a child, not the parent.  

**Correct:** A, B, C


#### 2. What is the time complexity of the basic insert operation in a binomial heap, and why?  
A) ✗ Insert does not always involve merging trees of equal degree immediately.  
B) ✓ O(log n) due to potential updates and merging of trees.  
C) ✗ Insert is not O(1) because min pointer update or merging may be needed.  
D) ✗ O(n) is too large for insert; scanning all trees is not required.  

**Correct:** B


#### 3. During the remove-min operation in a binomial heap, what steps are involved?  
A) ✓ Removing the min tree from the root list is the first step.  
B) ✓ Updating the min-element pointer by scanning all roots is required.  
C) ✗ Pairwise combining all trees regardless of degree happens only in enhanced remove-min, not basic remove-min.  
D) ✓ Reinserting subtrees of the removed min tree is necessary.  

**Correct:** A, B, D


#### 4. Why is the initial remove-min operation in a binomial heap considered O(n) in complexity?  
A) ✓ Updating the min pointer requires scanning all root nodes.  
B) ✗ It does not scan all nodes, only root nodes.  
C) ✓ Reinserting subtrees without consolidation can be costly.  
D) ✗ Pairwise combining all nodes does not happen in basic remove-min.  

**Correct:** A, C


#### 5. How does the enhanced remove-min operation improve the complexity of remove-min?  
A) ✗ Min-element pointer still needs updating after consolidation.  
B) ✓ Using a tree table to track trees by degree speeds up consolidation.  
C) ✓ Reducing the number of trees in the root list improves efficiency.  
D) ✓ Pairwise combining min trees of equal degree reduces the number of trees.  

**Correct:** B, C, D


#### 6. In the pairwise combine process, what determines which tree becomes the subtree of the other?  
A) ✓ The tree with larger root key becomes the subtree to maintain min-heap property.  
B) ✗ Degree is always equal when combining; degree does not determine subtree.  
C) ✗ The tree with smaller root key does not become the subtree.  
D) ✗ Position in the list does not determine which becomes subtree.  

**Correct:** A


#### 7. Which of the following correctly describe the properties of binomial trees Bk?  
A) ✗ Maximum degree of any node in Bk is not necessarily k; degree refers to root's children count.  
B) ✓ Bk has 2^k nodes by definition.  
C) ✗ Binomial trees are not necessarily balanced binary trees; they have a specific recursive structure.  
D) ✓ Bk is formed by linking two Bk-1 trees.  

**Correct:** B, D


#### 8. What is the relationship between the maximum degree of trees in a binomial heap and the number of elements n?  
A) ✗ MaxDegree depends on total elements, not just insert operations.  
B) ✗ MaxDegree is not O(n), that would be too large.  
C) ✗ MaxDegree grows with n, so not constant.  
D) ✓ MaxDegree = O(log n) because binomial trees grow exponentially in size.  

**Correct:** D


#### 9. When melding two binomial heaps, which of the following are true?  
A) ✓ The two root lists are combined into one circular linked list.  
B) ✓ The min-element pointer is updated after melding.  
C) ✗ Pairwise combining trees is not done immediately during meld; it happens during remove-min or explicitly.  
D) ✓ Meld operation takes O(log n) time due to merging root lists and updating min.  

**Correct:** A, B, D


#### 10. Regarding the circular linked list representation of binomial heaps, which statements are correct?  
A) ✗ Sibling pointer points to siblings, not parents.  
B) ✓ Removing a min tree from the root list is equivalent to removing a node from a circular list.  
C) ✓ If only one tree remains, removing it leaves the heap empty.  
D) ✓ The root list is maintained as a circular linked list of min trees.  

**Correct:** B, C, D