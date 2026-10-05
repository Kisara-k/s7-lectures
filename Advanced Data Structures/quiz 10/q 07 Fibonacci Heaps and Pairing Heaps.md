## 7. Fibonacci Heaps and Pairing Heaps

## Questions

#### 1. Which of the following statements about the amortized complexities of Fibonacci heap operations are correct?  
A) Decrease key operation has O(log n) amortized complexity.  
B) Remove min operation has O(log n) amortized complexity.  
C) Meld operation has O(log n) amortized complexity.  
D) Insert operation has O(1) amortized complexity.  

#### 2. In Dijkstra’s algorithm, when using a Fibonacci heap to manage the d() values, what is the overall time complexity in terms of vertices (n) and edges (e)?  
A) O(e log n)  
B) O(n²)  
C) O(n log n + e log n)  
D) O(n log n + e)  

#### 3. Regarding the node structure of a Fibonacci heap, which of the following fields are present?  
A) Degree  
B) Left and right sibling pointers forming a circular doubly linked list  
C) Parent pointer  
D) ChildCut boolean  

#### 4. What is the purpose of the ChildCut field in a Fibonacci heap node?  
A) To track the degree of the node  
B) To indicate if the node is a root node  
C) To mark if the node has lost a child since it became a child of its current parent  
D) To help in cascading cuts during decrease key operations  

#### 5. During a cascading cut in a Fibonacci heap, which of the following are true?  
A) The process stops at the first node with ChildCut = false, which is then set to true.  
B) Cascading cuts can have worst-case complexity O(log n).  
C) Nodes with ChildCut = true are cut and moved to the top-level list.  
D) Cascading cuts can have worst-case complexity O(n).  

#### 6. Which of the following statements about pairing heaps are correct?  
A) Pairing heaps maintain a ChildCut field similar to Fibonacci heaps.  
B) Experimental results suggest pairing heaps are often faster than Fibonacci heaps.  
C) Pairing heaps have parent pointers in their node structure.  
D) Pairing heaps use a doubly linked list of siblings that is not circular.  

#### 7. In a max pairing heap, what is the worst-case degree and height of the heap after inserting elements in ascending order?  
A) Worst-case degree = n - 1  
B) Worst-case height = n  
C) Worst-case height = log n  
D) Worst-case degree = log n  

#### 8. When performing an IncreaseKey operation in a pairing heap, which of the following steps are necessary?  
A) Detach the subtree rooted at theNode from its sibling list if theNode is not the root.  
B) Check if the new key is larger than the parent’s key before detaching.  
C) Update the ChildCut field of theNode.  
D) Meld the detached subtree back with the remaining tree.  

#### 9. Which of the following describes the two-pass scheme used to meld subtrees in pairing heaps?  
A) Pass 2 melds subtrees from right to left into a working tree.  
B) If the number of subtrees is odd, the last original subtree is melded with the last newly generated subtree in Pass 1.  
C) Pass 1 melds pairs of subtrees from left to right, reducing the number of subtrees by about half.  
D) Pass 2 melds subtrees from left to right into a working tree.  

#### 10. When removing a non-root element from a pairing heap, which of the following steps are involved?  
A) Meld the children of theNode using either the two-pass or multipass scheme.  
B) Remove theNode from its doubly linked sibling list.  
C) Meld the resulting tree with the remaining original tree.  
D) Update the ChildCut field of theNode’s parent.  



<br>

## Answers

#### 1. Which of the following statements about the amortized complexities of Fibonacci heap operations are correct?  
A) ✗ Decrease key operation has O(log n) amortized complexity. (It is O(1) amortized.)  
B) ✓ Remove min operation has O(log n) amortized complexity.  
C) ✗ Meld operation has O(log n) amortized complexity. (Meld is O(1) amortized.)  
D) ✓ Insert operation has O(1) amortized complexity.  

**Correct:** B, D


