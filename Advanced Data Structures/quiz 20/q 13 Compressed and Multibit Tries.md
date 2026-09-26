## 13. Compressed and Multibit Tries

## Questions

#### 1. Which of the following statements about compressed binary tries are true?  
A) No branch node has degree 1 in a compressed binary trie.  
B) Each branch node contains a bit# field indicating which bit to branch on.  
C) The number of branch nodes in a compressed binary trie is equal to the number of keys.  
D) Compressed binary tries always have the same height as uncompressed binary tries.  

#### 2. In a 10-way trie built for 9-digit decimal keys (NID numbers), which of the following are correct?  
A) The height of the trie is at most 10.  
B) Searching requires at most 9 branch traversals plus one final comparison.  
C) The trie nodes have 2 children each.  
D) Increasing the order of the trie to 100 reduces the height to at most 6.  

#### 3. Comparing search complexity, which of the following statements are accurate?  
A) A red-black tree storing 9-digit decimal keys has height approximately 60.  
B) An AVL tree storing the same keys has height approximately 40.  
C) A perfectly balanced binary tree storing the keys has height about 30.  
D) A 100-way trie has higher search complexity than a red-black tree for the same keys.  

#### 4. In a compressed NID trie, what does the char# field represent?  
A) The character or digit used for branching at that node.  
B) The number of non-null pointers in the node.  
C) The bit position used for branching.  
D) The total number of keys stored in the subtree rooted at that node.  

#### 5. When inserting variable length keys into a trie, what problem arises if one key is a proper prefix of another?  
A) The trie height becomes unbounded.  
B) The search may incorrectly terminate early.  
C) The trie cannot distinguish between the keys without additional information.  
D) The trie nodes must be converted to multibit nodes.  

#### 6. How does adding a special end-of-key character (#) to keys solve the prefix problem in tries?  
A) It marks the end of a key explicitly, preventing ambiguity.  
B) It reduces the height of the trie.  
C) It allows keys to be stored in compressed form.  
D) It eliminates the need for bit# or char# fields.  

#### 7. What is the purpose of adding an element field to each branch node in a trie with edge information?  
A) To point to an element node in the subtree for skipped characters.  
B) To store the bit# used for branching.  
C) To reduce the number of children per node.  
D) To speed up prefix matching by storing subtree summaries.  

#### 8. Which of the following are true about multibit tries?  
A) The stride (number of bits used for branching) can vary from node to node.  
B) Each node with stride s has 2^s children.  
C) Prefixes shorter than the node stride are expanded to the node stride length.  
D) Multibit tries cannot be used for longest prefix matching.  

#### 9. In multibit tries, what happens when a prefix P = 00* is expanded to P0 = 000* and P1 = 001* but Q = 000* already exists?  
A) P0 is eliminated because Q represents a longer match.  
B) P1 is eliminated because it conflicts with Q.  
C) Both P0 and P1 are kept to preserve all prefixes.  
D) The trie height increases by one level.  

#### 10. Which of the following are typical applications of multibit tries?  
A) Prefix search in routing tables.  
B) Automatic command or URL completion.  
C) LZW compression.  
D) Balanced binary search trees.  

#### 11. Regarding router rule tables, which statements are correct?  
A) Rules can be specified as address/mask pairs representing ranges.  
B) Prefix filters are a special case of range filters with masks having 1s on the left and 0s on the right.  
C) Router rules always have a fixed size of less than 1,000 entries.  
D) Tie breakers can be based on first matching rule, highest priority, or longest prefix.  

#### 12. Why are log2 n schemes problematic for router rule tables with over 1 million rules?  
A) They require too many memory accesses, impacting performance.  
B) They cannot handle IPv6 addresses.  
C) They do not support longest prefix matching.  
D) They consume excessive power and board space.  

#### 13. Which of the following are limitations of Ternary Content Addressable Memories (TCAMs) in router implementations?  
A) Limited capacity and high cost.  
B) High power consumption.  
C) Difficulty scaling to IPv6 address sizes.  
D) Inability to perform longest prefix matching.  

#### 14. What is the complexity of a 1-bit trie operation in terms of W, the key length?  
A) O(1)  
B) O(W)  
C) O(log W)  
D) O(W^2)  

#### 15. In fixed-stride tries, which of the following are true?  
A) The number of levels equals the number of distinct prefix lengths.  
B) Prefix expansion can reduce the number of distinct prefix lengths.  
C) Nodes at the same level can have different stride lengths.  
D) Fixed-stride tries always have fewer nodes than variable-stride tries.  

