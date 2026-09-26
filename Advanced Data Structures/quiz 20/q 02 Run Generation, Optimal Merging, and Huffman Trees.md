## 2. Run Generation, Optimal Merging, and Huffman Trees

## Questions

#### 1. What is the primary goal of improving run generation in external sorting?  
A) To increase the number of runs generated  
B) To overlap input, output, and CPU work  
C) To reduce the number of runs by increasing average run length  
D) To minimize disk memory usage  

#### 2. In the improved run generation strategy using loser trees, what is the minimum run size relative to the number of external nodes k?  
A) Run size ≤ k  
B) Run size = k  
C) Run size ≥ k  
D) Run size = n/k  

#### 3. Which of the following statements about loser trees in run generation is true?  
A) Using 3 buffers is always inadequate for steady state operation  
B) The total internal processing time using a loser tree is O(n log k)  
C) Sorted input results in multiple runs equal to n/k  
D) Average run size is approximately 2k  

#### 4. Weighted External Path Length (WEPL) is used to measure which of the following?  
A) The total number of runs generated  
B) The cost of merging runs of different lengths  
C) The transmission and decoding cost in message coding  
D) The size of the code table in lossless compression  

#### 5. In message coding and decoding, why is it sufficient to transmit only the code identifying the message index?  
A) Because messages change frequently  
B) Because both sender and receiver know the messages beforehand  
C) Because the code length is always fixed  
D) Because the messages are encrypted  

#### 6. Given message frequencies [2, 4, 8, 100] and fixed 2-bit codes, what is the total transmission cost?  
A) 114 bits  
B) 228 bits  
C) 228 * 2 bits  
D) 2 * (2 + 4 + 8 + 100) bits  

#### 7. Which property must a variable length code satisfy to ensure lossless data compression?  
A) All codes must have the same length  
B) No code is a prefix of another code  
C) Codes must be sorted by frequency  
D) Codes must be binary only  

#### 8. How does using a variable length prefix code affect the size of the compressed string compared to fixed length codes?  
A) It always increases the size  
B) It reduces the size by assigning shorter codes to more frequent symbols  
C) It has no effect on the size  
D) It increases the size due to the code table overhead  

#### 9. What is the main characteristic of Huffman trees?  
A) They maximize the weighted external path length  
B) They minimize the weighted external path length  
C) They are always balanced binary trees  
D) They are constructed using a dynamic programming approach  

#### 10. In the greedy algorithm for constructing a binary Huffman tree, what is the criterion for combining two trees?  
A) Combine the two trees with the maximum weights  
B) Combine the two trees with the minimum weights  
C) Combine any two trees randomly  
D) Combine the two trees with the median weights  

#### 11. What is the time complexity of building a Huffman tree using a min heap for n messages?  
A) O(n)  
B) O(n log n)  
C) O(n^2)  
D) O(log n)  

#### 12. Why does the greedy scheme fail for higher order (k-ary) Huffman trees?  
A) Because the weights are not sorted  
B) Because some nodes are not full k-way nodes without adding zero-weight runs  
C) Because the min heap cannot handle k-ary trees  
D) Because the weighted external path length is not defined for k-ary trees  

#### 13. For a k-way Huffman tree with initial runs r, how is the number q of zero-length runs to add determined?  
A) q = r mod k  
B) q = (1 - r) mod (k - 1)  
C) q = (r - 1) mod k  
D) q = (r + 1) mod (k - 1)  

#### 14. What is the significance of ensuring (r + q - 1) is divisible by (k - 1) in k-way merging?  
A) It guarantees the tree is balanced  
B) It ensures the number of runs reduces to exactly one after s merges  
C) It minimizes the number of zero-length runs added  
D) It maximizes the weighted external path length  

#### 15. In the context of buffer allocation during k-way merging, which run should be allocated the next input buffer?  
A) The run with the largest last key read  
B) The run with the smallest last key read  
C) The run with the most remaining data  
D) The run with the fewest buffers allocated  

