## 3. Neural Networks Continued

## Key Points

#### 1. 🧠 Perceptron and XOR Problem  
- A simple perceptron can represent linearly separable functions like AND and OR but **cannot represent the XOR function**.  
- Adding a **hidden layer** makes the XOR problem linearly separable in a higher-dimensional space.  
- The original perceptron learning algorithm **does not converge** for multilayer networks because the system becomes nonlinear.

#### 2. 🔄 Multilayer Neural Networks Structure  
- Multilayer neural networks have **input, hidden, and output layers**.  
- Hidden layers perform intermediate computations not directly visible to the user.  
- Signal propagation involves **forward propagation** of inputs and **backward propagation** of errors.

#### 3. 📉 Gradient Descent and Backpropagation  
- Gradient descent updates weights by moving in the direction of the **steepest decrease of error**.  
- The **learning rate (η)** controls the step size; too large causes instability, too small causes slow learning.  
- Backpropagation uses the **chain rule** to compute gradients of the loss function with respect to weights in all layers.  
- Backpropagation has two phases: **forward phase** (compute output and loss) and **backward phase** (compute gradients and update weights).

#### 4. 🎯 Loss Functions and Output Layers  
- **Cross-entropy loss** is commonly used with softmax activation for classification tasks.  
- **Squared loss** is commonly used for regression tasks with linear activation.  
- The choice of loss function depends on the application and output type.

#### 5. ⚠️ Overfitting and Regularization  
- Overfitting occurs when a model fits training data well but performs poorly on unseen data.  
- Regularization penalizes large weights to encourage simpler models and reduce overfitting.  
- **L2 regularization** penalizes the sum of squared weights; **L1 regularization** penalizes the sum of absolute weights and encourages sparsity.  
- Early stopping halts training when validation error starts to increase.  
- Dropout randomly sets weights to zero during training to reduce overfitting.

#### 6. ⚡ Vanishing and Exploding Gradients  
- Deep networks suffer from **vanishing gradients** (very small updates in early layers) or **exploding gradients** (very large updates).  
- Sigmoid activation functions often cause vanishing gradients due to derivatives less than 0.25.  
- ReLU activation and techniques like batch normalization help mitigate these problems.

#### 7. 🚀 Momentum and Learning Rate  
- Momentum incorporates a fraction of the previous weight update to smooth and accelerate learning.  
- Typical momentum values range from 0.1 to 0.99, often around 0.9.  
- Learning rate values commonly used are 0.1, 0.01, or 0.001.

#### 8. 🔄 Stochastic Gradient Descent (SGD) and Mini-batching  
- SGD updates weights after each training example, making it faster but noisier than batch gradient descent.  
- Mini-batch gradient descent uses small batches to balance efficiency and gradient stability.  
- One **epoch** is a full pass over the entire training dataset; one **iteration** is one update step using a mini-batch.

#### 9. 🖥️ Computational Challenges  
- Training deep neural networks can require **weeks of computation** on large datasets.  
- Efficient training requires careful choice of architecture, learning rate, and optimization techniques.



<br>

