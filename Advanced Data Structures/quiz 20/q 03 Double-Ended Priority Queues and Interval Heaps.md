## 3. Double-Ended Priority Queues and Interval Heaps

## Questions

#### 1. Which of the following operations are primary operations supported by a double-ended priority queue?  
A) Insert  
B) Remove Max  
C) Remove Min  
D) Find Median  

#### 2. In a dual single-ended priority queue implementation, what is a necessary feature of the single-ended priority queues used?  
A) Support for arbitrary remove operations  
B) Support only insert and remove min  
C) Each node must have a pointer to the corresponding node in the other queue  
D) They must be implemented as balanced binary search trees  

#### 3. What is a key disadvantage of maintaining dual single-ended priority queues for double-ended priority queue operations?  
A) Operation cost is more than doubled relative to a single heap  
B) Space complexity is reduced to n/2 nodes  
C) Insertions become constant time  
D) It requires no additional pointers between queues  

#### 4. In correspondence-based min and max single-ended priority queues, what happens when the number of elements n is odd?  
A) One element is placed in a buffer  
B) The min queue contains one extra element  
C) The max queue contains one extra element  
D) The structure becomes unbalanced  

#### 5. What does total correspondence between min and max single-ended priority queues imply?  
A) Each element in the min queue is paired with a different and greater or equal element in the max queue  
B) Each element in the min queue is paired with the exact same element in the max queue  
C) The min and max queues have the same number of elements always  
D) Elements in the max queue are always smaller than those in the min queue  

#### 6. When inserting a new element into a correspondence-based structure with a buffer, what is the correct procedure if the buffer is not empty?  
A) Insert the smaller of the new element and buffer element into the min queue, and the larger into the max queue  
B) Insert the new element directly into the buffer  
C) Insert the larger of the new element and buffer element into the min queue, and the smaller into the max queue  
D) Discard the buffer element and insert the new element into the min queue  

#### 7. Which of the following correctly describes the structure of an interval heap node?  
A) Each node contains exactly two elements, a and b, with a ≤ b  
B) Each node contains one or two elements, with the interval [a, b] representing the node  
C) The interval [a, b] in a node is always disjoint from its parent’s interval  
D) The last node may contain only one element, representing the interval [a, a]  

#### 8. In an interval heap, what property must hold between a node’s interval and its parent’s interval?  
A) The node’s interval is contained within the parent’s interval  
B) The node’s interval is disjoint from the parent’s interval  
C) The node’s interval is always larger than the parent’s interval  
D) The node’s interval overlaps partially with the parent’s interval  

#### 9. How are the min and max elements stored in an interval heap?  
A) Both are stored in the root node  
B) Min is stored in the leftmost leaf, max in the rightmost leaf  
C) Min is stored in the min single-ended priority queue, max in the max single-ended priority queue  
D) Min and max are stored in separate heaps outside the interval heap  

#### 10. When inserting a new element into an interval heap, what determines whether it becomes a left or right endpoint?  
A) If the new element is smaller, it becomes a left endpoint; if larger, a right endpoint  
B) New elements always become left endpoints  
C) New elements always become right endpoints  
D) The position is chosen randomly  

#### 11. What is the complexity of removing the minimum element from an interval heap when n > 2?  
A) It is straightforward and constant time  
B) It involves removing the left endpoint from the root and reinserting elements, requiring O(log n) time  
C) It requires scanning all nodes to find the minimum  
D) It is the same as removing the maximum element  

#### 12. During the remove-min operation in an interval heap, why might swapping with the right endpoint be necessary?  
A) To maintain the interval property that left endpoint ≤ right endpoint  
B) To rebalance the heap height  
C) To maintain the heap as a binary search tree  
D) To ensure the root node contains only one element  

#### 13. What is the purpose of the initialization process in an interval heap?  
A) To examine nodes bottom-up and swap endpoints if needed to maintain interval properties  
B) To convert the interval heap into a min heap  
C) To remove all duplicate elements  
D) To flatten the heap into a sorted array  

#### 14. Regarding cache optimization in heap operations, which statement is true?  
A) Insert percolates about 1.6 levels up the heap on average  
B) Remove min (max) operations cause no cache misses  
C) Cache utilization is irrelevant for heap performance  
D) Remove min (max) operations percolate about 10 levels down the heap on average  

