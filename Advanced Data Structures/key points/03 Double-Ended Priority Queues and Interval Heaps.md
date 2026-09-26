## 3. Double-Ended Priority Queues and Interval Heaps

## Key Points

#### 1. 🔄 Double-Ended Priority Queues (DEPQ)
- Support three primary operations: Insert, Remove Min, Remove Max.
- Single-ended priority queues support only one remove operation (either min or max).
- DEPQs can be implemented using dual min and max single-ended priority queues or specialized structures like interval heaps.

#### 2. 🔗 Dual Single-Ended Priority Queues
- Each element exists in both a min and a max single-ended priority queue.
- Each node has a pointer to its counterpart node in the other queue.
- Requires space for 2n nodes for n elements.
- Operation costs are more than doubled compared to a single heap.

#### 3. 🔄 Correspondence-Based Min-Max Queues
- Use two single-ended priority queues each holding about n/2 elements.
- When n is odd, one element is stored in a buffer.
- Correspondence between min and max queues can be total (each min element paired with a larger or equal max element) or leaf-based.
- Insertions involve placing smaller element in min queue and larger in max queue, establishing correspondence.

#### 4. 🏠 Interval Heaps Structure
- Complete binary tree where each node contains two elements forming an interval [a, b] with a ≤ b.
- The interval of each child node is contained within the interval of its parent.
- Left endpoints form a min-heap; right endpoints form a max-heap.
- Minimum and maximum elements are always in the root node.
- Stored as an array with height approximately log₂ n.

#### 5. ➕ Interval Heap Insertion
- New element becomes either a left endpoint (min heap) or right endpoint (max heap).
- Inserted by percolating up in the respective heap to maintain heap properties.

#### 6. ❌ Interval Heap Remove Min Operation
- If n=0, removal fails; if n=1, heap becomes empty.
- For n=2, remove left endpoint from the only node.
- For n>2, remove left endpoint from root and last node, reinsert last node’s left endpoint starting at root, delete last node if empty, swap with right endpoint if needed.

#### 7. ⚙️ Interval Heap Initialization
- Nodes examined bottom-up.
- Swap endpoints if left endpoint > right endpoint.
- Reinsert right endpoint into max heap and left endpoint into min heap.

#### 8. 💾 Cache Optimization in Heaps
- L1 cache line size is 32 bytes; each heap node is 8 bytes.
- 4 nodes fit per cache line.
- Remove min/max operations cause ~log₂ n cache misses on average.
- Cache-aligned arrays improve cache utilization.

#### 9. 🌳 d-ary Heaps
- Complete tree with degree d (e.g., d=4).
- Parent(i) = ceil((i-1)/d); children indices from d*(i-1)+2 to min(d*i+1, n).
- Height is log_d n; 4-ary heap height is half that of binary heap.
- Insert moves up about 1.6 levels on average.
- Remove-min does more comparisons per level but fewer levels overall.
- Cache-aligned 4-heap reduces cache misses to ~log₄ n.

#### 10. 📊 Interval Heap Applications
- Efficient for complementary range search problems.
- Insert point in O(log n).
- Remove point by location in O(log n).
- Report points not in range [a, b] in O(k), where k is number of points outside the range.



<br>

