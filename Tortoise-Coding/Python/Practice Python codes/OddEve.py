# program to check if the number is odd or even

while True:
    try:
        user_input = input("Enter a number (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break

        num = int(user_input)
        if num % 2 == 0:
            print("The number {0} is even".format(num))
        else:
            print("The number {0} is odd".format(num))
    except ValueError:
        print("Invalid input. Please enter a valid number or type 'exit' to quit.")

