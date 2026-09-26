## 4. Leftist Trees

## Questions

#### 1. Which of the following operations can be performed on a leftist tree with the same asymptotic complexity as on a binary heap?  
A) Insert a new element  
B) Remove the minimum (or maximum) element  
C) Initialize the tree from an unsorted array  
D) Search for an arbitrary element by value  

#### 2. In an extended binary tree, what is the relationship between the number of external nodes and internal nodes?  
A) Number of external nodes is equal to the number of internal nodes  
B) Number of external nodes is one more than the number of internal nodes  
C) Number of external nodes is twice the number of internal nodes  
D) Number of external nodes is less than the number of internal nodes  

#### 3. For a node $x$ in an extended binary tree, the function $s(x)$ is defined as:  
A) The length of the longest path from $x$ to an external node in its subtree  
B) The length of the shortest path from $x$ to an external node in its subtree  
C) The number of internal nodes in the subtree rooted at $x$  
D) The height of the subtree rooted at $x$  

#### 4. Which of the following statements about the $s()$ function are true?  
A) If $x$ is an external node, then $s(x) = 0$  
B) For an internal node $x$, $s(x) = \max(s(\text{leftChild}(x)), s(\text{rightChild}(x))) + 1$  
C) For an internal node $x$, $s(x) = \min(s(\text{leftChild}(x)), s(\text{rightChild}(x))) + 1$  
D) $s(x)$ measures the number of external nodes in the subtree rooted at $x$  

#### 5. A binary tree is a height-biased leftist tree if and only if:  
A) For every internal node $x$, $s(\text{leftChild}(x)) \leq s(\text{rightChild}(x))$  
B) For every internal node $x$, $s(\text{leftChild}(x)) \geq s(\text{rightChild}(x))$  
C) The left subtree is always taller than the right subtree  
D) The rightmost path is the longest path from root to an external node  

#### 6. Which of the following properties hold for leftist trees?  
A) The rightmost path from the root to an external node is the shortest such path in the tree  
B) The length of the rightmost path is equal to $s(\text{root})$  
C) The number of internal nodes $n$ satisfies $n \leq 2^{s(\text{root})} - 1$  
D) The number of internal nodes $n$ satisfies $n \geq 2^{s(\text{root})} - 1$  

#### 7. What is the asymptotic upper bound on the length of the rightmost path in a leftist tree with $n$ internal nodes?  
A) $O(n)$  
B) $O(\log n)$  
C) $O(\sqrt{n})$  
D) $O(1)$  

#### 8. When melding two min leftist trees, which of the following steps are performed?  
A) Traverse only the leftmost paths of both trees  
B) Meld the right subtree of the tree with the smaller root with the other tree  
C) Swap left and right subtrees if $s(\text{left}) < s(\text{right})$ after melding  
D) Always attach the larger root tree as the right subtree  

#### 9. The initialization of a leftist tree from $n$ elements in $O(n)$ time involves:  
A) Creating $n$ single-node min leftist trees and inserting them one by one into a single tree  
B) Creating $n$ single-node min leftist trees and repeatedly melding pairs of trees from a FIFO queue until one remains  
C) Sorting the elements first and then building the leftist tree in a bottom-up manner  
D) Using a heapify-like process similar to binary heaps  

#### 10. In the arbitrary remove operation for a node $x$ that is not the root, which of the following is true?  
A) The subtree rooted at $x$ is simply deleted without further adjustments  
B) The left subtree $L$ of $x$ is made the right subtree of $x$'s parent $p$  
C) The $s()$ values and leftist property are adjusted on the path from $p$ to the root  
D) The right subtree $R$ of $x$ is melded with the modified subtree rooted at $p$



<br>

## Answers

#### 1. Which of the following operations can be performed on a leftist tree with the same asymptotic complexity as on a binary heap?  
A) ✓ Leftist trees support insert with the same asymptotic complexity as heaps.  
B) ✓ Remove min (or max) is supported with the same asymptotic complexity.  
C) ✓ Initialization can be done in $O(n)$ time, similar to heaps.  
D) ✗ Searching for an arbitrary element by value is not efficient in leftist trees or heaps.  

