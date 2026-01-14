'''
Design a program for creating a machine which count number of 1's and 0's in a given string
'''

num = input("Enter a binary number -> ")
count = [0, 0]

for i in num:
    if i == "0":
        count[0] = count[0] + 1
    elif i == "1":
        count[1] = count[1] + 1
    else:
        print("Invalid Number")
print(f"count of 0's = {count[0]}, Count of 1's = {count[1]}")
