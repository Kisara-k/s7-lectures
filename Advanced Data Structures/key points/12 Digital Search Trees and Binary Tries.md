## 12. Digital Search Trees and Binary Tries

## Key Points

#### 1. 🌐 Digital Search Trees (DSTs)  
- DSTs store keys as binary strings of fixed length.  
- The root contains one dictionary pair.  
- Keys with first bit 0 go to the left subtree; keys with first bit 1 go to the right subtree.  
- Left and right subtrees are DSTs on the remaining bits.  
- Search, insert, and delete operations have time complexity O(#bits in key).  
- Number of key comparisons is O(height of the tree).  
- Operations become expensive for very long keys.

#### 2. 🌳 Binary Tries  
- Binary tries are binary trees with branch nodes (no data) and element nodes (data only).  
- Branch nodes have left and right child pointers but no data fields.  
- Element nodes have data fields but no child pointers.  
- Designed for fixed-length keys.  
- At most one key comparison is needed per search operation.

#### 3. 🔄 Variable Length Keys in Binary Tries  
- Nodes have left and right child pointers plus left and right pair fields.  
- Left pair stores the key terminating at the root of the left subtree or the single key otherwise stored there.  
- Right pair stores the key terminating at the root of the right subtree or the single key otherwise stored there.  
- Pair fields are null if no key terminates at that node.  
- Allows efficient search with at most one key comparison even for variable-length keys.

#### 4. ⚙️ Operations Complexity and Behavior  
- Search, insert, and delete in DSTs are O(#bits in key).  
- Binary tries require at most one key comparison per search.  
- Insertions in fixed-length keys may require zero or one key comparison.  
- Deletions in fixed-length keys may require one key comparison.  
- Deletion for variable-length keys is more complex and involves updating pair fields.

#### 5. 🌍 Applications  
- Used in IP routing, packet classification, and firewalls.  
- IPv4 addresses are 32-bit keys; IPv6 addresses are 128-bit keys.



<br>

