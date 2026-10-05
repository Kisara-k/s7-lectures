## 11. Handling Data Imbalance and Data Augmentation

## Questions

#### 1. Which of the following statements correctly describe the impact of data imbalance on machine learning classifiers?  
A) Classifiers tend to achieve high overall accuracy but perform poorly on the minority class.  
B) Data imbalance can introduce bias that reverses the actual relationship between variables.  
C) Imbalanced datasets always improve the classifier’s ability to detect rare events.  
D) Class imbalance causes decision boundaries to shift towards the majority class region.  

#### 2. What are the primary factors governing the class imbalance problem?  
A) Degree of class imbalance and complexity of the concept represented by the data.  
B) Overall size of the training data and the type of classifier used.  
C) The number of features and the dimensionality of the dataset.  
D) The imbalance ratio and the presence of class overlap or small disjoints.  

#### 3. Why do standard machine learning algorithms often fail on skewed datasets?  
A) Loss functions minimize overall error, giving little incentive to improve minority class predictions.  
B) Decision thresholds like 0.5 assume balanced classes, which is invalid in imbalanced data.  
C) Distance-based models like k-NN are biased towards the minority class due to fewer neighbors.  
D) Probability-based models such as Naive Bayes priors are dominated by the majority class distribution.  

#### 4. Which of the following metrics are more appropriate for evaluating classifiers on imbalanced datasets?  
A) Accuracy and overall error rate.  
B) F1 score and balanced accuracy score.  
C) Precision and recall, considering their trade-off.  
D) Confusion matrix alone without derived metrics.  

#### 5. Regarding undersampling techniques for handling class imbalance, which statements are true?  
A) Random undersampling removes random samples from the majority class but risks losing important information.  
B) Tomek links remove majority class samples that are close to minority class samples to reduce class overlap.  
C) Undersampling always improves model performance without any drawbacks.  
D) Undersampling techniques increase the size of the minority class.  

#### 6. Which of the following correctly describe SMOTE and its variants?  
A) SMOTE generates synthetic minority class samples by interpolation between existing minority points.  
B) Borderline-SMOTE focuses on generating samples near the decision boundary between classes.  
C) SMOTE-NC is designed for datasets with mixed nominal and continuous features.  
D) SMOTE always reduces runtime and computational cost in large datasets.  

#### 7. What are the advantages of ADASYN over SMOTE in oversampling minority classes?  
A) ADASYN generates more synthetic data from minority samples that are harder to classify.  
B) ADASYN ignores the density distribution of minority class samples.  
C) ADASYN uses a weighted distribution to focus on low-density minority regions.  
D) ADASYN always produces fewer synthetic samples than SMOTE.  

#### 8. Which of the following statements about text data augmentation strategies are correct?  
A) Word-level augmentation modifies individual words while trying to preserve sentence meaning.  
B) Phrase-level augmentation involves paraphrasing entire sentences to increase diversity.  
C) Sentence-level augmentation can use rule-based, synonym-based, or neural paraphrasing methods.  
D) Language-model-based augmentation can generate context-aware paraphrases and synthetic labeled examples.  

#### 9. What are the risks associated with higher-level text augmentation methods such as paraphrasing and language-model generation?  
A) They may unintentionally alter the original meaning of the text.  
B) They always preserve the semantic consistency of the original sentence.  
C) They have a higher risk of generating unreliable or irrelevant data compared to word-level methods.  
D) They cannot generate diverse examples beyond simple word replacements.  

#### 10. Why is effective data augmentation not simply about generating more data?  
A) Because generating more data always leads to overfitting.  
B) Because the augmented data must be useful, diverse, and reliable to improve model generalization.  
C) Because excessive augmentation can change the intended meaning and reduce data quality.  
D) Because only synthetic data generation is effective, while other methods are not useful.



<br>

## Answers

#### 1. Which of the following statements correctly describe the impact of data imbalance on machine learning classifiers?  
A) ✓ Classifiers tend to achieve high overall accuracy but perform poorly on the minority class due to bias toward the majority.  
B) ✓ Data imbalance can introduce bias that may distort or even reverse the true relationship between variables.  
C) ✗ Imbalanced datasets generally degrade the classifier’s ability to detect rare events, not improve it.  
D) ✗ Decision boundaries tend to drift toward the majority class region, not minority.  