#### 16. The fixed-stride trie optimization problem involves which of the following goals?  
A) Minimizing memory usage while bounding trie height by k.  
B) Maximizing the number of distinct prefix lengths.  
C) Minimizing the number of nodes regardless of height.  
D) Ensuring all nodes have stride 1.  

#### 17. Two-dimensional filters in tries are used to filter based on which of the following?  
A) Destination address only.  
B) Source address only.  
C) Destination-source address pairs.  
D) Packet payload content.  

#### 18. In two-dimensional tries, what is a least-cost tie breaker?  
A) Choosing the rule with the smallest numeric priority.  
B) Selecting the rule that matches the fewest packets.  
C) Selecting the rule with the lowest associated cost among overlapping matches.  
D) Always choosing the first matching rule.  

#### 19. Which of the following statements about multibit tries with variable stride are correct?  
A) Nodes on the same level can have different stride lengths.  
B) Variable stride tries can reduce trie height compared to fixed stride tries.  
C) Variable stride tries require all nodes to have the same number of children.  
D) Variable stride tries are not suitable for prefix expansion.  

#### 20. Regarding longest prefix matching in router tables, which are true?  
A) It selects the rule with the longest matching prefix for a given destination.  
B) It is a special case of highest-priority matching.  
C) It can be implemented efficiently using multibit tries.  
D) It always results in multiple matching rules being applied simultaneously.



<br>

## Answers

#### 1. Which of the following statements about compressed binary tries are true?  
A) ✓ No branch node has degree 1 in a compressed binary trie, as such nodes are compressed away.  
B) ✓ Each branch node contains a bit# field indicating which bit to branch on, essential for navigation.  
C) ✗ The number of branch nodes is n - 1, not equal to the number of keys n.  
D) ✗ Compressed tries usually have smaller height than uncompressed tries due to compression.  

**Correct:** A,B


#### 2. In a 10-way trie built for 9-digit decimal keys (NID numbers), which of the following are correct?  
A) ✓ Height ≤ 10 because each digit corresponds to one level.  
B) ✓ Search requires ≤ 9 branch traversals plus one final compare to confirm key.  
C) ✗ Nodes have up to 10 children, not 2 (binary).  
D) ✓ Increasing order to 100 reduces height to ≤ 6 by grouping digits.  

**Correct:** A,B,D


#### 3. Comparing search complexity, which of the following statements are accurate?  
A) ✓ Red-black tree height ~ 2 log2(10^9) ≈ 60.  
B) ✓ AVL tree height ~ 1.44 log2(10^9) ≈ 40.  
C) ✓ Perfectly balanced binary tree height ~ log2(10^9) ≈ 30.  
D) ✗ 100-way trie has lower height and search complexity than red-black tree.  

**Correct:** A,B,C


#### 4. In a compressed NID trie, what does the char# field represent?  
A) ✓ The character/digit used for branching at that node, analogous to bit# in binary tries.  
B) ✓ #ptr is the number of non-null pointers in the node, also stored.  
C) ✗ bit# is used in binary tries, not char# in NID tries.  
D) ✗ char# does not represent the total number of keys in the subtree.  

**Correct:** A,B


#### 5. When inserting variable length keys into a trie, what problem arises if one key is a proper prefix of another?  
A) ✗ Trie height is not necessarily unbounded due to prefix.  
B) ✓ Search may terminate early, confusing prefix key with longer key.  
C) ✓ Trie cannot distinguish keys without explicit end marker.  
D) ✗ Conversion to multibit nodes is unrelated to prefix problem.  

**Correct:** B,C


#### 6. How does adding a special end-of-key character (#) to keys solve the prefix problem in tries?  
A) ✓ Marks end of key explicitly, preventing ambiguity between prefix and longer keys.  
B) ✗ Does not reduce trie height.  
C) ✗ Does not compress keys.  
D) ✗ Bit# or char# fields are still needed for branching.  

**Correct:** A


#### 7. What is the purpose of adding an element field to each branch node in a trie with edge information?  
A) ✓ Points to an element node in subtree to recover skipped characters during traversal.  
B) ✗ Bit# is a separate field, not the element field.  
C) ✗ Does not reduce number of children.  
D) ✗ Does not store subtree summaries, only a pointer to an element.  

**Correct:** A


#### 8. Which of the following are true about multibit tries?  
A) ✓ Stride can vary from node to node (variable stride).  
B) ✓ Node with stride s has 2^s children.  
C) ✓ Short prefixes are expanded to node stride length for uniform branching.  
D) ✗ Multibit tries are designed for longest prefix matching.  

**Correct:** A,B,C


