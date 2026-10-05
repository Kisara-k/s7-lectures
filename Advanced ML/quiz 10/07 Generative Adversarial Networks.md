## 7. Generative Adversarial Networks

## Questions

#### 1. What are the primary roles of the Generator and Discriminator in a Generative Adversarial Network (GAN)?  
A) The Generator tries to maximize the Discriminator’s reward.  
B) The Discriminator tries to minimize the Generator’s loss.  
C) The Discriminator tries to classify samples as real or fake.  
D) The Generator tries to produce samples indistinguishable from real data.  

#### 2. Which of the following statements about Maximum Likelihood Estimation (MLE) and GANs are true?  
A) GANs estimate the parameters of a fixed distribution using MLE.  
B) MLE directly estimates the parameters of a fixed distribution like a Gaussian mixture.  
C) MLE is effective for modeling complex, high-dimensional data distributions like images.  
D) GANs learn a more complex implicit distribution rather than just estimating parameters.  

#### 3. Why is the training of GANs considered a minimax game, and what is the Nash equilibrium in this context?  
A) The Discriminator maximizes its classification accuracy between real and fake samples.  
B) The Nash equilibrium occurs when the Discriminator perfectly classifies all samples.  
C) The Generator minimizes the Discriminator’s ability to distinguish fake samples.  
D) The Nash equilibrium occurs when the Generator’s distribution matches the real data distribution, making the Discriminator unable to distinguish real from fake.  

#### 4. Which of the following are common training problems encountered in GANs?  
A) Mode collapse, where the Generator produces limited diversity in samples.  
B) The Discriminator becoming too weak to provide useful gradients.  
C) Non-convergence due to the adversarial nature of training.  
D) Overfitting of the Generator to the training data.  

#### 5. How can mode collapse in GANs be mitigated?  
A) Training the Generator exclusively without updating the Discriminator.  
B) Using batch normalization and input normalization techniques.  
C) By letting the Discriminator evaluate entire batches to detect lack of diversity.  
D) Incorporating feature statistics that capture diversity into the Discriminator’s input.  

#### 6. What are the key architectural features of Deep Convolutional GANs (DCGANs)?  
A) Use of fractional-strided convolutions in the Generator.  
B) Replacement of fully connected layers with convolutional layers.  
C) Use of ReLU activations in the output layer of the Generator.  
D) Application of batch normalization after each layer in both Generator and Discriminator.  

#### 7. In the context of conditional GANs, which statements are correct?  
A) Conditioning can be done using text embeddings, images, or class labels.  
B) Conditioning the Generator and Discriminator on class labels allows generation of specific types of outputs.  
C) Conditional GANs cannot be used for image-to-image translation tasks.  
D) Conditional GANs require paired data for training.  

#### 8. Which of the following describe the role and advantage of the Discriminator in GAN training?  
A) It forces the Generator to improve by providing gradients indicating how to fool it better.  
B) It directly models the probability distribution P(X).  
C) It provides a supervised learning signal to the Generator via backpropagation.  
D) It is discarded after training because it has no use in generation.  

#### 9. Regarding advanced GAN extensions, which of the following are true?  
A) Coupled GANs learn joint distributions across multiple domains using weight sharing without paired supervision.  
B) Adversarially Learned Inference combines an encoder and generator to learn latent representations adversarially.  
C) Laplacian Pyramid GANs generate high-resolution images by progressively refining lower-resolution images.  
D) Cycle GANs require paired images from source and target domains for training.  

#### 10. Which statements about the loss functions and training dynamics in GANs are accurate?  
A) The Generator tries to maximize the Discriminator’s reward to improve sample quality.  
B) Replacing cross-entropy with hinge loss allows the Discriminator to output unbounded real values instead of probabilities.  
C) The original GAN loss uses cross-entropy for both Generator and Discriminator.  
D) The Generator’s loss can suffer from vanishing gradients if the Discriminator becomes too confident.  



<br>

## Answers

#### 1. What are the primary roles of the Generator and Discriminator in a Generative Adversarial Network (GAN)?  
A) ✗ The Generator tries to maximize the Discriminator’s reward (it tries to minimize or fool it, not maximize).  
B) ✗ The Discriminator tries to minimize the Generator’s loss (it maximizes its own classification accuracy, not minimize Generator’s loss).  
C) ✓ The Discriminator tries to classify samples as real or fake.  
D) ✓ The Generator tries to produce samples indistinguishable from real data.  

