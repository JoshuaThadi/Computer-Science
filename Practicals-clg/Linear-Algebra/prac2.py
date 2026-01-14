# a] Diplaying two matrices

import numpy as np
a = np.array([[1, 2],[-3, 4]])
print("First matrix is : \n", a)
b = np.array([[1, 2, 3],[-4, -5, 6],[7, 8, 9]])
print("Second matrix is : \n", b)


# b] Retrieving rows from two elements

a = np.array([[1, 2, 3],[11, 12, 13],[12, 23, 34]])
print("Matrix : \n", a, "\n")
print("1st row of the matrix :", a[0, :])
print("2nd row of the matrix :", a[1, :])
print("3rd row of the matrix :", a[2, :])

# c] Retrieving columns of a matrix

a = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print("1st row of the matrix :", a[:, 0])
print("2nd row of the matrix :", a[:, 1])
print("3rd row of the matrix :", a[:, 2])
