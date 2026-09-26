## 14. Suffix Trees

## Questions

#### 1. Which of the following statements correctly describe a substring of a string S?  
A) A substring is composed of consecutive characters from S between indices i and j, where i ≤ j.  
B) The empty string is considered a substring of S.  
C) A substring can be formed by characters in S at indices i1 < i2 < ... < ik, not necessarily consecutive.  
D) A substring must always start at the first character of S.  

#### 2. Which of the following are true about subsequences of a string S?  
A) A subsequence is formed by characters of S at strictly increasing indices.  
B) Every substring is also a subsequence.  
C) The empty string is a subsequence of S.  
D) A subsequence must be contiguous in S.  

#### 3. Regarding string/pattern matching, which statements are correct?  
A) Knuth-Morris-Pratt (KMP) algorithm preprocesses the source string S.  
B) KMP runs in O(|S| + |pi|) time per query.  
C) Using suffix trees, multiple queries can be answered in O(|S| + Σ|pi|) time.  
D) Suffix trees preprocess the query strings pi, not the source string S.  

#### 4. Which of the following correctly describe suffix trees?  
A) A suffix tree is a compressed trie built from all nonempty suffixes of a string S.  
B) The keys in a suffix tree are all substrings of S.  
C) Each edge in a suffix tree stores a substring of S.  
D) Suffix trees can be used to find if a pattern pi is a substring of S.  

#### 5. Consider the string S = "sleeper". Which of the following are suffixes of S?  
A) "sleeper"  
B) "leeper"  
C) "leep"  
D) "per"  

#### 6. Why is it necessary to append a unique end-of-string character (e.g., '#') to S when building a suffix tree?  
A) To ensure no suffix is a prefix of another suffix.  
B) To reduce the size of the suffix tree.  
C) To handle cases where the last character of S repeats multiple times.  
D) To allow suffix trees to handle empty strings.  

#### 7. Which of the following are true about the time complexity of suffix tree construction?  
A) Using array nodes, the complexity is O(nr), where n = |S| and r = alphabet size.  
B) For constant alphabet size, suffix tree construction is O(n).  
C) Suffix tree construction always takes O(n²) time.  
D) Compressing tries is the only method to build suffix trees.  

#### 8. When searching for a pattern pi in a suffix tree, what does it mean if the search terminates at an element (leaf) node?  
A) pi appears exactly once in S.  
B) pi is not a substring of S.  
C) pi appears multiple times in S.  
D) pi is a prefix of some suffix of S.  

#### 9. If the search for pi in a suffix tree ends at a branch node, which of the following are true?  
A) pi appears multiple times in S.  
B) Each leaf node in the subtree rooted at this branch node corresponds to a different occurrence of pi.  
C) pi is not a substring of S.  
D) The number of occurrences of pi equals the number of leaf nodes in that subtree.  

#### 10. How can suffix trees be augmented to find all occurrences of a pattern pi efficiently?  
A) Link all leaf nodes into a chain in inorder.  
B) Each branch node stores pointers to the leftmost and rightmost leaf nodes in its subtree.  
C) Store the count of occurrences at each node.  
D) Precompute all substrings of S and store their positions.  

#### 11. Which of the following correctly describe the longest repeating substring problem?  
A) It finds the longest substring occurring more than once in S.  
B) Branch nodes are labeled with the number of leaf nodes in their subtree.  
C) The longest repeating substring corresponds to the branch node with the smallest label.  
D) The maximum length substring with label ≥ m (m > 1) is the answer.  

#### 12. Given two strings S and T, which of the following statements about longest common substring and longest common subsequence are true?  
A) The longest common substring can be found in O(|S| + |T|) time using suffix trees.  
B) The longest common subsequence can be found in O(|S| * |T|) time using dynamic programming.  
C) The longest common substring is always longer than the longest common subsequence.  
D) The longest common subsequence may contain characters not contiguous in S or T.  

#### 13. For the strings S = "carport" and T = "airports", which of the following are correct?  
A) The longest common substring is "rport".  
B) The longest common subsequence is "arport".  
C) "car" is a longest common substring.  
D) "airport" is a longest common subsequence.  

#### 14. How can the longest common substring of two strings S and T be found using suffix trees?  
A) Construct the suffix tree for the concatenated string U = S$T#, where $ and # are unique delimiters.  
B) Search for the longest path in the suffix tree that contains suffixes from both S and T.  
C) Use dynamic programming on the suffix tree edges.  
D) Build separate suffix trees for S and T and compare them.  

#### 15. Which of the following are true about the relationship between substrings and suffixes?  
A) A substring pi of S is a prefix of some suffix of S.  
B) Every suffix of S is also a substring of S.  
C) Every substring of S is a suffix of S.  
D) A suffix is always a substring starting at index 1.  

