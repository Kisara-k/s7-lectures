## 1. External Sorting and Tournament Trees

## Questions

#### 1. Which of the following statements correctly describe the characteristics and challenges of external sorting?  
A) External sorting methods rely solely on internal sorting algorithms without any buffering.  
B) Disk seek time is significantly more expensive than arithmetic operations.  
C) External sorting primarily focuses on minimizing CPU arithmetic operations.  
D) External sorting is used when the data size is too large to fit into main memory.  

#### 2. In the external adaptation of quick sort, what roles do the input, small, and large buffers play?  
A) The large buffer stores records greater than or equal to the pivot.  
B) The input buffer reads records from disk.  
C) The small buffer stores records less than or equal to the pivot.  
D) The middle group buffer is used to store records that are equal to the pivot only.  

#### 3. Regarding external merge sort, which of the following are true about run generation and run merging phases?  
A) Run merging merges runs pairwise until only one run remains.  
B) Run merging is always faster than run generation.  
C) The number of merge passes depends on the number of initial runs and the merge order.  
D) Run generation creates initial sorted sequences called runs.  

#### 4. When merging 20 runs using a 5-way merge, which of the following statements are correct?  
A) Increasing the merge order k always decreases the total I/O time.  
B) Increasing k reduces the number of merge passes but may increase seek and latency delays.  
C) The number of merge passes is 2.  
D) The block size per buffer increases as the merge order k increases.  

#### 5. What are the time complexities associated with initializing and updating a winner tree with n players?  
A) The height of the winner tree is proportional to n.  
B) Initializing the winner tree takes O(n) time.  
C) Replacing the winner and replaying matches takes Θ(log n) time.  
D) Getting the winner from the tree takes O(log n) time.  

#### 6. Which of the following correctly describe the difference between winner trees and loser trees?  
A) Both trees have the same asymptotic complexity for initialization and replay.  
B) Loser trees store the loser of each match at internal nodes.  
C) Loser trees require more time to replay matches than winner trees.  
D) Winner trees store the winner of each match at internal nodes.  

#### 7. In the context of bin packing heuristics, which statements are true?  
A) The heuristic bins used by First Fit and Best Fit are always less than or equal to the minimum number of bins.  
B) First Fit packs items into the leftmost bin where they fit, without sorting items first.  
C) Best Fit Decreasing sorts items in increasing order before packing.  
D) First Fit Decreasing sorts items in decreasing order before applying First Fit.  

#### 8. Considering the performance bounds of bin packing heuristics, which of the following are correct?  
A) Best Fit heuristic always produces fewer bins than First Fit heuristic.  
B) The performance bounds imply that heuristics can sometimes use more bins than the optimal solution.  
C) First Fit and Best Fit heuristics guarantee heuristic bins ≤ (17/10) * minimum bins + 2.  
D) First Fit Decreasing and Best Fit Decreasing heuristics guarantee heuristic bins ≤ (11/9) * minimum bins + 4.  

#### 9. Which of the following statements about the time to merge n records using tournament trees are correct?  
A) Total merge time using a tournament tree for r runs is proportional to n log₂ r.  
B) Tournament trees increase the number of comparisons compared to naive merging.  
C) Using a naive merge requires (k - 1) comparisons per record for k-way merging.  
D) Using a tournament tree reduces the merge time to O(n log₂ k).  

#### 10. Which of the following are true about improving run generation and run merging in external sorting?  
A) Generating runs longer than memory size reduces the number of initial runs.  
B) Overlapping input, output, and internal sorting/merging can improve overall run time.  
C) Using additional buffers can reduce I/O wait time during external quick sort adaptation.  
D) Increasing the merge order k indefinitely always improves total merge time.  



<br>

## Answers

#### 1. Which of the following statements correctly describe the characteristics and challenges of external sorting?  
A) ✗ Buffering is essential in external sorting to reduce I/O overhead; it does not rely solely on internal sorting.  
B) ✓ Disk seek time is much more expensive than arithmetic operations, making I/O optimization critical.  
C) ✗ External sorting focuses more on minimizing disk I/O than CPU arithmetic operations.  
D) ✓ External sorting is used when data size exceeds main memory capacity.  

**Correct:** B, D