#### 9. In multibit tries, what happens when a prefix P = 00* is expanded to P0 = 000* and P1 = 001* but Q = 000* already exists?  
A) ✓ P0 is eliminated because Q is a longer, more specific prefix.  
B) ✗ P1 is not eliminated; it remains valid.  
C) ✗ Both are not kept; P0 is removed to avoid redundancy.  
D) ✗ Trie height does not increase due to this expansion.  

**Correct:** A


#### 10. Which of the following are typical applications of multibit tries?  
A) ✓ Prefix search in routing tables is a primary application.  
B) ✓ Automatic command or URL completion uses prefix matching.  
C) ✓ LZW compression uses tries for dictionary representation.  
D) ✗ Balanced binary search trees are unrelated to multibit tries.  

**Correct:** A,B,C


#### 11. Regarding router rule tables, which statements are correct?  
A) ✓ Rules can be address/mask pairs representing ranges of addresses.  
B) ✓ Prefix filters are special cases with masks having 1s on left and 0s on right.  
C) ✗ Router tables can have over 1 million entries, not always small.  
D) ✓ Tie breakers include first matching, highest priority, and longest prefix.  

**Correct:** A,B,D


#### 12. Why are log2 n schemes problematic for router rule tables with over 1 million rules?  
A) ✓ They require many memory accesses, hurting performance at high speeds.  
B) ✗ They can handle IPv6 but with difficulty; not the main problem here.  
C) ✗ They do support longest prefix matching.  
D) ✗ Power and board space issues are more related to hardware like TCAMs.  

**Correct:** A


#### 13. Which of the following are limitations of Ternary Content Addressable Memories (TCAMs) in router implementations?  
A) ✓ Limited capacity and high cost are major issues.  
B) ✓ High power consumption is a known limitation.  
C) ✓ Scaling to IPv6 (128-bit prefixes) is challenging.  
D) ✗ TCAMs inherently support longest prefix matching.  

**Correct:** A,B,C


#### 14. What is the complexity of a 1-bit trie operation in terms of W, the key length?  
A) ✗ O(1) is too optimistic; traversal depends on key length.  
B) ✓ O(W) because each bit of the key is examined once.  
C) ✗ O(log W) is incorrect; tries do not use logarithmic search.  
D) ✗ O(W^2) is too pessimistic.  

**Correct:** B


#### 15. In fixed-stride tries, which of the following are true?  
A) ✓ Number of levels equals number of distinct prefix lengths after expansion.  
B) ✓ Prefix expansion reduces distinct prefix lengths by grouping prefixes.  
C) ✗ Nodes at same level have same stride by definition of fixed-stride tries.  
D) ✗ Fixed-stride tries do not always have fewer nodes than variable-stride tries.  

**Correct:** A,B


#### 16. The fixed-stride trie optimization problem involves which of the following goals?  
A) ✓ Minimize memory usage while bounding trie height by k.  
B) ✗ Maximizing distinct prefix lengths is counterproductive.  
C) ✗ Minimizing nodes regardless of height can lead to tall tries.  
D) ✗ Forcing stride 1 everywhere is not an optimization goal.  

**Correct:** A


#### 17. Two-dimensional filters in tries are used to filter based on which of the following?  
A) ✗ Destination only is one-dimensional filtering.  
B) ✗ Source only is one-dimensional filtering.  
C) ✓ Destination-source address pairs require 2D filtering.  
D) ✗ Packet payload content is not handled by these tries.  

**Correct:** C


#### 18. In two-dimensional tries, what is a least-cost tie breaker?  
A) ✗ Smallest numeric priority is not necessarily least cost.  
B) ✗ Matching fewest packets is unrelated to cost.  
C) ✓ Selecting rule with lowest associated cost among overlapping matches.  
D) ✗ Always choosing first matching rule is a different tie breaker.  

**Correct:** C


#### 19. Which of the following statements about multibit tries with variable stride are correct?  
A) ✓ Nodes on same level can have different stride lengths in variable stride tries.  
B) ✓ Variable stride tries can reduce trie height compared to fixed stride tries.  
C) ✗ Nodes do not require same number of children; children count depends on stride.  
D) ✗ Variable stride tries can use prefix expansion; not unsuitable.  

**Correct:** A,B


#### 20. Regarding longest prefix matching in router tables, which are true?  
A) ✓ It selects the rule with the longest matching prefix for a destination.  
B) ✗ It is not a special case of highest-priority matching; they are different criteria.  
C) ✓ Multibit tries can implement longest prefix matching efficiently.  
D) ✗ It results in a single best match, not multiple rules applied simultaneously.  

**Correct:** A,C