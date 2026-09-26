## 5. Amortized Complexity

## Questions

#### 1. Which of the following statements correctly describe the difference between worst-case complexity and amortized complexity?  
A) Worst-case complexity charges each task at least its actual cost, while amortized complexity may charge some tasks less than their actual cost.  
B) Amortized complexity always provides a tighter upper bound than worst-case complexity.  
C) Worst-case complexity bounds the cost of every single task, whereas amortized complexity bounds the average cost over a sequence of tasks.  
D) Amortized complexity requires the sum of amortized costs to be at least the sum of actual costs over all tasks.

#### 2. Consider a sequence of n tasks with worst-case cost c_wc per task and actual costs c_i. Which of the following are true?  
A) The total cost of the sequence is always less than or equal to n * c_wc.  
B) The average cost per task c_avg = (Σ c_i) / n is always an upper bound on the cost of the first j tasks for any j ≤ n.  
C) The sum of actual costs Σ c_i is always less than or equal to n * c_wc.  
D) The cost of the first j tasks can be bounded by j * c_avg.

#### 3. In the aggregate method of amortized analysis, which of the following are correct?  
A) The amortized cost per operation is obtained by dividing the total cost of n operations by n.  
B) It requires first finding a good upper bound on the total cost of n operations.  
C) It always gives a tighter bound than the accounting method.  
D) It can be used without knowing the total cost of the sequence.

#### 4. Regarding the potential function method, which statements are true?  
A) The potential function P(i) represents the amount by which the first i operations have been overcharged.  
B) The amortized cost of the ith operation equals the actual cost plus the change in potential, i.e., amortized cost = actual cost + ΔP.  
C) The potential function must always be non-negative for all i.  
D) The initial potential P(0) can be any positive number.

#### 5. When analyzing the processNextSymbol() function for rewriting arithmetic statements, which of the following are correct?  
A) The worst-case complexity is O(n²) because each iteration can pop up to i symbols from the stack.  
B) A more careful amortized analysis shows the overall complexity is O(n).  
C) The amortized cost per invocation of processNextSymbol() can be bounded by 2.  
D) The number of push operations is always equal to the number of pop operations.

#### 6. In the accounting method applied to the binary counter increment problem, which of the following are true?  
A) Each increment is charged an amortized cost of 2 units.  
B) Credits are stored on bits set to 1 to pay for future bit flips from 1 to 0.  
C) The total number of credits after m increments equals the number of 0 bits in the counter.  
D) The amortized cost per increment is less than the worst-case cost of n.

#### 7. For the binary counter increment problem, which statements about the potential function P(i) = number of 1s in the counter after the ith increment are correct?  
A) P(i) is always non-negative and P(0) = 0.  
B) The actual cost of the ith increment is 1 plus the number of trailing 1s before the increment.  
C) The amortized cost of the ith increment equals the actual cost minus the change in potential.  
D) The potential function decreases by the number of bits flipped from 1 to 0 during the increment.

#### 8. Which of the following are true about average complexity as discussed in the context of Quick Sort?  
A) The average time for sorting n distinct numbers is proportional to n log n.  
B) The average time is computed by summing the time over all n! permutations and dividing by n!.  
C) Sorting only a subset of sequences allows us to conclude the average time for that subset equals the average time over all sequences.  
D) The worst-case time provides an upper bound on the time for any input sequence.

#### 9. Which of the following correctly describe the relationship between actual cost, amortized cost, and potential function in amortized analysis?  
A) Σ actual cost ≤ Σ amortized cost.  
B) The potential function tracks the difference between amortized and actual costs cumulatively.  
C) The amortized cost of an operation can be less than its actual cost if the potential decreases.  
D) The potential function must always increase or stay constant.

#### 10. In the context of amortized complexity, which of the following statements are correct?  
A) Amortized complexity can provide a better upper bound on the total cost of a sequence of operations than worst-case complexity.  
B) The amortized cost of individual tasks must always be greater than or equal to their actual cost.  
C) The accounting method involves assigning "credits" to operations to pay for future expensive operations.  
D) The potential function method requires guessing a suitable potential function to prove the amortized bounds.



<br>

## Answers

#### 1. Which of the following statements correctly describe the difference between worst-case complexity and amortized complexity?  
A) ✓ Worst-case complexity charges each task at least its actual cost, while amortized complexity may charge some tasks less than their actual cost.  
B) ✗ Amortized complexity does not always provide a tighter bound; it provides a better bound on average over sequences, not necessarily tighter for every task.  
C) ✓ Worst-case bounds each task individually; amortized bounds average cost over a sequence.  
D) ✓ Amortized costs must sum to at least the sum of actual costs to ensure a valid upper bound.  

