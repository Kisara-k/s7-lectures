## 13. Compressed and Multibit Tries

## Study Notes

### 1. 🌲 Compressed Binary Tries: Introduction and Structure

A **trie** is a tree-like data structure used to store keys, typically strings or sequences of bits, where each edge represents a character or bit. A **binary trie** specifically branches on bits (0 or 1). However, a common inefficiency in binary tries is the presence of many nodes with only one child, which wastes space and slows down operations.

#### What is a Compressed Binary Trie?

A **compressed binary trie** improves on the basic binary trie by eliminating all branch nodes that have exactly one child. Instead of branching on every single bit, it "compresses" chains of single-child nodes into a single node that skips over those bits. This reduces the height of the trie and the number of nodes, making operations faster and more memory-efficient.

#### Key Features:

- **No branch node with degree 1:** Every branch node has either zero or two children.
- **bit# field:** Each branch node stores a `bit#` field, which tells you which bit of the key to examine to decide whether to go left or right. This is crucial because, after compression, nodes no longer correspond to consecutive bits.
- The number of branch nodes in a compressed binary trie with `n` keys is exactly `n - 1`.

#### How Insertion and Deletion Work:

- When inserting a key, you follow the bits indicated by the `bit#` fields until you find the correct place to insert.
- Deletion involves removing the key and possibly compressing the trie again if nodes become single-child nodes.


### 2. 🔢 Higher Order Tries: Multiway Branching for Larger Alphabets

When keys are composed of digits or characters (not just bits), we can use **higher order tries** where each node branches on more than two possibilities.

#### Example: NID Number Trie

- Suppose keys are 9-digit decimal numbers (digits 0-9).
- A **10-way trie** branches on each digit (0 through 9).
- The height of this trie is at most 10 (one level per digit).
- Searching involves following up to 9 branches plus one final comparison.

#### Comparing Different Data Structures for NID Numbers:

| Data Structure      | Height (approx.) | Search Cost (comparisons)               |
|---------------------|------------------|---------------------------------------|
| 10-way trie         | ≤ 10             | ≤ 9 branches + 1 compare               |
| 100-way trie        | ≤ 6              | ≤ 5 branches + 1 compare                |
| Red-Black tree      | ~60              | ≤ 60 compares of 9-digit numbers       |
| AVL tree            | ~40              | ≤ 40 compares of 9-digit numbers       |
| Best binary tree    | ~30              | ≤ 30 compares of 9-digit numbers       |

This shows that tries can be more efficient than balanced binary trees for certain key types.

#### Compressed NID Trie

- Similar to compressed binary tries, but branching on characters/digits.
- Each node stores:
  - `char#`: the character/digit used for branching (like `bit#` in binary tries).
  - `#ptr`: the number of non-null pointers (children).
- Null pointers are often omitted for clarity.


### 3. 🔣 Handling Variable Length Keys in Tries

When keys have variable lengths, a problem arises if one key is a prefix of another. For example, if you insert "0123" and "012345", the trie might confuse the shorter key as a prefix of the longer one.

#### Solution: End-of-Key Character

- Add a special **end-of-key character** (often denoted `#`) to each key.
- This character marks the end of a key explicitly.
- It prevents ambiguity by distinguishing keys that are prefixes of others.
- The trie then treats the end-of-key character as just another character to branch on.


### 4. 🔗 Tries with Edge Information: Skipping Characters

To optimize tries further, especially when skipping over multiple characters or bits, we can add **edge information** to branch nodes.

#### What is Edge Information?

- Each branch node has an extra field pointing to an element (or key) in its subtree.
- This pointer helps recover the skipped characters when traversing the trie.
- It allows the trie to skip over multiple bits or characters at once, reducing height and speeding up searches.

#### Expected Height

- For an order `m` trie (branching factor `m`), the expected height is approximately `log_m n`, where `n` is the number of keys.


### 5. 🧩 Multibit Tries: Branching on Multiple Bits at Once

A **multibit trie** is a variant of the binary trie where each node branches on multiple bits simultaneously, rather than just one bit.

#### Why Use Multibit Tries?

