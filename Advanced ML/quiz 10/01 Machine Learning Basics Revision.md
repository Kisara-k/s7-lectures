## 1. Machine Learning Basics Revision

## Questions

#### 1. Which of the following statements correctly describe the reasons why machine learning is preferred over explicit programming in complex tasks?  
A) Machine learning eliminates the need for any human expertise or domain knowledge.  
B) Machine learning models always provide fully interpretable and transparent decision processes.  
C) Data-driven approaches can outperform white-box models that rely on inaccurate assumptions.  
D) It is often impossible to design explicit rules due to incomplete knowledge and dynamic environments.  

#### 2. In the context of supervised learning, which of the following are true about classification and regression tasks?  
A) Both classification and regression require labeled training data.  
B) Classification predicts categorical outputs, while regression predicts continuous outputs.  
C) Classification can only handle binary classes, not multi-class or multi-label problems.  
D) Regression models are used when the output variable is discrete and finite.  

#### 3. Which of the following best characterize the No Free Lunch theorem in machine learning?  
A) Given sufficient data, all algorithms will converge to the same performance.  
B) Complex models always outperform simpler models regardless of the problem domain.  
C) Prior knowledge or assumptions are necessary to select an appropriate algorithm for a specific problem.  
D) No single learning algorithm is universally superior across all possible problems.  

#### 4. Regarding reinforcement learning, which statements are accurate?  
A) The policy maps states to actions to maximize expected cumulative future rewards.  
B) Reinforcement learning requires labeled input-output pairs for training.  
C) Delayed and scalar rewards make credit assignment a challenging problem.  
D) Rewards are typically immediate and provide detailed feedback for each action.  

#### 5. Which of the following are valid distinctions between machine learning and traditional statistics?  
A) Machine learning always requires probabilistic models, whereas statistics does not.  
B) Machine learning emphasizes predictive performance and scalability more than interpretability.  
C) Both fields share foundational mathematical tools like calculus and probability.  
D) Statistics focuses primarily on building autonomous agents.  

#### 6. In active learning, which of the following strategies correctly describe how the learner selects data points for labeling?  
A) Membership query synthesis involves generating new, synthetic examples for querying.  
B) Stream-based selective sampling evaluates each incoming example individually to decide on querying.  
C) Active learning is a form of reinforcement learning where the agent receives rewards for queries.  
D) Pool-based sampling ranks all unlabeled examples and queries the most informative ones in batches.  

#### 7. Which of the following statements about dimensionality reduction and the curse of dimensionality are true?  
A) Increasing feature dimensions always improves model predictive power if enough data is available.  
B) Dimensionality reduction techniques guarantee preservation of all intrinsic data properties.  
C) The curse of dimensionality implies that exponentially more data is needed as feature space dimensionality grows.  
D) Dimensionality reduction can distort data and lead to misleading interpretations if applied naively.  

#### 8. Consider the Rashomon effect in machine learning. Which of the following are correct implications?  
A) Multiple models with very different structures can achieve similar predictive accuracy on the same data.  
B) It highlights the subjectivity and variability in model selection and evaluation.  
C) Small perturbations in training data can lead to significantly different learned models with comparable performance.  
D) The Rashomon effect implies that interpretability is always sacrificed for accuracy.  

#### 9. Which of the following best describe the differences between inductive, deductive, and transductive learning?  
A) Deductive learning derives specific conclusions from general rules or facts.  
B) Transductive learning requires a fully labeled dataset for training.  
C) Transductive learning predicts specific examples directly without learning a general function.  
D) Inductive learning generalizes from specific examples to a universal rule.  

#### 10. Ensemble learning methods improve predictive performance by:  
A) Combining multiple models that disagree to reduce overall error.  
B) Averaging predictions from identical models trained on the same data without variation.  
C) Using a single complex model trained on all data to avoid bias.  
D) Incrementally focusing on training instances misclassified by previous models (boosting).  



<br>

## Answers

#### 1. Which of the following statements correctly describe the reasons why machine learning is preferred over explicit programming in complex tasks?  
A) ✗ Human expertise or domain knowledge is often still required to guide ML development.  
B) ✗ Machine learning models are often black boxes and not always fully interpretable or transparent.  
C) ✓ Data-driven approaches can outperform white-box models that rely on inaccurate assumptions.  
D) ✓ It is often impossible to design explicit rules due to incomplete knowledge and dynamic environments.  

