## 8. Dictionaries and Indexed Search Trees

## Study Notes

### 1. 📚 Introduction to Dictionaries

A **dictionary** is a fundamental data structure used to store a collection of items, where each item is a pair consisting of a **key** and an **element** (or value). The key acts as a unique identifier for the element, allowing efficient access, insertion, and deletion.

- **Key**: A unique identifier used to look up the element.
- **Element**: The data or value associated with the key.

#### Examples of Dictionaries:
- A collection of student records:  
  Each pair is (student name, list of assignment and exam scores). Here, student names are keys and must be distinct.
- Domain names and their owners:  
  Each pair is (domain name, owner information). Domain names are unique keys.

#### Dictionaries with Duplicates
Sometimes, keys are not unique. For example, a word dictionary may have multiple meanings for the same word:
- (bolt, a threaded pin)
- (bolt, a crash of thunder)
- (bolt, to shoot forth suddenly)

In such cases, the dictionary stores multiple pairs with the same key but different elements.


### 2. 🔍 Dictionary Operations

Dictionaries support several key operations, which differ slightly depending on whether the dictionary is **static** or **dynamic**.

#### Static Dictionary
- **Initialize/Create**: Build the dictionary once.
- **Get(key)**: Search for the element associated with the key.
  
Example applications:  
- CD-ROM word dictionaries  
- Geographic databases (cities, rivers, roads)  
- Auto navigation systems

#### Dynamic Dictionary
- **Get(key)**: Search for an element.
- **Put(key, element)**: Insert a new key-element pair.
- **Remove(key)**: Delete a key-element pair.

Dynamic dictionaries allow the collection to change over time.


### 3. 🗃️ Hash Table Dictionaries

Hash tables are a popular implementation of dictionaries offering:

- **Expected O(1) time** for get, put, and remove operations, meaning on average these operations are very fast.
- **Worst-case O(n) time** if many keys collide (hash to the same bucket).
- If collisions are handled by balanced search trees, worst-case time improves to **O(log n)**.

#### Limitations of Hash Tables:
- Not suitable for **nearest match queries** (e.g., find element with smallest key ≥ given key).
- Not suitable for **range queries** (e.g., get all elements with keys in a range).
- Not suitable for **indexed operations** (e.g., get or remove the element with the 3rd smallest key).


### 4. 📦 Bin Packing and Best Fit Heuristic

**Bin packing** is a problem where you have `n` items, each with a size, and bins with a fixed capacity `c`. The goal is to pack all items into the fewest bins possible.

#### Best Fit Heuristic
- Items are packed one at a time in the given order.
- For each item, find the set `S` of bins where the item fits.
- If `S` is empty, start a new bin.
- Otherwise, place the item in the bin with the **least available capacity** that can still hold the item.

#### Example:
Given weights `[4, 7, 3, 6]` and bin capacity `10`:
- Pack 4 into the first bin.
- 7 doesn’t fit in the first bin, so start a new bin.
- 3 fits into the second bin.
- 6 fits into the first bin.

#### Implementation:
- Use a **dynamic dictionary with duplicates** where keys are available capacities and values are bin indices.
- To pack an item of size `s`, find a bin with the smallest available capacity ≥ `s`.
- Update the bin’s available capacity after packing.
- If no bin fits, create a new bin.

#### Complexity:
- Using a balanced binary search tree, each get, put, or remove operation takes **O(log n)**.
- Total complexity for packing `n` items is **O(n log n)**.


### 5. 🌳 Indexed Binary Search Trees (BST)

An **Indexed BST** is a binary search tree augmented with extra information to support efficient indexed operations.

#### Key Idea:
Each node stores an additional field called `leftSize`, which is the number of nodes in its left subtree.

#### Why is this useful?
- It allows quick determination of the **rank** of an element (its position in sorted order).
- Enables operations like:
  - `get(index)`: Retrieve the element at a given position.
  - `remove(index)`: Remove the element at a given position.

#### How `get(index)` works:
- If `index == leftSize` of the current node, return the current node’s element.
- If `index < leftSize`, recurse into the left subtree.
- If `index > leftSize`, recurse into the right subtree with adjusted index `index - leftSize - 1`.

#### Example:
For a sorted list `[2,6,7,8,10,15,18,20,25,30,35,40]`, the indexed BST can quickly find the element at any position.


### 6. ⚙️ Performance of Indexed Structures

#### Linear List Implementations:
- Arrays and linked chains support get, put, and remove operations.
- Arrays provide fast access but slow insertions/removals.
- Chains (linked lists) have slow access times.

