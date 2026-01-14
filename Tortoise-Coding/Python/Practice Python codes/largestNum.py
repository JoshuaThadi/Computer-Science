# python program to find the largest number 

while True:
    try:
        number_a = input("Enter the 1st number | type exit to quit: ")
        if number_a.lower() == "exit":
            break
        num_a = int(number_a)

        number_b = input("Enter the 2st number | type exit to quit: ")
        if number_b.lower() == "exit":
            break
        num_b = int(number_b)

        if (num_a > num_b ):
            print("Number {0} is greater than {1}".format(num_a, num_b))
        elif (num_a == num_b):
            print("Number {0} is equal to {1}".format(num_a, num_b))
        else:
            print("Number {0} is greater than {1}".format(num_b, num_a))
    except ValueError:
        print("Invalid Input")

