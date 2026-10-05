## 14. Suffix Trees

## Questions

#### 1. Which of the following statements correctly describe a substring of a string S?  
A) A substring must always start at the first character of S.  
B) A substring is composed of consecutive characters from S between indices i and j, where i ≤ j.  
C) The empty string is considered a substring of S.  
D) A substring can be formed by characters in S at indices i1 < i2 < ... < ik, not necessarily consecutive.  

#### 2. Which of the following are true about subsequences of a string S?  
A) The empty string is a subsequence of S.  
B) Every substring is also a subsequence.  
C) A subsequence must be contiguous in S.  
D) A subsequence is formed by characters of S at strictly increasing indices.  

#### 3. Regarding string/pattern matching, which statements are correct?  
A) Knuth-Morris-Pratt (KMP) algorithm preprocesses the source string S.  
B) KMP runs in O(|S| + |pi|) time per query.  
C) Suffix trees preprocess the query strings pi, not the source string S.  
D) Using suffix trees, multiple queries can be answered in O(|S| + Σ|pi|) time.  

#### 4. Which of the following correctly describe suffix trees?  
A) Each edge in a suffix tree stores a substring of S.  
B) Suffix trees can be used to find if a pattern pi is a substring of S.  
C) A suffix tree is a compressed trie built from all nonempty suffixes of a string S.  
D) The keys in a suffix tree are all substrings of S.  

#### 5. Consider the string S = "sleeper". Which of the following are suffixes of S?  
A) "per"  
B) "leeper"  
C) "leep"  
D) "sleeper"  

#### 6. Why is it necessary to append a unique end-of-string character (e.g., '#') to S when building a suffix tree?  
A) To handle cases where the last character of S repeats multiple times.  
B) To reduce the size of the suffix tree.  
C) To allow suffix trees to handle empty strings.  
D) To ensure no suffix is a prefix of another suffix.  

#### 7. Which of the following are true about the time complexity of suffix tree construction?  
A) For constant alphabet size, suffix tree construction is O(n).  
B) Using array nodes, the complexity is O(nr), where n = |S| and r = alphabet size.  
C) Suffix tree construction always takes O(n²) time.  
D) Compressing tries is the only method to build suffix trees.  

#### 8. When searching for a pattern pi in a suffix tree, what does it mean if the search terminates at an element (leaf) node?  
A) pi is a prefix of some suffix of S.  
B) pi is not a substring of S.  
C) pi appears exactly once in S.  
D) pi appears multiple times in S.  

#### 9. If the search for pi in a suffix tree ends at a branch node, which of the following are true?  
A) Each leaf node in the subtree rooted at this branch node corresponds to a different occurrence of pi.  
B) The number of occurrences of pi equals the number of leaf nodes in that subtree.  
C) pi is not a substring of S.  
D) pi appears multiple times in S.  

#### 10. How can suffix trees be augmented to find all occurrences of a pattern pi efficiently?  
A) Precompute all substrings of S and store their positions.  
B) Link all leaf nodes into a chain in inorder.  
C) Each branch node stores pointers to the leftmost and rightmost leaf nodes in its subtree.  
D) Store the count of occurrences at each node.  

#### 11. Which of the following correctly describe the longest repeating substring problem?  
A) Branch nodes are labeled with the number of leaf nodes in their subtree.  
B) The longest repeating substring corresponds to the branch node with the smallest label.  
C) The maximum length substring with label ≥ m (m > 1) is the answer.  
D) It finds the longest substring occurring more than once in S.  

#### 12. Given two strings S and T, which of the following statements about longest common substring and longest common subsequence are true?  
A) The longest common substring can be found in O(|S| + |T|) time using suffix trees.  
B) The longest common subsequence may contain characters not contiguous in S or T.  
C) The longest common subsequence can be found in O(|S| * |T|) time using dynamic programming.  
D) The longest common substring is always longer than the longest common subsequence.  

#### 13. For the strings S = "carport" and T = "airports", which of the following are correct?  
A) "airport" is a longest common subsequence.  
B) "car" is a longest common substring.  
C) The longest common substring is "rport".  
D) The longest common subsequence is "arport".  

#### 14. How can the longest common substring of two strings S and T be found using suffix trees?  
A) Build separate suffix trees for S and T and compare them.  
B) Construct the suffix tree for the concatenated string U = S$T#, where $ and # are unique delimiters.  
C) Use dynamic programming on the suffix tree edges.  
D) Search for the longest path in the suffix tree that contains suffixes from both S and T.  

#### 15. Which of the following are true about the relationship between substrings and suffixes?  
A) Every suffix of S is also a substring of S.  
B) A substring pi of S is a prefix of some suffix of S.  
C) A suffix is always a substring starting at index 1.  
D) Every substring of S is a suffix of S.  