**Correct:** A, B


#### 2. What are the primary factors governing the class imbalance problem?  
A) ✓ Degree of class imbalance and complexity of the concept are the main factors affecting imbalance impact.  
B) ✓ Overall size of training data and classifier type also influence the problem but are secondary.  
C) ✗ Number of features and dimensionality are not primary factors in class imbalance.  
D) ✓ Imbalance ratio and class overlap (complexity) affect how difficult the problem is.  

**Correct:** A, B, D


#### 3. Why do standard machine learning algorithms often fail on skewed datasets?  
A) ✓ Loss functions minimize overall error, so minority class errors contribute little to total loss.  
B) ✓ Thresholds like 0.5 assume balanced classes, causing poor minority class detection.  
C) ✗ Distance-based models are biased toward the majority class, not minority, due to more neighbors.  
D) ✓ Probability-based models like Naive Bayes are dominated by majority class priors.  

**Correct:** A, B, D


#### 4. Which of the following metrics are more appropriate for evaluating classifiers on imbalanced datasets?  
A) ✗ Accuracy is misleading on imbalanced data because it favors the majority class.  
B) ✓ F1 score and balanced accuracy better reflect performance on both classes.  
C) ✓ Precision and recall are critical to understand trade-offs in minority class detection.  
D) ✗ Confusion matrix alone is raw data; derived metrics are needed for meaningful evaluation.  

**Correct:** B, C


#### 5. Regarding undersampling techniques for handling class imbalance, which statements are true?  
A) ✓ Random undersampling removes majority samples but risks losing important information.  
B) ✓ Tomek links remove majority samples near minority samples to reduce class overlap.  
C) ✗ Undersampling can degrade performance due to information loss; it is not always beneficial.  
D) ✗ Undersampling reduces majority class size; it does not increase minority class size.  

**Correct:** A, B


#### 6. Which of the following correctly describe SMOTE and its variants?  
A) ✓ SMOTE creates synthetic minority samples by interpolating between existing minority points.  
B) ✓ Borderline-SMOTE focuses on samples near the decision boundary to improve class separation.  
C) ✓ SMOTE-NC handles datasets with both nominal and continuous features.  
D) ✗ SMOTE can increase runtime, especially on large datasets; it does not reduce computational cost.  

**Correct:** A, B, C


#### 7. What are the advantages of ADASYN over SMOTE in oversampling minority classes?  
A) ✓ ADASYN generates more synthetic data from harder-to-classify minority samples.  
B) ✗ ADASYN explicitly considers density distribution, unlike SMOTE.  
C) ✓ ADASYN uses weighted distribution to focus on low-density minority regions.  
D) ✗ ADASYN does not necessarily produce fewer samples; it adapts sample generation based on difficulty.  

**Correct:** A, C


#### 8. Which of the following statements about text data augmentation strategies are correct?  
A) ✓ Word-level augmentation modifies individual words while preserving meaning as much as possible.  
B) ✗ Phrase-level augmentation modifies groups of words or phrases, not entire sentences (that’s sentence-level).  
C) ✓ Sentence-level augmentation includes rule-based, synonym-based, and neural paraphrasing methods.  
D) ✓ Language-model-based augmentation can generate context-aware paraphrases and synthetic labeled data.  

**Correct:** A, C, D


#### 9. What are the risks associated with higher-level text augmentation methods such as paraphrasing and language-model generation?  
A) ✓ They may unintentionally alter the original meaning, risking semantic drift.  
B) ✗ They do not always preserve semantic consistency; risk of meaning change is higher.  
C) ✓ Higher-level methods have greater risk of generating unreliable or irrelevant data than word-level methods.  
D) ✗ They can generate diverse examples beyond simple word replacements, which is their advantage.  

**Correct:** A, C


#### 10. Why is effective data augmentation not simply about generating more data?  
A) ✗ Generating more data does not always lead to overfitting; sometimes it helps generalization.  
B) ✓ Augmented data must be useful, diverse, and reliable to improve model generalization.  
C) ✓ Excessive or careless augmentation can change intended meaning and reduce data quality.  
D) ✗ Not only synthetic data generation is effective; other augmentation methods also contribute.  

**Correct:** B, C