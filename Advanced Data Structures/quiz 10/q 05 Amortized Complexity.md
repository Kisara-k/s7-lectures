## 5. Amortized Complexity

## Questions

#### 1. Which of the following statements correctly describe the difference between worst-case complexity and amortized complexity?  
A) Amortized complexity always provides a tighter upper bound than worst-case complexity.  
B) Amortized complexity requires the sum of amortized costs to be at least the sum of actual costs over all tasks.  
C) Worst-case complexity bounds the cost of every single task, whereas amortized complexity bounds the average cost over a sequence of tasks.  
D) Worst-case complexity charges each task at least its actual cost, while amortized complexity may charge some tasks less than their actual cost.  

#### 2. Consider a sequence of n tasks with worst-case cost c_wc per task and actual costs c_i. Which of the following are true?  
A) The total cost of the sequence is always less than or equal to n * c_wc.  
B) The sum of actual costs Σ c_i is always less than or equal to n * c_wc.  
C) The cost of the first j tasks can be bounded by j * c_avg.  
D) The average cost per task c_avg = (Σ c_i) / n is always an upper bound on the cost of the first j tasks for any j ≤ n.  

#### 3. In the aggregate method of amortized analysis, which of the following are correct?  
A) It can be used without knowing the total cost of the sequence.  
B) It always gives a tighter bound than the accounting method.  
C) It requires first finding a good upper bound on the total cost of n operations.  
D) The amortized cost per operation is obtained by dividing the total cost of n operations by n.  

#### 4. Regarding the potential function method, which statements are true?  
A) The initial potential P(0) can be any positive number.  
B) The amortized cost of the ith operation equals the actual cost plus the change in potential, i.e., amortized cost = actual cost + ΔP.  
C) The potential function must always be non-negative for all i.  
D) The potential function P(i) represents the amount by which the first i operations have been overcharged.  

#### 5. When analyzing the processNextSymbol() function for rewriting arithmetic statements, which of the following are correct?  
A) The number of push operations is always equal to the number of pop operations.  
B) The amortized cost per invocation of processNextSymbol() can be bounded by 2.  
C) The worst-case complexity is O(n²) because each iteration can pop up to i symbols from the stack.  
D) A more careful amortized analysis shows the overall complexity is O(n).  

#### 6. In the accounting method applied to the binary counter increment problem, which of the following are true?  
A) The total number of credits after m increments equals the number of 0 bits in the counter.  
B) Credits are stored on bits set to 1 to pay for future bit flips from 1 to 0.  
C) Each increment is charged an amortized cost of 2 units.  
D) The amortized cost per increment is less than the worst-case cost of n.  

#### 7. For the binary counter increment problem, which statements about the potential function P(i) = number of 1s in the counter after the ith increment are correct?  
A) The amortized cost of the ith increment equals the actual cost minus the change in potential.  
B) The potential function decreases by the number of bits flipped from 1 to 0 during the increment.  
C) P(i) is always non-negative and P(0) = 0.  
D) The actual cost of the ith increment is 1 plus the number of trailing 1s before the increment.  

#### 8. Which of the following are true about average complexity as discussed in the context of Quick Sort?  
A) The worst-case time provides an upper bound on the time for any input sequence.  
B) Sorting only a subset of sequences allows us to conclude the average time for that subset equals the average time over all sequences.  
C) The average time is computed by summing the time over all n! permutations and dividing by n!.  
D) The average time for sorting n distinct numbers is proportional to n log n.  

#### 9. Which of the following correctly describe the relationship between actual cost, amortized cost, and potential function in amortized analysis?  
A) The potential function must always increase or stay constant.  
B) The potential function tracks the difference between amortized and actual costs cumulatively.  
C) The amortized cost of an operation can be less than its actual cost if the potential decreases.  
D) Σ actual cost ≤ Σ amortized cost.  

#### 10. In the context of amortized complexity, which of the following statements are correct?  
A) The amortized cost of individual tasks must always be greater than or equal to their actual cost.  
B) The potential function method requires guessing a suitable potential function to prove the amortized bounds.  
C) Amortized complexity can provide a better upper bound on the total cost of a sequence of operations than worst-case complexity.  
D) The accounting method involves assigning "credits" to operations to pay for future expensive operations.  



<br>

## Answers

#### 1. Which of the following statements correctly describe the difference between worst-case complexity and amortized complexity?  
A) ✗ Amortized complexity does not always provide a tighter bound; it provides a better bound on average over sequences, not necessarily tighter for every task.  
B) ✓ Amortized costs must sum to at least the sum of actual costs to ensure a valid upper bound.  
C) ✓ Worst-case bounds each task individually; amortized bounds average cost over a sequence.  
D) ✓ Worst-case complexity charges each task at least its actual cost, while amortized complexity may charge some tasks less than their actual cost.  

