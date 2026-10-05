## 1. Machine Learning Basics Revision

## Questions

#### 1. Which of the following statements correctly describe the reasons why machine learning is preferred over explicit programming in complex tasks?  
A) It is often impossible to design explicit rules due to incomplete knowledge and dynamic environments.  
B) Machine learning models always provide fully interpretable and transparent decision processes.  
C) Data-driven approaches can outperform white-box models that rely on inaccurate assumptions.  
D) Machine learning eliminates the need for any human expertise or domain knowledge.

#### 2. In the context of supervised learning, which of the following are true about classification and regression tasks?  
A) Classification predicts categorical outputs, while regression predicts continuous outputs.  
B) Regression models are used when the output variable is discrete and finite.  
C) Both classification and regression require labeled training data.  
D) Classification can only handle binary classes, not multi-class or multi-label problems.

#### 3. Which of the following best characterize the No Free Lunch theorem in machine learning?  
A) No single learning algorithm is universally superior across all possible problems.  
B) Given sufficient data, all algorithms will converge to the same performance.  
C) Prior knowledge or assumptions are necessary to select an appropriate algorithm for a specific problem.  
D) Complex models always outperform simpler models regardless of the problem domain.

#### 4. Regarding reinforcement learning, which statements are accurate?  
A) Rewards are typically immediate and provide detailed feedback for each action.  
B) The policy maps states to actions to maximize expected cumulative future rewards.  
C) Reinforcement learning requires labeled input-output pairs for training.  
D) Delayed and scalar rewards make credit assignment a challenging problem.

#### 5. Which of the following are valid distinctions between machine learning and traditional statistics?  
A) Machine learning emphasizes predictive performance and scalability more than interpretability.  
B) Statistics focuses primarily on building autonomous agents.  
C) Both fields share foundational mathematical tools like calculus and probability.  
D) Machine learning always requires probabilistic models, whereas statistics does not.

#### 6. In active learning, which of the following strategies correctly describe how the learner selects data points for labeling?  
A) Membership query synthesis involves generating new, synthetic examples for querying.  
B) Stream-based selective sampling evaluates each incoming example individually to decide on querying.  
C) Pool-based sampling ranks all unlabeled examples and queries the most informative ones in batches.  
D) Active learning is a form of reinforcement learning where the agent receives rewards for queries.

#### 7. Which of the following statements about dimensionality reduction and the curse of dimensionality are true?  
A) Increasing feature dimensions always improves model predictive power if enough data is available.  
B) Dimensionality reduction can distort data and lead to misleading interpretations if applied naively.  
C) The curse of dimensionality implies that exponentially more data is needed as feature space dimensionality grows.  
D) Dimensionality reduction techniques guarantee preservation of all intrinsic data properties.

#### 8. Consider the Rashomon effect in machine learning. Which of the following are correct implications?  
A) Multiple models with very different structures can achieve similar predictive accuracy on the same data.  
B) Small perturbations in training data can lead to significantly different learned models with comparable performance.  
C) The Rashomon effect implies that interpretability is always sacrificed for accuracy.  
D) It highlights the subjectivity and variability in model selection and evaluation.

#### 9. Which of the following best describe the differences between inductive, deductive, and transductive learning?  
A) Inductive learning generalizes from specific examples to a universal rule.  
B) Deductive learning derives specific conclusions from general rules or facts.  
C) Transductive learning predicts specific examples directly without learning a general function.  
D) Transductive learning requires a fully labeled dataset for training.

#### 10. Ensemble learning methods improve predictive performance by:  
A) Combining multiple models that disagree to reduce overall error.  
B) Using a single complex model trained on all data to avoid bias.  
C) Incrementally focusing on training instances misclassified by previous models (boosting).  
D) Averaging predictions from identical models trained on the same data without variation.



<br>

## Answers

#### 1. Which of the following statements correctly describe the reasons why machine learning is preferred over explicit programming in complex tasks?  
A) ✓ It is often impossible to design explicit rules due to incomplete knowledge and dynamic environments.  
B) ✗ Machine learning models are often black boxes and not always fully interpretable or transparent.  
C) ✓ Data-driven approaches can outperform white-box models that rely on inaccurate assumptions.  
D) ✗ Human expertise or domain knowledge is often still required to guide ML development.

