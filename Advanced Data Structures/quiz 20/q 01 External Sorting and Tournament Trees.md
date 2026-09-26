## 1. External Sorting and Tournament Trees

## Questions

#### 1. Which of the following are primary concerns when studying advanced data structures for external sorting and related topics?  
A) Worst-case complexity  
B) Average complexity  
C) Amortized complexity  
D) Best-case complexity  

#### 2. External sorting is necessary when:  
A) The number of records n is very large and each record is small.  
B) The number of records n is small but each record is very large.  
C) The entire dataset fits comfortably in main memory.  
D) The dataset is stored on disk and cannot be fully loaded into memory at once.  

#### 3. Which of the following statements about disk characteristics are true?  
A) Seek time is approximately 100,000 arithmetic operations.  
B) Latency time is approximately 25,000 arithmetic operations.  
C) Transfer time is negligible compared to seek and latency times.  
D) Data access is performed by reading/writing blocks or tracks.  

#### 4. In the external adaptation of quick sort, what is the role of the "middle group"?  
A) It stores elements equal to the pivot.  
B) It stores elements less than the pivot.  
C) It stores elements greater than the pivot.  
D) It buffers elements that cannot be classified immediately.  

#### 5. When performing external merge sort, the number of merge passes required to reduce r initial runs to one is:  
A) ceil(log2 r) for binary merging  
B) ceil(logk r) where k is the merge order  
C) Always equal to r - 1  
D) Independent of the merge order  

#### 6. Which of the following improve the efficiency of run generation in external merge sort?  
A) Overlapping input, output, and internal sorting operations  
B) Generating runs longer than the available memory size on average  
C) Using only insertion sort for run generation  
D) Increasing the number of initial runs  

#### 7. What is a disadvantage of increasing the merge order k in external merge sort?  
A) The number of input buffers needed increases linearly with k.  
B) Block size decreases as k increases, leading to more blocks.  
C) Seek and latency delays per pass increase due to more blocks.  
D) Internal merge time increases exponentially with k.  

#### 8. The time complexity to merge n records using a naive k-way merge is:  
A) O(n log n)  
B) c(k - 1)n, where c is a constant  
C) O(n k log n)  
D) O(n log k)  

#### 9. How does using a tournament tree improve the merge time complexity compared to the naive method?  
A) It reduces the merge time to O(n log2 k) per pass.  
B) It eliminates the need for comparisons during merging.  
C) It reduces total merge time to O(n log2 r), where r is the number of runs.  
D) It increases the number of comparisons but reduces I/O time.  

#### 10. In a winner tree (tournament tree), what is stored at each internal node?  
A) The loser of the match between its two children  
B) The winner of the match between its two children  
C) The sum of the values of its two children  
D) The player with the maximum value among its children  

#### 11. What is the time complexity to initialize an n-player winner tree?  
A) O(log n)  
B) O(n)  
C) O(n log n)  
D) O(1)  

#### 12. Which of the following statements about loser trees are true?  
A) Each internal node stores the loser of the match between its children.  
B) The root stores the overall winner.  
C) Loser trees require more memory than winner trees.  
D) They can be used to efficiently implement k-way merging.  

#### 13. The complexity of replaying matches after replacing the winner in a tournament tree is:  
A) O(1)  
B) O(log n)  
C) O(n)  
D) O(n log n)  

#### 14. Which of the following are applications of tournament trees?  
A) Run generation in external sorting  
B) k-way merging of runs  
C) Packet routing and classification  
D) Truck loading and bin packing heuristics  

#### 15. The truck loading problem is equivalent to which classical problem?  
A) Traveling salesman problem  
B) Bin packing problem  
C) Minimum spanning tree  
D) Shortest path problem  

#### 16. Which of the following heuristics for bin packing guarantee that the number of bins used is at most (17/10) times the minimum number of bins plus 2?  
A) First Fit  
B) Best Fit  
C) First Fit Decreasing  
D) Best Fit Decreasing  

#### 17. In the First Fit heuristic for bin packing:  
A) Items are sorted in decreasing order before packing.  
B) Each item is placed in the leftmost bin where it fits.  
C) If no bin fits the item, a new bin is started.  
D) The heuristic always produces an optimal solution.  

