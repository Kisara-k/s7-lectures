## 3. Double-Ended Priority Queues and Interval Heaps

## Questions

#### 1. Which of the following operations are supported by a double-ended priority queue but not by a single-ended priority queue?  
A) Arbitrary element removal  
B) Remove Max  
C) Remove Min  
D) Insert  

#### 2. In a dual single-ended priority queue implementation, what is the primary reason for maintaining pointers between nodes in the min and max priority queues?  
A) To reduce space complexity  
B) To maintain heap order properties  
C) To speed up insertion operations  
D) To enable efficient arbitrary removal of elements  

#### 3. When using correspondence-based min and max single-ended priority queues with total correspondence, which of the following statements is true?  
A) The buffer always contains the largest element  
B) Each element in the min queue corresponds to a smaller element in the max queue  
C) Each element in the min queue corresponds to a different and greater or equal element in the max queue  
D) The buffer is used only when the number of elements is even  

#### 4. In an interval heap, which of the following properties hold for the intervals stored at each node?  
A) Intervals at sibling nodes are always disjoint  
B) The left endpoint is always less than or equal to the right endpoint  
C) The interval of a child node is contained within the interval of its parent node  
D) The root node contains the global minimum and maximum elements  

#### 5. During insertion into an interval heap, if the new element becomes a right endpoint, what heap property is primarily maintained?  
A) The max heap property on the right endpoints  
B) The binary search tree property  
C) The min heap property on the left endpoints  
D) The correspondence between min and max heaps  

#### 6. Which of the following correctly describe the process of removing the minimum element from an interval heap when n > 2?  
A) Swap the removed element with the right endpoint of the root node before reinsertion  
B) Delete the last node if it becomes empty after removal  
C) Remove the left endpoint from the last node and reinsert it into the min heap starting at the root  
D) Remove the left endpoint from the root node  

#### 7. Regarding cache optimization in heap operations, which statements are accurate?  
A) Insert operations percolate up approximately 1.6 levels on average  
B) The root and its children are always stored in different cache lines  
C) Using a 4-ary heap reduces the height of the heap compared to a binary heap  
D) Remove min or max operations cause about log₂ n cache misses on average  

#### 8. For a d-ary heap with degree d, which of the following formulas correctly describe the parent and children indices of node i (1-based indexing)?  
A) Children indices = d*(i - 1) + 2 to min{d*i + 1, n}  
B) Parent(i) = floor((i - 1) / d)  
C) Parent(i) = ceil((i - 1) / d)  
D) Children indices = d*i to d*i + d - 1  

#### 9. What are the advantages of using a cache-aligned 4-heap over a standard binary heap?  
A) Remove-min operations require fewer comparisons per level  
B) The number of levels to percolate during insert is doubled  
C) Siblings are stored in the same cache line, reducing cache misses  
D) Overall speedup of about 1.5 to 1.8 times in heapsort for large datasets  

#### 10. Which of the following statements about the application of interval heaps to the complementary range search problem are correct?  
A) Insertion of a point takes O(log n) time  
B) Reporting all points not in the range [a, b] takes O(k) time, where k is the number of points outside the range  
C) Removing a point given its location takes O(n) time  
D) Interval heaps can only store integer points, not real numbers  



<br>

## Answers

#### 1. Which of the following operations are supported by a double-ended priority queue but not by a single-ended priority queue?  
A) ✗ Arbitrary element removal is not a primary operation of double-ended priority queues, though some implementations support it.  
B) ✓ Remove Max is supported by double-ended but not necessarily by single-ended priority queues (which support only one remove operation).  
C) ✓ Remove Min is supported by double-ended but not necessarily by single-ended priority queues.  
D) ✓ Insert is supported by both single-ended and double-ended priority queues.  

**Correct:** B, C


#### 2. In a dual single-ended priority queue implementation, what is the primary reason for maintaining pointers between nodes in the min and max priority queues?  
A) ✗ It increases space usage rather than reducing it.  
B) ✗ The pointers do not maintain heap order properties but link corresponding elements.  
C) ✗ It does not primarily speed up insertion.  
D) ✓ Enables efficient arbitrary removal by linking corresponding elements in both queues.  

**Correct:** D


#### 3. When using correspondence-based min and max single-ended priority queues with total correspondence, which of the following statements is true?  
A) ✗ The buffer does not always contain the largest element; it holds one element when n is odd.  
B) ✗ Each element in the min queue corresponds to a greater or equal element, not smaller, in the max queue.  
C) ✓ Correct: each min queue element pairs with a different and greater or equal element in the max queue.  
D) ✗ The buffer is used when n is odd, not even.  

**Correct:** C


#### 4. In an interval heap, which of the following properties hold for the intervals stored at each node?  
A) ✗ Intervals at sibling nodes can overlap; disjointness is not guaranteed.  
B) ✓ Left endpoint ≤ right endpoint by definition of the interval.  
C) ✓ Child intervals are contained within parent intervals, maintaining heap order.  
D) ✓ Root node contains global min (left endpoint) and max (right endpoint).  

**Correct:** B, C, D


#### 5. During insertion into an interval heap, if the new element becomes a right endpoint, what heap property is primarily maintained?  
A) ✓ Right endpoints maintain the max heap property.  
B) ✗ Interval heaps do not maintain binary search tree properties.  
C) ✗ Left endpoints relate to the min heap property, not right endpoints.  
D) ✗ Correspondence between min and max heaps is not the primary concern here.  

**Correct:** A


#### 6. Which of the following correctly describe the process of removing the minimum element from an interval heap when n > 2?  
A) ✗ Swapping with right endpoint of root before reinsertion is not part of the standard removal process.  
B) ✓ Delete last node if it becomes empty after removal.  
C) ✓ Remove left endpoint from last node and reinsert it into min heap starting at root.  
D) ✓ Remove left endpoint from root node (minimum element).  

**Correct:** B, C, D


#### 7. Regarding cache optimization in heap operations, which statements are accurate?  
A) ✓ Insert percolates about 1.6 levels on average.  
B) ✗ Root and children are stored in the same cache line to optimize cache usage.  
C) ✓ Using a 4-ary heap reduces heap height compared to binary heap.  
D) ✓ Remove min/max causes about log₂ n cache misses on average.  

**Correct:** A, C, D


#### 8. For a d-ary heap with degree d, which of the following formulas correctly describe the parent and children indices of node i (1-based indexing)?  
A) ✓ Children indices = d*(i - 1) + 2 to min{d*i + 1, n} is correct.  
B) ✗ Parent(i) = floor((i - 1)/d) is incorrect; ceil is used.  
C) ✓ Parent(i) = ceil((i - 1)/d) is correct as per lecture.  
D) ✗ Children indices are not d*i to d*i + d - 1 in this scheme.  

**Correct:** A, C


#### 9. What are the advantages of using a cache-aligned 4-heap over a standard binary heap?  
A) ✗ Remove-min requires more comparisons per level (4 vs 2), not fewer.  
B) ✗ Insert percolation levels are about half, not doubled.  
C) ✓ Siblings stored in same cache line reduce cache misses.  
D) ✓ Overall speedup of about 1.5 to 1.8 times in heapsort for large data sets.  

**Correct:** C, D


#### 10. Which of the following statements about the application of interval heaps to the complementary range search problem are correct?  
A) ✓ Insertion takes O(log n) time.  
B) ✓ Reporting points not in [a,b] takes O(k), where k is number outside the range.  
C) ✗ Removing a point given its location takes O(log n), not O(n).  
D) ✗ Interval heaps can store any comparable elements, not limited to integers.  

**Correct:** A, B