#### Indexed AVL Tree (IAVL):
- A balanced binary search tree variant.
- Supports get, put, and remove in **O(log n)** time.
- Experimental results show IAVL is much faster than chains and only slightly slower than arrays for get operations.
- For 40,000 operations, IAVL performs well in both average and worst cases.


### 7. 🔎 Static Dictionaries and Optimal Binary Search Trees

#### Static Dictionaries:
- Contain fixed items with unique keys.
- Operations: initialize/create and get (search).

#### Perfect Hashing:
- Hash functions with no collisions.
- Minimal perfect hashing uses space exactly equal to the number of keys.
- Construction takes **O(n)** time.
- Search is **O(1)** time.

#### Search Trees for Static Dictionaries:
- Useful when hashing is inefficient for extended operations like range search or nearest match.
- Each key has an estimated access frequency (probability).
- Goal: build a binary search tree minimizing the **expected search cost** (weighted path length).


### 8. 🧮 Cost and Construction of Optimal Binary Search Trees

#### Search Types:
- **Successful search**: key is in the dictionary, ends at an internal node.
- **Unsuccessful search**: key not in dictionary, ends at an external (failure) node.

#### Nodes:
- A BST with `n` internal nodes has `n+1` external nodes.
- Keys are sorted: `key(s1) < key(s2) < ... < key(sn)`.
- External nodes represent intervals between keys.

#### Cost Calculation:
- Let `p_i` be the probability of searching for key `s_i`.
- Let `q_i` be the probability of searching for a key between `s_i` and `s_{i+1}`.
- The cost is the weighted sum of the levels of internal and external nodes.

#### Dynamic Programming Approach:
- Define `T_i_j` as the least cost tree for keys `a_{i+1}` to `a_j`.
- Use recursive formulas to compute costs and roots for subtrees.
- Complexity is **O(n^3)** but can be optimized to **O(n^2)**.


### 9. 🔄 Dynamic Dictionaries and Operations

Dynamic dictionaries support:

- **get(key)**: search for an element.
- **put(key, element)**: insert a new element.
- **remove(key)**: delete an element.

Additional operations include:

- **ascend()**: iterate over elements in ascending key order.
- **get(index)**: get element by rank.
- **remove(index)**: remove element by rank.

#### Complexity Summary:
| Operation       | Hash Table Worst Case | Balanced BST Worst Case | Balanced BST Expected |
|-----------------|----------------------|------------------------|----------------------|
| get, put, remove| O(n)                 | O(log n)               | O(log n)             |
| ascend          | O(D + n log n)       | O(log n)               | O(log n)             |
| get(index)      | O(D + n log n)       | O(log n)               | O(log n)             |
| remove(index)   | O(D + n log n)       | O(log n)               | O(log n)             |

`D` is the number of buckets in the hash table.


### 10. 🪓 Removing Elements from Binary Search Trees

Removing an element depends on the node’s degree (number of children):

- **Leaf node (degree 0)**: simply remove the node.
- **Degree 1 node**: replace the node with its single child.
- **Degree 2 node**: replace the node with either:
  - The largest key in its left subtree, or
  - The smallest key in its right subtree.

The replacement node will be a leaf or degree 1 node, making removal simpler.

The complexity of removal is proportional to the height of the tree, **O(height)**.


### 11. 🌲 Balanced Search Trees and Tree Height

Balanced trees maintain a height of **O(log n)** to ensure efficient operations.

Types of balanced trees:

- **Height Balanced**:  
  - AVL trees (Adelson-Velsky and Landis trees)
- **Weight Balanced**
- **Degree Balanced**:  
  - 2-3 trees  
  - 2-3-4 trees  
  - Red-black trees  
  - B-trees

Balanced trees allow insertions, deletions, and searches in logarithmic time, making them suitable for dynamic dictionaries.


### Summary

This lecture covered the theory and implementation of dictionaries and indexed search trees, focusing on:

- The structure and operations of dictionaries (static and dynamic).
- Hash tables and their limitations.
- Bin packing and the Best Fit heuristic using dynamic dictionaries.
- Indexed binary search trees for efficient rank-based operations.
- Construction of optimal binary search trees using dynamic programming.
- Complexity and performance comparisons of different data structures.
- Removal operations in BSTs and balanced tree types for maintaining efficiency.

Understanding these concepts is crucial for designing efficient data storage and retrieval systems, especially when dealing with large datasets requiring fast and flexible access patterns.