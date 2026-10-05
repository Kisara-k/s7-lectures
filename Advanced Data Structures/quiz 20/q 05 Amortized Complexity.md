## 5. Amortized Complexity

## Questions

#### 1. Which of the following statements about worst-case complexity are true?  
A) It represents the average time taken over all inputs of size n.  
B) It can be smaller than the average-case complexity for some inputs.  
C) It guarantees an upper bound on the time taken for every input of size n.  
D) There exists at least one input sequence of size n that attains the worst-case time.  

#### 2. When calculating the average time complexity of Quick Sort for n elements, which of the following is correct?  
A) Sorting only a subset of sequences allows concluding average time for that subset.  
B) Average time is always less than worst-case time for every input.  
C) Sum the time taken for all n! permutations and divide by n!.  
D) The average time for sorting 1000 elements is proportional to 5000 log2(1000).  

#### 3. Consider a sequence of n tasks with worst-case cost cwc per task. Which of the following are true?  
A) The average cost per task can exceed cwc.  
B) The cost of the first j tasks is at most j * cwc.  
C) The total cost of the sequence is always exactly n * cwc.  
D) The total cost is at most n * cwc.  

#### 4. Which statements about amortized complexity are correct?  
A) The sum of amortized costs over n tasks is always greater than or equal to the sum of actual costs.  
B) Amortized cost of a task can be less than its actual cost.  
C) Amortized cost provides a better upper bound on total cost than worst-case cost in some cases.  
D) Amortized complexity always equals worst-case complexity.  

#### 5. The potential function P(i) is defined as P(i) = amortizedCost(i) - actualCost(i) + P(i-1). Which of the following are true?  
A) P(i) can be negative if amortized costs are underestimated.  
B) P(0) is usually set to zero.  
C) P(i) represents the total overcharge after i tasks.  
D) P(n) - P(0) equals the sum of differences between amortized and actual costs for all n tasks.  

#### 6. In the arithmetic statement rewriting example, what is the worst-case complexity of processNextSymbol using conventional analysis?  
A) O(n log n)  
B) O(n²)  
C) O(1)  
D) O(n)  

#### 7. Why does a more careful analysis show that the complexity of processNextSymbol is O(n) instead of O(n²)?  
A) Because the total number of stack operations is linear in n.  
B) Because the for loop runs fewer times than n.  
C) Because parentheses reduce the number of operations.  
D) Because each symbol is pushed and popped at most once.  

#### 8. Which of the following are true about the aggregate method for amortized complexity?  
A) It requires finding a good upper bound on the total cost of n operations.  
B) It is always easier than the accounting or potential function methods.  
C) It divides the total cost by n to find the amortized cost per operation.  
D) It guarantees that the amortized cost is never less than the actual cost of any single operation.  

#### 9. In the accounting method, what is the role of the potential function P(i)?  
A) It must always be negative to ensure correctness.  
B) It helps prove that the guessed amortized cost bounds the actual cost.  
C) It tracks the credits or overcharges stored after i operations.  
D) It is unrelated to the actual cost of operations.  

#### 10. For the stack example in processNextSymbol, which of the following statements about the potential function are correct?  
A) The amortized cost of processing ')' is always less than the actual cost.  
B) The potential is zero at the end of processing all symbols.  
C) The potential equals the number of elements on the stack after processing the ith symbol.  
D) The potential can decrease when a ')' symbol is processed.  

#### 11. In the binary counter example, what is the worst-case cost of a single increment operation?  
A) n  
B) log n  
C) m (number of increments)  
D) 1  

#### 12. Using the aggregate method, what is the amortized cost of incrementing an n-bit binary counter m times?  
A) O(1)  
B) O(m)  
C) O(n)  
D) 2  

#### 13. In the accounting method for the binary counter, what does each unit of amortized cost represent?  
A) Credit stored to pay for flipping a bit from 1 to 0 later.  
B) The cost of resetting the entire counter.  
C) The total number of bits in the counter.  
D) Payment for flipping a bit from 0 to 1.  

#### 14. Which of the following statements about the potential function method are true?  
A) The potential function is arbitrary and does not affect the amortized cost.  
B) The amortized cost of the ith operation equals actual cost plus the change in potential.  
C) The potential function must always be non-negative.  
D) Choosing a suitable potential function can simplify amortized cost analysis.  

#### 15. For the binary counter, if P(i) is the number of 1s after the ith increment, which of the following are true?  
A) The amortized cost is always equal to the actual cost.  
B) The actual cost of the ith increment is 1 plus the number of trailing 1s before increment.  
C) P(0) = 0 since the counter starts at zero.  
D) The potential always increases after each increment.  