#### 16. Why are 2 output buffers necessary in the memory partitioning for k-way merging?  
A) To allow overlapping of output writing and merging  
B) To reduce the number of input buffers needed  
C) To store intermediate runs  
D) To increase the run size  

#### 17. When merging k runs, why might 2k input buffers not be sufficient?  
A) Because input buffers must be allocated dynamically based on run exhaustion  
B) Because output buffers consume input buffer space  
C) Because the loser tree requires more buffers  
D) Because the disk I/O speed limits buffer usage  

#### 18. During the kWayMerge method, what causes the merge to stop?  
A) When the output buffer is full  
B) When an end-of-run key is merged into the output buffer  
C) When all input buffers are empty  
D) Both A and B  

#### 19. What is the role of the loser tree in run generation and merging?  
A) To select the maximum key among input runs  
B) To efficiently select the minimum key among input runs  
C) To store output buffers  
D) To manage disk I/O scheduling  

#### 20. Which of the following statements about the average run size in run generation using a loser tree is correct?  
A) It is approximately equal to k/2  
B) It is approximately equal to 2k  
C) It depends on the input being sorted or reverse sorted  
D) It is always equal to n/k



<br>

## Answers

#### 1. What is the primary goal of improving run generation in external sorting?  
A) ✗ Increasing runs is opposite to the goal.  
B) ✓ Overlapping input, output, and CPU work improves efficiency.  
C) ✓ Reducing runs by increasing average run length is a key goal.  
D) ✗ Minimizing disk memory usage is not the main focus here.  

**Correct:** B, C


#### 2. In the improved run generation strategy using loser trees, what is the minimum run size relative to the number of external nodes k?  
A) ✗ Run size is not less than or equal to k.  
B) ✗ Run size equals k is not guaranteed, only a lower bound.  
C) ✓ Run size is at least k (≥ k).  
D) ✗ n/k runs is the number of runs for reverse sorted input, not run size.  

**Correct:** C


#### 3. Which of the following statements about loser trees in run generation is true?  
A) ✗ 3 buffers are actually adequate for steady state operation.  
B) ✓ Total internal processing time is O(n log k).  
C) ✗ Sorted input results in 1 run, not n/k runs.  
D) ✓ Average run size is approximately 2k.  

**Correct:** B, D


#### 4. Weighted External Path Length (WEPL) is used to measure which of the following?  
A) ✗ WEPL does not measure number of runs.  
B) ✓ WEPL measures cost related to merging runs of different lengths.  
C) ✓ WEPL corresponds to transmission and decoding cost in message coding.  
D) ✗ WEPL is not the size of the code table.  

**Correct:** B, C


#### 5. In message coding and decoding, why is it sufficient to transmit only the code identifying the message index?  
A) ✗ Messages do not change frequently.  
B) ✓ Both sender and receiver know the messages, so only code is needed.  
C) ✗ Code length can vary; fixed length is not necessary.  
D) ✗ Messages are not necessarily encrypted here.  

**Correct:** B


#### 6. Given message frequencies [2, 4, 8, 100] and fixed 2-bit codes, what is the total transmission cost?  
A) ✗ 114 bits is too low.  
B) ✗ 228 bits is just sum of frequencies, not weighted by code length.  
C) ✗ 228 * 2 bits is incorrect calculation.  
D) ✓ 2 * (2 + 4 + 8 + 100) bits = 228 * 2 = 456 bits total cost.  

**Correct:** D


#### 7. Which property must a variable length code satisfy to ensure lossless data compression?  
A) ✗ Codes can have variable length.  
B) ✓ No code is a prefix of another (prefix property).  
C) ✗ Sorting by frequency is not a requirement for prefix codes.  
D) ✗ Codes can be non-binary (e.g., ternary), prefix property still applies.  

**Correct:** B


#### 8. How does using a variable length prefix code affect the size of the compressed string compared to fixed length codes?  
A) ✗ It usually reduces size, not increases.  
B) ✓ It reduces size by assigning shorter codes to frequent symbols.  
C) ✗ It does affect size significantly.  
D) ✓ Code table overhead exists but compression ratio is still improved.  

**Correct:** B, D


