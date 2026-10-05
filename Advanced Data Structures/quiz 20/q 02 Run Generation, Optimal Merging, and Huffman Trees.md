## 2. Run Generation, Optimal Merging, and Huffman Trees

## Questions

#### 1. What is the primary goal of improving run generation in external sorting?  
A) To reduce the number of runs by increasing average run length  
B) To overlap input, output, and CPU work  
C) To increase the number of runs generated  
D) To minimize disk memory usage  

#### 2. In the improved run generation strategy using loser trees, what is the minimum run size relative to the number of external nodes k?  
A) Run size = n/k  
B) Run size ≥ k  
C) Run size = k  
D) Run size ≤ k  

#### 3. Which of the following statements about loser trees in run generation is true?  
A) Average run size is approximately 2k  
B) Sorted input results in multiple runs equal to n/k  
C) Using 3 buffers is always inadequate for steady state operation  
D) The total internal processing time using a loser tree is O(n log k)  

#### 4. Weighted External Path Length (WEPL) is used to measure which of the following?  
A) The total number of runs generated  
B) The size of the code table in lossless compression  
C) The transmission and decoding cost in message coding  
D) The cost of merging runs of different lengths  

#### 5. In message coding and decoding, why is it sufficient to transmit only the code identifying the message index?  
A) Because messages change frequently  
B) Because the code length is always fixed  
C) Because both sender and receiver know the messages beforehand  
D) Because the messages are encrypted  

#### 6. Given message frequencies [2, 4, 8, 100] and fixed 2-bit codes, what is the total transmission cost?  
A) 228 * 2 bits  
B) 228 bits  
C) 2 * (2 + 4 + 8 + 100) bits  
D) 114 bits  

#### 7. Which property must a variable length code satisfy to ensure lossless data compression?  
A) All codes must have the same length  
B) Codes must be binary only  
C) No code is a prefix of another code  
D) Codes must be sorted by frequency  

#### 8. How does using a variable length prefix code affect the size of the compressed string compared to fixed length codes?  
A) It reduces the size by assigning shorter codes to more frequent symbols  
B) It has no effect on the size  
C) It increases the size due to the code table overhead  
D) It always increases the size  

#### 9. What is the main characteristic of Huffman trees?  
A) They minimize the weighted external path length  
B) They are constructed using a dynamic programming approach  
C) They maximize the weighted external path length  
D) They are always balanced binary trees  

#### 10. In the greedy algorithm for constructing a binary Huffman tree, what is the criterion for combining two trees?  
A) Combine the two trees with the maximum weights  
B) Combine the two trees with the minimum weights  
C) Combine any two trees randomly  
D) Combine the two trees with the median weights  

#### 11. What is the time complexity of building a Huffman tree using a min heap for n messages?  
A) O(n^2)  
B) O(log n)  
C) O(n log n)  
D) O(n)  

#### 12. Why does the greedy scheme fail for higher order (k-ary) Huffman trees?  
A) Because the weights are not sorted  
B) Because some nodes are not full k-way nodes without adding zero-weight runs  
C) Because the weighted external path length is not defined for k-ary trees  
D) Because the min heap cannot handle k-ary trees  

#### 13. For a k-way Huffman tree with initial runs r, how is the number q of zero-length runs to add determined?  
A) q = r mod k  
B) q = (r + 1) mod (k - 1)  
C) q = (1 - r) mod (k - 1)  
D) q = (r - 1) mod k  

#### 14. What is the significance of ensuring (r + q - 1) is divisible by (k - 1) in k-way merging?  
A) It guarantees the tree is balanced  
B) It ensures the number of runs reduces to exactly one after s merges  
C) It maximizes the weighted external path length  
D) It minimizes the number of zero-length runs added  

#### 15. In the context of buffer allocation during k-way merging, which run should be allocated the next input buffer?  
A) The run with the largest last key read  
B) The run with the fewest buffers allocated  
C) The run with the most remaining data  
D) The run with the smallest last key read  

