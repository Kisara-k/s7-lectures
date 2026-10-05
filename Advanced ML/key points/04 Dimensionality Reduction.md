## 4. Dimensionality Reduction

## Key Points

#### 1. 📊 High-Dimensional Data and Curse of Dimensionality  
- High-dimensional data means data with a large number of features (dimensions).  
- Examples include Amazon review datasets, brain imaging, and image data with millions of features.  
- The curse of dimensionality refers to problems unique to high-dimensional spaces, such as:  
  - Optimization difficulty increases exponentially with dimensions.  
  - Distances between near and far points become similar (loss of contrast).  
  - Presence of irrelevant and highly correlated dimensions.  
  - Partitioning space becomes exponentially complex (2^d cells if dividing each dimension once).  
  - Pairwise distances become skewed.

#### 2. 🔍 Subspace Models  
- High-dimensional data often lies on a much smaller subspace or manifold within the full space.  
- Standard transformations (translation, rotation, scaling) produce data on low-dimensional manifolds embedded in high-dimensional space.  
- Subspace methods aim to discover this low-dimensional space for efficient modeling.  
- Linear subspaces include lines (D=2), planes (D=3), and hyperplanes (dimensions between 1 and D-1).

#### 3. 🎯 Dimensionality Reduction: Purpose and Benefits  
- Dimensionality reduction projects data from n dimensions to d dimensions (d << n) while preserving distances or variance.  
- Benefits include:  
  - Solving the curse of dimensionality.  
  - Data visualization and understanding class distributions.  
  - Improving interpretability of models.  
  - Speeding up algorithms by reducing computational complexity.  
  - Better generalization by removing noise and irrelevant features.  
  - Efficient use of resources (time, memory, communication).  
  - Data compression and modeling on lower-dimensional manifolds.

#### 4. 🛠️ Dimensionality Reduction Methods  
- **Feature Selection:** Selects a subset of original features.  
  - Filters use heuristics (e.g., ANOVA, Chi-Square, LDA).  
  - Wrappers select features based on model performance iteratively.  
  - Embedded methods combine filter and wrapper approaches during model training.  
- **Feature Extraction:** Creates new features from original ones.  
  - Examples include PCA, Autoencoders, FastMap, Random Projections, and Multi-Dimensional Scaling (MDS).

#### 5. 📐 Principal Component Analysis (PCA)  
- PCA finds axes (principal components) that maximize variance in the data.  
- Steps: center data, compute covariance matrix, find eigenvectors and eigenvalues, sort by eigenvalues, project data onto top components.  
- PCA minimizes reconstruction error or equivalently maximizes variance captured.  
- Principal components are orthogonal eigenvectors of the covariance matrix, ranked by eigenvalues.  
- PCA is optimal for linear dimensionality reduction but sensitive to outliers and nonlinearities.  
- Number of components chosen based on eigenvalues; small eigenvalues correspond to less important components.

#### 6. 🔄 Multi-Dimensional Scaling (MDS)  
- MDS maps data into a low-dimensional space by minimizing "stress," preserving pairwise distances.  
- Uses iterative optimization (steepest descent).  
- Computational complexity is O(N²), making it expensive for large datasets.



<br>

