# WAP to enter a matrix and check if it is invertable if inverse exists find inverse of it

import numpy as np

# WAP to enter a matrix and check if it is invertible, and if so, find the inverse.
r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))

if r != c:
    print("Matrix must be square to be invertible")
else:
    print("Enter the matrix elements row-wise: ")
    matrix = np.array([list(map(float, input().split())) for i in range(r)])  # Corrected parentheses
    det = np.linalg.det(matrix)
    if det == 0:
        print("The matrix is not invertible (determinant is zero)")
    else:
        inverse_matrix = np.linalg.inv(matrix)  # 
        print("The matrix is invertible")
        print("Inverse of the matrix:")
        print(inverse_matrix)
