## 1. Machine Learning Basics Revision

## Key Points

#### 1. 🤖 Definition of Machine Learning  
- Learning is any process by which a system improves performance from experience (Herbert Simon).  
- A computer program learns from experience E with respect to tasks T and performance measure P if its performance improves with experience (Tom M. Mitchell).  
- Machine learning is programming computers to optimize a performance criterion using example data or past experience.  

#### 2. 📊 When to Use Machine Learning  
- ML is used when human expertise does not exist or cannot be explained.  
- ML is needed when solutions change over time or require customization.  
- ML is suitable when models are based on huge amounts of data.  

#### 3. 🧠 Types of Learning  
- Supervised learning uses labeled data (input-output pairs).  
- Unsupervised learning uses unlabeled data to find hidden structure.  
- Semi-supervised learning uses a few labeled examples with many unlabeled examples.  
- Reinforcement learning learns from rewards based on sequences of actions without supervised output.  

#### 4. 🧩 Supervised Learning Tasks  
- Classification predicts discrete labels (e.g., spam or not spam).  
- Regression predicts continuous values (e.g., price prediction).  
- Multi-class classification involves more than two classes.  
- Multi-label classification assigns multiple labels to one example.  

#### 5. 🔍 Unsupervised Learning Tasks  
- Clustering groups data points into subsets based on similarity without labels.  
- Association learning finds probabilistic relationships between features (e.g., market basket analysis).  

#### 6. 🎯 Reinforcement Learning  
- The agent observes state s_t, takes action a_t, receives reward r_{t+1}, and transitions to state s_{t+1}.  
- The goal is to learn a policy mapping states to actions to maximize expected future rewards.  
- Rewards are often delayed and scalar, making learning difficult.  

#### 7. 🧩 Learning Paradigms  
- Transfer learning reuses a model trained on one domain/task for another.  
- Active learning allows the learner to query an oracle for labels on selected examples.  
- Ensemble learning combines multiple models to improve predictive performance.  

#### 8. ⚙️ Designing a Learning System  
- Choose training experience, target function, representation, and learning algorithm.  
- Training and testing data are assumed to be independently and identically distributed (i.i.d.).  

#### 9. 📈 Evaluation Metrics  
- Confusion matrix components: True Positive, False Positive, True Negative, False Negative.  
- Precision = TP / (TP + FP).  
- Recall = TP / (TP + FN).  
- Accuracy measures overall correctness.  

#### 10. ⚠️ Overfitting and Underfitting  
- Underfitting occurs when the model is too simple, causing high training and test errors.  
- Overfitting occurs when the model fits training data too well but performs poorly on test data.  

#### 11. 📉 Curse of Dimensionality  
- High-dimensional feature spaces require exponentially more training data to cover all value combinations.  
- Dimensionality reduction can preserve structure but may distort data if applied naively.  

#### 12. 🌀 Rashomon Effect  
- Multiple classifiers can achieve similar error rates but differ significantly in structure.  
- Small changes in training data can lead to very different models with similar performance.  

#### 13. 🚫 No Free Lunch Theorem  
- No learning algorithm is universally superior across all problems.  
- Performance depends on alignment between algorithm assumptions and problem characteristics.  
- Prior knowledge is essential to select the appropriate algorithm for a task.  

#### 14. 🧮 Common ML Model Representations  
- Numerical functions: Linear regression, neural networks, support vector machines.  
- Symbolic functions: Decision trees, propositional and first-order logic rules.  
- Instance-based functions: Nearest neighbor, case-based reasoning.  
- Probabilistic graphical models: Naïve Bayes, Bayesian networks, Hidden Markov Models.  

#### 15. 🔄 Optimization Algorithms in ML  
- Gradient descent is used in perceptron and backpropagation.  
- Greedy search is used in decision tree induction.  
- Dynamic programming is used in HMM and PCFG learning.  
- Evolutionary computation includes genetic algorithms and genetic programming.



<br>

