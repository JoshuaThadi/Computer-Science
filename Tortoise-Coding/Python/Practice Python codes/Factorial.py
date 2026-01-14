# python program to print factorial of a number

while True:
    try:
        num_put = input("Enter a number or 'exit' -> ")
        if num_put.lower() == "exit":
            break
        num = int(num_put)
        factorial = 1
        if num < 0:
            print("Factorial does not exists for negative number")
        elif num == 0:
            print("Factorial for 0 is 1")
        else:
            for i in range(1, num):
                factorial = factorial * i
            print(f"Factorial of {num} is {factorial}")
    except ValueError:
        print("Invalid Input, only enter numbers")

