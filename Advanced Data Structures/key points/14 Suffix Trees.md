## 14. Suffix Trees

## Key Points

#### 1. 🌐 String Basics  
- A **substring** of string `S` is a contiguous sequence of characters from `S`.  
- A **subsequence** of string `S` is a sequence of characters from `S` in order but not necessarily contiguous.  
- The empty string is both a substring and a subsequence of any string.

#### 2. 🔍 String/Pattern Matching Complexity  
- KMP algorithm preprocesses the **query string** and runs in `O(|S| + |p_i|)` time per query.  
- For `n` queries, KMP total time is `O(n|S| + Σ|p_i|)`.  
- Suffix tree preprocesses the **source string** `S` and answers queries in `O(|S| + Σ|p_i|)` total time.

#### 3. 🌳 Definition of Suffix Tree  
- A suffix tree is a **compressed trie** of all nonempty suffixes of a string `S`.  
- Keys in the suffix tree are the nonempty suffixes of `S`.  
- A string `p_i` is a substring of `S` if and only if `p_i` is a prefix of some suffix of `S`.

#### 4. ⚠️ Handling Repeated Last Characters  
- If the last character of `S` appears multiple times, some suffixes can be prefixes of others, causing ambiguity.  
- To fix this, append a unique end-of-string character (e.g., `#`) to `S` to ensure all suffixes are unique.

#### 5. 🏗️ Suffix Tree Construction Complexity  
- Naive construction takes `O(nr)` time, where `n = |S|` and `r` is alphabet size.  
- For constant alphabet size, construction is effectively `O(n)`.  
- More efficient linear-time algorithms exist (e.g., Ukkonen’s algorithm).

#### 6. 🔎 Substring Search Using Suffix Trees  
- Searching for pattern `p_i` in suffix tree takes `O(|p_i|)` time.  
- If search ends at a leaf node, `p_i` occurs exactly once in `S`.  
- If search ends at an internal (branch) node, `p_i` occurs multiple times.

#### 7. 🔗 Finding All Occurrences of a Pattern  
- Augment suffix tree by linking all leaf nodes in inorder.  
- Each internal node stores pointers to leftmost and rightmost leaf in its subtree.  
- This allows reporting all occurrences in time proportional to `|p_i|` plus number of occurrences.

#### 8. 🔁 Longest Repeating Substring  
- Label internal nodes with the number of leaf nodes in their subtree (occurrence count).  
- The longest repeating substring corresponds to the internal node with label ≥ `m` (occurs at least `m` times) and maximum substring length.

#### 9. 🔗 Longest Common Substring of Two Strings  
- Concatenate strings with unique separators: `U = S$T#`.  
- Build suffix tree for `U`.  
- The longest common substring is found at the deepest internal node whose subtree contains suffixes from both `S` and `T`.  
- This can be done in `O(|S| + |T|)` time.



<br>

