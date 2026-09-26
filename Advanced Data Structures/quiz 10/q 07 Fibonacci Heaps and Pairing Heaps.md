## 7. Fibonacci Heaps and Pairing Heaps

## Questions

#### 1. Which of the following statements about the amortized complexities of Fibonacci heap operations are correct?  
A) Insert operation has O(1) amortized complexity.  
B) Remove min operation has O(log n) amortized complexity.  
C) Decrease key operation has O(log n) amortized complexity.  
D) Meld operation has O(log n) amortized complexity.  

#### 2. In Dijkstra’s algorithm, when using a Fibonacci heap to manage the d() values, what is the overall time complexity in terms of vertices (n) and edges (e)?  
A) O(n²)  
B) O(n log n + e)  
C) O(n log n + e log n)  
D) O(e log n)  

#### 3. Regarding the node structure of a Fibonacci heap, which of the following fields are present?  
A) Degree  
B) Parent pointer  
C) ChildCut boolean  
D) Left and right sibling pointers forming a circular doubly linked list  

#### 4. What is the purpose of the ChildCut field in a Fibonacci heap node?  
A) To indicate if the node is a root node  
B) To mark if the node has lost a child since it became a child of its current parent  
C) To help in cascading cuts during decrease key operations  
D) To track the degree of the node  

#### 5. During a cascading cut in a Fibonacci heap, which of the following are true?  
A) Nodes with ChildCut = true are cut and moved to the top-level list.  
B) The process stops at the first node with ChildCut = false, which is then set to true.  
C) Cascading cuts can have worst-case complexity O(log n).  
D) Cascading cuts can have worst-case complexity O(n).  

#### 6. Which of the following statements about pairing heaps are correct?  
A) Pairing heaps have parent pointers in their node structure.  
B) Pairing heaps use a doubly linked list of siblings that is not circular.  
C) Experimental results suggest pairing heaps are often faster than Fibonacci heaps.  
D) Pairing heaps maintain a ChildCut field similar to Fibonacci heaps.  

#### 7. In a max pairing heap, what is the worst-case degree and height of the heap after inserting elements in ascending order?  
A) Worst-case degree = n - 1  
B) Worst-case degree = log n  
C) Worst-case height = n  
D) Worst-case height = log n  

#### 8. When performing an IncreaseKey operation in a pairing heap, which of the following steps are necessary?  
A) Check if the new key is larger than the parent’s key before detaching.  
B) Detach the subtree rooted at theNode from its sibling list if theNode is not the root.  
C) Meld the detached subtree back with the remaining tree.  
D) Update the ChildCut field of theNode.  

#### 9. Which of the following describes the two-pass scheme used to meld subtrees in pairing heaps?  
A) Pass 1 melds pairs of subtrees from left to right, reducing the number of subtrees by about half.  
B) Pass 2 melds subtrees from left to right into a working tree.  
C) If the number of subtrees is odd, the last original subtree is melded with the last newly generated subtree in Pass 1.  
D) Pass 2 melds subtrees from right to left into a working tree.  

#### 10. When removing a non-root element from a pairing heap, which of the following steps are involved?  
A) Remove theNode from its doubly linked sibling list.  
B) Meld the children of theNode using either the two-pass or multipass scheme.  
C) Meld the resulting tree with the remaining original tree.  
D) Update the ChildCut field of theNode’s parent.



<br>

## Answers

#### 1. Which of the following statements about the amortized complexities of Fibonacci heap operations are correct?  
A) ✓ Insert operation has O(1) amortized complexity.  
B) ✓ Remove min operation has O(log n) amortized complexity.  
C) ✗ Decrease key operation has O(log n) amortized complexity. (It is O(1) amortized.)  
D) ✗ Meld operation has O(log n) amortized complexity. (Meld is O(1) amortized.)  

**Correct:** A,B


