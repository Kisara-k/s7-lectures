## 12. Digital Search Trees and Binary Tries

## Questions

#### 1. What is the primary data type used as keys in Digital Search Trees and Binary Tries?  
A) Character strings  
B) Integer numbers  
C) Floating-point numbers  
D) Binary bit strings  

#### 2. Which of the following statements about Digital Search Trees (DST) is true?  
A) The left subtree contains pairs whose keys start with 0.  
B) The right subtree contains pairs whose keys start with 1.  
C) The root contains all dictionary pairs.  
D) DSTs only work with variable-length keys.  

#### 3. In a Digital Search Tree, what happens to the keys after the root node is assigned a dictionary pair?  
A) Keys are stored in a linked list attached to the root.  
B) Keys are split into left and right subtrees based on the first bit of their remaining bits.  
C) Keys are sorted numerically.  
D) All keys are stored in the root node.  

#### 4. Which of the following applications commonly use Digital Search Trees or Binary Tries?  
A) Firewalls  
B) IP routing  
C) Packet classification  
D) Sorting large arrays  

#### 5. What is the time complexity of search, insert, and delete operations in Digital Search Trees?  
A) O(log n)  
B) O(1)  
C) O(#bits in a key)  
D) O(n)  

#### 6. Why can operations on Digital Search Trees be expensive when keys are very long?  
A) Because the tree must be rebalanced after every operation.  
B) Because keys must be converted to decimal first.  
C) Because the number of key comparisons depends on the height of the tree, which grows with key length.  
D) Because the keys are stored in linked lists.  

#### 7. Which of the following is true about Binary Tries compared to Digital Search Trees?  
A) Binary Tries only work with variable-length keys.  
B) Binary Tries have at most one key comparison per operation.  
C) Element nodes in Binary Tries have no child pointers.  
D) Branch nodes in Binary Tries contain data fields.  

#### 8. In a Binary Trie, what is the role of branch nodes?  
A) They contain left and right child pointers but no data fields.  
B) They terminate the search.  
C) They store dictionary pairs.  
D) They store the entire key.  

#### 9. How do element nodes in a Binary Trie differ from branch nodes?  
A) Element nodes contain left and right child pointers.  
B) Element nodes have child pointers.  
C) Element nodes are always at the root.  
D) Element nodes contain data fields but no child pointers.  

#### 10. For variable-length keys in Binary Tries, what is the purpose of the left and right pair fields?  
A) To store all keys starting with 0 or 1.  
B) To store the entire subtree.  
C) To store pairs whose keys terminate at the root of the respective subtree.  
D) To store pointers to the next node.  

#### 11. Which of the following statements about fixed-length key insertion in Binary Tries is correct?  
A) Insertion complexity depends on the number of keys already in the tree.  
B) Inserting a key can sometimes require zero key comparisons.  
C) Insertion is always O(n) where n is the number of keys.  
D) Inserting a key always requires multiple key comparisons.  

#### 12. What is the maximum number of key comparisons required for a search operation in a Binary Trie?  
A) Equal to the height of the tree  
B) Equal to the length of the key  
C) At most one  
D) Equal to the number of keys in the tree  

#### 13. Which of the following is NOT a characteristic of Digital Search Trees?  
A) The root node contains one dictionary pair.  
B) The tree structure depends on the numeric value of keys.  
C) Keys are split based on their bits.  
D) Left and right subtrees are themselves Digital Search Trees on remaining bits.  

#### 14. When deleting a key from a fixed-length Binary Trie, which of the following is true?  
A) Deletion is impossible without rebalancing the tree.  
B) Deletion complexity depends on the length of the key.  
C) Deletion always requires multiple key comparisons.  
D) Deletion can sometimes be done with only one key comparison.  

#### 15. How does the structure of a Digital Search Tree change when inserting a key that shares a prefix with an existing key?  
A) The new key replaces the existing key at the root.  
B) The tree branches further down at the first differing bit.  
C) The tree remains unchanged.  
D) The new key is appended as a sibling node.  

#### 16. Which of the following best describes the relationship between Digital Search Trees and radix sort?  
A) Digital Search Trees use radix sort internally for balancing.  
B) Digital Search Trees are an analog of radix sort applied to searching.  
C) Digital Search Trees are a sorting algorithm unrelated to radix sort.  
D) Radix sort is a special case of Digital Search Trees.  

#### 17. In the context of IP routing, why are Digital Search Trees or Binary Tries suitable data structures?  
A) Because they allow efficient prefix matching.  
B) Because IP addresses are fixed-length binary strings.  
C) Because they support floating-point keys.  
D) Because they minimize memory usage compared to hash tables.  

#### 18. What is a key challenge when using Digital Search Trees with variable-length keys?  
A) Ensuring all keys have the same length.  
B) Converting keys to decimal format.  
C) Balancing the tree after every insertion.  
D) Handling keys that terminate at internal nodes.  

