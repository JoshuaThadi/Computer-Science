'''

Given a square matrix, 
calculate the absolute difference between the sums of its diagonals.

'''

def diagonal_difference(array):
    n = len(array)
    topleft_to_bottomright_diagonal = 0
    bottomright_to_topleft_diagonal = 0

    for i in range(n):
        topleft_to_bottomright_diagonal = topleft_to_bottomright_diagonal + array[i][i]
        bottomright_to_topleft_diagonal = bottomright_to_topleft_diagonal + array[i][n - 1 - i]

    sum_of_diagonals = topleft_to_bottomright_diagonal + bottomright_to_topleft_diagonal
    if sum_of_diagonals < 0:
        sum_of_diagonals = -sum_of_diagonals

    return sum_of_diagonals

if __name__ == '__main__':
    n = int(input().strip())
    array = []

    for _ in range(n):
        array.append(list(map(int, input().rstrip().split())))

    result = diagonal_difference(array)
    print(result)