#### 15. In a cache-aligned array for heaps, why is only half of each cache line used (except for the root’s)?  
A) Because each heap node is 8 bytes and a cache line holds 32 bytes, but nodes are spaced such that siblings are not fully packed  
B) Because the cache line size is too small to hold a full node  
C) Because heap nodes are stored in linked lists, not arrays  
D) Because the cache line is reserved for other data  

#### 16. For a d-ary heap with degree d, what is the formula for the parent of node i?  
A) Parent(i) = ceil((i - 1)/d)  
B) Parent(i) = floor(i/d)  
C) Parent(i) = i/d  
D) Parent(i) = i - d  

#### 17. How does the height of a 4-ary heap compare to that of a binary heap with the same number of nodes?  
A) The height of a 4-ary heap is about half that of a binary heap  
B) The height is the same for both heaps  
C) The 4-ary heap has twice the height of the binary heap  
D) The 4-ary heap height is logarithmic base 2 of the binary heap height  

#### 18. What is a trade-off when using a 4-ary heap instead of a binary heap for remove-min operations?  
A) More comparisons per level but fewer levels to traverse  
B) Fewer comparisons per level but more levels to traverse  
C) The same number of comparisons and levels as a binary heap  
D) Remove-min operations become linear time  

#### 19. How can cache utilization be improved for a 4-ary heap?  
A) By shifting the heap array by 2 slots so siblings are in the same cache line  
B) By storing the heap as a linked list  
C) By increasing the cache line size to 64 bytes  
D) By using a binary heap instead  

#### 20. Which of the following are true about the application of interval heaps in the complementary range search problem?  
A) Insertion of a point takes O(log n) time  
B) Removing a point given its location takes O(log n) time  
C) Reporting all points not in the range [a, b] takes O(k) time, where k is the number of points outside the range  
D) Interval heaps cannot efficiently support range queries



<br>

## Answers

#### 1. Which of the following operations are primary operations supported by a double-ended priority queue?  
A) ✓ Insert is a primary operation.  
B) ✓ Remove Max is a primary operation.  
C) ✓ Remove Min is a primary operation.  
D) ✗ Find Median is not a primary operation of double-ended priority queues.  

**Correct:** A,B,C


#### 2. In a dual single-ended priority queue implementation, what is a necessary feature of the single-ended priority queues used?  
A) ✓ Must support arbitrary remove to allow removal of elements from either queue.  
B) ✗ Supporting only insert and remove min is insufficient for dual queues.  
C) ✓ Each node must have a pointer to the corresponding node in the other queue for synchronization.  
D) ✗ Balanced binary search trees are not required; heaps are typical.  

**Correct:** A,C


#### 3. What is a key disadvantage of maintaining dual single-ended priority queues for double-ended priority queue operations?  
A) ✓ Operation cost more than doubles compared to a single heap.  
B) ✗ Space complexity increases to 2n nodes, not reduced.  
C) ✗ Insertions do not become constant time; they become more expensive.  
D) ✗ Additional pointers between queues are required.  

**Correct:** A


#### 4. In correspondence-based min and max single-ended priority queues, what happens when the number of elements n is odd?  
A) ✓ One element is placed in a buffer to maintain balance.  
B) ✗ The min queue does not necessarily have one extra element.  
C) ✗ The max queue does not necessarily have one extra element.  
D) ✗ The structure does not become unbalanced; buffer handles odd element.  

**Correct:** A


#### 5. What does total correspondence between min and max single-ended priority queues imply?  
A) ✓ Each min element is paired with a different and greater or equal max element.  
B) ✗ Elements are not the exact same in both queues; they are paired but distinct nodes.  
C) ✗ The queues may have different sizes if buffer is used.  
D) ✗ Max elements are not smaller than min elements; they are greater or equal.  

**Correct:** A


#### 6. When inserting a new element into a correspondence-based structure with a buffer, what is the correct procedure if the buffer is not empty?  
A) ✓ Insert smaller of new and buffer into min queue, larger into max queue, establish correspondence.  
B) ✗ New element is not inserted directly into buffer if buffer is occupied.  
C) ✗ Larger element goes to max queue, not min queue.  
D) ✗ Buffer element is not discarded.  

**Correct:** A


#### 7. Which of the following correctly describes the structure of an interval heap node?  
A) ✗ Nodes can have one or two elements; not always exactly two.  
B) ✓ Nodes have one or two elements representing interval [a, b].  
C) ✗ Node intervals are contained within parent intervals, not disjoint.  
D) ✓ Last node may have one element representing [a, a].  

**Correct:** B,D


