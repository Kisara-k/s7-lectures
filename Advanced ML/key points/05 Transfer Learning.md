## 5. Transfer Learning

## Key Points

#### 1. 📊 Transfer Learning Basics  
- Deep learning models typically require more than 50,000 labeled data items for effective training.  
- Transfer learning reuses a model developed for one task/domain as the starting point for another task/domain.  
- Transfer learning addresses challenges like limited labeled data in the target domain and differing data distributions between source and target domains.

#### 2. 🔄 Transfer Learning Paradigms  
- **Inductive transfer learning:** Labeled data available in the target domain; goal is to improve target task performance using knowledge from other tasks.  
- **Transductive transfer learning:** Labeled data only in the source domain; no labeled data in the target domain; focuses on domain adaptation.  
- **Unsupervised transfer learning:** No labeled data in either source or target domains; aims to learn useful representations from unlabeled data.

#### 3. 🛠️ Model Fine-tuning  
- Fine-tuning involves pre-training on source data and then adapting the model on target data.  
- To avoid overfitting with limited target data, some layers can be frozen while others are trained.  
- In image tasks, usually the first few layers are transferred; in speech tasks, often the last few layers are transferred.

#### 4. 🤝 Multi-task Learning  
- Multi-task learning trains a model on multiple related tasks simultaneously using shared hidden layers.  
- It improves generalization by learning shared representations useful across tasks.  
- Example: Multilingual speech recognition models share hidden layers for different languages.

#### 5. 🌐 Domain Adaptation  
- Domain adaptation handles the same task but different data distributions between source and target domains.  
- Domain-adversarial training uses a feature extractor, domain classifier, and label predictor to learn domain-invariant features.  
- The domain classifier tries to distinguish source vs. target domain, while the feature extractor tries to fool it.

#### 6. 🐾 Zero-shot Learning  
- Zero-shot learning recognizes classes in the target domain without any training examples for those classes.  
- It uses class attributes or semantic embeddings (e.g., word vectors) to represent classes.  
- The model maps inputs and class attributes into a shared embedding space to find the closest class.

#### 7. 🔄 Covariate Shift  
- Covariate shift occurs when input data distribution changes between training and testing, but the conditional distribution of outputs given inputs remains the same.  
- Formally, $P_S(x) \neq P_T(x)$ but $P_S(y|x) = P_T(y|x)$.  
- Examples include changes in lighting for image recognition or accents in speech recognition.

#### 8. 📚 Self-taught and Unsupervised Transfer Learning  
- Self-taught learning extracts better feature representations from large unlabeled source data to improve target task performance.  
- Unsupervised transfer learning clusters small target unlabeled data with large auxiliary unlabeled data to learn shared features.

#### 9. ⚠️ Avoiding Negative Transfer  
- Negative transfer occurs when transfer learning decreases target task performance.  
- Strategies to avoid it include rejecting harmful source knowledge, choosing the best source task, and modeling task similarity explicitly.

#### 10. 🖼️ Pre-training in CV and NLP  
- Pre-training on ImageNet is standard in computer vision to learn general visual features.  
- Pre-trained word embeddings are essential in NLP but are shallow and context-insensitive, only pre-training the embedding layer.



<br>

