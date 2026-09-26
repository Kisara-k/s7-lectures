## 1. External Sorting and Tournament Trees

## Study Notes

### 1. 📚 Introduction to Advanced Data Structures and Course Overview

This course focuses on advanced data structures that are essential for solving complex problems involving large data sets and specialized operations. The main topics include:

- **External sorting:** Techniques to sort data too large to fit into main memory.
- **Priority queues:** Including single-ended and double-ended variants.
- **Dictionaries:** Efficient data retrieval structures.
- **Multidimensional search:** Searching in data with multiple attributes.
- **Computational geometry:** Algorithms for geometric problems.
- **Image processing:** Data structures for handling images.
- **Packet routing and classification:** Network data handling.

The course emphasizes analyzing algorithms in terms of:

- **Worst-case complexity:** The maximum time or space an algorithm can take.
- **Average complexity:** Expected performance over typical inputs.
- **Amortized complexity:** Average cost per operation over a sequence of operations.

#### Prerequisites

To follow this course, you should be comfortable with:

- **Asymptotic notation:** Big O, Theta, and Omega for describing algorithm efficiency.
- **Basic data structures:** Stacks, queues, linked lists, trees, and graphs.
- **Programming languages:** C++, Java, or Python.


### 2. 💾 External Sorting: Sorting Large Data on Disk

#### What is External Sorting?

External sorting is the process of sorting data that cannot fit entirely into a computer’s main memory (RAM) and must be stored on external storage like disks. This is common when:

- The number of records, **n**, is very large.
- Each record is large in size.
- Or both.

Because the data is too big to load all at once, we cannot simply read all records into memory, sort them, and write them back. Instead, we use specialized algorithms that minimize disk input/output (I/O) operations, which are much slower than memory operations.

#### Why is Disk Access Slow?

Disk access involves several time components:

- **Seek time:** Time to move the disk’s read/write head to the correct track (~100,000 times slower than arithmetic operations).
- **Latency time:** Waiting for the disk to rotate to the correct position (~25,000 times slower).
- **Transfer time:** Time to actually read/write data once positioned.

Because of these delays, external sorting algorithms aim to reduce the number of disk accesses by reading and writing data in large blocks.


### 3. ⚙️ Internal Sorting Methods and Their Adaptation to External Sorting

#### Internal Sorting Recap

Two common internal sorting algorithms are:

- **Quick Sort:** Fast on average, but worst-case can be slow.
- **Merge Sort:** Consistent worst-case performance, good for external sorting.

#### Quick Sort Basics

Quick sort works by:

1. Selecting a **pivot** element.
2. Partitioning the data into three groups:
   - Left group: elements less than or equal to the pivot.
   - Middle group: the pivot itself.
   - Right group: elements greater than or equal to the pivot.
3. Recursively sorting the left and right groups.
4. Combining the sorted groups and the pivot to get the final sorted list.

#### Adapting Quick Sort for External Sorting

Since data is on disk, quick sort uses buffers to minimize disk I/O:

- **Input buffer:** Reads data from disk.
- **Small buffer:** Stores elements smaller than the pivot.
- **Large buffer:** Stores elements larger than the pivot.
- **Middle group:** Keeps elements close to the pivot.

The algorithm reads data into the input buffer, compares each record to the pivot, and places it into the appropriate buffer. When buffers fill up, they are written back to disk. This buffering reduces the number of disk reads and writes.

A **double-ended priority queue** is used to efficiently manage the middle group, allowing quick access to both the smallest and largest elements.


### 4. 🔄 External Merge Sort: A Reliable External Sorting Method

#### Overview

External merge sort is widely used because of its predictable performance. It works in two phases:

1. **Run generation:** Break the large data into smaller chunks (runs), sort each chunk internally, and write the sorted runs back to disk.
2. **Run merging:** Repeatedly merge pairs (or more) of sorted runs until only one sorted run remains.

#### Example Scenario

- Sort 10,000 records.
- Memory can hold 500 records.
- Disk block size is 100 records.

#### Run Generation

- Read 5 blocks (500 records) into memory.
- Sort them internally (e.g., using quick sort).
- Write the sorted run back to disk.
- Repeat 20 times to cover all 10,000 records.

#### Run Merging

- Merge pairs of runs (e.g., merge 20 runs into 10).
- Repeat merging passes until only one run remains.
- Each merge pass reads input buffers from two runs, merges them, and writes the output buffer.

#### Time Analysis

- Each merge pass involves reading and writing all blocks.
- The number of merge passes depends on the number of initial runs and the merge order (how many runs are merged at once).
- Total time includes disk I/O and internal merge time.


### 5. 🏆 Tournament Trees: Efficient Data Structures for Merging and Priority Queues

#### What is a Tournament Tree?

A tournament tree is a complete binary tree used to efficiently find the minimum or maximum element among many. It simulates a tournament where:

- **External nodes:** Represent players (elements).
- **Internal nodes:** Represent matches between two players, storing the winner.
- The root node stores the overall winner (smallest or largest element).

#### Types of Tournament Trees

- **Winner Tree:** Internal nodes store the winner of each match.
- **Loser Tree:** Internal nodes store the loser of each match, which can simplify updates.

#### Operations and Complexity

- **Initialization:** O(n) time to build the tree for n players.
- **Get winner:** O(1) time to access the root.
- **Replace winner and replay:** When the winner is removed or replaced, replay matches along the path to the root in O(log n) time.

#### Application in External Sorting

Tournament trees are used to efficiently merge multiple sorted runs (k-way merging) by always selecting the smallest next element among the runs.


### 6. 🚚 Truck Loading and Bin Packing: Practical Applications of Data Structures

#### Problem Description

- **Truck loading:** Load n packages into trucks, each with capacity c, minimizing the number of trucks.
- **Bin packing:** Pack n items into bins of capacity c, minimizing the number of bins.

These problems are essentially the same. Bin packing is known to be **NP-hard**, meaning no efficient algorithm is known to always find the optimal solution quickly.

#### Heuristics for Bin Packing

Since exact solutions are hard, heuristics are used:

- **First Fit:** Place each item in the first bin it fits into; if none, start a new bin.
- **First Fit Decreasing:** Sort items in decreasing size, then apply First Fit.
- **Best Fit:** Place each item in the bin that leaves the least leftover space after adding the item.
- **Best Fit Decreasing:** Sort items decreasingly, then apply Best Fit.

#### Performance Guarantees

- First Fit and Best Fit use at most about 1.7 times the minimum number of bins plus 2 extra bins.
- First Fit Decreasing and Best Fit Decreasing improve this to about 1.22 times the minimum plus 4 bins.

#### Using Tournament Trees for Bin Packing

Tournament trees can be used to efficiently track bins and their available capacities, helping to quickly find the best bin for each item.


### Summary

This lecture introduced key advanced data structures and algorithms for handling large data sets that cannot fit into memory, focusing on external sorting and tournament trees. We covered:

- The challenges of sorting data on disk and how external sorting algorithms minimize slow disk I/O.
- How internal sorting methods like quick sort and merge sort are adapted for external sorting.
- The detailed process and time analysis of external merge sort.
- Tournament trees as an efficient way to merge multiple sorted sequences and manage priority queues.
- Practical applications like truck loading and bin packing, including heuristic methods and their performance.

Understanding these concepts is crucial for designing efficient algorithms that work with massive data in real-world systems.