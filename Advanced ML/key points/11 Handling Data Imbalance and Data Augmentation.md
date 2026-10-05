## 11. Handling Data Imbalance and Data Augmentation

## Key Points

#### 1. 📊 Data Imbalance  
- Data imbalance means one class has a significantly higher percentage of examples than another.  
- Majority class refers to the class with more instances; minority class refers to the underrepresented class.  
- Imbalance Ratio (IR) = Total number of majority class examples / Total number of minority class examples.  
- Real-world examples of imbalance include fraud detection (~0.1-0.2% fraud), rare disease screening (<1%), manufacturing defects, customer churn, and spam detection.  

#### 2. ⚠️ Impact of Data Imbalance on Machine Learning  
- Standard algorithms minimize overall error, causing bias toward the majority class.  
- Decision boundaries tend to drift toward the minority class region due to imbalanced class probabilities.  
- Distance- and probability-based models (e.g., k-NN, Naive Bayes) are biased toward the majority class because of class dominance in neighborhoods or priors.  

#### 3. 📏 Metrics for Imbalanced Data  
- Accuracy is not suitable for imbalanced datasets.  
- Precision measures the proportion of true positives among predicted positives.  
- Recall measures the proportion of true positives detected among all actual positives.  
- F1 score is the harmonic mean of precision and recall: F1 = 2 * (Precision * Recall) / (Precision + Recall).  
- Balanced accuracy is the average recall obtained in each class.  

#### 4. 🔄 Techniques to Address Class Imbalance  
- **Under-sampling:** Randomly remove majority class samples; risk of losing information.  
- **Tomek Links:** Remove majority class samples close to minority class samples to clean class boundaries.  
- **Over-sampling:** Generate more minority class samples to balance the dataset.  
- **Random Over-sampling:** Duplicate minority class samples; risk of overfitting.  
- **SMOTE (Synthetic Minority Over-sampling Technique):** Creates synthetic minority samples by interpolating between existing minority points.  
- SMOTE disadvantages: May increase class overlap; increases runtime on large datasets.  
- SMOTE variants include Borderline-SMOTE, SMOTE-NC (for mixed numeric and categorical data), and SMOTEN (for nominal data).  
- **ADASYN (Adaptive Synthetic Sampling):** Focuses on generating synthetic samples for harder-to-classify minority examples in low-density areas.  

#### 5. 🖼️ Data Augmentation  
- Data augmentation increases training data size and diversity by creating new examples from existing data while preserving essential information.  
- It improves model generalization and reduces overfitting, especially when original datasets are small or imbalanced.  

#### 6. ✍️ Text Data Augmentation Strategies  
- Word-level augmentation: Synonym replacement, random insertion, deletion, and swapping of words.  
- Phrase-level augmentation: Phrase replacement, paraphrasing, insertion/deletion, and entity replacement.  
- Sentence-level augmentation: Paraphrasing using rule-based, synonym-based, neural, or LLM-based methods.  
- Contextual augmentation uses masked language models and transformer/LLM models to generate context-aware alternatives, paraphrases, or synthetic labeled examples.  

#### 7. 🎯 Trade-offs in Text Augmentation  
- Higher-level augmentations (sentence, synthetic data) generate more diversity but have a higher risk of changing the original meaning.  
- Effective augmentation balances diversity with preserving semantic meaning and label consistency.  

#### 8. 📊 Factors Governing Class Imbalance Impact  
- Degree of class imbalance (Imbalance Ratio).  
- Complexity of the concept (affected by class overlap and small disjoints).  
- Overall size of training data.  
- Type of classifier used.  
- Large imbalance may not affect classification if the concept is easy to learn.



<br>

