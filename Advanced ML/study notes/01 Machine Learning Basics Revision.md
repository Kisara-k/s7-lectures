## 1. Machine Learning Basics Revision

## Study Notes

### 1. 🤖 What is Machine Learning? An Introduction

Machine Learning (ML) is a fascinating field that enables computers to learn from data and improve their performance on tasks without being explicitly programmed for every detail. At its core, ML is about **learning from experience** — just like humans do. Herbert Simon, a pioneer in this field, defined learning as any process by which a system improves its performance from experience.

#### Why Machine Learning?

- **Human intelligence comes from experience.** We don’t explicitly program every behavior; instead, we learn from examples and adapt.
- **Designing explicit rules for complex tasks is hard or impossible.** For many problems, we don’t fully understand the underlying process or it’s too complex to model precisely.
- **Data-driven approaches can outperform traditional “white box” models.** Sometimes, treating the system as a “black box” and letting data guide the learning leads to better results.
- **Machine learning is essential when:**
  - Human expertise is unavailable (e.g., navigating Mars).
  - Humans can’t explain their expertise (e.g., speech recognition).
  - Solutions change over time (e.g., network routing).
  - Solutions need to be personalized (e.g., personalized medicine).
  - There is a huge amount of data (e.g., genomics).

#### What is Machine Learning?

- ML is about **building models** that approximate the relationship between inputs and outputs based on data.
- It involves **searching through a space of hypotheses** (possible models) to find the best fit for the training data.
- Alan Turing’s question “Can machines think?” evolved into “Can machines do what we can do?” — ML is a step toward answering that.
- Arthur Samuel (1959) described ML as a program that improves with experience.
- Tom Mitchell formalized it: A program learns from experience E with respect to tasks T and performance measure P if its performance improves with experience.

#### Machine Learning vs Traditional Programming

- Traditional programming: You write a program that processes input data to produce output.
- Machine learning: You provide data and output examples, and the computer learns the program (model) that maps inputs to outputs.


### 2. 📊 The Role of Data and Knowledge in Machine Learning

Machine learning thrives on **data** — which is cheap and abundant — while **knowledge** (human expertise) is expensive and scarce. ML algorithms balance between:

- **Prior knowledge (human assumptions, model structure).**
- **Empirical evidence (data samples).**

Different ML approaches place different emphasis on these two ends of the spectrum.

#### The Role of Statistics and Computer Science

- **Statistics** helps infer patterns from samples and provides mathematical rigor.
- **Computer science** provides efficient algorithms to optimize models and handle large data.
- ML aims to **automate automation** — letting computers program themselves by learning from data.


### 3. 🧩 Types of Machine Learning

Machine learning can be broadly categorized based on the type of data and feedback available during training:

#### Supervised Learning

- Training data includes **input-output pairs** (labeled data).
- The goal is to learn a function that maps inputs to outputs.
- Tasks:
  - **Classification:** Predict discrete labels (e.g., spam or not spam).
  - **Regression:** Predict continuous values (e.g., house prices).

#### Unsupervised Learning

- Training data has **no labels**.
- The goal is to find hidden structure or patterns in the data.
- Tasks:
  - **Clustering:** Group similar data points.
  - **Association:** Find relationships between features (e.g., market basket analysis).
  - **Dimensionality reduction:** Simplify data while preserving structure.

#### Semi-Supervised Learning

- Uses a small amount of labeled data combined with a large amount of unlabeled data.
- Useful when labeling is expensive or time-consuming.

#### Reinforcement Learning

- Learns by interacting with an environment.
- Receives **rewards** based on actions taken.
- Goal: Learn a policy to maximize cumulative rewards.
- Examples: Game playing, robot navigation.


### 4. 🛠️ The Learning Process and Tasks

#### Defining the Learning Task

Every ML problem involves:

- **Task (T):** What you want the system to do (e.g., classify emails as spam).
- **Performance measure (P):** How you measure success (e.g., accuracy).
- **Experience (E):** The data or interactions the system learns from.

#### Example: Spam Filtering

- Task: Identify spam emails.
- Performance: Percentage of spam correctly filtered and legitimate emails not incorrectly filtered.
- Experience: A database of emails labeled by users.

#### Training and Testing

- **Training:** The system learns from labeled examples.
- **Testing:** The system’s performance is evaluated on unseen data.
- Important assumption: Training and testing data come from the same distribution (i.i.d. assumption).


