## 14. Suffix Trees

## Questions

#### 1. Which of the following statements correctly describe substrings and subsequences of a string S?  
A) A substring is composed of consecutive characters from S.  
B) A subsequence is composed of characters from S in the same order but not necessarily consecutive.  
C) The empty string is neither a substring nor a subsequence of S.  
D) Every substring is also a subsequence, but not every subsequence is a substring.  

#### 2. Regarding string/pattern matching, which of the following are true?  
A) Knuth-Morris-Pratt (KMP) preprocesses the source string S.  
B) Suffix trees preprocess the source string S, allowing multiple queries to be answered efficiently.  
C) KMP runs in O(|S| + |pi|) time per query, where pi is the pattern.  
D) For n queries, suffix trees require O(n|S| + Σ|pi|) time in total.  

#### 3. Which of the following correctly characterize suffix trees?  
A) A suffix tree is a compressed trie built from all nonempty suffixes of a string S.  
B) The keys in a suffix tree are all substrings of S.  
C) Suffix trees allow substring queries to be answered in O(|pi|) time after preprocessing.  
D) Suffix trees can handle repeated last characters in S without any modification.  

#### 4. Why is it necessary to append a unique end-of-string character (e.g., #) to S when constructing a suffix tree?  
A) To ensure no suffix is a prefix of another suffix.  
B) To reduce the size of the suffix tree.  
C) To handle cases where the last character of S appears multiple times.  
D) To allow the suffix tree to represent empty substrings explicitly.  

#### 5. Consider the suffix tree construction for a string S of length n over an alphabet of size r. Which of the following statements are true?  
A) The naive construction using array nodes takes O(nr) time.  
B) If r is constant, the naive construction is effectively O(n).  
C) There exist better algorithms than the naive O(nr) approach for suffix tree construction.  
D) The suffix tree construction time depends exponentially on the length of S.  

#### 6. When searching for a pattern pi in a suffix tree of S, what does it mean if the search terminates at a branch node?  
A) The pattern pi does not occur in S.  
B) The pattern pi occurs exactly once in S.  
C) The pattern pi occurs multiple times in S.  
D) Each leaf node in the subtree rooted at that branch node corresponds to a distinct occurrence of pi.  

#### 7. How can a suffix tree be augmented to efficiently find all occurrences of a pattern pi in S?  
A) Link all element (leaf) nodes into a chain in inorder.  
B) Store pointers at each branch node to the leftmost and rightmost element nodes in its subtree.  
C) Store the frequency of each substring at every node.  
D) Use a hash table to map patterns to their occurrences.  

#### 8. Which of the following approaches correctly find the longest repeating substring in S that occurs more than m times?  
A) Label branch nodes with the number of element nodes in their subtree.  
B) Find the branch node with label ≥ m and the maximum depth (max char# field).  
C) Use dynamic programming on S to find repeated substrings.  
D) Search for the longest substring that appears exactly once.  

#### 9. Given two strings S and T, which of the following statements about longest common substring and longest common subsequence are true?  
A) The longest common substring can be found in O(|S| + |T|) time using a suffix tree.  
B) The longest common subsequence can be found in O(|S| * |T|) time using dynamic programming.  
C) The longest common substring is always longer than or equal to the longest common subsequence.  
D) Constructing the suffix tree for U = S$T# helps find the longest common substring.  

#### 10. Which of the following are true about suffix arrays and enhanced suffix arrays compared to suffix trees?  
A) Suffix arrays are a space-efficient alternative to suffix trees.  
B) Enhanced suffix arrays provide additional information to support substring queries efficiently.  
C) Suffix arrays can be constructed in linear time for constant alphabets.  
D) Suffix arrays inherently store all suffixes as nodes in a trie structure.



<br>

## Answers

#### 1. Which of the following statements correctly describe substrings and subsequences of a string S?  
A) ✓ A substring is composed of consecutive characters from S.  
B) ✓ A subsequence is composed of characters from S in the same order but not necessarily consecutive.  
C) ✗ The empty string is a substring and subsequence of S (by definition).  
D) ✓ Every substring is also a subsequence, but not every subsequence is a substring.  

