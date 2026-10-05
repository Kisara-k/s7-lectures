## 6. Deep Learning

## Study Notes

### 1. 🤖 What is Deep Learning? An Overview

Deep Learning (DL) is a powerful subset of machine learning (ML) focused on learning data representations automatically through multiple layers of processing. Unlike traditional machine learning, which depends heavily on human-designed features, deep learning models learn hierarchical features directly from raw data. This means the system can discover complex patterns by itself, given enough data and computational power.

The term **"deep"** refers to the many layers in the model architecture, which allow the system to build increasingly abstract representations of the input data. For example, in image recognition, the model might first detect edges, then textures, then parts of objects, and finally whole objects. Similarly, in language, it might learn characters, words, phrases, and sentences in a layered fashion.

#### Why is Deep Learning Important?

- **Automated Feature Learning:** DL removes the need for tedious, manual feature engineering, which is often application-specific and time-consuming.
- **Flexibility:** It can be applied to various types of data — images, text, audio, and more.
- **End-to-End Learning:** DL models can learn directly from raw inputs to final outputs without intermediate manual steps.
- **Performance:** Since around 2010, DL has consistently outperformed traditional ML methods in fields like computer vision, speech recognition, and natural language processing.
- **Data Hungry:** DL requires large amounts of data to train effectively, which is now more feasible with modern datasets and hardware.


### 2. 🧠 Anatomy of a Deep Neural Network

A deep neural network (DNN) is composed of several key components:

- **Layers:** These are the building blocks of the network. Each layer transforms its input data into a more abstract representation.
- **Input Data and Targets:** The network receives input data (e.g., images, text) and is trained to predict target outputs (e.g., labels, translations).
- **Loss Function:** This measures how far the network’s predictions are from the true targets. The goal during training is to minimize this loss.
- **Optimizer:** This algorithm updates the network’s weights to reduce the loss, using methods like stochastic gradient descent (SGD) or RMSProp.

#### Layers and Data Flow

- The input data is passed through multiple layers.
- Each layer applies a nonlinear transformation to the data.
- The final layer produces predictions.
- During training, the network compares predictions to true labels using the loss function.
- The optimizer adjusts weights to improve accuracy.

#### Types of Layers

- **Dense (Fully Connected):** Every neuron connects to every neuron in the previous layer.
- **Convolutional:** Specialized for spatial data like images, focusing on local regions.
- **Recurrent:** Designed for sequential data, maintaining memory of previous inputs.
- **Pooling, Normalization, Flattening:** Additional operations to reduce dimensionality, stabilize training, or reshape data.


### 3. 🖼️ Deep Learning in Computer Vision

Computer vision is one of the earliest and most successful applications of deep learning. Tasks include image classification, object detection, and segmentation.

#### Traditional ML vs Deep Learning in Vision

- Traditional ML requires handcrafted features (e.g., edges, textures) designed by experts.
- DL learns these features automatically from raw pixels.
- This automatic feature learning is hierarchical: from simple edges to complex objects.

#### Convolutional Neural Networks (CNNs)

CNNs are the backbone of modern computer vision systems. They are inspired by the visual cortex and designed to efficiently process images.

##### Key Concepts in CNNs:

- **Local Receptive Fields:** Each neuron looks at a small patch of the input image, not the entire image.
- **Filters (Kernels):** Small matrices of weights that slide over the image to detect specific features like edges or textures.
- **Shared Weights:** The same filter is applied across the entire image, drastically reducing the number of parameters.
- **Feature Maps:** The output of applying a filter across the image, showing where certain features appear.
- **Pooling Layers:** Reduce the spatial size of feature maps to lower computation and help generalize by summarizing features (e.g., max pooling takes the maximum value in a region).

##### Why CNNs?

- They reduce the number of parameters compared to fully connected networks.
- They are robust to spatial translations (e.g., an object shifted in the image is still recognized).
- They learn meaningful features automatically.


### 4. 🔄 Recurrent Neural Networks (RNNs) for Sequential Data

