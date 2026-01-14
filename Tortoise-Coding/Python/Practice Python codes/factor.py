''' python program to find the factor of a number '''

# this function computes the factor of the argument passed
def print_factors(x):
    print(f"The factor of {x} are -> ")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)

num = 320
print(print_factors(num))