**Correct:** B, C, D


#### 2. Consider a sequence of n tasks with worst-case cost c_wc per task and actual costs c_i. Which of the following are true?  
A) ✓ The total cost is always ≤ n * c_wc by definition of worst-case cost.  
B) ✓ Sum of actual costs ≤ n * c_wc since each c_i ≤ c_wc.  
C) ✗ j * c_avg is not guaranteed to be an upper bound on the first j tasks’ cost.  
D) ✗ c_avg is average over all tasks, but j * c_avg is not necessarily an upper bound on the first j tasks.  

**Correct:** A, B


#### 3. In the aggregate method of amortized analysis, which of the following are correct?  
A) ✗ Cannot be used without knowing total cost; total cost is essential to compute amortized cost.  
B) ✗ Aggregate method does not always give tighter bounds than accounting; depends on problem.  
C) ✓ Requires a good upper bound on total cost of n operations first.  
D) ✓ Amortized cost per operation is total cost divided by n.  

**Correct:** C, D


#### 4. Regarding the potential function method, which statements are true?  
A) ✗ Initial potential P(0) is usually set to zero for convenience and correctness.  
B) ✓ Amortized cost = actual cost + change in potential (ΔP).  
C) ✗ Potential function can be negative temporarily, but usually chosen to be non-negative; not strictly required.  
D) ✓ P(i) measures how much the first i operations have been overcharged.  

**Correct:** B, D


#### 5. When analyzing the processNextSymbol() function for rewriting arithmetic statements, which of the following are correct?  
A) ✗ Number of pushes is not always equal to pops at every point; only total pushes ≤ total pops + n.  
B) ✓ Amortized cost per invocation can be bounded by 2 (push and pop operations).  
C) ✓ Worst-case complexity is O(n²) because in iteration i, up to i symbols may be popped.  
D) ✓ Amortized analysis shows overall complexity is O(n), better than worst-case bound.  

**Correct:** B, C, D


#### 6. In the accounting method applied to the binary counter increment problem, which of the following are true?  
A) ✗ Number of credits equals number of 1s, not number of 0 bits.  
B) ✓ Credits are stored on bits set to 1 to pay for future flips from 1 to 0.  
C) ✓ Each increment is charged an amortized cost of 2 units (one for flipping 0→1, one saved as credit).  
D) ✓ Amortized cost per increment (2) is less than worst-case cost (n).  

**Correct:** B, C, D


#### 7. For the binary counter increment problem, which statements about the potential function P(i) = number of 1s in the counter after the ith increment are correct?  
A) ✗ Amortized cost = actual cost + ΔP, not actual cost minus ΔP.  
B) ✓ Potential decreases by number of bits flipped from 1 to 0 (since number of 1s decreases).  
C) ✓ P(i) ≥ 0 always and P(0) = 0 by definition.  
D) ✓ Actual cost of ith increment = 1 + number of trailing 1s flipped to 0.  

**Correct:** B, C, D


#### 8. Which of the following are true about average complexity as discussed in the context of Quick Sort?  
A) ✓ Worst-case time is an upper bound on time for any input sequence.  
B) ✗ Sorting only a subset of sequences does not allow concluding average time equals that over all sequences.  
C) ✓ Average time is computed by summing times over all n! permutations and dividing by n!.  
D) ✓ Average time is proportional to n log n for sorting n distinct numbers.  

**Correct:** A, C, D


#### 9. Which of the following correctly describe the relationship between actual cost, amortized cost, and potential function in amortized analysis?  
A) ✗ Potential function need not always increase; it can increase or decrease.  
B) ✓ Potential function tracks cumulative difference between amortized and actual costs.  
C) ✓ Amortized cost can be less than actual cost if potential decreases (ΔP negative).  
D) ✓ Sum of actual costs ≤ sum of amortized costs by definition.  

**Correct:** B, C, D


#### 10. In the context of amortized complexity, which of the following statements are correct?  
A) ✗ Amortized cost of individual tasks can be less than their actual cost (some tasks overcharged, some undercharged).  
B) ✓ Potential function method requires guessing a suitable potential function to prove bounds.  
C) ✓ Amortized complexity can provide better upper bounds on total cost than worst-case complexity.  
D) ✓ Accounting method assigns credits to pay for future expensive operations.  

**Correct:** B, C, D