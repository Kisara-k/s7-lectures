## 2. Neural Networks

## Study Notes

### 1. 🤖 Introduction to Neural Networks

Neural networks are a fascinating area of artificial intelligence that mimic how the human brain works to solve complex problems. To understand why neural networks are important, consider this: Have you ever seen images or videos that look incredibly real but are actually completely fake? For example, the website [thispersondoesnotexist.com](https://thispersondoesnotexist.com/) generates realistic human faces that do not belong to any real person. Similarly, deepfake videos can make it appear as if famous people like Barack Obama are saying things they never actually said (see [Obama deepfake](https://www.youtube.com/watch?v=cQ54GDm1eL0)).

These examples show that neural networks are no longer just theoretical ideas—they are practical tools used in real-world applications, from creating realistic images and videos to mastering complex games like AlphaGo by DeepMind, and even powering advanced language models like GPT-3.

But this power comes with challenges. For instance, can a computer recognize a famous person like Einstein from various pictures? What defines Einstein’s face? Why is it so hard for a computer to do what humans do effortlessly? The answer lies in how our brains approximate, learn, and generalize from incomplete or noisy information—abilities that neural networks try to replicate.


### 2. 🧠 Biological vs Artificial Neurons

#### Biological Neurons

Our brains contain about 10 billion neurons, which are specialized cells that receive, process, and transmit information. Each neuron connects to thousands of others through tiny gaps called synapses. When a neuron fires, it sends electrical signals (positive or negative charges) to connected neurons. These signals are combined through processes called spatial and temporal summation, which determine whether the receiving neuron will fire next.

#### Artificial Neurons

Artificial neurons are simplified models inspired by biological neurons. Each artificial neuron:

- Receives multiple inputs, each with an associated weight that adjusts the input’s importance.
- Adds these weighted inputs together.
- Passes the sum through an **activation function** to produce an output.

Neurons are organized into layers, and many neurons connected together form a **neural network**. The goal is to build machines that can perform high-level brain functions like learning and problem-solving, even though the machines themselves only perform simple calculations.


### 3. ⚙️ How Artificial Neural Networks Work

Artificial Neural Networks (ANNs) learn from data by adjusting the weights of connections between neurons. This learning can be:

- **Supervised** (learning from labeled examples),
- **Unsupervised** (finding patterns in unlabeled data).

Key properties of ANNs include:

- **Adaptivity:** They change connection strengths to improve performance.
- **Non-linearity:** Activation functions introduce non-linear behavior, allowing networks to model complex relationships.
- **Fault tolerance:** Even if some neurons or connections fail, the network can still function well.

These features make ANNs especially useful for problems where data is high-dimensional, noisy, or incomplete, and where traditional algorithms struggle.


### 4. 🧮 The Artificial Neuron in Detail

Mathematically, an artificial neuron computes:

- A **linear combination** of inputs:  

$$
  u_k = \sum_{i} w_i x_i
$$

  where $w_i$ are weights and $x_i$ are inputs.

- Then adds a **bias** term $b_k$ to get the **induced local field** (activation potential):  

$$
  v_k = u_k + b_k
$$


The bias acts like an extra input with a constant value of 1, allowing the neuron to shift the activation function and thus be more flexible.

Finally, the neuron applies an **activation function** $\phi(v_k)$ to produce the output.


### 5. 🔄 Activation Functions: The Heart of Neural Networks

The activation function determines the output of a neuron based on its input. Choosing the right activation function is crucial because it affects the network’s ability to learn and represent complex patterns.

#### Types of Activation Functions:

- **Linear (Identity) Function:**  
  Output is directly proportional to input. Limited because it can only model linear relationships.

- **Hard Limit (Sign) Function:**  
  Outputs +1 or -1 depending on whether input is above or below zero. Used in simple models like the perceptron.

- **Sigmoid Function:**  
  Smoothly maps input to a value between 0 and 1. Useful for probabilistic outputs.

- **Tanh Function:**  
  Similar to sigmoid but outputs between -1 and 1, centered at zero, which often helps learning.

- **ReLU (Rectified Linear Unit):**  
  Outputs zero if input is negative, otherwise outputs input directly. Popular in modern deep networks because it helps with faster learning and reduces some problems like vanishing gradients.

- **Hard Tanh:**  
  Clamps output between -1 and 1, combining linear and threshold behavior.

Each function has its pros and cons, and the choice depends on the specific problem and network architecture.


### 6. 🧩 The Perceptron: The Simplest Neural Network

The perceptron is the most basic type of neural network, consisting of a single neuron with a linear combiner followed by a hard limiter (sign function). It produces an output of +1 if the weighted sum of inputs is above a threshold, otherwise -1.

#### How the Perceptron Learns:

- Start with initial weights (often zero).
- For each training example, compute the output.
- Compare the output to the desired response.
- Adjust the weights based on the error (difference between actual and desired output).
- Repeat until the perceptron correctly classifies all training examples or reaches a stopping point.

This process is called the **Perceptron Learning Algorithm** or **Convergence Algorithm**.


### 7. 🔄 Perceptron Learning Algorithm: Step-by-Step

1. **Initialization:** Set all weights to zero.
2. **Input Application:** Present an input vector to the perceptron.
3. **Output Calculation:** Compute the weighted sum and apply the activation function.
4. **Error Calculation:** Find the difference between desired and actual output.
5. **Weight Update:** Adjust weights to reduce error using the formula:  

$$
   w_{new} = w_{old} + \eta (d - y) x
$$

   where $\eta$ is the learning rate, $d$ is desired output, $y$ is actual output, and $x$ is input.
6. **Repeat:** Continue with the next input vector until convergence.

#### Example: Learning the AND Gate

- Inputs: pairs of binary values (0 or 1).
- Desired output: 1 only if both inputs are 1, else -1.
- The perceptron adjusts weights over several iterations until it correctly models the AND function.


### 8. 🛑 Limitations of the Perceptron

While the perceptron can learn simple functions like AND and OR, it **cannot learn the XOR function** because XOR is not linearly separable. This means no single straight line (or hyperplane) can separate the XOR outputs correctly.

This limitation highlights the need for more complex networks with multiple layers (multi-layer perceptrons) and non-linear activation functions, which will be covered in future lessons.


### Summary

Neural networks are inspired by the brain’s neurons and aim to replicate high-level cognitive functions like learning and pattern recognition. Artificial neurons combine weighted inputs, add a bias, and apply an activation function to produce outputs. The perceptron is the simplest neural network that can learn linearly separable functions through an iterative weight adjustment process. However, it has limitations, such as failing to learn XOR, motivating the development of deeper, more complex networks.