#### 2. In Dijkstra’s algorithm, when using a Fibonacci heap to manage the d() values, what is the overall time complexity in terms of vertices (n) and edges (e)?  
A) ✗ O(e log n) (Does not account for vertex removals.)  
B) ✗ O(n²) (This is the complexity when using an array.)  
C) ✗ O(n log n + e log n) (This is for min heap, not Fibonacci heap.)  
D) ✓ O(n log n + e) (Correct for Fibonacci heap implementation.)  

**Correct:** D


#### 3. Regarding the node structure of a Fibonacci heap, which of the following fields are present?  
A) ✓ Degree (Tracks number of children.)  
B) ✓ Left and right sibling pointers forming a circular doubly linked list (Used for sibling traversal.)  
C) ✓ Parent pointer (Needed for cascading cuts.)  
D) ✓ ChildCut boolean (Indicates if node lost a child.)  

**Correct:** A, B, C, D


#### 4. What is the purpose of the ChildCut field in a Fibonacci heap node?  
A) ✗ To track the degree of the node (Degree is a separate field.)  
B) ✗ To indicate if the node is a root node (ChildCut is undefined for root nodes.)  
C) ✓ To mark if the node has lost a child since it became a child of its current parent (This is the exact purpose.)  
D) ✓ To help in cascading cuts during decrease key operations (Used to decide whether to cut parent.)  

**Correct:** C, D


#### 5. During a cascading cut in a Fibonacci heap, which of the following are true?  
A) ✓ The process stops at the first node with ChildCut = false, which is then set to true.  
B) ✗ Cascading cuts can have worst-case complexity O(log n). (Worst case is O(n).)  
C) ✓ Nodes with ChildCut = true are cut and moved to the top-level list.  
D) ✓ Cascading cuts can have worst-case complexity O(n).  

**Correct:** A, C, D


#### 6. Which of the following statements about pairing heaps are correct?  
A) ✗ Pairing heaps maintain a ChildCut field similar to Fibonacci heaps. (They do not have ChildCut.)  
B) ✓ Experimental results suggest pairing heaps are often faster than Fibonacci heaps.  
C) ✗ Pairing heaps have parent pointers in their node structure. (They do not have parent pointers.)  
D) ✓ Pairing heaps use a doubly linked list of siblings that is not circular.  

**Correct:** B, D


#### 7. In a max pairing heap, what is the worst-case degree and height of the heap after inserting elements in ascending order?  
A) ✗ Worst-case degree = n - 1 (This occurs when inserting in descending order.)  
B) ✓ Worst-case height = n (Inserting ascending order yields worst-case height.)  
C) ✗ Worst-case height = log n (Height can be linear, not logarithmic.)  
D) ✗ Worst-case degree = log n (No guarantee of logarithmic degree.)  

**Correct:** B


#### 8. When performing an IncreaseKey operation in a pairing heap, which of the following steps are necessary?  
A) ✓ Detach the subtree rooted at theNode from its sibling list if theNode is not the root.  
B) ✗ Check if the new key is larger than the parent’s key before detaching. (No parent pointer, so this check is not possible.)  
C) ✗ Update the ChildCut field of theNode. (No ChildCut field in pairing heaps.)  
D) ✓ Meld the detached subtree back with the remaining tree.  

**Correct:** A, D


#### 9. Which of the following describes the two-pass scheme used to meld subtrees in pairing heaps?  
A) ✓ Pass 2 melds subtrees from right to left into a working tree.  
B) ✓ If the number of subtrees is odd, the last original subtree is melded with the last newly generated subtree in Pass 1.  
C) ✓ Pass 1 melds pairs of subtrees from left to right, reducing the number of subtrees by about half.  
D) ✗ Pass 2 melds subtrees from left to right into a working tree. (Pass 2 is right to left.)  

**Correct:** A, B, C


#### 10. When removing a non-root element from a pairing heap, which of the following steps are involved?  
A) ✓ Meld the children of theNode using either the two-pass or multipass scheme.  
B) ✓ Remove theNode from its doubly linked sibling list.  
C) ✓ Meld the resulting tree with the remaining original tree.  
D) ✗ Update the ChildCut field of theNode’s parent. (No ChildCut field in pairing heaps.)  

**Correct:** A, B, C