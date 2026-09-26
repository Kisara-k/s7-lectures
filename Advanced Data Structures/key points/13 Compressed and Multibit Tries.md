## 13. Compressed and Multibit Tries

## Key Points

#### 1. 🌲 Compressed Binary Tries  
- No branch node has exactly one child (degree 1).  
- Each branch node stores a `bit#` field indicating which bit of the key to branch on.  
- Number of branch nodes in a compressed binary trie with `n` keys is `n - 1`.  

#### 2. 🔢 Higher Order Tries  
- A 10-way trie for 9-digit decimal keys has height ≤ 10.  
- A 100-way trie for the same keys has height ≤ 6.  
- Red-black tree height for 9-digit keys is approximately 60.  
- AVL tree height for 9-digit keys is approximately 40.  
- Best binary tree height for 9-digit keys is approximately 30.  

#### 3. 🔣 Variable Length Keys in Tries  
- Problem occurs when one key is a proper prefix of another.  
- Adding a special end-of-key character (`#`) to each key eliminates prefix ambiguity.  

#### 4. 🔗 Tries with Edge Information  
- Each branch node has an extra field pointing to an element node in its subtree.  
- This pointer helps recover skipped characters during traversal.  
- Expected height of an order `m` trie is approximately `log_m n`.  

#### 5. 🧩 Multibit Tries  
- Nodes branch on `s` bits at once (stride = `s`), not just one bit.  
- A node with stride `s` has `2^s` children and `2^s` element/prefix fields.  
- Prefixes shorter than stride length are expanded to the stride length.  
- Multibit tries reduce trie height by increasing branching factor per node.  
- Example: root stride 32 bits → height = 1; strides 16, 8, 8 → height = 3.  

#### 6. 🌍 Applications of Tries  
- Used for prefix search, autocomplete, and LZW compression.  
- Critical for Internet routers performing longest prefix matching on IP addresses.  

#### 7. 📡 Router Rule Tables and Longest Prefix Matching  
- Router rules often specified as prefix filters (address/mask pairs).  
- Tie breakers include first matching rule, highest priority, most specific, and longest prefix.  
- Routing tables can have over 1 million rules with prefixes up to 32 bits (IPv4) or 128 bits (IPv6).  
- Logarithmic search schemes may cause too many memory accesses for high-speed routing.  

#### 8. ⚙️ Hardware and Software Solutions for Routing  
- TCAM supports ternary matching (0,1, don't care) for longest prefix matching.  
- TCAM limitations: capacity, cost, power, board space, IPv6 scalability, and multidimensional filters.  
- Software solutions include 1-bit tries, multibit tries, compact tries, and 2D tries.  

#### 9. 🧮 Trie Complexity and Optimization  
- 1-bit trie operations take O(W) time, where W is key length in bits.  
- Fixed-stride tries use the same stride at each level; number of levels equals number of distinct prefix lengths.  
- Prefix expansion reduces the number of distinct prefix lengths in fixed-stride tries.  
- Variable-stride tries allow different strides at different levels for memory optimization.  

#### 10. 🔄 Two-Dimensional Filters and Multibit Tries  
- Two-dimensional tries filter on pairs of keys (e.g., source and destination addresses).  
- Tie breakers select the least-cost matching rule when multiple rules apply.  
- Variants include 2D 1-bit tries and 2D multibit tries.



<br>

