## 7. Generative Adversarial Networks

## Questions

#### 1. What are the primary roles of the Generator and Discriminator in a Generative Adversarial Network (GAN)?  
A) The Generator tries to produce samples indistinguishable from real data.  
B) The Discriminator tries to classify samples as real or fake.  
C) The Generator tries to maximize the Discriminator’s reward.  
D) The Discriminator tries to minimize the Generator’s loss.  

#### 2. Which of the following statements about Maximum Likelihood Estimation (MLE) and GANs are true?  
A) MLE directly estimates the parameters of a fixed distribution like a Gaussian mixture.  
B) GANs estimate the parameters of a fixed distribution using MLE.  
C) GANs learn a more complex implicit distribution rather than just estimating parameters.  
D) MLE is effective for modeling complex, high-dimensional data distributions like images.  

#### 3. Why is the training of GANs considered a minimax game, and what is the Nash equilibrium in this context?  
A) The Generator minimizes the Discriminator’s ability to distinguish fake samples.  
B) The Discriminator maximizes its classification accuracy between real and fake samples.  
C) The Nash equilibrium occurs when the Discriminator perfectly classifies all samples.  
D) The Nash equilibrium occurs when the Generator’s distribution matches the real data distribution, making the Discriminator unable to distinguish real from fake.  

#### 4. Which of the following are common training problems encountered in GANs?  
A) Mode collapse, where the Generator produces limited diversity in samples.  
B) Non-convergence due to the adversarial nature of training.  
C) Overfitting of the Generator to the training data.  
D) The Discriminator becoming too weak to provide useful gradients.  

#### 5. How can mode collapse in GANs be mitigated?  
A) By letting the Discriminator evaluate entire batches to detect lack of diversity.  
B) Using batch normalization and input normalization techniques.  
C) Training the Generator exclusively without updating the Discriminator.  
D) Incorporating feature statistics that capture diversity into the Discriminator’s input.  

#### 6. What are the key architectural features of Deep Convolutional GANs (DCGANs)?  
A) Use of fractional-strided convolutions in the Generator.  
B) Replacement of fully connected layers with convolutional layers.  
C) Use of ReLU activations in the output layer of the Generator.  
D) Application of batch normalization after each layer in both Generator and Discriminator.  

#### 7. In the context of conditional GANs, which statements are correct?  
A) Conditioning the Generator and Discriminator on class labels allows generation of specific types of outputs.  
B) Conditional GANs require paired data for training.  
C) Conditioning can be done using text embeddings, images, or class labels.  
D) Conditional GANs cannot be used for image-to-image translation tasks.  

#### 8. Which of the following describe the role and advantage of the Discriminator in GAN training?  
A) It provides a supervised learning signal to the Generator via backpropagation.  
B) It directly models the probability distribution P(X).  
C) It forces the Generator to improve by providing gradients indicating how to fool it better.  
D) It is discarded after training because it has no use in generation.  

#### 9. Regarding advanced GAN extensions, which of the following are true?  
A) Coupled GANs learn joint distributions across multiple domains using weight sharing without paired supervision.  
B) Laplacian Pyramid GANs generate high-resolution images by progressively refining lower-resolution images.  
C) Adversarially Learned Inference combines an encoder and generator to learn latent representations adversarially.  
D) Cycle GANs require paired images from source and target domains for training.  

#### 10. Which statements about the loss functions and training dynamics in GANs are accurate?  
A) The original GAN loss uses cross-entropy for both Generator and Discriminator.  
B) The Generator’s loss can suffer from vanishing gradients if the Discriminator becomes too confident.  
C) Replacing cross-entropy with hinge loss allows the Discriminator to output unbounded real values instead of probabilities.  
D) The Generator tries to maximize the Discriminator’s reward to improve sample quality.



<br>

## Answers

#### 1. What are the primary roles of the Generator and Discriminator in a Generative Adversarial Network (GAN)?  
A) ✓ The Generator tries to produce samples indistinguishable from real data.  
B) ✓ The Discriminator tries to classify samples as real or fake.  
C) ✗ The Generator tries to maximize the Discriminator’s reward (it tries to minimize or fool it, not maximize).  
D) ✗ The Discriminator tries to minimize the Generator’s loss (it maximizes its own classification accuracy, not minimize Generator’s loss).  

