## 13. Compressed and Multibit Tries

## Questions

#### 1. Which of the following statements correctly describe properties of a compressed binary trie?  
A) No branch node has degree 1.  
B) Each branch node contains a bit# field indicating which bit to branch on.  
C) The number of branch nodes in a compressed binary trie is equal to the number of keys n.  
D) Compressed binary tries always have a height equal to the length of the longest key.

#### 2. Regarding tries built for NID numbers (9 decimal digits), which of the following are true?  
A) A 10-way trie has height at most 10.  
B) A 100-way trie has height at most 6.  
C) A red-black tree storing 9-digit numbers has height approximately 60.  
D) An AVL tree storing 9-digit numbers has height approximately 30.

#### 3. When handling variable length keys in tries, what techniques are used to avoid prefix ambiguity?  
A) Adding a special end-of-key character (#) to each key.  
B) Using compressed tries to eliminate nodes with degree 1.  
C) Expanding shorter prefixes to the length of the node’s stride in multibit tries.  
D) Storing keys only if they have the same length.

#### 4. In multibit tries, which of the following statements are correct?  
A) Each node’s stride s determines the number of bits used for branching at that node.  
B) A node with stride s has 2^s children and 2^s element/prefix fields.  
C) All nodes in a multibit trie must have the same stride.  
D) Short prefixes are expanded to the length represented by the node’s stride.

#### 5. Which of the following are valid reasons why TCAMs (Ternary Content Addressable Memories) are limited in router implementations?  
A) High power consumption.  
B) Limited scalability to IPv6 address lengths.  
C) Inability to perform longest prefix matching.  
D) High cost and board space requirements.

#### 6. Consider the problem of fixed-stride tries. Which of the following statements are true?  
A) The number of levels equals the number of distinct prefix lengths.  
B) Prefix expansion can reduce the number of distinct prefix lengths.  
C) Fixed-stride tries always have fewer levels than variable-stride tries.  
D) The optimization problem is to find the least memory fixed-stride trie with height at most k.

#### 7. Which of the following correctly describe tie-breaking rules in router rule tables?  
A) The first matching rule is always chosen.  
B) The highest-priority rule is preferred over others.  
C) The most-specific rule is the one with the smallest range.  
D) The longest-prefix rule selects the rule with the longest matching prefix.

#### 8. In the context of tries with edge information, what is the purpose of adding a pointer field to each branch node?  
A) To point to any element node in the subtree for reconstructing skipped characters.  
B) To store the bit# or char# used for branching at that node.  
C) To reduce the height of the trie by skipping levels.  
D) To store the number of non-null pointers in the node.

#### 9. Which of the following statements about 2-dimensional tries and filters are correct?  
A) They handle destination-source address pairs for filtering.  
B) Tie-breaking can be based on least cost among matching rules.  
C) They are limited to 1-bit branching at each node.  
D) They can be implemented as 2D multibit tries.

#### 10. Regarding the complexity and performance of 1-bit and multibit tries, which statements are accurate?  
A) 1-bit tries have O(W) complexity per operation, where W is the key length in bits.  
B) Multibit tries reduce height by increasing stride at nodes.  
C) Fixed-stride tries always outperform variable-stride tries in memory usage.  
D) Multibit tries are particularly suitable for longest prefix matching in Internet routing.



<br>

## Answers

#### 1. Which of the following statements correctly describe properties of a compressed binary trie?  
A) ✓ No branch node has degree 1, which is a defining property of compressed tries to avoid unnecessary nodes.  
B) ✓ Each branch node contains a bit# field indicating which bit to branch on, used to decide left or right traversal.  
C) ✗ The number of branch nodes is n - 1, not equal to n (number of keys).  
D) ✗ Height depends on key length and compression; it is not always equal to the longest key length.

**Correct:** A, B


