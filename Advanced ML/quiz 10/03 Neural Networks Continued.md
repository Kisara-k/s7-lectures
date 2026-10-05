## 3. Neural Networks Continued

## Questions

#### 1. Which of the following statements about the perceptron and its limitations are true?  
A) Adding a hidden layer can make the XOR problem linearly separable in a higher-dimensional space.  
B) A simple perceptron can represent any logical function including XOR.  
C) Different weight initializations do not affect the perceptron’s ability to learn the XOR function.  
D) The perceptron convergence algorithm guarantees convergence only for linearly separable data.  

#### 2. In multilayer neural networks, why can’t the same learning algorithm used for a single-layer perceptron be applied directly?  
A) Because the training algorithm for single-layer perceptrons does not converge for multilayer networks.  
B) Because multilayer networks are nonlinear systems.  
C) Because multilayer networks require backpropagation to compute gradients.  
D) Because multilayer networks do not use activation functions.  

#### 3. Regarding gradient descent in neural network training, which of the following are correct?  
A) A very large learning rate can cause the algorithm to diverge.  
B) A small learning rate always guarantees faster convergence.  
C) The gradient points in the direction of the steepest increase of the error function.  
D) Adjusting weights in the direction opposite to the gradient reduces the error.  

#### 4. What challenges arise when propagating error signals backward through a multilayer neural network?  
A) The chain rule of calculus is used to compute gradients for weight updates.  
B) Hidden layers do not affect the overall error, so backpropagation is unnecessary.  
C) The “blame” for errors must be distributed among hidden neurons without explicit target outputs.  
D) It is straightforward to assign a desired response to hidden layer neurons.  

#### 5. Which of the following statements about loss functions and activation functions in neural networks are true?  
A) Hinge loss is primarily used in regression problems.  
B) Squared loss is commonly paired with linear activation for real-valued outputs.  
C) The choice of loss function depends on the nature of the output and the application.  
D) Cross-entropy loss is typically used with softmax activation for categorical outputs.  

#### 6. Overfitting in neural networks can be mitigated by which of the following methods?  
A) Early stopping based on validation set performance.  
B) Regularization techniques that penalize large weights.  
C) Increasing the number of parameters without constraints.  
D) Using dropout to randomly deactivate neurons during training.  

#### 7. Which of the following are true regarding the vanishing and exploding gradient problems?  
A) Batch normalization and adaptive learning rates can help stabilize training.  
B) Sigmoid activation functions often cause vanishing gradients due to their small derivatives.  
C) ReLU activation helps mitigate the vanishing gradient problem.  
D) Exploding gradients result in negligible weight updates in early layers.  

#### 8. Consider stochastic gradient descent (SGD) and mini-batch gradient descent. Which statements are correct?  
A) Using a batch size of one is equivalent to mini-batch gradient descent.  
B) Mini-batch gradient descent balances efficiency and gradient variance.  
C) Mini-batches can help the optimizer escape shallow local minima.  
D) SGD updates weights after computing gradients over the entire dataset.  

#### 9. Regarding regularization in neural networks, which of the following are accurate?  
A) Large weights correspond to simpler functions with lower variance.  
B) L2 regularization penalizes the sum of absolute values of weights.  
C) L1 regularization tends to produce sparse weight vectors by encouraging zeros.  
D) Regularization helps control the bias-variance tradeoff by constraining model complexity.  

#### 10. Momentum in gradient descent is used to:  
A) Replace the need for learning rate tuning entirely.  
B) Help the optimizer escape local minima by maintaining velocity.  
C) Incorporate a fraction of the previous weight update to smooth the optimization path.  
D) Increase the learning rate exponentially during training.  



<br>

## Answers

#### 1. Which of the following statements about the perceptron and its limitations are true?  
A) ✓ Adding a hidden layer transforms XOR into a linearly separable problem in higher dimensions.  
B) ✗ A simple perceptron cannot represent non-linearly separable functions like XOR.  
C) ✗ Weight initialization affects learning; poor initialization can hinder training.  
D) ✓ The perceptron convergence algorithm only guarantees convergence for linearly separable data.  