**Correct:** A, C


#### 2. In the context of supervised learning, which of the following are true about classification and regression tasks?  
A) ✓ Classification predicts categorical outputs, while regression predicts continuous outputs.  
B) ✗ Regression deals with continuous outputs, not discrete ones.  
C) ✓ Both classification and regression require labeled training data.  
D) ✗ Classification includes binary, multi-class, and multi-label problems, not just binary.

**Correct:** A, C


#### 3. Which of the following best characterize the No Free Lunch theorem in machine learning?  
A) ✓ No single learning algorithm is universally superior across all possible problems.  
B) ✗ Algorithms do not necessarily converge to the same performance given sufficient data; performance depends on problem alignment.  
C) ✓ Prior knowledge or assumptions are necessary to select an appropriate algorithm for a specific problem.  
D) ✗ Complex models do not always outperform simpler ones; performance depends on problem and data.

**Correct:** A, C


#### 4. Regarding reinforcement learning, which statements are accurate?  
A) ✗ Rewards are typically delayed and sparse, not immediate or detailed.  
B) ✓ The policy maps states to actions to maximize expected cumulative future rewards.  
C) ✗ Reinforcement learning does not require labeled input-output pairs; it learns from rewards.  
D) ✓ Delayed and scalar rewards make credit assignment challenging.

**Correct:** B, D


#### 5. Which of the following are valid distinctions between machine learning and traditional statistics?  
A) ✓ Machine learning emphasizes predictive performance and scalability more than interpretability.  
B) ✗ Statistics focuses more on inference and explanation, not primarily on building autonomous agents.  
C) ✓ Both fields share foundational mathematical tools like calculus and probability.  
D) ✗ Machine learning does not always require probabilistic models; many non-probabilistic methods exist.

**Correct:** A, C


#### 6. In active learning, which of the following strategies correctly describe how the learner selects data points for labeling?  
A) ✓ Membership query synthesis involves generating new, synthetic examples for querying.  
B) ✓ Stream-based selective sampling evaluates each incoming example individually to decide on querying.  
C) ✓ Pool-based sampling ranks all unlabeled examples and queries the most informative ones in batches.  
D) ✗ Active learning is not reinforcement learning; it requires human oracle feedback, not reward signals.

**Correct:** A, B, C


#### 7. Which of the following statements about dimensionality reduction and the curse of dimensionality are true?  
A) ✗ Increasing feature dimensions without enough data reduces predictive power due to sparsity.  
B) ✓ Dimensionality reduction can distort data and lead to misleading interpretations if applied naively.  
C) ✓ The curse of dimensionality implies exponentially more data is needed as feature space dimensionality grows.  
D) ✗ Dimensionality reduction techniques do not guarantee preservation of all intrinsic data properties.

**Correct:** B, C


#### 8. Consider the Rashomon effect in machine learning. Which of the following are correct implications?  
A) ✓ Multiple models with very different structures can achieve similar predictive accuracy on the same data.  
B) ✓ Small perturbations in training data can lead to significantly different learned models with comparable performance.  
C) ✗ The Rashomon effect does not imply interpretability is always sacrificed for accuracy; it highlights multiple equally good models.  
D) ✓ It highlights the subjectivity and variability in model selection and evaluation.

**Correct:** A, B, D


#### 9. Which of the following best describe the differences between inductive, deductive, and transductive learning?  
A) ✓ Inductive learning generalizes from specific examples to a universal rule.  
B) ✓ Deductive learning derives specific conclusions from general rules or facts.  
C) ✓ Transductive learning predicts specific examples directly without learning a general function.  
D) ✗ Transductive learning does not require a fully labeled dataset; it uses labeled examples directly for prediction without generalization.

**Correct:** A, B, C


#### 10. Ensemble learning methods improve predictive performance by:  
A) ✓ Combining multiple models that disagree to reduce overall error.  
B) ✗ Using a single complex model does not constitute ensemble learning.  
C) ✓ Incrementally focusing on training instances misclassified by previous models (boosting).  
D) ✗ Averaging identical models trained on the same data without variation does not improve performance.

**Correct:** A, C