#### 18. What is a key difference between First Fit and Best Fit heuristics?  
A) Best Fit packs items into the bin with the least available capacity that can still fit the item.  
B) First Fit sorts items before packing, Best Fit does not.  
C) First Fit always uses fewer bins than Best Fit.  
D) Best Fit always produces an optimal solution.  

#### 19. Which of the following statements about external quick sort adaptation are true?  
A) It uses three buffers: input, small, and large.  
B) The middle group buffer stores elements that are neither smaller than the minimum nor larger than the maximum of the middle group.  
C) It requires double-ended priority queues to manage the middle group.  
D) It sorts the entire dataset in memory before writing to disk.  

#### 20. Regarding the memory model and disk I/O in external sorting, which statements are correct?  
A) Disk I/O time dominates CPU time for sorting large datasets.  
B) Using buffering techniques can reduce I/O wait time.  
C) Transfer time is the only significant component of disk access time.  
D) The number of seek and latency operations increases with the number of blocks accessed.



<br>

## Answers

#### 1. Which of the following are primary concerns when studying advanced data structures for external sorting and related topics?  
A) ✓ Worst-case complexity is a key concern for algorithm analysis.  
B) ✓ Average complexity is also important to understand typical performance.  
C) ✓ Amortized complexity is relevant for data structures with operations over time.  
D) ✗ Best-case complexity is less emphasized in this context.  

**Correct:** A,B,C


#### 2. External sorting is necessary when:  
A) ✓ True, when n is very large and records are small, data cannot fit in memory.  
B) ✓ True, even if n is small but records are large, memory may be insufficient.  
C) ✗ If data fits in memory, external sorting is not needed.  
D) ✓ True, external sorting is used when data resides on disk and cannot be fully loaded.  

**Correct:** A,B,D


#### 3. Which of the following statements about disk characteristics are true?  
A) ✓ Seek time is roughly 100,000 arithmetic operations, a costly step.  
B) ✓ Latency time is about 25,000 arithmetic operations, significant delay.  
C) ✗ Transfer time is not negligible; it contributes to total access time.  
D) ✓ Data access is by blocks or tracks, not individual bytes.  

**Correct:** A,B,D


#### 4. In the external adaptation of quick sort, what is the role of the "middle group"?  
A) ✓ Middle group stores elements equal to the pivot.  
B) ✗ Left group stores elements less than or equal to pivot, not middle.  
C) ✗ Right group stores elements greater than or equal to pivot, not middle.  
D) ✗ Middle group does not buffer unclassified elements; it holds pivot-equal elements.  

**Correct:** A


#### 5. When performing external merge sort, the number of merge passes required to reduce r initial runs to one is:  
A) ✓ For binary merging, passes = ceil(log2 r).  
B) ✓ For k-way merging, passes = ceil(logk r).  
C) ✗ Number of passes is not r - 1; that would be too many.  
D) ✗ Number of passes depends on merge order k.  

**Correct:** A,B


#### 6. Which of the following improve the efficiency of run generation in external merge sort?  
A) ✓ Overlapping I/O and sorting reduces idle time.  
B) ✓ Generating runs longer than memory size reduces number of runs.  
C) ✗ Using only insertion sort is inefficient for large runs.  
D) ✗ Increasing number of runs increases merge passes, reducing efficiency.  

**Correct:** A,B


#### 7. What is a disadvantage of increasing the merge order k in external merge sort?  
A) ✓ Number of input buffers grows linearly with k, increasing memory needs.  
B) ✓ Block size decreases as k increases (fixed memory), increasing number of blocks.  
C) ✓ More blocks cause more seek and latency delays per pass.  
D) ✗ Internal merge time grows roughly linearly with k, not exponentially.  

**Correct:** A,B,C


#### 8. The time complexity to merge n records using a naive k-way merge is:  
A) ✗ O(n log n) is not the typical expression here.  
B) ✓ c(k - 1)n is correct; each record requires about k-1 comparisons.  
C) ✗ O(n k log n) overestimates complexity.  
D) ✗ O(n log k) is the complexity using tournament trees, not naive merge.  

**Correct:** B


#### 9. How does using a tournament tree improve the merge time complexity compared to the naive method?  
A) ✓ Tournament tree reduces merge time to O(n log2 k) per pass.  
B) ✗ Comparisons are still needed; tournament tree optimizes them but does not eliminate.  
C) ✓ Total merge time reduces to O(n log2 r) due to efficient merging.  
D) ✗ Tournament trees reduce comparisons, not increase them.  

