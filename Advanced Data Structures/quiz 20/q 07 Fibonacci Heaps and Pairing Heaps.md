## 7. Fibonacci Heaps and Pairing Heaps

## Questions

#### 1. Which of the following operations on a Fibonacci heap have an amortized complexity of O(1)?  
A) Insert  
B) Remove min  
C) Decrease key  
D) Meld  

#### 2. In Dijkstra’s algorithm, which data structure usage leads to an overall complexity of O(n log n + e)?  
A) Array  
B) Min heap  
C) Fibonacci heap  
D) Pairing heap  

#### 3. What is the role of the ChildCut field in a Fibonacci heap node?  
A) Indicates if the node is a root  
B) Tracks if the node has lost a child since becoming a child of its current parent  
C) Used to maintain the degree of the node  
D) Set to false only during remove min operation  

#### 4. During a DecreaseKey operation in a Fibonacci heap, what happens if the decreased key violates the heap order with its parent?  
A) The node is cut and moved to the top-level list  
B) The entire heap is rebuilt  
C) The node remains in place but marked as ChildCut = true  
D) A cascading cut may be triggered  

#### 5. Which of the following statements about cascading cuts in Fibonacci heaps is true?  
A) Cascading cuts always stop at the root node  
B) The complexity of cascading cuts is O(log n) amortized  
C) Nodes with ChildCut = true are cut and moved to the top-level list during cascading cuts  
D) Cascading cuts only occur during insert operations  

#### 6. What is the worst-case degree of a node in a pairing heap after inserting elements in descending order?  
A) O(log n)  
B) n - 1  
C) O(1)  
D) O(√n)  

#### 7. Which of the following are true about the node structure of pairing heaps compared to Fibonacci heaps?  
A) Pairing heaps do not have parent pointers  
B) Pairing heaps maintain a ChildCut field  
C) Pairing heaps use doubly linked sibling lists that are not circular  
D) Fibonacci heaps use circular doubly linked sibling lists  

#### 8. How is the meld operation performed in a max pairing heap?  
A) By comparing roots and making the tree with the smaller root the leftmost subtree  
B) By merging all children into a single list without comparisons  
C) By comparing roots and making the tree with the larger root the leftmost subtree  
D) By performing a cascading cut on the roots  

#### 9. What is the amortized complexity of the remove max operation in pairing heaps when using a bad meld strategy?  
A) O(log n)  
B) O(n)  
C) O(n²)  
D) O(1)  

#### 10. Which of the following best describes the two-pass scheme for melding subtrees in pairing heaps?  
A) Meld pairs of subtrees from left to right, then meld remaining trees from right to left  
B) Meld all subtrees in a single pass from left to right  
C) Use a FIFO queue to meld subtrees until one remains  
D) Meld subtrees randomly until only one remains  

#### 11. What is the main difference between the two-pass and multipass schemes for melding subtrees in pairing heaps?  
A) Two-pass uses a queue, multipass does not  
B) Multipass uses a queue and repeats melding until one tree remains, two-pass does not  
C) Two-pass has better asymptotic complexity than multipass  
D) Multipass is faster in practice than two-pass  

#### 12. Why is the increase key operation in pairing heaps more complicated than in Fibonacci heaps?  
A) Pairing heaps do not have parent pointers to check heap order violations  
B) Increase key requires rebuilding the entire heap in pairing heaps  
C) Increase key is not supported in pairing heaps  
D) Pairing heaps maintain ChildCut fields that complicate increase key  

#### 13. When removing a non-root element in a pairing heap, which steps are involved?  
A) Remove the node from its sibling list  
B) Meld the children of the removed node using two-pass or multipass scheme  
C) Meld the resulting tree with the remaining original tree  
D) Perform cascading cuts on the removed node’s ancestors  

#### 14. Which of the following statements about the complexity of operations in Fibonacci heaps is correct?  
A) Remove min has O(log n) amortized complexity  
B) Insert has O(log n) amortized complexity  
C) Decrease key has O(log n) amortized complexity  
D) Meld has O(n) amortized complexity  

#### 15. In the context of shortest path algorithms, why is the decrease key operation important?  
A) It updates the tentative shortest path estimates when a better path is found  
B) It removes vertices from the graph  
C) It merges two heaps representing different parts of the graph  
D) It initializes the distance array  

