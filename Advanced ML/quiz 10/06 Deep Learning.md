## 6. Deep Learning

## Questions

#### 1. Which of the following statements correctly describe the limitations of conventional (traditional) machine learning compared to deep learning?  
A) Conventional ML relies on manually designed features which are often application-specific and hard to transfer.  
B) Conventional ML models automatically learn hierarchical feature representations from raw data.  
C) Designing handcrafted features is usually tedious and costly in conventional ML.  
D) Deep learning requires less data than conventional ML to achieve good performance.

#### 2. In the context of deep learning, what does the term "deep" primarily refer to?  
A) The use of multiple layers that learn hierarchical feature representations.  
B) The depth of the input data, such as color channels in images.  
C) The number of neurons in a single hidden layer.  
D) The ability to learn features with increasing levels of abstraction automatically.

#### 3. Which of the following are true about convolutional neural networks (CNNs)?  
A) CNNs use local receptive fields and shared weights to reduce the number of parameters.  
B) CNNs are robust to spatial translations of objects in images.  
C) CNNs require fully connected layers at every stage to extract features.  
D) Filters in CNNs are manually designed and fixed during training.

#### 4. Regarding the training of deep neural networks, which statements about loss functions and optimizers are correct?  
A) Mean squared error is commonly used for multi-class classification tasks.  
B) Binary cross-entropy is suitable for two-class classification problems.  
C) RMSProp is a popular optimizer choice due to its adaptive learning rate properties.  
D) The loss function is the only metric that matters during training.

#### 5. Why are residual networks (ResNets) important in deep learning?  
A) They introduce skip connections that help mitigate the vanishing gradient problem.  
B) They allow training of very deep networks with over 1,000 layers.  
C) They eliminate the need for convolutional layers in deep networks.  
D) They are primarily used to reduce the number of parameters in shallow networks.

#### 6. Which of the following correctly describe the characteristics and challenges of recurrent neural networks (RNNs)?  
A) RNNs process sequential data by maintaining a hidden state that captures information from previous time steps.  
B) RNNs assume independence among training examples, similar to CNNs.  
C) RNNs are prone to the vanishing gradient problem, especially when learning long-term dependencies.  
D) RNNs use different weights at each time step to better model sequences.

#### 7. What are the key gating mechanisms in Long Short-Term Memory (LSTM) networks, and what are their functions?  
A) Input gate: controls which new information enters the memory cell.  
B) Output gate: controls which information from the memory cell is passed to the output.  
C) Forget gate: decides what information to discard from the memory cell.  
D) Reset gate: resets the entire memory cell at each time step.

#### 8. In the context of hyper-parameter tuning for neural networks, which of the following statements are accurate?  
A) Grid search exhaustively checks all parameter combinations within a specified range.  
B) Random search is often preferred over grid search because it can explore the parameter space more efficiently.  
C) Bayesian optimization is a fully solved problem with no active research ongoing.  
D) Common hyper-parameters include learning rate, number of layers, and dropout rate.

#### 9. Which of the following statements about autoencoders are true?  
A) Autoencoders learn to reconstruct their input at the output layer.  
B) The encoder compresses the input into a lower-dimensional representation.  
C) Adding noise to the input during training can help the autoencoder learn more robust features.  
D) Autoencoders are primarily used for supervised classification tasks.

#### 10. Consider the following statements about bidirectional RNNs (BRNNs). Which are correct?  
A) BRNNs process sequences in both forward and backward directions to capture past and future context.  
B) BRNNs are equivalent to stacking two independent RNNs without interaction.  
C) BRNNs are useful when the output depends on both previous and future elements in the sequence.  
D) BRNNs eliminate the vanishing gradient problem inherent in standard RNNs.



<br>

## Answers

#### 1. Which of the following statements correctly describe the limitations of conventional (traditional) machine learning compared to deep learning?  
A) ✓ Conventional ML relies on manually designed features which are often application-specific and hard to transfer.  
B) ✗ Conventional ML does not automatically learn hierarchical features; this is a key advantage of deep learning.  
C) ✓ Designing handcrafted features is usually tedious and costly in conventional ML.  
D) ✗ Deep learning generally requires more data, not less, than conventional ML to perform well.

