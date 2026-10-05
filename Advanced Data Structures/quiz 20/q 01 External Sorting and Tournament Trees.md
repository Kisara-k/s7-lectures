## 1. External Sorting and Tournament Trees

## Questions

#### 1. Which of the following are primary concerns when studying advanced data structures for external sorting and related topics?  
A) Worst-case complexity  
B) Best-case complexity  
C) Average complexity  
D) Amortized complexity  

#### 2. External sorting is necessary when:  
A) The dataset is stored on disk and cannot be fully loaded into memory at once.  
B) The entire dataset fits comfortably in main memory.  
C) The number of records n is very large and each record is small.  
D) The number of records n is small but each record is very large.  

#### 3. Which of the following statements about disk characteristics are true?  
A) Seek time is approximately 100,000 arithmetic operations.  
B) Latency time is approximately 25,000 arithmetic operations.  
C) Data access is performed by reading/writing blocks or tracks.  
D) Transfer time is negligible compared to seek and latency times.  

#### 4. In the external adaptation of quick sort, what is the role of the "middle group"?  
A) It stores elements less than the pivot.  
B) It stores elements equal to the pivot.  
C) It buffers elements that cannot be classified immediately.  
D) It stores elements greater than the pivot.  

#### 5. When performing external merge sort, the number of merge passes required to reduce r initial runs to one is:  
A) ceil(log2 r) for binary merging  
B) ceil(logk r) where k is the merge order  
C) Independent of the merge order  
D) Always equal to r - 1  

#### 6. Which of the following improve the efficiency of run generation in external merge sort?  
A) Overlapping input, output, and internal sorting operations  
B) Generating runs longer than the available memory size on average  
C) Increasing the number of initial runs  
D) Using only insertion sort for run generation  

#### 7. What is a disadvantage of increasing the merge order k in external merge sort?  
A) The number of input buffers needed increases linearly with k.  
B) Internal merge time increases exponentially with k.  
C) Block size decreases as k increases, leading to more blocks.  
D) Seek and latency delays per pass increase due to more blocks.  

#### 8. The time complexity to merge n records using a naive k-way merge is:  
A) O(n log k)  
B) O(n log n)  
C) c(k - 1)n, where c is a constant  
D) O(n k log n)  

#### 9. How does using a tournament tree improve the merge time complexity compared to the naive method?  
A) It eliminates the need for comparisons during merging.  
B) It reduces the merge time to O(n log2 k) per pass.  
C) It reduces total merge time to O(n log2 r), where r is the number of runs.  
D) It increases the number of comparisons but reduces I/O time.  

#### 10. In a winner tree (tournament tree), what is stored at each internal node?  
A) The player with the maximum value among its children  
B) The loser of the match between its two children  
C) The sum of the values of its two children  
D) The winner of the match between its two children  

#### 11. What is the time complexity to initialize an n-player winner tree?  
A) O(log n)  
B) O(n log n)  
C) O(1)  
D) O(n)  

#### 12. Which of the following statements about loser trees are true?  
A) They can be used to efficiently implement k-way merging.  
B) The root stores the overall winner.  
C) Loser trees require more memory than winner trees.  
D) Each internal node stores the loser of the match between its children.  

#### 13. The complexity of replaying matches after replacing the winner in a tournament tree is:  
A) O(log n)  
B) O(n log n)  
C) O(1)  
D) O(n)  

#### 14. Which of the following are applications of tournament trees?  
A) k-way merging of runs  
B) Truck loading and bin packing heuristics  
C) Run generation in external sorting  
D) Packet routing and classification  

#### 15. The truck loading problem is equivalent to which classical problem?  
A) Bin packing problem  
B) Shortest path problem  
C) Traveling salesman problem  
D) Minimum spanning tree  

#### 16. Which of the following heuristics for bin packing guarantee that the number of bins used is at most (17/10) times the minimum number of bins plus 2?  
A) Best Fit Decreasing  
B) First Fit  
C) First Fit Decreasing  
D) Best Fit  

#### 17. In the First Fit heuristic for bin packing:  
A) Each item is placed in the leftmost bin where it fits.  
B) Items are sorted in decreasing order before packing.  
C) If no bin fits the item, a new bin is started.  
D) The heuristic always produces an optimal solution.  

