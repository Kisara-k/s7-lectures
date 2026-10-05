## 6. Deep Learning

## Questions

#### 1. Which of the following statements correctly describe the limitations of conventional (traditional) machine learning compared to deep learning?  
A) Conventional ML models automatically learn hierarchical feature representations from raw data.  
B) Designing handcrafted features is usually tedious and costly in conventional ML.  
C) Conventional ML relies on manually designed features which are often application-specific and hard to transfer.  
D) Deep learning requires less data than conventional ML to achieve good performance.  

#### 2. In the context of deep learning, what does the term "deep" primarily refer to?  
A) The use of multiple layers that learn hierarchical feature representations.  
B) The number of neurons in a single hidden layer.  
C) The ability to learn features with increasing levels of abstraction automatically.  
D) The depth of the input data, such as color channels in images.  

#### 3. Which of the following are true about convolutional neural networks (CNNs)?  
A) CNNs are robust to spatial translations of objects in images.  
B) Filters in CNNs are manually designed and fixed during training.  
C) CNNs use local receptive fields and shared weights to reduce the number of parameters.  
D) CNNs require fully connected layers at every stage to extract features.  

#### 4. Regarding the training of deep neural networks, which statements about loss functions and optimizers are correct?  
A) Binary cross-entropy is suitable for two-class classification problems.  
B) The loss function is the only metric that matters during training.  
C) RMSProp is a popular optimizer choice due to its adaptive learning rate properties.  
D) Mean squared error is commonly used for multi-class classification tasks.  

#### 5. Why are residual networks (ResNets) important in deep learning?  
A) They are primarily used to reduce the number of parameters in shallow networks.  
B) They introduce skip connections that help mitigate the vanishing gradient problem.  
C) They allow training of very deep networks with over 1,000 layers.  
D) They eliminate the need for convolutional layers in deep networks.  

#### 6. Which of the following correctly describe the characteristics and challenges of recurrent neural networks (RNNs)?  
A) RNNs are prone to the vanishing gradient problem, especially when learning long-term dependencies.  
B) RNNs assume independence among training examples, similar to CNNs.  
C) RNNs process sequential data by maintaining a hidden state that captures information from previous time steps.  
D) RNNs use different weights at each time step to better model sequences.  

#### 7. What are the key gating mechanisms in Long Short-Term Memory (LSTM) networks, and what are their functions?  
A) Reset gate: resets the entire memory cell at each time step.  
B) Output gate: controls which information from the memory cell is passed to the output.  
C) Forget gate: decides what information to discard from the memory cell.  
D) Input gate: controls which new information enters the memory cell.  

#### 8. In the context of hyper-parameter tuning for neural networks, which of the following statements are accurate?  
A) Bayesian optimization is a fully solved problem with no active research ongoing.  
B) Grid search exhaustively checks all parameter combinations within a specified range.  
C) Random search is often preferred over grid search because it can explore the parameter space more efficiently.  
D) Common hyper-parameters include learning rate, number of layers, and dropout rate.  

#### 9. Which of the following statements about autoencoders are true?  
A) Autoencoders learn to reconstruct their input at the output layer.  
B) The encoder compresses the input into a lower-dimensional representation.  
C) Autoencoders are primarily used for supervised classification tasks.  
D) Adding noise to the input during training can help the autoencoder learn more robust features.  

#### 10. Consider the following statements about bidirectional RNNs (BRNNs). Which are correct?  
A) BRNNs process sequences in both forward and backward directions to capture past and future context.  
B) BRNNs are useful when the output depends on both previous and future elements in the sequence.  
C) BRNNs are equivalent to stacking two independent RNNs without interaction.  
D) BRNNs eliminate the vanishing gradient problem inherent in standard RNNs.  



<br>

## Answers

#### 1. Which of the following statements correctly describe the limitations of conventional (traditional) machine learning compared to deep learning?  
A) ✗ Conventional ML does not automatically learn hierarchical features; this is a key advantage of deep learning.  
B) ✓ Designing handcrafted features is usually tedious and costly in conventional ML.  
C) ✓ Conventional ML relies on manually designed features which are often application-specific and hard to transfer.  
D) ✗ Deep learning generally requires more data, not less, than conventional ML to perform well.  

