## 12. Digital Search Trees and Binary Tries

## Questions

#### 1. What is the primary data type used as keys in Digital Search Trees and Binary Tries?  
A) Integer numbers  
B) Binary bit strings  
C) Floating-point numbers  
D) Character strings  

#### 2. Which of the following statements about Digital Search Trees (DST) is true?  
A) The root contains all dictionary pairs.  
B) The left subtree contains pairs whose keys start with 0.  
C) The right subtree contains pairs whose keys start with 1.  
D) DSTs only work with variable-length keys.  

#### 3. In a Digital Search Tree, what happens to the keys after the root node is assigned a dictionary pair?  
A) All keys are stored in the root node.  
B) Keys are split into left and right subtrees based on the first bit of their remaining bits.  
C) Keys are sorted numerically.  
D) Keys are stored in a linked list attached to the root.  

#### 4. Which of the following applications commonly use Digital Search Trees or Binary Tries?  
A) IP routing  
B) Packet classification  
C) Firewalls  
D) Sorting large arrays  

#### 5. What is the time complexity of search, insert, and delete operations in Digital Search Trees?  
A) O(log n)  
B) O(n)  
C) O(#bits in a key)  
D) O(1)  

#### 6. Why can operations on Digital Search Trees be expensive when keys are very long?  
A) Because the number of key comparisons depends on the height of the tree, which grows with key length.  
B) Because keys must be converted to decimal first.  
C) Because the tree must be rebalanced after every operation.  
D) Because the keys are stored in linked lists.  

#### 7. Which of the following is true about Binary Tries compared to Digital Search Trees?  
A) Binary Tries have at most one key comparison per operation.  
B) Binary Tries only work with variable-length keys.  
C) Branch nodes in Binary Tries contain data fields.  
D) Element nodes in Binary Tries have no child pointers.  

#### 8. In a Binary Trie, what is the role of branch nodes?  
A) They store dictionary pairs.  
B) They contain left and right child pointers but no data fields.  
C) They terminate the search.  
D) They store the entire key.  

#### 9. How do element nodes in a Binary Trie differ from branch nodes?  
A) Element nodes have child pointers.  
B) Element nodes contain data fields but no child pointers.  
C) Element nodes are always at the root.  
D) Element nodes contain left and right child pointers.  

#### 10. For variable-length keys in Binary Tries, what is the purpose of the left and right pair fields?  
A) To store pairs whose keys terminate at the root of the respective subtree.  
B) To store all keys starting with 0 or 1.  
C) To store the entire subtree.  
D) To store pointers to the next node.  

#### 11. Which of the following statements about fixed-length key insertion in Binary Tries is correct?  
A) Inserting a key always requires multiple key comparisons.  
B) Inserting a key can sometimes require zero key comparisons.  
C) Insertion complexity depends on the number of keys already in the tree.  
D) Insertion is always O(n) where n is the number of keys.  

#### 12. What is the maximum number of key comparisons required for a search operation in a Binary Trie?  
A) Equal to the number of keys in the tree  
B) Equal to the height of the tree  
C) At most one  
D) Equal to the length of the key  

#### 13. Which of the following is NOT a characteristic of Digital Search Trees?  
A) Keys are split based on their bits.  
B) The root node contains one dictionary pair.  
C) The tree structure depends on the numeric value of keys.  
D) Left and right subtrees are themselves Digital Search Trees on remaining bits.  

#### 14. When deleting a key from a fixed-length Binary Trie, which of the following is true?  
A) Deletion always requires multiple key comparisons.  
B) Deletion can sometimes be done with only one key comparison.  
C) Deletion complexity depends on the length of the key.  
D) Deletion is impossible without rebalancing the tree.  

#### 15. How does the structure of a Digital Search Tree change when inserting a key that shares a prefix with an existing key?  
A) The new key replaces the existing key at the root.  
B) The tree branches further down at the first differing bit.  
C) The new key is appended as a sibling node.  
D) The tree remains unchanged.  

#### 16. Which of the following best describes the relationship between Digital Search Trees and radix sort?  
A) Digital Search Trees are a sorting algorithm unrelated to radix sort.  
B) Digital Search Trees are an analog of radix sort applied to searching.  
C) Radix sort is a special case of Digital Search Trees.  
D) Digital Search Trees use radix sort internally for balancing.  

#### 17. In the context of IP routing, why are Digital Search Trees or Binary Tries suitable data structures?  
A) Because IP addresses are fixed-length binary strings.  
B) Because they allow efficient prefix matching.  
C) Because they minimize memory usage compared to hash tables.  
D) Because they support floating-point keys.  

#### 18. What is a key challenge when using Digital Search Trees with variable-length keys?  
A) Handling keys that terminate at internal nodes.  
B) Ensuring all keys have the same length.  
C) Balancing the tree after every insertion.  
D) Converting keys to decimal format.  

