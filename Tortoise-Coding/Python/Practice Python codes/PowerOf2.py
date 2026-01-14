# Python program to display power of 2 using Anonymous Function

while True:
    try:
        input_2 = input("Enter the terms -> ")
        if input_2.lower() == "exit":
            break

        terms = int(input_2)
        result = list(map(lambda x : 2 ** x, range(terms)))
        print("Total terms are ", terms)
        for i in range(terms):
            print("2 to the power ", i, "is", result[i])

    except ValueError:
        print("Invalid Input")

