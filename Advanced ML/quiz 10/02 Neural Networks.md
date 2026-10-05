## 2. Neural Networks

## Questions

#### 1. What are some key characteristics of biological neurons that artificial neurons attempt to mimic?  
A) Receiving and transmitting information through synapses  
B) Processing inputs with associated weights and summing them  
C) Spatial and temporal summation of incoming signals  
D) Using a hard threshold function to produce binary outputs  

#### 2. Why is it difficult for a computer to recognize a person like Einstein based solely on images?  
A) Because computers cannot approximate or learn from examples  
B) Because defining what exactly constitutes "Einstein" is complex and ambiguous  
C) Because computers lack the ability to recall memory based on context rather than content  
D) Because computers can only solve well-posed problems with clear mathematical solutions  

#### 3. Which of the following are advantages of artificial neural networks compared to classical algorithmic solutions?  
A) Fault tolerance to damaged neurons or connections  
B) Ability to handle high-dimensional, noisy, or imprecise data  
C) Guaranteed convergence to the global optimum in all cases  
D) Adaptivity through changing connection strengths during learning  

#### 4. In the mathematical model of an artificial neuron, what role does the bias term play?  
A) It acts as an additional input with a fixed value to increase model flexibility  
B) It limits the output range of the neuron through the activation function  
C) It shifts the activation potential to allow the neuron to activate even when inputs are zero  
D) It replaces the need for weights on the inputs  

#### 5. Which of the following statements about activation functions are true?  
A) Non-linear activation functions are essential for neural networks to learn complex patterns  
B) Linear activation functions can model any non-linear relationship given enough neurons  
C) The sigmoid and tanh functions approximate threshold functions as their parameters increase  
D) ReLU activation outputs zero for all negative inputs and is widely used in modern networks  

#### 6. Regarding the perceptron learning algorithm, which of the following are correct?  
A) The perceptron updates weights based on the error between desired and actual output  
B) The learning rate parameter controls the magnitude of weight updates and must be between 0 and 1  
C) The perceptron can solve any classification problem, including XOR  
D) The algorithm guarantees convergence if a solution exists that perfectly separates the classes  

#### 7. What is the significance of the decision hyperplane in the perceptron model?  
A) It represents the boundary that separates different classes in the input space  
B) It is always a linear boundary defined by the weighted sum of inputs and bias  
C) It can represent non-linear decision boundaries by adjusting weights and biases  
D) It is used to visualize the regions where the perceptron outputs 1 or -1  

#### 8. Which of the following are limitations of the simple perceptron?  
A) It cannot represent functions that are not linearly separable, such as XOR  
B) It requires non-linear activation functions to converge  
C) It cannot learn from unlabelled data  
D) It cannot adapt weights once initialized  

#### 9. How do biological brains differ from artificial neural networks in handling "high-level functions"?  
A) Biological brains can solve ill-posed problems without explicit algorithms  
B) Biological brains rely heavily on exact accuracy and thresholds for decision making  
C) Biological brains recall memories based on context rather than exact content  
D) Artificial neural networks currently match biological brains in solving incomplete problems  

#### 10. Which of the following statements about learning in artificial neural networks are true?  
A) Learning involves changing connection strengths based on examples  
B) Both labelled and unlabelled data can be used for training  
C) Neural networks require explicit programming of all rules to function correctly  
D) Non-linearity in activation functions enables networks to approximate complex mappings



<br>

## Answers

#### 1. What are some key characteristics of biological neurons that artificial neurons attempt to mimic?  
A) ✓ Biological neurons receive and transmit information through synapses, which artificial neurons model as weighted connections.  
B) ✓ Artificial neurons process inputs with associated weights and sum them, mimicking biological signal integration.  
C) ✓ Spatial and temporal summation of signals is a key biological process that artificial neurons approximate by summing weighted inputs.  
D) ✗ Hard threshold functions are a simplification used in artificial neurons, but biological neurons do not operate strictly with binary outputs.  

**Correct:** A, B, C


