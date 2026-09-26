## 3. Double-Ended Priority Queues and Interval Heaps

## Questions

#### 1. Which of the following operations are supported by a double-ended priority queue but not by a single-ended priority queue?  
A) Insert  
B) Remove Max  
C) Remove Min  
D) Arbitrary element removal  

#### 2. In a dual single-ended priority queue implementation, what is the primary reason for maintaining pointers between nodes in the min and max priority queues?  
A) To reduce space complexity  
B) To enable efficient arbitrary removal of elements  
C) To speed up insertion operations  
D) To maintain heap order properties  

#### 3. When using correspondence-based min and max single-ended priority queues with total correspondence, which of the following statements is true?  
A) Each element in the min queue corresponds to a smaller element in the max queue  
B) Each element in the min queue corresponds to a different and greater or equal element in the max queue  
C) The buffer always contains the largest element  
D) The buffer is used only when the number of elements is even  

#### 4. In an interval heap, which of the following properties hold for the intervals stored at each node?  
A) The left endpoint is always less than or equal to the right endpoint  
B) The interval of a child node is contained within the interval of its parent node  
C) The root node contains the global minimum and maximum elements  
D) Intervals at sibling nodes are always disjoint  

#### 5. During insertion into an interval heap, if the new element becomes a right endpoint, what heap property is primarily maintained?  
A) The min heap property on the left endpoints  
B) The max heap property on the right endpoints  
C) The binary search tree property  
D) The correspondence between min and max heaps  

#### 6. Which of the following correctly describe the process of removing the minimum element from an interval heap when n > 2?  
A) Remove the left endpoint from the root node  
B) Remove the left endpoint from the last node and reinsert it into the min heap starting at the root  
C) Delete the last node if it becomes empty after removal  
D) Swap the removed element with the right endpoint of the root node before reinsertion  

#### 7. Regarding cache optimization in heap operations, which statements are accurate?  
A) Insert operations percolate up approximately 1.6 levels on average  
B) Remove min or max operations cause about log₂ n cache misses on average  
C) The root and its children are always stored in different cache lines  
D) Using a 4-ary heap reduces the height of the heap compared to a binary heap  

#### 8. For a d-ary heap with degree d, which of the following formulas correctly describe the parent and children indices of node i (1-based indexing)?  
A) Parent(i) = floor((i - 1) / d)  
B) Parent(i) = ceil((i - 1) / d)  
C) Children indices = d*(i - 1) + 2 to min{d*i + 1, n}  
D) Children indices = d*i to d*i + d - 1  

#### 9. What are the advantages of using a cache-aligned 4-heap over a standard binary heap?  
A) Siblings are stored in the same cache line, reducing cache misses  
B) The number of levels to percolate during insert is doubled  
C) Remove-min operations require fewer comparisons per level  
D) Overall speedup of about 1.5 to 1.8 times in heapsort for large datasets  

#### 10. Which of the following statements about the application of interval heaps to the complementary range search problem are correct?  
A) Insertion of a point takes O(log n) time  
B) Removing a point given its location takes O(n) time  
C) Reporting all points not in the range [a, b] takes O(k) time, where k is the number of points outside the range  
D) Interval heaps can only store integer points, not real numbers



<br>

## Answers

#### 1. Which of the following operations are supported by a double-ended priority queue but not by a single-ended priority queue?  
A) ✓ Insert is supported by both single-ended and double-ended priority queues.  
B) ✓ Remove Max is supported by double-ended but not necessarily by single-ended priority queues (which support only one remove operation).  
C) ✓ Remove Min is supported by double-ended but not necessarily by single-ended priority queues.  
D) ✗ Arbitrary element removal is not a primary operation of double-ended priority queues, though some implementations support it.  

**Correct:** B, C


#### 2. In a dual single-ended priority queue implementation, what is the primary reason for maintaining pointers between nodes in the min and max priority queues?  
A) ✗ It increases space usage rather than reducing it.  
B) ✓ Enables efficient arbitrary removal by linking corresponding elements in both queues.  
C) ✗ It does not primarily speed up insertion.  
D) ✗ The pointers do not maintain heap order properties but link corresponding elements.  

**Correct:** B


#### 3. When using correspondence-based min and max single-ended priority queues with total correspondence, which of the following statements is true?  
A) ✗ Each element in the min queue corresponds to a greater or equal element, not smaller, in the max queue.  
B) ✓ Correct: each min queue element pairs with a different and greater or equal element in the max queue.  
C) ✗ The buffer does not always contain the largest element; it holds one element when n is odd.  
D) ✗ The buffer is used when n is odd, not even.  

**Correct:** B


#### 4. In an interval heap, which of the following properties hold for the intervals stored at each node?  
A) ✓ Left endpoint ≤ right endpoint by definition of the interval.  
B) ✓ Child intervals are contained within parent intervals, maintaining heap order.  
C) ✓ Root node contains global min (left endpoint) and max (right endpoint).  
D) ✗ Intervals at sibling nodes can overlap; disjointness is not guaranteed.  

**Correct:** A, B, C


#### 5. During insertion into an interval heap, if the new element becomes a right endpoint, what heap property is primarily maintained?  
A) ✗ Left endpoints relate to the min heap property, not right endpoints.  
B) ✓ Right endpoints maintain the max heap property.  
C) ✗ Interval heaps do not maintain binary search tree properties.  
D) ✗ Correspondence between min and max heaps is not the primary concern here.  

**Correct:** B


#### 6. Which of the following correctly describe the process of removing the minimum element from an interval heap when n > 2?  
A) ✓ Remove left endpoint from root node (minimum element).  
B) ✓ Remove left endpoint from last node and reinsert it into min heap starting at root.  
C) ✓ Delete last node if it becomes empty after removal.  
D) ✗ Swapping with right endpoint of root before reinsertion is not part of the standard removal process.  

**Correct:** A, B, C


#### 7. Regarding cache optimization in heap operations, which statements are accurate?  
A) ✓ Insert percolates about 1.6 levels on average.  
B) ✓ Remove min/max causes about log₂ n cache misses on average.  
C) ✗ Root and children are stored in the same cache line to optimize cache usage.  
D) ✓ Using a 4-ary heap reduces heap height compared to binary heap.  

**Correct:** A, B, D


#### 8. For a d-ary heap with degree d, which of the following formulas correctly describe the parent and children indices of node i (1-based indexing)?  
A) ✗ Parent(i) = floor((i - 1)/d) is incorrect; ceil is used.  
B) ✓ Parent(i) = ceil((i - 1)/d) is correct as per lecture.  
C) ✓ Children indices = d*(i - 1) + 2 to min{d*i + 1, n} is correct.  
D) ✗ Children indices are not d*i to d*i + d - 1 in this scheme.  

**Correct:** B, C


#### 9. What are the advantages of using a cache-aligned 4-heap over a standard binary heap?  
A) ✓ Siblings stored in same cache line reduce cache misses.  
B) ✗ Insert percolation levels are about half, not doubled.  
C) ✗ Remove-min requires more comparisons per level (4 vs 2), not fewer.  
D) ✓ Overall speedup of about 1.5 to 1.8 times in heapsort for large data sets.  

**Correct:** A, D


#### 10. Which of the following statements about the application of interval heaps to the complementary range search problem are correct?  
A) ✓ Insertion takes O(log n) time.  
B) ✗ Removing a point given its location takes O(log n), not O(n).  
C) ✓ Reporting points not in [a,b] takes O(k), where k is number outside the range.  
D) ✗ Interval heaps can store any comparable elements, not limited to integers.  

**Correct:** A, C