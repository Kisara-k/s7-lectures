## 1. External Sorting and Tournament Trees

## Key Points

#### 1. 💾 External Sorting  
- External sorting is used when data is too large to fit into main memory.  
- Disk access times include seek time (~100,000 arithmetic operations), latency (~25,000 arithmetic operations), and transfer time.  
- External sorting algorithms minimize disk I/O by reading/writing data in blocks.  

#### 2. ⚙️ Internal Sorting Methods  
- Quick sort has the best average runtime but poor worst-case performance.  
- Merge sort has the best worst-case runtime and is stable.  
- Quick sort partitions data into left (≤ pivot), middle (= pivot), and right (≥ pivot) groups recursively.  

#### 3. 🔄 External Quick Sort Adaptation  
- Uses three buffers: input, small, and large, plus a middle group buffer.  
- Records ≤ middle group minimum go to small buffer; ≥ middle group maximum go to large buffer; others replace min/max in middle group.  
- Double-ended priority queues manage the middle group efficiently.  

#### 4. 🔀 External Merge Sort  
- Two phases: run generation (create sorted runs) and run merging (merge runs until one remains).  
- Run generation sorts chunks of data that fit into memory and writes sorted runs to disk.  
- Run merging merges pairs of runs repeatedly; number of passes = ceil(log₂(number of runs)).  
- Total merge pass time = 200t_IO + 100t_IM (t_IO = time to read/write one block, t_IM = time to merge one block).  

#### 5. 🏆 Tournament Trees  
- Complete binary tree with n external nodes (players) and n-1 internal nodes (matches).  
- Internal nodes store winners (winner tree) or losers (loser tree) of matches.  
- Initialization time: O(n).  
- Get winner time: O(1).  
- Replace winner and replay matches time: Θ(log n).  
- Used for k-way merging in external merge sort.  

#### 6. 🚚 Truck Loading and Bin Packing  
- Truck loading = bin packing problem; both aim to minimize number of bins/trucks used.  
- Bin packing is NP-hard.  
- Heuristics:  
  - First Fit: place item in first bin it fits.  
  - First Fit Decreasing: sort items decreasingly, then apply First Fit.  
  - Best Fit: place item in bin with least leftover space after placement.  
  - Best Fit Decreasing: sort items decreasingly, then apply Best Fit.  
- Performance bounds:  
  - First Fit and Best Fit ≤ (17/10) * minimum bins + 2.  
  - First Fit Decreasing and Best Fit Decreasing ≤ (11/9) * minimum bins + 4.  

#### 7. 📊 Merge Pass and Complexity  
- Number of merge passes depends on merge order k: passes = ceil(log_k(number of runs)).  
- Increasing merge order k reduces passes but increases I/O overhead due to smaller block sizes and more seeks.  
- Merge time per pass using tournament tree: dn log₂ k (d is constant).  
- Total merge time: dn log₂ r (r = number of initial runs).



<br>