**Correct:** A, B, D


#### 2. Regarding string/pattern matching, which of the following are true?  
A) ✗ KMP preprocesses the query string pi, not the source string S.  
B) ✓ Suffix trees preprocess the source string S, enabling efficient multiple queries.  
C) ✓ KMP runs in O(|S| + |pi|) time per query.  
D) ✗ For n queries, suffix trees require O(|S| + Σ|pi|) total time, not O(n|S| + Σ|pi|).  

**Correct:** B, C


#### 3. Which of the following correctly characterize suffix trees?  
A) ✓ A suffix tree is a compressed trie built from all nonempty suffixes of S.  
B) ✗ Keys are suffixes, not all substrings of S.  
C) ✓ Substring queries can be answered in O(|pi|) time after preprocessing.  
D) ✗ When the last character repeats, suffix trees need a unique end character to avoid suffix-prefix ambiguity.  

**Correct:** A, C


#### 4. Why is it necessary to append a unique end-of-string character (e.g., #) to S when constructing a suffix tree?  
A) ✓ To ensure no suffix is a prefix of another suffix, making suffixes distinct.  
B) ✗ It does not reduce the size of the suffix tree.  
C) ✓ To handle cases where the last character appears multiple times in S.  
D) ✗ The empty substring is always considered; the end character does not affect this.  

**Correct:** A, C


#### 5. Consider the suffix tree construction for a string S of length n over an alphabet of size r. Which of the following statements are true?  
A) ✓ Naive construction using array nodes takes O(nr) time.  
B) ✓ If r is constant, O(nr) = O(n), so naive construction is linear.  
C) ✓ Better algorithms (e.g., Ukkonen’s) exist with linear time complexity.  
D) ✗ Construction time is not exponential in n; it is linear or near-linear.  

**Correct:** A, B, C


#### 6. When searching for a pattern pi in a suffix tree of S, what does it mean if the search terminates at a branch node?  
A) ✗ The pattern pi does occur in S.  
B) ✗ Occurs more than once, not exactly once.  
C) ✓ The pattern pi occurs multiple times in S.  
D) ✓ Each leaf in the subtree corresponds to a distinct occurrence of pi.  

**Correct:** C, D


#### 7. How can a suffix tree be augmented to efficiently find all occurrences of a pattern pi in S?  
A) ✓ Linking all leaf nodes into an inorder chain allows traversal of occurrences.  
B) ✓ Branch nodes keep pointers to leftmost and rightmost leaves to quickly access occurrences.  
C) ✗ Storing frequency alone does not help find all occurrences efficiently.  
D) ✗ Hash tables are not part of the suffix tree augmentation described.  

**Correct:** A, B


#### 8. Which of the following approaches correctly find the longest repeating substring in S that occurs more than m times?  
A) ✓ Label branch nodes with the count of leaves in their subtree (occurrences).  
B) ✓ Find the branch node with label ≥ m and maximum depth (max char# field).  
C) ✗ Dynamic programming is not efficient for this problem compared to suffix trees.  
D) ✗ Looking for substrings that appear exactly once contradicts the "repeating" requirement.  

**Correct:** A, B


#### 9. Given two strings S and T, which of the following statements about longest common substring and longest common subsequence are true?  
A) ✓ Longest common substring can be found in O(|S| + |T|) time using a suffix tree.  
B) ✓ Longest common subsequence can be found in O(|S| * |T|) time using dynamic programming.  
C) ✗ The longest common substring is not necessarily longer than the longest common subsequence.  
D) ✓ Constructing suffix tree for U = S$T# helps find the longest common substring.  

**Correct:** A, B, D


#### 10. Which of the following are true about suffix arrays and enhanced suffix arrays compared to suffix trees?  
A) ✓ Suffix arrays are more space-efficient than suffix trees.  
B) ✓ Enhanced suffix arrays add information to support efficient substring queries.  
C) ✓ Suffix arrays can be constructed in linear time for constant alphabets.  
D) ✗ Suffix arrays do not store suffixes as trie nodes; they are sorted arrays of suffix indices.  

**Correct:** A, B, C