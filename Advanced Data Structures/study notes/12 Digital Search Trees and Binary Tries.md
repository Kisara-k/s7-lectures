## 12. Digital Search Trees and Binary Tries

## Study Notes

### 1. 🌐 Introduction to Digital Search Trees and Binary Tries

In this lecture, we explore two important data structures used for efficient searching and storing of keys that are represented as binary strings: **Digital Search Trees (DSTs)** and **Binary Tries**. These structures are particularly useful when keys are sequences of bits, such as IP addresses in networking. Unlike traditional search trees that compare keys as whole entities, these structures work by examining individual bits of the keys, making them analogous to radix sort but applied to searching.

The keys can be either **fixed length** (all keys have the same number of bits, e.g., 4-bit keys like 0110, 0010) or **variable length** (keys can have different lengths, e.g., 01, 00, 101). These data structures are widely used in applications like IP routing, packet classification, and firewall filtering, where keys are often IP addresses (IPv4 with 32 bits, IPv6 with 128 bits).


### 2. 🌲 Digital Search Trees (DSTs)

#### What is a Digital Search Tree?

A Digital Search Tree is a binary tree designed to store keys that are binary strings of fixed length. The main idea is to use the bits of the key to decide the path in the tree:

- The **root** node contains one dictionary pair (a key-value pair).
- All keys whose first bit is **0** go to the **left subtree**.
- All keys whose first bit is **1** go to the **right subtree**.
- This splitting continues recursively on the remaining bits of the keys in the subtrees.

#### How does it work?

Imagine you have a set of keys, each represented as a binary string of fixed length. When inserting or searching for a key, you look at the first bit:

- If it’s 0, you move to the left child.
- If it’s 1, you move to the right child.

At each level, you look at the next bit of the key until you reach a node that contains the key or where the key should be inserted.

#### Example of Insertion

- Start with an empty DST.
- Insert key **0110**: The root now contains this key.
- Insert key **0010**: Since the first bit is 0, it goes to the left subtree of the root.
- Insert key **1001**: First bit is 1, so it goes to the right subtree.
- Insert key **1011**: Also goes to the right subtree, but further down depending on the next bits.
- Insert key **0000**: Goes to the left subtree, branching further.

#### Complexity

- The time complexity for **search**, **insert**, and **delete** operations is proportional to the number of bits in the key, i.e., **O(#bits)**.
- The number of key comparisons depends on the height of the tree.
- This can be expensive if keys are very long (e.g., 128-bit IPv6 addresses).


### 3. 🌳 Binary Tries

#### What is a Binary Trie?

A Binary Trie is a special kind of digital search tree optimized for fixed-length keys. It is a binary tree where:

- **Branch nodes** have two child pointers (left and right) but **no data**.
- **Element nodes** (leaves) contain the actual dictionary pair (key-value) but have **no children**.

#### How does it differ from DST?

- In a Binary Trie, each internal node represents a bit position in the key.
- The path from the root to a leaf corresponds to the bits of the key.
- At most **one key comparison** is needed per search operation because the structure guides the search bit-by-bit.

#### Why is this useful?

Because the search path is determined by the bits of the key, you avoid multiple key comparisons at each node. This makes searching very efficient, especially for fixed-length keys.


### 4. 🔄 Handling Variable Length Keys in Binary Tries

#### What changes with variable length keys?

When keys have different lengths, the Binary Trie needs to handle keys that may terminate at different depths in the tree.

- Each node has **left and right child pointers**.
- Additionally, each node has **left and right pair fields**:
  - The **left pair** holds the key that terminates exactly at the root of the left subtree or the single key that would otherwise be stored there.
  - The **right pair** holds the key that terminates at the root of the right subtree or the single key that would otherwise be stored there.
- If no key terminates at that node, the pair field is null.

#### Why is this important?

This design allows the trie to store keys of varying lengths without losing the efficiency of bitwise navigation. It ensures that at most one key comparison is needed during search, even if keys differ in length.


### 5. ⚙️ Operations: Search, Insert, and Delete

#### Search

- In both DSTs and Binary Tries, searching involves following the path dictated by the bits of the key.
- For DSTs, the complexity is **O(#bits)**.
- For Binary Tries, at most **one key comparison** is needed, making it more efficient.

#### Insert

- Inserting a key involves navigating the tree according to the bits of the key.
- For fixed-length keys, insertion may require zero or one key comparison depending on the structure.
- For variable-length keys, the insertion process also updates the left/right pair fields if the key terminates at a node.

#### Delete

- Deletion involves finding the key and removing it.
- For fixed-length keys, deletion may require one key comparison.
- For variable-length keys, deletion is more complex because it may involve updating pair fields and restructuring the tree.
- The lecture mentions deletion for variable-length keys as an exercise, indicating it is more involved.


### 6. 📝 Summary and Applications

Digital Search Trees and Binary Tries are powerful data structures for managing keys represented as binary strings. They are especially useful in networking contexts like IP routing, where keys are IP addresses of fixed or variable length.

- **Digital Search Trees** split keys based on bits and store dictionary pairs in nodes.
- **Binary Tries** optimize this by separating branch nodes (no data) and element nodes (data only), enabling efficient searches with minimal comparisons.
- Handling **variable length keys** requires additional pair fields to store keys terminating at internal nodes.
- Operations like search, insert, and delete have complexities tied to the length of the keys, with tries offering more efficient search performance.

Understanding these structures helps in designing efficient algorithms for routing, packet classification, and other applications where keys are naturally represented as bit strings.


If you want, I can also provide diagrams or code examples to illustrate these concepts further!