**Correct:** A, D


#### 2. In multilayer neural networks, why can’t the same learning algorithm used for a single-layer perceptron be applied directly?  
A) ✓ The perceptron algorithm does not converge for nonlinear multilayer networks.  
B) ✓ Multilayer networks are nonlinear, unlike single-layer perceptrons.  
C) ✓ Backpropagation is required to compute gradients in multilayer networks.  
D) ✗ Multilayer networks do use activation functions; this is not a reason.  

**Correct:** A, B, C


#### 3. Regarding gradient descent in neural network training, which of the following are correct?  
A) ✓ A very large learning rate can cause divergence and instability.  
B) ✗ A small learning rate leads to slow convergence, not faster.  
C) ✗ The gradient points in the direction of steepest increase, so we move opposite to it.  
D) ✓ Adjusting weights opposite to the gradient reduces error.  

**Correct:** A, D


#### 4. What challenges arise when propagating error signals backward through a multilayer neural network?  
A) ✓ The chain rule is essential for computing gradients during backpropagation.  
B) ✗ Hidden layers affect overall error; backpropagation is necessary.  
C) ✓ The error must be distributed (“blamed”) among hidden neurons without explicit targets.  
D) ✗ It is not straightforward to assign desired responses to hidden neurons.  

**Correct:** A, C


#### 5. Which of the following statements about loss functions and activation functions in neural networks are true?  
A) ✗ Hinge loss is mainly used in classification (e.g., SVM), not regression.  
B) ✓ Squared loss is typically used with linear activation for real-valued outputs.  
C) ✓ Loss function choice depends on output type and application.  
D) ✓ Cross-entropy loss is commonly paired with softmax for categorical outputs.  

**Correct:** B, C, D


#### 6. Overfitting in neural networks can be mitigated by which of the following methods?  
A) ✓ Early stopping based on validation error helps prevent overfitting.  
B) ✓ Regularization penalizes large weights, reducing overfitting.  
C) ✗ Increasing parameters without constraints usually worsens overfitting.  
D) ✓ Dropout randomly deactivates neurons, improving generalization.  

**Correct:** A, B, D


#### 7. Which of the following are true regarding the vanishing and exploding gradient problems?  
A) ✓ Batch normalization and adaptive learning rates help stabilize training.  
B) ✓ Sigmoid’s small derivatives cause vanishing gradients.  
C) ✓ ReLU helps mitigate vanishing gradients by having derivative 1 for positive inputs.  
D) ✗ Exploding gradients cause excessively large updates, not negligible ones.  

**Correct:** A, B, C


#### 8. Consider stochastic gradient descent (SGD) and mini-batch gradient descent. Which statements are correct?  
A) ✓ Batch size of one is equivalent to SGD (a special case of mini-batch).  
B) ✓ Mini-batch gradient descent balances efficiency and gradient variance.  
C) ✓ Mini-batches can help escape shallow local minima due to noise in gradients.  
D) ✗ SGD updates weights after each example, not after the entire dataset.  

**Correct:** A, B, C


#### 9. Regarding regularization in neural networks, which of the following are accurate?  
A) ✗ Large weights correspond to complex functions with high variance, not simpler ones.  
B) ✗ L2 regularization penalizes the sum of squared weights, not absolute values.  
C) ✓ L1 regularization encourages sparsity by pushing weights toward zero.  
D) ✓ Regularization controls bias-variance tradeoff by limiting model complexity.  

**Correct:** C, D


#### 10. Momentum in gradient descent is used to:  
A) ✗ Momentum does not eliminate the need for learning rate tuning.  
B) ✓ Momentum helps escape local minima by maintaining velocity.  
C) ✓ Momentum incorporates previous updates to smooth optimization trajectory.  
D) ✗ Momentum does not increase learning rate exponentially.  

**Correct:** B, C