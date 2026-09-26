## 2. Run Generation, Optimal Merging, and Huffman Trees

## Questions

#### 1. Which of the following statements about run generation using a loser tree are true?  
A) The minimum run size generated is at least the number of external nodes in the loser tree.  
B) If the input is sorted, only one run is generated.  
C) The average run size is approximately half the number of external nodes in the loser tree.  
D) The total internal processing time using a loser tree is O(n log k), where k is the number of external nodes.  

#### 2. In the context of optimal merging of runs, the Weighted External Path Length (WEPL) is defined as:  
A) The sum of the weights of all internal nodes multiplied by their distance from the root.  
B) The sum of the weights of all external nodes multiplied by their distance from the root.  
C) The sum of the weights of all external nodes multiplied by their depth in the tree.  
D) The sum of the weights of all nodes multiplied by their distance from the root.  

#### 3. Regarding message coding and decoding using prefix codes, which of the following are correct?  
A) The code set must ensure no code is a prefix of another to guarantee lossless decoding.  
B) The decoding cost equals the transmission cost and corresponds to the WEPL of the decoding tree.  
C) Using fixed-length codes always results in the minimum transmission cost.  
D) Variable-length prefix codes can reduce the total number of bits transmitted compared to fixed-length codes.  

#### 4. Which of the following statements about Huffman trees and their construction are true?  
A) Huffman trees minimize the Weighted External Path Length for a given set of weights.  
B) The greedy algorithm for binary Huffman trees always produces an optimal tree.  
C) For k-ary Huffman trees (k > 2), the greedy algorithm without preprocessing always produces an optimal tree.  
D) The greedy algorithm combines the two trees with the smallest weights at each step.  

#### 5. When constructing a k-ary Huffman tree, why might it be necessary to add runs of length zero?  
A) To ensure that all internal nodes have exactly k children.  
B) To reduce the total number of runs to a power of k.  
C) To satisfy the condition that (r + q - 1) is divisible by (k - 1), where r is the initial number of runs and q is the number of zero-length runs added.  
D) To guarantee that the greedy algorithm produces an optimal tree.  

#### 6. Consider a 3-way Huffman tree with initial run weights [3, 6, 1, 9]. Which of the following statements explain why the greedy algorithm might fail to produce the optimal tree?  
A) The greedy algorithm does not consider adding zero-weight runs to balance the tree.  
B) The greedy algorithm always merges the largest weights first, which is suboptimal.  
C) One node in the greedy tree is not a 3-way node, effectively acting like a 2-way node with a zero-weight child missing.  
D) The greedy algorithm cannot handle more than two children per node.  

#### 7. In the k-way merge process using loser trees and buffer management, which of the following are true?  
A) Exactly two output buffers are needed for steady-state operation.  
B) At least k+1 input buffers are required, where k is the merge order.  
C) Input buffers must be allocated dynamically based on which run will exhaust first.  
D) Two input buffers per run are always sufficient for merging k runs.  

#### 8. During buffer allocation in k-way merging, how is the next input buffer load determined?  
A) By selecting the run with the largest last key read.  
B) By selecting the run with the smallest last key read.  
C) By enforcing a tie breaker when multiple runs have the same last key read.  
D) By randomly choosing any run with available input buffers.  

#### 9. Which of the following correctly describe the initialization steps for merging k runs using input buffer queues?  
A) Initialize k queues of input buffers, one per run, with one buffer each.  
B) Input one buffer load from each of the k runs initially.  
C) Place all input buffers into a single shared pool without queues.  
D) Set the active output buffer to 0 before starting the merge.  

#### 10. In the kWayMerge method, which of the following conditions cause the merge to stop?  
A) The output buffer becomes full.  
B) An end-of-run key is merged into the output buffer.  
C) All input buffers become empty simultaneously.  
D) The active output buffer is switched before the current merge completes.



<br>

## Answers

#### 1. Which of the following statements about run generation using a loser tree are true?  
A) ✓ The minimum run size is at least the number of external nodes (k) in the loser tree.  
B) ✓ If the input is sorted, only one run is generated because the entire input is already ordered.  
C) ✗ The average run size is approximately 2k, not half k.  
D) ✓ The internal processing time is O(n log k), where k is the number of external nodes.  