### 5. 🔍 Statistical Inference in Machine Learning

Machine learning involves different types of reasoning:

- **Inductive learning:** Generalizing from specific examples to a general rule.
- **Deductive learning:** Applying known rules to draw conclusions.
- **Transductive learning:** Making predictions directly on specific examples without generalizing a function (e.g., k-nearest neighbors).


### 6. 🧠 Supervised Learning in Detail

#### Classification

- Predicting discrete categories.
- Examples:
  - Medical diagnosis (disease or no disease).
  - Face recognition.
  - Credit scoring (low-risk vs high-risk).
- Can be:
  - **Binary classification:** Two classes.
  - **Multi-class classification:** More than two classes.
  - **Multi-label classification:** Each example can have multiple labels.

#### Regression

- Predicting continuous values.
- Example: Predicting the price of a used car based on its features.
- Useful for tasks like steering angle prediction in autonomous driving.


### 7. 🔎 Unsupervised Learning in Detail

#### Clustering

- Grouping data points into clusters based on similarity.
- No labels are provided.
- Applications:
  - Customer segmentation.
  - Image compression.
  - Bioinformatics (finding motifs).

#### Association Learning

- Discovering rules like “people who buy X also buy Y.”
- Example: Market basket analysis.


### 8. 🎯 Reinforcement Learning

- The agent interacts with an environment in discrete time steps.
- At each step, it observes a state, takes an action, receives a reward, and transitions to a new state.
- The goal is to learn a policy that maximizes the expected sum of future rewards.
- Challenges:
  - Rewards are often delayed.
  - Feedback is sparse and scalar.
- Applications: Robotics, game playing, autonomous control.


### 9. 🧩 Advanced Learning Paradigms

#### Transfer Learning

- Reusing a model trained on one task/domain to help learn another.
- Useful when labeled data is scarce in the target domain.

#### Active Learning

- The learner can query an oracle (e.g., a human) for labels on selected examples.
- Helps reduce labeling effort by focusing on the most informative examples.

#### Ensemble Learning

- Combines multiple models to improve performance.
- Example: Boosting, where models focus on correcting errors of previous models.
- Inspired by the “wisdom of crowds” — combining diverse opinions often yields better decisions.


### 10. ⚙️ Designing a Learning System

Key steps in building an ML system:

1. **Choose the training experience:** What data and feedback will the system learn from?
2. **Define the target function:** What exactly should the system learn to predict or do?
3. **Select a representation:** How will the function be represented? (e.g., neural networks, decision trees)
4. **Choose a learning algorithm:** How will the system search for the best function?
5. **Evaluate and test:** Measure performance on unseen data to ensure generalization.


### 11. 📈 Model Evaluation and Optimization

#### Evaluation Metrics

- **Confusion matrix:** Counts of true positives, false positives, true negatives, false negatives.
- **Accuracy:** Overall correctness.
- **Precision:** Correct positive predictions out of all positive predictions.
- **Recall:** Correct positive predictions out of all actual positives.
- **Other metrics:** Squared error, likelihood, entropy, etc.

#### Optimization Algorithms

- Algorithms search for the best model parameters.
- Examples:
  - Gradient descent (used in neural networks).
  - Greedy search (used in decision trees).
  - Genetic algorithms (evolutionary computation).
  - Dynamic programming (used in Hidden Markov Models).


### 12. ⚠️ Challenges in Machine Learning

#### Overfitting and Underfitting

- **Underfitting:** Model too simple, performs poorly on training and test data.
- **Overfitting:** Model too complex, fits training data too well but performs poorly on new data.
- Balance is key for good generalization.

#### Curse of Dimensionality

- High-dimensional data requires exponentially more samples to learn effectively.
- Dimensionality reduction techniques help but must be applied carefully to avoid losing important information.

#### Rashomon Effect

- Multiple models can explain the data equally well but differ significantly.
- This reflects the subjectivity and uncertainty in model selection.

#### No Free Lunch Theorem

- No single learning algorithm is best for all problems.
- Success depends on matching the algorithm to the problem and data characteristics.
- Prior knowledge and assumptions are essential.


### 13. 🧩 Summary: Machine Learning in a Nutshell

- ML is about learning from data to improve performance on tasks.
- It involves representation, evaluation, and optimization.
- There are many algorithms and approaches, each suited to different problems.
- Understanding the domain, data, and goals is crucial.
- ML systems must be carefully designed, trained, and evaluated to generalize well.