- They reduce the height of the trie by increasing the branching factor at each node.
- Useful in applications like Internet routing, where keys are IP addresses with variable-length prefixes.
- Support **longest prefix matching**, which is essential for routing decisions.

#### How Multibit Tries Work:

- Each node has a **stride** `s`, meaning it uses `s` bits of the key to decide which child to follow.
- The node has `2^s` children and `2^s` element/prefix fields.
- Prefixes shorter than the stride are expanded to the stride length by adding wildcards.
- For example, if the root stride is 3, prefixes shorter than 3 bits are expanded to length 3.

#### Example:

- Root stride = 32 bits → height = 1 (all bits checked at once).
- Strides of 16, 8, and 8 bits at levels 1, 2, and 3 → height = 3.


### 6. 🌍 Applications of Tries and Multibit Tries

#### Prefix Search

- Tries are ideal for prefix searches, where you want to find all keys starting with a certain prefix.
- Used in autocomplete systems (commands, phone numbers, URLs).

#### LZW Compression

- Tries help in dictionary-based compression algorithms like LZW by efficiently storing and searching prefixes.

#### Internet Routers and Longest Prefix Matching

- Routers use tries to decide where to forward packets based on destination IP addresses.
- Routing tables can have millions of rules.
- Rules are often specified as prefixes (e.g., IP address/mask pairs).
- The router must find the **longest matching prefix** for a given destination address.


### 7. 📡 Router Rule Tables and Longest Prefix Matching

#### Router Rule Table

- Contains rules mapping destination prefixes to output ports.
- Example: USA → Port 1, Sri Lanka → Port 2, etc.
- Rules can be ranges or prefix filters (mask with 1s on the left, 0s on the right).

#### Tie Breakers in Routing

- When multiple rules match, routers use tie breakers:
  - First matching rule.
  - Highest priority rule.
  - Most specific rule (narrowest range).
  - Longest prefix rule (longest matching prefix).

#### Challenges

- Large tables (1 million+ rules).
- IPv4 addresses are 32 bits; IPv6 addresses are 128 bits.
- High-speed routers (e.g., 10 Gbps) require very fast lookups.
- Logarithmic search schemes may cause too many memory accesses.


### 8. ⚙️ Hardware and Software Solutions for Routing

#### Hardware Solutions

- **TCAM (Ternary Content Addressable Memory):**
  - Can match bits with 0, 1, or "don't care" (wildcard).
  - Supports longest prefix matching efficiently.
  - Limitations: expensive, power-hungry, limited capacity, scalability issues for IPv6.

#### Software Solutions

- Use tries (1-bit or multibit).
- Compact representations of tries to save memory.
- Two-dimensional tries for filtering on source-destination pairs.


### 9. 🧮 Complexity and Optimization of Tries

#### 1-Bit Trie Complexity

- Each operation (search, insert, delete) takes O(W), where W is the key length in bits.

#### Fixed-Stride Tries

- All nodes at the same level use the same stride (number of bits).
- Number of levels equals the number of distinct prefix lengths.
- Use **prefix expansion** to reduce the number of distinct prefix lengths, which reduces trie height.

#### Variable-Stride Tries

- Nodes can have different strides at different levels.
- Allows more flexible and memory-efficient tries.
- Optimization problem: find the least memory fixed-stride trie with height ≤ k.


### 10. 🔄 Two-Dimensional Filters and Multibit Tries

- Some applications require filtering on pairs of keys, e.g., source and destination addresses.
- Two-dimensional tries branch on both keys simultaneously.
- Tie breakers and least-cost rules are used to decide which rule applies when multiple match.
- Variants include 2D 1-bit tries and 2D multibit tries.


### Summary

This lecture covered advanced trie data structures designed to improve efficiency in storing and searching keys, especially in applications like routing and prefix matching. Starting from compressed binary tries that reduce unnecessary nodes, to multibit tries that branch on multiple bits at once, these structures balance memory use and speed. Handling variable-length keys and adding edge information further optimize tries. In networking, tries support fast longest prefix matching, crucial for routing decisions. Both hardware (TCAM) and software (multibit tries) solutions exist, each with trade-offs. Finally, optimization problems and multidimensional tries extend these ideas to complex filtering scenarios.