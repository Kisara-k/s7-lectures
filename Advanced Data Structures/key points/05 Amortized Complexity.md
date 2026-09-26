## 5. Amortized Complexity

## Key Points

#### 1. 📊 Types of Complexity  
- Worst-case complexity gives an upper bound on the time/cost for any input of size *n*.  
- Average complexity is the expected time/cost over all inputs of size *n*.  
- Amortized complexity averages the cost of operations over a sequence, smoothing expensive spikes.

#### 2. 🛠️ Task Sequence Cost Bounds  
- Worst-case cost per task is $c_{wc}$, so total cost ≤ $n \times c_{wc}$.  
- Average cost per task is $c_{avg} = \frac{\sum c_i}{n}$, but $j \times c_{avg}$ is not an upper bound for first *j* tasks.  
- Amortized complexity can provide a better upper bound than worst-case bounds for sequences.

#### 3. 💡 Amortized Complexity Definition  
- Amortized cost per task is a charged amount such that $\sum \text{actualCost}(i) \leq \sum \text{amortizedCost}(i)$.  
- Some tasks may be charged less than their actual cost, balanced by others charged more.  
- Amortized cost may not directly correspond to actual cost of individual tasks.

#### 4. ⚖️ Potential Function  
- Defined as $P(i) = \text{amortizedCost}(i) - \text{actualCost}(i) + P(i-1)$ with $P(0) = 0$.  
- $P(i)$ measures overcharge (credit) after $i$ tasks.  
- If $P(n) \geq 0$, total amortized cost bounds total actual cost.

#### 5. 🔄 Arithmetic Statement Parsing Complexity  
- Naive worst-case complexity of `processNextSymbol()` is $O(n^2)$.  
- Total stack operations (push/pop) over *n* calls is at most $2n$.  
- Amortized cost per call is constant, so total complexity is $O(n)$.

#### 6. 🧮 Methods to Determine Amortized Complexity  
- Aggregate method: total cost of *n* operations divided by *n*.  
- Accounting method: assign amortized costs and maintain non-negative credit (potential).  
- Potential function method: define potential function to relate amortized and actual costs.

#### 7. 🔢 Binary Counter Increment Costs  
- Worst-case cost per increment is $n$ (all bits flip).  
- Aggregate cost for *m* increments is less than $2m$.  
- Amortized cost per increment is less than 2.  
- Accounting method uses credits stored on bits to pay for flips from 1 to 0.  
- Potential function defined as number of 1s in counter after increment; amortized cost = actual cost + change in potential.



<br>