#### 2. In the external adaptation of quick sort, what roles do the input, small, and large buffers play?  
A) ✓ The large buffer stores records greater than or equal to the pivot (middlemax).  
B) ✓ The input buffer reads records from disk into memory.  
C) ✓ The small buffer stores records less than or equal to the pivot (middlemin).  
D) ✗ The middle group buffer stores records within the pivot range, not only equal to the pivot element.  

**Correct:** A, B, C


#### 3. Regarding external merge sort, which of the following are true about run generation and run merging phases?  
A) ✓ Run merging merges runs pairwise until only one run remains.  
B) ✗ Run merging is not always faster; it depends on data size and I/O costs.  
C) ✓ Number of merge passes depends on initial runs and merge order k.  
D) ✓ Run generation creates initial sorted sequences called runs.  

**Correct:** A, C, D


#### 4. When merging 20 runs using a 5-way merge, which of the following statements are correct?  
A) ✗ Increasing k reduces passes but can increase I/O overhead due to smaller block sizes and more seeks.  
B) ✓ Increasing k reduces passes but may increase seek and latency delays due to more buffers and smaller blocks.  
C) ✓ Number of merge passes is 2 because ceil(log₅(20)) = 2.  
D) ✗ Block size per buffer decreases as k increases (fixed memory divided among more buffers).  

**Correct:** B, C


#### 5. What are the time complexities associated with initializing and updating a winner tree with n players?  
A) ✗ Height of the winner tree is O(log n), not proportional to n.  
B) ✓ Initializing takes O(n) time because each of the n-1 matches is played once.  
C) ✓ Replacing the winner and replaying matches takes Θ(log n) time due to path from leaf to root.  
D) ✗ Getting the winner is O(1) time, not O(log n).  

**Correct:** B, C


#### 6. Which of the following correctly describe the difference between winner trees and loser trees?  
A) ✓ Both have the same asymptotic complexity for initialization and replay.  
B) ✓ Loser trees store the loser of each match at internal nodes.  
C) ✗ Loser trees do not require more time to replay matches; both have Θ(log n) replay complexity.  
D) ✓ Winner trees store the winner of each match at internal nodes.  

**Correct:** A, B, D


#### 7. In the context of bin packing heuristics, which statements are true?  
A) ✗ Heuristic bins can exceed the minimum number of bins; heuristics do not guarantee optimality.  
B) ✓ First Fit packs items in given order into the leftmost bin where they fit, without sorting.  
C) ✗ Best Fit Decreasing sorts items in decreasing order, not increasing order.  
D) ✓ First Fit Decreasing sorts items in decreasing order before applying First Fit.  

**Correct:** B, D


#### 8. Considering the performance bounds of bin packing heuristics, which of the following are correct?  
A) ✗ Best Fit does not always produce fewer bins than First Fit; performance depends on input order.  
B) ✓ The bounds imply heuristics can use more bins than the optimal solution.  
C) ✓ First Fit and Best Fit heuristics have the bound: heuristic bins ≤ (17/10) * minimum bins + 2.  
D) ✓ First Fit Decreasing and Best Fit Decreasing heuristics have the tighter bound: heuristic bins ≤ (11/9) * minimum bins + 4.  

**Correct:** B, C, D


#### 9. Which of the following statements about the time to merge n records using tournament trees are correct?  
A) ✓ Total merge time using tournament trees for r runs is proportional to n log₂ r.  
B) ✗ Tournament trees reduce the number of comparisons compared to naive merging, not increase.  
C) ✓ Naive merge requires (k - 1) comparisons per record for k-way merging.  
D) ✓ Tournament trees reduce merge time to O(n log₂ k) by organizing comparisons efficiently.  

**Correct:** A, C, D


#### 10. Which of the following are true about improving run generation and run merging in external sorting?  
A) ✓ Generating runs longer than memory size reduces the number of initial runs, improving efficiency.  
B) ✓ Overlapping input, output, and internal sorting/merging improves overall run time by parallelizing I/O and computation.  
C) ✓ Using additional buffers reduces I/O wait time during external quick sort adaptation.  
D) ✗ Increasing merge order k indefinitely does not always improve total merge time due to increased I/O overhead.  

**Correct:** A, B, C