**Correct:** A,C


#### 10. In a winner tree (tournament tree), what is stored at each internal node?  
A) ✗ Loser trees store losers, not winner trees.  
B) ✓ Winner tree stores the winner of the match at each internal node.  
C) ✗ Internal nodes do not store sums.  
D) ✗ Internal nodes store winners, not necessarily maximum values unless min or max tree.  

**Correct:** B


#### 11. What is the time complexity to initialize an n-player winner tree?  
A) ✗ O(log n) is too low; initialization involves all nodes.  
B) ✓ O(n) since each of the n-1 internal nodes requires a match.  
C) ✗ O(n log n) overestimates initialization cost.  
D) ✗ O(1) is too low; initialization is not constant time.  

**Correct:** B


#### 12. Which of the following statements about loser trees are true?  
A) ✓ Loser trees store the loser of each match at internal nodes.  
B) ✓ The root stores the overall winner in loser trees as well.  
C) ✗ Loser trees do not require more memory than winner trees; memory is similar.  
D) ✓ Loser trees are used for efficient k-way merging.  

**Correct:** A,B,D


#### 13. The complexity of replaying matches after replacing the winner in a tournament tree is:  
A) ✗ O(1) is too low; replay involves traversing tree levels.  
B) ✓ O(log n) since replay occurs along the path to the root.  
C) ✗ O(n) is too high; only a path is replayed, not entire tree.  
D) ✗ O(n log n) is excessive for this operation.  

**Correct:** B


#### 14. Which of the following are applications of tournament trees?  
A) ✓ Run generation uses tournament trees to select minimum elements.  
B) ✓ k-way merging is a classic application of tournament trees.  
C) ✗ Packet routing/classification is not a direct application.  
D) ✓ Truck loading/bin packing heuristics can use tournament trees for selection.  

**Correct:** A,B,D


#### 15. The truck loading problem is equivalent to which classical problem?  
A) ✗ Traveling salesman problem is unrelated.  
B) ✓ Bin packing problem is equivalent to truck loading.  
C) ✗ Minimum spanning tree is unrelated.  
D) ✗ Shortest path problem is unrelated.  

**Correct:** B


#### 16. Which of the following heuristics for bin packing guarantee that the number of bins used is at most (17/10) times the minimum number of bins plus 2?  
A) ✓ First Fit has this performance bound.  
B) ✓ Best Fit also has this bound.  
C) ✗ First Fit Decreasing has a better bound (11/9).  
D) ✗ Best Fit Decreasing has a better bound (11/9).  

**Correct:** A,B


#### 17. In the First Fit heuristic for bin packing:  
A) ✗ Items are not sorted before packing in First Fit.  
B) ✓ Each item is placed in the leftmost bin where it fits.  
C) ✓ If no bin fits, a new bin is started.  
D) ✗ First Fit does not guarantee optimal solutions.  

**Correct:** B,C


#### 18. What is a key difference between First Fit and Best Fit heuristics?  
A) ✓ Best Fit packs items into the bin with least available capacity that fits the item.  
B) ✗ Neither heuristic sorts items before packing unless combined with decreasing order.  
C) ✗ First Fit does not always use fewer bins than Best Fit; depends on input.  
D) ✗ Best Fit does not guarantee optimal solutions.  

**Correct:** A


#### 19. Which of the following statements about external quick sort adaptation are true?  
A) ✓ Uses three buffers: input, small, and large.  
B) ✓ Middle group stores elements between middlemin and middlemax.  
C) ✓ Double-ended priority queues are used to manage the middle group efficiently.  
D) ✗ It does not sort entire dataset in memory; sorting is external.  

**Correct:** A,B,C


#### 20. Regarding the memory model and disk I/O in external sorting, which statements are correct?  
A) ✓ Disk I/O time dominates CPU time for large datasets.  
B) ✓ Buffering techniques reduce I/O wait time by overlapping operations.  
C) ✗ Transfer time is only one component; seek and latency are significant too.  
D) ✓ Number of seek and latency operations increases with number of blocks accessed.  

**Correct:** A,B,D