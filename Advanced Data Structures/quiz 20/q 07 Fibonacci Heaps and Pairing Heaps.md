## 7. Fibonacci Heaps and Pairing Heaps

## Questions

#### 1. Which of the following operations on a Fibonacci heap have an amortized complexity of O(1)?  
A) Meld  
B) Decrease key  
C) Insert  
D) Remove min  

#### 2. In Dijkstra’s algorithm, which data structure usage leads to an overall complexity of O(n log n + e)?  
A) Array  
B) Fibonacci heap  
C) Min heap  
D) Pairing heap  

#### 3. What is the role of the ChildCut field in a Fibonacci heap node?  
A) Tracks if the node has lost a child since becoming a child of its current parent  
B) Used to maintain the degree of the node  
C) Set to false only during remove min operation  
D) Indicates if the node is a root  

#### 4. During a DecreaseKey operation in a Fibonacci heap, what happens if the decreased key violates the heap order with its parent?  
A) The node is cut and moved to the top-level list  
B) A cascading cut may be triggered  
C) The entire heap is rebuilt  
D) The node remains in place but marked as ChildCut = true  

#### 5. Which of the following statements about cascading cuts in Fibonacci heaps is true?  
A) Nodes with ChildCut = true are cut and moved to the top-level list during cascading cuts  
B) Cascading cuts only occur during insert operations  
C) Cascading cuts always stop at the root node  
D) The complexity of cascading cuts is O(log n) amortized  

#### 6. What is the worst-case degree of a node in a pairing heap after inserting elements in descending order?  
A) O(log n)  
B) n - 1  
C) O(1)  
D) O(√n)  

#### 7. Which of the following are true about the node structure of pairing heaps compared to Fibonacci heaps?  
A) Fibonacci heaps use circular doubly linked sibling lists  
B) Pairing heaps use doubly linked sibling lists that are not circular  
C) Pairing heaps maintain a ChildCut field  
D) Pairing heaps do not have parent pointers  

#### 8. How is the meld operation performed in a max pairing heap?  
A) By performing a cascading cut on the roots  
B) By comparing roots and making the tree with the larger root the leftmost subtree  
C) By comparing roots and making the tree with the smaller root the leftmost subtree  
D) By merging all children into a single list without comparisons  

#### 9. What is the amortized complexity of the remove max operation in pairing heaps when using a bad meld strategy?  
A) O(log n)  
B) O(n²)  
C) O(1)  
D) O(n)  

#### 10. Which of the following best describes the two-pass scheme for melding subtrees in pairing heaps?  
A) Meld subtrees randomly until only one remains  
B) Use a FIFO queue to meld subtrees until one remains  
C) Meld all subtrees in a single pass from left to right  
D) Meld pairs of subtrees from left to right, then meld remaining trees from right to left  

#### 11. What is the main difference between the two-pass and multipass schemes for melding subtrees in pairing heaps?  
A) Two-pass uses a queue, multipass does not  
B) Multipass is faster in practice than two-pass  
C) Two-pass has better asymptotic complexity than multipass  
D) Multipass uses a queue and repeats melding until one tree remains, two-pass does not  

#### 12. Why is the increase key operation in pairing heaps more complicated than in Fibonacci heaps?  
A) Pairing heaps maintain ChildCut fields that complicate increase key  
B) Pairing heaps do not have parent pointers to check heap order violations  
C) Increase key requires rebuilding the entire heap in pairing heaps  
D) Increase key is not supported in pairing heaps  

#### 13. When removing a non-root element in a pairing heap, which steps are involved?  
A) Remove the node from its sibling list  
B) Meld the resulting tree with the remaining original tree  
C) Perform cascading cuts on the removed node’s ancestors  
D) Meld the children of the removed node using two-pass or multipass scheme  

#### 14. Which of the following statements about the complexity of operations in Fibonacci heaps is correct?  
A) Insert has O(log n) amortized complexity  
B) Decrease key has O(log n) amortized complexity  
C) Meld has O(n) amortized complexity  
D) Remove min has O(log n) amortized complexity  

#### 15. In the context of shortest path algorithms, why is the decrease key operation important?  
A) It removes vertices from the graph  
B) It merges two heaps representing different parts of the graph  
C) It updates the tentative shortest path estimates when a better path is found  
D) It initializes the distance array  

