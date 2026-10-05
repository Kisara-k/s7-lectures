## 3. Neural Networks Continued

## Questions

#### 1. Which of the following statements about the perceptron and its limitations are true?  
A) A simple perceptron can represent any logical function including XOR.  
B) The perceptron convergence algorithm guarantees convergence only for linearly separable data.  
C) Adding a hidden layer can make the XOR problem linearly separable in a higher-dimensional space.  
D) Different weight initializations do not affect the perceptron’s ability to learn the XOR function.

#### 2. In multilayer neural networks, why can’t the same learning algorithm used for a single-layer perceptron be applied directly?  
A) Because multilayer networks are nonlinear systems.  
B) Because the training algorithm for single-layer perceptrons does not converge for multilayer networks.  
C) Because multilayer networks do not use activation functions.  
D) Because multilayer networks require backpropagation to compute gradients.

#### 3. Regarding gradient descent in neural network training, which of the following are correct?  
A) A very large learning rate can cause the algorithm to diverge.  
B) A small learning rate always guarantees faster convergence.  
C) The gradient points in the direction of the steepest increase of the error function.  
D) Adjusting weights in the direction opposite to the gradient reduces the error.

#### 4. What challenges arise when propagating error signals backward through a multilayer neural network?  
A) It is straightforward to assign a desired response to hidden layer neurons.  
B) The “blame” for errors must be distributed among hidden neurons without explicit target outputs.  
C) The chain rule of calculus is used to compute gradients for weight updates.  
D) Hidden layers do not affect the overall error, so backpropagation is unnecessary.

#### 5. Which of the following statements about loss functions and activation functions in neural networks are true?  
A) Cross-entropy loss is typically used with softmax activation for categorical outputs.  
B) Squared loss is commonly paired with linear activation for real-valued outputs.  
C) Hinge loss is primarily used in regression problems.  
D) The choice of loss function depends on the nature of the output and the application.

#### 6. Overfitting in neural networks can be mitigated by which of the following methods?  
A) Increasing the number of parameters without constraints.  
B) Early stopping based on validation set performance.  
C) Regularization techniques that penalize large weights.  
D) Using dropout to randomly deactivate neurons during training.

#### 7. Which of the following are true regarding the vanishing and exploding gradient problems?  
A) Sigmoid activation functions often cause vanishing gradients due to their small derivatives.  
B) Exploding gradients result in negligible weight updates in early layers.  
C) ReLU activation helps mitigate the vanishing gradient problem.  
D) Batch normalization and adaptive learning rates can help stabilize training.

#### 8. Consider stochastic gradient descent (SGD) and mini-batch gradient descent. Which statements are correct?  
A) SGD updates weights after computing gradients over the entire dataset.  
B) Mini-batch gradient descent balances efficiency and gradient variance.  
C) Mini-batches can help the optimizer escape shallow local minima.  
D) Using a batch size of one is equivalent to mini-batch gradient descent.

#### 9. Regarding regularization in neural networks, which of the following are accurate?  
A) L2 regularization penalizes the sum of absolute values of weights.  
B) L1 regularization tends to produce sparse weight vectors by encouraging zeros.  
C) Regularization helps control the bias-variance tradeoff by constraining model complexity.  
D) Large weights correspond to simpler functions with lower variance.

#### 10. Momentum in gradient descent is used to:  
A) Increase the learning rate exponentially during training.  
B) Incorporate a fraction of the previous weight update to smooth the optimization path.  
C) Help the optimizer escape local minima by maintaining velocity.  
D) Replace the need for learning rate tuning entirely.



<br>

## Answers

#### 1. Which of the following statements about the perceptron and its limitations are true?  
A) ✗ A simple perceptron cannot represent non-linearly separable functions like XOR.  
B) ✓ The perceptron convergence algorithm only guarantees convergence for linearly separable data.  
C) ✓ Adding a hidden layer transforms XOR into a linearly separable problem in higher dimensions.  
D) ✗ Weight initialization affects learning; poor initialization can hinder training.