**Correct:** A, B, C


#### 2. In an extended binary tree, what is the relationship between the number of external nodes and internal nodes?  
A) ✗ They are not equal.  
B) ✓ The number of external nodes is exactly one more than the number of internal nodes.  
C) ✗ External nodes are not twice the internal nodes.  
D) ✗ External nodes are never fewer than internal nodes in an extended binary tree.  

**Correct:** B


#### 3. For a node $x$ in an extended binary tree, the function $s(x)$ is defined as:  
A) ✗ $s(x)$ is the shortest path length, not the longest.  
B) ✓ $s(x)$ is the length of the shortest path from $x$ to an external node in its subtree.  
C) ✗ $s(x)$ is not the count of internal nodes.  
D) ✗ $s(x)$ is not the height but the shortest path length to an external node.  

**Correct:** B


#### 4. Which of the following statements about the $s()$ function are true?  
A) ✓ For external nodes, $s(x) = 0$ by definition.  
B) ✗ $s(x)$ uses the minimum, not the maximum, of child $s()$ values.  
C) ✓ For internal nodes, $s(x) = \min(s(\text{leftChild}(x)), s(\text{rightChild}(x))) + 1$.  
D) ✗ $s(x)$ measures path length, not the number of external nodes.  

**Correct:** A, C


#### 5. A binary tree is a height-biased leftist tree if and only if:  
A) ✗ The inequality is reversed.  
B) ✓ For every internal node $x$, $s(\text{leftChild}(x)) \geq s(\text{rightChild}(x))$.  
C) ✗ The left subtree is not necessarily taller, only $s()$ values matter.  
D) ✗ The rightmost path is the shortest path, not the longest.  

**Correct:** B


#### 6. Which of the following properties hold for leftist trees?  
A) ✓ The rightmost path is the shortest root-to-external-node path.  
B) ✓ The length of the rightmost path equals $s(\text{root})$.  
C) ✗ The inequality is reversed; $n$ is at least $2^{s(\text{root})} - 1$, not at most.  
D) ✓ The number of internal nodes $n \geq 2^{s(\text{root})} - 1$.  

**Correct:** A, B, D


#### 7. What is the asymptotic upper bound on the length of the rightmost path in a leftist tree with $n$ internal nodes?  
A) ✗ Linear length is not guaranteed.  
B) ✓ The length is $O(\log n)$ due to the leftist property.  
C) ✗ No guarantee for square root bound.  
D) ✗ The path length grows with $n$, so not constant.  

**Correct:** B


#### 8. When melding two min leftist trees, which of the following steps are performed?  
A) ✗ The rightmost paths are traversed, not the leftmost.  
B) ✓ Meld the right subtree of the tree with the smaller root with the other tree.  
C) ✓ Swap left and right subtrees if $s(\text{left}) < s(\text{right})$ to maintain leftist property.  
D) ✗ The smaller root tree remains root; larger root tree is not always attached as right subtree.  

**Correct:** B, C


#### 9. The initialization of a leftist tree from $n$ elements in $O(n)$ time involves:  
A) ✗ Inserting one by one is $O(n \log n)$, not $O(n)$.  
B) ✓ Create $n$ single-node trees and repeatedly meld pairs from a FIFO queue until one remains.  
C) ✗ Sorting is not required for leftist tree initialization.  
D) ✗ Heapify-like bottom-up process is not used here; melding pairs is the method.  

**Correct:** B


#### 10. In the arbitrary remove operation for a node $x$ that is not the root, which of the following is true?  
A) ✗ The subtree is not simply deleted; adjustments are needed.  
B) ✓ The left subtree $L$ of $x$ is made the right subtree of $x$'s parent $p$.  
C) ✓ $s()$ values and leftist property are adjusted on the path from $p$ to the root.  
D) ✓ The right subtree $R$ of $x$ is melded with the modified subtree rooted at $p$.  

**Correct:** B, C, D