#### 16. Which of the following are advantages of pairing heaps over Fibonacci heaps based on experimental results?  
A) Better worst-case theoretical bounds  
B) Less space per node  
C) Simpler to implement  
D) Smaller runtime overheads  

#### 17. What is the actual cost of the insert operation in pairing heaps?  
A) O(n) amortized  
B) O(log n) amortized  
C) O(1) actual cost  
D) O(n log n) amortized  

#### 18. In a Fibonacci heap, what happens to the ChildCut field of a node after a remove min operation?  
A) It remains unchanged  
B) It is set to true for all nodes  
C) It is undefined for root nodes  
D) It is set to false for nodes that become children of another node  

#### 19. Which of the following statements about the height of a pairing heap are true?  
A) Worst-case height can be as large as n  
B) Worst-case height is always O(log n)  
C) Height is always balanced due to the meld operations  
D) Inserting elements in ascending order can produce worst-case height  

#### 20. During a remove operation in a Fibonacci heap, if the node to be removed is not the minimum, what is the complexity of the operation?  
A) O(n) amortized  
B) O(log n) amortized  
C) O(1) amortized  
D) O(n log n) amortized  



<br>

## Answers

#### 1. Which of the following operations on a Fibonacci heap have an amortized complexity of O(1)?  
A) ✓ Meld is O(1) amortized.  
B) ✓ Decrease key is O(1) amortized.  
C) ✓ Insert has O(1) amortized complexity.  
D) ✗ Remove min is O(log n) amortized, not O(1).  

**Correct:** A, B, C


#### 2. In Dijkstra’s algorithm, which data structure usage leads to an overall complexity of O(n log n + e)?  
A) ✗ Array leads to O(n²) complexity.  
B) ✗ Fibonacci heap leads to O(n log n + e) complexity, which is better than min heap.  
C) ✓ Min heap leads to O(n log n + e log n) complexity, close but not exactly O(n log n + e).  
D) ✗ Pairing heap complexity is not explicitly stated as O(n log n + e) here.  

**Correct:** C


#### 3. What is the role of the ChildCut field in a Fibonacci heap node?  
A) ✓ Correct: it tracks if the node has lost a child since becoming a child of its current parent.  
B) ✗ Degree tracks the number of children, not ChildCut.  
C) ✓ Correct: ChildCut is set to false only during remove min operation.  
D) ✗ ChildCut is undefined for root nodes, so it does not indicate if a node is root.  

**Correct:** A, C


#### 4. During a DecreaseKey operation in a Fibonacci heap, what happens if the decreased key violates the heap order with its parent?  
A) ✓ The node is cut and moved to the top-level list.  
B) ✓ Cascading cut may be triggered if parent’s ChildCut is true.  
C) ✗ The entire heap is not rebuilt.  
D) ✗ The node is removed, not just marked ChildCut = true.  

**Correct:** A, B


#### 5. Which of the following statements about cascading cuts in Fibonacci heaps is true?  
A) ✓ Nodes with ChildCut = true are cut and moved to the top-level list during cascading cuts.  
B) ✗ Cascading cuts occur during remove or decrease key, not insert.  
C) ✓ Cascading cuts stop at the first node with ChildCut = false or at the root.  
D) ✗ Complexity of cascading cuts can be O(h) = O(n) worst case, not O(log n).  

**Correct:** A, C


#### 6. What is the worst-case degree of a node in a pairing heap after inserting elements in descending order?  
A) ✗ Not O(log n).  
B) ✓ Worst-case degree can be n - 1.  
C) ✗ Not O(1).  
D) ✗ Not O(√n).  

**Correct:** B


#### 7. Which of the following are true about the node structure of pairing heaps compared to Fibonacci heaps?  
A) ✓ Fibonacci heaps use circular doubly linked sibling lists.  
B) ✓ Pairing heaps use doubly linked sibling lists that are not circular.  
C) ✗ Pairing heaps do not have ChildCut fields.  
D) ✓ Pairing heaps do not have parent pointers.  

**Correct:** A, B, D


#### 8. How is the meld operation performed in a max pairing heap?  
A) ✗ Cascading cuts are not part of meld operation.  
B) ✓ Tree with larger root becomes leftmost subtree in max pairing heap.  
C) ✗ Smaller root does not become leftmost subtree in max heap.  
D) ✗ Meld requires comparison of roots.  

