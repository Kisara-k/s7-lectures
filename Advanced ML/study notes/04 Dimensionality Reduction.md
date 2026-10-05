## 4. Dimensionality Reduction

## Study Notes

### 1. 📏 Understanding Dimensionality and High-Dimensional Data

When we talk about **dimensionality** in data, we mean the number of features or variables that describe each data point. For example, if you have a dataset of images, each pixel can be considered a feature, so an image with 1000 pixels has 1000 dimensions.

#### What is High-Dimensional Data?

High-dimensional data means data with a very large number of features. This is common in many real-world applications:

- **Amazon Review Dataset:** Each review might be represented by thousands of features, such as word counts or sentiment scores.
- **Brain Imaging:** Brain scans can have millions of voxels (3D pixels), each representing a feature.
- **Image Data:** A color image of size 1800 x 1200 pixels has roughly 6.5 million features (3 color channels × 1800 × 1200).

#### Why is High Dimensionality a Problem?

High-dimensional data brings unique challenges, often called the **Curse of Dimensionality**. This term covers many issues that arise when working with data in spaces with many dimensions, which do not appear in low-dimensional data.

Some key problems include:

- **Optimization Difficulty:** Algorithms that work well in low dimensions become exponentially harder to optimize as dimensions increase.
- **Distance Concentration:** In high dimensions, the difference between the nearest and farthest points becomes negligible. This means distances lose their meaning, making clustering or nearest neighbor searches unreliable.
- **Irrelevant and Correlated Features:** Many features might be irrelevant or highly correlated, which can confuse models.
- **Partitioning Complexity:** Dividing the space into meaningful regions becomes difficult because the number of cells grows exponentially with dimensions (e.g., dividing each dimension once creates 2^d cells).
- **Skewed Pairwise Distances:** Distances between points become skewed, affecting algorithms relying on distance metrics.


### 2. 🔍 Subspace Models: Finding the True Structure in High Dimensions

Although data might live in a very high-dimensional space, often the **intrinsic dimensionality** is much lower. This means the data actually lies on or near a smaller subspace or manifold within the high-dimensional space.

#### What is a Subspace?

A **subspace** is a smaller-dimensional space embedded inside the larger space. For example:

- In 2D (a plane), a subspace could be a line.
- In 3D, a subspace could be a line or a plane.
- In higher dimensions, a subspace is called a **hyperplane** with dimensionality between 1 and D-1.

#### Why Subspace Models Matter

- Real-world signals like images or audio often vary due to transformations such as rotation, translation, or scaling. These transformations form a low-dimensional manifold inside the high-dimensional space.
- Learning models directly in the full high-dimensional space is often impossible due to insufficient data.
- The goal of subspace methods is to **discover this low-dimensional space** where the data actually lies, enabling more efficient and accurate modeling.


### 3. 🎯 Dimensionality Reduction: The Core Idea and Its Benefits

#### What is Dimensionality Reduction?

Dimensionality reduction means transforming data from a high-dimensional space (with many features) into a lower-dimensional space while preserving important properties, such as distances or variance.

The main goal is to **project** the original n-dimensional data points into a d-dimensional space (where d << n) so that the structure of the data is preserved as much as possible.

#### Why Reduce Dimensionality?

Besides solving the curse of dimensionality, dimensionality reduction is useful for:

- **Data Visualization:** It’s easier to visualize data in 2D or 3D to understand distribution, class separation, or feature importance.
- **Interpretability:** Models built on fewer features are easier to understand.
- **Speeding Up Algorithms:** Many algorithms have complexity that depends on the number of features, so reducing dimensions speeds up training and inference.
- **Better Generalization:** Reducing dimensions can remove noise and irrelevant features, improving model performance.
- **Noise Removal:** Helps improve data quality by filtering out irrelevant information.
- **Resource Efficiency:** Saves memory, computation time, and communication bandwidth.
- **Compression:** Reduces storage requirements.
- **Data Modeling:** Makes it easier to model data that lies on a lower-dimensional manifold.


