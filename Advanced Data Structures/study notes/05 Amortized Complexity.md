## 5. Amortized Complexity

## Study Notes

### 1. 📊 Understanding Different Types of Complexity

When analyzing algorithms, we often want to understand how long they take to run or how much resource they consume. There are several ways to measure this:

- **Worst-case complexity:** This tells us the maximum time or cost an algorithm will take for any input of size *n*. It guarantees an upper bound, so the algorithm will never be slower than this.

- **Average complexity:** This measures the expected time or cost over all possible inputs of size *n*, assuming some distribution (often uniform). It gives a sense of typical performance.

- **Amortized complexity:** This is a more nuanced measure. It looks at the average cost per operation over a sequence of operations, even if some individual operations are expensive. It helps us understand the overall efficiency when tasks vary in cost.

#### Example: Quick Sort

- **Worst-case time:** Suppose sorting *n* distinct numbers takes at most $10n^2$ microseconds. This means there exists some input sequence of size *n* that causes Quick Sort to take exactly $10n^2$ microseconds, and no input will take longer.

- **Average time:** On average, Quick Sort takes about $5n \log_2 n$ microseconds. This is calculated by summing the time taken over all $n!$ permutations of the input and dividing by $n!$.

- **Important note:** If you only test a subset of inputs (e.g., 500 out of $1000!$ sequences), you cannot conclude the average time for those inputs; you can only say the total time is less than or equal to 500 times the worst-case time.


### 2. 🛠️ Task Sequences and Cost Bounds

Imagine performing a sequence of *n* tasks, each with some cost:

- Let the **worst-case cost** of any single task be $c_{wc}$.
- Let the **actual cost** of the $i^{th}$ task be $c_i$, where $c_i \leq c_{wc}$.

#### Upper Bounds on Costs

- The total cost for all *n* tasks is at most $n \times c_{wc}$.
- The cost for the first *j* tasks is at most $j \times c_{wc}$.

#### Average Cost

- The average cost per task in the sequence is $c_{avg} = \frac{\sum_{i=1}^n c_i}{n}$.
- The total cost is $n \times c_{avg}$.
- However, $j \times c_{avg}$ is **not** an upper bound on the cost of the first *j* tasks because the actual costs can vary widely.

#### Why Amortized Complexity?

Sometimes, the worst-case bounds are too pessimistic. Amortized complexity provides a better upper bound on the total cost of a sequence of tasks by averaging out expensive operations over many cheap ones.


### 3. 💡 What is Amortized Complexity?

Amortized complexity is a way to assign a "charge" or cost to each task in a sequence such that:

- The **sum of amortized costs** over all tasks is an upper bound on the **sum of actual costs**.
- Some tasks may be charged more than their actual cost, while others may be charged less.
- This approach smooths out the cost spikes of expensive operations by spreading their cost over multiple cheaper operations.

#### Formal Definition

For a sequence of tasks:


$$
\sum_{i=1}^n \text{actualCost}(i) \leq \sum_{i=1}^n \text{amortizedCost}(i)
$$


This means the total amortized cost is a valid upper bound on the total actual cost.

#### Key Differences from Worst-Case Analysis

- Worst-case analysis charges each task at least its actual cost.
- Amortized analysis allows some tasks to be charged less than their actual cost, as long as the total amortized cost covers the total actual cost.


### 4. ⚖️ Potential Function: A Tool for Amortized Analysis

The **potential function** is a mathematical tool used to analyze amortized complexity. It helps track how much "credit" or "debt" has been accumulated over a sequence of operations.

#### Definition

Let $P(i)$ be the potential after the $i^{th}$ task, defined as:


$$
P(i) = \text{amortizedCost}(i) - \text{actualCost}(i) + P(i-1)
$$


- $P(0)$ is usually set to 0.
- $P(i)$ represents the amount by which the first $i$ tasks have been overcharged (if positive) or undercharged (if negative).

#### Important Property


$$
P(n) - P(0) = \sum_{i=1}^n (\text{amortizedCost}(i) - \text{actualCost}(i))
$$


If $P(n) \geq 0$, it means the total amortized cost is at least the total actual cost.


### 5. 🔄 Example: Arithmetic Statement Parsing and Amortized Complexity

Consider rewriting an arithmetic statement without parentheses using a stack and a method called `processNextSymbol()`.

#### How `processNextSymbol()` Works

- For each symbol in the statement:
  - If the symbol is not `)` or `;`, push it onto the stack.
  - If the symbol is `)`, pop symbols until the matching `(` is found, generate an assignment statement, and push the left-hand symbol back.
  - If the symbol is `;`, pop all remaining symbols and generate the final assignment.

#### Complexity Analysis

- Each call to `processNextSymbol()` can pop multiple symbols.
- Naively, the worst-case complexity is $O(n^2)$ because each symbol might cause many pops.
- However, using amortized analysis, we find the total number of push and pop operations is at most $2n$.
- Therefore, the amortized cost per call is constant, and the total complexity is $O(n)$.


### 6. 🧮 Methods to Determine Amortized Complexity

There are three main methods to analyze amortized complexity:

#### 1. Aggregate Method

- Calculate the total cost of *n* operations.
- Divide by *n* to get the amortized cost per operation.
- Example: For `processNextSymbol()`, total stack operations are at most $2n$, so amortized cost is 2.

#### 2. Accounting Method

- Assign an amortized cost to each operation (guess).
- Show that the total amortized cost covers the actual cost.
- Use a "credit" system where some operations pay extra to cover future expensive operations.

#### 3. Potential Function Method

- Define a potential function $P(i)$ that measures stored "energy" or "credit".
- Show that the potential never goes negative.
- Calculate amortized cost as actual cost plus change in potential.


### 7. 🔢 Example: Binary Counter Increment

Consider an *n*-bit binary counter starting at 0. Incrementing the counter flips some bits:

- The cost of incrementing is the number of bits that change.
- Worst-case cost of one increment is $n$ (all bits flip).
- What about *m* increments?

#### Worst-Case Analysis

- Each increment can cost up to $n$.
- So, total cost for *m* increments is at most $m \times n$.

#### Aggregate Method

- Bit 0 flips every increment → flips *m* times.
- Bit 1 flips every 2 increments → flips $\lfloor m/2 \rfloor$ times.
- Bit 2 flips every 4 increments → flips $\lfloor m/4 \rfloor$ times.
- Summing all flips:


$$
m + \lfloor m/2 \rfloor + \lfloor m/4 \rfloor + \cdots < 2m
$$


- So total cost is less than $2m$.
- Amortized cost per increment is less than 2.

#### Accounting Method

- Guess amortized cost per increment is 2.
- Each increment pays 1 unit for the bit flip from 0 to 1.
- The other unit is stored as credit on that bit to pay for the flip from 1 to 0 later.
- Credits ensure no operation is undercharged.
- Potential $P(m)$ equals the number of 1s in the counter, always non-negative.

#### Potential Function Method

- Define potential $P(i)$ as the number of 1s in the counter after the $i^{th}$ increment.
- Actual cost of increment $i$ is $1 + q$, where $q$ is the number of trailing 1s before increment.
- Amortized cost = actual cost + change in potential.
- This confirms amortized cost per increment is constant.


### Summary

- **Amortized complexity** provides a way to analyze sequences of operations where some are expensive but rare.
- It ensures the average cost per operation over the sequence is low, even if individual operations vary.
- Tools like the **aggregate method**, **accounting method**, and **potential function method** help us rigorously prove amortized bounds.
- Examples like **stack operations in parsing** and **binary counter increments** illustrate how amortized analysis gives tighter, more realistic complexity bounds than worst-case analysis alone.