#### 8. In an interval heap, what property must hold between a node’s interval and its parent’s interval?  
A) ✓ Node’s interval is contained within parent’s interval.  
B) ✗ Intervals are not disjoint.  
C) ✗ Node’s interval is not larger than parent’s.  
D) ✗ Partial overlap without containment is not allowed.  

**Correct:** A


#### 9. How are the min and max elements stored in an interval heap?  
A) ✓ Both min and max are stored in the root node.  
B) ✗ Min and max are not stored at leaves.  
C) ✗ Min and max are not stored in separate single-ended priority queues here.  
D) ✗ Min and max are not stored outside the interval heap.  

**Correct:** A


#### 10. When inserting a new element into an interval heap, what determines whether it becomes a left or right endpoint?  
A) ✓ Smaller elements become left endpoints; larger become right endpoints.  
B) ✗ New elements do not always become left endpoints.  
C) ✗ New elements do not always become right endpoints.  
D) ✗ Position is not random.  

**Correct:** A


#### 11. What is the complexity of removing the minimum element from an interval heap when n > 2?  
A) ✗ It is not constant time or straightforward.  
B) ✓ Requires removing left endpoint from root, reinserting elements, O(log n) time.  
C) ✗ No scanning of all nodes is needed.  
D) ✗ Remove min and remove max differ in procedure.  

**Correct:** B


#### 12. During the remove-min operation in an interval heap, why might swapping with the right endpoint be necessary?  
A) ✓ To maintain the interval property that left endpoint ≤ right endpoint.  
B) ✗ Not for rebalancing height.  
C) ✗ Interval heaps are not binary search trees.  
D) ✗ Root node can have two elements; no need to reduce to one.  

**Correct:** A


#### 13. What is the purpose of the initialization process in an interval heap?  
A) ✓ Bottom-up examination to swap endpoints and maintain interval properties.  
B) ✗ It does not convert the heap into a min heap.  
C) ✗ It does not remove duplicates.  
D) ✗ It does not flatten the heap.  

**Correct:** A


#### 14. Regarding cache optimization in heap operations, which statement is true?  
A) ✓ Insert percolates about 1.6 levels up on average.  
B) ✗ Remove min (max) causes cache misses proportional to height.  
C) ✗ Cache utilization significantly affects performance.  
D) ✗ Remove min (max) percolates about log n levels, not 10 levels.  

**Correct:** A


#### 15. In a cache-aligned array for heaps, why is only half of each cache line used (except for the root’s)?  
A) ✓ Because nodes are spaced such that siblings are not fully packed in cache lines.  
B) ✗ Cache line size is sufficient for nodes.  
C) ✗ Heaps are stored as arrays, not linked lists.  
D) ✗ Cache lines are not reserved for other data in this context.  

**Correct:** A


#### 16. For a d-ary heap with degree d, what is the formula for the parent of node i?  
A) ✓ Parent(i) = ceil((i - 1)/d) is correct.  
B) ✗ floor(i/d) is incorrect.  
C) ✗ i/d without ceiling or floor is incorrect.  
D) ✗ i - d is incorrect.  

**Correct:** A


#### 17. How does the height of a 4-ary heap compare to that of a binary heap with the same number of nodes?  
A) ✓ Height of 4-ary heap is about half that of binary heap.  
B) ✗ Heights are not equal.  
C) ✗ 4-ary heap height is not twice binary heap height.  
D) ✗ Logarithmic base 2 of binary heap height is not meaningful here.  

**Correct:** A


#### 18. What is a trade-off when using a 4-ary heap instead of a binary heap for remove-min operations?  
A) ✓ More comparisons per level but fewer levels to traverse.  
B) ✗ Fewer comparisons per level is false.  
C) ✗ Same comparisons and levels is false.  
D) ✗ Remove-min does not become linear time.  

**Correct:** A


#### 19. How can cache utilization be improved for a 4-ary heap?  
A) ✓ By shifting the heap array by 2 slots so siblings align in the same cache line.  
B) ✗ Linked lists reduce cache locality.  
C) ✗ Increasing cache line size is hardware dependent, not a heap design.  
D) ✗ Using binary heap does not improve cache utilization here.  

**Correct:** A


#### 20. Which of the following are true about the application of interval heaps in the complementary range search problem?  
A) ✓ Insertion takes O(log n) time.  
B) ✓ Removing a point given its location takes O(log n) time.  
C) ✓ Reporting points not in [a,b] takes O(k) time, where k is number outside range.  
D) ✗ Interval heaps can efficiently support range queries as described.  

**Correct:** A,B,C