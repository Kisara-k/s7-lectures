## 2. Run Generation, Optimal Merging, and Huffman Trees

## Study Notes

### 1. 🏃 Run Generation: Improving Efficiency and Reducing Runs

When dealing with large datasets that don't fit entirely in memory, sorting is often done externally—meaning data is read from disk, processed in memory, and written back to disk in sorted chunks called **runs**. The goal in run generation is to create as few runs as possible, each as long as possible, because fewer runs mean less work during the merging phase.

#### Why Improve Run Generation?

- **Overlap work:** Ideally, while the CPU processes data, the system should simultaneously read new data from disk and write sorted runs back to disk. This overlapping of input, output, and CPU work improves overall throughput.
- **Reduce number of runs:** Longer runs mean fewer runs to merge later, which reduces total sorting time.

#### New Strategy: Using Multiple Buffers and a Loser Tree

- Use **2 input buffers** and **2 output buffers** to allow overlapping of reading and writing.
- The rest of the available memory is used to maintain a **min loser tree** data structure.

#### What is a Loser Tree?

A **loser tree** is a specialized tournament tree used to efficiently find the smallest element among multiple sorted sequences (or runs). It helps in merging runs by quickly identifying the next smallest element to output.

- If there are **k external nodes** (i.e., runs) in the loser tree, the **minimum run size generated is at least k**.
- If the input is already sorted, only **1 run** is generated.
- If the input is sorted in reverse, the number of runs can be as high as **n/k** (where n is total elements).
- On average, the run size is about **2k**.
- The internal processing time for run generation using a loser tree is **O(n log k)**, where n is the number of elements and k is the number of runs.


### 2. 🔀 Merging Runs of Different Lengths: Optimal Merging and Weighted External Path Length (WEPL)

After generating runs, the next step is to merge them into a fully sorted sequence. However, runs can be of different lengths, and merging them optimally can save time.

#### What is Weighted External Path Length (WEPL)?

WEPL is a measure used to evaluate the cost of merging runs or decoding messages. It is calculated as:


$$
\text{WEPL}(t) = \sum_{i} \text{weight of external node } i \times \text{distance of node } i \text{ from root}
$$


- The **weight** corresponds to the size or frequency of the run/message.
- The **distance** is the number of edges from the root to the external node in the tree.

Minimizing WEPL means minimizing the total cost of merging or decoding.

#### Example of WEPL Calculation

- Suppose we have external nodes with weights 4, 3, 6, and 9.
- If all nodes are at distance 2 from the root, WEPL = $4*2 + 3*2 + 6*2 + 9*2 = 44$.
- If nodes are at different distances, say 3, 3, 2, and 1, WEPL = $4*3 + 3*3 + 6*2 + 9*1 = 39$, which is better (lower cost).


### 3. 📡 Message Coding and Decoding: Connection to WEPL

The concept of WEPL also applies to **message coding and decoding**, especially in lossless data compression.

#### Scenario

- You have a fixed set of messages $M_0, M_1, ..., M_{n-1}$.
- Each message $M_i$ has a known frequency $f_i$.
- Both sender and receiver know the messages and their codes.
- The goal is to assign codes to messages to minimize the total transmission and decoding cost.

#### How Does WEPL Relate?

- Each message corresponds to an external node in a binary tree.
- The code length for a message corresponds to the distance of the node from the root.
- The total cost (transmission + decoding) equals the WEPL of the tree representing the code.

#### Example

- For 4 messages with frequencies [2, 4, 8, 100], using fixed 2-bit codes (like 00, 01, 10, 11) results in a cost of $2*2 + 4*2 + 8*2 + 100*2 = 228$.
- This cost is the same for transmission and decoding.


### 4. 🗜️ Lossless Data Compression: Using Variable-Length Codes

Using fixed-length codes is simple but inefficient when message frequencies vary widely.

#### Why Variable-Length Codes?

- Assign shorter codes to more frequent messages.
- Assign longer codes to less frequent messages.
- This reduces the average number of bits needed to represent the data.

#### Prefix Property

- Codes must satisfy the **prefix property**: no code is a prefix of another.
- This ensures unambiguous decoding.