#### 16. What problem arises if the last character of S appears multiple times and no unique end character is appended?  
A) Some suffixes become prefixes of other suffixes, causing ambiguity in the suffix tree.  
B) The suffix tree will have duplicate leaves.  
C) The suffix tree cannot be constructed.  
D) The suffix tree will have cycles.  

#### 17. Which of the following are valid suffixes of the string "creeper"?  
A) "creeper"  
B) "reeper"  
C) "eeper"  
D) "eper"  

#### 18. Which of the following statements about suffix arrays and enhanced suffix arrays are true?  
A) They are alternatives to suffix trees for substring queries.  
B) They store sorted suffixes of S in an array.  
C) Enhanced suffix arrays include additional data structures to speed up queries.  
D) They require more space than suffix trees.  

#### 19. Which of the following are advantages of suffix trees over KMP for multiple pattern queries?  
A) Suffix trees preprocess the source string once, allowing multiple queries efficiently.  
B) KMP preprocesses each query string separately, leading to higher total time for many queries.  
C) Suffix trees can answer substring queries in O(|pi|) time after preprocessing.  
D) KMP is faster than suffix trees for large alphabets.  

#### 20. In the context of suffix trees, what does the "max char#" field represent when finding the longest repeating substring?  
A) The length of the substring represented by the branch node.  
B) The maximum character code in the substring.  
C) The maximum number of occurrences of the substring.  
D) The maximum depth of the branch node in the suffix tree.



<br>

## Answers

#### 1. Which of the following statements correctly describe a substring of a string S?  
A) ✓ A substring is composed of consecutive characters from S between indices i and j, where i ≤ j.  
B) ✓ The empty string is considered a substring of S.  
C) ✗ This describes a subsequence, not a substring.  
D) ✗ A substring can start anywhere, not necessarily at the first character.  

**Correct:** A,B


#### 2. Which of the following are true about subsequences of a string S?  
A) ✓ A subsequence is formed by characters of S at strictly increasing indices.  
B) ✓ Every substring is also a subsequence (since substrings are contiguous subsequences).  
C) ✓ The empty string is a subsequence of S.  
D) ✗ A subsequence need not be contiguous.  

**Correct:** A,B,C


#### 3. Regarding string/pattern matching, which statements are correct?  
A) ✗ KMP preprocesses the query string pi, not the source string S.  
B) ✓ KMP runs in O(|S| + |pi|) time per query.  
C) ✓ Using suffix trees, multiple queries can be answered in O(|S| + Σ|pi|) time.  
D) ✗ Suffix trees preprocess the source string S, not the queries.  

**Correct:** B,C


#### 4. Which of the following correctly describe suffix trees?  
A) ✓ A suffix tree is a compressed trie built from all nonempty suffixes of a string S.  
B) ✗ Keys are suffixes, not all substrings.  
C) ✓ Each edge stores a substring (edge label) of S.  
D) ✓ Suffix trees can be used to find if a pattern pi is a substring of S.  

**Correct:** A,C,D


#### 5. Consider the string S = "sleeper". Which of the following are suffixes of S?  
A) ✓ "sleeper" is the full string, hence a suffix.  
B) ✓ "leeper" is suffix starting at index 2.  
C) ✗ "leep" is not a suffix (not from an index to the end).  
D) ✓ "per" is a suffix starting at index 5.  

**Correct:** A,B,D


#### 6. Why is it necessary to append a unique end-of-string character (e.g., '#') to S when building a suffix tree?  
A) ✓ To ensure no suffix is a prefix of another suffix, avoiding ambiguity.  
B) ✗ It does not reduce size; it ensures uniqueness.  
C) ✓ To handle cases where the last character repeats multiple times.  
D) ✗ The empty string is always a substring; this is unrelated.  

**Correct:** A,C


#### 7. Which of the following are true about the time complexity of suffix tree construction?  
A) ✓ Using array nodes, complexity is O(nr), where r is alphabet size.  
B) ✓ For constant alphabet size, construction is O(n).  
C) ✗ Construction is not always O(n²).  
D) ✗ There are better methods than compressing tries (e.g., Ukkonen’s algorithm).  

**Correct:** A,B


#### 8. When searching for a pattern pi in a suffix tree, what does it mean if the search terminates at an element (leaf) node?  
A) ✓ pi appears exactly once in S.  
B) ✗ pi is a substring, so search would not fail.  
C) ✗ Multiple occurrences would end at a branch node, not a leaf.  
D) ✓ pi is a prefix of some suffix of S (by definition).  

**Correct:** A,D


