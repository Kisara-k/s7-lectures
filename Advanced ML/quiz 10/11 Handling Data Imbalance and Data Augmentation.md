## 11. Handling Data Imbalance and Data Augmentation

## Questions

#### 1. Which of the following statements correctly describe the impact of data imbalance on machine learning classifiers?  
A) Imbalanced datasets always improve the classifier’s ability to detect rare events.  
B) Class imbalance causes decision boundaries to shift towards the majority class region.  
C) Classifiers tend to achieve high overall accuracy but perform poorly on the minority class.  
D) Data imbalance can introduce bias that reverses the actual relationship between variables.  

#### 2. What are the primary factors governing the class imbalance problem?  
A) The imbalance ratio and the presence of class overlap or small disjoints.  
B) The number of features and the dimensionality of the dataset.  
C) Degree of class imbalance and complexity of the concept represented by the data.  
D) Overall size of the training data and the type of classifier used.  

#### 3. Why do standard machine learning algorithms often fail on skewed datasets?  
A) Distance-based models like k-NN are biased towards the minority class due to fewer neighbors.  
B) Decision thresholds like 0.5 assume balanced classes, which is invalid in imbalanced data.  
C) Probability-based models such as Naive Bayes priors are dominated by the majority class distribution.  
D) Loss functions minimize overall error, giving little incentive to improve minority class predictions.  

#### 4. Which of the following metrics are more appropriate for evaluating classifiers on imbalanced datasets?  
A) F1 score and balanced accuracy score.  
B) Accuracy and overall error rate.  
C) Precision and recall, considering their trade-off.  
D) Confusion matrix alone without derived metrics.  

#### 5. Regarding undersampling techniques for handling class imbalance, which statements are true?  
A) Undersampling always improves model performance without any drawbacks.  
B) Undersampling techniques increase the size of the minority class.  
C) Tomek links remove majority class samples that are close to minority class samples to reduce class overlap.  
D) Random undersampling removes random samples from the majority class but risks losing important information.  

#### 6. Which of the following correctly describe SMOTE and its variants?  
A) SMOTE always reduces runtime and computational cost in large datasets.  
B) SMOTE generates synthetic minority class samples by interpolation between existing minority points.  
C) SMOTE-NC is designed for datasets with mixed nominal and continuous features.  
D) Borderline-SMOTE focuses on generating samples near the decision boundary between classes.  

#### 7. What are the advantages of ADASYN over SMOTE in oversampling minority classes?  
A) ADASYN ignores the density distribution of minority class samples.  
B) ADASYN uses a weighted distribution to focus on low-density minority regions.  
C) ADASYN generates more synthetic data from minority samples that are harder to classify.  
D) ADASYN always produces fewer synthetic samples than SMOTE.  

#### 8. Which of the following statements about text data augmentation strategies are correct?  
A) Language-model-based augmentation can generate context-aware paraphrases and synthetic labeled examples.  
B) Word-level augmentation modifies individual words while trying to preserve sentence meaning.  
C) Phrase-level augmentation involves paraphrasing entire sentences to increase diversity.  
D) Sentence-level augmentation can use rule-based, synonym-based, or neural paraphrasing methods.  

#### 9. What are the risks associated with higher-level text augmentation methods such as paraphrasing and language-model generation?  
A) They may unintentionally alter the original meaning of the text.  
B) They always preserve the semantic consistency of the original sentence.  
C) They cannot generate diverse examples beyond simple word replacements.  
D) They have a higher risk of generating unreliable or irrelevant data compared to word-level methods.  

#### 10. Why is effective data augmentation not simply about generating more data?  
A) Because only synthetic data generation is effective, while other methods are not useful.  
B) Because excessive augmentation can change the intended meaning and reduce data quality.  
C) Because the augmented data must be useful, diverse, and reliable to improve model generalization.  
D) Because generating more data always leads to overfitting.  



<br>

## Answers

#### 1. Which of the following statements correctly describe the impact of data imbalance on machine learning classifiers?  
A) ✗ Imbalanced datasets generally degrade the classifier’s ability to detect rare events, not improve it.  
B) ✗ Decision boundaries tend to drift toward the majority class region, not minority.  
C) ✓ Classifiers tend to achieve high overall accuracy but perform poorly on the minority class due to bias toward the majority.  
D) ✓ Data imbalance can introduce bias that may distort or even reverse the true relationship between variables.  

