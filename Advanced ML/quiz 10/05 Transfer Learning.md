## 5. Transfer Learning

## Questions

#### 1. Which of the following statements correctly describe challenges addressed by transfer learning?  
A) Deep learning models require large amounts of labeled data, often more than 50,000 items.  
B) Transfer learning assumes the source and target data distributions are always identical.  
C) Transfer learning helps when labeled data in the target domain is limited.  
D) Transfer learning eliminates the need for any labeled data in the target domain.  

#### 2. In the context of transfer learning paradigms, which of the following are true?  
A) Inductive transfer learning requires labeled data in the target domain.  
B) Transductive transfer learning assumes labeled data is available in both source and target domains.  
C) Unsupervised transfer learning involves no labeled data in either source or target domains.  
D) Inductive transfer learning can be applied when no labeled data is available in the source domain.  

#### 3. Regarding model fine-tuning in transfer learning, which statements are accurate?  
A) Fine-tuning always involves training the entire network from scratch on the target data.  
B) When target data is limited, only some layers are fine-tuned to avoid overfitting.  
C) In speech recognition, usually the last few layers are transferred during fine-tuning.  
D) In image recognition, typically the first few layers are transferred during fine-tuning.  

#### 4. Which of the following best describe multi-task learning?  
A) It involves training a model on multiple related tasks simultaneously to improve generalization.  
B) It requires that all tasks share the exact same input features.  
C) It can leverage shared hidden layers to transfer knowledge across languages in speech recognition.  
D) It is only applicable when tasks are identical in nature and domain.  

#### 5. Domain adaptation techniques often use domain-adversarial training. Which of the following are true about this approach?  
A) The feature extractor is trained to maximize domain classification accuracy.  
B) The feature extractor tries to fool the domain classifier to make domain classification difficult.  
C) The label predictor and domain classifier have conflicting objectives during training.  
D) Domain-adversarial training is unrelated to Generative Adversarial Networks (GANs).  

#### 6. Zero-shot learning in transfer learning involves which of the following concepts?  
A) Representing classes by their semantic attributes to enable recognition without direct training examples.  
B) Using a convex combination of semantic embeddings to represent unseen classes.  
C) Requires a large labeled dataset for every possible class in the source domain.  
D) Embedding both images and class attributes into a shared space for similarity comparison.  

#### 7. Covariate shift refers to which of the following scenarios?  
A) The input data distribution changes between training and testing, but the conditional distribution of labels given inputs remains the same.  
B) The output label distribution changes, but the input distribution remains constant.  
C) The source and target domains share the same input and output spaces but differ in marginal input distributions.  
D) It only occurs when the source and target domains have completely different tasks.  

#### 8. Self-taught learning differs from other transfer learning approaches because it:  
A) Uses labeled source data to improve target task performance.  
B) Focuses on unsupervised learning to extract better feature representations from source data.  
C) Requires labeled data in both source and target domains.  
D) Is primarily concerned with clustering unlabeled target data using auxiliary unlabeled data.  

#### 9. Unsupervised transfer learning aims to:  
A) Cluster a small set of unlabeled target data with the help of a large amount of auxiliary unlabeled data.  
B) Use labeled source data to directly train the target model.  
C) Simultaneously cluster target and auxiliary data to share feature representations.  
D) Require that target and auxiliary data have identical topic distributions.  

#### 10. Which of the following strategies help avoid negative transfer in transfer learning?  
A) Rejecting harmful source-task knowledge during target task learning.  
B) Choosing the best matching source task to transfer from.  
C) Ignoring task similarity and transferring knowledge indiscriminately.  
D) Explicitly modeling task relationships to guide transfer and reduce negative impact.



<br>

## Answers

#### 1. Which of the following statements correctly describe challenges addressed by transfer learning?  
A) ✓ Deep learning models require large amounts of labeled data, often more than 50,000 items.  
B) ✗ Transfer learning assumes the source and target data distributions are always identical. (This is false; transfer learning often deals with different distributions.)  
C) ✓ Transfer learning helps when labeled data in the target domain is limited.  
D) ✗ Transfer learning eliminates the need for any labeled data in the target domain. (Some labeled target data is often needed, especially in inductive transfer.)  

**Correct:** A, C