#### 19. Which of the following statements about the height of a Digital Search Tree is true?  
A) The height is always equal to the number of keys.  
B) The height depends on the number of bits in the keys.  
C) The height is independent of key length.  
D) The height is always logarithmic in the number of keys.  

#### 20. In a Binary Trie with variable-length keys, what does a null left or right pair field indicate?  
A) That there is no key terminating at the root of that subtree.  
B) That the subtree is empty.  
C) That the key is longer than the maximum allowed length.  
D) That the key must be stored in a linked list instead.



<br>

## Answers

#### 1. What is the primary data type used as keys in Digital Search Trees and Binary Tries?  
A) ✗ Integer numbers — Keys are binary bit strings, not integers per se.  
B) ✓ Binary bit strings — Correct; keys are represented as binary strings.  
C) ✗ Floating-point numbers — Not used as keys here.  
D) ✗ Character strings — Keys are binary strings, not general character strings.  

**Correct:** B


#### 2. Which of the following statements about Digital Search Trees (DST) is true?  
A) ✗ The root contains all dictionary pairs — The root contains only one dictionary pair.  
B) ✓ The left subtree contains pairs whose keys start with 0 — Correct by definition.  
C) ✓ The right subtree contains pairs whose keys start with 1 — Correct by definition.  
D) ✗ DSTs only work with variable-length keys — DSTs assume fixed or variable length but are not limited to variable length only.  

**Correct:** B, C


#### 3. In a Digital Search Tree, what happens to the keys after the root node is assigned a dictionary pair?  
A) ✗ All keys are stored in the root node — Only one pair is stored at the root.  
B) ✓ Keys are split into left and right subtrees based on the first bit of their remaining bits — Correct; keys are partitioned by bit prefixes.  
C) ✗ Keys are sorted numerically — Sorting is not the mechanism used.  
D) ✗ Keys are stored in a linked list attached to the root — No linked lists involved.  

**Correct:** B


#### 4. Which of the following applications commonly use Digital Search Trees or Binary Tries?  
A) ✓ IP routing — Correct; IP addresses are binary keys.  
B) ✓ Packet classification — Correct; requires prefix matching.  
C) ✓ Firewalls — Correct; packet filtering uses prefix-based structures.  
D) ✗ Sorting large arrays — Not a typical application of DST or tries.  

**Correct:** A, B, C


#### 5. What is the time complexity of search, insert, and delete operations in Digital Search Trees?  
A) ✗ O(log n) — Complexity depends on key length, not number of keys.  
B) ✗ O(n) — Not dependent on number of keys linearly.  
C) ✓ O(#bits in a key) — Correct; operations depend on key length.  
D) ✗ O(1) — Not constant time.  

**Correct:** C


#### 6. Why can operations on Digital Search Trees be expensive when keys are very long?  
A) ✓ Because the number of key comparisons depends on the height of the tree, which grows with key length — Correct; height relates to bits in keys.  
B) ✗ Because keys must be converted to decimal first — No conversion needed.  
C) ✗ Because the tree must be rebalanced after every operation — DSTs do not require rebalancing.  
D) ✗ Because the keys are stored in linked lists — Keys are stored in tree nodes, not lists.  

**Correct:** A


#### 7. Which of the following is true about Binary Tries compared to Digital Search Trees?  
A) ✓ Binary Tries have at most one key comparison per operation — Correct; tries minimize comparisons.  
B) ✗ Binary Tries only work with variable-length keys — They can work with fixed-length keys too.  
C) ✗ Branch nodes in Binary Tries contain data fields — Branch nodes have no data fields.  
D) ✓ Element nodes in Binary Tries have no child pointers — Correct; element nodes store data only.  

**Correct:** A, D


#### 8. In a Binary Trie, what is the role of branch nodes?  
A) ✗ They store dictionary pairs — Branch nodes do not store data.  
B) ✓ They contain left and right child pointers but no data fields — Correct; they guide traversal.  
C) ✗ They terminate the search — Element nodes terminate search.  
D) ✗ They store the entire key — Keys are implicit in path, not stored.  

**Correct:** B


#### 9. How do element nodes in a Binary Trie differ from branch nodes?  
A) ✗ Element nodes have child pointers — They do not have child pointers.  
B) ✓ Element nodes contain data fields but no child pointers — Correct; they hold dictionary pairs.  
C) ✗ Element nodes are always at the root — They can be anywhere.  
D) ✗ Element nodes contain left and right child pointers — Only branch nodes do.  

**Correct:** B


#### 10. For variable-length keys in Binary Tries, what is the purpose of the left and right pair fields?  
A) ✓ To store pairs whose keys terminate at the root of the respective subtree — Correct; handles keys ending at internal nodes.  
B) ✗ To store all keys starting with 0 or 1 — This is done by subtrees, not pair fields.  
C) ✗ To store the entire subtree — Subtrees are represented by child pointers.  
D) ✗ To store pointers to the next node — They store data pairs, not pointers.  

