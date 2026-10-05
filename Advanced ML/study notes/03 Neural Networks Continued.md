## 3. Neural Networks Continued

## Study Notes

### 1. 🧠 Neural Networks Recap and Motivation

Neural networks (NNs) are powerful computational models inspired by the human brain’s structure. They have become state-of-the-art tools in many applications such as image recognition, natural language processing, and autonomous driving. This lecture continues from last week’s introduction, where we covered the basics of perceptrons and simple logical functions like AND, OR, and XOR.

#### Biological Inspiration
Artificial neurons are inspired by biological neurons. In the brain, neurons receive signals, process them, and pass on outputs. Similarly, artificial neurons take inputs, apply weights, sum them, and pass the result through an activation function to produce an output.

#### Perceptron Recap
- **Perceptron**: The simplest neural network unit, which computes a weighted sum of inputs and applies a threshold function to decide the output.
- **Convergence Algorithm**: A method to adjust weights iteratively to minimize classification errors.
- **Limitations**: While perceptrons can solve linearly separable problems like AND and OR, they fail with non-linearly separable problems like XOR.


### 2. ❌ The XOR Problem and Hidden Layers

The XOR (exclusive OR) function outputs true only when inputs differ. Unlike AND or OR, XOR is not linearly separable, meaning a single perceptron cannot learn it.

#### Why XOR is Hard for a Single Perceptron
A perceptron draws a straight line (decision boundary) to separate classes. XOR requires a more complex boundary that a single line cannot provide.

#### Solution: Add a Hidden Layer
By introducing a hidden layer, the network gains an extra dimension to transform the input space, making XOR separable. This means the network can now learn XOR by combining multiple linear boundaries.

- **Hidden Layer**: Intermediate layer(s) between input and output layers where neurons perform computations not directly visible to the user.
- **Multi-layer Networks**: These networks are more powerful because they can represent complex functions by stacking layers.

#### Important Note
The simple perceptron learning algorithm does not work here because the system is no longer linear, and the training algorithm does not converge with the old method.


### 3. 🔄 Multilayer Neural Networks and Training

#### Structure
- **Input Layer**: Receives raw data.
- **Hidden Layers**: Perform intermediate computations.
- **Output Layer**: Produces the final prediction.

#### Signal Propagation
- **Forward Propagation**: Input signals move forward through the network to produce outputs.
- **Backward Propagation (Backpropagation)**: Error signals move backward to update weights.

#### The “Blame Game”
In multilayer networks, it’s unclear how to assign error responsibility to hidden neurons because we don’t have direct target outputs for them. Backpropagation solves this by calculating gradients of the loss function with respect to each weight using the chain rule.


### 4. 📉 Gradient Descent and Backpropagation

#### Gradient Descent
- The goal is to minimize the error (loss) by adjusting weights.
- The error is a function of weights.
- We compute the gradient (direction of steepest increase) and move weights in the opposite direction to reduce error.
- The learning rate (η) controls the step size:
  - Too small → slow learning.
  - Too large → unstable, oscillations, or divergence.

#### Backpropagation Algorithm
- **Forward phase**: Compute output and loss.
- **Backward phase**: Compute gradients of loss w.r.t weights using the chain rule.
- Update weights accordingly.

This method allows training of deep networks with multiple hidden layers.


### 5. 🎯 Loss Functions and Output Layers

#### Loss Functions
Loss functions measure how well the network’s predictions match the true labels. Choosing the right loss function depends on the task:

- **Cross-Entropy Loss**: Common for classification tasks, especially with softmax output.
- **Squared Loss**: Used for regression tasks.
- **Hinge Loss**: Used in Support Vector Machines (SVMs).

#### Softmax Layer
For multi-class classification, the softmax function converts raw output scores into probabilities that sum to 1, making it easier to interpret and optimize with cross-entropy loss.


### 6. ⚠️ Practical Issues in Training Neural Networks