#### 18. What is a key difference between First Fit and Best Fit heuristics?  
A) Best Fit packs items into the bin with the least available capacity that can still fit the item.  
B) Best Fit always produces an optimal solution.  
C) First Fit always uses fewer bins than Best Fit.  
D) First Fit sorts items before packing, Best Fit does not.  

#### 19. Which of the following statements about external quick sort adaptation are true?  
A) It sorts the entire dataset in memory before writing to disk.  
B) It requires double-ended priority queues to manage the middle group.  
C) The middle group buffer stores elements that are neither smaller than the minimum nor larger than the maximum of the middle group.  
D) It uses three buffers: input, small, and large.  

#### 20. Regarding the memory model and disk I/O in external sorting, which statements are correct?  
A) Transfer time is the only significant component of disk access time.  
B) Disk I/O time dominates CPU time for sorting large datasets.  
C) Using buffering techniques can reduce I/O wait time.  
D) The number of seek and latency operations increases with the number of blocks accessed.  



<br>

## Answers

#### 1. Which of the following are primary concerns when studying advanced data structures for external sorting and related topics?  
A) ✓ Worst-case complexity is a key concern for algorithm analysis.  
B) ✗ Best-case complexity is less emphasized in this context.  
C) ✓ Average complexity is also important to understand typical performance.  
D) ✓ Amortized complexity is relevant for data structures with operations over time.  

**Correct:** A, C, D


#### 2. External sorting is necessary when:  
A) ✓ True, external sorting is used when data resides on disk and cannot be fully loaded.  
B) ✗ If data fits in memory, external sorting is not needed.  
C) ✓ True, when n is very large and records are small, data cannot fit in memory.  
D) ✓ True, even if n is small but records are large, memory may be insufficient.  

**Correct:** A, C, D


#### 3. Which of the following statements about disk characteristics are true?  
A) ✓ Seek time is roughly 100,000 arithmetic operations, a costly step.  
B) ✓ Latency time is about 25,000 arithmetic operations, significant delay.  
C) ✓ Data access is by blocks or tracks, not individual bytes.  
D) ✗ Transfer time is not negligible; it contributes to total access time.  

**Correct:** A, B, C


#### 4. In the external adaptation of quick sort, what is the role of the "middle group"?  
A) ✗ Left group stores elements less than or equal to pivot, not middle.  
B) ✓ Middle group stores elements equal to the pivot.  
C) ✗ Middle group does not buffer unclassified elements; it holds pivot-equal elements.  
D) ✗ Right group stores elements greater than or equal to pivot, not middle.  

**Correct:** B


#### 5. When performing external merge sort, the number of merge passes required to reduce r initial runs to one is:  
A) ✓ For binary merging, passes = ceil(log2 r).  
B) ✓ For k-way merging, passes = ceil(logk r).  
C) ✗ Number of passes depends on merge order k.  
D) ✗ Number of passes is not r - 1; that would be too many.  

**Correct:** A, B


#### 6. Which of the following improve the efficiency of run generation in external merge sort?  
A) ✓ Overlapping I/O and sorting reduces idle time.  
B) ✓ Generating runs longer than memory size reduces number of runs.  
C) ✗ Increasing number of runs increases merge passes, reducing efficiency.  
D) ✗ Using only insertion sort is inefficient for large runs.  

**Correct:** A, B


#### 7. What is a disadvantage of increasing the merge order k in external merge sort?  
A) ✓ Number of input buffers grows linearly with k, increasing memory needs.  
B) ✗ Internal merge time grows roughly linearly with k, not exponentially.  
C) ✓ Block size decreases as k increases (fixed memory), increasing number of blocks.  
D) ✓ More blocks cause more seek and latency delays per pass.  

**Correct:** A, C, D


#### 8. The time complexity to merge n records using a naive k-way merge is:  
A) ✗ O(n log k) is the complexity using tournament trees, not naive merge.  
B) ✗ O(n log n) is not the typical expression here.  
C) ✓ c(k - 1)n is correct; each record requires about k-1 comparisons.  
D) ✗ O(n k log n) overestimates complexity.  

**Correct:** C