#### 16. What problem arises if the last character of S appears multiple times and no unique end character is appended?  
A) The suffix tree will have cycles.  
B) The suffix tree cannot be constructed.  
C) The suffix tree will have duplicate leaves.  
D) Some suffixes become prefixes of other suffixes, causing ambiguity in the suffix tree.  

#### 17. Which of the following are valid suffixes of the string "creeper"?  
A) "eeper"  
B) "eper"  
C) "creeper"  
D) "reeper"  

#### 18. Which of the following statements about suffix arrays and enhanced suffix arrays are true?  
A) They store sorted suffixes of S in an array.  
B) Enhanced suffix arrays include additional data structures to speed up queries.  
C) They require more space than suffix trees.  
D) They are alternatives to suffix trees for substring queries.  

#### 19. Which of the following are advantages of suffix trees over KMP for multiple pattern queries?  
A) KMP preprocesses each query string separately, leading to higher total time for many queries.  
B) Suffix trees preprocess the source string once, allowing multiple queries efficiently.  
C) KMP is faster than suffix trees for large alphabets.  
D) Suffix trees can answer substring queries in O(|pi|) time after preprocessing.  

#### 20. In the context of suffix trees, what does the "max char#" field represent when finding the longest repeating substring?  
A) The maximum character code in the substring.  
B) The maximum depth of the branch node in the suffix tree.  
C) The length of the substring represented by the branch node.  
D) The maximum number of occurrences of the substring.  



<br>

## Answers

#### 1. Which of the following statements correctly describe a substring of a string S?  
A) ✗ A substring can start anywhere, not necessarily at the first character.  
B) ✓ A substring is composed of consecutive characters from S between indices i and j, where i ≤ j.  
C) ✓ The empty string is considered a substring of S.  
D) ✗ This describes a subsequence, not a substring.  

**Correct:** B, C


#### 2. Which of the following are true about subsequences of a string S?  
A) ✓ The empty string is a subsequence of S.  
B) ✓ Every substring is also a subsequence (since substrings are contiguous subsequences).  
C) ✗ A subsequence need not be contiguous.  
D) ✓ A subsequence is formed by characters of S at strictly increasing indices.  

**Correct:** A, B, D


#### 3. Regarding string/pattern matching, which statements are correct?  
A) ✗ KMP preprocesses the query string pi, not the source string S.  
B) ✓ KMP runs in O(|S| + |pi|) time per query.  
C) ✗ Suffix trees preprocess the source string S, not the queries.  
D) ✓ Using suffix trees, multiple queries can be answered in O(|S| + Σ|pi|) time.  

**Correct:** B, D


#### 4. Which of the following correctly describe suffix trees?  
A) ✓ Each edge stores a substring (edge label) of S.  
B) ✓ Suffix trees can be used to find if a pattern pi is a substring of S.  
C) ✓ A suffix tree is a compressed trie built from all nonempty suffixes of a string S.  
D) ✗ Keys are suffixes, not all substrings.  

**Correct:** A, B, C


#### 5. Consider the string S = "sleeper". Which of the following are suffixes of S?  
A) ✓ "per" is a suffix starting at index 5.  
B) ✓ "leeper" is suffix starting at index 2.  
C) ✗ "leep" is not a suffix (not from an index to the end).  
D) ✓ "sleeper" is the full string, hence a suffix.  

**Correct:** A, B, D


#### 6. Why is it necessary to append a unique end-of-string character (e.g., '#') to S when building a suffix tree?  
A) ✓ To handle cases where the last character repeats multiple times.  
B) ✗ It does not reduce size; it ensures uniqueness.  
C) ✗ The empty string is always a substring; this is unrelated.  
D) ✓ To ensure no suffix is a prefix of another suffix, avoiding ambiguity.  

**Correct:** A, D


#### 7. Which of the following are true about the time complexity of suffix tree construction?  
A) ✓ For constant alphabet size, construction is O(n).  
B) ✓ Using array nodes, complexity is O(nr), where r is alphabet size.  
C) ✗ Construction is not always O(n²).  
D) ✗ There are better methods than compressing tries (e.g., Ukkonen’s algorithm).  

**Correct:** A, B


#### 8. When searching for a pattern pi in a suffix tree, what does it mean if the search terminates at an element (leaf) node?  
A) ✓ pi is a prefix of some suffix of S (by definition).  
B) ✗ pi is a substring, so search would not fail.  
C) ✓ pi appears exactly once in S.  
D) ✗ Multiple occurrences would end at a branch node, not a leaf.  

**Correct:** A, C


