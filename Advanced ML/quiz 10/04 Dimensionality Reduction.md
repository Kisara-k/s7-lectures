## 4. Dimensionality Reduction

## Questions

#### 1. Which of the following statements correctly describe the "Curse of Dimensionality"?  
A) High correlation among dimensions can complicate analysis  
B) Optimization problems become exponentially harder as dimensionality increases  
C) Partitioning the space becomes easier as the number of dimensions increases  
D) Distances between near and far neighbors become more distinct with higher dimensions  

#### 2. Why is dimensionality reduction often necessary when working with high-dimensional data such as images or acoustic signals?  
A) Because there is usually insufficient training data to model the full high-dimensional space effectively  
B) Because the data typically lie on a lower-dimensional manifold within the high-dimensional space  
C) Because dimensionality reduction always increases the number of features for better modeling  
D) Because standard transformations like rotations and scalings produce data that occupy a low-dimensional manifold  

#### 3. Which of the following are valid use cases for dimensionality reduction beyond addressing the curse of dimensionality?  
A) Increasing the dimensionality of the dataset for better visualization  
B) Improving interpretability of predictors  
C) Speeding up algorithms whose complexity depends on the number of features  
D) Removing noise and improving data quality  

#### 4. Regarding feature selection methods, which of the following statements are true?  
A) Wrappers select features by training models and iteratively adding or removing features based on model performance  
B) Feature selection always creates new features by combining existing ones  
C) Embedded methods combine aspects of both filters and wrappers  
D) Filters select features based on heuristics such as ANOVA or Chi-Square tests  

#### 5. Which of the following correctly describe Principal Component Analysis (PCA)?  
A) PCA finds the linear subspace that maximizes the explained variance of the data  
B) PCA minimizes the reconstruction error when projecting data onto principal components  
C) PCA requires the data to be Gaussian distributed to work properly  
D) PCA components are eigenvectors of the covariance matrix and are orthogonal to each other  

#### 6. What are some limitations or disadvantages of PCA?  
A) It only works for datasets with fewer than 1000 dimensions  
B) It always perfectly preserves all information in the original data  
C) It is sensitive to outliers and nonlinearities in the data  
D) It is computationally expensive but can be improved with random sampling  

#### 7. When deciding how many principal components to keep after PCA, which considerations are correct?  
A) The number of components should always equal the original number of features to avoid losing information  
B) Components with small eigenvalues can often be discarded with minimal information loss  
C) The eigenvalues indicate the amount of variance explained by each principal component  
D) Selecting fewer components reduces dimensionality but may lose some variance in the data  

#### 8. Which of the following statements about subspace models and manifolds are true?  
A) Subspace methods aim to discover and exploit these lower-dimensional manifolds for efficient modeling  
B) High-dimensional data often lie on a low-dimensional manifold embedded in the high-dimensional space  
C) Standard transformations like translations and rotations produce data that fill the entire high-dimensional space uniformly  
D) A hyperplane in D-dimensional space can have dimensionality ranging from 1 to D-1  

#### 9. Multi-Dimensional Scaling (MDS) as a feature extraction method:  
A) Has a computational complexity of O(N) for N data points  
B) Is typically faster than PCA for very large datasets  
C) Attempts to map items into a k-dimensional space by minimizing a stress function  
D) Uses a steepest descent algorithm to iteratively reduce stress by moving points  

#### 10. Which of the following statements about dimensionality reduction methods are correct?  
A) Feature extraction methods compute new features from the original features, often reducing dimensionality  
B) Feature selection methods always create new features by combining existing ones  
C) Dimensionality reduction can improve generalization by reducing overfitting caused by irrelevant features  
D) Dimensionality reduction can be used for data compression and more efficient resource usage  



<br>

## Answers

#### 1. Which of the following statements correctly describe the "Curse of Dimensionality"?  
A) ✓ High correlation among dimensions can complicate analysis  
B) ✓ Optimization problems become exponentially harder as dimensionality increases  
C) ✗ Partitioning the space becomes easier as the number of dimensions increases (it becomes harder)  
D) ✗ Distances between near and far neighbors become more distinct with higher dimensions (actually, distances become more similar)  

