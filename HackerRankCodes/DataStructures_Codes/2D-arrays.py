'''

There are 16 hourglasses in a 6 X 6 array. The hourglass sum is the sum of the values in an hourglass.
Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum.

'''

# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.

def hourglass_sum(array):
    max_sum = -63

    for i in range(4):
        for j in range(4):
            top = array[i][j] + array[i][j + 1] + array[i][j + 2]
            middle = array[i + 1][j + 1]
            bottom = array[i + 2][j] + array[i + 2][j + 1] + array[i + 2][j + 2]

            current_sum = top + middle + bottom
            max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == '__main__':
    array = []
    print("Enter the 6x6 matrix (each row separated by space):")
    for _ in range(6):
        array.append(list(map(int, input().split())))

    result = hourglass_sum(array)
    print(f"Maximum hourglass sum: {result}")