### 4. 🛠️ Methods of Dimensionality Reduction

There are two main approaches to dimensionality reduction:

#### 4.1 Feature Selection

This method selects a subset of the original features without creating new ones. The goal is to keep the most informative features and discard the rest.

- **Filters:** Use heuristics or statistical tests to select features independently of any model. Examples include ANOVA, Chi-Square tests, and Linear Discriminant Analysis (LDA).
- **Wrappers:** Use a predictive model to evaluate subsets of features. Features are added or removed based on model performance.
- **Embedded Methods:** Combine filter and wrapper approaches by selecting features during model training (e.g., Lasso regression).

#### 4.2 Feature Extraction

This method creates new features by transforming the original features, often combining them to capture the most important information.

- **Principal Component Analysis (PCA):** Finds new axes (principal components) that capture the greatest variance in the data.
- **Autoencoders:** Neural networks that learn to compress and reconstruct data, extracting meaningful features.
- **Other Methods:** FastMap, Random Projections, and Multi-Dimensional Scaling (MDS).


### 5. 📊 Principal Component Analysis (PCA): A Key Feature Extraction Method

#### What is PCA?

PCA is a technique that finds the directions (called principal components) along which the data varies the most. By projecting data onto these directions, we reduce dimensionality while preserving as much variance as possible.

#### How PCA Works (Intuition)

- Imagine a cloud of points in space. PCA finds the line (or plane, or hyperplane) that best fits the data by capturing the largest spread (variance).
- The first principal component is the direction with the greatest variance.
- The second principal component is orthogonal (at right angles) to the first and captures the next highest variance, and so on.

#### Mathematical Steps in PCA

1. **Center the Data:** Subtract the mean from each feature so the data is centered at the origin.
2. **Compute Covariance Matrix:** This matrix shows how features vary together.
3. **Find Eigenvectors and Eigenvalues:** Eigenvectors define the new axes (principal components), and eigenvalues measure the variance along these axes.
4. **Sort Components:** Order the principal components by their eigenvalues from largest to smallest.
5. **Project Data:** Transform the original data onto the top p principal components to reduce dimensionality.

#### Advantages and Disadvantages of PCA

- **Advantages:**
  - Optimal linear dimensionality reduction in terms of variance preservation.
  - Can be applied to any multidimensional dataset, not just Gaussian.
- **Disadvantages:**
  - Computationally expensive for very large datasets (though can be improved with random sampling).
  - Sensitive to outliers and nonlinear relationships.

#### PCA Interpretations

- PCA can be seen as finding an affine transformation that minimizes reconstruction error (the difference between original and projected data).
- Alternatively, it maximizes the variance captured by the projections.
- The first principal component minimizes the mean squared error (MSE) of reconstruction or maximizes variance.

#### Choosing the Number of Components

- You select the number of principal components based on the eigenvalues.
- Components with small eigenvalues contribute little variance and can be discarded with minimal information loss.
- This reduces the data from n dimensions to p dimensions (p < n).


### 6. 🔄 Other Feature Extraction Methods: Multi-Dimensional Scaling (MDS)

MDS is a technique that tries to place data points in a low-dimensional space such that the distances between points are preserved as well as possible.

- It minimizes a quantity called **stress**, which measures how well the low-dimensional distances match the original distances.
- MDS uses iterative optimization (like steepest descent) to adjust point positions.
- However, MDS can be computationally expensive, especially for large datasets (O(N²) time complexity).


### Summary

Dimensionality reduction is a crucial step in handling high-dimensional data. It helps overcome the curse of dimensionality by finding a smaller, meaningful representation of the data. This makes data easier to visualize, interpret, and model, while improving computational efficiency and potentially enhancing model performance.

Two main approaches are:

- **Feature Selection:** Choosing a subset of original features.
- **Feature Extraction:** Creating new features that summarize the original data.

Among feature extraction methods, **PCA** is a foundational technique that finds directions of maximum variance to reduce dimensionality optimally in a linear sense.

Understanding these concepts and methods equips you to handle complex, high-dimensional datasets effectively.