#### Overfitting
- Occurs when the model fits training data too closely but performs poorly on unseen data.
- Happens especially with complex models and small datasets.

#### Mitigating Overfitting
- **Regularization**: Penalizes large weights to encourage simpler models.
- **Early Stopping**: Stop training when performance on a validation set starts to degrade.
- **Dropout**: Randomly “drops” neurons during training to prevent co-adaptation.
- **Parameter Sharing and Architecture Design**: Use domain knowledge to design efficient networks (e.g., convolutional layers for images).

#### Vanishing and Exploding Gradients
- In deep networks, gradients can become very small (vanish) or very large (explode) during backpropagation.
- Vanishing gradients slow down or stop learning in early layers.
- Exploding gradients cause unstable updates.
- Solutions include using ReLU activation, batch normalization, and adaptive learning rates.

#### Learning Rate and Convergence
- Learning rate must be carefully chosen.
- Too high causes instability.
- Too low causes slow convergence.
- Momentum helps by smoothing updates and escaping local minima.

#### Local Optima
- Neural networks have complex loss surfaces with many local minima.
- Stochastic gradient descent and momentum help avoid getting stuck in poor local minima.

#### Computational Challenges
- Training deep networks can be very time-consuming, often requiring powerful hardware and days or weeks of training.


### 7. 🔄 Stochastic Gradient Descent and Mini-Batching

#### Gradient Descent Variants
- **Batch Gradient Descent**: Uses all training data to compute gradients before updating weights.
- **Stochastic Gradient Descent (SGD)**: Updates weights after each training example, faster but noisier.
- **Mini-batch Gradient Descent**: Compromise using small batches, balancing speed and stability.

#### Epochs and Iterations
- **Iteration**: One update step using a mini-batch.
- **Epoch**: One full pass through the entire training dataset.

Mini-batching is efficient and helps the model escape shallow minima due to noise in gradient estimates.


### 8. 🛡️ Regularization Techniques in Detail

#### Why Regularize?
Regularization helps prevent overfitting by encouraging simpler models that generalize better.

#### Small Weights and Occam’s Razor
- Large weights cause the model to be sensitive to small input changes, increasing variance and overfitting.
- Small weights lead to smoother, simpler functions.

#### Types of Regularization
- **L2 Regularization (Ridge)**: Penalizes the sum of squared weights. Encourages small but non-zero weights.
- **L1 Regularization (Lasso)**: Penalizes the sum of absolute weights. Encourages sparsity (many weights become zero), useful for noisy or irrelevant features.

#### Choosing Between L1 and L2
- L2 is generally better for most classification problems.
- L1 is better when many features are irrelevant or noisy.


### 9. 🚀 Advanced Training Techniques: Momentum and Dropout

#### Momentum
- Momentum adds a fraction of the previous weight update to the current update.
- Helps accelerate learning in consistent gradient directions.
- Helps avoid getting stuck in local minima.
- Typical momentum values range from 0.1 to 0.99, often around 0.9.

#### Dropout
- During training, randomly “drop” neurons with probability π.
- Prevents neurons from co-adapting too much.
- Acts like training an ensemble of many smaller networks.
- Reduces overfitting and improves generalization.


### 10. 🔧 Summary and Next Steps

This lecture covered the transition from simple perceptrons to multilayer neural networks, explaining why hidden layers are necessary for complex problems like XOR. We explored how gradient descent and backpropagation enable training of deep networks, and discussed practical challenges such as overfitting, vanishing gradients, and computational costs.

Understanding these fundamentals prepares you to implement and train neural networks effectively. The next step is to practice building multilayer perceptrons (MLPs) and experiment with different architectures and training techniques.


**Additional Resources:**

- For detailed derivations of backpropagation and LMS algorithms, refer to supplementary materials.
- Try the provided MLP implementation notebook: [MLP Implementation on Colab](https://colab.research.google.com/drive/1rtlWcZIoJ5vzNMdcg8ORfUqm0L32kKUD?usp=sharing)