#### 16. Which of the following are correct interpretations of amortized complexity?  
A) It averages the cost of operations over a worst-case sequence.  
B) It guarantees the cost of every single operation is below the amortized cost.  
C) It can charge some operations more and others less than their actual cost.  
D) It is useful when occasional expensive operations are offset by many cheap ones.  

#### 17. Regarding the Quick Sort example, which statements are true?  
A) The average time is computed by averaging over all permutations of input.  
B) The worst-case time can be significantly larger than the average time.  
C) Sorting a small subset of sequences allows us to infer the average time for all sequences.  
D) The worst-case time is an upper bound for all input sequences of size n.  

#### 18. When using the potential function method, what does it mean if P(n) - P(0) < 0?  
A) The potential function is invalid for this analysis.  
B) The actual cost is always less than the amortized cost.  
C) The amortized cost overestimates the actual cost over n operations.  
D) The amortized cost underestimates the actual cost over n operations.  

#### 19. In the arithmetic statement rewriting example, what happens when the next symbol is ‘;’?  
A) The processNextSymbol method terminates immediately.  
B) An assignment statement is generated.  
C) The left-hand symbol is added to the stack.  
D) Symbols are popped until the stack is empty.  

#### 20. Which of the following are true about the relationship between amortized cost and actual cost?  
A) Amortized cost provides a useful bound when worst-case cost is too pessimistic.  
B) Amortized cost must always be greater than or equal to worst-case cost.  
C) Individual amortized costs can be less than actual costs for some tasks.  
D) The sum of amortized costs over all tasks is always at least the sum of actual costs.  



<br>

## Answers

#### 1. Which of the following statements about worst-case complexity are true?  
A) ✗ Represents average time, not worst-case.  
B) ✗ Worst-case complexity is an upper bound, so it cannot be smaller than average.  
C) ✓ Guarantees an upper bound on time for every input of size n.  
D) ✓ There exists at least one input sequence that attains worst-case time.  

**Correct:** C, D


#### 2. When calculating the average time complexity of Quick Sort for n elements, which of the following is correct?  
A) ✗ Sorting only a subset does not allow concluding average time for that subset.  
B) ✗ Average time is not guaranteed to be less than worst-case for every input.  
C) ✓ Average time is computed by summing times over all n! permutations and dividing by n!.  
D) ✓ The average time for n=1000 is proportional to 5000 log2(1000).  

**Correct:** C, D


#### 3. Consider a sequence of n tasks with worst-case cost cwc per task. Which of the following are true?  
A) ✗ Average cost per task cannot exceed worst-case cost cwc.  
B) ✓ Cost of first j tasks is at most j * cwc.  
C) ✗ Total cost is at most n * cwc, not always exactly equal.  
D) ✓ Total cost cannot exceed n * cwc.  

**Correct:** B, D


#### 4. Which statements about amortized complexity are correct?  
A) ✓ Sum of amortized costs over n tasks is ≥ sum of actual costs.  
B) ✓ Amortized cost can be less than actual cost for some tasks.  
C) ✓ Amortized cost can provide a better upper bound than worst-case cost.  
D) ✗ Amortized complexity can be less than worst-case complexity.  

**Correct:** A, B, C


#### 5. The potential function P(i) is defined as P(i) = amortizedCost(i) - actualCost(i) + P(i-1). Which of the following are true?  
A) ✗ P(i) should not be negative if amortized costs are correctly chosen.  
B) ✓ P(0) is usually set to zero.  
C) ✓ P(i) represents total overcharge after i tasks.  
D) ✓ P(n) - P(0) equals sum of differences between amortized and actual costs.  

**Correct:** B, C, D


#### 6. In the arithmetic statement rewriting example, what is the worst-case complexity of processNextSymbol using conventional analysis?  
A) ✗ Not O(n log n).  
B) ✓ Conventional analysis yields O(n²).  
C) ✗ Not constant time.  
D) ✗ Actual worst-case is O(n²) by naive analysis.  

**Correct:** B


#### 7. Why does a more careful analysis show that the complexity of processNextSymbol is O(n) instead of O(n²)?  
A) ✓ Total stack operations are linear in n.  
B) ✗ The for loop runs n times, not fewer.  
C) ✗ Parentheses alone do not reduce operations to linear.  
D) ✓ Each symbol is pushed and popped at most once.  

**Correct:** A, D