#### 19. Which of the following statements about the height of a Digital Search Tree is true?  
A) The height is always equal to the number of keys.  
B) The height is always logarithmic in the number of keys.  
C) The height depends on the number of bits in the keys.  
D) The height is independent of key length.  

#### 20. In a Binary Trie with variable-length keys, what does a null left or right pair field indicate?  
A) That there is no key terminating at the root of that subtree.  
B) That the subtree is empty.  
C) That the key is longer than the maximum allowed length.  
D) That the key must be stored in a linked list instead.  



<br>

## Answers

#### 1. What is the primary data type used as keys in Digital Search Trees and Binary Tries?  
A) ✗ Character strings — Keys are binary strings, not general character strings.  
B) ✗ Integer numbers — Keys are binary bit strings, not integers per se.  
C) ✗ Floating-point numbers — Not used as keys here.  
D) ✓ Binary bit strings — Correct; keys are represented as binary strings.  

**Correct:** D


#### 2. Which of the following statements about Digital Search Trees (DST) is true?  
A) ✓ The left subtree contains pairs whose keys start with 0 — Correct by definition.  
B) ✓ The right subtree contains pairs whose keys start with 1 — Correct by definition.  
C) ✗ The root contains all dictionary pairs — The root contains only one dictionary pair.  
D) ✗ DSTs only work with variable-length keys — DSTs assume fixed or variable length but are not limited to variable length only.  

**Correct:** A, B


#### 3. In a Digital Search Tree, what happens to the keys after the root node is assigned a dictionary pair?  
A) ✗ Keys are stored in a linked list attached to the root — No linked lists involved.  
B) ✓ Keys are split into left and right subtrees based on the first bit of their remaining bits — Correct; keys are partitioned by bit prefixes.  
C) ✗ Keys are sorted numerically — Sorting is not the mechanism used.  
D) ✗ All keys are stored in the root node — Only one pair is stored at the root.  

**Correct:** B


#### 4. Which of the following applications commonly use Digital Search Trees or Binary Tries?  
A) ✓ Firewalls — Correct; packet filtering uses prefix-based structures.  
B) ✓ IP routing — Correct; IP addresses are binary keys.  
C) ✓ Packet classification — Correct; requires prefix matching.  
D) ✗ Sorting large arrays — Not a typical application of DST or tries.  

**Correct:** A, B, C


#### 5. What is the time complexity of search, insert, and delete operations in Digital Search Trees?  
A) ✗ O(log n) — Complexity depends on key length, not number of keys.  
B) ✗ O(1) — Not constant time.  
C) ✓ O(#bits in a key) — Correct; operations depend on key length.  
D) ✗ O(n) — Not dependent on number of keys linearly.  

**Correct:** C


#### 6. Why can operations on Digital Search Trees be expensive when keys are very long?  
A) ✗ Because the tree must be rebalanced after every operation — DSTs do not require rebalancing.  
B) ✗ Because keys must be converted to decimal first — No conversion needed.  
C) ✓ Because the number of key comparisons depends on the height of the tree, which grows with key length — Correct; height relates to bits in keys.  
D) ✗ Because the keys are stored in linked lists — Keys are stored in tree nodes, not lists.  

**Correct:** C


#### 7. Which of the following is true about Binary Tries compared to Digital Search Trees?  
A) ✗ Binary Tries only work with variable-length keys — They can work with fixed-length keys too.  
B) ✓ Binary Tries have at most one key comparison per operation — Correct; tries minimize comparisons.  
C) ✓ Element nodes in Binary Tries have no child pointers — Correct; element nodes store data only.  
D) ✗ Branch nodes in Binary Tries contain data fields — Branch nodes have no data fields.  

**Correct:** B, C


#### 8. In a Binary Trie, what is the role of branch nodes?  
A) ✓ They contain left and right child pointers but no data fields — Correct; they guide traversal.  
B) ✗ They terminate the search — Element nodes terminate search.  
C) ✗ They store dictionary pairs — Branch nodes do not store data.  
D) ✗ They store the entire key — Keys are implicit in path, not stored.  

**Correct:** A


#### 9. How do element nodes in a Binary Trie differ from branch nodes?  
A) ✗ Element nodes contain left and right child pointers — Only branch nodes do.  
B) ✗ Element nodes have child pointers — They do not have child pointers.  
C) ✗ Element nodes are always at the root — They can be anywhere.  
D) ✓ Element nodes contain data fields but no child pointers — Correct; they hold dictionary pairs.  

**Correct:** D


#### 10. For variable-length keys in Binary Tries, what is the purpose of the left and right pair fields?  
A) ✗ To store all keys starting with 0 or 1 — This is done by subtrees, not pair fields.  
B) ✗ To store the entire subtree — Subtrees are represented by child pointers.  
C) ✓ To store pairs whose keys terminate at the root of the respective subtree — Correct; handles keys ending at internal nodes.  
D) ✗ To store pointers to the next node — They store data pairs, not pointers.  

