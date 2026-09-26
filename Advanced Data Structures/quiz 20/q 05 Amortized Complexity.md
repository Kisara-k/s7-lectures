## 5. Amortized Complexity

## Questions

#### 1. Which of the following statements about worst-case complexity are true?  
A) It guarantees an upper bound on the time taken for every input of size n.  
B) It represents the average time taken over all inputs of size n.  
C) There exists at least one input sequence of size n that attains the worst-case time.  
D) It can be smaller than the average-case complexity for some inputs.  

#### 2. When calculating the average time complexity of Quick Sort for n elements, which of the following is correct?  
A) Sum the time taken for all n! permutations and divide by n!.  
B) Average time is always less than worst-case time for every input.  
C) The average time for sorting 1000 elements is proportional to 5000 log2(1000).  
D) Sorting only a subset of sequences allows concluding average time for that subset.  

#### 3. Consider a sequence of n tasks with worst-case cost cwc per task. Which of the following are true?  
A) The total cost of the sequence is always exactly n * cwc.  
B) The total cost is at most n * cwc.  
C) The cost of the first j tasks is at most j * cwc.  
D) The average cost per task can exceed cwc.  

#### 4. Which statements about amortized complexity are correct?  
A) Amortized cost of a task can be less than its actual cost.  
B) The sum of amortized costs over n tasks is always greater than or equal to the sum of actual costs.  
C) Amortized complexity always equals worst-case complexity.  
D) Amortized cost provides a better upper bound on total cost than worst-case cost in some cases.  

#### 5. The potential function P(i) is defined as P(i) = amortizedCost(i) - actualCost(i) + P(i-1). Which of the following are true?  
A) P(0) is usually set to zero.  
B) P(i) represents the total overcharge after i tasks.  
C) P(i) can be negative if amortized costs are underestimated.  
D) P(n) - P(0) equals the sum of differences between amortized and actual costs for all n tasks.  

#### 6. In the arithmetic statement rewriting example, what is the worst-case complexity of processNextSymbol using conventional analysis?  
A) O(n)  
B) O(n log n)  
C) O(n²)  
D) O(1)  

#### 7. Why does a more careful analysis show that the complexity of processNextSymbol is O(n) instead of O(n²)?  
A) Because the total number of stack operations is linear in n.  
B) Because each symbol is pushed and popped at most once.  
C) Because parentheses reduce the number of operations.  
D) Because the for loop runs fewer times than n.  

#### 8. Which of the following are true about the aggregate method for amortized complexity?  
A) It requires finding a good upper bound on the total cost of n operations.  
B) It divides the total cost by n to find the amortized cost per operation.  
C) It is always easier than the accounting or potential function methods.  
D) It guarantees that the amortized cost is never less than the actual cost of any single operation.  

#### 9. In the accounting method, what is the role of the potential function P(i)?  
A) It tracks the credits or overcharges stored after i operations.  
B) It must always be negative to ensure correctness.  
C) It helps prove that the guessed amortized cost bounds the actual cost.  
D) It is unrelated to the actual cost of operations.  

#### 10. For the stack example in processNextSymbol, which of the following statements about the potential function are correct?  
A) The potential equals the number of elements on the stack after processing the ith symbol.  
B) The potential can decrease when a ')' symbol is processed.  
C) The amortized cost of processing ')' is always less than the actual cost.  
D) The potential is zero at the end of processing all symbols.  

#### 11. In the binary counter example, what is the worst-case cost of a single increment operation?  
A) 1  
B) log n  
C) n  
D) m (number of increments)  

#### 12. Using the aggregate method, what is the amortized cost of incrementing an n-bit binary counter m times?  
A) O(n)  
B) O(m)  
C) O(1)  
D) 2  

#### 13. In the accounting method for the binary counter, what does each unit of amortized cost represent?  
A) Payment for flipping a bit from 0 to 1.  
B) Credit stored to pay for flipping a bit from 1 to 0 later.  
C) The total number of bits in the counter.  
D) The cost of resetting the entire counter.  

#### 14. Which of the following statements about the potential function method are true?  
A) The potential function must always be non-negative.  
B) The amortized cost of the ith operation equals actual cost plus the change in potential.  
C) The potential function is arbitrary and does not affect the amortized cost.  
D) Choosing a suitable potential function can simplify amortized cost analysis.  

#### 15. For the binary counter, if P(i) is the number of 1s after the ith increment, which of the following are true?  
A) P(0) = 0 since the counter starts at zero.  
B) The actual cost of the ith increment is 1 plus the number of trailing 1s before increment.  
C) The amortized cost is always equal to the actual cost.  
D) The potential always increases after each increment.  