#### 9. If the search for pi in a suffix tree ends at a branch node, which of the following are true?  
A) ✓ Each leaf in the subtree corresponds to a different occurrence of pi.  
B) ✓ Number of occurrences equals number of leaf nodes in that subtree.  
C) ✗ pi is a substring, so search does not fail.  
D) ✓ pi appears multiple times in S.  

**Correct:** A, B, D


#### 10. How can suffix trees be augmented to find all occurrences of a pattern pi efficiently?  
A) ✗ Precomputing all substrings is infeasible and not used.  
B) ✓ Link all leaf nodes into a chain in inorder.  
C) ✓ Each branch node stores pointers to leftmost and rightmost leaf nodes in its subtree.  
D) ✗ Storing counts alone is insufficient to list all occurrences.  

**Correct:** B, C


#### 11. Which of the following correctly describe the longest repeating substring problem?  
A) ✓ Branch nodes are labeled with the number of leaf nodes in their subtree (occurrences).  
B) ✗ The longest repeating substring corresponds to the branch node with the largest label ≥ m.  
C) ✓ The maximum length substring with label ≥ m (m > 1) is the answer.  
D) ✓ It finds the longest substring occurring more than once in S.  

**Correct:** A, C, D


#### 12. Given two strings S and T, which of the following statements about longest common substring and longest common subsequence are true?  
A) ✓ Longest common substring can be found in O(|S| + |T|) time using suffix trees.  
B) ✓ Longest common subsequence may contain non-contiguous characters.  
C) ✓ Longest common subsequence can be found in O(|S| * |T|) time using dynamic programming.  
D) ✗ Longest common substring is not always longer than subsequence; subsequence can be longer.  

**Correct:** A, B, C


#### 13. For the strings S = "carport" and T = "airports", which of the following are correct?  
A) ✗ "airport" is not a subsequence of S.  
B) ✗ "car" is a substring of S but not a longest common substring with T.  
C) ✓ The longest common substring is "rport".  
D) ✓ The longest common subsequence is "arport".  

**Correct:** C, D


#### 14. How can the longest common substring of two strings S and T be found using suffix trees?  
A) ✗ Building separate suffix trees and comparing is inefficient and not standard.  
B) ✓ Construct suffix tree for U = S$T#, with unique delimiters.  
C) ✗ Dynamic programming is not performed on suffix tree edges.  
D) ✓ Find the deepest node whose subtree contains suffixes from both S and T.  

**Correct:** B, D


#### 15. Which of the following are true about the relationship between substrings and suffixes?  
A) ✓ Every suffix of S is also a substring of S.  
B) ✓ A substring pi of S is a prefix of some suffix of S.  
C) ✗ A suffix starts at some index i ≥ 1, not necessarily index 1.  
D) ✗ Not every substring is a suffix; substrings can start anywhere.  

**Correct:** A, B


#### 16. What problem arises if the last character of S appears multiple times and no unique end character is appended?  
A) ✗ Suffix trees are acyclic by definition.  
B) ✗ The suffix tree can still be constructed but is ambiguous.  
C) ✗ Duplicate leaves do not occur; ambiguity is structural.  
D) ✓ Some suffixes become prefixes of other suffixes, causing ambiguity in the suffix tree.  

**Correct:** D


#### 17. Which of the following are valid suffixes of the string "creeper"?  
A) ✓ "eeper" is a suffix starting at index 3  
B) ✓ "eper" is a suffix starting at index 4  
C) ✓ "creeper" (full string)  
D) ✗ "reeper" is not a suffix (missing first character 'c')  

**Correct:** A, B, C


#### 18. Which of the following statements about suffix arrays and enhanced suffix arrays are true?  
A) ✓ They store sorted suffixes of S in an array.  
B) ✓ Enhanced suffix arrays include additional data structures (like LCP arrays) to speed queries.  
C) ✗ They generally require less space than suffix trees.  
D) ✓ They are alternatives to suffix trees for substring queries.  

**Correct:** A, B, D


#### 19. Which of the following are advantages of suffix trees over KMP for multiple pattern queries?  
A) ✓ KMP preprocesses each query separately, increasing total time for many queries.  
B) ✓ Suffix trees preprocess the source string once, enabling efficient multiple queries.  
C) ✗ KMP is not necessarily faster for large alphabets; suffix trees handle large alphabets efficiently.  
D) ✓ Suffix trees answer substring queries in O(|pi|) time after preprocessing.  

**Correct:** A, B, D


#### 20. In the context of suffix trees, what does the "max char#" field represent when finding the longest repeating substring?  
A) ✗ It is not the maximum character code.  
B) ✗ It is not the depth of the node.  
C) ✓ The length of the substring represented by the branch node (max character count).  
D) ✗ It is not the number of occurrences but related to substring length.  

**Correct:** C