#### 2. Why is it difficult for a computer to recognize a person like Einstein based solely on images?  
A) ✗ Computers can approximate and learn from examples; this is the basis of neural networks.  
B) ✓ Defining "Einstein" is complex because it involves abstract features and context, not just pixel data.  
C) ✓ Computers typically recall based on exact content, whereas humans use context, making recognition harder for machines.  
D) ✓ Computers struggle with ill-posed problems lacking clear mathematical solutions, such as recognizing faces under varied conditions.  

**Correct:** B, C, D


#### 3. Which of the following are advantages of artificial neural networks compared to classical algorithmic solutions?  
A) ✓ Neural networks are fault tolerant; damage to some neurons/connections does not break the whole system.  
B) ✓ They handle high-dimensional, noisy, and imprecise data better than classical methods.  
C) ✗ Neural networks do not guarantee convergence to a global optimum in all cases; they may get stuck in local minima.  
D) ✓ Adaptivity through weight changes during learning is a core advantage of neural networks.  

**Correct:** A, B, D


#### 4. In the mathematical model of an artificial neuron, what role does the bias term play?  
A) ✓ The bias acts as an additional input with a fixed value (usually 1), increasing the neuron's flexibility.  
B) ✗ The activation function limits output range, but the bias itself does not limit output; it shifts the activation potential.  
C) ✓ The bias shifts the activation potential, allowing activation even if weighted inputs sum to zero.  
D) ✗ The bias complements weights; it does not replace them.  

**Correct:** A, C


#### 5. Which of the following statements about activation functions are true?  
A) ✓ Non-linear activation functions are essential for neural networks to learn complex, non-linear patterns.  
B) ✗ Linear activation functions cannot model non-linear relationships regardless of network size.  
C) ✓ Sigmoid and tanh functions approximate threshold functions as their steepness parameter increases.  
D) ✓ ReLU outputs zero for negative inputs and is widely used due to its simplicity and effectiveness.  

**Correct:** A, C, D


#### 6. Regarding the perceptron learning algorithm, which of the following are correct?  
A) ✓ The perceptron updates weights based on the error between desired and actual output.  
B) ✓ The learning rate controls the size of weight updates and must be between 0 and 1 for stability.  
C) ✗ The perceptron cannot solve non-linearly separable problems like XOR.  
D) ✓ The algorithm guarantees convergence if a perfect linear separator exists.  

**Correct:** A, B, D


#### 7. What is the significance of the decision hyperplane in the perceptron model?  
A) ✓ It represents the boundary separating different classes in input space.  
B) ✓ It is always a linear boundary defined by weighted inputs and bias.  
C) ✗ The perceptron cannot represent non-linear boundaries; it is limited to linear separability.  
D) ✓ It visualizes regions where the perceptron outputs 1 or -1.  

**Correct:** A, B, D


#### 8. Which of the following are limitations of the simple perceptron?  
A) ✓ It cannot represent non-linearly separable functions like XOR.  
B) ✗ The perceptron uses a hard limiter (sign function), not non-linear activation functions like sigmoid or ReLU.  
C) ✗ The perceptron is a supervised learning algorithm and requires labelled data, but this is not a limitation per se.  
D) ✗ The perceptron adapts weights continuously during training; it does not keep them fixed.  

**Correct:** A


#### 9. How do biological brains differ from artificial neural networks in handling "high-level functions"?  
A) ✓ Biological brains can solve ill-posed problems without explicit algorithms.  
B) ✗ Biological brains often tolerate inaccuracy and do not rely heavily on strict thresholds.  
C) ✓ Biological brains recall memories based on context rather than exact content, unlike most artificial systems.  
D) ✗ Artificial neural networks do not yet match biological brains in solving incomplete or ill-posed problems effortlessly.  

**Correct:** A, C


#### 10. Which of the following statements about learning in artificial neural networks are true?  
A) ✓ Learning involves adjusting connection strengths (weights) based on examples.  
B) ✓ Both labelled (supervised) and unlabelled (unsupervised) data can be used for training neural networks.  
C) ✗ Neural networks do not require explicit programming of all rules; they learn patterns from data.  
D) ✓ Non-linearity in activation functions enables networks to approximate complex mappings beyond linear functions.  

**Correct:** A, B, D