**Correct:** A, B


#### 2. Why is dimensionality reduction often necessary when working with high-dimensional data such as images or acoustic signals?  
A) ✓ Insufficient training data to model the full high-dimensional space effectively  
B) ✓ Data typically lie on a lower-dimensional manifold within the high-dimensional space  
C) ✗ Dimensionality reduction does not increase the number of features; it reduces or transforms them  
D) ✓ Standard transformations produce data that occupy a low-dimensional manifold  

**Correct:** A, B, D


#### 3. Which of the following are valid use cases for dimensionality reduction beyond addressing the curse of dimensionality?  
A) ✗ Increasing dimensionality is not a use case; dimensionality reduction reduces it  
B) ✓ Improving interpretability of predictors  
C) ✓ Speeding up algorithms whose complexity depends on the number of features  
D) ✓ Removing noise and improving data quality  

**Correct:** B, C, D


#### 4. Regarding feature selection methods, which of the following statements are true?  
A) ✓ Wrappers iteratively select features based on model performance  
B) ✗ Feature selection does not create new features; it selects existing ones  
C) ✓ Embedded methods combine filter and wrapper qualities  
D) ✓ Filters select features based on heuristics like ANOVA or Chi-Square  

**Correct:** A, C, D


#### 5. Which of the following correctly describe Principal Component Analysis (PCA)?  
A) ✓ PCA finds the linear subspace maximizing explained variance  
B) ✓ PCA minimizes reconstruction error when projecting data onto principal components  
C) ✗ PCA does not require Gaussian data; it works on any multidimensional dataset  
D) ✓ PCA components are eigenvectors of the covariance matrix and are orthogonal  

**Correct:** A, B, D


#### 6. What are some limitations or disadvantages of PCA?  
A) ✗ PCA can be applied to very high-dimensional data, not limited to fewer than 1000 dimensions  
B) ✗ PCA does not perfectly preserve all information; some variance is lost when reducing dimensions  
C) ✓ Sensitive to outliers and nonlinearities  
D) ✓ Computationally expensive but improvable with random sampling  

**Correct:** C, D


#### 7. When deciding how many principal components to keep after PCA, which considerations are correct?  
A) ✗ Keeping all components defeats the purpose of dimensionality reduction  
B) ✓ Components with small eigenvalues can often be discarded with minimal information loss  
C) ✓ Eigenvalues indicate variance explained by each principal component  
D) ✓ Selecting fewer components reduces dimensionality but may lose some variance  

**Correct:** B, C, D


#### 8. Which of the following statements about subspace models and manifolds are true?  
A) ✓ Subspace methods aim to discover and exploit these lower-dimensional manifolds  
B) ✓ High-dimensional data often lie on a low-dimensional manifold embedded in the high-dimensional space  
C) ✗ Standard transformations produce data on low-dimensional manifolds, not filling the entire space uniformly  
D) ✓ A hyperplane in D-dimensional space can have dimensionality from 1 to D-1  

**Correct:** A, B, D


#### 9. Multi-Dimensional Scaling (MDS) as a feature extraction method:  
A) ✗ Running time is O(N²), not O(N)  
B) ✗ MDS is typically slower than PCA for large datasets due to O(N²) complexity  
C) ✓ Maps items into k-dimensional space by minimizing stress  
D) ✓ Uses steepest descent to iteratively reduce stress by moving points  

**Correct:** C, D


#### 10. Which of the following statements about dimensionality reduction methods are correct?  
A) ✓ Feature extraction computes new features from original features, often reducing dimensionality  
B) ✗ Feature selection does not create new features; it selects existing ones  
C) ✓ Dimensionality reduction can improve generalization by reducing overfitting from irrelevant features  
D) ✓ Dimensionality reduction can be used for compression and more efficient resource usage  

**Correct:** A, C, D