## 13. Compressed and Multibit Tries

## Questions

#### 1. Which of the following statements about compressed binary tries are true?  
A) No branch node has degree 1 in a compressed binary trie.  
B) Each branch node contains a bit# field indicating which bit to branch on.  
C) Compressed binary tries always have the same height as uncompressed binary tries.  
D) The number of branch nodes in a compressed binary trie is equal to the number of keys.  

#### 2. In a 10-way trie built for 9-digit decimal keys (NID numbers), which of the following are correct?  
A) Searching requires at most 9 branch traversals plus one final comparison.  
B) The trie nodes have 2 children each.  
C) Increasing the order of the trie to 100 reduces the height to at most 6.  
D) The height of the trie is at most 10.  

#### 3. Comparing search complexity, which of the following statements are accurate?  
A) A perfectly balanced binary tree storing the keys has height about 30.  
B) A red-black tree storing 9-digit decimal keys has height approximately 60.  
C) A 100-way trie has higher search complexity than a red-black tree for the same keys.  
D) An AVL tree storing the same keys has height approximately 40.  

#### 4. In a compressed NID trie, what does the char# field represent?  
A) The total number of keys stored in the subtree rooted at that node.  
B) The character or digit used for branching at that node.  
C) The number of non-null pointers in the node.  
D) The bit position used for branching.  

#### 5. When inserting variable length keys into a trie, what problem arises if one key is a proper prefix of another?  
A) The trie height becomes unbounded.  
B) The trie nodes must be converted to multibit nodes.  
C) The search may incorrectly terminate early.  
D) The trie cannot distinguish between the keys without additional information.  

#### 6. How does adding a special end-of-key character (#) to keys solve the prefix problem in tries?  
A) It allows keys to be stored in compressed form.  
B) It eliminates the need for bit# or char# fields.  
C) It marks the end of a key explicitly, preventing ambiguity.  
D) It reduces the height of the trie.  

#### 7. What is the purpose of adding an element field to each branch node in a trie with edge information?  
A) To store the bit# used for branching.  
B) To point to an element node in the subtree for skipped characters.  
C) To speed up prefix matching by storing subtree summaries.  
D) To reduce the number of children per node.  

#### 8. Which of the following are true about multibit tries?  
A) Each node with stride s has 2^s children.  
B) The stride (number of bits used for branching) can vary from node to node.  
C) Prefixes shorter than the node stride are expanded to the node stride length.  
D) Multibit tries cannot be used for longest prefix matching.  

#### 9. In multibit tries, what happens when a prefix P = 00* is expanded to P0 = 000* and P1 = 001* but Q = 000* already exists?  
A) Both P0 and P1 are kept to preserve all prefixes.  
B) P0 is eliminated because Q represents a longer match.  
C) P1 is eliminated because it conflicts with Q.  
D) The trie height increases by one level.  

#### 10. Which of the following are typical applications of multibit tries?  
A) Prefix search in routing tables.  
B) Automatic command or URL completion.  
C) Balanced binary search trees.  
D) LZW compression.  

#### 11. Regarding router rule tables, which statements are correct?  
A) Tie breakers can be based on first matching rule, highest priority, or longest prefix.  
B) Rules can be specified as address/mask pairs representing ranges.  
C) Router rules always have a fixed size of less than 1,000 entries.  
D) Prefix filters are a special case of range filters with masks having 1s on the left and 0s on the right.  

#### 12. Why are log2 n schemes problematic for router rule tables with over 1 million rules?  
A) They require too many memory accesses, impacting performance.  
B) They consume excessive power and board space.  
C) They cannot handle IPv6 addresses.  
D) They do not support longest prefix matching.  

#### 13. Which of the following are limitations of Ternary Content Addressable Memories (TCAMs) in router implementations?  
A) High power consumption.  
B) Difficulty scaling to IPv6 address sizes.  
C) Inability to perform longest prefix matching.  
D) Limited capacity and high cost.  

#### 14. What is the complexity of a 1-bit trie operation in terms of W, the key length?  
A) O(1)  
B) O(W^2)  
C) O(log W)  
D) O(W)  

#### 15. In fixed-stride tries, which of the following are true?  
A) Nodes at the same level can have different stride lengths.  
B) Prefix expansion can reduce the number of distinct prefix lengths.  
C) Fixed-stride tries always have fewer nodes than variable-stride tries.  
D) The number of levels equals the number of distinct prefix lengths.  