**Correct:** C, D


#### 2. In the context of supervised learning, which of the following are true about classification and regression tasks?  
A) ✓ Both classification and regression require labeled training data.  
B) ✓ Classification predicts categorical outputs, while regression predicts continuous outputs.  
C) ✗ Classification includes binary, multi-class, and multi-label problems, not just binary.  
D) ✗ Regression deals with continuous outputs, not discrete ones.  

**Correct:** A, B


#### 3. Which of the following best characterize the No Free Lunch theorem in machine learning?  
A) ✗ Algorithms do not necessarily converge to the same performance given sufficient data; performance depends on problem alignment.  
B) ✗ Complex models do not always outperform simpler ones; performance depends on problem and data.  
C) ✓ Prior knowledge or assumptions are necessary to select an appropriate algorithm for a specific problem.  
D) ✓ No single learning algorithm is universally superior across all possible problems.  

**Correct:** C, D


#### 4. Regarding reinforcement learning, which statements are accurate?  
A) ✓ The policy maps states to actions to maximize expected cumulative future rewards.  
B) ✗ Reinforcement learning does not require labeled input-output pairs; it learns from rewards.  
C) ✓ Delayed and scalar rewards make credit assignment challenging.  
D) ✗ Rewards are typically delayed and sparse, not immediate or detailed.  

**Correct:** A, C


#### 5. Which of the following are valid distinctions between machine learning and traditional statistics?  
A) ✗ Machine learning does not always require probabilistic models; many non-probabilistic methods exist.  
B) ✓ Machine learning emphasizes predictive performance and scalability more than interpretability.  
C) ✓ Both fields share foundational mathematical tools like calculus and probability.  
D) ✗ Statistics focuses more on inference and explanation, not primarily on building autonomous agents.  

**Correct:** B, C


#### 6. In active learning, which of the following strategies correctly describe how the learner selects data points for labeling?  
A) ✓ Membership query synthesis involves generating new, synthetic examples for querying.  
B) ✓ Stream-based selective sampling evaluates each incoming example individually to decide on querying.  
C) ✗ Active learning is not reinforcement learning; it requires human oracle feedback, not reward signals.  
D) ✓ Pool-based sampling ranks all unlabeled examples and queries the most informative ones in batches.  

**Correct:** A, B, D


#### 7. Which of the following statements about dimensionality reduction and the curse of dimensionality are true?  
A) ✗ Increasing feature dimensions without enough data reduces predictive power due to sparsity.  
B) ✗ Dimensionality reduction techniques do not guarantee preservation of all intrinsic data properties.  
C) ✓ The curse of dimensionality implies exponentially more data is needed as feature space dimensionality grows.  
D) ✓ Dimensionality reduction can distort data and lead to misleading interpretations if applied naively.  

**Correct:** C, D


#### 8. Consider the Rashomon effect in machine learning. Which of the following are correct implications?  
A) ✓ Multiple models with very different structures can achieve similar predictive accuracy on the same data.  
B) ✓ It highlights the subjectivity and variability in model selection and evaluation.  
C) ✓ Small perturbations in training data can lead to significantly different learned models with comparable performance.  
D) ✗ The Rashomon effect does not imply interpretability is always sacrificed for accuracy; it highlights multiple equally good models.  

**Correct:** A, B, C


#### 9. Which of the following best describe the differences between inductive, deductive, and transductive learning?  
A) ✓ Deductive learning derives specific conclusions from general rules or facts.  
B) ✗ Transductive learning does not require a fully labeled dataset; it uses labeled examples directly for prediction without generalization.  
C) ✓ Transductive learning predicts specific examples directly without learning a general function.  
D) ✓ Inductive learning generalizes from specific examples to a universal rule.  

**Correct:** A, C, D


#### 10. Ensemble learning methods improve predictive performance by:  
A) ✓ Combining multiple models that disagree to reduce overall error.  
B) ✗ Averaging identical models trained on the same data without variation does not improve performance.  
C) ✗ Using a single complex model does not constitute ensemble learning.  
D) ✓ Incrementally focusing on training instances misclassified by previous models (boosting).  

**Correct:** A, D