#### 9. How does using a tournament tree improve the merge time complexity compared to the naive method?  
A) ✗ Comparisons are still needed; tournament tree optimizes them but does not eliminate.  
B) ✓ Tournament tree reduces merge time to O(n log2 k) per pass.  
C) ✓ Total merge time reduces to O(n log2 r) due to efficient merging.  
D) ✗ Tournament trees reduce comparisons, not increase them.  

**Correct:** B, C


#### 10. In a winner tree (tournament tree), what is stored at each internal node?  
A) ✗ Internal nodes store winners, not necessarily maximum values unless min or max tree.  
B) ✗ Loser trees store losers, not winner trees.  
C) ✗ Internal nodes do not store sums.  
D) ✓ Winner tree stores the winner of the match at each internal node.  

**Correct:** D


#### 11. What is the time complexity to initialize an n-player winner tree?  
A) ✗ O(log n) is too low; initialization involves all nodes.  
B) ✗ O(n log n) overestimates initialization cost.  
C) ✗ O(1) is too low; initialization is not constant time.  
D) ✓ O(n) since each of the n-1 internal nodes requires a match.  

**Correct:** D


#### 12. Which of the following statements about loser trees are true?  
A) ✓ Loser trees are used for efficient k-way merging.  
B) ✓ The root stores the overall winner in loser trees as well.  
C) ✗ Loser trees do not require more memory than winner trees; memory is similar.  
D) ✓ Loser trees store the loser of each match at internal nodes.  

**Correct:** A, B, D


#### 13. The complexity of replaying matches after replacing the winner in a tournament tree is:  
A) ✓ O(log n) since replay occurs along the path to the root.  
B) ✗ O(n log n) is excessive for this operation.  
C) ✗ O(1) is too low; replay involves traversing tree levels.  
D) ✗ O(n) is too high; only a path is replayed, not entire tree.  

**Correct:** A


#### 14. Which of the following are applications of tournament trees?  
A) ✓ k-way merging is a classic application of tournament trees.  
B) ✓ Truck loading/bin packing heuristics can use tournament trees for selection.  
C) ✓ Run generation uses tournament trees to select minimum elements.  
D) ✗ Packet routing/classification is not a direct application.  

**Correct:** A, B, C


#### 15. The truck loading problem is equivalent to which classical problem?  
A) ✓ Bin packing problem is equivalent to truck loading.  
B) ✗ Shortest path problem is unrelated.  
C) ✗ Traveling salesman problem is unrelated.  
D) ✗ Minimum spanning tree is unrelated.  

**Correct:** A


#### 16. Which of the following heuristics for bin packing guarantee that the number of bins used is at most (17/10) times the minimum number of bins plus 2?  
A) ✗ Best Fit Decreasing has a better bound (11/9).  
B) ✓ First Fit has this performance bound.  
C) ✗ First Fit Decreasing has a better bound (11/9).  
D) ✓ Best Fit also has this bound.  

**Correct:** B, D


#### 17. In the First Fit heuristic for bin packing:  
A) ✓ Each item is placed in the leftmost bin where it fits.  
B) ✗ Items are not sorted before packing in First Fit.  
C) ✓ If no bin fits, a new bin is started.  
D) ✗ First Fit does not guarantee optimal solutions.  

**Correct:** A, C


#### 18. What is a key difference between First Fit and Best Fit heuristics?  
A) ✓ Best Fit packs items into the bin with least available capacity that fits the item.  
B) ✗ Best Fit does not guarantee optimal solutions.  
C) ✗ First Fit does not always use fewer bins than Best Fit; depends on input.  
D) ✗ Neither heuristic sorts items before packing unless combined with decreasing order.  

**Correct:** A


#### 19. Which of the following statements about external quick sort adaptation are true?  
A) ✗ It does not sort entire dataset in memory; sorting is external.  
B) ✓ Double-ended priority queues are used to manage the middle group efficiently.  
C) ✓ Middle group stores elements between middlemin and middlemax.  
D) ✓ Uses three buffers: input, small, and large.  

**Correct:** B, C, D


#### 20. Regarding the memory model and disk I/O in external sorting, which statements are correct?  
A) ✗ Transfer time is only one component; seek and latency are significant too.  
B) ✓ Disk I/O time dominates CPU time for large datasets.  
C) ✓ Buffering techniques reduce I/O wait time by overlapping operations.  
D) ✓ Number of seek and latency operations increases with number of blocks accessed.  

**Correct:** B, C, D