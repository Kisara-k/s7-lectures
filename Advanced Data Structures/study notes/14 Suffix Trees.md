## 14. Suffix Trees

## Study Notes

### 1. 🌳 Introduction to Suffix Trees and Strings

Before diving into suffix trees, it’s important to understand some basic string concepts.

A **string** is simply a sequence of characters. For example, the string `cater` consists of the characters `c`, `a`, `t`, `e`, `r`.

- A **substring** of a string `S` is a contiguous sequence of characters taken from `S`. For example, in `cater`, `ate` is a substring because it appears consecutively in the string (`c-a-t-e-r`). However, `car` is **not** a substring because those characters do not appear consecutively in that order.
- The **empty string** (a string with zero characters) is considered a substring of any string.

A **subsequence** is a sequence of characters that appear in the same order as in the original string but not necessarily consecutively. For example, in `cater`:
- `ate` is a subsequence (characters appear in order: a, t, e).
- `car` is also a subsequence (characters appear in order: c, a, r).
- The empty string is also a subsequence.

Understanding the difference between substrings and subsequences is crucial because suffix trees deal with substrings, not subsequences.


### 2. 🔍 String/Pattern Matching and Its Challenges

One common problem in computer science is **string matching**: given a source string `S`, we want to answer queries like "Is the string `p_i` a substring of `S`?"

#### Traditional Approach: Knuth-Morris-Pratt (KMP) Algorithm
- KMP preprocesses the **query string** `p_i` to efficiently search for it in `S`.
- It takes time proportional to the length of `S` plus the length of `p_i` for each query.
- For `n` queries, the total time is roughly `O(n|S| + Σ|p_i|)`.

#### Suffix Tree Approach
- Instead of preprocessing each query, suffix trees preprocess the **source string** `S`.
- This allows answering multiple substring queries more efficiently.
- The total time for `n` queries becomes `O(|S| + Σ|p_i|)`, which is often much faster.

#### Applications
- Genome sequencing: Searching for gene sequences (strings over the alphabet {A, T, G, C}) in large databases.
- Text databases: Quickly finding if a new sequence appears in a large collection of strings.


### 3. 🌲 What is a Suffix Tree?

A **suffix tree** is a special data structure that represents all the suffixes of a string in a compressed form.

- It is a **compressed trie** (a tree-like structure) where each edge is labeled with a substring of the original string.
- The keys stored in the suffix tree are the **nonempty suffixes** of the string `S`.

For example, consider the string `sleeper`. Its nonempty suffixes are:
- `sleeper`
- `leeper`
- `eeper`
- `eper`
- `per`
- `er`
- `r`

Each suffix corresponds to a path from the root to a leaf in the suffix tree.

#### Important property:
A string `p_i` is a substring of `S` if and only if `p_i` is a **prefix of some suffix** of `S`. This is why suffix trees are so useful for substring queries.


### 4. ⚠️ Handling Repeated Characters and the End Marker

When the last character of `S` appears multiple times in `S`, some suffixes can be prefixes of others. This can cause ambiguity in the suffix tree.

For example, in `creeper`:
- Suffixes include `creeper`, `reeper`, `eeper`, `eper`, `per`, `er`, `r`.
- Notice that some suffixes start with the same characters, and one suffix can be a prefix of another.

#### Solution: Add a unique end-of-string character
- Append a special character (often `#`) that does not appear anywhere else in the string.
- For `creeper`, use `creeper#`.
- This ensures all suffixes are unique and no suffix is a prefix of another.


### 5. 🏗️ Constructing a Suffix Tree

The suffix tree is built by compressing a trie of all suffixes of `S`.

- A **trie** is a tree where each edge represents a single character.
- A **compressed trie** merges chains of single-child nodes into one edge labeled by a substring.

#### Complexity
- If `|S| = n` and the alphabet size is `r`, a naive construction takes `O(nr)` time.
- For constant or small alphabets, this is effectively `O(n)`.

More advanced algorithms (like Ukkonen’s algorithm) can build suffix trees in linear time.


### 6. 🔎 Using Suffix Trees for Substring Matching

To check if a pattern `p_i` is a substring of `S`:

- Start at the root of the suffix tree.
- Follow edges matching the characters of `p_i`.
- If you can follow the entire pattern, `p_i` is a substring.
- If the search ends at a **leaf node**, `p_i` occurs exactly once.
- If the search ends at an **internal (branch) node**, `p_i` occurs multiple times.

#### Finding all occurrences
- Each leaf corresponds to a suffix, which indicates the starting position of an occurrence.
- To efficiently find all occurrences, augment the suffix tree:
  - Link all leaf nodes in an inorder chain.
  - Each internal node stores pointers to the leftmost and rightmost leaves in its subtree.
- This allows reporting all occurrences in time proportional to the length of `p_i` plus the number of occurrences.


### 7. 🔁 Longest Repeating Substring

A **longest repeating substring** is the longest substring that appears at least `m > 1` times in `S`.

- To find it, label each internal node with the number of leaf nodes in its subtree (which corresponds to the number of occurrences).
- Find the internal node with label ≥ `m` that corresponds to the longest substring (longest path from root).
- The substring represented by this node is the longest repeating substring.


### 8. 🔗 Longest Common Substring Between Two Strings

Given two strings `S` and `T`, the **longest common substring** is the longest string that appears as a substring in both.

- Example: `S = carport`, `T = airports`
  - Longest common substring: `rport`
  - Longest common subsequence (not necessarily contiguous): `arport`

#### Finding longest common substring with suffix trees
- Concatenate the two strings with unique end markers: `U = S$T#` (where `$` and `#` are unique symbols).
- Build the suffix tree for `U`.
- The longest substring that appears in both `S` and `T` corresponds to the deepest internal node whose subtree contains suffixes from both `S` and `T`.
- This can be found in `O(|S| + |T|)` time, which is much faster than the dynamic programming approach for longest common subsequence (`O(|S| * |T|)`).


### Summary

Suffix trees are powerful data structures that allow efficient substring queries and solve complex string problems like longest repeating substrings and longest common substrings. They work by representing all suffixes of a string in a compressed trie, enabling fast searches and pattern matching. Adding unique end markers ensures uniqueness of suffixes, and augmenting the tree helps find all occurrences of a pattern efficiently. These properties make suffix trees invaluable in fields like bioinformatics and text processing.