#### 16. Which of the following are correct interpretations of amortized complexity?  
A) It averages the cost of operations over a worst-case sequence.  
B) It guarantees the cost of every single operation is below the amortized cost.  
C) It can charge some operations more and others less than their actual cost.  
D) It is useful when occasional expensive operations are offset by many cheap ones.  

#### 17. Regarding the Quick Sort example, which statements are true?  
A) The worst-case time is an upper bound for all input sequences of size n.  
B) The average time is computed by averaging over all permutations of input.  
C) Sorting a small subset of sequences allows us to infer the average time for all sequences.  
D) The worst-case time can be significantly larger than the average time.  

#### 18. When using the potential function method, what does it mean if P(n) - P(0) < 0?  
A) The amortized cost underestimates the actual cost over n operations.  
B) The amortized cost overestimates the actual cost over n operations.  
C) The potential function is invalid for this analysis.  
D) The actual cost is always less than the amortized cost.  

#### 19. In the arithmetic statement rewriting example, what happens when the next symbol is ‘;’?  
A) Symbols are popped until the stack is empty.  
B) An assignment statement is generated.  
C) The left-hand symbol is added to the stack.  
D) The processNextSymbol method terminates immediately.  

#### 20. Which of the following are true about the relationship between amortized cost and actual cost?  
A) The sum of amortized costs over all tasks is always at least the sum of actual costs.  
B) Individual amortized costs can be less than actual costs for some tasks.  
C) Amortized cost must always be greater than or equal to worst-case cost.  
D) Amortized cost provides a useful bound when worst-case cost is too pessimistic.



<br>

## Answers

#### 1. Which of the following statements about worst-case complexity are true?  
A) ✓ Guarantees an upper bound on time for every input of size n.  
B) ✗ Represents average time, not worst-case.  
C) ✓ There exists at least one input sequence that attains worst-case time.  
D) ✗ Worst-case complexity is an upper bound, so it cannot be smaller than average.  

**Correct:** A, C


#### 2. When calculating the average time complexity of Quick Sort for n elements, which of the following is correct?  
A) ✓ Average time is computed by summing times over all n! permutations and dividing by n!.  
B) ✗ Average time is not guaranteed to be less than worst-case for every input.  
C) ✓ The average time for n=1000 is proportional to 5000 log2(1000).  
D) ✗ Sorting only a subset does not allow concluding average time for that subset.  

**Correct:** A, C


#### 3. Consider a sequence of n tasks with worst-case cost cwc per task. Which of the following are true?  
A) ✗ Total cost is at most n * cwc, not always exactly equal.  
B) ✓ Total cost cannot exceed n * cwc.  
C) ✓ Cost of first j tasks is at most j * cwc.  
D) ✗ Average cost per task cannot exceed worst-case cost cwc.  

**Correct:** B, C


#### 4. Which statements about amortized complexity are correct?  
A) ✓ Amortized cost can be less than actual cost for some tasks.  
B) ✓ Sum of amortized costs over n tasks is ≥ sum of actual costs.  
C) ✗ Amortized complexity can be less than worst-case complexity.  
D) ✓ Amortized cost can provide a better upper bound than worst-case cost.  

**Correct:** A, B, D


#### 5. The potential function P(i) is defined as P(i) = amortizedCost(i) - actualCost(i) + P(i-1). Which of the following are true?  
A) ✓ P(0) is usually set to zero.  
B) ✓ P(i) represents total overcharge after i tasks.  
C) ✗ P(i) should not be negative if amortized costs are correctly chosen.  
D) ✓ P(n) - P(0) equals sum of differences between amortized and actual costs.  

**Correct:** A, B, D


#### 6. In the arithmetic statement rewriting example, what is the worst-case complexity of processNextSymbol using conventional analysis?  
A) ✗ Actual worst-case is O(n²) by naive analysis.  
B) ✗ Not O(n log n).  
C) ✓ Conventional analysis yields O(n²).  
D) ✗ Not constant time.  

**Correct:** C


#### 7. Why does a more careful analysis show that the complexity of processNextSymbol is O(n) instead of O(n²)?  
A) ✓ Total stack operations are linear in n.  
B) ✓ Each symbol is pushed and popped at most once.  
C) ✗ Parentheses alone do not reduce operations to linear.  
D) ✗ The for loop runs n times, not fewer.  

**Correct:** A, B


