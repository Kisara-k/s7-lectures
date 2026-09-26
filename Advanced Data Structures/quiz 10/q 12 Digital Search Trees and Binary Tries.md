## 12. Digital Search Trees and Binary Tries

## Questions

#### 1. Which of the following statements correctly describe the structure of a digital search tree for fixed-length binary keys?  
A) The root contains one dictionary pair chosen arbitrarily from the set of keys.  
B) All keys with a leading 0 bit are stored in the right subtree.  
C) The left and right subtrees are themselves digital search trees on the remaining bits of the keys.  
D) Keys are stored only at the leaves of the tree.

#### 2. What is the time complexity of search, insert, and delete operations in a digital search tree with keys of length *k* bits?  
A) O(k)  
B) O(log n) where n is the number of keys  
C) O(height of the tree)  
D) O(k²)

#### 3. Which of the following are true about binary tries with fixed-length keys?  
A) Branch nodes contain data fields holding dictionary pairs.  
B) Branch nodes have left and right child pointers but no data fields.  
C) Element nodes have no child pointers but contain data fields.  
D) Binary tries require multiple key comparisons per search operation.

#### 4. In the context of variable-length keys in a binary trie, what is the role of the left and right pair fields at a node?  
A) They store pairs whose keys terminate exactly at the root of the left or right subtree.  
B) They store pairs that would otherwise be stored deeper in the subtree.  
C) They always contain non-null values.  
D) They replace the need for child pointers in the trie.

#### 5. Which of the following applications are typical use cases for digital search trees and binary tries?  
A) IP routing for IPv4 and IPv6 addresses  
B) Sorting large arrays of integers using comparison-based sorting  
C) Packet classification in network firewalls  
D) Implementing balanced binary search trees like AVL or Red-Black trees

#### 6. Consider inserting the key 1101 into a fixed-length digital search tree. Which of the following statements about the number of key comparisons is correct?  
A) Inserting 1101 always requires zero key comparisons.  
B) The first insertion of 1101 requires one key comparison.  
C) Subsequent insertions of 1101 may require one or more key comparisons depending on the tree structure.  
D) Key comparisons depend only on the length of the key, not on the tree structure.

#### 7. Why can digital search trees become expensive when keys are very long?  
A) Because the number of key comparisons grows exponentially with key length.  
B) Because the complexity of operations is proportional to the number of bits in the key.  
C) Because the height of the tree can become very large, increasing search time.  
D) Because keys must be compared character-by-character rather than bit-by-bit.

#### 8. Which of the following correctly describe differences between digital search trees and binary tries?  
A) Digital search trees store dictionary pairs at internal nodes, while binary tries store pairs only at leaves.  
B) Binary tries have at most one key comparison per operation, while digital search trees may have multiple.  
C) Digital search trees require child pointers only for keys starting with 1.  
D) Binary tries can handle variable-length keys by using left and right pair fields.

#### 9. In a digital search tree, what happens to keys that share the same prefix bits?  
A) They are stored in the same subtree corresponding to that prefix.  
B) They are split between left and right subtrees randomly.  
C) They are stored at the root node.  
D) They cause the tree to become unbalanced and inefficient.

#### 10. Regarding deletion operations in fixed-length digital search trees and binary tries, which statements are true?  
A) Deletion complexity is O(number of bits in the key).  
B) Deletion may require one or more key comparisons depending on the key and tree structure.  
C) Deletion in variable-length key tries is trivial and requires no comparisons.  
D) Deletion always requires traversing the entire height of the tree.



<br>

## Answers

#### 1. Which of the following statements correctly describe the structure of a digital search tree for fixed-length binary keys?  
A) ✓ The root contains one dictionary pair chosen arbitrarily from the set of keys.  
B) ✗ Keys with leading 0 go to the left subtree, not the right.  
C) ✓ Left and right subtrees are digital search trees on remaining bits.  
D) ✗ Keys can be stored at internal nodes, not only leaves.

**Correct:** A, C


#### 2. What is the time complexity of search, insert, and delete operations in a digital search tree with keys of length *k* bits?  
A) ✓ Complexity is O(k), proportional to bits in key.  
B) ✗ Not O(log n), since structure depends on bits, not number of keys.  
C) ✓ Number of key comparisons is O(height), which is O(k).  
D) ✗ Complexity is linear in bits, not quadratic.

**Correct:** A, C


#### 3. Which of the following are true about binary tries with fixed-length keys?  
A) ✗ Branch nodes do not contain data fields.  
B) ✓ Branch nodes have left and right child pointers but no data fields.  
C) ✓ Element nodes have no child pointers but contain data fields.  
D) ✗ At most one key comparison per search, not multiple.

**Correct:** B, C


#### 4. In the context of variable-length keys in a binary trie, what is the role of the left and right pair fields at a node?  
A) ✓ They store pairs whose keys terminate exactly at the root of the left or right subtree.  
B) ✓ They also store the single pair that might otherwise be deeper in the subtree.  
C) ✗ These fields can be null if no such pair exists.  
D) ✗ They do not replace child pointers; child pointers still exist.

**Correct:** A, B


#### 5. Which of the following applications are typical use cases for digital search trees and binary tries?  
A) ✓ IP routing for IPv4 and IPv6 addresses is a classic application.  
B) ✗ Radix-based structures are not used for general comparison-based sorting.  
C) ✓ Packet classification in firewalls is a known application.  
D) ✗ Balanced BSTs like AVL or Red-Black trees are different data structures.

**Correct:** A, C


#### 6. Consider inserting the key 1101 into a fixed-length digital search tree. Which of the following statements about the number of key comparisons is correct?  
A) ✗ First insertion cannot require zero comparisons if tree is non-empty.  
B) ✓ First insertion of 1101 may require one key comparison to find position.  
C) ✓ Subsequent insertions depend on tree structure, so comparisons may vary.  
D) ✗ Comparisons depend on tree structure, not just key length.

**Correct:** B, C


#### 7. Why can digital search trees become expensive when keys are very long?  
A) ✗ Number of comparisons grows linearly, not exponentially, with key length.  
B) ✓ Complexity is proportional to number of bits in the key.  
C) ✓ Height can be large, increasing search time.  
D) ✗ Keys are compared bit-by-bit, not character-by-character.

**Correct:** B, C


#### 8. Which of the following correctly describe differences between digital search trees and binary tries?  
A) ✓ Digital search trees store pairs at internal nodes; binary tries store pairs at element nodes (leaves).  
B) ✓ Binary tries have at most one key comparison per operation; digital search trees may have more.  
C) ✗ Digital search trees require child pointers for both 0 and 1 branches, not only for keys starting with 1.  
D) ✓ Binary tries handle variable-length keys using left and right pair fields.

**Correct:** A, B, D


#### 9. In a digital search tree, what happens to keys that share the same prefix bits?  
A) ✓ They are stored in the same subtree corresponding to that prefix.  
B) ✗ Keys are not split randomly; splitting is based on bit values.  
C) ✗ Keys are not stored at the root unless root’s key matches.  
D) ✗ Sharing prefixes does not inherently cause imbalance or inefficiency.

**Correct:** A


#### 10. Regarding deletion operations in fixed-length digital search trees and binary tries, which statements are true?  
A) ✓ Deletion complexity is O(number of bits in the key).  
B) ✓ Deletion may require one or more key comparisons depending on key and tree structure.  
C) ✗ Deletion in variable-length tries is not trivial and may require comparisons.  
D) ✗ Deletion does not always require traversing the entire height; depends on key.

**Correct:** A, B