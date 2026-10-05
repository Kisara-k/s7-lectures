## 6. Deep Learning

## Key Points

#### 1. 🤖 Deep Learning Basics  
- Deep learning refers to machine learning models with multiple layers that learn hierarchical data representations automatically.  
- Deep learning models learn features from raw data, unlike traditional ML which relies on handcrafted features.  
- Deep learning requires large amounts of training data to be effective.  
- Since around 2010, deep learning has outperformed traditional ML in vision, speech, and NLP tasks.

#### 2. 🧠 Deep Neural Network Components  
- A deep neural network consists of layers, input data, targets, a loss function, and an optimizer.  
- Loss functions measure prediction error; common types include mean squared error (regression), binary cross-entropy (binary classification), and categorical cross-entropy (multi-class classification).  
- Optimizers like stochastic gradient descent (SGD) and RMSProp update weights to minimize loss.  
- Layers can be densely connected, convolutional, recurrent, or include pooling and normalization.

#### 3. 🖼️ Convolutional Neural Networks (CNNs)  
- CNNs use local receptive fields where neurons connect only to small regions of the input.  
- Filters (kernels) slide over the input to detect features; weights are shared across spatial locations.  
- Shared weights drastically reduce the number of parameters compared to fully connected layers.  
- Pooling layers (max, average, L2) reduce spatial dimensions and help prevent overfitting.  
- CNNs are robust to spatial translations in images.

#### 4. 🔄 Recurrent Neural Networks (RNNs)  
- RNNs process sequential data by maintaining a hidden state that acts as memory of previous inputs.  
- The same weights are used at every time step in an RNN.  
- RNNs are trained using backpropagation through time.  
- RNNs are sensitive to the vanishing gradient problem, limiting their ability to learn long-term dependencies.  
- Bidirectional RNNs process sequences in both forward and backward directions to capture past and future context.

#### 5. 🧩 Long Short-Term Memory (LSTM) Networks  
- LSTMs are a type of RNN designed to combat the vanishing gradient problem.  
- LSTMs use a memory cell and three gates: input gate, forget gate, and output gate to control information flow.  
- LSTMs can learn long-term dependencies over many time steps (1000+).  
- Most modern RNN models use LSTM or similar gated units like GRUs.

#### 6. 🏗️ Residual Networks (ResNets)  
- ResNets introduce identity skip connections that add layer inputs directly to outputs.  
- Skip connections help mitigate vanishing gradients and enable training of very deep networks (100+ layers).  
- ResNets serve as base models for many state-of-the-art architectures.

#### 7. 🧩 Autoencoders  
- Autoencoders are neural networks trained to reconstruct their input.  
- They consist of an encoder (input to hidden representation) and a decoder (hidden to output).  
- Deep autoencoders have multiple hidden layers in encoder and decoder.  
- Adding noise to inputs during training (denoising autoencoders) forces learning of robust features.

#### 8. ⚙️ Training and Regularization  
- Dropout randomly disables neurons during training to reduce overfitting; typical dropout rates are 20-50%.  
- Hyperparameters include number of layers, neurons per layer, learning rate, optimizer type, batch size, and regularization parameters.  
- Hyperparameter tuning methods include grid search, random search, and Bayesian optimization.



<br>