**Correct:** A, B


#### 2. Which of the following statements about Maximum Likelihood Estimation (MLE) and GANs are true?  
A) ✓ MLE directly estimates parameters of a fixed distribution like Gaussian mixtures.  
B) ✗ GANs do not estimate parameters of a fixed distribution using MLE; they learn implicit distributions.  
C) ✓ GANs learn a more complex implicit distribution rather than just estimating parameters.  
D) ✗ MLE struggles with complex, high-dimensional data like images, which is why GANs are preferred.  

**Correct:** A, C


#### 3. Why is the training of GANs considered a minimax game, and what is the Nash equilibrium in this context?  
A) ✓ The Generator minimizes the Discriminator’s ability to distinguish fake samples.  
B) ✓ The Discriminator maximizes its classification accuracy between real and fake samples.  
C) ✗ Nash equilibrium is not when Discriminator perfectly classifies all samples (that would mean Generator fails).  
D) ✓ Nash equilibrium occurs when Generator’s distribution matches real data, making Discriminator unable to distinguish real from fake.  

**Correct:** A, B, D


#### 4. Which of the following are common training problems encountered in GANs?  
A) ✓ Mode collapse, where Generator produces limited diversity, is common.  
B) ✓ Non-convergence due to adversarial training dynamics is common.  
C) ✗ Overfitting of Generator is less common because it never sees training data directly.  
D) ✗ Discriminator becoming too weak is not typical; usually it becomes too strong.  

**Correct:** A, B


#### 5. How can mode collapse in GANs be mitigated?  
A) ✓ Letting Discriminator evaluate entire batches helps detect lack of diversity.  
B) ✓ Batch normalization and input normalization help stabilize training and reduce collapse.  
C) ✗ Training Generator exclusively without Discriminator updates worsens mode collapse.  
D) ✓ Incorporating diversity-related feature statistics into Discriminator input encourages diverse outputs.  

**Correct:** A, B, D


#### 6. What are the key architectural features of Deep Convolutional GANs (DCGANs)?  
A) ✓ Use of fractional-strided convolutions in Generator for upsampling.  
B) ✓ Replacement of fully connected layers with convolutional layers improves spatial structure.  
C) ✗ ReLU is used in hidden layers, but output layer uses Tanh, not ReLU.  
D) ✓ Batch normalization is applied after each layer to stabilize training.  

**Correct:** A, B, D


#### 7. In the context of conditional GANs, which statements are correct?  
A) ✓ Conditioning on class labels allows generation of specific outputs.  
B) ✗ Conditional GANs do not require paired data; they can work with unpaired data depending on setup.  
C) ✓ Conditioning can be done using text embeddings, images, or class labels.  
D) ✗ Conditional GANs are widely used for image-to-image translation tasks.  

**Correct:** A, C


#### 8. Which of the following describe the role and advantage of the Discriminator in GAN training?  
A) ✓ It provides a supervised learning signal to Generator via backpropagation.  
B) ✗ It does not explicitly model P(X); GANs model implicit distributions.  
C) ✓ It forces Generator to improve by providing gradients on how to fool it better.  
D) ✗ The Discriminator is useful during training and discarded after; it has no direct role in generation.  

**Correct:** A, C


#### 9. Regarding advanced GAN extensions, which of the following are true?  
A) ✓ Coupled GANs learn joint distributions across domains using weight sharing without paired supervision.  
B) ✓ Laplacian Pyramid GANs generate high-res images by progressively refining lower-res images.  
C) ✓ Adversarially Learned Inference combines encoder and generator to learn latent representations adversarially.  
D) ✗ Cycle GANs do not require paired images; they work with unpaired datasets.  

**Correct:** A, B, C


#### 10. Which statements about the loss functions and training dynamics in GANs are accurate?  
A) ✓ Original GAN loss uses cross-entropy for both Generator and Discriminator.  
B) ✓ Generator’s loss can vanish if Discriminator becomes too confident, causing training difficulties.  
C) ✓ Replacing cross-entropy with hinge loss lets Discriminator output unbounded real values instead of probabilities.  
D) ✗ Generator tries to minimize Discriminator’s reward (or maximize its loss), not maximize Discriminator’s reward.  

**Correct:** A, B, C