#### 16. Which of the following are advantages of pairing heaps over Fibonacci heaps based on experimental results?  
A) Simpler to implement  
B) Smaller runtime overheads  
C) Less space per node  
D) Better worst-case theoretical bounds  

#### 17. What is the actual cost of the insert operation in pairing heaps?  
A) O(log n) amortized  
B) O(1) actual cost  
C) O(n) amortized  
D) O(n log n) amortized  

#### 18. In a Fibonacci heap, what happens to the ChildCut field of a node after a remove min operation?  
A) It is set to true for all nodes  
B) It is set to false for nodes that become children of another node  
C) It remains unchanged  
D) It is undefined for root nodes  

#### 19. Which of the following statements about the height of a pairing heap are true?  
A) Worst-case height can be as large as n  
B) Worst-case height is always O(log n)  
C) Inserting elements in ascending order can produce worst-case height  
D) Height is always balanced due to the meld operations  

#### 20. During a remove operation in a Fibonacci heap, if the node to be removed is not the minimum, what is the complexity of the operation?  
A) O(1) amortized  
B) O(log n) amortized  
C) O(n) amortized  
D) O(n log n) amortized



<br>

## Answers

#### 1. Which of the following operations on a Fibonacci heap have an amortized complexity of O(1)?  
A) ✓ Insert has O(1) amortized complexity.  
B) ✗ Remove min is O(log n) amortized, not O(1).  
C) ✓ Decrease key is O(1) amortized.  
D) ✓ Meld is O(1) amortized.  

**Correct:** A,C,D


#### 2. In Dijkstra’s algorithm, which data structure usage leads to an overall complexity of O(n log n + e)?  
A) ✗ Array leads to O(n²) complexity.  
B) ✓ Min heap leads to O(n log n + e log n) complexity, close but not exactly O(n log n + e).  
C) ✗ Fibonacci heap leads to O(n log n + e) complexity, which is better than min heap.  
D) ✗ Pairing heap complexity is not explicitly stated as O(n log n + e) here.  

**Correct:** B


#### 3. What is the role of the ChildCut field in a Fibonacci heap node?  
A) ✗ ChildCut is undefined for root nodes, so it does not indicate if a node is root.  
B) ✓ Correct: it tracks if the node has lost a child since becoming a child of its current parent.  
C) ✗ Degree tracks the number of children, not ChildCut.  
D) ✓ Correct: ChildCut is set to false only during remove min operation.  

**Correct:** B,D


#### 4. During a DecreaseKey operation in a Fibonacci heap, what happens if the decreased key violates the heap order with its parent?  
A) ✓ The node is cut and moved to the top-level list.  
B) ✗ The entire heap is not rebuilt.  
C) ✗ The node is removed, not just marked ChildCut = true.  
D) ✓ Cascading cut may be triggered if parent’s ChildCut is true.  

**Correct:** A,D


#### 5. Which of the following statements about cascading cuts in Fibonacci heaps is true?  
A) ✓ Cascading cuts stop at the first node with ChildCut = false or at the root.  
B) ✗ Complexity of cascading cuts can be O(h) = O(n) worst case, not O(log n).  
C) ✓ Nodes with ChildCut = true are cut and moved to the top-level list during cascading cuts.  
D) ✗ Cascading cuts occur during remove or decrease key, not insert.  

**Correct:** A,C


#### 6. What is the worst-case degree of a node in a pairing heap after inserting elements in descending order?  
A) ✗ Not O(log n).  
B) ✓ Worst-case degree can be n - 1.  
C) ✗ Not O(1).  
D) ✗ Not O(√n).  

**Correct:** B


#### 7. Which of the following are true about the node structure of pairing heaps compared to Fibonacci heaps?  
A) ✓ Pairing heaps do not have parent pointers.  
B) ✗ Pairing heaps do not have ChildCut fields.  
C) ✓ Pairing heaps use doubly linked sibling lists that are not circular.  
D) ✓ Fibonacci heaps use circular doubly linked sibling lists.  

**Correct:** A,C,D


#### 8. How is the meld operation performed in a max pairing heap?  
A) ✗ Smaller root does not become leftmost subtree in max heap.  
B) ✗ Meld requires comparison of roots.  
C) ✓ Tree with larger root becomes leftmost subtree in max pairing heap.  
D) ✗ Cascading cuts are not part of meld operation.  

