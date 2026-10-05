## 2. Neural Networks

## Key Points

#### 1. 🤖 Neural Networks Overview  
- Neural networks are inspired by the biological brain and aim to replicate high-level cognitive functions such as learning and problem-solving.  
- Neural networks are practical and used in real-world applications like deepfakes, AlphaGo, and GPT-3.  
- Neural networks learn by approximation and generalization from examples, not by explicit programming.

#### 2. 🧠 Biological Neurons  
- The brain contains about 10 billion interconnected neurons.  
- Neurons communicate via synapses, where electrical charges (positive or negative) are transmitted.  
- Neurons sum incoming signals through spatial and temporal summation to decide whether to fire.

#### 3. ⚙️ Artificial Neurons  
- An artificial neuron receives multiple inputs, each with an associated weight.  
- The neuron computes a weighted sum of inputs plus a bias term (affine transformation).  
- The weighted sum is passed through an activation function to produce the output.  
- Neurons are arranged in layers to form neural networks.

#### 4. 🔄 Activation Functions  
- Activation functions introduce non-linearity, essential for neural networks to model complex patterns.  
- Common activation functions include:  
  - Linear (identity) function  
  - Hard limit (sign) function  
  - Sigmoid function (outputs between 0 and 1)  
  - Tanh function (outputs between -1 and 1)  
  - ReLU (Rectified Linear Unit) function (outputs zero for negative inputs, linear for positive)  
  - Hard Tanh function (clamps output between -1 and 1)

#### 5. 🧩 Perceptron Model  
- The perceptron is a single-layer neural network with a linear combiner followed by a hard limiter activation function.  
- It outputs +1 if the weighted sum is ≥ 0, otherwise -1.  
- The bias can be represented as an input with a constant value of 1 and an adjustable weight.

#### 6. 🔄 Perceptron Learning Algorithm  
- Initialize weights to zero.  
- For each training input, compute output and compare with desired output.  
- Update weights using the rule:  

$$
  w_{new} = w_{old} + \eta (d - y) x
$$
  
  where $\eta$ is the learning rate, $d$ is desired output, $y$ is actual output, and $x$ is input.  
- Repeat until the perceptron correctly classifies all training examples or converges.

#### 7. 🛑 Limitations of the Perceptron  
- The perceptron can learn linearly separable functions such as AND and OR.  
- The perceptron **cannot** learn the XOR function because XOR is not linearly separable.  
- This limitation requires more complex networks (multi-layer perceptrons) to solve.



<br>

