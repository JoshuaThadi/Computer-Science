# python program to find the L.C.M of two input number

def compute_lcm(x, y):

    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y 

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater 
            break
        greater = greater + 1

    return lcm 

number1 = 54; number2 = 24
print(f"The L.C.M is {compute_lcm(number1, number2)}")

'''
This program stores two number in num1 and num2 respectively. 
These numbers are passed to the compute_lcm() function. The function returns the L.C.M of two numbers.
In the function, we first determine the greater of the two numbers since the L.C.M. can only be greater than or equal to the largest number.
We then use an infinite while loop to go from that number and beyond.
In each iteration, we check if both the numbers perfectly divide our number. 
If so, we store the number as L.C.M. and break from the loop. Otherwise, the number is incremented by 1 and the loop continues.
The above program is slower to run.We can make it more efficient by using the fact 
that the product of two numbers is equal to the product of the least common multiple and greatest common divisor of those two numbers.
'''

# python program to find largest common multiple of two number using GCD (greatest common divisor)

def compute_gcd(num1, num2):
    while(num2):
        num1, num2 = num2, num1 % num2;
        return num1 

# this function computes LCM 

def compute_lcm(num1, num2):
    lcm = (num1 * num2)//compute_gcd(num1, num2)
    return lcm 

number_1 = 54; number_2 = 24 
print(f"The L.C.M is {compute_lcm(number_1, number_2)}")