#### 9. What is the main characteristic of Huffman trees?  
A) ✗ They minimize, not maximize, WEPL.  
B) ✓ They minimize weighted external path length.  
C) ✗ They are not necessarily balanced.  
D) ✗ Constructed by greedy algorithm, not dynamic programming.  

**Correct:** B


#### 10. In the greedy algorithm for constructing a binary Huffman tree, what is the criterion for combining two trees?  
A) ✗ Maximum weights are not combined first.  
B) ✓ Two trees with minimum weights are combined.  
C) ✗ Random combination is not used.  
D) ✗ Median weights are irrelevant.  

**Correct:** B


#### 11. What is the time complexity of building a Huffman tree using a min heap for n messages?  
A) ✗ O(n) is too optimistic.  
B) ✓ O(n log n) is correct due to heap operations.  
C) ✗ O(n^2) is too high.  
D) ✗ O(log n) is too low.  

**Correct:** B


#### 12. Why does the greedy scheme fail for higher order (k-ary) Huffman trees?  
A) ✗ Weight sorting is not the cause.  
B) ✓ Because some nodes are not full k-way nodes without adding zero-weight runs.  
C) ✗ Min heap can handle k-ary trees with modifications.  
D) ✗ WEPL is defined for k-ary trees.  

**Correct:** B


#### 13. For a k-way Huffman tree with initial runs r, how is the number q of zero-length runs to add determined?  
A) ✗ q is not r mod k.  
B) ✓ q = (1 - r) mod (k - 1) ensures divisibility condition.  
C) ✗ (r - 1) mod k is incorrect formula.  
D) ✗ (r + 1) mod (k - 1) is incorrect.  

**Correct:** B


#### 14. What is the significance of ensuring (r + q - 1) is divisible by (k - 1) in k-way merging?  
A) ✗ It does not guarantee balanced tree.  
B) ✓ Ensures number of runs reduces to exactly one after s merges.  
C) ✓ Minimizes zero-length runs added (q < k - 1).  
D) ✗ It minimizes WEPL, not maximizes.  

**Correct:** B, C


#### 15. In the context of buffer allocation during k-way merging, which run should be allocated the next input buffer?  
A) ✗ Largest last key read is not correct.  
B) ✓ Run with smallest last key read will exhaust first and gets next buffer.  
C) ✗ Most remaining data is not the criterion.  
D) ✗ Fewest buffers allocated is irrelevant.  

**Correct:** B


#### 16. Why are 2 output buffers necessary in the memory partitioning for k-way merging?  
A) ✓ To overlap output writing and merging for efficiency.  
B) ✗ They do not reduce input buffer needs.  
C) ✗ They are not for storing intermediate runs.  
D) ✗ They do not directly increase run size.  

**Correct:** A


#### 17. When merging k runs, why might 2k input buffers not be sufficient?  
A) ✓ Because input buffers must be allocated dynamically based on run exhaustion.  
B) ✗ Output buffers do not consume input buffer space.  
C) ✗ Loser tree does not require more buffers than allocated.  
D) ✗ Disk I/O speed does not limit buffer count directly.  

**Correct:** A


#### 18. During the kWayMerge method, what causes the merge to stop?  
A) ✓ Output buffer full causes stop.  
B) ✓ End-of-run key merged causes stop.  
C) ✗ Input buffers empty alone does not stop merge.  
D) ✗ Only A and B cause stop, not C.  

**Correct:** A, B


#### 19. What is the role of the loser tree in run generation and merging?  
A) ✗ It selects minimum, not maximum key.  
B) ✓ Efficiently selects minimum key among input runs.  
C) ✗ It does not store output buffers.  
D) ✗ It does not manage disk I/O scheduling.  

**Correct:** B


#### 20. Which of the following statements about the average run size in run generation using a loser tree is correct?  
A) ✗ Average run size is not k/2.  
B) ✓ Average run size is approximately 2k.  
C) ✓ It depends on input order: sorted input yields 1 run, reverse sorted yields n/k runs.  
D) ✗ Average run size is not always n/k; that is number of runs for reverse sorted input.  

**Correct:** B, C