#### 16. Why are 2 output buffers necessary in the memory partitioning for k-way merging?  
A) To allow overlapping of output writing and merging  
B) To increase the run size  
C) To reduce the number of input buffers needed  
D) To store intermediate runs  

#### 17. When merging k runs, why might 2k input buffers not be sufficient?  
A) Because the loser tree requires more buffers  
B) Because input buffers must be allocated dynamically based on run exhaustion  
C) Because output buffers consume input buffer space  
D) Because the disk I/O speed limits buffer usage  

#### 18. During the kWayMerge method, what causes the merge to stop?  
A) When an end-of-run key is merged into the output buffer  
B) When all input buffers are empty  
C) Both A and B  
D) When the output buffer is full  

#### 19. What is the role of the loser tree in run generation and merging?  
A) To store output buffers  
B) To select the maximum key among input runs  
C) To efficiently select the minimum key among input runs  
D) To manage disk I/O scheduling  

#### 20. Which of the following statements about the average run size in run generation using a loser tree is correct?  
A) It is approximately equal to k/2  
B) It depends on the input being sorted or reverse sorted  
C) It is always equal to n/k  
D) It is approximately equal to 2k  



<br>

## Answers

#### 1. What is the primary goal of improving run generation in external sorting?  
A) ✓ Reducing runs by increasing average run length is a key goal.  
B) ✓ Overlapping input, output, and CPU work improves efficiency.  
C) ✗ Increasing runs is opposite to the goal.  
D) ✗ Minimizing disk memory usage is not the main focus here.  

**Correct:** A, B


#### 2. In the improved run generation strategy using loser trees, what is the minimum run size relative to the number of external nodes k?  
A) ✗ n/k runs is the number of runs for reverse sorted input, not run size.  
B) ✓ Run size is at least k (≥ k).  
C) ✗ Run size equals k is not guaranteed, only a lower bound.  
D) ✗ Run size is not less than or equal to k.  

**Correct:** B


#### 3. Which of the following statements about loser trees in run generation is true?  
A) ✓ Average run size is approximately 2k.  
B) ✗ Sorted input results in 1 run, not n/k runs.  
C) ✗ 3 buffers are actually adequate for steady state operation.  
D) ✓ Total internal processing time is O(n log k).  

**Correct:** A, D


#### 4. Weighted External Path Length (WEPL) is used to measure which of the following?  
A) ✗ WEPL does not measure number of runs.  
B) ✗ WEPL is not the size of the code table.  
C) ✓ WEPL corresponds to transmission and decoding cost in message coding.  
D) ✓ WEPL measures cost related to merging runs of different lengths.  

**Correct:** C, D


#### 5. In message coding and decoding, why is it sufficient to transmit only the code identifying the message index?  
A) ✗ Messages do not change frequently.  
B) ✗ Code length can vary; fixed length is not necessary.  
C) ✓ Both sender and receiver know the messages, so only code is needed.  
D) ✗ Messages are not necessarily encrypted here.  

**Correct:** C


#### 6. Given message frequencies [2, 4, 8, 100] and fixed 2-bit codes, what is the total transmission cost?  
A) ✗ 228 * 2 bits is incorrect calculation.  
B) ✗ 228 bits is just sum of frequencies, not weighted by code length.  
C) ✓ 2 * (2 + 4 + 8 + 100) bits = 228 * 2 = 456 bits total cost.  
D) ✗ 114 bits is too low.  

**Correct:** C


#### 7. Which property must a variable length code satisfy to ensure lossless data compression?  
A) ✗ Codes can have variable length.  
B) ✗ Codes can be non-binary (e.g., ternary), prefix property still applies.  
C) ✓ No code is a prefix of another (prefix property).  
D) ✗ Sorting by frequency is not a requirement for prefix codes.  

**Correct:** C


#### 8. How does using a variable length prefix code affect the size of the compressed string compared to fixed length codes?  
A) ✓ It reduces size by assigning shorter codes to frequent symbols.  
B) ✗ It does affect size significantly.  
C) ✓ Code table overhead exists but compression ratio is still improved.  
D) ✗ It usually reduces size, not increases.  

**Correct:** A, C


