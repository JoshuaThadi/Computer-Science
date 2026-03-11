# Practical No: 06 - Principal Component
# Analysis (PCA)
# Aim: erform PCA on a dataset to reduce
# dimensionality. Evaluate the explained
# variance and select the appropriate number
# of principal components. Visualize the data
# in the reduced-dimensional space.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler 

data = load_iris()
X = data.data
y = data.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA()
X_pca = pca.fit_transform(X_scaled)

explained_variance = pca.explained_variance_ratio_
cumulative_variance = np.cumsum(explained_variance)

plt.figure(figsize=(6, 4))
plt.plot(range(1, len(explained_variance) + 1), cumulative_variance, marker='o', linestyle="--")

plt.xlabel('Number of Principal Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('Explained Variance vs. Number of Components')
plt.grid(True)
plt.show()

pca_2d = PCA(n_components=2)
X_pca_2d = pca_2d.fit_transform(X_scaled)

plt.figure(figsize=(6, 4))
plt.scatter(X_pca_2d[:, 0], X_pca_2d[:, 1], c = y, cmap='viridis', edgecolor='k')
plt.xlabel('Principal Components 1')
plt.ylabel('Principal Component 2')
plt.title('PCA: 2D Projection of Data')
plt.colorbar(label='Class Label')
plt.grid(True)
plt.show()