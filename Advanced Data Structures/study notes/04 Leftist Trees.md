## 4. Leftist Trees

## Study Notes

### 1. 🌳 Introduction to Leftist Trees

Leftist trees are a special kind of binary tree designed to efficiently implement priority queues, similar to heaps. They support all the basic heap operations such as inserting elements, removing the minimum (or maximum), and initializing the structure, all while maintaining the same asymptotic time complexity as heaps. What makes leftist trees particularly interesting is their ability to **meld** (or merge) two priority queues efficiently in **O(log n)** time, which is not as straightforward in standard binary heaps.

In essence, leftist trees are **linked binary trees** with a special structure that biases the tree to keep the rightmost path short. This bias helps keep operations efficient, especially melding, which is a key advantage over other heap implementations.


### 2. 🌲 Extended Binary Trees and the s() Function

Before diving into leftist trees, we need to understand the concept of **extended binary trees** and the function **s()**, which are foundational to leftist trees.

#### Extended Binary Trees

An extended binary tree is created by starting with any binary tree and then adding **external nodes** (also called null or leaf nodes) wherever there is an empty subtree. This means every internal node has exactly two children, which may be internal nodes or external nodes.

- If the original tree has **n** internal nodes, the extended binary tree will have **n + 1** external nodes.
- External nodes represent the "end" of a path in the tree.

#### The s() Function

For any node **x** in an extended binary tree, **s(x)** is defined as the length of the shortest path from **x** down to an external node in the subtree rooted at **x**.

- If **x** is an external node, then **s(x) = 0** because the shortest path to an external node from itself is zero.
- If **x** is an internal node, then:


$$
  s(x) = \min(s(\text{leftChild}(x)), s(\text{rightChild}(x))) + 1
$$


This means **s(x)** measures how "close" the nearest external node is from **x**.


### 3. 🌿 Height-Biased Leftist Trees: Definition and Properties

#### What is a Height-Biased Leftist Tree?

A **height-biased leftist tree** is a binary tree where, for every internal node **x**, the **s()** value of the left child is always **greater than or equal to** the **s()** value of the right child:


$$
s(\text{leftChild}(x)) \geq s(\text{rightChild}(x))
$$


This condition biases the tree to be "heavier" on the left side, meaning the right subtree is always the shortest path to an external node.

#### Key Properties of Leftist Trees

1. **Rightmost Path is the Shortest Path**

   In a leftist tree, the rightmost path from the root to an external node is the shortest such path in the tree. The length of this path is exactly **s(root)**.

2. **Number of Internal Nodes is at Least $2^{s(root)} - 1$**

   Because the shortest path to an external node is on the rightmost path, the levels from 1 to $s(root)$ contain no external nodes. This implies the tree has a minimum number of internal nodes, which grows exponentially with $s(root)$.

3. **Length of the Rightmost Path is $O(\log n)$**

   Since the number of internal nodes $n$ is at least $2^{s(root)} - 1$, it follows that:


$$
   s(root) \leq \log_2(n + 1)
$$


   Therefore, the rightmost path length is logarithmic in the number of nodes, which is crucial for efficient operations.


### 4. 🎯 Leftist Trees as Priority Queues

Leftist trees can be used as **priority queues**, supporting both **min** and **max** variants:

- **Min Leftist Tree:** The root always contains the minimum element.
- **Max Leftist Tree:** The root always contains the maximum element.

This lecture focuses mainly on **min leftist trees**, but the concepts apply symmetrically to max leftist trees.

#### Basic Operations

- **put(x):** Insert a new element $x$ into the priority queue.
- **removeMin():** Remove the minimum element (the root).
- **meld(T1, T2):** Merge two leftist trees $T1$ and $T2$ into one.
- **initialize():** Build a leftist tree from a collection of elements efficiently.


### 5. 🔄 The Meld Operation: Core of Leftist Trees

The **meld** operation is the heart of leftist trees and allows two priority queues to be merged efficiently.

#### How Meld Works

- Compare the roots of the two trees.
- The tree with the smaller root becomes the new root.
- Recursively meld the **right subtree** of this smaller-root tree with the other tree.
- After melding, check the **s()** values of the left and right children.
- If $s(\text{leftChild}) < s(\text{rightChild})$, swap the left and right children to maintain the leftist property.
- Update the $s()$ value of the root.

#### Why Meld Only on Right Paths?

Because the rightmost path is the shortest path to an external node and is guaranteed to be $O(\log n)$ in length, melding only involves traversing and modifying nodes along this path, ensuring logarithmic time complexity.


### 6. ➕ Insertion and Removal Using Meld

#### Insertion (put)

To insert a new element $x$:

- Create a new single-node leftist tree containing $x$.
- Meld this new tree with the existing leftist tree.
- This operation takes $O(\log n)$ time due to the meld.

#### Removal of Minimum (removeMin)

To remove the minimum element (the root):

- Remove the root node.
- Meld the left and right subtrees of the root.
- The result is the new leftist tree.
- This also takes $O(\log n)$ time.


### 7. ⚙️ Initializing a Leftist Tree in O(n) Time

To build a leftist tree from $n$ elements efficiently:

- Create $n$ single-node leftist trees, each containing one element.
- Place all these trees into a FIFO queue.
- Repeatedly remove two trees from the queue, meld them, and put the resulting tree back into the queue.
- Continue until only one tree remains in the queue.
- This process is similar to heap initialization and runs in $O(n)$ time.


### 8. ❌ Arbitrary Removal of Elements

Leftist trees also support removing an arbitrary element pointed to by a node $x$:

- If $x$ is the root, this is just a removeMin operation.
- If $x$ is not the root:
  - Let $L$ be the left subtree of $x$.
  - Let $R$ be the right subtree of $x$.
  - Replace $x$ with $L$ in its parent $p$.
  - Adjust the $s()$ values and restore the leftist property on the path from $p$ to the root.
  - Meld the subtree rooted at $R$ with the updated tree.
  
This operation is more complex but still efficient due to the logarithmic height of the tree.


### Summary

Leftist trees are a powerful data structure for priority queues, especially when efficient merging of two queues is required. They maintain a special leftist property based on the shortest path to external nodes, which keeps the rightmost path short and operations efficient. The meld operation is the key to their efficiency, enabling insertion, removal, and merging in logarithmic time. Initialization can be done in linear time, and even arbitrary removal of elements is supported with careful adjustments.

This combination of properties makes leftist trees a versatile and efficient choice for priority queue implementations where merging is a frequent operation.