# a] Vector - matrix multiplication

import numpy as np
x = np.array([1, 2, 3])
y = np.array([[4, 5],[6, 7],[8, 9]])
print("Matrix : \n", y)
print("Vector : ", x)
print("The vector - matrix multiple is ", np.dot(x, y), "\n")

# b] Matrix - Matrix multiplication

x = np.array([[1, 2],[3, 4]])
y = np.array([[1, 2],[3, 4]])
print("1st matrix : \n", x, "\n 2nd matrix : \n", y)
print("The matrix - matrix multiplication is \n", np.dot(x, y))


