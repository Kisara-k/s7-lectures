## 6. Binomial Heaps

## Study Notes

### 1. 📚 Introduction to Binomial Heaps

Binomial heaps are a type of advanced data structure used to efficiently implement priority queues. They are particularly useful when you need to perform operations like inserting elements, finding the minimum element, removing the minimum element, and merging two heaps (meld) efficiently.

A binomial heap is essentially a **collection of binomial trees** that are linked together in a specific way. Each binomial tree in the heap follows a min-heap property, meaning the root of each tree is the smallest element in that tree. The heap itself maintains a pointer to the minimum element among all the trees.

The key advantage of binomial heaps is that they allow efficient merging of two heaps, which is not as straightforward in simpler heap structures like binary heaps.


### 2. 🌳 Structure of Binomial Heaps and Nodes

#### What is a Binomial Heap?

A binomial heap is made up of several **binomial trees**, each of which has a specific structure and degree. These trees are linked together in a **circular linked list** at the top level, where each node contains pointers to its children and siblings.

#### Node Structure

Each node in a binomial heap contains the following fields:

- **Degree**: This is the number of children the node has. It helps identify the size and structure of the binomial tree rooted at this node.
- **Child**: A pointer to one of the node’s children. If the node has no children, this pointer is null.
- **Sibling**: A pointer used to link nodes that are siblings in a circular linked list. This allows traversal of all children of a node or all trees in the heap.
- **Data**: The actual value stored in the node.

#### Representation of the Heap

The binomial heap itself is represented as a **circular linked list of binomial trees**, each with a different degree. The degrees of these trees are unique within the heap, which helps maintain the heap’s structure and efficiency.


### 3. ➕ Insertion in Binomial Heaps

Inserting a new element into a binomial heap is straightforward:

- Create a new binomial heap consisting of a single node (a binomial tree of degree 0).
- Meld (merge) this new single-node heap with the existing binomial heap.
- Update the pointer to the minimum element if the new node’s value is smaller.

This operation is efficient because it involves merging two heaps, which can be done in logarithmic time relative to the number of elements.


### 4. 🔗 Meld Operation (Merging Two Binomial Heaps)

Melding is the process of combining two binomial heaps into one. This is done by:

- Combining the two top-level circular linked lists of binomial trees from both heaps.
- Sorting or merging these trees by their degree, ensuring that there is at most one binomial tree of any degree.
- Updating the pointer to the minimum element in the new combined heap.

Melding is a key operation that makes binomial heaps powerful, especially when you need to merge priority queues efficiently.


### 5. 🗑️ Removing the Minimum Element (Remove Min)

Removing the minimum element from a binomial heap is more complex than insertion or melding. The process involves several steps:

#### Step 1: Identify and Remove the Minimum Tree

- Find the binomial tree whose root contains the minimum element.
- Remove this tree from the top-level circular linked list.

#### Step 2: Reinsert Subtrees of the Removed Tree

- The removed tree’s children form a set of smaller binomial trees.
- These children are reinserted into the heap by melding their circular linked list with the remaining trees in the heap.

#### Step 3: Update the Minimum Pointer

- After reinserting the subtrees, the heap’s minimum pointer must be updated by examining the roots of all the binomial trees in the heap.

#### Complexity of Remove Min

- The naive approach to remove min involves scanning all trees and reinserting subtrees, which can take **O(n)** time in the worst case, where n is the number of elements.


### 6. ⚙️ Enhanced Remove Min with Pairwise Combining

To improve the efficiency of the remove min operation, binomial heaps use a technique called **pairwise combining**:

- During reinsertion of the subtrees, binomial trees with the same degree are combined pairwise.
- Combining two binomial trees of the same degree involves making the tree with the larger root a child of the other, increasing the degree of the resulting tree by one.
- This process continues until no two trees of the same degree remain.

#### How Pairwise Combining Works

- Use a table (or array) indexed by degree to keep track of trees.
- Iterate over the trees, and for each tree:
  - If the table entry for its degree is empty, store the tree there.
  - If not empty, combine the two trees and repeat the process with the new tree.
- After processing all trees, the table contains at most one tree per degree.
- These trees are then linked together to form the new top-level circular list.

#### Complexity of Enhanced Remove Min

- Initializing the table takes **O(MaxDegree)** time.
- Combining trees and rebuilding the heap also takes **O(MaxDegree + s)**, where s is the number of trees before combining.
- Since the maximum degree is logarithmic in the number of elements (MaxDegree = O(log n)), the overall complexity of remove min becomes **O(log n)**.


### 7. 🌲 Binomial Trees: The Building Blocks

#### What is a Binomial Tree?

A binomial tree $B_k$ of degree $k$ is defined recursively:

- $B_0$ is a single node.
- For $k > 0$, $B_k$ is formed by linking two $B_{k-1}$ trees, making one the child of the other.

#### Properties of Binomial Trees

- The number of nodes in $B_k$ is $2^k$.
- The degree of the root is $k$.
- The height of $B_k$ is $k$.
- The children of the root are roots of binomial trees $B_{k-1}, B_{k-2}, \ldots, B_0$.

#### Why Binomial Trees?

Because binomial heaps are collections of binomial trees with unique degrees, the heap can represent any number of elements efficiently. The unique degree property ensures that the number of trees in the heap is at most $O(\log n)$, where $n$ is the number of elements.


### 8. 📈 Summary of Complexity and Efficiency

| Operation       | Time Complexity       |
|-----------------|-----------------------|
| Insert          | $O(\log n)$       |
| Remove Min      | $O(\log n)$ (enhanced) |
| Meld (Merge)    | $O(\log n)$       |
| Find Min        | $O(1)$ (with pointer) |

- The **insert** operation is efficient because it involves melding a single-node tree.
- The **remove min** operation is optimized by pairwise combining trees to maintain the heap structure.
- The **meld** operation is efficient due to the unique degree property and the circular linked list representation.
- The **find min** operation is constant time because the heap maintains a pointer to the minimum element.


### Final Notes

Binomial heaps are a powerful data structure for priority queues, especially when you need to merge heaps frequently. Their structure based on binomial trees and the clever use of pairwise combining during remove min operations allow them to maintain good performance guarantees.

Understanding binomial heaps requires grasping the recursive nature of binomial trees, the circular linked list representation, and the merging strategies that keep the heap balanced and efficient.