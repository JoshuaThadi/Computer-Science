# Python program to find the natural numbers

while True:
    try:
        input_num = input("Enter a number -> ")
        if input_num.lower() == "exit":
            break
        
        num = int(input_num)
        if num < 0:
            print("Enter a positive number!")
        else:
            sum = 0
            while (num > 0):
                sum = sum + num
                num = num - 1
            print("The sum is ", sum)
    except ValueError:
        print("Invalid input!")

