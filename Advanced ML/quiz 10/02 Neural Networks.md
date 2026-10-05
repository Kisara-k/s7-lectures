## 2. Neural Networks

## Questions

#### 1. What are some key characteristics of biological neurons that artificial neurons attempt to mimic?  
A) Receiving and transmitting information through synapses  
B) Processing inputs with associated weights and summing them  
C) Using a hard threshold function to produce binary outputs  
D) Spatial and temporal summation of incoming signals  

#### 2. Why is it difficult for a computer to recognize a person like Einstein based solely on images?  
A) Because computers cannot approximate or learn from examples  
B) Because computers lack the ability to recall memory based on context rather than content  
C) Because computers can only solve well-posed problems with clear mathematical solutions  
D) Because defining what exactly constitutes "Einstein" is complex and ambiguous  

#### 3. Which of the following are advantages of artificial neural networks compared to classical algorithmic solutions?  
A) Ability to handle high-dimensional, noisy, or imprecise data  
B) Guaranteed convergence to the global optimum in all cases  
C) Fault tolerance to damaged neurons or connections  
D) Adaptivity through changing connection strengths during learning  

#### 4. In the mathematical model of an artificial neuron, what role does the bias term play?  
A) It replaces the need for weights on the inputs  
B) It acts as an additional input with a fixed value to increase model flexibility  
C) It shifts the activation potential to allow the neuron to activate even when inputs are zero  
D) It limits the output range of the neuron through the activation function  

#### 5. Which of the following statements about activation functions are true?  
A) ReLU activation outputs zero for all negative inputs and is widely used in modern networks  
B) The sigmoid and tanh functions approximate threshold functions as their parameters increase  
C) Linear activation functions can model any non-linear relationship given enough neurons  
D) Non-linear activation functions are essential for neural networks to learn complex patterns  

#### 6. Regarding the perceptron learning algorithm, which of the following are correct?  
A) The learning rate parameter controls the magnitude of weight updates and must be between 0 and 1  
B) The perceptron updates weights based on the error between desired and actual output  
C) The algorithm guarantees convergence if a solution exists that perfectly separates the classes  
D) The perceptron can solve any classification problem, including XOR  

#### 7. What is the significance of the decision hyperplane in the perceptron model?  
A) It can represent non-linear decision boundaries by adjusting weights and biases  
B) It is used to visualize the regions where the perceptron outputs 1 or -1  
C) It represents the boundary that separates different classes in the input space  
D) It is always a linear boundary defined by the weighted sum of inputs and bias  

#### 8. Which of the following are limitations of the simple perceptron?  
A) It cannot learn from unlabelled data  
B) It cannot adapt weights once initialized  
C) It requires non-linear activation functions to converge  
D) It cannot represent functions that are not linearly separable, such as XOR  

#### 9. How do biological brains differ from artificial neural networks in handling "high-level functions"?  
A) Biological brains rely heavily on exact accuracy and thresholds for decision making  
B) Biological brains recall memories based on context rather than exact content  
C) Artificial neural networks currently match biological brains in solving incomplete problems  
D) Biological brains can solve ill-posed problems without explicit algorithms  

#### 10. Which of the following statements about learning in artificial neural networks are true?  
A) Learning involves changing connection strengths based on examples  
B) Non-linearity in activation functions enables networks to approximate complex mappings  
C) Both labelled and unlabelled data can be used for training  
D) Neural networks require explicit programming of all rules to function correctly  



<br>

## Answers

#### 1. What are some key characteristics of biological neurons that artificial neurons attempt to mimic?  
A) ✓ Biological neurons receive and transmit information through synapses, which artificial neurons model as weighted connections.  
B) ✓ Artificial neurons process inputs with associated weights and sum them, mimicking biological signal integration.  
C) ✗ Hard threshold functions are a simplification used in artificial neurons, but biological neurons do not operate strictly with binary outputs.  
D) ✓ Spatial and temporal summation of signals is a key biological process that artificial neurons approximate by summing weighted inputs.  

**Correct:** A, B, D