#### 2. In Dijkstra’s algorithm, when using a Fibonacci heap to manage the d() values, what is the overall time complexity in terms of vertices (n) and edges (e)?  
A) ✗ O(n²) (This is the complexity when using an array.)  
B) ✓ O(n log n + e) (Correct for Fibonacci heap implementation.)  
C) ✗ O(n log n + e log n) (This is for min heap, not Fibonacci heap.)  
D) ✗ O(e log n) (Does not account for vertex removals.)  

**Correct:** B


#### 3. Regarding the node structure of a Fibonacci heap, which of the following fields are present?  
A) ✓ Degree (Tracks number of children.)  
B) ✓ Parent pointer (Needed for cascading cuts.)  
C) ✓ ChildCut boolean (Indicates if node lost a child.)  
D) ✓ Left and right sibling pointers forming a circular doubly linked list (Used for sibling traversal.)  

**Correct:** A,B,C,D


#### 4. What is the purpose of the ChildCut field in a Fibonacci heap node?  
A) ✗ To indicate if the node is a root node (ChildCut is undefined for root nodes.)  
B) ✓ To mark if the node has lost a child since it became a child of its current parent (This is the exact purpose.)  
C) ✓ To help in cascading cuts during decrease key operations (Used to decide whether to cut parent.)  
D) ✗ To track the degree of the node (Degree is a separate field.)  

**Correct:** B,C


#### 5. During a cascading cut in a Fibonacci heap, which of the following are true?  
A) ✓ Nodes with ChildCut = true are cut and moved to the top-level list.  
B) ✓ The process stops at the first node with ChildCut = false, which is then set to true.  
C) ✗ Cascading cuts can have worst-case complexity O(log n). (Worst case is O(n).)  
D) ✓ Cascading cuts can have worst-case complexity O(n).  

**Correct:** A,B,D


#### 6. Which of the following statements about pairing heaps are correct?  
A) ✗ Pairing heaps have parent pointers in their node structure. (They do not have parent pointers.)  
B) ✓ Pairing heaps use a doubly linked list of siblings that is not circular.  
C) ✓ Experimental results suggest pairing heaps are often faster than Fibonacci heaps.  
D) ✗ Pairing heaps maintain a ChildCut field similar to Fibonacci heaps. (They do not have ChildCut.)  

**Correct:** B,C


#### 7. In a max pairing heap, what is the worst-case degree and height of the heap after inserting elements in ascending order?  
A) ✗ Worst-case degree = n - 1 (This occurs when inserting in descending order.)  
B) ✗ Worst-case degree = log n (No guarantee of logarithmic degree.)  
C) ✓ Worst-case height = n (Inserting ascending order yields worst-case height.)  
D) ✗ Worst-case height = log n (Height can be linear, not logarithmic.)  

**Correct:** C


#### 8. When performing an IncreaseKey operation in a pairing heap, which of the following steps are necessary?  
A) ✗ Check if the new key is larger than the parent’s key before detaching. (No parent pointer, so this check is not possible.)  
B) ✓ Detach the subtree rooted at theNode from its sibling list if theNode is not the root.  
C) ✓ Meld the detached subtree back with the remaining tree.  
D) ✗ Update the ChildCut field of theNode. (No ChildCut field in pairing heaps.)  

**Correct:** B,C


#### 9. Which of the following describes the two-pass scheme used to meld subtrees in pairing heaps?  
A) ✓ Pass 1 melds pairs of subtrees from left to right, reducing the number of subtrees by about half.  
B) ✗ Pass 2 melds subtrees from left to right into a working tree. (Pass 2 is right to left.)  
C) ✓ If the number of subtrees is odd, the last original subtree is melded with the last newly generated subtree in Pass 1.  
D) ✓ Pass 2 melds subtrees from right to left into a working tree.  

**Correct:** A,C,D


#### 10. When removing a non-root element from a pairing heap, which of the following steps are involved?  
A) ✓ Remove theNode from its doubly linked sibling list.  
B) ✓ Meld the children of theNode using either the two-pass or multipass scheme.  
C) ✓ Meld the resulting tree with the remaining original tree.  
D) ✗ Update the ChildCut field of theNode’s parent. (No ChildCut field in pairing heaps.)  

**Correct:** A,B,C