#### 16. The fixed-stride trie optimization problem involves which of the following goals?  
A) Minimizing memory usage while bounding trie height by k.  
B) Minimizing the number of nodes regardless of height.  
C) Maximizing the number of distinct prefix lengths.  
D) Ensuring all nodes have stride 1.  

#### 17. Two-dimensional filters in tries are used to filter based on which of the following?  
A) Destination-source address pairs.  
B) Packet payload content.  
C) Destination address only.  
D) Source address only.  

#### 18. In two-dimensional tries, what is a least-cost tie breaker?  
A) Selecting the rule with the lowest associated cost among overlapping matches.  
B) Always choosing the first matching rule.  
C) Choosing the rule with the smallest numeric priority.  
D) Selecting the rule that matches the fewest packets.  

#### 19. Which of the following statements about multibit tries with variable stride are correct?  
A) Variable stride tries can reduce trie height compared to fixed stride tries.  
B) Variable stride tries require all nodes to have the same number of children.  
C) Variable stride tries are not suitable for prefix expansion.  
D) Nodes on the same level can have different stride lengths.  

#### 20. Regarding longest prefix matching in router tables, which are true?  
A) It can be implemented efficiently using multibit tries.  
B) It always results in multiple matching rules being applied simultaneously.  
C) It selects the rule with the longest matching prefix for a given destination.  
D) It is a special case of highest-priority matching.  



<br>

## Answers

#### 1. Which of the following statements about compressed binary tries are true?  
A) ✓ No branch node has degree 1 in a compressed binary trie, as such nodes are compressed away.  
B) ✓ Each branch node contains a bit# field indicating which bit to branch on, essential for navigation.  
C) ✗ Compressed tries usually have smaller height than uncompressed tries due to compression.  
D) ✗ The number of branch nodes is n - 1, not equal to the number of keys n.  

**Correct:** A, B


#### 2. In a 10-way trie built for 9-digit decimal keys (NID numbers), which of the following are correct?  
A) ✓ Search requires ≤ 9 branch traversals plus one final compare to confirm key.  
B) ✗ Nodes have up to 10 children, not 2 (binary).  
C) ✓ Increasing order to 100 reduces height to ≤ 6 by grouping digits.  
D) ✓ Height ≤ 10 because each digit corresponds to one level.  

**Correct:** A, C, D


#### 3. Comparing search complexity, which of the following statements are accurate?  
A) ✓ Perfectly balanced binary tree height ~ log2(10^9) ≈ 30.  
B) ✓ Red-black tree height ~ 2 log2(10^9) ≈ 60.  
C) ✗ 100-way trie has lower height and search complexity than red-black tree.  
D) ✓ AVL tree height ~ 1.44 log2(10^9) ≈ 40.  

**Correct:** A, B, D


#### 4. In a compressed NID trie, what does the char# field represent?  
A) ✗ char# does not represent the total number of keys in the subtree.  
B) ✓ The character/digit used for branching at that node, analogous to bit# in binary tries.  
C) ✓ #ptr is the number of non-null pointers in the node, also stored.  
D) ✗ bit# is used in binary tries, not char# in NID tries.  

**Correct:** B, C


#### 5. When inserting variable length keys into a trie, what problem arises if one key is a proper prefix of another?  
A) ✗ Trie height is not necessarily unbounded due to prefix.  
B) ✗ Conversion to multibit nodes is unrelated to prefix problem.  
C) ✓ Search may terminate early, confusing prefix key with longer key.  
D) ✓ Trie cannot distinguish keys without explicit end marker.  

**Correct:** C, D


#### 6. How does adding a special end-of-key character (#) to keys solve the prefix problem in tries?  
A) ✗ Does not compress keys.  
B) ✗ Bit# or char# fields are still needed for branching.  
C) ✓ Marks end of key explicitly, preventing ambiguity between prefix and longer keys.  
D) ✗ Does not reduce trie height.  

**Correct:** C


#### 7. What is the purpose of adding an element field to each branch node in a trie with edge information?  
A) ✗ Bit# is a separate field, not the element field.  
B) ✓ Points to an element node in subtree to recover skipped characters during traversal.  
C) ✗ Does not store subtree summaries, only a pointer to an element.  
D) ✗ Does not reduce number of children.  

**Correct:** B


#### 8. Which of the following are true about multibit tries?  
A) ✓ Node with stride s has 2^s children.  
B) ✓ Stride can vary from node to node (variable stride).  
C) ✓ Short prefixes are expanded to node stride length for uniform branching.  
D) ✗ Multibit tries are designed for longest prefix matching.  

**Correct:** A, B, C


