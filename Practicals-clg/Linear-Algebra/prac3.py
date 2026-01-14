# a] Enter an r x n matrix

r = int(input("Enter the no.of rows : "))
c = int(input("Enter the no.of columns : "))

matrix = []
print("Enter the matrix elements row-wise : ")

for i in range(r):
    row = [int(x) for x in input().split()]
    matrix.append(row)
print("Matrix : ")
for row in matrix:
    print(row, "\n")

# b] Display a matrix row and column

import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrix : \n", a, "\n")
print("1st row of matrix:", a[0, :])
print("2nd row of matrix:", a[1, :])
print("3rd row of matrix:", a[2, :])
print("1st column of matrix:", a[:, 0])
print("2nd column of matrix:", a[:, 1])
print("3rd column of matrix:", a[:, 2], "\n")

# c] Scalar Multiplication of matrix

import numpy as np
a = 5
m = np.array([[1, 2], [3, 4]])
print("Matrix \n", m)
b = a * m
print("\n Scalar Multiplication of matrix is \n", b, "\n")

# d] Transpace of a Matrix

import numpy as np
a = np.array([[12, 4],[4, 5],[3, 8]])
print("Matrix is \n", a)
print("\nTransposed matrix is \n", a.transpose())