**Correct:** A,C,D


#### 2. Consider a sequence of n tasks with worst-case cost c_wc per task and actual costs c_i. Which of the following are true?  
A) ✓ The total cost is always ≤ n * c_wc by definition of worst-case cost.  
B) ✗ c_avg is average over all tasks, but j * c_avg is not necessarily an upper bound on the first j tasks.  
C) ✓ Sum of actual costs ≤ n * c_wc since each c_i ≤ c_wc.  
D) ✗ j * c_avg is not guaranteed to be an upper bound on the first j tasks’ cost.  

**Correct:** A,C


#### 3. In the aggregate method of amortized analysis, which of the following are correct?  
A) ✓ Amortized cost per operation is total cost divided by n.  
B) ✓ Requires a good upper bound on total cost of n operations first.  
C) ✗ Aggregate method does not always give tighter bounds than accounting; depends on problem.  
D) ✗ Cannot be used without knowing total cost; total cost is essential to compute amortized cost.  

**Correct:** A,B


#### 4. Regarding the potential function method, which statements are true?  
A) ✓ P(i) measures how much the first i operations have been overcharged.  
B) ✓ Amortized cost = actual cost + change in potential (ΔP).  
C) ✗ Potential function can be negative temporarily, but usually chosen to be non-negative; not strictly required.  
D) ✗ Initial potential P(0) is usually set to zero for convenience and correctness.  

**Correct:** A,B


#### 5. When analyzing the processNextSymbol() function for rewriting arithmetic statements, which of the following are correct?  
A) ✓ Worst-case complexity is O(n²) because in iteration i, up to i symbols may be popped.  
B) ✓ Amortized analysis shows overall complexity is O(n), better than worst-case bound.  
C) ✓ Amortized cost per invocation can be bounded by 2 (push and pop operations).  
D) ✗ Number of pushes is not always equal to pops at every point; only total pushes ≤ total pops + n.  

**Correct:** A,B,C


#### 6. In the accounting method applied to the binary counter increment problem, which of the following are true?  
A) ✓ Each increment is charged an amortized cost of 2 units (one for flipping 0→1, one saved as credit).  
B) ✓ Credits are stored on bits set to 1 to pay for future flips from 1 to 0.  
C) ✗ Number of credits equals number of 1s, not number of 0 bits.  
D) ✓ Amortized cost per increment (2) is less than worst-case cost (n).  

**Correct:** A,B,D


#### 7. For the binary counter increment problem, which statements about the potential function P(i) = number of 1s in the counter after the ith increment are correct?  
A) ✓ P(i) ≥ 0 always and P(0) = 0 by definition.  
B) ✓ Actual cost of ith increment = 1 + number of trailing 1s flipped to 0.  
C) ✗ Amortized cost = actual cost + ΔP, not actual cost minus ΔP.  
D) ✓ Potential decreases by number of bits flipped from 1 to 0 (since number of 1s decreases).  

**Correct:** A,B,D


#### 8. Which of the following are true about average complexity as discussed in the context of Quick Sort?  
A) ✓ Average time is proportional to n log n for sorting n distinct numbers.  
B) ✓ Average time is computed by summing times over all n! permutations and dividing by n!.  
C) ✗ Sorting only a subset of sequences does not allow concluding average time equals that over all sequences.  
D) ✓ Worst-case time is an upper bound on time for any input sequence.  

**Correct:** A,B,D


#### 9. Which of the following correctly describe the relationship between actual cost, amortized cost, and potential function in amortized analysis?  
A) ✓ Sum of actual costs ≤ sum of amortized costs by definition.  
B) ✓ Potential function tracks cumulative difference between amortized and actual costs.  
C) ✓ Amortized cost can be less than actual cost if potential decreases (ΔP negative).  
D) ✗ Potential function need not always increase; it can increase or decrease.  

**Correct:** A,B,C


#### 10. In the context of amortized complexity, which of the following statements are correct?  
A) ✓ Amortized complexity can provide better upper bounds on total cost than worst-case complexity.  
B) ✗ Amortized cost of individual tasks can be less than their actual cost (some tasks overcharged, some undercharged).  
C) ✓ Accounting method assigns credits to pay for future expensive operations.  
D) ✓ Potential function method requires guessing a suitable potential function to prove bounds.  

**Correct:** A,C,D