**Correct:** C


#### 11. Which of the following statements about fixed-length key insertion in Binary Tries is correct?  
A) ✗ Insertion complexity depends on the number of keys already in the tree — Complexity depends on key length.  
B) ✓ Inserting a key can sometimes require zero key comparisons — Correct; if no conflict arises.  
C) ✗ Insertion is always O(n) where n is the number of keys — Complexity depends on key length, not number of keys.  
D) ✗ Inserting a key always requires multiple key comparisons — Sometimes zero or one comparison suffices.  

**Correct:** B


#### 12. What is the maximum number of key comparisons required for a search operation in a Binary Trie?  
A) ✗ Equal to the height of the tree — Height can be large, but tries optimize comparisons.  
B) ✗ Equal to the length of the key — Comparisons minimized to one.  
C) ✓ At most one — Correct; tries guarantee at most one key comparison.  
D) ✗ Equal to the number of keys in the tree — No, independent of number of keys.  

**Correct:** C


#### 13. Which of the following is NOT a characteristic of Digital Search Trees?  
A) ✗ The root node contains one dictionary pair — True for DST.  
B) ✓ The tree structure depends on the numeric value of keys — Incorrect; structure depends on bit prefixes, not numeric value.  
C) ✗ Keys are split based on their bits — This is a defining characteristic.  
D) ✗ Left and right subtrees are themselves Digital Search Trees on remaining bits — True by definition.  

**Correct:** B


#### 14. When deleting a key from a fixed-length Binary Trie, which of the following is true?  
A) ✗ Deletion is impossible without rebalancing the tree — No rebalancing needed.  
B) ✗ Deletion complexity depends on the length of the key — Complexity depends on key length but comparisons can be minimal.  
C) ✗ Deletion always requires multiple key comparisons — Sometimes only one comparison is needed.  
D) ✓ Deletion can sometimes be done with only one key comparison — Correct; deletion can be efficient.  

**Correct:** D


#### 15. How does the structure of a Digital Search Tree change when inserting a key that shares a prefix with an existing key?  
A) ✗ The new key replaces the existing key at the root — Root remains unchanged unless empty.  
B) ✓ The tree branches further down at the first differing bit — Correct; branching occurs at first bit difference.  
C) ✗ The tree remains unchanged — Tree structure changes to accommodate new key.  
D) ✗ The new key is appended as a sibling node — Not how DSTs organize keys.  

**Correct:** B


#### 16. Which of the following best describes the relationship between Digital Search Trees and radix sort?  
A) ✗ Digital Search Trees use radix sort internally for balancing — No balancing or sorting internally.  
B) ✓ Digital Search Trees are an analog of radix sort applied to searching — Correct; DSTs mimic radix sort logic for search.  
C) ✗ Digital Search Trees are a sorting algorithm unrelated to radix sort — They are related.  
D) ✗ Radix sort is a special case of Digital Search Trees — Radix sort is a sorting algorithm, not a tree.  

**Correct:** B


#### 17. In the context of IP routing, why are Digital Search Trees or Binary Tries suitable data structures?  
A) ✓ Because they allow efficient prefix matching — Critical for routing decisions.  
B) ✓ Because IP addresses are fixed-length binary strings — Correct; IP addresses fit the key model.  
C) ✗ Because they support floating-point keys — IP addresses are binary, not floating-point.  
D) ✗ Because they minimize memory usage compared to hash tables — Memory usage is not necessarily minimal.  

**Correct:** A, B


#### 18. What is a key challenge when using Digital Search Trees with variable-length keys?  
A) ✗ Ensuring all keys have the same length — Variable-length keys by definition differ in length.  
B) ✗ Converting keys to decimal format — No conversion needed.  
C) ✗ Balancing the tree after every insertion — DSTs do not require balancing.  
D) ✓ Handling keys that terminate at internal nodes — Correct; variable-length keys may end inside the tree.  

**Correct:** D


#### 19. Which of the following statements about the height of a Digital Search Tree is true?  
A) ✗ The height is always equal to the number of keys — Height depends on key length, not number of keys.  
B) ✗ The height is always logarithmic in the number of keys — Not guaranteed; depends on key bit patterns.  
C) ✓ The height depends on the number of bits in the keys — Correct; height relates to key length.  
D) ✗ The height is independent of key length — Incorrect; key length affects height.  

**Correct:** C


#### 20. In a Binary Trie with variable-length keys, what does a null left or right pair field indicate?  
A) ✓ That there is no key terminating at the root of that subtree — Correct; null means no terminating key there.  
B) ✗ That the subtree is empty — Subtree may exist even if pair field is null.  
C) ✗ That the key is longer than the maximum allowed length — Not related to pair field nullity.  
D) ✗ That the key must be stored in a linked list instead — No linked lists used here.  

**Correct:** A