#### 2. Regarding tries built for NID numbers (9 decimal digits), which of the following are true?  
A) ✓ A 10-way trie has height ≤ 10, since each digit corresponds to one level.  
B) ✓ A 100-way trie has height ≤ 6, due to grouping digits and reducing height.  
C) ✓ Red-black tree height is about 2 log2(10^9) ≈ 60, as stated.  
D) ✗ AVL tree height is about 1.44 log2(10^9) ≈ 40, not 30.

**Correct:** A, B, C


#### 3. When handling variable length keys in tries, what techniques are used to avoid prefix ambiguity?  
A) ✓ Adding a special end-of-key character (#) distinguishes keys that are prefixes of others.  
B) ✗ Compressed tries remove degree-1 nodes but do not solve prefix ambiguity directly.  
C) ✓ Expanding shorter prefixes to node stride length is used in multibit tries to handle prefix lengths.  
D) ✗ Storing keys only if same length is not practical and not a technique mentioned.

**Correct:** A, C


#### 4. In multibit tries, which of the following statements are correct?  
A) ✓ Node stride s determines how many bits are used for branching at that node.  
B) ✓ Node with stride s has 2^s children and 2^s element/prefix fields.  
C) ✗ Nodes can have variable strides; they do not all have to be the same.  
D) ✓ Short prefixes are expanded to the node’s stride length to maintain consistency.

**Correct:** A, B, D


#### 5. Which of the following are valid reasons why TCAMs (Ternary Content Addressable Memories) are limited in router implementations?  
A) ✓ High power consumption is a known limitation of TCAMs.  
B) ✓ Scalability to IPv6 (longer prefixes) is problematic for TCAMs.  
C) ✗ TCAMs can perform longest prefix matching; this is one of their strengths.  
D) ✓ High cost and board space requirements limit TCAM deployment.

**Correct:** A, B, D


#### 6. Consider the problem of fixed-stride tries. Which of the following statements are true?  
A) ✓ Number of levels equals the number of distinct prefix lengths in fixed-stride tries.  
B) ✓ Prefix expansion reduces the number of distinct prefix lengths by normalizing them.  
C) ✗ Fixed-stride tries do not always have fewer levels than variable-stride tries; variable strides can reduce height.  
D) ✓ The optimization problem is to find the least memory fixed-stride trie with height ≤ k.

**Correct:** A, B, D


#### 7. Which of the following correctly describe tie-breaking rules in router rule tables?  
A) ✓ First matching rule can be a tie-breaker in some implementations.  
B) ✓ Highest-priority rule is often used to break ties.  
C) ✓ Most-specific rule means the smallest range or most precise match.  
D) ✓ Longest-prefix rule selects the rule with the longest matching prefix.

**Correct:** A, B, C, D


#### 8. In the context of tries with edge information, what is the purpose of adding a pointer field to each branch node?  
A) ✓ Points to an element node in the subtree to reconstruct skipped characters on the path.  
B) ✗ Bit# or char# fields are separate from this pointer; this pointer is for element reference.  
C) ✗ It does not directly reduce height but helps recover skipped information.  
D) ✗ Number of non-null pointers is a different field (#ptr), not this pointer.

**Correct:** A


#### 9. Which of the following statements about 2-dimensional tries and filters are correct?  
A) ✓ They handle destination-source address pairs for filtering packets.  
B) ✓ Tie-breaking can be based on least cost among matching rules.  
C) ✗ They are not limited to 1-bit branching; multibit versions exist.  
D) ✓ They can be implemented as 2D multibit tries.

**Correct:** A, B, D


#### 10. Regarding the complexity and performance of 1-bit and multibit tries, which statements are accurate?  
A) ✓ 1-bit tries have O(W) complexity per operation, where W is key length in bits.  
B) ✓ Multibit tries reduce height by increasing stride at nodes, improving efficiency.  
C) ✗ Fixed-stride tries do not always outperform variable-stride tries in memory usage; variable strides can be more memory efficient.  
D) ✓ Multibit tries are well-suited for longest prefix matching in Internet routing.

**Correct:** A, B, D