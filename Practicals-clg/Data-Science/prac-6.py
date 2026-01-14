# Practical No: 06 - Principal Component Analysis (PCA)
# Aim: Perform PCA on a dataset to reduce dimensionality,
# evaluate explained variance, and visualize in reduced-dimensional space.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# Step 1: Load dataset (Iris dataset)
data = load_iris()
X = data.data  # Features
y = data.target  # Labels

# Step 2: Standardize the data (important for PCA)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Perform PCA
pca = PCA()
X_pca = pca.fit_transform(X_scaled)

# Step 4: Evaluate explained variance
explained_variance = pca.explained_variance_ratio_
cumulative_variance = np.cumsum(explained_variance)

# Step 5: Plot cumulative explained variance
plt.figure(figsize=(6, 4))
plt.plot(range(1, len(explained_variance) + 1), cumulative_variance, marker='o', linestyle='--')
plt.xlabel('Number of Principal Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('Explained Variance vs. Number of Components')
plt.xticks(range(1, len(explained_variance) + 1))
plt.grid(True)
plt.show()

# Step 6: Choose first two principal components for visualization
pca_2d = PCA(n_components=2)
X_pca_2d = pca_2d.fit_transform(X_scaled)

# Scatter plot of the first two principal components
plt.figure(figsize=(6, 4))
plt.scatter(X_pca_2d[:, 0], X_pca_2d[:, 1], c=y, cmap='viridis', edgecolor='k')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA: 2D Projection of Data')
plt.colorbar(label='Class Label')
plt.grid(True)
plt.show()
