# python program to find the armstrong number 
        
# method 2
print("\nArmstrong numbers from 1 to 10000 in an interval")
def is_armstrong(num):
    """Check if a number is an Armstrong number."""
    num_digits = len(str(num))  
    sum_of_powers = sum(int(digit) ** num_digits for digit in str(num))
    return sum_of_powers == num 

for num in range(1, 10000 + 1):
    if is_armstrong(num):  
        print(num, end=" ")

# method 3
armstrong_numbers = [num for num in range(1, 10000 + 1) if is_armstrong(num)]
print("\n"), print(armstrong_numbers)

# Method 1  
def is_armstrong(num):
    sum = 0
    temp = num
    num_digit = len(str(num))
    while temp > 0:
        digits = temp % 10
        sum = sum + digits ** num_digit
        temp = temp // 10
    return sum == num

for num in range(1, 10000):
    if is_armstrong(num):
        print(num, end = " ")

# Method 4        
while True:
    try:    
        num_put = input("\nEnter the number or 'exit' -> ")
        if num_put.lower() == "exit":
            break

        num = int(num_put)
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum = sum + digit ** 3
            temp = temp // 10

        if num == sum:
            print(num, "is a armstrong number")
        else:
            print(num, "is not a armstrong number")
 
    except ValueError:
        print("Invalid Input")