#### 9. In multibit tries, what happens when a prefix P = 00* is expanded to P0 = 000* and P1 = 001* but Q = 000* already exists?  
A) ✗ Both are not kept; P0 is removed to avoid redundancy.  
B) ✓ P0 is eliminated because Q is a longer, more specific prefix.  
C) ✗ P1 is not eliminated; it remains valid.  
D) ✗ Trie height does not increase due to this expansion.  

**Correct:** B


#### 10. Which of the following are typical applications of multibit tries?  
A) ✓ Prefix search in routing tables is a primary application.  
B) ✓ Automatic command or URL completion uses prefix matching.  
C) ✗ Balanced binary search trees are unrelated to multibit tries.  
D) ✓ LZW compression uses tries for dictionary representation.  

**Correct:** A, B, D


#### 11. Regarding router rule tables, which statements are correct?  
A) ✓ Tie breakers include first matching, highest priority, and longest prefix.  
B) ✓ Rules can be address/mask pairs representing ranges of addresses.  
C) ✗ Router tables can have over 1 million entries, not always small.  
D) ✓ Prefix filters are special cases with masks having 1s on left and 0s on right.  

**Correct:** A, B, D


#### 12. Why are log2 n schemes problematic for router rule tables with over 1 million rules?  
A) ✓ They require many memory accesses, hurting performance at high speeds.  
B) ✗ Power and board space issues are more related to hardware like TCAMs.  
C) ✗ They can handle IPv6 but with difficulty; not the main problem here.  
D) ✗ They do support longest prefix matching.  

**Correct:** A


#### 13. Which of the following are limitations of Ternary Content Addressable Memories (TCAMs) in router implementations?  
A) ✓ High power consumption is a known limitation.  
B) ✓ Scaling to IPv6 (128-bit prefixes) is challenging.  
C) ✗ TCAMs inherently support longest prefix matching.  
D) ✓ Limited capacity and high cost are major issues.  

**Correct:** A, B, D


#### 14. What is the complexity of a 1-bit trie operation in terms of W, the key length?  
A) ✗ O(1) is too optimistic; traversal depends on key length.  
B) ✗ O(W^2) is too pessimistic.  
C) ✗ O(log W) is incorrect; tries do not use logarithmic search.  
D) ✓ O(W) because each bit of the key is examined once.  

**Correct:** D


#### 15. In fixed-stride tries, which of the following are true?  
A) ✗ Nodes at same level have same stride by definition of fixed-stride tries.  
B) ✓ Prefix expansion reduces distinct prefix lengths by grouping prefixes.  
C) ✗ Fixed-stride tries do not always have fewer nodes than variable-stride tries.  
D) ✓ Number of levels equals number of distinct prefix lengths after expansion.  

**Correct:** B, D


#### 16. The fixed-stride trie optimization problem involves which of the following goals?  
A) ✓ Minimize memory usage while bounding trie height by k.  
B) ✗ Minimizing nodes regardless of height can lead to tall tries.  
C) ✗ Maximizing distinct prefix lengths is counterproductive.  
D) ✗ Forcing stride 1 everywhere is not an optimization goal.  

**Correct:** A


#### 17. Two-dimensional filters in tries are used to filter based on which of the following?  
A) ✓ Destination-source address pairs require 2D filtering.  
B) ✗ Packet payload content is not handled by these tries.  
C) ✗ Destination only is one-dimensional filtering.  
D) ✗ Source only is one-dimensional filtering.  

**Correct:** A


#### 18. In two-dimensional tries, what is a least-cost tie breaker?  
A) ✓ Selecting rule with lowest associated cost among overlapping matches.  
B) ✗ Always choosing first matching rule is a different tie breaker.  
C) ✗ Smallest numeric priority is not necessarily least cost.  
D) ✗ Matching fewest packets is unrelated to cost.  

**Correct:** A


#### 19. Which of the following statements about multibit tries with variable stride are correct?  
A) ✓ Variable stride tries can reduce trie height compared to fixed stride tries.  
B) ✗ Nodes do not require same number of children; children count depends on stride.  
C) ✗ Variable stride tries can use prefix expansion; not unsuitable.  
D) ✓ Nodes on same level can have different stride lengths in variable stride tries.  

**Correct:** A, D


#### 20. Regarding longest prefix matching in router tables, which are true?  
A) ✓ Multibit tries can implement longest prefix matching efficiently.  
B) ✗ It results in a single best match, not multiple rules applied simultaneously.  
C) ✓ It selects the rule with the longest matching prefix for a destination.  
D) ✗ It is not a special case of highest-priority matching; they are different criteria.  

**Correct:** A, C