#### 2. In the context of transfer learning paradigms, which of the following are true?  
A) ✓ Inductive transfer learning requires labeled data in the target domain.  
B) ✗ Transductive transfer learning assumes labeled data is available in both source and target domains. (It assumes no labeled target data.)  
C) ✓ Unsupervised transfer learning involves no labeled data in either source or target domains.  
D) ✗ Inductive transfer learning can be applied when no labeled data is available in the source domain. (Usually source domain is labeled.)  

**Correct:** A, C


#### 3. Regarding model fine-tuning in transfer learning, which statements are accurate?  
A) ✗ Fine-tuning always involves training the entire network from scratch on the target data. (Fine-tuning usually starts from a pre-trained model.)  
B) ✓ When target data is limited, only some layers are fine-tuned to avoid overfitting.  
C) ✗ In speech recognition, usually the last few layers are transferred during fine-tuning. (Usually the first layers are transferred in image, last layers in speech.)  
D) ✓ In image recognition, typically the first few layers are transferred during fine-tuning.  

**Correct:** B, D


#### 4. Which of the following best describe multi-task learning?  
A) ✓ It involves training a model on multiple related tasks simultaneously to improve generalization.  
B) ✗ It requires that all tasks share the exact same input features. (Tasks can have different inputs.)  
C) ✓ It can leverage shared hidden layers to transfer knowledge across languages in speech recognition.  
D) ✗ It is only applicable when tasks are identical in nature and domain. (It works for related but different tasks.)  

**Correct:** A, C


#### 5. Domain adaptation techniques often use domain-adversarial training. Which of the following are true about this approach?  
A) ✗ The feature extractor is trained to maximize domain classification accuracy. (It tries to minimize domain classification accuracy.)  
B) ✓ The feature extractor tries to fool the domain classifier to make domain classification difficult.  
C) ✓ The label predictor and domain classifier have conflicting objectives during training.  
D) ✗ Domain-adversarial training is unrelated to Generative Adversarial Networks (GANs). (It is inspired by GANs.)  

**Correct:** B, C


#### 6. Zero-shot learning in transfer learning involves which of the following concepts?  
A) ✓ Representing classes by their semantic attributes to enable recognition without direct training examples.  
B) ✓ Using a convex combination of semantic embeddings to represent unseen classes.  
C) ✗ Requires a large labeled dataset for every possible class in the source domain. (Zero-shot avoids this.)  
D) ✓ Embedding both images and class attributes into a shared space for similarity comparison.  

**Correct:** A, B, D


#### 7. Covariate shift refers to which of the following scenarios?  
A) ✓ The input data distribution changes between training and testing, but the conditional distribution of labels given inputs remains the same.  
B) ✗ The output label distribution changes, but the input distribution remains constant. (Covariate shift is about input distribution change.)  
C) ✓ The source and target domains share the same input and output spaces but differ in marginal input distributions.  
D) ✗ It only occurs when the source and target domains have completely different tasks. (Covariate shift can occur within the same task.)  

**Correct:** A, C


#### 8. Self-taught learning differs from other transfer learning approaches because it:  
A) ✗ Uses labeled source data to improve target task performance. (It is unsupervised, uses unlabeled source data.)  
B) ✓ Focuses on unsupervised learning to extract better feature representations from source data.  
C) ✗ Requires labeled data in both source and target domains. (It does not require labeled data.)  
D) ✗ Is primarily concerned with clustering unlabeled target data using auxiliary unlabeled data. (This describes unsupervised transfer learning.)  

**Correct:** B


#### 9. Unsupervised transfer learning aims to:  
A) ✓ Cluster a small set of unlabeled target data with the help of a large amount of auxiliary unlabeled data.  
B) ✗ Use labeled source data to directly train the target model. (It uses unlabeled data.)  
C) ✓ Simultaneously cluster target and auxiliary data to share feature representations.  
D) ✗ Require that target and auxiliary data have identical topic distributions. (They can differ in topic distribution.)  

**Correct:** A, C


#### 10. Which of the following strategies help avoid negative transfer in transfer learning?  
A) ✓ Rejecting harmful source-task knowledge during target task learning.  
B) ✓ Choosing the best matching source task to transfer from.  
C) ✗ Ignoring task similarity and transferring knowledge indiscriminately. (This increases risk of negative transfer.)  
D) ✓ Explicitly modeling task relationships to guide transfer and reduce negative impact.  

**Correct:** A, B, D