#### 9. What is the main characteristic of Huffman trees?  
A) ✓ They minimize weighted external path length.  
B) ✗ Constructed by greedy algorithm, not dynamic programming.  
C) ✗ They minimize, not maximize, WEPL.  
D) ✗ They are not necessarily balanced.  

**Correct:** A


#### 10. In the greedy algorithm for constructing a binary Huffman tree, what is the criterion for combining two trees?  
A) ✗ Maximum weights are not combined first.  
B) ✓ Two trees with minimum weights are combined.  
C) ✗ Random combination is not used.  
D) ✗ Median weights are irrelevant.  

**Correct:** B


#### 11. What is the time complexity of building a Huffman tree using a min heap for n messages?  
A) ✗ O(n^2) is too high.  
B) ✗ O(log n) is too low.  
C) ✓ O(n log n) is correct due to heap operations.  
D) ✗ O(n) is too optimistic.  

**Correct:** C


#### 12. Why does the greedy scheme fail for higher order (k-ary) Huffman trees?  
A) ✗ Weight sorting is not the cause.  
B) ✓ Because some nodes are not full k-way nodes without adding zero-weight runs.  
C) ✗ WEPL is defined for k-ary trees.  
D) ✗ Min heap can handle k-ary trees with modifications.  

**Correct:** B


#### 13. For a k-way Huffman tree with initial runs r, how is the number q of zero-length runs to add determined?  
A) ✗ q is not r mod k.  
B) ✗ (r + 1) mod (k - 1) is incorrect.  
C) ✓ q = (1 - r) mod (k - 1) ensures divisibility condition.  
D) ✗ (r - 1) mod k is incorrect formula.  

**Correct:** C


#### 14. What is the significance of ensuring (r + q - 1) is divisible by (k - 1) in k-way merging?  
A) ✗ It does not guarantee balanced tree.  
B) ✓ Ensures number of runs reduces to exactly one after s merges.  
C) ✗ It minimizes WEPL, not maximizes.  
D) ✓ Minimizes zero-length runs added (q < k - 1).  

**Correct:** B, D


#### 15. In the context of buffer allocation during k-way merging, which run should be allocated the next input buffer?  
A) ✗ Largest last key read is not correct.  
B) ✗ Fewest buffers allocated is irrelevant.  
C) ✗ Most remaining data is not the criterion.  
D) ✓ Run with smallest last key read will exhaust first and gets next buffer.  

**Correct:** D


#### 16. Why are 2 output buffers necessary in the memory partitioning for k-way merging?  
A) ✓ To overlap output writing and merging for efficiency.  
B) ✗ They do not directly increase run size.  
C) ✗ They do not reduce input buffer needs.  
D) ✗ They are not for storing intermediate runs.  

**Correct:** A


#### 17. When merging k runs, why might 2k input buffers not be sufficient?  
A) ✗ Loser tree does not require more buffers than allocated.  
B) ✓ Because input buffers must be allocated dynamically based on run exhaustion.  
C) ✗ Output buffers do not consume input buffer space.  
D) ✗ Disk I/O speed does not limit buffer count directly.  

**Correct:** B


#### 18. During the kWayMerge method, what causes the merge to stop?  
A) ✓ End-of-run key merged causes stop.  
B) ✗ Input buffers empty alone does not stop merge.  
C) ✗ Only A and B cause stop, not C.  
D) ✓ Output buffer full causes stop.  

**Correct:** A, D


#### 19. What is the role of the loser tree in run generation and merging?  
A) ✗ It does not store output buffers.  
B) ✗ It selects minimum, not maximum key.  
C) ✓ Efficiently selects minimum key among input runs.  
D) ✗ It does not manage disk I/O scheduling.  

**Correct:** C


#### 20. Which of the following statements about the average run size in run generation using a loser tree is correct?  
A) ✗ Average run size is not k/2.  
B) ✓ It depends on input order: sorted input yields 1 run, reverse sorted yields n/k runs.  
C) ✗ Average run size is not always n/k; that is number of runs for reverse sorted input.  
D) ✓ Average run size is approximately 2k.  

**Correct:** B, D