#### 9. If the search for pi in a suffix tree ends at a branch node, which of the following are true?  
A) ✓ pi appears multiple times in S.  
B) ✓ Each leaf in the subtree corresponds to a different occurrence of pi.  
C) ✗ pi is a substring, so search does not fail.  
D) ✓ Number of occurrences equals number of leaf nodes in that subtree.  

**Correct:** A,B,D


#### 10. How can suffix trees be augmented to find all occurrences of a pattern pi efficiently?  
A) ✓ Link all leaf nodes into a chain in inorder.  
B) ✓ Each branch node stores pointers to leftmost and rightmost leaf nodes in its subtree.  
C) ✗ Storing counts alone is insufficient to list all occurrences.  
D) ✗ Precomputing all substrings is infeasible and not used.  

**Correct:** A,B


#### 11. Which of the following correctly describe the longest repeating substring problem?  
A) ✓ It finds the longest substring occurring more than once in S.  
B) ✓ Branch nodes are labeled with the number of leaf nodes in their subtree (occurrences).  
C) ✗ The longest repeating substring corresponds to the branch node with the largest label ≥ m.  
D) ✓ The maximum length substring with label ≥ m (m > 1) is the answer.  

**Correct:** A,B,D


#### 12. Given two strings S and T, which of the following statements about longest common substring and longest common subsequence are true?  
A) ✓ Longest common substring can be found in O(|S| + |T|) time using suffix trees.  
B) ✓ Longest common subsequence can be found in O(|S| * |T|) time using dynamic programming.  
C) ✗ Longest common substring is not always longer than subsequence; subsequence can be longer.  
D) ✓ Longest common subsequence may contain non-contiguous characters.  

**Correct:** A,B,D


#### 13. For the strings S = "carport" and T = "airports", which of the following are correct?  
A) ✓ The longest common substring is "rport".  
B) ✓ The longest common subsequence is "arport".  
C) ✗ "car" is a substring of S but not a longest common substring with T.  
D) ✗ "airport" is not a subsequence of S.  

**Correct:** A,B


#### 14. How can the longest common substring of two strings S and T be found using suffix trees?  
A) ✓ Construct suffix tree for U = S$T#, with unique delimiters.  
B) ✓ Find the deepest node whose subtree contains suffixes from both S and T.  
C) ✗ Dynamic programming is not performed on suffix tree edges.  
D) ✗ Building separate suffix trees and comparing is inefficient and not standard.  

**Correct:** A,B


#### 15. Which of the following are true about the relationship between substrings and suffixes?  
A) ✓ A substring pi of S is a prefix of some suffix of S.  
B) ✓ Every suffix of S is also a substring of S.  
C) ✗ Not every substring is a suffix; substrings can start anywhere.  
D) ✗ A suffix starts at some index i ≥ 1, not necessarily index 1.  

**Correct:** A,B


#### 16. What problem arises if the last character of S appears multiple times and no unique end character is appended?  
A) ✓ Some suffixes become prefixes of other suffixes, causing ambiguity in the suffix tree.  
B) ✗ Duplicate leaves do not occur; ambiguity is structural.  
C) ✗ The suffix tree can still be constructed but is ambiguous.  
D) ✗ Suffix trees are acyclic by definition.  

**Correct:** A


#### 17. Which of the following are valid suffixes of the string "creeper"?  
A) ✓ "creeper" (full string)  
B) ✗ "reeper" is not a suffix (missing first character 'c')  
C) ✓ "eeper" is a suffix starting at index 3  
D) ✓ "eper" is a suffix starting at index 4  

**Correct:** A,C,D


#### 18. Which of the following statements about suffix arrays and enhanced suffix arrays are true?  
A) ✓ They are alternatives to suffix trees for substring queries.  
B) ✓ They store sorted suffixes of S in an array.  
C) ✓ Enhanced suffix arrays include additional data structures (like LCP arrays) to speed queries.  
D) ✗ They generally require less space than suffix trees.  

**Correct:** A,B,C


#### 19. Which of the following are advantages of suffix trees over KMP for multiple pattern queries?  
A) ✓ Suffix trees preprocess the source string once, enabling efficient multiple queries.  
B) ✓ KMP preprocesses each query separately, increasing total time for many queries.  
C) ✓ Suffix trees answer substring queries in O(|pi|) time after preprocessing.  
D) ✗ KMP is not necessarily faster for large alphabets; suffix trees handle large alphabets efficiently.  

**Correct:** A,B,C


#### 20. In the context of suffix trees, what does the "max char#" field represent when finding the longest repeating substring?  
A) ✓ The length of the substring represented by the branch node (max character count).  
B) ✗ It is not the maximum character code.  
C) ✗ It is not the number of occurrences but related to substring length.  
D) ✗ It is not the depth of the node.  

**Correct:** A