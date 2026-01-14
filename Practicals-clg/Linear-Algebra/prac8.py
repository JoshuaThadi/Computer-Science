# WAP  to enter a given matrix and an eigen values of the same and also find eigen vector

import numpy as np
A = np.array([[-2, 1],[2, -3]])
print("Eigen values of A are ",np.linalg.eigvals(A))
eigenValues, eigenVectors = np.linalg.eig(A)
print("First set of eigen values ", eigenValues)
print("Second set of eigen vector ", eigenVectors)
