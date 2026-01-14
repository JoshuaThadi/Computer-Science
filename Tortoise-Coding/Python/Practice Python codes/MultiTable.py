# Python program to print multiplication table

while True:
    try:
        num_table = input("Enter a number or 'exit' -> ")
        if num_table.lower() == "exit":
            break

        num = int(num_table)
        for i in range(1, 10 + 1):
            print(f"{num} x {i} = {num * i}")

    except ValueError:
        print("Invalid Input")