**Correct:** B


#### 9. What is the amortized complexity of the remove max operation in pairing heaps when using a bad meld strategy?  
A) ✗ O(log n) is for good meld strategies.  
B) ✓ O(n²) amortized complexity occurs with bad meld strategy.  
C) ✗ O(1) is too low for remove max.  
D) ✗ O(n) is not the worst case here.  

**Correct:** B


#### 10. Which of the following best describes the two-pass scheme for melding subtrees in pairing heaps?  
A) ✗ Meld is not done randomly.  
B) ✗ Using a FIFO queue is the multipass scheme, not two-pass.  
C) ✗ Two-pass requires two passes, not a single pass.  
D) ✓ Meld pairs left to right, then meld remaining trees right to left.  

**Correct:** D


#### 11. What is the main difference between the two-pass and multipass schemes for melding subtrees in pairing heaps?  
A) ✗ Two-pass does not use a queue.  
B) ✗ Two-pass generally has better observed performance, not multipass.  
C) ✗ Both have same asymptotic complexity.  
D) ✓ Multipass uses a queue and repeats melding until one tree remains; two-pass does not.  

**Correct:** D


#### 12. Why is the increase key operation in pairing heaps more complicated than in Fibonacci heaps?  
A) ✗ Pairing heaps do not have ChildCut fields.  
B) ✓ No parent pointers in pairing heaps to check heap order violations.  
C) ✗ Increase key does not require rebuilding entire heap.  
D) ✗ Increase key is supported.  

**Correct:** B


#### 13. When removing a non-root element in a pairing heap, which steps are involved?  
A) ✓ Remove the node from its sibling list.  
B) ✓ Meld the resulting tree with the remaining original tree.  
C) ✗ Cascading cuts are not part of pairing heap remove operation.  
D) ✓ Meld the children of the removed node using two-pass or multipass scheme.  

**Correct:** A, B, D


#### 14. Which of the following statements about the complexity of operations in Fibonacci heaps is correct?  
A) ✗ Insert is O(1) amortized, not O(log n).  
B) ✗ Decrease key is O(1) amortized, not O(log n).  
C) ✗ Meld is O(1) amortized, not O(n).  
D) ✓ Remove min is O(log n) amortized.  

**Correct:** D


#### 15. In the context of shortest path algorithms, why is the decrease key operation important?  
A) ✗ It does not remove vertices.  
B) ✗ It does not merge heaps.  
C) ✓ It updates tentative shortest path estimates when a better path is found.  
D) ✗ It does not initialize distances.  

**Correct:** C


#### 16. Which of the following are advantages of pairing heaps over Fibonacci heaps based on experimental results?  
A) ✗ Pairing heaps do not have better worst-case theoretical bounds.  
B) ✓ Less space per node.  
C) ✓ Simpler to implement.  
D) ✓ Smaller runtime overheads.  

**Correct:** B, C, D


#### 17. What is the actual cost of the insert operation in pairing heaps?  
A) ✗ Not O(n) amortized.  
B) ✗ Not O(log n) amortized.  
C) ✓ Actual cost is O(1).  
D) ✗ Not O(n log n).  

**Correct:** C


#### 18. In a Fibonacci heap, what happens to the ChildCut field of a node after a remove min operation?  
A) ✗ It is changed during remove min, not left unchanged.  
B) ✗ It is not set to true for all nodes.  
C) ✓ ChildCut is undefined for root nodes.  
D) ✓ Set to false for nodes that become children of another node.  

**Correct:** C, D


#### 19. Which of the following statements about the height of a pairing heap are true?  
A) ✓ Worst-case height can be as large as n.  
B) ✗ Height is not always O(log n).  
C) ✗ Height is not always balanced due to meld operations.  
D) ✓ Inserting elements in ascending order can produce worst-case height.  

**Correct:** A, D


#### 20. During a remove operation in a Fibonacci heap, if the node to be removed is not the minimum, what is the complexity of the operation?  
A) ✓ Actual cost is O(n) amortized.  
B) ✗ Not O(log n) amortized.  
C) ✗ Not O(1) amortized.  
D) ✗ Not O(n log n).  

**Correct:** A