**Correct:** B, C


#### 2. In the context of deep learning, what does the term "deep" primarily refer to?  
A) ✓ "Deep" refers to multiple layers learning hierarchical features.  
B) ✗ Number of neurons in a single layer does not define "deep"; depth refers to number of layers.  
C) ✓ Deep learning automatically learns features with increasing abstraction through layers.  
D) ✗ Depth of input data (e.g., color channels) is unrelated to the term "deep" in deep learning.  

**Correct:** A, C


#### 3. Which of the following are true about convolutional neural networks (CNNs)?  
A) ✓ CNNs are robust to spatial translations due to convolution and pooling.  
B) ✗ Filters are learned during training, not manually designed or fixed.  
C) ✓ CNNs use local receptive fields and shared weights to reduce parameters.  
D) ✗ Fully connected layers are used only at the end, not at every stage.  

**Correct:** A, C


#### 4. Regarding the training of deep neural networks, which statements about loss functions and optimizers are correct?  
A) ✓ Binary cross-entropy is suitable for two-class classification.  
B) ✗ Other metrics (e.g., accuracy) also matter, though loss is the main optimization target.  
C) ✓ RMSProp is a popular optimizer due to adaptive learning rate and good performance.  
D) ✗ Mean squared error is typically used for regression, not multi-class classification.  

**Correct:** A, C


#### 5. Why are residual networks (ResNets) important in deep learning?  
A) ✗ ResNets are designed for deep, not shallow, networks and do not primarily reduce parameters.  
B) ✓ Skip connections help mitigate vanishing gradients.  
C) ✓ ResNets enable training very deep networks (1000+ layers).  
D) ✗ ResNets do not eliminate convolutional layers; they build on them.  

**Correct:** B, C


#### 6. Which of the following correctly describe the characteristics and challenges of recurrent neural networks (RNNs)?  
A) ✓ RNNs suffer from vanishing gradients, especially for long-term dependencies.  
B) ✗ RNNs do not assume independence among examples; they explicitly model sequence dependence.  
C) ✓ RNNs maintain hidden states to capture sequential dependencies.  
D) ✗ RNNs use the same weights across all time steps to generalize across sequences.  

**Correct:** A, C


#### 7. What are the key gating mechanisms in Long Short-Term Memory (LSTM) networks, and what are their functions?  
A) ✗ Reset gate is not part of LSTM; it is used in GRUs.  
B) ✓ Output gate controls what information leaves the memory cell to output.  
C) ✓ Forget gate controls what information is discarded from the memory cell.  
D) ✓ Input gate controls what new information enters the memory cell.  

**Correct:** B, C, D


#### 8. In the context of hyper-parameter tuning for neural networks, which of the following statements are accurate?  
A) ✗ Bayesian optimization is an active research area, not a fully solved problem.  
B) ✓ Grid search exhaustively checks all parameter combinations in a range.  
C) ✓ Random search can be more efficient than grid search in exploring parameter space.  
D) ✓ Common hyper-parameters include learning rate, layers, and dropout rate.  

**Correct:** B, C, D


#### 9. Which of the following statements about autoencoders are true?  
A) ✓ Autoencoders learn to reconstruct their input at the output layer.  
B) ✓ The encoder compresses input into a lower-dimensional representation (latent space).  
C) ✗ Autoencoders are unsupervised and not primarily used for supervised classification.  
D) ✓ Adding noise during training (denoising autoencoder) helps learn robust features.  

**Correct:** A, B, D


#### 10. Consider the following statements about bidirectional RNNs (BRNNs). Which are correct?  
A) ✓ BRNNs process sequences forward and backward to capture full context.  
B) ✓ BRNNs are useful when output depends on both past and future elements.  
C) ✗ BRNNs are two RNNs combined, but their outputs interact to produce final results.  
D) ✗ BRNNs do not solve the vanishing gradient problem; they only improve context modeling.  

**Correct:** A, B