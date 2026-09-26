## 3. Double-Ended Priority Queues and Interval Heaps

## Study Notes

### 1. 🔄 Introduction to Double-Ended Priority Queues

A **double-ended priority queue** is a special kind of data structure that allows you to efficiently access and remove both the smallest and largest elements. This is different from a regular (single-ended) priority queue, which only supports removing either the minimum or the maximum element, but not both.

#### Key Operations
- **Insert:** Add a new element to the queue.
- **Remove Min:** Remove the smallest element.
- **Remove Max:** Remove the largest element.

These operations are fundamental because they allow flexible priority management from both ends of the data set.


### 2. 🔗 Dual Single-Ended Priority Queues and Correspondence Structures

One way to implement a double-ended priority queue is by combining two single-ended priority queues: one that supports removing the minimum element (a min-heap) and one that supports removing the maximum element (a max-heap).

#### Dual Single-Ended Priority Queues
- Each element exists in both the min and max priority queues.
- To keep track of the same element in both queues, each node has a pointer linking it to its counterpart in the other queue.
- This allows operations like removing an arbitrary element efficiently because you can find and remove it from both queues.
- However, this approach doubles the space usage (2n nodes for n elements) and increases operation costs compared to a single heap.

#### Correspondence-Based Structures
- Instead of duplicating all elements, the elements are split between the min and max queues.
- For example, if there are n elements, about half (n/2) go into the min queue and the other half into the max queue.
- When n is odd, one element is kept in a buffer.
- Correspondence between elements in the min and max queues is established, either totally (each element in min queue paired with a larger or equal element in max queue) or partially (leaf correspondence).
- This method reduces space but requires careful management of the correspondence during insertions and removals.


### 3. 🏠 Interval Heaps: A Specialized Double-Ended Priority Queue

An **interval heap** is a more advanced and efficient data structure designed specifically for double-ended priority queues.

#### Structure of Interval Heaps
- It is a **complete binary tree**, meaning all levels are fully filled except possibly the last.
- Each node contains **two elements**, except possibly the last node, which may have one or two.
- The two elements in a node form an **interval** [a, b], where a ≤ b.
- If a node has only one element a, its interval is [a, a].
- The key property: the interval of any child node is contained within the interval of its parent node. This means the child's interval is always between the parent's minimum and maximum values.

#### How Interval Heaps Work
- The **left endpoints** of intervals form a min-heap.
- The **right endpoints** form a max-heap.
- This dual heap property allows quick access to both the minimum and maximum elements, which are always found in the root node.
- The interval heap is typically stored as an array for efficient indexing, similar to binary heaps.


### 4. ➕ Inserting Elements into Interval Heaps

When inserting a new element into an interval heap, the process depends on whether the element becomes a left or right endpoint of an interval.

- If the new element is smaller, it becomes a left endpoint and is inserted into the min-heap part.
- If larger, it becomes a right endpoint and is inserted into the max-heap part.
- Sometimes, the new element can become both endpoints if it forms a single-element interval.
- The insertion process involves percolating the element up the appropriate heap (min or max) to maintain heap properties.

This approach ensures that the interval heap remains balanced and maintains its ordering properties.


### 5. ❌ Removing the Minimum Element from Interval Heaps

Removing the minimum element (the left endpoint of the root interval) is more complex than in a simple heap:

- If the heap is empty (n=0), removal fails.
- If there is only one element (n=1), removing it empties the heap.
- If there are two elements (n=2), removing the left endpoint leaves the right endpoint as the only element.
- For larger heaps (n > 2), the process involves:
  - Removing the left endpoint from the root.
  - Removing the left endpoint from the last node.
  - Reinserting the last node’s left endpoint into the min-heap starting at the root.
  - If the last node becomes empty, it is deleted.
  - Swapping with the right endpoint if necessary to maintain the interval property.

This ensures the heap remains valid and balanced after removal.


### 6. ⚙️ Initialization and Maintenance of Interval Heaps

When building or rebalancing an interval heap:

- Nodes are examined from the bottom up.
- If the two elements in a node are out of order (left endpoint greater than right endpoint), they are swapped.
- The right endpoint is reinserted into the max-heap.
- The left endpoint is reinserted into the min-heap.

This bottom-up approach ensures the heap properties are restored efficiently.


### 7. 💾 Cache Optimization and d-ary Heaps

#### Cache Optimization
- Modern processors use caches to speed up memory access.
- A cache line typically holds multiple elements (e.g., 32 bytes can hold 4 nodes of 8 bytes each).
- Heap operations cause cache misses when accessing nodes at different levels.
- On average, insertions percolate up about 1.6 levels.
- Remove-min or remove-max operations percolate down about height - 1 levels.
- Optimizing cache usage can significantly improve performance.

#### d-ary Heaps
- A **d-ary heap** generalizes binary heaps by allowing each node to have d children instead of 2.
- For example, a 4-ary heap has 4 children per node.
- This reduces the height of the heap (log base d of n), which can reduce the number of levels traversed during operations.
- However, each level requires more comparisons (e.g., 4 comparisons per level in a 4-ary heap).
- Cache alignment can be improved by arranging nodes so siblings fit within the same cache line, reducing cache misses.

#### Performance
- Using a 4-ary heap can speed up operations by about 1.5 to 1.8 times compared to a binary heap.
- For interval heaps, using a 4-ary structure instead of binary is recommended for better cache performance.


### 8. 📊 Applications of Interval Heaps

Interval heaps are particularly useful in problems where you need to efficiently manage ranges or intervals, such as:

- **Complementary range search:** Given a collection of 1D points (numbers), you want to:
  - Insert a point in O(log n) time.
  - Remove a point given its location in O(log n) time.
  - Report all points **not** in a given range [a, b] in O(k) time, where k is the number of points outside the range.

This makes interval heaps valuable in computational geometry, databases, and other areas where range queries and dynamic updates are common.


### Summary

Double-ended priority queues extend the functionality of regular priority queues by allowing efficient access to both minimum and maximum elements. They can be implemented by combining two single-ended priority queues or by using specialized structures like interval heaps. Interval heaps are particularly elegant because they store intervals in each node, maintaining min-heap and max-heap properties simultaneously. Optimizations such as cache alignment and d-ary heaps improve performance, making these structures practical for large-scale applications involving dynamic range queries.