'''

An array is a data structure that stores elements of the same type in a contiguous block of memory.
Your task is to reverse an array of integers.

'''

# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.

def reverse_array(array):
    return array[::-1]

if __name__ == '__main__':
    array = list(map(int, input(f"Enter the array : ").rstrip().split()))
    res = reverse_array(array)
    print(f"Reversed array : {res}")
