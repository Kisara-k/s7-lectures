## 14. Suffix Trees

## Questions

#### 1. Which of the following statements correctly describe substrings and subsequences of a string S?  
A) A substring is composed of consecutive characters from S.  
B) Every substring is also a subsequence, but not every subsequence is a substring.  
C) A subsequence is composed of characters from S in the same order but not necessarily consecutive.  
D) The empty string is neither a substring nor a subsequence of S.  

#### 2. Regarding string/pattern matching, which of the following are true?  
A) For n queries, suffix trees require O(n|S| + Σ|pi|) time in total.  
B) Knuth-Morris-Pratt (KMP) preprocesses the source string S.  
C) Suffix trees preprocess the source string S, allowing multiple queries to be answered efficiently.  
D) KMP runs in O(|S| + |pi|) time per query, where pi is the pattern.  

#### 3. Which of the following correctly characterize suffix trees?  
A) Suffix trees allow substring queries to be answered in O(|pi|) time after preprocessing.  
B) A suffix tree is a compressed trie built from all nonempty suffixes of a string S.  
C) Suffix trees can handle repeated last characters in S without any modification.  
D) The keys in a suffix tree are all substrings of S.  

#### 4. Why is it necessary to append a unique end-of-string character (e.g., #) to S when constructing a suffix tree?  
A) To reduce the size of the suffix tree.  
B) To allow the suffix tree to represent empty substrings explicitly.  
C) To ensure no suffix is a prefix of another suffix.  
D) To handle cases where the last character of S appears multiple times.  

#### 5. Consider the suffix tree construction for a string S of length n over an alphabet of size r. Which of the following statements are true?  
A) The naive construction using array nodes takes O(nr) time.  
B) There exist better algorithms than the naive O(nr) approach for suffix tree construction.  
C) The suffix tree construction time depends exponentially on the length of S.  
D) If r is constant, the naive construction is effectively O(n).  

#### 6. When searching for a pattern pi in a suffix tree of S, what does it mean if the search terminates at a branch node?  
A) The pattern pi does not occur in S.  
B) Each leaf node in the subtree rooted at that branch node corresponds to a distinct occurrence of pi.  
C) The pattern pi occurs multiple times in S.  
D) The pattern pi occurs exactly once in S.  

#### 7. How can a suffix tree be augmented to efficiently find all occurrences of a pattern pi in S?  
A) Store pointers at each branch node to the leftmost and rightmost element nodes in its subtree.  
B) Use a hash table to map patterns to their occurrences.  
C) Link all element (leaf) nodes into a chain in inorder.  
D) Store the frequency of each substring at every node.  

#### 8. Which of the following approaches correctly find the longest repeating substring in S that occurs more than m times?  
A) Use dynamic programming on S to find repeated substrings.  
B) Search for the longest substring that appears exactly once.  
C) Find the branch node with label ≥ m and the maximum depth (max char# field).  
D) Label branch nodes with the number of element nodes in their subtree.  

#### 9. Given two strings S and T, which of the following statements about longest common substring and longest common subsequence are true?  
A) Constructing the suffix tree for U = S$T# helps find the longest common substring.  
B) The longest common substring can be found in O(|S| + |T|) time using a suffix tree.  
C) The longest common subsequence can be found in O(|S| * |T|) time using dynamic programming.  
D) The longest common substring is always longer than or equal to the longest common subsequence.  

#### 10. Which of the following are true about suffix arrays and enhanced suffix arrays compared to suffix trees?  
A) Suffix arrays inherently store all suffixes as nodes in a trie structure.  
B) Suffix arrays are a space-efficient alternative to suffix trees.  
C) Suffix arrays can be constructed in linear time for constant alphabets.  
D) Enhanced suffix arrays provide additional information to support substring queries efficiently.  



<br>

## Answers

#### 1. Which of the following statements correctly describe substrings and subsequences of a string S?  
A) ✓ A substring is composed of consecutive characters from S.  
B) ✓ Every substring is also a subsequence, but not every subsequence is a substring.  
C) ✓ A subsequence is composed of characters from S in the same order but not necessarily consecutive.  
D) ✗ The empty string is a substring and subsequence of S (by definition).  

