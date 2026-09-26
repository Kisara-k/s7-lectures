## 7. Fibonacci Heaps and Pairing Heaps

## Key Points

#### 1. 🔢 Fibonacci Heap Complexities  
- Insert: O(1) amortized  
- Remove Min (or Max): O(log n) amortized  
- Meld (Union): O(1) amortized  
- Decrease Key: O(1) amortized  
- Remove (arbitrary node): O(log n) amortized  

#### 2. 📊 Fibonacci Heap Use in Dijkstra’s Algorithm  
- Remove Min operation done O(n) times (n = number of vertices)  
- Decrease Key operation done O(e) times (e = number of edges)  
- Overall complexity with Fibonacci heap: O(n log n + e)  
- Using array: O(n²) overall complexity  
- Using binary min heap: O(n log n + e log n) overall complexity  

#### 3. 🌳 Fibonacci Heap Node Structure  
- Contains Degree, Child, Data  
- Left and Right Sibling pointers form a circular doubly linked list  
- Parent pointer to parent node  
- ChildCut boolean flag indicates if node lost a child since becoming a child of current parent  
- ChildCut is set to false by remove min operation  
- ChildCut undefined for root nodes  

#### 4. ✂️ Fibonacci Heap Remove and Decrease Key Operations  
- Remove(theNode): remove node from sibling list, add its children to root list, update parent pointers  
- DecreaseKey(theNode, amount): if new key < parent key and node is not root, cut subtree and add to root list  
- Cascading Cut: cuts nodes up the tree if ChildCut = true, stops at first node with ChildCut = false and sets it to true  

#### 5. 🔄 Cascading Cut Complexity  
- Actual complexity can be O(h) = O(n) in worst case  
- Amortized complexity remains efficient due to cascading cuts  

#### 6. ⚙️ Pairing Heap Complexities  
- Insert: O(log n) amortized (often close to O(1) in practice)  
- Remove Min (or Max): O(log n) amortized  
- Meld: O(log n) amortized  
- Decrease Key (or Increase Key): O(log n) amortized  

#### 7. 🌲 Pairing Heap Node Structure  
- Child pointer to first child  
- Left and Right Sibling pointers for doubly linked list (not circular)  
- Left pointer of first child points to parent  
- No Parent, Degree, or ChildCut fields  

#### 8. 🔧 Pairing Heap Meld Operation  
- Compare roots of two heaps  
- Smaller root becomes parent, other becomes leftmost child  
- Actual cost: O(1)  

#### 9. 🛠️ Pairing Heap Insert and Increase Key  
- Insert: create single-node heap and meld with existing heap, cost O(1)  
- IncreaseKey: detach node from sibling list and meld subtree back, cost O(1)  

#### 10. 🗑️ Pairing Heap Remove Max (or Min)  
- Remove root and meld all subtrees into one heap  
- Bad meld method (sequential meld) leads to O(n²) amortized cost  
- Good meld methods: Two-pass and Multipass schemes, both O(n) amortized  
- Two-pass scheme: meld pairs left to right, then meld resulting trees right to left  
- Multipass scheme: use FIFO queue to repeatedly meld pairs until one tree remains  

#### 11. ⚠️ Pairing Heap Worst-Case Structural Properties  
- Worst-case degree of root can be n - 1 (inserting decreasing keys)  
- Worst-case height can be n (inserting increasing keys)  

#### 12. 🧩 Removing Non-root Node in Pairing Heap  
- Remove node from sibling list  
- Meld children using two-pass or multipass scheme  
- Meld resulting tree with remaining heap  
- Actual cost: O(n) amortized



<br>