**Correct:** B, C


#### 2. In multilayer neural networks, why can’t the same learning algorithm used for a single-layer perceptron be applied directly?  
A) ✓ Multilayer networks are nonlinear, unlike single-layer perceptrons.  
B) ✓ The perceptron algorithm does not converge for nonlinear multilayer networks.  
C) ✗ Multilayer networks do use activation functions; this is not a reason.  
D) ✓ Backpropagation is required to compute gradients in multilayer networks.

**Correct:** A, B, D


#### 3. Regarding gradient descent in neural network training, which of the following are correct?  
A) ✓ A very large learning rate can cause divergence and instability.  
B) ✗ A small learning rate leads to slow convergence, not faster.  
C) ✗ The gradient points in the direction of steepest increase, so we move opposite to it.  
D) ✓ Adjusting weights opposite to the gradient reduces error.

**Correct:** A, D


#### 4. What challenges arise when propagating error signals backward through a multilayer neural network?  
A) ✗ It is not straightforward to assign desired responses to hidden neurons.  
B) ✓ The error must be distributed (“blamed”) among hidden neurons without explicit targets.  
C) ✓ The chain rule is essential for computing gradients during backpropagation.  
D) ✗ Hidden layers affect overall error; backpropagation is necessary.

**Correct:** B, C


#### 5. Which of the following statements about loss functions and activation functions in neural networks are true?  
A) ✓ Cross-entropy loss is commonly paired with softmax for categorical outputs.  
B) ✓ Squared loss is typically used with linear activation for real-valued outputs.  
C) ✗ Hinge loss is mainly used in classification (e.g., SVM), not regression.  
D) ✓ Loss function choice depends on output type and application.

**Correct:** A, B, D


#### 6. Overfitting in neural networks can be mitigated by which of the following methods?  
A) ✗ Increasing parameters without constraints usually worsens overfitting.  
B) ✓ Early stopping based on validation error helps prevent overfitting.  
C) ✓ Regularization penalizes large weights, reducing overfitting.  
D) ✓ Dropout randomly deactivates neurons, improving generalization.

**Correct:** B, C, D


#### 7. Which of the following are true regarding the vanishing and exploding gradient problems?  
A) ✓ Sigmoid’s small derivatives cause vanishing gradients.  
B) ✗ Exploding gradients cause excessively large updates, not negligible ones.  
C) ✓ ReLU helps mitigate vanishing gradients by having derivative 1 for positive inputs.  
D) ✓ Batch normalization and adaptive learning rates help stabilize training.

**Correct:** A, C, D


#### 8. Consider stochastic gradient descent (SGD) and mini-batch gradient descent. Which statements are correct?  
A) ✗ SGD updates weights after each example, not after the entire dataset.  
B) ✓ Mini-batch gradient descent balances efficiency and gradient variance.  
C) ✓ Mini-batches can help escape shallow local minima due to noise in gradients.  
D) ✓ Batch size of one is equivalent to SGD (a special case of mini-batch).

**Correct:** B, C, D


#### 9. Regarding regularization in neural networks, which of the following are accurate?  
A) ✗ L2 regularization penalizes the sum of squared weights, not absolute values.  
B) ✓ L1 regularization encourages sparsity by pushing weights toward zero.  
C) ✓ Regularization controls bias-variance tradeoff by limiting model complexity.  
D) ✗ Large weights correspond to complex functions with high variance, not simpler ones.

**Correct:** B, C


#### 10. Momentum in gradient descent is used to:  
A) ✗ Momentum does not increase learning rate exponentially.  
B) ✓ Momentum incorporates previous updates to smooth optimization trajectory.  
C) ✓ Momentum helps escape local minima by maintaining velocity.  
D) ✗ Momentum does not eliminate the need for learning rate tuning.

**Correct:** B, C