**Correct:** A


#### 11. Which of the following statements about fixed-length key insertion in Binary Tries is correct?  
A) ✗ Inserting a key always requires multiple key comparisons — Sometimes zero or one comparison suffices.  
B) ✓ Inserting a key can sometimes require zero key comparisons — Correct; if no conflict arises.  
C) ✗ Insertion complexity depends on the number of keys already in the tree — Complexity depends on key length.  
D) ✗ Insertion is always O(n) where n is the number of keys — Complexity depends on key length, not number of keys.  

**Correct:** B


#### 12. What is the maximum number of key comparisons required for a search operation in a Binary Trie?  
A) ✗ Equal to the number of keys in the tree — No, independent of number of keys.  
B) ✗ Equal to the height of the tree — Height can be large, but tries optimize comparisons.  
C) ✓ At most one — Correct; tries guarantee at most one key comparison.  
D) ✗ Equal to the length of the key — Comparisons minimized to one.  

**Correct:** C


#### 13. Which of the following is NOT a characteristic of Digital Search Trees?  
A) ✗ Keys are split based on their bits — This is a defining characteristic.  
B) ✗ The root node contains one dictionary pair — True for DST.  
C) ✓ The tree structure depends on the numeric value of keys — Incorrect; structure depends on bit prefixes, not numeric value.  
D) ✗ Left and right subtrees are themselves Digital Search Trees on remaining bits — True by definition.  

**Correct:** C


#### 14. When deleting a key from a fixed-length Binary Trie, which of the following is true?  
A) ✗ Deletion always requires multiple key comparisons — Sometimes only one comparison is needed.  
B) ✓ Deletion can sometimes be done with only one key comparison — Correct; deletion can be efficient.  
C) ✗ Deletion complexity depends on the length of the key — Complexity depends on key length but comparisons can be minimal.  
D) ✗ Deletion is impossible without rebalancing the tree — No rebalancing needed.  

**Correct:** B


#### 15. How does the structure of a Digital Search Tree change when inserting a key that shares a prefix with an existing key?  
A) ✗ The new key replaces the existing key at the root — Root remains unchanged unless empty.  
B) ✓ The tree branches further down at the first differing bit — Correct; branching occurs at first bit difference.  
C) ✗ The new key is appended as a sibling node — Not how DSTs organize keys.  
D) ✗ The tree remains unchanged — Tree structure changes to accommodate new key.  

**Correct:** B


#### 16. Which of the following best describes the relationship between Digital Search Trees and radix sort?  
A) ✗ Digital Search Trees are a sorting algorithm unrelated to radix sort — They are related.  
B) ✓ Digital Search Trees are an analog of radix sort applied to searching — Correct; DSTs mimic radix sort logic for search.  
C) ✗ Radix sort is a special case of Digital Search Trees — Radix sort is a sorting algorithm, not a tree.  
D) ✗ Digital Search Trees use radix sort internally for balancing — No balancing or sorting internally.  

**Correct:** B


#### 17. In the context of IP routing, why are Digital Search Trees or Binary Tries suitable data structures?  
A) ✓ Because IP addresses are fixed-length binary strings — Correct; IP addresses fit the key model.  
B) ✓ Because they allow efficient prefix matching — Critical for routing decisions.  
C) ✗ Because they minimize memory usage compared to hash tables — Memory usage is not necessarily minimal.  
D) ✗ Because they support floating-point keys — IP addresses are binary, not floating-point.  

**Correct:** A, B


#### 18. What is a key challenge when using Digital Search Trees with variable-length keys?  
A) ✓ Handling keys that terminate at internal nodes — Correct; variable-length keys may end inside the tree.  
B) ✗ Ensuring all keys have the same length — Variable-length keys by definition differ in length.  
C) ✗ Balancing the tree after every insertion — DSTs do not require balancing.  
D) ✗ Converting keys to decimal format — No conversion needed.  

**Correct:** A


#### 19. Which of the following statements about the height of a Digital Search Tree is true?  
A) ✗ The height is always equal to the number of keys — Height depends on key length, not number of keys.  
B) ✓ The height depends on the number of bits in the keys — Correct; height relates to key length.  
C) ✗ The height is independent of key length — Incorrect; key length affects height.  
D) ✗ The height is always logarithmic in the number of keys — Not guaranteed; depends on key bit patterns.  

**Correct:** B


#### 20. In a Binary Trie with variable-length keys, what does a null left or right pair field indicate?  
A) ✓ That there is no key terminating at the root of that subtree — Correct; null means no terminating key there.  
B) ✗ That the subtree is empty — Subtree may exist even if pair field is null.  
C) ✗ That the key is longer than the maximum allowed length — Not related to pair field nullity.  
D) ✗ That the key must be stored in a linked list instead — No linked lists used here.  

**Correct:** A