**Correct:** C, D


#### 2. What are the primary factors governing the class imbalance problem?  
A) ✓ Imbalance ratio and class overlap (complexity) affect how difficult the problem is.  
B) ✗ Number of features and dimensionality are not primary factors in class imbalance.  
C) ✓ Degree of class imbalance and complexity of the concept are the main factors affecting imbalance impact.  
D) ✓ Overall size of training data and classifier type also influence the problem but are secondary.  

**Correct:** A, C, D


#### 3. Why do standard machine learning algorithms often fail on skewed datasets?  
A) ✗ Distance-based models are biased toward the majority class, not minority, due to more neighbors.  
B) ✓ Thresholds like 0.5 assume balanced classes, causing poor minority class detection.  
C) ✓ Probability-based models like Naive Bayes are dominated by majority class priors.  
D) ✓ Loss functions minimize overall error, so minority class errors contribute little to total loss.  

**Correct:** B, C, D


#### 4. Which of the following metrics are more appropriate for evaluating classifiers on imbalanced datasets?  
A) ✓ F1 score and balanced accuracy better reflect performance on both classes.  
B) ✗ Accuracy is misleading on imbalanced data because it favors the majority class.  
C) ✓ Precision and recall are critical to understand trade-offs in minority class detection.  
D) ✗ Confusion matrix alone is raw data; derived metrics are needed for meaningful evaluation.  

**Correct:** A, C


#### 5. Regarding undersampling techniques for handling class imbalance, which statements are true?  
A) ✗ Undersampling can degrade performance due to information loss; it is not always beneficial.  
B) ✗ Undersampling reduces majority class size; it does not increase minority class size.  
C) ✓ Tomek links remove majority samples near minority samples to reduce class overlap.  
D) ✓ Random undersampling removes majority samples but risks losing important information.  

**Correct:** C, D


#### 6. Which of the following correctly describe SMOTE and its variants?  
A) ✗ SMOTE can increase runtime, especially on large datasets; it does not reduce computational cost.  
B) ✓ SMOTE creates synthetic minority samples by interpolating between existing minority points.  
C) ✓ SMOTE-NC handles datasets with both nominal and continuous features.  
D) ✓ Borderline-SMOTE focuses on samples near the decision boundary to improve class separation.  

**Correct:** B, C, D


#### 7. What are the advantages of ADASYN over SMOTE in oversampling minority classes?  
A) ✗ ADASYN explicitly considers density distribution, unlike SMOTE.  
B) ✓ ADASYN uses weighted distribution to focus on low-density minority regions.  
C) ✓ ADASYN generates more synthetic data from harder-to-classify minority samples.  
D) ✗ ADASYN does not necessarily produce fewer samples; it adapts sample generation based on difficulty.  

**Correct:** B, C


#### 8. Which of the following statements about text data augmentation strategies are correct?  
A) ✓ Language-model-based augmentation can generate context-aware paraphrases and synthetic labeled data.  
B) ✓ Word-level augmentation modifies individual words while preserving meaning as much as possible.  
C) ✗ Phrase-level augmentation modifies groups of words or phrases, not entire sentences (that’s sentence-level).  
D) ✓ Sentence-level augmentation includes rule-based, synonym-based, and neural paraphrasing methods.  

**Correct:** A, B, D


#### 9. What are the risks associated with higher-level text augmentation methods such as paraphrasing and language-model generation?  
A) ✓ They may unintentionally alter the original meaning, risking semantic drift.  
B) ✗ They do not always preserve semantic consistency; risk of meaning change is higher.  
C) ✗ They can generate diverse examples beyond simple word replacements, which is their advantage.  
D) ✓ Higher-level methods have greater risk of generating unreliable or irrelevant data than word-level methods.  

**Correct:** A, D


#### 10. Why is effective data augmentation not simply about generating more data?  
A) ✗ Not only synthetic data generation is effective; other augmentation methods also contribute.  
B) ✓ Excessive or careless augmentation can change intended meaning and reduce data quality.  
C) ✓ Augmented data must be useful, diverse, and reliable to improve model generalization.  
D) ✗ Generating more data does not always lead to overfitting; sometimes it helps generalization.  

**Correct:** B, C