**Correct:** C, D


#### 2. Which of the following statements about Maximum Likelihood Estimation (MLE) and GANs are true?  
A) ✗ GANs do not estimate parameters of a fixed distribution using MLE; they learn implicit distributions.  
B) ✓ MLE directly estimates parameters of a fixed distribution like Gaussian mixtures.  
C) ✗ MLE struggles with complex, high-dimensional data like images, which is why GANs are preferred.  
D) ✓ GANs learn a more complex implicit distribution rather than just estimating parameters.  

**Correct:** B, D


#### 3. Why is the training of GANs considered a minimax game, and what is the Nash equilibrium in this context?  
A) ✓ The Discriminator maximizes its classification accuracy between real and fake samples.  
B) ✗ Nash equilibrium is not when Discriminator perfectly classifies all samples (that would mean Generator fails).  
C) ✓ The Generator minimizes the Discriminator’s ability to distinguish fake samples.  
D) ✓ Nash equilibrium occurs when Generator’s distribution matches real data, making Discriminator unable to distinguish real from fake.  

**Correct:** A, C, D


#### 4. Which of the following are common training problems encountered in GANs?  
A) ✓ Mode collapse, where Generator produces limited diversity, is common.  
B) ✗ Discriminator becoming too weak is not typical; usually it becomes too strong.  
C) ✓ Non-convergence due to adversarial training dynamics is common.  
D) ✗ Overfitting of Generator is less common because it never sees training data directly.  

**Correct:** A, C


#### 5. How can mode collapse in GANs be mitigated?  
A) ✗ Training Generator exclusively without Discriminator updates worsens mode collapse.  
B) ✓ Batch normalization and input normalization help stabilize training and reduce collapse.  
C) ✓ Letting Discriminator evaluate entire batches helps detect lack of diversity.  
D) ✓ Incorporating diversity-related feature statistics into Discriminator input encourages diverse outputs.  

**Correct:** B, C, D


#### 6. What are the key architectural features of Deep Convolutional GANs (DCGANs)?  
A) ✓ Use of fractional-strided convolutions in Generator for upsampling.  
B) ✓ Replacement of fully connected layers with convolutional layers improves spatial structure.  
C) ✗ ReLU is used in hidden layers, but output layer uses Tanh, not ReLU.  
D) ✓ Batch normalization is applied after each layer to stabilize training.  

**Correct:** A, B, D


#### 7. In the context of conditional GANs, which statements are correct?  
A) ✓ Conditioning can be done using text embeddings, images, or class labels.  
B) ✓ Conditioning on class labels allows generation of specific outputs.  
C) ✗ Conditional GANs are widely used for image-to-image translation tasks.  
D) ✗ Conditional GANs do not require paired data; they can work with unpaired data depending on setup.  

**Correct:** A, B


#### 8. Which of the following describe the role and advantage of the Discriminator in GAN training?  
A) ✓ It forces Generator to improve by providing gradients on how to fool it better.  
B) ✗ It does not explicitly model P(X); GANs model implicit distributions.  
C) ✓ It provides a supervised learning signal to Generator via backpropagation.  
D) ✗ The Discriminator is useful during training and discarded after; it has no direct role in generation.  

**Correct:** A, C


#### 9. Regarding advanced GAN extensions, which of the following are true?  
A) ✓ Coupled GANs learn joint distributions across domains using weight sharing without paired supervision.  
B) ✓ Adversarially Learned Inference combines encoder and generator to learn latent representations adversarially.  
C) ✓ Laplacian Pyramid GANs generate high-res images by progressively refining lower-res images.  
D) ✗ Cycle GANs do not require paired images; they work with unpaired datasets.  

**Correct:** A, B, C


#### 10. Which statements about the loss functions and training dynamics in GANs are accurate?  
A) ✗ Generator tries to minimize Discriminator’s reward (or maximize its loss), not maximize Discriminator’s reward.  
B) ✓ Replacing cross-entropy with hinge loss lets Discriminator output unbounded real values instead of probabilities.  
C) ✓ Original GAN loss uses cross-entropy for both Generator and Discriminator.  
D) ✓ Generator’s loss can vanish if Discriminator becomes too confident, causing training difficulties.  

**Correct:** B, C, D