#### 2. Why is it difficult for a computer to recognize a person like Einstein based solely on images?  
A) ✗ Computers can approximate and learn from examples; this is the basis of neural networks.  
B) ✓ Computers typically recall based on exact content, whereas humans use context, making recognition harder for machines.  
C) ✓ Computers struggle with ill-posed problems lacking clear mathematical solutions, such as recognizing faces under varied conditions.  
D) ✓ Defining "Einstein" is complex because it involves abstract features and context, not just pixel data.  

**Correct:** B, C, D


#### 3. Which of the following are advantages of artificial neural networks compared to classical algorithmic solutions?  
A) ✓ They handle high-dimensional, noisy, and imprecise data better than classical methods.  
B) ✗ Neural networks do not guarantee convergence to a global optimum in all cases; they may get stuck in local minima.  
C) ✓ Neural networks are fault tolerant; damage to some neurons/connections does not break the whole system.  
D) ✓ Adaptivity through weight changes during learning is a core advantage of neural networks.  

**Correct:** A, C, D


#### 4. In the mathematical model of an artificial neuron, what role does the bias term play?  
A) ✗ The bias complements weights; it does not replace them.  
B) ✓ The bias acts as an additional input with a fixed value (usually 1), increasing the neuron's flexibility.  
C) ✓ The bias shifts the activation potential, allowing activation even if weighted inputs sum to zero.  
D) ✗ The activation function limits output range, but the bias itself does not limit output; it shifts the activation potential.  

**Correct:** B, C


#### 5. Which of the following statements about activation functions are true?  
A) ✓ ReLU outputs zero for negative inputs and is widely used due to its simplicity and effectiveness.  
B) ✓ Sigmoid and tanh functions approximate threshold functions as their steepness parameter increases.  
C) ✗ Linear activation functions cannot model non-linear relationships regardless of network size.  
D) ✓ Non-linear activation functions are essential for neural networks to learn complex, non-linear patterns.  

**Correct:** A, B, D


#### 6. Regarding the perceptron learning algorithm, which of the following are correct?  
A) ✓ The learning rate controls the size of weight updates and must be between 0 and 1 for stability.  
B) ✓ The perceptron updates weights based on the error between desired and actual output.  
C) ✓ The algorithm guarantees convergence if a perfect linear separator exists.  
D) ✗ The perceptron cannot solve non-linearly separable problems like XOR.  

**Correct:** A, B, C


#### 7. What is the significance of the decision hyperplane in the perceptron model?  
A) ✗ The perceptron cannot represent non-linear boundaries; it is limited to linear separability.  
B) ✓ It visualizes regions where the perceptron outputs 1 or -1.  
C) ✓ It represents the boundary separating different classes in input space.  
D) ✓ It is always a linear boundary defined by weighted inputs and bias.  

**Correct:** B, C, D


#### 8. Which of the following are limitations of the simple perceptron?  
A) ✗ The perceptron is a supervised learning algorithm and requires labelled data, but this is not a limitation per se.  
B) ✗ The perceptron adapts weights continuously during training; it does not keep them fixed.  
C) ✗ The perceptron uses a hard limiter (sign function), not non-linear activation functions like sigmoid or ReLU.  
D) ✓ It cannot represent non-linearly separable functions like XOR.  

**Correct:** D


#### 9. How do biological brains differ from artificial neural networks in handling "high-level functions"?  
A) ✗ Biological brains often tolerate inaccuracy and do not rely heavily on strict thresholds.  
B) ✓ Biological brains recall memories based on context rather than exact content, unlike most artificial systems.  
C) ✗ Artificial neural networks do not yet match biological brains in solving incomplete or ill-posed problems effortlessly.  
D) ✓ Biological brains can solve ill-posed problems without explicit algorithms.  

**Correct:** B, D


#### 10. Which of the following statements about learning in artificial neural networks are true?  
A) ✓ Learning involves adjusting connection strengths (weights) based on examples.  
B) ✓ Non-linearity in activation functions enables networks to approximate complex mappings beyond linear functions.  
C) ✓ Both labelled (supervised) and unlabelled (unsupervised) data can be used for training neural networks.  
D) ✗ Neural networks do not require explicit programming of all rules; they learn patterns from data.  

**Correct:** A, B, C