**Correct:** A, B, C


#### 2. Regarding string/pattern matching, which of the following are true?  
A) ✗ For n queries, suffix trees require O(|S| + Σ|pi|) total time, not O(n|S| + Σ|pi|).  
B) ✗ KMP preprocesses the query string pi, not the source string S.  
C) ✓ Suffix trees preprocess the source string S, enabling efficient multiple queries.  
D) ✓ KMP runs in O(|S| + |pi|) time per query.  

**Correct:** C, D


#### 3. Which of the following correctly characterize suffix trees?  
A) ✓ Substring queries can be answered in O(|pi|) time after preprocessing.  
B) ✓ A suffix tree is a compressed trie built from all nonempty suffixes of S.  
C) ✗ When the last character repeats, suffix trees need a unique end character to avoid suffix-prefix ambiguity.  
D) ✗ Keys are suffixes, not all substrings of S.  

**Correct:** A, B


#### 4. Why is it necessary to append a unique end-of-string character (e.g., #) to S when constructing a suffix tree?  
A) ✗ It does not reduce the size of the suffix tree.  
B) ✗ The empty substring is always considered; the end character does not affect this.  
C) ✓ To ensure no suffix is a prefix of another suffix, making suffixes distinct.  
D) ✓ To handle cases where the last character appears multiple times in S.  

**Correct:** C, D


#### 5. Consider the suffix tree construction for a string S of length n over an alphabet of size r. Which of the following statements are true?  
A) ✓ Naive construction using array nodes takes O(nr) time.  
B) ✓ Better algorithms (e.g., Ukkonen’s) exist with linear time complexity.  
C) ✗ Construction time is not exponential in n; it is linear or near-linear.  
D) ✓ If r is constant, O(nr) = O(n), so naive construction is linear.  

**Correct:** A, B, D


#### 6. When searching for a pattern pi in a suffix tree of S, what does it mean if the search terminates at a branch node?  
A) ✗ The pattern pi does occur in S.  
B) ✓ Each leaf in the subtree corresponds to a distinct occurrence of pi.  
C) ✓ The pattern pi occurs multiple times in S.  
D) ✗ Occurs more than once, not exactly once.  

**Correct:** B, C


#### 7. How can a suffix tree be augmented to efficiently find all occurrences of a pattern pi in S?  
A) ✓ Branch nodes keep pointers to leftmost and rightmost leaves to quickly access occurrences.  
B) ✗ Hash tables are not part of the suffix tree augmentation described.  
C) ✓ Linking all leaf nodes into an inorder chain allows traversal of occurrences.  
D) ✗ Storing frequency alone does not help find all occurrences efficiently.  

**Correct:** A, C


#### 8. Which of the following approaches correctly find the longest repeating substring in S that occurs more than m times?  
A) ✗ Dynamic programming is not efficient for this problem compared to suffix trees.  
B) ✗ Looking for substrings that appear exactly once contradicts the "repeating" requirement.  
C) ✓ Find the branch node with label ≥ m and maximum depth (max char# field).  
D) ✓ Label branch nodes with the count of leaves in their subtree (occurrences).  

**Correct:** C, D


#### 9. Given two strings S and T, which of the following statements about longest common substring and longest common subsequence are true?  
A) ✓ Constructing suffix tree for U = S$T# helps find the longest common substring.  
B) ✓ Longest common substring can be found in O(|S| + |T|) time using a suffix tree.  
C) ✓ Longest common subsequence can be found in O(|S| * |T|) time using dynamic programming.  
D) ✗ The longest common substring is not necessarily longer than the longest common subsequence.  

**Correct:** A, B, C


#### 10. Which of the following are true about suffix arrays and enhanced suffix arrays compared to suffix trees?  
A) ✗ Suffix arrays do not store suffixes as trie nodes; they are sorted arrays of suffix indices.  
B) ✓ Suffix arrays are more space-efficient than suffix trees.  
C) ✓ Suffix arrays can be constructed in linear time for constant alphabets.  
D) ✓ Enhanced suffix arrays add information to support efficient substring queries.  

**Correct:** B, C, D