While CNNs excel at spatial data, many problems involve sequences — like text, speech, or video — where the order of data points matters.

#### Why RNNs?

- Traditional neural networks treat each input independently.
- RNNs maintain a **memory** of previous inputs by feeding the hidden state from one time step to the next.
- This allows them to model temporal dependencies and varying input/output lengths.

#### How RNNs Work

- At each time step, the RNN takes the current input and the previous hidden state to produce a new hidden state.
- The hidden state acts as a memory, capturing information from the past.
- The same weights are used at every time step, enabling the network to generalize across sequences of different lengths.

#### Applications of RNNs

- Language modeling and text generation
- Sentiment analysis
- Machine translation
- Video and speech processing

#### Bidirectional RNNs

- These process sequences in both forward and backward directions.
- Useful when the output depends on both past and future context (e.g., predicting a missing word in a sentence).


### 5. 🧩 Long Short-Term Memory (LSTM) Networks: Solving RNN Limitations

Standard RNNs struggle with **vanishing gradients**, making it hard to learn long-term dependencies in sequences.

#### What are LSTMs?

- A special type of RNN designed to remember information over long periods.
- They use a **memory cell** and three gates to control information flow:
  - **Input Gate:** Decides what new information to store.
  - **Forget Gate:** Decides what information to discard.
  - **Output Gate:** Decides what information to output.

#### Why LSTMs Work Better

- The gating mechanism allows LSTMs to maintain a more constant error signal during training.
- This helps them learn dependencies over hundreds or thousands of time steps.
- LSTMs are widely used in modern sequence modeling tasks.


### 6. 🧩 Other Deep Learning Architectures and Concepts

#### Residual Networks (ResNets)

- Deep networks can suffer from vanishing gradients and training difficulties.
- ResNets introduce **skip connections** that add the input of a layer directly to its output.
- This helps gradients flow better and allows training of very deep networks (100+ layers).
- ResNets are foundational models for many state-of-the-art architectures.

#### Autoencoders

- Autoencoders are neural networks trained to reconstruct their input.
- They consist of an **encoder** (compresses input to a smaller representation) and a **decoder** (reconstructs the input).
- Deep autoencoders have multiple layers in both encoder and decoder.
- They can be used for dimensionality reduction, denoising, and unsupervised feature learning.
- Adding noise to inputs during training (denoising autoencoders) forces the model to learn robust features.


### 7. ⚙️ Training Deep Neural Networks: Loss, Optimizers, and Hyperparameters

#### Loss Functions

- Measure how well the network’s predictions match the true targets.
- Common losses:
  - **Mean Squared Error (MSE):** For regression tasks.
  - **Binary Cross-Entropy:** For two-class classification.
  - **Categorical Cross-Entropy:** For multi-class classification.

#### Optimizers

- Algorithms that update network weights to minimize loss.
- Examples:
  - **Stochastic Gradient Descent (SGD):** Basic optimizer.
  - **Momentum:** Accelerates SGD by considering past gradients.
  - **RMSProp:** Adapts learning rates for each parameter, often a good first choice.

#### Hyperparameter Tuning

- Deep networks have many hyperparameters:
  - Number of layers and neurons
  - Learning rate and decay schedule
  - Optimizer type
  - Regularization parameters (dropout rate, weight decay)
  - Batch size
- Tuning these is crucial but can be time-consuming.
- Methods include grid search, random search, and Bayesian optimization.

#### Regularization: Dropout

- Dropout randomly disables neurons during training.
- This prevents overfitting by forcing the network to learn redundant representations.
- Typically, 20-50% of neurons are dropped during training.
- Dropout acts like training an ensemble of slightly different networks.


### Summary

Deep learning is a transformative approach to machine learning that automatically learns hierarchical features from data through deep, layered neural networks. It excels in tasks involving images, sequences, and complex data patterns. Key architectures include CNNs for spatial data, RNNs (and LSTMs) for sequential data, and ResNets for very deep networks. Training involves minimizing loss functions with optimizers and carefully tuning hyperparameters. Regularization techniques like dropout help improve generalization.