**Correct:** A, B, D


#### 2. In the context of optimal merging of runs, the Weighted External Path Length (WEPL) is defined as:  
A) ✗ WEPL involves external nodes, not internal nodes.  
B) ✓ WEPL is the sum over external nodes of (weight × distance from root).  
C) ✓ Distance from root is equivalent to depth, so this is correct.  
D) ✗ WEPL does not include internal nodes’ weights.  

**Correct:** B, C


#### 3. Regarding message coding and decoding using prefix codes, which of the following are correct?  
A) ✓ Prefix property ensures no code is a prefix of another, enabling lossless decoding.  
B) ✓ Decoding cost equals transmission cost and corresponds to WEPL of the decoding tree.  
C) ✗ Fixed-length codes do not always minimize transmission cost; variable-length codes can do better.  
D) ✓ Variable-length prefix codes reduce total bits transmitted compared to fixed-length codes.  

**Correct:** A, B, D


#### 4. Which of the following statements about Huffman trees and their construction are true?  
A) ✓ Huffman trees minimize WEPL for given weights.  
B) ✓ The greedy algorithm for binary Huffman trees always produces an optimal tree.  
C) ✗ For k-ary trees (k > 2), greedy algorithm without preprocessing may fail to produce optimal trees.  
D) ✓ The greedy algorithm combines the two trees with the smallest weights at each step.  

**Correct:** A, B, D


#### 5. When constructing a k-ary Huffman tree, why might it be necessary to add runs of length zero?  
A) ✓ To ensure all internal nodes have exactly k children, balancing the tree.  
B) ✗ The goal is not to reduce runs to a power of k but to satisfy divisibility conditions.  
C) ✓ The condition (r + q - 1) divisible by (k - 1) must hold for proper merging.  
D) ✓ Adding zero-length runs ensures the greedy algorithm produces an optimal tree.  

**Correct:** A, C, D


#### 6. Consider a 3-way Huffman tree with initial run weights [3, 6, 1, 9]. Which of the following statements explain why the greedy algorithm might fail to produce the optimal tree?  
A) ✓ The greedy algorithm does not add zero-weight runs needed to balance the tree.  
B) ✗ The greedy algorithm merges smallest weights first, not largest.  
C) ✓ One node is effectively a 2-way node missing a zero-weight child, causing suboptimality.  
D) ✗ The greedy algorithm can handle more than two children per node in k-ary trees but may fail without preprocessing.  

**Correct:** A, C


#### 7. In the k-way merge process using loser trees and buffer management, which of the following are true?  
A) ✓ Exactly two output buffers are needed for steady-state operation.  
B) ✓ At least k+1 input buffers are required, where k is the merge order.  
C) ✓ Input buffers must be allocated dynamically based on which run will exhaust first.  
D) ✗ Two input buffers per run are not always sufficient; dynamic allocation is needed.  

**Correct:** A, B, C


#### 8. During buffer allocation in k-way merging, how is the next input buffer load determined?  
A) ✗ The run with the largest last key read is not chosen.  
B) ✓ The run with the smallest last key read will exhaust first and is chosen.  
C) ✓ Tie breakers are enforced when multiple runs have the same last key read.  
D) ✗ Random selection is not used; selection is deterministic.  

**Correct:** B, C


#### 9. Which of the following correctly describe the initialization steps for merging k runs using input buffer queues?  
A) ✓ Initialize k queues of input buffers, one per run, with one buffer each.  
B) ✓ Input one buffer load from each of the k runs initially.  
C) ✗ Input buffers are organized per run, not all in a single shared pool without queues.  
D) ✓ Set the active output buffer to 0 before starting the merge.  

**Correct:** A, B, D


#### 10. In the kWayMerge method, which of the following conditions cause the merge to stop?  
A) ✓ The merge stops if the output buffer becomes full.  
B) ✓ The merge stops if an end-of-run key is merged into the output buffer.  
C) ✗ The merge does not necessarily stop if all input buffers become empty simultaneously; it depends on output buffer state.  
D) ✗ The active output buffer is switched only after the current merge completes, not before.  

**Correct:** A, B