#### 8. Which of the following are true about the aggregate method for amortized complexity?  
A) ✓ Requires a good upper bound on total cost of n operations.  
B) ✓ Divides total cost by n to get amortized cost per operation.  
C) ✗ Not always easier than other methods.  
D) ✗ Amortized cost can be less than actual cost for some operations.  

**Correct:** A, B


#### 9. In the accounting method, what is the role of the potential function P(i)?  
A) ✓ Tracks credits or overcharges after i operations.  
B) ✗ P(i) should not be negative for correctness.  
C) ✓ Helps prove guessed amortized cost bounds actual cost.  
D) ✗ It is directly related to actual cost differences.  

**Correct:** A, C


#### 10. For the stack example in processNextSymbol, which of the following statements about the potential function are correct?  
A) ✓ Potential equals number of elements on stack after ith symbol.  
B) ✓ Potential decreases when ')' is processed (stack shrinks).  
C) ✗ Amortized cost of ')' is not always less than actual cost; it balances out.  
D) ✗ Potential is zero at start and end only if stack is empty at end.  

**Correct:** A, B


#### 11. In the binary counter example, what is the worst-case cost of a single increment operation?  
A) ✗ Can be more than 1.  
B) ✗ Not logarithmic in n.  
C) ✓ Worst-case cost is n (all bits flip).  
D) ✗ m is number of increments, not cost per increment.  

**Correct:** C


#### 12. Using the aggregate method, what is the amortized cost of incrementing an n-bit binary counter m times?  
A) ✗ Not O(n) per increment.  
B) ✗ Total cost is O(m), amortized per increment is constant.  
C) ✗ Not O(1) exactly, but constant factor 2.  
D) ✓ Amortized cost per increment is 2.  

**Correct:** D


#### 13. In the accounting method for the binary counter, what does each unit of amortized cost represent?  
A) ✓ Payment for flipping bit from 0 to 1.  
B) ✓ Credit stored to pay for flipping bit from 1 to 0 later.  
C) ✗ Not total number of bits.  
D) ✗ Not cost of resetting entire counter.  

**Correct:** A, B


#### 14. Which of the following statements about the potential function method are true?  
A) ✓ Potential function must be non-negative for correctness.  
B) ✓ Amortized cost = actual cost + change in potential.  
C) ✗ Potential function choice affects amortized cost calculation.  
D) ✓ Choosing suitable potential simplifies analysis.  

**Correct:** A, B, D


#### 15. For the binary counter, if P(i) is the number of 1s after the ith increment, which of the following are true?  
A) ✓ P(0) = 0 since counter starts at zero.  
B) ✓ Actual cost of ith increment is 1 plus number of trailing 1s before increment.  
C) ✗ Amortized cost differs from actual cost due to potential change.  
D) ✗ Potential can increase or decrease depending on bits flipped.  

**Correct:** A, B


#### 16. Which of the following are correct interpretations of amortized complexity?  
A) ✓ It averages cost over a worst-case sequence of operations.  
B) ✗ Does not guarantee every single operation cost ≤ amortized cost.  
C) ✓ Some operations charged more, others less than actual cost.  
D) ✓ Useful when expensive operations are offset by many cheap ones.  

**Correct:** A, C, D


#### 17. Regarding the Quick Sort example, which statements are true?  
A) ✓ Worst-case time is an upper bound for all inputs of size n.  
B) ✓ Average time computed by averaging over all permutations.  
C) ✗ Sorting a small subset does not allow inferring average time for all.  
D) ✓ Worst-case time can be much larger than average time.  

**Correct:** A, B, D


#### 18. When using the potential function method, what does it mean if P(n) - P(0) < 0?  
A) ✓ Amortized cost underestimates actual cost over n operations (invalid).  
B) ✗ This would mean amortized cost overestimates actual cost, which is not negative difference.  
C) ✓ Potential function is invalid if difference is negative.  
D) ✗ Actual cost is not always less than amortized cost if difference negative.  

**Correct:** A, C


#### 19. In the arithmetic statement rewriting example, what happens when the next symbol is ‘;’?  
A) ✓ Symbols are popped until stack is empty.  
B) ✓ Final assignment statement is generated.  
C) ✗ Left-hand symbol is not added to stack at this point.  
D) ✗ processNextSymbol does not terminate immediately on ‘;’.  

**Correct:** A, B


#### 20. Which of the following are true about the relationship between amortized cost and actual cost?  
A) ✓ Sum of amortized costs ≥ sum of actual costs.  
B) ✓ Individual amortized costs can be less than actual costs.  
C) ✗ Amortized cost can be less than worst-case cost.  
D) ✓ Amortized cost useful when worst-case cost is too pessimistic.  

**Correct:** A, B, D