#### Example

- Alphabet: {a, b, c, d} with frequencies 10, 5, 100, 900.
- Using fixed 2-bit codes: total size = $10*2 + 5*2 + 100*2 + 900*2 = 2030$ bits.
- Using variable-length codes (e.g., a=3 bits, b=3 bits, c=2 bits, d=1 bit): total size = $10*3 + 5*3 + 100*2 + 900*1 = 1145$ bits.
- Compression ratio ≈ 2030 / 1145 ≈ 1.8, meaning almost half the size.


### 5. 🌲 Huffman Trees: Building Optimal Prefix Codes

**Huffman trees** are binary trees that minimize the WEPL, thus providing the most efficient prefix codes for lossless compression.

#### How to Build a Huffman Tree?

- Use a **greedy algorithm**:
  1. Start with a forest of single-node trees, each node representing a message with its frequency.
  2. Repeatedly select the two trees with the smallest weights.
  3. Combine them into a new tree with a root node whose weight is the sum of the two.
  4. Insert the new tree back into the forest.
  5. Repeat until only one tree remains.

#### Why Greedy Works?

- Combining the smallest weights first ensures minimal increase in WEPL.
- The final tree corresponds to the optimal prefix code.

#### Data Structures for Efficiency

- Use a **min-heap** to efficiently find and remove the two smallest trees.
- Initialization takes $O(n)$.
- Each of the $n-1$ merges involves removing two minimum trees and inserting one new tree, each operation $O(\log n)$.
- Total time complexity: $O(n \log n)$.


### 6. 🌳 Higher-Order Trees: Challenges Beyond Binary Huffman Trees

Sometimes, instead of binary trees, we want **k-ary trees** (e.g., ternary trees) for coding or merging.

#### Why is Greedy Algorithm Not Always Optimal for k-ary Trees?

- The greedy approach can fail because nodes may not have exactly k children.
- For example, with weights [3, 6, 1, 9] and a 3-way tree, greedy cost is 29, but the optimal cost is 23.

#### How to Fix This?

- Add **zero-weight runs** (dummy nodes) to ensure the number of runs fits the k-ary tree structure.
- The number of zero-weight runs $q$ to add satisfies:


$$
(r + q - 1) \mod (k - 1) = 0
$$


where $r$ is the initial number of runs.

- This ensures all internal nodes have exactly k children.


### 7. 💾 Memory Partitioning and Buffer Management in k-Way Merging

When merging k runs, memory must be carefully partitioned to balance input and output buffers.

#### Buffer Requirements

- Exactly **2 output buffers** are needed to allow overlapping writing.
- At least **k+1 input buffers** are needed for the loser tree.
- Using **2k input buffers** is often sufficient.

#### Buffer Allocation Strategy

- Input buffers are allocated dynamically based on which run will exhaust first.
- To decide which run exhausts first:
  - Look at the last key read from each run.
  - The run with the smallest last key is expected to finish first.
  - Use a tie-breaker if needed.

#### Initialization for Merging k Runs

- Initialize k queues of input buffers, one per run.
- Load one buffer from each run.
- Place unused buffers into a free pool.
- Start reading the next buffer from the run expected to exhaust first.

#### The kWayMerge Method

- Merge data from input queues into the active output buffer.
- Stop merging when:
  - The output buffer is full, or
  - An end-of-run key is merged.
- If an input buffer empties, move to the next buffer in its queue and free the empty buffer.
- Repeat until all runs are merged.


### Summary

This lecture covered advanced techniques for external sorting and data compression:

- **Run generation** is improved by overlapping I/O and CPU work and using loser trees to produce longer runs.
- **Optimal merging** minimizes the weighted external path length (WEPL), reducing total merge cost.
- **Message coding and lossless compression** use prefix codes represented by binary trees, where minimizing WEPL leads to efficient codes.
- **Huffman trees** provide an optimal greedy method for binary prefix codes.
- For **higher-order trees**, additional zero-weight runs are needed to maintain optimality.
- Efficient **buffer management** is crucial for merging multiple runs in external memory.

Understanding these concepts is essential for designing efficient external sorting algorithms and compression schemes.