## 5. Transfer Learning

## Study Notes

### 1. 📚 Introduction to Transfer Learning

Transfer learning is a powerful machine learning technique designed to overcome some of the biggest challenges faced by deep learning models in real-world applications. Deep learning models typically require vast amounts of labeled data—often more than 50,000 examples—to train effectively. However, in many practical scenarios, such large labeled datasets are unavailable, especially in the target domain where the model is intended to be applied.

Moreover, traditional machine learning assumes that the training data (source domain) and the data where the model will be used (target domain) come from the same distribution. This assumption often fails in real life, where data distributions can differ significantly between domains. Transfer learning addresses these issues by reusing knowledge gained from one task or domain (source) to improve learning in another task or domain (target), even when labeled data in the target domain is scarce or unavailable.

In simple terms, transfer learning helps a model trained on one problem to adapt and perform well on a related but different problem, saving time, computational resources, and data requirements.


### 2. 🔄 What is Transfer Learning? Key Concepts and Paradigms

At its core, **transfer learning** involves taking a model developed for one task or domain and using it as the starting point for a model on a different task or domain. This reuse can happen in several ways depending on the availability of labeled data in the source and target domains.

#### Types of Transfer Learning Based on Data Availability:

- **Inductive Transfer Learning:**  
  Here, labeled data is available in the target domain. The goal is to improve the target task’s performance by leveraging knowledge from a different but related source task. For example, pre-training a model on a large dataset and then fine-tuning it on a smaller labeled dataset for a specific task.

- **Transductive Transfer Learning:**  
  In this case, labeled data is available only in the source domain, and the target domain has no labeled data. The focus is on adapting the model to the target domain despite the lack of labels, often called domain adaptation. This is common in natural language processing (NLP) where labeled data in the target domain is scarce.

- **Unsupervised Transfer Learning:**  
  Neither the source nor the target domain has labeled data. The goal is to learn useful representations or features from unlabeled data that can be transferred across domains or tasks.

#### Why Transfer Learning is Needed:

- **Data scarcity:** Target domain may have limited or no labeled data.
- **Domain differences:** Source and target data distributions differ.
- **Task differences:** Tasks may be related but not identical (e.g., image recognition vs. speech recognition).
- **Efficiency:** Reduces training time and computational cost by reusing existing models.


### 3. 🛠️ Transfer Learning Approaches

There are several approaches to transfer learning, each suited to different scenarios and data availability:

#### 3.1 Model Fine-tuning

Fine-tuning is one of the most common transfer learning methods. It involves two steps:

1. **Pre-training:** Train a model on a large source dataset (e.g., ImageNet for images, large speech datasets for audio).
2. **Fine-tuning:** Adapt the pre-trained model to the target dataset by continuing training on the target data.

Fine-tuning is especially useful when the target dataset is small. However, care must be taken to avoid overfitting due to limited target data.

- **Layer Transfer:**  
  Often, only some layers of the pre-trained model are reused. For example, in image tasks, the first few layers (which capture general features like edges and textures) are transferred, while the later layers (task-specific) are retrained. In speech tasks, sometimes the last few layers are transferred.

- **Conservative Training:**  
  Freeze some layers to prevent overfitting and only train the remaining layers on the target data.

- **One-shot Learning:**  
  Extreme case of fine-tuning where only a few examples are available in the target domain.

#### 3.2 Multi-task Learning

Multi-task learning trains a single model on multiple related tasks simultaneously. The idea is that learning shared representations across tasks improves generalization.

- Neural networks with shared hidden layers can learn features useful for all tasks.
- Example: Multilingual speech recognition where a model learns to recognize speech in multiple languages by sharing hidden layers.
- Benefits include improved performance on all tasks and better feature extraction.

#### 3.3 Domain Adaptation

Domain adaptation is a type of transfer learning where the task remains the same, but the data distribution changes between source and target domains.

- **Domain-Adversarial Training:**  
  Inspired by Generative Adversarial Networks (GANs), this method trains a feature extractor to produce features that confuse a domain classifier (which tries to distinguish source vs. target domain), while simultaneously training a label predictor to correctly classify the task labels. The goal is to learn domain-invariant features that work well on both domains.

- This approach is widely used in NLP and computer vision to handle shifts in data distribution.

#### 3.4 Zero-shot Learning

Zero-shot learning addresses the problem of recognizing classes in the target domain that were never seen during training.

- It uses **class attributes** or semantic embeddings (e.g., word vectors) to represent classes.
- The model learns to map input data and class attributes into a shared embedding space.
- At test time, the model predicts the class whose attributes are closest to the input’s embedding.
- Example: Recognizing a new animal species by its attributes (e.g., furry, four legs, tail) without having seen images of it during training.

#### 3.5 Covariate Shift

Covariate shift occurs when the input data distribution changes between training and testing, but the relationship between inputs and outputs remains the same.

- For example, a facial recognition model trained on images with certain lighting conditions may perform poorly when lighting changes.
- The model must adapt to the new input distribution without changing the output labels.
- Transfer learning techniques can help by adjusting the model to the new input distribution.

#### 3.6 Self-taught Learning

Self-taught learning is an unsupervised approach where the model learns better feature representations from large amounts of unlabeled source data.

- These learned features can then be used to improve performance on the target task.
- It helps when labeled data is scarce but unlabeled data is abundant.

#### 3.7 Unsupervised Transfer Learning

This approach clusters unlabeled target data with the help of large auxiliary unlabeled datasets.

- The goal is to learn common features that help cluster and understand the target data better.
- Useful when no labeled data is available in either domain.


### 4. ⚠️ Avoiding Negative Transfer

Negative transfer happens when transferring knowledge from the source domain actually harms the performance on the target task.

To avoid this:

- **Reject Bad Information:**  
  Identify and ignore harmful or irrelevant knowledge from the source domain.

- **Choose the Right Source Task:**  
  Select source tasks that are closely related to the target task to maximize positive transfer.

- **Model Task Similarity:**  
  Explicitly model relationships between tasks to guide transfer learning and reduce the risk of negative transfer.


### 5. 🔍 Pre-training in Practice: CV and NLP

#### Computer Vision (CV)

- Pre-training on large datasets like ImageNet has become standard.
- Models trained on ImageNet learn general visual features that can be fine-tuned for specific tasks with smaller datasets.

#### Natural Language Processing (NLP)

- Pre-trained word embeddings (e.g., Word2Vec, GloVe) are widely used to provide initial word representations.
- However, traditional embeddings are shallow and context-insensitive—they assign the same vector to a word regardless of its meaning in context.
- Only the embedding layer is pre-trained; the rest of the model is trained from scratch.
- Recent advances (not covered in this lecture) include contextual embeddings like BERT and GPT, which address these limitations.


### Summary

Transfer learning is a versatile and essential technique in modern machine learning that helps overcome data scarcity and domain differences by reusing knowledge from related tasks or domains. It includes various approaches such as model fine-tuning, multi-task learning, domain adaptation, zero-shot learning, and more. Understanding when and how to apply these methods, and how to avoid negative transfer, is key to building effective machine learning systems in real-world scenarios.