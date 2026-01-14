# python program to print fibonacci series
print("Fibonacci Series of number 10")

# Method 1 (using recursive method)
def fibonacciSeries(i):
    if i <= 1:
        return i
    else:
        return (fibonacciSeries(i - 1) + fibonacciSeries(i - 2))

num = 10 
if num <= 0: 
    print("\nPrint enter a positive number ")
else:
    print("\nFibonacci Series(m1) : ", end=" ")
    for i in range(num):
        print(fibonacciSeries(i), end=" ")

# method 2 (using simple iteration)
num = 10
n1, n2 = 0, 1
print("\nFibonacci Series(m2) : ", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2 
    n1 = n2 
    n2 = n3 
    print(n3, end = " ")

print()

# Method 3
while True:
    try:
        fib_put = input("\nHow many terms ? ")
        if fib_put.lower() == "exit":
            break

        # first 2 terms  
        nterms = int(fib_put)
        n1, n2 = 0, 1
        count = 0

        # check if the number of terms is valid
        if nterms <= 0:
            print("\nPlease enter a positive number ")

        # if there is only one term, return n1 
        elif nterms == 1:
            print("\nFibonacci series upto", nterms, ":")
            print(n1)

        # generate fibonacci series 
        print("Fibonacci Sequence : ")
        while count < nterms:
            print(n1, end = " ")
            nth = n1 + n2 
            # update values 
            n1 = n2 
            n2 = nth 
            count = count + 1

    except ValueError:
        print("Invalid Input")