**Correct:** C


#### 9. What is the amortized complexity of the remove max operation in pairing heaps when using a bad meld strategy?  
A) ✗ O(log n) is for good meld strategies.  
B) ✗ O(n) is not the worst case here.  
C) ✓ O(n²) amortized complexity occurs with bad meld strategy.  
D) ✗ O(1) is too low for remove max.  

**Correct:** C


#### 10. Which of the following best describes the two-pass scheme for melding subtrees in pairing heaps?  
A) ✓ Meld pairs left to right, then meld remaining trees right to left.  
B) ✗ Two-pass requires two passes, not a single pass.  
C) ✗ Using a FIFO queue is the multipass scheme, not two-pass.  
D) ✗ Meld is not done randomly.  

**Correct:** A


#### 11. What is the main difference between the two-pass and multipass schemes for melding subtrees in pairing heaps?  
A) ✗ Two-pass does not use a queue.  
B) ✓ Multipass uses a queue and repeats melding until one tree remains; two-pass does not.  
C) ✗ Both have same asymptotic complexity.  
D) ✗ Two-pass generally has better observed performance, not multipass.  

**Correct:** B


#### 12. Why is the increase key operation in pairing heaps more complicated than in Fibonacci heaps?  
A) ✓ No parent pointers in pairing heaps to check heap order violations.  
B) ✗ Increase key does not require rebuilding entire heap.  
C) ✗ Increase key is supported.  
D) ✗ Pairing heaps do not have ChildCut fields.  

**Correct:** A


#### 13. When removing a non-root element in a pairing heap, which steps are involved?  
A) ✓ Remove the node from its sibling list.  
B) ✓ Meld the children of the removed node using two-pass or multipass scheme.  
C) ✓ Meld the resulting tree with the remaining original tree.  
D) ✗ Cascading cuts are not part of pairing heap remove operation.  

**Correct:** A,B,C


#### 14. Which of the following statements about the complexity of operations in Fibonacci heaps is correct?  
A) ✓ Remove min is O(log n) amortized.  
B) ✗ Insert is O(1) amortized, not O(log n).  
C) ✗ Decrease key is O(1) amortized, not O(log n).  
D) ✗ Meld is O(1) amortized, not O(n).  

**Correct:** A


#### 15. In the context of shortest path algorithms, why is the decrease key operation important?  
A) ✓ It updates tentative shortest path estimates when a better path is found.  
B) ✗ It does not remove vertices.  
C) ✗ It does not merge heaps.  
D) ✗ It does not initialize distances.  

**Correct:** A


#### 16. Which of the following are advantages of pairing heaps over Fibonacci heaps based on experimental results?  
A) ✓ Simpler to implement.  
B) ✓ Smaller runtime overheads.  
C) ✓ Less space per node.  
D) ✗ Pairing heaps do not have better worst-case theoretical bounds.  

**Correct:** A,B,C


#### 17. What is the actual cost of the insert operation in pairing heaps?  
A) ✗ Not O(log n) amortized.  
B) ✓ Actual cost is O(1).  
C) ✗ Not O(n) amortized.  
D) ✗ Not O(n log n).  

**Correct:** B


#### 18. In a Fibonacci heap, what happens to the ChildCut field of a node after a remove min operation?  
A) ✗ It is not set to true for all nodes.  
B) ✓ Set to false for nodes that become children of another node.  
C) ✗ It is changed during remove min, not left unchanged.  
D) ✓ ChildCut is undefined for root nodes.  

**Correct:** B,D


#### 19. Which of the following statements about the height of a pairing heap are true?  
A) ✓ Worst-case height can be as large as n.  
B) ✗ Height is not always O(log n).  
C) ✓ Inserting elements in ascending order can produce worst-case height.  
D) ✗ Height is not always balanced due to meld operations.  

**Correct:** A,C


#### 20. During a remove operation in a Fibonacci heap, if the node to be removed is not the minimum, what is the complexity of the operation?  
A) ✗ Not O(1) amortized.  
B) ✗ Not O(log n) amortized.  
C) ✓ Actual cost is O(n) amortized.  
D) ✗ Not O(n log n).  

**Correct:** C