#### 8. Which of the following are true about the aggregate method for amortized complexity?  
A) ✓ Requires a good upper bound on total cost of n operations.  
B) ✗ Not always easier than other methods.  
C) ✓ Divides total cost by n to get amortized cost per operation.  
D) ✗ Amortized cost can be less than actual cost for some operations.  

**Correct:** A, C


#### 9. In the accounting method, what is the role of the potential function P(i)?  
A) ✗ P(i) should not be negative for correctness.  
B) ✓ Helps prove guessed amortized cost bounds actual cost.  
C) ✓ Tracks credits or overcharges after i operations.  
D) ✗ It is directly related to actual cost differences.  

**Correct:** B, C


#### 10. For the stack example in processNextSymbol, which of the following statements about the potential function are correct?  
A) ✗ Amortized cost of ')' is not always less than actual cost; it balances out.  
B) ✗ Potential is zero at start and end only if stack is empty at end.  
C) ✓ Potential equals number of elements on stack after ith symbol.  
D) ✓ Potential decreases when ')' is processed (stack shrinks).  

**Correct:** C, D


#### 11. In the binary counter example, what is the worst-case cost of a single increment operation?  
A) ✓ Worst-case cost is n (all bits flip).  
B) ✗ Not logarithmic in n.  
C) ✗ m is number of increments, not cost per increment.  
D) ✗ Can be more than 1.  

**Correct:** A


#### 12. Using the aggregate method, what is the amortized cost of incrementing an n-bit binary counter m times?  
A) ✗ Not O(1) exactly, but constant factor 2.  
B) ✗ Total cost is O(m), amortized per increment is constant.  
C) ✗ Not O(n) per increment.  
D) ✓ Amortized cost per increment is 2.  

**Correct:** D


#### 13. In the accounting method for the binary counter, what does each unit of amortized cost represent?  
A) ✓ Credit stored to pay for flipping bit from 1 to 0 later.  
B) ✗ Not cost of resetting entire counter.  
C) ✗ Not total number of bits.  
D) ✓ Payment for flipping bit from 0 to 1.  

**Correct:** A, D


#### 14. Which of the following statements about the potential function method are true?  
A) ✗ Potential function choice affects amortized cost calculation.  
B) ✓ Amortized cost = actual cost + change in potential.  
C) ✓ Potential function must be non-negative for correctness.  
D) ✓ Choosing suitable potential simplifies analysis.  

**Correct:** B, C, D


#### 15. For the binary counter, if P(i) is the number of 1s after the ith increment, which of the following are true?  
A) ✗ Amortized cost differs from actual cost due to potential change.  
B) ✓ Actual cost of ith increment is 1 plus number of trailing 1s before increment.  
C) ✓ P(0) = 0 since counter starts at zero.  
D) ✗ Potential can increase or decrease depending on bits flipped.  

**Correct:** B, C


#### 16. Which of the following are correct interpretations of amortized complexity?  
A) ✓ It averages cost over a worst-case sequence of operations.  
B) ✗ Does not guarantee every single operation cost ≤ amortized cost.  
C) ✓ Some operations charged more, others less than actual cost.  
D) ✓ Useful when expensive operations are offset by many cheap ones.  

**Correct:** A, C, D


#### 17. Regarding the Quick Sort example, which statements are true?  
A) ✓ Average time computed by averaging over all permutations.  
B) ✓ Worst-case time can be much larger than average time.  
C) ✗ Sorting a small subset does not allow inferring average time for all.  
D) ✓ Worst-case time is an upper bound for all inputs of size n.  

**Correct:** A, B, D


#### 18. When using the potential function method, what does it mean if P(n) - P(0) < 0?  
A) ✓ Potential function is invalid if difference is negative.  
B) ✗ Actual cost is not always less than amortized cost if difference negative.  
C) ✗ This would mean amortized cost overestimates actual cost, which is not negative difference.  
D) ✓ Amortized cost underestimates actual cost over n operations (invalid).  

**Correct:** A, D


#### 19. In the arithmetic statement rewriting example, what happens when the next symbol is ‘;’?  
A) ✗ processNextSymbol does not terminate immediately on ‘;’.  
B) ✓ Final assignment statement is generated.  
C) ✗ Left-hand symbol is not added to stack at this point.  
D) ✓ Symbols are popped until stack is empty.  

**Correct:** B, D


#### 20. Which of the following are true about the relationship between amortized cost and actual cost?  
A) ✓ Amortized cost useful when worst-case cost is too pessimistic.  
B) ✗ Amortized cost can be less than worst-case cost.  
C) ✓ Individual amortized costs can be less than actual costs.  
D) ✓ Sum of amortized costs ≥ sum of actual costs.  

**Correct:** A, C, D