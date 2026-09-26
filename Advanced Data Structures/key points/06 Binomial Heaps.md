## 6. Binomial Heaps

## Key Points

#### 1. 🌳 Binomial Heap Structure  
- A binomial heap is a collection of binomial trees linked in a circular linked list.  
- Each node contains degree (number of children), child pointer, sibling pointer, and data.  
- The heap maintains a pointer to the minimum element among all trees.

#### 2. ➕ Insertion  
- Insertion adds a new single-node binomial tree (degree 0) to the heap.  
- The min-element pointer is updated if the new node is smaller.  
- Insert operation runs in $O(\log n)$ time.

#### 3. 🔗 Meld (Merge)  
- Meld combines the two top-level circular linked lists of binomial trees.  
- After melding, the min-element pointer is updated.  
- Meld operation runs in $O(\log n)$ time.

#### 4. 🗑️ Remove Min (Basic)  
- Remove min removes the binomial tree with the minimum root.  
- The removed tree’s children are reinserted by melding their circular list with the remaining heap.  
- The min pointer is updated by scanning all root nodes.  
- Basic remove min has $O(n)$ complexity due to scanning all trees.

#### 5. ⚙️ Enhanced Remove Min with Pairwise Combining  
- During reinsertion, trees with the same degree are combined pairwise.  
- Combining two trees of degree $k$ creates a tree of degree $k+1$ by making the larger root a child of the smaller root.  
- A table indexed by degree is used to track and combine trees efficiently.  
- Enhanced remove min runs in $O(\log n)$ time, where $\log n$ is the maximum degree.

#### 6. 🌲 Binomial Trees  
- A binomial tree $B_k$ has $2^k$ nodes and degree $k$.  
- $B_k$ is formed by linking two $B_{k-1}$ trees, making one the child of the other.  
- The maximum degree of any tree in a binomial heap with $n$ elements is $O(\log n)$.

#### 7. 📈 Complexity Summary  
- Insert: $O(\log n)$  
- Remove Min (enhanced): $O(\log n)$  
- Meld: $O(\log n)$  
- Find Min: $O(1)$ (due to min pointer)



<br>