**Correct:** A, C


#### 2. In the context of deep learning, what does the term "deep" primarily refer to?  
A) ✓ "Deep" refers to multiple layers learning hierarchical features.  
B) ✗ Depth of input data (e.g., color channels) is unrelated to the term "deep" in deep learning.  
C) ✗ Number of neurons in a single layer does not define "deep"; depth refers to number of layers.  
D) ✓ Deep learning automatically learns features with increasing abstraction through layers.

**Correct:** A, D


#### 3. Which of the following are true about convolutional neural networks (CNNs)?  
A) ✓ CNNs use local receptive fields and shared weights to reduce parameters.  
B) ✓ CNNs are robust to spatial translations due to convolution and pooling.  
C) ✗ Fully connected layers are used only at the end, not at every stage.  
D) ✗ Filters are learned during training, not manually designed or fixed.

**Correct:** A, B


#### 4. Regarding the training of deep neural networks, which statements about loss functions and optimizers are correct?  
A) ✗ Mean squared error is typically used for regression, not multi-class classification.  
B) ✓ Binary cross-entropy is suitable for two-class classification.  
C) ✓ RMSProp is a popular optimizer due to adaptive learning rate and good performance.  
D) ✗ Other metrics (e.g., accuracy) also matter, though loss is the main optimization target.

**Correct:** B, C


#### 5. Why are residual networks (ResNets) important in deep learning?  
A) ✓ Skip connections help mitigate vanishing gradients.  
B) ✓ ResNets enable training very deep networks (1000+ layers).  
C) ✗ ResNets do not eliminate convolutional layers; they build on them.  
D) ✗ ResNets are designed for deep, not shallow, networks and do not primarily reduce parameters.

**Correct:** A, B


#### 6. Which of the following correctly describe the characteristics and challenges of recurrent neural networks (RNNs)?  
A) ✓ RNNs maintain hidden states to capture sequential dependencies.  
B) ✗ RNNs do not assume independence among examples; they explicitly model sequence dependence.  
C) ✓ RNNs suffer from vanishing gradients, especially for long-term dependencies.  
D) ✗ RNNs use the same weights across all time steps to generalize across sequences.

**Correct:** A, C


#### 7. What are the key gating mechanisms in Long Short-Term Memory (LSTM) networks, and what are their functions?  
A) ✓ Input gate controls what new information enters the memory cell.  
B) ✓ Output gate controls what information leaves the memory cell to output.  
C) ✓ Forget gate controls what information is discarded from the memory cell.  
D) ✗ Reset gate is not part of LSTM; it is used in GRUs.

**Correct:** A, B, C


#### 8. In the context of hyper-parameter tuning for neural networks, which of the following statements are accurate?  
A) ✓ Grid search exhaustively checks all parameter combinations in a range.  
B) ✓ Random search can be more efficient than grid search in exploring parameter space.  
C) ✗ Bayesian optimization is an active research area, not a fully solved problem.  
D) ✓ Common hyper-parameters include learning rate, layers, and dropout rate.

**Correct:** A, B, D


#### 9. Which of the following statements about autoencoders are true?  
A) ✓ Autoencoders learn to reconstruct their input at the output layer.  
B) ✓ The encoder compresses input into a lower-dimensional representation (latent space).  
C) ✓ Adding noise during training (denoising autoencoder) helps learn robust features.  
D) ✗ Autoencoders are unsupervised and not primarily used for supervised classification.

**Correct:** A, B, C


#### 10. Consider the following statements about bidirectional RNNs (BRNNs). Which are correct?  
A) ✓ BRNNs process sequences forward and backward to capture full context.  
B) ✗ BRNNs are two RNNs combined, but their outputs interact to produce final results.  
C) ✓ BRNNs are useful when output depends on both past and future elements.  
D) ✗ BRNNs do not solve the vanishing gradient problem; they only improve context modeling.

**Correct:** A, C