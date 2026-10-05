## 12. Digital Search Trees and Binary Tries

## Questions

#### 1. Which of the following statements correctly describe the structure of a digital search tree for fixed-length binary keys?  
A) Keys are stored only at the leaves of the tree.  
B) The left and right subtrees are themselves digital search trees on the remaining bits of the keys.  
C) The root contains one dictionary pair chosen arbitrarily from the set of keys.  
D) All keys with a leading 0 bit are stored in the right subtree.  

#### 2. What is the time complexity of search, insert, and delete operations in a digital search tree with keys of length *k* bits?  
A) O(log n) where n is the number of keys  
B) O(k²)  
C) O(k)  
D) O(height of the tree)  

#### 3. Which of the following are true about binary tries with fixed-length keys?  
A) Branch nodes have left and right child pointers but no data fields.  
B) Element nodes have no child pointers but contain data fields.  
C) Binary tries require multiple key comparisons per search operation.  
D) Branch nodes contain data fields holding dictionary pairs.  

#### 4. In the context of variable-length keys in a binary trie, what is the role of the left and right pair fields at a node?  
A) They store pairs whose keys terminate exactly at the root of the left or right subtree.  
B) They always contain non-null values.  
C) They replace the need for child pointers in the trie.  
D) They store pairs that would otherwise be stored deeper in the subtree.  

#### 5. Which of the following applications are typical use cases for digital search trees and binary tries?  
A) Packet classification in network firewalls  
B) Implementing balanced binary search trees like AVL or Red-Black trees  
C) IP routing for IPv4 and IPv6 addresses  
D) Sorting large arrays of integers using comparison-based sorting  

#### 6. Consider inserting the key 1101 into a fixed-length digital search tree. Which of the following statements about the number of key comparisons is correct?  
A) Inserting 1101 always requires zero key comparisons.  
B) Key comparisons depend only on the length of the key, not on the tree structure.  
C) The first insertion of 1101 requires one key comparison.  
D) Subsequent insertions of 1101 may require one or more key comparisons depending on the tree structure.  

#### 7. Why can digital search trees become expensive when keys are very long?  
A) Because keys must be compared character-by-character rather than bit-by-bit.  
B) Because the height of the tree can become very large, increasing search time.  
C) Because the complexity of operations is proportional to the number of bits in the key.  
D) Because the number of key comparisons grows exponentially with key length.  

#### 8. Which of the following correctly describe differences between digital search trees and binary tries?  
A) Digital search trees require child pointers only for keys starting with 1.  
B) Binary tries can handle variable-length keys by using left and right pair fields.  
C) Digital search trees store dictionary pairs at internal nodes, while binary tries store pairs only at leaves.  
D) Binary tries have at most one key comparison per operation, while digital search trees may have multiple.  

#### 9. In a digital search tree, what happens to keys that share the same prefix bits?  
A) They are stored at the root node.  
B) They are split between left and right subtrees randomly.  
C) They cause the tree to become unbalanced and inefficient.  
D) They are stored in the same subtree corresponding to that prefix.  

#### 10. Regarding deletion operations in fixed-length digital search trees and binary tries, which statements are true?  
A) Deletion complexity is O(number of bits in the key).  
B) Deletion may require one or more key comparisons depending on the key and tree structure.  
C) Deletion always requires traversing the entire height of the tree.  
D) Deletion in variable-length key tries is trivial and requires no comparisons.  



<br>

## Answers

#### 1. Which of the following statements correctly describe the structure of a digital search tree for fixed-length binary keys?  
A) ✗ Keys can be stored at internal nodes, not only leaves.  
B) ✓ Left and right subtrees are digital search trees on remaining bits.  
C) ✓ The root contains one dictionary pair chosen arbitrarily from the set of keys.  
D) ✗ Keys with leading 0 go to the left subtree, not the right.  

**Correct:** B, C


#### 2. What is the time complexity of search, insert, and delete operations in a digital search tree with keys of length *k* bits?  
A) ✗ Not O(log n), since structure depends on bits, not number of keys.  
B) ✗ Complexity is linear in bits, not quadratic.  
C) ✓ Complexity is O(k), proportional to bits in key.  
D) ✓ Number of key comparisons is O(height), which is O(k).  

**Correct:** C, D


#### 3. Which of the following are true about binary tries with fixed-length keys?  
A) ✓ Branch nodes have left and right child pointers but no data fields.  
B) ✓ Element nodes have no child pointers but contain data fields.  
C) ✗ At most one key comparison per search, not multiple.  
D) ✗ Branch nodes do not contain data fields.  

**Correct:** A, B


#### 4. In the context of variable-length keys in a binary trie, what is the role of the left and right pair fields at a node?  
A) ✓ They store pairs whose keys terminate exactly at the root of the left or right subtree.  
B) ✗ These fields can be null if no such pair exists.  
C) ✗ They do not replace child pointers; child pointers still exist.  
D) ✓ They also store the single pair that might otherwise be deeper in the subtree.  

**Correct:** A, D


#### 5. Which of the following applications are typical use cases for digital search trees and binary tries?  
A) ✓ Packet classification in firewalls is a known application.  
B) ✗ Balanced BSTs like AVL or Red-Black trees are different data structures.  
C) ✓ IP routing for IPv4 and IPv6 addresses is a classic application.  
D) ✗ Radix-based structures are not used for general comparison-based sorting.  

**Correct:** A, C


#### 6. Consider inserting the key 1101 into a fixed-length digital search tree. Which of the following statements about the number of key comparisons is correct?  
A) ✗ First insertion cannot require zero comparisons if tree is non-empty.  
B) ✗ Comparisons depend on tree structure, not just key length.  
C) ✓ First insertion of 1101 may require one key comparison to find position.  
D) ✓ Subsequent insertions depend on tree structure, so comparisons may vary.  

**Correct:** C, D


#### 7. Why can digital search trees become expensive when keys are very long?  
A) ✗ Keys are compared bit-by-bit, not character-by-character.  
B) ✓ Height can be large, increasing search time.  
C) ✓ Complexity is proportional to number of bits in the key.  
D) ✗ Number of comparisons grows linearly, not exponentially, with key length.  

**Correct:** B, C


#### 8. Which of the following correctly describe differences between digital search trees and binary tries?  
A) ✗ Digital search trees require child pointers for both 0 and 1 branches, not only for keys starting with 1.  
B) ✓ Binary tries handle variable-length keys using left and right pair fields.  
C) ✓ Digital search trees store pairs at internal nodes; binary tries store pairs at element nodes (leaves).  
D) ✓ Binary tries have at most one key comparison per operation; digital search trees may have more.  

**Correct:** B, C, D


#### 9. In a digital search tree, what happens to keys that share the same prefix bits?  
A) ✗ Keys are not stored at the root unless root’s key matches.  
B) ✗ Keys are not split randomly; splitting is based on bit values.  
C) ✗ Sharing prefixes does not inherently cause imbalance or inefficiency.  
D) ✓ They are stored in the same subtree corresponding to that prefix.  

**Correct:** D


#### 10. Regarding deletion operations in fixed-length digital search trees and binary tries, which statements are true?  
A) ✓ Deletion complexity is O(number of bits in the key).  
B) ✓ Deletion may require one or more key comparisons depending on key and tree structure.  
C) ✗ Deletion does not always require traversing the entire height; depends on key.  
D) ✗ Deletion in variable-length tries is not trivial and may require comparisons.  

**Correct:** A, B