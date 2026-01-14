# WAP to convert a matrix into echelon form

# Function to convert a matrix to row echelon form
def row_echelon(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    for i in range(min(rows, cols)):
        # Find the pivot (make sure the leading coefficient is not zero)
        if matrix[i][i] != 0:
            divisor = matrix[i][i]
            # Normalize the row by dividing it by the pivot element
            for j in range(i, cols):
                matrix[i][j] /= divisor
            
            # Eliminate entries below the pivot in the current column
            for k in range(i + 1, rows):
                factor = matrix[k][i]
                for j in range(i, cols):
                    matrix[k][j] -= factor * matrix[i][j]
    
    return matrix

# Example matrix
A = [[2, 1, -1, -3],
     [4, 5, -3, -7],
     [2, 6, -1, 6]]

# Convert to row echelon form
ref_matrix = row_echelon(A)

# Print the row echelon form
for row in ref_matrix:
    print(row)
